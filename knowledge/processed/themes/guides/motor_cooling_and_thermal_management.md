# Motor Cooling & Thermal Management Notes

## Why Fans Rarely Help Scooter Hubs
- Denis Yurev reminded the workshop that scooters already move fresh air past the hub at riding speed, so bolt-on fan kits add little cooling compared with ensuring good heat transfer from the windings to the shell.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L422-L441】
- Riders debating CPU-style blowers learned that evaporation-driven skin cooling does not apply to dry aluminum shells; without a wet surface the only lever is temperature delta, so focus on conductive paths instead of add-on spinners.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L424-L441】
- Veterans recommended ferrofluid or oil-fill experiments (with leak safeguards) if you need real winding-to-shell transfer—simply drilling covers or gluing “windmills” to the hub only cools the outer case.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L456-L520】
- Field logs continue to show that decorative deck fans and ad-hoc water loops stall immediately without serious thermal interfaces—properly clamping MOSFET plates to structural aluminum still beats gadget fans or hobby radiators.【F:knowledge/notes/input_part005_review.md†L249-L250】
- Open-face fans mounted over controller cutouts do almost nothing without a duct or exhaust path; in some cases they block the natural airstream, so plan sealed, pressure-rated blowers if you chase forced convection.【F:knowledge/notes/input_part005_review.md†L482-L485】

## Controller Interface Refresh Checklist
- When raising voltage, replace Kapton tape with 0.5 mm thermal pads so MOSFETs stay isolated yet shed heat; stacking pads on top of Kapton just adds resistance.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L202-L223】
- Sand controller bases, clean MOSFET tabs, and reinstall paste before clamping the box—loose wiring under the plate prevents full contact and spikes temperatures on the first ride.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60020-L60025】
- Keep silicone pads on hand when chasing 48 V/15 S tunes; the crew pairs IRFB4110 MOSFETs with 100 V 1,000 µF and 47 µF capacitors and swaps pads plus paste before closing the case.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60009-L60024】

## Heat Transfer Upgrades from VESC Field Logs
- Spintend dual-Ubox owners report the factory ships thermal pads (not paste) on MOSFET plates; lapping the deck and adding fresh paste keeps Laotie builds under ≈80 °C even on hard pulls.【F:knowledge/notes/input_part005_review.md†L113-L121】
- Epoxy putty doubles as a heat spreader around controller cases while builders embed thermistors through the existing hall harness and pot them with epoxy or silicone for direct winding contact.【F:knowledge/notes/input_part005_review.md†L115-L124】
- Resin-potted water-cooled Flipsky builds now ship with INA181 phase sensors and denser heatsinks, but veterans still expect MOSFET-to-heatsink contact to be the bottleneck until independent testing confirms the claimed improvements.【F:knowledge/notes/input_part005_review.md†L486-L488】

## Temperature Guardrails
- Battery temps around 41 °C were deemed healthy for summer rides, but the group flagged ~60 °C as a ceiling—anything hotter accelerates degradation and calls for gentler tunes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60004-L60008】
- Larger packs and long shocks trap heat around the deck; riders re-bend frames, add inner/outer steel plates, and swap to lower-rate springs instead of trimming coils so the chassis and cells stop cooking each other.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L90030-L90136】
- Cheap neodymium magnets lose strength around 80 °C while premium grades stretch toward 120 °C; enamel windings survive roughly 150 °C, so monitor stator temps and dose ferrofluid carefully to avoid dumping heat into magnet stacks during repeated 3 kW pulls.【F:knowledge/notes/input_part005_review.md†L236-L237】

## Coil Retention & Harness Dressing
- Inside hub motors, standard nylon cable ties survive stator temperatures when cinched correctly; some builders still wrap phases with cotton rope for redundancy, so combining both methods keeps windings tight without melting ties.【F:knowledge/notes/input_part014_review.md†L185-L185】

## Adhesives & Sensor Retention
- Hall sensors that walk out of their slots should be glued with heat-tolerant RTV 704 or slow-drying high-temp silicone; super glue works after scuffing the pocket but runs hotter under load.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131261-L131275】
- Keep 704 RTV on the bench for accessory wiring too—the same adhesive secures buck-converter leads so vibration cannot snap them before the scooter ever rolls out.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L31-L32】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131265-L131275】

## Hub Capability & Magnet Geometry Reality Check
- “5,600 W” Laotie hubs mirror Vsett hardware and only sustain ~1.2 kW continuous / 3 kW peak; 60 H/70 H race hubs hit 20–33 kW only in dual configurations with aggressive cooling and thick phase leads.【F:knowledge/notes/input_part005_review.md†L125-L132】
- Longer magnets and thicker stators both raise continuous power, but removable-rim Huameng hubs surrender iron volume versus 90 H LY motors that comfortably handle ~30 kW when run as a cooled pair.【F:knowledge/notes/input_part005_review.md†L126-L132】

## Sensor Calibration & Telemetry Sanity Checks
- Xiaodash custom firmware has shown 140 °C readings on Max G2 builds while the hub shell stayed hand-cool—treat suspect dash data as a calibration fault and verify against embedded NTC sensors.【F:knowledge/notes/input_part005_review.md†L168-L172】
- Expect stators to run ≈100 °C hotter than shells for minutes when ferrofluid is absent; wait for internal sensors to stabilise before trusting exterior touch tests on high-power pulls.【F:knowledge/notes/input_part005_review.md†L170-L172】
