# input_part000.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part000.txt`
- Coverage:
  - Batch 1: 2021-04-02 23:23:16 through 2021-04-03 01:46:36 (lines 1-320)
  - Batch 2: 2021-04-03 01:46:51 through 2021-05-18 17:49:41 (lines 321-2400)
  - Batch 3: 2021-05-18 17:50:23 through 2021-05-28 19:56:29 (lines 2401-3600)
  - Batch 4: 2021-05-28 19:56:29 through 2021-05-31 00:01:06 (lines 3601-4210)
  - Batch 5: 2021-05-31 00:01:07 through 2021-06-17 16:13:29 (lines 4211-6400)
  - Next starting point: line 6401 (2021-06-17T16:13:29 and later)

## Key Findings

### Group Purchasing & Hardware Checklist (Batch 1)
- Coordinated bulk order recommended to exploit a single-use 20% Flipsky discount, with shipping routed through France; discount code valid 24 hours and can be reactivated by contacting Flipsky.【F:data/vesc_help_group/text_slices/input_part000.txt†L3-L5】【F:data/vesc_help_group/text_slices/input_part000.txt†L147-L152】
- Suggested starter kit for dual builds: two Flipsky 7550 controllers (rated for up to 16 S), Bluetooth module v6, CAN bus cable, anti-spark switch for 20 S packs, and assorted JST leads for hall sensors, throttle, and brakes.【F:data/vesc_help_group/text_slices/input_part000.txt†L6-L13】【F:data/vesc_help_group/text_slices/input_part000.txt†L22-L23】
- Additional wiring supplies called out: XT60/XT90 connectors, JST plugs, and 4 mm–6 mm bullet connectors for motor phases.【F:data/vesc_help_group/text_slices/input_part000.txt†L107-L108】
- Buyers should budget roughly €940 incl. VAT for two Trampa/Stormcore-class controllers (≈£350 each before tax/shipping) and consider gear insurance given the replacement cost.【F:data/vesc_help_group/text_slices/input_part000.txt†L175-L206】

### Battery & Motor Configuration Notes (Batch 1)
- Example personal builds include dual 1000 W motors on a 15 S 8 P pack with 40 A BMS, and alternate plans for 13 S packs scaling to 15 S later.【F:data/vesc_help_group/text_slices/input_part000.txt†L20-L23】
- VESC platform lacks a native dashboard; riders typically rely on the mobile app or an optional TFT display, though the group finds the official screen bulky and aesthetically unappealing.【F:data/vesc_help_group/text_slices/input_part000.txt†L63-L104】
- Brake sensors are important—without functioning brakes the controller can stutter every 1–2 seconds under throttle.【F:data/vesc_help_group/text_slices/input_part000.txt†L97-L98】
- Rosheee reports voltage spikes above 100 V when running delta windings on a 36 V system and warns that delta + VESC reliability is still unproven; alternate firmware/hardware combinations may mitigate the spikes.【F:data/vesc_help_group/text_slices/input_part000.txt†L112-L119】【F:data/vesc_help_group/text_slices/input_part000.txt†L172-L176】
- Stock Xiaomi/Segway controllers can survive aggressive settings (e.g., battery current ≥56 A) in delta mode but risk failure; multiple ESCs were blown while chasing ~70 km/h on 10 S packs and higher voltage packs (48 V) amplified stress.【F:data/vesc_help_group/text_slices/input_part000.txt†L295-L320】
- Spintend VESC firmware packages: 100 A battery firmware (recommended) and 300 A variant (voids warranty). Battery input apparently capped at 60 A with observed 147 A phase to the motor.【F:data/vesc_help_group/text_slices/input_part000.txt†L190-L197】

### Accessory & UX Considerations (Batch 1)
- Sleep function exists but needs custom wiring to tie into a physical power button; anti-spark switch currently used as a manual cutoff.【F:data/vesc_help_group/text_slices/input_part000.txt†L66-L76】
- Off-the-shelf TFT displays can be zip-tied to stock dashboards or replaced with phone mounts; participants are exploring 3D-printed housings and sturdier auxiliary handlebars for mounting accessories.【F:data/vesc_help_group/text_slices/input_part000.txt†L99-L278】
- Lighting upgrades under evaluation include high-output (3 000–9 000 lm) USB-C rechargeable headlights that double as power banks, programmable LED tail lights, and mirror-mounted 12 V solutions; stock Xiaomi headlights considered underpowered and glaring.【F:data/vesc_help_group/text_slices/input_part000.txt†L207-L258】

### High-End Scooter Upgrades & Rider Safety (Batch 2)
- Rosheee is investing in a Rion RE90 (≈€7 500) and plans mountain climbs; the group questions marketing claims of 400 A per phase and 136 PS motors, citing likely battery limitations and marketing exaggeration.【F:data/vesc_help_group/text_slices/input_part000.txt†L337-L405】
- Import math for the RE90 highlights hidden costs: $6 800 base price rises to €7 500 after 20 % VAT, 6 % customs, and ~$600 shipping, motivating hand-carry or Paris pickup runs to cut duty.【F:data/vesc_help_group/text_slices/input_part000.txt†L410-L434】
- Protective gear recommendations emphasize quality jackets with D3O armor or traditional level-2 padding and Alpinestars-branded protection, underscoring the speed ambitions in the chat.【F:data/vesc_help_group/text_slices/input_part000.txt†L325-L333】
- Rion’s 23 S 6 P (~3 kWh) battery and carbon construction are praised, yet riders acknowledge the platform lacks waterproofing and may need slick tires tailored to dry performance.【F:data/vesc_help_group/text_slices/input_part000.txt†L350-L482】

### Displays, Lighting & Peripherals (Batch 2)
- Spintend is monitoring the group’s feedback and is pivoting toward scooter-specific screens and throttles; Russian-language communities are a key source of technical experimentation.【F:data/vesc_help_group/text_slices/input_part000.txt†L1045-L1049】
- Riders compare display solutions (Davega X, Eye3-compatible ESP32 projects, Flipsky TFT) and debate stealth installs that reuse stock casings for legal compliance.【F:data/vesc_help_group/text_slices/input_part000.txt†L1071-L1149】
- Multiple USB and 12 V headlight candidates are assessed for beam cutoffs, with emphasis on mirror optics to avoid glare and potential integration into existing scooter housings.【F:data/vesc_help_group/text_slices/input_part000.txt†L1113-L1151】
- Ideas for smart dashboards include ESP32-based limit toggles, button combinations to enforce legal speed profiles, and CAN/UART communication trade-offs for reliability under high current noise.【F:data/vesc_help_group/text_slices/input_part000.txt†L2047-L2150】

### Battery Architecture, Cells & Wiring (Batch 2)
- Spintend Ubox incident: a Wolf Warrior 16 S build caught fire during motor wizard setup; Spintend promised warranty replacement and requested motor/battery specs for replication, suggesting a defective B-side MOSFET stage.【F:data/vesc_help_group/text_slices/input_part000.txt†L1159-L1206】
- Francois targets 15 S 6 P Samsung 40T and later 15 S 10 P VTC6 packs to eliminate voltage sag, while others await Samsung 50S cells (5000 mAh, 20 A continuous) despite €6.5+ unit costs through Vapcell rewraps.【F:data/vesc_help_group/text_slices/input_part000.txt†L1207-L2104】
- Detailed pack-layout brainstorming covers 16 S 7 P and 12 S 9 P assemblies, nickel strip cross-sections, and copper busbar “sandwich” welds to sustain 70–80 A continuous draws without overheating.【F:data/vesc_help_group/text_slices/input_part000.txt†L1578-L1784】【F:data/vesc_help_group/text_slices/input_part000.txt†L2089-L2098】
- Community-sourced tables compare connector resistances (XT60/90/150, EC5) and matching AWG limits, prompting rewiring of Ubox leads that ship with 10–12 AWG conductors.【F:data/vesc_help_group/text_slices/input_part000.txt†L2127-L2133】

### Controller Behavior & Diagnostics (Batch 2)
- Riders differentiate sine-wave controllers from full field-oriented control (FOC), noting Xiaomi M365 mods achieved 90 A only with reinforced hardware; FOC’s efficiency gains explain higher top speed and cooler motors on identical battery packs.【F:data/vesc_help_group/text_slices/input_part000.txt†L2003-L2046】
- EMI concerns on UART throttle lines at high phase currents motivate discussion about adding CAN transceivers (e.g., SN65HVD230) for noise immunity in future accessory designs.【F:data/vesc_help_group/text_slices/input_part000.txt†L2047-L2067】
- Troubleshooting a Flipsky 7550 build points to BMS current cutoffs: scooters run fine unloaded but shut down under rider weight; lowering battery current to 30 A fails, suggesting the pack’s protection circuitry is tripping under load.【F:data/vesc_help_group/text_slices/input_part000.txt†L1640-L1686】
- Performance logs show 12 S controllers delivering ~45 km/h on flat ground at 32.5 A, with advice to raise voltage to 15 S and dial back current for better efficiency and cooler operation.【F:data/vesc_help_group/text_slices/input_part000.txt†L1500-L1537】

### Community Logistics & Fitment Tips (Batch 2)
- Discussions cover bearing replacements (6001 rear, 16003 stainless front for Monorim 500 W motor) and tire clearance limits when upsizing to 2.5–3.0 inch rubber on Xiaomi frames.【F:data/vesc_help_group/text_slices/input_part000.txt†L780-L835】
- Ninebot Max and Xiaomi Pro deck extensions accommodate up to 16 S 5 P 21700 packs with ~27 mm spacers; builders trim VESC housings or rotate controllers for cleaner installs.【F:data/vesc_help_group/text_slices/input_part000.txt†L2015-L2085】

### Smart Controller & Display Development (Batch 3)
- Koxx’s ESP32 “smartcontroller” intercepts throttle and brake signals (0–5 V sensors) before forwarding a DAC-shaped 0–3.3 V feed to the VESC, enabling features such as throttle lock-out when the anti-theft beacon is absent and level shifting for MiniMotors EYE throttles that otherwise swing 0.9–4.1 V—above the STM32’s safe range.【F:data/vesc_help_group/text_slices/input_part000.txt†L2430-L2483】
- The next production batch targets a 100 V regulator and native EYE-throttle support; bare-bones DIY kits run ~100 € in parts plus 40 € R&D and 10 € shipping, but require owners to 3D-print enclosures and solder fine-pitch FPC connectors themselves.【F:data/vesc_help_group/text_slices/input_part000.txt†L2522-L2532】【F:data/vesc_help_group/text_slices/input_part000.txt†L3209-L3217】
- Switching to a 3.5″ VA TFT with anti-glare glass dramatically improves sunlight legibility, though the current PNP dimming stage dissipates ~130 mA and raises PCB temps to ~52 °C when idling in the box.【F:data/vesc_help_group/text_slices/input_part000.txt†L3234-L3254】

### Wiring & Power Delivery Notes (Batch 3)
- Never feed VESC ADC inputs directly with 5 V throttle rails; use the 3.3 V reference (or an adapter board) because exceeding 3.3 V can quickly destroy the STM32 ADC despite some Honeywell SS49E throttles preferring 5 V. Deadband or filtering can tame the ~0.02 V noise seen when powering those sensors safely at 3.3 V.【F:data/vesc_help_group/text_slices/input_part000.txt†L2656-L2665】【F:data/vesc_help_group/text_slices/input_part000.txt†L3575-L3599】
- Long power runs on undersized wire add major sag: a 12 S 7 P pack on 4 m of 16 AWG with XT30 connectors dropped ~0.5 V per cell at 40 A; the group recommends shortening 16 AWG tails, upgrading to XT60/XT90 and 10–12 AWG leads, and eliminating extra connectors wherever possible.【F:data/vesc_help_group/text_slices/input_part000.txt†L2676-L2773】
- Spintend’s Ubox arrives with an XT90 battery pigtail but only female motor connectors, so builders plan on swapping to 5.5 mm bullets and trimming excess lead length; routing power cables down one deck side and signal/brake harnesses down the other helps minimise EMI in cramped Vsett installs.【F:data/vesc_help_group/text_slices/input_part000.txt†L3371-L3386】【F:data/vesc_help_group/text_slices/input_part000.txt†L3483-L3486】

### ESC Reliability & Mitigations (Batch 3)
- Multiple Flipsky 7550 controllers stopped spinning motors despite clean detection traces; firmware reflashes and bench tests showed no MOSFET shorts, pointing to dead STM32/USB stages and prompting a community fundraiser plus vendor outreach for replacements.【F:data/vesc_help_group/text_slices/input_part000.txt†L2556-L2635】【F:data/vesc_help_group/text_slices/input_part000.txt†L2748-L2824】
- To shield controller logic from back-EMF spikes when battery cables are long, add low-ESR 470 µF capacitors near the ESC input—Panasonic FM/FR series in parallel offer lower ESR than a single 1000 µF can and help prevent MCU brownouts or failures.【F:data/vesc_help_group/text_slices/input_part000.txt†L3084-L3090】

### Vehicle Setup & Battery Management Highlights (Batch 3)
- A Zero 10X build is running 100 A rear / 60 A front phase limits with 80 A/50 A battery settings, delivering smooth launches and pronounced mid-speed acceleration without excessive motor heat so far.【F:data/vesc_help_group/text_slices/input_part000.txt†L3001-L3019】
- VSETT’s stock controllers taper output whenever pack voltage hits ~52 V (~10 % remaining), effectively lowering the “battery max” current to protect cells from high-resistance heating—a behaviour the group wants to port into VESC firmware for builds lacking smart BMS data.【F:data/vesc_help_group/text_slices/input_part000.txt†L3326-L3334】
- Early Spintend Ubox shakedowns show MOSFET temps climbing to ~50 °C within seconds at 50 A battery draw before the BMS begins limiting; VESC’s default thermal limits are much higher (~80 °C), so riders can safely raise thresholds once pack protection is confirmed.【F:data/vesc_help_group/text_slices/input_part000.txt†L3488-L3524】

### Throttle & Sensor Voltage Safety (Batch 4)
- VESC control logic is referenced to 3.3 V; feeding 5 V hall throttles directly into ADC or UART pins risks exceeding the STM32 absolute maximum (≈4 V on ADC, ≈7.3 V on UART), which has already killed several ESP32-based add-ons.【F:data/vesc_help_group/text_slices/input_part000.txt†L3600-L3655】
- Builders mitigate by powering SS49E throttles from 5 V but dividing the signal down with 1 kΩ/2 kΩ resistors, or by sourcing 3.3 V-friendly sensors; some low-cost throttles produce zero output at 3.3 V and need a level converter instead.【F:data/vesc_help_group/text_slices/input_part000.txt†L3619-L3665】
- Residual 0.15 V noise on scaled signals can be filtered with VESC deadband settings rather than extra capacitors.【F:data/vesc_help_group/text_slices/input_part000.txt†L4194-L4210】

### Thermal Limits & Ubox Performance (Batch 4)
- Spintend’s published defaults start derating at 85 °C MOSFET temperature and shut down at 100 °C, but logs show riders seeing 70–75 °C during long pulls; the underlying FDBL0150N80 devices are rated to 175 °C, so keeping cutback around 100 °C with good frame contact and thermal paste preserves headroom while respecting sensor placement outside the silicon junction.【F:data/vesc_help_group/text_slices/input_part000.txt†L3680-L3708】
- Community acceleration data confirms Ubox builds hitting target speeds quickly, though square-wave Zero 11X controllers running 72 V/55 A still out-launch 60 V Ubox setups until phase current limits are raised; adding active cooling fans is under consideration for enclosed decks.【F:data/vesc_help_group/text_slices/input_part000.txt†L3710-L3764】

### Battery vs Phase Current Insights (Batch 4)
- Artem formalised the relationship `I_phase = I_batt * V_batt / V_motor`, explaining why battery current caps determine how long full phase torque is sustained as motor voltage rises, and why output power cannot exceed the input wattage.【F:data/vesc_help_group/text_slices/input_part000.txt†L3770-L3818】
- Practical takeaway: keep phase current above battery current, and expect battery amps to climb from ~16 A at launch (100 A phase, 10 V back-EMF) toward the configured limit as RPM and motor voltage increase.【F:data/vesc_help_group/text_slices/input_part000.txt†L3786-L3818】

### Cruise Control & Remote Integration (Batch 4)
- VESC Tool lacks native cruise control, but the Spintend handheld remote offers button-activated cruise, light, and horn outputs via its own receiver—reducing wiring runs for throttle, e-brake, lighting, and display cables by consolidating signals through the radio link.【F:data/vesc_help_group/text_slices/input_part000.txt†L3820-L3850】
- Koxx’s smart display firmware could add cruise by locking speed with a button-triggered profile, though the project remains open source and contributions are encouraged.【F:data/vesc_help_group/text_slices/input_part000.txt†L3837-L3844】

### Analog Braking Concepts (Batch 4)
- Most scooter brake levers are digital on/off switches; achieving proportional e-braking requires hall-based sensors such as Xiaomi’s lever or custom SS49E + magnet housings for hydraulic brakes, which the smart display can interpret to blend braking force based on pull speed or throttle position.【F:data/vesc_help_group/text_slices/input_part000.txt†L3880-L3915】

### Battery Experiments & Cell Selection (Batch 4)
- Long-term abuse of 250 W hub motors with 84 V/2 000 W inputs pushed magnets past 80 °C, causing demagnetisation and permanent speed loss—highlighting the need for thermal monitoring on recycled hardware.【F:data/vesc_help_group/text_slices/input_part000.txt†L3944-L3948】
- Builders compare recycled 18650 packs (EVE 26V cells limited to ~5 A each) with new Samsung 35E/50S/48X options, noting 21700 formats pack more energy into Xiaomi decks and that Samsung 50S delivers leading Wh at 15–20 A draws despite high cost.【F:data/vesc_help_group/text_slices/input_part000.txt†L3997-L4053】【F:data/vesc_help_group/text_slices/input_part000.txt†L4054-L4090】

### Aerlang & Legal Modes (Batch 4)
- The Aerlang 500 W scooter pairs a feature-rich 48 V/25 A controller, integrated lighting, NFC alarm, and 17.5 Ah pack for ~€400, but the flat deck plate fatigues and cracks at the neck or rear suspension mounts without reinforcement—making structural upgrades mandatory before exploiting its 45 km/h potential.【F:data/vesc_help_group/text_slices/input_part000.txt†L4120-L4124】
- Its speed limiter toggles via an eight-click sequence, supporting stealth “police mode” profiles that riders aim to replicate on VESC builds to avoid attention while staying within ~35 km/h when necessary.【F:data/vesc_help_group/text_slices/input_part000.txt†L4130-L4178】

### Capacitor Noise Mitigation & Parallel Pack Wiring (Batch 5)
- For throttle signal filtering, builders recommend scavenging ~100 nF ceramics from dead electronics instead of grafting oversized drone capacitors; discharge and meter salvaged parts after removal to confirm capacitance before installing them across signal-to-ground.【F:data/vesc_help_group/text_slices/input_part000.txt†L4211-L4306】
- When paralleling 16 S packs, tie all grounds together, ensure matched cell counts/capacity, pre-balance voltages, and watch for cross-charging to avoid over-stressing the smaller pack despite individual BMS protection.【F:data/vesc_help_group/text_slices/input_part000.txt†L4322-L4383】

### Thermal Interface & Cooling Tweaks (Batch 5)
- Spintend reiterated that stock firmware derates around 75 °C and encouraged extra airflow; swapping thick thermal pads for copper shims with quality paste can cut MOSFET temperatures roughly 20 % when clamped to the deck.【F:data/vesc_help_group/text_slices/input_part000.txt†L4425-L4509】
- Field reports show Ubox channels staying near 45 °C while sustaining ~100 A battery / 130 A phase with those interface mods, and Spintend is preparing a Ubox Pro revision to support 150 A phase with improved EMI isolation.【F:data/vesc_help_group/text_slices/input_part000.txt†L4672-L4687】

### Acceleration Logging & Calibration Practices (Batch 5)
- Riders benchmark 0–70 km/h runs with apps like Dragy/Race Timer, capturing 60 fps footage of calibrated displays and averaging multiple passes in identical conditions to offset GPS lag and accuracy swings.【F:data/vesc_help_group/text_slices/input_part000.txt†L4615-L4641】
- To align VESC telemetry with GPS, set pole counts correctly and measure wheel diameter under rider load (or full wheel circumference), accounting for tyre compression and ensuring the controller’s reported speed slightly exceeds GPS for safety margins.【F:data/vesc_help_group/text_slices/input_part000.txt†L4652-L4671】

### SmartDisplay Roadmap & Boost Logic (Batch 5)
- SmartDisplay firmware already offers 25/35/unlimited speed slots and is slated for user-configurable limits plus legal/eco/normal/boost profiles that scale current (e.g., eco at 0.6× phase, 0.7× battery) and gate the temporary boost via MOSFET temperature warnings.【F:data/vesc_help_group/text_slices/input_part000.txt†L4562-L4596】

### Troubleshooting & Repair Lessons (Batch 5)
- Diagnosing no-power VESCs centers on checking LDO regulators and supply rails; careless probing can arc and vaporize PCB traces, so the group now solders test pigtails or uses current-limited supplies before measuring sensitive components.【F:data/vesc_help_group/text_slices/input_part000.txt†L5000-L5075】

### Battery Current Guidance for 16 S Builds (Batch 5)
- A 16 S 5 P Samsung 35E pack should be capped near 40 A continuous (50 A short bursts) with phase current around 110–125 A and ABS max at 180 A; regen targets stay below ~7 A battery / 15 A motor to protect cells while FOC keeps motor temps manageable.【F:data/vesc_help_group/text_slices/input_part000.txt†L5203-L5400】

### Shipping & Accessory Insights (Batch 5)
- Spintend direct orders often arrive in the EU declared as sub-$30 “electric speed controllers,” avoiding VAT when sent by postal carriers, and their remote consolidates throttle, brake, horn, light, and ABS/regen controls to minimize wiring.【F:data/vesc_help_group/text_slices/input_part000.txt†L4950-L4964】【F:data/vesc_help_group/text_slices/input_part000.txt†L5808-L5841】

### Shipping, Drop-in Kits & Cell Sourcing (Batch 6)
- Bulk orders of Samsung 50S 21700 cells can be arranged for about €4.71 each (≈15 % less when bypassing eBay/PayPal fees), providing an avenue for high-discharge pack builds if buyers are comfortable coordinating the shared purchase.【F:data/vesc_help_group/text_slices/input_part000.txt†L6433-L6434】
- The Smart+Eye drop-in kit targets riders who want VESC functionality without rewiring controls; the finger-throttle/display bundle keeps labour to €100–150 versus €350–400 for full custom wiring despite ergonomic compromises.【F:data/vesc_help_group/text_slices/input_part000.txt†L6428-L6440】

### Battery Waterproofing & Diagnostics Lessons (Batch 6)
- Rain-soaked packs can confuse Daly BMS readings without tripping output, so riders now fully open enclosures, dry balance harnesses, and reinforce future builds with layered fish paper, waterproof tape, silicone sealant, and desiccant bags to prevent repeat moisture faults.【F:data/vesc_help_group/text_slices/input_part000.txt†L6512-L6599】

### Brake Sensor Experiments & Compatibility (Batch 6)
- Builders are prototyping progressive regen by pairing hydro levers with hall-effect pots or magnets, noting Xiaomi’s stock lever already outputs a smooth analog signal even if the plastic hardware feels flimsy.【F:data/vesc_help_group/text_slices/input_part000.txt†L7201-L7246】
- Spintend’s €10 ADC board supports switch- or pot-based levers at 3.3 V or 5 V logic; Magura MT5e buyers should choose the normally-open (HIGO “closer”) lever variant to match the expected brake input behaviour.【F:data/vesc_help_group/text_slices/input_part000.txt†L8270-L8294】

### Regen & Control Tuning Cautions (Batch 6)
- Bench-testing regen on ADC2 with modest -15 A motor / -5 A battery limits still tripped a VESC shutdown, reinforcing earlier warnings about voltage spikes when spinning wheels unloaded.【F:data/vesc_help_group/text_slices/input_part000.txt†L7299-L7313】
- Artem reiterated that phase current sets launch torque while battery amps cap how long that thrust lasts; as battery voltage droops, available watts shrink and the controller must taper phase amps once motor voltage exceeds the battery watt ceiling.【F:data/vesc_help_group/text_slices/input_part000.txt†L8037-L8099】

### Spintend Roadmap & Smart Integration (Batch 6)
- The upcoming Spintend single (target <€180) carries separate logic/power boards, IMU support, ~75 V/100 A specs, and lessons from the dual Ubox—while transparent BLE passthrough now lets the SmartDisplay act as a USB dongle for Android VESC Tool, easing diagnostics on controllers without onboard Bluetooth.【F:data/vesc_help_group/text_slices/input_part000.txt†L7733-L7772】【F:data/vesc_help_group/text_slices/input_part000.txt†L8005-L8013】【F:data/vesc_help_group/text_slices/input_part000.txt†L8227-L8236】

### Procurement & VAT Changes (Batch 7)
- EU’s July 2021 VAT reform pushed marketplaces such as AliExpress to adopt IOSS collection, adding ~21 % tax at checkout but eliminating the €24+ handling fees postal carriers were charging on arrival—making direct imports simpler even though sticker prices rise.【F:data/vesc_help_group/text_slices/input_part000.txt†L8321-L8332】
- Members are lobbying Spintend for a companion BMS and coordinating comments on the esk8.news thread so the vendor can gauge demand for a matched battery management stack.【F:data/vesc_help_group/text_slices/input_part000.txt†L8333-L8338】

### Battery Limit Modeling & Hardware Expectations (Batch 7)
- Artem shared comparative charts that visualise how raising battery current extends the RPM range where full phase torque is sustained, reiterating the `V_batt × I_batt = V_motor × I_phase` trade-off and noting higher battery limits add motor heat from I²R losses even as top speed improves.【F:data/vesc_help_group/text_slices/input_part000.txt†L8340-L8367】
- Spintend’s forthcoming single controller remains unreleased—once the beta is official they plan to clarify pricing and warranty terms, but expectations are for parity with the production dual given the company’s past support track record.【F:data/vesc_help_group/text_slices/input_part000.txt†L8373-L8378】
- Supply updates later in the thread confirm the single’s casing delay pushed availability toward mid-July, so builders are planning interim options accordingly.【F:data/vesc_help_group/text_slices/input_part000.txt†L9030-L9033】

### Brake Hardware & Rotor Sizing Debates (Batch 7)
- Magura’s CMe5 hydraulic lever works cleanly with VESC braking without needing ABS-specific wiring, offering a sturdier metal assembly than MT5e plastics for those chasing analog brake feel.【F:data/vesc_help_group/text_slices/input_part000.txt†L8384-L8385】
- A spirited comparison of 140 mm versus 160 mm rotors highlights that Rion scooters lack e-brakes and run small discs, leading to fade after just a couple of hot laps; riders who tracked with 160 mm MDR-C rotors saw them glowing red and temporarily losing bite, reinforcing the need for larger or vented hardware at >100 km/h speeds.【F:data/vesc_help_group/text_slices/input_part000.txt†L8888-L8951】
- Carbon-Ti’s 160 mm vented rotor offers better airflow than Magura’s MDR-C but costs ~€160 each, so some builders are balancing price against heat rejection when upgrading heavy scooters.【F:data/vesc_help_group/text_slices/input_part000.txt†L8943-L8957】

### Ninebot Max Rental Platform Insights (Batch 7)
- Rental-spec G30 Max frames ship with dual mechanical brakes and thicker swingarms yet still accept 1200 W hub motors without adapters, letting builders preserve both brakes while upgrading powertrains.【F:data/vesc_help_group/text_slices/input_part000.txt†L8763-L8777】
- The ex-rental battery module is a 6 P pack using 2 500 mAh cells (≈15 Ah) secured with extensive silicone and hidden screws; once opened, cells tested around 2 700 mAh and the deck includes a remote-controlled latch so fleet techs can hot-swap packs quickly.【F:data/vesc_help_group/text_slices/input_part000.txt†L8788-L8796】【F:data/vesc_help_group/text_slices/input_part000.txt†L9201-L9227】

### Controller & BMS Alternatives (Batch 7)
- ENNOID is testing a 100 V/75 A ESC measuring roughly 70 mm × 75 mm × 16 mm—compact enough for tight decks but expected to cost about $200 given the brand’s premium BMS line.【F:data/vesc_help_group/text_slices/input_part000.txt†L8396-L8403】
- Riders weighing 16 S builds but balking at VESC pricing are evaluating Minimotors’ 60 V/30 A controllers (smaller housings, no hall sensors) and Kaboo-branded units, though tax and shipping push landed cost near €150—comparable to entry-level VESC hardware.【F:data/vesc_help_group/text_slices/input_part000.txt†L9140-L9187】
- Space-constrained decks like the Boosted Rev are trending toward charge-only BMS boards plus external fusing because Ant BMS models with Bluetooth are too tall; Daly’s slimline 120 A 16 S variant fits with a ~20–25 mm enclosure extension, while touchscreen “smart” BMS units add valuable telemetry at the cost of significant bulk.【F:data/vesc_help_group/text_slices/input_part000.txt†L9229-L9269】【F:data/vesc_help_group/text_slices/input_part000.txt†L9380-L9411】【F:data/vesc_help_group/text_slices/input_part000.txt†L9404-L9406】

### SmartDisplay Manufacturing Status (Batch 7)
- Community testing suggests the Flipsky TFT V2 (a Davega-inspired clone) misbehaves on Spintend Ubox setups, so riders are advised to limit trials to scooters with large (>255 mm) wheels until compatibility issues are solved.【F:data/vesc_help_group/text_slices/input_part000.txt†L9320-L9323】
- Koxx released the full STL set for the SmartDisplay v2 enclosure and control buttons, enabling resin-print runs while the team finalises PCB sourcing through JLCPCB (all components secured except the temperature/humidity sensor).【F:data/vesc_help_group/text_slices/input_part000.txt†L9342-L9364】

### Battery Pack Fabrication & Cell Selection (Batch 7)
- Custom battery efforts lean on PETG honeycomb holders modeled in Tinkercad and printed on tuned Ender machines; builders share STL designs and offer to draft bespoke layouts for Boosted and Ninebot packs.【F:data/vesc_help_group/text_slices/input_part000.txt†L9412-L9434】【F:data/vesc_help_group/text_slices/input_part000.txt†L9440-L9458】
- Artem recommends forming 2 S 6 P blocks with 25 mm nickel strip, welding each layer before folding to minimise resistance, shorten BMS leads, and cut voltage sag versus stitching narrower strips; he also linked cost-effective 25 mm pure nickel stock for large packs.【F:data/vesc_help_group/text_slices/input_part000.txt†L9716-L9731】【F:data/vesc_help_group/text_slices/input_part000.txt†L9723-L9726】
- Linked tutorials and ongoing debates weigh 18650 versus 21700 formats: VTC6 18650 cells deliver higher Wh/L in cramped decks and tolerate triple the current of Samsung 35E, while 21700 formats (40T, P42A, 50E/G) run cooler at high amperage but consume more volume—underscoring the need to match cell choice to available space and current draw.【F:data/vesc_help_group/text_slices/input_part000.txt†L9752-L9820】

### Battery Geometry & Cell Selection Debates (Batch 8)
- Builders compared 6 P 21700 layouts against 7 P 18650 packs and stressed evaluating watt-hours instead of amp-hours when space is constrained, pointing newcomers to Lygte discharge curves and recommending ≤0.25 C charging for longevity regardless of cell size.【F:data/vesc_help_group/text_slices/input_part000.txt†L9821-L9860】
- Artem steered 12 S 5 P high-amp projects toward Samsung 48X or LG 50G cells (≈75 A continuous, 100 A peak) while warning that Samsung 50E chemistry overheats past 10–12 A per cell and thus suits range builds more than performance scooters.【F:data/vesc_help_group/text_slices/input_part000.txt†L10442-L10451】【F:data/vesc_help_group/text_slices/input_part000.txt†L10474-L10485】

### Pack Layout, Charging & Wiring Tips (Batch 8)
- A spacer-equipped M365 Pro deck can host 12 S 5 P 21700 cells stood vertically, letting riders chase higher discharge packs without abandoning the stock chassis footprint.【F:data/vesc_help_group/text_slices/input_part000.txt†L10452-L10456】
- Artem prefers 4 mm or twin 3 mm solid-core leads on the long battery-to-BMS run to cut resistance, noting that ampacity tables often assume kilometre-long multi-strand looms and therefore undersell what short, dense conductors can safely deliver in scooters.【F:data/vesc_help_group/text_slices/input_part000.txt†L10539-L10551】

### SmartDisplay Supply Chain & Enclosure Plans (Batch 8)
- With the AliExpress TFT supplier nearly out of stock, Koxx is contacting the upstream manufacturer for a 20-unit batch while the group explores CNC, sheet-metal pressing, and composite filaments to ship premium aluminium or bronze SmartDisplay housings without ballooning labour costs.【F:data/vesc_help_group/text_slices/input_part000.txt†L9926-L9967】

### Delta Rewiring Experiments & Controller Limits (Batch 8)
- Delta-wound rental hub experiments pushed 16 S builds to 91 km/h before cooking a G30 controller, reinforcing that factory boards survive only to ~15 S and that the community still needs logged torque/speed graphs to gauge delta’s efficiency versus star wiring at high voltage.【F:data/vesc_help_group/text_slices/input_part000.txt†L10021-L10033】

### Spintend CAN Fault Case Study (Batch 8)
- Rowan’s dual-Spintend setup lost one internal CAN transceiver and the other’s soft-power latch; Artem suspects the controllers were powered asymmetrically so current back-fed through the CAN harness, underscoring the need to share ground and avoid hot-plugging linked VESCs separately.【F:data/vesc_help_group/text_slices/input_part000.txt†L10290-L10340】

### Rental Deck Modding & Lock Integration Ideas (Batch 8)
- SNSC/Ninebot builders are carving deck edges, relocating BMS boards, and experimenting with 5 V servo locks tied to VESC aux outputs to retain swappable fleet latches while improving waterproofing—though some still default to sealing the hatch for reliability.【F:data/vesc_help_group/text_slices/input_part000.txt†L11232-L11312】

### Spintend Single Ubox Launch & Voltage Limits (Batch 9)
- Spintend opened beta sales of a $150 single-channel Ubox with built-in antispark, giving builders a cheaper path to 75 V/100 A hardware while the dual remains pricier and often back-ordered.【F:data/vesc_help_group/text_slices/input_part000.txt†L11322-L11336】【F:data/vesc_help_group/text_slices/input_part000.txt†L11712-L11760】
- Contributors reiterated that the beta hardware cannot be modded for 20 S packs because multiple subsystems—shunt amplifiers, latch logic, and MOSFET choices—top out around 75 V despite some regulators supporting 100 V.【F:data/vesc_help_group/text_slices/input_part000.txt†L11374-L11394】

### Xiaomi Deck Mounting & Control Wiring Tips (Batch 9)
- Xiaomi/Ninebot decks are double-walled around the controller cavity; owners have successfully tapped one wall for threads or bonded studs with epoxy when mounting accessories, but many still prefer external nuts for strength.【F:data/vesc_help_group/text_slices/input_part000.txt†L11337-L11352】
- Shielding the combined ADC/UART harness and tying the braid to ground eliminates throttle noise and keeps VESC UART reliable at 115200 baud even with 120 A phase settings—handy for scooters that route long signal runs.【F:data/vesc_help_group/text_slices/input_part000.txt†L11381-L11386】

### SmartDisplay USB Failure Case & Ubox Build Quality (Batch 9)
- Plugging a SmartDisplay’s USB into a computer while the linked Ubox remained battery-powered nuked the controller’s 3.3 V rail and possibly the STM32, prompting a hard warning to avoid USB tethering and stick to BLE/Wi-Fi debugging unless the VESC is already sequenced on.【F:data/vesc_help_group/text_slices/input_part000.txt†L11633-L11707】
- Post-mortem photos highlight hand-soldered power stages and unclear 3.3 V regulation paths on the affected Ubox, underscoring both the repair difficulty and variability in assembly quality on early production runs.【F:data/vesc_help_group/text_slices/input_part000.txt†L11650-L11687】

### EU Shipping & VAT Expectations (Batch 9)
- Since the July 2021 IOSS changes, EU buyers report couriers like FedEx/UPS always collecting VAT plus handling fees, whereas EMS/postal channels still occasionally slip through but can be rerouted via DHL Global Mail; anything over 150 € now skips pre-paid VAT and risks customs delays.【F:data/vesc_help_group/text_slices/input_part000.txt†L11714-L11866】

### Battery Cell Procurement & Validation (Batch 9)
- 13 S 5 P packs built from NCR21700A cells fit tightly inside rental decks, offering premium range if you accept the expense and vertical cell orientation.【F:data/vesc_help_group/text_slices/input_part000.txt†L11454-L11476】
- A delayed NKON shipment arrived with scuffed tops and tab marks, leading veterans to suspect refurbished stock and recommend IR/capacity checks with multi-bay testers like the XTAR VC8 before paying.【F:data/vesc_help_group/text_slices/input_part000.txt†L11756-L11818】
- Sourcing remains volatile: Chinese wholesalers are quoting Samsung 50G/48X around 4.8–5.1 € per cell, while 21700 pricing now rivals 18650 options on a per-cell basis.【F:data/vesc_help_group/text_slices/input_part000.txt†L12224-L12229】【F:data/vesc_help_group/text_slices/input_part000.txt†L12194-L12217】

### Pack Builds & Parallel BMS Lessons (Batch 9)
- Running stock MJ1 packs in parallel with auxiliary MH1 bricks can trip SmartBMS short-circuit thresholds (e.g., 115 A) during throttle spikes, so tuners should align current limits and watch for reverse-charge imbalances between disparate chemistries.【F:data/vesc_help_group/text_slices/input_part000.txt†L11827-L11853】
- Builders debating interim 12 S limits on 13 S packs were reminded to raise low-voltage cutoffs (≈39 V) to protect the higher-series battery when spoofing controller voltage assumptions.【F:data/vesc_help_group/text_slices/input_part000.txt†L11837-L11855】

### Legal Profiles & Throttle Scaling Strategies (Batch 9)
- VESC stores only one persistent “default” profile; higher-power modes live in RAM until reboot, so keeping the legal tune as the saved configuration plus BLE pairing prevents officers from toggling modes roadside.【F:data/vesc_help_group/text_slices/input_part000.txt†L12160-L12188】
- Riders chasing dual throttle behaviour (e.g., torque sensor vs thumb throttle) can hardware-scale voltages with resistors or use separate ADC channels, though ADC3 currently requires firmware/tool changes to enable.【F:data/vesc_help_group/text_slices/input_part000.txt†L12172-L12190】

### Motor Current Tuning & Brake Outputs (Batch 9)
- Artem suggests seeding current limits by dividing motor wattage by 10 for phase amps, capping battery amps at roughly two-thirds of that, and adjusting both by equal percentages to trade launch torque against heat—keeping high-power Ubox builds balanced around 120 A phase/74–80 A battery on 1.2 kW hubs.【F:data/vesc_help_group/text_slices/input_part000.txt†L12491-L12510】
- Ubox users report rumours that the legacy PPM pin can be remapped as a DAC brake-light output on 75/300-based boards, though maintainers have yet to confirm firmware support.【F:data/vesc_help_group/text_slices/input_part000.txt†L12500-L12512】

### SmartDisplay Hardware Updates & Expansion Buses (Batch 9)
- The single-core Spintend lacks onboard Bluetooth, making SmartDisplay’s BLE passthrough or external dongles essential if you avoid direct USB while powered; its CAN lead also includes power, so Spintend support is being consulted on safe dual-controller hookups.【F:data/vesc_help_group/text_slices/input_part000.txt†L12516-L12541】
- Internally the SmartDisplay relies on I²C plus a custom one-wire expansion bus, which tolerates long cable runs better than I²C and is earmarked for future accessory keypads or signal breakout boards.【F:data/vesc_help_group/text_slices/input_part000.txt†L12536-L12547】

### Regen Over-Voltage Hardware (Batch 9)
- Spintend’s new rheostatic braking module can sink roughly 10 A of regen current when pack voltage spikes, trimming what the battery and controller must absorb during hard stops on high-voltage scooters.【F:data/vesc_help_group/text_slices/input_part000.txt†L12811-L12820】

### Regen Braking Heat Limits on VESC Hardware (Batch 10)
- Artem reminded builders that if the battery cannot absorb regen energy, the braking current is converted to MOSFET heat, so aggressive regen without a dump load can still cook the controller despite the pack being safe.【F:data/vesc_help_group/text_slices/input_part000.txt†L12821-L12821】

### Vsett Hub Temperature Sensor Retrofit (Batch 10)
- Detailed the three-hour process for adding a temp probe inside a tightly packed Vsett hub: document the stock wiring, desolder and fan out the stator strands, cut a groove in the insulation jacket, seat one sensor lead in the groove before shrinking, solder the twisted fan-outs, then sleeve the repair with high-voltage loom to keep the harness from binding in the axle.【F:data/vesc_help_group/text_slices/input_part000.txt†L12880-L12896】

### Mixed Brake Sensor Compatibility (Batch 10)
- Running a hall-based Xiaomi lever alongside a normally-open hydraulic switch on the same ADC input yields mismatched behaviour (progressive vs. on/off); the group advised using only the hall lever or adding a hall sensor to the hydraulic brake instead of mixing signal types.【F:data/vesc_help_group/text_slices/input_part000.txt†L12911-L12949】

### Plexiglass Deck Covers & Load Limits (Batch 10)
- A 6 mm laser-cut acrylic deck plate can survive light riders when backed by foam and cell supports, but others reported the material fractures under heavier loads, suggesting plexiglass lids remain a prototype-only solution.【F:data/vesc_help_group/text_slices/input_part000.txt†L12963-L12982】【F:data/vesc_help_group/text_slices/input_part000.txt†L12973-L12980】

### Spintend Single-Core Thermal Logs (Batch 10)
- First rides on the single-channel Spintend at 120 A phase / 80 A battery pushed a 750 W Boosted hub to ~80 °C in under ten minutes while the controller held ~55 °C, confirming the motor—not the ESC—is the bottleneck at that tune.【F:data/vesc_help_group/text_slices/input_part000.txt†L13166-L13178】
- Follow-up data logging showed the VESC clamps duty cycle once the motor NTC hits its limit and that hard regen events add several degrees of heat, prompting plans to retest at 100/50, 90/45, and 80/40 A to balance speed and temps.【F:data/vesc_help_group/text_slices/input_part000.txt†L13299-L13325】

### Quick Current-Limit Heuristics (Batch 10)
- Artem proposed a beginner formula: start with motor rated watts ÷ 10 for both phase and battery amps (e.g., 750 W ≈ 75 A), then raise one limit only if the other is reduced by the same percentage to keep heat constant—though veterans cautioned to validate against real thermal logs.【F:data/vesc_help_group/text_slices/input_part000.txt†L13224-L13236】
- He also restated the fundamental balance that battery voltage × battery current must equal motor voltage × phase current, meaning low battery limits choke phase amps at higher duty and explain why acceleration falls off as speed rises.【F:data/vesc_help_group/text_slices/input_part000.txt†L13334-L13375】

### Pack Rehabilitation & Cell Testing (Batch 10)
- Builders reviving old packs urged capacity and IR testing on every cell, noting imbalance issues when a single weak parallel cell siphons charge from its peers during storage; tools like XTAR VC8s or custom dischargers help flag suspect groups before rebuilding.【F:data/vesc_help_group/text_slices/input_part000.txt†L13046-L13079】【F:data/vesc_help_group/text_slices/input_part000.txt†L13569-L13709】

### Insulation Materials & Fish Paper Debate (Batch 10)
- Koxx’s 14 S 6 P build used Repackr groupings plus hot-glued, fish-paper-wrapped p-groups due to the Boosted deck’s tight tolerances, sparking discussion about whether to double-layer insulation in cramped stacks.【F:data/vesc_help_group/text_slices/input_part000.txt†L13480-L13541】
- Others pitched recyclable kraftplex jackets, but Artem reiterated that any series stack lacking fish paper or holders risks can-to-can shorts because the cell shell is negative, so at minimum insulate between series rows.【F:data/vesc_help_group/text_slices/input_part000.txt†L13506-L13533】

### Nucular Controller Availability Warnings (Batch 10)
- The group flagged that Nucular’s high-power controllers aren’t VESC-compatible, ship extremely slowly, and have seen repeated price hikes—one buyer cancelled after 18 months of delays—so builders should temper expectations before switching ecosystems.【F:data/vesc_help_group/text_slices/input_part000.txt†L13605-L13619】

## Open Questions / Follow-ups
- Validate whether the 20% Flipsky code can be shared or must be redeemed by the original account holder.【F:data/vesc_help_group/text_slices/input_part000.txt†L147-L152】
- Document wiring steps to integrate the VESC sleep function with the scooter’s stock power button and headlights.【F:data/vesc_help_group/text_slices/input_part000.txt†L66-L109】【F:data/vesc_help_group/text_slices/input_part000.txt†L1113-L1151】
- Gather delta-winding reliability data on VESC hardware, especially regarding voltage spikes and firmware choices (Spintend vs. stock).【F:data/vesc_help_group/text_slices/input_part000.txt†L112-L197】
- Confirm whether the observed Flipsky 7550 cutouts stem from BMS limits or controller faults and capture the eventual fix for reference.【F:data/vesc_help_group/text_slices/input_part000.txt†L1640-L1686】
- Track Spintend’s scooter-focused display/throttle roadmap and any firmware updates that add CAN bus support for noise resilience.【F:data/vesc_help_group/text_slices/input_part000.txt†L1045-L1049】【F:data/vesc_help_group/text_slices/input_part000.txt†L2047-L2067】
- Record real-world fitment data for 16 S 5 P 21700 packs and corresponding deck modifications (spacer heights, enclosure reinforcements).【F:data/vesc_help_group/text_slices/input_part000.txt†L2015-L2085】
- Prototype and validate the recommended low-ESR capacitor add-on for long cable runs, documenting values, placement, and thermal impact.【F:data/vesc_help_group/text_slices/input_part000.txt†L3084-L3090】
- Explore how to replicate VSETT’s low-voltage power tapering inside VESC Tool so battery stress cues remain without smart BMS telemetry.【F:data/vesc_help_group/text_slices/input_part000.txt†L3326-L3334】
- Quantify how much the copper-shim thermal mod and future Ubox Pro revisions extend sustained current limits versus stock pads or firmware settings.【F:data/vesc_help_group/text_slices/input_part000.txt†L4425-L4431】【F:data/vesc_help_group/text_slices/input_part000.txt†L4672-L4687】
- Capture delta-versus-star performance logs (torque, efficiency, controller temps) once the rewound hub kits are ready so builders can judge when the conversion justifies the extra thermal stress.【F:data/vesc_help_group/text_slices/input_part000.txt†L10018-L10025】
