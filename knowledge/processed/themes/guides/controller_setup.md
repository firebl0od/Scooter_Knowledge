# Controller Setup and Tuning

## Baseline Build Profiles

- Dual 1 000 W motors paired with a 15 S 8 P battery and 40 A BMS deliver a proven commuting setup, with some builders planning 13 S packs initially and leaving room to scale back up to 15 S.[^build_example]

## Control Modes and Current Limits

- Riders switching from sine-wave controllers to full field-oriented control report higher top speeds and cooler motors on the same battery settings, noting that Xiaomi M365 conversions only held 90 A after reinforcing their hardware.[^foc_advantages]
- Square-wave aftermarket controller kits remain tempting at ~€80 for a dual pack with dash, but they hammer 150–200 A phase at launch, ride harsher for new users, and run noisier than VESC-based FOC setups despite the simple wiring.[^1]
- Sustained cut-outs under load may point to BMS current limits: scooters that pass bench tests but trip under rider weight likely need higher-capacity packs or relaxed protection thresholds.[^bms_cutout]
- Logs from 12 S setups show ~45 km/h at 32.5 A; raising voltage to 15 S and reducing current is recommended for better efficiency and lower heat.[^voltage_swap]
- VTA controllers keep daily service around 35 A and can stretch to brief 65 A bursts on 13 S builds once phase leads are upsized, but stock crimps have melted near 45 A—upgrade cabling before chasing headline currents.[^vta_wiring]
- XiaoGen’s “power control” throttle profiles map lever position directly to current; use the flat curve for linear torque delivery and the quadratic curve when you need a softer launch before full power arrives.[^power_control_modes]
- Lock “Direct power control” to Always On when chasing top speed—leaving speed control enabled caps Pro/1S builds near the 45 km/h firmware entry even if the hardware can deliver more.[^direct_power_control]
- Voltage without current headroom hits diminishing returns: 14 S tunes on Monorim 500 W hubs plateau near 55 km/h unless peak amps rise, and stock 12 S–13 S conversions overheat 350 W motors until you move to a 500 W hub with reinforced controllers.[^voltage_headroom]

## Current Relationships & Cruise Options

- Artem’s relationship `I_phase = I_batt × V_batt ÷ V_motor` explains why phase torque fades as ERPM rises; expect battery current to climb from ~16 A at launch toward the configured limit as motor voltage increases, and keep phase current above battery current for predictable torque.[^phase_relationship]
- VESC Tool still lacks native cruise control, but Spintend’s handheld remote consolidates throttle, brake, horn, and light lines while offering button-activated cruise and reducing deck wiring; open-source SmartDisplay firmware may add a speed-lock profile later.[^spintend_cruise]

## Practical Current Heuristics

- Start hub tunes with Artem’s sizing math: phase amps roughly equal to motor wattage ÷ 10 and battery amps ≈ phase × 0.67; if you raise phase current for stronger launches, trim battery current by the same proportion so small stators stay inside their thermal envelope.[^2]
- Keep CFW battery current near 24 A on stock traces and only stretch to 27–28 A after reinforcing the board—“1200 W” presets without hardware upgrades still overheat adapters.[^cfw_24a_ceiling]
- Track controller and stator telemetry together.
  - Koxx’s logs showed phase current clipping once battery limits were reached around 25–30 km/h and that hard regen pulses add ≈5 °C to the stator, highlighting why current math and temperature logging must be reviewed together after every tune change.[^3]
- Treat field-weakening as a high-speed tool only; riders are still seeing 20–40 km/h gains but warn that the extra current draw demands tight temperature monitoring and duty-cycle triggers so launch torque and controller temps stay manageable.[^4]
- Dual Spintend crews treat 120–130 A phase per motor (≈160 A ABS max) as the realistic ceiling; if a hub “stutters” above ~85 A, assume a blown MOSFET or loose phase and inspect wiring or rerun sensorless detection before simply lowering limits.[^5]
- Keep Xiaomi throttle “intensity of current change” near 100 mA when onboarding newcomers on 13 S4 P builds—higher ramps deliver twitchy launches even though the added voltage more than doubles stock energy.[^throttle_intensity]
- Expect 500 W hubs to pull the full 32 A that Xiaogen allows once fed by larger packs; start closer to 29 A on 4 P batteries, log controller temperatures, and only raise current if the hardware stays cool.[^500w_currents]
- Rita’s 40 A fuse leaves almost no buffer—telemetry already shows 39 A spikes on 13 S13 P packs without adding useful torque above ~35 A on single Xiaomi hubs, so most riders settle near 32 A to protect the adapter.[^rita_fuse_ceiling]
- Stock Xiaomi controllers survive short 12 S shakedowns when current stays near 25 A and KERS is disabled; reinforce traces and components before lifting limits with XiaoGen or custom firmware.[^stock_12s_limit]

## Thermal Management & Regen Safety

- Flipsky’s compact single begins brushing 60 °C on the MOSFETs within 3 km at 50 A battery / 85 A phase, pushing owners to improve heatsink pressure, refresh thermal paste, and add 40 mm fans before experimenting with 100–120 A tunes.[^6]
- Keep battery-side regen at or below the pack’s amp-hour rating (e.g., ≤10 A on a 10 Ah block) and set controller regen roughly 15 A higher so excess energy bleeds off as heat instead of spiking the cells or BMS.[^7]
- Manual hall detection on warm motors at ≈70 A finally cleared Mirono’s off-the-line clonk; rerun both motor wizards on a full battery and road-test immediately after detection so sensor faults surface before a commute.[^8]
- When sensorless detection misbehaves, unplug the hall loom and rerun the test.
  - Wheelway and Spintend owners found that leaving halls connected during “sensorless” detection corrupted profiles until they re-detected with the harness removed.[^9]
- If Spintend’s external ADC module feeds nonsense values, temporarily bypass it by wiring 3.3 V, signal, and ground straight from the VESC to the throttle or brake; just avoid slamming 5 V accessories onto the 3.3 V rail to protect the board.[^10]
- Monorim 500 W hubs that vibrate after a 45 km/h panic stop usually signal controller stress rather than bad bearings; inspect Rita braking current, VTA MOSFET clamping pressure, and thermal paste coverage before condemning the motor.[^monorim_vibration]
- Builders now coat controller fasteners with medium-strength thread locker and replace Kapton tape under MOSFETs with high-conductivity pads to keep clamp pressure even and improve heat transfer on high-current tunes.[^threadlocker_pads]
- Clone controller shells sometimes need longer screws and washers; swapping 10 mm hardware for 16 mm cured intermittent error 28 by clamping the PCB properly.[^clone_screw_length]
- Refresh cooling stacks during installs: clean flux, replace Kapton with silicone pads, add rubber preload, and seat the temperature sensor between MOSFETs so contact pressure and readings stay accurate.[^pad_stack_refresh]
- Treat 60–65 °C as the sustainable ceiling for stock Xiaomi controllers—even 36 V builds that creep toward 88 °C on long climbs need derated current or upgraded hardware before the MOSFETs fail.[^controller_60c]

## Firmware & Tooling Notes

- Paid XiaoFlasher remains the most reliable way to generate Xiaomi firmware bundles; fall back to ScooterHacking.org or XiaoGen only when slower iteration is acceptable, and keep 12 S scooters on conservative Xiaogen defaults until reinforced hardware is ready—tune voltage limits instead of chasing aggressive presets on fragile builds.[^xiaoflasher_priority]
- Flash stock firmware with standard DownG for BLE 073/DRV 1.5.5, then switch to the Xiaogen-modded DownG APK for custom ZIPs—XiaoFlasher cannot push Xiaogen bundles directly, and remember BLE firmware lives on the dashboard.[^downg_workflow]
- Keep a USB ST-Link V2 in the toolbox before downgrading Pro 2 dashboards; failed BLE writes leave only a blinking tail light until you clip on and reflash.[^stlink_backup]
- Treat a solid red controller LED paired with a locked wheel as a shorted MOSFET bank—replace the transistors instead of chasing phantom wiring faults.[^red_led_mosfet]
- Avoid bypassing the scooter BMS when adding externals; Denis’ production harness already exposes the required leads without sacrificing safety checks.[^bms_bypass_warning]
- Babysit Rita firmware updates: keep the scooter in the dash’s Wi-Fi update screen, toggle the headlight every minute to defeat auto-sleep, and expect the progress bar to sit still before it completes.[^rita_update_babysit]
- Favor Rita v6 on dual-pack builds—it clears spurious over-temperature warnings without the v5 instability riders logged on paired 13 S packs.[^rita_v6_preferred]
- Flash BLE 090 on M365 dashboards before loading XiaoGen firmware; skipping the step leaves the migration tools unable to talk to newer boards.[^xiaogen_ble090]
- XiaoGen migrations for Pro 2/1S/Essential scooters still demand a bridge ZIP: restore DRV155 stock firmware, flash `XioGen2-0-5_Migrate.zip` with the Xiaogen DownG app, then load custom builds; future updates repeat the bridge and rollbacks use standard DownG/XiaoFlasher tools.[^xg_bridge_workflow]
- Set Rita’s external-pack cell count explicitly (e.g., dual 12 S) so dashboard voltage and speed telemetry stay live; disabling BMS checks in firmware robs you of that data.[^dual12s_config]
- Electronic braking still works on 12 S externals once Rita’s cell-count setting matches the hardware—the early “no e-brake above 10 S” reports traced back to misconfiguration.[^regen_cellcount]
- Expect the M365 2.0 dash to keep showing 0 W after a Rita install; the adapter emulates the original telemetry but does not update the wattage field.[^dash_watt_zero]
- iOS owners still need Android hardware (or an emulator) for ScooterHacking utilities because Apple blocks sideloading; otherwise ST-Link reflashes remain the fallback.[^ios_android]
- BLE 074 stays the stable choice on Pro dashboards, while BLE 073 v6 continues to act erratically; power-cycle stubborn boards between flashes to clear connection issues.[^ble074]
- VTA controllers ship with ESC 1.5.5 for Pro 2 hardware, but their dashboards should not be downgraded to BLE 090—stick with modern BLE and double-flash Xiaogen if the first pass stalls.[^vta_ble]
- Tudor can ship replacement VTA boards in roughly one to two days and is bench-testing hardware past 60 V, giving builders confidence to explore 14 S setups once braking currents are under control.[^tudor_support]
- Pocket XT30 wattmeters cost about €10; extend their leads and mount them near the handlebar to log charge/discharge current without upsetting KERS or Rita wiring.[^xt30_wattmeter]
- If a scooter stays dark after adding Rita, disconnect the dashboard and short the second-bottom and top pins to confirm the ESC still powers, inspect underside traces, and fall back to an ST-Link if the 5 V rail looks suspect.[^dark_after_rita]
- Camilo’s BLE 074 v7 adds throttle filtering and slow mode, but some Xiaogen/power-control riders report sluggish launches or random slow-mode engagement—disable cruise or revert to earlier BLE until patches land.[^ble074v7]
- Avoid “speed booster” 3 S add-ons in series with a 10 S pack; sag on hills trips firmware limits or BMS protection, so monitor current with M365 Dashboard graphs and retune amps before re-enabling the booster.[^series_booster]
- A healthy 12 S conversion (≈50.4 V external paired with ~41 V internal) should spin near 40 km/h even on the 250 W 1S motor—32 km/h results mean the firmware is still limiting output and needs a fresh XiaoGen tune.[^12s_speed_expectation]
- Rita still needs matching over-voltage firmware when experimenting with 13 S/15 S packs—set the controller ceiling near 63 V and confirm the hardware can tolerate the target voltage before expecting Rita to clear error 24.[^rita_overvoltage]
- Stock VTA controllers now reject Xiaogen firmware unless you spoof a valid serial (`21886/00XXXXXX`) and flash through the modified DownG build; keep an ST-Link handy in case the dashboard bricks mid-write.[^vta_sn_spoof]
- 1S riders stepping up to 12 S externals first downgrade to `mp365_drv221_1s` and `mp365_ble129_1s`, then load a 51 V XiaoFlasher profile with ~25 A sport, 15 A eco, KERS off, and active temperature logging—skipping the sequence has already killed controllers until an ST-Link rescue.[^1s_migrate]
- XiaoGen migrations for 1S and Essential scooters still require flashing the provided “migrate” bundle before custom firmware, keeping stock BLE, and staging an ST-Link in case the dash blanks on first boot.[^essential_migrate]
- Lite/Essential riders pushing 12 S externals cap custom firmware around 51 V so the dash stays happy; Rita’s configuration panel only appears once the external pack sits a few tenths of a volt above the internal.[^lite_ceiling]
- Custom 11 S builds drop regen ceilings toward 47 V and align Rita’s cell-count settings while budgeting a dedicated 11 S charger, since the stock 10 S brick stalls near 41.7 V.[^regen_11s]

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
[^xiaoflasher_priority]: Source: knowledge/notes/all_part01_review.md†L601-L601
[^vta_sn_spoof]: Source: knowledge/notes/all_part01_review.md†L637-L637
[^1s_migrate]: Source: knowledge/notes/all_part01_review.md†L638-L638
[^vta_wiring]: Source: knowledge/notes/all_part01_review.md†L617-L617
[^rita_fuse_ceiling]: Source: knowledge/notes/all_part01_review.md†L619-L619
[^stock_12s_limit]: Source: knowledge/notes/all_part01_review.md†L620-L620
[^power_control_modes]: Source: knowledge/notes/all_part01_review.md†L713-L713
[^direct_power_control]: Source: knowledge/notes/all_part01_review.md†L840-L840
[^red_led_mosfet]: Source: knowledge/notes/all_part01_review.md†L707-L707
[^bms_bypass_warning]: Source: knowledge/notes/all_part01_review.md†L708-L708
[^rita_update_babysit]: Source: knowledge/notes/all_part01_review.md†L709-L709
[^rita_v6_preferred]: Source: knowledge/notes/all_part01_review.md†L710-L710
[^xiaogen_ble090]: Source: knowledge/notes/all_part01_review.md†L712-L712
[^dual12s_config]: Source: knowledge/notes/all_part01_review.md†L714-L714
[^regen_cellcount]: Source: knowledge/notes/all_part01_review.md†L715-L715
[^dash_watt_zero]: Source: knowledge/notes/all_part01_review.md†L716-L716
[^controller_60c]: Source: knowledge/notes/all_part01_review.md†L621-L621
[^essential_migrate]: Source: knowledge/notes/all_part01_review.md†L668-L668
[^lite_ceiling]: Source: knowledge/notes/all_part01_review.md†L669-L669
[^regen_11s]: Source: knowledge/notes/all_part01_review.md†L671-L671
[^voltage_headroom]: Source: knowledge/notes/all_part01_review.md†L685-L685
[^cfw_24a_ceiling]: Source: knowledge/notes/all_part01_review.md†L845-L845
[^clone_screw_length]: Source: knowledge/notes/all_part01_review.md†L810-L810
[^pad_stack_refresh]: Source: knowledge/notes/all_part01_review.md†L809-L809
[^xg_bridge_workflow]: Source: knowledge/notes/all_part01_review.md†L839-L839
[^12s_speed_expectation]: Source: knowledge/notes/all_part01_review.md†L844-L844


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
[^monorim_vibration]: Source: knowledge/notes/all_part01_review.md†L508-L508
[^threadlocker_pads]: Source: knowledge/notes/all_part01_review.md†L509-L509
[^downg_workflow]: Source: knowledge/notes/all_part01_review.md†L522-L522
[^stlink_backup]: Source: knowledge/notes/all_part01_review.md†L523-L523
[^ios_android]: Source: knowledge/notes/all_part01_review.md†L524-L524
[^ble074]: Source: knowledge/notes/all_part01_review.md†L525-L525
[^vta_ble]: Source: knowledge/notes/all_part01_review.md†L526-L526
[^tudor_support]: Source: knowledge/notes/all_part01_review.md†L527-L527
[^xt30_wattmeter]: Source: knowledge/notes/all_part01_review.md†L528-L528
[^dark_after_rita]: Source: knowledge/notes/all_part01_review.md†L534-L534
[^ble074v7]: Source: knowledge/notes/all_part01_review.md†L535-L535
[^series_booster]: Source: knowledge/notes/all_part01_review.md†L536-L536
[^rita_overvoltage]: Source: knowledge/notes/all_part01_review.md†L537-L537
[^throttle_intensity]: Source: knowledge/notes/all_part01_review.md†L514-L514
[^500w_currents]: Source: knowledge/notes/all_part01_review.md†L519-L519
