# Spintend Controllers Brand Dossier

## TL;DR
- Community veterans now default to Spintend when budget Makerbase/Flipsky boards melt down—the Ubox lineup shrugs off BMS trips and keeps scooters rolling where 75xxx-class ESCs lock wheels or self-destruct under the same abuse.[^1]
- Even with the shared “no limits” firmware, single Ubox installs treat ~80 A battery and 130 A phase as the sensible ceiling—the hardware clamp near 300 A still applies, so cooling and telemetry matter more than chasing the unlocked config file.[^40]
- Early 85250 V1 controllers used current-transformer sensing that saturates near 100 A and complicates auto-detection, so Smart Repair now nudges heavy builds toward shunt-based MK8/X12 footprints (or waits for the teased 18-FET refresh) unless the board has been reworked with proven Toll MOSFETs.[^ct_limit]
- Thermal success hinges on treating every Spintend as a passively cooled module: clamp the aluminum base to a 3–5 mm plate with paste or pads and reserve generous deck space for 25 × 15 cm heatsinks so dual stacks stay below ~70 °C.[^2]
- Treat the ADC lighting bridge as an accessory tap, not a main switch—its ~12 V / 3 A rail and updated harnesses simplify pods and brake throttles, but real kill circuits still require relays, smart-BMS buttons, or loop keys.[^3]
- Stock MOSFETs still fail when builders push >40 A of field weakening on 20 S packs; plan on HY- or HSBL-class swaps before chasing high-ERPM targets on 85150/85250 hardware.[^20]
- Random throttle surges continue to surface on 85 V/240 A, 100 V/100 A, and even v2 85 V/250 A units, so budget time for filtering, shielded cabling, and harness inspections when diagnosing jitter complaints.[^17]
- Spintend sunset the 85/250 and now routes the 85/240 through a New Jersey hub for U.S. buyers—stock spares if you rely on the higher-rated board because the replacement is easier to source but capped a touch lower.[^logistics_update]
- Ordering direct remains the safest path when you need factory support; Matthew flagged AliExpress markups on 85150/85250s and prefers Spintend’s own store for warranty help, while Protopulse fills the gap as a vetted EU reseller when the official storefront glitches.[^direct_order]
- Community RMAs still funnel through James Soderstrom, who has repaired failed driver stages and even replaced missing BLE modules for 🇪🇸AYO#74’s crew—budget his services (and shipping time) when planning spares.[^soderstrom]

## Inbound QC & Power-Up Protocol
1. **Full teardown and dry clean before first power.** Crack the enclosure, remove conformal covers, vacuum or IPA-wipe solder balls, and inspect gate-driver rails prior to energising the board.[^41]
2. **Torque and upgrade the high-current connectors.** Swap factory XT90 jumpers for QS8/AS150-class hardware or busbars with proper lugs, and route control wiring through shielded CAT6A pairs to avoid melted solder-only links.[^42]
3. **Hunt for stray conductive debris.** Rental-fleet autopsies found solder beads bridging phase outputs on dual installs—confirm nothing rattles inside before closing the case.[^43]
4. **Respect symmetric power loops.** When disconnecting packs, pull both battery leads or open the main contactor before touching CAN; popping one lead while the bus is live has blown Ubox Lite ESD protection.[^44]
5. **Document baseline idle draw.** Expect roughly 20 mA standby current with the latching power button off—any illuminated switch LED signals a wiring fault.[^45]
6. **Only enable the phase filter during detection.** Spintend confirmed the toggle exists to stabilise the motor wizard; leaving it on while riding injects noise and can resurrect ABS overcurrent faults.[^54]

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
- Smart Repair’s track-tested window keeps refreshed 85 250/240 stacks reliable around 380 A phase, 480 A absolute, and ~200 A battery once you strip paint, add thermal paste, and clamp the base to added aluminum mass.[^smartrepair_85250]
- The revised 85250 V2 may handle 22 S, but early adopters are still collecting long-term data before trusting race builds at ≈92 V—treat the voltage headroom as experimental until logs prove otherwise.【F:knowledge/notes/input_part013_review.md†L709-L710】
- Daily riders now treat 85150s as ~150 A battery / 250 A phase hardware even after flashing the no-limits BIN; pushing harder cooked stock-firmware units within days when regen stayed disabled.[^safe_envelope]
- **Single Ubox 100/100 daily safe zone:** Lonnyo 65 H commuters are holding tunes near 130–135 A phase with 85–90 A battery and 150–180 A absolute, trimming duty to ~98 % and starting FW around 88 % to clear residual stutter without climbing past 40 °C case temps.[^u100_daily]
- With upgraded MOT1111T silicon and external cooling, riders have logged ~480 A phase bursts per controller on 85250 stacks—proof the hardware has headroom when thermals are engineered properly.[^hackintosh_burst]
- Field logs from daily 18 S commuters show 85150 hardware getting unhappy above ~240 A phase; trimming tunes to roughly 220 A phase, 90 A battery, and ≈60 A of field weakening kept case temps stable without neutering performance.【F:data/vesc_help_group/text_slices/input_part013.txt†L3769-L3770】【F:data/vesc_help_group/text_slices/input_part013.txt†L4184-L4184】
- Real-world logs show dual Lite builds requesting 160/140 A phase yet barely topping 100 A peaks, underscoring the need to capture data from both controllers before chasing higher numbers.[^10]
- Solo commuters copying the shared 300 A hardware-limit BIN still hold tunes near 80 A battery / 130 A phase until they validate heatsinking and airflow; the file only removes software clamps—it does not grant extra headroom.[^40]
- Firmware bundles ship in 100 A and 300 A flavours; Smart Repair urges riders to stay on the 100 A pack for warranty support because the higher bin both voids coverage and still bottlenecks battery input near 60 A even when phase currents spike around 147 A.[^firmware-bins]
- Even the new 85/240 single pushes 80 H hubs toward 95 km/h on 22 S, so the smaller shell still demands proper cooling and current discipline before chasing dual-motor-class speeds.[^u85240_speed]
- Heavy riders continue blowing 12‑FET stages even with modest throttle inputs; treat 20 S commuter builds as derated compared with lightweight race scooters and reserve “fat VESC” footprints when riders plus cargo exceed ~120 kg.[^18]
- Start with conservative dual-drive baselines: 17 S builds have settled near 2×120 A phase / 2×90 A battery / 2×180 A absolute, while 16 S commuters ride closer to 2×100 A phase / 2×60 A battery until thermal logs show headroom.[^30]
- Remember the Spintend bridge mirrors battery current to both controllers—profile toggles or 1WD/2WD switches must isolate CAN or power, otherwise the smaller front ESC still sees the rear controller’s amps.[^bridge_mirror]
- Bluetooth staying alive while the controller refuses new connections often traces to a sagging logic regulator or cooked CAN resistor—treat the symptom as a pre-failure warning rather than a firmware glitch.[^arnau_dropout]

## Sourcing & Support Signals
- Direct Spintend orders remain the recommended channel when you need firmware help or replacement boards; AliExpress resellers add markup without improving support and have left newcomers stranded after failures.【F:knowledge/notes/input_part013_review.md†L229-L234】
- Smart Repair reminded techs that clearing an accidental “paired” flag on the BLE module requires plugging into USB and resetting the state inside VESC Tool, so document that workflow for remote support calls.【F:knowledge/notes/input_part013_review.md†L431-L432】
- EU buyers lean on Protopulse as a verified reseller when Spintend’s own shop misbehaves, and 🇪🇸AYO#74 credits James Soderstrom with board-level repairs and replacement BLE modules when local support falls short.【F:knowledge/notes/input_part013_review.md†L236-L244】
- When builders weigh Flipsky 75100 duals or FT85BD stacks, veterans now steer them toward Spintend’s 85150 lineup (with the ADC3 accessory bridge) or MP2 DIY builds as the practical upgrade path for 85 V-class torque scooters.【F:knowledge/notes/input_part013_review.md†L311-L311】

### Voltage & Regen Discipline
- Riders stepping into 22 S still back off charge voltage or disable heavy regen to avoid 100 V spike failures that plague 75xxx competitors; Ubox-class controllers tolerate the packs but demand measured braking ramps.[^11]
- Ubox 100/100 revisions still cap regen safely below full pack voltage; Smart Repair warns the stage ships without ST-Link pads or beefy 12 V rails and arrives set around 135 A phase / 180 A absolute until you validate cooling.[^u100_baseline]
- Firmware caps near 300 A phase on early 85/200 units until owners compile the unofficial “no limits” branch—use sparingly because support teams treat it as a warranty break.[^12]
- Watch for BMS thermal trips even on Spintend hardware—dual Ubox owners running 2×135 A phase / 2×71 A battery still logged pack over-temp around 90 A spikes; monitor pack sag and internal resistance monthly.[^31]
- Size battery groups for the torque you plan: 65 H motors needed roughly 150–200 A battery per side, and undersized parallel packs tripped companion BMSes when regen slammed add-on modules.[^32]
- Treat BMS cutoffs as glide events, not anchors—Spintend hardware coasts when a pack trips, but trim regen near full charge (≈76.6 V on 20 S) to avoid repeated over-voltage faults.[^1][^33]
- Builders continue popping 85150s on 20 S when they stack MTPA or heavy field weakening on top of aggressive tunes—derate or upgrade MOSFETs before chasing those maps.【F:knowledge/notes/input_part013_review.md†L781-L781】
- Replacement HY power stages sourced through Raphaël Foujiwara are still capped at ≤20 S (~400 A phase) unless you add his HF filter and cooling mods; even experienced builders with the new boards are holding off on 22 S experiments until thermal issues are solved.【F:knowledge/notes/input_part011_review.md†L31-L31】【F:knowledge/notes/input_part011_review.md†L169-L169】

### Field-Weakening & High-Load Limits
- Stock 85150 MOSFETs overheat quickly once you layer 45 A of field weakening on top of 105–120 A battery and 150–175 A phase requests; riders chasing higher ERPMs swap in HY/HSBL Toll packages with hotplate reflow or back FW down to ~50 A at 87 % duty.[^20]
- 85240 hardware is happiest at 20 S—one HY-revision board tolerated 21 S, but pushing to 22 S without auditing supporting components risks the same runaway failures seen on overloaded 12-FET stages.[^22]
- Heavy riders continue blowing 85/250 units even with gentle ramps, so dual-motor “fat VESC” upgrades or derated current ceilings remain the conservative path for >20 S commuters.[^18]

## Thermal & Packaging Playbook
- Mount each ESC against aluminum with thermal compound on both faces; copper spacers are discouraged because corrosion outweighs the modest conductivity gain once you already have aluminum-to-aluminum contact.[^2]
- Retain or improve OEM pad compression—Ubox V2 temperature deltas often trace back to NTC placement and clamp pressure more than exotic pad swaps.[^25]
- **Water-cooled base plates keep daily pulls tame.** Custom Ubox 100/100 plates dropped MOSFET temps from ~54 °C back to 40 °C within a minute during 130 A phase pulls even in 35 °C ambient once duty and FW trims were dialed.[^u100_cooling]
- Bolt controllers directly to bare metal structure: sand paint, polish deck plates, and clamp the Ubox to aluminum or copper spreaders to hold MOSFETs near 55 °C at 50 A battery / 120 A phase.[^26]
- Maintain pad thickness discipline; thicker thermal replacements have pushed case temps toward 70 °C when compression was lost.[^27]
- Mount 6‑FET minis on 3–5 mm aluminum plates with paste on both faces—copper sandwiches corrode faster than they help once you already couple to aluminum.[^28]
- Share load across dual drives when possible: single-controller hill climbs hit ~60 °C while dual-drive equivalents stay below 40 °C, underscoring the headroom gained by splitting torque.[^29]
- A single 25 × 15 cm heatsink can host two 12‑FET bodies without fin trimming, giving dual builds a repeatable footprint for under-deck cooling plates.[^2]
- Plan airflow and strain relief so BMS cutoffs do not shock the controllers—Spintend hardware coasts through pack trips, but keeping harnesses tidy prevents the upstream faults that still kill rivals.[^1]
- Bonding the 85150 case to the scooter frame with thermal adhesive and watching per-motor temperature logs helps spot miswired phases or sensor faults before they torch a controller.[^21]
- Re-tap the tiny M2.5 bosses or print adapter plates when mounting 85/240 and Lite boards—the flat housings ship without hardware and benefit from thicker pads or thermal glue plus reinforced brackets.[^mounting_threads]
- Repurpose dead 75/200 baseplates as aux heat spreaders—JPPL’s stack adds aluminum spacers and CNC clamps while Shlomozero sketches radiator blocks tied into Dualtron side plates to keep HY power stages cool.[^baseplate_spreader]
- JPPL’s X12 installs highlight the packaging ceiling: the accessory rail only delivers 5 V / 150 mA, so plan on a dedicated buck converter if you need 12 V lighting or telemetry alongside the ADC bridge.[^53]
- Water-cooled loops can hold 85250 cores within ~4 °C of ambient at 90 A battery / 130 A phase, yet those builds still suffer tariff-driven price creep and encourage interest in the teased 18‑FET alternative positioned around €180.[^52]
- Protect exposed decks with sacrificial hardware—Pandalgns’ 100 % infill ASA “anti-fall” sliders bolt under the controller stack and survive low-sides without chewing through housings, so stash the STL alongside mounting hardware plans.【F:data/vesc_help_group/text_slices/input_part013.txt†L3633-L3634】

## Wiring & Accessory Integration
- The latest v3 ADC adapter arrives with proper harness plugs; pair it with the documented throttle pinout (3.3 V red, ground black, ADC1 signal) and keep the NRF port free for Bluetooth modules.[^3][^13]
- Budget the ADC rail for light loads only: dual 18 W lamps already stress the ~12 V / 3 A output, so horns, halogens, or RGB kits belong on dedicated DC/DC converters triggered by the adapter or a relay—and Dualtron riders now reserve the rail for brake lights after burning controllers by running both headlight and taillight sets directly.【F:knowledge/notes/input_part013_review.md†L430-L431】[^3]
- **Hang heavy accessories on an external buck.** A dedicated 12 V/20 A converter powering horns, pumps, fans, and lights only sips ~4–6 A from a 60 V pack, and trimming controller battery amps preserves BMS headroom during horn spikes.[^accessory_buck]
- When reusing OEM dashes or switches, add pull-down resistors or relays instead of tying controller 5 V rails together—shared ignition lines without isolation have cooked boards in cramped conversions.[^3]
- The ADC adapter already handles turn-signal strips and Spin dial throttles; use the supplied JST harness for ADC3, calibrate legacy Spin Y pods manually, and keep phase leads equal length when trimming looms.[^23]
- Anthony’s Spinny throttle and Davega experiments confirmed the harness follows standard RX/TX wiring and that the CNC Rion throttle he admired is still just a hall sensor in a premium shell—temper performance expectations accordingly when swapping grips.【F:knowledge/notes/input_part013_review.md†L517-L519】
- Sequential LED turn signals still require extra logic; riders rewiring looms from scratch report the VESC signal wires cannot drive cascaded strips directly, so plan dedicated controllers if you expect chase effects.[^seq_led]
- If throttle noise persists, compress the ADC window so idle rests near 0.8–1.0 V, verify chassis grounding, and add filtering before blaming firmware for runaway acceleration reports.[^17][^24]
- Leverage the ADC adapter without killing CAN—run ADC1/2 through the splitter while leaving UART dashboards online, and diode-isolate lighting feeds so traction control and telemetry stay intact.[^34]
- Feed auxiliary rails from a clean supply: Ubox Lite lacks a native 12 V rail, so power the ADC adapter from an external DC-DC while keeping grounds common to prevent lighting glitches.[^35]
- Sequence dash power carefully—Flipsky Smart Display harnesses have already blown multiple ADC daughterboards when 5 V was applied before 12 V; energise the lighting rail first, then logic power, and keep grounds shared.【F:data/vesc_help_group/text_slices/input_part013.txt†L2375-L2387】【F:data/vesc_help_group/text_slices/input_part013.txt†L3188-L3193】
- Before paralleling both 12 V outputs for accessories, confirm whether your enclosure actually splits regulators; riders probing KOX Smart Display installs suspect some 85× shells share a single buck that cannot sustain doubled loads.【F:data/vesc_help_group/text_slices/input_part013.txt†L4085-L4114】
- Mind standby behaviour before adding smart switches—the latching Spintend button already isolates the logic rail with minimal drain; external anti-spark solutions are optional unless you need hard battery isolation.[^45]

## Commissioning & Diagnostics Checklist
1. **Audit firmware limits before tuning.** Confirm the phase ceiling in VESC Tool; early 85/200 units stall at ~300 A until reflashed, and Lite boards mirror duals so mismatched limits skew traction control.[^12][^5]
2. **Flash vendor firmware and let auto-detection pick the hardware profile.** Spintend-supplied BINs and automatic R3 detection remain the safe path; forcing V6 targets or manual overrides has bricked controllers on the bench.[^46]
3. **Validate motor detection results.** Limited-edition hubs have returned ~270 A recommendations despite ~200 A safe limits, and some Ubox V2 units only auto-detect ~88 A versus ~135 A on V1—log outputs and set limits manually when they drift.[^47][^48]
4. **Disable regen during PSU testing.** Spinning up field-weakening on a bench supply can over-voltage the source; keep regen off until testing on a full battery stack.[^49]
5. **Capture fault codes before power-cycling.** If ABS overcurrent trips during early rides, dump VESC `faults` logs before rebooting so you can correlate spikes with wiring or observer changes.[^50]
6. **Log both controllers on every shakedown.** Aggregate CAN data to verify commanded vs. actual amps; many “weak” builds simply read one side and miss per-motor dropouts.[^10]
7. **Stage regen carefully on 22 S builds.** Drop charge voltage a few volts or cap braking current until you validate pack and controller headroom with logs.[^11]
8. **Inspect phase filters on older duals.** Populate missing components or add external LC filters if noise, thermal, or EMI issues surface on early 75/100 hardware.[^8]
9. **Verify accessory wiring.** Keep lighting loads within the ADC bridge limits and route any kill-switch expectations through smart-BMS logic or physical loop keys.[^3]

## Procurement & Support Signals
- ExpressLine DDP shipments are clearing customs in about a week for EU buyers, yet import offices still assess duties despite the “duty paid” label.[^14]
- Regional mark-ups can double MSRP—Israeli riders now see ~$575 street pricing, pushing them toward direct factory orders or alternative brands when budgets are tight.[^14]
- Sellers occasionally under-declare controller value (e.g., listing €160 modules at €55); while it trims duties, buyers carry the audit risk if customs spot the mismatch.[^14]
- Expect warranty friction on unexplained failures—retailers are already pointing at firmware versions (e.g., 6.05) to deny coverage—so document software builds, logs, and install photos before submitting RMAs.[^19]
- Spintend’s capacitor bank remains thin for oversized QS hubs; heavy builders increasingly migrate to shunt-sensed platforms (Ennoid MK8, Tronic X12) when repeated gate-driver deaths surface.[^16]

## Failure Watchlist & Logging Habits
- Track voltage ambitions on the 85/150 carefully—units have failed at 20 S when stacked with high-Kv hubs, MTPA, and aggressive field weakening, so treat 22 S as experimental until more telemetry lands.[^36]
- Vet MOSFET swaps before chasing 200 A+: bargain JJmicro devices underperform while Huayi parts have held 20 kW loads below 40 °C, so confirm datasheets before reflowing silicon.[^37]
- Log every ride by exporting VESC Tool CSVs or bridging Android sessions to desktop so you can correlate current spikes, duty limits, and temps before relaxing guardrails.[^38]
- Inspect for contamination after heavy service—moisture ingress and solder splatter have spoofed temperature telemetry and shorted controllers even after repairs, so schedule post-ride inspections after rain or workshop work.[^39]
- Budget for QA misses: multiple 85/250s arrived DOA or died within weeks at 200 A battery / 170 A motor settings, pushing riders toward Seven or 3Shul spares while they wait on replacements.[^doa250]
- Capture restart procedures for silent latch-offs: Ubox 250s have quit at ~60 V/120 A with the LED still green, so log accessory-rail health and reset steps before blaming firmware flashes.【F:data/vesc_help_group/text_slices/input_part013.txt†L4545-L4549】
- Track the stubborn Ubox 100/100 shutdown bug—one unit refused to power down even with auto-off disabled, suggesting accessory bleed or stuck logic rails worth documenting before more commuters adopt the hardware.【F:knowledge/notes/input_part013_review.md†L464-L464】

## Source Notes
[^1]: Makerbase/Flipsky QC issues versus Spintend reliability, plus reports that Ubox controllers coast through BMS trips instead of locking wheels.【F:knowledge/notes/input_part005_review.md†L17-L20】【F:knowledge/notes/input_part008_review.md†L31-L36】
[^2]: Community thermal practices for Spintend hardware, including aluminum plate mounting guidance and dual-controller heatsink sizing.【F:knowledge/notes/input_part008_review.md†L25-L30】【F:knowledge/notes/input_part010_review.md†L531-L531】
[^3]: Limits and wiring expectations for Spintend’s ADC adapter, including delivered harness connectors and accessory-current ceilings.【F:knowledge/notes/input_part005_review.md†L57-L58】【F:knowledge/notes/input_part007_review.md†L221-L223】
[^4]: Dual Ubox 75/100 capabilities and continued 75 V-class usage in race builds.【F:knowledge/notes/input_part010_review.md†L189-L190】
[^5]: Packaging flexibility and current targets for Ubox Lite singles versus the dual 100/100 chassis.【F:knowledge/notes/input_part010_review.md†L92-L98】
[^6]: Field logs showing 12‑FET Ubox battery and phase limits when cooled.【F:knowledge/notes/input_part010_review.md†L190-L190】
[^7]: Details on the revised 85 V/240 A single Ubox with 8 AWG leads and reversible exits.【F:knowledge/notes/input_part010_review.md†L535-L536】
[^8]: Early dual 75/100 revisions shipping without populated phase filters.【F:knowledge/notes/input_part005_review.md†L167-L167】
[^9]: Recommended continuous versus peak targets for 85-250 hardware and firmware-imposed voltage/current caps.【F:knowledge/notes/input_part010_review.md†L567-L567】
[^10]: Dual-controller log evidence showing commanded versus actual current disparities on Lite builds.【F:knowledge/notes/input_part010_review.md†L564-L564】
[^11]: Regen strategies and voltage precautions for 21–22 S packs to avoid over-voltage failures.【F:knowledge/notes/input_part005_review.md†L152-L153】
[^12]: Firmware-imposed ~300 A phase ceiling on early 85/200 controllers and the risks of flashing unofficial builds.【F:knowledge/notes/input_part007_review.md†L236-L236】
[^13]: Documented throttle pinout and NRF/Bluetooth layout for Spintend controllers.【F:knowledge/notes/input_part010_review.md†L526-L526】
[^14]: Shipping timelines, regional price hikes, and customs under-valuation practices affecting Spintend buyers.【F:knowledge/notes/input_part010_review.md†L179-L179】【F:knowledge/notes/input_part010_review.md†L361-L361】【F:knowledge/notes/input_part005_review.md†L100-L100】
[^16]: Heavy QS hub loads overheating undersized Spintend capacitor banks and the push toward heavier-duty controllers.【F:knowledge/notes/input_part014_review.md†L16-L16】
[^firmware-bins]: Official Spintend firmware offers 100 A and 300 A battery-limit variants; the hotter bin voids warranty and still shows ≈60 A battery ceilings with ~147 A phase bursts in field logs.【F:knowledge/notes/input_part000_review.md†L42-L42】
[^ct_limit]: Early 85250 V1 current-transformer sensing saturating near 100 A and Smart Repair’s recommendation to pivot to shunt-based MK8/X12 footprints (with IPTC017N12NM6 swaps for Ennoid builds) until the 18-FET revision ships.【F:knowledge/notes/input_part014_review.md†L12-L13】
[^17]: Persistent throttle jitter complaints across multiple Ubox hardware revisions that require wiring and filtering fixes.【F:knowledge/notes/input_part014_review.md†L17-L17】
[^18]: Heavy riders continuing to burn 12-FET 85/250 hardware despite conservative ramps, reinforcing derating guidance.【F:knowledge/notes/input_part014_review.md†L19-L19】
[^19]: Warranty denials tied to firmware blame, underscoring the need to document software builds before submitting RMAs.【F:knowledge/notes/input_part014_review.md†L12-L22】
[^20]: Field-weakening failure case on 85150 hardware and guidance to cap FW or swap MOSFETs before chasing more ERPM.【F:knowledge/notes/input_part014_review.md†L21-L21】【F:knowledge/notes/input_part014_review.md†L167-L168】
[^21]: Thermal adhesive mounting tips, per-motor temperature monitoring, and reminders that workmanship faults still kill controllers.【F:knowledge/notes/input_part014_review.md†L22-L22】【F:knowledge/notes/input_part014_review.md†L45-L45】
[^22]: Voltage headroom cautions for 85240 revisions and the need for full-component audits before 22 S experiments.【F:knowledge/notes/input_part014_review.md†L205-L205】
[^23]: Turn-signal strip support, Spin dial harness guidance, and equal-length phase lead reminders for tidy installs.【F:knowledge/notes/input_part014_review.md†L208-L210】
[^24]: ADC window compression, grounding checks, and filtering strategies that resolved runaway throttle noise on compact Spintend builds.【F:knowledge/notes/input_part014_review.md†L85-L86】【F:knowledge/notes/input_part014_review.md†L220-L221】
[^25]: Comparative thermal readings showing OEM pad compression impacts on Ubox V2 temperature deltas.【F:knowledge/notes/input_part001_review.md†L181-L183】
[^26]: Deck-sanding and clamp-mount techniques that held Ubox cases near 55 °C under 50 A/120 A loads.【F:knowledge/notes/input_part001_review.md†L249-L250】
[^27]: Thermal pad shootout results where thicker aftermarket pads raised MOSFET temperatures.【F:knowledge/notes/input_part001_review.md†L855-L856】
[^28]: Mounting guidance for Spintend aluminum 6-FET units using 3–5 mm plates and thermal paste.【F:knowledge/notes/input_part008_review.md†L29-L29】
[^29]: Thermal headroom gains observed when sharing load across dual controllers versus single-drive pulls.【F:knowledge/notes/input_part008_review.md†L28-L28】
[^30]: Current baselines logged on 17 S and 16 S dual-drive Spintend builds.【F:knowledge/notes/input_part001_review.md†L207-L207】
[^31]: Observed 2×135 A phase / 2×71 A battery setups and associated BMS thermal trip warnings.【F:knowledge/notes/input_part001_review.md†L657-L662】
[^32]: Battery group sizing lessons from high-Kv hubs requiring ≥150 A battery per side and companion pack BMS trips during regen.【F:knowledge/notes/input_part008_review.md†L291-L291】【F:knowledge/notes/input_part008_review.md†L275-L276】
[^33]: Regen adjustments needed to clear BMS over-voltage faults around 76.6 V on 20 S packs.【F:knowledge/notes/input_part008_review.md†L607-L607】
[^34]: ADC adapter wiring with diode isolation while keeping UART dashboards online.【F:knowledge/notes/input_part009_review.md†L84-L86】
[^35]: Feeding Spintend’s ADC adapter from an external DC-DC on Ubox Lite builds.【F:knowledge/notes/input_part008_review.md†L606-L606】
[^hackintosh_burst]: Hackintoshhhh’s MOT1111T-equipped 85250 build tolerated ~480 A phase bursts per controller once the upgraded silicon and cooling were dialed in.【F:knowledge/notes/input_part013_review.md†L34-L34】
[^arnau_dropout]: Arnau Martinez Casals’ Ubox 250 stayed powered yet blocked Bluetooth pairing after a 60 V/120 A trip—evidence of failing regulators or CAN protection parts rather than a pure software fault.【F:knowledge/notes/input_part013_review.md†L61-L62】
[^direct_order]: Matthew’s reminder that direct-from-Spintend orders avoid AliExpress markups and keep warranty support responsive for 85150/85250 hardware.【F:knowledge/notes/input_part013_review.md†L227-L234】
[^soderstrom]: 🇪🇸AYO#74’s shout-out to James Soderstrom for repairing Spintend driver stages and fabricating replacement BLE modules during RMA backlogs.【F:knowledge/notes/input_part013_review.md†L236-L244】
[^u100_daily]: Matthew and ’lekrsu’ aligned on ~130–135 A phase, 85–90 A battery, and 150–180 A absolute as the dependable daily window for single Ubox 100/100 Lonnyo 65 H builds once duty and FW trims were set.【F:data/vesc_help_group/text_slices/input_part013.txt†L17015-L17084】
[^u100_cooling]: The same build’s custom water-cooled base plate shed ~14 °C within a minute at 130 A phase in 35 °C ambient tests, making back-to-back pulls viable.【F:data/vesc_help_group/text_slices/input_part013.txt†L17077-L17084】【F:data/vesc_help_group/text_slices/input_part013.txt†L17358-L17363】
[^accessory_buck]: Matthew’s accessory-rail math showed a 12 V/20 A converter only draws ~4–6 A from a 60 V pack while running horns, pumps, fans, and lights; he now trims controller battery amps to protect the BMS during horn spikes.【F:data/vesc_help_group/text_slices/input_part013.txt†L17300-L17340】【F:data/vesc_help_group/text_slices/input_part013.txt†L17449-L17477】
[^safe_envelope]: Rogerio’s stock-firmware 85250 failed within days at 180 A phase / 80 A battery with regen disabled, prompting the group to flash the no-limits firmware but cap daily tunes near 150 A battery / 250 A phase while keeping enclosures clean.【F:knowledge/notes/input_part013_review.md†L225-L234】
[^36]: Spintend 85/150 failures at 20 S under heavy field-weakening stress.【F:knowledge/notes/input_part009_review.md†L87-L87】
[^37]: MOSFET reliability comparisons favouring Huayi devices over cheaper alternatives for 200 A-class loads.【F:knowledge/notes/input_part009_review.md†L88-L88】
[^38]: Recommended CSV logging workflows via VESC Tool and Android bridge methods.【F:knowledge/notes/input_part001_review.md†L149-L150】
[^39]: Moisture contamination spoofing temperature telemetry until enclosures were cleaned and resealed.【F:knowledge/notes/input_part008_review.md†L40-L40】
[^logistics_update]: Spintend discontinuing the 85/250 while routing 85/240 shipments through a New Jersey hub so U.S. buyers see faster delivery and minimal tariffs, leaving the higher-rated board scarce.[【F:knowledge/notes/input_part012_review.md†L111-L135】【F:knowledge/notes/input_part012_review.md†L379-L405】
[^smartrepair_85250]: Smart Repair’s community briefing pegged dependable limits for 85 250/240 controllers at ≈380 A phase, 480 A absolute, and 200 A battery provided the frame is bare metal with thermal paste and a clamp plate adding extra mass.【F:knowledge/notes/input_part013_review.md†L601-L605】
[^u100_baseline]: Smart Repair’s teardown of the Ubox 100/100 highlights its 22 S limit, ≈135 A phase / 180 A absolute defaults, lack of ST-Link pads, and the need to tame regen unless you’re ready for MOSFET swaps.【F:knowledge/notes/input_part012_review.md†L48-L48】
[^u85240_speed]: Single 85/240 builds have already pushed Lonnyo 80 H hubs to ~95 km/h on 22 S, underscoring that the compact case still needs race-grade cooling before chasing dual-drive numbers.【F:knowledge/notes/input_part012_review.md†L24-L24】
[^seq_led]: Sequential LED strips overrun the ADC turn-signal line without helper logic, so riders rewire lighting looms or add controllers when they want chase effects.【F:knowledge/notes/input_part012_review.md†L481-L481】
[^mounting_threads]: Riders printing adapter plates, adding 0.5 mm pads, or retapping the tiny M2.5 bosses because 85/240/Lite housings ship without sturdy mounting ears or hardware.[【F:knowledge/notes/input_part012_review.md†L419-L420】【F:knowledge/notes/input_part012_review.md†L465-L466】
[^doa250]: Reports of 85/250 controllers arriving DOA or failing quickly at 200 A battery / 170 A motor, prompting owners to migrate toward Seven or 3Shul alternatives.[【F:knowledge/notes/input_part012_review.md†L110-L111】【F:knowledge/notes/input_part012_review.md†L135-L136】
[^40]: Shared 300 A hardware-limit firmware for single Ubox installs and the reminder to keep real tunes near 80 A battery / 130 A phase with solid cooling.【F:knowledge/notes/input_part001_review.md†L12-L12】
[^41]: Solder-ball contamination on new Ubox V2 units prompting full disassembly and cleaning before use.【F:knowledge/notes/input_part001_review.md†L238-L240】
[^42]: Connector melt reports that led riders to upgrade to QS8/AS150 hardware with shielded control wiring.【F:knowledge/notes/input_part001_review.md†L242-L244】
[^43]: Fleet teardown showing stray solder balls bridging dual Spintend outputs and destroying both controllers.【F:knowledge/notes/input_part008_review.md†L268-L268】
[^44]: Ubox Lite ESD failures caused by unsymmetrical power disconnects while CAN remained energised.【F:knowledge/notes/input_part008_review.md†L269-L269】
[^45]: Standby draw measurements and LED behaviour on Spintend’s latching power switch.【F:knowledge/notes/input_part001_review.md†L214-L216】
[^46]: Community flashing workflow relying on Spintend-supplied BINs and auto-detection to avoid bricking controllers.【F:knowledge/notes/input_part001_review.md†L632-L633】
[^47]: Auto-detect anomalies recommending ~270 A on dual-phase hubs until limits are manually corrected.【F:knowledge/notes/input_part001_review.md†L824-L825】
[^48]: Ubox V1 vs. V2 motor detection variances demanding manual review of current limits.【F:knowledge/notes/input_part001_review.md†L889-L889】
[^49]: Bench-testing guidance to disable regen and field weakening on PSU-powered Spintend setups to avoid over-voltage damage.【F:knowledge/notes/input_part009_review.md†L84-L84】
[^50]: Fault logging workflow for ABS overcurrent and sensorless diagnostics before power-cycling, plus recommended CSV logging methods.【F:knowledge/notes/input_part001_review.md†L138-L150】
[^52]: Water-cooled 85250 performance data, tariff-driven price creep, and the teased €180 18-FET revision.【F:knowledge/notes/input_part014_review.md†L20-L20】
[^53]: Spintend X12 accessory rail limits and the need for external buck converters to power lighting or telemetry hardware.【F:knowledge/notes/input_part014_review.md†L140-L143】
[^54]: The phase-filter toggle should be used only during motor detection; leaving it active while riding reintroduces noise and ABS overcurrent errors.【F:knowledge/notes/input_part004_review.md†L31-L31】
[^bridge_mirror]: Spintend’s bridge keeps battery current mirrored across controllers—Smart Repair’s GT1 logs showed the front 150 A unit inheriting the rear controller’s battery amps until CAN or power was isolated.[【F:knowledge/notes/input_part011_review.md†L79-L79】【F:knowledge/notes/input_part011_review.md†L317-L317】
[^baseplate_spreader]: JPPL and Shlomozero are reusing dead 75/200 baseplates as auxiliary heatsinks with aluminum spacers and radiator blocks tied into Dualtron side plates to cool HY-equipped stages.【F:knowledge/notes/input_part011_review.md†L521-L521】
