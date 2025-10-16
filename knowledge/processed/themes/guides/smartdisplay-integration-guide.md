# SmartDisplay Integration & Operations Guide

## TL;DR
- SmartDisplay now ships with modular harnesses that bridge VESC Tool, Minimotors, Kelly, Zero, and VSETT controllers while logging GPS, RTC, and media controls, so plan UART + CAN runs even if you start with legacy hardware.【F:knowledge/notes/input_part004_review.md†L103-L120】
- Current production firmware bundles Kelly KLS profiles and police-mode button combos, with Sabvoton and BAC support queued once hardware output stabilises; OTA updates arrive over HTTPS with encrypted images to deter cloning.【F:data/vesc_help_group/text_slices/input_part001.txt†L10887-L11025】
- SmartDisplay pairs with VESC and legacy controllers over UART today and will gain native CAN + VESC Express support on the incoming hardware spin, so budget both 5 V logic power and CAN high/low when future-proofing harnesses.[^1]
- The latest CNC aluminium housing ships with anti-glare glass, RTC, navigation, music controls, and dual buttons that already support single/double-click mapping; encoder knobs are planned for the production wave later this year.[^cnc-case]
- Treat the display as the hub for lighting, telemetry, and speed-mode governance: its OTA chain flashes every connected accessory board (5 V/12 V light drivers, button pods) alongside the head unit, simplifying updates if the CAN bus is wired correctly.[^2]
- Never tether SmartDisplay’s USB port to a computer while the controller is live; a single ground loop already blew the 3.3 V rail and STM32 on a Ubox, forcing an RMA.[^3]
- Enable the “transparent” BLE bridge when controllers lack onboard Bluetooth—the SmartDisplay can proxy VESC Tool traffic like a USB dongle, but veterans still default to wired sessions if nearby trackers or radios inject interference.[^15]

---

## Hardware Snapshot & Compatibility Matrix
| Revision | Host Link | Required Leads | Notable Peripherals |
| --- | --- | --- | --- |
| 2022–mid 2024 batches | UART (RX/TX/GND/5 V) | 4-wire JST or soldered pigtail | External button harness, optional light board |
| Upcoming hardware (2024Q4 roadmap) | CAN + UART bridge | CANH/CANL, 12 V lighting feed, 5 V aux | Native VESC Express slot, ESP32‑C3 module, CAN daisy-chain[^1] |
| Maker batches (2024) | UART + BLE pass-through | 4-wire JST, optional USB-C | Dash or deck module, transparent BLE bridge, SmartController companion board[^15][^18] |

- Early adopters validated SmartDisplay on dual Kelly, VESC, and Minimotors controllers; firmware exposes ≈95 % of editable parameters on-device and defers long strings (Wi‑Fi SSID) to the mobile apps.[^4]
- The Voyage/TJA1051 CAN transceiver is the go-to spare for Voyage/SmartDisplay repair benches; stock a few for field swaps.[^5]
- Rage Mechanics’ latest C350 controller kits now bundle SmartDisplay, thicker IMS plates, and ESP32-based BLE/IMU telemetry with an onboard 12 V 3 A rail—harnesses remain DIY extras for now, so budget fabrication time.【F:knowledge/notes/input_part004_review.md†L339-L339】
- Builders priced a €17 ESP32 touch display that ships with ready-to-flash Arduino code, letting teams print a housing and add Wi‑Fi/Bluetooth telemetry without buying premium dashboards; community members even offer remote flashing help and printable cases for the €20 Turkish variant if you need a turnkey budget dash.【F:data/vesc_help_group/text_slices/input_part009.txt†L9655-L9659】【F:data/vesc_help_group/text_slices/input_part009.txt†L10775-L10783】【F:data/vesc_help_group/text_slices/input_part009.txt†L10789-L10793】【F:data/vesc_help_group/text_slices/input_part009.txt†L12468-L12480】

## Companion Boards & OEM Dash Retention
- **QS-S4 stealth swaps.** Vsett’s QS-S4 display and RFID pod speak UART like Zero dashboards, letting SmartDisplay integrations reuse the factory harness for stealth compliance checks once you dig the loom out of the foam and silicone potting.【F:data/vesc_help_group/text_slices/input_part000.txt†L20364-L20389】
- **SmartController dev board.** Koxx’s €60 SmartController motherboard + shield keeps the OEM display for riders comfortable with coding and SMD work; the open-source build currently drives a single VESC with dual-motor support reserved for the paid “pro” release.【F:data/vesc_help_group/text_slices/input_part000.txt†L22102-L22133】
- **Button and harness expectations.** The SmartController expects momentary buttons and custom cabling, so builders plan to reuse dual-button pods while letting the board orchestrate speed-mode UART commands across both controllers to keep rear hubs from overheating.【F:data/vesc_help_group/text_slices/input_part000.txt†L22115-L22144】

## Wiring & Installation Checklist
1. **Bench-Test Power Rails.** Confirm 5 V and 3.3 V logic rails on the controller before introducing SmartDisplay to avoid misdiagnosing brownouts.[^6]
2. **Route Lighting Bus.** The companion light board feeds both 5 V and 12 V lighting branches and reports controller faults back through SmartDisplay, so land CAN and the accessory power leads in the same session.[^2]
3. **Budget CAN power for add-ons.** The SmartRepair harness can back-feed 5 V lighting from the CAN header—drop an inline resistor and remember the servo header’s PWM pads if you want blinkers instead of always-on lamps.[^can-backfeed]
3. **Program OTA Chain.** Firmware updates publish to a web server; once the display flashes over Wi‑Fi, it cascades the new build to every detected expansion board via CAN.[^2][^7]
4. **Choose controller roles intentionally.** Race teams sometimes assign the rear controller as the slave so SmartDisplay keeps the features they want (traction control, telemetry overlays) while the front stays the master—validate the pairing before track days.【F:knowledge/notes/input_part006_review.md†L86-L86】
4. **Map Hotkeys & External Buttons.** Internal buttons can act as hotkeys, but external latching or momentary switches are supported for mode toggles and lighting; riders often park lighting on the auxiliary harness instead of the face buttons.[^7]
5. **Speed Modes via ADC2.** Tie ADC2 “eco” limits to SmartDisplay’s virtual throttle ceilings when mixing with ADC-based throttles—the display writes percentage caps that VESC enforces as duty/phase ceilings.[^7]
6. **Log UART throttle packets before rewiring.** SmartDisplay streams CRC-protected commands over UART, so capture the live data to confirm dips originate upstream before blaming harness noise or shielding.[^uart-crc]
7. **Finish the enclosure.** The shared 3.5 in STL pack suits SLS/SLA printing, and builders now sand, paint, or resin-coat the housing to prevent translucent shells from yellowing under UV before bolting stem-cap mounts in place.[^16]
- **Grab the right dashboard firmware.** Xiaomi M365 owners running VESC 6.05 hardware rely on the `6_05_adc` community branch to fix braking/current bugs—GitHub mirrors can lag a few minutes, so re-download if the patch fails on first flash.【F:knowledge/notes/input_part006_review.md†L148-L148】

## Feature Set & Navigation
- **Integrated GPS + Nav Prompts.** The 3.5 in unit houses turn-by-turn guidance to keep phones off the bars; builders cite 10 × 6.5 cm packaging as a sweet spot for 100 km/h scooters.[^8]
- **Waze Overlay.** Beta firmware already overlays Waze police alerts directly on the dashboard, foreshadowing richer third-party integrations once CAN message catalogs stabilize.[^9]
- **Active dev logs map the roadmap.** Weekly SmartDisplay diaries document layout experiments, overlay prototypes, and the Waze alert workflow so installers can reproduce CAN dashboards without waiting on formal docs.【F:data/vesc_help_group/text_slices/input_part003.txt†L11850-L11955】【F:data/vesc_help_group/text_slices/input_part003.txt†L26600-L26606】
- **Production gearing up.** Koxx shared assembly photos and UI previews while Rage Mechanics prepared commercial support, signalling that plug-in TFT units with temperature alarms and custom icon packs are nearly ready for wider release.【F:data/vesc_help_group/text_slices/input_part003.txt†L11046-L11048】【F:data/vesc_help_group/text_slices/input_part003.txt†L11852-L11872】
- **Theme editor & live switching.** Rage Mechanics now ships a web-based theme designer that can push new skins over Wi‑Fi and swap layouts in real time on the scooter, making it easier to brand race fleets or share telemetry presets.【F:knowledge/notes/input_part010_review.md†L312-L314】
- **Telemetry Dashboards.** Race teams log throttle position, per-motor phase amps, traction-control response, and segment comparisons from SmartDisplay sessions—handy for coaching and driver swaps.[^10]
- **Sunton ESP32-8048S043 builds.** Denis Shelema’s DIY Sunton dash brings a 4.3″ 800×480 capacitive touchscreen with GPS logging, configurable gauges, Wi‑Fi firmware updates, handlebar button inputs, and onboard storage for odometer/settings once you finish the custom firmware and enclosure work.【F:data/vesc_help_group/text_slices/input_part009.txt†L12929-L12947】【F:data/vesc_help_group/text_slices/input_part009.txt†L13089-L13092】
- **Fast boot sequence.** Unlike Raspberry Pi-based dashboards that slog through a 45–95 s OS boot, SmartDisplay’s MCU firmware brings up telemetry in about 10 s once CAN current initializes.[^boot]
- **Lighting + Error Telemetry.** Kelly and VESC users receive controller error feedback (screenshots, codes) on SmartDisplay, easing remote debugging.[^2]
- **Wearable fallback.** Riders who skip a dash lean on the XMatic VESC Apple Watch app when they want telemetry without mounting extra hardware.【F:data/vesc_help_group/text_slices/input_part004.txt†L15297-L15302】

## Firmware & Profile Management
- SmartDisplay “profiles” live inside the phone app—switching Eco/Sport rewrites live controller configs, so riders keep UART bridges (e.g., basti30’s Arduino tool) handy when they want on-scooter buttons that push alternate maps without cycling power.[^profile_bridge]
- The single-channel Spintend ships without Bluetooth; SmartDisplay’s pass-through mode or an external module keeps VESC Tool access alive while the rugged one-wire bus handles remote IO where I²C runs fall over past ~15 cm.[^single_bt]

- Production retail is targeting **€400–€600** with a €199.99 early-adopter slot for the first ten units; budget above €300 until volume ramps even though beta testers paid €300.【F:knowledge/notes/input_part004_review.md†L129-L131】
- Rage Mechanics has logged 4,000+ development hours and keeps firmware closed-source while supporting Minimotors, VESC, Zero, VSETT, Kelly, and Kunteng buses—explaining the ~€500 price point despite open-hardware roots.【F:knowledge/notes/input_part004_review.md†L259-L259】
- Beta batches sold at **300 €** for 15 testers with August assembly runs; production pricing remains under review.[^11]
- Rage Mechanics currently bundles SmartDisplay with its dual-controller kits (~489 €), and standalone sales are pending cost-down work—plan purchases early if you need just the dash.[^12]
- Expect retail pricing closer to €500 once the premium feature set (CAN/UART breakout, telemetry, OTA, GPS, lighting control) is factored in—Face de Pin Sucé’s rundown helps set expectations for new buyers.【F:knowledge/notes/input_part010_review.md†L314-L314】
- Riders chasing budget instrumentation still repurpose RTV VESC-only displays or even spare phones when SmartDisplay pricing overshoots a project’s scope.【F:knowledge/notes/input_part010_review.md†L314-L315】
- Competing IPS dashboards (e.g., Voyage Megan) target 300–400 € but lack SmartDisplay’s lighting bus, telemetry depth, and OTA ecosystem, so many riders still default to SmartDisplay.[^13]
- Low-volume CNC and SLS case work keeps retail expectations above €300 until injection tooling arrives; the team is tooling distributors, planning a ~20-unit May build run with new central-mount housings, and baking “panic mode” legal presets alongside wider controller harness support.[^14]

## Telemetry Interpretation Notes
- SmartDisplay power numbers trend ~6–7 kW below VESC RT Tool because it calculates from CAN-reported battery amps × voltage without VESC’s instantaneous filtering; align on one source before publishing specs.[^10]
- Bench telemetry already logged 332 A / 21.4 kW peaks from a 20 S6 P Molicel 40T pack with heavy sag (~55 A per parallel), so capture per-parallel stress in your logs when validating high-power bursts.【F:data/vesc_help_group/text_slices/input_part003.txt†L21249-L21283】
- Phase-current overlays highlight traction-control activity (e.g., 189 A front vs. 317 A rear mid-corner) and help tune duty-cycle ramps after firmware changes.[^10]

## Safety, Service & Troubleshooting
- **Dash-only scripts drop security features.** Rage Mechanics’ “dash-only” SmartDisplay firmware frees wiring but loses start-speed locks, button combos, and motor lockouts when the dashboard powers down—recreate those safeties elsewhere before relying on the stripped harness.【F:knowledge/notes/input_part004_review.md†L193-L195】
- **Cruise control stays manual.** The team refuses to spoof cruise via Lisp—use the dedicated button on the remote or SmartDisplay’s onboard toggle rather than scripting ADC hacks that can run away.【F:knowledge/notes/input_part004_review.md†L342-L342】
- **USB Isolation.** Only flash or debug SmartDisplay over Wi‑Fi/BLE when the controller is energized; USB-to-PC tests while the scooter is live can short grounds and nuke 3.3 V logic.[^3]
- **CAN Health.** Expect ≈3.3 V differential between CANH and CANL on a healthy bus; anomalous readings justify probing harness crimps before blaming firmware.[^6]
- **Spare Components.** Keep TJA1051 CAN ICs, JST pigtails, and spare ESP32 modules in the pit box to minimize downtime when a dash takes a spill.[^5]
- **Dual-motor presets.** Early “police mode” experiments target CAN-synced loadouts that mute the front motor while leaving rear torque, so expect firmware drops that combine preset buttons with the BLE bridge once the prototypes stabilize.[^17]

## Roadmap & Ecosystem Outlook
- SmartDisplay’s apps push updates in minutes—developers can add a new setting, publish OTA, and have riders flashing within five minutes over Wi‑Fi.[^4]
- NetworkDir’s next hardware rev will speak native CAN, mimic Trampa’s SmartDisplay device registration, and bundle ESP32‑C3 Wi‑Fi/BLE modules to host VESC Express dashboards without extra dongles.[^1]
- Rage Mechanics is weaving the display into turnkey race scooters, streaming telemetry to crews and elevating expectations for pro-grade HUDs in the VESC scene.[^12]
- Public release cadence targets late 2024/early 2025 with broader controller support, pricing between €400 and €600, and bundle options that include light boards and button pods—set customer expectations accordingly.【F:data/vesc_help_group/text_slices/input_part004.txt†L11857-L11916】
- Firmware planning now includes encrypted OTA packages, Kelly/Sabvoton harness kits, and configurable “panic mode” speed caps so riders can stay compliant during roadside checks.[^14]
- Upcoming builds expand the existing 25/35/unlimited slots into user-tuned eco/normal/boost profiles that scale phase and battery current (e.g., eco at 0.6×/0.7×) and warn when MOSFET temps approach the boost gate.【F:knowledge/notes/input_part000_review.md†L137-L137】
- Production now spans dash-mounted screens and minimalist deck modules assembled by Koxx’s team, letting riders hide the BLE bridge in the deck when they prefer to keep phones on the bars for live telemetry.[^18]

---

## Source Notes
[^1]: Upcoming SmartDisplay hardware adds CAN connectivity, VESC Express support, and self-hosted ESP32‑C3 modules beyond the current RX/TX/GND/5 V requirement.【F:knowledge/notes/input_part010_review.md†L16-L18】
[^2]: Light-board OTA chain updating 5 V/12 V accessories and returning controller fault feedback through SmartDisplay.【F:knowledge/notes/input_part002_review.md†L843-L845】
[^3]: USB debugging while connected to a live VESC killed the Ubox 3.3 V rail and STM32—use wireless links instead.【F:knowledge/notes/input_part000_review.md†L262-L265】
[^4]: SmartDisplay exposes nearly all controller settings on-device, supports Kelly/VESC/Minimotors, and pushes OTA firmware via apps within minutes.【F:knowledge/notes/input_part002_review.md†L844-L845】
[^5]: Voyage/SmartDisplay CAN transceiver reference (TJA1051) shared for stocking spares.【F:knowledge/notes/input_part010_review.md†L17-L18】
[^6]: Verification of controller rails and CAN voltage expectations during SmartDisplay bring-up.【F:knowledge/notes/input_part011_review.md†L231-L233】
[^7]: External buttons, OTA flashing screens, and SmartDisplay speed-mode mapping via ADC2 percentage caps.【F:knowledge/notes/input_part002_review.md†L843-L845】
[^8]: SmartDisplay navigation mock-up dimensions (10 cm × 6.5 cm, 3.5 in screen) targeting 100 km/h builds to avoid phone mounts.【F:knowledge/notes/input_part003_review.md†L571-L573】
[^9]: Waze police-alert overlays already prototyped on SmartDisplay dashboards.【F:knowledge/notes/input_part003_review.md†L697-L699】
[^10]: Race telemetry logs comparing SmartDisplay and VESC RT data (power delta, per-motor phase amps, throttle tracing).【F:knowledge/notes/input_part005_review.md†L179-L183】
[^11]: Beta pricing (300 €) and limited 15-unit run with August assembly schedule.【F:knowledge/notes/input_part002_review.md†L845-L845】
[^12]: Rage Mechanics bundling SmartDisplay with dual-controller kits and teasing standalone availability once pricing stabilizes.【F:knowledge/notes/input_part013_review.md†L684-L684】
[^13]: Voyage Megan IPS display positioning at 300–400 € and community comparisons favoring SmartDisplay’s richer feature set.【F:knowledge/notes/input_part005_review.md†L378-L379】
[^megan_alt]: Arnau’s Voyage Megan bundle lacks out-of-box waterproofing and costs ~€400, so Smart Repair points budget builders toward mark99i’s Raspberry Pi dashboard as a configurable alternative.【F:knowledge/notes/input_part011_review.md†L560-L562】
[^14]: Encrypted OTA releases, €300+ price expectations, distributor planning, and SmartDisplay “panic mode” presets outlined during beta updates.【F:knowledge/notes/input_part001_review.md†L598-L606】【F:knowledge/notes/input_part001_review.md†L668-L670】【F:knowledge/notes/input_part001_review.md†L858-L859】
[^15]: SmartDisplay assembly photos and UI previews showing temperature alarms, custom icons, and Rage Mechanics’ commercial support prep ahead of mass release.【F:data/vesc_help_group/text_slices/input_part003.txt†L11046-L11048】【F:data/vesc_help_group/text_slices/input_part003.txt†L11852-L11872】
[^boot]: MCU firmware initializes dashboards in ≈10 s, avoiding the 45–95 s boot delays seen on Raspberry Pi VESC displays.【F:knowledge/notes/input_part004_review.md†L83-L83】
[^uart-crc]: SmartDisplay throttle traffic includes CRC checks—log the UART stream before chasing shielding fixes for perceived duty dips.【F:knowledge/notes/input_part004_review.md†L214-L215】
[^can-backfeed]: Smart Repair’s harness can power lights directly from the CAN header, but builders add inline resistors and tap the servo PWM pads when they want flashing indicators instead of constant-on lamps.【F:knowledge/notes/input_part012_review.md†L19323-L19405】
[^15]: SmartDisplay’s transparent BLE bridge lets Android VESC Tool sessions piggyback through the dash like a USB dongle, though the team still leans on wired hookups when local trackers cause interference.【F:knowledge/notes/input_part000_review.md†L201-L201】
[^16]: Community STL packs and resin-print finishing steps keep the 3.5 in enclosure centred on the stem while preventing UV yellowing.[^15][^smartdisplay-stl]
[^17]: CAN-linked presets such as “police mode” are being prototyped to mute the front motor while retaining rear torque for roadside compliance checks.【F:knowledge/notes/input_part000_review.md†L203-L203】
[^18]: Koxx now hand-assembles SmartDisplay and SmartController batches, selling both the dash-mounted unit and a display-less deck module for riders who prefer phone dashboards over BLE.【F:knowledge/notes/input_part000_review.md†L264-L264】
[^profile_bridge]: SmartDisplay profiles live on the phone; riders use UART bridges like basti30’s Arduino tool to push alternate maps without power-cycling the controller.【F:knowledge/notes/input_part000_review.md†L270-L271】
[^single_bt]: Spintend’s single-channel controller lacks onboard Bluetooth, so builders lean on SmartDisplay pass-through or external modules and reserve the one-wire bus for remote IO because I²C fails past ~15 cm.【F:knowledge/notes/input_part000_review.md†L299-L299】
[^smartdisplay-stl]: Shared 3.5 in SmartDisplay STL kits support SLA/SLS printing and stem-cap mounts; builders finish prints with opaque paint to avoid UV yellowing.【F:knowledge/notes/input_part000_review.md†L202-L202】【F:knowledge/notes/input_part000_review.md†L293-L293】

## Production Timeline & Pricing Updates
- **SmartDisplay nearing production with premium pricing.** Rage Mechanics' SmartDisplay now lives in a CNC aluminium, anti-glare housing with VESC Tool bridging, navigation, RTC timekeeping, and music controls; two buttons support single/double-click mapping today, with knob controls planned once production launches—early adopters expect €199.99 launch slots before the €400–600 retail range.[^smart_production]
- **Harnesses are modular and interchangeable.** Production units ship with interchangeable harnesses for VESC, Minimotors, Kelly, Zero, and Vsett pins, and the project is no longer open source despite earlier forks.[^smart_harness]

## Source Notes (continued)
[^smart_production]: SmartDisplay production timeline, hardware features, and pricing expectations.【F:knowledge/notes/input_part004_review.md†L21-L21】【F:knowledge/notes/input_part004_review.md†L52-L52】
[^smart_harness]: SmartDisplay modular harness system for various controller brands.【F:knowledge/notes/input_part004_review.md†L52-L52】【F:knowledge/notes/input_part004_review.md†L339-L339】
[^boot]: SmartDisplay boot time comparison vs. Raspberry Pi dashboards.【F:knowledge/notes/input_part004_review.md†L83-L83】
[^uart-crc]: SmartDisplay UART throttle troubleshooting and CRC-protected command stream.【F:knowledge/notes/input_part004_review.md†L608-L608】
