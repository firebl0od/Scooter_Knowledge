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

- **Pack economics remain chemistry-dependent.** Artem still favours P42A-class cells for 25 A-per-cell projects, considers Samsung 48X only a slight upgrade over 50G, and flags M50LT Gen 2 for 0–15 A commuters while crews chase scarce 50E/Molicel stock across Europe.【F:knowledge/notes/input_part002_review.md†L692-L693】
- **Budget whole-pack pricing.** A 20 S9 P Samsung 48X build lands around $5.75 per cell delivered from Canada (~$1,035 total), supports 150 A bursts (~17.2 A/cell), and returns 40–80 mile range depending on riding style—use it as a baseline when comparing long-range quotes.【F:knowledge/notes/input_part002_review.md†L694-L694】

## Welding Equipment Decision Guide
| Scenario | Recommended Tooling | Why It Wins | Follow-Up Checks |
| --- | --- | --- | --- |
| First copper pack, limited budget | Rent/borrow K-Weld or Glitter kit | Proven to fuse 0.1 mm copper reliably versus unproven 90 € units | Inspect weld nuggets under magnification; rip-test samples before scaling.[^3] |
| Daily fabrication shop | Own Glitter 811A or K-Weld with high-current PSU | Handles repeated 4 kA+ hits when contacts are clean | Schedule bus pin cleaning to prevent E01 faults and maintain 4.4 kA output.[^10] |
| Mixed chemistries (pouch + cylindrical) | Use adjustable pulse welders with copper/nickel sandwiches | Controls heat on dissimilar tabs, minimizes swelling risk | Pair with upgraded ≥230 A BMS and temperature probes on parallel groups.[^6] |

## Pack Architecture Case Studies
| Platform | Layout & Cells | Controller Pairing | Lessons |
| --- | --- | --- | --- |
| Dual 70H race scooter | 22 S10/11 P P45B modules | MakerX G300 duals | Logs justify nearly 500 A continuous; plan dual-BMS or fuse strategy until 700 A-class boards exist.[^4][^7] |
| Dualtron Achilleus | 20 S8 P Molicel / 22 S9 P custom | Spintend 85250 relocated outside deck | Deck measures ≈48.5 cm × 18.1 cm—external controller mounting frees volume for ≥100 A batteries.[^4][^8] |
| Nami commuter upgrade | 22 S10 P layout in development | Awaiting high-current controllers | CNC + 3D-printed supports required; treat as modular sled to service 50PL packs.[^12] |
| G3 30 S conversion | 30 S3 P modules (15 S6 P split) | High-voltage VESC | Requires grinding factory brackets; 30 S4 P too wide without chassis surgery and new BMS routing.[^13] |
| 20 S10 P Samsung 40T | Dual Ubox 85250 | 0.2 mm copper busbars deliver ~350 A continuous / 450 A burst; avoid mixing pouch cells in parallel due to swelling | Reserve space for ≥230 A BMS and monitor temps during 40 kW pulls.[^6] |

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
- **Bridge long packs with multiple jumpers.** 16 S 8 P layouts that only bridge two series cells choke current and cook the interconnect—double back with extra jumpers or a second copper layer so each parallel group shares the load evenly.【F:knowledge/notes/input_part002_review.md†L606-L608】
- **Tin and fold copper busbars before welding.** Solder the main leads to copper strip, fold it for a double-thick bus, and insulate with Kapton or fish paper before closing the pack so K-weld adopters avoid hot spots and exposed edges.【F:knowledge/notes/input_part002_review.md†L606-L608】
- **Trim welder leads:** KWeld’s stock 8 AWG harness can waste kilowatts at the lugs—shorten cables, refresh soldered ends, or parallel LiPo packs so weld energy stays consistent during copper “sandwich” builds.【F:data/vesc_help_group/text_slices/input_part002.txt†L11188-L11209】
- **Treat copper-nickel sandwiches cautiously:** Exposed stacks crack over time when dissimilar metals oxidise—seal the assembly or fall back to pure nickel if your welder struggles with copper.【F:knowledge/notes/input_part002_review.md†L401-L401】
- **0.15 mm nickel-plated copper sits around 15 A per cell.** Builders like the 8 mm strip for commuter packs, but once group currents top 25 A they still stack full copper plates or sandwich sheets to keep resistance low.【F:data/vesc_help_group/text_slices/input_part002.txt†L12622-L12654】
- **Direct copper spot welds remain risky.** Without inert gas the joint oxidises, 0.2 mm copper sticks to probes, and the extra heat endangers cells—most crews stick with copper plate plus nickel/steel caps unless they can TIG busbars safely.【F:data/vesc_help_group/text_slices/input_part002.txt†L13624-L13640】
- **Finish work around positives:** Deburr nickel edges near cell tops and re-seat fishpaper before closing the pack—sharp tabs have already pierced insulation on low-current power-bank builds.【F:knowledge/notes/denis_all_part02_review.md†L122364-L122385】
- **Let smart BMS boards police shorts.** Builders reminded newcomers that quality smart BMS hardware trips far faster than external fuses while still handling balancing duty—treat fuses as supplements, not replacements.【F:knowledge/notes/input_part002_review.md†L418-L418】
- **Print holders for heat, not looks.** PLA cradles slump once cells warm; switch to PETG or ASA around 230 °C/100 °C bed temps so 21700 honeycombs and Wildman bag sleds stay rigid in summer decks.【F:knowledge/notes/denis_all_part02_review.md†L116230-L116236】【F:knowledge/notes/denis_all_part02_review.md†L89665-L89696】
- **Document capacity checks.** Time OEM chargers (≈1.7 Ah per hour on Xiaomi bricks) when vetting customer packs; a genuine 12 Ah module needs nearly seven hours from empty.【F:knowledge/notes/denis_all_part02_review.md†L98595-L98598】
- **Log cell provenance.** Refurb lots from NKON (late-2021 Samsung 35E/50E) arrive graded and safe when treated like fresh stock; track batch codes and keep compression on pouch experiments so swelling doesn’t lift tabs.【F:knowledge/notes/denis_all_part02_review.md†L97241-L97259】
- **Reinforce shrink wrap for shipping.** Double-layer lighter “Albert” sleeves with thicker “Denis” stock, add padding over balance leads, and heat the wrap with a gun (not just a dryer) so decks don’t abrade the pack in transit.【F:knowledge/notes/input_part002_review.md†L671-L673】
- **Stop pack shuffle before blaming wrap.** If shrink is wearing through, fix clamp pressure or enclosure padding—the workshop called loose packs the root cause, not the plastic itself.【F:knowledge/notes/input_part002_review.md†L671-L673】

### Mounting & Housing Patterns
- **Armor deck-mounted conduits.** Twin 10S packs strapped along the deck need metal shielding and permanent wiring—open conduit runs are “self-propelled bombs” unless the housing resists impacts and stays wired for continuous duty.【F:knowledge/notes/denis_all_part02_review.md†L230-L234】
- **Overbuild bag brackets.** Wildman bag packs now use eight screw/wide-washer mounts, fiberglass sleeving, and interior foam so cells can’t chafe on hardware or eject during pothole hits.【F:knowledge/notes/denis_all_part02_review.md†L361-L362】
- **Expect tight tolerances.** A 13S5P/16S3P 21700 stack just fits a 3 L Wildman when you skip holders, while 13S4P assemblies barely squeeze into 2–3 L shells—plan for custom spacers, cardboard liners, and printed cages before drilling the pack.【F:knowledge/notes/denis_all_part02_review.md†L362-L363】【F:knowledge/notes/denis_all_part02_review.md†L165-L165】
- **Retire fatigued brackets.** Heavy 13S packs crack 3D-printed rear supports near the rear bolt; inspect and replace printed mounts routinely or swap to metal before pushing high-speed builds.【F:knowledge/notes/denis_all_part02_review.md†L352-L352】
- **Question oversized deck spacers.** Plastic trays that promise room for four Xiaomi packs rely on sparse M3 fasteners and flex under a 30 kg battery—plan metal reinforcement or decline the mod altogether.【F:knowledge/notes/input_part002_review.md†L407-L409】

### Layout Modeling Tips
- **Use planners as estimates, not gospel.** RePackr and e4bike.ru visualisers help brainstorm cell counts, but Artem still defaults to CAD or cardboard mockups for tight triangle packs and vertical stacking tricks.【F:knowledge/notes/input_part002_review.md†L415-L417】
- **Finish copper busbars properly.** Spray Kontakt 60, wear gloves, and seal stacks with Kapton, fish paper, and heat-shrink so copper “sandwich” joints do not corrode before the scooter ever rolls.【F:knowledge/notes/input_part002_review.md†L417-L417】

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
