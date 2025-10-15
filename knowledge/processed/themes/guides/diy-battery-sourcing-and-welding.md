# DIY Battery Sourcing & Welding Playbook (2025)

## TL;DR
- Grade-A 50PL and P45B cells now define the performance ceiling, but prices swing from €1–1.5 in the EU to ~$9 in the US, so teams must align sourcing tactics with customs realities before scoping pack power levels.[^1][^2]
- Copper spot welding remains the gating competency: bargain 90 € welders rarely prove 0.15 mm claims, while K-Weld or Glitter rigs with proper maintenance reliably join 0.1 mm copper for 22 S packs.[^3][^10]
- Budget worksheets should factor in consumables, BMS headroom, and future tariff shocks (e.g., QS8 connectors drifting toward $35) to avoid mid-build redesigns when scaling beyond 300 A continuous.[^4][^5]

## Workshop Pricing & BMS Baselines
- Denis’ catalog still quotes ~€170 for a 10S4P Samsung 35E pack, €30 for the Wildman bag, and roughly €20 for EU shipping via DPD/UPS; he insists on genuine XT30 hardware and 20 A common-port BMS boards rather than AliExpress knock-offs.[^denis-pricing]
- External packs stay on common-port BMSes so Rita can police charge flow—Denis refuses to ship his smart separate-port boards in range kits because they can’t stop overcharge through the discharge lead.[^common-port-chat]
- Production packs come from the m365Krakow workshop; Denis handles support and logistics while the partner assembles cells, so large orders should plan around their combined lead times.[^m365krakow]

## Cell Market Benchmarks
| Source | Typical Price & Availability | Verified Performance | Procurement Notes |
| --- | --- | --- | --- |
| **Stark Varg salvage modules (50PL)** | ≈€1 per cell after labor in Europe | Bench-tested at 60 A discharge / 15 A charge with tight variance | Requires teardown expertise and logistics for pallet shipments.[^1] |
| **NKON / EU wholesalers (50PL)** | €1.5 per cell retail; logos often milled off | Verified as grade A despite shaved markings | Maintain purchase records to satisfy customs queries about rebranded stock.[^2] |
| **US resellers (50PL)** | ~$9 per cell | Same performance as EU stock | Factor in tariffs and shipping; consider freight-forwarding via EU partners.[^2] |
| **Custom P45B/P50B packs** | €3000–€4500 for 22 S 10 P/11 P assemblies | Continuous ≈495 A, BMS peaks ≈1040 A | Group buys enable supply; document BMS limits (≤500 A continuous today).[^6][^7] |
| **Commissioned builds (UK/US)** | Varies; premium vs DIY delta covers tooling | Output tied to builder’s QC logs | Trusted builders like jamessoderstrom eliminate tooling spend for one-off packs.[^11] |

## Welding Equipment Decision Guide
| Scenario | Recommended Tooling | Why It Wins | Follow-Up Checks |
| --- | --- | --- | --- |
| First copper pack, limited budget | Rent/borrow K-Weld or Glitter kit | Proven to fuse 0.1 mm copper reliably versus unproven 90 € units | Inspect weld nuggets under magnification; rip-test samples before scaling.[^3] |
| Daily fabrication shop | Own Glitter 811A or K-Weld with high-current PSU | Handles repeated 4 kA+ hits when contacts are clean | Schedule bus pin cleaning to prevent E01 faults and maintain 4.4 kA output.[^10] |
| Mixed chemistries (pouch + cylindrical) | Use adjustable pulse welders with copper/nickel sandwiches | Controls heat on dissimilar tabs, minimizes swelling risk | Pair with upgraded ≥230 A BMS and temperature probes on parallel groups.[^6] |

- Budget builders are experimenting with €25 purple PCB welders powered by 72 Ah car batteries—they handle 0.2 mm nickel but lack the transistor count for 0.15 mm copper, so reserve thick copper stacks for Glitter/KWeld-class rigs.【F:knowledge/notes/input_part009_review.md†L364-L365】

## Pack Architecture Case Studies
| Platform | Layout & Cells | Controller Pairing | Lessons |
| --- | --- | --- | --- |
| Dual 70H race scooter | 22 S10/11 P P45B modules | MakerX G300 duals | Logs justify nearly 500 A continuous; plan dual-BMS or fuse strategy until 700 A-class boards exist.[^4][^7] |
| Dualtron Achilleus | 20 S8 P Molicel / 22 S9 P custom | Spintend 85250 relocated outside deck | Deck measures ≈48.5 cm × 18.1 cm—external controller mounting frees volume for ≥100 A batteries.[^4][^8] |
| Nami commuter upgrade | 22 S10 P layout in development | Awaiting high-current controllers | CNC + 3D-printed supports required; treat as modular sled to service 50PL packs.[^12] |
| G3 30 S conversion | 30 S3 P modules (15 S6 P split) | High-voltage VESC | Requires grinding factory brackets; 30 S4 P too wide without chassis surgery and new BMS routing.[^13] |
| 20 S10 P Samsung 40T | Dual Ubox 85250 | 0.2 mm copper busbars deliver ~350 A continuous / 450 A burst; avoid mixing pouch cells in parallel due to swelling | Reserve space for ≥230 A BMS and monitor temps during 40 kW pulls.[^6] |

### 2024 Telegram Updates (input_part009)

#### Cell & Materials Decisions
| Finding | Implementation Guidance | Implication |
| --- | --- | --- |
| 30 S ANT boards misreport when wired to 22 S harnesses without pin swaps.[^ip009-ant-down] | Document the harness repin and configure the app for the shorter stack before trimming leads. | Preserves telemetry accuracy when down-populating high-series boards. |
| Mixed-color LG M26 stock is safe once parallel groups are binned to matching IR values.[^ip009-m26] | Grade and bin cells before welding rather than chasing cosmetic uniformity. | Focus QC time on electrical variance, not sleeve colour. |
| P42A packs bring minimal benefit on scooters capped near 120 A battery when 50H motors saturate around 60 A.[^ip009-p42a] | Choose lower-cost cells if the drivetrain cannot exploit higher current headroom. | Budget savings can fund thermal instrumentation or spare packs. |
| ASA‑CF holders demand heated chambers but deliver exceptionally rigid frames at ~€50 per 750 g of filament.[^ip009-asacf] | Reserve these prints for high-stress packs and price builds accordingly. | Factor double-the-standard-ASA material cost into client quotes. |
| XT90S anti-spark connectors fatigue quickly under scooter loads; QS8 is the preferred drop-in upgrade.[^ip009-xt90] | Upsize to QS8 (or similar) on any build expecting repeated high-current plugs. | Reduces arcing failures and warranty returns on performance scooters. |
| EVE 40PL cells hold roughly 45–70 A continuous with ~60 % capacity left after 300 cycles at 30 A.[^ip009-40pl] | Treat manufacturer 100 A claims as marketing and size packs for realistic current and lifespan. | Helps frame warranty terms around accelerated ageing on torque builds. |

#### Protection & BMS Practice
| Finding | Implementation Guidance | Implication |
| --- | --- | --- |
| Parallel range-extender packs only stay safe if each BMS shares voltage; a tripped BMS dumps full load onto the remaining packs.[^ip009-parallel] | Align pack voltages and current limits, and add coordinated cutoff logic or fusing. | Prevents cascading overload when one BMS trips mid-ride. |
| VESC regen respected 71.4 V on 17 S builds, so 72 V setpoints remained within controller limits.[^ip009-regen] | You can leave regen enabled near full charge on 17 S scooters without overstressing the controller, provided wiring supports it. | Simplifies regen tuning for riders who top off frequently. |
| Deep-discharging a JK-managed pack to 57 V killed cells and the BMS interface.[^ip009-deepdis] | Enforce conservative low-voltage alarms on extender packs and recharge well before hard cutoff. | Avoids irreversible cell damage and lost telemetry. |
| Active balancing boards restored pack parity in roughly an hour versus days on stock JBD balancing.[^ip009-active] | Deploy active balancers during commissioning or service to accelerate equalisation. | Shortens delivery timelines for large-capacity builds. |
| Cloud-connected smart BMS portals can be tampered with, and some apps break if you change default passwords.[^ip009-bms-app] | Keep smart BMS units offline or maintain default credentials with physical security layers. | Reduces remote sabotage risk while preserving diagnostics. |
| JK’s mobile app can disable the discharge MOSFET for storage or anti-theft once the pack is full.[^ip009-jk-mosfet] | Add the MOSFET-disable workflow to delivery checklists so riders can lock packs without rewiring. | Provides a simple parking lock without extra hardware. |
| Compact 10 S builds pulling 30–45 A per cell still favour JK/JBD 100 A boards (with ANT as backup) for protection and telemetry.[^ip009-compact-bms] | Budget space for smart BMS hardware even in tight enclosures to retain diagnostics. | Confirms that reliable protection trumps marginal space savings. |

#### Assembly & Mechanics
| Finding | Implementation Guidance | Implication |
| --- | --- | --- |
| Thin epoxy sheets between balance leads and copper busbars maintain insulation where plastic holders will not fit.[^ip009-epoxy] | Stock epoxy board alongside fishpaper for slim packs, especially Zero 10X builds. | Improves durability without increasing pack thickness. |
| Silicone spacers backed with fishpaper/Kapton keep honeycomb rows insulated when hot-gluing rebuilt packs.[^ip009-silicone] | Stage silicone/Kapton strips during rebuilds instead of relying on shrink alone. | Reduces rewrap labour after service. |
| Twin steel strip overlays support ~8 A per cell in LG M26 packs when reinforced, keeping 17 P builds near 10–11 kW.[^ip009-steel] | Pair steel overlays with structural bracing for high-parallel-count packs. | Offers a path to higher power without full copper busbars. |
| 0.1 mm copper sheet is the minimum for busbars; thinner 0.01 mm craft foil tears under welding current.[^ip009-copperthick] | Audit material deliveries before welding and reject ultra-thin foil. | Prevents catastrophic busbar failure mid-build. |
| Chamfer copper/nickel edges near positive terminals to stop them slicing insulation under heavy compression.[^ip009-chamfer] | Add deburring passes before final shrink and compression. | Cuts down on latent shorts in high-mass packs. |
| Tight-tolerance 3D-printed holders (PETG/ASA/ABS) outperform hot glue for spacing and heat paths, especially on long packs.[^ip009-holders] | Prioritise high-temp filaments for holders exposed to parked-car heat. | Raises mechanical reliability for summer storage. |
| Double-layer “makaron” shrink can substitute for fishpaper between rows, but scuffs faster and still benefits from fishpaper on series barriers.[^ip009-makaron] | Use makaron only for supplemental abrasion resistance, not as the sole barrier. | Avoids premature insulation wear. |
| Fiberboard between copper folds keeps 0.20–0.25 mm busbars separated until spacers land.[^ip009-fiberboard] | Slide thin fiberboard into the fold before clamping and remove it once epoxy spacers are seated. | Prevents shorting while the copper stack is aligned. |
| Barley paper at strip ends stops heavy copper sandwiches from chafing insulation when packs flex.[^ip009-barley] | Wrap each series strip in barley paper before final compression or shrink. | Boosts abrasion resistance on high-mass builds. |
| Pre-tension springy copper before welding to tame rebound.[^ip009-pretension] | Drag the strip gently over a table edge so it lies flat once the first welds land. | Makes folding safer and keeps busbars seated. |
| Reinforce hanging extender bags with rigid bases or tailored straps.[^ip009-bag] | Add structural panels or relocate the pack to stop sag that stresses frames mid-ride. | Keeps twin-pack builds stable and protects enclosures. |
| G30 conversions fitting 20 S 6 P 21700 stacks needed a 36 mm deck extender plus ~1 mm grinding around the rail opening.[^ip009-g30] | Budget machining time and extender hardware when packaging large packs with dual controllers. | Prevents rework when packs will not seat flush. |
| Twin-MP2 G30 builds stack the 20 S brick to ~14.5 cm, park the smart BMS vertically at the nose, and split current across parallel QS8 leads with multiple 8 AWG runs while a welded rear controller box preserves the deck arches.[^ip009-g30blueprint] | Mock up the vertical BMS bay and welded enclosure before final welding to confirm harness slack and controller cooling. | Keeps tall packs serviceable without weakening the frame. |
| Flush cutters lift welded nickel without grinding off plating; remaining specks can stay once flattened.[^ip009-flush] | Equip teardown stations with sharp flush cutters and burnishers. | Speeds rebuilds while preserving cell cans. |
| Adhesive-lined “marine” shrink grips bullet connectors more securely than thin sleeves.[^ip009-marine] | Standardise on glue-lined shrink for high-current leads. | Reduces connector loosening under vibration. |
| 🇪🇸AYO#74 secures rebuilt modules with hot silicone plus glass filament tape to stop vibration fret.[^ip009-ayo] | Add silicone tacks and filament wrap when custom holders are unavailable. | Lightweight reinforcement alternative for tight enclosures. |
| Switching Laotie builds to seated frames freed enough deck volume for a 240-cell main pack once the extender battery was repurposed.[^ip009-laotie240] | Scope bracing and BMS routing for the larger brick before committing to the chassis swap. | Avoids mid-build packaging surprises on cramped commuter frames. |
| Refurbishing Glitter 811H consumables restored reliable 0.25–0.30 mm copper weld strength on budget rigs.[^ip009-811h-refresh] | Keep spare electrodes and cables on the shelf and requalify weld nuggets after each refresh. | Extends the service life of 811H setups when KWeld imports are blocked. |

#### Consumables & Logistics
| Finding | Implementation Guidance | Implication |
| --- | --- | --- |
| Leaded solder continues to slip through AliExpress when shipped with Chinese labelling, letting builders finish 13S8P packs even where customs screenings are strict.[^ip009-solder] | Order spare reels ahead of schedule and document the supplier details in build logs in case a batch is seized. | Keeps bench work on track when domestic suppliers restrict leaded alloys. |

## Cost Planning Worksheet
1. **Cell procurement** – price the primary chemistry plus 10 % spares for grading losses and future replacements.[^2][^11]
2. **Interconnects & welding** – include copper/nickel, insulation, weld probe maintenance, and PPE alongside the welder cost or rental fees.[^3][^10]
3. **BMS & protection** – today’s compact boards cap around 500 A continuous; large packs may need dual-BMS or fuse-plus-charge solutions until 700 A hardware lands.[^7]
4. **Connectors & harnessing** – QS8 connectors, 8–10 AWG silicone wire, and panel mounts are trending upward in price due to tariffs—stockpile early.[^5][^9]
5. **Enclosure & structural supports** – CNC plates, 3D spacers, and adhesives trump hot glue for 22 S builds; treat mechanical retention as part of the electrical budget.[^8][^14]
6. **Labor or outsourcing** – weigh the tooling investment against commissioning vetted builders when customs, shipping, or learning curves threaten schedules.[^11]

## QA & Maintenance Protocols
- **Thermal interface audits:** Log controller and stator temperatures on first shakedown runs; resurface heatsink plates and refresh thermal paste before chasing 400 A+ per motor.[^9]
- **Weld verification:** Rip-test sample strips each session, especially after cleaning Glitter bus pins, to confirm energy settings haven’t drifted.[^10]
- **Harness strain relief:** Use deck plates or external mounts to keep relocated controllers from stressing phase leads and QS8 connectors during pack swaps.[^8][^9]
- **Telemetry cross-checks:** Pair CAN smart BMS data with VESC logs to validate current draw and spot calibration drift in shunt-based readings.[^7]
- **Finish work around positives:** Deburr nickel edges near cell tops and re-seat fishpaper before closing the pack—sharp tabs have already pierced insulation on low-current power-bank builds.【F:knowledge/notes/denis_all_part02_review.md†L122364-L122385】
- **Print holders for heat, not looks.** PLA cradles slump once cells warm; switch to PETG or ASA around 230 °C/100 °C bed temps so 21700 honeycombs and Wildman bag sleds stay rigid in summer decks.【F:knowledge/notes/denis_all_part02_review.md†L116230-L116236】【F:knowledge/notes/denis_all_part02_review.md†L89665-L89696】
- **Document capacity checks.** Time OEM chargers (≈1.7 Ah per hour on Xiaomi bricks) when vetting customer packs; a genuine 12 Ah module needs nearly seven hours from empty.【F:knowledge/notes/denis_all_part02_review.md†L98595-L98598】
- **Log cell provenance.** Refurb lots from NKON (late-2021 Samsung 35E/50E) arrive graded and safe when treated like fresh stock; track batch codes and keep compression on pouch experiments so swelling doesn’t lift tabs.【F:knowledge/notes/denis_all_part02_review.md†L97241-L97259】

### Mounting & Housing Patterns
- **Armor deck-mounted conduits.** Twin 10S packs strapped along the deck need metal shielding and permanent wiring—open conduit runs are “self-propelled bombs” unless the housing resists impacts and stays wired for continuous duty.【F:knowledge/notes/denis_all_part02_review.md†L230-L234】
- **Overbuild bag brackets.** Wildman bag packs now use eight screw/wide-washer mounts, fiberglass sleeving, and interior foam so cells can’t chafe on hardware or eject during pothole hits.【F:knowledge/notes/denis_all_part02_review.md†L361-L362】
- **Expect tight tolerances.** A 13S5P/16S3P 21700 stack just fits a 3 L Wildman when you skip holders, while 13S4P assemblies barely squeeze into 2–3 L shells—plan for custom spacers, cardboard liners, and printed cages before drilling the pack.【F:knowledge/notes/denis_all_part02_review.md†L362-L363】【F:knowledge/notes/denis_all_part02_review.md†L165-L165】
- **Retire fatigued brackets.** Heavy 13S packs crack 3D-printed rear supports near the rear bolt; inspect and replace printed mounts routinely or swap to metal before pushing high-speed builds.【F:knowledge/notes/denis_all_part02_review.md†L352-L352】

### Salvage & Pack Handling Lessons
- **Plan for encapsulated fleet packs.** Ninebot rental batteries bury their BMS inside silicone potting; expect to chisel sealant or swap a fresh board because resets are impossible while encapsulated.[^15]
- **Avoid grinders on aluminum shells.** Score the silicone bead with a utility knife, brace the enclosure in a vise, and drive the cell brick out with a wooden drift from the non-BMS end to preserve wiring.[^16]
- **Treat 0.1 mm nickel stacks like structural parts.** Double layers safely carry ≈20 A BMS currents, but only when bonded with multiple high-energy weld strikes—thin hot glue fails once packs warm.[^17]
- **Invest in training before welding.** Veterans keep Micah Toll’s handbook on the bench so new builders understand failure modes before touching live cells.[^18]
- **Model builds around stock chemistries.** Xiaomi packs routinely ship with LG M26 or blue EVE 18650 cells; use those discharge curves when calculating performance instead of optimistic MJ1 assumptions.[^19]
- **Distribute shoulder-bag loads.** Add thin aluminum plates outside fiberglass fire sleeves to spread weight and shield packs from direct flame when slinging externals over a shoulder.[^20]

## Action Checklist
1. **Lock sourcing** – secure cell batches (with customs paperwork) before welding to avoid chemistry mismatches mid-build.[^1][^2]
2. **Stage tooling** – confirm welder calibration with sacrificial strips and schedule maintenance (cleaning, electrode dressing) ahead of production days.[^3][^10]
3. **Model pack fitment** – dry-fit modules in CAD or cardboard using deck measurements (e.g., 48.5 cm × 18.1 cm for Dualtron Achilleus) to plan controller relocation.[^8]
4. **Budget protection gear** – purchase BMS units, fuses, QS8 connectors, and spare harness parts before tariffs or stockouts force redesigns.[^5][^7][^9]
5. **Document performance** – archive discharge/charge test data, weld logs, and thermal profiles so future revisions start from validated baselines.[^1][^6][^10]

## Source Notes
[^ip009-m26]: Mixing grey and purple LG M26 cells proved acceptable once each parallel group was matched on internal resistance.【F:knowledge/notes/input_part009_review.md†L19-L19】
[^ip009-p42a]: Builders saw little advantage in P42A packs on scooters limited to ~120 A battery draw because 50H motors saturated around 60 A battery current on 20 S builds.【F:knowledge/notes/input_part009_review.md†L20-L20】
[^ip009-asacf]: Custom ASA‑CF holders demand heated chambers but deliver very rigid packs at roughly €50 per 750 g of filament—about twice the cost of standard ASA.【F:knowledge/notes/input_part009_review.md†L21-L21】
[^ip009-xt90]: XT90S anti-spark plugs failed quickly under scooter duty, pushing builders toward QS8 connectors for reliability.【F:knowledge/notes/input_part009_review.md†L22-L22】
[^ip009-40pl]: Community testing pegs EVE 40PL cells at 45–70 A continuous with ~60 % capacity remaining after 300 cycles at 30 A, far below marketing claims.【F:knowledge/notes/input_part009_review.md†L39-L39】
[^ip009-parallel]: Running range-extender packs with independent BMS boards works only when voltages align; a tripped board can dump the entire load on the others and overstress them instantly.【F:knowledge/notes/input_part009_review.md†L23-L23】
[^ip009-regen]: Heavy 17 S builds reported VESC regen respecting the 71.4 V full-charge voltage, keeping 72 V setpoints within limits.【F:knowledge/notes/input_part009_review.md†L24-L24】
[^ip009-deepdis]: A JK-managed pack left at 57 V lost BMS communications and damaged cells, underscoring the risk of deep discharge on extender packs.【F:knowledge/notes/input_part009_review.md†L29-L29】
[^ip009-active]: Active balancing boards equalised large packs in about an hour compared with days on passive JBD balancing.【F:knowledge/notes/input_part009_review.md†L27-L27】
[^ip009-bms-app]: Builders warned that keeping smart-BMS apps online invites tampering and even password changes can break connectivity, so many keep packs offline.【F:knowledge/notes/input_part009_review.md†L33-L33】
[^ip009-jk-mosfet]: JK’s app lets riders disable the discharge MOSFET to keep scooters from waking while parked.【F:knowledge/notes/input_part009_review.md†L35-L35】
[^ip009-compact-bms]: Even cramped 10 S builds drawing 30–45 A per cell rely on JK/JBD 100 A smart boards (with ANT backups) for protection and telemetry.【F:knowledge/notes/input_part009_review.md†L36-L36】
[^ip009-ant-down]: Down-populating a 30 S ANT board onto a 22 S harness produced bogus voltages until the pinout and app settings were updated for the shorter stack.【F:knowledge/notes/input_part009_review.md†L403-L403】
[^ip009-epoxy]: Zero 10X pack builders slid thin epoxy sheets between balance harnesses and copper busbars when plastic holders would not fit, preserving insulation without added thickness.【F:knowledge/notes/input_part009_review.md†L18-L18】
[^ip009-silicone]: Rebuilt honeycomb packs benefited from silicone spacers plus fishpaper or Kapton between series rows when hot gluing groups.【F:knowledge/notes/input_part009_review.md†L25-L25】
[^ip009-steel]: Using twin steel strips over nickel supported roughly 8 A per cell in LG M26 packs while keeping 17 P layouts near 10–11 kW.【F:knowledge/notes/input_part009_review.md†L26-L26】
[^ip009-copperthick]: Builders reminded AYO that 0.1 mm copper sheet is required for busbars; 0.01 mm foil tears under welding current.【F:knowledge/notes/input_part009_review.md†L28-L28】
[^ip009-chamfer]: Copper strip edges near positive terminals can slice insulation under heavy load, so chamfering is now standard before shrink-wrapping.【F:knowledge/notes/input_part009_review.md†L30-L30】
[^ip009-holders]: Multiple builders reiterated that tight-tolerance 3D-printed holders (PETG/ASA/ABS) improve spacing and thermal paths over hot glue, especially for long packs.【F:knowledge/notes/input_part009_review.md†L31-L31】
[^ip009-makaron]: Double-layer “makaron” shrink can replace fishpaper between rows but still scuffs faster, so veterans still prefer fishpaper for series barriers.【F:knowledge/notes/input_part009_review.md†L32-L32】
[^ip009-g30]: Squeezing a 20 S 6 P 21700 pack plus twin MP2 controllers into a G30 required a 36 mm deck extender and ~1 mm of grinding around the rail opening.【F:knowledge/notes/input_part009_review.md†L34-L34】
[^ip009-fiberboard]: Sliding thin fiberboard into 0.20–0.25 mm copper folds keeps the busbars separated until epoxy spacers land.【F:knowledge/notes/input_part009_review.md†L398-L399】
[^ip009-barley]: Builders finish each series strip with barley paper so heavy copper stacks don’t chafe insulation when the pack flexes.【F:knowledge/notes/input_part009_review.md†L400-L400】
[^ip009-pretension]: Pre-tensioning copper by bending it over a table edge keeps springy sheets seated once the first welds land.【F:knowledge/notes/input_part009_review.md†L401-L401】
[^ip009-bag]: Twin-pack minibike builds now reinforce external battery bags with tailored straps or rigid bases after sagging stressed the frame mid-ride.【F:knowledge/notes/input_part009_review.md†L402-L402】
[^ip009-g30blueprint]: The 20 S 12 P twin-MP2 concept stacks cells to roughly 14.5 cm, stands the smart BMS vertically ahead of the brick, and feeds dual QS8 harnesses with parallel 8 AWG leads while a welded rear controller box keeps the deck arches intact.【F:data/vesc_help_group/text_slices/input_part009.txt†L21845-L21939】
[^ip009-flush]: Veterans prefer flush cutters for tearing down welded packs, leaving flattened remnants that accept new strip without grinding plating away.【F:knowledge/notes/input_part009_review.md†L37-L37】
[^ip009-marine]: Adhesive-lined “marine” heat-shrink grips bullet connectors far better than thin sleeves that slide off under load.【F:knowledge/notes/input_part009_review.md†L38-L38】
[^ip009-ayo]: 🇪🇸AYO#74 secures rebuilt modules with hot silicone and glass filament tape so vibration cannot fret the wraps.【F:knowledge/notes/input_part009_review.md†L40-L40】
[^ip009-laotie240]: Switching from a stand-up to a seated Laotie frame let Haku fold a 240-cell pack into the main chassis instead of a bolt-on extender, albeit with heavy labor and safety cautions.【F:knowledge/notes/input_part009_review.md†L206-L214】
[^ip009-811h-refresh]: Fresh electrodes and cables brought a Glitter 811H back to consistent 0.25–0.30 mm copper welds, keeping it competitive with KWeld rigs despite customs limits.【F:knowledge/notes/input_part009_review.md†L214-L214】
[^ip009-solder]: Leaded solder reels are still arriving via AliExpress despite customs checks, letting builders complete 13S8P packs once shipments clear.【F:data/vesc_help_group/text_slices/input_part009.txt†L110-L111】
[^1]: Salvaged Stark Varg 50PL modules pricing and 60 A/15 A validation results.【F:knowledge/notes/input_part014_review.md†L35-L35】
[^2]: EU vs. US 50PL pricing, customs considerations, and grade-A assurances on rebranded cells.【F:knowledge/notes/input_part014_review.md†L36-L36】
[^3]: Spot welder cost comparison between 90 € generics and reliable K-Weld/Glitter setups for 0.1 mm copper joints.【F:knowledge/notes/input_part014_review.md†L34-L34】
[^4]: High-output pack examples (22 S10/11 P P45B, 20 S8 P Molicel) and their controller pairings.【F:knowledge/notes/input_part014_review.md†L37-L37】
[^5]: Tariff-driven QS8 and cell stockpiling strategies for US builders.【F:knowledge/notes/input_part014_review.md†L38-L38】
[^6]: Haku’s 20 S10 P Samsung 40T build, busbar thickness, and BMS upgrade warning against mixed chemistries.【F:knowledge/notes/input_part014_review.md†L39-L39】
[^7]: Continuous and peak current expectations plus current BMS limitations for 22 S packs.【F:knowledge/notes/input_part014_review.md†L60-L61】【F:knowledge/notes/input_part014_review.md†L101-L101】
[^8]: Dualtron Achilleus deck dimensions and mounting implications for high-current batteries.【F:knowledge/notes/input_part014_review.md†L44-L44】
[^9]: Thermal envelope reminders (≤45 °C controller, ≤100 °C stator) and conductor upgrades for 400 A pursuits.【F:knowledge/notes/input_part014_review.md†L61-L61】【F:knowledge/notes/input_part014_review.md†L75-L75】
[^10]: Glitter 811A maintenance steps to recover 4.4 kA output and recommended rip-testing routine.【F:knowledge/notes/input_part014_review.md†L152-L152】
[^11]: Guidance on commissioning trusted builders to bypass tooling purchases for single packs.【F:knowledge/notes/input_part014_review.md†L156-L156】
[^12]: Nami 22 S 10 P layout planning with CNC/3D-printed supports.【F:knowledge/notes/input_part014_review.md†L159-L159】
[^13]: G3 30 S conversion constraints and required chassis modifications.【F:knowledge/notes/input_part014_review.md†L160-L160】
[^14]: Rejection of hot glue for 22 S 10 P packs and emphasis on structural spacers/adhesives.【F:knowledge/notes/input_part014_review.md†L172-L172】
[^15]: Fleet Ninebot G30 rental packs arrive fully potted, hiding the BMS and forcing either destructive teardown or outright replacement during refurb work.【F:knowledge/notes/all_part01_review.md†L87214-L87233】
[^16]: Recommended aluminum-pack teardown workflow—score silicone, secure the case, and drive cells out with a wooden dowel from the non-BMS side to keep harnesses intact.【F:knowledge/notes/all_part01_review.md†L88057-L88085】
[^17]: Double-stacked 0.1 mm × 8 mm nickel supports 20 A BMS loads only when welded with multiple high-power strikes; low-temp hot glue fails once packs heat during use.【F:knowledge/notes/all_part01_review.md†L88155-L88333】
[^18]: Community reminder to read Micah Toll’s battery handbook before building packs to avoid costly mistakes.【F:knowledge/notes/all_part01_review.md†L88244-L88245】
[^19]: Stock Xiaomi batteries typically use LG M26 or blue EVE 18650 cells—model upgrades around those chemistries for realistic performance estimates.【F:knowledge/notes/all_part01_review.md†L88335-L88345】
[^20]: Shoulder-bag pack carriers add thin aluminum plates outside fiberglass sleeves to diffuse heat and prevent straps from pinching cells during transport.【F:knowledge/notes/all_part01_review.md†L88051-L88055】
[^denis-pricing]: 【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L1510-L1526】
[^common-port-chat]: 【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L1545-L1594】
[^m365krakow]: 【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L1612-L1618】
