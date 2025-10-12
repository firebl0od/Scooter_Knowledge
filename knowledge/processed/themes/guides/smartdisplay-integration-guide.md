# SmartDisplay Integration & Operations Guide

## TL;DR
- SmartDisplay pairs with VESC and legacy controllers over UART today and will gain native CAN + VESC Express support on the incoming hardware spin, so budget both 5 V logic power and CAN high/low when future-proofing harnesses.[^1]
- Treat the display as the hub for lighting, telemetry, and speed-mode governance: its OTA chain flashes every connected accessory board (5 V/12 V light drivers, button pods) alongside the head unit, simplifying updates if the CAN bus is wired correctly.[^2]
- Never tether SmartDisplay’s USB port to a computer while the controller is live; a single ground loop already blew the 3.3 V rail and STM32 on a Ubox, forcing an RMA.[^3]

---

## Hardware Snapshot & Compatibility Matrix
| Revision | Host Link | Required Leads | Notable Peripherals |
| --- | --- | --- | --- |
| 2022–mid 2024 batches | UART (RX/TX/GND/5 V) | 4-wire JST or soldered pigtail | External button harness, optional light board |
| Upcoming hardware (2024Q4 roadmap) | CAN + UART bridge | CANH/CANL, 12 V lighting feed, 5 V aux | Native VESC Express slot, ESP32‑C3 module, CAN daisy-chain[^1] |

- Early adopters validated SmartDisplay on dual Kelly, VESC, and Minimotors controllers; firmware exposes ≈95 % of editable parameters on-device and defers long strings (Wi‑Fi SSID) to the mobile apps.[^4]
- The Voyage/TJA1051 CAN transceiver is the go-to spare for Voyage/SmartDisplay repair benches; stock a few for field swaps.[^5]

## Wiring & Installation Checklist
1. **Bench-Test Power Rails.** Confirm 5 V and 3.3 V logic rails on the controller before introducing SmartDisplay to avoid misdiagnosing brownouts.[^6]
2. **Route Lighting Bus.** The companion light board feeds both 5 V and 12 V lighting branches and reports controller faults back through SmartDisplay, so land CAN and the accessory power leads in the same session.[^2]
3. **Program OTA Chain.** Firmware updates publish to a web server; once the display flashes over Wi‑Fi, it cascades the new build to every detected expansion board via CAN.[^2][^7]
4. **Map Hotkeys & External Buttons.** Internal buttons can act as hotkeys, but external latching or momentary switches are supported for mode toggles and lighting; riders often park lighting on the auxiliary harness instead of the face buttons.[^7]
5. **Speed Modes via ADC2.** Tie ADC2 “eco” limits to SmartDisplay’s virtual throttle ceilings when mixing with ADC-based throttles—the display writes percentage caps that VESC enforces as duty/phase ceilings.[^7]

## Feature Set & Navigation
- **Integrated GPS + Nav Prompts.** The 3.5 in unit houses turn-by-turn guidance to keep phones off the bars; builders cite 10 × 6.5 cm packaging as a sweet spot for 100 km/h scooters.[^8]
- **Waze Overlay.** Beta firmware already overlays Waze police alerts directly on the dashboard, foreshadowing richer third-party integrations once CAN message catalogs stabilize.[^9]
- **Telemetry Dashboards.** Race teams log throttle position, per-motor phase amps, traction-control response, and segment comparisons from SmartDisplay sessions—handy for coaching and driver swaps.[^10]
- **Lighting + Error Telemetry.** Kelly and VESC users receive controller error feedback (screenshots, codes) on SmartDisplay, easing remote debugging.[^2]

## Pricing, Bundling & Availability Signals
- Beta batches sold at **300 €** for 15 testers with August assembly runs; production pricing remains under review.[^11]
- Rage Mechanics currently bundles SmartDisplay with its dual-controller kits (~489 €), and standalone sales are pending cost-down work—plan purchases early if you need just the dash.[^12]
- Competing IPS dashboards (e.g., Voyage Megan) target 300–400 € but lack SmartDisplay’s lighting bus, telemetry depth, and OTA ecosystem, so many riders still default to SmartDisplay.[^13]
- Low-volume CNC and SLS case work keeps retail expectations above €300 until injection tooling arrives, and the team is preparing regional distributors plus “panic mode” legal presets alongside wider controller harness support.[^14]

## Telemetry Interpretation Notes
- SmartDisplay power numbers trend ~6–7 kW below VESC RT Tool because it calculates from CAN-reported battery amps × voltage without VESC’s instantaneous filtering; align on one source before publishing specs.[^10]
- Phase-current overlays highlight traction-control activity (e.g., 189 A front vs. 317 A rear mid-corner) and help tune duty-cycle ramps after firmware changes.[^10]

## Safety, Service & Troubleshooting
- **USB Isolation.** Only flash or debug SmartDisplay over Wi‑Fi/BLE when the controller is energized; USB-to-PC tests while the scooter is live can short grounds and nuke 3.3 V logic.[^3]
- **CAN Health.** Expect ≈3.3 V differential between CANH and CANL on a healthy bus; anomalous readings justify probing harness crimps before blaming firmware.[^6]
- **Spare Components.** Keep TJA1051 CAN ICs, JST pigtails, and spare ESP32 modules in the pit box to minimize downtime when a dash takes a spill.[^5]

## Roadmap & Ecosystem Outlook
- SmartDisplay’s apps push updates in minutes—developers can add a new setting, publish OTA, and have riders flashing within five minutes over Wi‑Fi.[^4]
- NetworkDir’s next hardware rev will speak native CAN, mimic Trampa’s SmartDisplay device registration, and bundle ESP32‑C3 Wi‑Fi/BLE modules to host VESC Express dashboards without extra dongles.[^1]
- Rage Mechanics is weaving the display into turnkey race scooters, streaming telemetry to crews and elevating expectations for pro-grade HUDs in the VESC scene.[^12]
- Firmware planning now includes encrypted OTA packages, Kelly/Sabvoton harness kits, and configurable “panic mode” speed caps so riders can stay compliant during roadside checks.[^14]

---

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
[^14]: Encrypted OTA releases, €300+ price expectations, distributor planning, and SmartDisplay “panic mode” presets outlined during beta updates.【F:knowledge/notes/input_part001_review.md†L598-L606】【F:knowledge/notes/input_part001_review.md†L668-L670】【F:knowledge/notes/input_part001_review.md†L858-L859】
