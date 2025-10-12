# Ninebot G2 Max VESC Conversion Blueprint

## Build Objectives & Performance Targets
- **Stealth commuter spec:** Base conversion keeps the platform single-motor with a rear Q5 Evo hub, 20S 6P Molicel pack, and Magura MT7 brake with a Shimano Deore lever so the scooter stays nimble, wheelie-friendly, and outside DGT registration triggers while matching high-power peers for acceleration.【F:knowledge/notes/input_part013_review.md†L350-L353】
- **Road-legal mindset:** Builders are targeting legal-looking frames (e.g., Thunder 3 shells) and single-motor G2 layouts for Spanish compliance efforts, so conversion plans should preserve OEM lighting, horn, and indicator support where possible.【F:knowledge/notes/input_part013_review.md†L491-L492】【F:knowledge/notes/input_part013_review.md†L349-L353】

## Core Component Options
| Subsystem | Recommended Parts | Rationale |
| --- | --- | --- |
| Rear drive | Q5 Evo hub (primary), Lonnyo 65H 17×4 option via factory WhatsApp/website contact | Q5 Evo keeps steering light; Lonnyo 65H offers high-torque upgrade paths with direct factory support for wind customization.【F:knowledge/notes/input_part013_review.md†L350-L353】【F:knowledge/notes/input_part013_review.md†L357-L359】 |
| Suspension | Monorim fork with EXA air shock + all-new M6 fasteners | OEM bolts strip easily; swapping to quality hardware is mandatory when you add fork-mounted VESC wiring and brake torque.【F:knowledge/notes/input_part013_review.md†L352-L353】 |
| Brakes | Magura MT7 caliper + Shimano Deore lever; optional 203 mm rotor spacer kit | Proven pairing on G2 conversions, with machining precedent for moto rotors if more thermal headroom is needed.【F:knowledge/notes/input_part013_review.md†L350-L353】【F:knowledge/notes/input_part013_review.md†L160-L161】 |
| Battery | Custom 20S 6P Molicel pack; drop-in 20S 3P EVE 50E module (JBD BMS) as interim | 6P target maximizes performance without registration; 20S 3P aftermarket pack fits with spacers for riders awaiting a weld slot.【F:knowledge/notes/input_part013_review.md†L350-L353】【F:knowledge/notes/input_part013_review.md†L37-L38】【F:knowledge/notes/input_part013_review.md†L96-L96】 |
| Controller bridge | Smart Repair’s G2↔VESC CAN bridge (field-ready demo) | Enables retention of OEM controls/displays when migrating to dual VESC controllers.【F:knowledge/notes/input_part013_review.md†L144-L144】【F:knowledge/notes/input_part013_review.md†L506-L507】 |

## Mechanical Preparation
1. **Swingarm & mudguard:** Reinstall the rear arm with two bolts, metal sleeves, and a 3D-printed mudguard support to restore stiffness after the harness swap.【F:knowledge/notes/input_part013_review.md†L42-L45】
2. **Dropout widening:** Stock rear spacing (~115 mm) can be stretched to ~150 mm by adding ~10 mm bushings and longer shoulder bolts while retaining OEM screws; choose softer bushing metals (copper/brass) so the frame tabs do not gall.【F:knowledge/notes/input_part013_review.md†L355-L355】
3. **Cell packaging ceiling:** Expect ≈208 cylindrical cells before extensive deck surgery; plan your enclosure and harness routing before welding to avoid overcrowding the swingarm pivot area.【F:knowledge/notes/input_part013_review.md†L354-L354】
4. **Underbody protection:** Heavy-duty builds are fabricating CNC adapter plates plus a 10 mm steel skid to house 20S 5P Samsung 40T packs and larger Rage FH60 motors while preserving ground clearance and legal looks.【F:knowledge/notes/input_part013_review.md†L123-L123】
5. **Controller thermal path:** Lap a 50 × 100 × 10 mm aluminium plate between the frame and ESC with thermal paste after stripping paint; this keeps customer scooters below 50 °C even on steel chassis.【F:knowledge/notes/input_part013_review.md†L606-L606】

## Electrical Integration & Firmware Steps
- **ST-Link unlock workflow:** Derestricting or reusing the stock controller still hinges on ST-Link V2 access—document pinout, backup, and flashing steps before lifting current limits to avoid bricking the OEM board.【F:knowledge/notes/input_part013_review.md†L351-L351】【F:knowledge/notes/input_part013_review.md†L609-L609】
- **Bridge maturity:** Smart Repair’s bridge hardware is now demoed in the field, giving confidence that horn/indicator paths can be preserved; outstanding work includes publishing exact pinouts and firmware expectations for Flipsky dual stacks.【F:knowledge/notes/input_part013_review.md†L506-L508】【F:knowledge/notes/input_part013_review.md†L516-L518】
- **Controller targets:** Riders prepping for the bridge are budgeting roughly 150–175 A battery and 250–300 A phase per controller, so plan CAN telemetry that exposes per-wheel data to avoid misreading aggregated currents.【F:knowledge/notes/input_part013_review.md†L507-L508】
- **Harness power limits:** Remember that Tronic X12 logic rails only supply ~150 mA at 5 V; heavy accessories still require a dedicated buck when paired with G2 conversions to avoid brownouts.【F:knowledge/notes/input_part013_review.md†L32-L33】【F:knowledge/notes/input_part013_review.md†L360-L360】
- **ADC safety:** Never feed 5 V into VESC ADC inputs—stay on the 3.3 V rail when adapting OEM throttles and buttons from the G2 loom to prevent MCU damage.【F:knowledge/notes/input_part013_review.md†L329-L329】

## Battery Architecture & Thermal Management
- **Pack options & delivery:** NKON’s popular cells can take a month to arrive, while Vapcell ships in 3–5 days but may require top-balancing mixed-voltage lots—plan lead times and QA accordingly before freezing the build schedule.【F:knowledge/notes/input_part013_review.md†L819-L1006】
- **Volume audits:** Jose’s crew is confirming 6P packaging fits by mock-building modules; Diego already proved 16 S works on the OEM controller after upgrading capacitors and is sizing the compartment for 18–20 S VESC hardware next.【F:knowledge/notes/input_part013_review.md†L350-L353】【F:knowledge/notes/input_part013_review.md†L353-L353】
- **Reinforcement strategy:** When targeting street-legal yet high-discharge packs, fabricate skid plates and adapter brackets early so the added mass does not overstress the swingarm hardware.【F:knowledge/notes/input_part013_review.md†L123-L123】【F:knowledge/notes/input_part013_review.md†L354-L354】
- **Thermal checks:** Pair the aluminium heat spreader with high-quality thermal paste and stripped paint surfaces; confirm temps after long pulls to validate the interface before sealing the deck.【F:knowledge/notes/input_part013_review.md†L606-L606】

## Braking, Suspension & Ride Safety
- **Hybrid braking setups:** Some conversions lean on −90 A motor brake plus a front drum until displays arrive—treat this as temporary and prioritise fitting the Magura MT7 hydraulic system for repeatable stops.【F:knowledge/notes/input_part013_review.md†L163-L163】
- **Rotor upgrades:** If you pursue 203 mm moto rotors, follow the community spacer blueprint that aligns Sur-Ron discs with Magura calipers to avoid pad taper and caliper rub.【F:knowledge/notes/input_part013_review.md†L160-L160】
- **Headset service:** Clean any carbon paste overspill from the steering bearings; the paste can masquerade as a steering damper but eventually seizes the headset.【F:knowledge/notes/input_part013_review.md†L194-L194】

## Wiring & Regen Considerations
- **Parallel pack etiquette:** Match pack voltages and avoid ideal diodes—the team observed throttle cut-outs on mismatched 17S/16S packs with diodes, while direct paralleling self-balances within ~1 A provided regen totals stay within combined pack capability.【F:knowledge/notes/input_part013_review.md†L551-L552】
- **Regen dependency:** Ensure the BMS charge FET is enabled; disabling it weakened regen braking until the charge channel was restored, a critical safety note for conversions that delay mechanical brake installs.【F:knowledge/notes/input_part013_review.md†L505-L505】【F:knowledge/notes/input_part013_review.md†L163-L163】

## Outstanding Documentation Tasks
1. Publish the complete ST-Link flash checklist (pin mapping, firmware backup, voltage guardrails).【F:knowledge/notes/input_part013_review.md†L609-L609】
2. Release the Smart Repair bridge pinout plus compatibility matrix for Flipsky, Spintend, and MakerX controllers so horn/indicator circuits stay intact.【F:knowledge/notes/input_part013_review.md†L175-L177】【F:knowledge/notes/input_part013_review.md†L516-L518】
3. Capture torque specs and torque-arm patterns for the dropout-widening bushings to standardise 150 mm conversions.【F:knowledge/notes/input_part013_review.md†L618-L618】
4. Document telemetry workflows that split per-controller CAN data for dual-drive G2 builds before riders push 300 A per wheel.【F:knowledge/notes/input_part013_review.md†L507-L508】
