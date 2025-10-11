# input_part010.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part010.txt`
- Coverage: 2024-10-27 21:20:42 through 2024-12-17 09:08:46 (lines 6700-20200)
- Latest addition: lines 18701-20200 (2024-12-09T17:54:05 through 2024-12-17T09:08:46)
- Next starting point: line 20201 (2024-12-17T09:08:46 and later)

## Key Findings

### Brake Rotor Sourcing Updates (lines 18701-18712)
- Yamal and 🇪🇸AYO#74 double down on the solid 3 mm “Wolf” discs from AliExpress, noting they’re non-floating despite the two-piece look, cost about €30 each online versus €80‑100 in shops, and have survived where riveted rotors sheared under braking, so riders buy spares in sets of four.【F:data/vesc_help_group/text_slices/input_part010.txt†L18701-L18712】

### Cell Projects & Chemistry Comparisons (lines 18727-18765, 19893-20022)
- Jerome is assembling a 20S9P pack with EVE 40P cells, ultimately favoring them for lower internal resistance and colder-weather output even after Patrick praised Bak 45D’s higher discharge ceiling over Molicel P45B; 40PL is deemed overkill for the target build.【F:data/vesc_help_group/text_slices/input_part010.txt†L18727-L18741】
- Patrick’s 30 S single-motor ambitions lean on Samsung 40T only because customs complicate EVE imports, while his Lonnyo 16×4 hub plans include wiring both ends so he can swap between star and delta to chase 120 km/h when voltage and cells allow.【F:data/vesc_help_group/text_slices/input_part010.txt†L19893-L20028】

### Assembly & Spot-Welding Guidance (lines 18743-18997)
- GABE’s struggle to solder nickel to cells drew a reminder to avoid the “hack” altogether—light sanding is a last resort—while Jerome now outsources welding to a 24 kW capacitor-based rig after tossing two overheated packs, underscoring the risk of DIY copper work without proper gear.【F:data/vesc_help_group/text_slices/input_part010.txt†L18743-L18766】
- The crew’s welding physics debate reiterates that amp delivery (≈1 kA pulses) and sufficient voltage to overcome joint resistance matter more than headline kW ratings when joining steel or copper, aligning with Paolo’s Ohm’s-law caution.【F:data/vesc_help_group/text_slices/input_part010.txt†L18982-L19024】

### Heatsink & Thermal Planning (lines 19035-20157)
- Noname’s 9×12‑inch heatsink experiment suggests mounting dual VESCs beneath a shared plate is viable because thermal-paste losses are minor relative to the fin area, provided builders find deck space for the bulk.【F:data/vesc_help_group/text_slices/input_part010.txt†L19035-L19044】
- Later in the week Noname reports keeping a single VESC under ~40 °C at 6 kW with thermal pads and paste, aiming to add ram-air ducting, while haku’s hardware still peaks near 70 °C—useful real-world benchmarks for cooling goals.【F:data/vesc_help_group/text_slices/input_part010.txt†L20140-L20158】

### Safe Parameter Targets for G30 + Vsett Builds (lines 19045-19864)
- Shlomozero advises that the Vsett 1400 W hub tolerates far more than 55 A phase and suggests capping battery current around 25 A based on the BMS, while ‘lekrsu’ flags that Christophe’s regen brake was effectively disabled in his shared profile; Christophe settled on 130 A motor and 45 A battery limits to keep his Spintend 85 V swap reliable at ~50 km/h cruise speeds.【F:data/vesc_help_group/text_slices/input_part010.txt†L19045-L19067】【F:data/vesc_help_group/text_slices/input_part010.txt†L19864-L19864】

### High-Voltage Controller Plans & Supply (lines 19876-19933)
- Rage Mechanics confirmed haku’s new “22 S-capable” powerstage came from Raphael Fujiguara, with Yamal noting the RFP shop also replaces MOSFETs and supporting components to survive 22 S abuse—haku will still shake it down on 20 S before chasing the 30 kW targets the crew now treats as the new benchmark.【F:data/vesc_help_group/text_slices/input_part010.txt†L19876-L19933】

### Motor & Controller Procurement Notes (lines 19507-20022)
- Noname surfaced an LY/LONNYO 11‑inch hub catalog spanning 60‑120 V and up to 6 kW, while 🇪🇸AYO#74 learned that some 2024 Dualtron Storm Limited runs quietly upgraded to 70 H stators despite 60 H listings, reinforcing the need to confirm windings before purchase.【F:data/vesc_help_group/text_slices/input_part010.txt†L19507-L19518】
- Patrick’s Lonnyo swap experiences highlight that the stock Vsett motor overheats with sustained 45‑50 km/h runs, whereas the 16×4 Lonnyo’s 110 mm stator and 65 mm magnets stay cool on climbs albeit with lower top speed until he experiments with a 22×3 tire or delta wiring.【F:data/vesc_help_group/text_slices/input_part010.txt†L20021-L20028】

### Battery Current & Pack Management (lines 19921-19942)
- Haku’s 20 S12 P Molicel P42A pack routinely runs 250 A battery and 300 A phase with a 520 A BMS cutoff, prompting reminders that such peaks demand large parallel counts to hold highway loads without sag or overheating.【F:data/vesc_help_group/text_slices/input_part010.txt†L19921-L19942】

### Controller Packaging Strategies for Tight Decks (lines 20034-20062)
- Purp’s hall-less Mantis 10 conversion planning shows single Ubox/Spintend modules (~58 mm wide) can be stood on edge along the frame or split between floor and lid, with Noname suggesting foam or 3D-printed dummies to test fit and cautioning that screw mounting becomes the bottleneck in the cramped controller bay.【F:data/vesc_help_group/text_slices/input_part010.txt†L20034-L20062】

### ANT BMS App Access (lines 19869-19873)
- ‘lekrsu’ confirmed the ANT BMS companion is simply on Apple’s App Store, so iPhone-using friends can configure packs without sideloading tools.【F:data/vesc_help_group/text_slices/input_part010.txt†L19869-L19873】

### Nami Controller Voltage Experiments (lines 19994-20108)
- 🇪🇸AYO#74 is testing whether 72 V Nami controllers will run on a homemade 60 V pack by rewiring phase leads, underscoring a gap in verified down-voltage operation data for that platform.【F:data/vesc_help_group/text_slices/input_part010.txt†L19994-L20108】

### Dualtron Thunder Conversion Planning (lines 20185-20199)
- Shlomozero is prepping dual Dualtron Thunder builds with VESC control and a 72 V/36 Ah (8 C) Powerpacks battery, and Yamal urges documenting controller-bay dimensions plus verifying the stock 60 H hubs’ 4 mm phase leads before parts orders are finalized.【F:data/vesc_help_group/text_slices/input_part010.txt†L20185-L20199】

### Logistics, Displays & Firmware Access (lines 17340-17360)
- Spintend’s ExpressLine DDP orders are taking roughly a week to hit Germany, but riders should budget for additional import duties even on “duty paid” invoices.【F:data/vesc_help_group/text_slices/input_part010.txt†L17340-L17348】
- 🇪🇸AYO#74 is sharing the Nami LCD screen files privately while ✨🇪🇸عمر compiles an 84 V firmware build; a €2 CH340 USB-TTL dongle let him bypass an €80 PAS-removal fee when flashing the Eye 3/Eye 4 displays for VESC use.【F:data/vesc_help_group/text_slices/input_part010.txt†L17351-L17360】

### Controller Capability & Voltage Limits (lines 17364-17435)
- Face de Pin Sucé reports the C350 V4 hardware moved to low-side shunts and 12 FET packs that tolerate ~500 A absolute / 400 A phase, clarifying why the label still lists 200 A battery but seasoned tuners lean on the higher phase ceiling.【F:data/vesc_help_group/text_slices/input_part010.txt†L17364-L17397】【F:data/vesc_help_group/text_slices/input_part010.txt†L17405-L17406】
- Max Rainlogix pegs Flipsky 84100 controllers around 60 A battery continuous (≈100-series) and 84200 units near 150 A before FET reliability nosedives, so chasing more current requires stepping up to Spintend 85-series hardware.【F:data/vesc_help_group/text_slices/input_part010.txt†L17460-L17471】
- Pandalgns warned that 60 V Laotie/J&P square-wave controllers cap out around 19 S—20 S “go boom”—and suggested Damao-branded 72 V boxes when builders need cheap 20 S support instead of gambling on stock electronics.【F:data/vesc_help_group/text_slices/input_part010.txt†L17410-L17422】
- 🇪🇸AYO#74’s wheelie attempts show VESC traction control can still lift the front under heavy torque, so tuning slip limits remains essential on high-power builds.【F:data/vesc_help_group/text_slices/input_part010.txt†L17434-L17435】

### High-Power Single-Motor Lessons (lines 17480-17538)
- Jan’s 12 kW single-motor scooter hit ~62 km/h without field weakening but tried to loop out from a standstill, reinforcing that >8 kW rear-wheel builds demand extreme chassis control or a switch to dual motors.【F:data/vesc_help_group/text_slices/input_part010.txt†L17480-L17512】
- Patrick and Jan note that chasing 100 km/h on a 20 S single requires large 16×4–22×3 hubs plus heavy field weakening or star/delta switching, yet packaging relays/FET boards and preserving efficiency make dual Vsett 10+ hubs the safer upgrade path.【F:data/vesc_help_group/text_slices/input_part010.txt†L17492-L17524】【F:data/vesc_help_group/text_slices/input_part010.txt†L17533-L17545】

### Hub Cooling & Motor Design Debates (lines 17547-17612)
- The crew agreed that adding internal fins or covers barely helps because hub motors are still air-gapped from the case; Jan argues that only water-cool quick-connects or full mid-drive swaps meaningfully shed heat while keeping the motor sealed.【F:data/vesc_help_group/text_slices/input_part010.txt†L17547-L17612】
- Builders keep eyeing mid-drives to cut unsprung mass, but they concede chains/belts complicate packaging on scooter frames, so premium hubs remain the practical compromise for now.【F:data/vesc_help_group/text_slices/input_part010.txt†L17602-L17612】

### Pack Architecture Cautions (lines 17769-17797)
- Z’s Apollo Phantom plan to stack two 14 S packs in series drew warnings: Paolo insists on building dual 28 S 5 P packs with separate BMSs to avoid series mismatch faults, pointing to ANT units when high-current 28 S hardware is needed.【F:data/vesc_help_group/text_slices/input_part010.txt†L17769-L17797】

### Fast-Charging & Charger Procurement (lines 17819-17899)
- A 95 A EV-charger demo sparked reminders that Samsung 40T/Molicel P42A packs stay healthiest near 1 C; a 20 S6 P would already pull ~6.3 kW and needs dedicated EV infrastructure plus careful thermal monitoring.【F:data/vesc_help_group/text_slices/input_part010.txt†L17819-L17844】
- Noname cataloged AliExpress telecom-derived chargers—about US$340 for a 60 A Huawei unit or US$260 for a touchscreen 50 A model—while noting they’re simply modified rectifiers despite factory-style marketing.【F:data/vesc_help_group/text_slices/input_part010.txt†L17847-L17899】

### Ride Data, Instrumentation & Wheel Calibration (lines 17863-18310)
- 🇪🇸AYO#74’s Nami runs hit GPS-indicated ~140 km/h on 70H motors fed by Molicel P45B packs, but he’s cross-checking with relive.cc because GoPro GPro GPS struggled in tunnels.【F:data/vesc_help_group/text_slices/input_part010.txt†L17863-L17875】【F:data/vesc_help_group/text_slices/input_part010.txt†L18295-L18298】
- Face de Pin Sucé logged a Fardriver-powered 22 S9 P Samsung 50S / LY 75H setup hitting 140 km/h, adding another benchmark for hyper-scooter gearing.【F:data/vesc_help_group/text_slices/input_part010.txt†L18008-L18010】
- Correcting wheel diameter from 271 mm to 279.4 mm tightened 🇪🇸AYO#74’s speed telemetry, highlighting how a few millimeters of tire OD drift can skew GPS/odometer comparisons.【F:data/vesc_help_group/text_slices/input_part010.txt†L18305-L18310】

### Parameter Tuning & Diagnostics (lines 18012-18052)
- 🇪🇸AYO#74 cured persistent motor vibration by cutting detected inductance from ~22.5 µH to 16–17 µH and re-running VSS sensorless tuning; the VESC mobile app stores backups, letting iPhone users restore experiments without a laptop.【F:data/vesc_help_group/text_slices/input_part010.txt†L18012-L18052】

### Tooling, Wiring & Conductor Limits (lines 18070-18158)
- ✨🇪🇸عمر’s copper-capable spot-welder build runs off a 5 S 1 P, 20 Ah, 200 A-rated Li-ion pack harvested from an industrial battery, providing a template for mobile copper welding setups.【F:data/vesc_help_group/text_slices/input_part010.txt†L18070-L18082】
- Cable debates reaffirmed that silicone 12 AWG can stomach ~100 A for short bursts while 8 AWG claims of 300–400 A continuous are fantasy—temperature rise, insulation, and bundle routing dictate safe limits more than tables suggest.【F:data/vesc_help_group/text_slices/input_part010.txt†L18149-L18158】【F:data/vesc_help_group/text_slices/input_part010.txt†L18362-L18363】

### Brake & Rotor Considerations (lines 18163-18700)
- Apo cautioned that motorcycle Brembo calipers demand thick rotors and extra clearance most scooter forks lack; premium bicycle systems (Magura, etc.) remain the realistic upgrade path until frames adopt moto-style mounts.【F:data/vesc_help_group/text_slices/input_part010.txt†L18163-L18174】
- Yamal dislikes floating bicycle rotors on e-scooters despite their looks, implying riders should stick with proven solid discs for consistent bite.【F:data/vesc_help_group/text_slices/input_part010.txt†L18694-L18700】

### Tire Setup & Wheel Service (lines 18202-18262)
- Seating stubborn 10-inch beads often needs a ratchet strap, soap or window cleaner, and >100 psi bursts; cheaply molded tires can still leave paper-width gaps that require repeated lubricant/pressure cycles to seal.【F:data/vesc_help_group/text_slices/input_part010.txt†L18202-L18224】
- Riders remain split on tubeless versus tubes: tubeless with sealant offers puncture resilience for long routes, but some still slip tubes into tubeless rims for easier roadside fixes despite the added heat risk.【F:data/vesc_help_group/text_slices/input_part010.txt†L18228-L18262】

### Charging & BMS Management (lines 18321-18363)
- Yamal watches cell swing during top-offs, letting the pack rest an hour before low-current balancing with the 2.8 A OEM charger, while 🇪🇸AYO#74 recommends limiting equalization to 2–4 A and tightening BMS drift thresholds near 0.01 V to stop perpetual micro-charging.【F:data/vesc_help_group/text_slices/input_part010.txt†L18321-L18363】

### Pitbike & Mini-Moto Platforms (lines 18331-18345)
- Generic 48 V/1.5 kW mini bikes now ship with small Fardriver controllers that accept parameter edits, giving builders a 72 V-ready base without immediately swapping electronics.【F:data/vesc_help_group/text_slices/input_part010.txt†L18331-L18345】

### High-Voltage Ambitions & QS Sourcing (lines 14201-14242)
- Jason is preparing to push 5–7 kW through his platform and experiment with a 30S arrangement by chaining three Segway 10S packs, underscoring the appetite for hobby-grade 30S scooters once ESC capability and battery supply align.【F:data/vesc_help_group/text_slices/input_part010.txt†L14222-L14236】
- Pandalgns surfaced a 72 V, 15 kW QS-motor scooter listing, confirming that turnkey high-power drivetrains are accessible on AliExpress for builders who would rather buy than rewind their own hubs.【F:data/vesc_help_group/text_slices/input_part010.txt†L14239-L14242】

### G30 Fabrication & Pack Layout Updates (lines 14254-14263)
- GABE is reprinting his G30 structural pieces in 100 % PETG and stacking Kapton–copper layers so every conductor stays on the top side of the pack, adding a plastic isolation sheet to protect the wraparound bus bars inside the tight deck tolerances.【F:data/vesc_help_group/text_slices/input_part010.txt†L14254-L14263】

### Nami Platform Benchmarks (lines 14269-14285)
- 🇪🇸AYO#74 noted that the Nami 28 Ah trim keeps 1 000 W motors, while the 32–40 Ah versions step up to 1 500 W hubs, and his crew is now chasing 35–40 kW combined output—useful power targets when selecting factory configurations for future VESC swaps.【F:data/vesc_help_group/text_slices/input_part010.txt†L14269-L14285】

### Tire Fitment & Mini BMX Conversion Planning (lines 14299-15075)
- Noname reminded Haku that the 6.5″ rim on his mini-bike hub will accept 10″ tires, but to wait for the frame before buying rubber to verify real clearance around the dropouts.【F:data/vesc_help_group/text_slices/input_part010.txt†L14299-L14306】
- To shrink the contact patch, the group pointed to 10×3.0-6.5 tires and calculated that the stock 11″ pattern measures roughly 4.10″ wide on a 4″ rim, helping size slimmer replacements for narrow stays.【F:data/vesc_help_group/text_slices/input_part010.txt†L14700-L14756】
- Haku ultimately measured that his new frame needs another 10–15 mm of dropout width and may either widen the forks or switch to dual 10″ LY 65H motors with 125 mm axles, showing the packaging compromises behind “Peak G30 v2” conversions.【F:data/vesc_help_group/text_slices/input_part010.txt†L15065-L15075】
- When stripping powder-coated mini-BMX frames for battery mounts, Noname recommended chemical stripper, sanding, or heat to clear decals without gouging the tubing.【F:data/vesc_help_group/text_slices/input_part010.txt†L14960-L14982】

### Motor Rewire & Harness Guidance (lines 14418-14762)
- Shlomozero’s Zero 10X upgrade thread confirmed you can reuse existing phase leads but should add a fresh hall harness, follow color order, and drop in a temperature sensor while the motor is open to avoid future rewinds.【F:data/vesc_help_group/text_slices/input_part010.txt†L14440-L14461】
- NetworkDir benchmarked that short 4 mm phase leads tolerate about 50 A battery and 120 A phase current, framing realistic limits for Mantis/Wolf-class motors.【F:data/vesc_help_group/text_slices/input_part010.txt†L14418-L14429】
- Pandalgns reported running 12 AWG silicone wire on 60H hubs (and 16 AWG on 1 kW motors) while the group debated switching to metric mm² sizing, capturing common cable choices for 3 kW-class scooters.【F:data/vesc_help_group/text_slices/input_part010.txt†L14745-L14762】

### Halo T107 Loom Management (lines 14499-14509)
- Pandalgns drafted a Halo T107 extender that isolates the battery bay from control wiring and adds pass-throughs for phase, hall, brake, dash, and charger leads, effectively giving the frame Dualtron-style service access.【F:data/vesc_help_group/text_slices/input_part010.txt†L14499-L14509】

### Diagnostics & Noise Troubleshooting (lines 14507-14573)
- After Yamal heard scraping from his front motor, 🇪🇸AYO#74 warned that deviating from the Ortega dash can upset the tune, and the group ultimately traced the metallic rattle to a vibrating phone mount—saving an unnecessary teardown.【F:data/vesc_help_group/text_slices/input_part010.txt†L14507-L14573】

### IMU Wheelie Control Limitations (lines 14510-14521)
- Noname cautioned that VESC’s IMU always chases level, so trying to enable “wheelie mode” mid-stunt would yank the bike upright unless you start at the exact angle, limiting its usefulness on small-stator scooters without custom logic.【F:data/vesc_help_group/text_slices/input_part010.txt†L14510-L14521】

### GT2 Telemetry & Thermal Guardrails (lines 14550-14588)
- Jerome’s Segway GT2 log showed dual Spintend 85150s at 60 A battery / 150 A phase each with 30 A field weakening on a 19S9P EVE 50E pack, noting the cells are the bottleneck until a higher-output battery is built.【F:data/vesc_help_group/text_slices/input_part010.txt†L14550-L14565】
- Patrick advised setting battery BMS cutoffs near 75 °C (80 °C max) and reassured riders that a well-designed ESC will ride through those events without damage, countering fears that a thermal trip will “kill” the controller.【F:data/vesc_help_group/text_slices/input_part010.txt†L14580-L14592】

### Copper Busbars & Pack Safety (lines 14870-14959)
- GABE’s wraparound-cell 20/22S2P pack keeps every conductor on the top deck, but he nearly overheated the copper bridges during welding, prompting reminders to anneal or otherwise manage heat when working with thin PETG carriers.【F:data/vesc_help_group/text_slices/input_part010.txt†L14870-L14959】

### Display Ecosystem & SmartDisplay Options (lines 15083-15253)
- Rage Mechanics added a web-based theme editor and live theme switching to SmartDisplay, fueling demand for CAN dashboards on dual-VESC scooters.【F:data/vesc_help_group/text_slices/input_part010.txt†L15083-L15090】
- Face de Pin Sucé justified the €500 price by enumerating differentiators—GPS navigation, CAN/UART expansion for lighting and BMS, tyre-pressure support, offline/online telemetry, DAC-based throttle calibration, CNC housing, and more—setting expectations for premium clusters.【F:data/vesc_help_group/text_slices/input_part010.txt†L15244-L15253】
- For cheaper instrumentation, ✨🇪🇸عمر highlighted the U.S.-made RTV display as a VESC-only option while others reminded builders that even a spare phone can still serve as a budget dash.【F:data/vesc_help_group/text_slices/input_part010.txt†L15219-L15222】【F:data/vesc_help_group/text_slices/input_part010.txt†L15217-L15218】

### Controller Reliability & Replacement Strategies (lines 15100-15295)
- David’s 74 V bench test blew the DC-link caps on his Flipsky, leading the group to recommend Nichicon replacements, raising the ADC low end to ~0.2 V to tame throttle chatter, and relocating capacitors with pigtails when the aluminum shell blocks clearance.【F:data/vesc_help_group/text_slices/input_part010.txt†L15100-L15140】
- Builders warned that Flipsky QC remains inconsistent and suggested sourcing Spintend 85150/85250 controllers—often via @jamessoderstrom—instead of buying another 75200 for LY rear or OX front motors.【F:data/vesc_help_group/text_slices/input_part010.txt†L15272-L15295】

### Throttle Recommendations (lines 15349-15365)
- ✨🇪🇸عمر praised the Spin-Y2 throttle on his Xiaomi build, while Haku linked a $3 AliExpress thumb throttle that has survived duty on his son’s Peak G30, giving both premium and budget upgrade paths.【F:data/vesc_help_group/text_slices/input_part010.txt†L15349-L15365】

### Thick Copper Busbars & 40PL Pack Builds (lines 15663-15699)
- Rosheee is running a 20S6P Samsung 40PL pack from @jamessoderstrom and is now sourcing 0.3 mm copper busbars for future 26S experiments, noting that James’ conservative limits keep the GT2 safe even when riders crave “send it” performance.【F:data/vesc_help_group/text_slices/input_part010.txt†L15663-L15699】

### Tronic X12 Failure & 40PL Ambitions (lines 15701-15755)
- Rosheee’s Tronic X12 blew immediately after enabling ANT BMS discharge, underscoring the risk of toggling pack-side discharge FETs during commissioning and highlighting that the 24 S unit is often run at 26 S because Gal says the MOSFETs have headroom.【F:data/vesc_help_group/text_slices/input_part010.txt†L15701-L15756】
- He plans to pair dual X12s with Samsung 40PL cells at 250 A battery per controller despite a 70 A datasheet rating, making temperature sensors and copper bus reinforcement mandatory for validation runs.【F:data/vesc_help_group/text_slices/input_part010.txt†L15735-L15755】

### SNSC Packaging & Bearing Refresh (lines 15796-15844)
- Jason’s SNSC conversion will grind in rails for a mounting plate and shift the motor rearward because the monofork struggles with a 17×4″ front wheel; Rosheee insists on replacing worn bearings to restore stability before more power mods.【F:data/vesc_help_group/text_slices/input_part010.txt†L15796-L15818】
- GABE reminds builders that SNSC frames weigh roughly 55 kg and do not fold, so transporting the platform requires shipping packs separately or planning alternative logistics.【F:data/vesc_help_group/text_slices/input_part010.txt†L15836-L15844】

### Vsett 11+ Battery Planning (lines 15849-15881)
- New member Jean Bilbao is targeting a 60 V 50 Ah pack for a Vsett 11+, and the group stressed logging exact LG cell model numbers and motor windings because stock 2 000 W hubs can already be pushed to ≈10 kW with quality packs.【F:data/vesc_help_group/text_slices/input_part010.txt†L15849-L15880】
- Noname expects LG M50LT cells in 10 P strings (≈14 A each) to deliver about 9 kW safely while leaving room for controller upgrades once component clearances inside the deck are confirmed.【F:data/vesc_help_group/text_slices/input_part010.txt†L15879-L15881】

### Tire Sizing & Rim Fitment Lessons (lines 15890-16039)
- Mini BMX and G30 builders confirmed that 10×3.0‑6.5 tubeless tires measure about 3 inches wide and seat cleanly on 73 mm (≈2.84″) rims, providing a safer profile than narrower 70/65-6.5 options that stretch on wide hubs.【F:data/vesc_help_group/text_slices/input_part010.txt†L15890-L16017】
- Noname reiterated the tire-nomenclature math—first number is width, aspect ratio yields sidewall height, and imperial 10×3.0 tires translate to 10″ tall and 3″ wide—helping riders compare metric and inch-based listings.【F:data/vesc_help_group/text_slices/input_part010.txt†L15991-L16039】

### Cell Handling & Pack Tooling (lines 16048-16082)
- Budget cell holders with 19 mm spacing can pack 16 cells per row, but salvaged LG modules may be epoxied together; acetone softens the adhesive, and removed wraps often need replacement to avoid insulation pinholes.【F:data/vesc_help_group/text_slices/input_part010.txt†L16048-L16082】

### Brake Discs & CAN Accessories (lines 16102-16116)
- Yamal sourced Shimano-pattern 6‑bolt rotors from Brake-Stuff to replace worn discs, while JPPL is experimenting with a Titaone X10 controller plus Bluetooth module to see whether it exposes VESC telemetry and can run alongside a 20 S 4 P commuter pack at 60 A.【F:data/vesc_help_group/text_slices/input_part010.txt†L16102-L16117】

### MP2 Controller Packaging & Welder Safety (lines 16222-16295)
- MP2 dual controllers offer an inexpensive 20 S solution but require precise mounting—GABE proved they fit upright between Ninebot Pro 2 rails if elevated with spacers and insulated with Kapton or mesh tape to prevent rail shorts.【F:data/vesc_help_group/text_slices/input_part010.txt†L16222-L16295】
- His 801D welder failure traced to stomping the AC adapter power button while the foot pedal was pressed, illustrating why HV spot welders need clear switch guarding and why car batteries remain a viable backup for nickel tabbing.【F:data/vesc_help_group/text_slices/input_part010.txt†L16231-L16252】【F:data/vesc_help_group/text_slices/input_part010.txt†L16301-L16305】

### High-Power Ambitions & Cooling Plans (lines 16313-16399)
- Patrick’s fleet of Spintend and Tronic controllers lacked launch torque until he disabled traction-control experiments and discovered his motor temperature limit was stuck at 0 °C, clamping phase amps to ~86 A; restoring a 112‑120 °C limit brought back full 160 A output.【F:data/vesc_help_group/text_slices/input_part010.txt†L16313-L16353】【F:data/vesc_help_group/text_slices/input_part010.txt†L16737-L16738】
- Builders continue chasing 30‑40 kW scooters: Noname advises liquid-cooling QS hubs with inexpensive AliExpress radiators, targeting ~52 mph on 20 S and 42 mph on 16 S while reserving 32 S packs for future 30 kW attempts.【F:data/vesc_help_group/text_slices/input_part010.txt†L16332-L16348】
- Spintend’s revised 12‑FET (85 V/240 A) shares the 6‑FET architecture with doubled silicon, leading GABE to estimate ≈26 kW ceiling and prefer James Soderstrom as a vendor to dodge month-long factory lead times.【F:data/vesc_help_group/text_slices/input_part010.txt†L16404-L16415】

### Field Weakening & Sensorless Guidance (lines 16561-16615)
- Yoann’s misread phase currents after MOSFET swaps traced to a lifted source leg that needed re-soldering, while Shlomozero confirmed traction control still benefits sensorless hubs once both motors receive hall retrofits.【F:data/vesc_help_group/text_slices/input_part010.txt†L16561-L16599】【F:data/vesc_help_group/text_slices/input_part010.txt†L16711-L16715】
- For M365 field weakening on Flipsky 75200s, ‘lekrsu’ recommends lowering the duty-cycle activation threshold if the scooter never hits 80 % duty, editing Lisp current limits directly, and considering VSS speed estimation because VESC leverages back-EMF above 5 km/h even without halls.【F:data/vesc_help_group/text_slices/input_part010.txt†L16602-L16615】

### Frame Reliability & Upgrade Paths (lines 16640-16688)
- NetworkDir warns that Zero 10X frames, stems, and stock suspension can crack at >60 km/h, and while upgraded Ukrainian parts exist, Vsett 10+ chassis offer better redundancy with dual stems when pushing high power.【F:data/vesc_help_group/text_slices/input_part010.txt†L16640-L16674】
- Shlomozero is outsourcing hall-sensor installs and rewinds to Alex (“nuc” specialist) for 72 V conversions, reinforcing that professional motor service remains in demand for high-discharge builds.【F:data/vesc_help_group/text_slices/input_part010.txt†L16695-L16715】

### Washer & Hardware Sourcing (lines 16718-16752)
- Pandalgns is hunting thin thrust washers that sit between hub-motor shafts and end caps, flagging a sourcing gap for maintenance kits alongside his habit of burning Xiaomi 2.1/3.0 controller boards when hot-rodding commuters.【F:data/vesc_help_group/text_slices/input_part010.txt†L16718-L16752】

### Controller Selection & Power Budgets (lines 16769-16819)
- Rage Mechanics’ C350 remains the community’s go-to when riders ask for 28 S VESCs capable of ≈200 A battery and 700 A phase, while NetworkDir still ranks Fardriver above Kelly/Votol but below native VESC options for extreme scooters.【F:data/vesc_help_group/text_slices/input_part010.txt†L16769-L16771】【F:data/vesc_help_group/text_slices/input_part010.txt†L16743-L16746】
- Omar is staging two Nami builds: run 100 V/100 A now, jump to 100 V/250 A later, and reserve a Tronic X12 for a Kaabo-based race scooter that will never see rain, illustrating how builders assign premium controllers by duty cycle and environment.【F:data/vesc_help_group/text_slices/input_part010.txt†L16790-L16819】

### Lighting & Accessory Power (lines 16813-16835)
- Yamal’s dying MagicShine pack pushed the crew to recommend repacking generic “10 000 mAh” bike lights with real 18650/21700 cells—AYO even linked a 5×P90 AliExpress light—so commuters carry reliable lumens instead of inflated marketing figures.【F:data/vesc_help_group/text_slices/input_part010.txt†L16813-L16835】

### Display & Control Integration
- Pandalgns confirmed the common Ninebot/Laotie TFT is now a generic "JP" unit (formerly TF100/TS100), reminding builders to trace each button and display lead back to the controller when sourcing replacements.【F:data/vesc_help_group/text_slices/input_part010.txt†L6700-L6709】
- NetworkDir noted their in-house dash currently needs UART (RX, TX, GND, 5 V) but an upcoming hardware spin will speak native CAN and can host a VESC Express module, simplifying clean integrations into OEM cockpits.【F:data/vesc_help_group/text_slices/input_part010.txt†L6954-L6969】
- JPPL pointed Haku to Voyage Systems’ Megan CAN display as a premium plug-and-play option for illuminated builds seeking polished instrumentation.【F:data/vesc_help_group/text_slices/input_part010.txt†L8174-L8178】

### VESC Tuning & Traction Setup
- ‘lekrsu’ cautioned that simply running motor detection leaves Xiaomi/Laotie scooters sluggish; enabling the “rocket fuel” tune and trimming acceleration ramp time tightened throttle response, though Haku may re-introduce ramping to curb wheelspin.【F:data/vesc_help_group/text_slices/input_part010.txt†L6710-L6721】
- NetworkDir reminded AYO#74 that a fresh hall-sensor calibration does not require re-running motor detection—riders can launch hall detection directly once the motor profile is dialed in.【F:data/vesc_help_group/text_slices/input_part010.txt†L7398-L7401】
- Her0DasH highlighted the VESC Tool “hand test” as an often-forgotten pre-ride safety check to validate throttle, brake, and input mappings, with the caveat that riders must disable it afterward to restore normal operation.【F:data/vesc_help_group/text_slices/input_part010.txt†L7320-L7329】

### High-Voltage G30 & Frame Planning
- Finn is reviving a dual-16×4 inch, dual-controller G30: he’s weighing 16S6P internals versus a 20S or 22S hybrid (16S deck + 6S add-on), running a Ubox Lite up front with a rear Ubox 85150 that tolerates 22S so long as regen is disabled, although routing eight runs of 10 AWG through the stem is a packaging hurdle.【F:data/vesc_help_group/text_slices/input_part010.txt†L6728-L6769】
- The same discussion surfaced PETG cell-holder behaviors (P42A cans are ~0.25 mm narrower than 40P, and PETG will relax with heat) plus Pandalgns’ work on a fully enclosed 16S Xiaomi holder with BMS service holes, illustrating how printed carriers can balance retention and serviceability.【F:data/vesc_help_group/text_slices/input_part010.txt†L6773-L6789】

### Battery Fabrication & Pack Retrofits
- PuneDir delivered a custom 16S7P Molicel M26 pack to replace an OEM 13S battery, demonstrating a common mid-power retrofit path for legacy scooters that need more voltage without abandoning stock enclosures.【F:data/vesc_help_group/text_slices/input_part010.txt†L6900-L6910】
- Haku flagged an auto-layout tool that can generate printable cell holders from simple series/parallel inputs—worth locating to accelerate future custom pack designs.【F:data/vesc_help_group/text_slices/input_part010.txt†L6789-L6790】
- Pandalgns unveiled a modular 10S6P 21700 bicycle battery holder: twin base plates clamp the cells, a screw-linked column system locks the layers, and a removable mesh cap shields nickel strips while leaving space for a dedicated BMS plate—an adaptable blueprint for irregular triangle packs.【F:data/vesc_help_group/text_slices/input_part010.txt†L8119-L8136】

### Thermal Management & Cooling Experiments
- Haku’s dual controllers currently sit on a thin metal plate sandwiched between battery and deck with a generous coat of budget thermal paste; ‘lekrsu’ and Noname urged adding proper pads and improving airflow because the front tire blocks convection, hinting that a dedicated heatsink or relocation is prudent before sustained high-load runs.【F:data/vesc_help_group/text_slices/input_part010.txt†L6808-L6835】
- Follow-up chatter explored auxiliary cooling: Haku considered side-mounted heatsinks and even liquid loops, while Noname suggested compact radiators or convection plates (with leak precautions) and Lieven reminded the group that well-designed watercooling dramatically increases surface area even if it adds mass.【F:data/vesc_help_group/text_slices/input_part010.txt†L6997-L7018】
- For motor cooling, Haku proposed welding fins and drilling angled vents into LY covers; peers warned that without ferrofluid the stator-to-cover air gap limits gains and open ports invite magnetic dust, whereas water-cooled stators or active airflow offer more reliable results.【F:data/vesc_help_group/text_slices/input_part010.txt†L7312-L7352】

### Charging, Traction & Maintenance Safety
- PuneDir asked about fast-charging a 16S pack with an 84 V (20S) supply clamped by a JK BMS at 4.0 V/cell; Noname stressed the CC/CV mismatch and uncertainty around forcing a higher-voltage charger to sag, reinforcing the need for voltage-appropriate chargers even when BMS limits are lowered.【F:data/vesc_help_group/text_slices/input_part010.txt†L7121-L7135】
- After a Ninebot F2 Pro slide on polished asphalt, the group concluded that while lower pressures increase contact patch, they also reduce ground pressure and can hurt grip on smooth or wet surfaces; experimenting around the rider’s 40–48 psi range and upgrading compound may help more than pressure swings alone.【F:data/vesc_help_group/text_slices/input_part010.txt†L7136-L7150】
- Haku’s Peak G30 battery straps keep snapping in cold weather; the group recommended metal zip ties from Harbor Freight plus hose clamps or U-bolts as compact, weather-resistant alternatives for heavy 72 V packs.【F:data/vesc_help_group/text_slices/input_part010.txt†L8089-L8105】

### Controller Selection & Procurement Notes
- Luis is exploring dual-motor upgrades for a Xiaomi Pro 2 and balked at dual-controller pricing; NetworkDir and Shlomozero steered him toward Spintend Ubox units (dual or single) while warning that Flipsky/Makerbase 75100-series ESCs still suffer reliability issues despite the newer 84100HP revision’s improvements.【F:data/vesc_help_group/text_slices/input_part010.txt†L8033-L8060】【F:data/vesc_help_group/text_slices/input_part010.txt†L8051-L8056】
- Shlomozero detailed Israel’s import reality: premium track scooters must enter as loose parts for reassembly unless buyers hold an importer license, and domestic battery sourcing is required, adding cost and complexity for enthusiasts.【F:data/vesc_help_group/text_slices/input_part010.txt†L8158-L8164】

### Diagnostics & Ride Prep
- Haku finally aligned his VESC logs with GPS speed by verifying CAN bus settings, underscoring the value of double-checking CAN IDs when telemetry disagrees.【F:data/vesc_help_group/text_slices/input_part010.txt†L8185-L8185】
- Ion’s unanswered query about derestricting Bosch e-bikes without pricey tuning chips highlights a knowledge gap worth filling for crossover scooter/e-bike builders.【F:data/vesc_help_group/text_slices/input_part010.txt†L8140-L8141】

### Suspension & Chassis Upgrades
- The Weepor’s stock rear suspension bottoms out under Haku’s weight; he’s targeting an EXA 150 mm shock as a mandatory upgrade, with peers noting that sourcing quality dampers is challenging yet necessary for heavier riders on high-powered builds.【F:data/vesc_help_group/text_slices/input_part010.txt†L8194-L8199】

### Traction Control & High-Voltage Planning (lines 12701-13820)
- 🇪🇸AYO#74 confirmed that VESC traction control made his high-power scooter far more manageable but cost some peak speed; later he asked for a way to trim intervention strength (e.g., dialing back from the default 100 %) so both stability and acceleration survive at hyper-scooter power levels.【F:data/vesc_help_group/text_slices/input_part010.txt†L12701-L12703】【F:data/vesc_help_group/text_slices/input_part010.txt†L13818-L13820】
- Haku, Max Rainlogix, and rosheee discussed running 26S–30S packs on 110 mm-class stators, noting frame volume can accept 30S8P layouts but controller cost (≈US$600 per Seven/VESC) becomes the gating factor for hobbyists eyeing 30 kW builds.【F:data/vesc_help_group/text_slices/input_part010.txt†L12715-L12738】【F:data/vesc_help_group/text_slices/input_part010.txt†L13232-L13240】

### Motor Lead Upgrades & Temperature Monitoring (lines 12754-12805)
- Pandalgns upsized Halo Knight T107Pro 60H hub leads to 12 AWG by drilling the axle feed-through from 8 mm to 10 mm, but discovered the thicker harness no longer slipped through the stock bearings—he plans to partially reassemble (fit cover first, then re-thread each phase) to avoid sourcing custom-ID bearings.【F:data/vesc_help_group/text_slices/input_part010.txt†L12754-L12799】
- Builders reiterated the value of embedded thermistors (NTC 10 k is common) because “hand as sensor” isn’t reliable for safeguarding rewound hubs pushed beyond 3 kW.【F:data/vesc_help_group/text_slices/input_part010.txt†L12757-L12805】【F:data/vesc_help_group/text_slices/input_part010.txt†L13204-L13204】

### Kukirin G2 Master VESC Conversion Guidance (lines 13108-13171)
- For the 52 V dual-motor Kukirin G2 Master, Haku recommended twin Mini Ubox controllers to retain the stock pack and 1 000 W hubs, while Marius warned the chassis wobbles above ~40 km/h even with a steering damper and suggested limiting speed to ~50 km/h or investing in a more stable platform like a G30 with speed forks for 15 kW ambitions.【F:data/vesc_help_group/text_slices/input_part010.txt†L13108-L13170】
- ‘lekrsu’ priced Ubox Alu Lite units around €100–120, setting realistic budgeting expectations for European riders comparing DIY conversions against professional retrofits.【F:data/vesc_help_group/text_slices/input_part010.txt†L13134-L13139】

### Motor & Controller Sourcing Notes (lines 13208-13262)
- JPPL confirmed current Teverun motors are LY-built but not the 90H variant, and highlighted factory upgrade kits (shocks, bearings, VESC controls, 13-inch tires, Samsung 40T packs) that transform the platform toward 30 kW targets with LY 75 speed motors.【F:data/vesc_help_group/text_slices/input_part010.txt†L13208-L13241】
- Finn relayed that a popular 8 kW Alibaba hub lists a 70H, 33×2 winding, giving shoppers a data point when vetting alternatives to LY catalogs.【F:data/vesc_help_group/text_slices/input_part010.txt†L13255-L13262】

### Control Wiring & Diagnostics (lines 13265-13287)
- For Xiaomi-based throttles/brakes, Давно пора advised routing red/black to 3.3 V/GND and the blue (or green) lead to ADC2 on the VESC, sidestepping BLE pucks during conversions.【F:data/vesc_help_group/text_slices/input_part010.txt†L13265-L13271】
- David’s light-throttle knocking on a new motor drew consensus to retest hall sensors, reinforcing that hall issues manifest at low ERPM before full-throttle smooths out.【F:data/vesc_help_group/text_slices/input_part010.txt†L13275-L13287】

### Connector & Hardware Choices (lines 13599-13602)
- Jason recommended XT150 bullets for high-current phase leads while keeping XT90s on the battery side, and ‘lekrsu’ reminded the group that MT60 plugs bundle three XT60-style bullets for tidy triple-phase hookups.【F:data/vesc_help_group/text_slices/input_part010.txt†L13599-L13603】

### High-Performance Cell Options (lines 13622-13652)
- Builders pursuing 14S3P and 22S11P packs praised Molicel P50B cells for 50 A capability but flagged limited supply (≈€7.95 per cell via NKON plus ~US$80 shipping) versus more attainable Samsung 50S or Bak 45D alternatives.【F:data/vesc_help_group/text_slices/input_part010.txt†L13622-L13636】【F:data/vesc_help_group/text_slices/input_part010.txt†L13648-L13652】
- 🇪🇸AYO#74 noted that honeycomb holder geometry was essential to nest 22S11P P45B packs inside Nami chassis without exceeding deck width.【F:data/vesc_help_group/text_slices/input_part010.txt†L13631-L13641】

### Compact Pack Packaging Lessons (lines 13663-13803)
- GABE’s Xiaomi Pro 2 conversion maxed out at 20S2P (40 cells) once spacer thickness and rail clearances were accounted for, forcing decisions about external enclosures or sanding down PETG carriers for sub-millimeter gains.【F:data/vesc_help_group/text_slices/input_part010.txt†L13663-L13803】
- Max Rainlogix suggested mounting VESCs vertically against the deck wall or underneath to free cell volume—an approach worth testing on cramped commuter frames.【F:data/vesc_help_group/text_slices/input_part010.txt†L13721-L13724】【F:data/vesc_help_group/text_slices/input_part010.txt†L13742-L13745】

### Copper Welding & Battery Fabrication (lines 13727-13738)
- Pandalgns considered repurposing a €100–120 spot welder for copper bus work on a planned 20S10P P45B pack; peers advised trial welds at low power (≈0.1 s pulses) to verify the tool can reliably join copper before committing an entire high-discharge build.【F:data/vesc_help_group/text_slices/input_part010.txt†L13727-L13738】

### High-Voltage Commuter Builds (lines 13746-13813)
- GABE is pushing a 250 W Xiaomi hub at ~72 V with 30 A battery and 70 A phase limits (≈1.7–2.1 kW), planning copper sheets above the pack while warning that stopping with a hot motor can cook it—riders should keep rolling at ~20 km/h for cooling or drill vent holes judiciously.【F:data/vesc_help_group/text_slices/input_part010.txt†L13746-L13798】【F:data/vesc_help_group/text_slices/input_part010.txt†L13803-L13805】
- Haku championed external controller mounting and proper thermal interfaces after ‘lekrsu’ logged 55 °C with poor pads but <40 °C once upgraded, proving that even 30 A commuter builds need real heatsinking, especially in sealed compartments.【F:data/vesc_help_group/text_slices/input_part010.txt†L14156-L14167】

### Aftermarket Frames & Accessories (lines 14099-14126)
- Yamal shared Raphael Foujiguara Performance components—reinforced decks, welded battery boxes, mudguards—built around 20S-class scooters with Thunder-style necks, offering boutique chassis upgrades when factories omit essentials like fenders.【F:data/vesc_help_group/text_slices/input_part010.txt†L14099-L14126】

### Hall Sensor Service & Adhesives (lines 11201-11320)
- 🇪🇸AYO#74 and ‘lekrsu’ advise against hot glue for hall boards because it softens near 120 °C; high-temperature silicone or epoxy keeps sensors seated without melting during hub heat cycles, and sensors should be inspected before soldering because occasional DOA parts slip through.【F:data/vesc_help_group/text_slices/input_part010.txt†L11201-L11225】
- For Kaabo Wolf King GT 60H motors, 🇪🇸AYO#74 shared an AliExpress 60 ° hall board that has worked on 2 kW-class hubs, giving builders a vetted spare option when refurbishing large scooters.【F:data/vesc_help_group/text_slices/input_part010.txt†L11226-L11228】

### Water & Advanced Cooling Experiments (lines 11241-11367)
- High-speed riders debating 100 mph builds concluded that controller cooling is the limiting factor; Lieven keeps recommending radiator-based loops because a VESC sitting in airflow lacks enough surface area, while haku weighs CPU-style liquid kits despite Jan warning they can still be passive bottlenecks without full-loop engineering.【F:data/vesc_help_group/text_slices/input_part010.txt†L11241-L11367】
- Jan notes ferrofluid (Statorade) is still the cheapest first step for hub cooling, but drilling water passages or adapting ebike blocks requires serious machining budgets, so experimentation should start on sacrificial motors.【F:data/vesc_help_group/text_slices/input_part010.txt†L11330-L11367】

### VESC Burnout Autopsy & Repair Steps (lines 11394-11505)
- A one-second front-wheel burnout on a 33×2 scooter instantly killed Haku’s slave VESC; NetworkDir walked through fault isolation—check for pack-to-phase shorts with a multimeter’s continuity buzzer, confirm the motor still spins freely, and expect at least two shorted FETs on the aluminum power board.【F:data/vesc_help_group/text_slices/input_part010.txt†L11394-L11427】
- NetworkDir cautioned that opening the controller while short-circuit protection is active can worsen damage, and ‘lekrsu’ reminded the group that mixing MOSFETs between 6-fet and 12-fet Spitend boards isn’t viable—reflow work on aluminum substrates is one of the hardest DIY repairs.【F:data/vesc_help_group/text_slices/input_part010.txt†L11401-L11483】
- Post-mortem advice emphasized avoiding regen-only braking (physical brakes saved the day when power cut mid-burnout) and temporarily detuning to smaller controllers until a repaired or replacement 12-fet arrives.【F:data/vesc_help_group/text_slices/input_part010.txt†L11438-L11505】

### Marketplace & Controller Notes (lines 11527-11612)
- Yamal finds Amass 8 mm bullets fit snugger on dual 10 AWG phase leads than generic 8 mm connectors, though Haku has shaved 10 mm bullets to work in a pinch—underscoring tolerance differences on high-current leads.【F:data/vesc_help_group/text_slices/input_part010.txt†L11527-L11529】
- Winter demand dips are hitting premium builds: Andrei is sitting on four high-end scooters, including a Zero 11X with dual Flipsky 75200 Pros, because local buyers have dried up until spring.【F:data/vesc_help_group/text_slices/input_part010.txt†L11547-L11555】
- Haku is tempted by $160 450 A FarDrivers despite distrusting their software; sombre_enfant confirmed Amy’s factory still repairs the controllers free, offering a safety net for anyone who experiments outside the VESC ecosystem.【F:data/vesc_help_group/text_slices/input_part010.txt†L11561-L11607】

### Tuning & Traction Control (lines 11314-12593)
- Ramp Time still matters: ‘lekrsu’ reiterated that positive ramp delays dull launch response, so traction-control-minded riders set it near zero and add other safeguards instead.【F:data/vesc_help_group/text_slices/input_part010.txt†L11314-L11322】
- 🇪🇸AYO#74 is testing 400 A phase / 180 A battery per motor with 40 points of field weakening on 22S builds, noting duty cycle is capped by road length more than controller limits and that larger 13″ wheels need extra room to spin up.【F:data/vesc_help_group/text_slices/input_part010.txt†L11815-L11843】
- FluidFreeRide alumni warn that fork harnesses pinch at full steering lock, so traction hiccups may stem from damaged neck wiring before software tweaks get blamed.【F:data/vesc_help_group/text_slices/input_part010.txt†L11832-L11835】
- Yamal documented the wiring order for Spintend throttles (3.3 V red, GND black, signal on ADC1) and confirmed the NRF port hosts the Bluetooth module; 🇪🇸AYO#74 later enabled traction control via VESC Tool’s ADC tab (local controller only) and praised how it eliminated wheelspin even at 800 A combined phase.【F:data/vesc_help_group/text_slices/input_part010.txt†L11847-L11855】【F:data/vesc_help_group/text_slices/input_part010.txt†L12142-L12190】【F:data/vesc_help_group/text_slices/input_part010.txt†L12579-L12588】
- Sensorless scooters will still stutter without a kick-start—🇪🇸AYO#74 reminded RicharDON that the behavior is normal unless hall sensors are added.【F:data/vesc_help_group/text_slices/input_part010.txt†L12589-L12593】

### Heatsinks, Packaging & Accessory Modules (lines 11867-11990)
- Arsenus confirmed the always-on accessory module bundled with some VESC kits can be removed; otherwise the controller never sleeps, wasting deck space and standby power.【F:data/vesc_help_group/text_slices/input_part010.txt†L11867-L11885】
- Yamal’s 25 × 15 cm AliExpress heatsink fits a pair of 12-fet Spintend controllers without trimming fins, offering a proven footprint for deck-mounted cooling plates on twin-VESC scooters.【F:data/vesc_help_group/text_slices/input_part010.txt†L11972-L11988】
- Backpack battery builds remain viable but tight: Pandalgns can just squeeze a folded 20S4P into a stripped 5 L pack, while Haku validates that aluminum quick-release racks still need reinforcement to haul heavy spare packs safely.【F:data/vesc_help_group/text_slices/input_part010.txt†L12090-L12100】

### Controller & Motor Upgrades (lines 12002-12366)
- Ion is offloading the original dual Ubox (≈75 V, ~150 A phase per side), and JPPL highlighted Spintend’s new 85 V/240 A single Ubox revision with 8 AWG phases and configurable cable exits—10 A less battery current than the outgoing model but cheaper and smaller for compact decks.【F:data/vesc_help_group/text_slices/input_part010.txt†L12002-L12043】
- Noname reminds builders that mismatched magnet stacks (e.g., 80 H rear, 70 H front) are fine when windings match so one motor doesn’t overdrive the other; plan cases or heat sinks if adopting PCB-only “Seven” VESCs because they ship without enclosures.【F:data/vesc_help_group/text_slices/input_part010.txt†L12043-L12058】
- Pandalgns upgraded a 3 kW hub to 12 AWG phase leads and 28 AWG hall wiring by drilling the axle from 8 mm to 10 mm, noting only minimal metal removal was needed to avoid weakening the shaft—an approach for 72 V conversions chasing higher phase amps.【F:data/vesc_help_group/text_slices/input_part010.txt†L12390-L12399】

### Battery & Cell Planning (lines 11890-12237)
- Ms Cars’ Kukirin G2 Master roadmap: step one is high-discharge cells (Samsung 50S/E or EVE 40PL) and a voltage bump from 52 V (14S) to 60 V (16S) for tangible speed gains; Max Rainlogix assured the cells have plenty of headroom for future controller swaps and clarified pack voltage math for new builders.【F:data/vesc_help_group/text_slices/input_part010.txt†L12201-L12237】
- Yamal keeps a 20S scooter pack at ~76 V during shakedowns and logs 130 A battery / 200 A phase per controller as his baseline before experimenting with higher voltage traction-control tunes.【F:data/vesc_help_group/text_slices/input_part010.txt†L12210-L12224】【F:data/vesc_help_group/text_slices/input_part010.txt†L12556-L12565】

### Motor Sourcing & Pricing Reality (lines 12135-12324)
- JPPL confirmed LY’s new split rims share the same stator cores as their legacy non-split hubs—the upgrade is mainly easier tire service—while the group swapped sources: TaoBao lists 70 H motors near $200 versus $317 direct, but expect to buy rims separately and mind tariffs.【F:data/vesc_help_group/text_slices/input_part010.txt†L12135-L12325】
- Builders are eyeing 80 H rears paired with 70 H fronts plus additional Ubox controllers to push beyond 30S packs, though availability of Seven-series VESCs and high-current BMS options remain constraints for 24S ambitions.【F:data/vesc_help_group/text_slices/input_part010.txt†L12326-L12352】

### Charging & Tire Management (lines 8201-8320)
- Vesc Project Paradise confirmed that a 10P Samsung 40T pack is comfortable with 20 A charging (≈1.6 kW) while 50 A is excessive; the bigger obstacle is locating outlets that reliably supply that current on the road.【F:data/vesc_help_group/text_slices/input_part010.txt†L8201-L8212】
- Riders running 50 psi max tires backed their pressure down to roughly 45 psi for daily riding to balance bead security with traction in cooler weather.【F:data/vesc_help_group/text_slices/input_part010.txt†L8223-L8232】

### Suspension & Frame Notes (lines 8201-9700)
- Builders continue to hunt for stiffer dampers; Nami owners report the OEM suspension still delivers the best comfort/off-road blend, yet high-speed riders often resort to the stiffest springs they can source.【F:data/vesc_help_group/text_slices/input_part010.txt†L8201-L8209】【F:data/vesc_help_group/text_slices/input_part010.txt†L8265-L8269】
- Dualtron and Thunder owners discussing frame swaps highlighted how scarce replacement columns and hinges are, making custom fabrication the practical path when refurbishing used chassis.【F:data/vesc_help_group/text_slices/input_part010.txt†L8933-L8986】
- Upgrading Dualtron Victors to 11-inch wheels requires Thunder swingarms, which remain difficult to obtain locally in Israel’s constrained parts market.【F:data/vesc_help_group/text_slices/input_part010.txt†L9585-L9594】

### Jetson & Mini-Bike Conversions (lines 8330-8700)
- Haku’s $50 Jetson Bolt project will jump to 72 V with an 80/150 controller, but peers urged keeping phase current near 30–50 A and monitoring motor temps; wider 10" QS hubs would overwhelm the 230 mm dropouts, so retaining the stock motor or other scooter hubs is safer.【F:data/vesc_help_group/text_slices/input_part010.txt†L8361-L8429】
- The Bolt’s “bean” battery bay can accommodate folded 20S packs, and community STL files already exist for enlarged compartments, enabling sleeper builds without cutting the frame.【F:data/vesc_help_group/text_slices/input_part010.txt†L8422-L8472】
- Before shunt-modding the 15 A controller, the group recommends spinning the hub with a low-current bench supply, draining capacitors, and only then beefing the shunt; the frame even has mounting points for dual motors if thermal limits are respected.【F:data/vesc_help_group/text_slices/input_part010.txt†L8611-L8656】
- Follow-up spin tests suggested these commuter hubs are direct drive—plastic gearing fears were unfounded—and budget four-piston calipers with DOT 4/5 fluid continue to perform well on similar Chinese scooters.【F:data/vesc_help_group/text_slices/input_part010.txt†L8650-L8657】【F:data/vesc_help_group/text_slices/input_part010.txt†L8667-L8670】

### Hyper-Scooter Benchmarks & Controller Limits (lines 8370-9060)
- 🇪🇸AYO#74 logged ~22 kW from the rear motor alone, implying 43–45 kW combined once the front controller is repaired; the setup has already demonstrated 150 km/h capability given enough straight roadway.【F:data/vesc_help_group/text_slices/input_part010.txt†L8371-L8393】
- Jerome’s GT ride data shows dual Spintend controllers drawing 55–60 A battery each (120 A pack) with phase targets of 160/140 A yet only ~100 A peaks, underscoring the importance of logging to validate tuning.【F:data/vesc_help_group/text_slices/input_part010.txt†L8477-L8495】
- The Rion Apex has been rebadged as the Leo Apex; riders praise the compact Tronic X12 controllers but report chassis wobble that likely needs a steering damper, and the LY 60H 22/3 motors’ 4 mm phase wires cap safe continuous current near 180–200 A despite the 24S pack.【F:data/vesc_help_group/text_slices/input_part010.txt†L8519-L8566】
- European racers gravitate toward Velity or Momen frames despite €9 000+ prices because of their stability, often replacing stock Nutt brakes immediately for track duty.【F:data/vesc_help_group/text_slices/input_part010.txt†L8571-L8597】
- Tronic/Spintend 85-250 units remain happiest on 20S: veterans aim for ~150 A battery/200 A phase continuous with 400 A/260 A peaks if they flash no-limit firmware (voiding warranty) and upgrade motors; the OEM firmware enforces ~83 V and ~300 A phase caps.【F:data/vesc_help_group/text_slices/input_part010.txt†L8838-L8854】
- Pairing a 20S10P Samsung 40T battery with LY 60H motors supports short 250 A phase bursts, but most daily riders stay around 200 A to preserve the thin phase leads.【F:data/vesc_help_group/text_slices/input_part010.txt†L8855-L8864】

### Lighting, Accessories & Low-Voltage Rails (lines 8280-8880)
- 🇪🇸AYO#74 now powers running lights from a voltage reducer while leaving a small brake LED on the controller feed; the latest C350 controllers add a user 12 V rail (~1.2 A) whereas earlier revisions lacked any accessory supply.【F:data/vesc_help_group/text_slices/input_part010.txt†L8280-L8280】【F:data/vesc_help_group/text_slices/input_part010.txt†L8754-L8876】
- Riders shared compact, E-marked motorcycle turn-signal options from AliExpress that suit scooter builds and pair well with external DC-DC converters.【F:data/vesc_help_group/text_slices/input_part010.txt†L9307-L9310】

### Lighting & Signaling Upgrades (lines 9701-10360)
- 🇪🇸AYO#74 shared low-cost AliExpress options for compact motorcycle brake lights, waterproof COB LED strips, and inline three-button dimmer modules that can be paired with 12 V rails or reducers for custom scooter lighting suites.【F:data/vesc_help_group/text_slices/input_part010.txt†L9706-L9718】
- Haku and ‘lekrsu’ highlighted the wiring load imposed by multi-function lighting when using Ubox Lite controllers—without a native 12 V feed, builders should budget extra conductors and a dedicated step-down to run ADC modules and signaling hardware.【F:data/vesc_help_group/text_slices/input_part010.txt†L10277-L10284】
- Haku continues to experiment with AliExpress flasher modules to drive aftermarket blinkers, noting some models require external flashers even when tied to 12 V supplies.【F:data/vesc_help_group/text_slices/input_part010.txt†L10329-L10361】

### Burnouts, Braking & Control Tricks (lines 9701-9734)
- Group burnout experiments confirm that reversing the front hub in VESC and biasing brakes ~70 % front / 30 % rear helps hold the scooter while spinning the rear, though opinions differ on which lever should operate which wheel for rider ergonomics.【F:data/vesc_help_group/text_slices/input_part010.txt†L9715-L9733】

### Jetson & Compact Platform Packaging (lines 9745-9763)
- Haku’s 72 V Jetson Bolt conversion lacks space for an internal VESC, steering him toward a mini-Spintend or external mounting; Jason’s planned Lonnyo 65H (16×4) hub upgrade underscores the availability of 180 °C-rated commuter motors for budget sleeper builds.【F:data/vesc_help_group/text_slices/input_part010.txt†L9745-L9763】

### Motor & Wiring Upgrades (lines 9765-10137)
- Finn rewired a Blade hub with 12 AWG, 200 °C leads to raise thermal headroom, while Shlomozero sourced used Kaabo Wolf (≈60 H) hubs and confirmed 11-inch wheel kits demand matching brake hardware and longer fasteners for clearance.【F:data/vesc_help_group/text_slices/input_part010.txt†L9765-L9850】【F:data/vesc_help_group/text_slices/input_part010.txt†L10241-L10247】
- Koxx/Francois identified the TJA1051 as the CAN bus transceiver to keep on hand for controller repairs, giving DIYers a specific SMD replacement target.【F:data/vesc_help_group/text_slices/input_part010.txt†L9736-L9772】
- ‘lekrsu’ reiterated that Ubox Lite controllers are capped around 150 A phase per motor (even when run as a dual), setting realistic expectations for traction upgrades.【F:data/vesc_help_group/text_slices/input_part010.txt†L10112-L10116】

### Vsett 10 Dual Lite Conversion Results (lines 10062-10075)
- Yoann Tsobanoglou’s Vsett 10 now runs dual Lite VESCs with all stock instrumentation by using a 5 V-triggered relay to bring up an external 12 V converter; he stresses immediate suspension and tire upgrades because the factory front end is unstable at VESC power levels.【F:data/vesc_help_group/text_slices/input_part010.txt†L10062-L10065】
- The team stretched the OEM pack to 72 V by adding cells and swapping in a Nami 80 A BMS—BMS trips occur above ~120 A pack draw, so they cap output at 100–120 A combined and rely on custom Lisp code to ramp phase current with ERPM for traction management.【F:data/vesc_help_group/text_slices/input_part010.txt†L10071-L10075】

### Market & Procurement Notes (lines 10077-10150)
- FreehandZ benchmarked Dualtron GT2 resale at €1 400 (vs. €1 800–2 000 typical locally and €3 700 new) but highlighted lithium shipping restrictions that complicate remote purchases, pushing some builders to design custom swingarms and stems for 80 H motors instead.【F:data/vesc_help_group/text_slices/input_part010.txt†L10077-L10096】
- Pandalgns and GABE compared “hyper daily” stealth builds: keeping 20S 600 Wh packs inside stock 250 W frames demands meticulous pack layout, while full customs risk legal exposure in markets like Spain where 250 W limits are enforced.【F:data/vesc_help_group/text_slices/input_part010.txt†L10131-L10156】

### Battery Building & Component Tooling (lines 10126-10325)
- Pandalgns is iterating stronger 20S8P printed holders after Haku found a shared STL too flimsy, and Noname’s shop is lobbying for a $17 k laser welder to speed precision pack assembly—evidence that serious builds now expect pro-grade welding gear.【F:data/vesc_help_group/text_slices/input_part010.txt†L10126-L10139】【F:data/vesc_help_group/text_slices/input_part010.txt†L10321-L10325】
- GABE’s compact hyper-scooter plan keeps 8.5-inch CST tires and stock cosmetics while hiding upgraded electronics, illustrating packaging trade-offs when staying under the radar.【F:data/vesc_help_group/text_slices/input_part010.txt†L10131-L10144】

### Controller Behavior & Performance Targets (lines 10153-10183)
- GABE’s testing suggests XESC controllers deliver higher top speeds than equivalently tuned VESCs on stock Laotie hardware, though VESCs provide smoother response; he and Haku note 13S commuter setups plateau near 35 km/h while 20S and beyond unlock real performance but introduce packaging constraints with MP2 packs.【F:data/vesc_help_group/text_slices/input_part010.txt†L10153-L10183】

### Brake, Suspension & Frame Reliability (lines 10241-11150)
- Shlomozero’s 11-inch wheel conversion on a Zero 10X requires upgraded brake kits for rotor clearance, and Face de Pin Sucé reported a Slack Core 920R frame snapping before it could be prepped—underscoring the need to inspect boutique frames before pushing power mods.【F:data/vesc_help_group/text_slices/input_part010.txt†L10241-L10246】【F:data/vesc_help_group/text_slices/input_part010.txt†L10370-L10376】
- Haku pointed David to a 3 mm-thick 160 mm rotor that’s readily available on AliExpress for builders chasing stiffer braking setups; stock availability direct from factories remains sporadic.【F:data/vesc_help_group/text_slices/input_part010.txt†L11052-L11057】
- NetworkDir cautioned that Dualtron frames, forks, and motors are heavily outsourced and require full modification for racing despite their popularity in French leagues, so builders shouldn’t assume stock Minimotors components are premium.【F:data/vesc_help_group/text_slices/input_part010.txt†L11151-L11176】

### Battery Cell Debates & Sourcing (lines 11061-11095)
- Patrick resurfaced independent test data showing EVE 40P cells remain the “budget beast” despite limited cycle life, advising riders to spring for Molicel P42A when they need both endurance and discharge margin; impending tariffs on 40PL/BAK cells have builders stockpiling early.【F:data/vesc_help_group/text_slices/input_part010.txt†L11061-L11095】

### Sensor & Hall Maintenance (lines 10109-11200)
- AYO located 60° hall boards for Kaabo Wolf motors, while ‘lekrsu’ warned against securing hall plates with low-temperature hot glue—use high-temp silicone adhesives instead to survive hub heating cycles.【F:data/vesc_help_group/text_slices/input_part010.txt†L10109-L10120】【F:data/vesc_help_group/text_slices/input_part010.txt†L11185-L11200】

### Media & Instrumentation (lines 11120-11121)
- JPPL confirmed Insta360 cameras still offer in-app GPS overlays whereas the GoPro Hero 12 dropped native GPS, guiding riders documenting performance runs.【F:data/vesc_help_group/text_slices/input_part010.txt†L11120-L11121】

### Motor Selection & Troubleshooting (lines 8890-9266)
- Low-side shunts remain standard on controllers such as Torp 500, G300, Spintend, Flipsky C350, and older C700/C1000 units; three-phase current sensing mainly benefits very low-inductance or high-ERPM machines and isn’t a cure-all for hub scooters using HFI.【F:data/vesc_help_group/text_slices/input_part010.txt†L8894-L8905】
- When Wheelway 1000 W hubs chatter above 70 A phase, the crew reruns detection with higher phase current limits, bumps “Power Loss” to ~1 kW, shortens phase wiring, and ultimately recommends LY 60H 22/3 motors if more torque is required.【F:data/vesc_help_group/text_slices/input_part010.txt†L9240-L9247】
- MP2-based 22S2P (≈650 Wh) packs fit neatly inside compact frames, allowing 24S layouts with six extra 21700 cells under the ESC while keeping regenerative braking intact.【F:data/vesc_help_group/text_slices/input_part010.txt†L8997-L9023】
- PuneDir’s sluggish 27 H rear hub (38 km/h on 74 V) illustrates why sourcing reputable QS or YM motors locally is often the only customs-safe path; some regions block direct AliExpress imports.【F:data/vesc_help_group/text_slices/input_part010.txt†L9656-L9670】

### Cooling, Packaging & Fabrication (lines 8470-9345)
- Andrei Albert’s 56 mm-tall controller enclosure mounts at the rear with bi-directional fins, while peers experiment with 250 × 150 × 30 mm skived heat sinks that may require trimming to clear decks, highlighting the DIY nature of scooter cooling upgrades.【F:data/vesc_help_group/text_slices/input_part010.txt†L9313-L9345】
- STL files and machined covers for Jetson Bolt battery bays, MP2 packs, and heatsink adapters are increasingly common, reducing the need to design enclosures from scratch.【F:data/vesc_help_group/text_slices/input_part010.txt†L8471-L8476】【F:data/vesc_help_group/text_slices/input_part010.txt†L9313-L9345】

### Performance Data & Safety (lines 8470-9293)
- 🇪🇸AYO#74 hit 131 km/h on rear motor alone before running out of room, reinforcing the need for long, obstacle-free straights (or closed courses) when validating 30 kW+ builds.【F:data/vesc_help_group/text_slices/input_part010.txt†L9282-L9293】
- With scooter dynos still rare, riders lean on CAN logs, GPS runs, and disciplined cooling upgrades to vet performance instead of relying solely on optimistic app readouts.【F:data/vesc_help_group/text_slices/input_part010.txt†L8477-L8495】【F:data/vesc_help_group/text_slices/input_part010.txt†L9033-L9047】

### Sourcing & Community Logistics (lines 8960-9598)
- Israeli builders face steep cell prices (≈€47 for two P42A cells) and limited import options; the crew suggests contacting trusted builders like @jamessoderstrom or switching to EVE 40P cells, which trade 1 Ah for double the discharge headroom at similar cost.【F:data/vesc_help_group/text_slices/input_part010.txt†L9073-L9093】
- Thunder frames remain scarce locally and often cost double international prices, pushing riders toward piecemeal builds or alternative platforms such as the Nami or Teverun Blade despite their weight penalties.【F:data/vesc_help_group/text_slices/input_part010.txt†L8965-L8986】【F:data/vesc_help_group/text_slices/input_part010.txt†L9586-L9598】

## Open Questions / Follow-ups
- Identify which VESC traction-control parameters (slip limits, strength, filtering) let 🇪🇸AYO#74 and Yamal soften intervention to reclaim top speed without reviving wheelspin.【F:data/vesc_help_group/text_slices/input_part010.txt†L13818-L13820】
- Track down the auto-generated cell-holder design tool Haku referenced for streamlined pack CAD workflows.【F:data/vesc_help_group/text_slices/input_part010.txt†L6789-L6790】
- Gather proven methods (if any) for safely increasing Bosch e-bike speed/acceleration without aftermarket “tuning” dongles to answer Ion’s inquiry.【F:data/vesc_help_group/text_slices/input_part010.txt†L8140-L8141】
- Document effective Weepor shock replacements and tuning guidelines once Haku tests the proposed EXA 150 mm unit.【F:data/vesc_help_group/text_slices/input_part010.txt†L8194-L8199】
- Confirm whether the rumored auto cell-holder generator resurfaced during the Jetson Bolt planning and catalog any STL sources shared with the group.【F:data/vesc_help_group/text_slices/input_part010.txt†L8471-L8476】
- Capture field results on 22S/24S MP2-based packs in compact frames, especially how builders preserve e-brake support and thermal margins at higher voltages.【F:data/vesc_help_group/text_slices/input_part010.txt†L8997-L9023】
- Document a repeatable wiring recipe for Ubox Lite builds that need brake lights, blinkers, and ADC accessories without native 12 V outputs (step-down specs, harness routing, etc.).【F:data/vesc_help_group/text_slices/input_part010.txt†L10277-L10361】
- Follow the Slack Core 920R failure to understand whether the frame snapped from manufacturing defects or prior crash damage before upgrades.【F:data/vesc_help_group/text_slices/input_part010.txt†L10370-L10376】
- Collect Zero 10X frame cavity measurements and component layouts once David reports back so future battery retrofits can be planned confidently.【F:data/vesc_help_group/text_slices/input_part010.txt†L11109-L11110】
- Evaluate whether liquid-cooling experiments (radiators vs. CPU loops) deliver meaningful gains on high-power scooter hubs before riders drill stators or invest in bespoke hardware.【F:data/vesc_help_group/text_slices/input_part010.txt†L11330-L11367】
- Capture repair guides for replacing shorted MOSFETs on Spintend aluminum boards, including recommended hot-plate/reflow techniques and part sourcing to revive burnt controllers like Haku’s.【F:data/vesc_help_group/text_slices/input_part010.txt†L11394-L11483】
- Gather real-world data on Spintend’s revised 85 V/240 A single Ubox to confirm how the smaller enclosure handles sustained current compared with the outgoing 250 A model.【F:data/vesc_help_group/text_slices/input_part010.txt†L12009-L12037】
- Track 🇪🇸AYO#74’s experiment to determine if 72 V Nami controllers operate safely on a 60 V pack after phase rewiring.【F:data/vesc_help_group/text_slices/input_part010.txt†L19994-L20108】
- Record the final controller placement solution for purp’s hall-less Mantis 10 once the mounting hardware and cooling plan are proven in real-world use.【F:data/vesc_help_group/text_slices/input_part010.txt†L20034-L20062】
