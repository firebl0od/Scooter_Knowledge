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
- Spin-Y batch-2 firmware now bakes in OEM dead-zone compensation, one-minute calibration, and steadier cruise control, with textured wheel options and longer harnesses queued for gloved riders—ship updated setup guides with every throttle kit.[^spin_y_fw]
- Community trust took a hit after Spin-Y storefront reviews disappeared; keep archiving QC feedback in case the official channels go quiet.【F:data/vesc_help_group/text_slices/input_part003.txt†L5746-L5748】

## Roadmap & Community Feedback
- **Copper single backlog.** Late-August updates confirmed ~100 pre-orders in flight (≈500 Spin-Y throttles) with copper-backed singles, seven-wire looms, and a dedicated onboarding video in production.[^copper_backlog]
- **Packaging goals.** Artem and the community want the 100 V single under ~25 × 52 × 85 mm with vertical FET mounting and modular accessory “integrator” boards so dual builds stay compact.[^roadmap_dims]
- **Aux-power debate.** Riders insisted on keeping a ~3 A 12 V rail because external bucks fail in service; Spintend’s removable integrator board is the compromise for non-essential IO without bloating the main PCB.[^aux_debate]
- **Industrial design asks.** Early photos triggered calls for slimmer housings, aluminum variants, vertical FET layouts, and deck-bolt mounting that shortens harness runs while holding MSRP near $119.[^packaging_feedback]
- **Thermal rethink.** Copper bases risk galvanic corrosion and resin-limited heat flow; 130–150 A runs already hit 80 °C, so testers are trying graphite pads, potting gaps, and waiting on the promised aluminum PCB revision.[^thermal_rethink]
- **Documentation backlog.** Builders still want clearer Spin-Y wiring and voltage diagrams; Spintend linked interim manuals, promised better graphics, is prepping quick-start one-pagers that spell out voltage ranges and cruise/regen mapping, and continues reworking clamp geometry plus longer harness options for 22.2 mm bars with shims and relief cuts.[^spin_y_docs][^spin_y_fw]
- **Gen2 throttle roadmap.** The upcoming Spin-Y doubles usable throw (≈65° drive / 35–45° regen), adds internal cruise wiring, dead-zone compensation for legacy controllers, magnet spacers for linear hall output, optional textured wheels, and longer harness choices—retrofit kits are planned once validation batches finish.[^spin_y_gen2]
- **Aluminum singles + tiering.** Aluminum-core singles are slated to ship with fdbl MOSFET options, thicker copper, SH8/6 AWG support, and firmware-locked S/M/L product tiers (~200–350 A phase) while Spintend expands staff after spotting solder balls on prototypes.[^aluminum_refresh]
- **DIY MP2 resurgence.** Community group buys for MP2 ESC PCBs plus F405 “pills” keep modular firmware alive, but they require separate MOSFET, DC-DC, and busbar sourcing—publish vetted BOMs before clones appear.[^mp2_update]
- **SmartDisplay demand.** Vsett owners and other high-speed riders want the 3.5 in SmartDisplay precisely to ditch phone mounts that eject devices at 140 km/h—the compact 10 cm × 6.5 cm housing with CAN telemetry and navigation prompts addresses those ergonomics complaints.【F:data/vesc_help_group/text_slices/input_part003.txt†L21249-L21272】【F:data/vesc_help_group/text_slices/input_part003.txt†L21255-L21271】
- **Navigation overlays.** Francois’s prototype merges SmartDisplay CAN telemetry with Waze alerts; document the overlay workflow so commuting builds can replicate the police-alert demo once the production firmware drops.【F:data/vesc_help_group/text_slices/input_part003.txt†L26600-L26606】

## Inbound QC & Power-Up Protocol
1. **Full teardown and dry clean before first power.** Crack the enclosure, remove conformal covers, vacuum or IPA-wipe solder balls, and inspect gate-driver rails prior to energising the board.[^41]
2. **Torque and upgrade the high-current connectors.** Swap factory XT90 jumpers for QS8/AS150-class hardware or busbars with proper lugs, and route control wiring through shielded CAT6A pairs to avoid melted solder-only links.[^42]
3. **Hunt for stray conductive debris.** Rental-fleet autopsies found solder beads bridging phase outputs on dual installs—confirm nothing rattles inside before closing the case.[^43]
4. **Inspect copper and aluminum bases for machining shavings.** Early aluminum-backed singles shipped with loose metal dust that can short MOSFET legs—blow out cavities and wipe the base before adding thermal pads.【F:data/vesc_help_group/text_slices/input_part003.txt†L6873-L6878】
5. **Respect symmetric power loops.** When disconnecting packs, pull both battery leads or open the main contactor before touching CAN; popping one lead while the bus is live has blown Ubox Lite ESD protection.[^44]
6. **Document baseline idle draw.** Expect roughly 20 mA standby current with the latching power button off—any illuminated switch LED signals a wiring fault.[^45]
7. **Only enable the phase filter during detection.** Spintend confirmed the toggle exists to stabilise the motor wizard; leaving it on while riding injects noise and can resurrect ABS overcurrent faults.[^54]
8. **Expose hidden firmware builds.** The phone app hides alternative firmware once paired; toggle “Show non-default firmware” in desktop VESC Tool or compile binaries locally before flashing bootloaders over USB.[^fw_distribution]

## Product Line Cheat Sheet
| Model | Nominal Pack Window | Field Envelope & Use Case | Distinguishing Notes |
| --- | --- | --- | --- |
| Dual Ubox 75/100 | 16–20 S | ≈150 A phase per side when cooled properly; duals still popular for compact dual-motor decks | Legacy two-in-one chassis remains a 75 V-class unit that survives racing loads when given airflow.[^4] |
| Ubox Lite (single) | 16–20 S | ≈150 A battery/phase; dual Lite = two singles under one lid | Lite boards share hardware with the dual 100/100, letting riders mix singles or duals to balance heat against mounting simplicity.[^5] |
| Ubox 85/200 (12‑FET) | 18–22 S | 250 A battery / ~350 A phase with cooling; dual stacks log ~500 A combined bursts | Tuners report faults only past ~450 A phase when thermals are dialed in, making the 12‑FET the workhorse for 20–22 S superbikes.[^6] |
| Ubox 85/240 (rev.) | 18–22 S (marketing 24 S with care) | Targeting ~240 A battery in a smaller shell for tight decks | New single-chassis revision ships with 8 AWG leads, reversible exits, and a lower price than the outgoing 250 A model, prompting direct-import demand.[^7] |
| Dual 75/100 (early rev.) | 16–20 S | Needs external filtering for the noisiest installs | First batches omitted phase filters; retrofit boards or external filters tame switching noise on sensitive builds.[^8] |

Spintend now colour-codes dual Ubox trims—red prioritises current for commuter tunes, purple adds TVS protection for safer 18 S work, and black pairs with 22 S builds so long as e-brake regen is capped under ~80 V—so log the shell colour before assuming voltage headroom.【F:knowledge/notes/input_part003_review.md†L223-L223】

## Operating Guardrails
### Battery & Phase Current Targets
- Stock firmware keeps 85‑250 hardware near 150 A battery / 200 A phase continuous, with seasoned tuners only flashing no-limit binaries once motors and cooling can stomach 400 A phase spikes.[^9]
- Real-world logs show dual Lite builds requesting 160/140 A phase yet barely topping 100 A peaks, underscoring the need to capture data from both controllers before chasing higher numbers.[^10]
- Solo commuters copying the shared 300 A hardware-limit BIN still hold tunes near 80 A battery / 130 A phase until they validate heatsinking and airflow; the file only removes software clamps—it does not grant extra headroom.[^40]
- Firmware bundles ship in 100 A and 300 A flavours; Smart Repair urges riders to stay on the 100 A pack for warranty support because the higher bin both voids coverage and still bottlenecks battery input near 60 A even when phase currents spike around 147 A.[^firmware-bins]
- Even the new 85/240 single pushes 80 H hubs toward 95 km/h on 22 S, so the smaller shell still demands proper cooling and current discipline before chasing dual-motor-class speeds.[^u85240_speed]
- Heavy riders continue blowing 12‑FET stages even with modest throttle inputs; treat 20 S commuter builds as derated compared with lightweight race scooters and reserve “fat VESC” footprints when riders plus cargo exceed ~120 kg.[^18]
- Start with conservative dual-drive baselines: 17 S builds have settled near 2×120 A phase / 2×90 A battery / 2×180 A absolute, while 16 S commuters ride closer to 2×100 A phase / 2×60 A battery until thermal logs show headroom.[^30]
- Remember the Spintend bridge mirrors battery current to both controllers—profile toggles or 1WD/2WD switches must isolate CAN or power, otherwise the smaller front ESC still sees the rear controller’s amps.[^bridge_mirror]
- Respect the published 17 S ceiling on 75 V duals (16 S with heavy regen) unless you move to the 100 V “black” chassis; red/purple shells run different FET stacks and leave less margin for 20 S experiments.[^voltage_ceiling]

### Voltage & Regen Discipline
- Riders stepping into 22 S still back off charge voltage or disable heavy regen to avoid 100 V spike failures that plague 75xxx competitors; Ubox-class controllers tolerate the packs but demand measured braking ramps.[^11]
- Ubox 100/100 revisions still cap regen safely below full pack voltage; Smart Repair warns the stage ships without ST-Link pads or beefy 12 V rails and arrives set around 135 A phase / 180 A absolute until you validate cooling.[^u100_baseline]
- Firmware caps near 300 A phase on early 85/200 units until owners compile the unofficial “no limits” branch—use sparingly because support teams treat it as a warranty break.[^12]
- Watch for BMS thermal trips even on Spintend hardware—dual Ubox owners running 2×135 A phase / 2×71 A battery still logged pack over-temp around 90 A spikes; monitor pack sag and internal resistance monthly.[^31]
- Size battery groups for the torque you plan: 65 H motors needed roughly 150–200 A battery per side, and undersized parallel packs tripped companion BMSes when regen slammed add-on modules.[^32]
- Treat BMS cutoffs as glide events, not anchors—Spintend hardware coasts when a pack trips, but trim regen near full charge (≈76.6 V on 20 S) to avoid repeated over-voltage faults.[^1][^33]
- Replacement HY power stages sourced through Raphaël Foujiwara are still capped at ≤20 S (~400 A phase) unless you add his HF filter and cooling mods; even experienced builders with the new boards are holding off on 22 S experiments until thermal issues are solved.【F:knowledge/notes/input_part011_review.md†L31-L31】【F:knowledge/notes/input_part011_review.md†L169-L169】

### Field-Weakening & High-Load Limits
- Stock 85150 MOSFETs overheat quickly once you layer 45 A of field weakening on top of 105–120 A battery and 150–175 A phase requests; riders chasing higher ERPMs swap in HY/HSBL Toll packages with hotplate reflow or back FW down to ~50 A at 87 % duty.[^20]
- 85240 hardware is happiest at 20 S—one HY-revision board tolerated 21 S, but pushing to 22 S without auditing supporting components risks the same runaway failures seen on overloaded 12-FET stages.[^22]
- Heavy riders continue blowing 85/250 units even with gentle ramps, so dual-motor “fat VESC” upgrades or derated current ceilings remain the conservative path for >20 S commuters.[^18]

## Thermal & Packaging Playbook
- **Track the 2022 copper-single experiments.** Early feedback from the 75/100 single community showed copper sandwich plates and resin potting still cooked past 80 °C once riders pushed 130 A phase, so reviewers started trialing graphite pads and waiting on the promised aluminum-core revision before ordering more copper hardware.[^graphite_triage]
- Mount each ESC against aluminum with thermal compound on both faces; copper spacers are discouraged because corrosion outweighs the modest conductivity gain once you already have aluminum-to-aluminum contact.[^2]
- Retain or improve OEM pad compression—Ubox V2 temperature deltas often trace back to NTC placement and clamp pressure more than exotic pad swaps.[^25]
- Bolt controllers directly to bare metal structure: sand paint, polish deck plates, and clamp the Ubox to aluminum or copper spreaders to hold MOSFETs near 55 °C at 50 A battery / 120 A phase.[^26]
- Maintain pad thickness discipline; thicker thermal replacements have pushed case temps toward 70 °C when compression was lost.[^27]
- Mirko’s 15 mm aluminum baseplate plus open-deck airflow kept dual 190 A phase / 70 A battery pulls near 52 °C, underscoring how enclosure design matters as much as MOSFET choice when evaluating upcoming aluminum-core revisions.【F:data/vesc_help_group/text_slices/input_part003.txt†L12443-L12494】
- Mount 6‑FET minis on 3–5 mm aluminum plates with paste on both faces—copper sandwiches corrode faster than they help once you already couple to aluminum.[^28]
- Share load across dual drives when possible: single-controller hill climbs hit ~60 °C while dual-drive equivalents stay below 40 °C, underscoring the headroom gained by splitting torque.[^29]
- A single 25 × 15 cm heatsink can host two 12‑FET bodies without fin trimming, giving dual builds a repeatable footprint for under-deck cooling plates.[^2]
- Plan airflow and strain relief so BMS cutoffs do not shock the controllers—Spintend hardware coasts through pack trips, but keeping harnesses tidy prevents the upstream faults that still kill rivals.[^1]
- Bonding the 85150 case to the scooter frame with thermal adhesive and watching per-motor temperature logs helps spot miswired phases or sensor faults before they torch a controller.[^21]
- Re-tap the tiny M2.5 bosses or print adapter plates when mounting 85/240 and Lite boards—the flat housings ship without hardware and benefit from thicker pads or thermal glue plus reinforced brackets.[^mounting_threads]
- Repurpose dead 75/200 baseplates as aux heat spreaders—JPPL’s stack adds aluminum spacers and CNC clamps while Shlomozero sketches radiator blocks tied into Dualtron side plates to keep HY power stages cool.[^baseplate_spreader]
- JPPL’s X12 installs highlight the packaging ceiling: the accessory rail only delivers 5 V / 150 mA, so plan on a dedicated buck converter if you need 12 V lighting or telemetry alongside the ADC bridge.[^53]
- Water-cooled loops can hold 85250 cores within ~4 °C of ambient at 90 A battery / 130 A phase, yet those builds still suffer tariff-driven price creep and encourage interest in the teased 18‑FET alternative positioned around €180.[^52]

## Wiring & Accessory Integration
- The latest v3 ADC adapter arrives with proper harness plugs; pair it with the documented throttle pinout (3.3 V red, ground black, ADC1 signal) and keep the NRF port free for Bluetooth modules.[^3][^13]
- Budget the ADC rail for light loads only: dual 18 W lamps already stress the ~12 V / 3 A output, so horns, halogens, or RGB kits belong on dedicated DC/DC converters triggered by the adapter or a relay.[^3]
- When reusing OEM dashes or switches, add pull-down resistors or relays instead of tying controller 5 V rails together—shared ignition lines without isolation have cooked boards in cramped conversions.[^3]
- The ADC adapter already handles turn-signal strips and Spin dial throttles; use the supplied JST harness for ADC3, calibrate legacy Spin Y pods manually, and keep phase leads equal length when trimming looms.[^23]
- Sequential LED turn signals still require extra logic; riders rewiring looms from scratch report the VESC signal wires cannot drive cascaded strips directly, so plan dedicated controllers if you expect chase effects.[^seq_led]
- If throttle noise persists, compress the ADC window so idle rests near 0.8–1.0 V, verify chassis grounding, and add filtering before blaming firmware for runaway acceleration reports.[^17][^24]
- Leverage the ADC adapter without killing CAN—run ADC1/2 through the splitter while leaving UART dashboards online, and diode-isolate lighting feeds so traction control and telemetry stay intact.[^34]
- Feed auxiliary rails from a clean supply: Ubox Lite lacks a native 12 V rail, so power the ADC adapter from an external DC-DC while keeping grounds common to prevent lighting glitches.[^35]
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

## Roadmap Signals & Known Pain Points (Aug–Oct 2022)
- **Production cadence:** Artem’s August 2022 status update confirmed 500 Spin-Y throttles were moving through hand-soldering while copper-backed singles entered onboarding—expect staggered deliveries and keep install guides handy for first-time buyers.[^2022_prod_update]
- **Traction-control heat spikes:** September test logs showed traction-control pulls heating Ubox singles faster than manual throttle launches; Artem said the next single would ship in 80 V and 100 V MOSFET flavours until the integrator board is ready, so plan cooling plates before flashing aggressive slip control.[^tc_heat]

## Late-2022 Iteration Highlights
- **Spin-Y Gen2 throttle polish.** Artem’s November updates locked in a 65° forward / 35° regen sweep, longer cabling, batch‑1 retrofit discounts, and a 1 mm magnet spacer that recovers two-thirds of the dead zone. Follow-on prototypes trialled wider diamond-cut wheels with glove-friendly textures, plus a single-magnet Spin-Y2 profile that flattens the output curve while Spintend recruits more QA coverage for the ramp-up.[^spin_y_gen2]
- **Control cluster & accessory planning.** The same push yielded a five-position thumb switch for blinkers, horn, and lighting along with reminders that Spintend’s light cluster *sources* 12 V—drive external relays instead of hanging accessories directly on the harness.[^spin_y_controls]
- **Aluminum-core Ubox roadmap.** Artem confirmed 6- and 12-FET aluminum singles are in flight with thicker copper, SH8/6 AWG support, and firmware-locked tiers that hold phase near 200–300 A and battery near 150 A until cooling is proven.[^aluminum_roadmap]
- **Single Ubox tuning guardrails.** Community clinics continue to steer 75 V singles toward ~130 A phase / 50–60 A battery, motor NTC retrofits, and bare-metal deck contact (scrape the paint) before chasing S/M/L tier upgrades or 200–350 A 6‑FET targets.[^single_tuning]
- **QC watchlist.** Fresh singles still arrive with missing screws or solder balls; pair the teardown with an ANT standby-draw check (a few tenths of a volt overnight is normal when the latching key is wired correctly) and document any power-board swaps before warranty claims.[^spintend_qc_nov]
- **Traction-control caution.** Rosheee’s rear Tronic fire after a traction-control slip renewed guidance to dial phase/battery limits and prefer front-only slip control when experimenting on Spintend duals.[^tc_failure]
- **ADC accessory budget.** Builders toasted the ADC adapter by adding 12 V fans to the board; treat it as a signal bridge and keep heavier loads on dedicated converters.[^adc_overload]
- **Diagnostics & rescue.** Mirono mapped the single’s unpopulated SWD pads to STM32 pins 46/49 and reminded rescuers to clean flux before micro-soldering, while SmartDisplay testers layered Waze alerts over Spintend CAN data for richer nav dashboards.[^stlink_waze]

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
[^36]: Spintend 85/150 failures at 20 S under heavy field-weakening stress.【F:knowledge/notes/input_part009_review.md†L87-L87】
[^37]: MOSFET reliability comparisons favouring Huayi devices over cheaper alternatives for 200 A-class loads.【F:knowledge/notes/input_part009_review.md†L88-L88】
[^38]: Recommended CSV logging workflows via VESC Tool and Android bridge methods.【F:knowledge/notes/input_part001_review.md†L149-L150】
[^39]: Moisture contamination spoofing temperature telemetry until enclosures were cleaned and resealed.【F:knowledge/notes/input_part008_review.md†L40-L40】
[^logistics_update]: Spintend discontinuing the 85/250 while routing 85/240 shipments through a New Jersey hub so U.S. buyers see faster delivery and minimal tariffs, leaving the higher-rated board scarce.[【F:knowledge/notes/input_part012_review.md†L111-L135】【F:knowledge/notes/input_part012_review.md†L379-L405】
[^u100_baseline]: Smart Repair’s teardown of the Ubox 100/100 highlights its 22 S limit, ≈135 A phase / 180 A absolute defaults, lack of ST-Link pads, and the need to tame regen unless you’re ready for MOSFET swaps.【F:knowledge/notes/input_part012_review.md†L48-L48】
[^u85240_speed]: Single 85/240 builds have already pushed Lonnyo 80 H hubs to ~95 km/h on 22 S, underscoring that the compact case still needs race-grade cooling before chasing dual-drive numbers.【F:knowledge/notes/input_part012_review.md†L24-L24】
[^copper_backlog]: Copper single backlog update covering ~100 pre-orders, seven-wire harnesses, and onboarding video plans for the 100 V single plus Spin-Y throttles.【F:knowledge/notes/input_part003_review.md†L358-L359】
[^roadmap_dims]: Packaging roadmap calling for ~25 × 52 × 85 mm housings with vertical FETs and modular auxiliary boards so dual builds stay compact.【F:knowledge/notes/input_part003_review.md†L359-L360】
[^aux_debate]: Riders demanded a retained 3 A 12 V rail while Spintend pushed a removable “integrator” accessory module as a compromise.【F:knowledge/notes/input_part003_review.md†L360-L360】
[^packaging_feedback]: Early copper-single photos triggered calls for slimmer housings, aluminum options, vertical FET layouts, deck-bolt mounting, and sub-$119 pricing.【F:knowledge/notes/input_part003_review.md†L361-L361】
[^thermal_rethink]: Copper-base thermal debates—galvanic risk, resin bottlenecks, 130–150 A runs at 80 °C, and experiments with graphite pads, potting gaps, and an aluminum PCB revision.【F:knowledge/notes/input_part003_review.md†L362-L362】
[^seq_led]: Sequential LED strips overrun the ADC turn-signal line without helper logic, so riders rewire lighting looms or add controllers when they want chase effects.【F:knowledge/notes/input_part012_review.md†L481-L481】
[^mounting_threads]: Riders printing adapter plates, adding 0.5 mm pads, or retapping the tiny M2.5 bosses because 85/240/Lite housings ship without sturdy mounting ears or hardware.[【F:knowledge/notes/input_part012_review.md†L419-L420】【F:knowledge/notes/input_part012_review.md†L465-L466】
[^doa250]: Reports of 85/250 controllers arriving DOA or failing quickly at 200 A battery / 170 A motor, prompting owners to migrate toward Seven or 3Shul alternatives.[【F:knowledge/notes/input_part012_review.md†L110-L111】【F:knowledge/notes/input_part012_review.md†L135-L136】
[^40]: Shared 300 A hardware-limit firmware for single Ubox installs and the reminder to keep real tunes near 80 A battery / 130 A phase with solid cooling.【F:knowledge/notes/input_part001_review.md†L12-L12】
[^41]: Solder-ball contamination on new Ubox V2 units prompting full disassembly and cleaning before use.【F:knowledge/notes/input_part001_review.md†L238-L240】
[^42]: Connector melt reports that led riders to upgrade to QS8/AS150 hardware with shielded control wiring.【F:knowledge/notes/input_part001_review.md†L242-L244】
[^spin_y_gen2]: Spin-Y Gen2 roadmap covering the 65° drive / 35–45° regen travel, internal cruise wiring, magnet spacers for hall linearity, textured wheel plans, and retrofit demand once validation batches ship.【F:data/vesc_help_group/text_slices/input_part003.txt†L11768-L11824】【F:data/vesc_help_group/text_slices/input_part003.txt†L11972-L12033】【F:data/vesc_help_group/text_slices/input_part003.txt†L12023-L12055】【F:data/vesc_help_group/text_slices/input_part003.txt†L12202-L12209】
[^spin_y_controls]: Five-way thumb cluster planning, MJ1 sag benchmarks, and reminders that the light cluster sources 12 V so relays should shoulder accessory loads.【F:knowledge/notes/input_part003_review.md†L121-L129】
[^aluminum_roadmap]: Spintend’s aluminum-core Ubox roadmap plus the 6- and 12-FET prototype targets for 200–300 A phase and 150 A battery ceilings.【F:knowledge/notes/input_part003_review.md†L112-L118】
[^spin_y_fw]: Spin-Y batch-2 firmware features (dead-zone compensation, one-minute calibration, steadier cruise) plus harness and wheel updates for gloved riders.【F:data/vesc_help_group/text_slices/input_part003.txt†L9349-L9352】【F:data/vesc_help_group/text_slices/input_part003.txt†L11768-L11824】【F:data/vesc_help_group/text_slices/input_part003.txt†L7767-L7805】【F:data/vesc_help_group/text_slices/input_part003.txt†L8600-L8605】
[^spin_y_docs]: Community requests for clearer Spin-Y wiring/voltage diagrams, interim manuals, and clamp-geometry tweaks for 22.2 mm bars.【F:data/vesc_help_group/text_slices/input_part003.txt†L3006-L3084】【F:data/vesc_help_group/text_slices/input_part003.txt†L3231-L3249】
[^aluminum_refresh]: Aluminum-core single roadmap outlining fdbl MOSFET options, thicker copper, SH8/6 AWG harnesses, product-tier planning, and QA staffing after spotting solder balls.【F:data/vesc_help_group/text_slices/input_part003.txt†L12321-L12355】【F:data/vesc_help_group/text_slices/input_part003.txt†L12890-L12957】【F:data/vesc_help_group/text_slices/input_part003.txt†L13533-L13633】【F:data/vesc_help_group/text_slices/input_part003.txt†L14880-L14946】
[^mp2_update]: DIY MP2 controller group buys, required component sourcing, and the need for vetted BOMs before clones arrive.【F:data/vesc_help_group/text_slices/input_part003.txt†L12357-L12383】
[^fw_distribution]: Firmware-delivery lessons covering hidden desktop toggles, app limitations, and compiling binaries before flashing bootloaders.【F:data/vesc_help_group/text_slices/input_part003.txt†L18185-L18336】【F:data/vesc_help_group/text_slices/input_part003.txt†L18775-L19035】
[^voltage_ceiling]: Artem and Gordan reiterating 17 S limits on 75 V duals (16 S with heavy regen) and mapping red/purple/black FET stacks, steering 20 S riders to the 100 V chassis.【F:data/vesc_help_group/text_slices/input_part003.txt†L22629-L22656】
[^single_tuning]: Single Ubox tuning clinic advice on 75 V builds: add motor NTCs, scrape paint for deck contact, and hold ~130 A phase / 50–60 A battery until cooling is validated.[【F:knowledge/notes/input_part003_review.md†L118-L118】
[^spintend_qc_nov]: November QC observations (missing screws, solder balls) plus ANT standby-draw expectations when the key throttle is wired correctly.【F:knowledge/notes/input_part003_review.md†L123-L129】
[^tc_failure]: Traction-control investigations after Rosheee’s Tronic failure and Artem’s reminder to limit phase/battery and prefer front-only TC on high-power builds.【F:knowledge/notes/input_part003_review.md†L116-L124】
[^adc_overload]: ADC adapter overload case where a 12 V fan fried the board, reinforcing that heavy loads belong on separate DC/DC rails.【F:knowledge/notes/input_part003_review.md†L126-L128】
[^stlink_waze]: Spintend single ST-Link pad mapping and the SmartDisplay + Waze overlay proof-of-concept on the same CAN backbone.【F:knowledge/notes/input_part003_review.md†L168-L192】
[^43]: Fleet teardown showing stray solder balls bridging dual Spintend outputs and destroying both controllers.【F:knowledge/notes/input_part008_review.md†L268-L268】
[^44]: Ubox Lite ESD failures caused by unsymmetrical power disconnects while CAN remained energised.【F:knowledge/notes/input_part008_review.md†L269-L269】
[^45]: Standby draw measurements and LED behaviour on Spintend’s latching power switch.【F:knowledge/notes/input_part001_review.md†L214-L216】
[^46]: Community flashing workflow relying on Spintend-supplied BINs and auto-detection to avoid bricking controllers.【F:knowledge/notes/input_part001_review.md†L632-L633】
[^47]: Auto-detect anomalies recommending ~270 A on dual-phase hubs until limits are manually corrected.【F:knowledge/notes/input_part001_review.md†L824-L825】
[^graphite_triage]: Graphite pad trials on resin-potted copper singles still saw >80 °C case temps at 130 A phase, signalling the need for the aluminum-core revision before committing to more copper hardware.【F:knowledge/notes/input_part003_review.md†L65-L65】
[^2022_prod_update]: Artem’s 16 August 2022 production note covered 500 Spin-Y throttles in hand-solder and copper-backed single onboarding, forecasting staggered shipments and the need for fresh setup guides.【F:knowledge/notes/input_part003_review.md†L60-L63】
[^tc_heat]: 20 September 2022 traction-control experiments overheated Ubox singles faster than manual launches, and Artem confirmed the upcoming single will ship in 80 V and 100 V MOSFET variants until the integrator board lands.【F:knowledge/notes/input_part003_review.md†L70-L72】
[^48]: Ubox V1 vs. V2 motor detection variances demanding manual review of current limits.【F:knowledge/notes/input_part001_review.md†L889-L889】
[^49]: Bench-testing guidance to disable regen and field weakening on PSU-powered Spintend setups to avoid over-voltage damage.【F:knowledge/notes/input_part009_review.md†L84-L84】
[^50]: Fault logging workflow for ABS overcurrent and sensorless diagnostics before power-cycling, plus recommended CSV logging methods.【F:knowledge/notes/input_part001_review.md†L138-L150】
[^52]: Water-cooled 85250 performance data, tariff-driven price creep, and the teased €180 18-FET revision.【F:knowledge/notes/input_part014_review.md†L20-L20】
[^53]: Spintend X12 accessory rail limits and the need for external buck converters to power lighting or telemetry hardware.【F:knowledge/notes/input_part014_review.md†L140-L143】
[^54]: The phase-filter toggle should be used only during motor detection; leaving it active while riding reintroduces noise and ABS overcurrent errors.【F:knowledge/notes/input_part004_review.md†L31-L31】
[^bridge_mirror]: Spintend’s bridge keeps battery current mirrored across controllers—Smart Repair’s GT1 logs showed the front 150 A unit inheriting the rear controller’s battery amps until CAN or power was isolated.[【F:knowledge/notes/input_part011_review.md†L79-L79】【F:knowledge/notes/input_part011_review.md†L317-L317】
[^baseplate_spreader]: JPPL and Shlomozero are reusing dead 75/200 baseplates as auxiliary heatsinks with aluminum spacers and radiator blocks tied into Dualtron side plates to cool HY-equipped stages.【F:knowledge/notes/input_part011_review.md†L521-L521】
