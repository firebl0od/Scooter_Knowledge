# Ninebot G2 Max VESC Conversion Blueprint

## Build Objectives & Performance Targets

- **Stealth commuter spec:** Base conversion keeps the platform single-motor with a rear Q5 Evo hub, 20S 6P Molicel pack, and Magura MT7 brake with a Shimano Deore lever so the scooter stays nimble, wheelie-friendly, and outside DGT registration triggers while matching high-power peers for acceleration.[^1]
- **Road-legal mindset:** Builders are targeting legal-looking frames (e.g., Thunder 3 shells) and single-motor G2 layouts for Spanish compliance efforts, so conversion plans should preserve OEM lighting, horn, and indicator support where possible.[^2][^3]
- **80 km/h upgrade recipe:** Community checklists push rear spacing to ≈150 mm, grind the separator plate, install a 65 H 22×3 hub, and pair at least a 20 S 5–6 P 21700 pack with a robust VESC (e.g., Ubox 85/150) before chasing sustained highway speeds.[^4][^5]
- **Heavy-rider packaging:** Francois (≈140 kg, 2 m tall) is proving a Rage Mechanics recipe.
  - H60 rear motor, C350 controller, 20 S pack, and SmartDisplay-derived dash
  - can still fit a Max G2 deck when meticulously routed, making it the current benchmark for oversized riders who want to stay single-motor.[^6]

## Core Component Options

| Subsystem | Recommended Parts | Rationale |
| --- | --- | --- |
| Rear drive | Q5 Evo hub (primary), Lonnyo 65H 17×4 option via factory WhatsApp/website contact | Q5 Evo keeps steering light; Lonnyo 65H offers high-torque upgrade paths with direct factory support for wind customization.[^1][^7] |
| Suspension | Monorim fork with EXA air shock + all-new M6 fasteners | OEM bolts strip easily; swapping to quality hardware is mandatory when you add fork-mounted VESC wiring and brake torque.[^8] |
| Brakes | Magura MT7 caliper + Shimano Deore lever; optional 203 mm rotor spacer kit | Proven pairing on G2 conversions, with machining precedent for moto rotors if more thermal headroom is needed.[^1][^9] |
| Battery | Custom 20S 6P Molicel pack; drop-in 20S 3P EVE 50E module (JBD BMS) as interim | 6P target maximizes performance without registration; 20S 3P aftermarket pack fits with spacers for riders awaiting a weld slot.[^1][^10][^11] |
| Controller bridge | Smart Repair’s G2↔VESC CAN bridge (field-ready demo) | Enables retention of OEM controls/displays when migrating to dual VESC controllers.[^12][^13][^14] |

## Mechanical Preparation

1. **Swingarm & mudguard:** Reinstall the rear arm with two bolts, metal sleeves, and a 3D-printed mudguard support to restore stiffness after the harness swap, and budget longer swingarm bolts when fitting Lonnyo 80 H hubs so the caliper clears.[^15][^16]
2. **Dropout widening:** Stock rear spacing (~115 mm) can be stretched to ~150 mm by adding ~10 mm bushings and longer shoulder bolts while retaining OEM screws; choose softer bushing metals (copper/brass) so the frame tabs do not gall.[^17]

- **Exploit deck headroom:** The Max G2 deck hides extra space once you relocate the stock controller, letting you tuck external 20 S modules or triple-layer nickel bricks inside after grinding internal partitions for clearance.[^18]
3. **Cell packaging ceiling:** Expect ≈208 cylindrical cells before extensive deck surgery; plan your enclosure and harness routing before welding to avoid overcrowding the swingarm pivot area.[^19]
4. **Underbody protection:** Heavy-duty builds are fabricating CNC adapter plates plus a 10 mm steel skid to house 20S 5P Samsung 40T packs and larger Rage FH60 motors while preserving ground clearance and legal looks.[^20]
5. **Controller thermal path:** Lap a 50 × 100 × 10 mm aluminium plate between the frame and ESC with thermal paste after stripping paint; this keeps customer scooters below 50 °C even on steel chassis.[^21]

## Electrical Integration & Firmware Steps

- **ST-Link unlock workflow:** Derestricting or reusing the stock controller still hinges on ST-Link V2 access.
  - document pinout, backup, and flashing steps before lifting current limits to avoid bricking the OEM board.[^22][^23]
- **Bridge maturity:** Smart Repair’s bridge hardware is now demoed in the field, giving confidence that horn/indicator paths can be preserved; outstanding work includes publishing exact pinouts and firmware expectations for Flipsky dual stacks.[^24][^25][^14][^26]
- **Controller targets:** Riders prepping for the bridge are budgeting roughly 150–175 A battery and 250–300 A phase per controller, so plan CAN telemetry that exposes per-wheel data to avoid misreading aggregated currents.[^27][^28][^29]
- **XiaoDash unlocks without controller swaps:** Flash Denis’ XiaoDash build onto the stock G2 ESC, add the dashboard harness, and apply the SHFW Gen 4 patch to raise the speed ceiling while retaining blinkers and buzzer support.
  - no G30 controller transplant required.[^30]
- **Bridge maturity:** Smart Repair’s bridge hardware is now demoed in the field, giving confidence that horn/indicator paths can be preserved; outstanding work includes publishing exact pinouts and firmware expectations for Flipsky dual stacks.[^24][^25]
- **Controller targets:** Riders prepping for the bridge are budgeting roughly 150–175 A battery and 250–300 A phase per controller, so plan CAN telemetry that exposes per-wheel data to avoid misreading aggregated currents.[^27]
- **Harness power limits:** Remember that Tronic X12 logic rails only supply ~150 mA at 5 V; heavy accessories still require a dedicated buck when paired with G2 conversions to avoid brownouts.[^31][^32]
- **ADC safety:** Never feed 5 V into VESC ADC inputs.
  - stay on the 3.3 V rail when adapting OEM throttles and buttons from the G2 loom to prevent MCU damage.[^33]
- **Dash limitations:** Flipsky’s UART display still reports only GPS speed on G2 builds even when wired correctly.
  - budget time for custom dash scripts or SmartDisplay integration if you need richer telemetry.[^dash]

## Battery Architecture & Thermal Management

- **Pack options & delivery:** NKON’s popular cells can take a month to arrive, while Vapcell ships in 3–5 days but may require top-balancing mixed-voltage lots.
  - plan lead times and QA accordingly before freezing the build schedule.[^34]
- **Volume audits:** Jose’s crew is confirming 6P packaging fits by mock-building modules; Diego already proved 16 S works on the OEM controller after upgrading capacitors and is sizing the compartment for 18–20 S VESC hardware next.[^1][^35]
- **Reinforcement strategy:** When targeting street-legal yet high-discharge packs, fabricate skid plates and adapter brackets early so the added mass does not overstress the swingarm hardware.[^20][^19]
- **Thermal checks:** Pair the aluminium heat spreader with high-quality thermal paste and stripped paint surfaces; confirm temps after long pulls to validate the interface before sealing the deck.[^21]
- **Stock BMS telemetry envelope:** Expect roughly 33 A continuous discharge and brief ~44 A regen bursts when CAN comms stay intact.
  - use those ceilings when staging VESC limits so field-weakening pulls do not trip the pack.[^36][^37]
- Ninebot’s OEM packs cite IEC 62133-2 compliance, giving the stock modules a higher safety bar than generic Laotie-style batteries when you keep CAN comms intact.[^38]
- **Field-weakening guardrails:** Custom firmware running 60 A phase plus 35 A FW lifts top speed to ~35–40 km/h even with 140 kg riders, but stators peaked near 150 °C and ferrofluid overheated magnets.
  - budget temperature probes and cooling before leaning on FW for long pulls.[^39]

## Braking, Suspension & Ride Safety

- **Hybrid braking setups:** Some conversions lean on −90 A motor brake plus a front drum until displays arrive.
  - treat this as temporary and prioritise fitting the Magura MT7 hydraulic system for repeatable stops.[^40]
- **Rotor upgrades:** If you pursue 203 mm moto rotors, follow the community spacer blueprint that aligns Sur-Ron discs with Magura calipers to avoid pad taper and caliper rub.[^41]
- **Monitor arm fatigue:** Builders are already cracking stock G2 suspension arms under high-power loads; swap to reinforced forks or aftermarket arms if you plan to add a second 65H motor or daily heavy riders.[^42]
- **Retire Monorim hardware for high-power builds.** Community 80 km/h plans keep noting Monorim front ends bend, strip threads, and misalign under heavy hubs.
  - budget a speed fork or upgraded suspension before adding dual motors or moto-class brakes.[^43]
- **Headset service:** Clean any carbon paste overspill from the steering bearings; the paste can masquerade as a steering damper but eventually seizes the headset.[^44]

## Wiring & Regen Considerations

- **Parallel pack etiquette:** Match pack voltages and avoid ideal diodes.
  - the team observed throttle cut-outs on mismatched 17S/16S packs with diodes, while direct paralleling self-balances within ~1 A provided regen totals stay within combined pack capability.[^45]
- **Regen dependency:** Ensure the BMS charge FET is enabled; disabling it weakened regen braking until the charge channel was restored, a critical safety note for conversions that delay mechanical brake installs.[^46][^40]

## Outstanding Documentation Tasks

1. Publish the complete ST-Link flash checklist (pin mapping, firmware backup, voltage guardrails).[^23]
2. Release the Smart Repair bridge pinout plus compatibility matrix for Flipsky, Spintend, and MakerX controllers so horn/indicator circuits stay intact.[^47][^25]
3. Capture torque specs and torque-arm patterns for the dropout-widening bushings to standardise 150 mm conversions.[^48]
4. Document telemetry workflows that split per-controller CAN data for dual-drive G2 builds before riders push 300 A per wheel.[^27]

- Publish printable battery spacers and dash wiring workarounds now that stock accessories still limit displays to GPS-only readouts.[^49]
- Confirm whether bundled VESC Express boards enumerate cleanly.
  - Seven’s headers still require a separate CAN-connected module until firmware catches up, so capture the adapter wiring that G2 conversions will need.[^express_enum]

## Source Notes

- Single-motor conversion targets, component selections, mechanical packaging, and compliance considerations compile the 2025 Ninebot G2 Max threads covering Q5/Lonnyo motor choices, Monorim suspension, thermal plates, and legal stealth goals for Spanish riders.[^50][^51]
- Parallel-pack etiquette, regen dependencies, and Smart Repair bridge deliverables reflect the same review’s guidance on BMS charge-path requirements, CAN bridge readiness, and telemetry planning for high-current G2 builds.[^52][^53]
[^dash]: G2 owners report that Flipsky’s UART display only shows GPS speed despite correct wiring, pushing teams toward custom dash scripts or SmartDisplay swaps.[^49]
[^express_enum]: Seven’s bundled VESC Express board currently fails to enumerate; builders still rely on separate CAN-connected modules until firmware and header maps are patched.[^54][^55]


## References

[^1]: Source: knowledge/notes/input_part013_review.md†L350-L353
[^2]: Source: knowledge/notes/input_part013_review.md†L491-L492
[^3]: Source: knowledge/notes/input_part013_review.md†L349-L353
[^4]: Source: knowledge/notes/input_part011_review.md†L447-L448
[^5]: Source: knowledge/notes/input_part011_review.md†L18290-L18383
[^6]: Source: knowledge/notes/input_part011_review.md†L788-L796
[^7]: Source: knowledge/notes/input_part013_review.md†L357-L359
[^8]: Source: knowledge/notes/input_part013_review.md†L352-L353
[^9]: Source: knowledge/notes/input_part013_review.md†L160-L161
[^10]: Source: knowledge/notes/input_part013_review.md†L37-L38
[^11]: Source: knowledge/notes/input_part013_review.md†L96-L96
[^12]: Source: knowledge/notes/input_part013_review.md†L144-L144
[^13]: Source: knowledge/notes/input_part013_review.md†L506-L507
[^14]: Source: data/vesc_help_group/text_slices/input_part013.txt†L5620-L5621
[^15]: Source: knowledge/notes/input_part013_review.md†L42-L45
[^16]: Source: knowledge/notes/input_part011_review.md†L756-L757
[^17]: Source: knowledge/notes/input_part013_review.md†L355-L355
[^18]: Source: knowledge/notes/input_part005_review.md†L137-L137
[^19]: Source: knowledge/notes/input_part013_review.md†L354-L354
[^20]: Source: knowledge/notes/input_part013_review.md†L123-L123
[^21]: Source: knowledge/notes/input_part013_review.md†L606-L606
[^22]: Source: knowledge/notes/input_part013_review.md†L351-L351
[^23]: Source: knowledge/notes/input_part013_review.md†L609-L609
[^24]: Source: knowledge/notes/input_part013_review.md†L506-L508
[^25]: Source: knowledge/notes/input_part013_review.md†L516-L518
[^26]: Source: data/vesc_help_group/text_slices/input_part013.txt†L5627-L5634
[^27]: Source: knowledge/notes/input_part013_review.md†L507-L508
[^28]: Source: data/vesc_help_group/text_slices/input_part013.txt†L5655-L5658
[^29]: Source: data/vesc_help_group/text_slices/input_part013.txt†L6488-L6493
[^30]: Source: knowledge/notes/denis_all_part02_review.md†L114520-L114535
[^31]: Source: knowledge/notes/input_part013_review.md†L32-L33
[^32]: Source: knowledge/notes/input_part013_review.md†L360-L360
[^33]: Source: knowledge/notes/input_part013_review.md†L329-L329
[^34]: Source: knowledge/notes/input_part013_review.md†L55-L56
[^35]: Source: knowledge/notes/input_part013_review.md†L353-L353
[^36]: Source: knowledge/notes/input_part005_review.md†L138-L138
[^37]: Source: knowledge/notes/input_part005_review.md†L369-L369
[^38]: Source: knowledge/notes/input_part005_review.md†L139-L139
[^39]: Source: knowledge/notes/input_part005_review.md†L367-L368
[^40]: Source: knowledge/notes/input_part013_review.md†L163-L163
[^41]: Source: knowledge/notes/input_part013_review.md†L160-L160
[^42]: Source: knowledge/notes/input_part011_review.md†L713-L714
[^43]: Source: knowledge/notes/input_part011_review.md†L460-L461
[^44]: Source: knowledge/notes/input_part013_review.md†L194-L194
[^45]: Source: knowledge/notes/input_part013_review.md†L551-L552
[^46]: Source: knowledge/notes/input_part013_review.md†L505-L505
[^47]: Source: knowledge/notes/input_part013_review.md†L175-L177
[^48]: Source: knowledge/notes/input_part013_review.md†L618-L618
[^49]: Source: knowledge/notes/input_part014_review.md†L189-L189
[^50]: Source: knowledge/notes/input_part013_review.md†L123-L360
[^51]: Source: knowledge/notes/input_part013_review.md†L491-L609
[^52]: Source: knowledge/notes/input_part013_review.md†L505-L552
[^53]: Source: knowledge/notes/input_part013_review.md†L506-L618
[^54]: Source: knowledge/notes/input_part014_review.md†L146-L148
[^55]: Source: knowledge/notes/input_part014_review.md†L180-L180
