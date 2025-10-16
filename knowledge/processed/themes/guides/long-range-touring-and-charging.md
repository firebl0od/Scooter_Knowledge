# Long-Range Touring & Public Charging Guide

## TL;DR

- Multi-hundred-mile scooter tours are feasible with proper pack sizing (≥5 kWh), thermal management, and access to Level 2 EV charging infrastructure, but riders must plan charging etiquette, adapter compatibility, and backup power strategies before leaving home base.[^tour-viable][^ev-infra]
- Public charging demands J1772 adapters, protocol triggers for Tesla plugs (FoCcci boards or equivalent), and awareness that app-locked stations typically release only one handle per session.
  - coordinate with EV drivers and respect charging bay time limits.[^j1772][^tesla-protocol]
- Treat improvised series-charging stacks as last-resort hacks.
  - verify isolation with an ohmmeter before tying chargers together or you risk energising scooter frames and tripping breakers; purpose-built high-voltage supplies remain the safe touring option.[^1]
- Generator-assisted touring remains experimental; a 1 kW portable generator paired with a 5+ kWh pack could theoretically support coast-to-coast attempts, but weight, noise, and reliability trade-offs need field validation before serious planning.[^generator]

## Long-Range Riding Benchmarks

- Noname logged an 18-hour Appalachian ride covering roughly 150 miles at 50 mph bursts, noting the VESC stayed cool and demonstrating that high-capacity packs (likely 10+ kWh class given the distance) enable extended touring when thermal management is dialed in.[^appalachian]
- Yamal squeezes about 100 km from a 40 Ah pack by planning two 10 A charge stops each way on weekend tours and now considers a 20 A fast charger plus a spare pack the key upgrades for quicker turnarounds between legs.[^2]
- His latest mountain loop stacked 260 miles in 12 hours by chaining 45 A roadside charges (≈100 miles added per hour back to ~74 % state of charge) and confirms 50 A is tolerable while 70 A “is too much” without extra cooling.
  - bake those thresholds into fast-charge planning for alpine routes.[^3][^4]
- He is now staging a 480 km, seven-day group ride with a chase van, targeting 20 mph cruise speeds, 30–40 km/h efficiency windows, and 2.6 kW fast-charging on EVE 40P packs.
  - use those planning numbers as a starting template for multi-day tours.[^5]
- The same crew crammed a Segway C80, Begode Q3, Vsett 10, Master Pro, and EX30 plus camping gear for five riders into a support van, giving planners a proven packing list for multi-scooter road trips.[^6]
- Shade and redundancy mattered on that ride.
  - cooling packs under tree cover during 50 A stops and carrying spare phones for offline navigation both kept the schedule intact when cell service dropped.[^7][^8]
- The same rider’s 20 S 35 P (≈700-cell) 18650 pack delivered 96 miles while using only about half of its 10.2 kWh capacity, showing how oversized bricks can double range without stressing cells when the chassis can carry the weight.[^noname-96mi]
- Pack sizing for 150+ mile rides typically requires 7–10 kWh or more depending on terrain, speed, and rider weight; builders planning tours should log Wh/mi consumption during shorter test rides to estimate realistic range before committing to long routes.[^pack-sizing]
- Mirono’s 3D-printed deck extender now houses 260 cells (~15 S 17 P) to chase 120 km coastal rides, while the group prototypes cargo trailers for hauling auxiliary batteries, logging ~2 A at 36 V from 80 W folding solar panels during scouting runs.[^deck-extender]
- Wind drag still dominates at speed—a 20 S VSETT tuned for 63–65 Wh/km in calm conditions jumped to 72 Wh/km in strong headwinds.[^ip001-wind-drag]
- Artem’s Xiaomi/Ninebot controller shootout underscores tuning impact on Wh/km: the stock 52 V 13 Ah square-wave build burned ~26 Wh/km flat out, his dual-motor VESC swap held ~22.5 Wh/km at higher speeds, and a sine-modulated Vsett managed ~17 Wh/km cruising 25–35 km/h on a 676 Wh pack.[^9]
- Community VESC logs peg commuter consumption near 25 Wh/km at 40 km/h in calm weather and roughly 28 Wh/km with stiff headwinds; run 20 km loops in both directions to average wind and terrain before quoting numbers publicly.[^ip001-whkm][^ip001-whkm-loop]
- The same datasets show heavier riders and hilly routes inflating Wh/km even on identical scooters, so benchmark on flat courses when comparing builds.[^ip001-whkm-mass]
- Expect regen to return modest energy—many Daly dashboards still show zero current during gentle “walking” regen even as pack voltage creeps upward, and VESC riders rarely exceed ~12 % recovery without huge packs and aggressive settings.[^ip001-regen-eff]
- Bolt-on saddles shift rider weight rearward and make speed bumps harder to unload.
  - test balance changes before multi-day tours and confirm frame-bag width still leaves foot room when swapping between 2.5 L and 3 L options.[^10]
- Real-world comparisons between Wepoor and dual Lonnyo 22×3 builds highlight how gearing, tire size, and pack capacity shape usable range: a 12 P Wepoor returns roughly 50 miles at 35–50 mph but drains quickly past 65 mph, while a 10 P 22×3 setup stretches to ~100 km per charge at similar cruising speeds.[^11]
- Jason’s alpine shakedown pushed a 30 S 6 P pack to ≈3 V per cell on steep climbs before regen only recovered a few percent on the descent.
  - proof that mountain routes drain small packs rapidly and require pre-planned mid-ride charging stops.[^12]
- Yamal carries a fast charger into cafés on 100 km+ itineraries; his 20 S 10 P pack returns roughly 100 km of range in mild weather when he tops up partway through the day.[^13]
- Long-range Vsett crews plan 125–200 mile weekends by chaining J1772 pedestals through ~2 kW Huawei supplies, accepting ~10 mph average speed once four partial charges are factored in while dual Spintend 85/250 controllers stay cool over 320 km of mixed riding.[^vsett_weekend_loop]
- A 16 S 6 P Sanyo pack paired with dual Spintend 85/250 controllers still delivers roughly 10.8 kW and 54 mph when riders focus on voltage monitoring instead of full telemetry dashboards.[^sanyo_spintend_benchmark]
- Denis’ production data puts a Pro 2 with his 36 V 10 Ah external “boat” pack around 50 km of real range, while mixed 10S3P/10S4P clone combos manage ≈30 km before tapering.
  - proof that pack health and chemistry drive perceived acceleration more than motor swaps on voltage-limited hubs.[^14][^15]

## Public Charging Strategies

### Level 2 EV Infrastructure

- AC EV posts only supply mains voltage, so scooters still need onboard or portable chargers.
  - carry your own brick even when tapping Tesla or Type 2 sockets.[^16]
- J1772 adapters allow scooter packs to draw from public Level 2 pedestals, supporting charge rates from as low as 2 A (for emergency trickle charging) up to the pack's BMS limit when paired with appropriate cables and adapters.[^j1772]
- App-controlled charging stations (ChargePoint, Blink, etc.) typically release only one charging handle per session, so riders planning group tours must coordinate with EV drivers or use multiple stations to charge simultaneously.[^app-locks]
- Tesla destination chargers and Superchargers require protocol triggers such as FoCcci boards to initiate handshake sequences; without these adapters, the plug will not energize even with a physical J1772 adapter installed.[^tesla-protocol]
- Verify EVSE pilot wiring when building adapters; one Type 2 unit only came online after swapping the pilot resistor to 880 Ω and adding a manual status button so public chargers recognized the scooter pack.[^type2_pilot]

### Telecom & Lab-Supply Chargers

- Fast-charger demos remind builders that healthy packs still prefer ≈1 C; for example, a 20 S 6 P Samsung 40T/Molicel P42A pack already pulls roughly 6.3 kW, so plan EV-grade infrastructure and tight thermal monitoring before pushing higher.[^telecom-fast]
- Noname cataloged AliExpress telecom-derived bricks.
  - around US$340 for Huawei 60 A units or US$260 for touchscreen 50 A models
  - emphasizing they are rebadged rectifiers despite factory-style marketing.[^telecom-fast]
- Popular adjustable “lab” supplies shipped through AliExpress have shown over-voltage spikes from crude internal mods; veterans now derate them heavily or avoid using them on traction packs altogether.[^ip001-adjustable-psu]

### Charging Etiquette & Best Practices

1. **Respect charging bay time limits.** Move scooters promptly once charged to free stations for EV drivers who often have fewer alternatives than scooter riders with portable packs.[^etiquette]
2. **Treat live charge-port work as a solo job.** A Vsett shorted the moment a friend helped swap the inlet; even qualified assistants need a repeatable double-check ritual before touching energized leads.[^charge_port_discipline]
2. **Communicate charge rate expectations.** Inform station operators or fellow users when drawing only 2–3 A for safety testing versus full-rate charging to avoid confusion about bay availability.[^charge-rate]
3. **Plan for single-handle sessions.** Budget extra time when touring in groups, as most app-based systems won't release multiple handles simultaneously from the same account.[^app-locks]
4. **Monitor thermal margins.** Long charging sessions at high rates (≥6 A per pack) can heat cells and BMS hardware, so log temperatures and adjust charge current if ambient temps exceed 30 °C or packs show elevated thermal readings.[^thermal-charging]
5. **Confirm facility headroom before promising fast turns.** Typical European three-phase residential feeds offer roughly 16 A per leg (~11 kW total), so 40 C “minutes-long” home charges still demand industrial service upgrades or external venues.[^17]

### Adapter & Hardware Recommendations

- **J1772 to scooter pack adapter:** Verify pin compatibility, voltage range (most scooters charge at 48–100 V), and current rating before purchasing or fabricating custom adapters.
- **GTK 0–102 V adjustable supply:** A cheaper wide-voltage bench charger alternative to the Grin Satiator, provided you accept bulkier hardware and ~3 A default current.[^18]
- **Adjustable-voltage telecom bricks:** Riders are actively sourcing CC/CV chargers with programmable ceilings so they can cap routine charges near 95 % SOC instead of sitting at 100 %.[^adj_voltage]
- **FoCcci or equivalent Tesla protocol board:** Required for Tesla plug compatibility; confirm firmware version supports your charging voltage before field deployment.
- **Portable multimeter and voltage monitor:** Essential for verifying station output voltage and diagnosing adapter issues before connecting expensive battery packs.
- **Plan ahead for 20 S chargers.** 84 V chargers remain scarce outside China, so touring riders stock adjustable lab supplies, series-stack smaller bricks, or wait on AliExpress shipments rather than overvolting 67.2 V units; upgrade thin Xiaomi charge ports to XT60 leads when pushing beyond ~3 A.[^19]
- **Inspect third-party chargers on arrival.** One “500 W” AliExpress brick arrived labeled 350 W (~70 V×5 A) with lower voltage limits, forcing a partial refund; test and document hardware before the dispute window closes.[^ip001-ali-bait]
- **Stick with proven CC‑CV bricks.** The group keeps defaulting to Wate or YZPower chargers because bargain adjustables wander off voltage set-points and cook packs unless you meter every session; CC-only supplies still leave passive-balancing BMSs short of a full charge.[^20]
- **Treat series-stacked chargers as a stopgap.** Builders will stack dual 10 S bricks only while waiting for proper 20 S units and even then monitor them closely.
  - dedicated charge ports and sealed enclosures remain the commuter-friendly solution for high-voltage packs.[^21][^22]

### Programmable Telecom Supplies & Bench Chargers

- **AliExpress adjustable bricks struggle above 84 V.** Community testing on adjustable 20 S/24 S chargers shows budget units browning out or failing outright once riders push past ≈84 V, so bring spares or derate them when touring with 96 V packs.[^23]
- **Celler-branded 20 S adjustable brick has field approval—monitor the fan.** Jonas’ long-term test group rates the Celler AliExpress charger as accurate and mechanically solid, noting the only annoyance so far is its always-on fan.[^celler]
- **Inspect adjustable 20 S supplies before first ride.** Recent teardown chatter urges buyers to open housings, upsize output leads to ≥4 mm² for sustained 20–30 A service, and always energise the charger from the wall before connecting scooter packs so diode-less stages don’t arc across XT plugs.[^adjustable-20s]
- **WANPTEK benchtops are voltage-flexible but current-limited.** Their compact supplies work as emergency travel chargers thanks to programmable setpoints, yet the 3 A ceiling makes them impractical for fast top-ups.
- **Map the trim pots before tweaking Meanwell-style supplies.** VR1 handles output voltage, VR2 sets charge current, and VR3 defines cutoff current; tune against a partially discharged pack while watching a meter so you don’t overshoot setpoints.[^charger-trims]
  - plan overnight charges only.[^23]
- **Huawei telecom rectifiers remain the reliable high-power option.** Riders still prize these 4 kW-class bricks for 20 S+ builds because they hold voltage under load and integrate with app-based control, though the size, cost, and fan noise make them best suited to support vans or home base charging hubs rather than café stops.[^23][^24]
- **Compact 2 kW adjustable chargers are resurfacing.** AliExpress listings now advertise 66–93 V @ 23 A and 72–101 V @ 16 A bricks; stock remains sparse, so treat them as opportunistic pickups rather than dependable tour gear.[^25]
5. **Top to 80–85 % when weather windows open.** Riders wait for rain to clear before tapping public chargers or EV adapters, then stop around 80 % state of charge to preserve pack longevity and resume touring without wasting time on slow CV phases.[^13]

- **J1772 to scooter pack adapter:** Verify pin compatibility, voltage range (most scooters charge at 48–100 V), and current rating before purchasing or fabricating custom adapters. The latest build notes call for logging pilot-resistor values, conductor gauges, and enclosure choices so future 3 kW tour adapters are reproducible rather than ad-hoc harnesses.[^26]
- **3.2 kW “2900 W” chargers:** Jason’s brick already exceeds its nameplate 26 A output when pushing tour builds.
  - validate cord and connector temperatures before sustaining similar rates.[^27]

### High-Power Charger Deployments

- **6 kW hyper-charger kits are spreading.** Fast-tour riders now draw up to 6 kW from EV posts; the €400-class hardware is often paired with another ~$2 k in adapters and cabling, and real-world current is capped either by the battery (e.g., Jason’s pack) or the pedestal (Noname’s logs). Document hardware cost, pedestal limits, and pack ceilings together so teammates can copy a proven recipe instead of overloading tour builds.[^28][^29]
- **Plan pack limits before cranking current.** Even copper “sandwich” busbars need cross-section math.
  - Jason is double-checking that his 150 A junctions have enough copper to survive repeated lunch-break charges before final assembly.[^30]
- **Log real ride endurance.** Noname just finished a 148-mile NIU day that mixed pavement, dirt, and even 12" water crossings.
  - capture similar logs to set expectations for seated VESC rigs.[^31]

## Generator-Assisted Touring (Experimental)

- A 1 kW portable generator paired with a 5+ kWh pack has been theorized for coast-to-coast scooter attempts, potentially providing 8–10 hours of riding per fuel tank when charging on-the-go at low rates.[^generator]
- Weight penalties (generator, fuel, mounting hardware) and noise considerations make this strategy impractical for urban routes or stealth camping scenarios; field testing is needed before committing to this approach for serious tours.[^generator-limits]
- Backup charging bricks (3–5 A rated) remain more practical for overnight hotel stops or emergency trickle charging when infrastructure is unavailable.[^backup-chargers]

## Pack & BMS Considerations for Touring

- **Over-provision capacity:** Plan for 20–30 % reserve capacity to account for voltage sag, cold weather, headwinds, and unexpected detours; aggressive riders logging 2 Wh/mi at 30 mph should budget ≥3 Wh/mi for tour planning.[^capacity-buffer]
- **Quantify delivery duty cycles before rebuilding packs.** Swapping from P42A to 5 Ah-class cells only nets ≈0.8 kWh extra on typical delivery scooters; interview couriers about shift length and swap packs before committing to a full rebuild.[^32]
- **BMS thermal limits:** High-capacity packs (≥7 kWh) under sustained discharge can heat BMS MOSFETs or balance boards; log temps during test rides and add active cooling if boards exceed 50 °C under load.[^bms-thermal]
- **Charge rate planning:** If fast-charging via Level 2 infrastructure, ensure BMS charge current limits (typically 10–30 A for scooter-class hardware) match adapter capabilities and won't trip thermal or over-current protections.[^charge-limits]
- **Respect OEM charge ceilings:** Segway Ninebot G30 BMS firmware trips if charge current exceeds ~8 A even though the pack accepts Segway’s 5 A fast charger, while F-series and Xiaomi packs top out around 4 A continuous.
  - dial adjustable lab supplies accordingly to avoid nuisance cut-offs.[^g30-charge-limit]
- **Carry on-the-road spares.** Travellers keep tubes and compact toolkits handy because hotel stairs, missing elevators, and recurring rear flats remain common on high-power builds abroad.[^33]
- **Keep scooters multimodal.** Gig riders still favour compact G30/Xiaomi sleepers for train and bus legs, while oversized dual-motor builds demand storage plans before you leave home.[^34]
- **Balance gently at the top:** Yamal lets packs rest before topping off with a 2.8 A brick, and 🇪🇸AYO#74 caps equalisation around 2–4 A while tightening drift thresholds near 0.01 V so BMSs stop “micro-charging” all night.[^bms-balance]
- **Document pack mass and expectations.** Noname’s 20 S 32 P Samsung 35E pack stores ≈112 Ah (≈9.4 kWh) and delivers ~70 mi while leaving the scooter near 350 lb; he’d now favour a lighter 32 S 20 P layout for better torque-to-weight on long tours.[^35]
- **Respect BMS trip stories.** A JK BMS saved a C80 conversion by tripping at 60 A when the rider pulled 70 A battery.
  - use the incident as a reminder to size packs around controller demand rather than bypassing protection.[^36]

## Safety & Reliability Tips

1. **Test all charging adapters at home before departure.** Verify voltage, current draw, and thermal behavior with a multimeter and infrared thermometer during bench charging sessions.[^pre-test]
2. **Carry backup charging bricks and cables.** Hotel outlets and standard 120 V receptacles remain the most reliable fallback when public infrastructure is unavailable or malfunctioning.[^backup]
3. **Log ride telemetry and charging sessions.** Track Wh consumed per mile, charge times, and thermal peaks to refine future tour plans and identify pack degradation early.[^telemetry]
4. **Plan routes with charging station density in mind.** Use PlugShare or ChargePoint maps to identify backup stations within 20–30 miles of primary stops in case of equipment failure or station downtime.[^route-planning]

- **Carry a vetted charger.** Budget 0–90 V/5 A AliExpress bricks (~€76 shipped) keep arriving late or DOA.
  - Mirono lines up disputes in advance
  - while others swallow the cost of a Grin Satiator to avoid repeated support fights on tour.[^37]
5. **Confirm delivery SOC and rebalance before tours.** Logistics warehouses often ship scooters between 30–50 % SOC even when some units arrive near 70–100 %; check and balance packs on arrival so you start long trips with known baselines.[^warehouse-soc]
6. **Keep packs warm in winter.** Riders commuting near freezing rely on heated battery bags or external heaters to hold cells above ~10 °C and reduce cold-weather voltage sag before setting out.[^winter-bags]
7. **Budget cold-weather PPE.** Winter riders treat full-face helmets and balaclavas as consumables.
  - expect to spend $120+ keeping replacements ready so gear stays warm and theft-resistant during sub-zero commutes.[^38]
- 8. **Adjust tire pressure for load.** Fleet technicians keep commuter tires at ≥20 psi and push heavy riders toward ~3.6 bar rear pressure when aiming for 60 km/h travel to fend off chronic punctures.[^39]
- 9. **Prioritise torque and thermal resilience.** Even burnout-focused city builds lean on manageable 20 S10 P packs with regen, valuing heat margin over chasing absolute top speed.[^40]
- 10. **Integrate track-safe enclosures.** Race officials now ban external battery bags at 100 km/h events because loose packs eject and ignite in crashes.
  - touring builds destined for track days need fully enclosed compartments.[^41]

### Tour Readiness Checklist (Latest Review Actions)

- **Pack an adapter kit that covers public pedestals and cafes.** The crew now keeps J1772 adapters, travel bricks, and café-friendly extension cords grouped so mid-route stops don’t sag small packs below ≈3 V per cell on mountain grades.[^42]
- **Brush up on fast-charging etiquette.** Revisit how you’ll brief café staff, share bays, and shuffle scooters before rain rolls in; the latest review explicitly called for folding etiquette reminders into the touring checklist rather than leaving them scattered across chat threads.[^43]
- **Note ferrofluid and hub-prep chores.** A fresh maintenance list now ties Segway-class hub service (ferrofluid fills, temp probes) to tour prep so high-mileage weeks don’t start with neglected drivetrains.[^44][^45]

## Regional Compliance & Planning Pressure

- Spanish riders are already budgeting stealthier frames, €3 k shell swaps, or downsized scooters ahead of the 2027 crackdown.
  - expect to validate deck dimensions (e.g., Achilleus vs. Thunder) and controller placements against DGT listings when planning tours across stricter jurisdictions.[^46]
- Scandinavia’s patchwork rules complicate touring—Denmark lacks theft coverage above ≈20 km/h, Sweden caps legal scooters at 250 W/20 km/h with pedal assist, and Finland sells ~€50–€70/year policies that lift limits to roughly 1 kW when throttles stay discreet.[^scand_rules]
- Swiss roadside checks now cite riders more than €1 300 and even impound scooters if they appear modified; Rosheee’s scooter was seized until paperwork proved a “250 W” profile, highlighting the need for stealth modes and documentation.[^swiss_fines]
  - Enforcement benches log instantaneous wattage—one dual-motor build limited to 250 W/25 km/h still read 665 W—so keep invoices and compliance paperwork ready before the officer plugs in the dyno.[^swiss_peaktest]
- Local enforcement is already citing micromobility capable of >35 mph in Las Vegas after a fatal crash; high-speed builds need route plans that respect posted limits and rider training when sharing public streets.[^47][^48]
5. **Prep for winter efficiency hits.** Riders report Wh/km nearly doubling in freezing conditions (≈30 Wh/km vs. 18–20 Wh/km in summer); keep packs warm indoors or add gentle heaters before rolling out in sub-zero weather.[^49]

## Follow-Up Actions Needed

- Draft EV-charger etiquette notes covering time limits, single-handle session restrictions, and communication protocols for mixed scooter/EV charging scenarios.[^follow-etiquette]
- Document field-tested J1772 adapter builds (wiring, fusing, voltage range) to provide builders with reproducible charging solutions.[^follow-adapter]
- Validate generator-assisted touring feasibility with real-world weight, noise, and reliability data before promoting as a viable long-distance strategy.[^follow-generator]
- Capture thermal management strategies for multi-hour charging sessions at public stations, including active cooling thresholds and BMS temperature monitoring.[^follow-thermal]

## Source Notes

[^tour-viable]: Noname's 18-hour, 150-mile Appalachian ride demonstrating VESC thermal stability and feasibility of long-range touring.[^50]
[^ev-infra]: Public charging infrastructure discussions covering Level 2 access and protocol requirements.[^51]
[^j1772]: J1772 adapter compatibility allowing 2 A trickle charging up to BMS-limited rates from Level 2 pedestals.[^51]
[^app-locks]: App-controlled charging stations releasing only one handle per session, requiring coordination for group tours.[^51]
[^tesla-protocol]: Tesla plug requirement for protocol triggers (FoCcci boards) to initiate charging handshake sequences.[^51]
[^charge_port_discipline]: Source: knowledge/notes/input_part003_review.md†L525-L525
[^type2_pilot]: Source: knowledge/notes/input_part003_review.md†L527-L527
[^generator]: Theoretical 1 kW generator + 5 kWh pack configuration for coast-to-coast touring attempts.[^50]
[^adj_voltage]: Source: knowledge/notes/input_part001_review.md†L504-L505
[^ip001-whkm]: Source: data/vesc_help_group/text_slices/input_part001.txt†L19187-L19265
[^ip001-whkm-loop]: Source: data/vesc_help_group/text_slices/input_part001.txt†L19187-L19265
[^ip001-whkm-mass]: Source: data/vesc_help_group/text_slices/input_part001.txt†L19206-L19227
[^ip001-regen-eff]: Source: data/vesc_help_group/text_slices/input_part001.txt†L17551-L17690
[^appalachian]: Noname's 150-mile ride log demonstrating thermal management and extended touring feasibility.[^50]
[^noname-96mi]: Noname’s 20 S 35 P commuter pack recorded 96 miles of riding while burning roughly half its 10.2 kWh capacity.[^52]
[^pack-sizing]: General guidance for 7–10 kWh pack sizing for 150+ mile tours based on consumption testing.
[^deck-extender]: Source: knowledge/notes/input_part000_review.md, line 159.
[^ip001-wind-drag]: Source: data/vesc_help_group/text_slices/input_part001.txt†L24891-L24895
[^etiquette]: Charging bay etiquette reminders to respect time limits and communicate with EV drivers.
[^charge-rate]: Communication guidelines for low-rate vs. full-rate charging to avoid station confusion.
[^thermal-charging]: Thermal monitoring recommendations during extended charging sessions.
[^generator-limits]: Weight, noise, and practicality constraints for generator-assisted touring.
[^backup-chargers]: Backup charging brick recommendations for hotel stops and emergency scenarios.
[^capacity-buffer]: Reserve capacity planning (20–30 %) for voltage sag, weather, and detours.
[^bms-thermal]: BMS thermal management during sustained high-capacity pack discharge.
[^charge-limits]: BMS charge current limit matching for public infrastructure compatibility.
[^telecom-fast]: Fast-charging cautions highlighting ≈1 C limits on Samsung 40T/Molicel P42A packs and pricing for telecom-derived 50–60 A chargers.[^53]
[^ip001-adjustable-psu]: Source: data/vesc_help_group/text_slices/input_part001.txt†L24277-L24284
[^bms-balance]: Yamal and 🇪🇸AYO#74’s top-off routine.
  - rest before balance charging, limit equalisation to 2–4 A, and tighten drift thresholds near 0.01 V to stop endless micro-charging.[^54]
[^pre-test]: Pre-departure adapter testing protocols with multimeter and thermal validation.
[^backup]: Backup charging equipment recommendations for reliability.
[^telemetry]: Ride telemetry logging for consumption tracking and pack health monitoring.
[^route-planning]: Route planning recommendations using PlugShare/ChargePoint for backup station identification.
[^g30-charge-limit]: Segway G30 packs accept the 5 A fast charger but BMS firmware trips above ~8 A, and smaller F-series/Xiaomi packs prefer ≤4 A continuous from adjustable supplies.[^55]
[^ip001-ali-bait]: Source: data/vesc_help_group/text_slices/input_part001.txt†L27505-L27534
[^warehouse-soc]: Warehouse storage guidance recommending 30–50 % SOC even when some scooters arrive closer to 70–100 %, prompting balance checks on delivery.[^56]
[^winter-bags]: Winter commuters keeping packs above ~10 °C with heated battery bags or external heaters to limit cold-weather sag.[^57]
[^follow-etiquette]: Follow-up action to draft detailed EV-charger etiquette notes.[^58]
[^follow-adapter]: Follow-up action to document field-tested J1772 adapter builds.
[^follow-generator]: Follow-up action to validate generator-assisted touring with real-world data.
[^follow-thermal]: Follow-up action to capture thermal management strategies for extended charging sessions.
[^scand_rules]: Source: knowledge/notes/input_part001_review.md†L535-L537
[^swiss_fines]: Source: knowledge/notes/input_part001_review.md†L601-L603
[^swiss_peaktest]: Source: knowledge/notes/input_part001_review.md†L610-L611


## References

[^vsett_weekend_loop]: Source: knowledge/notes/input_part008_review.md†L464-L465
[^sanyo_spintend_benchmark]: Source: knowledge/notes/input_part008_review.md†L466-L466
[^1]: Source: knowledge/notes/input_part004_review.md†L225-L225
[^2]: Source: knowledge/notes/input_part009_review.md†L325-L325
[^3]: Source: data/vesc_help_group/text_slices/input_part013.txt†L16054-L16058
[^4]: Source: data/vesc_help_group/text_slices/input_part013.txt†L16440-L16452
[^5]: Source: knowledge/notes/input_part013_review.md†L200-L200
[^6]: Source: knowledge/notes/input_part013_review.md†L240-L240
[^7]: Source: data/vesc_help_group/text_slices/input_part013.txt†L16112-L16121
[^8]: Source: data/vesc_help_group/text_slices/input_part013.txt†L16347-L16376
[^9]: Source: knowledge/notes/input_part000_review.md†L486-L489
[^10]: Source: knowledge/notes/input_part006_review.md†L133-L133
[^11]: Source: knowledge/notes/input_part011_review.md†L301-L305
[^12]: Source: knowledge/notes/input_part012_review.md†L208-L213
[^13]: Source: knowledge/notes/input_part012_review.md†L209-L213
[^14]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L91124-L91132
[^15]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L93450-L93478
[^16]: Source: knowledge/notes/input_part005_review.md†L142-L142
[^17]: Source: knowledge/notes/input_part009_review.md†L349-L349
[^18]: Source: knowledge/notes/input_part005_review.md†L143-L143
[^19]: Source: knowledge/notes/input_part005_review.md†L331-L338
[^20]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24033-L24075
[^21]: Source: data/vesc_help_group/text_slices/input_part005.txt†L23075-L23093
[^22]: Source: data/vesc_help_group/text_slices/input_part005.txt†L23941-L23953
[^23]: Source: knowledge/notes/input_part011_review.md†L101-L106
[^celler]: Source: data/vesc_help_group/text_slices/input_part004.txt†L19666-L19710
[^adjustable-20s]: Source: data/vesc_help_group/text_slices/input_part004.txt†L22000-L22046
[^charger-trims]: Source: data/vesc_help_group/text_slices/input_part004.txt†L17519-L17544
[^24]: Source: knowledge/notes/input_part011_review.md†L209-L212
[^25]: Source: knowledge/notes/input_part011_review.md†L460-L463
[^26]: Source: knowledge/notes/input_part012_review.md†L303-L303
[^27]: Source: knowledge/notes/input_part012_review.md†L211-L212
[^28]: Source: knowledge/notes/input_part012_review.md†L274-L279
[^29]: Source: knowledge/notes/input_part012_review.md†L310-L310
[^30]: Source: knowledge/notes/input_part012_review.md†L286-L288
[^31]: Source: knowledge/notes/input_part012_review.md†L414-L414
[^32]: Source: knowledge/notes/input_part011_review.md†L332-L339
[^33]: Source: knowledge/notes/input_part006_review.md†L180-L180
[^34]: Source: knowledge/notes/input_part006_review.md†L228-L228
[^35]: Source: knowledge/notes/input_part012_review.md†L312-L316
[^36]: Source: knowledge/notes/input_part012_review.md†L280-L285
[^37]: Source: data/vesc_help_group/text_slices/input_part002.txt†L22438-L22450
[^38]: Source: knowledge/notes/input_part006_review.md†L91-L91
[^39]: Source: knowledge/notes/input_part006_review.md†L174-L174
[^40]: Source: knowledge/notes/input_part006_review.md†L229-L229
[^41]: Source: knowledge/notes/input_part006_review.md†L385-L385
[^42]: Source: knowledge/notes/input_part012_review.md†L307-L307
[^43]: Source: knowledge/notes/input_part012_review.md†L307-L308
[^44]: Source: knowledge/notes/input_part012_review.md†L306-L306
[^45]: Source: knowledge/notes/input_part012_review.md†L309-L309
[^46]: Source: knowledge/notes/input_part013_review.md†L238-L239
[^47]: Source: data/vesc_help_group/text_slices/input_part013.txt†L15064-L15090
[^48]: Source: data/vesc_help_group/text_slices/input_part013.txt†L15084-L15086
[^49]: Source: knowledge/notes/denis_all_part02_review.md†L115861-L115872
[^50]: Source: knowledge/notes/input_part013_review.md†L146-L146
[^51]: Source: knowledge/notes/input_part013_review.md†L147-L149
[^52]: Source: knowledge/notes/input_part013_review.md†L95-L95
[^53]: Source: knowledge/notes/input_part010_review.md†L245-L247
[^54]: Source: knowledge/notes/input_part010_review.md†L269-L270
[^55]: Source: knowledge/notes/input_part006_review.md†L75-L75
[^56]: Source: knowledge/notes/input_part006_review.md†L76-L76
[^57]: Source: knowledge/notes/input_part006_review.md†L77-L77
[^58]: Source: knowledge/notes/input_part013_review.md†L516-L516
