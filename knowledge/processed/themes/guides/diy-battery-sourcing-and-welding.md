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

Regional sourcing realities still shape chemistry choices: Turkish builders blocked from NKON settle for Samsung 29E/50E lots despite higher sag, while racers keep paying for Molicel P45B as the only 21700 that resists brutal voltage droop at high current.【F:knowledge/notes/input_part005_review.md†L513-L513】 AliExpress flash sales still advertise fantasy pricing—message sellers for real quotes, expect shipping to erase the $6-per-cell clickbait, and stick with the one vetted vendor the community trusts when you cannot buy direct.【F:knowledge/notes/input_part005_review.md†L579-L579】

### 8–9 P Chemistry Trade-offs
- **P45B for brute force.** Choose Molicel P45B when the build needs 400 A+ bursts and minimal voltage sag; the premium pricing beats rebuilding packs that rely on mid-grade cells and cook under race duty.【F:knowledge/notes/input_part005_review.md†L605-L605】
- **P42A as the value pick.** P42A arrays still deliver stout 300–350 A performance for commuters and canyon riders, especially when paired with faster charging rather than upsizing parallel count.【F:knowledge/notes/input_part005_review.md†L605-L605】
- **Samsung 50S for range.** 50S and LG 50LT cells stretch 8–9 P packs for touring but expect more sag—pair them with conservative current limits or dual-pack fast-charging plans instead of chasing peak amps.【F:knowledge/notes/input_part005_review.md†L605-L605】
- **Budget chemistries need charge discipline.** Builders chasing LG M58 or Samsung 50E endurance budgets lean on higher-current chargers instead of premium cells; model turnaround times so clients understand the compromise.【F:knowledge/notes/input_part005_review.md†L605-L605】

## Welding Equipment Decision Guide
| Scenario | Recommended Tooling | Why It Wins | Follow-Up Checks |
| --- | --- | --- | --- |
| First copper pack, limited budget | Rent/borrow K-Weld or Glitter kit | Proven to fuse 0.1 mm copper reliably versus unproven 90 € units | Inspect weld nuggets under magnification; rip-test samples before scaling.[^3] |
| Daily fabrication shop | Own Glitter 811A or K-Weld with high-current PSU | Handles repeated 4 kA+ hits when contacts are clean | Schedule bus pin cleaning to prevent E01 faults and maintain 4.4 kA output.[^10] |
| Mixed chemistries (pouch + cylindrical) | Use adjustable pulse welders with copper/nickel sandwiches | Controls heat on dissimilar tabs, minimizes swelling risk | Pair with upgraded ≥230 A BMS and temperature probes on parallel groups.[^6] |

Glitter 811A/811H rigs promise 6 kA bursts with 35 mm² cables for 0.2 mm copper sandwiches, but early adopters still tear them down to resolder loose capacitors and confirm the shop has 110 V/220 V service before committing.【F:knowledge/notes/input_part005_review.md†L352-L354】

### Copper Busbars & Sandwich Welding Notes
- Laser-cut 0.5 mm copper combs (e.g., from Peng Chen) spot-weld cleanly when clamped under nickel-plated steel overlays, delivering neat 20 S 10 P layouts without bulky braided jumpers.【F:knowledge/notes/input_part005_review.md†L145-L147】
- Plan on ≥1 kA pulse capacity—KWeld or 1,600 A Malectrics rigs—to bond 0.2 mm copper reliably; hobby welders under the 1 kA mark struggle and drive builders back to nickel overlays.【F:knowledge/notes/input_part005_review.md†L147-L151】
- Practice on dead cells before committing copper-nickel sandwiches to live packs; slotted nickel forces current through the can and punishes misaligned welds.【F:knowledge/notes/input_part005_review.md†L488-L490】

## Pack Architecture Case Studies
| Platform | Layout & Cells | Controller Pairing | Lessons |
| --- | --- | --- | --- |
| Dual 70H race scooter | 22 S10/11 P P45B modules | MakerX G300 duals | Logs justify nearly 500 A continuous; plan dual-BMS or fuse strategy until 700 A-class boards exist.[^4][^7] |
| Dualtron Achilleus | 20 S8 P Molicel / 22 S9 P custom | Spintend 85250 relocated outside deck | Deck measures ≈48.5 cm × 18.1 cm—external controller mounting frees volume for ≥100 A batteries.[^4][^8] |
| Nami commuter upgrade | 22 S10 P layout in development | Awaiting high-current controllers | CNC + 3D-printed supports required; treat as modular sled to service 50PL packs.[^12] |
| G3 30 S conversion | 30 S3 P modules (15 S6 P split) | High-voltage VESC | Requires grinding factory brackets; 30 S4 P too wide without chassis surgery and new BMS routing.[^13] |
| 20 S10 P Samsung 40T | Dual Ubox 85250 | 0.2 mm copper busbars deliver ~350 A continuous / 450 A burst; avoid mixing pouch cells in parallel due to swelling | Reserve space for ≥230 A BMS and monitor temps during 40 kW pulls.[^6] |
| MH1 commuter rebuild | 20 S4 P aging pack → planned 20 S6 P 21700 swap | Makerbase 75100 single | Stock MH1 cells sagged from 80 % to 35 % under load; rebuilders are upsizing parallel count and logging rest voltage before landing the replacement BMS.【F:knowledge/notes/input_part005_review.md†L420-L422】 |

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
- **Respect connector ceilings.** XT90s plateau around 45 A continuous—plan QS8s, dual XT90s, or AS150/6 mm bullets plus matching cable gauge before commanding 100 A peaks.【F:knowledge/notes/input_part005_review.md†L311-L312】
- **Upsize single QS8 runs.** Treat lone QS8 battery leads targeting ~350 A as 6 AWG territory; dual-connector layouts can survive on 8 AWG, and no one trusts “100 A” claims on household wire for these peaks.【F:knowledge/notes/input_part005_review.md†L505-L505】
- **Match harness gauge to peak current.** 20 S 9 P packs chasing ~350 A bursts call for 6 AWG leads or dual 8 AWG runs, and true 500 A duty needs roughly 50 mm² conductors even if racers skate by with short leads.【F:knowledge/notes/input_part005_review.md†L456-L458】
- **Reference a QS8 harness chart.** Treat 300 A builds as 7 AWG/10 mm² territory, 400 A as 6 AWG/13 mm², and 500 A as 4 AWG/21 mm² when the leads stay under 30 cm; double up parallel runs or step to 35 mm² when the deck forces longer routing to keep voltage drop and connector temps in check.【F:knowledge/notes/input_part005_review.md†L604-L604】
- **Prefer disciplined CC-CV chargers.** Wate/YZPower bricks remain the dependable budget picks; adjustable lab supplies can overvolt packs if someone bumps the knob, so only use them with strict pre-ride voltage checks and healthy BMS safeguards.【F:knowledge/notes/input_part005_review.md†L447-L452】
- **Plan ahead for 20 S chargers.** Supply outside China is thin—shops stock adjustable lab supplies, run bricks in series, or wait on AliExpress shipments rather than overvolting 67.2 V units, and Xiaomi charge ports bottleneck around 3 A until you upgrade to XT60-class wiring.【F:knowledge/notes/input_part005_review.md†L321-L323】
- **Match externals perfectly.** When paralleling shoulder-bag booster packs (e.g., 20 S 4 P modules in 5 L Wildman bags), keep chemistry, capacity, and internal resistance aligned with the deck pack to avoid imbalance when you bridge them for a 20 S 8 P Ninebot build.【F:knowledge/notes/input_part005_review.md†L221-L222】
- **Treat bargain Daly boards as storage-only.** Daly BMS units that brown out under load have killed LiPo packs by dragging cells to 0 V—reserve them for stationary powerwalls and spec LLT/JK hardware for ride packs.【F:knowledge/notes/input_part005_review.md†L223-L223】
- **Inspect bulk shipments even when weld tabs look untouched.** Large P42A orders have arrived with cosmetic glue residue but intact insulation—photograph and document any damage before the cells ever touch a welder.【F:knowledge/notes/input_part005_review.md†L364-L365】
- **Do not spot-weld Samsung 33J U-cap cans.** Their foil caps arc immediately—swap chemistries instead of forcing them into scooter packs.【F:knowledge/notes/input_part005_review.md†L420-L421】
- **Never weld with the charger connected.** Builders have already blown inexpensive chargers by leaving them attached during spot-welding—disconnect mains gear before you energise the welder.【F:knowledge/notes/input_part005_review.md†L397-L397】
- **Double up insulation if you skip holders.** Custom honeycomb shells still leave ~0.4 mm gaps—wrap bare packs with kapton or fish paper before potting so vibration doesn’t abrade cells when hot glue is the only retention.【F:knowledge/notes/input_part005_review.md†L394-L395】
- **Telemetry cross-checks:** Pair CAN smart BMS data with VESC logs to validate current draw and spot calibration drift in shunt-based readings.[^7]
- **Finish work around positives:** Deburr nickel edges near cell tops and re-seat fishpaper before closing the pack—sharp tabs have already pierced insulation on low-current power-bank builds.【F:knowledge/notes/denis_all_part02_review.md†L122364-L122385】
- **Print holders for heat, not looks.** PLA cradles slump once cells warm; switch to PETG or ASA around 230 °C/100 °C bed temps so 21700 honeycombs and Wildman bag sleds stay rigid in summer decks.【F:knowledge/notes/denis_all_part02_review.md†L116230-L116236】【F:knowledge/notes/denis_all_part02_review.md†L89665-L89696】
- **Document capacity checks.** Time OEM chargers (≈1.7 Ah per hour on Xiaomi bricks) when vetting customer packs; a genuine 12 Ah module needs nearly seven hours from empty.【F:knowledge/notes/denis_all_part02_review.md†L98595-L98598】
- **Log cell provenance.** Refurb lots from NKON (late-2021 Samsung 35E/50E) arrive graded and safe when treated like fresh stock; track batch codes and keep compression on pouch experiments so swelling doesn’t lift tabs.【F:knowledge/notes/denis_all_part02_review.md†L97241-L97259】
- **Plan disposal with reclaimed cells.** Dyson vacuum tear-downs still yield usable P42A modules, but U.S. builders lack convenient lithium drop-offs compared with EU mall programs—budget safe storage and recycling runs when culling weak cells.【F:knowledge/notes/input_part005_review.md†L458-L459】

### Mounting & Housing Patterns
- **Prototype harness guides cheaply.** Builders mock up deck layouts with cardboard brackets before printing TPU/PETG fixtures, weighing Bambu P1P versus Ender 3 SE ownership while outsourcing large ASA/PEEK parts to avoid €1,500 machines.【F:knowledge/notes/input_part005_review.md†L11-L14】
- **Print in-place frames for strength, not speed.** Print-in-place battery sleds need 100 % infill PETG (or stronger) plus fiberglass skins—low-infill PLA softens in the sun and won’t protect the pack in a crash.【F:knowledge/notes/input_part005_review.md†L221-L222】
- **Armor deck-mounted conduits.** Twin 10S packs strapped along the deck need metal shielding and permanent wiring—open conduit runs are “self-propelled bombs” unless the housing resists impacts and stays wired for continuous duty.【F:knowledge/notes/denis_all_part02_review.md†L230-L234】
- **Overbuild bag brackets.** Wildman bag packs now use eight screw/wide-washer mounts, fiberglass sleeving, and interior foam so cells can’t chafe on hardware or eject during pothole hits.【F:knowledge/notes/denis_all_part02_review.md†L361-L362】
- **Expect tight tolerances.** A 13S5P/16S3P 21700 stack just fits a 3 L Wildman when you skip holders, while 13S4P assemblies barely squeeze into 2–3 L shells—plan for custom spacers, cardboard liners, and printed cages before drilling the pack.【F:knowledge/notes/denis_all_part02_review.md†L362-L363】【F:knowledge/notes/denis_all_part02_review.md†L165-L165】
- **Account for honeycomb growth.** Printed honeycomb holders add roughly 3 cm to a 20 S stick thanks to 1.5 mm walls—verify deck clearance and inspect any shipped pack with crushed heat-shrink or stray metal before trusting it on a ride.【F:knowledge/notes/input_part005_review.md†L501-L501】
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
