# 3Shul Controllers

## Overview

3Shul produces high-end VESC-compatible controllers (C350, R350, CL-series) favored by racers for their reliability and power handling, but they require proper cooling and come with boutique pricing and support. This brand dossier covers the 3Shul controller lineup, real-world current limits, voltage capabilities, thermal management requirements, and support expectations. Understanding 3Shul's strengths and limitations helps you decide when they're worth the premium over alternatives.

## What You'll Learn

- 3Shul model comparison (C350, R350, CL350, CL500+)
- Real-world current and voltage limits
- Thermal management requirements for race applications
- Traction control and field weakening behavior
- Support model and warranty considerations
- When 3Shul justifies premium pricing vs. Spintend/Makerbase
- Upcoming CL500/700/1000 roadmap

## 🏆 Why Choose 3Shul?

✅ **Race-proven**: Survives 22S race weekends
✅ **High current**: Real 400A phase capability
✅ **Thermal performance**: Excellent when properly cooled
⚠️ **Boutique pricing**: Premium cost
⚠️ **Paid support**: No free warranty service

## 📋 Quick Model Comparison

| Model | Pack Range | Battery Current | Phase Current | Best For |
|-------|-----------|-----------------|---------------|----------|
| C350 | 18-22S | 200A | 400A | Race builds with budget |
| R350 | 18-22S | 250A | 400A | Premium race with smart latch |
| CL350 | 18-22S | 200A | 400A | Runs hotter, needs cooling |
| CL500 | 18-30S | TBD | 500A+ | Future racing (preview) |

💡 **Pro Tip**: C350 is easier to source in Europe than R350. Both perform similarly with proper cooling.

## 🔧 Related Brand Dossiers

- [Spintend Controllers](spintend.md) - Mainstream alternative
- [Tronic Controllers](tronic.md) - High-voltage option
- [Makerbase Controllers](makerbase.md) - Budget alternative

## Key Principles

- G300 controllers remain easier to source than boutique R-series stock in Europe, but they still demand aggressive cooling; JPPL calls the unit a “rock” provided the case can dump heat, while race teams lean on the rarer R350 when they can secure it.[^g300_stock]
- C350-class stacks keep surviving 22 S race weekends around 400 A phase / 200 A battery provided regen stays off and installs are logged meticulously, while CL350 revisions still run hotter and deserve conservative envelopes until proven otherwise.[^race22s]
- Capability arrives with boutique support: Raphaël Foujiwara contrasts C350 vs. R350 hardware but reminds buyers that post-sale help is paid, regional techs bill hourly, and DIY installs rarely win warranty leniency.[^support]
- Marketing about 32 S compatibility still outpaces validated telemetry—veterans cap CL-series controllers near 29–30 S with regen disabled because the 135 V FET stack and onboard DC/DC rails offer thin transient margin above that point.[^voltage_cap]
- Traction-control and field-weakening experiments show 3Shul hardware shunting torque rearward at 22 S, but those gains hinge on accurate hall data, tuned observers, and disciplined logging to avoid ABS over-current faults.[^tc_fw]
- Rage Mechanics is already teasing CL500/CL700/CL1000 successors with flatter capacitor banks, thicker busbars, and 30 S ambitions, yet the community still wants burn-in data before treating the roadmap as production-ready.[^roadmap]
- Current C350 batches ship with thicker IMS plates, a 200 A battery rating, and bundled ESP32 BLE/IMU telemetry plus a 12 V 3 A rail—wiring looms remain DIY, but the hardware is edging toward SmartDisplay-ready kits.[^c350-refresh-2023]

## Product Line Cheat Sheet

| Model | Nominal Pack Window | Community Envelope | Differentiators & Caveats |
| --- | --- | --- | --- |
| C350 | 18–22 S | ≈400 A phase / 200 A battery with regen disabled on well-cooled builds | Upgraded capacitance and MOSFETs versus early runs; compact footprint for dual installs.[^c350_specs] |
| R350 | 18–22 S | Commonly tuned around 400 A phase despite a 350 A spec | CNC chassis with smart latch, integrated 12 V 3 A rail, and a 250 A battery rating that outpaces the C350’s nominal ceiling.[^r350_specs] |
| CL350 | 18–22 S | Survives 22 S racing but runs hotter; regen-off strongly advised | Shares firmware with C350 yet reports higher case temps and noisier QC, so racers still prefer the C350 for endurance.[^cl350_heat] |
| CL500 (preview) | 18–30 S (regen disabled above ≈30 S) | Targeting ≥500 A phase once shipping | 12 ToLL FETs on a 25.86 mm IMS base, integrated Bluetooth, thicker 200 A busbars; EU distribution currently routed through Rage Mechanics.[^cl500_preview] |
| CL700 / CL1000 (preview) | 18–32 S (marketing) | Projected 800–1 000 A peaks | Larger ToLL stages pitched at 30 S superbikes, but durability and regen behavior remain unverified.[^cl500_preview] |

## Voltage & Current Guardrails

- Treat 32 S marketing as experimental: CL-series failures after 120 V charging prompted veterans to cap operation near 29–30 S without regen, pointing out that the 135 V FETs leave little spike headroom and the onboard 12 V supply sags below 1 A unless you add external rails.[^1][^voltage_cap]
- Full-race telemetry keeps 22 S C350 builds alive by disabling regen, holding per-controller battery current near 200 A, and auditing wiring so BMS trips do not hard-cut the power stage.[^race22s]
- Field logs that chase 400 A phase still lean on traction control, balanced CAN settings, and thorough CSV exports to confirm both controllers share the load before raising limits further.[^tc_fw]
- CL350-class controllers ride out split-second pack dropouts better than Makerbase peers when riders add auxiliary 12 V capacitance, but the margin is thin—treat BMS trips as faults to fix, not normal operating behavior.[^supply_margin]

## Tuning & Control Behavior

- Traction control can shove torque rearward on 22 S 33×2 LY hubs with ~70 % field weakening, but riders disable TC temporarily when mapping limits and re-enable it once hall data, observers, and wheel parameters match across CAN nodes.[^tc_fw]
- CL350 V4 owners cleared ABS over-current faults by rerunning detection with a 500 µs timing step, swapping to the Ortega observer, and dialing the tune manually per Vedder’s demos—auto-detect defaults proved unreliable at race power.[^abs_fix]
- Sensor checks remain mandatory: recent rescues traced bogus temperature readings to mismatched 10 k NTC probes and dead powerboards, reinforcing that every harness and daughterboard needs inspection before blaming firmware.[^ntc_check]
- Delta-to-star rewiring and aggressive field weakening still trade efficiency for top speed; community race logs show ESC thermals stay the bottleneck even as hub KV and FW increase.[^fw_losses]
- Auto-detect shortcuts still burn hardware: veterans insist CL-series controllers need hand-tuned drive and regen currents because automated regen mirrors whatever drive amps you request, spiking hardware unless you rein it in—newcomers who want plug-and-play behaviour should consider simpler controllers.[^manual_setup]
- Losing throttle ground still commands full power—builders now strain-relief the ground pin, enable Safe Start voltage checks, and rerun both input and motor detection after traction-control or ramp tweaks to confirm the new limits actually saved.[^throttle_ground]

## Diagnostics & Support Reality

- Raphaël Foujiwara and other specialists now charge roughly €60 / hr to revive failed boards, and some owners have spent €1 700 on repairs that still failed to boot—stocking spares or fallback controllers remains prudent.[^repair_cost]
- The same crew credits Figiwara with reviving three failed controllers for the race team, cementing his bench as the go-to EU repair channel when premium boards die mid-season.[^2]
- Publish a contact roster (Figiwara, regional techs, shipping expectations) alongside RMA notes so riders outside core service regions know who to call before hardware fails mid-season.[^3]
- Nobrrr and Paolo traced blown hardware to reveal 3Shul’s “custom” MOSFETs are standard ON Semi HSBL009N10T devices (marked N009N10T), so repair benches can source replacements through normal supply chains instead of hunting bespoke silicon.[^mosfet_crossref]
- Firmware distribution is opaque: the official CL350 V3 sources live in a shared Drive folder, so teams archive binaries locally and keep dual stacks on matching revisions before flashing.[^firmware_repo]
- Community sentiment still treats 3Shul as the reliable alternative when Makerbase/Tronic stock falters, but buyers accept minimal transparency and shoulder all QC (capacitor staking, harness validation, moisture inspection) themselves.[^community_view]
- Dual installs require tidy ignition wiring—feed the key-switch lead to each controller (or bridge the 5 V enable rails), isolate any failed Bluetooth daughterboards that can dead-short the logic rail, and remember that the latch circuit stays energized whenever the pack is plugged in.[^ignition_wiring]

## Motor Pairing & Field-Weakening Insights

- Arnau’s Valencia build plan pairs twin G300s with Ambrosini 75H motors, a 22 S 10 P P45B pack, and a 10 mm RTR aluminum spreader purely to tame controller temps while the pack is finished—treat heat sinking as mandatory when leaning on readily available G-series hardware for race duty.[^arnau_valencia]
- 3Shul’s C700 motor catalogue documents 70H vs. 75H rim options, ~28.6 KV windings, and 350 A phase capability while warning that counterfeit Panasonic packs marketed alongside the hubs cannot sustain the advertised performance—quality cells and sag monitoring remain non-negotiable.[^c700_hub]
- Race teams pushing 22 S+ builds still log each pull, monitor pack sag, and treat ≥10 P parallels with copper busbars as the minimum for sustained 200 A-per-controller launches.[^race22s]
- Volkan’s Langfeite GT2RS telemetry shows twin LY hubs on 24 S 20 P EVE 40PL packs pulling 330 A phase / 170 A battery with ~3 V sag while 100 A of field weakening holds 20 kHz switching; correcting a mis-set 30-pole magnet count to the real 40 poles dropped the claimed 150–160 km/h to ~120 km/h GPS—validate sensors before celebrating speed gains.[^volkan_gt2rs]

## Packaging & Integration Notes

- Fresh G300 teardowns revealed an 18-FET stack literally bedded in thick thermal compound that floods into the CNC housing; messy or not, the paste turns the enclosure into a dual-sided heatsink so builders now resist scraping it out during QC checks.[^g300_paste]
- Rage Mechanics is revising C350 packaging with flatter capacitor stacks and dual high-current plugs to squeeze into 100 × 120 × 25 mm cavities where Little FOCer and Tronic boards keep failing—expect install footprints to shrink slightly once those batches land.[^packaging_refresh]
- EU buyers now route orders through Face de Pin Sucé to secure 2023 batches that ship with 8 AWG motor leads and tidier harness QC instead of gambling on ad-hoc Telegram resellers.[^eu_sourcing]
- Dual-controller Ninebot decks only fit with stripped housings and tidy harness routing; builders planning AWD conversions pair custom plates with external heatsinks to keep 22 S hardware cool.[^deck_fit]
- Fresh-batch QA checks now include validating every MOSFET NTC lead before first power-up after a new run shipped with a missing sensor that forced −70 °C readings on a slave controller.[^yoann_ntc]

## Ecosystem & Roadmap

- Riders are evaluating 3Shul’s forthcoming SmartDisplay-class dash, multifunction switch pods, and RGB integrations as potential successors to Davega once CAN/BMS data streams stabilize.[^accessory_roadmap]
- Russia’s billet RTV Ultra superbike underscores the brand’s ceiling: dual 3Shul stacks feed 115 mm stators from 26 S 64 Ah packs for ≈40 kW peaks, but turnkey buyers still quote six-month lead times.[^rtv_ultra]
- Telemetry comparisons show VESC real-time power overshoots peaks without filtering, so crews pair 3Shul controllers with SmartDisplay or Voyage Megan dashboards to cross-check pack watts against phase estimates.[^community_view]
- Rage Mechanics’ RM-Light and Thunder-based RM-X race programs continue to showcase tuned 3Shul stacks—expect ≈37 kg curb weights with 22 S 4 P tabless packs for 130–140 km/h sprint events, and plan for aggressive airflow once Thunder builds chase 170 km/h records that already heat hubs past 112 °C within minutes.[^rmx_program]
- Early CL1400 previews trumpet 30 S / 1 000 A aspirations, but community reviewers already spotted blown MOSFETs in demo footage, so the roadmap still needs independent endurance logs before builders commit.[^cl1400_caution]

## When to Choose Alternatives

- Builders lacking access to trusted 3Shul repair pipelines lean toward Spintend 85/250 or Seven 18 controllers despite lower phase ceilings, prioritizing broader distribution and clearer warranty paths.[^community_view]
- Projects that truly require ≥30 S operation or regen above 22 S still look at Thor 400, FarDriver stages, or forthcoming Tronic X-series hardware until 3Shul publishes validated CL700/CL1000 stress tests.[^alternatives]

## Source Notes

[^race22s]: C350 race telemetry showing ≈400 A phase / 200 A battery survivability at 22 S with regen disabled, plus reports that CL350 hardware runs hotter under the same envelope. Source: knowledge/notes/input_part008_review.md, L305 to L305. Source: knowledge/notes/input_part012_review.md, L256 to L258
[^support]: Raphaël Foujiwara’s C350 vs. R350 comparison, CAN connector cautions, and the reminder that unpaid support is unsustainable. Source: knowledge/notes/input_part011_review.md, L26 to L28
[^voltage_cap]: CL-series voltage ceiling warnings and DC/DC sag observations that cap practical operation near 29–30 S without regen. Source: knowledge/notes/input_part006_review.md, L71 to L72
[^tc_fw]: Traction-control and field-weakening behavior on 22 S LY hubs, plus logging discipline required to avoid inflated speed readings or control faults. Source: knowledge/notes/input_part009_review.md, L109 to L124. Source: knowledge/notes/input_part009_review.md, L121 to L121
[^roadmap]: CL500/CL700/CL1000 roadmap previews, packaging dimensions, and distribution updates from Rage Mechanics. Source: knowledge/notes/input_part004_review.md, L288 to L288. Source: knowledge/notes/input_part004_review.md, L436 to L436
[^c350-refresh-2023]: Source: data/vesc_help_group/text_slices/input_part004.txt†L24404-L24428
[^c350_specs]: Field data confirming the C350’s 400 A phase / 200 A battery envelope on disciplined builds. Source: knowledge/notes/input_part012_review.md, L256 to L258
[^r350_specs]: R350 feature comparison including the 12 V 3 A rail, smart latch, and 250 A battery rating. Source: knowledge/notes/input_part011_review.md, L26 to L28
[^cl350_heat]: Reports of CL350 heat and QC variance relative to C350 units on 22 S race scooters. Source: knowledge/notes/input_part008_review.md, L305 to L305
[^cl500_preview]: Packaging refresh teasers and roadmap notes covering the CL500/CL700/CL1000 series. Source: knowledge/notes/input_part004_review.md, L288 to L288. Source: knowledge/notes/input_part004_review.md, L304 to L304
[^abs_fix]: Detection workflow (500 µs timing, Ortega observer) that cleared CL350 V4 ABS over-current faults. Source: knowledge/notes/input_part009_review.md, L123 to L124
[^ntc_check]: Case studies tracing temperature faults to failed powerboards or mismatched 10 k NTC probes on 3Shul installs. Source: knowledge/notes/input_part008_review.md, L42 to L43
[^fw_losses]: Community notes on 3Shul hub KV, field-weakening losses, and counterfeit Panasonic pack recalls tied to C700 marketing. Source: knowledge/notes/input_part003_review.md, L160 to L160. Source: knowledge/notes/input_part003_review.md, L207 to L215
[^manual_setup]: Kirill and Happy Giraffe reminded riders that CL-series reliability hinges on manually tuning motor and brake currents—auto-detected regen mirrors drive amps and will spike hardware unless you rein it in. Source: knowledge/notes/input_part007_review.md, L335 to L335
[^repair_cost]: Regional repair anecdotes including €60 / hr service rates and costly yet unsuccessful rebuild attempts. Source: knowledge/notes/input_part012_review.md, L256 to L269. Source: knowledge/notes/input_part012_review.md, L388 to L389
[^firmware_repo]: Guidance pointing owners to the official Drive share containing CL350 V3 firmware sources. Source: knowledge/notes/input_part008_review.md, L417 to L417
[^community_view]: Community sentiment that 3Shul remains a high-voltage alternative when other controllers are scarce, alongside praise for capacitor durability and reminders to self-manage QC. Source: knowledge/notes/input_part014_review.md, L15 to L20. Source: knowledge/notes/input_part014_review.md, L71 to L72
[^c700_hub]: 3Shul C700 hub specifications (rim options, KV, phase limits) plus cautions about counterfeit Panasonic packs. Source: knowledge/notes/input_part003_review.md, L160 to L160. Source: knowledge/notes/input_part003_review.md, L215 to L215
[^packaging_refresh]: Packaging refresh teasers describing flatter capacitor layouts and dual connectors for upcoming C350 batches. Source: knowledge/notes/input_part004_review.md, L304 to L304
[^eu_sourcing]: European buyers now channel orders through Face de Pin Sucé to guarantee 2023 3Shul batches with 8 AWG leads and improved harness QC rather than relying on informal resellers. Source: knowledge/notes/input_part004_review.md, L234 to L234
[^deck_fit]: Dual-controller Ninebot deck packaging examples highlighting the need for stripped casings and precise harness routing. Source: knowledge/notes/input_part004_review.md, L28 to L28
[^accessory_roadmap]: Emerging accessory ecosystem (displays, switch pods, RGB integration) tied to upcoming 3Shul releases. Source: knowledge/notes/input_part014_review.md, L78 to L83
[^rtv_ultra]: Russia’s RTV Ultra billet scooter specification with dual 3Shul controllers, 26 S 64 Ah packs, 115 mm stators, and long lead times as a reference build. Source: knowledge/notes/input_part012_review.md, L184 to L184
[^alternatives]: Discussions weighing 3Shul pricing against Spintend/Seven availability and recommending Thor/FarDriver or other platforms for ≥30 S regen builds until CL700/CL1000 data arrives. Source: knowledge/notes/input_part014_review.md, L15 to L20. Source: knowledge/notes/input_part014_review.md, L194 to L195
[^yoann_ntc]: Yoann documented a fresh 3Shul batch that shipped with a missing MOSFET temperature lead, forcing −70 °C readings and reminding installers to validate sensor harnesses before first ride. Source: knowledge/notes/input_part007_review.md, L44 to L44
[^cl1400_caution]: Community reviewers flagged early CL1400 demo footage that already showed blown MOSFETs despite 30 S / 1 000 A marketing claims, so stress testing is still pending before adoption. Source: knowledge/notes/input_part003_review.md, L686 to L686
[^supply_margin]: CL350-class controllers absorbing brief supply interruptions when buffered with extra 12 V capacitance, unlike Makerbase peers that die on BMS trips. Source: knowledge/notes/input_part008_review.md, L31 to L34
[^throttle_ground]: CL350 harness failures that shove 5 V down the throttle signal if ground breaks, plus reminders to rerun detection after traction-control changes because calibration can drop silently. Source: knowledge/notes/input_part005_review.md, L33 to L39. Source: knowledge/notes/input_part005_review.md, L43 to L48
[^rmx_program]: RM-Light race scooter specs (≈37 kg, 22 S 4 P tabless pack, RM-X 2024 motors, Beringer brakes) alongside Thunder-based RM-X record attempts that already log ~112 °C motor temps within minutes at 170 km/h targets. Source: knowledge/notes/input_part012_review.md, L383 to L383. Source: knowledge/notes/input_part013_review.md, L204 to L204. Source: knowledge/notes/input_part013_review.md, L452 to L452. Source: knowledge/notes/input_part009_review.md, L288 to L288
[^mosfet_crossref]: Community teardown confirming 3Shul’s MOSFETs match ON Semi HSBL009N10T components, easing replacement sourcing after failures. Source: knowledge/notes/input_part013_review.md, L791 to L791
[^volkan_gt2rs]: Langfeite GT2RS data showing 330 A phase / 170 A battery pulls with ~3 V sag on 24 S 20 P EVE 40PL packs and corrected 120 km/h GPS speeds once the magnet count was set to the proper 40 poles. Source: knowledge/notes/input_part009_review.md, L291 to L291
[^ignition_wiring]: Key-switch wiring guidance confirming both CL controllers need the ignition lead, that failed Bluetooth boards can dead-short the rail, and that the latch circuit remains live with the pack connected. Source: knowledge/notes/input_part004_review.md, L56 to L60. Source: knowledge/notes/input_part004_review.md, L203 to L207. Source: knowledge/notes/input_part004_review.md, L292 to L296
[^g300_stock]: JPPL and Yamal contrasted easily sourced G300 controllers with harder-to-find R350 race hardware, noting the G-series still needs serious cooling despite its availability. Source: knowledge/notes/input_part011_review.md†L601-L602
[^g300_paste]: JPPL’s G300 teardown found the 18-FET stack immersed in thermal compound that conducts into the CNC housing, effectively turning the case into a dual-sided heatsink. Source: knowledge/notes/input_part011_review.md†L698-L699
[^arnau_valencia]: Arnau’s Valencia race prep pairs twin G300s with Ambrosini 75H motors, a 22 S 10 P P45B pack, and a 10 mm RTR aluminum spreader to manage controller heat while the battery build finishes. Source: knowledge/notes/input_part011_review.md†L631-L632

## References

[^1]: Source: knowledge/notes/input_part006_review.md, L156 to L156
[^2]: Source: knowledge/notes/input_part012_review.md, L363 to L364
[^3]: Source: knowledge/notes/input_part012_review.md, L314 to L314
