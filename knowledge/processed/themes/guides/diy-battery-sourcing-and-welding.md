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
| **EVE 40PL prisms** | ≈€6–7 each in small quantities | Held 3.0 V for 62 s at 100 A while P45B sagged to 2.78 V after 44 s, making them the new benchmark for 20 kW+ scooters when packaging allows.[^21] | Require wider housings than 21700 cells—model pack volume and reinforce busbars before switching chemistries. |
| **ElectricPowa bulk lots (Spain)** | Samsung 50E ≈€3.20, Molicel P42A ≈€2.90 | Authentic surplus stock; pricing attractive for EU buyers | International shipping can erase savings—verify landed cost before importing to North America.【F:knowledge/notes/input_part008_review.md†L470-L472】 |
| **Liquidation Samsung 50E/M50LT modules** | ~$150 for 11 S10 P scooter bricks when liquidation hits | Provide turnkey 50E harnesses with BMS ready for harvesting | Move quickly—lots disappear fast and need full re-termination and QA before service.【F:knowledge/notes/input_part008_review.md†L15773-L15799】 |
| **Tenpower 40TG pilots** | Limited runs; early testers pulled ≈65 A per cell in 4 P blocks | Datasheet claims 40 A continuous; field tests pending for sustained packs | Budget for extensive thermal logging before embracing them for commuter duty.【F:knowledge/notes/input_part008_review.md†L19028-L19052】 |
| **Molicel XA-series prototypes** | Early race-focused 2.6 Ah cells (≈1.5–2 mΩ) | Previewed at 125 A charge / 250 A discharge envelopes—positioned between P45B and 40PL for burst power | Limited availability—budget validation packs and assume premium pricing until production ramps.[^25] |
| **Commissioned builds (UK/US)** | Varies; premium vs DIY delta covers tooling | Output tied to builder’s QC logs | Trusted builders like jamessoderstrom eliminate tooling spend for one-off packs.[^11] |

## Welding Equipment Decision Guide
| Scenario | Recommended Tooling | Why It Wins | Follow-Up Checks |
| --- | --- | --- | --- |
| First copper pack, limited budget | Rent/borrow K-Weld or Glitter kit | Proven to fuse 0.1 mm copper reliably versus unproven 90 € units | Inspect weld nuggets under magnification; rip-test samples before scaling.[^3] |
| Daily fabrication shop | Own Glitter 811A or K-Weld with high-current PSU | Handles repeated 4 kA+ hits when contacts are clean | Schedule bus pin cleaning to prevent E01 faults and maintain 4.4 kA output.[^10] |
| Mixed chemistries (pouch + cylindrical) | Use adjustable pulse welders with copper/nickel sandwiches | Controls heat on dissimilar tabs, minimizes swelling risk | Pair with upgraded ≥230 A BMS and temperature probes on parallel groups.[^6] |
| Budget capacitor welder (0.1–0.15 mm nickel) | Docreate DO-02 with pedal kit | Lands around $100 shipped, logs ~0.36 mΩ capacitor ESR, and ships with teardown videos vets used to validate wiring before use | Prefer the foot-pedal variant for thicker leads; Glitter 801D remains a fallback when copper is not required.[^docreate] |

## Pack Architecture Case Studies
| Platform | Layout & Cells | Controller Pairing | Lessons |
| --- | --- | --- | --- |
| Dual 70H race scooter | 22 S10/11 P P45B modules | MakerX G300 duals | Logs justify nearly 500 A continuous; plan dual-BMS or fuse strategy until 700 A-class boards exist.[^4][^7] |
| Dualtron Achilleus | 20 S8 P Molicel / 22 S9 P custom | Spintend 85250 relocated outside deck | Deck measures ≈48.5 cm × 18.1 cm—external controller mounting frees volume for ≥100 A batteries.[^4][^8] |
| Zero 10X deck extender | 20 S7 P 21700 (holderless) | Dual controllers relocated with custom wiring | Requires a 45 mm deck spacer, layered insulation, and carefully dressed harnesses to prevent chafing once the cavity is filled edge to edge.[^22] |
| Nami commuter upgrade | 22 S11 P pack with ≈8 mm deck riser | Awaiting high-current controllers | CNC + 3D-printed supports required; treat as modular sled to service 50PL packs and confirm riser clearance before cutting.【F:knowledge/notes/input_part008_review.md†L494-L497】[^12] |
| G3 30 S conversion | 30 S3 P modules (15 S6 P split) | High-voltage VESC | Requires grinding factory brackets; 30 S4 P too wide without chassis surgery and new BMS routing.[^13] |
| 20 S10 P Samsung 40T | Dual Ubox 85250 | 0.2 mm copper busbars deliver ~350 A continuous / 450 A burst; avoid mixing pouch cells in parallel due to swelling | Reserve space for ≥230 A BMS and monitor temps during 40 kW pulls.[^6] |
| Xiaomi Pro 2 internal max-out | 13 S8 P (≈1.15 kWh) with side-mounted BMS | ESC relocated to free deck depth | Holderless asymmetrical stacking fits 104 cells but demands meticulous insulation and harness rerouting.[^26] |

## Cost Planning Worksheet
1. **Cell procurement** – price the primary chemistry plus 10 % spares for grading losses and future replacements.[^2][^11]
2. **Interconnects & welding** – include copper/nickel, insulation, weld probe maintenance, and PPE alongside the welder cost or rental fees.[^3][^10]
3. **BMS & protection** – today’s compact boards cap around 500 A continuous; large packs may need dual-BMS or fuse-plus-charge solutions until 700 A hardware lands.[^7]
4. **Connectors & harnessing** – QS8 connectors, 8–10 AWG silicone wire, and panel mounts are trending upward in price due to tariffs—stockpile early.[^5][^9]
5. **Copper inventory** – Nickel-copper laminate pricing swung from ~€15 to €45 per roll within weeks and is climbing again alongside copper-strip inflation debates; secure stock ahead of builds or budget fallbacks that rely on pure nickel when costs spike.[^23】【F:knowledge/notes/input_part008_review.md†L16198-L16266】
6. **Enclosure & structural supports** – CNC plates, 3D spacers, and adhesives trump hot glue for 22 S builds; treat mechanical retention as part of the electrical budget.[^8][^14]
7. **Labor or outsourcing** – weigh the tooling investment against commissioning vetted builders when customs, shipping, or learning curves threaten schedules.[^11]

## QA & Maintenance Protocols
- **Thermal interface audits:** Log controller and stator temperatures on first shakedown runs; resurface heatsink plates and refresh thermal paste before chasing 400 A+ per motor.[^9]
- **Bench chargers with storage cycles:** Xtar’s VC8 only runs capacity/storage tests on slots 1–4 at 0.5 A, while the VC8S enables all eight bays at 1 A—budget for the S revision if you routinely condition whole 8 P strings.【F:knowledge/notes/input_part008_review.md†L302-L321】
- **Store surplus cells cold and half-full:** Builders parking spare P42A lots target ≈30 % state-of-charge and refrigerate packs to slow aging until welding begins.【F:knowledge/notes/input_part008_review.md†L414-L415】
- **Weld verification:** Rip-test sample strips each session, especially after cleaning Glitter bus pins, to confirm energy settings haven’t drifted.[^10]
- **Copper strip finishing:** Keep scissors pivoted near their hinge for leverage on 0.15 mm sheet, cut curves gradually, and flatten tabs with a rubber or soft-blow mallet before stacking so laminates sit flat without specialty shears; builders also radius every corner and pre-tin copper inserts before welding so sharp edges and dry joints can’t chew through insulation once the pack is strapped together.【F:data/vesc_help_group/text_slices/input_part009.txt†L1343-L1352】【F:data/vesc_help_group/text_slices/input_part009.txt†L1492-L1493】
- **Respect kWeld lead lengths:** A 1.2 kA overcurrent alarm traced back to using the wrong cable length—swapping to the recommended leads cleared the fault—so keep probe wiring within spec before blaming the control board.【F:data/vesc_help_group/text_slices/input_part009.txt†L1489-L1495】
- **Harness strain relief:** Use deck plates or external mounts to keep relocated controllers from stressing phase leads and QS8 connectors during pack swaps.[^8][^9]
- **Telemetry cross-checks:** Pair CAN smart BMS data with VESC logs to validate current draw and spot calibration drift in shunt-based readings.[^7]
- **Scale protection with pack size:** Large 20 S24 P builds now parallel two to three smart BMS boards so each unit handles a fraction of the discharge current instead of tripping mid-ride.[^24]
- **Skip “thermal foam” fillers.** Use small insulating pads just to stop rattles and leave air gaps so deck packs can still shed heat—solid foam cradles trap heat.[^27]
- **Expect permanent bonds from marine adhesives.** 3M marine sealant cures rock-solid; plan mechanical removal or fresh holders during rework and avoid relying on “peel-off” serviceability.【F:knowledge/notes/input_part008_review.md†L394-L395】
- **Plate or coat copper busbars.** Nickel-plating or zinc-rich sprays keep copper straps from corroding without giving up the low-resistance gains that motivated the material switch.【F:knowledge/notes/input_part008_review.md†L416-L419】
- **Feed welders with high-C LiPos, not car batteries.** Builders saw car batteries sag after a handful of strikes while CNHL 4S 9.5 Ah and similar high-C LiPos kept kWeld delivering 2 kA pulses without undervoltage faults; aging RC packs and USB power banks overheated even with extra heatsinks.[^kweld-lipo]
- **Template metalwork before welding.** A Hyosung battery box that missed the frame opening by 1 cm halted the project—dry-fit enclosures or mock with cardboard before cutting steel.[^28]
- **Reality-check fast-charge math.** 40 C claims demand ~11 kW even on 20 S6 P packs—far beyond 10 A home circuits—so plan industrial infrastructure for multi-minute fills.[^29]
- **Pick sealed charge ports for harsh weather.** IP67 Cnlinko LP16 connectors survive outdoor abuse, while XT60s remain adequate for 20 A indoor charging—select based on exposure.[^30]
- **Track import ceilings.** Turkey’s new €30 personal-import cap blocks direct orders of controllers, welders, and frames; expect 2–3× markups or work with licensed importers.[^31]
- **Program controllers for total series voltage.** Even when chaining two 10 S packs, configure VESC Tool for 20 S so cutoffs and telemetry match pack reality.[^32]
- **Vet welder QC aggressively.** Glitter 811H boards have arrived half-charged with dead MOSFETs; repair before trusting 0.2 mm copper claims, and remember kWeld overheats on repeated 0.15 mm copper sandwiches past ~75 J.[^33]
- **Pivot to TIG when resistance welders struggle.** Paolo now TIGs heavy buswork to avoid spot-welder sag and unlock thicker copper layouts at lower duty cycles.[^34]
- **Never grind reclaimed cells bare.** Grinding old nickel sparked instant thermal runaway in one shop; use chemical soaks or cold chisels instead of abrasive wheels.[^35]
- **Avoid mixing capacities without smart management.** Pairing LG 40T and M50LT strings in one parallel demands conservative currents and a smart BMS to keep the weaker chemistry in check.[^36]
- **Budget physical volume for smart BMS boards.** No-name “smart” boards can be twice the footprint of ANT units despite lower amp ratings, while the 21 S 100 A JBD still slips between 18650 rows at ~€45.[^37]
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
- **Retire leaky Navee packs.** Salvaged Navee N65 modules have shown leaking cells around 900 km; builders now plan full Aspilsan replacements or scrap the platform rather than risk venting packs.【F:knowledge/notes/input_part008_review.md†L359-L359】
- **Treat bargain “Ultrafire” packs as a structural hazard.** A fatal elevator blaze traced to an e-bike stuffed with dubious Ultrafire cells reminded the community to isolate DIY packs from living spaces, add vent paths, and respect condo/building bans before charging indoors.【F:knowledge/notes/input_part008_review.md†L601-L604】
- **Log Aspilsan thermal limits.** Early A28 tests hit >90 °C at 10–15 A while LG M26 cells on the same rig stayed near 40 °C—don’t parallel chemistries without temperature data.【F:knowledge/notes/input_part008_review.md†L15885-L15938】
- **Budget extra time for soldered salvage packs.** Military surplus modules arrived with soldered busbars and even fasteners, forcing full desoldering or dremel work instead of quick bolt removal.【F:knowledge/notes/input_part008_review.md†L395-L396】
- **Scrap waterlogged LG M26 stock.** Builders binned cells that took on water rather than risk corrosion-induced failures in new high-capacity packs.【F:knowledge/notes/input_part008_review.md†L518-L522】
- **Leverage welded 50E clear-outs.** Surplus Samsung 50E modules pre-welded for robots have dropped near $0.80 per cell when you buy 2,000+, making them worthwhile commuters after full inspection and re-termination.【F:knowledge/notes/input_part008_review.md†L500-L503】
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
[^21]: Patrick’s 100 A discharge logs showed EVE 40PL prismatic cells holding 3.0 V for 62 s while Molicel P45B packs sagged to 2.78 V after 44 s.【F:knowledge/notes/input_part008_review.md†L16-L16】
[^22]: Zero 10X builders fitting 20 S7 P packs plus dual controllers documented the need for a 45 mm deck extender, added insulation, and tightly managed wiring to avoid shorts.【F:knowledge/notes/input_part008_review.md†L13-L14】
[^23]: Community price tracking logged 0.1 × 200 × 5,000 mm nickel-copper laminate jumping from roughly €15 to €45 per roll in a matter of weeks.【F:knowledge/notes/input_part008_review.md†L17-L17】
[^24]: High-current motorcycle builds now run three BMS boards in parallel so massive 20 S24 P packs can share hundreds of amps without single-board cutoffs.【F:knowledge/notes/input_part008_review.md†L15-L15】
[^25]: NetworkDir previewed Molicel’s XA-series race cells at ≈2.6 Ah, ~1.5–2 mΩ, and 125 A charge / 250 A discharge capability as the next step beyond P45B once they reach production.【F:knowledge/notes/input_part008_review.md†L132-L133】
[^26]: GABE’s Xiaomi Pro 2 build squeezed a 13 S8 P pack (≈1.15 kWh) plus side-mounted BMS after relocating the ESC and carefully stacking cells without holders.【F:knowledge/notes/input_part008_review.md†L108-L109】
[^27]: Cihan’s hunt for thermally conductive foam ended with veterans recommending tiny insulating pads and open air gaps instead of dense foam blocks to avoid trapping heat around deck packs.【F:knowledge/notes/input_part008_review.md†L138-L138】
[^28]: PuneDir’s steel battery box missed his Hyosung frame opening by 1 cm, stranding the build and underscoring the need to template enclosures before welding or ordering heavy shells.【F:knowledge/notes/input_part008_review.md†L139-L139】
[^29]: Community fast-charge debates noted that 40 C fills on 20 S6 P packs would need roughly 11 kW from three-phase mains—far beyond household 10 A circuits—so “minutes-long” charges demand industrial power.【F:knowledge/notes/input_part008_review.md†L143-L143】
[^30]: Builders weighing charge ports recommended IP67-rated Cnlinko LP16 connectors for weatherproof installs, while others stick with XT60 for 20 A charging when water ingress is not a concern.【F:knowledge/notes/input_part008_review.md†L144-L144】
[^31]: Turkish riders confirmed a new €30 personal-import ceiling that blocks direct purchases of scooters, motors, and welders, forcing reliance on licensed importers or accepting 2–3× local markups.【F:knowledge/notes/input_part008_review.md†L147-L148】
[^32]: Yamal reminded builders to configure VESC Tool for the combined series count (e.g., 20 S) even when chaining two 10 S packs so telemetry and cutoffs remain accurate.【F:knowledge/notes/input_part008_review.md†L153-L153】
[^33]: Glitter 811H spot welders have arrived with dead MOSFETs and half-charged banks; after repairs they still weld 0.2 mm copper-on-nickel, while kWeld handles 0.15 mm copper around 75 J but overheats during continuous runs.【F:knowledge/notes/input_part008_review.md†L156-L158】
[^34]: Paolo shifted heavy pack fabrication to TIG welding with pulse controllers, arguing it avoids thermal sag and unlocks thicker bus work faster than resistance welders.【F:knowledge/notes/input_part008_review.md†L158-L158】
[^35]: Grinding nickel off reclaimed cells has already ignited cells—builders now avoid abrasive removal and document arc flashes from unstable Glitter welders to reinforce the fire risk.【F:knowledge/notes/input_part008_review.md†L159-L159】
[^36]: A Spanish NAMI rider paralleled LG 40T sticks with M50LT groups to extend range but now caps draw and leans on a 150 A smart BMS so the lower-capacity chemistry doesn’t overheat or drift out of balance.【F:knowledge/notes/input_part008_review.md†L188-L189】
[^37]: Budget “smart” BMS boards shipped twice the size of ANT units while the 21 S 100 A JBD still fits between 18650 rows and cost ~€45 during recent sales, making it the better fit for tight decks.【F:knowledge/notes/input_part008_review.md†L189-L189】
[^docreate]: Cihan priced the Docreate DO-02 capacitor welder around $108 delivered to Turkey (less with coupons) and confirmed ~0.36 mΩ capacitor ESR via teardown notes; peers recommend the foot-pedal bundle or Glitter 801D when welding only thin nickel.【F:knowledge/notes/input_part008_review.md†L398-L399】
[^kweld-lipo]: kWeld owners retired car batteries after a few welds sagged voltage; CNHL 4S 9.5 Ah hardcase packs and other high-C LiPos sustained 2 kA pulses while old RC packs and power banks overheated despite extra heatsinks.【F:knowledge/notes/input_part008_review.md†L237-L238】
[^denis-pricing]: 【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L1510-L1526】
[^common-port-chat]: 【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L1545-L1594】
[^m365krakow]: 【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L1612-L1618】
