# Controller Setup and Tuning

## Baseline Build Profiles

- Dual 1 000 W motors paired with a 15 S 8 P battery and 40 A BMS deliver a proven commuting setup, with some builders planning 13 S packs initially and leaving room to scale back up to 15 S.[^build_example]

## Control Modes and Current Limits

- Riders switching from sine-wave controllers to full field-oriented control report higher top speeds and cooler motors on the same battery settings, noting that Xiaomi M365 conversions only held 90 A after reinforcing their hardware.[^foc_advantages]
- Square-wave aftermarket controller kits remain tempting at ~€80 for a dual pack with dash, but they hammer 150–200 A phase at launch, ride harsher for new users, and run noisier than VESC-based FOC setups despite the simple wiring.[^1]
- Sustained cut-outs under load may point to BMS current limits: scooters that pass bench tests but trip under rider weight likely need higher-capacity packs or relaxed protection thresholds.[^bms_cutout]
- Logs from 12 S setups show ~45 km/h at 32.5 A; raising voltage to 15 S and reducing current is recommended for better efficiency and lower heat.[^voltage_swap]

## Current Relationships & Cruise Options

- Artem’s relationship `I_phase = I_batt × V_batt ÷ V_motor` explains why phase torque fades as ERPM rises; expect battery current to climb from ~16 A at launch toward the configured limit as motor voltage increases, and keep phase current above battery current for predictable torque.[^phase_relationship]
- VESC Tool still lacks native cruise control, but Spintend’s handheld remote consolidates throttle, brake, horn, and light lines while offering button-activated cruise and reducing deck wiring; open-source SmartDisplay firmware may add a speed-lock profile later.[^spintend_cruise]

## Practical Current Heuristics

- Start hub tunes with Artem’s sizing math: phase amps roughly equal to motor wattage ÷ 10 and battery amps ≈ phase × 0.67; if you raise phase current for stronger launches, trim battery current by the same proportion so small stators stay inside their thermal envelope.[^2]
- Track controller and stator telemetry together.
  - Koxx’s logs showed phase current clipping once battery limits were reached around 25–30 km/h and that hard regen pulses add ≈5 °C to the stator, highlighting why current math and temperature logging must be reviewed together after every tune change.[^3]
- Treat field-weakening as a high-speed tool only; riders are still seeing 20–40 km/h gains but warn that the extra current draw demands tight temperature monitoring and duty-cycle triggers so launch torque and controller temps stay manageable.[^4]
- Dual Spintend crews treat 120–130 A phase per motor (≈160 A ABS max) as the realistic ceiling; if a hub “stutters” above ~85 A, assume a blown MOSFET or loose phase and inspect wiring or rerun sensorless detection before simply lowering limits.[^5]

## Sensor Modes & Launch Tuning

- Lower the hall-to-sensorless handoff when hubs cog: Mirono cut the switchover from 2 000 to ≈1 200 ERPM so Vsett hubs stay synced at crawl speeds, and the tweak aligns with the community reminder that halls usually drop out around 2 500 ERPM.[^hall_switchover]
- Vedder’s recent HFI refinements now deliver hall-less launches on Xiaomi-class ESC ports, and Spintend’s uBox shows up inside VESC Tool’s hardware directory after the Onside Ring submission—proof that official firmware recognises the hardware and that hall-free starts are improving.[^hfi_update]
- Full sensorless starts on 20 S hardware still need a kick; riders keep adding hall looms to legacy hubs and watch VESC logs for “brbrbr” oscillations that point to bad flux or inductance autodetect values.[^sensorless_caveats]

## Firmware Recovery & Diagnostics

- When the Spintend uBox BLE module refuses to pair, builders still connect over USB, flash both bootloader and firmware from the shared Google Drive, and only then retry Bluetooth pairing; VESC Tool desktop first, then Android, with a controller reboot between steps keeps the module advertising.[^ubox_ble]
- If Spintend firmware 5.3 throws false ABS over-current trips at high ERPM, enable the ABS feature in VESC Tool and lower the current-filter constant to calm the protection logic before chasing hardware fixes.[^spintend_abs]
- Mirono cured mid-load surging by reordering hall wires back to the standard 1-2-3 sequence and lowering the sensorless handover from 2 000 ERPM to 1 200 ERPM, proving that VESC auto-detect can pass with mis-sequenced halls yet still misfire on-road.[^hall_reorder]

## Harness Preparation & CAN Safety

- JST-SM three-pin leads from AliExpress match the uBox V2 harness, but set the Spintend ADC adapter to 5 V mode, route every signal before you apply pack voltage, and back motor autodetect amps down if the defaults seem aggressive.[^jst_adapter]
- Factory Flipsky 75100 mains often arrive as cold joints; trim insulation so the wire bottoms out, flood the bullet with solder, and flatten the strands onto the PCB pad with ceramic tweezers before shrinking the insulation.[^flipsky_rework]
- Dual-controller scooters that limp on a single ESC should disconnect the slave’s CAN and battery leads (phases and halls can stay, though full isolation is safer) to avoid back-feeding the dead controller.[^dual_can_isolation]

## Display & Control Integrations

- Artem published an open-source TTGO T-Display dashboard for ESP32/RP2040 variants that reads VESC telemetry over BLE and gives scooters a configurable wireless cluster.[^ttgo_display]
- Xiaomi’s BLE dash maintains stock-style modes, telemetry, and VESC Tool access when paired with a separate Bluetooth module, making it a stealth drop-in for commuter builds.[^xiaomi_ble]
- Spintend’s ADC adapter offers switchable 5 V/3.3 V outputs with onboard filtering, and the crew notes Spintend’s LCD throttle can bypass the board entirely when space is tight.[^spintend_adc]

## Thermal Management & Regen Safety

- Flipsky’s compact single begins brushing 60 °C on the MOSFETs within 3 km at 50 A battery / 85 A phase, pushing owners to improve heatsink pressure, refresh thermal paste, and add 40 mm fans before experimenting with 100–120 A tunes.[^6]
- Keep battery-side regen at or below the pack’s amp-hour rating (e.g., ≤10 A on a 10 Ah block) and set controller regen roughly 15 A higher so excess energy bleeds off as heat instead of spiking the cells or BMS.[^7]
- Manual hall detection on warm motors at ≈70 A finally cleared Mirono’s off-the-line clonk; rerun both motor wizards on a full battery and road-test immediately after detection so sensor faults surface before a commute.[^8]
- When sensorless detection misbehaves, unplug the hall loom and rerun the test.
  - Wheelway and Spintend owners found that leaving halls connected during “sensorless” detection corrupted profiles until they re-detected with the harness removed.[^9]
- If Spintend’s external ADC module feeds nonsense values, temporarily bypass it by wiring 3.3 V, signal, and ground straight from the VESC to the throttle or brake; just avoid slamming 5 V accessories onto the 3.3 V rail to protect the board.[^10]

## Firmware Notes & Controller Limits

- Artem continues to warn that uBox hardware can burn on firmware 5.3 due to a current-sensing regression; either hold on 5.2 or lower amp limits until Spintend publishes a fix.[^ubox_fw53]
- Gigolo Joe’s Flipsky 75100 V2 proved stable on 20 S (≈77 V) with firmware 5.03 at 160 A phase / 110 A battery, but the controller reads pack voltage a few volts low—budget extra headroom near max voltage.[^75100_20s]

## Example Tuning Profiles

- A Zero 10X dialled to 100 A rear / 60 A front phase with 80 A/50 A battery caps provides smooth launches and strong mid-speed pull without overheating.[^zero10x]
- Stock VSETT controllers taper output around 52 V (~10 % state of charge), effectively reducing battery current to protect aging cells.
  - behaviour the community wants to replicate in VESC firmware for builds lacking smart BMS data.[^vsett_taper]
- Kelly KLS scooter controllers often refuse USB connections.
  - plan on the BLE module or legacy Windows XP drivers when you need to flash or configure those platforms.[^11]
- Track crews mapped Kelly KLS power output by matching phase and battery percentages: a 7212S labelled for 50 A battery actually delivered ~120 A, while 7218S builds logged 240 A at 115 km/h until cooling became the bottleneck—size cabling accordingly.[^kelly_mapping]

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
[^ubox_ble]: Source: knowledge/notes/input_part002_review.md†L551-L553
[^spintend_abs]: Source: knowledge/notes/input_part002_review.md†L567-L567
[^hall_reorder]: Source: knowledge/notes/input_part002_review.md†L576-L576
[^ttgo_display]: Source: knowledge/notes/input_part002_review.md†L18713-L18727
[^xiaomi_ble]: Source: knowledge/notes/input_part002_review.md†L19188-L19193
[^spintend_adc]: Source: knowledge/notes/input_part002_review.md†L19972-L19990
[^ubox_fw53]: Source: knowledge/notes/input_part002_review.md†L578-L578
[^75100_20s]: Source: knowledge/notes/input_part002_review.md†L580-L580
[^kelly_mapping]: Source: knowledge/notes/input_part002_review.md†L562-L563
[^hall_switchover]: Source: data/vesc_help_group/text_slices/input_part002.txt†L21201-L21224; data/vesc_help_group/text_slices/input_part002.txt†L21233-L21257
[^hfi_update]: Source: data/vesc_help_group/text_slices/input_part002.txt†L21212-L21411
[^sensorless_caveats]: Source: data/vesc_help_group/text_slices/input_part002.txt†L21195-L21211; data/vesc_help_group/text_slices/input_part002.txt†L21257-L21310
[^jst_adapter]: Source: data/vesc_help_group/text_slices/input_part002.txt†L20810-L20832
[^flipsky_rework]: Source: data/vesc_help_group/text_slices/input_part002.txt†L21055-L21084
[^dual_can_isolation]: Source: data/vesc_help_group/text_slices/input_part002.txt†L21442-L21487


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
