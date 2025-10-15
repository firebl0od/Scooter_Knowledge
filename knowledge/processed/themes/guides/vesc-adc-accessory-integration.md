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
2. **Clamp 5 V inputs.** Xiaomi/Boosted-style throttles swing ≈0.8–4.1 V from a 5 V rail; drop them through a 1 kΩ/2 kΩ divider or use the ADC adapter so the STM32 never sees more than 3.3 V.[^voltage-divider]
2. **Match lever logic.** Magura’s MT5e ships in normally-closed (2700985) and normally-open (2700984) variants, and the Spintend ADC board can flip between switch and hall sensing with onboard toggles plus 5 V/3.3 V selection—confirm the lever SKU before crimping harnesses.[^25]
3. **Spin-Y & other multi-button throttles:** Version 1 units need custom JST‑1.0 leads into ADC2/COMM2; version 2 ships with a four-conductor harness that lands cleanly on the adapter board.[^2]
3. **Spintend adapter v3 harness:** Modern boards arrive with keyed plugs—no more screw terminals—so match the supplied loom instead of hand-crimping tiny JST shells.[^3]
4. **MakerX footpads & 3.3 V-only sensors:** Confirm both ADC rails output 3.3 V before blaming pads; swapping to 5 V kills the hall board.[^4]
5. **Interpret ADC counts, not raw voltage:** VESC Tool reports hall inputs as 0–4095 counts—track the delta between idle and full throw, and if readings compress, repeat the test with a stable 5 V source to rule out noisy 3.3 V regulators before replacing sensors; Spintend’s adapter manual expects ~0.8 V idle, so stop and rewire if a channel sits near 3 V.[^22][^adapter-idle]
6. **Filter noise in software first:** Builders tamed runaway triggers by compressing throttle activation to ~0.83–1.2 V inside VESC Tool rather than rewiring hardware; chassis grounding tricks have also helped but carry short-to-frame risk if insulation fails.[^adc-noise]
7. **Shield noisy looms.** Running ADC throttles and SmartDisplay UART over shielded cable tied to controller ground cleared 120 A jitter, and separating signal bundles from phase wires kept FOC noise out of high-amp Ubox builds.[^signal-shield]
8. **Fail-safe defaults:** Add a pull-down resistor from throttle signal to ground so any broken wire snaps to zero instead of ghost acceleration.[^19]
9. **Legacy dash retention:** Leaving throttle through a dash adapter adds perceptible lag; many builders keep the dash for display only and wire throttles directly to the controller instead.[^20]
10. **Refresh mappings after downtime.** Scooters that sat for months have thrown false brake/throttle behaviour until riders reran the ADC wizard and removed stale inversion flags inside VESC Tool.[^storage-cal]
11. **Monitor brake sensors.** Dead brake halls make some VESC scooters pulse the motor every second or two under throttle, so replace failed sensors before ride testing.【F:knowledge/notes/input_part000_review.md†L39-L39】
12. **Keep hall brakes separate.** Do not tie two hall levers to one ADC input—floating outputs land at different voltages and can latch regen; dedicate one channel per lever and leave the spare brake mechanical if you run out of inputs.【F:knowledge/notes/input_part000_review.md†L335-L337】

### Regen Buttons & Variable Brakes
- **Momentary button recipe:** Wire the button between ADC2 signal and the 3.3 V rail; avoid series resistors because they created “stuck brake” faults in testing.[^6]
- **Analog lever mapping:** Run the ADC calibration wizard, keep the window open while sweeping the lever, then assign the channel to “Current (No Reverse)” so regen ramps in with negative motor/battery limits.[^7][^8]
- **Hall-based levers:** Pair Xiaomi hall levers or custom SS49E + magnet housings with the SmartDisplay/ADC board to unlock proportional braking—digital on/off microswitches pulse the motor and feel unnatural once regen replaces cable brakes.[^analog-halls]
- **Hydraulic mix-and-match:** When swapping Ninebot G30 front levers, move the factory hall sensor and magnet into the hydraulic body so proportional regen survives the upgrade.[^ninebot-hall]
- **Scroll-wheel throttles:** Thumbwheel throttles work well as dedicated regen controls—Mirono’s Ubox build runs ~80 A phase / 15 A battery for a smooth 47 km/h eco mode while still craving BLDC punch at launch.【F:data/vesc_help_group/text_slices/input_part000.txt†L17625-L17654】【F:data/vesc_help_group/text_slices/input_part000.txt†L18388-L18395】
- **Front-only caution:** Riders running “Shigura” hybrids keep front regen low or disabled; abrupt ramps can lock a lightly loaded front tyre on wet pavement.[^26]
- **Boosted Rev mapping:** Expect ≈1.6 V full brake, 2.54 V neutral, and 3.3 V wide open on Boosted Rev thumbwheels once mapped to VESC ADC inputs, delivering strong regen with minimal mechanical braking.[^boosted-map]

### Lighting, Horns & Aux Loads
- **Use the adapter as logic, not power:** The horn output only sources a couple of amps—enough for low-power buzzers but not vintage 35 W halogens—so trigger a relay or MOSFET that pulls from a beefier DC/DC converter.[^9][^10]
- **85250 & Ubox installs:** Route brake-light logic through the ADC breakout, but feed lamps from a separate converter so you don’t brown out the controller when multiple 12 V loads fire at once.[^11]
- **TF100 & OEM switch pods:** Reuse factory throttles by landing the red/black hall power and the green signal lead on a 3.3 V ADC input; this preserves dash ergonomics without custom PCBs.[^12]
- **Skip illuminated combo pods:** Backlit handlebar switches feed accessory voltage into the signal lines and confuse the ADC board unless you gut the lighting—treat them as incompatible without a full rewire.[^24]
- **Avoid parasitic taps:** Pulling 12 V from internal headlight pins (e.g., X12) drags the logic rail and costs range—draw pack power into a dedicated converter instead.[^15]
- **Protect logic rails:** Shorting auxiliary leads straight on the controller board has already destroyed logic stages; isolate accessories and fuse every feed.[^16]
- **Fuse the adapter output:** One builder shorted the 12 V rail on a brand-new Spintend 85240 while wiring lights and killed the buck stage; add inline fuses or external bucks so a single mistake doesn’t scrap the controller.[^16][^23]
- **Treat buttons as triggers only:** The ADC adapter does not replace a loop key or smart-BMS latch; plan a real kill switch for theft deterrence or maintenance.[^17][^18]
- **Leverage DAC outputs.** Spintend 75/300 firmware can repurpose the PPM pin into a DAC brake-light feed, but expect to lean on community firmware drops until official docs land.[^31]

## Configuration & Validation Workflow
1. **Bench prep:** Wire controls with the pack off, confirm continuity, and verify 3.3 V and 5 V rails before powering up.
2. **Calibrate ADC inputs:** In VESC Tool, run the ADC mapping wizard for each channel, noting min/max values and checking that neutral centers correctly.[^7]
3. **Assign app functions:** Map ADC1 to throttle, ADC2 to “Current No Reverse” for regen, and ensure throttle curves or safe-start options suit the rider.[^8]
4. **Understand bench limitations:** Once ADC control is enabled, the manual FWD/REV buttons in VESC Tool stop working—switch the app to UART or disable ADC temporarily for bench spins.[^13]
5. **Write configs explicitly:** Mobile reconnects and desktop wizards can wipe ADC settings unless you press “Write Motor Config” and “Write App Config” after every change.[^21]
6. **Log shakedowns:** Capture CAN or USB logs on the first rides to confirm commanded vs. actual current and verify regen ramps without triggering BMS cutoffs.[^11]

## Safety & Troubleshooting Checklist
- **Separate controller rails:** Do not tie CAN-connected controllers’ 5 V rails together unless they share the same ignition path; mismatched power buttons have already killed hardware.[^14]
- **Disconnect before rewiring.** Builders keep blowing ADC daughterboards by hot-plugging throttles and accessories—always kill the battery before touching the harness or you’ll spike converters despite heat-shrink and shielding.【F:data/vesc_help_group/text_slices/input_part000.txt†L18335-L18382】【F:data/vesc_help_group/text_slices/input_part000.txt†L18423-L18444】
- **Seat the adapter switches before testing.** If the Spintend board reads erratically, confirm the 5 V/3.3 V selector and NO/NC toggles are firmly latched, then bypass the board with the controller’s 3.3 V rail only for short diagnostic sweeps—full travel on 5 V sensors while direct-wired has already killed modules.【F:knowledge/notes/input_part000_review.md†L707-L715】【F:knowledge/notes/input_part000_review.md†L748-L748】
- **Keep kill-switch redundancy:** Combine Safe Start, loop keys, and/or smart-BMS latches so thieves or techs can de-energise the scooter without relying on ADC buttons alone.[^17]
- **Watch for brownouts:** Builds that still depend on Makerbase/Flipsky rails should budget extra capacitance or buffer packs—the same rail that feeds ADC accessories is the one that dies during BMS trips.[^10]
- **If a channel dies:** Check for 3.3 V on the sensor, rerun ADC mapping, inspect JST orientation, and confirm the pull-down still measures the expected resistance.[^7][^19]
- **Bypass the adapter when debugging.** When the external ADC module starts spitting nonsense, feed 3.3 V, signal, and ground straight from the controller to the throttle/brake to prove the harness—just never slam 5 V accessories onto the STM32’s 3.3 V rail during the test.【F:knowledge/notes/input_part000_review.md†L648-L648】
- **Clamp high-voltage throttles.** MiniMotors EYE triggers swing ≈0.8–4.1 V from a 5 V rail—drop a resistor divider or use the ADC adapter before landing them on STM32 pins.[^28]
- **Mind mixed levers.** Xiaomi hall brakes share 5 V/GND safely, but paralleling them with normally-open Magura hydraulics leaves floating signals unless you add a hall puck to the hydraulic lever.[^32]
- **One lever, one channel.** Sharing an ADC input between hall levers leaves each at a different float voltage and creates stuck-brake faults—wire them independently or drop the extra hall.[^hall-split]

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
[^analog-halls]: Hall-based brake levers (Xiaomi or custom SS49E builds) let SmartDisplay/ADC boards blend braking force; digital microswitch levers pulse the motor instead of delivering progressive regen.【F:knowledge/notes/input_part000_review.md†L113-L113】
[^25]: Magura MT5e lever SKU guidance plus Spintend ADC toggle support for normally-open or normally-closed brake sensors.【F:knowledge/notes/input_part000_review.md†L206-L206】
[^26]: Riders debating “Shigura” hybrids warned that front-only regen should be limited or disabled to avoid low-traction lockups.[^25][^rev-cite]
[^27]: Shielded ADC and UART looms tied to controller ground eliminated 120 A cruise-control jitter and reduced FOC noise on Ubox builds.[^signal-shield]
[^28]: MiniMotors Eye throttles output ≈0.8–4.1 V from a 5 V rail, so dividers or adapter boards must clamp the signal below 3.3 V.[^signal-clamp]
[^29]: Boosted Rev thumbwheel voltage map delivering strong regen without relying on mechanical brakes.[^boosted-map]
[^30]: Ninebot builders move the stock hall sensor and magnet into aftermarket levers to keep proportional regen with hydraulic fronts.[^ninebot-hall]
[^31]: Spintend 75/300 firmware can remap the PPM pin into a DAC-driven brake light even though official documentation is still pending.【F:knowledge/notes/input_part000_review.md†L297-L297】
[^32]: Xiaomi hall levers coexist on 5 V/GND rails, but pairing them directly with normally-open Magura hydraulics leaves floating signals until a hall puck is added.[^signal-clamp]
[^voltage-divider]: Xiaomi-style throttles and levers output ≈0.8–4.1 V from a 5 V rail, so builders add 1 kΩ/2 kΩ dividers or the ADC adapter to clamp signals under 3.3 V before landing on STM32 pins.【F:knowledge/notes/input_part000_review.md†L335-L336】
[^hall-split]: Hall brake handles float at different voltages when paralleled—dedicate one ADC channel per lever and leave the spare brake mechanical if you run out of inputs.【F:knowledge/notes/input_part000_review.md†L335-L337】
[^signal-shield]: Running shielded control looms tied to controller ground and routed away from phase wires removed 120 A jitter on Spintend Ubox installs.【F:knowledge/notes/input_part000_review.md†L258-L258】
[^signal-clamp]: MiniMotors throttle voltage span and Xiaomi/Magura compatibility lessons shared during ADC integration deep dives.【F:knowledge/notes/input_part000_review.md†L259-L259】【F:knowledge/notes/input_part000_review.md†L299-L299】
[^boosted-map]: Boosted Rev ADC readings (~1.6 V brake to 3.3 V WOT) that yield strong regen and reduced reliance on mechanical brakes.【F:knowledge/notes/input_part000_review.md†L246-L246】
[^ninebot-hall]: Ninebot G30 builders transplant the OEM hall puck and magnet into new levers to preserve proportional regen after hydraulic upgrades.【F:knowledge/notes/input_part000_review.md†L296-L296】
[^rev-cite]: Shimano Saint + Magura hybrid discussions cautioning against aggressive front regen on low-traction surfaces.【F:knowledge/notes/input_part000_review.md†L207-L207】
