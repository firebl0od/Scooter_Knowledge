# Controller Setup and Tuning

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

## Current Relationships & Cruise Options

- Artem’s relationship `I_phase = I_batt × V_batt ÷ V_motor` explains why phase torque fades as ERPM rises; expect battery current to climb from ~16 A at launch toward the configured limit as motor voltage increases, and keep phase current above battery current for predictable torque.[^phase_relationship]
- VESC Tool still lacks native cruise control, but Spintend’s handheld remote consolidates throttle, brake, horn, and light lines while offering button-activated cruise and reducing deck wiring; open-source SmartDisplay firmware may add a speed-lock profile later.[^spintend_cruise]

## Firmware Notes

- VESC Tool 6.05 ships with a Lisp demo that converts MP3 files into motor audio, but builders reported severe frame resonance and poor fidelity—treat it as a novelty rather than a production feature.[^vesc_audio_demo]

## Practical Current Heuristics

- Start hub tunes with Artem’s sizing math: phase amps roughly equal to motor wattage ÷ 10 and battery amps ≈ phase × 0.67; if you raise phase current for stronger launches, trim battery current by the same proportion so small stators stay inside their thermal envelope.[^2]
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

## Thermal Management & Regen Safety

- Flipsky’s compact single begins brushing 60 °C on the MOSFETs within 3 km at 50 A battery / 85 A phase, pushing owners to improve heatsink pressure, refresh thermal paste, and add 40 mm fans before experimenting with 100–120 A tunes.[^6]
- Keep battery-side regen at or below the pack’s amp-hour rating (e.g., ≤10 A on a 10 Ah block) and set controller regen roughly 15 A higher so excess energy bleeds off as heat instead of spiking the cells or BMS.[^7]
- Makerbase 84100 riders have yanked live XT60s at speed without killing the controller, but they now cap maximum throttle voltage in VESC Tool instead of adding pull-down resistors—ADC adapters top out around 2.1 V anyway.[^makerbase_disconnect]
- Regen tuning notes from recent 22 S builds keep battery braking near 3 A per cell and phase braking around 70 % of forward phase current, stepping changes gradually and pairing strong regen with a dedicated throttle so brake pads still share the load.[^regen_phase_ratio]
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
