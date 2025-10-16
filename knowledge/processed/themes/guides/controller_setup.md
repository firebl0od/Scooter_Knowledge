# Controller Setup and Tuning

## Baseline Build Profiles

- Dual 1 000 W motors paired with a 15 S 8 P battery and 40 A BMS deliver a proven commuting setup, with some builders planning 13 S packs initially and leaving room to scale back up to 15 S.[^build_example]

## Control Modes and Current Limits

- Riders switching from sine-wave controllers to full field-oriented control report higher top speeds and cooler motors on the same battery settings, noting that Xiaomi M365 conversions only held 90 A after reinforcing their hardware.[^foc_advantages]
- Square-wave aftermarket controller kits remain tempting at ~€80 for a dual pack with dash, but they hammer 150–200 A phase at launch, ride harsher for new users, and run noisier than VESC-based FOC setups despite the simple wiring.[^1]
- Sustained cut-outs under load may point to BMS current limits: scooters that pass bench tests but trip under rider weight likely need higher-capacity packs or relaxed protection thresholds.[^bms_cutout]
- Logs from 12 S setups show ~45 km/h at 32.5 A; raising voltage to 15 S and reducing current is recommended for better efficiency and lower heat.[^voltage_swap]

## Xiaomi Firmware Workflows (Denis Part 02 Lines 3 001–4 500 & 7 501–9 000)

- **Follow the XiaoGen migration order.** Keep the original BLE board, run the m365Downgrade XG Mod migrator once on Pro 2/1S/Essential scooters, then load custom configs—future updates skip the migrate package entirely to avoid bricks.[^denis-xiaogen-flow]
- **SpeedBoost isn’t free power.** XiaoDash’s paid field-weakening mode mimics Ninebot’s magic serial trick, boosting speed 35–40 % at the cost of range, heat, and a requirement for uprated batteries, MOSFETs, and cabling.[^denis-speedboost]
- **20S emulation is still vaporware.** XiaoDash’s promised 20S BMS mode remains “coming soon”; veterans warn that extreme 6S booster packs and 20S trace-cut builds keep killing hardware despite the marketing.[^denis-20s-emu]
- **Clone controller checklist.** Spoofed DRV/BLE boards often need their serial re-entered in DownG before XiaoGen will flash—load the migrate package twice on Pro 1 hardware, but run the dedicated migrator first on Pro 2 units.[^denis-clone-serial]
- **Recover missing telemetry by rebuilding firmware.** If XiaoGen flashes leave the battery gauge blank, read the UID from DownG with a stock pack, rebuild the firmware, reflash, and restore single-tap mode by assigning the same action to every press profile in the generator.[^denis-xiaogen-uid]
- **Kill power before rewiring trace cuts.** Never reconnect a trace-cut harness with the wheel spinning; tests have torched the U4 regulator instantly, so power down before touching Rita leads or jumpers.[^denis-tracecut-warning]

## Current Relationships & Cruise Options

- Artem’s relationship `I_phase = I_batt × V_batt ÷ V_motor` explains why phase torque fades as ERPM rises; expect battery current to climb from ~16 A at launch toward the configured limit as motor voltage increases, and keep phase current above battery current for predictable torque.[^phase_relationship]
- VESC Tool still lacks native cruise control, but Spintend’s handheld remote consolidates throttle, brake, horn, and light lines while offering button-activated cruise and reducing deck wiring; open-source SmartDisplay firmware may add a speed-lock profile later.[^spintend_cruise]

## Practical Current Heuristics

- Start hub tunes with Artem’s sizing math: phase amps roughly equal to motor wattage ÷ 10 and battery amps ≈ phase × 0.67; if you raise phase current for stronger launches, trim battery current by the same proportion so small stators stay inside their thermal envelope.[^2]
- Track controller and stator telemetry together.
  - Koxx’s logs showed phase current clipping once battery limits were reached around 25–30 km/h and that hard regen pulses add ≈5 °C to the stator, highlighting why current math and temperature logging must be reviewed together after every tune change.[^3]
- Treat field-weakening as a high-speed tool only; riders are still seeing 20–40 km/h gains but warn that the extra current draw demands tight temperature monitoring and duty-cycle triggers so launch torque and controller temps stay manageable.[^4]
- Dual Spintend crews treat 120–130 A phase per motor (≈160 A ABS max) as the realistic ceiling; if a hub “stutters” above ~85 A, assume a blown MOSFET or loose phase and inspect wiring or rerun sensorless detection before simply lowering limits.[^5]

## Thermal Management & Regen Safety

- Xiaomi V3 controller upgrades still start with hard parts: swap in IRFB4110 or NCEP85T14 MOSFETs, replace Kapton tape with 0.5 mm thermal pads, flood copper traces with solder or supplemental wire, and direct-solder phase leads instead of stacking adapters; Mirono’s reinforced build held roughly 55 °C continuous before the motor became the thermal limit.[^denis-controller-hardening]
- Flipsky’s compact single begins brushing 60 °C on the MOSFETs within 3 km at 50 A battery / 85 A phase, pushing owners to improve heatsink pressure, refresh thermal paste, and add 40 mm fans before experimenting with 100–120 A tunes.[^6]
- Keep battery-side regen at or below the pack’s amp-hour rating (e.g., ≤10 A on a 10 Ah block) and set controller regen roughly 15 A higher so excess energy bleeds off as heat instead of spiking the cells or BMS.[^7]
- Paolo’s 15 S-ready ESC mod cuts the feed trace to U4 and strings diodes in series; double-check the ≈3 W dissipation across 21 diodes and log NTC temps before treating it as production-ready.[^denis-u4]
- Manual hall detection on warm motors at ≈70 A finally cleared Mirono’s off-the-line clonk; rerun both motor wizards on a full battery and road-test immediately after detection so sensor faults surface before a commute.[^8]
- When sensorless detection misbehaves, unplug the hall loom and rerun the test.
  - Wheelway and Spintend owners found that leaving halls connected during “sensorless” detection corrupted profiles until they re-detected with the harness removed.[^9]
- If Spintend’s external ADC module feeds nonsense values, temporarily bypass it by wiring 3.3 V, signal, and ground straight from the VESC to the throttle or brake; just avoid slamming 5 V accessories onto the 3.3 V rail to protect the board.[^10]

## Example Tuning Profiles

- A Zero 10X dialled to 100 A rear / 60 A front phase with 80 A/50 A battery caps provides smooth launches and strong mid-speed pull without overheating.[^zero10x]
- Stock VSETT controllers taper output around 52 V (~10 % state of charge), effectively reducing battery current to protect aging cells.
  - behaviour the community wants to replicate in VESC firmware for builds lacking smart BMS data.[^vsett_taper]
- Kelly KLS scooter controllers often refuse USB connections.
  - plan on the BLE module or legacy Windows XP drivers when you need to flash or configure those platforms.[^11]

## Acceleration Logging & Telemetry

- Benchmark 0–70 km/h runs with Dragy or Race Timer, filming calibrated dashboards at 60 fps and averaging matched-direction passes to cancel GPS lag; Drag Racer remains convenient but needs clear skies to hold lock.[^accel_logging]
- Align controller telemetry with GPS by setting accurate pole counts and measuring wheel diameter under rider load so VESC speed stays slightly above GPS.
  - a useful safety margin for legal compliance checks.[^speed_alignment]
- Use phase-current logging as a health check: veterans start commuter hubs around 90 A phase / 30 A battery and scale toward 120 A phase if cooling allows, noting that excessive phase amps raise EMI/noise stress on Ubox logic stages.[^phase_baseline]

[^build_example]: Source: knowledge/notes/input_part000_review.md, line 37.
[^foc_advantages]: Source: knowledge/notes/input_part000_review.md, line 68.
[^bms_cutout]: Source: knowledge/notes/input_part000_review.md, line 70.
[^voltage_swap]: Source: knowledge/notes/input_part000_review.md, line 71.
[^phase_relationship]: Source: knowledge/notes/input_part000_review.md, line 106.
[^spintend_cruise]: Source: knowledge/notes/input_part000_review.md, line 110.
[^zero10x]: Source: knowledge/notes/input_part000_review.md, line 92.
[^vsett_taper]: Source: knowledge/notes/input_part000_review.md, line 93.
[^accel_logging]: Source: knowledge/notes/input_part000_review.md, line 133.
[^speed_alignment]: Source: knowledge/notes/input_part000_review.md, line 135.
[^phase_baseline]: Source: knowledge/notes/input_part000_review.md, line 198.
[^denis-xiaogen-flow]: Source: knowledge/notes/denis_all_part02_review.md†L910-L910
[^denis-speedboost]: Source: knowledge/notes/denis_all_part02_review.md†L912-L912
[^denis-20s-emu]: Source: knowledge/notes/denis_all_part02_review.md†L917-L917
[^denis-clone-serial]: Source: knowledge/notes/denis_all_part02_review.md†L958-L958
[^denis-xiaogen-uid]: Source: knowledge/notes/denis_all_part02_review.md†L1028-L1028
[^denis-tracecut-warning]: Source: knowledge/notes/denis_all_part02_review.md†L959-L959


## References

[^1]: Source: knowledge/notes/input_part000_review.md†L671-L675
[^2]: Source: knowledge/notes/input_part000_review.md†L304-L304
[^3]: Source: knowledge/notes/input_part000_review.md†L306-L306
[^4]: Source: knowledge/notes/input_part000_review.md†L307-L307
[^5]: Source: knowledge/notes/input_part000_review.md†L708-L716
[^6]: Source: knowledge/notes/input_part000_review.md†L456-L458
[^7]: Source: knowledge/notes/input_part000_review.md†L458-L461
[^8]: Source: knowledge/notes/input_part000_review.md†L514-L518
[^9]: Source: knowledge/notes/input_part000_review.md†L720-L725
[^10]: Source: knowledge/notes/input_part000_review.md†L734-L739
[^11]: Source: knowledge/notes/input_part000_review.md†L688-L690
[^denis-u4]: Source: knowledge/notes/denis_all_part02_review.md†L700-L700
[^denis-controller-hardening]: Source: knowledge/notes/denis_all_part02_review.md†L702-L724
