# Controller Setup and Tuning

## Overview

Setting up VESC and other controllers for electric scooters involves choosing control modes, configuring current limits, and understanding firmware workflows. This guide covers baseline build profiles, FOC vs. square-wave operation, motor detection procedures, and platform-specific configuration (Xiaomi, Spintend, Kelly, etc.). Proper controller setup maximizes performance while protecting hardware from damage.

## What You'll Learn

- Baseline controller configurations for common builds
- FOC vs. square-wave control modes and trade-offs
- Current limit tuning (battery vs. phase current)
- Firmware update procedures and compatibility
- Traction control configuration
- Platform-specific workflows (Xiaomi, Spintend, Kelly, Sabvoton)
- Troubleshooting common setup issues
- BMS interaction and cut-out prevention

## Baseline Build Profiles

- Dual 1 000 W motors paired with a 15 S 8 P battery and 40 A BMS deliver a proven commuting setup, with some builders planning 13 S packs initially and leaving room to scale back up to 15 S.[^build_example]
- Newcomers pairing MKSESC 75100 controllers with sub‑1 kW commuter hubs still ask for step-by-step guidance beyond YouTube walkthroughs—capture a starter-friendly configuration checklist so they can get rolling without expert hand-holding.[^mksesc-onboarding]

## Control Modes and Current Limits

- Riders switching from sine-wave controllers to full field-oriented control report higher top speeds and cooler motors on the same battery settings, noting that Xiaomi M365 conversions only held 90 A after reinforcing their hardware.[^foc_advantages]
- Square-wave aftermarket controller kits remain tempting at ~€80 for a dual pack with dash, but they hammer 150–200 A phase at launch, ride harsher for new users, and run noisier than VESC-based FOC setups despite the simple wiring.[^1]
- Sabvoton’s phone app still lacks live current readouts and its heavy case worries single-stem builders; Kelly deployments continue to work but demand staged programming, BLE adapters, and careful wiring to avoid red-light detection faults on high-KV hubs.[^sabvoton_kelly]
- When updating Spintend firmware, stick with the vendor-supplied FW 5.3 BIN and let VESC Tool auto-detect the R3 hardware; forcing V6 targets or manual overrides has already bricked FlipSky units.[^ip001-spintendfw]
- Paolo’s unlocked FW 5.3 binary lifts thermal/current ceilings on Flipsky 75100 controllers, but there is no equivalent for the Spintend Ubox V2 yet because the vendor firmware needed to port the hack is unavailable; plan on staying within stock limits on Ubox hardware.[^ip001-flipsky-unlock]
- Traction control keeps dual builds tidy but still trims torque—JPPL reminds newcomers that VESC’s algorithm is “ok” yet sacrifices punch to rein in wheelspin, so treat it as a stability aid rather than a free performance boost.[^vesc_tc_torque]
- Sustained cut-outs under load may point to BMS current limits: scooters that pass bench tests but trip under rider weight likely need higher-capacity packs or relaxed protection thresholds.[^bms_cutout]
- If one motor must run sensorless, tune VSS carefully and be ready to gate the front controller—HFI or scripting a PWM disable below a chosen ERPM keeps dual-drive launches smooth until you can rewire hall sensors.[^sensorless_launch]
- Logs from 12 S setups show ~45 km/h at 32.5 A; raising voltage to 15 S and reducing current is recommended for better efficiency and lower heat.[^voltage_swap]
- VTA controllers keep daily service around 35 A and can stretch to brief 65 A bursts on 13 S builds once phase leads are upsized, but stock crimps have melted near 45 A—upgrade cabling before chasing headline currents.[^vta_wiring]
- XiaoGen’s “power control” throttle profiles map lever position directly to current; use the flat curve for linear torque delivery and the quadratic curve when you need a softer launch before full power arrives.[^power_control_modes]
- Lock “Direct power control” to Always On when chasing top speed—leaving speed control enabled caps Pro/1S builds near the 45 km/h firmware entry even if the hardware can deliver more.[^direct_power_control]
- Voltage without current headroom hits diminishing returns: 14 S tunes on Monorim 500 W hubs plateau near 55 km/h unless peak amps rise, and stock 12 S–13 S conversions overheat 350 W motors until you move to a 500 W hub with reinforced controllers.[^voltage_headroom]

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

## Firmware Notes

- VESC Tool 6.05 ships with a Lisp demo that converts MP3 files into motor audio, but builders reported severe frame resonance and poor fidelity—treat it as a novelty rather than a production feature.[^vesc_audio_demo]

## Practical Current Heuristics

- Start hub tunes with Artem’s sizing math: phase amps roughly equal to motor wattage ÷ 10 and battery amps ≈ phase × 0.67; if you raise phase current for stronger launches, trim battery current by the same proportion so small stators stay inside their thermal envelope.[^2]
- Keep CFW battery current near 24 A on stock traces and only stretch to 27–28 A after reinforcing the board—“1200 W” presets without hardware upgrades still overheat adapters.[^cfw_24a_ceiling]
- Track controller and stator telemetry together.
  - Koxx’s logs showed phase current clipping once battery limits were reached around 25–30 km/h and that hard regen pulses add ≈5 °C to the stator, highlighting why current math and temperature logging must be reviewed together after every tune change.[^3]
- Treat field-weakening as a high-speed tool only; riders are still seeing 20–40 km/h gains but warn that the extra current draw demands tight temperature monitoring and duty-cycle triggers so launch torque and controller temps stay manageable.[^4]
- Updating Nucular controllers requires a FAT32 microSD with one firmware file per device (e.g., `Ncontr.bin`, `Ndisp.bin`); flash controller stages before the display and consider zeroing flux linkage to disable MTPA after detection if FW 0.8.5 quirks appear while you evaluate 0.8.6.[^ip001-nucular-fw]
- Back-to-back pulls comparing pure current control, MTPA, and +40 A field-weakening on dual Ubox hardware showed how 16 S 6 P test packs respond when FW engages near 90 % duty—use staged tests to document the trade-offs before shipping aggressive tunes.[^rosheee_fw]
- Izuna’s MP2 v0.5 cleared repeated ABS overcurrent faults only after trimming battery current and switching to hall sensors, highlighting how firmware sample modes interact with current limits on high-speed runs.[^izuna_abs]
- Dual Spintend crews treat 120–130 A phase per motor (≈160 A ABS max) as the realistic ceiling; if a hub “stutters” above ~85 A, assume a blown MOSFET or loose phase and inspect wiring or rerun sensorless detection before simply lowering limits.[^5]
- When ABS faults trip at modest battery current, raise the absolute-current ceiling to roughly 1.5× the phase limit so regen spikes and launch surges stop tripping protections while keeping the controller inside its thermal window.[^abs_ratio]

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
- Keep Xiaomi throttle “intensity of current change” near 100 mA when onboarding newcomers on 13 S4 P builds—higher ramps deliver twitchy launches even though the added voltage more than doubles stock energy.[^throttle_intensity]
- Expect 500 W hubs to pull the full 32 A that Xiaogen allows once fed by larger packs; start closer to 29 A on 4 P batteries, log controller temperatures, and only raise current if the hardware stays cool.[^500w_currents]
- Rita’s 40 A fuse leaves almost no buffer—telemetry already shows 39 A spikes on 13 S13 P packs without adding useful torque above ~35 A on single Xiaomi hubs, so most riders settle near 32 A to protect the adapter.[^rita_fuse_ceiling]
- Stock Xiaomi controllers survive short 12 S shakedowns when current stays near 25 A and KERS is disabled; reinforce traces and components before lifting limits with XiaoGen or custom firmware.[^stock_12s_limit]

## Thermal Management & Regen Safety

- Xiaomi V3 controller upgrades still start with hard parts: swap in IRFB4110 or NCEP85T14 MOSFETs, replace Kapton tape with 0.5 mm thermal pads, flood copper traces with solder or supplemental wire, and direct-solder phase leads instead of stacking adapters; Mirono’s reinforced build held roughly 55 °C continuous before the motor became the thermal limit.[^denis-controller-hardening]
- Flipsky’s compact single begins brushing 60 °C on the MOSFETs within 3 km at 50 A battery / 85 A phase, pushing owners to improve heatsink pressure, refresh thermal paste, and add 40 mm fans before experimenting with 100–120 A tunes.[^6]
- Keep battery-side regen at or below the pack’s amp-hour rating (e.g., ≤10 A on a 10 Ah block) and set controller regen roughly 15 A higher so excess energy bleeds off as heat instead of spiking the cells or BMS.[^7]
- Makerbase 84100 riders have yanked live XT60s at speed without killing the controller, but they now cap maximum throttle voltage in VESC Tool instead of adding pull-down resistors—ADC adapters top out around 2.1 V anyway.[^makerbase_disconnect]
- Regen tuning notes from recent 22 S builds keep battery braking near 3 A per cell and phase braking around 70 % of forward phase current, stepping changes gradually and pairing strong regen with a dedicated throttle so brake pads still share the load.[^regen_phase_ratio]
- Paolo’s 15 S-ready ESC mod cuts the feed trace to U4 and strings diodes in series; double-check the ≈3 W dissipation across 21 diodes and log NTC temps before treating it as production-ready.[^denis-u4]
- Manual hall detection on warm motors at ≈70 A finally cleared Mirono’s off-the-line clonk; rerun both motor wizards on a full battery and road-test immediately after detection so sensor faults surface before a commute.[^8]
- If motor detection spits out huge inductance values on undersized hubs, override them to roughly 150–300 µH to calm jitter and recover torque on Ubox Lite 100 V/100 A builds.[^manual_inductance_override]
- When sensorless detection misbehaves, unplug the hall loom and rerun the test.
  - Wheelway and Spintend owners found that leaving halls connected during “sensorless” detection corrupted profiles until they re-detected with the harness removed.[^9]
- Use the phase-current graph inside VESC Tool as a MOSFET health check—failed DRV legs show noisy hall traces, force BLDC-only operation beyond ≈10 % throttle, and shut the controller down until the stage is repaired.[^fault_trace]
- If Spintend’s external ADC module feeds nonsense values, double-check the 5 V/3.3 V selector before temporarily bypassing it with the controller’s 3.3 V rail; keep throttle sweeps short while testing direct-to-VESC wiring and never hot-plug 5 V sensors onto the 3.3 V pins to avoid killing the adapter.[^10]
- Bench tests with 90 % duty field weakening pulled ~100 A phase (≈20 A battery) to jump hubs from 38 kERPM to 53 kERPM at roughly 1.2 kW, confirming the ~40 % speed gain comes with heavy heat and poor efficiency.[^fw_jump]

## Wiring & Dual-Controller Notes

- Flipsky 75350 riders keep the throttle on ADC1, the brake switch on ADC2 with “Current No Reverse Brake ADC2,” and avoid tying hall 5 V rails between controllers unless absolutely necessary to prevent ground loops.[^flipsky_75350_wiring]
- Mixed-brand 75-series controllers share CAN only when they run identical firmware builds; Spintend’s ADC splitter forces stand-alone mode and kills traction control, so crews now pursue Lisp toggles or direct button wiring that preserves CAN where possible.[^mixed_can_fw]
- Dual-motor scooters that haze the front tire above ~100 A phase are taming launches by enabling Motor Current Scale profiles alongside traction control to soften initial torque without sacrificing top-end power.[^motor_current_scale]

## Firmware & Resources

- 3Shul CL350 owners hunting firmware can pull the official V3 sources from the Drive share community members unearthed to build 6.2-capable binaries even when the vendor site is silent.[^cl350_drive_share]

## Firmware Notes & Controller Limits

- Artem continues to warn that uBox hardware can burn on firmware 5.3 due to a current-sensing regression; either hold on 5.2 or lower amp limits until Spintend publishes a fix.[^ubox_fw53]
- Gigolo Joe’s Flipsky 75100 V2 proved stable on 20 S (≈77 V) with firmware 5.03 at 160 A phase / 110 A battery, but the controller reads pack voltage a few volts low—budget extra headroom near max voltage.[^75100_20s]
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
- Yoann’s Vsett 10 dual Lite conversion uses the ADC board’s 5 V rail to trigger a relay for a dedicated 12 V converter, keeps OEM lighting happy, and flags that the stock front suspension and tyres need upgrading once dual torque is unlocked.[^vsett-dual-lite]
- The build reuses a Nami 80 A BMS that trips near 120 A total, so Yoann caps pack current around 100–120 A while custom Lisp code scales phase amps versus ERPM to prevent wheelspin; note the thinner Alu Lite baseplate solders easier but trades some thermal mass.[^vsett-dual-lite]
- Kelly KLS scooter controllers often refuse USB connections.
  - plan on the BLE module or legacy Windows XP drivers when you need to flash or configure those platforms.[^11]
- Track crews mapped Kelly KLS power output by matching phase and battery percentages: a 7212S labelled for 50 A battery actually delivered ~120 A, while 7218S builds logged 240 A at 115 km/h until cooling became the bottleneck—size cabling accordingly.[^kelly_mapping]

## Sensorless Setup Considerations

- 🇪🇸AYO#74 is already riding a 22 S 11 P Molicel P45B pack without hall or cam sensors and is asking for configuration help, underscoring the need for a robust high-voltage sensorless checklist before first rides.[^sensorless_22s]

## Acceleration Logging & Telemetry

- Benchmark 0–70 km/h runs with Dragy or Race Timer, filming calibrated dashboards at 60 fps and averaging matched-direction passes to cancel GPS lag; Drag Racer remains convenient but needs clear skies to hold lock.[^accel_logging]
- Align controller telemetry with GPS by setting accurate pole counts and measuring wheel diameter under rider load so VESC speed stays slightly above GPS.
  - a useful safety margin for legal compliance checks.[^speed_alignment]
- Use phase-current logging as a health check: veterans start commuter hubs around 90 A phase / 30 A battery and scale toward 120 A phase if cooling allows, noting that excessive phase amps raise EMI/noise stress on Ubox logic stages.[^phase_baseline]

## Firmware Discipline & Safety Routines

- Treat beta firmware as a matched bundle: one crew cleared recurring “limited mode” flags only after downloading the same 6.06 beta on desktop, reflashing both controllers, and rerunning detection so the mobile client and ESC firmware stayed in lockstep.[^firmware-match]
- Keep a stealth profile on deck when jurisdictions cap speed—builders load a 25 km/h preset for roadside checks, then power-cycle to restore full output once police leave instead of tweaking menus in traffic.[^stealth-profile]
- Populate Motor Current Max Brake/Max Regen and validate halls before trusting regen; AliExpress hall testers let riders confirm sensor health without opening sealed hubs, and temperature probes should land on the controller’s temp+GND pins rather than the 5 V rail.[^hall-tester]

## Harness Mapping & Diagnostics

- Vsett harness tear-downs map orange to pack voltage, pink to the on/off detect line, white to the brake signal, and black to ground—meter continuity before repinning so accessory wiring doesn’t backfeed logic rails.[^vsett-colors]
## Platform-Specific Notes

- For the 52 V dual-motor Kukirin G2 Master, Haku recommends twin Mini Ubox controllers to retain the stock pack and 1 000 W hubs, while Marius warns the chassis wobbles above ~40 km/h even with a steering damper—keep speed near 50 km/h or move to a more stable frame for 15 kW ambitions.[^kukirin-g2]
- Expect roughly €100–120 per Alu Lite when budgeting European Mini Ubox stacks, setting realistic expectations when comparing DIY conversions against turnkey retrofits.[^kukirin-g2]
- 🇪🇸AYO#74 is rewiring a 60 V pack for 72 V Nami controllers; treat the phase-swapped experiment as provisional until field logs confirm the controllers stay happy on lower voltage.
  - capture start-up behaviour, temperature swing, and any firmware guardrails before recommending the retrofit.[^nami-72v-on-60v]

[^build_example]: Source: knowledge/notes/input_part000_review.md, line 37.
[^mksesc-onboarding]: Source: knowledge/notes/input_part013_review.md†L776-L776
[^foc_advantages]: Source: knowledge/notes/input_part000_review.md, line 68.
[^bms_cutout]: Source: knowledge/notes/input_part000_review.md, line 70.
[^voltage_swap]: Source: knowledge/notes/input_part000_review.md, line 71.
[^phase_relationship]: Source: knowledge/notes/input_part000_review.md, line 106.
[^spintend_cruise]: Source: knowledge/notes/input_part000_review.md, line 110.
[^vesc_audio_demo]: Source: knowledge/notes/input_part009_review.md†L414-L414.
[^zero10x]: Source: knowledge/notes/input_part000_review.md, line 92.
[^vsett_taper]: Source: knowledge/notes/input_part000_review.md, line 93.
[^vsett-dual-lite]: Source: knowledge/notes/input_part010_review.md†L604-L605
[^accel_logging]: Source: knowledge/notes/input_part000_review.md, line 133.
[^speed_alignment]: Source: knowledge/notes/input_part000_review.md, line 135.
[^phase_baseline]: Source: knowledge/notes/input_part000_review.md, line 198.
[^sensorless_22s]: Source: knowledge/notes/input_part009_review.md†L422-L422.
[^firmware-match]: Source: knowledge/notes/input_part012_review.md, line 401.
[^stealth-profile]: Source: knowledge/notes/input_part012_review.md, line 432.
[^hall-tester]: Source: knowledge/notes/input_part012_review.md, line 433.
[^vsett-colors]: Source: knowledge/notes/input_part012_review.md, line 431.
[^ip001-flipsky-unlock]: Source: data/vesc_help_group/text_slices/input_part001.txt†L17515-L17566
[^ip001-nucular-fw]: Source: data/vesc_help_group/text_slices/input_part001.txt†L23984-L23992
[^rosheee_fw]: Source: knowledge/notes/input_part008_review.md†L327-L327
[^izuna_abs]: Source: knowledge/notes/input_part008_review.md†L328-L328
[^flipsky_75350_wiring]: Source: knowledge/notes/input_part008_review.md†L317-L317
[^mixed_can_fw]: Source: knowledge/notes/input_part008_review.md†L352-L354
[^motor_current_scale]: Source: knowledge/notes/input_part008_review.md†L355-L355
[^cl350_drive_share]: Source: knowledge/notes/input_part008_review.md†L417-L417
[^makerbase_disconnect]: Source: knowledge/notes/input_part008_review.md†L446-L447
[^regen_phase_ratio]: Source: knowledge/notes/input_part008_review.md†L447-L448
[^manual_inductance_override]: Source: knowledge/notes/input_part008_review.md†L450-L451
[^kukirin-g2]: Source: knowledge/notes/input_part010_review.md†L469-L471
[^nami-72v-on-60v]: Source: knowledge/notes/input_part010_review.md†L701-L703
[^vesc_tc_torque]: Source: knowledge/notes/input_part011_review.md†L502-L502.
[^abs_ratio]: Source: knowledge/notes/input_part011_review.md†L538-L538.
[^sensorless_launch]: Source: knowledge/notes/input_part011_review.md†L540-L541.
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
[^denis-xiaogen-flow]: Source: knowledge/notes/denis_all_part02_review.md†L910-L910
[^denis-speedboost]: Source: knowledge/notes/denis_all_part02_review.md†L912-L912
[^denis-20s-emu]: Source: knowledge/notes/denis_all_part02_review.md†L917-L917
[^denis-clone-serial]: Source: knowledge/notes/denis_all_part02_review.md†L958-L958
[^denis-xiaogen-uid]: Source: knowledge/notes/denis_all_part02_review.md†L1028-L1028
[^denis-tracecut-warning]: Source: knowledge/notes/denis_all_part02_review.md†L959-L959


## References

[^1]: Source: knowledge/notes/input_part000_review.md†L671-L675
[^sabvoton_kelly]: Source: knowledge/notes/input_part001_review.md†L590-L590
[^ip001-spintendfw]: Source: knowledge/notes/input_part001_review.md†L632-L633
[^2]: Source: knowledge/notes/input_part000_review.md†L304-L304
[^3]: Source: knowledge/notes/input_part000_review.md†L306-L306
[^4]: Source: knowledge/notes/input_part000_review.md†L307-L307
[^5]: Source: knowledge/notes/input_part000_review.md†L708-L716
[^6]: Source: knowledge/notes/input_part000_review.md†L456-L458
[^7]: Source: knowledge/notes/input_part000_review.md†L458-L461
[^8]: Source: knowledge/notes/input_part000_review.md†L514-L518
[^9]: Source: knowledge/notes/input_part000_review.md†L726-L727
[^10]: Source: knowledge/notes/input_part000_review.md†L705-L707
[^11]: Source: knowledge/notes/input_part000_review.md†L688-L690
[^fault_trace]: Source: knowledge/notes/input_part000_review.md†L726-L727
[^fw_jump]: Source: knowledge/notes/input_part000_review.md†L728-L728
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
[^denis-u4]: Source: knowledge/notes/denis_all_part02_review.md†L700-L700
[^denis-controller-hardening]: Source: knowledge/notes/denis_all_part02_review.md†L702-L724
