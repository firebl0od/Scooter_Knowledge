# VESC Accessory Power & Display Integration Checklist

## Purpose
This guide distills field reports on powering lights, horns, and dashboards from aftermarket VESC controllers so builders avoid overloading regulator rails or frying logic accessories during swaps.

## Quick Reference Matrix
| Controller family | Native accessory rails | Verified limits & caveats | Recommended mitigations |
| --- | --- | --- | --- |
| Tronic X12 | 5 V logic (≈150 mA) | Rail cannot sustain heavy peripherals such as displays or fans without brownouts.【F:knowledge/notes/input_part013_review.md†L360-L361】 | Budget an external buck converter for any load above small sensors and throttle/gear switches.【F:knowledge/notes/input_part013_review.md†L360-L361】 |
| Spintend Ubox 85×/24× | 5 V logic, 12 V rail (rated 3 A) | Riders only trust the 12 V feed for a brake light; running both Dualtron headlight and taillight exceeded the regulator’s comfort zone.【F:knowledge/notes/input_part013_review.md†L430-L431】 | Keep lighting minimalist or offload to a dedicated buck; fuse each branch so single shorts do not collapse the regulator.【F:knowledge/notes/input_part013_review.md†L430-L431】 |
| Spintend X12 / upcoming 120 V | 5 V rail only (~150 mA) | The compact extrusion exposes just a weak 5 V output, so Express boards and lighting demand a separate buck or the ADC adapter plus DC/DC combo.【F:knowledge/notes/input_part014_review.md†L140-L144】 | Pair the ADC board with an external step-down to feed 12 V lighting, and mount panel QS8 connectors to tidy high-current leads.【F:knowledge/notes/input_part014_review.md†L140-L145】 |
| MakerBase 75×/85×/X12 bridge | 3.3 V ADC, 5 V UART/Comm | Hall throttles must stay near 3.3 V; 5 V injection into ADCs burns STM32 inputs.【F:knowledge/notes/input_part013_review.md†L503-L505】【F:knowledge/notes/input_part013_review.md†L329-L329】 | Measure throttle min/max before connection; insert resistor ladders or shunt regulators if the lever exceeds 3.3 V.【F:knowledge/notes/input_part013_review.md†L503-L505】 |
| Any high-load build | External 12 V/20 A buck | Horns and compressors spike current; expect ≈4–6 A draw from a 60 V pack when heavily accessorised.【F:knowledge/notes/input_part013_review.md†L400-L401】 | Adjust controller battery limits to preserve BMS overhead; isolate horns on separate fuses or relays.【F:knowledge/notes/input_part013_review.md†L400-L401】 |

## Power Sequencing & Harness Safety
1. **Order matters on dual-rail harnesses.** Feeding 5 V into a Flipsky Smart Display before the 12 V lead repeatedly destroyed Spintend ADC daughterboards; always energise 12 V first, then 5 V, and confirm the display ground is shared with the controller.【F:knowledge/notes/input_part013_review.md†L366-L367】
2. **Map every connector before power-up.** MakerBase looms expose 3.3 V/GND/ADC1 at the “comm” header and reroute Bluetooth through the NRF pins; miswired TX/RX leads cause telemetry dropouts or back-power logic rails.【F:knowledge/notes/input_part013_review.md†L368-L368】
3. **Secure hall boards and sensor looms.** Hall PCBs that peel free can short against the rotor housing and mimic logic-rail failures; inspect adhesive and strain relief during reassembly.【F:knowledge/notes/input_part013_review.md†L603-L604】
4. **Exploit the ADC harness features.** Spintend’s ADC v3 board already supports spin dial throttles, dual-button pods, and turn-signal LED strips—plan channel assignments before closing the deck and keep phase leads equal length when trimming looms.【F:knowledge/notes/input_part014_review.md†L209-L210】
5. **Leverage CAN power sync sparingly.** Spintend 85-series controllers share a CAN power line, so a single button can wake both units once linked; treat it as a logic trigger and avoid stacking accessory loads on the shared feed.【F:knowledge/notes/input_part011_review.md†L19016-L19035】
6. **Use CAN headers for logic, not lighting.** Smart Repair’s harness can back-feed 5 V lights through the CAN plug, but riders add inline resistors and rely on the servo PWM pads when they need flashing indicators instead of constant-on lamps.【F:knowledge/notes/input_part012_review.md†L19323-L19405】
7. **Spec flexible signal looms.** Stem runs live longer with shielded multi-core RVVP cable (26–22 AWG) because the fine strands tolerate folding loads; builders reserve solid Ethernet leads for fixed sections or short jumper runs and terminate every spare pair so throttles cannot snap and pin controllers wide open.【F:knowledge/notes/input_part006_review.md†L32-L33】【F:knowledge/notes/input_part006_review.md†L405-L406】

### Deck-Mounted Accessory PCB Encapsulation
- Solder jumpers from the rear, lock trim pots, then flood the exposed component side with neutral-cure 704 silicone before sliding the board into an antistatic sleeve over foam so vibration cannot chafe leads against the deck.【F:knowledge/notes/input_part006_review.md†L399-L401】
- Pre-route accessory harnesses and strain-relief the sleeve so the cured silicone isn’t the only thing resisting motion when the scooter folds or flexes.【F:knowledge/notes/input_part006_review.md†L399-L401】

## CAN Dash & 5 V Rail Stabilization
- Prefer Vedder’s `code_server` when driving CAN dashboards; it retries frames up to five times and proved more reliable than `can-cmd`, provided you flip RX/TX wiring when moving from Flipsky to Ubox/Makerbase pinouts and flash the `slave_esc.lisp` script on every CAN slave.【F:knowledge/notes/input_part006_review.md†L18-L19】
- Makerbase dashboards that ran flawlessly on Flipsky crash on Spintend/UBOX swaps until both the BLE and dash harnesses have their RX/TX leads swapped to match the new controller pinout; once rewired, the legacy 6.0 scripts keep working on 6.02/6.2 firmware without ADC inputs.【F:knowledge/notes/input_part006_review.md†L19-L19】
- Cure persistent Makerbase dash reboots on Vsett conversions by adding ≈220 µF of bulk capacitance on the 5 V rail plus ~50 µF near the driver boards and by fixing stray pull-up resistors; the extra filtering stops brownouts during heavy phase-current spikes.【F:knowledge/notes/input_part006_review.md†L20-L20】
- Keep CAN bus termination at 120 Ω even on Zero 10X harness experiments—dropping to 100 Ω invited faults, and any burnt traces on the aluminum PCB should be replaced with fresh wiring or a dedicated antispark instead of solder-bridging damaged pads.【F:knowledge/notes/input_part006_review.md†L507-L507】
- When reusing Zero ALU-PCB assemblies, document the antispark conversion (loop-key vs. contactor), verify the new termination resistor with a meter, and retire the board outright if corrosion or lifted copper remains after cleaning; chasing intermittent CAN or ignition faults wastes more time than replacing the carrier.【F:knowledge/notes/input_part006_review.md†L507-L507】

## Display & Telemetry Options
- **SimpleVescDisplay (ESP32).** Smart Repair recommends flashing the open-source SimpleVescDisplay and 3D-printing its mount as a reliable alternative when Flipsky Voyage units glitch.【F:knowledge/notes/input_part013_review.md†L367-L367】
- **VESC-Express (ESP32-S3).** The €20 CAN↔BLE/Wi-Fi bridge adds LED or remote control outputs and modernises telemetry without touching fragile UART dongles.【F:knowledge/notes/input_part013_review.md†L418-L418】
- **VESC Express logging quirks.** Firmware 6.06 currently restarts SD logging every ~3 s and Spintend X12 rails only offer 5 V/150 mA, so power Express boards from a dedicated buck and stick to 6.05 (or plan CAN updates) until patches land.【F:knowledge/notes/input_part014_review.md†L5969-L6037】
- **Secondary UART headers.** When Voyage displays misbehave, moving telemetry to MakerBase’s TX2/RX2 header stabilised data without firmware changes; ensure extension leads are shielded if the replacements are short.【F:knowledge/notes/input_part013_review.md†L518-L518】
- **Stealth OEM casings.** Builders zip-tie TFT displays into stock dashboards or relocate them to auxiliary handlebars with 3D-printed mounts when they need legal-looking installs that still expose VESC telemetry.【F:knowledge/notes/input_part000_review.md†L45-L47】【F:knowledge/notes/input_part000_review.md†L57-L58】
- **Xiaomi M365 dashboards.** Run the community 6_05_adc branch on VESC 6.05 to fix braking/current bugs; GitHub may take a few minutes to publish binaries, so re-download if the patch doesn’t appear immediately.【F:knowledge/notes/input_part006_review.md†L109-L109】
- **Split CAN telemetry.** Dual-controller logs can show ~500 A phase on Voyage/Ambrosini dashboards even when each controller only pulls ~250 A—set per-controller CAN IDs or run dual sessions when you need wheel-specific diagnostics.[^per-controller]
- **Flipsky Voyage quirks.** G2 owners report the Voyage/Flipsky UART display only shows GPS speed even with correct wiring—plan for custom dash scripts or SmartDisplay integrations if you need richer telemetry.[^voyage]

## Accessory Load Planning Workflow
1. **Audit native rails.** Before paralleling dual 12 V outputs, verify continuity—builders suspect some Ubox taps share a single buck regulator, making combined 30 W loads risky.【F:knowledge/notes/input_part013_review.md†L547-L547】
2. **Decide external vs. onboard power.** If planned accessories exceed 3 A at 12 V or 150 mA at 5 V, route them through an external buck tied to the main battery with proper fusing rather than the controller rail.【F:knowledge/notes/input_part013_review.md†L360-L361】【F:knowledge/notes/input_part013_review.md†L430-L431】
3. **Preserve regen braking.** Disabling the BMS charge FET weakens regen—confirm the charge path is active before relying solely on motor braking for testing or street riding.【F:knowledge/notes/input_part013_review.md†L505-L505】
4. **Limit regen totals to pack capability.** When paralleling packs directly, match voltages and budget regen to the sum of both packs’ charge ratings; diode isolators caused throttle cut-outs on mismatched modules.【F:knowledge/notes/input_part013_review.md†L550-L552】
5. **Plan for 5 V-only controllers.** X12-class builds need a dedicated buck for anything beyond sensors—budget space for the converter alongside the ADC board and document wiring so the accessory rail stays within its ~150 mA ceiling.【F:knowledge/notes/input_part014_review.md†L140-L144】
6. **Offload heavy lighting on Nucular conversions.** Scooters running ≥60 W of lighting on Nucular controllers now dedicate an isolated auxiliary supply so the onboard DC/DC never trips or sags when fans, headlights, and strobes fire together.【F:knowledge/notes/input_part006_review.md†L484-L484】

## Lighting Hardware Spotlight
- **Offbondge projector upgrade.** Riders migrating from 1,300 lm compact beams report Offbondge’s 2,000–2,500 lm projector headlight slots straight into existing 12 V harnesses, spreads light without dazzling traffic, and still benefits from external bucks or fused rails on single-controller builds.【F:knowledge/notes/input_part005_review.md†L404-L404】【F:knowledge/notes/input_part005_review.md†L571-L571】
- **USB-C floodlight banks.** Commuters are trialling 3,000–9,000 lm rechargeable headlights that double as power banks and pair them with programmable LED tails or mirror-mounted 12 V lamps for better cutoff control than stock scooter beams.【F:knowledge/notes/input_part000_review.md†L47-L48】

## Addressable Lighting Integration
- Choose 12 V-friendly WS2815 or similar pixel strips so a single buck can feed both controller logic and the lighting rail without brownouts; mount strips in aluminum or polycarbonate channels to shed heat and protect silicone jackets from tire spray.【F:knowledge/notes/input_part006_review.md†L511-L511】
- Flash ESP32/WLED controllers with per-mode current caps, set boot presets that default to dim commuter profiles, and isolate the data line with a logic-level shifter when the strip sits far from the controller harness.【F:knowledge/notes/input_part006_review.md†L511-L511】
- Budget fusing and surge suppression—inline 3–5 A fuses plus TVS diodes on the buck output prevent decorative installs from collapsing the accessory rail when pixels short or moisture enters connectors.【F:knowledge/notes/input_part006_review.md†L511-L511】

## Wireless Security Hardening
- Mask the controller’s identity, enforce MAC filtering, and require PIN prompts so park-side pranksters cannot overwrite ride profiles while the scooter is unattended.【F:knowledge/notes/input_part006_review.md†L80-L80】【F:knowledge/notes/input_part006_review.md†L428-L429】
- Back Bluetooth hardening with keyed or NFC-switched power so even successful pairings cannot energise the controller without physical access.【F:knowledge/notes/input_part006_review.md†L80-L80】【F:knowledge/notes/input_part006_review.md†L428-L429】

## Commissioning Checklist
- Meter throttle outputs with the controller unpowered and confirm signal stays ≤3.3 V at full travel.【F:knowledge/notes/input_part013_review.md†L503-L505】
- Before flashing or editing parameters, follow the VESC Tool workflow—**Read → edit → Write**—to ensure current limits and accessory cut-offs persist after reboots.【F:knowledge/notes/input_part013_review.md†L542-L544】
- Log live current on accessory rails during first rides to validate that horns, lights, and pumps stay within regulator capacity; retune battery current if accessories share pack headroom with the controller.【F:knowledge/notes/input_part013_review.md†L400-L401】
- After harness work, perform continuity checks on 12 V outputs and confirm no sensor grounds are floating before closing the deck.【F:knowledge/notes/input_part013_review.md†L547-L547】【F:knowledge/notes/input_part013_review.md†L368-L368】

## Outstanding Documentation Needs
1. Publish a formal power-sequencing diagram for Flipsky and SimpleVescDisplay installs on Spintend/MakerBase hardware, including connector pinouts and ground references.【F:knowledge/notes/input_part013_review.md†L366-L368】
2. Capture tested fuse ratings and wire gauges for external 12 V bucks powering horns, lights, and air compressors so builders can size safety hardware confidently.【F:knowledge/notes/input_part013_review.md†L400-L401】
3. Verify whether Spintend’s Spinny/ADC v2 harness can safely source dual-function tail/brake lights or if relays are required, then publish the findings alongside rail current measurements.【F:knowledge/notes/input_part013_review.md†L430-L431】【F:knowledge/notes/input_part013_review.md†L548-L548】

## Source Notes
- Accessory rail limits, regen dependencies, and buck converter planning consolidate Smart Repair’s October 2025 integration notes covering Ubox rail continuity, 3.3 V throttle safety, CAN-powered lighting, and parallel-pack regen etiquette.【F:knowledge/notes/input_part013_review.md†L360-L552】【F:knowledge/notes/input_part012_review.md†L19323-L19405】
- Lighting hardware, accessory sourcing, and controller-rail constraints reflect the broader VESC Help Group coverage of Offbondge projector testing, Voyage/SmartDisplay integration, and Spinny harness current ceilings.【F:knowledge/notes/input_part005_review.md†L404-L571】【F:knowledge/notes/input_part014_review.md†L140-L144】
[^per-controller]: Voyage/Ambrosini dashboards can display ~500 A combined phase current on dual-controller builds, so configure per-controller CAN IDs or split sessions when you need wheel-specific telemetry.【F:knowledge/notes/input_part013_review.md†L186-L209】
[^voyage]: Voyage/Flipsky displays on Ninebot G2 builds have been limited to GPS-only readouts despite proper wiring, prompting teams to script custom dashboards or adopt SmartDisplay alternatives.【F:knowledge/notes/input_part014_review.md†L189-L189】
