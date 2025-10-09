# input_part004.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part004.txt`
- Coverage:
  - Initial pass: 2023-01-20 03:01 through 2023-05-03 10:03 (lines 1-10,955)
  - Second pass: 2023-03-02 15:39 through 2023-04-15 18:34 (lines 4,000-8,499)
- Next starting point: line 8,500 (continue second-pass review of 2023-04-15 18:34 onward)

## Key Findings

### Second-pass Deep Dive (Lines 4,000-5,499 | 2023-03-02 – 2023-03-11)
- **High-voltage braking headroom.** Builders running 22S packs cautioned that regen spikes demand at least 120–130 V-rated components (including TVS clamps and logic-side converters), because protection devices can begin clamping in the mid-90 V range when braking hard.【F:data/vesc_help_group/text_slices/input_part004.txt†L4018-L4026】
- **Spintend single-board hardware observations.** The new single Spintend board ships with G015N10 MOSFETs on an aluminum PCB; veterans emphasized leaving that stack alone unless you also retune gate resistors and snubbers, since the board inherits Zero 11X driver values that were dialed in for Infineon devices.【F:data/vesc_help_group/text_slices/input_part004.txt†L4246-L4274】
- **Makerbase/Flipsky 75xxx noise & firmware patches.** Makerbase 75200 samples arrived with glue instead of thermal paste and noisy current-sense stages that trip ABS overcurrent faults; Jake circulated an experimental `fsesc_75_200_alu_sample2.bin` build that averages phase currents to calm the readings, but it remains an unofficial test branch.【F:data/vesc_help_group/text_slices/input_part004.txt†L4454-L4495】
- **Controller mounting & cooling for Xiaomi builds.** When adapting Spintend hardware to Xiaomi decks, the crew recommends bending or machining metal straps (or tapping the HDPE base) so the case bolts down firmly; thermal tape or glue alone doesn’t manage heat or survive potholes.【F:data/vesc_help_group/text_slices/input_part004.txt†L4360-L4412】
- **Motor temperature instrumentation.** Installing EPCOS/TDK B57861S0502F040 2×4 mm NTCs against the hall/phase bundle, secured with thermal epoxy during a Statorade and lead rework, delivered accurate 150 °C-capable phase readings in minutes.【F:data/vesc_help_group/text_slices/input_part004.txt†L4545-L4573】
- **Stacked Ninebot packs & cutoff voltage.** Riders stacking two stock Ninebot G30 packs into 20S lowered the VESC battery cutoff to about 56.5 V (~2.85 V/cell) to ride through sag without hitting BMS limits prematurely.【F:data/vesc_help_group/text_slices/input_part004.txt†L4677-L4697】

### Second-pass Deep Dive (Lines 5,500-6,999 | 2023-03-13 – 2023-03-25)
- **QS205 sealing vs ferrofluid trade-offs.** Builders highlighted that QS205 hubs ship with a solid factory seal and may not need ferrofluid on bicycle frames; opening the case just to add coolant risks water ingress unless it is resealed with a thin bead of neutral RTV (e.g., 704) rather than generic silicone that hardens poorly.【F:data/vesc_help_group/text_slices/input_part004.txt†L5527-L5544】
- **Rotor and caliper upgrades for 20 kW-class hubs.** Magura MDR-C rotors nearly melted on 22×3 wheel builds; seasoned riders favor BrakeStuff or Trickstuff 3 mm rotors (or Magura’s MDR-P in 180 mm sizes) and remind newcomers to break factory threadlocker before swapping hardware.【F:data/vesc_help_group/text_slices/input_part004.txt†L5581-L5599】
- **Police-mode Lisp workflow.** Ofek’s shared Lisp app toggles between a 25 km/h/50 % current “safe” profile and full power after the bike stops, using timed brake-and-throttle holds; it requires both ADC1 and ADC2 inputs and the dwell time can be reduced (e.g., to 2 km/h for detection).【F:data/vesc_help_group/text_slices/input_part004.txt†L6111-L6120】
- **Dual-motor detection drift troubleshooting.** Uneven phase resistance readings between front and rear VSETT motors were traced to harness differences and detection quirks; the group recommended manual tuning and temporarily lowering zero-vector frequency to 5–10 kHz during FOC detection before restoring 20–25 kHz to quiet the noise that appeared at 180 A/80 A limits.【F:data/vesc_help_group/text_slices/input_part004.txt†L6122-L6149】
- **ANT BMS precharge limits.** ANT owners liked raising precharge from 20 A to 30 A to prevent cold-weather brownouts, but veterans warned that routinely exceeding 20 A has blown the precharge FETs, reinforcing the need for external resistors or staged buttons instead of abusing the built-in circuit.【F:data/vesc_help_group/text_slices/input_part004.txt†L5880-L5892】
- **Stall torture killing 75 100s.** Multiple Makerbase/Flipsky 75 100 controllers died after ~3 s stalls at 90 A, highlighting how TO-220 MOSFET pairs overheat before the heatsink sensor reacts; suggestions included bolting the ESC to a real heatsink, replacing Kapton isolators with thermal pads, and seeking Toll8-based revisions for abuse tolerance.【F:data/vesc_help_group/text_slices/input_part004.txt†L6227-L6276】
- **Makerbase power-up fault above 3 S.** A brand-new Makerbase 75 100 that booted on 3 S refused to wake on 13 S/16 S packs even after flashing multiple 6.0–6.02 binaries, pointing to a high-voltage hardware defect that likely warrants RMA rather than further firmware experiments.【F:data/vesc_help_group/text_slices/input_part004.txt†L6534-L6706】
- **Display boot-time expectations.** Raspberry Pi-based VESC dashboard images can take 45–95 s to load because they start a full OS before the UI, whereas the SmartDisplay’s MCU firmware shows data in ≈10 s by skipping the Linux boot chain and waiting only for CAN/current initialization.【F:data/vesc_help_group/text_slices/input_part004.txt†L6980-L6993】

### Controller Faults, Firmware Glitches & Mitigations
- Burned MOSFETs tend to fail under low-current loads; expect seemingly random cutouts once devices have been overstressed at hundreds of amps.【F:data/vesc_help_group/text_slices/input_part004.txt†L33-L41】
- Stacking a stock Ninebot G30 36 V pack with an external 4 S battery requires matching BMS capabilities: the internal pack clamps at ≈20 A, and both packs need similar charge levels and discharge capability; swapping to a 60 V pack restored normal power and produced complete detection data in VESC Tool.【F:data/vesc_help_group/text_slices/input_part004.txt†L129-L178】
- Multiple Spintend UBOX Single 100/100 boards arrived with faulty current-sense op-amps that force nonsensical offsets (30–4 000 counts) and trigger faults until the parts are replaced; a separate maintenance reconnect blew three input capacitors and XT60s, pointing to batch-quality issues.【F:data/vesc_help_group/text_slices/input_part004.txt†L184-L194】【F:data/vesc_help_group/text_slices/input_part004.txt†L915-L923】
- Flypsky 75200 CAN comms can soft-fail; restoring factory defaults and re-running detection revived the interface without hardware swaps.【F:data/vesc_help_group/text_slices/input_part004.txt†L81-L95】
- Little FOCer throttles behave if wired to 3.3 V reference (with halls left on 5 V); running the pot on 5 V can hold full throttle, so ensure 0.6–0.9 V idle and 2.5–3.3 V WOT after rewiring and writing the new setup.【F:data/vesc_help_group/text_slices/input_part004.txt†L339-L387】

### Motor Thermal Management & Repair Tactics
- VSETT hub motors dislike sustained 190 A phase / 90 A battery loads; builders recommend 160 A peak, 140 A sustained, and to inspect for heat-damaged solder joints when symptoms (stalling when hot) appear.【F:data/vesc_help_group/text_slices/input_part004.txt†L600-L621】
- Factory phase terminations on VSETT motors often need rework—strip enamel with flame, flood with flux, solder thoroughly, and clean stray solder to avoid shorts before reassembling grommets and sleeves.【F:data/vesc_help_group/text_slices/input_part004.txt†L1085-L1103】
- Persistent cogging once warm can be attacked stepwise: add ferrofluid and a temperature sensor, raise zero-vector frequency, enable saturation compensation, and only then reduce current limits if needed.【F:data/vesc_help_group/text_slices/input_part004.txt†L1124-L1141】
- Raising the sensorless transition to ~3 000 eRPM (instead of 500–700) cured low-speed stutter after heat soak by delaying the switch-over until sufficient back-EMF is present.【F:data/vesc_help_group/text_slices/input_part004.txt†L1195-L1233】
- Moderate field weakening (≈20 A) with 85–89 % duty and longer ramp times (~800 ms) smooths top-end pull while softening battery current spikes on single-motor builds aiming for ~74 km/h.【F:data/vesc_help_group/text_slices/input_part004.txt†L1247-L1259】

### Battery Construction & Power Delivery Notes
- Copper busbar “sandwich” welds can fail from oxidation; brazing with tin under inert gas yields lower resistance joints, especially when mixing copper and nickel, but demands shielding (argon) that spot welders lack by default.【F:data/vesc_help_group/text_slices/input_part004.txt†L274-L310】
- When pairing OEM and DIY battery packs, confirm each BMS is rated for the combined discharge, charge them separately to similar voltages, and ensure the auxiliary pack has at least the same parallel count/cell capability as the stock unit.【F:data/vesc_help_group/text_slices/input_part004.txt†L163-L166】

### Instrumentation & Display Ecosystem
- Rage Mechanics’ SmartDisplay project is maturing into a CNC aluminum, anti-glare unit that bridges to VESC Tool, manages BLE/Minimotors/Kelly controllers, logs GPS, and adds RTC plus media controls; current hardware supports double-click button mapping with plans for encoder knobs and web availability later this year.【F:data/vesc_help_group/text_slices/input_part004.txt†L935-L975】

### Controller & Firmware Insights (2023-02-07 – 2023-03-05)
- Little FOCer/Tronic 250 hardware still relies on a 6-FET layout, so builders cap them around 100 A battery, 250 A phase (300 A absolute) and 45 A of field weakening; recent revisions run cooler when kept dry, while earlier burnouts were largely tied to over-current and water ingress.【F:data/vesc_help_group/text_slices/input_part004.txt†L2223-L2241】
- Voltage headroom matters: the same setup clocked 0–50 km/h in 3.7 s on 16 S (≈166 A battery peak) versus 3.2 s on 20 S (≈258 A battery peak), underscoring how higher pack voltage slashes acceleration times.【F:data/vesc_help_group/text_slices/input_part004.txt†L2294-L2294】
- Kelly 7212 controllers use 12×5.5 mΩ FETs and feel torque-starved above 120 A, whereas 7230 builds with 60 mm+ motors have logged bursts near 592 A phase / 225 A battery when paired with Makerbase 75200 hardware, exceeding what 75100 units can sustain.【F:data/vesc_help_group/text_slices/input_part004.txt†L2467-L2509】【F:data/vesc_help_group/text_slices/input_part004.txt†L4133-L4139】
- Spintend UBOX phase filters should be enabled only during the detection wizard; leaving them active while riding raises the risk of sensor noise and ABS overcurrent faults.【F:data/vesc_help_group/text_slices/input_part004.txt†L2677-L2682】
- Persistent ABS overcurrent on Flipsky 75100 setups is usually software-related—rerun detections with sane current limits, enable the slow ABS limiter, and flash matching bootloader/firmware pairs from the same VESC Tool release (desktop flashing is more reliable than mobile).【F:data/vesc_help_group/text_slices/input_part004.txt†L3703-L3796】
- Dual-profile “legal/illegal” throttles need firmware work: stock VESC mappings ignore ADC2, and even Lisp scripts can’t override the app without remapping inputs or consolidating signals onto ADC3.【F:data/vesc_help_group/text_slices/input_part004.txt†L3814-L3833】

### Controller Hardware & Firmware Updates (2023-03-06 – 2023-04-24)
- Spintend’s new single board arrived with an aluminum PCB and G015N10 FET stack; builders trust the package when the gate network is matched to those devices, cautioning against random MOSFET swaps that ignore the driver’s resistor/capacitor tuning.【F:data/vesc_help_group/text_slices/input_part004.txt†L4241-L4268】
- UBOX V2 on firmware 6.0 reported lab-grade voltage accuracy and stable torque when switching to the Mxlemming observer on Segway GT2 hubs (≈21–22 mΩ), with the tool auto-selecting lambda compensation after detection.【F:data/vesc_help_group/text_slices/input_part004.txt†L4282-L4290】
- A Makerbase 75100 alu PCB that worked on 16 S instantly shorted at the first throttle input on 22 S, leaving both motors resistive—community consensus was blown MOSFETs from the higher pack voltage and regen spikes.【F:data/vesc_help_group/text_slices/input_part004.txt†L6459-L6464】
- Jake’s troubleshooting confirms Flipsky/Makerbase 75200 hardware still needs custom “no-limit” firmware builds to suppress noise-induced stutter at high duty; the sample binaries smooth large motors but should be tested cautiously above 80 % duty until an official fix ships.【F:data/vesc_help_group/text_slices/input_part004.txt†L8942-L8968】

### Wiring, Thermal Sensing & Motor Care
- Installing EPCOS/TDK B57861S0502F040 NTCs (≈2 × 4 mm) right at the hall bundle gives accurate phase temperatures; the crew solders the tiny beads to the phase leads, secures them with thermal epoxy, and pairs the job with Statorade and phase rework during motor overhauls.【F:data/vesc_help_group/text_slices/input_part004.txt†L4545-L4573】
- Heavy scooter builds push wiring hard: even 8 AWG harnesses start heating near 150 A, and Paolo sees sub-50 % efficiency with 330 A bursts unless forced-air cooling and vented covers keep the stator in check.【F:data/vesc_help_group/text_slices/input_part004.txt†L9418-L9434】

### Power Management & BMS Practices
- ANT BMS users bumped precharge from 20 A to 30 A to avoid cold-weather brownouts on 13 S/33 A builds, but others warn that exceeding 20 A regularly blows the precharge FETs—documenting safe resistor/button add-ons remains a priority.【F:data/vesc_help_group/text_slices/input_part004.txt†L5880-L5893】【F:data/vesc_help_group/text_slices/input_part004.txt†L5933-L5940】
- When recapping Tronic or Little FOCer controllers, builders emphasise low-ESR electrolytics (with ceramic snubbers already on-board) and warn that arbitrarily upsizing capacitance can destabilize the inverter and kill the ESC.【F:data/vesc_help_group/text_slices/input_part004.txt†L8236-L8277】
- A handheld 1 kHz AC meter (YR1035-class) proved quick and repeatable for matching cell internal resistance; although the absolute numbers read lower than DC tests, the crew still relies on the relative spread to bin cells for packs.【F:data/vesc_help_group/text_slices/input_part004.txt†L8875-L8897】

### Displays, Instrumentation & Control UX
- Rage Mechanics’ SmartDisplay is nearing production with modular harnesses for VESC, Kelly, Minimotors, Zero, and VSETT plus swappable UI themes; pricing is expected at €400–€600 retail (first 10 units €199.99) once the initial 100-piece run lands.【F:data/vesc_help_group/text_slices/input_part004.txt†L5214-L5237】
- The SmartDisplay boots in ≈10 s thanks to its MCU stack, whereas the Raspberry Pi-based open-source VESC display needs 60–95 s because it has to start a full OS before the app—users found headless images faster but lost touchscreen support and CAN access.【F:data/vesc_help_group/text_slices/input_part004.txt†L6980-L6993】
- Ofek shared a “police mode” Lisp app that toggles between locked 25 km/h and full power when the rider holds brake and throttle together (1.5 s for safe mode, 5.5 s for unlock), assuming both ADC1 and ADC2 inputs are wired.【F:data/vesc_help_group/text_slices/input_part004.txt†L6112-L6119】

### Charging & Power Supply Reliability
- A refurbished “Meanwell” fast charger failed intermittently—loose add-on circuitry and cold solder joints caused LED dropouts, RCD trips, and eventual death, convincing riders to hunt for genuine 22 S-capable supplies despite the higher €200+ price tags.【F:data/vesc_help_group/text_slices/input_part004.txt†L9300-L9374】

### Motor & Drivetrain Maintenance
- One “new” VSETT hub arrived rusty with loose magnets; the group recommends stripping corrosion, re-gluing magnets with Loctite AA326, and reinspecting before reuse.【F:data/vesc_help_group/text_slices/input_part004.txt†L2133-L2152】
- Fresh 60 mm hubs responded well to ferrofluid fills, with riders comfortable targeting ~50 A battery and 100 A phase once the stator is rewrapped and clamped correctly.【F:data/vesc_help_group/text_slices/input_part004.txt†L3001-L3015】
- High-torque 11-inch hubs can shed magnets if hammered with sustained 200 A+ phase current; temper the amps or expect heat-driven failures.【F:data/vesc_help_group/text_slices/input_part004.txt†L2695-L2706】
- Magura brakes that smoke under heavy decel should be cooled while rolling—stopping immediately traps heat, boils fluid, and forces a re-bleed.【F:data/vesc_help_group/text_slices/input_part004.txt†L4146-L4156】
- Rage Mechanics now sells FH60 (high-speed) and FHT60 (torque) motors for G30 dual-20 S builds: expect ~120–130 km/h with the speed wind or ~100 km/h with the torque wind, and plan on 6" rims supporting e-Fire 10×2–3 tires (10×2 is tight).【F:data/vesc_help_group/text_slices/input_part004.txt†L3475-L3496】
- CST 10×2.5 inner tubes have held up to months of mixed on/off-road use; they’re thick enough for 10×3 tires, though 20 S setups can still shred them if pressures stay low.【F:data/vesc_help_group/text_slices/input_part004.txt†L2640-L2656】

### Battery & Cell Diagnostics
- Internal-resistance testers need low-value calibration loads: builders aim for ≈20 mΩ references, observe ~8 mΩ on P42A cells, ~10 mΩ on Samsung 50S, and ≥22 mΩ on aged Samsung 50E packs; AC 1 kHz meters are best for comparisons rather than absolutes.【F:data/vesc_help_group/text_slices/input_part004.txt†L3235-L3308】
- Pulling 110 A from 60 A-rated cells for several seconds spikes sag and accelerates degradation—acceptable occasionally, but repeated abuse shortens pack life fast.【F:data/vesc_help_group/text_slices/input_part004.txt†L3723-L3730】

### Tuning & Performance Notes
- Switching to the Mxlemming observer, dropping measured inductance ~15%, and limiting zero-vector frequency to 10 kHz during detection noticeably reduces cogging and restores launch torque on high-saturation hubs compared with Ortega Original.【F:data/vesc_help_group/text_slices/input_part004.txt†L3561-L3575】
- Geared hubs that stumble above 80 A phase benefit from raising the sensorless hand-off eRPM after hall detection—otherwise saturation compensation still leaves dead spots once the controller transitions.【F:data/vesc_help_group/text_slices/input_part004.txt†L4192-L4203】

### Accessories & Data Logging
- Dragy’s DRG70 pre-order swaps in a 10th-gen u-blox GPS with better accuracy, but its magnetic mount needs bare steel—aluminum stems require an auxiliary bracket or adhesive magnet once the finish is removed.【F:data/vesc_help_group/text_slices/input_part004.txt†L4120-L4132】

### Controller Safety, Traction & Firmware (2023-04-24 – 2023-05-03)
- Dual-throttle experiments showed the practical limits of CAN sharing: keep both controllers on VESC CAN mode, feed the throttle only into the master with `ADC+UART`, and let CAN status messages mirror torque to the slave; if you truly need independent wheels, split CAN and wire separate throttles while capping the front phase current near the battery limit to tame slip.【F:data/vesc_help_group/text_slices/input_part004.txt†L9519-L9545】
- Riders flagged how Little FOCer traction control can double heat soak—10 kW pulls climbed from ~35 °C to ~70 °C until they disabled TC—while C350 owners running 15 kW at 350 A phase saw no such spike, reinforcing that hardware, not the shared VESC algorithm, is over-stressing the FOCer boards.【F:data/vesc_help_group/text_slices/input_part004.txt†L9569-L9594】
- Flipsky and Makerbase 75100 v1 units that mis-detect motors on 6.xx firmware settled down after flashing the 75300_r2 hardware package and disabling the phase filters once setup was complete, restoring sane readings across multiple controllers.【F:data/vesc_help_group/text_slices/input_part004.txt†L9794-L9815】
- High-speed duty faults cropped up on both Tronic and MP2 builds when heavy field weakening pushed battery amps past 300 A; reverting to 5.3 firmware or dropping FW cleared the cutouts, and builders suspect shunt mods and sensor limits are letting current divergence trip the safeguards near top speed.【F:data/vesc_help_group/text_slices/input_part004.txt†L10655-L10715】

### Battery, Charging & BMS Practices (2023-04-24 – 2023-05-03)
- Running Xiaomi chargers in series for 20 S packs is discouraged unless you confirm galvanic isolation—builders recommend selling the OEM bricks, buying purpose-built units, and avoiding ad-hoc mains hacks that can trip breakers or worse.【F:data/vesc_help_group/text_slices/input_part004.txt†L10020-L10048】
- Riders who bypassed BMS protection ended up juggling cells manually; veterans cautioned that unbalanced parallel groups eventually fail, urging proper smart BMS installs (ANT or LLT) instead of bargain 40 A boards or shunted resistors that outstrip their FET ratings.【F:data/vesc_help_group/text_slices/input_part004.txt†L9925-L9949】【F:data/vesc_help_group/text_slices/input_part004.txt†L10217-L10255】

### Displays, Controls & Instrumentation Updates (2023-04-24 – 2023-05-03)
- VESC builds using scooter throttles should still feed 3.3 V references and, when necessary, add dividers so the ADC never sees more than ~3.1 V even if the hall rail jumps to 5 V, avoiding runaway acceleration if a short forces the wiper high; Spintend’s ADC adapter remains a drop-in safeguard.【F:data/vesc_help_group/text_slices/input_part004.txt†L10733-L10738】
- Safe-start logic only catches hard faults, so one rider recounted a stuck throttle cable launching his bike the moment power returned; the new community VSETT Lisp script now mirrors speed on stock LT-01/QS displays and provides a foundation for profile switching, but testers are encouraged to report quirks as features like mode toggles come online.【F:data/vesc_help_group/text_slices/input_part004.txt†L10742-L10769】【F:data/vesc_help_group/text_slices/input_part004.txt†L10754-L10764】

### Brake, Chassis & Suspension Notes (Second Pass, 2023-03-25 – 2023-03-31)
- Riders swapping to 3 mm Brakestuff rotors reported that Magura Saints only stay quiet if the discs are perfectly true—any runout makes them “cling” constantly—while Hope Tech 4 V4 calipers on the same rotors delivered the strongest stopping power tested so far.【F:data/vesc_help_group/text_slices/input_part004.txt†L7401-L7405】【F:data/vesc_help_group/text_slices/input_part004.txt†L7469-L7472】
- Upgrading Dualtron suspension bushings from OEM bronze to iglidur sleeves felt smooth initially but deformed within weeks, reinforcing that plastic bushings are consumables best reserved for light loads while metal options handle heat and shock better in the long term.【F:data/vesc_help_group/text_slices/input_part004.txt†L7513-L7528】

### Motor Sensing & Display Integration (Second Pass, 2023-03-27 – 2023-03-28)
- A second pass through the Xiaomi/VSETT swap experiments confirmed that hall PCB spacing and orientation keep the Vsett10+ motor from running on Xiaomi controllers even after replacing damaged halls; riders concluded that incompatible geometry—not firmware—causes the persistent cogging.【F:data/vesc_help_group/text_slices/input_part004.txt†L7238-L7258】
- To retain OEM dashboards while moving propulsion to VESC hardware, builders split the five hall outputs (power, ground, and three phases) so the stock controller still counts speed, noting that IO Hawk gear hubs also carry a sixth “tach” hall dedicated to the display signal.【F:data/vesc_help_group/text_slices/input_part004.txt†L7264-L7287】

### Controller, Firmware & Powertrain Findings (Second Pass, 2023-03-31 – 2023-04-11)
- One rider logged dual Makerbase 75200 failures after 452 A phase spikes at ~70 km/h; both controllers shorted until the battery BMS cut at 2.9 V per cell, underscoring how aggressive e-braking or saggy packs can simultaneously trip controllers and protection boards.【F:data/vesc_help_group/text_slices/input_part004.txt†L7577-L7678】
- Rage Mechanics and community testers reiterated that Ubox v2 units plateau near 150 A phase and 50–60 A battery per motor; anyone chasing 150 A DC and 350 A phase per wheel needs to step up to C350-class hardware or non-VESC Kelly options instead of overdriving Uboxes.【F:data/vesc_help_group/text_slices/input_part004.txt†L7771-L7787】
- Firmware 6.0/6.2 still induces heavy-load stutter on high-current hubs that run smoothly on 5.3 with identical parameters, pointing to sensorless observer changes that oversaturate small stators unless current limits are reduced.【F:data/vesc_help_group/text_slices/input_part004.txt†L7797-L7810】
- Makerbase 75100 Alu boards continue to die gracefully—logging only ~44 °C—when pushed on 22 S with strong field weakening, suggesting the MOSFET stage is marginal even when telemetry reports safe temperatures.【F:data/vesc_help_group/text_slices/input_part004.txt†L7916-L7947】
- Flipsky 75200 owners tracking hardware repairs confirmed the power stage uses Infineon N015N10 MOSFETs; replacing cracked devices requires hot-air plus preheat (or even an iron) to evenly lift the TOLL packages without lifting pads.【F:data/vesc_help_group/text_slices/input_part004.txt†L7866-L7889】

### Wiring, Thermal & Maintenance Practices (Second Pass, 2023-04-03 – 2023-04-06)
- A cable failure autopsy showed 2.5 mm² motor leads melting inside a Blade hub after 110–155 A pulls; the fix was upsizing to 4–6 mm² conductors through the axle while keeping halls intact, and adding heavier external jumpers only delays—not prevents—inner lead burnups.【F:data/vesc_help_group/text_slices/input_part004.txt†L8086-L8137】
- Riders troubleshooting ADC2 brake inputs on VESC Tool still have to recompile firmware with remapped inputs or switch to simple current-control modes—stock binaries ignore the secondary analog channel for braking logic.【F:data/vesc_help_group/text_slices/input_part004.txt†L8138-L8144】

### Component Selection & Power Electronics Guidance (Second Pass, 2023-04-07 – 2023-04-08)
- MP2 builders debated insulation stacks for TO-220 FETs and landed on high-quality thermal pads (or mica with paste) rated for the planned 300 A phase loads, respecting the hardware designer’s 18-FET limits before chasing higher currents.【F:data/vesc_help_group/text_slices/input_part004.txt†L8204-L8223】
- When recapping Tronic, Little FOCer, or other VESC derivatives, the group prioritized low-ESR electrolytics sized per the reference design and paralleled with 100–470 nF ceramics; simply chasing higher capacitance can lengthen charge times and destabilize the controller.【F:data/vesc_help_group/text_slices/input_part004.txt†L8236-L8276】

## Follow-ups / Open Questions
- Confirm whether Spintend has issued an RMA or component revision for the faulty current-sense chain and capacitor explosions noted here.【F:data/vesc_help_group/text_slices/input_part004.txt†L184-L194】【F:data/vesc_help_group/text_slices/input_part004.txt†L915-L923】
- Document best practices for resealing VSETT hubs after phase re-soldering (potting, strain relief, hall verification) to complement the solder guidance captured above.【F:data/vesc_help_group/text_slices/input_part004.txt†L1085-L1148】
- Capture the exact SmartDisplay release timeline, pricing, and wiring guides once Rage Mechanics publishes the commercial offering.【F:data/vesc_help_group/text_slices/input_part004.txt†L962-L975】
- Explore whether custom firmware patches (or VESC Tool updates) will expose ADC2/ADC3 mapping so legal/illegal ride profiles can switch between torque sensor and throttle without hardware switches.【F:data/vesc_help_group/text_slices/input_part004.txt†L3814-L3833】
- Validate a repeatable calibration workflow for low-resistance battery testers so IR readings remain comparable across shops.【F:data/vesc_help_group/text_slices/input_part004.txt†L3235-L3308】
- Track whether Flipsky/Makerbase publish permanent firmware or hardware fixes for high-duty jitter on 75100/75200 units beyond Jake’s experimental binaries.【F:data/vesc_help_group/text_slices/input_part004.txt†L8942-L8968】
- Document safe precharge configurations for ANT BMS owners so cold-weather starts don’t require exceeding the 20 A FET limit.【F:data/vesc_help_group/text_slices/input_part004.txt†L5880-L5893】【F:data/vesc_help_group/text_slices/input_part004.txt†L5933-L5940】
- Source and validate dependable 22 S fast chargers to replace the refurbished Meanwell builds that failed under load here.【F:data/vesc_help_group/text_slices/input_part004.txt†L9300-L9374】
- Investigate whether Little FOCer traction-control overheating stems from shunt mods, firmware, or hardware tolerances before teams re-enable TC on high-power builds.【F:data/vesc_help_group/text_slices/input_part004.txt†L9569-L9594】【F:data/vesc_help_group/text_slices/input_part004.txt†L10655-L10715】
- Compile definitive guidance on stacking chargers and selecting robust smart BMS options so DIYers stop serializing non-isolated Xiaomi bricks or relying on undersized 40 A boards.【F:data/vesc_help_group/text_slices/input_part004.txt†L10020-L10048】【F:data/vesc_help_group/text_slices/input_part004.txt†L10217-L10255】
- Exercise and document the new VSETT Lisp display script (modes, failsafes, throttle interactions) once additional features land, ensuring safe-start expectations align with real behavior.【F:data/vesc_help_group/text_slices/input_part004.txt†L10742-L10769】【F:data/vesc_help_group/text_slices/input_part004.txt†L10754-L10764】
- Validate Ofek’s police-mode Lisp packaging (ADC wiring, PAS integration) so riders can legally unlock profiles without tripping failsafes.【F:data/vesc_help_group/text_slices/input_part004.txt†L6111-L6120】
- Determine whether Makerbase’s 75 100 power-up issue above 3 S is a batch defect or configuration pitfall and document the RMA path if hardware-faulty units persist.【F:data/vesc_help_group/text_slices/input_part004.txt†L6534-L6706】
- Explore firmware or hardware safeguards that prevent stalled Vsett motors from nuking 75 100 MOSFETs before temperature feedback reacts.【F:data/vesc_help_group/text_slices/input_part004.txt†L6227-L6276】
- Identify firmware or hardware workarounds that let Xiaomi/VSETT hall boards interoperate, or document a proven method to remount sensors so mixed motor/controller combos stop cogging.【F:data/vesc_help_group/text_slices/input_part004.txt†L7238-L7258】
- Capture a safe repair workflow for replacing cracked N015N10 TOLL devices on Flipsky 75200s (preheat temps, adhesives, conformal coating) before more owners attempt hot-air swaps.【F:data/vesc_help_group/text_slices/input_part004.txt†L7866-L7889】
- Quantify how much additional capacitance VESC-derived controllers can accept before soft-start or charge-pump stages misbehave so recap projects stay within stability margins.【F:data/vesc_help_group/text_slices/input_part004.txt†L8236-L8276】
