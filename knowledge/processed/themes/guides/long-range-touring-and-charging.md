# Long-Range Touring & Public Charging Guide

## TL;DR
- Multi-hundred-mile scooter tours are feasible with proper pack sizing (≥5 kWh), thermal management, and access to Level 2 EV charging infrastructure, but riders must plan charging etiquette, adapter compatibility, and backup power strategies before leaving home base.[^tour-viable][^ev-infra]
- Public charging demands J1772 adapters, protocol triggers for Tesla plugs (FoCcci boards or equivalent), and awareness that app-locked stations typically release only one handle per session—coordinate with EV drivers and respect charging bay time limits.[^j1772][^tesla-protocol]
- Treat improvised series-charging stacks as last-resort hacks—verify isolation with an ohmmeter before tying chargers together or you risk energising scooter frames and tripping breakers; purpose-built high-voltage supplies remain the safe touring option.【F:knowledge/notes/input_part004_review.md†L225-L225】
- Generator-assisted touring remains experimental; a 1 kW portable generator paired with a 5+ kWh pack could theoretically support coast-to-coast attempts, but weight, noise, and reliability trade-offs need field validation before serious planning.[^generator]

## Long-Range Riding Benchmarks
- Noname logged an 18-hour Appalachian ride covering roughly 150 miles at 50 mph bursts, noting the VESC stayed cool and demonstrating that high-capacity packs (likely 10+ kWh class given the distance) enable extended touring when thermal management is dialed in.[^appalachian]
- Yamal squeezes about 100 km from a 40 Ah pack by planning two 10 A charge stops each way on weekend tours and now considers a 20 A fast charger plus a spare pack the key upgrades for quicker turnarounds between legs.【F:knowledge/notes/input_part009_review.md†L325-L325】
- His latest mountain loop stacked 260 miles in 12 hours by chaining 45 A roadside charges (≈100 miles added per hour back to ~74 % state of charge) and confirms 50 A is tolerable while 70 A “is too much” without extra cooling—bake those thresholds into fast-charge planning for alpine routes.【F:data/vesc_help_group/text_slices/input_part013.txt†L16054-L16058】【F:data/vesc_help_group/text_slices/input_part013.txt†L16440-L16452】
- He is now staging a 480 km, seven-day group ride with a chase van, targeting 20 mph cruise speeds, 30–40 km/h efficiency windows, and 2.6 kW fast-charging on EVE 40P packs—use those planning numbers as a starting template for multi-day tours.【F:knowledge/notes/input_part013_review.md†L200-L200】
- The same crew crammed a Segway C80, Begode Q3, Vsett 10, Master Pro, and EX30 plus camping gear for five riders into a support van, giving planners a proven packing list for multi-scooter road trips.【F:knowledge/notes/input_part013_review.md†L240-L240】
- Shade and redundancy mattered on that ride—cooling packs under tree cover during 50 A stops and carrying spare phones for offline navigation both kept the schedule intact when cell service dropped.【F:data/vesc_help_group/text_slices/input_part013.txt†L16112-L16121】【F:data/vesc_help_group/text_slices/input_part013.txt†L16347-L16376】
- The same rider’s 20 S 35 P (≈700-cell) 18650 pack delivered 96 miles while using only about half of its 10.2 kWh capacity, showing how oversized bricks can double range without stressing cells when the chassis can carry the weight.[^noname-96mi]
- Pack sizing for 150+ mile rides typically requires 7–10 kWh or more depending on terrain, speed, and rider weight; builders planning tours should log Wh/mi consumption during shorter test rides to estimate realistic range before committing to long routes.[^pack-sizing]
- Mirono’s 3D-printed deck extender now houses 260 cells (~15 S 17 P) to chase 120 km coastal rides, while the group prototypes cargo trailers for hauling auxiliary batteries, logging ~2 A at 36 V from 80 W folding solar panels during scouting runs.[^deck-extender]
- Artem’s Xiaomi/Ninebot controller shootout underscores tuning impact on Wh/km: the stock 52 V 13 Ah square-wave build burned ~26 Wh/km flat out, his dual-motor VESC swap held ~22.5 Wh/km at higher speeds, and a sine-modulated Vsett managed ~17 Wh/km cruising 25–35 km/h on a 676 Wh pack.【F:knowledge/notes/input_part000_review.md†L486-L489】
- Bolt-on saddles shift rider weight rearward and make speed bumps harder to unload—test balance changes before multi-day tours and confirm frame-bag width still leaves foot room when swapping between 2.5 L and 3 L options.【F:knowledge/notes/input_part006_review.md†L133-L133】
- Real-world comparisons between Wepoor and dual Lonnyo 22×3 builds highlight how gearing, tire size, and pack capacity shape usable range: a 12 P Wepoor returns roughly 50 miles at 35–50 mph but drains quickly past 65 mph, while a 10 P 22×3 setup stretches to ~100 km per charge at similar cruising speeds.【F:knowledge/notes/input_part011_review.md†L301-L305】
- Jason’s alpine shakedown pushed a 30 S 6 P pack to ≈3 V per cell on steep climbs before regen only recovered a few percent on the descent—proof that mountain routes drain small packs rapidly and require pre-planned mid-ride charging stops.【F:knowledge/notes/input_part012_review.md†L208-L213】
- Yamal carries a fast charger into cafés on 100 km+ itineraries; his 20 S 10 P pack returns roughly 100 km of range in mild weather when he tops up partway through the day.【F:knowledge/notes/input_part012_review.md†L209-L213】
- Denis’ production data puts a Pro 2 with his 36 V 10 Ah external “boat” pack around 50 km of real range, while mixed 10S3P/10S4P clone combos manage ≈30 km before tapering—proof that pack health and chemistry drive perceived acceleration more than motor swaps on voltage-limited hubs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L91124-L91132】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L93450-L93478】

## Public Charging Strategies

### Level 2 EV Infrastructure
- AC EV posts only supply mains voltage, so scooters still need onboard or portable chargers—carry your own brick even when tapping Tesla or Type 2 sockets.【F:knowledge/notes/input_part005_review.md†L142-L142】
- J1772 adapters allow scooter packs to draw from public Level 2 pedestals, supporting charge rates from as low as 2 A (for emergency trickle charging) up to the pack's BMS limit when paired with appropriate cables and adapters.[^j1772]
- App-controlled charging stations (ChargePoint, Blink, etc.) typically release only one charging handle per session, so riders planning group tours must coordinate with EV drivers or use multiple stations to charge simultaneously.[^app-locks]
- Tesla destination chargers and Superchargers require protocol triggers such as FoCcci boards to initiate handshake sequences; without these adapters, the plug will not energize even with a physical J1772 adapter installed.[^tesla-protocol]

### Telecom & Lab-Supply Chargers
- Fast-charger demos remind builders that healthy packs still prefer ≈1 C; for example, a 20 S 6 P Samsung 40T/Molicel P42A pack already pulls roughly 6.3 kW, so plan EV-grade infrastructure and tight thermal monitoring before pushing higher.[^telecom-fast]
- Noname cataloged AliExpress telecom-derived bricks—around US$340 for Huawei 60 A units or US$260 for touchscreen 50 A models—emphasizing they are rebadged rectifiers despite factory-style marketing.[^telecom-fast]

### Charging Etiquette & Best Practices
1. **Respect charging bay time limits.** Move scooters promptly once charged to free stations for EV drivers who often have fewer alternatives than scooter riders with portable packs.[^etiquette]
2. **Communicate charge rate expectations.** Inform station operators or fellow users when drawing only 2–3 A for safety testing versus full-rate charging to avoid confusion about bay availability.[^charge-rate]
3. **Plan for single-handle sessions.** Budget extra time when touring in groups, as most app-based systems won't release multiple handles simultaneously from the same account.[^app-locks]
4. **Monitor thermal margins.** Long charging sessions at high rates (≥6 A per pack) can heat cells and BMS hardware, so log temperatures and adjust charge current if ambient temps exceed 30 °C or packs show elevated thermal readings.[^thermal-charging]
5. **Confirm facility headroom before promising fast turns.** Typical European three-phase residential feeds offer roughly 16 A per leg (~11 kW total), so 40 C “minutes-long” home charges still demand industrial service upgrades or external venues.【F:knowledge/notes/input_part009_review.md†L349-L349】
### Adapter & Hardware Recommendations
- **J1772 to scooter pack adapter:** Verify pin compatibility, voltage range (most scooters charge at 48–100 V), and current rating before purchasing or fabricating custom adapters.
- **GTK 0–102 V adjustable supply:** A cheaper wide-voltage bench charger alternative to the Grin Satiator, provided you accept bulkier hardware and ~3 A default current.【F:knowledge/notes/input_part005_review.md†L143-L143】
- **FoCcci or equivalent Tesla protocol board:** Required for Tesla plug compatibility; confirm firmware version supports your charging voltage before field deployment.
- **Portable multimeter and voltage monitor:** Essential for verifying station output voltage and diagnosing adapter issues before connecting expensive battery packs.
- **Plan ahead for 20 S chargers.** 84 V chargers remain scarce outside China, so touring riders stock adjustable lab supplies, series-stack smaller bricks, or wait on AliExpress shipments rather than overvolting 67.2 V units; upgrade thin Xiaomi charge ports to XT60 leads when pushing beyond ~3 A.【F:knowledge/notes/input_part005_review.md†L331-L338】
- **Stick with proven CC‑CV bricks.** The group keeps defaulting to Wate or YZPower chargers because bargain adjustables wander off voltage set-points and cook packs unless you meter every session; CC-only supplies still leave passive-balancing BMSs short of a full charge.【F:data/vesc_help_group/text_slices/input_part005.txt†L24033-L24075】
- **Treat series-stacked chargers as a stopgap.** Builders will stack dual 10 S bricks only while waiting for proper 20 S units and even then monitor them closely—dedicated charge ports and sealed enclosures remain the commuter-friendly solution for high-voltage packs.【F:data/vesc_help_group/text_slices/input_part005.txt†L23075-L23093】【F:data/vesc_help_group/text_slices/input_part005.txt†L23941-L23953】
### Programmable Telecom Supplies & Bench Chargers
- **AliExpress adjustable bricks struggle above 84 V.** Community testing on adjustable 20 S/24 S chargers shows budget units browning out or failing outright once riders push past ≈84 V, so bring spares or derate them when touring with 96 V packs.【F:knowledge/notes/input_part011_review.md†L101-L106】
- **WANPTEK benchtops are voltage-flexible but current-limited.** Their compact supplies work as emergency travel chargers thanks to programmable setpoints, yet the 3 A ceiling makes them impractical for fast top-ups—plan overnight charges only.【F:knowledge/notes/input_part011_review.md†L101-L106】
- **Huawei telecom rectifiers remain the reliable high-power option.** Riders still prize these 4 kW-class bricks for 20 S+ builds because they hold voltage under load and integrate with app-based control, though the size, cost, and fan noise make them best suited to support vans or home base charging hubs rather than café stops.【F:knowledge/notes/input_part011_review.md†L101-L106】【F:knowledge/notes/input_part011_review.md†L209-L212】
- **Compact 2 kW adjustable chargers are resurfacing.** AliExpress listings now advertise 66–93 V @ 23 A and 72–101 V @ 16 A bricks; stock remains sparse, so treat them as opportunistic pickups rather than dependable tour gear.【F:knowledge/notes/input_part011_review.md†L460-L463】
5. **Top to 80–85 % when weather windows open.** Riders wait for rain to clear before tapping public chargers or EV adapters, then stop around 80 % state of charge to preserve pack longevity and resume touring without wasting time on slow CV phases.【F:knowledge/notes/input_part012_review.md†L209-L213】
- **J1772 to scooter pack adapter:** Verify pin compatibility, voltage range (most scooters charge at 48–100 V), and current rating before purchasing or fabricating custom adapters. The latest build notes call for logging pilot-resistor values, conductor gauges, and enclosure choices so future 3 kW tour adapters are reproducible rather than ad-hoc harnesses.【F:knowledge/notes/input_part012_review.md†L303-L303】
- **3.2 kW “2900 W” chargers:** Jason’s brick already exceeds its nameplate 26 A output when pushing tour builds—validate cord and connector temperatures before sustaining similar rates.【F:knowledge/notes/input_part012_review.md†L211-L212】
### High-Power Charger Deployments
- **6 kW hyper-charger kits are spreading.** Fast-tour riders now draw up to 6 kW from EV posts; the €400-class hardware is often paired with another ~$2 k in adapters and cabling, and real-world current is capped either by the battery (e.g., Jason’s pack) or the pedestal (Noname’s logs). Document hardware cost, pedestal limits, and pack ceilings together so teammates can copy a proven recipe instead of overloading tour builds.【F:knowledge/notes/input_part012_review.md†L274-L279】【F:knowledge/notes/input_part012_review.md†L310-L310】
- **Plan pack limits before cranking current.** Even copper “sandwich” busbars need cross-section math—Jason is double-checking that his 150 A junctions have enough copper to survive repeated lunch-break charges before final assembly.【F:knowledge/notes/input_part012_review.md†L286-L288】
- **Log real ride endurance.** Noname just finished a 148-mile NIU day that mixed pavement, dirt, and even 12" water crossings—capture similar logs to set expectations for seated VESC rigs.【F:knowledge/notes/input_part012_review.md†L414-L414】

## Generator-Assisted Touring (Experimental)
- A 1 kW portable generator paired with a 5+ kWh pack has been theorized for coast-to-coast scooter attempts, potentially providing 8–10 hours of riding per fuel tank when charging on-the-go at low rates.[^generator]
- Weight penalties (generator, fuel, mounting hardware) and noise considerations make this strategy impractical for urban routes or stealth camping scenarios; field testing is needed before committing to this approach for serious tours.[^generator-limits]
- Backup charging bricks (3–5 A rated) remain more practical for overnight hotel stops or emergency trickle charging when infrastructure is unavailable.[^backup-chargers]

## Pack & BMS Considerations for Touring
- **Over-provision capacity:** Plan for 20–30 % reserve capacity to account for voltage sag, cold weather, headwinds, and unexpected detours; aggressive riders logging 2 Wh/mi at 30 mph should budget ≥3 Wh/mi for tour planning.[^capacity-buffer]
- **Quantify delivery duty cycles before rebuilding packs.** Swapping from P42A to 5 Ah-class cells only nets ≈0.8 kWh extra on typical delivery scooters; interview couriers about shift length and swap packs before committing to a full rebuild.【F:knowledge/notes/input_part011_review.md†L332-L339】
- **BMS thermal limits:** High-capacity packs (≥7 kWh) under sustained discharge can heat BMS MOSFETs or balance boards; log temps during test rides and add active cooling if boards exceed 50 °C under load.[^bms-thermal]
- **Charge rate planning:** If fast-charging via Level 2 infrastructure, ensure BMS charge current limits (typically 10–30 A for scooter-class hardware) match adapter capabilities and won't trip thermal or over-current protections.[^charge-limits]
- **Respect OEM charge ceilings:** Segway Ninebot G30 BMS firmware trips if charge current exceeds ~8 A even though the pack accepts Segway’s 5 A fast charger, while F-series and Xiaomi packs top out around 4 A continuous—dial adjustable lab supplies accordingly to avoid nuisance cut-offs.[^g30-charge-limit]
- **Carry on-the-road spares.** Travellers keep tubes and compact toolkits handy because hotel stairs, missing elevators, and recurring rear flats remain common on high-power builds abroad.【F:knowledge/notes/input_part006_review.md†L180-L180】
- **Keep scooters multimodal.** Gig riders still favour compact G30/Xiaomi sleepers for train and bus legs, while oversized dual-motor builds demand storage plans before you leave home.【F:knowledge/notes/input_part006_review.md†L228-L228】
- **Balance gently at the top:** Yamal lets packs rest before topping off with a 2.8 A brick, and 🇪🇸AYO#74 caps equalisation around 2–4 A while tightening drift thresholds near 0.01 V so BMSs stop “micro-charging” all night.[^bms-balance]
- **Document pack mass and expectations.** Noname’s 20 S 32 P Samsung 35E pack stores ≈112 Ah (≈9.4 kWh) and delivers ~70 mi while leaving the scooter near 350 lb; he’d now favour a lighter 32 S 20 P layout for better torque-to-weight on long tours.【F:knowledge/notes/input_part012_review.md†L312-L316】
- **Respect BMS trip stories.** A JK BMS saved a C80 conversion by tripping at 60 A when the rider pulled 70 A battery—use the incident as a reminder to size packs around controller demand rather than bypassing protection.【F:knowledge/notes/input_part012_review.md†L280-L285】

## Safety & Reliability Tips
1. **Test all charging adapters at home before departure.** Verify voltage, current draw, and thermal behavior with a multimeter and infrared thermometer during bench charging sessions.[^pre-test]
2. **Carry backup charging bricks and cables.** Hotel outlets and standard 120 V receptacles remain the most reliable fallback when public infrastructure is unavailable or malfunctioning.[^backup]
3. **Log ride telemetry and charging sessions.** Track Wh consumed per mile, charge times, and thermal peaks to refine future tour plans and identify pack degradation early.[^telemetry]
4. **Plan routes with charging station density in mind.** Use PlugShare or ChargePoint maps to identify backup stations within 20–30 miles of primary stops in case of equipment failure or station downtime.[^route-planning]
- **Carry a vetted charger.** Budget 0–90 V/5 A AliExpress bricks (~€76 shipped) keep arriving late or DOA—Mirono lines up disputes in advance—while others swallow the cost of a Grin Satiator to avoid repeated support fights on tour.【F:data/vesc_help_group/text_slices/input_part002.txt†L22438-L22450】
5. **Confirm delivery SOC and rebalance before tours.** Logistics warehouses often ship scooters between 30–50 % SOC even when some units arrive near 70–100 %; check and balance packs on arrival so you start long trips with known baselines.[^warehouse-soc]
6. **Keep packs warm in winter.** Riders commuting near freezing rely on heated battery bags or external heaters to hold cells above ~10 °C and reduce cold-weather voltage sag before setting out.[^winter-bags]
7. **Budget cold-weather PPE.** Winter riders treat full-face helmets and balaclavas as consumables—expect to spend $120+ keeping replacements ready so gear stays warm and theft-resistant during sub-zero commutes.【F:knowledge/notes/input_part006_review.md†L91-L91】
- 8. **Adjust tire pressure for load.** Fleet technicians keep commuter tires at ≥20 psi and push heavy riders toward ~3.6 bar rear pressure when aiming for 60 km/h travel to fend off chronic punctures.【F:knowledge/notes/input_part006_review.md†L174-L174】
- 9. **Prioritise torque and thermal resilience.** Even burnout-focused city builds lean on manageable 20 S10 P packs with regen, valuing heat margin over chasing absolute top speed.【F:knowledge/notes/input_part006_review.md†L229-L229】
- 10. **Integrate track-safe enclosures.** Race officials now ban external battery bags at 100 km/h events because loose packs eject and ignite in crashes—touring builds destined for track days need fully enclosed compartments.【F:knowledge/notes/input_part006_review.md†L385-L385】
### Tour Readiness Checklist (Latest Review Actions)
- **Pack an adapter kit that covers public pedestals and cafes.** The crew now keeps J1772 adapters, travel bricks, and café-friendly extension cords grouped so mid-route stops don’t sag small packs below ≈3 V per cell on mountain grades.【F:knowledge/notes/input_part012_review.md†L307-L307】
- **Brush up on fast-charging etiquette.** Revisit how you’ll brief café staff, share bays, and shuffle scooters before rain rolls in; the latest review explicitly called for folding etiquette reminders into the touring checklist rather than leaving them scattered across chat threads.【F:knowledge/notes/input_part012_review.md†L307-L308】
- **Note ferrofluid and hub-prep chores.** A fresh maintenance list now ties Segway-class hub service (ferrofluid fills, temp probes) to tour prep so high-mileage weeks don’t start with neglected drivetrains.【F:knowledge/notes/input_part012_review.md†L306-L306】【F:knowledge/notes/input_part012_review.md†L309-L309】
## Regional Compliance & Planning Pressure
- Spanish riders are already budgeting stealthier frames, €3 k shell swaps, or downsized scooters ahead of the 2027 crackdown—expect to validate deck dimensions (e.g., Achilleus vs. Thunder) and controller placements against DGT listings when planning tours across stricter jurisdictions.【F:knowledge/notes/input_part013_review.md†L238-L239】
- Local enforcement is already citing micromobility capable of >35 mph in Las Vegas after a fatal crash; high-speed builds need route plans that respect posted limits and rider training when sharing public streets.【F:data/vesc_help_group/text_slices/input_part013.txt†L15064-L15090】【F:data/vesc_help_group/text_slices/input_part013.txt†L15084-L15086】
5. **Prep for winter efficiency hits.** Riders report Wh/km nearly doubling in freezing conditions (≈30 Wh/km vs. 18–20 Wh/km in summer); keep packs warm indoors or add gentle heaters before rolling out in sub-zero weather.【F:knowledge/notes/denis_all_part02_review.md†L115861-L115872】

## Follow-Up Actions Needed
- Draft EV-charger etiquette notes covering time limits, single-handle session restrictions, and communication protocols for mixed scooter/EV charging scenarios.[^follow-etiquette]
- Document field-tested J1772 adapter builds (wiring, fusing, voltage range) to provide builders with reproducible charging solutions.[^follow-adapter]
- Validate generator-assisted touring feasibility with real-world weight, noise, and reliability data before promoting as a viable long-distance strategy.[^follow-generator]
- Capture thermal management strategies for multi-hour charging sessions at public stations, including active cooling thresholds and BMS temperature monitoring.[^follow-thermal]

## Source Notes
[^tour-viable]: Noname's 18-hour, 150-mile Appalachian ride demonstrating VESC thermal stability and feasibility of long-range touring.【F:knowledge/notes/input_part013_review.md†L146-L146】
[^ev-infra]: Public charging infrastructure discussions covering Level 2 access and protocol requirements.【F:knowledge/notes/input_part013_review.md†L147-L149】
[^j1772]: J1772 adapter compatibility allowing 2 A trickle charging up to BMS-limited rates from Level 2 pedestals.【F:knowledge/notes/input_part013_review.md†L147-L149】
[^app-locks]: App-controlled charging stations releasing only one handle per session, requiring coordination for group tours.【F:knowledge/notes/input_part013_review.md†L147-L149】
[^tesla-protocol]: Tesla plug requirement for protocol triggers (FoCcci boards) to initiate charging handshake sequences.【F:knowledge/notes/input_part013_review.md†L147-L149】
[^generator]: Theoretical 1 kW generator + 5 kWh pack configuration for coast-to-coast touring attempts.【F:knowledge/notes/input_part013_review.md†L146-L146】
[^appalachian]: Noname's 150-mile ride log demonstrating thermal management and extended touring feasibility.【F:knowledge/notes/input_part013_review.md†L146-L146】
[^noname-96mi]: Noname’s 20 S 35 P commuter pack recorded 96 miles of riding while burning roughly half its 10.2 kWh capacity.【F:knowledge/notes/input_part013_review.md†L95-L95】
[^pack-sizing]: General guidance for 7–10 kWh pack sizing for 150+ mile tours based on consumption testing.
[^deck-extender]: Source: knowledge/notes/input_part000_review.md, line 159.
[^etiquette]: Charging bay etiquette reminders to respect time limits and communicate with EV drivers.
[^charge-rate]: Communication guidelines for low-rate vs. full-rate charging to avoid station confusion.
[^thermal-charging]: Thermal monitoring recommendations during extended charging sessions.
[^generator-limits]: Weight, noise, and practicality constraints for generator-assisted touring.
[^backup-chargers]: Backup charging brick recommendations for hotel stops and emergency scenarios.
[^capacity-buffer]: Reserve capacity planning (20–30 %) for voltage sag, weather, and detours.
[^bms-thermal]: BMS thermal management during sustained high-capacity pack discharge.
[^charge-limits]: BMS charge current limit matching for public infrastructure compatibility.
[^telecom-fast]: Fast-charging cautions highlighting ≈1 C limits on Samsung 40T/Molicel P42A packs and pricing for telecom-derived 50–60 A chargers.【F:knowledge/notes/input_part010_review.md†L245-L247】
[^bms-balance]: Yamal and 🇪🇸AYO#74’s top-off routine—rest before balance charging, limit equalisation to 2–4 A, and tighten drift thresholds near 0.01 V to stop endless micro-charging.【F:knowledge/notes/input_part010_review.md†L269-L270】
[^pre-test]: Pre-departure adapter testing protocols with multimeter and thermal validation.
[^backup]: Backup charging equipment recommendations for reliability.
[^telemetry]: Ride telemetry logging for consumption tracking and pack health monitoring.
[^route-planning]: Route planning recommendations using PlugShare/ChargePoint for backup station identification.
[^g30-charge-limit]: Segway G30 packs accept the 5 A fast charger but BMS firmware trips above ~8 A, and smaller F-series/Xiaomi packs prefer ≤4 A continuous from adjustable supplies.【F:knowledge/notes/input_part006_review.md†L75-L75】
[^warehouse-soc]: Warehouse storage guidance recommending 30–50 % SOC even when some scooters arrive closer to 70–100 %, prompting balance checks on delivery.【F:knowledge/notes/input_part006_review.md†L76-L76】
[^winter-bags]: Winter commuters keeping packs above ~10 °C with heated battery bags or external heaters to limit cold-weather sag.【F:knowledge/notes/input_part006_review.md†L77-L77】
[^follow-etiquette]: Follow-up action to draft detailed EV-charger etiquette notes.【F:knowledge/notes/input_part013_review.md†L516-L516】
[^follow-adapter]: Follow-up action to document field-tested J1772 adapter builds.
[^follow-generator]: Follow-up action to validate generator-assisted touring with real-world data.
[^follow-thermal]: Follow-up action to capture thermal management strategies for extended charging sessions.
