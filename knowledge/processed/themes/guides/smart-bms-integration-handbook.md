# Smart BMS Integration Handbook

## TL;DR
- Oversize protection hardware and choose the right architecture for the pack: JK active-balancing boards bring dual 7 AWG busbars and remote toggles but recent self-burn reports push installers toward JBD/LLT or ANT units when decks are cramped or uptime is critical.[^1][^2][^3]
- Commission every pack like a high-energy experiment—enable both charge and discharge FETs before regen tests, validate balance-lead order, and log first rides because a single BMS cutoff or miswire has already nuked controllers and power stages that survived normal abuse.[^4][^5][^6]
- Treat balancing and calibration as routine maintenance: Daly boards need full charge/discharge learning and higher voltage to balance, while JK hardware wakes via the accessory display, runs active shuttling above ~0.015 V delta, and benefits from monthly thermal/IR audits.[^7][^8][^9]

---

## Selection Matrix (2024–2025 Field Data)
| BMS Family | Typical Continuous / Peak Rating | Strengths Observed in the Field | Known Pitfalls & Mitigations |
| --- | --- | --- | --- |
| **JK Smart (active balancer)** | 150 A / 300 A-class packs with dual 7 AWG busbars | Integrated active charge shuttling, remote charge/discharge toggles, long-range Bluetooth displays, antispark-friendly architecture.[^1][^10] | Multiple batches have cooked balance resistors or frozen after opening the discharge page; keep spares, add airflow for the warm copper planes, and prep harnesses for a JBD swap.[^2][^11] |
| **ANT Smart** | 200 A (70 mm-wide) to 240 A/600 A surge boards | Compact footprint, app-based current ramp controls, simultaneous cell balancing, proven on Weped FS builds and 20 s 7 p side-mounted packs.[^3][^12][^13] | Regen kills controllers if charge FETs stay disabled; app pairing quirks persist, and discharge toggles can trip Tronic stages—stage regen carefully and double-check settings after firmware updates.[^4][^14] |
| **LLT / JBD (passive)** | 60–100 A continuous in slim 10–17 s shells | Gentle pre-charge that protects controller caps, configurable temp limits, compact housings ideal for tight decks, credible JK alternative when space matters.[^3][^15] | Firmware listings exaggerate series counts; confirm real 21 s ceiling, watch balance current (≈100–160 mA), and document harness pinouts to avoid miswired sense leads.[^15][^16][^17] |
| **Daly Smart** | 35–80 A commuter packs | Cheap, ubiquitous, workable for light-duty commuters once calibrated; some riders still rely on them when better boards won’t fit.[^7][^18] | Balancing often waits for ≥4.18 V per cell, SoC drifts until full cycles are logged, and users call failure rates a “casino”—derate heavily and monitor cell temps monthly.[^7][^19][^20] |
| **Charge-only + Active Balancer** | Depends on fuse + controller limits | When space is scarce, builders fuse the main lead, rely on VESC undervoltage, and clip JK balancers across the stack to keep cells aligned without discharge FET losses.[^21] | Requires disciplined fusing and logging because discharge faults no longer open automatically; not suitable where regulatory compliance mandates full protection stages.[^21] |

## Commissioning & Wiring Guardrails
1. **Wake the hardware correctly.** JK boards ship asleep—use the €15 display or a 5–7 V bench supply, confirm charge/discharge toggles, and leave the board powered before sealing the pack.[^8]
2. **Validate sense-lead order before soldering B−.** Step through the harness at 3.5 V increments; reversing the negative pair has already cooked resistors on new ANT installs.[^5]
3. **Keep both FET banks enabled for regen tests.** Builders traced repeated ESC deaths to disabled charge FETs on JK smart boards—regen had nowhere to dump energy.[^4]
4. **Stage first rides with logging.** Riders lost Spintend and Makerbase controllers the moment a BMS tripped under load; gather current and voltage traces to verify the protection stays latched through braking and launches.[^6]
5. **Oversize connectors and plan airflow.** High-current boards warm noticeably near their limits—route copper planes into moving air or heatsinks, especially on JK units that reinforce traces with bus rods.[^10]
6. **Confirm advertised series support.** JBD listings still misstate 22 s capability; verify firmware revisions before wiring high-voltage packs.[^16]

## Regen & Current Budgeting
- **Cap braking currents around the BMS charge envelope.** Community testing now caps regen near 120 A and keeps charge/discharge FETs closed so controllers ride through decel events instead of seeing open-circuit spikes.[^6]
- **Treat BMS trips as design failures.** Flipsky 75100s and Wepoor power stages died instantly when the pack opened; prioritize parallel groups, pack cooling, and conservative regen so the BMS never has to intervene.[^6]
- **Oversize protection for big packs.** Large scooters are already paralleling multiple BMS boards or choosing 200 A-class ANT/JK units even for 70 A packs, proving that headroom beats marketing limits when chasing reliability.[^3][^22]

## Balancing & Calibration Practices
- **Map delta thresholds to chemistry.** Experienced builders trigger active balancing around 0.015–0.025 V and cap charge at ~4.15 V when longevity outweighs peak range.[^9]
- **Expect Daly learning cycles.** Their coulomb-counting SoC meters read low for several rides; plan full discharge/charge sessions or manual 100 % resets so telemetry aligns with reality.[^7]
- **Leverage telemetry displays.** JK screens offer long-range Bluetooth and remote toggles, effectively doubling as pack dashboards on scooters lacking dedicated HUD space.[^10]
- **Schedule thermal/IR checks.** JK smart boards run warm near 60 A; monthly infrared sweeps and rest torque checks catch rising resistance before it snowballs.[^10]

## Troubleshooting & Service Checklist
- **Document anti-theft workflows.** JK’s remote discharge disable doubles as a parking lock; confirm the board re-arms before rides to avoid brownouts.[^23]
- **Log balance behavior after storage.** JK units can self-immolate while idle and Daly boards stop balancing once “full”—review app history after downtime before sending the pack back into service.[^2][^19]
- **Teach recovery procedures.** Publish lead-order diagrams and wake-up checklists so drained JK packs (≈57 V on 20 s) or JBD miswires don’t strand riders without telemetry.[^17][^24]
- **Escalate when firmware toggles misbehave.** ANT app glitches that trip discharge FETs or JK UIs that freeze mid-session warrant immediate vendor contact and a fallback BMS plan.[^11][^14]

---

## Source Notes
[^1]: JK smart BMS hardware ships with dual 7 AWG busbars, active balancing, and remote charge/discharge toggles alongside long-range displays.【F:knowledge/notes/input_part001_review.md†L470-L488】【F:knowledge/notes/input_part001_review.md†L560-L560】
[^2]: Field reports detail JK balance resistors burning and boards freezing after opening the discharge page, pushing riders toward alternatives and prompting advice to keep spares ready.【F:knowledge/notes/input_part007_review.md†L175-L280】
[^3]: Builders oversize protection—pairing 200 A ANT/JK boards with 70 A packs or fitting 240 A ANT hardware into side-mounted 20 s builds—highlighting reliability-driven headroom choices.【F:knowledge/notes/input_part008_review.md†L12-L21】【F:knowledge/notes/input_part008_review.md†L489-L503】
[^4]: JK users traced repeated controller deaths to disabled charge FETs before regen tests, underscoring the need to keep both FET banks active.【F:knowledge/notes/input_part007_review.md†L27-L27】
[^5]: Miswired negative sense leads on an ANT install cooked components, reinforcing step-by-step voltage validation before soldering B−.【F:knowledge/notes/input_part008_review.md†L1980-L2055】
[^6]: BMS cutoffs have killed controllers mid-ride, and the community now caps regen near 120 A while logging early shakedowns to ensure protections stay latched.【F:knowledge/notes/input_part011_review.md†L15-L62】【F:knowledge/notes/input_part011_review.md†L276-L276】【F:knowledge/notes/input_part008_review.md†L688-L705】
[^7]: Daly smart boards rely on coulomb counting, demand ≥4.18 V to balance, and frequently misreport SoC until relearn cycles complete.【F:knowledge/notes/input_part001_review.md†L177-L705】
[^8]: JK packs ship in protection mode; installers wake them with a display or bench supply, toggle outputs, and leave the board energized before sealing the enclosure.【F:knowledge/notes/input_part001_review.md†L766-L768】
[^9]: Active-balancer veterans target 0.015–0.025 V delta triggers and conservative 4.15 V charge ceilings to balance longevity with usable capacity.【F:knowledge/notes/input_part001_review.md†L21820-L21880】
[^10]: JK boards reinforce traces with copper rods, run warm near their 60 A comfort zone, and provide remote telemetry screens for high-power scooters.【F:knowledge/notes/input_part001_review.md†L482-L560】【F:knowledge/notes/input_part001_review.md†L732-L733】
[^11]: Recent JK batches self-destructed even while idle or during basic app interactions, earning community warnings to prep JBD swaps as insurance.【F:knowledge/notes/input_part007_review.md†L175-L280】
[^12]: ANT hardware’s simultaneous balancing and compact footprint have proven reliable on long-lived Weped FS packs despite high peak currents.【F:knowledge/notes/input_part007_review.md†L286-L286】
[^13]: Side-mounted Vsett builds demonstrate ANT’s 240 A/600 A board fitting alongside controllers, validating the form factor for cramped decks.【F:knowledge/notes/input_part008_review.md†L489-L503】
[^14]: ANT discharge toggles and firmware glitches have bricked controllers during commissioning, so riders double-check app states after updates and stage regen conservatively.【F:knowledge/notes/input_part010_review.md†L315-L315】
[^15]: LLT/JBD smart boards earn praise for compact housings, gentle pre-charge, and configurable protections, giving builders a slimmer alternative to JK hardware.【F:knowledge/notes/input_part007_review.md†L192-L262】
[^16]: Community members caution that JBD firmware listings overstate maximum series counts—verify the real 21 s ceiling before wiring high-voltage packs.【F:knowledge/notes/input_part007_review.md†L64-L141】
[^17]: Harness diagrams and recovery guides remain in demand because miswired JBD/ANT balance leads are a recurring failure point during repairs.【F:knowledge/notes/input_part009_review.md†L453-L469】
[^18]: Budget builds continue to rely on Daly smart boards when higher-end options will not fit, accepting the trade-offs for commuter duty.【F:knowledge/notes/input_part001_review.md†L475-L499】
[^19]: Daly units often stop balancing once “full,” and riders derate them heavily after repeated over-discharge failures, treating the platform as a gamble.【F:knowledge/notes/input_part001_review.md†L475-L705】
[^20]: Monthly IR checks and conservative charge currents help detect rising resistance after Daly-class thermal trips.【F:knowledge/notes/input_part001_review.md†L662-L705】
[^21]: Kaabo Wolf builders documented charge-only BMS layouts fused at the main lead while clipping JK active balancers across the stack when discharge FET space was unavailable.【F:knowledge/notes/input_part002_review.md†L148-L312】
[^22]: Large motorcycle-class scooters now parallel multiple BMS boards so 20 s 24 p packs can share hundreds of amps safely.【F:knowledge/notes/input_part008_review.md†L13914-L13920】
[^23]: JK’s app-controlled discharge disable doubles as an anti-theft toggle once the pack is charged, a workflow riders now bake into parking habits.【F:knowledge/notes/input_part009_review.md†L35-L36】
[^24]: Recovery checklists cover JK low-voltage wake-ups around 57 V on 20 s packs and balance-lead troubleshooting so riders don’t lose telemetry after servicing.【F:knowledge/notes/input_part009_review.md†L29-L35】【F:knowledge/notes/input_part009_review.md†L467-L469】
