# 3Shul Controllers Brand Dossier

## TL;DR
- C350-class stacks keep surviving 22 S race weekends around 400 A phase / 200 A battery provided regen stays off and installs are logged meticulously, while CL350 revisions still run hotter and deserve conservative envelopes until proven otherwise.[^race22s]
- Capability arrives with boutique support: Raphaël Foujiwara contrasts C350 vs. R350 hardware but reminds buyers that post-sale help is paid, regional techs bill hourly, and DIY installs rarely win warranty leniency.[^support]
- Marketing about 32 S compatibility still outpaces validated telemetry—veterans cap CL-series controllers near 29–30 S with regen disabled because the 135 V FET stack and onboard DC/DC rails offer thin transient margin above that point.[^voltage_cap]
- Traction-control and field-weakening experiments show 3Shul hardware shunting torque rearward at 22 S, but those gains hinge on accurate hall data, tuned observers, and disciplined logging to avoid ABS over-current faults.[^tc_fw]
- Rage Mechanics is already teasing CL500/CL700/CL1000 successors with flatter capacitor banks, thicker busbars, and 30 S ambitions, yet the community still wants burn-in data before treating the roadmap as production-ready.[^roadmap]

## Product Line Cheat Sheet
| Model | Nominal Pack Window | Community Envelope | Differentiators & Caveats |
| --- | --- | --- | --- |
| C350 | 18–22 S | ≈400 A phase / 200 A battery with regen disabled on well-cooled builds | Upgraded capacitance and MOSFETs versus early runs; compact footprint for dual installs.[^c350_specs] |
| R350 | 18–22 S | Commonly tuned around 400 A phase despite a 350 A spec | CNC chassis with smart latch, integrated 12 V 3 A rail, and a 250 A battery rating that outpaces the C350’s nominal ceiling.[^r350_specs] |
| CL350 | 18–22 S | Survives 22 S racing but runs hotter; regen-off strongly advised | Shares firmware with C350 yet reports higher case temps and noisier QC, so racers still prefer the C350 for endurance.[^cl350_heat] |
| CL500 (preview) | 18–30 S (regen disabled above ≈30 S) | Targeting ≥500 A phase once shipping | 12 ToLL FETs on a 25.86 mm IMS base, integrated Bluetooth, thicker 200 A busbars; EU distribution currently routed through Rage Mechanics.[^cl500_preview] |
| CL700 / CL1000 (preview) | 18–32 S (marketing) | Projected 800–1 000 A peaks | Larger ToLL stages pitched at 30 S superbikes, but durability and regen behavior remain unverified.[^cl500_preview] |

## Voltage & Current Guardrails
- Treat 32 S marketing as experimental: CL-series failures after 120 V charging prompted veterans to cap operation near 29–30 S without regen and to add external DC/DC rails when voltage climbs.[^voltage_cap]
- Full-race telemetry keeps 22 S C350 builds alive by disabling regen, holding per-controller battery current near 200 A, and auditing wiring so BMS trips do not hard-cut the power stage.[^race22s]
- Field logs that chase 400 A phase still lean on traction control, balanced CAN settings, and thorough CSV exports to confirm both controllers share the load before raising limits further.[^tc_fw]

## Tuning & Control Behavior
- Traction control can shove torque rearward on 22 S 33×2 LY hubs with ~70 % field weakening, but riders disable TC temporarily when mapping limits and re-enable it once hall data, observers, and wheel parameters match across CAN nodes.[^tc_fw]
- CL350 V4 owners cleared ABS over-current faults by rerunning detection with a 500 µs timing step, swapping to the Ortega observer, and dialing the tune manually per Vedder’s demos—auto-detect defaults proved unreliable at race power.[^abs_fix]
- Sensor checks remain mandatory: recent rescues traced bogus temperature readings to mismatched 10 k NTC probes and dead powerboards, reinforcing that every harness and daughterboard needs inspection before blaming firmware.[^ntc_check]
- Delta-to-star rewiring and aggressive field weakening still trade efficiency for top speed; community race logs show ESC thermals stay the bottleneck even as hub KV and FW increase.[^fw_losses]

## Diagnostics & Support Reality
- Raphaël Foujiwara and other specialists now charge roughly €60 / hr to revive failed boards, and some owners have spent €1 700 on repairs that still failed to boot—stocking spares or fallback controllers remains prudent.[^repair_cost]
- Firmware distribution is opaque: the official CL350 V3 sources live in a shared Drive folder, so teams archive binaries locally and keep dual stacks on matching revisions before flashing.[^firmware_repo]
- Community sentiment still treats 3Shul as the reliable alternative when Makerbase/Tronic stock falters, but buyers accept minimal transparency and shoulder all QC (capacitor staking, harness validation, moisture inspection) themselves.[^community_view]

## Motor Pairing & Field-Weakening Insights
- 3Shul’s C700 motor catalogue documents 70H vs. 75H rim options, ~28.6 KV windings, and 350 A phase capability while warning that counterfeit Panasonic packs marketed alongside the hubs cannot sustain the advertised performance—quality cells and sag monitoring remain non-negotiable.[^c700_hub]
- Race teams pushing 22 S+ builds still log each pull, monitor pack sag, and treat ≥10 P parallels with copper busbars as the minimum for sustained 200 A-per-controller launches.[^race22s]

## Packaging & Integration Notes
- Rage Mechanics is revising C350 packaging with flatter capacitor stacks and dual high-current plugs to squeeze into 100 × 120 × 25 mm cavities where Little FOCer and Tronic boards keep failing—expect install footprints to shrink slightly once those batches land.[^packaging_refresh]
- Dual-controller Ninebot decks only fit with stripped housings and tidy harness routing; builders planning AWD conversions pair custom plates with external heatsinks to keep 22 S hardware cool.[^deck_fit]

## Ecosystem & Roadmap
- Riders are evaluating 3Shul’s forthcoming SmartDisplay-class dash, multifunction switch pods, and RGB integrations as potential successors to Davega once CAN/BMS data streams stabilize.[^accessory_roadmap]
- Telemetry comparisons show VESC real-time power overshoots peaks without filtering, so crews pair 3Shul controllers with SmartDisplay or Voyage Megan dashboards to cross-check pack watts against phase estimates.[^community_view]

## When to Choose Alternatives
- Builders lacking access to trusted 3Shul repair pipelines lean toward Spintend 85/250 or Seven 18 controllers despite lower phase ceilings, prioritizing broader distribution and clearer warranty paths.[^community_view]
- Projects that truly require ≥30 S operation or regen above 22 S still look at Thor 400, FarDriver stages, or forthcoming Tronic X-series hardware until 3Shul publishes validated CL700/CL1000 stress tests.[^alternatives]

## Source Notes
[^race22s]: C350 race telemetry showing ≈400 A phase / 200 A battery survivability at 22 S with regen disabled, plus reports that CL350 hardware runs hotter under the same envelope.【F:knowledge/notes/input_part008_review.md†L305-L305】【F:knowledge/notes/input_part012_review.md†L256-L258】
[^support]: Raphaël Foujiwara’s C350 vs. R350 comparison, CAN connector cautions, and the reminder that unpaid support is unsustainable.【F:knowledge/notes/input_part011_review.md†L26-L28】
[^voltage_cap]: CL-series voltage ceiling warnings and DC/DC sag observations that cap practical operation near 29–30 S without regen.【F:knowledge/notes/input_part006_review.md†L71-L72】
[^tc_fw]: Traction-control and field-weakening behavior on 22 S LY hubs, plus logging discipline required to avoid inflated speed readings or control faults.【F:knowledge/notes/input_part009_review.md†L109-L124】【F:knowledge/notes/input_part009_review.md†L121-L121】
[^roadmap]: CL500/CL700/CL1000 roadmap previews, packaging dimensions, and distribution updates from Rage Mechanics.【F:knowledge/notes/input_part004_review.md†L15522-L15541】【F:knowledge/notes/input_part004_review.md†L16149-L16186】
[^c350_specs]: Field data confirming the C350’s 400 A phase / 200 A battery envelope on disciplined builds.【F:knowledge/notes/input_part012_review.md†L256-L258】
[^r350_specs]: R350 feature comparison including the 12 V 3 A rail, smart latch, and 250 A battery rating.【F:knowledge/notes/input_part011_review.md†L26-L28】
[^cl350_heat]: Reports of CL350 heat and QC variance relative to C350 units on 22 S race scooters.【F:knowledge/notes/input_part008_review.md†L305-L305】
[^cl500_preview]: Packaging refresh teasers and roadmap notes covering the CL500/CL700/CL1000 series.【F:knowledge/notes/input_part004_review.md†L15522-L15541】【F:knowledge/notes/input_part004_review.md†L16149-L16186】
[^abs_fix]: Detection workflow (500 µs timing, Ortega observer) that cleared CL350 V4 ABS over-current faults.【F:knowledge/notes/input_part009_review.md†L123-L124】
[^ntc_check]: Case studies tracing temperature faults to failed powerboards or mismatched 10 k NTC probes on 3Shul installs.【F:knowledge/notes/input_part008_review.md†L42-L43】
[^fw_losses]: Community notes on 3Shul hub KV, field-weakening losses, and counterfeit Panasonic pack recalls tied to C700 marketing.【F:knowledge/notes/input_part003_review.md†L21001-L21048】
[^repair_cost]: Regional repair anecdotes including €60 / hr service rates and costly yet unsuccessful rebuild attempts.【F:knowledge/notes/input_part012_review.md†L256-L269】【F:knowledge/notes/input_part012_review.md†L388-L389】
[^firmware_repo]: Guidance pointing owners to the official Drive share containing CL350 V3 firmware sources.【F:knowledge/notes/input_part008_review.md†L417-L417】
[^community_view]: Community sentiment that 3Shul remains a high-voltage alternative when other controllers are scarce, alongside praise for capacitor durability and reminders to self-manage QC.【F:knowledge/notes/input_part014_review.md†L15-L20】【F:knowledge/notes/input_part014_review.md†L71-L72】
[^c700_hub]: 3Shul C700 hub specifications (rim options, KV, phase limits) plus cautions about counterfeit Panasonic packs.【F:knowledge/notes/input_part003_review.md†L21001-L21048】
[^packaging_refresh]: Packaging refresh teasers describing flatter capacitor layouts and dual connectors for upcoming C350 batches.【F:knowledge/notes/input_part004_review.md†L20064-L20108】
[^deck_fit]: Dual-controller Ninebot deck packaging examples highlighting the need for stripped casings and precise harness routing.【F:knowledge/notes/input_part004_review.md†L2267-L2273】
[^accessory_roadmap]: Emerging accessory ecosystem (displays, switch pods, RGB integration) tied to upcoming 3Shul releases.【F:knowledge/notes/input_part014_review.md†L78-L83】
[^alternatives]: Discussions weighing 3Shul pricing against Spintend/Seven availability and recommending Thor/FarDriver or other platforms for ≥30 S regen builds until CL700/CL1000 data arrives.【F:knowledge/notes/input_part014_review.md†L15-L20】【F:knowledge/notes/input_part014_review.md†L194-L195】
