# VESC Accessory Power & Display Integration Checklist

## Purpose

This guide distills field reports on powering lights, horns, and dashboards from aftermarket VESC controllers so builders avoid overloading regulator rails or frying logic accessories during swaps. Recent X12 case studies underline how little headroom exists on their 5 V rails and why every accessory deserves its own buck converter.[^1]

## Quick Reference Matrix

| Controller family | Native accessory rails | Verified limits & caveats | Recommended mitigations |
| --- | --- | --- | --- |
| Tronic X12 | 5 V logic (≈150 mA) | Rail cannot sustain heavy peripherals such as displays or fans without brownouts.[^2] | Budget an external buck converter for any load above small sensors and throttle/gear switches.[^2] |
| Spintend Ubox 85×/24× | 5 V logic, 12 V rail (rated 3 A) | Field tests keep the onboard 12 V rail around 1.5 A.
  - enough for wireless switches or a limiter relay—remote receivers draw about 1.5 A on Spintend’s rail, so verify load before ditching a dedicated DC-DC converter[^spintend_relay_current]
  - while dual head/tail-light loads still overwhelm the regulator.[^3][^4][^spintend_remote] | Keep lighting minimalist or offload to a dedicated buck; fuse each branch so single shorts do not collapse the regulator.[^3] |
| Spintend X12 / upcoming 120 V | 5 V rail only (~150 mA) | The compact extrusion exposes just a weak 5 V output, so Express boards and lighting demand a separate buck or the ADC adapter plus DC/DC combo.[^5] | Pair the ADC board with an external step-down to feed 12 V lighting, and mount panel QS8 connectors to tidy high-current leads.[^6] |
| MakerBase 75×/85×/X12 bridge | 3.3 V ADC, 5 V UART/Comm | Hall throttles must stay near 3.3 V; 5 V injection into ADCs burns STM32 inputs, and older Xiaomi 5 V throttles still need resistor ladders whereas the 3.3 V variants can wire straight in.[^7][^8][^9] | Measure throttle min/max before connection; insert resistor ladders or shunt regulators if the lever exceeds 3.3 V.[^7] |
| MP2 open-source ESC | Open-frame 12 V DC/DC brick | Stable on 30 S packs but the stock transformer footprint is bulky, so builders are investigating custom windings to shrink the module for tighter decks.[^10] | Budget space for the brick or commission a smaller winding before finalizing enclosure CAD; keep a separate buck ready if you split accessory loads. |
| Spintend X12 / upcoming 120 V | 5 V rail only (~150 mA) | The compact 88 × 38 × 70 mm extrusion exposes just a weak 5 V output, so Express boards and lighting demand a separate buck or the ADC adapter plus DC/DC combo.[^5][^11] | Pair the ADC board with an external step-down to feed 12 V lighting, and mount panel QS8 connectors to tidy high-current leads.[^6] |
| MakerBase 75×/85×/X12 bridge | 3.3 V ADC, 5 V UART/Comm | Hall throttles must stay near 3.3 V; 5 V injection into ADCs burns STM32 inputs, and older Xiaomi 5 V throttles still need resistor ladders whereas the 3.3 V variants can wire straight in.[^7][^8][^12] | Measure throttle min/max before connection; insert resistor ladders or shunt regulators if the lever exceeds 3.3 V.[^7] |
| Any high-load build | External 12 V/20 A buck | Horns and compressors spike current; expect ≈4–6 A draw from a 60 V pack when heavily accessorised.[^13] | Adjust controller battery limits to preserve BMS overhead; isolate horns on separate fuses or relays.[^13] |

## Dash Replacement Notes

- Unbranded “generic JP” TFTs follow TF/TS100 button colour order; wire RX/TX/GND/5 V today and keep loom slack because NetworkDir’s next hardware spin will speak native CAN and host an ESP32‑C3 VESC Express module.[^jp-generic]
- Voyage’s “Megan” CAN dash remains the premium plug-and-play option when you need polished lighting integration without UART compromises.[^voyage-megan]
- RFP and Voyage are also fielding CAN-first displays that require firmware 6.05 plus custom Lisp on every controller; builders leaning Express kits get similar telemetry without rewiring UART looms.[^can-display-roadmap]

## Telemetry Accuracy & Power Auditing

- **Filter VESC Tool data.** Real-time power readouts are instantaneous duty×current estimates; without ≥100–300 ms filtering they overshoot logged pack power by 10 kW or more, so treat RT numbers as qualitative and lean on logged data for marketing claims.[^14]
- **Cross-check with smart BMS logs.** CAN-connected BMS telemetry remains the more reliable pack-current source because most VESCs only measure low-side shunts.
  - calibrate the BMS and even add DC-bus hall sensors when you need ±500 W accuracy around 35 kW builds.[^15]

## Power Sequencing & Harness Safety

1. **Use latching mains switches on VESC power leads.** Builders wire latching buttons in series with the main supply and leave momentary toggles for logic-only functions to ensure controllers truly power down when parked.[^16]
2. **Order matters on dual-rail harnesses.** Feeding 5 V into a Flipsky Smart Display before the 12 V lead repeatedly destroyed Spintend ADC daughterboards; always energise 12 V first, then 5 V, and confirm the display ground is shared with the controller.[^17]
3. **Spec brake-sensor resistors intentionally.** Dual brake throttles still need resistor values that match the controller’s expected voltage.
  - publish a reference chart so builders stop guessing on Zoom/Nutt lever wiring.[^18]
4. **Tame floating hall throttles.** Makerbase/Flipsky throttles that float when unplugged calm down once you add a 3.3 kΩ pull-down on ADC 1; if a lever only wakes when hard-wired to the controller, assume the harness opened up during repairs and add the resistor before reassembling the loom.[^adc-pulldown]
2. **Order matters on dual-rail harnesses.** Feeding 5 V into a Flipsky Smart Display before the 12 V lead repeatedly destroyed Spintend ADC daughterboards; always energise 12 V first, then 5 V, and confirm the display ground is shared with the controller.[^19]
3. **G300 power buttons ship as momentary inputs.** Reconfigure App → General so a button press toggles shutdown; otherwise the controller only wakes when the battery connects and ignores the dash switch.[^20][^21]
3. **Map every connector before power-up.** MakerBase looms expose 3.3 V/GND/ADC1 at the “comm” header and reroute Bluetooth through the NRF pins; miswired TX/RX leads cause telemetry dropouts or back-power logic rails.[^22]
4. **Favor multi-core RVVP over solid Ethernet in stems.** Fine-strand shielded RVVP survives stem flex better than solid-core Cat6, still carries halls, CAN, and spare conductors, and keeps throttles from snapping wide open when wires fracture.[^23]
5. **Reserve shielded Ethernet for signal runs only.** Builders keep XT150/QS8 on the power leads and repurpose Ethernet or RVVP pairs for 5 V, hall, and CAN wiring so accessories can be added later without tearing the stem apart.[^24][^25]
- **Pull the always-on accessory module if you don’t need it.** Some VESC kits ship with a piggyback board that keeps the controller awake indefinitely—removing it frees deck space and restores true shutdown behaviour.[^accessory-sleep]
- Compact stand-alone 12 V DC-DC converters tuck beside Flipsky ESCs when you need accessory power without opening the stock loom.[^compact-dcdc]
4. **Secure hall boards and sensor looms.** Hall PCBs that peel free can short against the rotor housing and mimic logic-rail failures; inspect adhesive and strain relief during reassembly.[^26]
4. **Secure hall boards and sensor looms.** Pandalgns’ front hall PCB peeled loose, shorted against the rotor, and even masqueraded as serial-port dropouts until it was re-glued and strain-relieved; bake adhesive checks and harness support into every reassembly.[^hall_short_fix]
5. **Exploit the ADC harness features.** Spintend’s ADC v3 board already supports spin dial throttles, dual-button pods, and turn-signal LED strips.
  - plan channel assignments before closing the deck and keep phase leads equal length when trimming looms.[^27]
6. **Never steal headlight power from throttle rails.** Dragging even 0.5 A from the throttle’s 5 V supply collapses the regulator, starves the ADC daughterboard, and can back-feed the 12 V converter.
  - run auxiliary lights from dedicated DC-DC converters or local packs instead.[^28]
7. **Leverage CAN power sync sparingly.** Spintend 85-series controllers share a CAN power line, so a single button can wake both units once linked; treat it as a logic trigger and avoid stacking accessory loads on the shared feed.[^29]
8. **Use CAN headers for logic, not lighting.** Smart Repair’s harness can back-feed 5 V lights through the CAN plug, but riders add inline resistors and rely on the servo PWM pads when they need flashing indicators instead of constant-on lamps.[^30]
9. **Adopt dedicated CAN lighting hubs when available.** Koxx’s 6 cm × 3 cm board feeds front, rear, and addressable channels at up to 10 A from selectable 5 V/12 V rails and daisy-chains turn signals, letting one four-wire stem trunk replace separate analog looms.[^31]
10. **Budget external bucks for single-channel builds.** Spintend’s single lacks a native auxiliary rail.
  - riders now fuse standalone DC-DC converters and only tap the horn output for low-current loads.[^32]
6. **Use multi-strand silicone for high-current leads.** PVC house wire can’t cope with scooter heat or tight bends—stick with flexible silicone/PTFE jackets when upsizing harnesses.[^multistrand]
7. **Budget dedicated DC/DC converters for heavy lighting.** Ubox buck rails sag under accessory loads; add a 12 V/3 A module or external supply instead of tying mains bricks across the HV caps.[^dc-dedicated]
5. **Exploit the ADC harness features.** Spintend’s ADC v3 board already supports spin dial throttles, dual-button pods, and turn-signal LED strips.
  - plan channel assignments before closing the deck and keep phase leads equal length when trimming looms.[^27] Skip the illuminated Spintend handlebar pod unless you’re ready to rewire it
  - the integrated lighting feeds voltage back into the signal lines instead of acting as isolated switches.[^33]
6. **Leverage CAN power sync sparingly.** Spintend 85-series controllers share a CAN power line, so a single button can wake both units once linked; treat it as a logic trigger and avoid stacking accessory loads on the shared feed.[^29]
7. **Use CAN headers for logic, not lighting.** Smart Repair’s harness can back-feed 5 V lights through the CAN plug, but riders add inline resistors and rely on the servo PWM pads when they need flashing indicators instead of constant-on lamps.[^30]
8. **Break out heavy lighting loads.** On 85250 builds, Smart Repair steers anything beyond two 12 V lamps through the ADC breakout so the controller still feeds brake-light logic while a DC/DC handles lamp current; the same harness confirmed Spin-Y2 throttle compatibility once the adapter is in place.[^34]
9. **Don’t overload the horn lead.** The Makerbase/Spintend horn channel only sources a couple of amps.
  - driving vintage 12 V 35 W halogens directly risks cooking the board; use the line to trigger a relay or low-current accessory instead.[^35]
9. **Stabilise Makerbase dash power on controller swaps.** When a Makerbase dash moves from Flipsky to Spintend/UBOX hardware, add ≈220 µF of bulk capacitance on the 5 V bus plus ~50 µF near the drivers and correct misplaced pull-up resistors to cure reboot loops under heavy accessory load.[^makerbase-dash-rails]
10. **Follow the factory lighting diagrams.** One owner cured button issues only after rewiring the Spintend ADC lighting board exactly as shown in the manual.
  - misplaced leads ghost buttons and confuse the controller.[^36]
10. **Confirm ADC signal voltage mixing.** AliExpress ADC adapters have been proven to coexist with Flipsky 75100 throttles while mixing 5 V brake levers and 3.3 V throttle inputs.
  - just keep wiring tidy and confirm shared grounds before closing the deck.[^37]
11. **Document UART swaps.** Mirko’s telemetry outage traced back to plugging the BLE module into the wrong UART; moving the dongle to ESC A (and sharing cables with the ADC module) restored data without reflashing.
  - label both ends of shared harnesses when rerouting ports.[^38]
10. **Treat Spintend’s five-way thumb cluster as a 12 V source.** Each output feeds battery voltage, so drive relays or opto inputs if you need ground-referenced logic and budget for external loads instead of hanging accessories directly on the pod.[^39]
11. **Extend Spin-Y harnesses thoughtfully.** Until longer looms arrive, riders splice shielded CAT6 to relocate the throttle and experiment with thumb-wheel grips.
  - document pinouts and strain relief so prototypes don’t fail mid-ride.[^40][^41]
12. **Pick looms that match tight passthroughs.** Shared-ground 24–26 AWG multi-core cables or slim AliExpress harnesses keep throttle, brake, and start wires tidy through VSETT/Ninebot necks; stiff Ethernet runs chafe housings and CAN cabling remains the cleanest option for long-term installs.[^42]
12. **Bundle deck looms into multi-pin plugs.** Recent harness refreshes consolidate throttle, lighting, power, and brake leads into shared multi-pin connectors while reserving 7 mm bullets for phase wires and AS150-class plugs for higher-current packs.
  - plan matching connector blocks before sealing the deck.[^43]
12. **Keep Xiaomi dash resistors in circuit.** The “noise filter” resistor on Xiaomi dashboards still needs the correct ohmic and wattage rating; leaving it out or guessing values adds instability to hall sensors after VESC swaps.[^44]
12. **Route brake contactors within ADC limits.** When you land a brake switch on ADC2, feed its positive lead straight into the pin only if it stays under 3.3 V; integrated dividers on some harnesses safely share 5 V logic, but unverified looms still need external resistors.[^45]
13. **Respect Nucular aux rails.** 12F controllers trip when you hang 60 W headlights on the onboard supply.
  - add an isolated buck for big loads even though the logic rails survive 20 S duty.[^46]
14. **Document charge-through tricks.** Some Nucular owners still feed lower-voltage sources through the hub windings to “charge through the ESC”; revive the how-to before recommending the legacy workflow.[^47]
5. **Power accessories from verified bucks.** Riders now splice a dedicated converter from the main pack to feed GPS units and other 5 V gear instead of leaning on the ADC board’s light outputs; bench-test the buck first because mislabeled modules have cooked 6 V accessories in the past.[^48]
6. **Characterise wide-input buck modules before installing them.** The popular 9–120 V down-converters rated for 5 V/2–3 A occasionally arrive with incorrect idle-draw stickers or poor calibration, so crews now sweep output with a bench supply, confirm the ≈1 mA standby claim, and document real efficiency before hanging lighting or GPS loads.
  - the ADC daughterboard is still only a signal interface, not a DC/DC substitute.[^49]
7. **Treat ADC throttle pods as momentary sources.** The Ubox 85/150 ADC harness only sends brief pulses for its on/off and light buttons, sharing the throttle ground.
  - plan downstream latching logic or relays for headlights and main-power control instead of relying on the pod alone.[^50]
8. **Exploit the ADC harness features.** Spintend’s ADC v3 board already supports spin dial throttles, dual-button pods, and turn-signal LED strips.
  - plan channel assignments before closing the deck and keep phase leads equal length when trimming looms.[^27]
9. **Leverage CAN power sync sparingly.** Spintend 85-series controllers share a CAN power line, so a single button can wake both units once linked; treat it as a logic trigger and avoid stacking accessory loads on the shared feed.[^29]
10. **Use CAN headers for logic, not lighting.** Smart Repair’s harness can back-feed 5 V lights through the CAN plug, but riders add inline resistors and rely on the servo PWM pads when they need flashing indicators instead of constant-on lamps.[^30]
11. **Confirm ADC signal voltage mixing.** AliExpress ADC adapters have been proven to coexist with Flipsky 75100 throttles while mixing 5 V brake levers and 3.3 V throttle inputs.
  - just keep wiring tidy and confirm shared grounds before closing the deck.[^37]
12. **Document UART swaps.** Mirko’s telemetry outage traced back to plugging the BLE module into the wrong UART; moving the dongle to ESC A (and sharing cables with the ADC module) restored data without reflashing.
  - label both ends of shared harnesses when rerouting ports.[^38]
13. **Treat Spintend’s five-way thumb cluster as a 12 V source.** Each output feeds battery voltage, so drive relays or opto inputs if you need ground-referenced logic and budget for external loads instead of hanging accessories directly on the pod.[^39]
14. **Bridge Minimotors dashboards with care.** Flipsky FT85BD and Ubox Lite clones need the VSETT Lisp bridge (GitHub build) to speak EY3-style displays, and leaving the bridge’s throttle-out lead floating bricks the setup.
  - treat the adapter as a complete throttle pass-through when wiring Minimotors hardware onto non-VESC controllers.[^51]
15. **Extend Spin-Y harnesses thoughtfully.** Until longer looms arrive, riders splice shielded CAT6 to relocate the throttle and experiment with thumb-wheel grips.
  - document pinouts and strain relief so prototypes don’t fail mid-ride.[^40][^41]

## Dual-Controller Wiring Patterns

- **Dual 75100 harness essentials.** Keep Makerbase twins on CAN-only links, share a single momentary power button, and bypass the G30 dash UART bridge whenever loops appear; the community wiring sketch routes each controller to its own CAN tail while the OEM dash lives on a dedicated UART breakout.[^52]
- **Keep the G30 dash powered.** Deadword proved the open-source dash lets a Makerbase 75100 route throttle and brake through the stock harness so long as the display remains powered from the VESC rail.[^53]
- **Respect CAN termination.** Mixed-controller buses pop transceivers.
  - document whether 60 Ω or 120 Ω ends are fitted, list the SN65/TJA part numbers, and isolate FlipSky units rather than trusting mismatched resistors on shared harnesses; Zero 10X experiments confirmed 120 Ω termination is mandatory and dropping to 100 Ω invites bus faults, so leave the OEM ALU-PCB to act as an antispark/key switch instead of swapping resistor values.[^54][^zero10x-120ohm]
- **Confirm what dual power leads actually feed.** One new VESC convert was already on XT150 motor leads and dual XT90 battery plugs, but the vendor demo only powered a rear wheel.
  - verify whether the second XT90 is just a pass-through before planning split-current experiments.[^xt150-split]
- **Leave the 5 V rails isolated.** Linking twin 75100s only needs CAN-H/CAN-L; tying logic rails together without a shared switch has killed hardware, so land throttles directly on a controller if the dash bridge causes loops.[^dual-5v]
- **Ninebot Vsett display harness.** The main 6-pin dash plug already carries throttle, brake, lights, and indicators.
  - map those pins (orange = pack voltage, pink = on/off detect, white = brake, black = ground) before rewiring so VESC swaps keep every control without hunting separate looms.[^55][^56]

## Display & Telemetry Options

- Analog gauge clusters look cool but add little.
  - VESC already logs current and voltage, so most riders simply mount a phone dash unless they crave retro styling.[^57]
- **SimpleVescDisplay (ESP32).** Smart Repair recommends flashing the open-source SimpleVescDisplay and 3D-printing its mount as a reliable alternative when Flipsky Voyage units glitch; PuneDir and NetworkDir now run the firmware on a €9 ESP32 touch panel that mirrors VESC Tool over BLE/Wi‑Fi, refreshes telemetry every 10 ms, keeps odometer counts stable versus 6.05 firmware, and leaves CAN free by riding over UART.[^58][^esp32-panel]
- NetworkDir surfaced the official Dualtron EY2 firmware hex and confirmed EY1/EY2/EY4 clusters run WCH CH582M MCUs that flash via WCHISPStudio, giving Dualtron owners a reproducible path to compile 6-series builds.[^dualtron_ey2_firmware]
- Oreo huzky’s CarPlay retrofit mirrors VESC telemetry onto a jailbroken iPhone or custom Android script, offering a high-visibility dash option when you’d rather leave the main phone stowed.[^carplay_dash_demo]
- **SimpleVescDisplay (ESP32).** Smart Repair recommends flashing the open-source SimpleVescDisplay and 3D-printing its mount as a reliable alternative when Flipsky Voyage units glitch.[^58]
- **Profile templates worth copying.** Yamal maintains a 23 km/h compliance mode, a 14 kW “Seven Routes” touring preset, and a “Hot Summer” throttle clamp to keep dual Uboxes cool in 40 °C commutes—log similar modes for riders balancing legality and thermals.[^yamal-profiles]
- **Tiny NRF boards have no range.** Flashing Vedder’s `nrf51_vesc` firmware onto ultra-small BLE boards left riders with unusable range, so they still buy the €2 full-size modules for dependable VESC Tool links.[^59]
- **Vedder’s `code_server` is still the stable CAN bridge.** It automatically retries failed frames five times, but you must flip RX/TX leads when moving a Makerbase/Flipsky dash loom onto Spintend/UBOX controllers and flash `slave_esc.lisp` onto every CAN slave before the dash comes alive.[^code-server]
- **SimpleVescDisplay odometer logging.** NetworkDir’s latest firmware now buffers odometer data locally on the ESP32 so riders keep mileage even if CAN frames drop, giving budget builds a telemetry path that still respects VESC Tool logs.[^60]
- **JPPL Smart Display RAM ceiling.** Running Wi-Fi and Bluetooth simultaneously exhausts the JPPL display’s RAM; leave only one wireless interface active to keep the UI responsive.[^61]
- **Rage SmartDisplay roadmap.** Rage Mechanics teased an official SmartDisplay UI refresh with thumb-wheel ergonomics feedback plus a 3.5 in navigation prototype that folds GPS into the dash.
  - validate firmware support before promising integrated maps and remember the new display only ships with controllers until CE paperwork clears; a companion anti-theft module is also in the works to hook any controller over 4/5G links.[^62][^rage-ce]
- **Waze overlay proof.** Early testers piped Waze alerts over the SmartDisplay CAN feed, proving richer overlays are feasible once the navigation stack ships.
  - capture the workflow Francois used so commuters can reproduce the police-alert demo.[^63][^64]
- **iOS configuration lockouts.** iOS riders found firmware 6.05 sessions stay read-only unless they install the TestFlight beta or pay for the App Store build—plan for the upgrade before attempting on-scooter tuning over BLE.[^ios-beta]
- **Reinstall VESC Tool before flashing Lisp.** Dash-side Lisp scripts that crashed on upload cleaned up after reinstalling the desktop app, so refresh the environment before assuming the hardware bricked.[^65]
- **Navigation demand.** Vsett and other high-speed riders want the SmartDisplay precisely to avoid strapping phones to 100 km/h scooters; the 10 cm × 6.5 cm mock-up with CAN telemetry and prompts addresses those ergonomics complaints.[^66]
- **ANT BMS display repurpose.** With few dedicated VESC dashboards shipping, riders now mount ANT smart-BMS displays as secondary cockpits to surface pack telemetry alongside MakerX and similar builds, strapping the budget screens near the bars for live pack voltage/current until purpose-built VESC dashes are available.[^67][^68]
- **Budget TFT alternative.** Builders pair ESP32-2432S028 modules with tuned TFT_eSPI firmware and 3D-printed cases to create resilient VESC dashboards while they wait for premium SmartDisplay drops.[^69]
- **Flash bargain BLE modules.** A new walkthrough covers reflashing €4 WT51822 boards into VESC telemetry bridges, trimming dash budgets further when paired with ESP32 displays.[^70]
- **Phone mounts remain brittle.** The same crews documented phone cradles ejecting devices on jumps or at 140 km/h, preferring dedicated SmartDisplays plus wireless charging only when they need extended features.[^71]
- **Decode Vsett display wiring.** The blue “DS” pin back-feeds logic power to the controller, the dash MOSFET acts as the on/off switch once the RFID tag authenticates, and the display polls the ECU every 500 ms while receiving commands roughly every 200 ms.
  - document this before splicing into the harness.[^72]
- **Dual-motor button harness.** Continuity tests show the dual-motor button shares the DS harness, toggling the slave controller while the display mirrors status.
  - tie into the loom carefully so the indicator continues to track actual drive state.[^73]
- **Xiaomi VESC firmware progress.** Koxx’s STM32-based Xiaomi firmware already auto-detects motors, keeps CPU load around 30 %, and has BLE telemetry; sensorless launch support is still in testing but hints at €25 controllers hitting 100 V/100 A once RAM/flash limits are solved.[^74]
- **Android beta caveats.** The companion Android app looks cleaner than stock VESC Tool but still mixes some motor parameters, so testers are keeping it off daily riders until sensorless launches and UI quirks are resolved.[^75]
- **Phones as interim dashboards.** Builders still stage used phones or tablets on Quad Lock mounts as temporary VESC dashboards before budgeting SmartDisplay hardware, so plan harness slack and charging for those stopgaps.[^phone-dash-plan]
- **Vsett AK script quirks.** NetworkDir reports the AK display script loses CAN control on firmware 6.02; beta 6.05 (and older beta 15) work while beta 28 does not, and every reboot rewrites the dash to “No App” and wipes ADC throttle settings.[^76]
- **VESC Tool distribution.** Vedder merged 6.0 into mainline on 8 Dec and the desktop ZIP bundles the Android APK.
  - sideload known-good versions when Play Store updates lag and archive builds before flashing customer scooters.[^77]
- **Official Android APK workflow.** Riders confirmed you can “purchase” VESC Tool for €0 on vesc-project.com and download the signed Android APK from the purchases page, eliminating the need for mirror sites during customer handoffs.[^78]
- **Display shopping list expands.** Builders now weigh 3Shull and Trampa dashboards alongside Davega, keeping AliExpress VESC screens as budget fallbacks.
  - note CAN/UART needs before rewiring looms.[^79]
- **Match app and firmware versions.** Limited-mode lockouts vanished after riders matched the mobile VESC Tool app to controllers on 6.06 firmware; sideload the APK when stores lag behind releases.[^80]
- **Mobile rollback reminder.** The latest Android APK briefly lost GPS speed on FW 5.3; keep signed installers handy so you can downgrade when regressions surface.[^81]
- **VESC-Express (ESP32-S3).** The €20 CAN↔BLE/Wi-Fi bridge adds LED or remote control outputs and modernises telemetry without touching fragile UART dongles.[^82]
- **Flash Express modules correctly.** Smart Repair’s workflow is to connect the Express over USB without CAN leads attached, open the ESP Programmer panel (bottom-left), choose the COM port, flash firmware, then move the cable to CAN for normal use.[^83]
- **Use station mode for remote sessions.** Switching VESC Express from AP to station mode lets your home router hand out the IP address, eliminating flaky TCP discovery and keeping the ESC reachable any time the scooter is powered.[^84]
- **Recover Express modules over CAN when USB ghosts.** If an Express board refuses to enumerate over USB, power it from CAN and trigger the ESP flasher inside VESC Tool before declaring the hardware dead.[^85]
- **CAN keeps telemetry alive when USB-C dies.** Riders with dead controller USB ports still pull real-time data via Express over CAN/Bluetooth, but any configuration changes require a direct USB session to the ESC itself.[^86]
- **Antenna placement matters.** Relocating and shielding the VESC Express whip restored rock-solid BLE across two concrete walls, and outdoor tests logged GPS HDOP around 0.7 once the antenna had clean sky view.
  - treat mounting as part of commissioning, not an afterthought.[^87]
- **Kaabo NFC displays.** Kaabo’s sealed NFC/password dash shares protocol with IO Hawk/VSETT units, stores top speed, and offers modern UI touches for cockpit swaps.[^88]
- **Reuse OEM dashboards via hall splitting.** Segway/Xiaomi conversions split the five hall leads (power, ground, and three sensors) so the stock controller keeps counting speed even after propulsion swaps; IO Hawk gear hubs add a sixth tach hall for the dash, so label every lead before teeing into the VESC harness.[^89]
- **Reuse the stock Vsett display with VESC.** NetworkDir confirmed the factory display keeps working on firmware 6.05 when you flash the GitHub LISP build and follow the wiring guide; it can share the ADC adapter harness if you still need light outputs.[^90][^91]
- **Carry a USB GPS backup.** Noname vouched for a ~$10 USB GPS speedometer that locks within a minute from a 5 V feed, giving scooters without CAN accessories a quick dashboard alternative when wiring full displays isn’t practical.[^92]
- **Reuse OEM dashboards via hall splitting.** Segway/Xiaomi conversions run hall power/ground plus the three phase halls to the VESC while teeing the same leads into the stock dash so trip data and speed stay intact during upgrades.[^93]
- **VESC Express logging quirks.** Firmware 6.06 currently restarts SD logging every ~3 s and Spintend X12 rails only offer 5 V/150 mA, so power Express boards from a dedicated buck and stick to 6.05 (or plan CAN updates) until patches land.[^94]
- **CAN reverse-engineering progress.** Community tooling now enumerates VESC nodes and reads live status frames; the remaining to-do is mapping extended-frame writes for current/speed limits so SmartController firmware can enforce ride modes over CAN alone.[^95]
- **Reuse OEM dashboards via hall splitting.** Segway/Xiaomi conversions run hall power/ground plus the three phase halls to the VESC while teeing the same leads into the stock dash so trip data and speed stay intact during upgrades.[^93]
- **Tame G30 brake buttons.** Swap the dash pull-up to ≈470 Ω.
  - 1 kΩ parts and oversized bulk caps keep tripping lock mode and can overstress the 5 V regulator.[^96]
- **Divide Xiaomi switch voltage.** Stock button pods push 36 V into the harness; add resistor ladders and clamp diodes before feeding 3.3 V VESC inputs so regen spikes don’t float logic rails.[^97]
- **Lock down the Express bridge.** New hardware enforces BLE passwords and exposes a Wi-Fi gateway, but the documentation lags.
  - capture setup steps so commuters don’t leave dashboards open to opportunistic pairing.[^98]
- **Raspberry Pi dash bridge.** Yoann’s Pi-powered display now ships with a TCP bridge because the Pi Zero UART is tied up by the touchscreen; dropping baud to 9,600 cleared timeouts temporarily, but USB restored the original speed and a shared 3D case is on the way.[^99]
- **Budget BLE bridges.** Generic nRF51 and ESP32 modules remain drop-in VESC Tool adapters once flashed with Vedder’s firmware, saving buyers from pricey Bluetooth dongles—and Mirono keeps steering newcomers toward reflashed ESP32s instead of branded dongles when they want reliable telemetry on a budget.[^100][^101][^esp32-ble-swap]
- **Stabilise nRF51822 boards.** A €2 BLE module held a 10 m connection through walls after a 10 µF ceramic decoupler was soldered across its supply rails, curing the random crashes riders saw on bare modules.[^102]
- **Track emerging CAN dashboards.** JPPL is test-driving the Titaone X10 controller plus Bluetooth module to see if it exposes VESC telemetry while sharing power with a 20 S 4 P commuter pack at 60 A.
  - log compatibility findings before promising customers a drop-in alt-dash.[^103]
- **Secondary UART headers.** When Voyage displays misbehave, moving telemetry to MakerBase’s TX2/RX2 header stabilised data without firmware changes; ensure extension leads are shielded if the replacements are short.[^104]
- **Secondary UART headers.** When Voyage displays misbehave, moving telemetry to MakerBase’s TX2/RX2 header stabilised data without firmware changes; Smart Repair traced the original glitch to a miswired harness and the replacement loom was so short it needed extensions.
  - label both ends before routing.[^104][^105]
- **Voyage Megan expectations.** The IPS Megan dash may launch at €300–400 with GPS and a custom app, but early adopters doubt demand above ~€150 because SmartDisplay already covers similar telemetry for less.
  - budget accordingly before preordering.[^106]
- **Stealth OEM casings.** Builders zip-tie TFT displays into stock dashboards or relocate them to auxiliary handlebars with 3D-printed mounts when they need legal-looking installs that still expose VESC telemetry.[^107][^108]
- **Budget HMI stack.** August 2022 experiments priced Nextion HMIs, waterproof Android dash conversions, Raspberry Pi round displays with gyro/RFID support, and Arduino clusters as modular QS-S4 replacements.
  - log boot times, sunlight visibility, and noise immunity before promising production swaps.[^109][^110]
- **LVGL touch display prototypes.** Mihail is validating a CAN-enabled LVGL touchscreen that breaks out throttle and brake lines but still keeps those sensors hard-wired to the ESC to avoid latency, and he already stockpiled 480×320 IPS panels plus ESP32-S3 drivers for future builds.
  - coordinate firmware sharing with Chris Culver’s existing LVGL dash work before duplicating effort.[^111][^112]
- **Integrator dash teaser.** Artem’s ~$120 “integrator” module stores police-mode presets in EEPROM and bridges QS-S4/MiniMotors displays while the full custom dash matures.
  - capture pinouts and UART voltage levels once prototypes ship.[^113]
- **Smartelec display roadmap.** The community expects Koxx’s Smartelec dash (~€400) to drop by year end with QS-S4 compatibility and power-mode presets, so document the CAN/UART wiring as soon as launch units appear.[^114]
- **Kaabo TFT prospect.** Kaabo is prototyping a rugged throttle/display combo that could expose a VESC-friendly protocol.
  - watch for CAN sniffing results before promising it as a plug-in replacement.[^115]
- **Lisp dash compatibility.** BLE 0.90 boards running heavy Lisp scripts can stutter dashboards, whereas BLE 1.2.x plus the new beta firmware boot reliably.
  - lean on OEM boards over purple clones for customer installs.[^116]
- **SmartDisplay production update.** Koxx shared assembly photos and UI previews while Rage Mechanics lined up commercial support, signaling that plug-in TFTs with temp alarms and custom icons are imminent.
  - prepare wiring diagrams and accessory budgets now.[^117][^118]
- **Android dash cradle.** Artem floated locking a €25 Android handset into a CNC mount that autoboots a stripped-down VESC monitor; evaluate boot time, glare, and OS maintenance before adopting it for commuters.[^119]
- **Split CAN telemetry.** Dual-controller logs can show ~500 A phase on Voyage/Ambrosini dashboards even when each controller only pulls ~250 A.
  - set per-controller CAN IDs or run dual sessions when you need wheel-specific diagnostics.[^per-controller]
- **Flipsky Voyage quirks.** G2 owners report the Voyage/Flipsky UART display only shows GPS speed even with correct wiring.
  - plan for custom dash scripts or SmartDisplay integrations if you need richer telemetry.[^voyage]
- **Vsett dual-drive display.** The blue “DS” line backfeeds logic power and wakes the controller once the RFID tag authenticates; the throttle itself remains analog while CAN-like messages update modes every few hundred milliseconds. Keep the dual-motor enable trace intact when repinning harnesses or the display will light up without actually toggling the slave controller.[^120]

## Switchgear & Lighting Modules

- **Koxx CAN lighting daughterboard.** Provides brake/turn LED outputs plus a programming header and extra button inputs but expects an external 5 V/12 V feed.
  - budget a buck converter or tap the Ubox rail when adding addressable strips or steering-column buttons.[^121]
- **C350 accessory rail refresh.** The latest C350 controllers now expose a ~1.2 A 12 V output for running lights, so older revisions still need an external reducer while new batches can power low-draw lamps directly.[^c350-rail]
- **Premium throttle triggers.** Polish-made e-bikestuff triggers deliver a 0.96–4.31 V sweep with zero deadband, letting riders set endpoints cleanly in VESC Tool for smoother launches if they can justify the shipping cost.[^122]
- **Lock-ring button pods.** Clamp-on grip modules add tactile turn buttons and mimic Vsett switchgear at budget prices, trading a bit of mass for ergonomic access to indicators and lighting.[^123]

## Accessory Power Practices

- **Keep lights off throttle rails.** Builders who tried to pull 0.5 A for headlights from the throttle’s 5 V line collapsed the regulator, starved ADC boards, and back-fed the 12 V converter.
  - run separate DC-DC lines or local packs instead of tapping control wiring.[^124]
- **Relay medium-power beams.** Artem’s preferred 15–16 W projector throws 40–100 m but still switches through a relay or MOSFET so the handlebar button doesn’t dump inrush current straight onto Spintend’s 3 A accessory rail.[^125]
- **Budget fused bucks for singles.** Spintend single-channel controllers omit the 12 V/3 A lighting tap.
  - plan dedicated, fused buck converters instead of hijacking fan headers or expecting the ADC board to power headlights.[^126]
- **Seal accessory PCBs carefully.** When hard-mounting display or lighting boards, solder jumpers from the rear, lock trim pots, then flood the exposed face with neutral-cure 704 silicone before sliding the board into an antistatic sleeve so component legs do not chafe against the deck.[^127]
- **Leverage Spintend’s ADC adapter for signals only.** Matthew’s Ubox 100/100 setup relies on the ADC adapter (or Lenco’s clone) to drive brake lights and turn signals; keep it on logic duty while feeding actual lighting loads from a dedicated buck so the board survives long-term.[^128]
- **Exploit the onboard 12 V rail for light loads.** Ubox owners now power wireless light switches and 20 × 11 × 11 mm limiter relays directly from the controller at ≈1.5 A, wiring 12 V, ground, and the normally-closed lead without adding another buck.
  - just stay under the comfort ceiling before stacking more accessories.[^4]
- **Fuse pack-driven headlights.** Even 20–25 W lamps only pull ~0.6 A from a 60 V pack; riders now run 0.75 mm² silicone leads with a 1 A fast-blow or polyfuse and shrink-wrap the splice, skipping bulky 16 AWG looms.[^129]

## Accessory Load Planning Workflow

1. **Audit native rails.** Before paralleling dual 12 V outputs, verify continuity.
  - builders suspect some Ubox taps share a single buck regulator, making combined 30 W loads risky.[^130]
2. **Decide external vs. onboard power.** If planned accessories exceed 3 A at 12 V or 150 mA at 5 V, route them through an external buck tied to the main battery with proper fusing rather than the controller rail.[^2][^3]
   - Matthew’s accessory rail lives on an external 12 V/20 A converter that feeds horns, pumps, lights, and fans; expect roughly 4–6 A draw from a 60 V pack and trim controller battery amps if horn surges threaten BMS headroom.[^128]
3. **Preserve regen braking.** Disabling the BMS charge FET weakens regen.
  - confirm the charge path is active before relying solely on motor braking for testing or street riding.[^131]
4. **Limit regen totals to pack capability.** When paralleling packs directly, match voltages and budget regen to the sum of both packs’ charge ratings; diode isolators caused throttle cut-outs on mismatched modules.[^132]
5. **Plan for 5 V-only controllers.** X12-class builds need a dedicated buck for anything beyond sensors.
  - budget space for the converter alongside the ADC board and document wiring so the accessory rail stays within its ~150 mA ceiling.[^5]
6. **Keep fans off the ADC adapter.** Dumping 12 V loads such as cooling fans onto Spintend’s ADC board has already scorched the adapter.
  - treat it strictly as a signal bridge and power accessories from standalone bucks.[^133]

## Lighting Hardware Spotlight

- **Kaabo hub harness expectations.** The Kaabo junction box wants pack voltage fed into the orange lead before it backfeeds 12 V blinkers.
  - jumper battery positive into the hub PCB when bypassing the stock display, reuse the handlebar switch harness, and meter the orange/brown pair because the silkscreen omits polarity while the PCB sources both pack-voltage headlight rails and a regulated 12 V branch.[^134]
- **Spintend accessory board prototype.** Recent beta boards bundle addressable LED outputs (likely WS2812/WS2815) and an integrated buzzer alongside throttle inputs, hinting that future harnesses could ship with native lighting control instead of add-on strips.[^135]
- **Match LEDs to the right rail.** Stock Xiaomi/M365 headlights expect ≈6.7 V at ~170 mA with a series resistor.
  - owners who overdrive them at 11 V either add the proper resistor, swap to 12–90 V scooter lamps, or run 6–12 V Magicshine ME-STVZO units that sip ≤1.5 A from the VESC 12 V rail.[^136]
- **Clean 5 V feeds for rear lights.** Xiaomi brake lamps driven by Spintend ADC adapters need a solid 5 V, 120 mA supply; misconfigured inputs make the brake lever act like a throttle until riders recalibrate in current mode and hand-edit the brake values.[^137]
- **Stage running/brake lights with relays.** Dual-relay modules let VESC outputs drop a resistor for running lights while energising the brake circuit separately, matching the two-level behaviour Nucular owners enjoy without bespoke boards.[^138]
- **Offbondge projector upgrade.** Riders migrating from 1,300 lm compact beams report Offbondge’s 2,000–2,500 lm projector headlight slots straight into existing 12 V harnesses, spreads light without dazzling traffic, and still benefits from external bucks or fused rails on single-controller builds.[^139][^140]
- **CNSunnylight LX18 spotlight.** The LX18’s dual-mode ~60 W beam accepts 8–90 V packs, letting commuters replace multi-headlight stacks with a single housing while ordering dual-white batches when they need balanced colour temperature.[^141]
- Tail-light retrofits need either built-in flasher ICs or MOSFET drivers; builders lean on AliExpress strips with sequencers and power 48 V accessories through dedicated bucks or aux packs instead of hanging them off controller rails.[^142]
- **Offbondge projector upgrade.** Riders migrating from 1,300 lm compact beams report Offbondge’s 2,000–2,500 lm projector headlight slots straight into existing 12 V harnesses, spreads light without dazzling traffic, and still benefits from external bucks or fused rails on single-controller builds.[^143]
- **Prioritise beam control over lumen hype.** Riders rate STVZO-compliant Magicshine 100 lux headlights for crisp cutoffs that avoid blinding traffic, making them a better commuter upgrade than raw-lumen floodlights.[^144]
- **USB-C floodlight banks.** Commuters are trialling 3,000–9,000 lm rechargeable headlights that double as power banks and pair them with programmable LED tails or mirror-mounted 12 V lamps for better cutoff control than stock scooter beams.[^145]
- **Custom dual-white housings.** Builders have also commissioned 9–80 V dual-white lamps (~€43) that split 40 W low/20 W high output across an 8 m beam, creating compact alternatives to bulky multi-light arrays.[^146]
- **Stacked horn strategy.** Compact GREATZT QSI-4840 sirens (~€2.76) shrink to ≈30 × 20 mm once de-cased, blast 120–125 dB from the Ubox horn output, and stay permanently wired to the traction pack so there’s no battery upkeep. Builders then add a friendlier 110 dB cycling horn (≈35 × 30 × 20 mm PCB) on a second button or remote for polite alerts while keeping the siren for traffic conflicts.[^147][^148]
- **Centralised CAN lighting.** The same CAN board handles per-channel dimming, addressable strips, and horn/turn-signal logic, while Artem’s stem-mounted connector block muxes OEM throttle/brake UART into CAN so only two to four conductors run down the column.[^31]
- **Stacked horn strategy.** Compact GREATZT QSI-4840 sirens (~€2.76) shrink to ≈30 × 20 mm once de-cased, blast 120–125 dB from the Ubox horn output, and stay permanently wired to the traction pack so there’s no battery upkeep. Builders then add a friendlier 110 dB cycling horn (≈35 × 30 × 20 mm PCB) on a second button or remote for polite alerts while keeping the siren for traffic conflicts, often retaining the stock Xiaomi bell for low-key trail etiquette alongside 120 dB square-wave buzzers for dense traffic.[^147][^148][^149][^150]
- **Hardwire over stand-alone packs.** Riders who experimented with battery-powered alarms now prefer buck-fed horns with the controller’s horn output or dedicated wiring harnesses so everything wakes with the scooter, even if the accessory offers handheld remotes out of the box.[^151]
- **High-beam benchmark.** Artem’s preferred high beam is a genuine 15–16 W module that throws 40–100 m and pulls roughly 1.3 A from a 12 V rail; trigger it with a relay or MOSFET off a physical button so the controller’s 3 A accessory output never sees the switching surge directly.[^152]
- **Meter AliExpress wattage claims.** “20 W” projector pods routinely draw only 10–14 W at 48 V; log current and dispute listings before trusting catalog specs, especially on dual-beam shells that split output between high and low filaments.[^153]

## High-Current Connector Guidance

- **Avoid house-style clamps above 150 A.** WAGO and screw-terminal blocks overheat on 150 A+ scooter feeds.
  - solder joints backed by AS150/EC8 connectors remain the reliable path for controller and lighting trunks.[^154]
- **Skip screw-terminal mains blocks entirely.** AdianV’s attempt to route pack leads through low-cost terminal strips melted near 5 A and threatened the controller; hard-solder high-gauge leads or step up to genuine Amass/AS150 hardware instead.[^155]
- **Stagger and heatshrink splices.** When upsizing harnesses for lighting looms or dash power, stagger solder joints and double-wall heatshrink them to prevent shorts once the deck compresses wiring.[^156]
- **Lock accessories with adhesive as well as hardware.** Builders stick with XT60-class connectors for modular add-ons and back them up with Pattex hot glue plus Sikaflex 11fc+ so high-power lights and horns stay planted despite deck vibration.[^157][^158]
- **Plan for dual QS8 harness bulk.** Yamal and Gabe are running paired QS8s with 6 AWG leads on their multi-controller builds.
  - budget thick silicone jackets and extra routing space when following those race layouts.[^dual-qs8-harness]
- **Match connector ratings to current.** QS10 plugs hover around 180 A, while QS12 handles ~300 A and should back 175 A-per-controller builds that would cook QS8 hardware.[^qs12]
- **Upsize parallel leads when stretching pack current.** Doubling 14 AWG runs or stepping to 12 AWG keeps 35 A paths from cooking inside sealed decks.[^awg-upsize]

## Addressable Lighting Integration

- Choose 12 V-friendly WS2815 or similar pixel strips so a single buck can feed both controller logic and the lighting rail without brownouts; they still need ESP32/WLED drivers and regulated supplies or the strips overheat.[^159]
- Flash ESP32/WLED controllers with per-mode current caps, set boot presets that default to dim commuter profiles, and isolate the data line with a logic-level shifter when the strip sits far from the controller harness.[^159]
- **Repurpose failed controllers as CAN/BLE hubs.** Even with the power stage removed, a VESC still runs dashboards, BLE bridges, and other peripherals when its DC/DC section is intact, letting travelers keep telemetry alive while waiting on replacement ESCs.[^vesc-can-bridge]
- Budget fusing and surge suppression.
  - inline 3–5 A fuses plus TVS diodes on the buck output prevent decorative installs from collapsing the accessory rail when pixels short or moisture enters connectors.[^159]

## Wireless Security Hardening

- Mask the controller’s identity, enforce MAC filtering, and require PIN prompts so park-side pranksters cannot overwrite ride profiles while the scooter is unattended.[^160][^161]
- Back Bluetooth hardening with keyed or NFC-switched power so even successful pairings cannot energise the controller without physical access.[^160][^161]
- Riders still want a VESC-powered GPS beacon that sips from the traction pack; until one ships, they rotate SIM trackers, Samsung SmartTags, or Jedich Nixan beacons that recharge on rides but only last days when parked.[^162]
- Mask the controller’s identity, enforce MAC filtering, and require PIN prompts so park-side pranksters cannot overwrite ride profiles while the scooter is unattended.[^161]
- Back Bluetooth hardening with keyed or NFC-switched power so even successful pairings cannot energise the controller without physical access.[^161]

## Control Hardware Picks

- **Waterproof thumb throttles.** 🇪🇸AYO#74🏁 favors a three-pin thumb throttle with minimal dead zone and warns that the CNC Spin-Y2 twin-action throttle breaks easily despite regen convenience.
  - budget spares or alternatives when planning builds.[^163]
- **Hall-sensor brake levers and sensors.** Builders recommend hall-based brake levers for smaller hands and pair them with waterproof two-pin hydraulic sensors that slot neatly into Magura or Nutt setups.[^164]
- **Auxiliary throttle braking caveats.** Repurposing a spare throttle as an auxiliary brake only adds meaningful stopping power when regen is configured high; keep mechanical lever ergonomics dialled for everyday stops.[^165]
- **CAN button pods on the wishlist.** Riders want stem-mounted pods with built-in transceivers so a four-wire trunk (power, ground, CAN_H, CAN_L) can replace bulky analog harnesses for lights, horn, and turn signals.
  - plan for that future wiring when routing today’s builds.[^166]
- **Keep stock Vsett throttles in spec.** Marko preserved the factory thumb lever by sliding its hall sensor until wide-open output hit 3.3 V; when geometry won’t cooperate, riders swap to 5 V throttles with resistor dividers or Spintend’s ADC module for cleaner filtering.[^167]
- **Plan a discrete brake-light trigger.** Most VESC controllers.
  - including Makerbase 75/200 variants
  - lack a native regen-triggered brake light, so dedicate an ADC output or external GPIO with a relay/transistor stage if you need 12 V lighting to mirror throttle-based braking.[^168][^169]

### Field Lighting Power Patterns

- Yamal prefers tapping 12 V bars directly from the traction battery through a fused buck so they recharge with the scooter, whereas Noname populates USB hubs on every build for removable lights and accessories.[^170]
- Haku routinely feeds inexpensive AliExpress lightbars through the ADC harness, underscoring why guides should spell out current limits and fuse math before riders stack accessories on controller rails.[^171]
- Mirono needs more than 3 A at 12 V for auxiliary lighting and horns, so he parallels dual buck converters when he refuses to carry a separate pack.
  - Paolo still flags an external battery as the simpler path when accessory current climbs.[^172]
- Spintend’s ADC v2 light rail only supplies ≈3.3 V and 30–40 W; halogen H1/H3 bulbs overheat MOSFETs and housings, so stick to step-down-fed LEDs or low-watt motorcycle bulbs until refreshed hardware lands.[^173]

## Commissioning Checklist

- Meter throttle outputs with the controller unpowered and confirm signal stays ≤3.3 V at full travel.[^7]
- Before flashing or editing parameters, follow the VESC Tool workflow.
  - **Read → edit → Write**
  - and explicitly hit **Write Motor/App Config** after each wizard so Xiaomi throttles and ADC settings persist across power cycles instead of forcing full detections at the next boot.[^174][^175]
- Haku routinely feeds inexpensive AliExpress lightbars through the ADC harness, underscoring why guides should spell out current limits, fuse values, and wiring diagrams before riders stack accessories on controller rails.[^176]
- Rogerio’s tests show Spinny/ADC daughterboards fry if you power them from external 12 V rails after the controller wakes—energise the auxiliary supply first or keep them on the native rail.[^spinny-sequence]
- Map the MakerBase comm header before plugging in displays.
  - NRF pins handle Bluetooth, the hall plug feeds sensors, and the comm port exposes 3.3 V/GND/ADC1 for throttles, so labelling each lead prevents back-powering telemetry gear.[^177]
- Before flashing or editing parameters, follow the VESC Tool workflow.
  - **Read → edit → Write**
  - and explicitly hit **Write Motor/App Config** after each wizard so Xiaomi throttles and ADC settings persist across power cycles instead of forcing full detections at the next boot.[^174][^178]
- Log live current on accessory rails during first rides to validate that horns, lights, and pumps stay within regulator capacity; retune battery current if accessories share pack headroom with the controller.[^13]
- After harness work, perform continuity checks on 12 V outputs and confirm no sensor grounds are floating before closing the deck.[^130][^22]
- Confirm Spintend singles leave the NRF header free for Bluetooth.
  - external dongles must use that port because the lone RX/TX pair is usually occupied by dashboards or ADC adapters.[^179]

## Fabrication Helpers

- Keep a square-hole drilling jig handy for controller brackets and switch panels—Haku surfaced an off-the-shelf guide that saves hours compared with freehand work.[^square-jig]
- Carbon-fibre–filled PETG is only semi-insulating; add extra sleeving or barriers when routing AC charge plugs through printed mains covers.[^cf-petg]

## Outstanding Documentation Needs

1. Publish a formal power-sequencing diagram for Flipsky and SimpleVescDisplay installs on Spintend/MakerBase hardware, including connector pinouts and ground references.[^180]
2. Capture tested fuse ratings and wire gauges for external 12 V bucks powering horns, lights, and air compressors so builders can size safety hardware confidently.[^13]
3. Verify whether Spintend’s Spinny/ADC v2 harness can safely source dual-function tail/brake lights or if relays are required, then publish the findings alongside rail current measurements.[^3][^181]
4. Track the community Nextion/Pico dash builds and the promised €120 integrator display so we can ship pinout diagrams the moment production units land.[^182][^183]
5. Capture a reproducible Spintend Ubox 85_250 firmware build.
  - Thierry still compiles it manually and patches header typos because VESC Tool omits the binary and 6.02 throws build errors while 6.05 beta remains the safe fallback.[^99]
4. Confirm whether the twin 12 V outputs on Ubox 85240 controllers share a single buck regulator before riders parallel them for higher current loads, and publish continuity test steps once validated.[^184]
5. Track the community Nextion/Pico dash builds and the promised €120 integrator display so we can ship pinout diagrams the moment production units land.[^182][^183]

## Source Notes

- Accessory rail limits, regen dependencies, and buck converter planning consolidate Smart Repair’s October 2025 integration notes covering Ubox rail continuity, 3.3 V throttle safety, CAN-powered lighting, and parallel-pack regen etiquette.[^185][^30]
- Late-2022 Spintend updates add latching-switch expectations, SmartDisplay roadmap teasers, the ADC adapter overload case, and reminders that the light cluster sources 12 V rather than sinking loads.[^186][^187][^63]
- Lighting hardware, accessory sourcing, and controller-rail constraints reflect the broader VESC Help Group coverage of Offbondge projector testing, Voyage/SmartDisplay integration, and Spinny harness current ceilings.[^188][^5]
- Eye4 integration status captures the ongoing Telegram debate that no production firmware exists yet and retrofitters still need to wire full UART plus the wake line before a VESC-specific build is viable.[^189]
[^xt150-split]: Vendor demo builds with dual XT90s and XT150 motor leads may still feed a single controller.
  - confirm wiring before assuming split current capability.[^190]
[^phone-dash-plan]: Riders are still planning Quad Lock-mounted phones or tablets as temporary dashboards before moving to SmartDisplay hardware.[^191]
[^square-jig]: Square-hole drilling jig shared for cleaner controller bracket installs.[^192]
[^dual-qs8-harness]: Dual QS8 harness photos highlighted 6 AWG silicone leads and chunky routing on Yamal and Gabe’s builds.[^193]
[^multistrand]: Yamal and Gabe reiterated that high-power phase leads should stay multi-strand silicone/PTFE.
  - PVC house wire can’t take heat or tight bends.[^194]
[^dc-dedicated]: Ubox buck rails sag under heavy accessory loads.
  - Sombre_enfant adds a dedicated 12 V/3 A converter or external supply instead of tying mains bricks across the HV capacitor.[^195]
[^dual-5v]: Twin 75100s only need CAN-H/CAN-L; tying the 5 V rails together without a shared power button has killed hardware, so wire throttles straight to the controller if the dash bridge causes loops.[^196]
[^qs12]: Kirill’s connector rundown pegs QS10 around 180 A while QS12 handles ≈300 A, making the latter the safe choice for 175 A-per-controller builds.[^197]
[^awg-upsize]: Gabe doubled 14 AWG battery leads—and often steps to 12 AWG—to keep 35 A runs from heating sealed decks.[^198]
[^cf-petg]: Carbon-fibre–filled PETG behaves like a weak conductor even at 100–1,000 V.
  - treat printed mains covers as semi-conductive and add insulation.[^199]
[^per-controller]: Voyage/Ambrosini dashboards can display ~500 A combined phase current on dual-controller builds, so configure per-controller CAN IDs or split sessions when you need wheel-specific telemetry.[^200]
[^voyage]: Voyage/Flipsky displays on Ninebot G2 builds have been limited to GPS-only readouts despite proper wiring, prompting teams to script custom dashboards or adopt SmartDisplay alternatives.[^201]
[^jp-generic]: TF/TS100-style colour order confirmation for the unlabeled “generic JP” display plus upcoming CAN/SmartDisplay hardware that keeps RX, TX, GND, and 5 V today and adds ESP32-C3 Express telemetry next revision.[^202]
[^voyage-megan]: Voyage “Megan” dash sold direct to riders chasing CAN-first lighting integrations without UART compromises.[^203]
[^spintend-pod]: Spintend’s illuminated handlebar pod feeds voltage back into ADC signal lines instead of acting as isolated switches, so it requires rewiring for VESC compatibility.[^33]


## References

[^1]: Source: knowledge/notes/input_part012_review.md†L404-L405
[^2]: Source: knowledge/notes/input_part013_review.md†L360-L361
[^3]: Source: knowledge/notes/input_part013_review.md†L430-L431
[^4]: Source: knowledge/notes/input_part000_review.md†L687-L687
[^spintend_remote]: Source: knowledge/notes/input_part000_review.md†L735-L736
[^5]: Source: knowledge/notes/input_part014_review.md†L140-L144
[^6]: Source: knowledge/notes/input_part014_review.md†L140-L145
[^7]: Source: knowledge/notes/input_part013_review.md†L503-L505
[^8]: Source: knowledge/notes/input_part013_review.md†L329-L329
[^9]: Source: data/vesc_help_group/text_slices/input_part005.txt†L21844-L21933
[^10]: Source: knowledge/notes/input_part012_review.md†L49-L49
[^11]: Source: knowledge/notes/input_part014_review.md†L7726-L7758
[^12]: Source: knowledge/notes/input_part005_review.md†L405-L408
[^13]: Source: knowledge/notes/input_part013_review.md†L400-L401
[^14]: Source: knowledge/notes/input_part014_review.md†L79-L79
[^15]: Source: knowledge/notes/input_part014_review.md†L80-L82
[^16]: Source: knowledge/notes/input_part003_review.md†L101-L101
[^17]: Source: knowledge/notes/input_part013_review.md†L366-L367
[^18]: Source: knowledge/notes/input_part002_review.md†L174-L176
[^19]: Source: knowledge/notes/input_part013_review.md†L111-L111
[^20]: Source: knowledge/notes/input_part013_review.md†L219-L219
[^21]: Source: knowledge/notes/input_part013_review.md†L247-L247
[^22]: Source: knowledge/notes/input_part013_review.md†L368-L368
[^23]: Source: knowledge/notes/input_part006_review.md†L426-L427
[^24]: Source: knowledge/notes/input_part006_review.md†L405-L406
[^25]: Source: knowledge/notes/input_part006_review.md†L427-L427
[^26]: Source: knowledge/notes/input_part013_review.md†L603-L604
[^27]: Source: knowledge/notes/input_part014_review.md†L209-L210
[^28]: Source: knowledge/notes/input_part000_review.md†L406-L408
[^29]: Source: knowledge/notes/input_part011_review.md†L19016-L19035
[^30]: Source: knowledge/notes/input_part012_review.md†L19323-L19405
[^31]: Source: knowledge/notes/input_part000_review.md†L556-L559
[^32]: Source: knowledge/notes/input_part000_review.md†L544-L544
[^33]: Source: knowledge/notes/input_part010_review.md†L75-L77
[^spintend_relay_current]: Source: knowledge/notes/input_part000_review.md†L735-L735
[^34]: Source: knowledge/notes/input_part012_review.md†L180-L180
[^35]: Source: knowledge/notes/input_part012_review.md†L97-L97
[^36]: Source: knowledge/notes/input_part012_review.md†L434-L434
[^37]: Source: data/vesc_help_group/text_slices/input_part003.txt†L5708-L5714
[^38]: Source: data/vesc_help_group/text_slices/input_part003.txt†L7402-L7424
[^39]: Source: data/vesc_help_group/text_slices/input_part003.txt†L15721-L15747
[^40]: Source: data/vesc_help_group/text_slices/input_part003.txt†L7767-L7805
[^41]: Source: data/vesc_help_group/text_slices/input_part003.txt†L8600-L8605
[^42]: Source: data/vesc_help_group/text_slices/input_part001.txt†L6481-L6504
[^43]: Source: data/vesc_help_group/text_slices/input_part003.txt†L19431-L19437
[^44]: Source: knowledge/notes/input_part005_review.md†L315-L318
[^45]: Source: knowledge/notes/input_part006_review.md†L205-L206
[^46]: Source: knowledge/notes/input_part006_review.md†L298-L298
[^47]: Source: knowledge/notes/input_part006_review.md†L299-L299
[^48]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21797-L21820
[^49]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21797-L21839
[^50]: Source: knowledge/notes/input_part009_review.md†L383-L383
[^51]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21880-L21903
[^52]: Source: knowledge/notes/input_part007_review.md†L505-L505
[^53]: Source: knowledge/notes/input_part007_review.md†L400-L404
[^54]: Source: knowledge/notes/input_part007_review.md†L527-L527
[^55]: Source: knowledge/notes/input_part012_review.md†L383-L383
[^56]: Source: knowledge/notes/input_part012_review.md†L431-L431
[^57]: Source: knowledge/notes/input_part005_review.md†L128-L128
[^58]: Source: knowledge/notes/input_part013_review.md†L367-L367
[^59]: Source: knowledge/notes/input_part005_review.md†L346-L347
[^60]: Source: knowledge/notes/input_part008_review.md†L203-L204
[^61]: Source: data/vesc_help_group/text_slices/input_part009.txt†L12510-L12513
[^yamal-profiles]: Source: knowledge/notes/input_part013_review.md†L841-L841
[^62]: Source: knowledge/notes/input_part003_review.md†L108-L163
[^63]: Source: knowledge/notes/input_part003_review.md†L192-L192
[^esp32-ble-swap]: Source: data/vesc_help_group/text_slices/input_part004.txt†L20350-L20370
[^vesc-can-bridge]: Source: data/vesc_help_group/text_slices/input_part004.txt†L23039-L23042
[^64]: Source: data/vesc_help_group/text_slices/input_part003.txt†L26600-L26606
[^65]: Source: knowledge/notes/input_part012_review.md†L170-L170
[^66]: Source: data/vesc_help_group/text_slices/input_part003.txt†L21249-L21272
[^67]: Source: knowledge/notes/input_part002_review.md†L167-L167
[^68]: Source: data/vesc_help_group/text_slices/input_part002.txt†L10912-L10916
[^69]: Source: knowledge/notes/input_part006_review.md†L235-L235
[^70]: Source: knowledge/notes/input_part006_review.md†L240-L240
[^71]: Source: data/vesc_help_group/text_slices/input_part003.txt†L21255-L21271
[^72]: Source: knowledge/notes/input_part000_review.md†L756-L762
[^73]: Source: knowledge/notes/input_part000_review.md†L762-L766
[^74]: Source: knowledge/notes/input_part000_review.md†L766-L772
[^75]: Source: knowledge/notes/input_part000_review.md†L772-L777
[^76]: Source: knowledge/notes/input_part007_review.md†L356-L360
[^77]: Source: data/vesc_help_group/text_slices/input_part003.txt†L17564-L17573
[^78]: Source: knowledge/notes/input_part008_review.md†L257-L259
[^79]: Source: knowledge/notes/input_part012_review.md†L381-L381
[^80]: Source: knowledge/notes/input_part012_review.md†L171-L171
[^81]: Source: data/vesc_help_group/text_slices/input_part003.txt†L21434-L21447
[^82]: Source: knowledge/notes/input_part013_review.md†L418-L418
[^83]: Source: knowledge/notes/input_part012_review.md†L251-L255
[^84]: Source: knowledge/notes/input_part012_review.md†L108-L108
[^85]: Source: knowledge/notes/input_part012_review.md†L172-L172
[^86]: Source: knowledge/notes/input_part012_review.md†L255-L258
[^87]: Source: knowledge/notes/input_part012_review.md†L89-L90
[^88]: Source: knowledge/notes/input_part004_review.md†L268-L268
[^89]: Source: data/vesc_help_group/text_slices/input_part004.txt†L7264-L7287
[^90]: Source: data/vesc_help_group/text_slices/input_part009.txt†L6920-L6920
[^91]: Source: data/vesc_help_group/text_slices/input_part009.txt†L9655-L9697
[^92]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21858-L21867
[^93]: Source: knowledge/notes/input_part004_review.md†L166-L167
[^94]: Source: knowledge/notes/input_part014_review.md†L5969-L6037
[^95]: Source: knowledge/notes/input_part000_review.md†L558-L558
[^96]: Source: knowledge/notes/input_part006_review.md†L204-L204
[^97]: Source: knowledge/notes/input_part006_review.md†L205-L205
[^98]: Source: knowledge/notes/input_part006_review.md†L270-L270
[^99]: Source: knowledge/notes/input_part007_review.md†L360-L364
[^100]: Source: knowledge/notes/input_part004_review.md†L279-L279
[^101]: Source: knowledge/notes/input_part004_review.md†L307-L307
[^102]: Source: knowledge/notes/input_part005_review.md†L247-L247
[^103]: Source: knowledge/notes/input_part010_review.md†L391-L392
[^104]: Source: knowledge/notes/input_part013_review.md†L518-L518
[^105]: Source: data/vesc_help_group/text_slices/input_part013.txt†L6220-L6227
[^106]: Source: knowledge/notes/input_part005_review.md†L378-L379
[^107]: Source: knowledge/notes/input_part000_review.md†L45-L47
[^108]: Source: knowledge/notes/input_part000_review.md†L57-L58
[^109]: Source: data/vesc_help_group/text_slices/input_part003.txt†L5218-L5261
[^110]: Source: data/vesc_help_group/text_slices/input_part003.txt†L5690-L5707
[^111]: Source: knowledge/notes/input_part008_review.md†L210-L212
[^112]: Source: knowledge/notes/input_part008_review.md†L246-L247
[^113]: Source: data/vesc_help_group/text_slices/input_part003.txt†L7310-L7315
[^114]: Source: knowledge/notes/input_part003_review.md†L77-L77
[^115]: Source: data/vesc_help_group/text_slices/input_part003.txt†L9804-L9808
[^116]: Source: data/vesc_help_group/text_slices/input_part003.txt†L10439-L10459
[^117]: Source: data/vesc_help_group/text_slices/input_part003.txt†L11046-L11048
[^118]: Source: data/vesc_help_group/text_slices/input_part003.txt†L11852-L11872
[^119]: Source: data/vesc_help_group/text_slices/input_part003.txt†L8798-L8799
[^120]: Source: knowledge/notes/input_part000_review.md†L734-L741
[^121]: Source: knowledge/notes/input_part000_review.md†L624-L624
[^accessory-sleep]: Source: knowledge/notes/input_part010_review.md†L543-L543
[^c350-rail]: Source: knowledge/notes/input_part010_review.md†L584-L584
[^122]: Source: knowledge/notes/input_part000_review.md†L625-L625
[^123]: Source: knowledge/notes/input_part000_review.md†L626-L626
[^124]: Source: data/vesc_help_group/text_slices/input_part000.txt†L17986-L18013
[^125]: Source: data/vesc_help_group/text_slices/input_part000.txt†L16921-L16943
[^126]: Source: data/vesc_help_group/text_slices/input_part000.txt†L18956-L18988
[^127]: Source: knowledge/notes/input_part006_review.md†L399-L399
[^128]: Source: knowledge/notes/input_part013_review.md†L398-L401
[^129]: Source: data/vesc_help_group/text_slices/input_part000.txt†L19990-L20099
[^130]: Source: knowledge/notes/input_part013_review.md†L547-L547
[^131]: Source: knowledge/notes/input_part013_review.md†L505-L505
[^132]: Source: knowledge/notes/input_part013_review.md†L550-L552
[^133]: Source: knowledge/notes/input_part003_review.md†L126-L128
[^134]: Source: knowledge/notes/input_part002_review.md†L488-L491
[^135]: Source: knowledge/notes/input_part001_review.md†L629-L630
[^136]: Source: knowledge/notes/input_part006_review.md†L189-L189
[^137]: Source: knowledge/notes/input_part006_review.md†L190-L190
[^138]: Source: knowledge/notes/input_part006_review.md†L300-L300
[^139]: Source: knowledge/notes/input_part005_review.md†L404-L404
[^140]: Source: knowledge/notes/input_part005_review.md†L571-L571
[^141]: Source: data/vesc_help_group/text_slices/input_part003.txt†L4700-L4890
[^142]: Source: knowledge/notes/input_part005_review.md†L127-L127
[^143]: Source: data/vesc_help_group/text_slices/input_part005.txt†L22250-L22257
[^dualtron_ey2_firmware]: Source: knowledge/notes/input_part008_review.md†L479-L480
[^carplay_dash_demo]: Source: knowledge/notes/input_part008_review.md†L481-L481
[^hall_short_fix]: Source: knowledge/notes/input_part013_review.md†L604-L604
[^144]: Source: knowledge/notes/input_part005_review.md†L58-L59
[^145]: Source: knowledge/notes/input_part000_review.md†L47-L48
[^146]: Source: data/vesc_help_group/text_slices/input_part003.txt†L8188-L8223
[^147]: Source: data/vesc_help_group/text_slices/input_part000.txt†L23001-L23039
[^148]: Source: data/vesc_help_group/text_slices/input_part000.txt†L23080-L23097
[^149]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11814-L11822
[^150]: Source: data/vesc_help_group/text_slices/input_part002.txt†L12070-L12078
[^151]: Source: data/vesc_help_group/text_slices/input_part000.txt†L23029-L23034
[^152]: Source: knowledge/notes/input_part000_review.md†L404-L406
[^153]: Source: knowledge/notes/input_part000_review.md†L541-L544
[^154]: Source: data/vesc_help_group/text_slices/input_part004.txt†L17752-L17764
[^155]: Source: knowledge/notes/input_part010_review.md†L369-L370
[^156]: Source: knowledge/notes/input_part004_review.md†L248-L248
[^157]: Source: data/vesc_help_group/text_slices/input_part003.txt†L7283-L7284
[^158]: Source: data/vesc_help_group/text_slices/input_part003.txt†L7433-L7439
[^159]: Source: knowledge/notes/input_part006_review.md†L431-L431
[^160]: Source: knowledge/notes/input_part006_review.md†L80-L80
[^161]: Source: knowledge/notes/input_part006_review.md†L428-L429
[^162]: Source: knowledge/notes/input_part005_review.md†L238-L238
[^163]: Source: knowledge/notes/input_part009_review.md†L393-L395
[^164]: Source: knowledge/notes/input_part009_review.md†L395-L395
[^165]: Source: knowledge/notes/input_part009_review.md†L396-L396
[^166]: Source: knowledge/notes/input_part000_review.md†L529-L529
[^167]: Source: knowledge/notes/input_part007_review.md†L404-L408
[^adc-pulldown]: knowledge/notes/input_part007_review.md lines 401-401.
[^esp32-panel]: knowledge/notes/input_part007_review.md lines 405-405.
[^rage-ce]: knowledge/notes/input_part007_review.md lines 406-406.
[^ios-beta]: knowledge/notes/input_part007_review.md lines 407-407.
[^168]: Source: data/vesc_help_group/text_slices/input_part009.txt†L7134-L7141
[^169]: Source: data/vesc_help_group/text_slices/input_part009.txt†L7741-L7754
[^170]: Source: knowledge/notes/input_part013_review.md†L217-L224
[^171]: Source: knowledge/notes/input_part013_review.md†L222-L224
[^172]: Source: data/vesc_help_group/text_slices/input_part002.txt†L12063-L12095
[^173]: Source: knowledge/notes/input_part005_review.md†L311-L317
[^174]: Source: knowledge/notes/input_part013_review.md†L542-L544
[^175]: Source: data/vesc_help_group/text_slices/input_part005.txt†L22481-L22495
[^176]: Source: knowledge/notes/input_part013_review.md†L222-L249
[^spinny-sequence]: Source: knowledge/notes/input_part013_review.md†L796-L796
[^177]: Source: knowledge/notes/input_part013_review.md†L406-L408
[^178]: Source: knowledge/notes/input_part005_review.md†L410-L413
[^179]: Source: knowledge/notes/input_part004_review.md†L197-L197
[^180]: Source: knowledge/notes/input_part013_review.md†L366-L368
[^181]: Source: knowledge/notes/input_part013_review.md†L548-L548
[^182]: Source: knowledge/notes/input_part003_review.md†L67-L68
[^183]: Source: knowledge/notes/input_part003_review.md†L72-L73
[^184]: Source: knowledge/notes/input_part013_review.md†L130-L130
[^185]: Source: knowledge/notes/input_part013_review.md†L360-L552
[^186]: Source: knowledge/notes/input_part003_review.md†L101-L129
[^187]: Source: knowledge/notes/input_part003_review.md†L108-L128
[^188]: Source: data/vesc_help_group/text_slices/input_part005.txt†L21883-L22257
[^189]: Source: data/vesc_help_group/text_slices/input_part007.txt†L147-L161
[^190]: Source: knowledge/notes/input_part007_review.md†L132-L132
[^191]: Source: knowledge/notes/input_part007_review.md†L136-L136
[^192]: Source: knowledge/notes/input_part007_review.md†L113-L113
[^193]: Source: knowledge/notes/input_part007_review.md†L158-L175
[^194]: Source: knowledge/notes/input_part007_review.md†L220-L220
[^195]: Source: knowledge/notes/input_part007_review.md†L221-L221
[^196]: Source: knowledge/notes/input_part007_review.md†L260-L260
[^197]: Source: knowledge/notes/input_part007_review.md†L222-L222
[^198]: Source: knowledge/notes/input_part007_review.md†L230-L230
[^199]: Source: knowledge/notes/input_part007_review.md†L261-L261
[^200]: Source: knowledge/notes/input_part013_review.md†L186-L209
[^201]: Source: knowledge/notes/input_part014_review.md†L189-L189
[^202]: Source: knowledge/notes/input_part010_review.md†L16-L18
[^203]: Source: knowledge/notes/input_part010_review.md†L18-L18
[^code-server]: Source: knowledge/notes/input_part006_review.md†L21-L21
[^makerbase-dash-rails]: Source: knowledge/notes/input_part006_review.md†L23-L23
[^zero10x-120ohm]: Source: knowledge/notes/input_part006_review.md†L24-L24
[^can-display-roadmap]: Source: knowledge/notes/input_part010_review.md†L668-L668
[^compact-dcdc]: Source: knowledge/notes/input_part010_review.md†L670-L670
