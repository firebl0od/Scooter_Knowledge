# VESC Accessory Power & Display Integration Checklist

## Purpose
This guide distills field reports on powering lights, horns, and dashboards from aftermarket VESC controllers so builders avoid overloading regulator rails or frying logic accessories during swaps.

## Quick Reference Matrix
| Controller family | Native accessory rails | Verified limits & caveats | Recommended mitigations |
| --- | --- | --- | --- |
| Tronic X12 | 5 V logic (≈150 mA) | Rail cannot sustain heavy peripherals such as displays or fans without brownouts.【F:knowledge/notes/input_part013_review.md†L360-L361】 | Budget an external buck converter for any load above small sensors and throttle/gear switches.【F:knowledge/notes/input_part013_review.md†L360-L361】 |
| Spintend Ubox 85×/24× | 5 V logic, 12 V rail (rated 3 A) | Riders only trust the 12 V feed for a brake light; running both Dualtron headlight and taillight exceeded the regulator’s comfort zone.【F:knowledge/notes/input_part013_review.md†L430-L431】 | Keep lighting minimalist or offload to a dedicated buck; fuse each branch so single shorts do not collapse the regulator.【F:knowledge/notes/input_part013_review.md†L430-L431】 |
| MakerBase 75×/85×/X12 bridge | 3.3 V ADC, 5 V UART/Comm | Hall throttles must stay near 3.3 V; 5 V injection into ADCs burns STM32 inputs.【F:knowledge/notes/input_part013_review.md†L503-L505】【F:knowledge/notes/input_part013_review.md†L329-L329】 | Measure throttle min/max before connection; insert resistor ladders or shunt regulators if the lever exceeds 3.3 V.【F:knowledge/notes/input_part013_review.md†L503-L505】 |
| Any high-load build | External 12 V/20 A buck | Horns and compressors spike current; expect ≈4–6 A draw from a 60 V pack when heavily accessorised.【F:knowledge/notes/input_part013_review.md†L400-L401】 | Adjust controller battery limits to preserve BMS overhead; isolate horns on separate fuses or relays.【F:knowledge/notes/input_part013_review.md†L400-L401】 |

## Power Sequencing & Harness Safety
1. **Order matters on dual-rail harnesses.** Feeding 5 V into a Flipsky Smart Display before the 12 V lead repeatedly destroyed Spintend ADC daughterboards; always energise 12 V first, then 5 V, and confirm the display ground is shared with the controller.【F:knowledge/notes/input_part013_review.md†L366-L367】
2. **Map every connector before power-up.** MakerBase looms expose 3.3 V/GND/ADC1 at the “comm” header and reroute Bluetooth through the NRF pins; miswired TX/RX leads cause telemetry dropouts or back-power logic rails.【F:knowledge/notes/input_part013_review.md†L368-L368】
3. **Secure hall boards and sensor looms.** Hall PCBs that peel free can short against the rotor housing and mimic logic-rail failures; inspect adhesive and strain relief during reassembly.【F:knowledge/notes/input_part013_review.md†L603-L604】

## Display & Telemetry Options
- **SimpleVescDisplay (ESP32).** Smart Repair recommends flashing the open-source SimpleVescDisplay and 3D-printing its mount as a reliable alternative when Flipsky Voyage units glitch.【F:knowledge/notes/input_part013_review.md†L367-L367】
- **VESC-Express (ESP32-S3).** The €20 CAN↔BLE/Wi-Fi bridge adds LED or remote control outputs and modernises telemetry without touching fragile UART dongles.【F:knowledge/notes/input_part013_review.md†L418-L418】
- **Secondary UART headers.** When Voyage displays misbehave, moving telemetry to MakerBase’s TX2/RX2 header stabilised data without firmware changes; ensure extension leads are shielded if the replacements are short.【F:knowledge/notes/input_part013_review.md†L518-L518】

## Accessory Load Planning Workflow
1. **Audit native rails.** Before paralleling dual 12 V outputs, verify continuity—builders suspect some Ubox taps share a single buck regulator, making combined 30 W loads risky.【F:knowledge/notes/input_part013_review.md†L547-L547】
2. **Decide external vs. onboard power.** If planned accessories exceed 3 A at 12 V or 150 mA at 5 V, route them through an external buck tied to the main battery with proper fusing rather than the controller rail.【F:knowledge/notes/input_part013_review.md†L360-L361】【F:knowledge/notes/input_part013_review.md†L430-L431】
3. **Preserve regen braking.** Disabling the BMS charge FET weakens regen—confirm the charge path is active before relying solely on motor braking for testing or street riding.【F:knowledge/notes/input_part013_review.md†L505-L505】
4. **Limit regen totals to pack capability.** When paralleling packs directly, match voltages and budget regen to the sum of both packs’ charge ratings; diode isolators caused throttle cut-outs on mismatched modules.【F:knowledge/notes/input_part013_review.md†L550-L552】

## Lighting Hardware Spotlight
- **Offbondge projector upgrade.** Riders migrating from 1,300 lm compact beams report Offbondge’s 2,000–2,500 lm projector headlight slots straight into existing 12 V harnesses, spreads light without dazzling traffic, and still benefits from external bucks or fused rails on single-controller builds.【F:knowledge/notes/input_part005_review.md†L404-L404】【F:knowledge/notes/input_part005_review.md†L571-L571】

## Commissioning Checklist
- Meter throttle outputs with the controller unpowered and confirm signal stays ≤3.3 V at full travel.【F:knowledge/notes/input_part013_review.md†L503-L505】
- Before flashing or editing parameters, follow the VESC Tool workflow—**Read → edit → Write**—to ensure current limits and accessory cut-offs persist after reboots.【F:knowledge/notes/input_part013_review.md†L542-L544】
- Log live current on accessory rails during first rides to validate that horns, lights, and pumps stay within regulator capacity; retune battery current if accessories share pack headroom with the controller.【F:knowledge/notes/input_part013_review.md†L400-L401】
- After harness work, perform continuity checks on 12 V outputs and confirm no sensor grounds are floating before closing the deck.【F:knowledge/notes/input_part013_review.md†L547-L547】【F:knowledge/notes/input_part013_review.md†L368-L368】

## Outstanding Documentation Needs
1. Publish a formal power-sequencing diagram for Flipsky and SimpleVescDisplay installs on Spintend/MakerBase hardware, including connector pinouts and ground references.【F:knowledge/notes/input_part013_review.md†L366-L368】
2. Capture tested fuse ratings and wire gauges for external 12 V bucks powering horns, lights, and air compressors so builders can size safety hardware confidently.【F:knowledge/notes/input_part013_review.md†L400-L401】
3. Verify whether Spintend’s Spinny/ADC v2 harness can safely source dual-function tail/brake lights or if relays are required, then publish the findings alongside rail current measurements.【F:knowledge/notes/input_part013_review.md†L430-L431】【F:knowledge/notes/input_part013_review.md†L548-L548】
