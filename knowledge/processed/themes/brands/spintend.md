# Spintend Controllers Brand Dossier

## TL;DR
- Community veterans now default to Spintend when budget Makerbase/Flipsky boards melt down—the Ubox lineup shrugs off BMS trips and keeps scooters rolling where 75xxx-class ESCs lock wheels or self-destruct under the same abuse.[^1]
- Thermal success hinges on treating every Spintend as a passively cooled module: clamp the aluminum base to a 3–5 mm plate with paste or pads and reserve generous deck space for 25 × 15 cm heatsinks so dual stacks stay below ~70 °C.[^2]
- Treat the ADC lighting bridge as an accessory tap, not a main switch—its ~12 V / 3 A rail and updated harnesses simplify pods and brake throttles, but real kill circuits still require relays, smart-BMS buttons, or loop keys.[^3]
- Stock MOSFETs still fail when builders push >40 A of field weakening on 20 S packs; plan on HY- or HSBL-class swaps before chasing high-ERPM targets on 85150/85250 hardware.[^15]
- Random throttle surges continue to surface on 85 V/240 A, 100 V/100 A, and even v2 85 V/250 A units, so budget time for filtering, shielded cabling, and harness inspections when diagnosing jitter complaints.[^16]

## Product Line Cheat Sheet
| Model | Nominal Pack Window | Field Envelope & Use Case | Distinguishing Notes |
| --- | --- | --- | --- |
| Dual Ubox 75/100 | 16–20 S | ≈150 A phase per side when cooled properly; duals still popular for compact dual-motor decks | Legacy two-in-one chassis remains a 75 V-class unit that survives racing loads when given airflow.[^4] |
| Ubox Lite (single) | 16–20 S | ≈150 A battery/phase; dual Lite = two singles under one lid | Lite boards share hardware with the dual 100/100, letting riders mix singles or duals to balance heat against mounting simplicity.[^5] |
| Ubox 85/200 (12‑FET) | 18–22 S | 250 A battery / ~350 A phase with cooling; dual stacks log ~500 A combined bursts | Tuners report faults only past ~450 A phase when thermals are dialed in, making the 12‑FET the workhorse for 20–22 S superbikes.[^6] |
| Ubox 85/240 (rev.) | 18–22 S (marketing 24 S with care) | Targeting ~240 A battery in a smaller shell for tight decks | New single-chassis revision ships with 8 AWG leads, reversible exits, and a lower price than the outgoing 250 A model, prompting direct-import demand.[^7] |
| Dual 75/100 (early rev.) | 16–20 S | Needs external filtering for the noisiest installs | First batches omitted phase filters; retrofit boards or external filters tame switching noise on sensitive builds.[^8] |

## Operating Guardrails
### Battery & Phase Current Targets
- Stock firmware keeps 85‑250 hardware near 150 A battery / 200 A phase continuous, with seasoned tuners only flashing no-limit binaries once motors and cooling can stomach 400 A phase spikes.[^9]
- Real-world logs show dual Lite builds requesting 160/140 A phase yet barely topping 100 A peaks, underscoring the need to capture data from both controllers before chasing higher numbers.[^10]
- Heavy riders continue blowing 12‑FET stages even with modest throttle inputs; treat 20 S commuter builds as derated compared with lightweight race scooters and reserve “fat VESC” footprints when riders plus cargo exceed ~120 kg.[^17]

### Voltage & Regen Discipline
- Riders stepping into 22 S still back off charge voltage or disable heavy regen to avoid 100 V spike failures that plague 75xxx competitors; Ubox-class controllers tolerate the packs but demand measured braking ramps.[^11]
- Firmware caps near 300 A phase on early 85/200 units until owners compile the unofficial “no limits” branch—use sparingly because support teams treat it as a warranty break.[^12]

## Thermal & Packaging Playbook
- Mount each ESC against aluminum with thermal compound on both faces; copper spacers are discouraged because corrosion outweighs the modest conductivity gain once you already have aluminum-to-aluminum contact.[^2]
- A single 25 × 15 cm heatsink can host two 12‑FET bodies without fin trimming, giving dual builds a repeatable footprint for under-deck cooling plates.[^2]
- Plan airflow and strain relief so BMS cutoffs do not shock the controllers—Spintend hardware coasts through pack trips, but keeping harnesses tidy prevents the upstream faults that still kill rivals.[^1]
- Water-cooled loops can hold 85250 cores within ~4 °C of ambient at 90 A battery / 130 A phase, yet those builds still suffer tariff-driven price creep and encourage interest in the teased 18‑FET alternative positioned around €180.[^18]

## Wiring & Accessory Integration
- The latest v3 ADC adapter arrives with proper harness plugs; pair it with the documented throttle pinout (3.3 V red, ground black, ADC1 signal) and keep the NRF port free for Bluetooth modules.[^3][^13]
- Budget the ADC rail for light loads only: dual 18 W lamps already stress the ~12 V / 3 A output, so horns, halogens, or RGB kits belong on dedicated DC/DC converters triggered by the adapter or a relay.[^3]
- When reusing OEM dashes or switches, add pull-down resistors or relays instead of tying controller 5 V rails together—shared ignition lines without isolation have cooked boards in cramped conversions.[^3]

## Commissioning & Diagnostics Checklist
1. **Audit firmware limits before tuning.** Confirm the phase ceiling in VESC Tool; early 85/200 units stall at ~300 A until reflashed, and Lite boards mirror duals so mismatched limits skew traction control.[^12][^5]
2. **Log both controllers on every shakedown.** Aggregate CAN data to verify commanded vs. actual amps; many “weak” builds simply read one side and miss per-motor dropouts.[^10]
3. **Stage regen carefully on 22 S builds.** Drop charge voltage a few volts or cap braking current until you validate pack and controller headroom with logs.[^11]
4. **Inspect phase filters on older duals.** Populate missing components or add external LC filters if noise, thermal, or EMI issues surface on early 75/100 hardware.[^8]
5. **Verify accessory wiring.** Keep lighting loads within the ADC bridge limits and route any kill-switch expectations through smart-BMS logic or physical loop keys.[^3]

## Procurement & Support Signals
- ExpressLine DDP shipments are clearing customs in about a week for EU buyers, yet import offices still assess duties despite the “duty paid” label.[^14]
- Regional mark-ups can double MSRP—Israeli riders now see ~$575 street pricing, pushing them toward direct factory orders or alternative brands when budgets are tight.[^14]
- Sellers occasionally under-declare controller value (e.g., listing €160 modules at €55); while it trims duties, buyers carry the audit risk if customs spot the mismatch.[^14]
- Expect warranty friction on unexplained failures—retailers are already pointing at firmware versions (e.g., 6.05) to deny coverage—so document software builds, logs, and install photos before submitting RMAs.[^19]
- Spintend’s capacitor bank remains thin for oversized QS hubs; heavy builders increasingly migrate to shunt-sensed platforms (Ennoid MK8, Tronic X12) when repeated gate-driver deaths surface.[^20]

## Source Notes
[^1]: Makerbase/Flipsky QC issues versus Spintend reliability, plus reports that Ubox controllers coast through BMS trips instead of locking wheels.【F:knowledge/notes/input_part005_review.md†L17-L20】【F:knowledge/notes/input_part008_review.md†L31-L36】
[^2]: Community thermal practices for Spintend hardware, including aluminum plate mounting guidance and dual-controller heatsink sizing.【F:knowledge/notes/input_part008_review.md†L25-L30】【F:knowledge/notes/input_part010_review.md†L531-L531】
[^3]: Limits and wiring expectations for Spintend’s ADC adapter, including delivered harness connectors and accessory-current ceilings.【F:knowledge/notes/input_part005_review.md†L57-L58】【F:knowledge/notes/input_part007_review.md†L221-L223】
[^4]: Dual Ubox 75/100 capabilities and continued 75 V-class usage in race builds.【F:knowledge/notes/input_part010_review.md†L189-L190】
[^5]: Packaging flexibility and current targets for Ubox Lite singles vs. the dual 100/100 chassis.【F:knowledge/notes/input_part010_review.md†L92-L98】
[^6]: Field logs showing 12‑FET Ubox battery and phase limits when cooled.【F:knowledge/notes/input_part010_review.md†L190-L190】
[^7]: Details on the revised 85 V/240 A single Ubox with 8 AWG leads and reversible exits.【F:knowledge/notes/input_part010_review.md†L535-L536】
[^8]: Early dual 75/100 revisions shipping without populated phase filters.【F:knowledge/notes/input_part005_review.md†L167-L167】
[^9]: Recommended continuous vs. peak targets for 85-250 hardware and firmware-imposed voltage/current caps.【F:knowledge/notes/input_part010_review.md†L567-L567】
[^10]: Dual-controller log evidence showing commanded vs. actual current disparities on Lite builds.【F:knowledge/notes/input_part010_review.md†L564-L564】
[^11]: Regen strategies and voltage precautions for 21–22 S packs to avoid over-voltage failures.【F:knowledge/notes/input_part005_review.md†L152-L153】
[^12]: Firmware-imposed ~300 A phase ceiling on early 85/200 controllers and the risks of flashing unofficial builds.【F:knowledge/notes/input_part007_review.md†L236-L236】
[^13]: Documented throttle pinout and NRF/Bluetooth layout for Spintend controllers.【F:knowledge/notes/input_part010_review.md†L526-L526】
[^14]: Shipping timelines, regional price hikes, and customs under-valuation practices affecting Spintend buyers.【F:knowledge/notes/input_part010_review.md†L179-L179】【F:knowledge/notes/input_part010_review.md†L361-L361】【F:knowledge/notes/input_part005_review.md†L100-L100】
[^15]: Reports of MOSFET deaths when applying 45 A of field weakening on stock 20 S Spintend 85150 setups without upgrading to HY/HSBL devices.【F:knowledge/notes/input_part014_review.md†L21-L21】
[^16]: Continuing throttle jitter complaints across 85 V/240 A, 100 V/100 A, and v2 85 V/250 A controllers that require wiring and filtering mitigations.【F:knowledge/notes/input_part014_review.md†L17-L17】
[^17]: Heavy riders overloading 12‑FET 85/250 controllers despite gentle throttle ramps, prompting recommendations for larger “fat VESC” hardware.【F:knowledge/notes/input_part014_review.md†L19-L19】
[^18]: Water-cooled 85250 thermal performance data alongside price creep and interest in a forthcoming €180 18‑FET revision.【F:knowledge/notes/input_part014_review.md†L20-L20】
[^19]: Warranty denials tied to firmware blame, encouraging thorough documentation before submitting RMAs.【F:knowledge/notes/input_part014_review.md†L14-L14】
[^20]: Capacitor-bank shortcomings on heavy QS hub builds driving riders toward shunt-sensed alternatives like Ennoid MK8 or Tronic X12.【F:knowledge/notes/input_part014_review.md†L16-L16】
