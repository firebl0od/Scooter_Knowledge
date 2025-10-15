# Motor Cooling & Thermal Management Notes

## Why Fans Rarely Help Scooter Hubs
- Denis Yurev reminded the workshop that scooters already move fresh air past the hub at riding speed, so bolt-on fan kits add little cooling compared with ensuring good heat transfer from the windings to the shell.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L422-L441】
- Riders debating CPU-style blowers learned that evaporation-driven skin cooling does not apply to dry aluminum shells; without a wet surface the only lever is temperature delta, so focus on conductive paths instead of add-on spinners.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L424-L441】
- Veterans recommended ferrofluid or oil-fill experiments (with leak safeguards) if you need real winding-to-shell transfer—simply drilling covers or gluing “windmills” to the hub only cools the outer case.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L456-L520】

## Controller Interface Refresh Checklist
- When raising voltage, replace Kapton tape with 0.5 mm thermal pads so MOSFETs stay isolated yet shed heat; stacking pads on top of Kapton just adds resistance.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L202-L223】
- Sand controller bases, clean MOSFET tabs, and reinstall paste before clamping the box—loose wiring under the plate prevents full contact and spikes temperatures on the first ride.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60020-L60025】
- Keep silicone pads on hand when chasing 48 V/15 S tunes; the crew pairs IRFB4110 MOSFETs with 100 V 1,000 µF and 47 µF capacitors and swaps pads plus paste before closing the case.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60009-L60024】

## Temperature Guardrails
- Battery temps around 41 °C were deemed healthy for summer rides, but the group flagged ~60 °C as a ceiling—anything hotter accelerates degradation and calls for gentler tunes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60004-L60008】
- Larger packs and long shocks trap heat around the deck; riders re-bend frames, add inner/outer steel plates, and swap to lower-rate springs instead of trimming coils so the chassis and cells stop cooking each other.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L90030-L90136】

## Field Gauges & Coolant Debates
- Eduuuuuuuuu’s “ten-second touch test” remains a simple thermal sanity check—if you cannot keep a hand on the motor shell for ten seconds, drop phase amps before heat soaks the windings.【F:knowledge/notes/input_part013_review.md†L232-L233】
- Shlomozero’s 75 H 22/3 test hit ~80 °C within minutes at 400 A because undersized phase leads bottlenecked cooling; peers now hold the same hardware nearer 200–250 A motor current and treat 300 A uphill bursts as a winding death sentence.【F:data/vesc_help_group/text_slices/input_part013.txt†L9778-L9819】【F:data/vesc_help_group/text_slices/input_part013.txt†L10160-L10169】【F:data/vesc_help_group/text_slices/input_part013.txt†L10549-L10555】
- Arnau’s single-motor 75 H 22/3 setup stayed below 90 °C at 200 A phase once he swapped the thermistor pull-up to 100 kΩ, pairing a Ubox 240 with a 20 S 6 P P45B pack and ANT 450 A BMS—evidence that accurate sensing plus sane currents keep Daly-equipped commuters alive.【F:data/vesc_help_group/text_slices/input_part013.txt†L10221-L10248】
- Matthew continues to see ~30 °C drops within minutes when hubs get ≈4 ml of Statorade, but Haku cautions that sealing the air gap can overheat magnets—log magnet temps and weigh long-term wear before filling every race hub.【F:data/vesc_help_group/text_slices/input_part013.txt†L10299-L10309】
- Yamal’s dual 33/2 windings hold roughly 49–63 °C during hard pulls, proving so-called “speed” winds can still deliver torque when the pack and cooling strategy are dialed.【F:knowledge/notes/input_part013_review.md†L715-L715】

## Rotor & Magnet Integrity
- 7" LY 90 H hubs run a 127 mm stator with 40-magnet rotors, hitting noticeably harder than 110 mm-class cans but forcing builders onto matching 7" tire inventory and careful chassis clearance checks.【F:knowledge/notes/input_part013_review.md†L445-L445】
- Double-magnet 80 H stacks have twisted stators after 350–500 A assaults and 133–144 °C cores; Paolo warns lamination glue softens and magnets can demagnetise past ≈120 °C, so log temps and back current down before the damage becomes permanent.【F:knowledge/notes/input_part013_review.md†L446-L447】
- After pothole strikes at speed, Lonnyo/Shul race hubs that trip current or throw “voltage imbalance” faults should be torn down to inspect magnets, hall boards, and harness strain before the next run.【F:knowledge/notes/input_part013_review.md†L744-L767】

## Coil Retention & Harness Dressing
- Inside hub motors, standard nylon cable ties survive stator temperatures when cinched correctly; some builders still wrap phases with cotton rope for redundancy, so combining both methods keeps windings tight without melting ties.【F:knowledge/notes/input_part014_review.md†L185-L185】

## Adhesives & Sensor Retention
- Hall sensors that walk out of their slots should be glued with heat-tolerant RTV 704 or slow-drying high-temp silicone; super glue works after scuffing the pocket but runs hotter under load.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131261-L131275】
- Keep 704 RTV on the bench for accessory wiring too—the same adhesive secures buck-converter leads so vibration cannot snap them before the scooter ever rolls out.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L31-L32】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131265-L131275】
