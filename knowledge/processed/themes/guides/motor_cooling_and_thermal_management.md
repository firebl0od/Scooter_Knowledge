# Motor Cooling & Thermal Management Notes

## Why Fans Rarely Help Scooter Hubs
- Denis Yurev reminded the workshop that scooters already move fresh air past the hub at riding speed, so bolt-on fan kits add little cooling compared with ensuring good heat transfer from the windings to the shell.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L422-L441】
- Riders debating CPU-style blowers learned that evaporation-driven skin cooling does not apply to dry aluminum shells; without a wet surface the only lever is temperature delta, so focus on conductive paths instead of add-on spinners.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L424-L441】
- Veterans recommended ferrofluid or oil-fill experiments (with leak safeguards) if you need real winding-to-shell transfer—simply drilling covers or gluing “windmills” to the hub only cools the outer case.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L456-L520】

## Controller Interface Refresh Checklist
- When raising voltage, replace Kapton tape with 0.5 mm thermal pads so MOSFETs stay isolated yet shed heat; stacking pads on top of Kapton just adds resistance.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L202-L223】
- Sand controller bases, clean MOSFET tabs, and reinstall paste before clamping the box—loose wiring under the plate prevents full contact and spikes temperatures on the first ride.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60020-L60025】
- Keep silicone pads on hand when chasing 48 V/15 S tunes; the crew pairs IRFB4110 MOSFETs with 100 V 1,000 µF and 47 µF capacitors and swaps pads plus paste before closing the case.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60009-L60024】
- Paolo now favours thin Kapton plus paste on CNC-machined housings, reserving thick pads for rough castings, and slips washers under printed coolers so air can pass beneath dual-sided plates—the Laotie ES19 bolt pattern even matches Vsett 10 hubs for mirrored heatsinks.【F:knowledge/notes/input_part002_review.md†L356-L357】
- Dropping zero-vector frequency from 30 kHz to 20 kHz on an Inokim OX shaved roughly 30 °C off MOSFET temps while still holding 72 V/250–300 A pulls—treat PWM settings as another thermal lever before redesigning hardware.【F:data/vesc_help_group/text_slices/input_part002.txt†L13653-L13668】
- Treat mass-first cooling as the baseline. Riders still favour upsized heat spreaders or sabvoton-style cases over experimental water loops, and a billet aluminium cradle recently dropped case temps from 80 °C to 45 °C on the bench—yet without airflow or fins it merely stores heat instead of rejecting it.【F:knowledge/notes/input_part002_review.md†L54-L56】

## Thermal Interface Shootouts
- Hydronaut paste (≈14 W/m·K) and Alphacool/SARCON XR-m pads (≈17 W/m·K) beat commodity silicone sheets in back-to-back controller installs, while liquid-metal compounds stay off the list because they conduct electricity and corrode aluminium heatsinks.【F:knowledge/notes/input_part002_review.md†L213-L214】
- Arctic MX-4 class compounds continue to outlast bargain AliExpress paste; riders reopened controllers after weeks to find cheap grease dried out while MX-4 maintained contact pressure and cooling.【F:knowledge/notes/input_part002_review.md†L439-L439】
- Beryllium-oxide pastes push ~300 W/m·K but the toxicity makes them a non-starter for scooter builders; graphene pads promise 62 W/m·K yet prove brittle and eager to short components during clamping.【F:knowledge/notes/input_part002_review.md†L214-L215】
- Spintend’s stock pads continue to outperform ad-hoc swaps in the field, underscoring that contact pressure and installation technique matter as much as datasheet numbers when taming dual-Ubox temperatures.【F:knowledge/notes/input_part002_review.md†L215-L216】

## Temperature Guardrails
- Battery temps around 41 °C were deemed healthy for summer rides, but the group flagged ~60 °C as a ceiling—anything hotter accelerates degradation and calls for gentler tunes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60004-L60008】
- Larger packs and long shocks trap heat around the deck; riders re-bend frames, add inner/outer steel plates, and swap to lower-rate springs instead of trimming coils so the chassis and cells stop cooking each other.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L90030-L90136】

## Coil Retention & Harness Dressing
- Inside hub motors, standard nylon cable ties survive stator temperatures when cinched correctly; some builders still wrap phases with cotton rope for redundancy, so combining both methods keeps windings tight without melting ties.【F:knowledge/notes/input_part014_review.md†L185-L185】

## Adhesives & Sensor Retention
- Hall sensors that walk out of their slots should be glued with heat-tolerant RTV 704 or slow-drying high-temp silicone; super glue works after scuffing the pocket but runs hotter under load.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131261-L131275】
- Keep 704 RTV on the bench for accessory wiring too—the same adhesive secures buck-converter leads so vibration cannot snap them before the scooter ever rolls out.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L31-L32】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131265-L131275】

## Hub Fluid Experiments
- Filling stators with automatic transmission fluid sounded tempting for additional thermal mass, but veterans warned the cable gland and bearings would leak while ferrofluid remains the most controllable way to bridge the rotor air gap.【F:knowledge/notes/input_part002_review.md†L46-L47】
- Some riders are considering hybrid fills—ferrofluid near the magnet track topped with a thin ATF layer—yet the group is holding out for real-world temperature data before endorsing the experiment.【F:knowledge/notes/input_part002_review.md†L47-L48】
- Paolo drills vent holes in hub covers before applying ferrofluid but warns the compound must stay dry between refreshes—moisture hardens the fluid and ruins the stator, so bag wheels immediately after washing.【F:data/vesc_help_group/text_slices/input_part002.txt†L13748-L13758】
- Inject ferrofluid through the valve opening without pulling the wheel apart—the magnets wick it into the gap—and reseal the side cover with silicone once you’ve added the ~5 mL most scooter hubs actually need to avoid leaks.【F:knowledge/notes/input_part002_review.md†L626-L627】【F:knowledge/notes/input_part002_review.md†L667-L668】
- Overfilling (≈10–12 mL) only makes covers hotter; veterans cap fills around 5 mL and wipe any excess before buttoning the hub to keep decks clean.【F:knowledge/notes/input_part002_review.md†L667-L669】

## Hub Servicing Tactics
- Blade motor tear-downs now standardise on prying covers evenly, resealing with silicone, injecting ferrofluid through the magnet gap, and bracing the rim between your feet so the stator slides back without slamming parts together—plus Kapton over XT150 bullets to keep coolant off the joints.【F:knowledge/notes/input_part002_review.md†L444-L445】

## External Heatsink Experiments
- Mirono’s budget build wrapped low-cost PC heatsinks around a hub using thermal tape and four stainless-wire loops tightened 90° apart; the €30 mod held the VESC heatsink near 42 °C in 34 °C weather and proved the hub shell now tracks coil temps, confirming heat is leaving the stator efficiently.【F:knowledge/notes/input_part002_review.md†L230-L232】
- Riders compared the DIY approach to €135–€200 Turbinator kits and concluded the wired heatsinks offer a cost-effective stopgap while they wait for commercial restocks.【F:knowledge/notes/input_part002_review.md†L232-L232】
- Premium ferrofluids such as Statorade command about 10 % more than generic mixes, yet riders still pay the premium when it yields 15–30 % more continuous performance—especially on €200 hubs where the labour dwarfs the fluid cost.【F:knowledge/notes/input_part002_review.md†L241-L244】
- Carbon-fibre bodywork ideas keep surfacing—Kaabo builders are sketching new fenders, CNC spacers, and even heat-pipe arrays—but without direct MOSFET-to-baseplate contact these exotic shells barely outperform Spintend’s resin-filled layout.【F:data/vesc_help_group/text_slices/input_part002.txt†L9381-L9431】
- Even after potting controllers, adding deck-mounted clamps, and running heat pipes into thick aluminium plates, 220–250 A surges still blew dual-Ubox traces—airflow and external mounting remain mandatory on extreme builds.【F:knowledge/notes/input_part002_review.md†L357-L358】
- Vapor-chamber deck inserts with 30 cm heatpipes can hold controllers near ambient when ducted airflow passes across the fins, but they dump the heat into the battery plate and raise questions about low-cost heatpipe integrity.【F:knowledge/notes/input_part002_review.md†L641-L643】
- Builders are prototyping long CNC collars, industrial fins, and other hardware to rival Grin’s hubsinks; treat them as experiments until you log whether higher‑Kv motors actually run cooler under the same current.【F:knowledge/notes/input_part002_review.md†L699-L700】

## Controller Temperature Measurements
- Resin-encapsulated MOSFETs in some Ubox revisions bottleneck heat transfer because only thin PCB copper contacts the case, so expect hotter readings than Little FOCer or Tronic hardware that clamp directly to the FET tab.【F:knowledge/notes/input_part002_review.md†L272-L273】
- Handheld IR thermometers pointed at heatsinks routinely under-read junction temperature; expose FET surfaces or use higher-end thermal cameras before declaring a cooling experiment successful.【F:knowledge/notes/input_part002_review.md†L274-L274】
- Real-world logs show rewound single-motor builds can push TO-220 stages to ~96 °C even with CPU-style heatsinks and field weakening, and 14 kW single uBox pulls still end in fireworks when paper-insulated repairs substitute for real thermal mass—budget conservative current limits or redundant controllers for budget hardware.【F:knowledge/notes/input_part002_review.md†L426-L428】【F:knowledge/notes/input_part002_review.md†L476-L478】
