# Parallel Battery & Regen Integration Manual

## TL;DR
- Match pack voltages before paralleling and avoid ideal diodes; real-world tests on 17S/16S stacks caused throttle cut-outs and offered no regen benefits compared with direct, voltage-matched links.【F:knowledge/notes/input_part013_review.md†L153-L156】
- Treat regen as a controller- and battery-limited budget: split braking current across packs, keep the combined limit within both packs’ safe charge rates, and raise BMS regen ceilings (e.g., 100 A on JBD units) so the controller does not dump energy into MOSFETs instead.【F:knowledge/notes/input_part013_review.md†L154-L157】【F:knowledge/notes/input_part013_review.md†L693-L703】
- Regen only works when the charge path is enabled; disabling the BMS charge MOSFET or relying on regen without hydraulic brakes has already produced weak braking and safety gaps on live builds.【F:knowledge/notes/input_part013_review.md†L157-L163】

## Pack Pairing Pre-Flight Checklist
1. **Equalise voltage first.** Bring both packs to the same resting voltage before making the parallel connection. Builders observed natural balancing currents under ~1 A once voltages matched, versus abrupt faults when voltages differed by a full cell group.【F:knowledge/notes/input_part013_review.md†L154-L156】
2. **Plan capacity-aware cutoffs.** Mixed packs (e.g., small internal C-rate plus large 2 C external) still share state-of-charge; log per-pack voltage drop during endurance runs (≈13 V over 38 mi in testing) to size cutoffs and avoid deep cycling the smaller module.【F:knowledge/notes/input_part013_review.md†L154-L155】
3. **Verify BMS readiness.** Confirm that every pack’s charge path is active and any smart-BMS current limits exceed expected regen peaks (≥100 A on 20 S JBD examples) before heading out.【F:knowledge/notes/input_part013_review.md†L157-L157】【F:knowledge/notes/input_part013_review.md†L703-L703】
- **Load-test suspect externals.** Denis’ workshop found bargain 10 S packs sagging immediately, leaving the internal module to carry the ride—bench them alone at low amperage before trusting their specs in a parallel stack.[^cheap-externals]

## Wiring & Current-Sharing Strategy
- **Skip ideal diodes for everyday riding.** Diode-protected tests on 17 S/16 S packs triggered throttle cut-outs without meaningfully reducing balancing current. Instead, match voltages, plug in directly, and rely on pack capacity differences to dictate current share (larger packs naturally absorb more regen).【F:knowledge/notes/input_part013_review.md†L154-L156】
- **Use high-quality connectors and inspections.** High-current scooters running parallel harnesses have destroyed QS8 links and controllers when connections loosened; add pre-ride continuity checks whenever you modify pack wiring.【F:knowledge/notes/input_part013_review.md†L411-L411】
- **Fuse each leg.** Install inline fuses or breakers per pack so a single short does not cascade through the entire parallel assembly—a lesson reinforced by riders dailying 20 S packs without discharge-side BMS protection.【F:knowledge/notes/input_part013_review.md†L224-L224】

## Regen Budgeting & Controller Configuration
- **Allocate regen per pack.** Limit VESC negative battery current so the sum of all packs’ settings stays below their combined safe charge rate; riders planning 30 A, 3 s emergency stops are using these calculations to remain within chemical limits.【F:knowledge/notes/input_part013_review.md†L154-L156】【F:knowledge/notes/input_part013_review.md†L173-L173】
- **Respect controller ceilings.** Regen remains phase-current limited—pushing beyond the controller’s thermal capacity will overheat MOSFETs before healthy packs object. Keep controller telemetry on hand to verify that regen spikes stay inside hardware budgets.【F:knowledge/notes/input_part013_review.md†L156-L156】
- **Tune VESC voltage caps.** One 75 200 failure traced to regen voltage spikes because the controller’s max input voltage exceeded the pack’s comfort zone while the JBD limit stayed at stock; raising the BMS regen ceiling and tightening VESC’s voltage limit prevented further MOSFET deaths.【F:knowledge/notes/input_part013_review.md†L693-L703】

## BMS & Charge-Path Safeguards
- **Leave charge MOSFETs enabled.** Disabling the BMS charge FET neutered regen braking until riders re-enabled it, proving that “charge off” modes directly cut regen authority.【F:knowledge/notes/input_part013_review.md†L157-L157】
- **Audit charge-only BMS setups.** Some 20 S commuters are still riding with only a 40 A charge-side ANT board; peers called out the fire risk and urged restoring full discharge protection before another controller failure.【F:knowledge/notes/input_part013_review.md†L224-L224】
- **Log smart-BMS telemetry.** JBD/Xiaoxiang apps expose regen current, pack voltage, and MOSFET temperatures—capture these during first shakedowns to validate that firmware changes (e.g., no-limit builds) stay inside BMS envelopes.【F:knowledge/notes/input_part013_review.md†L693-L703】
- **Bridge data into the VESC bus.** Plug-in CAN adapters let LLT/JBD boards stream pack voltage, current, and alarms directly to controllers and dashboards, making it easier to catch regen spikes before they cook MOSFETs.[^can-bridge]

## Thermal & Mechanical Guardrails
- **Monitor pack heating under parallel pulls.** Dual MakerBase 100 A stacks pushing ~400 A battery combined already flirt with pack heat soak; adding parallel packs raises sustained power capability but only if you manage airflow and thermal mass.【F:knowledge/notes/input_part013_review.md†L539-L540】
- **Keep hydraulic brakes in service.** Several Ninebot and Ubox conversions rode with only −90 A motor brake while waiting on parts; others survived emergency stops thanks to cable/hydraulic brakes when regen-only systems failed. Treat regen as supplemental, not primary, stopping power.【F:knowledge/notes/input_part013_review.md†L163-L163】【F:knowledge/notes/input_part013_review.md†L395-L395】
- **Document heat thresholds.** Builders noted controller temps climbing before motors when leaning on regen for long descents; watch MOSFET sensors and dial back regen if controller temps spike even when motors feel cool.【F:knowledge/notes/input_part013_review.md†L395-L395】
- **Check packs after wet rides.** A 30 S parallel group drifted out of balance after moisture seeped into the enclosure—dry and inspect housings before re-paralleling so regen doesn’t push mismatched groups further apart.【F:knowledge/notes/input_part012_review.md†L10491-L10505】

## Implementation Checklist
1. Balance pack voltages and confirm BMS charge paths are active before making the parallel connection.【F:knowledge/notes/input_part013_review.md†L154-L157】
2. Set per-pack regen limits inside VESC Tool so the total equals the combined safe charge current, and raise any smart-BMS charge limits accordingly.【F:knowledge/notes/input_part013_review.md†L154-L157】【F:knowledge/notes/input_part013_review.md†L693-L703】
3. Log the first shakedown ride—capture pack voltage delta, peak regen current, and controller temperatures—to validate assumptions before sealing the deck.【F:knowledge/notes/input_part013_review.md†L155-L156】【F:knowledge/notes/input_part013_review.md†L395-L395】
4. Schedule periodic mechanical brake inspections; regen-only builds have already highlighted the danger of delaying hydraulic installs or maintenance.【F:knowledge/notes/input_part013_review.md†L163-L163】【F:knowledge/notes/input_part013_review.md†L395-L395】

## Source Notes
- Parallel-pack behaviour, diode testing, and regen budgeting come from the Ninebot/Nami integration threads detailing voltage matching, current share, and regen calculations for 17–22 S builds.【F:knowledge/notes/input_part013_review.md†L153-L173】【F:knowledge/notes/input_part013_review.md†L693-L703】
- Safety guardrails on charge-path enablement, fuse planning, moisture checks, and mechanical brake reliance reflect the same discussions of charge-only BMS risks, wet-pack drift, and high-current harness failures.【F:knowledge/notes/input_part013_review.md†L224-L224】【F:knowledge/notes/input_part013_review.md†L395-L411】【F:knowledge/notes/input_part013_review.md†L539-L540】【F:knowledge/notes/input_part012_review.md†L10491-L10505】
[^can-bridge]: LLT/JBD smart BMS boards now offer plug-in CAN adapters that share telemetry over the existing harness, simplifying regen verification inside VESC Tool or CAN dashboards.【F:knowledge/notes/input_part006_review.md†L365-L365】
[^cheap-externals]: Cheap external packs that collapse under minimal load force the main battery to supply all current—test them independently before paralleling or sizing regen budgets.【F:knowledge/notes/denis_all_part02_review.md†L5499-L5526】
