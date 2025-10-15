# Motor Cooling & Thermal Management Notes

## Why Fans Rarely Help Scooter Hubs
- Denis Yurev reminded the workshop that scooters already move fresh air past the hub at riding speed, so bolt-on fan kits add little cooling compared with ensuring good heat transfer from the windings to the shell.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L422-L441】
- Riders debating CPU-style blowers learned that evaporation-driven skin cooling does not apply to dry aluminum shells; without a wet surface the only lever is temperature delta, so focus on conductive paths instead of add-on spinners.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L424-L441】
- Veterans recommended ferrofluid or oil-fill experiments (with leak safeguards) if you need real winding-to-shell transfer—simply drilling covers or gluing “windmills” to the hub only cools the outer case.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L456-L520】

## Controller Interface Refresh Checklist
- When raising voltage, replace Kapton tape with 0.5 mm thermal pads so MOSFETs stay isolated yet shed heat; stacking pads on top of Kapton just adds resistance.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L202-L223】
- Sand controller bases, clean MOSFET tabs, and reinstall paste before clamping the box—loose wiring under the plate prevents full contact and spikes temperatures on the first ride.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60020-L60025】
- Keep silicone pads on hand when chasing 48 V/15 S tunes; the crew pairs IRFB4110 MOSFETs with 100 V 1,000 µF and 47 µF capacitors and swaps pads plus paste before closing the case.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60009-L60024】
- Generic CPU thermal paste is still an acceptable stopgap for controller interfaces as long as the surfaces are cleaned before clamping, making it easy to refresh heat transfer when boutique compounds are out of stock.【F:data/vesc_help_group/text_slices/input_part009.txt†L1337-L1338】

## Controller Thermal Benchmarks (2024 field data)
- Spintend duals shed roughly half the heat of comparable Tronic stacks, yet riders still see 84100-class boxes climb near 180 A output, so external heatsinks and fresh thermal paste remain mandatory even on “efficient” ESCs.[^cooling-heat]
- Nucular 12-FET controllers clamped directly to aluminum decks held 210 A at ~48 °C, proving that rigid mounting pressure and broad contact area pay bigger dividends than exotic cooling loops.[^cooling-nucular]
- Summer endurance riders are even downsizing to 12-FET packages when leathers aren’t practical; Mirono now caps power on hot days to avoid rider overheating long before the hardware gives up.【F:knowledge/notes/input_part008_review.md†L22164-L22176】
- Treat thermal paste like a desktop CPU: the crew now refreshes paste and clears dust every ~24 months to keep MOSFET temperatures predictable before ramping up current again.[^cooling-maint]
- Single-drive NAMI builds on steep climbs still pushed lone Tronic 250 units toward 60 °C, while matched dual-drive riders on identical hardware hovered below 40 °C—shared load matters as much as controller selection.[^cooling-loadshare]
- Spintend’s aluminum six-FET controllers prefer a “sandwich” mount with 3–5 mm aluminum plates and paste on both sides; copper plates invite galvanic corrosion once everything is bolted to an aluminum deck.[^cooling-mount]
- Benur Lgl’s radiator-fed C350 race scooter held ~38.5 kW peaks and 850 A phase while keeping controllers near 55 °C by clamping the case to a finned aluminum enclosure with copper-backed Arctic Gel—evidence that rigid heat sinks beat ad-hoc fan kits even at race power levels.[^benur-c350]
- Ubox Alu Lite riders found the stock 5 mm thermal pads too insulative; swapping to thinner pads or straight paste dropped controller temps out of the 70 °C range and highlighted that the integrated heatpipes saturate quickly without low-impedance interfaces.[^ubox-lite-pads]
- Aluminum-core controller boards kept a 3.2 kW setup hovering near 29 °C, and `mxlemming` detection trims on 30 S gear cut case temps from ~80 °C to ~60 °C at ~150 A—though some racers abandoned the algorithm when it cost top speed on high-power hubs.【F:knowledge/notes/input_part008_review.md†L313-L313】
- Raphael’s race logs showed G300 controllers creeping toward 90 °C on hub motors that kept an R350 near 40 °C, reinforcing why riders favor C350/R350 aluminum PCBs over FR4 boards that can burn outright during MOSFET shorts.【F:knowledge/notes/input_part008_review.md†L375-L375】

## Temperature Guardrails
- Battery temps around 41 °C were deemed healthy for summer rides, but the group flagged ~60 °C as a ceiling—anything hotter accelerates degradation and calls for gentler tunes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60004-L60008】
- Larger packs and long shocks trap heat around the deck; riders re-bend frames, add inner/outer steel plates, and swap to lower-rate springs instead of trimming coils so the chassis and cells stop cooking each other.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L90030-L90136】
- Racing smaller hubs beyond 35 A battery now demands active cooling—10" PMT slick experiments leaned on ferrofluid, ice packs, and post-run cool-downs just to survive summer heats without cooking the stator.【F:knowledge/notes/input_part008_review.md†L22247-L22263】

## Coil Retention & Harness Dressing
- Inside hub motors, standard nylon cable ties survive stator temperatures when cinched correctly; some builders still wrap phases with cotton rope for redundancy, so combining both methods keeps windings tight without melting ties.【F:knowledge/notes/input_part014_review.md†L185-L185】

## Adhesives & Sensor Retention
- Hall sensors that walk out of their slots should be glued with heat-tolerant RTV 704 or slow-drying high-temp silicone; super glue works after scuffing the pocket but runs hotter under load.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131261-L131275】
- Keep 704 RTV on the bench for accessory wiring too—the same adhesive secures buck-converter leads so vibration cannot snap them before the scooter ever rolls out.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L31-L32】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131265-L131275】

## Motor Cleaning & Service
- Contaminated Bafang BBSHD mid-drives respond best to a compressed-air blast first, followed by brake cleaner or isopropyl alcohol applied sparingly with lint-free cloths so adhesives and magnet glue stay intact.[^cleaning-bbshd]
- Even fast-evaporating brake cleaner leaves residue—dry stators with compressed air and confirm windings aren’t left damp before resealing the case.[^cleaning-dry]

[^cooling-heat]: Builders noted Spintend controllers shedding roughly half the heat of Tronic units, yet 84100 boxes still climbed toward 180 A output without extra heatsinking or fresh thermal paste.【F:knowledge/notes/input_part008_review.md†L25-L25】
[^cooling-nucular]: Nucular 12-FET controllers clamped to deck aluminum sustained 210 A at approximately 48 °C thanks to robust MOSFETs and tight mounting pressure.【F:knowledge/notes/input_part008_review.md†L26-L26】
[^cooling-maint]: Community maintenance now mirrors desktop PC habits—reapply thermal paste and clean heatsinks every ~two years to stabilize controller temperatures.【F:knowledge/notes/input_part008_review.md†L27-L27】
[^cooling-loadshare]: Single-drive NAMI riders on steep climbs logged ~60 °C controller temps while dual-drive peers on matching hardware stayed below 40 °C, underscoring the value of shared load.[^cooling-heat][^cooling-nucular]【F:knowledge/notes/input_part008_review.md†L28-L28】
[^cooling-mount]: Spintend six-FET units run best when sandwiched against 3–5 mm aluminum plates with paste on both faces; copper spacers corrode faster once bolted into aluminum decks.【F:knowledge/notes/input_part008_review.md†L29-L29】
[^benur-c350]: Benur Lgl’s 20 S12 P C350 race build uses a finned aluminum radiator and copper-backed Arctic Gel interface to hold controller temps near 55 °C while pushing ~38.5 kW and 850 A phase.【F:knowledge/notes/input_part008_review.md†L17951-L17966】【F:knowledge/notes/input_part008_review.md†L17954-L17958】
[^ubox-lite-pads]: Ubox Alu Lite logs showed 5 mm thermal pads trapping heat; thinner pads or direct paste kept the case below 70 °C and underscored the limited capacity of the built-in heatpipes.【F:knowledge/notes/input_part008_review.md†L18030-L18075】
[^cleaning-bbshd]: Bafang BBSHD cleaning workflow of compressed air plus careful brake-cleaner/alcohol wipes preserves adhesives and magnet glue inside the mid-drive.【F:knowledge/notes/input_part008_review.md†L49-L50】
[^cleaning-dry]: Riders still dry stators with compressed air after brake-cleaner use so windings are not left damp before reassembly.【F:knowledge/notes/input_part008_review.md†L50-L51】
