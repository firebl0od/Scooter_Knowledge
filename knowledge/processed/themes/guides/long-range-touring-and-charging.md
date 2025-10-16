# Long-Range Touring & Public Charging Guide

## TL;DR
- Multi-hundred-mile scooter tours are feasible with proper pack sizing (≥5 kWh), thermal management, and access to Level 2 EV charging infrastructure, but riders must plan charging etiquette, adapter compatibility, and backup power strategies before leaving home base.[^tour-viable][^ev-infra]
- Public charging demands J1772 adapters, protocol triggers for Tesla plugs (FoCcci boards or equivalent), and awareness that app-locked stations typically release only one handle per session—coordinate with EV drivers and respect charging bay time limits.[^j1772][^tesla-protocol]
- Generator-assisted touring remains experimental; a 1 kW portable generator paired with a 5+ kWh pack could theoretically support coast-to-coast attempts, but weight, noise, and reliability trade-offs need field validation before serious planning.[^generator]

## Long-Range Riding Benchmarks
- Noname logged an 18-hour Appalachian ride covering roughly 150 miles at 50 mph bursts, noting the VESC stayed cool and demonstrating that high-capacity packs (likely 10+ kWh class given the distance) enable extended touring when thermal management is dialed in.[^appalachian]
- Pack sizing for 150+ mile rides typically requires 7–10 kWh or more depending on terrain, speed, and rider weight; builders planning tours should log Wh/mi consumption during shorter test rides to estimate realistic range before committing to long routes.[^pack-sizing]
- Jason’s alpine shakedown pushed a 30 S 6 P pack to ≈3 V per cell on steep climbs before regen only recovered a few percent on the descent—proof that mountain routes drain small packs rapidly and require pre-planned mid-ride charging stops.【F:knowledge/notes/input_part012_review.md†L208-L213】
- Yamal carries a fast charger into cafés on 100 km+ itineraries; his 20 S 10 P pack returns roughly 100 km of range in mild weather when he tops up partway through the day.【F:knowledge/notes/input_part012_review.md†L209-L213】

## Public Charging Strategies

### Level 2 EV Infrastructure
- J1772 adapters allow scooter packs to draw from public Level 2 pedestals, supporting charge rates from as low as 2 A (for emergency trickle charging) up to the pack's BMS limit when paired with appropriate cables and adapters.[^j1772]
- App-controlled charging stations (ChargePoint, Blink, etc.) typically release only one charging handle per session, so riders planning group tours must coordinate with EV drivers or use multiple stations to charge simultaneously.[^app-locks]
- Tesla destination chargers and Superchargers require protocol triggers such as FoCcci boards to initiate handshake sequences; without these adapters, the plug will not energize even with a physical J1772 adapter installed.[^tesla-protocol]

### Charging Etiquette & Best Practices
1. **Respect charging bay time limits.** Move scooters promptly once charged to free stations for EV drivers who often have fewer alternatives than scooter riders with portable packs.[^etiquette]
2. **Communicate charge rate expectations.** Inform station operators or fellow users when drawing only 2–3 A for safety testing versus full-rate charging to avoid confusion about bay availability.[^charge-rate]
3. **Plan for single-handle sessions.** Budget extra time when touring in groups, as most app-based systems won't release multiple handles simultaneously from the same account.[^app-locks]
4. **Monitor thermal margins.** Long charging sessions at high rates (≥6 A per pack) can heat cells and BMS hardware, so log temperatures and adjust charge current if ambient temps exceed 30 °C or packs show elevated thermal readings.[^thermal-charging]
5. **Top to 80–85 % when weather windows open.** Riders wait for rain to clear before tapping public chargers or EV adapters, then stop around 80 % state of charge to preserve pack longevity and resume touring without wasting time on slow CV phases.【F:knowledge/notes/input_part012_review.md†L209-L213】

### Adapter & Hardware Recommendations
- **J1772 to scooter pack adapter:** Verify pin compatibility, voltage range (most scooters charge at 48–100 V), and current rating before purchasing or fabricating custom adapters. The latest build notes call for logging pilot-resistor values, conductor gauges, and enclosure choices so future 3 kW tour adapters are reproducible rather than ad-hoc harnesses.【F:knowledge/notes/input_part012_review.md†L303-L303】
- **FoCcci or equivalent Tesla protocol board:** Required for Tesla plug compatibility; confirm firmware version supports your charging voltage before field deployment.
- **Portable multimeter and voltage monitor:** Essential for verifying station output voltage and diagnosing adapter issues before connecting expensive battery packs.
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
- **BMS thermal limits:** High-capacity packs (≥7 kWh) under sustained discharge can heat BMS MOSFETs or balance boards; log temps during test rides and add active cooling if boards exceed 50 °C under load.[^bms-thermal]
- **Charge rate planning:** If fast-charging via Level 2 infrastructure, ensure BMS charge current limits (typically 10–30 A for scooter-class hardware) match adapter capabilities and won't trip thermal or over-current protections.[^charge-limits]
- **Document pack mass and expectations.** Noname’s 20 S 32 P Samsung 35E pack stores ≈112 Ah (≈9.4 kWh) and delivers ~70 mi while leaving the scooter near 350 lb; he’d now favour a lighter 32 S 20 P layout for better torque-to-weight on long tours.【F:knowledge/notes/input_part012_review.md†L312-L316】
- **Respect BMS trip stories.** A JK BMS saved a C80 conversion by tripping at 60 A when the rider pulled 70 A battery—use the incident as a reminder to size packs around controller demand rather than bypassing protection.【F:knowledge/notes/input_part012_review.md†L280-L285】

## Safety & Reliability Tips
1. **Test all charging adapters at home before departure.** Verify voltage, current draw, and thermal behavior with a multimeter and infrared thermometer during bench charging sessions.[^pre-test]
2. **Carry backup charging bricks and cables.** Hotel outlets and standard 120 V receptacles remain the most reliable fallback when public infrastructure is unavailable or malfunctioning.[^backup]
3. **Log ride telemetry and charging sessions.** Track Wh consumed per mile, charge times, and thermal peaks to refine future tour plans and identify pack degradation early.[^telemetry]
4. **Plan routes with charging station density in mind.** Use PlugShare or ChargePoint maps to identify backup stations within 20–30 miles of primary stops in case of equipment failure or station downtime.[^route-planning]

### Tour Readiness Checklist (Latest Review Actions)
- **Pack an adapter kit that covers public pedestals and cafes.** The crew now keeps J1772 adapters, travel bricks, and café-friendly extension cords grouped so mid-route stops don’t sag small packs below ≈3 V per cell on mountain grades.【F:knowledge/notes/input_part012_review.md†L307-L307】
- **Brush up on fast-charging etiquette.** Revisit how you’ll brief café staff, share bays, and shuffle scooters before rain rolls in; the latest review explicitly called for folding etiquette reminders into the touring checklist rather than leaving them scattered across chat threads.【F:knowledge/notes/input_part012_review.md†L307-L308】
- **Note ferrofluid and hub-prep chores.** A fresh maintenance list now ties Segway-class hub service (ferrofluid fills, temp probes) to tour prep so high-mileage weeks don’t start with neglected drivetrains.【F:knowledge/notes/input_part012_review.md†L306-L306】【F:knowledge/notes/input_part012_review.md†L309-L309】

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
[^pack-sizing]: General guidance for 7–10 kWh pack sizing for 150+ mile tours based on consumption testing.
[^etiquette]: Charging bay etiquette reminders to respect time limits and communicate with EV drivers.
[^charge-rate]: Communication guidelines for low-rate vs. full-rate charging to avoid station confusion.
[^thermal-charging]: Thermal monitoring recommendations during extended charging sessions.
[^generator-limits]: Weight, noise, and practicality constraints for generator-assisted touring.
[^backup-chargers]: Backup charging brick recommendations for hotel stops and emergency scenarios.
[^capacity-buffer]: Reserve capacity planning (20–30 %) for voltage sag, weather, and detours.
[^bms-thermal]: BMS thermal management during sustained high-capacity pack discharge.
[^charge-limits]: BMS charge current limit matching for public infrastructure compatibility.
[^pre-test]: Pre-departure adapter testing protocols with multimeter and thermal validation.
[^backup]: Backup charging equipment recommendations for reliability.
[^telemetry]: Ride telemetry logging for consumption tracking and pack health monitoring.
[^route-planning]: Route planning recommendations using PlugShare/ChargePoint for backup station identification.
[^follow-etiquette]: Follow-up action to draft detailed EV-charger etiquette notes.【F:knowledge/notes/input_part013_review.md†L516-L516】
[^follow-adapter]: Follow-up action to document field-tested J1772 adapter builds.
[^follow-generator]: Follow-up action to validate generator-assisted touring with real-world data.
[^follow-thermal]: Follow-up action to capture thermal management strategies for extended charging sessions.
