# Scooter Diagnostic Toolkit & Field Practices

## Core Instruments

- **Handheld multimeter:** Expect budget meters to ship with 12 V A23 cells and fragile F200 mA fuses.
  - stock replacements and keep a sturdier backup such as the Mustool MT111 on hand for daily troubleshooting.[^1]
- **Cell testing bench:** Pair LiitoKala or Opus bays with a 3.3 Ω / 25 W Ohmite resistor block so you can discharge or capacity-test loose 18650s before grouping them into packs, especially when customer batteries arrive full.[^2]
- **Firmware lifeline:** ST-Link V2 programmers remain the fastest recovery path for bricked dashboards, ESCs, and Rita-linked BMS boards.
  - clip onto the pads, flash stock firmware, then resume Bluetooth updates once communications return. Modern Ninebot Max dashboards also demand ST-Link access because recent BLE revisions block OTA downgrades, and Mi 3 dashboards that lock themselves “on” after 48 V swaps only recover after flashing stock firmware in XiaoDash, reactivating, and then reapplying the performance profile.[^3][^4][^5][^6][^7]
- **Express flashing workflow:** Smart Repair now flashes VESC Express modules by powering them over USB alone, picking the COM port inside the ESP Programmer panel, and only then reconnecting CAN; if a controller’s USB-C port dies you can still stream live data over CAN/BLE, but configuration changes require a direct USB session to the ESC.[^8]
- **Windows installer caveat:** VESC Tool 6.05 packages still fail to launch on some Windows machines even though the build runs under Ubuntu.
  - ship dependency notes or known workarounds with the binaries so support doesn’t stall at install time.[^9][^10]
- **VESC Express automation tests:** Builders are cloning Spintend’s green board logic with VESC Express plus LispBM.
  - brake lights and CAN-triggered motor braking already work, with latency tuning underway before wider deployment.[^11]
- **Capture the visuals.** The next deliverable asks for screenshot walkthroughs, USB-C failure triage, and CAN-only telemetry expectations.
  - bake them into the guide so riders aren’t guessing how to recover a module that only boots over Wi‑Fi.[^12]
- **Low-voltage logging:** Keep Bluetooth thermometers or CR2032-powered loggers in the spares bin when validating experimental packs so you can capture temperature spikes before they cook cells.[^13]
- **ESC error crib sheet:** Keep Denis’ error table handy.
  - codes such as 28 for HS FET faults speed up post-mod triage before you pull controllers apart.[^14]
- **High-precision GPS.** Dragy’s DRG70 bumps to a 10th-gen u-blox receiver with tighter accuracy but its magnetic mount won’t grab anodised aluminium stems.
  - budget steel inserts or adhesive plates before track days and consider 3D-printed steel-backed clamps for VSETT stems.[^15][^16]
- **VESC Bridge V2.** The refreshed Segway/Ninebot bridge is slated to ship with OTA firmware, plug-and-play GT1/GT2/G30 harnesses (hall/phase aside), anti-theft lockouts, per-motor torque biasing, adjustable regen ceilings, PowerNine lighting modes, and roadmap support for JK/JBD/ANT/Daly BMS telemetry.
  - stage wiring now so the module drops in once released.[^17]
- **AC milliohm meter:** Industry-standard 1 kHz testers like the YR1035+ expose weak cells quickly even if readings differ from DC load checks.
  - ideal for sorting cells before pack assembly.[^18]
- **LCR-T4 component tester:** Handy for confirming MOSFETs, caps, and diodes on suspect VESC boards when DC readings look off.
  - builders caught 1–2 V voltage-sense drift and shorted drivers before reinstalling hardware.[^19]
- **PlatformIO build environment:** The aging VescUart Arduino libraries compile reliably under PlatformIO (Nano/Pro Mini profiles); the stock Arduino IDE often misses dependencies for custom dashboards. Use the PlatformIO quick-start from the VESC telemetry display project to clone configs, flash boards, and share binaries quickly.[^20][^21]
- **DIY dashboard replicas:** NeatDash-style boards work only when the published resistor (120–150 Ω) and diode orientation are followed; clone BLE controllers still refuse to talk reliably, so shops are preparing ESP32/OLED replacements once Mirono and NVRAM publish open-source hardware.[^22]
- **VESC Tool mobile update workflow:** Back up motor/app XMLs before flashing in the Android/iOS app, use the in-app firmware flasher while the pack is connected, and sideload older APKs if 6.0+ releases hide configuration menus.
  - the crew now keeps a rollback archive specifically for field recoveries.[^23]
- **Use the mobile app for live ADC checks.** VESC Tool’s smartphone build still exposes RT data and ADC mapping panels.
  - connect over TCP, Wi-Fi, or USB to watch throttle and brake voltages without digging through hidden menus.[^24]
- **Insulation & adhesive supplies:** Stock RTV silicone, Kapton, and zip ties to strain-relieve DC/DC converters and harnesses; vibration snaps converter leads unless they are glued or tied back to the PCB before the scooter ever rolls.[^25]
- **Instant translation:** Plus Messenger’s built-in translator lets techs follow Spanish- and French-language repair chats without copy-paste gymnastics.
  - handy when sourcing parts from multinational groups.[^26]
- **Dedicated GPS logger:** Relive overstates peak speed by ~7 km/h when GPS drops, so shops now run Speed View GPS Pro for floating dashboards, exportable logs, and reliable range data alongside VESC telemetry.[^27][^28]
- **Retire sketchy refurbished chargers.** A “Meanwell” fast charger with loose add-on circuitry and cold solder joints tripped RCDs and died outright.
  - budget for genuine 22 S-capable supplies even if they cost €200+ rather than gambling on rebuilds.[^29]
- **Background-safe VESC logging:** Field tests confirmed VESC Tool keeps writing logs while the Android app sits in the background, letting technicians foreground GPS overlays or camera apps during top-speed runs without losing controller data; just reconnect afterward to pull the files.[^30]
- **Quarter-inch impact driver discipline:** Keep 1/4" hex impacts for gentle screw spinning with impact-rated sockets and a light trigger; avoid split-rim bolts, tapping threads, or hammering hardware you care about because the percussion shatters taps and fasteners.[^31]
- **CAN-to-BLE bridge:** K3BAB’s €20 VESC-Express (ESP32-S3) module drops onto the CAN bus, bridges BLE/Wi‑Fi, and can drive LEDs or BLE remotes.
  - carry one for telemetry upgrades when legacy SPP dongles keep dropping.[^32]

## Wiring & Harness Checks

1. **Start at the XT30:** After any crash or curb strike, verify the adapter output voltage before chasing other faults; browned phase pins or half-seated BMS harnesses are the most common culprits when scooters power-cycle on bumps.[^33]
2. **Inspect pack protection:** Cheap “25 A” eBay BMS boards routinely trip around 18 A despite balanced cell groups.
  - swap in reputable 20–30 A hardware before blaming Rita or the controller for brownouts.[^34]
3. **Match radio gear:** Immobiliser and alarm kits ship in multiple frequencies; confirm your remote (315 MHz vs. 415 MHz) before hard-wiring to the scooter’s 5 V accessory tap so the system actually arms.[^35]
4. **Treat locks as consumables:** Light cable locks such as compact Master Lock loops work for coffee stops only if they stay lubricated with graphite.
  - dry mechanisms jam quickly after rain or grit exposure.[^36]
5. **Identify controller silicon before flashing.** New Xiaomi ESCs use GD32 MCUs; flashing STM firmware bricks them, so zoom in on chip markings and grab the GD image set before running ST-Link recoveries.[^37]
6. **Secure accessory power taps.** Dashboards only expose 5 V logic.
  - drive headlights and horns from a dedicated DC/DC converter, tie the output wires to the board with RTV, and route the harness away from moving stems so the leads do not fatigue.[^38][^25]
6. **Respect Spintend accessory rails.** The built-in 12 V/3 A rail is fine for a brake light, but running both Dualtron head and tail lights from it has already tripped installs.
  - budget external bucks when the load climbs beyond a single lamp.[^39]
7. **Reflow noisy balance taps.** JK smart boards throw alternating “short circuit” and “low voltage” alarms when a single balance lead lifts.
  - re-solder any suspect tap before blaming firmware or swapping the BMS.[^40][^41]
7. **Trace weak 5 V accessory ports back to the buck converter.** A Max G30 plug that still shows 5 V but no current usually means a failed converter stage.
  - follow the trace with a multimeter until you reach the DC/DC module and verify components between it and the port before ordering a replacement board.[^42]
8. **Refinish soldered connectors, don’t patch corroded XT60s.** R3VOLT’s refresh reminded the crew to swap oxidised housings entirely, heat the bullet.
  - not the wire
  - so solder flows, and slide the molded cover back over the last few millimetres before heat-shrinking insulation to prevent shorts.[^43]
9. **Use drilling jigs when precision holes matter.** Off-the-shelf square-hole guides keep controller and bracket installs tidy for builders who struggle to drill straight freehand.[^44]

- **Step drills for control hardware.** Enlarging round switch holes stays cleanest with step bits, while rectangular cut-outs still need files or nibblers; finish with a hand ratchet on axle nuts to feel clamp load instead of hammering them with an impact.[^45]
- **Throttle extensions hold up.** Two-metre throttle runs on quality silicone cable have stayed noise-free, so shielded loom is optional for most scooters.[^46]
- **Parallel smaller leads when space is tight.** Doubling up 12 AWG silicone wire handled ~80 A battery current on GABE’s compact pack, making parallel runs a workable compromise when harness routing is constrained.[^47]
- **Inspect anti-spark connectors periodically.** Noname spotted the precharge strip inside an XT90S-style plug browning after repeated use.
  - retire housings that show discoloration or heat damage before they melt during high-current launches.[^48]
10. **Prefer controlled hand crimpers for JST signal pins.** Manual “non-ratcheting” tools let you feel the conductor and insulation wings seat properly.
  - ratcheting jaws kept crushing insulation and hiding bad contacts on MP2/75100 harnesses until the team switched tools.[^49]
11. **Match connector families on MakerX harnesses.** The 75100 V2 signal looms use JST-PH (2.0 mm) shells rather than larger JST-XH housings.
  - order the right housings and dies before recrimping.[^50]
10. **Add abrasion armor to oversized leads.** 6 mm² cable upgrades can tear PTFE insulation as they pass through motor axles.
  - wrap them in abrasion-resistant sleeving or PTFE-lined braid before reassembly so the insulation survives vibration and axle edges.[^51]
11. **Upsize motor leads thoughtfully.** 🇪🇸AYO#74 recommends AWG 11 silicone for hot climates because AWG 10 rarely fits through scooter axles, and Paolo reminded everyone that “AWG” is just a gauge label.
  - call out conductor material (tinned copper vs. PVC) in shopping lists so replacements actually fit.[^52]

## Controller & Motor Tests

- Hall sensor PCBs vary by scooter.
  - spacing, voltage, and middle-sensor types change
  - so don’t expect universal replacements when diagnosing dead Reid/Boost motors or throttle faults.[^53]
- **Continuity sweep before power-up:** With the battery unplugged, probe between B+ / B− and each motor phase. Any reading below ~50 Ω signals a shorted MOSFET that must be replaced before reconnecting cells.[^54]
- **Start with the low-voltage rails on “dead” VESCs.** Before condemning a no-power controller, check every LDO regulator and supply rail with a meter; technicians now solder test pigtails or use current-limited supplies so a slipped probe does not vaporise PCB traces during the investigation.[^ldo_probe]
- **Meter controller rails before blaming accessories.** Ubox V2 troubleshooting now starts with the 12 V rail.
  - if it sags or reads open, chase the controller before condemning lights or pumps.[^55]
- **Check CAN bus levels with a meter, not assumptions.** Healthy ANT/JK CAN pairs sit around a 3.3 V differential between CAN_H and CAN_L.
  - readings in the teens usually mean the multimeter reference is wrong, not that the bus is out of spec.[^56]
7. **Don’t blame regen for dim lights.** KERS-fed current won’t hurt a 36–40 V headlight tied to an external pack, but a failing “purple” dashboard can sag throttle voltage whenever the lights are on, capping speed until the dash is replaced.
  - meter the dash before chasing wiring ghosts.[^57]
8. **Reflow noisy balance taps.** JK smart boards throw alternating “short circuit” and “low voltage” alarms when a single balance lead lifts.
  - re-solder any suspect tap before blaming firmware or swapping the BMS.[^40][^41]
9. **Trace weak 5 V accessory ports back to the buck converter.** A Max G30 plug that still shows 5 V but no current usually means a failed converter stage.
  - follow the trace with a multimeter until you reach the DC/DC module and verify components between it and the port before ordering a replacement board.[^42]
10. **Refinish soldered connectors, don’t patch corroded XT60s.** R3VOLT’s refresh reminded the crew to swap oxidised housings entirely, heat the bullet.
  - not the wire
  - so solder flows, and slide the molded cover back over the last few millimetres before heat-shrinking insulation to prevent shorts.[^43]
11. **Use drilling jigs when precision holes matter.** Off-the-shelf square-hole guides keep controller and bracket installs tidy for builders who struggle to drill straight freehand.[^44]

- **Diagnose dead scooters at the controller first.** A dark ESC status LED means the dashboard button isn’t the culprit.
  - it merely bridges ground to signal
  - so trace the controller’s power rails, inspect coil drops, and probe each regulator stage before blaming the dash.[^58]
- **Interpreting error 28 after water ingress:** Persistent MOSFET beeps usually trace to a shorted high-side bridge.
  - if the wheel lived through repeated wet/dry cycles and now shows pink moisture stickers or white corrosion, swap the controller instead of chasing intermittent faults.[^59]
- **Power-cycling dashboards:** Erratic battery percentages or random resets often point to oxidation hiding under the white battery plug; pull the connector, flush with contact cleaner, dry thoroughly, and assume the stock IP54 gasket is decorative if the scooter sees floods or heavy rain.[^60]
- **Stop auto-boot loops by cleaning the dash.** Mi 3 dashboards that stay “on” after 48 V swaps usually have water-contaminated buttons.
  - scrub the board with 99 % isopropanol, dry thoroughly, and avoid folding wet stems so moisture doesn’t pool around the electronics.[^61]
- **Front-burnout postmortem workflow:** If a VESC dies mid-burnout, meter the QS8 battery connector and each phase to ground in buzzer mode.
  - any tone confirms shorted MOSFETs. Verify the hub still spins freely to rule out a seized motor, then plan a matched-set MOSFET swap using proper hot-air or hot-plate gear; aluminum boards are notoriously hard to rework and you cannot mix spare FETs across controllers. Keep mechanical brakes functional because regen-only setups leave you helpless when the controller faults.[^62]
- **Cycle temp presets before condemning sensors.** NetworkDir clears bogus VESC temperature telemetry by stepping through the 10 kΩ NTC, 1 kΩ PTC, and 100 kΩ NTC presets.
  - if readings stay wrong after the sweep, chase wiring faults before blaming hardware.[^63]
- **Hall sensor alignment:** Preserve the original spacing when replacing hall ICs.
  - swapping long packages for short ones costs roughly 10 km/h, and forgetting isolation pads risks shorting MOSFETs to the case.[^64]
- **120° hall boards swap freely when wired correctly.** Halo builders chasing front-motor faults confirmed any 120° sensor plate works on VESC hardware as long as the phase/hall order matches the controller harness.[^65]
- **CAN networks scale past dual-drive.** VESC Tool comfortably runs at least four controllers from a single throttle (one parent plus three children), so document IDs and wiring carefully before expanding into kart or fan-drive experiments.[^66]
- **Warm-motor hall detection:** If a scooter clonks off the line, rerun manual hall detection with the motor warm and phase current around 70 A.
  - Mirono’s G30 build stopped stuttering immediately after re-detecting on a full battery.[^67]
- **Clean contaminated mid-drives methodically.** Blow debris out with compressed air first, then spot-clean windings and PCBs with brake cleaner or isopropyl on lint-free cloths.
  - avoid microfiber that sheds fibres and be gentle around magnet glue and adhesives.[^68]
- **Sensorless sanity check:** When tuning sensorless profiles, unplug the hall harness and rerun detection to avoid mixed inputs.
  - builders chasing intermittent faults cleared them the moment the halls were removed during detection.[^69]
- **Graph phase current for MOSFET health.** VESC Tool’s phase-current traces flag dead drivers immediately.
  - a blown DRV forced one controller into noisy BLDC-only operation and shut down above ~10 % throttle until the failed MOSFETs were replaced.[^70]
- **Keep Vedder’s `code_server` for CAN telemetry.** It automatically retries failed frames five times and stays more reliable than legacy scripts as long as firmware is current; just remember to swap RX/TX when moving Makerbase/Flipsky looms to Spintend/UBOX controllers and flash `slave_esc.lisp` on every CAN slave before logging.[^71][^code-server]
- **Motor-detection MOSFET triage.** When detection pops FETs, pause and meter gate drivers, confirm phase-filter components, and rerun detection with conservative parameters before applying power again; the crew now treats this flowchart as mandatory after every detection fault.[^motor_detect_flow]
- **Keep Vedder’s `code_server` for CAN telemetry.** Riders still trust it over legacy scripts so long as firmware stays current and they capture logs during faults for later review.[^71]
- **Quick hall re-detection:** 🇪🇸AYO#74 confirmed you can rerun hall detection without a full motor calibration, but remember to disable the VESC Tool hand-test once inputs check out or throttle/brake channels stay latched in test mode.[^72]
- **SmartESC UI caveat:** NetworkDir reminded riders that Xiaomi SmartESC firmware only mimics the VESC Tool interface.
  - it does not run VESC code
  - so treat its readouts as cosmetic and keep real tuning in VESC Tool.[^73]
- **Tame vibration by re-detecting inductance.** 🇪🇸AYO#74 cured a persistent shudder by trimming detected inductance from ~22.5 µH to 16–17 µH, re-running VSS sensorless tuning, and restoring settings from the VESC mobile app’s onboard backups.
  - useful for iPhone users without laptops on hand.[^74]
- **Chase vibrations methodically:** When Yamal reported front-motor scraping, 🇪🇸AYO#74 first checked the dash swap (Ortega vs. stock) and ultimately found a vibrating phone mount.
  - rule out accessories before tearing hubs apart.[^75]
- **DRV fault symptoms:** Loud BLDC-only operation that vanishes after recalibrating FOC points to a past DRV overcurrent, whereas persistent noise after recalibration usually means the DRV chip is dead.
  - treat the symptom set as a hardware tell before reflashing endlessly.[^76]
- **Finish Makerbase wizard runs on a PC.** Android app wizards hide throttle/brake assignments; the group now saves configs in desktop VESC Tool, resolves 75_300_R2 hardware-ID mismatches, and flashes Izuna’s firmware for accurate 75100 voltage readings once the controller enumerates correctly.[^77]
- **Verify magnet strength with a Gauss meter.** Rewound hub projects now include handheld Gauss checks after re-magnetising stators so you can confirm field strength before sealing the motor.[^78]
- **Log the Flipsky blue-LED unbrick steps.** One 75100 stayed locked on a blue LED despite ST-Link attempts.
  - document the SWD recovery workflow so the next repair isn’t a fresh science project.[^79]
- **Read before writing over CAN.** When tuning ADC or throttle settings through a master controller, hit `Read` first so VESC Tool doesn’t clone the same ID across both nodes and strand the CAN bus.[^80]
- **Set wheel data on every controller.** Enter wheel diameter, pole count, and gear ratio on both VESCs so paired dashboards report the same speed during bench tests.[^81]
- **Pull CAN jumpers while changing IDs.** Remove termination jumpers when reassigning addresses; leaving them connected lets both controllers grab the same ID and appear “dead.”[^82]
- **Wire CAN before applying power.** Plug the CAN harness in before energising the controllers.
  - booting them first left Shlomo’s pair invisible until the link was connected and IDs were resynced.[^83]
- **ABS over-current noise sometimes just needs a higher ceiling.** Alex cleared repeated ABS warnings by raising the Max ABS Current in VESC Tool.
  - log regen-heavy tunes before swapping hardware.[^84]
- **Rerun detection if resistance numbers look wrong.** A Zero 10X hub that overheated on modest 30 A battery / 70 A phase / 20 A FW tunes reported 172 mΩ instead of the normal ~40 mΩ.
  - rerun detection on trusted hardware before drilling cooling holes.[^85][^86]
- **Hall vs. sensorless triage.** Anthony’s “Bad FOC Hall detection” on dual Flipsky 75100s traced back to a failed hall sensor; the crew leaned on sensorless HFI (Ortega observer, medium inrunner preset) as a stopgap up to ~6 kW/60 km/h.
  - add that workflow to quick-starts so riders can limp home while sourcing hall boards.[^87][^88]
- **Regression-test VESC Tool 6.06 detection.** Basti’s hardware-no-limit controller throws motor-detection errors on 6.06, so keep legacy configs handy and validate new wizard releases before rolling them to customer builds.[^89]
- **MakerBase latch inversion.** One 84100HP shipped with reversed key-switch logic; the toggle closed opposite the desired direction and rewiring didn’t help.
  - document latching workflows or firmware overrides before final assembly.[^90]
- **MP2 voltage scaling audit.** Patrick’s MP2 v0.6 build reports incorrect pack voltage even after firmware reflash and short checks.
  - log ADC divider values and known errata before green-lighting rides.[^91]
- **Watch boot-time throttle spikes.** Mirono caught a hall throttle jumping to ~2 V only during VESC boot; inspect filtering and shielding around ADC1 before blaming firmware.[^92]
- **Wheelway sensor QA:** Replacement Wheelway boards keep shipping with mismatched SS41/SS43 halls; bench-test each sensor at 5 V before sealing the hub and keep a sensorless profile ready in case the new board desyncs within the first 20 km.[^93][^94]
- **Isolate mixed-brand CAN issues.** MakerBase and Flipsky clones rarely share a healthy CAN bus.
  - swap to known-good JST-PH/XHB harnesses and log each controller independently before condemning hardware.[^95][^96]
- **Isolate flaky hall looms.** A Trampa MK6 that rebooted on throttle stopped crashing the moment the hall loom was unplugged.
  - rerun diagnostics sensorless to confirm the loom or PCB is shorting before replacing the controller.[^97]
- **Compare controller hall reports on dual drives.** A mismatched hall sensor left one controller detecting 160 A motor current while the mate read 144 A, upsetting traction until the weak sensor was replaced.
  - verify both controllers report identical idle and detection values before blaming firmware math.[^98]
- **Short phases to count magnets.** When you need the magnet count without cracking the hub, short any two phases together and spin the wheel.
  - the number of detents equals the magnet tally for VESC Tool setup.[^99]
- **ADC overrides block bench tests.** Enabling ADC control stops manual FWD/REV overrides in VESC Tool; switch the control app to UART or disable ADC when you need to spin motors on the stand.[^100]
- **Chase hall loom faults before phases.** Burned or waterlogged hall harnesses can mimic loose phase leads.
  - try sensorless mode or rewire halls before assuming a shorted phase stack.[^101]
- **Sensorless launches still need momentum.** Hall-less 75100 builds require a push start for zero-speed torque, and smoothness varies by motor.
  - keep at least one hall-equipped axle in dual setups for reliable takeoffs.[^102]
- **Check for missing phases.** If the scooter brakes when you blip the throttle and only creeps at 20 A, inspect every phase lead and hall orientation.
  - one loose phase on a Wheelway build created identical symptoms until the harness was reseated.[^103]
- **Kelly KLS quirks.** Expect USB drivers to fail on modern Windows; plan on the BLE module or legacy Windows XP tools when configuring scooters running KLS hardware.[^104]
- **Phase-current ceilings as diagnostics.** Dual Spintend riders treat 120–130 A phase per motor (≈160 A ABS) as normal; stuttering above ~85 A points to blown MOSFETs or loose phase leads, so log traces and rerun hall/sensorless tests before simply dropping current limits.[^105]
- **3Shul ABS fixes need manual detection.** CL350 V4 owners cleared ABS overcurrent faults by rerunning detection with a 500 µs timing step, switching from `mxlemming` to the Ortega observer, and dialing the tune in manually per Vedder’s demos.[^106]
- **Data-line triage after regen faults:** Error 21 that appears immediately after an emergency stop usually points to a cooked controller data line. Bench-test the pack on a known-good scooter or send it in rather than reflashing firmware blindly.[^107]
- **Backfeed with care:** A depleted 44 V pack can be nudged awake with a 36 V charger only when its open-circuit voltage sits under ~41 V. Anything higher risks over-voltage damage once the charger’s CV phase kicks in.[^54]
- **Log Rita/Happy current spikes:** Error 39 beeps and thermal cutbacks appear when firmware demands exceed Rita’s ~30 A ceiling; capture live amps with m365Tools before dialing tuning back.[^108]
- **Replace scorched hubs outright.** A motor that screeched after 33 A hill climbs revealed melted slot insulation.
  - techs recommended swapping to hall-sensored Blade 10/Vsett 10+ hubs because sensorless replacements like Vsett 11+ won’t run on stock Xiaomi controllers without added halls.[^109]
- **Calibrate controller voltage sensors.** Spintend Ubox reports have skewed low by ~3 V until owners compared readings against trusted multimeters (e.g., UNI-T UT123C) and adjusted ADC scaling after new installs.[^110]
- **Seal vulnerable USB-C cutouts.** Water intrusion through exposed controller USB-C ports has already spoofed temperature telemetry; relocate the connector internally and silicone the original opening before returning the scooter to service.[^111]
- **Reflash controllers after ABS-trigger resets.** Patrick’s Makerbase build only stopped rebooting after he backed up settings, wiped firmware, and performed a clean flash instead of tweaking values in place.
  - budget time for full reflashes when ABS overcurrent faults persist.[^112][^113]
- **PAS scripts can brick motion until configs reload.** Mirono’s pedal-assist Lisp locks the motor after high-phase pulls on a Flipsky 75100 V2; lower phase amps or add ceramic-cap filtering before shipping similar scripts to customers.[^114]

## Performance Logging & Calibration

- **Acceleration tests:** Use Dragy or Race Timer to record repeated 0–70 km/h pulls, filming the dash at 60 fps and averaging matching-direction runs so GPS lag doesn’t skew results.[^115]
- **Export pack sag logs:** Pull CSV/XLS files from VESC Tool after hill climbs or heavy regen sessions so you can quantify voltage drop before raising current limits or rewiring parallel packs.[^116]
- **Benchmark sprint claims with Dragy.** The group still treats Dragy GPS modules as the trusted reference when validating AWD launches or top-speed runs, so capture their CAN-aligned logs before publishing numbers.[^117]
- **Cross-check GPS overlays.** One 200 A test logged a 7 km discrepancy between a phone overlay and the VESC dash; export the VESC log as the ground truth whenever overlays disagree to avoid publishing inflated speed claims.[^118]
- **Child-friendly profiles:** Use VESC Tool’s Profiles tab to scale Max Current down (≈60 % cuts one rider’s scooter to ~5 mph) while keeping smooth launches for training sessions.[^119]
- **Speedometer alignment:** Measure wheel circumference under rider load, set accurate pole counts, and bias VESC telemetry slightly above GPS speed so commuters get an early warning before hitting legal caps.[^120]
- **Mantis circumference baseline:** Builders running 10″ Mantis hubs log VESC Tool wheel circumference around 253–254 mm, with 254 mm reading 3–5 km/h high.
  - handy for quick GPS cross-checks.[^121]
- **Keep traction-control data honest.** NetworkDir recommends enabling traction control.
  - or at least matching pole, gear, and tyre values across CAN nodes
  - so slipping front wheels don’t inflate dash speed beyond GPS reality.[^122]
- **Cross-check GPS logs:** 🇪🇸AYO#74’s ~140 km/h Nami runs highlighted how GoPro GPS can fail in tunnels.
  - export Relive.cc or similar telemetry to validate hyper-scooter data and benchmark other builds like Face de Pin Sucé’s 22 S9 P Samsung 50S / LY 75H log.[^123]
- **Re-measure wheel OD after tire swaps:** Correcting diameter from 271 mm to 279.4 mm tightened 🇪🇸AYO#74’s speed telemetry, proving a few millimetres of drift can skew GPS/odometer comparisons.[^124]
- **Magnet count discipline:** Enter the actual magnet count (not pole pairs) and the compressed tyre diameter in VESC Tool.
  - GPS traces lag too much for launch tuning compared with controller RPM telemetry.[^125]
- **Validate pole counts after repairs.** A mis-set 30-pole value made NetworkDir’s GT2RS display 165 km/h when GPS confirmed ~120 km/h on 40-pole hubs.
  - double-check counts before bragging about top speed.[^126]
- **Confirm hub windings with proper instrumentation.** LY motors often share castings.
  - either open the stator or measure phase resistance with a four-wire milliohm meter such as the YR1035+; a genuine 75 H 22×3 is unlikely to top 120 km/h without heavy FW, which helps sanity-check “33×2” shipments.[^127]
- **Log during tests:** VESCs only store faults while a client is connected; keep xmatic or VESC Tool running on shakedowns so overcurrent or BMS events are captured before power-cycling.[^128]
- **Pair dashboards with matching firmware.** Dual-VESC conversions on G30 or Mantis frames share one dash over CAN; mixing a stock G30 controller with a lone VESC stays “the jankiest” fix until you flash community firmware on both units so VESC Tool recognises them cleanly.[^129]
- **Characterise shunt mods with a bench supply.** Paolo walks builders through feeding the controller from a current-limited bench supply, measuring millivolt drop across the shunt, and using Ohm’s law instead of trusting hobby meters when recalculating resistance.[^130]
- **Tame Android TCP dropouts.** Pixel owners keep VESC Tool’s TCP bridge alive by disabling battery optimisation, allowing unrestricted background use, or pairing third-party screen-off utilities so the phone doesn’t kill the session mid-log.[^131]

## Field Recovery Tricks

- **Wake sleeping packs:** Happy BMS batteries ship dormant.
  - tap them with a charger to enable the discharge MOSFETs before chasing wiring faults.[^132]
- **Revive latched Happy BMS boards.** After reconnecting a pack, some Happy BMS units keep discharge off until they see the charger.
  - expect to “tickle” the pack briefly before the controller wakes.[^133]
- **Reconnect stubborn externals:** If Rita “ghosts” an auxiliary pack, blip the throttle for a second to force rediscovery before tearing down wiring.[^134]
- **Let Kaabo CAN bridges sleep.** A Kaabo King GT’s legacy 100 V/100 A bridge revived CAN comms after sitting unpowered overnight.
  - sometimes patience beats a full tear-down when chasing phantom bus faults.[^135]
- **Time full charges when vetting replacements:** Stock Xiaomi bricks add ≈1.7 Ah per hour; a legitimate 12 Ah Pro 2 pack should need nearly seven hours from empty, so a “full” light in 90 minutes signals a counterfeit pack.[^136]
- **Restore serials after bad flashes.** ScooterHacking or XiaoDash updates that wipe the serial/odometer recover quickly by writing the ID back with DownG; only reach for ST-Link if you truly need to reinstate lifetime mileage counters.[^137]
- **Probe every series group on dead packs:** When a fresh build refuses to wake, crack the wrap and meter each group.
  - bypassing the BMS is for testing only because running without it is a fire risk.[^138]
- **Tighten loose bullet plugs without damage.** Medhi wedges a sliver of hard plastic into the female bullet to flare the contact gently, restoring grip without gouging the connector bore.[^139]
- **Go sensorless when halls fail.** If a Zero or similar scooter loses hall sensors mid-ride, drop open-loop ERPM to 0, switch to the Mxlemming observer with BEMF decoupling, and limp home on sensorless starts.[^140]
- **Go sensorless when halls fail.** If a Zero or similar scooter loses hall sensors mid-ride, drop open-loop ERPM to 0, switch to the Mxlemming observer with BEMF decoupling, and limp home on sensorless starts; the same approach rescued a loom-burned build once halls were suspect and kept a G30 rider mobile after a severed hall lead.[^140][^101][^141]
- **Recover CAN chains through the survivor.** Change the remaining controller’s VESC ID and reflash the bootloader over the intact CAN link to revive dead peers before opening sealed housings.[^142]
- **Reseat BMS harnesses before condemning packs.** Noname’s Vsett 11+ “dead” pack woke up after unplugging and re-seating the multi-pin BMS connector.
  - add the check before ordering replacement batteries.[^143]
- **Capture PAS-script bugs.** Mirono’s Flipsky 75100 V2 runs fine until the PAS Lisp script pauses at high phase current.
  - after that the motor only vibrates until the config is rewritten, pointing to an observer or firmware edge case that needs reproducible logs.[^144]
- **Clear stuck Spintend BLE pairings via USB.** If a module gets marked “paired” in error, plug in over USB, clear the flag, and reboot; Smart Repair confirmed the recovery works even after field misconfigurations.[^145][^146]

## Connectivity & Firmware Utilities

- Pair an ESP32-C3 with a CAN daughterboard running VESC Express when you need Wi-Fi, Bluetooth, logging, and GPS without relying on ageing NRF dongles.[^147]
- Salvaged Segway G30 dashboards flashed with VESC NRF firmware work as low-cost wireless bridges for fresh builds.
  - keep donor boards on hand for budget diagnostics.[^148]
- Ofek’s “kick start” script disables motor output below a set speed (~1 m/s by default), giving commuters a push-to-start safety layer when throttle-only launches are risky.[^149]

## Chassis & Suspension Quick Fixes

- **Rebuild sloppy folding clamps:** Shim ovalized bushings with thin metal or heat-shrink and lock every fastener with threadlocker so the top plate stops wallowing out mid-ride.[^150]
- **Silence Vsett 10+ hub clunks:** Loud knocks between braking and throttle almost always trace to loose axles or missing hub washers after bearing swaps.
  - retorque hardware and add proper torque washers/arms before chasing controller faults.[^151]
- **Replace washer stacks with bushings.** Jamaludin’s refreshed Nami rode quieter and braked cleaner after swapping improvised washer stacks for machined bushings, rechecking cable routing, and realigning calipers before delivery.[^152]
- **Inspect early Nami frames for cracks.** Spain’s community contrasted first-gen weld failures with reinforced 72/40 updates.
  - use their photos as a checklist before buying used frames.[^153]
- **Tune cheap steering dampers:** Swap generic damper fluid for 10W/60 shock oil or Citroën LHM+ to regain adjustability without chewing seals, especially on freebie take-offs.[^damper-oil]
- **Favor suspended frames for high-power conversions:** Ninebot Max G2 chassis with suspension outlast rigid G30 decks under vibration, SNSC rental frames survive high-speed crashes with minimal damage, and DNM shock/13"×7" tire combos plus lever-free hub tire removals keep service visits efficient.[^154]

## Hardware & Fastener Rescue

- **Free rounded Thunder hardware.** Cut a slot with a Dremel or rotary tool, hammer in an oversized flat-head (“Thor head”) bit, or heat the screw to break the Loctite before extraction.
  - these tricks keep swingarms and deck plates serviceable without drilling the frame.[^155]
- **Confirm motor orientation before detection.** Unplugging phases for service doesn’t require a fresh motor detection.
  - miswired phases simply spin backwards, so fix wiring before rerunning the wizard.[^156]
- **Flip Segway’s “new motor” flag after swaps.** Color-matching G30 phase leads still works across model years, but newer firmware won’t spin until you toggle the new-motor flag.
  - note it in your service checklist.[^157]
- **Lean on Ortega observers for stuttering launches.** 75 200 builds that lock under hard throttle smooth out once the Ortega observer replaces mxlemming.
  - note it as the go-to fix before chasing hardware faults.[^158]
- **Reset CAN IDs before assuming transceiver failure.** If dual stacks refuse to sync, change CAN IDs in VESC Tool and reboot both controllers.
  - Figiwara’s crew fixes most “dead” pairs this way before opening the hardware.[^159]

## Deck Swaps & Packaging Checks

- **Thunder deck on Victor frames.** Skrtt transplanted a Thunder deck box onto a Dualtron Victor for extra battery room; the Victor mounts share the Thunder’s 7.5 cm spacing and cost roughly €200, avoiding custom machining.[^160]
- **Plan swingarm upgrades for 11" hubs.** Thunder swingarms remain the go-to for squeezing 70 H or 11" motors onto Victors, while builders can run 11" tires first if they grind minor fork contact points and seat axles at the dropout tips for clearance checks.[^161]
- **Order GT rims without new hubs.** Skrtt confirmed AliExpress “rim only” listings fit worn GT-series motors, but inspect the hub carefully before reusing magnets and halls.[^162]
- **Stock axle hardware.** Konyk conversion kits still include matching axle nuts, simplifying rear motor swaps when OEM hardware is discontinued.
  - add spares to the field kit.[^163]

## Tire & Traction Observations

- **Stock alternatives to PMT slicks.** Xeuancheng and ULIP 11″ tires work as PMT stand-ins when shipping falters.
  - expect minor brake-mount trimming on some frames and grab extras when discounts pop up.[^164]
- **NAMI track pace sans FW.** Dialed geometry and sticky rubber already push Nami builds near 100 km/h without field weakening.
  - treat FW as optional headroom, not a crutch.[^165]
- **Burnouts destroy budget slicks.** Continuous burnouts in 48 °C heat shredded “snake” tread street tires, nudging riders back to PMT Juniors or at least frequent rotations before cords appear.[^166]
- **Prep beads before sealing.** Slow leaks and reseat headaches traced back to leftover mold flash and embedded debris.
  - scuff beads clean and inspect carcasses before final inflation.[^167]
- **Skid-test 90/65-6.5 clones before trusting them.** Veterans force a burnout: nylon clones squeal loudly while real rubber heats up and feels sticky.
  - reject any tire that fails the test before high-speed runs.[^168]
- **6.5" sourcing is inconsistent.** Options range from questionable PMT “Stardale” clones to TOUVT 100/55-6.5 casings, while Xuancheng PMTs remain the favourite despite recent 50 % price hikes on AliExpress.
  - stock extras when prices dip.[^169]
- **Use quality sealant first.** Muc-Off tubeless formula handles most slow leaks via the valve core; stubborn punctures still need tubes or patches after inspecting the carcass for debris.[^170]
- **Patches outlast multi-plug repairs.** Matthew prefers internal patches for longevity, though Noname notes multi-plug off-road fixes can hold for years; everyone agrees to scuff the casing and let cement tack before bonding.[^171]
- **Burnout smoke depends on build.** Tread compound, wheel speed, and chassis weight dictate smoke output.
  - lighter 6.5" builds shed less rubber than heavy Weped-style setups unless using gimmick “gender reveal” compounds.[^172]
- **Treat valve cores as consumables.** Tubeless conversions keep spares on hand because damaged cores or rushed cement work reopen leaks until replaced and fully cured.[^173]
- **Balance electronics with mechanics:** Traction control helps rein front-wheel slip up to ~55 mph, but riders still cut front phase amps to keep dual-drive scooters manageable in launches.[^174]
- **Match tires to power levels:** Xuancheng 12" slicks stay budget-friendly but spin under hard launches, so high-power builds migrate to CST or PMT rubber; on 6" rims, Tuovt 90/55-6 casings grip better than CST 90/65-6 while oversized 6.5" skins pinch split rims and look sloppy.[^175]
- **Pick tires for the surface, not hype:** Riders are steering 10" Zero/Vsett owners toward CST 10×3 or PMT 10×3.5 rubber, calling Xuancheng slicks short-lived above 4 kW without traction control, and leaning on Tuovt 90/55-6 for broken pavement longevity.[^176]
- **Address pinch flats proactively:** Vsett 9 owners fighting split-rim pinch flats now double heavy-duty Ulip tubes, dust them with baby powder during install, and experiment with 3D-printed bead covers to protect the tube crease.[^177]
- **Seat beads aggressively on 10″ tires:** Ratchet straps, lubricant, and >100 psi blasts are often required to pop stubborn beads; cheap molds can still leave paper-thin gaps that need repeated cycles to seal.[^178]
- **Tubeless vs. tubes remains situational:** Tubeless with sealant pays off on long routes, but some riders still slip tubes into tubeless rims for roadside convenience despite the added heat load.[^179]
- **Source tires regionally but plan spares.** ULIP 90/60‑6 clones remain the affordable standby when PMT Juniors hit ~€130 locally, yet riders still prefer PMT grip when shipping behaves.
  - stock extras before the next shortage.[^180]
- **Budget for CNC rims and wider axles.** Ambrosini/LY 6.5" rims still land around €100–€120 each and expect 155 mm+ axles plus chunky AWG 7–8 phase sleeves.
  - verify spacing before ordering batches.[^181]
- **Tune pressures to the compound.** Shlomozero still skids the front at 30 psi even with 220 A phase, while French racers drop PMTs to ~14 psi for turn-in grip.
  - log pressures with each tire swap.[^182]
- **Baby powder plus Ulip tubes works for commuters.** Noname logged only three flats in four years by dusting Ulip tubes with baby powder and banning burnouts, though he still prefers tubeless where rims cooperate.
  - adopt the ritual when you cannot seat tubeless tires reliably.[^183]
- **Budget powered inflators for stubborn tubeless installs.** Manual pumps struggled to seat Chaoyang tubeless tires on G30 rims while Ulip tires on Bolt hubs aired up cleanly.
  - plan compressor access when converting commuter wheels to tubeless rubber.[^184]

## Security Layers & Theft Response

- Hide GPS trackers along the main harness, combine Rita builds with motion alarms inside the battery bag, and budget a hardened chain for long stops; layered defenses buy recovery time even though determined thieves can still lift a 20 kg scooter.[^185]

## Documentation & Support Habits

- Keep a photo log of connector routing, ST-Link pinouts, and fuse replacements so future technicians can retrace your steps. Denis’ English manual is updated as new edge cases surface.
  - reference it before opening support tickets.[^134]
- Archive Voyage/Ninebot error-code cheat sheets alongside those photos; francois schempers’ quick reference covers everything from BLE comm faults to ABS overcurrent and speeds troubleshooting when Voyage dashes flash cryptic codes.[^186]
- Archive VESC Tool logs before sealing decks: Android 11+ hides files under `Android/data/vedder.vesctool/files`, so plan to pull them via TCP bridge or file managers like XFolder after each shakedown.[^187]
- Track firmware sizes before flashing. Vedder’s 6.0 beta already stretches binaries past single Ubox MCU limits unless paired with the matching VESC Tool build, so mirror Git changelog notes and update desktop tools before pushing field upgrades.[^188][^189]
- **Flash VESC Express over CAN when USB fails.** Builders now power the module over USB for flashing screenshots, then fall back to CAN-only sessions if the USB-C port refuses to enumerate.
  - expect to use the ESP flasher inside VESC Tool and document the station-mode workflow for teammates.[^190]
- Add a mid-power controller comparison to the follow-up queue.
  - V keeps asking whether Flipsky 75100 duals or FT85BD boards suit a stock Vsett 11+, so we owe commuters a concise decision tree.[^191]
- Split CAN telemetry per controller whenever possible.
  - Voyage and Ambrosini dashboards still aggregate phase current across dual VESCs by default, so assign unique IDs or run separate sessions before diagnosing which hub is fading.[^192][^193]
- Clarify VESC Tool backup formats.
  - builders still lack a clear answer on whether XML, C, or UUID exports cover disaster recovery, so capture official guidance once Vedder or firmware maintainers respond.[^194]
- Document four-controller CAN workflows for 4WD projects; Adrian Geanca is still hunting best practices for sequencing power and communication on quad 75100 Pro v2 stacks.[^195]

## Mini-Bike & Fiido L3 Conversions

- **Respect the stock controller limits:** Fiido L3 controllers float loose without heatsinks and only deliver ~25 A; jumping straight to 20 S test packs without pre-charging popped factory BMS units. Match pack voltages before connecting higher-voltage VESC hardware.[^196]
- **Dial conservative currents:** After cutting battery current to ~20 A, setting traction control to 20/20 A, and capping phase around 60 A with FW, builders hit 45 km/h and repeatable wheelies without overheating the compact hub.[^197]
- **Plan full teardowns:** Packs are heavily sealed.
  - glued busbars, soldered fasteners, and tripped protection boards left entire parallel groups at 0 V
  - so refurb projects require full BMS removal rather than capacitor swaps.[^198]

[^damper-oil]: PuneDir’s free steering damper only behaved after switching to lighter fluids; veterans now recommend 10W/60 shock oil or Citroën LHM+ to preserve seals while restoring adjustability.[^199]
[^ldo_probe]: Source: knowledge/notes/input_part000_review.md, line 141.



## References

[^1]: Source: knowledge/notes/all_part01_review.md†L164-L164
[^2]: Source: knowledge/notes/all_part01_review.md†L165-L165
[^3]: Source: knowledge/notes/all_part01_review.md†L47-L49
[^4]: Source: knowledge/notes/all_part01_review.md†L166-L166
[^5]: Source: knowledge/notes/all_part01_review.md†L331-L331
[^6]: Source: knowledge/notes/denis_all_part02_review.md†L103-L104
[^7]: Source: knowledge/notes/denis_all_part02_review.md†L409-L411
[^8]: Source: knowledge/notes/input_part012_review.md†L228-L231
[^9]: Source: data/vesc_help_group/text_slices/input_part009.txt†L6354-L6356
[^10]: Source: data/vesc_help_group/text_slices/input_part009.txt†L6483-L6490
[^11]: Source: knowledge/notes/input_part011_review.md†L426-L428
[^12]: Source: knowledge/notes/input_part012_review.md†L318-L318
[^13]: Source: knowledge/notes/all_part01_review.md†L372-L372
[^14]: Source: knowledge/notes/all_part01_review.md†L124-L124
[^15]: Source: knowledge/notes/input_part004_review.md†L153-L155
[^16]: Source: data/vesc_help_group/text_slices/input_part004.txt†L4101-L4132
[^17]: Source: knowledge/notes/input_part011_review.md†L280-L287
[^18]: Source: knowledge/notes/input_part004_review.md†L206-L206
[^19]: Source: data/vesc_help_group/text_slices/input_part005.txt†L23147-L23160
[^20]: Source: knowledge/notes/input_part004_review.md†L261-L261
[^21]: Source: data/vesc_help_group/text_slices/input_part004.txt†L12626-L12646
[^22]: Source: knowledge/notes/denis_all_part02_review.md†L318-L320
[^23]: Source: data/vesc_help_group/text_slices/input_part004.txt†L12073-L12089
[^24]: Source: knowledge/notes/input_part006_review.md†L344-L344
[^25]: Source: knowledge/notes/denis_all_part02_review.md†L31-L32
[^26]: Source: data/vesc_help_group/text_slices/input_part001.txt†L1665-L1689
[^27]: Source: data/vesc_help_group/text_slices/input_part001.txt†L6003-L6013
[^28]: Source: data/vesc_help_group/text_slices/input_part001.txt†L6414-L6436
[^29]: Source: data/vesc_help_group/text_slices/input_part004.txt†L9300-L9374
[^30]: Source: knowledge/notes/input_part008_review.md†L256-L257
[^31]: Source: data/vesc_help_group/text_slices/input_part009.txt†L15566-L15585
[^32]: Source: data/vesc_help_group/text_slices/input_part013.txt†L16485-L16488
[^33]: Source: knowledge/notes/all_part01_review.md†L195-L195
[^34]: Source: knowledge/notes/all_part01_review.md†L172-L172
[^35]: Source: knowledge/notes/all_part01_review.md†L167-L167
[^36]: Source: knowledge/notes/all_part01_review.md†L191-L191
[^37]: Source: knowledge/notes/denis_all_part02_review.md†L95680-L95780
[^38]: Source: knowledge/notes/denis_all_part02_review.md†L28-L32
[^39]: Source: data/vesc_help_group/text_slices/input_part013.txt†L16042-L16046
[^40]: Source: knowledge/notes/input_part000_review.md†L650-L650
[^41]: Source: knowledge/notes/input_part000_review.md†L690-L690
[^42]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L110038-L110041
[^43]: Source: knowledge/notes/input_part007_review.md†L84-L84
[^44]: Source: knowledge/notes/input_part007_review.md†L97-L97
[^45]: Source: data/vesc_help_group/text_slices/input_part009.txt†L19023-L19038
[^46]: Source: data/vesc_help_group/text_slices/input_part009.txt†L7164-L7185
[^47]: Source: data/vesc_help_group/text_slices/input_part009.txt†L6581-L6584
[^48]: Source: data/vesc_help_group/text_slices/input_part009.txt†L20442-L20448
[^49]: Source: knowledge/notes/input_part012_review.md†L83-L83
[^50]: Source: knowledge/notes/input_part012_review.md†L84-L84
[^51]: Source: knowledge/notes/input_part013_review.md†L48-L48
[^52]: Source: knowledge/notes/input_part013_review.md†L190-L191
[^53]: Source: knowledge/notes/input_part005_review.md†L162-L162
[^54]: Source: knowledge/notes/denis_all_part02_review.md†L37-L38
[^55]: Source: knowledge/notes/input_part006_review.md†L108-L108
[^56]: Source: knowledge/notes/input_part011_review.md†L410-L417
[^57]: Source: knowledge/notes/denis_all_part02_review.md†L487-L487
[^58]: Source: knowledge/notes/denis_all_part02_review.md†L94-L95
[^59]: Source: knowledge/notes/denis_all_part02_review.md†L307-L308
[^60]: Source: knowledge/notes/denis_all_part02_review.md†L307-L309
[^61]: Source: knowledge/notes/denis_all_part02_review.md†L455-L455
[^62]: Source: data/vesc_help_group/text_slices/input_part010.txt†L11412-L11459
[^63]: Source: data/vesc_help_group/text_slices/input_part010.txt†L9579-L9586
[^64]: Source: knowledge/notes/denis_all_part02_review.md†L40-L41
[^65]: Source: knowledge/notes/input_part011_review.md†L314-L322
[^66]: Source: knowledge/notes/input_part011_review.md†L355-L356
[^67]: Source: data/vesc_help_group/text_slices/input_part000.txt†L18463-L18495
[^68]: Source: knowledge/notes/input_part008_review.md†L49-L51
[^69]: Source: knowledge/notes/input_part000_review.md†L646-L646
[^70]: Source: knowledge/notes/input_part000_review.md†L744-L751
[^71]: Source: knowledge/notes/input_part006_review.md†L109-L109
[^72]: Source: knowledge/notes/input_part010_review.md†L38-L40
[^73]: Source: knowledge/notes/input_part010_review.md†L38-L39
[^74]: Source: knowledge/notes/input_part010_review.md†L255-L255
[^75]: Source: knowledge/notes/input_part010_review.md†L299-L300
[^76]: Source: knowledge/notes/input_part000_review.md†L647-L647
[^77]: Source: data/vesc_help_group/text_slices/input_part002.txt†L27369-L27428
[^78]: Source: data/vesc_help_group/text_slices/input_part009.txt†L19004-L19009
[^79]: Source: data/vesc_help_group/text_slices/input_part009.txt†L7995-L7995
[^80]: Source: knowledge/notes/input_part009_review.md†L93-L93
[^81]: Source: knowledge/notes/input_part009_review.md†L96-L96
[^82]: Source: knowledge/notes/input_part009_review.md†L97-L97
[^83]: Source: knowledge/notes/input_part009_review.md†L99-L99
[^84]: Source: data/vesc_help_group/text_slices/input_part009.txt†L194-L197
[^85]: Source: data/vesc_help_group/text_slices/input_part009.txt†L11001-L11010
[^86]: Source: data/vesc_help_group/text_slices/input_part009.txt†L11223-L11262
[^87]: Source: knowledge/notes/input_part013_review.md†L113-L113
[^88]: Source: knowledge/notes/input_part013_review.md†L169-L169
[^89]: Source: knowledge/notes/input_part013_review.md†L381-L382
[^90]: Source: data/vesc_help_group/text_slices/input_part013.txt†L6685-L6688
[^91]: Source: data/vesc_help_group/text_slices/input_part013.txt†L6691-L6695
[^92]: Source: data/vesc_help_group/text_slices/input_part013.txt†L6378-L6381
[^93]: Source: data/vesc_help_group/text_slices/input_part000.txt†L21687-L21726
[^94]: Source: data/vesc_help_group/text_slices/input_part000.txt†L21783-L21888
[^95]: Source: data/vesc_help_group/text_slices/input_part003.txt†L22032-L22103
[^96]: Source: data/vesc_help_group/text_slices/input_part003.txt†L24174-L24355
[^97]: Source: data/vesc_help_group/text_slices/input_part000.txt†L21535-L21684
[^98]: Source: knowledge/notes/input_part012_review.md†L13-L13
[^99]: Source: knowledge/notes/input_part012_review.md†L105-L105
[^100]: Source: knowledge/notes/input_part012_review.md†L144-L144
[^101]: Source: knowledge/notes/input_part012_review.md†L145-L145
[^102]: Source: knowledge/notes/input_part012_review.md†L177-L177
[^103]: Source: knowledge/notes/input_part000_review.md†L649-L649
[^104]: Source: knowledge/notes/input_part000_review.md†L635-L635
[^105]: Source: knowledge/notes/input_part000_review.md†L663-L664
[^106]: Source: data/vesc_help_group/text_slices/input_part009.txt†L17692-L17699
[^107]: Source: knowledge/notes/denis_all_part02_review.md†L368-L369
[^108]: Source: knowledge/notes/denis_all_part02_review.md†L55-L57
[^109]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L96894-L96912
[^110]: Source: knowledge/notes/input_part001_review.md†L541-L542
[^111]: Source: knowledge/notes/input_part008_review.md†L259-L260
[^112]: Source: knowledge/notes/input_part013_review.md†L257-L258
[^113]: Source: knowledge/notes/input_part013_review.md†L278-L278
[^114]: Source: knowledge/notes/input_part013_review.md†L259-L259
[^115]: Source: knowledge/notes/input_part000_review.md†L133-L133
[^116]: Source: knowledge/notes/input_part000_review.md†L301-L301
[^117]: Source: data/vesc_help_group/text_slices/input_part003.txt†L26407-L26482
[^118]: Source: knowledge/notes/input_part008_review.md†L257-L258
[^119]: Source: data/vesc_help_group/text_slices/input_part009.txt†L10073-L10087
[^120]: Source: knowledge/notes/input_part000_review.md†L134-L134
[^121]: Source: data/vesc_help_group/text_slices/input_part009.txt†L15504-L15522
[^122]: Source: data/vesc_help_group/text_slices/input_part009.txt†L13108-L13115
[^123]: Source: knowledge/notes/input_part010_review.md†L249-L251
[^124]: Source: knowledge/notes/input_part010_review.md†L252-L252
[^125]: Source: knowledge/notes/input_part000_review.md†L326-L328
[^126]: Source: data/vesc_help_group/text_slices/input_part009.txt†L19199-L19203
[^127]: Source: knowledge/notes/input_part009_review.md†L384-L384
[^128]: Source: knowledge/notes/input_part000_review.md†L381-L381
[^129]: Source: knowledge/notes/input_part006_review.md†L265-L266
[^130]: Source: knowledge/notes/input_part009_review.md†L380-L380
[^131]: Source: knowledge/notes/input_part011_review.md†L521-L526
[^132]: Source: knowledge/notes/denis_all_part02_review.md†L376-L376
[^133]: Source: knowledge/notes/input_part004_review.md†L301-L302
[^134]: Source: knowledge/notes/all_part01_review.md†L209-L210
[^135]: Source: knowledge/notes/input_part011_review.md†L444-L450
[^136]: Source: knowledge/notes/denis_all_part02_review.md†L230-L231
[^137]: Source: knowledge/notes/denis_all_part02_review.md†L465-L465
[^138]: Source: knowledge/notes/denis_all_part02_review.md†L121801-L121804
[^139]: Source: knowledge/notes/input_part009_review.md†L381-L381
[^140]: Source: knowledge/notes/input_part007_review.md†L411-L411
[^141]: Source: knowledge/notes/input_part012_review.md†L176-L176
[^142]: Source: knowledge/notes/input_part007_review.md†L412-L412
[^143]: Source: knowledge/notes/input_part013_review.md†L219-L219
[^144]: Source: knowledge/notes/input_part013_review.md†L391-L393
[^145]: Source: data/vesc_help_group/text_slices/input_part013.txt†L16110-L16111
[^146]: Source: data/vesc_help_group/text_slices/input_part013.txt†L16461-L16468
[^147]: Source: knowledge/notes/input_part010_review.md†L350-L351
[^148]: Source: knowledge/notes/input_part010_review.md†L351-L352
[^149]: Source: knowledge/notes/input_part010_review.md†L353-L353
[^150]: Source: knowledge/notes/input_part008_review.md†L54-L54
[^151]: Source: knowledge/notes/input_part006_review.md†L16-L16
[^152]: Source: knowledge/notes/input_part012_review.md†L137-L137
[^153]: Source: knowledge/notes/input_part012_review.md†L138-L138
[^154]: Source: knowledge/notes/input_part008_review.md†L316-L316
[^155]: Source: knowledge/notes/input_part012_review.md†L220-L223
[^156]: Source: knowledge/notes/input_part012_review.md†L231-L233
[^157]: Source: knowledge/notes/input_part012_review.md†L360-L360
[^158]: Source: knowledge/notes/input_part012_review.md†L374-L374
[^159]: Source: knowledge/notes/input_part012_review.md†L397-L399
[^160]: Source: knowledge/notes/input_part012_review.md†L224-L228
[^161]: Source: knowledge/notes/input_part012_review.md†L228-L233
[^162]: Source: knowledge/notes/input_part012_review.md†L348-L348
[^163]: Source: knowledge/notes/input_part012_review.md†L349-L349
[^164]: Source: knowledge/notes/input_part012_review.md†L111-L111
[^165]: Source: knowledge/notes/input_part012_review.md†L112-L112
[^166]: Source: knowledge/notes/input_part012_review.md†L184-L184
[^167]: Source: knowledge/notes/input_part012_review.md†L185-L185
[^168]: Source: knowledge/notes/input_part012_review.md†L368-L368
[^169]: Source: knowledge/notes/input_part012_review.md†L234-L239
[^170]: Source: knowledge/notes/input_part012_review.md†L240-L242
[^171]: Source: knowledge/notes/input_part012_review.md†L242-L246
[^172]: Source: knowledge/notes/input_part012_review.md†L246-L248
[^173]: Source: knowledge/notes/input_part012_review.md†L248-L250
[^174]: Source: knowledge/notes/input_part008_review.md†L74-L74
[^175]: Source: knowledge/notes/input_part008_review.md†L75-L78
[^176]: Source: knowledge/notes/input_part008_review.md†L348-L350
[^177]: Source: knowledge/notes/input_part008_review.md†L79-L79
[^178]: Source: knowledge/notes/input_part010_review.md†L265-L266
[^179]: Source: knowledge/notes/input_part010_review.md†L266-L267
[^180]: Source: knowledge/notes/input_part012_review.md†L36-L36
[^181]: Source: knowledge/notes/input_part012_review.md†L426-L426
[^182]: Source: knowledge/notes/input_part012_review.md†L74-L74
[^183]: Source: knowledge/notes/input_part013_review.md†L51-L51
[^184]: Source: knowledge/notes/input_part013_review.md†L52-L52
[^185]: Source: knowledge/notes/all_part01_review.md†L896-L896
[^186]: Source: knowledge/notes/input_part011_review.md†L402-L406
[^187]: Source: data/vesc_help_group/text_slices/input_part001.txt†L3440-L4018
[^188]: Source: data/vesc_help_group/text_slices/input_part002.txt†L1841-L1853
[^189]: Source: data/vesc_help_group/text_slices/input_part002.txt†L2125-L2127
[^190]: Source: data/vesc_help_group/text_slices/input_part012.txt†L11592-L11619
[^191]: Source: data/vesc_help_group/text_slices/input_part013.txt†L9230-L9336
[^192]: Source: knowledge/notes/input_part013_review.md†L209-L209
[^193]: Source: data/vesc_help_group/text_slices/input_part013.txt†L6488-L6493
[^194]: Source: data/vesc_help_group/text_slices/input_part013.txt†L5211-L5211
[^195]: Source: data/vesc_help_group/text_slices/input_part013.txt†L6072-L6074
[^196]: Source: knowledge/notes/input_part008_review.md†L381-L381
[^197]: Source: knowledge/notes/input_part008_review.md†L382-L382
[^198]: Source: knowledge/notes/input_part008_review.md†L383-L383
[^199]: Source: knowledge/notes/input_part008_review.md†L56-L56
[^code-server]: Source: knowledge/notes/input_part006_review.md†L21-L21
[^motor_detect_flow]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24741-L24763
