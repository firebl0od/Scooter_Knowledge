# Seven Controllers Brand Dossier

## TL;DR

- Seven 18-class controllers mirror Tronic X12 offerings with 24 S and 30 S options, 18- or 30-FET power stages, onboard logging memory, and a 12 V / 4 A auxiliary rail—positioning them as a premium alternative once inventory stabilises.[^lineup]
- Early tuning data keeps 16 S baselines near 180 A battery, 300 A phase, and ~50 A of field weakening at 87 % duty; more FW headroom is possible, but only after validating thermal and traction margins.[^fw_baseline]
- Firmware releases lag hardware: launch units ship with VESC Tool 6.06 binaries but no published source, and the bundled VESC Express board still fails to enumerate without a separate CAN-connected module.[^firmware][^express]
- Alibaba resellers now liquidate Seven/Tronic stock straight from the contract manufacturer, so pricing resembles the defunct brand while official support remains uncertain—treat purchases as boutique hardware that needs self-managed documentation.[^supply]

## Product Snapshot

| Variant | Nominal Pack Window | Stock Aux Outputs | Differentiators & Watchpoints |
| --- | --- | --- | --- |
| Seven 18 (18 FET) | 24 S marketing target | 12 V / 4 A rail, bundled Express daughterboard | Shares Toll-class MOSFETs with Tronic X12; stacked on 1.6 mm FR-4 so the thermal edge over X12 heat-sink mounting is only ≈15–20 %. Verify clamping and paste before chasing 500 A claims.[^lineup][^thermal]
| Seven 30 (30 FET) | 30 S ambitions | 12 V / 4 A rail, logging memory | Inventory still rumoured; expect identical firmware caveats and insist on source drops plus Express fixes before committing race builds.[^lineup][^firmware]

## Operating Envelope & Tuning Baselines

- Hold initial tunes near the documented 16 S recipe (≈180 A battery, 300 A phase, ~50 A FW at 87 % duty) until independent logs confirm higher limits; heavier FW experiments should ramp slowly with traction-control audits.[^fw_baseline]
- Pair Toll-FET stages with robust cooling—Paolo’s teardown shows the FR-4 sandwich limiting thermal spread, so racers seeking a major headroom jump may still prefer direct-to-heatsink platforms like the K900 until Seven publishes validated datalogs.[^thermal]

## Firmware, Telemetry & Compliance

- Demand the GPL-mandated `.c/.h` releases alongside binaries; current shipments arrive with 6.06 firmware but no source, putting builders in a legal and support grey area until Seven responds.[^firmware]
- Budget an external Express or CAN logger—the bundled board has yet to enumerate reliably, forcing JPPL to hang a separate Express module for telemetry.[^express]
- Track VESC Tool compatibility: Bluetooth pairing hiccups on 6.06 already nudged crews back to 6.05 until patches landed, so document software builds whenever flashing new Seven hardware.[^firmware]

## Supply Chain & Support Reality

- Treat Alibaba listings as direct-from-factory clearances. Pricing matches historical Seven/Tronic numbers but arrives without brand backing, so stock spares, log calibrations, and plan local repair options before deployment.[^supply]
- Early adopters are still waiting on partial shipments—one six-pack order only delivered two controllers after four months—so factor unpredictable lead times and missing units into project schedules.[^1]
- Catalog serial numbers, MOSFET batches, and thermal-interface steps for every install—the community “VESC museum” is already queuing comparison runs against Maxim, Tronic, and MakerX controllers, and shared telemetry will accelerate validation once source drops catch up.[^lineup][^tracking]

## Action Items

1. **Archive firmware and demand source** before installing—refuse to run closed drops on production fleets.[^firmware]
2. **Verify Express telemetry** with a separate CAN-connected board until bundled hardware enumerates cleanly.[^express]
3. **Log thermal profiles** on first rides to confirm the FR-4 sandwich delivers the promised headroom over X12 mounts.[^thermal]
4. **Document pricing and support contacts** whenever sourcing via Alibaba so future buyers understand warranty realities.[^supply]

## Source Notes

[^lineup]: Seven 18 product outline covering 24 S/30 S variants with 18 or 30 FETs, onboard logging, and a 12 V / 4 A rail, plus plans to benchmark them alongside Maxim launches. Source: knowledge/notes/input_part014_review.md, L52 to L54. Source: knowledge/notes/input_part014_review.md, L27 to L27
[^fw_baseline]: Reported Seven/Spintend tuning baseline of ≈180 A battery, 300 A phase, and ~50 A FW at 87 % duty for 16 S builds. Source: knowledge/notes/input_part014_review.md, L54 to L54
[^firmware]: Seven 18 prototypes arriving with VESC Tool 6.06 firmware but no source release, prompting GPL compliance reminders and firmware-tracking discipline. Source: knowledge/notes/input_part014_review.md, L147 to L148
[^express]: Bundled VESC Express boards failing to enumerate, forcing installers to hang separate CAN-connected modules for telemetry until firmware and header maps are fixed. Source: knowledge/notes/input_part014_review.md, L146 to L148. Source: knowledge/notes/input_part014_review.md, L180 to L180
[^supply]: Alibaba listings shipping Seven/Tronic controllers directly from the contract manufacturer with historical pricing but uncertain official support. Source: knowledge/notes/input_part014_review.md, L163 to L164
[^thermal]: Paolo’s assessment that the 18-FET Seven sandwiches Toll-class MOSFETs on 1.6 mm FR-4, yielding only ~15–20 % thermal improvement over X12 heat-sink mounting and keeping racers interested in alternatives like the K900. Source: knowledge/notes/input_part014_review.md, L164 to L164
[^tracking]: Community focus on logging Seven availability, pricing, and verified current limits as testing pushes past 210 A battery / 310 A phase baselines. Source: knowledge/notes/input_part014_review.md, L217 to L217

## References

[^1]: Source: knowledge/notes/input_part011_review.md, L770 to L772
