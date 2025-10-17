# Segway Platform Dossier

## Overview

Segway produces a range of electric scooters from entry-level commuters to sport platforms, with the G30 (Ninebot Max) and GT-series representing the most popular upgrade platforms. This brand dossier covers Segway/Ninebot models including the G30, GT1/GT2/GT3, P100, C80, F-series, and upcoming ST-series, examining stock configurations, upgrade potential, common issues, and best practices. Segway platforms offer stable geometry and good parts availability, making them solid foundations for VESC conversions.

## What You'll Learn

- Model comparison and platform selection
- Stock electrical architectures and upgrade paths
- G30 (Max) VESC conversion considerations
- GT-series mechanical limitations and fixes
- Rental frame recovery and reconditioning
- C80 seated platform for high-capacity builds
- Common failure points and reinforcement strategies
- When Segway platforms justify their popularity

# Segway Platform Dossier

- Segway's G- and GT-series frames still anchor the community's "minimum viable" commuter and sport builds thanks to stable geometry, roomy decks, and a deep spare-parts ecosystem, but every chassis demands reinforcement checks around stems, braces, and controller mounts before accepting more power.[^1][^2]
- North American shoppers still treat the Xiaomi Pro 2 and Segway G30 as the entry-level commuter floor; Segway F-series and supermarket clones arrive with weak frames, sensorless motors, and limited spares that rarely justify upgrades.[^1]
- GT-class scooters ship with a 14 S 12 P Lishen pack, single-MCU 24‑FET controller, 10 AWG phase leads, and adjustable suspension hardware—good bones that tolerate 70 km/h stock and 100 km/h+ once packs, bearings, and stem hardware are upgraded, yet stem bearings, axle machining, shock packaging, and deck cooling must be addressed up front.[^3][^4][^5][^6][^gt_shock][^gt_teardown]
- Segway's seated C80 platform and forthcoming ST line show the brand stretching into moped territory: C80 conversions already hide 9 kWh packs and 6–7 kW charging while ST2 prototypes promise factory 72 V drivetrains, making Segway a rare OEM path from commuter scooters to turn-key high-voltage builds.[^11][^12][^13]
- Rental-grade Ninebot G30 frames arrive overbuilt with added mass, red thread-lock, and MJ1 packs; recovering them means reviving deeply discharged cells whose rental BMS prioritized telemetry over protection, so plan cell reconditioning before upgrades.[^2][^3]
- Segway's seated C80 platform and forthcoming ST line show the brand stretching into moped territory: C80 conversions already hide 9 kWh packs and 6–7 kW charging, while the ST1 keeps a straight fork for ~40–50 km/h commuters and the ST2 steps to a 72 V drivetrain aiming near 85 km/h with factory hydraulics.[^11][^12][^13]
- For Ninebot Max builds, Denis Yurev's crew now steers riders toward a single 13 S pack on the stock motor paired with Rita/Happy BMS current logging instead of chasing dual hubs—quality pneumatics and Monorim + DNM suspension upgrades keep 50 km/h conversions stable while foam "solid" tires are blamed for magnet failures.[^new-13s][^new-suspension]
- Fleet SNSC 2.3 frames are drying up as operators pivot to Okai hardware, so builders keen on rental-grade donors are scouting Brussels, Düsseldorf, and bulk fleet deals before stocks disappear.[^4]


## 🏆 Why Choose Segway/Ninebot?

✅ **Parts availability**: Best aftermarket support
✅ **Stable geometry**: Proven commuter platform
✅ **VESC documentation**: Extensive conversion guides
✅ **Entry-level friendly**: G30 is beginner-friendly

## 📋 Platform Comparison

| Model | Stock Pack | Best For | VESC Difficulty | Max Voltage |
|-------|------------|----------|-----------------|-------------|
| G30 (Max) | 36V, 551Wh | Commuter base | ⭐ Easy | 13S (48V) tested |
| P100 | 52V, 1.2kWh | Longer range | ⭐⭐ Medium | 16S possible |
| GT1/GT2 | 60V, dual hub | Performance | ⭐⭐⭐ Complex | 20S+ |
| C80 (seated) | 60V+ | High capacity | ⭐⭐⭐⭐ Advanced | 24S tested |

💡 **Pro Tip**: The G30 is the most documented VESC conversion platform. Start here for your first build.

## ⚠️ Critical G30 Warnings

🔴 **Foam tires shake magnets loose** - Switch to pneumatic
🔴 **Frame welds crack under overload** - Reinforce stem
🔴 **Stock controller mount is weak** - Add bracing

## 🔧 Related Brand Dossiers

- [VSETT Scooters](vsett.md) - Performance alternative  
- [Denis Yurev Workshop](denis_yurev_workshop.md) - Rita battery expansion for Xiaomi/Segway

## Platform Map

| Model | Stock Electrical Architecture | Known Strengths | Critical Watchpoints | First-Line Upgrades |
| --- | --- | --- | --- | --- |
| Ninebot/Segway G30 (Max) | 36 V, ~551 Wh pack, single hub | Proven commuter baseline with abundant parts and CAN documentation; stock hub holds 40–45 km/h once paired with 13 S packs and sane 30–40 A tunes.[^1][^new-13s] | Frame welds at the folding joint and controller mounts can crack when overloaded; F-series siblings share weaker weld quality and foam "solid" tires shake magnets loose.[^14][^new-suspension] | Bushing and bearing refresh, deck sealing, quality 10-inch pneumatics, and staged voltage/current increases with thermistor logging.[^2][^new-suspension] |
| Ninebot P100 | 52 V 23 Ah pack (~1.2 kWh), single hub | Factory-stiff chassis with upgraded cockpit hardware that shares parts with G30 customs.[^p100] | Stock pack only returns ~25 mi at 30 mph and feels firmware-limited; budget for range mods before chasing speed.[^p100] | Start with battery upgrades and efficiency logging alongside stem swaps so handling gains aren’t undermined by range anxiety.[^p100] |
| Segway GT1/GT2 | 14 S 12 P Lishen pack (~60 V), single 24‑FET controller, dual 1 400 W hubs | Stable 1.5 m wheelbase, 2.42 mm rotors, roomy bay for aftermarket controllers; holds 70 km/h to ~10 % SOC stock.[^3][^4][^5] | Fragile upper stem bearing; both axles need machining for larger hubs; rotor and shock packaging limit brake/tire swaps without spacers; deck reinforcement needed above 8–10 kW pulls.[^2][^6][^gt_shock] | Repaste controller, add Hope V4/DOT brakes, log pack sag, machine axles for 65–70 H hubs, add thermal plates.[^3][^4][^6] |
| Segway GT3 / GT3 Pro | 48 V (base) or 72 V (Pro) packs with deeper chassis | Retains GT steering geometry while offering more enclosure depth on the Pro for higher-voltage packs.[^6] | Base GT3 keeps cramped bay and legacy controller; both trims still require dropout/brake mods for high-power hubs.[^6] | Start with dropout widening, axle machining, and brake upgrades before chasing higher voltage.[^6] |
| Segway C80 seated scooter | 16 S stock pack, drum brake rear hub | 165 mm dropout accepts threaded 10" hubs; interior swallows four 6×10 cell layers and supports 6–7 kW charging with stock 100/100 Lite controller.[^10][^12] | Stock 60 A BMS will trip above 70 A battery; curb weight balloons toward 350 lb with 32 P packs, hurting handling.[^11] | Upgrade BMS before raising battery current, notch shock bracket for cleaner pack fit, add thermal monitoring, plan weight distribution.[^10][^11][^12] |
| Segway ST1/ST2 (announced) | Targeting 60 V (ST1) and 72 V (ST2) systems | Factory hydraulic suspension and higher-voltage electronics promise turnkey 40–85 km/h readiness.[^13] | Pricing and aftermarket support unknown; expect premium cost and limited early spares.[^13] | Monitor launch hardware; plan accessory/BMS support from GT ecosystem where compatible.[^13] |

## Ninebot F2 Pro Specific Notes

- ScooterHacking Firmware users confirmed that fully sensorless launches are acceptable—the initial "brr" noise is simply the controller switching from hall emulation—and this firmware path unlocks speed ceilings without sacrificing factory indicators and buzzers.[^f2pro-shfw]
- The F2 Pro's stock over-current protection trips near 30 A even if higher limits are set in the utility app, so riders planning power upgrades must accept this hardware ceiling or plan controller swaps.[^f2pro-ocp]
- Because the F2's BMS cannot detect externally paralleled packs, riders planning add-on batteries were advised to share current through the auxiliary pack while respecting the native 25–30 A ceiling to avoid tripping the internal protection mid-ride.[^f2pro-limits]
- Firmware updates bumped the Ninebot F2 Pro fast-charge ceiling from roughly 2.4 A to 3.2 A, but the crew still warns against 5–6 A experiments until the BMS proves it can dissipate the extra heat.[^5]
- Commuter builds should keep current demands below 30 A and leverage sensorless mode for reliable launches rather than chasing dual-motor complexity on this entry-level platform.[^f2pro-shfw][^f2pro-limits]
- F2 Pro front hubs ship nearly dry—open the wheel, repack the 6001RS bearings with polyurea or marine grease, and swap in SKF RSH 2RS hardware instead of smearing silicone on the caps, which only drags on the races.[^6]
- Ninebot F-series hubs still spin on 6203 bearings; stock a quality SKF/Koyo/Nachi/NSK set during the first teardown because OEM parts are treated as disposable wear items.[^7]
- The platform’s smart BMS enforces roughly 2.4 A charge current; adjustable chargers set higher simply shut off mid-session.[^8]
- Keep F2 Pro pressures realistic—Cihan’s 46/48 psi slide on polished asphalt prompted the crew to drop a few PSI for wet grip while remembering worn CST casings and rain still erode traction, so log surface conditions alongside pressure changes.[^9]

## Chassis & Handling Insights

- GT-class stability stems from generous wheelbase and rake, but riders still reinforce the deck and stem interfaces before high-power conversions; controller-mount fractures have occurred on GT and SNSC rental frames when extra weight is added up the stem.[^3][^2]
- Ninebot G2 owners are already replacing the fragile stock suspension arms with beefier forks that even leave room for a second 65 H motor, treating the larger frame as a better city platform than the legacy G30 once reinforced.[^g2_arm_swap]
- G30D v2 stems drop into Max builds with thicker latches, and hybridizing P100 stems demands precise cutting plus inner/outer welds that tighten turning radius while stiffening the cockpit; keep an “eco mode” profile handy for roadside legality checks when officers inspect power settings.[^stem_swap]
- Stem bearings and dropout machining are mandatory on GT2 upgrades: the OEM upper bearing fails early and both axles need lathe work before 65–70 H hubs will seat properly, and Hope V4 calipers require rotor spacers plus shock-clearing brackets to avoid fouling the trailing arm.[^6][^gt_shock]
- Crashed GT2 stems continue to shear and OEM spares remain scarce, so rebuilds lean on aftermarket dampers and even Zoom EZ MTB bleed kits to tighten the cockpit while parts trickle in.[^10][^11]
- Rotor diameter tops out near 140 mm without trimming the trailing arm; larger discs and reservoir shocks demand custom brackets or welded arms even on long-wheelbase GT frames.[^gt_packaging]
- Foam-filled "solid" tires vibrate enough to loosen magnets and shake packs apart on high-speed G30 conversions—pair quality 10-inch pneumatics with a Monorim front fork and DNM rear damper, or Sharkset forks if you stay below ~45 km/h.[^new-suspension]
- Monorim setups need tuning: Mirko’s G30 build settled on 250 lb EXA 291R shocks for ≈95 kg riders and a steering damper to quash 55 km/h wobbles once the vertical hinge hardware is torqued correctly.[^12]
- Builders chasing GT acceleration are already machining thicker stainless dropouts and custom Monorim plates so Xiaomi-class forks can fit ever-wider hubs without tearing the swingarm.[^13][^14]
- Max G2 owners are machining swingarm extensions to swallow larger rear hubs while keeping 20 S 5 P packs inside the frame with only a 2 mm spacer—proof the chassis can host sleeper upgrades without external battery boxes when fabrication time is budgeted.[^15]
- 130 kg riders have cracked G30 swingarms at the deck cut-outs; fabricators are modelling reinforcement plates that spread load around the rear fork bracket before stacking more power into the chassis.[^g30-swingarm]
- Grinding G30 forks for 11″ tires weakens the structure; veterans add triangulated reinforcement or welded plates instead of relying on hollow webbing after clearancing the castings.[^16]
- F-series and budget Segways exhibit rough welds and cracked deck braces near the folding joint, so inspections, gussets, or protective film are prerequisites for commuter-duty reliability.[^14]
- When reworking folding joints that were epoxied from the factory, strip the assembly, heat the glue thoroughly, and only then press components apart to avoid cracking the stem casting or leaving hidden voids.[^17]
- C80 riders note the stretched saddle forces a forward hunch; taller bars or switching foot placement onto the passenger pegs straightens posture for long rides.[^18]
- Rear-end stability improves when builders bend a 10 mm aluminum rod under the axle nut to brace wide mudguards; swapping in full-width G30 fenders (~11.5 cm) keeps 2.5″ tires from blasting commuters with spray.[^19][^20]

## Powertrain & Upgrade Guardrails

- Stock GT electronics (14 S 12 P pack, single 24‑FET controller, 10 AWG phases) support reliable 70 km/h operation; pushing past 8–10 kW demands deck stiffening, improved dampers, and monitored pack sag to avoid chassis fatigue.[^3][^2]
- Ninebot Max G2 motors shed heat no better than legacy G30 hubs, so serious power targets still rely on larger hub swaps; even throttle detection needs a full sweep in VESC Tool to keep hall checks from failing during setup.[^21][^22]
- 2.42 mm rotors and Hope V4 calipers are proven upgrades for repeated high-speed stops; the thicker discs avoid the warp-prone 1.8–2.0 mm hardware common on smaller scooters.[^3][^5]
- Segway GT2 riders log 70 km/h down to ~10 % SOC on the factory setup; pushing beyond that range requires higher-current packs or field-weakening, so plan for thermal headroom if adding torque or speed.[^4]
- Track officials now ban external battery bags at 100 km/h events because loose packs eject and ignite in crashes—serious GT/G-series builds need fully integrated compartments before showing up to scrutineering.[^23]
- Advertised 6 kW GT2 figures stem from brief inverter-side peaks and field-weakening—expect ~65–70 km/h stability stock and treat triple-digit ambitions as field-weakening experiments until higher-voltage packs or rewound hubs are fitted.[^24][^25]
- Geared hubs like the Navee S65 add torque for heavier riders but introduce noise and mechanical complexity, so set expectations before recommending them over proven direct-drive swaps.[^s65]
- High-power GT conversions now prove out 22 S8 P P42A trays (~485 × 210 × 86 mm), 400 A ANT BMS installs, QS10/QS8 leads, dual motor NTCs, and 155 mm×3.1 mm rotors with Hope V4 calipers; plan enclosure depth, rotor spacing, and wiring clearances before committing to 20 kW-class builds.[^gt_packaging]
- C80 conversions must respect the stock 60 A BMS limit until upgraded—attempting 70 A battery trips protection and heats the motor to ~76 °C, reinforcing the need for a higher-current BMS before raising output.[^11]
- Konyk rear-motor kits ship with replacement axle nuts, smoothing hub swaps when OEM hardware is discontinued or chewed up during teardown.[^26]
- New firmware paths let Ninebot G2 owners stay on the stock controller—flash XiaoDash, apply the SHFW Gen 4 patch, and keep factory blinkers/buzzers while lifting the speed ceiling instead of grafting in a G30 ESC.[^g2-shfw]
- Ninebot F2 Pro commuters see ~45 km/h once SHU firmware and field weakening are active, but the low-kV hub sags below 65 % SOC and traction control earns its keep on icy mornings even when summer riders disable it.[^f2pro_fw]
- SHU firmware riders confirmed the F2 Pro happily launches sensorless—the startup “brr” is normal hall emulation—but the stock over-current trip still fires near 30 A, so parallel add-on packs must share current through the auxiliary harness while staying inside the native 25–30 A envelope to avoid mid-ride shutdowns.[^27]

## Thermal & Controller Packaging

- Grinding paint to bare metal, adding thermal glue, and clamping controllers to aluminum plates keeps GT decks below ~60 °C; PETG brackets alone trap heat and left some builds idling at ~64 °C.[^7]
- Smart Repair’s Ninebot G2 retrofit keeps controller temps below 50 °C by stripping paint at the mount, buttering both sides with thermal paste, and sandwiching a 50 × 100 × 10 mm aluminum slab between the frame and ESC before torquing it down.[^28]
- Ferrofluid refreshes on Segway hubs should be sparing (2.5–3 ml for 10–11" shells) and paired with dedicated temperature probes because shell temperatures lag winding heat when current climbs.[^8]
- Deck volume fits Ubox Lite, 85/240, or MP2 controllers; a stock GT2 can even mount an 85240 on the rear wall once insulation is removed—plan pass-throughs and strain relief before closing the deck.[^7]
- Segway GT decks sag under multi-kilowatt pulls, so add aluminum spreaders or belly plates when doubling controller power, mirroring the community’s 3 mm laser-cut solutions.[^2][^9]

## Battery & Charging Strategy

- Smart Repair’s Kaabo GT pack blueprint logs about 12 V sag at 500 A phase on a self-built 20 S 9 P Eve 40 module with a 550 A-rated BMS, reinforcing why he stacks three 0.2 mm copper sheets over the nickel busbars while planning a 22 S successor once the front hub jumps to 65 H hardware.[^29]
- Pending: Log Jerome’s GT2 road tests once the 20 S 9 P pack, 100Balance BMS, and Smart Repair harnesses finish commissioning so range and thermal data can be folded back into Segway guidance.[^jerome-gt2]
- Extreme G30 conversions stacking twin MP2s now model 20 S 12 P bricks roughly 14.5 cm tall with the smart BMS standing vertically at the pack’s nose and parallel QS8/8 AWG leads feeding a welded rear controller box so the deck arches stay intact.[^g30-blueprint]
- C80 owners have demonstrated ~6–7 kW charging through the stock 100/100 Lite controller at mid-pack SOC, keeping compact scooters viable if thermal paths are improved.[^12]
- Group rides now haul 6 kW Hyper Chargers and EV adapters, but Jason’s pack still bottlenecked charge rate while the pedestal had headroom—set current at the charger or pack rather than assuming infrastructure is the limit.[^30]
- A lightly used Ninebot Max G2 pack with roughly 50–60 indoor-stored cycles provides a baseline for evaluating second-hand batteries before committing to upgrades.[^31]
- Segway-based mopeds with 32 P Samsung 35E packs weigh about 350 lb before the rider yet return ~70 mi, highlighting the trade-off between range and maneuverability; builders now favor lighter 32 S 20 P layouts with higher-power controllers for better torque-to-weight balance.[^11]
- Field deployments show stock GT rotors and brakes survive repeated high-speed runs once cooling and hydraulic upgrades are in place, but pack reinforcements remain essential to avoid sag-induced cut-outs.[^3][^9]
- G30 dashboards only expose 5 V logic—run dedicated DC/DC converters for 12 V lighting, stress-relieve converter leads, and avoid pulling accessory power from charge ports to preserve BMS protections.[^32][^33][^34]
- Happy BMS happily manages packs larger than its nominal 32 Ah rating—the display just hits 0 % with ~3 Ah remaining—but its 44 A ceiling is fixed, so AWD ambitions still need Daly/ANT-class boards before targeting 3 kW outputs.[^35][^36]
- Fleet refurb techs lean on Digikey part numbers WM20246-ND (socket) and WM19542-ND (plug) when rebuilding Ninebot Max charge ports that arrive without hardware.[^37]
- Upsizing G2 packs to ~38 Ah pushes charge times to ~13 h on the stock 3 A brick and ~7.5 h on vetted 5 A chargers; Denis stopped bundling chargers in 2025, so plan for third-party CC/CV supplies within those limits.[^38]
- When the G30 accessory port shows 5 V with almost no current, trace the wiring to the onboard buck converter before swapping looms—faulty components between the converter and port have caused the same symptom in workshop diagnostics.[^39]

## Maintenance & Reliability Watchlist

- Inspect GT controller mounts and stem hardware for cracks after hard hits; SNSC rental frames with similar architecture fractured at controller mounts under off-road abuse—especially when handlebar battery packs added leverage—reinforcing the need for gussets and to relocate auxiliary packs off the bars before returning a frame to service.[^40]
- Ninebot winter fender STLs keep salty slush off controllers—print with PETG/ASA, add stainless fasteners, and inspect after storms for cracks before the next commute.[^41]
- Replace bearings proactively—GT rotors pair well with quality SKF replacements, and C80 builds benefit from upgraded hubs or temp probes to keep long commutes in check.[^5][^8][^10]
- G-series commuters require bushing and weld inspections; F-series weld porosity has already caused brace cracks, so reinforcements and protective films are recommended before heavy use.[^14]
- Run a dedicated F-series weld checklist before adding power: inspect the deck spine, folding brace, and downtube gussets for porosity, add polyurethane or UHMW film where harnesses rub the welds, and torque the folding bolts with medium-strength threadlocker after reassembly.[^42]
- Stress-relieve buck-converter leads with glue or zip ties so vibration does not snap accessory power wires before the scooter ever leaves the bench.[^33]
- GT-series rims can be replaced without swapping hubs—AliExpress sells “rim only” shells, but verify the motor is healthy before reusing it on fresh hoops.[^43]

## Accessory & Telemetry Integration

- Segway CAN dashboards diverge from Xiaomi formats, so confirm message maps before layering SmartDisplay overlays or Express telemetry; VESC Express station mode eases remote access once the scooter joins home Wi‑Fi.[^2][^15]
- GT2 dashboards still lack a published protocol—expect to sniff frames or source donor hardware until Segway releases message catalogs, and plan to convert captures into Lisp scripts for SmartDisplay once hardware access is available.[^44]
- Stock G30 throttles and dashboards expect 3.3 V logic when paired with MakerX/Segway conversions—miswiring 5 V rails has already blown logic boards, so verify accessory voltage before powering OEM controls.[^16]
- ADC horn outputs on Segway conversions only source a couple of amps; route lighting and horn loads through a dedicated DC/DC converter and use the controller for signaling only.[^17]

## Procurement & Roadmap Signals

- Upcoming ST1/ST2 models are expected to sit above GT pricing with factory hydraulics and 72 V options, making them potential turnkey platforms for riders who want OEM-grade frames before VESC swaps.[^13]
- Veteran builders are even selling Thunder-class hardware to pivot onto Ninebot G2s for family use, treating the G2 as a calmer daily while keeping high-power Nami projects for personal builds.[^g2_family_pivot]
- Before recommending premium-looking Segway P-series or NIU/Nami alternatives to family, confirm aftermarket parts availability—community veterans warn support lags behind the proven G-series/Xiaomi ecosystem.[^45]
- Segway’s widespread aftermarket support keeps GT and G-series parts available, but heavier GT builds still require machining (axles, rotors, spacers) and thermal rework, so budget workshop time alongside electronics upgrades.[^4][^10]
- Mid-tier dual-motor imports (Dualtron, Vsett, Zero) still demand controller overhauls despite high resale pricing; Denis’ crew often steers buyers toward sleeper G30/G2 builds with 13 S/35 A tunes that hold 40–45 km/h while remaining discreet and mechanically robust.[^dual-motor]
- Denis still cannot export lithium packs outside the EU; overseas owners order Rita and bags separately, then lean on VTA, Scootermode, or local builders for compliant battery packs.[^46]

## Source Notes

[^1]: Community consensus on Segway G30 viability and F-series weaknesses for North American commuters. Source: knowledge/notes/input_part006_review.md, L45 to L48
[^2]: GT deck sag, stem reinforcement needs, and SNSC frame fracture anecdotes under high load. Source: knowledge/notes/input_part003_review.md, L285 to L288
[^3]: Segway GT teardown showing 14 S 12 P pack, 24‑FET controller, and braking upgrades with Hope V4 hardware. Source: knowledge/notes/input_part003_review.md, L232 to L233
[^4]: Kirill’s GT2 ride log documenting 70 km/h stock performance and rotor clearance for 180 mm Magura setups. Source: knowledge/notes/input_part002_review.md, L188 to L188
[^5]: Measurement of GT2’s 2.42 mm six-bolt rotors as an upgrade over commuter-class discs. Source: knowledge/notes/input_part006_review.md, L357 to L357
[^6]: GT2 stem bearing fragility, axle machining requirements, and GT3 chassis comparisons. Source: knowledge/notes/input_part011_review.md, L439 to L441
[^7]: Guidance on grinding deck paint, adding thermal glue, and mounting Ubox/MP2 controllers in Segway GT bays. Source: knowledge/notes/input_part012_review.md, L92 to L92
[^8]: Recommendations for sparing ferrofluid application and temperature-probe installs on Segway hubs. Source: knowledge/notes/input_part012_review.md, L191 to L191
[^9]: GT pack sag under 500 A phase and copper busbar reinforcement details for future 22 S upgrades. Source: knowledge/notes/input_part011_review.md, L467 to L469
[^g30-blueprint]: Twin MP2 conversions stack 20 S 12 P bricks to roughly 14.5 cm, stand the smart BMS vertically up front, and split current across parallel QS8/8 AWG harnesses while a welded rear controller box preserves the deck arches. Source: data/vesc_help_group/text_slices/input_part009.txt, L21845 to L21939
[^jerome-gt2]: Pending GT2 range/thermal validation once Jerome finishes commissioning the 20 S 9 P pack with Smart Repair’s harness and a 100Balance BMS. Source: knowledge/notes/input_part011_review.md†L911-L911
[^10]: Segway C80 battery packaging, dropout dimensions, and retained drum/sprocket hardware for future drivetrain swaps. Source: knowledge/notes/input_part012_review.md, L340 to L341
[^11]: Weight, BMS limits, and range benchmarks for Segway-based moped builds with 32 P Samsung 35E packs. Source: knowledge/notes/input_part012_review.md, L324 to L327. Source: knowledge/notes/input_part012_review.md, L343 to L344
[^12]: C80 fast-charge validation (≈6–7 kW) on the stock 100/100 Lite controller. Source: knowledge/notes/input_part012_review.md, L266 to L266
[^13]: Overview of Segway’s upcoming ST line noting the ST1’s commuter fork and the ST2’s 72 V target near 85 km/h. Source: knowledge/notes/input_part006_review.md, L421 to L421
[^14]: F-series weld inspections and reinforcement reminders before heavy-duty use. Source: knowledge/notes/input_part006_review.md, L408 to L409
[^p100]: Ninebot P100 teardown and range report showing the 52 V 23 Ah pack only returns ~25 mi at 30 mph despite the stiffer chassis and shared cockpit hardware with G30 builds. Source: knowledge/notes/input_part003_review.md, L701 to L748
[^stem_swap]: Rosheee’s stem upgrade log covering thicker G30D v2 latches, P100 hybrid welding steps, and SNSC controller-mount failures when handlebar battery packs add leverage. Source: knowledge/notes/input_part003_review.md, L705 to L748
[^s65]: Navee S65 geared-hub teardown outlining added torque, noise, and service complexity versus direct-drive swaps. Source: knowledge/notes/input_part003_review.md, L701 to L746
[^gt_dash]: GT2 dashboard integration gaps requiring protocol sniffing or donor assemblies before CAN overlays function reliably. Source: knowledge/notes/input_part003_review.md, L744 to L745
[^15]: SmartDisplay CAN overlay and VESC Express station-mode networking guidance for Segway dashboards. Source: knowledge/notes/input_part003_review.md, L304 to L308. Source: knowledge/notes/input_part012_review.md, L100 to L101
[^16]: MakerX footpad and dashboard wiring expectations around 3.3 V logic on Segway conversions. Source: knowledge/notes/input_part012_review.md, L349 to L349
[^17]: Limits of ADC horn outputs on Makerbase/Spintend harnesses used in Segway conversions. Source: knowledge/notes/input_part012_review.md, L96 to L97
[^g2-shfw]: Source: knowledge/notes/denis_all_part02_review.md, L149 to L153
[^dual-motor]: Source: knowledge/notes/denis_all_part02_review.md, L191 to L193
[^g2_family_pivot]: Source: data/vesc_help_group/text_slices/input_part011.txt, L20969 to L21013
[^new-13s]: Guidance from Denis Yurev and Happy Giraffe to favor a single 13 S Max pack on the stock hub, logging 30–40 A pulls with Rita/Happy BMS rather than chasing dual-motor swaps. Source: knowledge/notes/denis_all_part02_review.md, L10 to L12
[^new-suspension]: Community consensus against foam “solid” tires and in favor of quality 10-inch pneumatics with Monorim front/DNM rear suspension for 50 km/h Ninebot builds; Sharkset forks remain comfortable but wobble above ~45 km/h. Source: knowledge/notes/denis_all_part02_review.md, L13 to L14
- **Stack external packs only with BMS parity.** Pairing a stock 10 S G30 pack with a DIY 4 S extender demands healthy BMS boards charged to similar voltages; the stock pack still clamps around 20 A, and VESC detection fails until proper voltage support restores power.[^pack_stack]
- **Expect 45–48 km/h from dual-motor G30s at 48 V.** Riders warned that voltage headroom is generous (enamel withstands kilovolt spikes), but phase amps cook motors—75100 builds stay around 70 A battery / 150 A phase to avoid smoking stators.[^dual_g30_speed]
- **Set 20 S G30 cutoffs near 56.5 V (~2.85 V/cell) to ride through sag.** This value keeps dual stock packs alive under load while bypassed BMS boards stay clear of 2.5 V absolute limits.[^g30_cutoff]
- **Dual-stock Ninebot packs fit with tall spacers and flipped SNSC suspension.** Builds using 80 mm hardware, 3D-printed deck risers, and inverted SNSC brackets net ~6 cm ground clearance so two OEM packs plus externals ride without scraping.[^dual_pack_fitment]
- **Ninebot hub thermal ceiling is ~40–45 A battery.** Paolo confirmed OG Ninebot motors burn above this threshold even on 20 S—cap phase/battery settings and resist feeding dual 15 A controllers continuous load without upgraded hubs.[^ninebot_thermal]
- **F-series stems bend under load.** The elongated aluminum steering tube will bend where factory drilling weakened it for harness routing—inspect for flex before hard riding and treat as weaker than Xiaomi's 45° pipe assembly.[^f_stem]
- **ARS suspension stretches the wheelbase.** Italian-made front and rear kits push the G30 chassis outward, accept 125 mm hubs, and pair cleanly with 160 mm rotors; the rear kit is shipping while the zero-play front assembly is still in beta.[^ars_suspension]
[^pack_stack]: Stacking Ninebot G30 packs with DIY extenders requires BMS parity and matched voltages. Source: knowledge/notes/input_part004_review.md, L14 to L14
[^dual_g30_speed]: Dual-motor G30 speed expectations at 48 V with thermal management warnings. Source: knowledge/notes/input_part004_review.md, L74 to L74
[^g30_cutoff]: Recommended VESC battery cutoff voltage for 20 S stacked Ninebot packs. Source: knowledge/notes/input_part004_review.md, L48 to L48. Source: knowledge/notes/input_part004_review.md, L70 to L70
[^dual_pack_fitment]: Dual Ninebot pack packaging with tall spacers and flipped SNSC suspension. Source: knowledge/notes/input_part004_review.md, L47 to L47
[^ninebot_thermal]: Ninebot hub motor thermal ceiling around 40–45 A battery current. Source: knowledge/notes/input_part004_review.md, L298 to L298
[^f_stem]: Ninebot F-series stem bending cautions due to factory harness routing holes. Source: knowledge/notes/input_part004_review.md, L346 to L346
[^ars_suspension]: ARS front/rear suspension kits extend the G30 wheelbase, fit 125 mm hubs, and support 160 mm rotors with zero-play linkages once the front beta ships. Source: knowledge/notes/input_part004_review.md, L26 to L26
[^g2_arm_swap]: Source: data/vesc_help_group/text_slices/input_part011.txt, L20407 to L20430
[^f2pro-shfw]: ScooterHacking Firmware confirming sensorless launch reliability on F2 Pro with hall emulation noise during controller switching. Source: knowledge/notes/input_part013_review.md, L146 to L148
[^f2pro-ocp]: F2 Pro over-current protection tripping near 30 A regardless of utility app settings. Source: knowledge/notes/input_part013_review.md, L146 to L148
[^f2pro-limits]: F2 Pro external pack current sharing guidance to avoid BMS trips while respecting 25–30 A ceiling. Source: knowledge/notes/input_part013_review.md, L148 to L150

## References

[^1]: Source: knowledge/notes/input_part006_review.md, L83 to L83
[^2]: Source: data/vesc_help_group/text_slices/input_part002.txt, L1705 to L1717
[^3]: Source: data/vesc_help_group/text_slices/input_part002.txt, L2830 to L2846
[^4]: Source: data/vesc_help_group/text_slices/input_part005.txt, L24537 to L24551
[^5]: Source: data/vesc_help_group/text_slices/input_part010.txt, L10734 to L10738
[^6]: Source: knowledge/notes/input_part006_review.md, L409 to L409
[^7]: Source: knowledge/notes/input_part006_review.md, L410 to L410
[^8]: Source: knowledge/notes/input_part006_review.md, L183 to L183
[^9]: Source: knowledge/notes/input_part010_review.md, L35 to L36
[^10]: Source: data/vesc_help_group/text_slices/input_part005.txt, L22561 to L22586
[^11]: Source: data/vesc_help_group/text_slices/input_part005.txt, L22571 to L22575
[^12]: Source: knowledge/notes/input_part002_review.md, L480 to L482
[^13]: Source: data/vesc_help_group/text_slices/input_part001.txt, L26146 to L26158
[^14]: Source: data/vesc_help_group/text_slices/input_part001.txt, L26395 to L26399
[^15]: Source: knowledge/notes/input_part006_review.md, L349 to L349
[^g30-swingarm]: Source: knowledge/notes/input_part006_review.md†L18-L18
[^16]: Source: knowledge/notes/input_part006_review.md, L350 to L350
[^17]: Source: knowledge/notes/input_part006_review.md, L449 to L449
[^18]: Source: knowledge/notes/input_part012_review.md, L338 to L339
[^19]: Source: knowledge/notes/all_part01_review.md, L91065 to L91070
[^20]: Source: knowledge/notes/all_part01_review.md, L91188 to L91224
[^21]: Source: data/vesc_help_group/text_slices/input_part010.txt, L10379 to L10413
[^22]: Source: data/vesc_help_group/text_slices/input_part010.txt, L10726 to L10728
[^23]: Source: knowledge/notes/input_part006_review.md, L385 to L385
[^24]: Source: data/vesc_help_group/text_slices/input_part003.txt, L1325 to L1533
[^25]: Source: data/vesc_help_group/text_slices/input_part003.txt, L1499 to L1700
[^26]: Source: knowledge/notes/input_part012_review.md, L348 to L349
[^27]: Source: knowledge/notes/input_part013_review.md, L441 to L442
[^28]: Source: knowledge/notes/input_part013_review.md, L616 to L618
[^29]: Source: knowledge/notes/input_part011_review.md, L479 to L481
[^30]: Source: knowledge/notes/input_part012_review.md, L335 to L336
[^31]: Source: knowledge/notes/input_part012_review.md, L443 to L443
[^32]: Source: knowledge/notes/denis_all_part02_review.md, L28 to L32
[^33]: Source: knowledge/notes/denis_all_part02_review.md, L31 to L32
[^34]: Source: knowledge/notes/denis_all_part02_review.md, L70 to L71
[^35]: Source: knowledge/notes/denis_all_part02_review.md, L15 to L17
[^36]: Source: knowledge/notes/denis_all_part02_review.md, L170 to L171
[^37]: Source: knowledge/notes/all_part01_review.md, L88272 to L88278
[^38]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt, L131278 to L131307
[^39]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt, L110038 to L110041
[^40]: Source: data/vesc_help_group/text_slices/input_part003.txt, L26560 to L26622
[^41]: Source: data/vesc_help_group/text_slices/input_part003.txt, L14258 to L14270
[^42]: Source: knowledge/notes/input_part006_review.md, L508 to L508
[^43]: Source: knowledge/notes/input_part012_review.md, L347 to L348
[^44]: Source: data/vesc_help_group/text_slices/input_part003.txt, L26364 to L26496
[^45]: Source: knowledge/notes/input_part006_review.md, L84 to L84
[^46]: Source: knowledge/notes/all_part01_review.md, L92935 to L92960
