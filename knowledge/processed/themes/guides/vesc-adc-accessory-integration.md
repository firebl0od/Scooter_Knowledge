# VESC ADC & Accessory Power Integration Playbook

## TL;DR
- Wire throttles, brakes, and regen controls straight into the controller’s ADC pins and keep everything on 3.3 V logic—dash adapters and 5 V accessories routinely add lag or kill channels when they fail.[^1][^2][^4]
- Treat the Spintend/MakerX auxiliary board as a low-current signal bridge: its ~12 V/3 A rail can light LEDs or run logic, but headlamps, horns, and pumps still need a dedicated DC/DC or relay-fed supply.[^3][^9][^10][^11]
- Map and validate every analog input inside VESC Tool before sealing the deck; enabling ADC control blocks bench FWD/REV overrides, so miswired harnesses must be fixed before ride testing.[^7][^8][^13]
- Protect logic rails by isolating accessory power, adding pull-down failsafes, and avoiding shared 5 V lines between controllers—shorts or ground loops keep blowing MOSFET drivers and display boards.[^14][^16][^17][^19]

## Signal & Power Budget Cheatsheet
| Channel | Voltage | Continuous Current | Typical Uses | Guardrails |
| --- | --- | --- | --- | --- |
| ADC1 / ADC2 (signal) | 3.3 V reference | ≈1 mA (input) | Throttle, brake, regen slider | Stay on 3.3 V hall outputs or add dividers/pull-downs so open circuits fall to zero.[^1][^4][^19] |
| Spintend ADC v3 accessory rail | 12 V (buck) | ≈3 A total | Tail lights, brake triggers, small relays | Parallel 18 W lamps already flirt with the limit—push heavier loads through an external converter.[^3][^10] |
| Controller logic rail | 5 V from onboard DC/DC | <0.5 A budget | Displays, hall sensors, footpads | Never back-feed from other controllers or dashes; a single short can blow the logic board.[^14][^16] |
| External DC/DC (recommended) | Pack → 12 V/5 V | Sized to load | Headlights, horns, pumps, fans | Use relays or MOSFETs triggered by the ADC board for safe switching.[^9][^11][^15] |

## Wiring Recipes
### Throttles & Brakes
1. **Direct hall wiring:** Route throttle and brake halls straight to ADC1/ADC2 signal, 3.3 V, and ground to keep control even when the OEM dash is removed.[^1] Keep the sensors on the controller’s 3.3 V rail—feeding 5 V halls directly into STM32 ADCs has already killed logic stages.【F:knowledge/notes/input_part000_review.md†L82-L84】
2. **Spin-Y & other multi-button throttles:** Version 1 units need custom JST‑1.0 leads into ADC2/COMM2; version 2 ships with a four-conductor harness that lands cleanly on the adapter board.[^2]
3. **Spintend adapter v3 harness:** Modern boards arrive with keyed plugs—no more screw terminals—so match the supplied loom instead of hand-crimping tiny JST shells.[^3]
4. **MakerX footpads & 3.3 V-only sensors:** Confirm both ADC rails output 3.3 V before blaming pads; swapping to 5 V kills the hall board.[^4]
5. **Interpret ADC counts, not raw voltage:** VESC Tool reports hall inputs as 0–4095 counts—track the delta between idle and full throw, and if readings compress, repeat the test with a stable 5 V source to rule out noisy 3.3 V regulators before replacing sensors; Spintend’s adapter manual expects ~0.8 V idle, so stop and rewire if a channel sits near 3 V.[^22][^adapter-idle]
6. **Filter noise in software first:** Builders tamed runaway triggers by compressing throttle activation to ~0.83–1.2 V inside VESC Tool rather than rewiring hardware; chassis grounding tricks have also helped but carry short-to-frame risk if insulation fails.[^adc-noise]
6. **Fail-safe defaults:** Add a pull-down resistor from throttle signal to ground so any broken wire snaps to zero instead of ghost acceleration.[^19]
7. **Legacy dash retention:** Leaving throttle through a dash adapter adds perceptible lag; many builders keep the dash for display only and wire throttles directly to the controller instead.[^20]
8. **Refresh mappings after downtime.** Scooters that sat for months have thrown false brake/throttle behaviour until riders reran the ADC wizard and removed stale inversion flags inside VESC Tool.[^storage-cal]
9. **Monitor brake sensors.** Dead brake halls make some VESC scooters pulse the motor every second or two under throttle, so replace failed sensors before ride testing.【F:knowledge/notes/input_part000_review.md†L39-L39】

### Regen Buttons & Variable Brakes
- **Momentary button recipe:** Wire the button between ADC2 signal and the 3.3 V rail; avoid series resistors because they created “stuck brake” faults in testing.[^6]
- **Analog lever mapping:** Run the ADC calibration wizard, keep the window open while sweeping the lever, then assign the channel to “Current (No Reverse)” so regen ramps in with negative motor/battery limits.[^7][^8]

### Lighting, Horns & Aux Loads
- **Use the adapter as logic, not power:** The horn output only sources a couple of amps—enough for low-power buzzers but not vintage 35 W halogens—so trigger a relay or MOSFET that pulls from a beefier DC/DC converter.[^9][^10]
- **85250 & Ubox installs:** Route brake-light logic through the ADC breakout, but feed lamps from a separate converter so you don’t brown out the controller when multiple 12 V loads fire at once.[^11]
- **TF100 & OEM switch pods:** Reuse factory throttles by landing the red/black hall power and the green signal lead on a 3.3 V ADC input; this preserves dash ergonomics without custom PCBs.[^12]
- **Skip illuminated combo pods:** Backlit handlebar switches feed accessory voltage into the signal lines and confuse the ADC board unless you gut the lighting—treat them as incompatible without a full rewire.[^24]
- **Avoid parasitic taps:** Pulling 12 V from internal headlight pins (e.g., X12) drags the logic rail and costs range—draw pack power into a dedicated converter instead.[^15]
- **Protect logic rails:** Shorting auxiliary leads straight on the controller board has already destroyed logic stages; isolate accessories and fuse every feed.[^16]
- **Fuse the adapter output:** One builder shorted the 12 V rail on a brand-new Spintend 85240 while wiring lights and killed the buck stage; add inline fuses or external bucks so a single mistake doesn’t scrap the controller.[^16][^23]
- **Treat buttons as triggers only:** The ADC adapter does not replace a loop key or smart-BMS latch; plan a real kill switch for theft deterrence or maintenance.[^17][^18]

## Configuration & Validation Workflow
1. **Bench prep:** Wire controls with the pack off, confirm continuity, and verify 3.3 V and 5 V rails before powering up.
2. **Calibrate ADC inputs:** In VESC Tool, run the ADC mapping wizard for each channel, noting min/max values and checking that neutral centers correctly.[^7]
3. **Assign app functions:** Map ADC1 to throttle, ADC2 to “Current No Reverse” for regen, and ensure throttle curves or safe-start options suit the rider.[^8]
4. **Understand bench limitations:** Once ADC control is enabled, the manual FWD/REV buttons in VESC Tool stop working—switch the app to UART or disable ADC temporarily for bench spins.[^13]
5. **Write configs explicitly:** Mobile reconnects and desktop wizards can wipe ADC settings unless you press “Write Motor Config” and “Write App Config” after every change.[^21]
6. **Log shakedowns:** Capture CAN or USB logs on the first rides to confirm commanded vs. actual current and verify regen ramps without triggering BMS cutoffs.[^11]

## Safety & Troubleshooting Checklist
- **Separate controller rails:** Do not tie CAN-connected controllers’ 5 V rails together unless they share the same ignition path; mismatched power buttons have already killed hardware.[^14]
- **Keep kill-switch redundancy:** Combine Safe Start, loop keys, and/or smart-BMS latches so thieves or techs can de-energise the scooter without relying on ADC buttons alone.[^17]
- **Watch for brownouts:** Builds that still depend on Makerbase/Flipsky rails should budget extra capacitance or buffer packs—the same rail that feeds ADC accessories is the one that dies during BMS trips.[^10]
- **If a channel dies:** Check for 3.3 V on the sensor, rerun ADC mapping, inspect JST orientation, and confirm the pull-down still measures the expected resistance.[^7][^19]

## Source Notes
[^1]: Routing throttle and brake halls directly into ADC1/ADC2 preserves control without the OEM dash.【F:knowledge/notes/input_part012_review.md†L11-L13】
[^2]: Spin Y throttle versions and wiring expectations for Spintend/Ubox adapters.【F:knowledge/notes/input_part007_review.md†L47-L47】
[^3]: Spintend v3 adapter now ships with keyed harness connectors.【F:knowledge/notes/input_part007_review.md†L221-L221】
[^4]: MakerX S100 footpads require the controller’s 3.3 V rail and fail on 5 V feeds.【F:knowledge/notes/input_part012_review.md†L255-L255】
[^6]: Regen button tied directly between ADC2 and 3.3 V without series resistors eliminated false braking faults.【F:knowledge/notes/input_part012_review.md†L13-L13】
[^7]: ADC calibration workflow and reminder to let VESC Tool find neutral before assigning functions.【F:knowledge/notes/input_part012_review.md†L93-L94】
[^8]: Regen mapping best practices from community quick-start guides.【F:knowledge/notes/input_part007_review.md†L239-L240】
[^9]: Horn output current limit cautions on Makerbase/Spintend harnesses.【F:knowledge/notes/input_part012_review.md†L97-L97】
[^10]: Spintend ADC aux outputs top out around 12 V / 3 A and need DC/DC help for bigger loads.【F:knowledge/notes/input_part005_review.md†L58-L58】
[^11]: Smart Repair’s 85250 guidance—use the ADC board for logic and a DC/DC converter for lamp current.【F:knowledge/notes/input_part012_review.md†L173-L173】
[^12]: TF100 throttle wiring recipe using the controller’s 3.3 V hall supply.【F:knowledge/notes/input_part012_review.md†L174-L174】
[^13]: Enabling ADC control disables manual FWD/REV overrides inside VESC Tool until you switch apps.【F:knowledge/notes/input_part012_review.md†L137-L137】
[^14]: CAN-linked controllers should not share 5 V rails; doing so has already killed boards.【F:knowledge/notes/input_part007_review.md†L226-L226】
[^15]: Drawing accessory power from the X12 headlight feed drags the logic rail and wastes energy.【F:knowledge/notes/input_part012_review.md†L395-L395】
[^16]: Shorting controller auxiliary leads has destroyed logic boards, proving the need for isolated accessory supplies.【F:knowledge/notes/input_part012_review.md†L248-L248】
[^17]: Builders still rely on loop keys, smart-BMS buttons, and Safe Start—ADC boards alone do not provide a true kill switch.【F:knowledge/notes/input_part005_review.md†L348-L350】
[^18]: Spintend’s ADC adapter v2 only ferries 5 V/12 V accessory power and cannot act as an anti-spark or ignition switch.【F:knowledge/notes/input_part005_review.md†L254-L254】
[^19]: Pull-down resistors on throttle lines guarantee a zero output if the signal wire opens.【F:knowledge/notes/input_part007_review.md†L223-L223】
[^20]: Routing throttle through dash adapters adds noticeable lag; direct ADC wiring restores responsiveness.【F:knowledge/notes/input_part007_review.md†L225-L225】
[^21]: VESC Tool can wipe ADC settings after reconnects unless you explicitly write both motor and app configs.【F:knowledge/notes/input_part005_review.md†L573-L573】
[^22]: Hall-diagnostics workflow focusing on ADC count deltas and re-testing with a clean 5 V rail when noisy 3.3 V supplies flatten readings.【F:knowledge/notes/input_part001_review.md†L15-L16】
[^23]: Shorting the Spintend 85240 aux rail to ground killed the unfused buck regulator, reinforcing the need for inline fuses or external converters when powering lighting from the adapter.【F:knowledge/notes/input_part011_review.md†L659-L660】
[^24]: Illuminated AliExpress switch pods leak voltage into ADC signal lines and require major rewiring to behave.【F:knowledge/notes/input_part010_review.md†L74-L77】
[^adc-noise]: Compressing throttle activation windows to ~0.83–1.2 V cleared ADC-trigger noise on Spintend builds; some riders grounded the chassis for extra stability but warn the practice risks shorts if insulation fails.【F:knowledge/notes/input_part014_review.md†L85-L86】
[^adapter-idle]: Spintend’s adapter manual targets ~0.8 V idle readings—seeing ~3 V idle means the channel is wired wrong and will act like a stuck brake.【F:knowledge/notes/input_part008_review.md†L21846-L21848】
[^storage-cal]: Re-running the ADC wizard and clearing stale inversion flags resolved Xiaomi brake/throttle glitches after long storage.【F:knowledge/notes/input_part011_review.md†L16211-L16217】

## Little FOCer & Compact Controller Specifics
- **Little FOCer throttles belong on 3.3 V.** Feeding ADC1 from 5 V left a Little FOCer scooter stuck at WOT; veterans reiterated that idle should sit around 0.6–0.9 V and WOT near 2.5–3.3 V, with halls staying on 5 V while the throttle uses the 3.3 V rail to protect the STM32 input.[^little_focer_3v3]

## VESC Latch & Key Switch Integration
- **Understand VESC latch quirks before wiring key switches.** The logic rail is live whenever the pack is connected, and tying the 5 V switch pin to ground turns the controller off—unlike Flipsky aluminums, which still need external contactors or BMS gating to avoid MOSFET stress.[^vesc_latch]

## ADC App Timeout Safeguards
- **ADC adapter placement and firmware safeguards.** Long throttle runs stayed quiet when riders mounted Spintend's ADC adapter beside the controller (or used shielded cable) and fed 5 V halls through resistor dividers; Vedder's mid-June patch now timeouts ADC-detach scripts so Xiaomi dash integrations can safely hand inputs back to hardware control.[^adc_timeout]

## Brake Light Wiring
- **Understand brake light output behavior.** One rider's 12 V tail lamp powered up via the ADC V2 adapter (ground/12 V/brake leads) but never entered brake mode, underscoring the need to clarify how the board sinks brake current and which firmware settings drive the output.[^brake_light_wiring]

## Source Notes (continued)
[^little_focer_3v3]: Little FOCer throttle voltage requirements and WOT prevention.【F:knowledge/notes/input_part004_review.md†L18-L18】【F:knowledge/notes/input_part004_review.md†L90-L90】
[^vesc_latch]: VESC latch behavior and key switch wiring considerations.【F:knowledge/notes/input_part004_review.md†L56-L56】
[^adc_timeout]: ADC adapter placement, shielding, and firmware timeout safeguards.【F:knowledge/notes/input_part004_review.md†L286-L286】
[^brake_light_wiring]: Brake light wiring confusion on ADC V2 adapter.【F:knowledge/notes/input_part004_review.md†L352-L352】
