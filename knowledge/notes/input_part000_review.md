# input_part000.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part000.txt`
- Coverage:
  - Batch 1: 2021-04-02 23:23:16 through 2021-04-03 01:46:36 (lines 1-320)
  - Batch 2: 2021-04-03 01:46:51 through 2021-05-18 17:49:41 (lines 321-2400)
  - Batch 3: 2021-05-18 17:50:23 through 2021-05-28 19:56:29 (lines 2401-3600)
  - Batch 4: 2021-05-28 19:56:29 through 2021-05-31 00:01:06 (lines 3601-4210)
  - Batch 5: 2021-05-31 00:01:07 through 2021-06-17 16:13:29 (lines 4211-6400)
  - Batch 6: 2021-06-17 16:13:29 through 2021-06-27 14:36:28 (lines 6401-7900)
  - Batch 7: 2021-06-27 14:37:07 through 2021-07-12 20:29:50 (lines 7901-9400)
  - Batch 8: 2021-07-12 20:30:16 through 2021-07-26 09:10:08 (lines 9401-10900)
  - Batch 9: 2021-07-26 09:10:55 through 2021-08-16 19:05:34 (lines 10901-12400)
  - Batch 10: 2021-08-16 19:05:52 through 2021-08-23 13:52:48 (lines 12401-13900)
  - Batch 11: 2021-08-23 13:52:58 through 2021-08-29 18:33:32 (lines 13901-15400)
  - Batch 12: 2021-08-29 18:33:41 through 2021-09-07 23:42:47 (lines 15401-16900)
  - Batch 13: 2021-09-07 23:43:11 through 2021-09-20 14:32:21 (lines 16901-18400)
  - Batch 14: 2021-09-20 14:32:25 through 2021-10-03 17:05:35 (lines 18401-19900)
  - Batch 15: 2021-10-03 17:06:12 through 2021-10-21 10:55:08 (lines 19901-21400)
  - Batch 16: 2021-10-21 10:55:20 through 2021-10-30 20:39:35 (lines 21401-22900)
  - Batch 17: 2021-10-30 14:12:00 through 2021-11-10 12:40:52 (lines 22901-24400)
  - Batch 18: 2021-11-10 12:42:59 through 2021-11-19 20:49:20 (lines 24401-25900)
  - Batch 19: 2021-11-19 20:50:13 through 2021-12-09 15:08:50 (lines 25901-27400)
  - Batch 20: 2021-12-09 15:08:59 through 2021-12-19 16:01:42 (lines 27401-28024)
  - Next starting point: line 28025 (file fully reviewed)

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
- Its firmware is read/write encrypted, leaving shunt tweaks as the only viable stock-controller mod and steering tinkerers toward full controller swaps when they need custom logic.【F:data/vesc_help_group/text_slices/input_part000.txt†L4140-L4144】
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

### Bulk Cell Deals & Drop-In Kits (Batch 6)
- Tudor flagged how AliExpress motor bundles can tack on £163 of “standard” shipping to a £405 dual-hub order—costlier than flying to pick them up—making it essential to haggle with sellers or freight forwarders before paying list freight quotes.【F:data/vesc_help_group/text_slices/input_part000.txt†L6404-L6429】
- Artem lined up a group buy for Samsung 50S 21700 cells at €4.71 each (with the potential for ~15 % savings outside of eBay/PayPal), giving high-discharge pack builders a vetted source if they coordinate payment protections.【F:data/vesc_help_group/text_slices/input_part000.txt†L6433-L6434】
- Koxx’s Smart+Eye drop-in kit keeps stock controls while swapping in VESC brains; even if riders dislike the side-mounted finger throttle, the €100–150 install cost massively undercuts the €350–400 in labour for a full custom loom.【F:data/vesc_help_group/text_slices/input_part000.txt†L6438-L6440】

### Battery Waterproofing & Daly BMS Moisture Recovery (Batch 6)
- A rain-soaked Daly smart BMS began reporting 5 V on random groups despite balanced cells; Mirono advised fully opening the pack, drying the balance harness with hot air, and even dunking the board in isopropyl before resealing because the unit is potted except for its lead entry points.【F:data/vesc_help_group/text_slices/input_part000.txt†L6520-L6620】
- His preferred rebuild recipe now layers fish paper, five wraps of waterproof tape, outer shrink, silicone on every seam, and silica-gel packs to keep future condensation from dragging cells to 3.1 V or latching the discharge FETs off.【F:data/vesc_help_group/text_slices/input_part000.txt†L6534-L6556】【F:data/vesc_help_group/text_slices/input_part000.txt†L6561-L6569】
- After repeated hair-dryer cycles and airing the BMS overnight, the pack resumed normal balancing—reinforcing the need for full waterproofing before field tests even if the enclosure bag claims to be sealed.【F:data/vesc_help_group/text_slices/input_part000.txt†L6800-L6838】

### Range Extensions & Cargo Concepts (Batch 6)
- Mirono’s latest 3D-printed deck extender houses 260 cells (e.g., 15 S 17 P) so he can attempt a 120 km ride to the coast on one charge, while others joked about the 600 A peaks such a pack could supply.【F:data/vesc_help_group/text_slices/input_part000.txt†L6888-L6902】
- The group is also prototyping cargo trailers for battery transport; one rider logged 2 A at 36 V from an 80 W folding solar panel and another is mapping a 500 km Bonn-to-coast ride, reinforcing that staged charging and swappable packs make long tours viable.【F:data/vesc_help_group/text_slices/input_part000.txt†L6926-L6935】【F:data/vesc_help_group/text_slices/input_part000.txt†L6903-L6930】
- Ninebot Max frames remain desirable donors because they swallow 50 Ah 10 S packs or even 15 S 4 P 21700 arrays once controllers are relocated, giving ample room for long-range builds.【F:data/vesc_help_group/text_slices/input_part000.txt†L6852-L6859】【F:data/vesc_help_group/text_slices/input_part000.txt†L6860-L6863】

### Motor & Controller Performance Notes (Batch 6)
- Luis’s 54 Ah pack and dual Minimotors controllers managed ~90 km at 38 km/h, but he acknowledged VESC tuning is more conservative with energy while Vsett 10+ owners see 77–82 km/h in turbo with 30–35 A sine-wave controllers.【F:data/vesc_help_group/text_slices/input_part000.txt†L6463-L6470】【F:data/vesc_help_group/text_slices/input_part000.txt†L6470-L6475】
- Riders pushing 2000 W hub motors noted they warm after 3 km at 60 A battery / 100 A phase and are planning 3000 W swaps to sustain 3000–4000 W bursts without cooking the stator.【F:data/vesc_help_group/text_slices/input_part000.txt†L6977-L6986】
- Face de Pin Sucé’s Dualtron Spider conversion runs 135 A motor / 35 A battery per channel with 100 A regen per motor, highlighting how easily stock packs sag when asked for 260 A combined bursts.【F:data/vesc_help_group/text_slices/input_part000.txt†L7519-L7535】

### Smart BMS Diagnostics & Precharge Settings (Batch 6)
- Recovering from the regen-induced shutdown, Luis measured about 19.9 kΩ across the Ubox input, noted the controller blinking undervoltage while powered from 8–15 V bench packs, and ultimately had to enable the smart-BMS discharge MOSFET before connection and raise pre-charge to 40 A for his 35 Ah 16 S pack to pass startup self-tests.【F:data/vesc_help_group/text_slices/input_part000.txt†L7401-L7419】【F:data/vesc_help_group/text_slices/input_part000.txt†L7413-L7418】

### Brake Lever Sensors & Upgrade Paths (Batch 6)
- The Magura MT5e lever still ships with an on/off microswitch, so the group is eyeing Shimano Deore M6100/M6120 kits (~€124–€170 pre-bled) and plotting hall-effect potentiometer mods epoxied to the lever arm for progressive regen input.【F:data/vesc_help_group/text_slices/input_part000.txt†L7100-L7179】【F:data/vesc_help_group/text_slices/input_part000.txt†L7180-L7212】
- Measuring lever output requires feeding 5 V to the hall sensor and reading the signal wire—multimeters alone won’t show activity without powering the circuit.【F:data/vesc_help_group/text_slices/input_part000.txt†L7281-L7291】

### Regen Safety & Configuration Lessons (Batch 6)
- A bench test using ADC2 for braking at just -15 A motor / -5 A battery repeatedly tripped a Spintend Ubox, confirming that unloaded wheels can generate lethal back-EMF; both Mirono and Koxx have already blown bench supplies experimenting with regen on high-voltage Xiaomi mods.【F:data/vesc_help_group/text_slices/input_part000.txt†L7299-L7345】
- Artem recommends capping battery regen to the pack’s amp-hour value (e.g., 50 A for 50 Ah) and keeping controller “reverb” about 15 A above that so excess energy is shed as heat through the FETs instead of into the cells.【F:data/vesc_help_group/text_slices/input_part000.txt†L7426-L7434】
- Discussion of laboratory power supplies lacking internal resistance explained why back-EMF spikes can exceed the applied voltage, reinforcing the need for real batteries or load banks when testing regen settings.【F:data/vesc_help_group/text_slices/input_part000.txt†L7360-L7372】

### Spintend Single Roadmap & Fitment Notes (Batch 6)
- Artem previewed the Ubox Pro refresh: dual 100 V channels rated for at least 150 A phase with five independent 12 V outputs for lights, horn, and signals—still similar in size but far sturdier on back-EMF thanks to separated logic/power boards.【F:data/vesc_help_group/text_slices/input_part000.txt†L7440-L7444】【F:data/vesc_help_group/text_slices/input_part000.txt†L7763-L7772】
- The forthcoming single-channel unit should measure roughly 85 mm × 54 mm (with mounts), target sub-€180 pricing, include an IMU, and may move the USB port to an external pigtail so tight decks can keep the lid closed during tuning.【F:data/vesc_help_group/text_slices/input_part000.txt†L7442-L7459】【F:data/vesc_help_group/text_slices/input_part000.txt†L7732-L7771】
- Community support for Spintend remains high because of responsive warranty service and spare power/logic boards, contrasting sharply with frustration over Flipsky QC and table-only “reviews.”【F:data/vesc_help_group/text_slices/input_part000.txt†L7722-L7735】【F:data/vesc_help_group/text_slices/input_part000.txt†L7713-L7729】

### Dualtron Spider Rigidity Observations (Batch 6)
- Removing the deck from a Dualtron Spider leaves the frame too flexy to stand on; Face de Pin Sucé stiffened the chassis with his own 3500 W motors and expects 80–85 km/h once hall wiring and 10 AWG phase leads are sorted.【F:data/vesc_help_group/text_slices/input_part000.txt†L7446-L7481】

### Throttle & Hall Wiring Maintenance (Batch 6)
- Pulsing acceleration on Happy Giraffe’s build mimicked hall dropout until he discovered the plastic throttle had failed; soldering the hall connectors directly and swapping to a higher-quality throttle resolved the surging.【F:data/vesc_help_group/text_slices/input_part000.txt†L7546-L7578】

### Sensorless Flipsky 7550 Troubleshooting (Batch 6)
- Koxx’s sensorless Flipsky 7550 delivered “hashed” torque until he raised phase current toward 90 A, bumped BLDC switching frequency to 20 kHz/35 kHz, and accepted that kicks to ~11 km/h are needed before the controller can commutate cleanly without halls.【F:data/vesc_help_group/text_slices/input_part000.txt†L7583-L7687】【F:data/vesc_help_group/text_slices/input_part000.txt†L7801-L7829】
- Even after swapping power stages he suspects a weak shunt or MOSFET bank, underscoring the shaky reliability of Flipsky power sections versus Spintend units tested in the same scooter.【F:data/vesc_help_group/text_slices/input_part000.txt†L7688-L7715】【F:data/vesc_help_group/text_slices/input_part000.txt†L7883-L7900】

### Acceleration Analytics & Current Balancing (Batch 7)
- Drag Racer remains convenient for Android telemetry, but the group confirms it needs clear skies to hold GPS lock and can misreport 0–40 km/h runs; Artem instead uses a higher-fidelity app (iOS/Android) to validate his 6.6 s single-motor pulls and compare VESC vs. Minimotors setups.【F:data/vesc_help_group/text_slices/input_part000.txt†L7901-L7935】【F:data/vesc_help_group/text_slices/input_part000.txt†L7921-L7998】
- Artem reiterates that torque is governed by phase current while battery current extends the RPM range before taper, recommending 90 A phase/30 A battery as a safe starting point for 1 kW hubs, scaling toward 120 A phase if cooling allows, and warning that excessive phase amps raise EMI/noise stress on the Ubox logic stage.【F:data/vesc_help_group/text_slices/input_part000.txt†L7999-L8071】【F:data/vesc_help_group/text_slices/input_part000.txt†L8058-L8070】
- He provides an at-a-glance formula—battery voltage × battery-limit amps = motor voltage × phase amps—to explain why higher pack voltage preserves phase current at speed, and supplies regen guidance to cap battery braking current at 1.5 C plus 15 A (e.g., 16 Ah pack ⇒ 24 A battery / 39 A controller regen).【F:data/vesc_help_group/text_slices/input_part000.txt†L8354-L8364】【F:data/vesc_help_group/text_slices/input_part000.txt†L8178-L8183】

### SmartDisplay Connectivity & Mounting (Batch 7)
- Francois unlocks a “transparent” BLE bridge so the SmartDisplay can act as a USB dongle for VESC Tool on Android—handy for controllers lacking onboard Bluetooth—though he still prefers wired links to avoid interference seen with nearby anti-theft trackers.【F:data/vesc_help_group/text_slices/input_part000.txt†L8005-L8014】
- He shares STL packs for the 3.5″ SmartDisplay enclosure while the team experiments with SLA/SLS resin prints, stem-cap mounts, and multi-jet services to center the display without overhanging the bars.【F:data/vesc_help_group/text_slices/input_part000.txt†L8211-L8267】【F:data/vesc_help_group/text_slices/input_part000.txt†L9341-L9348】
- CAN will continue syncing slave data to the SmartDisplay master in dual-controller builds, but Artem flags the need for presets such as “police mode” that could disable front-phase output while keeping rear torque—work that remains in prototyping.【F:data/vesc_help_group/text_slices/input_part000.txt†L8234-L8244】

### Brake Lever Compatibility & Sensor Options (Batch 7)
- Magura confirms the MT5e ships with two SKUs—2700985 (normally closed) and 2700984 (normally open/Higo “Closer”)—and the Spintend ADC board supports both switch and hall inputs via onboard toggles plus 5 V/3.3 V selection, simplifying integration with Shimano levers or Magura CMe5 all-metal assemblies.【F:data/vesc_help_group/text_slices/input_part000.txt†L8270-L8385】
- Riders debating “Shigura” hybrids conclude Shimano Saint levers offer sturdier feel while retaining Magura calipers, and note that regen on front-only builds should be tested carefully or omitted to avoid low-traction lockups.【F:data/vesc_help_group/text_slices/input_part000.txt†L8470-L8511】【F:data/vesc_help_group/text_slices/input_part000.txt†L8310-L8330】

### Emerging Hardware & Supply Chain Notes (Batch 7)
- ENNOID teased a 100 V/75 A single VESC in a 70 × 75 × 16 mm package (~$200) that could satisfy compact builds waiting on Spintend’s single-channel unit, which is now targeting a mid-July beta once enclosures arrive.【F:data/vesc_help_group/text_slices/input_part000.txt†L8396-L8400】【F:data/vesc_help_group/text_slices/input_part000.txt†L9030-L9033】
- AliExpress’ shift to IOSS should add ~21–24 % VAT upfront but remove €10–€24 postal handling fees in much of the EU, softening customs shocks for incoming controllers and cell batches.【F:data/vesc_help_group/text_slices/input_part000.txt†L8321-L8332】【F:data/vesc_help_group/text_slices/input_part000.txt†L9186-L9191】
- The group is lobbying Spintend for an integrated BMS, comparing Daly’s slimmer 120 A layout (easier to package in <25 mm deck extensions) against ANT’s bulkier but feature-rich smart units with touch displays.【F:data/vesc_help_group/text_slices/input_part000.txt†L8334-L8338】【F:data/vesc_help_group/text_slices/input_part000.txt†L9380-L9399】【F:data/vesc_help_group/text_slices/input_part000.txt†L9232-L9254】

### Battery Pack Fabrication & Materials (Batch 8)
- Tudor continues to model PETG honeycomb holders in Tinkercad and prints interlocking connectors so Xiaomi and G30 packs can be dry-fit without glue, while other builders laser-cut 3–6 mm kraftplex skeletons, add thin PETG jackets, and still tape the stack with fish paper because sealed decks trap heat regardless of insulation choices.【F:data/vesc_help_group/text_slices/input_part000.txt†L9412-L9427】【F:data/vesc_help_group/text_slices/input_part000.txt†L9599-L9634】
- Recycling guarantees are pushing European pack shops toward kraftplex or other recyclable wraps, though they still pad cells internally; Tudor notes enclosed scooter frames remain a “sauna,” underscoring the need for thermal audits on long-range builds.【F:data/vesc_help_group/text_slices/input_part000.txt†L9630-L9649】

### High-Current Pack Architecture & Tooling (Batch 8)
- Francois is splitting a 15 S 10 P VTC6 pack across the deck and two side bags under a 150 A discharge / 60 A charge BMS with 8 AWG leads, enabling aggressive e-brake settings that dump regen into the battery without overloading the MOSFETs.【F:data/vesc_help_group/text_slices/input_part000.txt†L9707-L9718】
- Artem recommends welding 25 mm pure nickel into 2 S 6 P “accordions,” folding them to shorten BMS sense leads and cut voltage sag; the crew leans on Easy Battery Calculator and RePackr to balance parallel groups before welding.【F:data/vesc_help_group/text_slices/input_part000.txt†L9683-L9731】【F:data/vesc_help_group/text_slices/input_part000.txt†L9752-L9756】【F:data/vesc_help_group/text_slices/input_part000.txt†L10032-L10034】
- Builders experimenting with 3 S booster packs for the Ninebot G30 warn that 18650 versions struggled at 60 A, so the latest 21700 “3S mod” ships with 100 A BMS units to keep delta-wound rentals alive.【F:data/vesc_help_group/text_slices/input_part000.txt†L10796-L10807】

### Cell Selection, Discharge Math & Charger Tips (Batch 8)
- Artem’s rule of thumb is to size cells by watt-hours at the expected load, not nominal amp-hours: 6 P of 21700s roughly equals 7 P of 18650s for enclosure volume, 12 S of VTC6 can match 13 S of 35E for voltage sag, and the Samsung 35E / LG MH1 remain cost-effective under 7 A per cell.【F:data/vesc_help_group/text_slices/input_part000.txt†L9771-L9836】
- For 12 S 5 P Xiaomi packs pulling 60–80 A, Samsung 48X or 50G deliver more usable Wh at 15 A than P42A while staying cool; 50E is discouraged because it overheats beyond 10–12 A, and Artem shares discharge curves to back the advice.【F:data/vesc_help_group/text_slices/input_part000.txt†L10442-L10485】【F:data/vesc_help_group/text_slices/input_part000.txt†L10634-L10658】
- Tudor is stacking 17 S 6 P 40T/50G arrays with copper busbars and notes that 21700 availability now makes them the go-to for high-performance scooters despite €5–7 per cell pricing spikes at NKON.【F:data/vesc_help_group/text_slices/input_part000.txt†L10494-L10517】【F:data/vesc_help_group/text_slices/input_part000.txt†L10510-L10569】
- Charger sourcing remains tricky for 12 S packs: riders lean on YZPower or AliExpress vendors for 50.4 V 3 A units, then add 5–6 A options while ensuring connectors and wiring are rated for the higher current.【F:data/vesc_help_group/text_slices/input_part000.txt†L10518-L10531】【F:data/vesc_help_group/text_slices/input_part000.txt†L10523-L10530】

### Delta Wiring & Voltage Scaling Lessons (Batch 8)
- Delta-wound Xiaomi builds can hit ~55 km/h on 10 S but draw 50–100 A spikes; one rider logged 91 km/h on 16 S before blowing the OEM controller, prompting a consensus that stock boards stay reliable only up to 15 S, while 20 S star-mode conversions still reach ~78 km/h.【F:data/vesc_help_group/text_slices/input_part000.txt†L9883-L9909】【F:data/vesc_help_group/text_slices/input_part000.txt†L10901-L10907】
- Artem reminds the team that higher series counts let VESCs maintain speed with half the amps of 10 S delta builds, keeping hub temperatures in check while retaining torque via phase-current limits.【F:data/vesc_help_group/text_slices/input_part000.txt†L9907-L9915】【F:data/vesc_help_group/text_slices/input_part000.txt†L8178-L8183】

### Spintend Reliability & Wiring Safeguards (Batch 8)
- Rowan’s 4WD scooter blew one Ubox CAN transceiver and another power switch when the controllers were energized separately; Artem suspects a momentary reverse-polarity path through the CAN harness if one VESC still had battery positive tied in, highlighting the need for synchronized power-up or isolation relays.【F:data/vesc_help_group/text_slices/input_part000.txt†L10290-L10351】

### Wiring, Anti-Theft & Instrumentation (Batch 8)
- Artem prefers 4 mm or dual 3 mm solid-core runs for BMS leads on long packs because the shorter, denser conductors shed less heat than multi-strand silicone wire over the same distance; koxx is simultaneously cataloging realistic amp limits for common connectors after discovering conflicting tables online.【F:data/vesc_help_group/text_slices/input_part000.txt†L10539-L10551】【F:data/vesc_help_group/text_slices/input_part000.txt†L10809-L10815】
- Koxx is prototyping an ESP32-based 4G+GPS tracker so VESC builds can report IMEI-backed telemetry for anti-theft alerts alongside the SmartDisplay.【F:data/vesc_help_group/text_slices/input_part000.txt†L10558-L10561】
- Tudor’s 120 A BMS build uses 0.1 mm copper busbar “sandwiches,” and Artem confirms the stack is fine; when debugging hall sensors, the crew reminds newcomers to meter each signal against controller ground rather than probing unpowered leads.【F:data/vesc_help_group/text_slices/input_part000.txt†L10563-L10574】【F:data/vesc_help_group/text_slices/input_part000.txt†L10570-L10573】

### Controller & Display Integration (Batch 8)
- Artem shared an NFC-enabled Zero-style throttle/display whose UART RFID module handles key management (P18 menu) and drops into VSETT wiring, offering a plug-and-play immobilizer for future SmartDisplay revisions.【F:data/vesc_help_group/text_slices/input_part000.txt†L10586-L10599】
- Ubox buyers confirm the dual controller ships with onboard Bluetooth but still needs the ADC adapter so Xiaomi/Zero brakes and throttles map correctly; without it, many analog levers and hall throttles won’t interface cleanly.【F:data/vesc_help_group/text_slices/input_part000.txt†L10733-L10774】

### Boosted Rev Throttle Mapping & Performance (Batch 8)
- The Boosted Rev thumbwheel outputs ~1.6 V at full brake, 2.54 V at neutral, and 3.3 V at wide open, giving linear e-brake control on a VESC; koxx reports the regen is so strong he rarely touches the mechanical brakes.【F:data/vesc_help_group/text_slices/input_part000.txt†L10882-L10894】
- Spintend-powered rental conversions continue to push boundaries: a modded Xiaomi hit 70 km/h on 20 S, while a Ninebot Max G30 with 48 V delta/star wiring logged 72 km/h on the dash (67.7 km/h GPS), emphasizing the need for widened bars and chassis reinforcement at those speeds.【F:data/vesc_help_group/text_slices/input_part000.txt†L10901-L10907】

### High-Voltage Xiaomi & Spintend Single Insights (Batch 9)
- Koxx’s Xiaomi test bed is already pulling three 45 A channels from a 10 S P42A pack yet caps out near 40 km/h, prompting a 14 S 6 P Samsung 30Q rebuild while Ninebot rentals with 20 S delta/star mods have clocked 67–72 km/h on stock controllers—highlighting the stability upgrades (bars, chassis) needed before chasing similar speeds.【F:data/vesc_help_group/text_slices/input_part000.txt†L10901-L10921】【F:data/vesc_help_group/text_slices/input_part000.txt†L10905-L10907】
- The Spintend single-core preview shares twin-UBOX DNA but needs active cooling above ~30–50 A; expect ≈100 A capability with a fan, a case barely twice the size of an XT90, and pricing around $150 once anodized enclosures ship.【F:data/vesc_help_group/text_slices/input_part000.txt†L10927-L10943】【F:data/vesc_help_group/text_slices/input_part000.txt†L11322-L11336】
- On dual-motor builds koxx is holding 40 A battery per controller with 100 A/60 A phase ceilings and traction control enabled to stop the front tyre from roasting—useful guardrails for early adopters until higher-capacity packs arrive.【F:data/vesc_help_group/text_slices/input_part000.txt†L10980-L10986】
- Delta rewinds demand doubled phase current for the same torque; builders recommend uprating hub leads before swapping the star termination to avoid overheated stock windings.【F:data/vesc_help_group/text_slices/input_part000.txt†L10946-L10954】【F:data/vesc_help_group/text_slices/input_part000.txt†L11421-L11428】

### Regen & Control Wiring Updates (Batch 9)
- Baseline regen targets from koxx land near −30 A battery/−80 A phase on the rear wheel and −25 A/−55 A on the front, giving firm braking without tripping the controller.【F:data/vesc_help_group/text_slices/input_part000.txt†L10956-L10962】
- Regen testing on a 10 S 2 P P42A pack showed 2.55 kW bursts and rapid motor/MOSFET heating, reinforcing why field sessions should log stator temperatures when aggressive braking profiles are enabled.【F:data/vesc_help_group/text_slices/input_part000.txt†L10974-L10986】
- Running ADC throttles and UART over shielded cable tied to controller ground removed cruise-control jitter at 120 A phase, and routing signal looms away from phase wires further cuts FOC-induced noise on high-amp Ubox installs.【F:data/vesc_help_group/text_slices/input_part000.txt†L11179-L11198】【F:data/vesc_help_group/text_slices/input_part000.txt†L11381-L11388】
- MiniMotors EYE throttles output roughly 0.8–4.1 V, so adapters or resistor dividers must clamp signals below 3.3 V before feeding VESC ADC inputs to avoid killing the STM32; all the finger/trigger throttles share 5 V, ground, and signal pins.【F:data/vesc_help_group/text_slices/input_part000.txt†L11903-L11907】
- Builders still want cruise control on Spintend—long rides leave trigger hands numb—so firmware or SmartDisplay macros to hold duty cycle remain a backlog item.【F:data/vesc_help_group/text_slices/input_part000.txt†L11901-L11930】

### SmartDisplay & Firmware Handling (Batch 9)
- VESC “profiles” live on the phone: applying Eco/Sport modes rewrites live controller/app configs, so riders deploy small UART bridges (e.g., basti30’s Arduino tool) when they want on-scooter buttons that push alternate maps into RAM without power-cycling.【F:data/vesc_help_group/text_slices/input_part000.txt†L11095-L11103】
- Koxx now hand-builds SmartDisplay and SmartController boards (20 more arrived this batch) and offers both a dash-mounted screen and a display-less deck module for riders who prefer to use their phone over BLE.【F:data/vesc_help_group/text_slices/input_part000.txt†L10991-L11002】
- Never connect the SmartDisplay’s USB to a PC while it is still plugged into a live Ubox: a ground-loop instantly nuked the 3.3 V rail on koxx’s controller and bricked the STM32, forcing an RMA and reinforcing the need for galvanic isolation or wireless debugging.【F:data/vesc_help_group/text_slices/input_part000.txt†L11633-L11705】

### Battery Pack Fabrication & Components (Batch 9)
- Mirono’s Ninebot Max build squeezes a Daly smart BMS and 13 S 5 P NCR21700A pack into the rental frame after grinding internal ribs; copper “sandwich” busbars remain on the table for lower resistance if field weakening proves insufficient.【F:data/vesc_help_group/text_slices/input_part000.txt†L11269-L11308】【F:data/vesc_help_group/text_slices/input_part000.txt†L11454-L11488】
- Tudor is laminating 0.1 mm copper with 0.15 mm nickel to carry roughly 150 A without bulky straps—an approach that dovetails with the crew’s earlier copper-bus experiments.【F:data/vesc_help_group/text_slices/input_part000.txt†L11931-L11940】
- JKBMS’s 17 S active-balancing board (≈10 × 8 × 1.7 cm) manages 60 A continuous/100 A burst while redistributing 600 mA between cells, giving compact packs smarter balancing than passive Daly units.【F:data/vesc_help_group/text_slices/input_part000.txt†L11081-L11093】
- Clear 160 mm shrink plus kraft paper keeps 8 P sticks visible, and Artem’s SIM/GPS-enabled BMS hides theft tracking inside the enclosure without external antennas.【F:data/vesc_help_group/text_slices/input_part000.txt†L11069-L11079】
- Pre-soldered AS150 harnesses now ship with 8 AWG power leads and four 24 AWG signal wires, simplifying 70 A+ quick-disconnects that carry BMS comms in parallel.【F:data/vesc_help_group/text_slices/input_part000.txt†L12006-L12010】
- Suspicious “new” cells still show up with tab remnants; the group leans on XTAR VC8 analyzers (8-slot charge/discharge with IR readouts) and rejects budget LittoKala testers when validating reclaimed 21700s.【F:data/vesc_help_group/text_slices/input_part000.txt†L11770-L11818】
- Artem is coordinating bulk Samsung 50G/50S orders direct from China at ~€4.9–5.1 per cell (100 pc MOQ), praising 50S for 20 A fanless or 35 A fan-cooled discharges while 48X trails slightly on heat; expect €10 pricing through EU resellers.【F:data/vesc_help_group/text_slices/input_part000.txt†L12344-L12366】【F:data/vesc_help_group/text_slices/input_part000.txt†L12358-L12366】
- Vsett 9 motors use 92 mm stators with 0.5 mm laminations and 9×7 slot/pole counts—handy specs for rewinding or sourcing stealth 500 W covers that mask the true 650 W+ output.【F:data/vesc_help_group/text_slices/input_part000.txt†L12347-L12354】【F:data/vesc_help_group/text_slices/input_part000.txt†L12306-L12321】

### Shipping, Legal & Compliance Notes (Batch 9)
- FedEx almost guarantees VAT/fees in the EU, whereas EMS routed through national posts often slips through untaxed in France; AliExpress Standard Shipping now excludes VAT on orders over €150, so customs still add 10–20 € handling per parcel.【F:data/vesc_help_group/text_slices/input_part000.txt†L11857-L11866】
- Artem disguises a dual-motor Vsett 9 as a single-motor 500 W scooter by fitting blank front covers and explaining the second hub as an “electric brake,” underscoring how inspectors still look for engraved wattage ratings despite riders limiting speed in firmware.【F:data/vesc_help_group/text_slices/input_part000.txt†L12306-L12321】

### BMS & Safety Diagnostics (Batch 9)
- Luis’s Wolf Warrior cut out at 60–70 km/h when the smart BMS flagged a 115 A “short”—resetting the fault cleared the ride, but mixing two packs (10 S 10 P MJ1 + 6 P MH1) leaves little margin for current spikes and complicates fault tracing.【F:data/vesc_help_group/text_slices/input_part000.txt†L11826-L11854】
- Another builder shorted pack leads while swapping connectors yet walked away unharmed thanks to the BMS trip, reinforcing why charge/discharge protection is mandatory when experimenting with new plugs.【F:data/vesc_help_group/text_slices/input_part000.txt†L11832-L11833】
- Rental deck locks are simple 5 V servos actuated through relays, so VESC-powered builds can reclaim the space by sealing the cavity or wiring the latch to the controller’s accessory rails for remote release while improving waterproofing.【F:data/vesc_help_group/text_slices/input_part000.txt†L11269-L11312】

### Brake & Control Hardware Options (Batch 9)
- Magura confirms the MT5e lever can be mounted left or right, but riders balk at €225 delivered and note that Nutt hydraulics provide similar feel for less—fuel for brake upgrade budgeting.【F:data/vesc_help_group/text_slices/input_part000.txt†L11819-L11824】
- MiniMotors trigger throttles from the Eye display output 3.3 V and plug straight into VESC ADC adapters, offering a roomier throw than Xiaomi paddles for smoother cruising once the voltage is clamped.【F:data/vesc_help_group/text_slices/input_part000.txt†L11868-L11899】
- Builders still hunt for hall-based e-brake levers; most aftermarket options are simple normally-open cut-offs, so Xiaomi hall levers remain desirable even though right-side mounting risks cable droop without custom brackets.【F:data/vesc_help_group/text_slices/input_part000.txt†L12387-L12400】

### Miscellaneous Build Notes (Batch 9)
- Grinding Xiaomi/Ninebot frame ribs is common to fit BMS hardware, but riders warn the rental deck lid loses waterproofing unless re-siliconed and that servo-lock cavities are better sealed than left to rust.【F:data/vesc_help_group/text_slices/input_part000.txt†L11269-L11312】
- Resin-printing SmartDisplay housings benefits from fresh resin and UV-safe paint; translucent shells yellow quickly under sunlight, so most owners now spray them opaque after post-curing.【F:data/vesc_help_group/text_slices/input_part000.txt†L11046-L11068】

### Brake & Control Integration (Batch 10)
- Ninebot G30 builders move the stock hall sensor and magnet onto replacement brake levers so they can mix hydraulic fronts with mechanical rears while keeping proportional regen on the VESC input.【F:data/vesc_help_group/text_slices/input_part000.txt†L12402-L12416】
- Artem confirmed the Spintend 75/300 architecture can remap the PPM pin to a DAC for brake-light duty, but koxx notes the public firmware lacks documentation, so experiments still rely on shared code snippets before it becomes an official feature.【F:data/vesc_help_group/text_slices/input_part000.txt†L12500-L12504】
- The single-channel Spintend ships without Bluetooth, so riders lean on SmartDisplay’s pass-through mode or external modules, power both controllers before plugging in CAN to avoid ground loops, and reserve the rugged “one-wire” bus for remote IO because I²C runs fall over past ~15 cm.【F:data/vesc_help_group/text_slices/input_part000.txt†L12528-L12555】
- Xiaomi hall levers output analog voltage while Magura-style hydraulics are normally open, making them incompatible in parallel; the group suggests adding a hall sensor to the hydro lever and reminds newcomers that throttle and brake sensors can safely share the 5 V/GND rails on a VESC loom.【F:data/vesc_help_group/text_slices/input_part000.txt†L12867-L12869】【F:data/vesc_help_group/text_slices/input_part000.txt†L12924-L12949】
- Riders log pack sag in VESC Tool on their phones and export the CSV/XLS files for graphing, letting them quantify voltage drop under heavy regen or hill climbs before retuning current limits.【F:data/vesc_help_group/text_slices/input_part000.txt†L12570-L12576】

### Motor & Controller Behaviour (Batch 10)
- Artem’s sizing heuristic keeps hubs safe by starting with phase amps ≈ motor wattage ÷ 10 and battery amps ≈ phase × 0.67, then reducing battery current in the same proportion whenever phase current is raised for stronger launches.【F:data/vesc_help_group/text_slices/input_part000.txt†L12491-L12499】
- A 750 W Boosted Rev hub on the Spintend single hit 55 °C controller and 80 °C stator within eight minutes at 120 A phase/80 A battery, proving small motors need gentler limits despite the ESC headroom.【F:data/vesc_help_group/text_slices/input_part000.txt†L13166-L13168】
- Koxx’s temperature logs show the controller clipping phase current once battery limits are reached around 25–30 km/h and that hard regen pulses add ~5 °C to the stator, reinforcing why current math and thermal logging go hand in hand.【F:data/vesc_help_group/text_slices/input_part000.txt†L13324-L13343】
- Field-weakening remains a high-speed tool: riders report 20–40 km/h gains on big ebikes but warn about massive current draw, so they enable it only above a set speed to preserve launch torque and controller temperatures.【F:data/vesc_help_group/text_slices/input_part000.txt†L13620-L13637】
- Spintend quietly bakes an alarm/horn into the Ubox—if the remote fails to connect at power-up the scooter screams while still allowing the motors to drive, encouraging owners to wire brake interlocks or extra sirens for theft deterrence.【F:data/vesc_help_group/text_slices/input_part000.txt†L13826-L13836】

### Battery & BMS Planning (Batch 10)
- Mirono’s G30 runs a hand-built 13 S 5 P NCR21700A pack (≈15 A per cell), but he starts at 50 A battery current and expects to cap at 75 A to keep the 5 P string within spec.【F:data/vesc_help_group/text_slices/input_part000.txt†L12450-L12461】
- Newcomers eyeing AWD conversions learn that 12 S 3 P packs sag or overheat on VESCs—veterans recommend buying the dual controller and running a single motor until a 16 S 5–7 P or larger battery is ready, or pairing internal/external packs for 16 S hybrids.【F:data/vesc_help_group/text_slices/input_part000.txt†L12639-L12665】
- Luis’ mixed MJ1/MH1 packs sag 10–12 V at 9 A per cell; Artem caps both chemistries near 7 A, pitches Samsung 50G or Molicel P42A for higher current, and still points riders to Murata VTC6 when they need the best 18650 performance.【F:data/vesc_help_group/text_slices/input_part000.txt†L12583-L12632】
- Koxx is assembling a 14 S 6 P pack with RePackr-balanced groups, glued cells, and glass fiber between layers, illustrating how equalising resistance across parallels keeps discharge uniform in cramped decks.【F:data/vesc_help_group/text_slices/input_part000.txt†L13433-L13479】
- Fish-paper rolls are suddenly scarce, prompting ideas like 0.8 mm kraftplex jackets, yet the crew stresses that series separators remain mandatory to prevent can-to-can shorts despite the recycling push.【F:data/vesc_help_group/text_slices/input_part000.txt†L13458-L13525】
- Daly’s smart BMS won’t honour remote power-off commands, so Mirono now relies on an external antispark while still favouring Daly’s display UI over ANT’s tiny screens.【F:data/vesc_help_group/text_slices/input_part000.txt†L12989-L12993】
- Spintend’s rheostatic brake module can dump an extra 10 A when regen saturates, trimming MOSFET stress, but high-regen builds still need the pack to absorb most current or risk heating the controller.【F:data/vesc_help_group/text_slices/input_part000.txt†L12811-L12821】
- Liitokala’s budget LiFePO₄ cells arrive unbalanced, sag heavily above 12 A, and ship slowly by boat; the chemistry stays attractive for stationary builds thanks to safety and cycle life but disappoints in scooters without large enclosures.【F:data/vesc_help_group/text_slices/input_part000.txt†L13560-L13575】
- Artem sourced compact JK active-balancing BMS units and shared the firmware/manual links so the team can compare their 17 S, 60 A continuous specs with Daly and ANT alternatives.【F:data/vesc_help_group/text_slices/input_part000.txt†L13900-L13900】

### Fabrication & Testing Tools (Batch 10)
- Artem documented how he added a thermistor to a Vsett hub—desoldering strands, splicing the sensor in a grooved heat-shrink channel, and sleeving the joint—so future retrofits avoid chafing inside the axle.【F:data/vesc_help_group/text_slices/input_part000.txt†L12872-L12880】
- Builders are experimenting with transparent deck plates: Mirono’s 6 mm acrylic lid rests on foam and cells but peers warn it will crack over time, while Artem is CNCing a 12 mm plexiglass spacer to hide addressable LED turn/brake strips around the deck lip.【F:data/vesc_help_group/text_slices/input_part000.txt†L12968-L13011】
- Serious pack testing now involves either an iCharger 4010 Duo or Mirono’s DIY 400 W (soon 1 kW) resistor bank in a miner chassis, giving them controlled charge/discharge logs before packs hit the road.【F:data/vesc_help_group/text_slices/input_part000.txt†L13586-L13599】
- External battery riders are upgrading to 4 mm gold bullets, AS120 mains, and even direct-soldered phase leads after discovering stock 2 mm conductors and MR60 plugs overheat above 80–100 A; backpack packs like Happy Giraffe’s 13 S 7 P bag stay sag-free once rewired.【F:data/vesc_help_group/text_slices/input_part000.txt†L13746-L13819】

### Motor Telemetry & Controller Performance (Batch 11)
- Artem reminds riders to enter the actual magnet count (not pole pairs) and a compressed wheel diameter measured under load in VESC Tool so speed, range, and acceleration logs stay accurate—GPS is too latent for launch metrics compared with the controller’s RPM telemetry.【F:data/vesc_help_group/text_slices/input_part000.txt†L13901-L13915】
- Ubox hardware keeps pace with extreme builds—one setup runs 180 A phase/130 A battery on the rear and 150 A/90 A on the front without cooking, thanks to lower-FET resistance and solid thermal pad contact that held FET temps near 39 °C at 90 A per wheel.【F:data/vesc_help_group/text_slices/input_part000.txt†L13933-L13963】

### Controller Packaging & Connectivity (Batch 11)
- Dual singles let builders park a controller at each deck end to shorten phase wires, but Artem notes overall layout depends on deck proportions because battery leads must stay short too—even if the two singles can be stacked when frame height allows.【F:data/vesc_help_group/text_slices/input_part000.txt†L14196-L14201】【F:data/vesc_help_group/text_slices/input_part000.txt†L14914-L14918】
- Spintend’s single-core board ships without Bluetooth; riders add one external module (shared over CAN) and can email Spintend to bundle it or ship a forgotten module later, avoiding lost SmartDisplay features like police mode.【F:data/vesc_help_group/text_slices/input_part000.txt†L14211-L14233】【F:data/vesc_help_group/text_slices/input_part000.txt†L14683-L14694】
- When pairing two singles, Spintend includes the CAN link; keep the UART accessories on the master and only add a second ADC board if you want a physical motor-disable switch—separate enclosures also improve heat shedding even though the stack consumes more volume.【F:data/vesc_help_group/text_slices/input_part000.txt†L14894-L14915】

### ADC & Brake Integration (Batch 11)
- Xiaomi-style throttles and levers output 0.8–4.1 V from a 5 V rail, so riders must use an ADC adapter or at least a 1 kΩ/2 kΩ divider to clamp signals under 3.3 V or they will cook the VESC’s STM32 inputs; Artem keeps spare boards in the EU for emergencies.【F:data/vesc_help_group/text_slices/input_part000.txt†L14233-L14260】
- Hall brake handles dislike being tied together—each can float at different voltages—so dedicate one VESC ADC per hall lever and leave the other brake purely mechanical if you only have two channels available.【F:data/vesc_help_group/text_slices/input_part000.txt†L14291-L14307】

### Sensorless & Firmware Notes (Batch 11)
- Crunchy low-throttle behaviour on sensorless Spintend setups is a known VESC firmware quirk; the in-development build smooths the vibration, and the crew considers the noise safe to ride with until the fix lands.【F:data/vesc_help_group/text_slices/input_part000.txt†L14313-L14324】

### Pack Layout & Cell Debates (Batch 11)
- Rental and Xiaomi decks can stretch to 120–150 cells with trimmed honeycomb spacers, but builders argue over adhesives—hot glue wastes less space yet can soften near 80 °C, so many supplement with silicone ribs or switch to reusable spacers with full nickel bussing to equalise resistance.【F:data/vesc_help_group/text_slices/input_part000.txt†L14327-L14339】【F:data/vesc_help_group/text_slices/input_part000.txt†L14924-L14966】
- Artem’s cell rundown keeps MJ1/MH1 around 7 A per cell, flags their extra 0.15 V sag versus 35E, and praises the 35E’s flat tail that yields more usable watt-hours under scooter loads—GA only wins once discharge passes roughly 10 A.【F:data/vesc_help_group/text_slices/input_part000.txt†L14731-L14747】

### Supply Chain & Vendor Vetting (Batch 11)
- The crew now treats the €140 “Spintend” AliExpress listing as a likely scam: the storefront was brand new, claimed thousands of units in stock, ignored messages, and the bill of materials alone—twin STM32s during the chip shortage—costs more than the advertised price.【F:data/vesc_help_group/text_slices/input_part000.txt†L14758-L14772】

### Field-Weakening & Motor Sourcing (Batch 11)
- Firmware 5.3 beta already delivers roughly +8 km/h via field weakening at an extra 20 A, letting riders hold 50 km/h even as packs sag, though they still toggle it only when headroom exists.【F:data/vesc_help_group/text_slices/input_part000.txt†L15031-L15033】
- Artem pegs the Vsett 9 hub around 48 km/h on 52 V (58 km/h dual) and says the 10+ wheel needs 60 V to shine, otherwise 48 V riders should expect reduced top speed despite its ~130 A/50 A thermal headroom and 1400 W nominal rating.【F:data/vesc_help_group/text_slices/input_part000.txt†L15035-L15108】
- Vsett’s split-rim motor simplifies servicing—tubes and discs unbolt without unplugging leads—making it attractive once riders secure sensible shipping versus the €150 quotes on offer.【F:data/vesc_help_group/text_slices/input_part000.txt†L15087-L15108】

### BMS Cutoffs & Failure Analysis (Batch 11)
- BMS trips can nuke controllers: a Daly shutdown mid-ride can back-feed voltage spikes into the FETs, so the team now probes pack voltage before and after disconnects, uses chargers to wake latched BMS boards, and watches regen current that can exceed Xiaomi’s 40 A limit.【F:data/vesc_help_group/text_slices/input_part000.txt†L15292-L15335】
- Happy Giraffe’s “water-killed” VESC turned out to be a stray solder ball after opening the silicone-sealed deck—reinforcing the need for meticulous cleaning and moisture control after wet rides despite aggressive sealing.【F:data/vesc_help_group/text_slices/input_part000.txt†L15340-L15400】

### Controller QA & Warranty Handling (Batch 12)
- Riders now open every Spintend controller before first power-up—Happy Giraffe found a solder ball shorting his single Ubox, while Artem recommends adding hard spacers instead of foam to keep components off the case and checking suspect resistors/caps with a meter before deciding on warranty vs. DIY repairs.【F:data/vesc_help_group/text_slices/input_part000.txt†L15401-L15441】
- Spintend continues to honour RMAs even after dramatic failures (Luis’ Ubox fire that also damaged his battery), but owners should expect to foot any pack repair costs, reinforcing why thorough bench inspection precedes live runs.【F:data/vesc_help_group/text_slices/input_part000.txt†L15435-L15436】

### Rider Safety & Stealth Practices (Batch 12)
- Helmet advice stresses ECE 22.05/22.06 full-face lids (DOT stickers alone are meaningless) plus MIPS-style rotational protection; even 30 km/h lowsides can smash chins, so the group rides in full moto gear despite the attention it attracts.【F:data/vesc_help_group/text_slices/input_part000.txt†L15473-L15534】【F:data/vesc_help_group/text_slices/input_part000.txt†L15520-L15531】
- Staying under the radar with police means choosing discreet frames (Xiaomi/Boosted over Dualtron-class builds), keeping LEDs subdued, and relying on “police mode” or field-weakening buttons only for brief escapes while otherwise cruising near rental speeds.【F:data/vesc_help_group/text_slices/input_part000.txt†L15535-L15572】【F:data/vesc_help_group/text_slices/input_part000.txt†L15549-L15568】

### Daly BMS Behaviour & Power Management (Batch 12)
- Daly display BMS units latch their discharge MOSFETs off after cell sag near 2.7 V and cannot be reset from the LCD—only the Bluetooth app (password 123456) can toggle charge/discharge, forcing Mirono to crack sealed decks to pull XT90s when regen or hard launches trip protection.【F:data/vesc_help_group/text_slices/input_part000.txt†L15647-L15684】【F:data/vesc_help_group/text_slices/input_part000.txt†L15655-L15667】
- Regen spikes can also flip Daly charge MOSFETs mid-brake, momentarily cutting power and nearly pitching riders, so they’re raising current thresholds and treating antispark switches as safety only, not a substitute for proper BMS logic.【F:data/vesc_help_group/text_slices/input_part000.txt†L15782-L15788】【F:data/vesc_help_group/text_slices/input_part000.txt†L16120-L16123】
- Daly SoC estimates remain unreliable (e.g., 3.1 V per cell reporting 31 %), pushing the crew toward external logging for range planning.【F:data/vesc_help_group/text_slices/input_part000.txt†L15764-L15769】

### Wiring, Lighting & Deck Fabrication (Batch 12)
- For 90 A packs, the group now defaults to AWG10 main leads (or dual AWG12 runs) and even 3–3.5 mm solid-core copper between pack negatives and BMS plates, noting the ~40 % ampacity bonus over stranded wire when runs stay short.【F:data/vesc_help_group/text_slices/input_part000.txt†L15706-L15738】
- Artem’s Vsett headlight retrofit needs a stiffer mount: the higher the lamp, the longer the dark “dead zone,” so he’s CADing a stem bracket to curb shaking while preserving the OEM look.【F:data/vesc_help_group/text_slices/input_part000.txt†L15641-L15646】
- Mirono’s clear 6 mm plexiglass deck shows off LEDs but demands structural support, threadlocker everywhere, silicone seals, and tougher adhesive (epoxy or dual-component glue) because strip tape peels and 6 mm sheets can crack under load or temperature swings.【F:data/vesc_help_group/text_slices/input_part000.txt†L16056-L16110】【F:data/vesc_help_group/text_slices/input_part000.txt†L16073-L16107】
- Rental G30 frames accept printed battery extenders, though BMS wiring height can block vertical cells—rewiring harness exits or adding 2 mm spacers keeps packs from fouling deck lids.【F:data/vesc_help_group/text_slices/input_part000.txt†L15632-L15640】

### Motor & Controller Reliability (Batch 12)
- Flipsky 4.2 hardware cannot survive 150 A phase: repeated hard launches triggered `fault_code_drv`, leaving only noisy BLDC mode operable—evidence that pushing far past spec silently degrades MOSFETs before they fail outright.【F:data/vesc_help_group/text_slices/input_part000.txt†L16191-L16245】【F:data/vesc_help_group/text_slices/input_part000.txt†L16231-L16241】
- Artem caps Spintend single phase current at 115–125 A until more data arrives, reminding builders that even Ubox duels rarely stay clean above ~130 A without short phase leads and solid thermal coupling.【F:data/vesc_help_group/text_slices/input_part000.txt†L16296-L16299】【F:data/vesc_help_group/text_slices/input_part000.txt†L15800-L15808】
- Sensorless HFI tuning hinges on at least a 15 % Ld/Lq inductance delta (measure via `measure_ind`); once dialed, it grants near-hall launch torque with only a faint startup whine, making it a viable fallback when hall harnesses fail.【F:data/vesc_help_group/text_slices/input_part000.txt†L15889-L15915】【F:data/vesc_help_group/text_slices/input_part000.txt†L15901-L15907】
- VESCs log faults only while a phone/PC is connected—the xmatic app captures them because the controller lacks onboard flash for history, so post-mortem debugging depends on staying tethered during tests.【F:data/vesc_help_group/text_slices/input_part000.txt†L16032-L16044】

### Motor Selection & Specification Notes (Batch 12)
- Wheelway’s “1000 W” hubs hide modest 36 mm magnets versus 1200 W units with 60 mm stacks; Spintend’s advertised 2.8 kW hub doubles nominal ratings for marketing, so riders now compare stator width, magnet depth, and real-world amp limits rather than nameplate watts.【F:data/vesc_help_group/text_slices/input_part000.txt†L15995-L16007】【F:data/vesc_help_group/text_slices/input_part000.txt†L16001-L16007】
- G30 rental motors include a brown lead for the embedded 10 k/100 k NTC—use it for thermal rollback because covers stay cool even while windings hit 80 °C.【F:data/vesc_help_group/text_slices/input_part000.txt†L15816-L15836】【F:data/vesc_help_group/text_slices/input_part000.txt†L15862-L15873】
- Artem catalogued the Vsett 9/9+ hub (92 mm stator, 30 magnets, 9/7 wind with 0.5 mm strands, RUWH 6003RS bearings) and estimates the 10+ wheel delivers ~62 km/h on 48 V at 35 A despite marketing claims near 90 km/h on 60 V.【F:data/vesc_help_group/text_slices/input_part000.txt†L16799-L16822】【F:data/vesc_help_group/text_slices/input_part000.txt†L16833-L16835】
- HM’s 60 V 1600–3500 W hubs run ~€160 shipped from Spain but arrive with low recommended ESC currents (25/37 A); the crew plans to confirm phase amp tolerances before trusting the spec sheet.【F:data/vesc_help_group/text_slices/input_part000.txt†L16858-L16888】

### Hall Sensor Repair & Orientation (Batch 12)
- Replacing Ninebot G30 halls requires matching the original switch parts (SS41F vs. R43) and keeping the stamped face oriented consistently; mismatched or reversed sensors output ~2 V constantly and won’t sync, forcing repeated tear-downs until firmware detection passes.【F:data/vesc_help_group/text_slices/input_part000.txt†L16405-L16535】【F:data/vesc_help_group/text_slices/input_part000.txt†L16520-L16535】
- Superglue secures loose elements, but Mirono ultimately restored operation by rerunning the VESC motor setup and dropping limits to 40 A battery/80 A phase while he sources proper hall spares.【F:data/vesc_help_group/text_slices/input_part000.txt†L16425-L16524】【F:data/vesc_help_group/text_slices/input_part000.txt†L16520-L16524】

### Pack Building Techniques & Tools (Batch 12)
- Artem’s 16 S 8 P build uses twin 3 mm copper busbars from each 4 P cluster to the BMS for equal draw and favours Samsung 35E over 50G: an 8 P 35E block delivers similar Wh to 5 P 50G while running cooler at 60–80 A thanks to lower per-cell load.【F:data/vesc_help_group/text_slices/input_part000.txt†L16304-L16312】
- Aligning copper/nickel “sandwich” packs demands jigs—wood boxes or chessboard frames keep six-cell folds flat, while epoxy shims prevent intermittent contact when layers flex.【F:data/vesc_help_group/text_slices/input_part000.txt†L16481-L16499】【F:data/vesc_help_group/text_slices/input_part000.txt†L16490-L16499】
- Acetone remains the go-to for dissolving stubborn double-sided tape between LiPo bricks before repurposing them as spot-welder supplies, although improvised multi-pack power sources look messy to outsiders.【F:data/vesc_help_group/text_slices/input_part000.txt†L16504-L16519】【F:data/vesc_help_group/text_slices/input_part000.txt†L16390-L16398】

### Shipping & Vendor Follow-ups (Batch 12)
- Postal math matters: returning a VESC via national post cost €15 versus €60–€80 with DHL/UPS, but EMS recently bounced electronics exports out of Guangzhou—Spintend had to rebook shipments on alternate carriers.【F:data/vesc_help_group/text_slices/input_part000.txt†L15840-L15840】【F:data/vesc_help_group/text_slices/input_part000.txt†L16537-L16544】
- AliExpress disputes can stall for months (Mirono’s €80 controller stuck at “processing”), so the team now pays with PayPal or cards that support chargebacks and documents faulty halls or motors aggressively for leverage.【F:data/vesc_help_group/text_slices/input_part000.txt†L16892-L16898】【F:data/vesc_help_group/text_slices/input_part000.txt†L16405-L16524】

### Lighting Integration & Accessory Power (Batch 13)
- Artem’s preferred “high beam” scooter lamp is a genuine 15–16 W unit that throws 40–100 m and pulls about 1.3 A from a 12 V rail; he wires it through a relay or MOSFET triggered by a physical button so the Ubox’s 3 A accessory output isn’t switched directly by the handlebar control.【F:data/vesc_help_group/text_slices/input_part000.txt†L16921-L16943】
- Riders debating where to power auxiliary lights concluded that stealing the throttle’s 5 V line risks burning the regulator—drawing even 0.5 A can collapse the rail, starve the ADC daughterboard, and back-feed the 12 V converter—so they now plan dedicated DC-DC runs or local packs instead of tapping control wiring.【F:data/vesc_help_group/text_slices/input_part000.txt†L17986-L18013】

### Wheelway Motor QC & Sensor Replacement (Batch 13)
- Tear-downs of Wheelway hubs revealed loose metal shards in the stator, inconsistent hall sensors (SS41F outer sensors with an unidentified center device), and even unused slots riders now repurpose for temperature probes—reinforcing complaints about the vendor’s QA and the need for thorough cleaning before use.【F:data/vesc_help_group/text_slices/input_part000.txt†L16966-L17029】【F:data/vesc_help_group/text_slices/input_part000.txt†L17545-L17566】
- Multiple members logged hall failures within ~25 km: motors ran smoothly on Xiaomi controllers yet desynced on VESCs until the halls were replaced or the builds were run sensorless, suggesting poor component grading rather than wiring mistakes.【F:data/vesc_help_group/text_slices/input_part000.txt†L17545-L17564】【F:data/vesc_help_group/text_slices/input_part000.txt†L17210-L17238】

### Temperature Monitoring & Harness Upgrades (Batch 13)
- For motor thermistors the group now standardises on compact 100 kΩ NTC probes: splice the sensor between hall ground and a new signal lead, run ultra-thin (≈30 AWG) PTFE-insulated wire through the axle, and re-sheath the harness with heat-shrink rather than bulking it up with folded insulation.【F:data/vesc_help_group/text_slices/input_part000.txt†L17250-L17305】
- Adding the extra conductor takes patience—Mirono spends three to four hours desoldering the factory loom, cutting a channel in the outer jacket, and shrink-wrapping the bundle so it still fits the motor exit without chafing.【F:data/vesc_help_group/text_slices/input_part000.txt†L17290-L17305】

### Motor Sourcing & Performance Planning (Batch 13)
- PaoloWu’s Blade 10 hub (≈€150 plus shipping) remains the leading Xiaomi drop-in: riders report 55–60 km/h on 13 S, 65 km/h on 13 S field weakening, and the ability to stomach ~150 A phase, while Zero 10X and Boyueda/Laotie alternatives offer similar kv at higher prices.【F:data/vesc_help_group/text_slices/input_part000.txt†L17036-L17067】【F:data/vesc_help_group/text_slices/input_part000.txt†L17145-L17193】
- Artem documented the Vsett 10+ motor construction (dual-rim shell, ~6.1″ stator width) and warns that marketing wattage is meaningless—inspect winding fill and magnet stacks to gauge true headroom before committing to high phase amps.【F:data/vesc_help_group/text_slices/input_part000.txt†L17100-L17110】【F:data/vesc_help_group/text_slices/input_part000.txt†L17098-L17105】
- Builders planning AWD conversions still favour keeping packs modest (e.g., 15 S 2 P) unless they upgrade BMS and wiring; even Mirono shelved a second motor after realising his 30 A battery couldn’t feed dual hubs safely.【F:data/vesc_help_group/text_slices/input_part000.txt†L16913-L16923】

### Controller Thermal Management & ADC Safeguards (Batch 13)
- Flipsky’s compact single struggles at 50 A battery / 85 A phase—MOSFETs hit ~60 °C within 3 km, prompting plans for better heatsink pressure, thermal paste, and 40 mm fans before chasing 100–120 A experiments.【F:data/vesc_help_group/text_slices/input_part000.txt†L17166-L17186】
- Artem reiterated regen math: keep battery regen at or below the pack’s amp-hour rating (e.g., ≤10 A on a 10 Ah block) and set controller regen roughly 15 A higher so excess power dumps as heat instead of spiking the cells or BMS.【F:data/vesc_help_group/text_slices/input_part000.txt†L17390-L17416】
- Koxx’s latest ADC survival checklist now includes never plugging accessories with the main pack live, banning raw 5 V throttles on the STM32 ADC pins, and shielding all ADC/UART runs—after voltage spikes cooked two converter boards despite heat-shrink protection.【F:data/vesc_help_group/text_slices/input_part000.txt†L18335-L18382】

### Battery Packaging & Fitment Logistics (Batch 13)
- Riders squeezing 12 S 4 P–5 P 21700 packs into Xiaomi frames stand the cells vertically with deck spacers, wrap every edge in fish paper, and insulate the tray so the aluminium chassis can’t abrade the nickel—otherwise even 0.8 mm gaps around magnets become failure points.【F:data/vesc_help_group/text_slices/input_part000.txt†L16998-L17008】【F:data/vesc_help_group/text_slices/input_part000.txt†L17015-L17021】
- European builders are struggling to source <1 kg batches of 21700 honeycomb nickel; some now band together for half-kilo orders or court EU suppliers despite 40 € quotes to avoid waiting for AliExpress consolidation.【F:data/vesc_help_group/text_slices/input_part000.txt†L17309-L17312】
- When telemetry over-reports speed, double-check both wheel diameter under load (~235 mm on CST 10″ tires) and motor-pole count (30 magnets ⇒ enter 30 poles) before chasing firmware ghosts.【F:data/vesc_help_group/text_slices/input_part000.txt†L17503-L17513】

### Maintenance, Repairs & Riding Practices (Batch 13)
- Tubeless rim dents can sometimes be heated and hammered flat, but Mirono’s 1200 W wheel still leaked, so he plans either aggressive silicone sealing or a full tire swap—evidence that even suspended G30 builds need proper tire pressure and impact checks after curbs.【F:data/vesc_help_group/text_slices/input_part000.txt†L17940-L18007】
- Stem hardware on rental G30s arrives with red Loctite; if you reassemble without threadlocker the pole will wobble, so the group now reuses washers, blue Loctite, and heat when disassembling to keep the steering column tight.【F:data/vesc_help_group/text_slices/input_part000.txt†L17960-L17982】
- Scroll-wheel throttles make excellent regen controls on Ubox builds—Mirono runs 80 A phase / 15 A battery for a smooth 47 km/h eco mode, while acknowledging he still craves the brutal punch that BLDC square waves deliver at low speed.【F:data/vesc_help_group/text_slices/input_part000.txt†L17625-L17654】【F:data/vesc_help_group/text_slices/input_part000.txt†L18388-L18395】

### Range & Efficiency Benchmarks (Batch 14)
- Artem’s Xiaomi/Ninebot experiments show how controller choice alters watt-hours per kilometre: the stock 52 V 13 Ah square-wave pack needed ~26 Wh/km at full chat, his dual-motor VESC build trimmed it to ~22.5 Wh/km despite higher speeds, and the sine-modulated Vsett managed ~17 Wh/km at 25–35 km/h when limited to 676 Wh.【F:data/vesc_help_group/text_slices/input_part000.txt†L18411-L18422】
- Range math threads now scale factory speed claims—Happy Giraffe pegs the Blade 10 hub at ~65 km/h on 13 S and ~50 km/h once load and voltage sag are considered, helping riders size gearing and forks for Xiaomi frame swaps before ordering Paolo Wu’s €150 kits.【F:data/vesc_help_group/text_slices/input_part000.txt†L18523-L18558】

### ADC & Control Reliability (Batch 14)
- Builders continue to blow ADC daughterboards by hot-plugging; Koxx reiterates that every manipulation demands a battery disconnect, that EMI stems from high current loops, and Artem advises switching to native 3.3 V throttles/brakes once a board glitches from reconnections.【F:data/vesc_help_group/text_slices/input_part000.txt†L18423-L18444】
- Manual hall detection on warm motors at ~70 A finally cures Mirono’s off-the-line “clonk,” reinforcing Artem’s tip to rerun both motor wizards on a full battery and road-test immediately so stalls are caught before riding season.【F:data/vesc_help_group/text_slices/input_part000.txt†L18463-L18495】
- Wheelway and Xiaomi hall hardware still output 4.8–4.9 V, so anyone chasing native VESC inputs either needs proper voltage dividers or rare 3.3 V sensors; otherwise two-wire brake cut-offs simply short 5 V to signal for an on/off stop with no proportional control.【F:data/vesc_help_group/text_slices/input_part000.txt†L19234-L19280】

### Wheel & Tire Service (Batch 14)
- Tubeless-on-solid rims continues to frustrate home mechanics—Mirono resorts to cutting the bead wire and adding a tube, only to trigger warnings about centrifugal failures at 65 km/h and reminders that dish soap, split rims, or pro tire presses are safer than brute force.【F:data/vesc_help_group/text_slices/input_part000.txt†L18668-L18755】
- Split rims earn praise for rapid swaps, yet the crew still debates tubeless versus tube reliability and notes premium platforms like Weped use rubber isolators plus dual bolt circles to seal the halves, underscoring why proper hardware matters when chasing airtight builds.【F:data/vesc_help_group/text_slices/input_part000.txt†L18811-L18868】
- Rim and axle swaps spark frame planning chats: stiffer Chinese frames that accept ~200 cells, DT2 EX donor shells, and Vsett or Blade swingarms all surface as options for dual 72 V projects once builders secure matching forks and brake adapters.【F:data/vesc_help_group/text_slices/input_part000.txt†L18712-L18720】【F:data/vesc_help_group/text_slices/input_part000.txt†L18805-L18815】【F:data/vesc_help_group/text_slices/input_part000.txt†L18854-L18868】

### Motor & Component Sourcing (Batch 14)
- Rage Mechanics’ 75 mm stator motors run over 10 kW per wheel without overheating on Weped platforms, dwarfing TunExtrem and Weped FS units but commanding ~€650 each depending on order volume—data that helps justify the spend for 120 km/h builds while highlighting axle-width constraints.【F:data/vesc_help_group/text_slices/input_part000.txt†L18931-L18955】【F:data/vesc_help_group/text_slices/input_part000.txt†L19204-L19233】
- Flipsky’s incoming GT100 and 75100 revisions ship with higher-spec Magnachip FETs and better enclosures, yet the team warns that thermal dissipation still hinges on mounting the case directly to the frame or stripping covers for tighter contact.【F:data/vesc_help_group/text_slices/input_part000.txt†L18893-L18908】
- DHL eCommerce and other bargain couriers keep losing Spintend parcels, so power users now request FedEx or AliExpress Standard/4PX consolidation with prepaid VAT to avoid multi-month purgatory in German customs depots.【F:data/vesc_help_group/text_slices/input_part000.txt†L19097-L19136】

### Battery Builds & BMS Practices (Batch 14)
- Artem’s latest 14 S pack packs dual 3 mm copper busbars, layered insulation, and remote BMS wiring that requires a 5 V pre-charge before plugging in the balance loom—an unusual activation sequence others should document before flashing the SIM-enabled board.【F:data/vesc_help_group/text_slices/input_part000.txt†L18837-L18854】
- Daly smart BMS users still fight quirks: voltage looks wrong until the harness is connected, SOC reporting drifts, and the display model won’t manually re-enable discharge after a trip, forcing riders to regen while rolling to wake it back up.【F:data/vesc_help_group/text_slices/input_part000.txt†L19140-L19172】
- Budget pack shops lean on silicone and Kapton once M3 inserts strip, but veteran builders push for rigid spacers, fish paper under BMS boards, and thicker leads after seeing exposed balance wires and XT30 mains labelled “fire starters.”【F:data/vesc_help_group/text_slices/input_part000.txt†L19126-L19129】【F:data/vesc_help_group/text_slices/input_part000.txt†L19787-L19899】
- Range logs from 12 S 4 P P42A packs show 15–20 km of hard riding burning ~40 % capacity with peaks at 40 A battery and 80 A phase, reminding commuters that lower-voltage Wheelway hubs heat quickly without embedded thermistors or cooling mods.【F:data/vesc_help_group/text_slices/input_part000.txt†L19037-L19087】【F:data/vesc_help_group/text_slices/input_part000.txt†L19094-L19122】

### Logistics & Accessory Power (Batch 14)
- Spintend singles omit the 12 V/3 A lighting rail—only the dual with remote modules exposes horn/headlight ports—so single-ESC riders must budget for fused buck converters instead of hijacking the temperature-controlled fan header.【F:data/vesc_help_group/text_slices/input_part000.txt†L18956-L18988】
- Scooter couriers swap antisparks and connectors frequently; Mirono’s GT100 build now relies on silicone beds and 8 mm bullets to secure gear once M3 threads strip, showing how mechanical fatigue drives builders toward overkill wiring and adhesives.【F:data/vesc_help_group/text_slices/input_part000.txt†L18939-L18955】【F:data/vesc_help_group/text_slices/input_part000.txt†L19126-L19129】

### Battery Fabrication & Deck Fitment (Batch 15)
- Mirono refuses to build small packs without holders or honeycomb cages; he argues the plastic grids add impact protection and airflow, and other builders sanding Xiaomi frame rails pair the structure with rubber liners to squeeze 12 S 4 P 21700 packs alongside VESC wiring without chafing the aluminium tray.【F:data/vesc_help_group/text_slices/input_part000.txt†L19913-L19947】

### Accessory Power & Wiring (Batch 15)
- For 20–25 W headlights driven directly from the traction pack, the crew favours a 1 A fast-blow glass fuse or PCB resettable fuse mounted inline and shrink-wrapped, noting that 0.75 mm² (≈20–21 AWG) silicone wire easily carries the ~0.6 A load while 16 AWG looms are overkill; Artem also shares a quick ampacity estimate—divide acceptable voltage drop by round-trip resistance, then halve (or third) it for continuous duty.【F:data/vesc_help_group/text_slices/input_part000.txt†L19990-L20099】

### Phase Wiring & Connector Limits (Batch 15)
- Artem pegs 12 AWG phase leads at roughly 100 A continuous, yet Mirono still spikes 150 A bursts on a 13 S low-kv 1.2 kW hub with 60 A battery limits, reporting ~45 °C after spirited rides—evidence that light riders can momentarily exceed published ampacity when cooling and duty cycle cooperate.【F:data/vesc_help_group/text_slices/input_part000.txt†L20025-L20057】
- The group circulates Amass’ connector thermal charts, concluding that 10 AWG is the realistic minimum for 60 A continuous and that AS120 plugs stay cooler than AS150 in scooter duty because their contact geometry sheds heat better than legacy XT bullet shells above ~70 A.【F:data/vesc_help_group/text_slices/input_part000.txt†L20132-L20136】

### Ubox Firmware & Thermal Management (Batch 15)
- Community members share the unofficial 300 A firmware builds for both Micro-USB and USB‑C Ubox singles, reminding each other that flashing them voids warranty even though they lift the 100 A factory limit.【F:data/vesc_help_group/text_slices/input_part000.txt†L20181-L20187】
- Face de Pin Sucé’s Dualtron Spider runs dual Spintend singles at 130 A phase/35 A battery per motor on 16 S and still overheats under hard regen, prompting a raft of cooling tactics: add 40–90 mm 12 W fans to blow between the stacked PCBs, cut intake/exhaust slots in the deck, clamp the case to aluminium blocks with quality paste, and even replace the stock pads with copper bars plus ProlimaTech PK‑3 to couple the FETs to the chassis after sanding paint off the mounting surface.【F:data/vesc_help_group/text_slices/input_part000.txt†L20190-L20299】

### Display & Stealth Integration (Batch 15)
- Artem confirms Vsett’s QS‑S4 display and RFID pod speak UART like Zero dashboards; koxx is building a “smart board” so VESC swaps can retain the OEM display for stealth checks, though extracting the harness requires digging through factory foam and silicone potting.【F:data/vesc_help_group/text_slices/input_part000.txt†L20364-L20389】

### Motor Measurements & Hardware (Batch 15)
- Happy Giraffe logs key Blade hub dimensions—130 mm inner axle, ≈160 mm fork span, M12 threads with 10 mm flats, 12 mm rotor offset, 4 mm hex hardware—and confirms the shell is tubeless-ready, giving Xiaomi builders a reference when ordering forks, spacers, and brake adapters.【F:data/vesc_help_group/text_slices/input_part000.txt†L20527-L20536】
- Wheelway honoured hall-board complaints for shipping plus a few euros, but riders still warn the supplier’s QA is inconsistent after receiving piles of returned parts, reinforcing the need to bench-test sensors before sealing motors again.【F:data/vesc_help_group/text_slices/input_part000.txt†L20403-L20406】【F:data/vesc_help_group/text_slices/input_part000.txt†L20518-L20520】

### Controller Logistics & Warranty Friction (Batch 15)
- Spintend’s DHL eCommerce option is painfully slow—previous RMAs took five weeks—and repeated capacitor failures on single Ubox units have riders threatening to blacklist the brand unless it upgrades the low-cost electrolytics; most now request FedEx despite the surcharge and document every unboxing for future claims.【F:data/vesc_help_group/text_slices/input_part000.txt†L20741-L20786】【F:data/vesc_help_group/text_slices/input_part000.txt†L20872-L20888】
- Artem relays that Ubox Pro is in final testing with 100 V support (likely 22 S regen) but urges Spintend to harden I/O before release, while koxx plans to inspect every new unit for solder balls or metal shavings after finding debris inside earlier runs.【F:data/vesc_help_group/text_slices/input_part000.txt†L20490-L20506】【F:data/vesc_help_group/text_slices/input_part000.txt†L20940-L20950】

### Sensor QA & FOC Diagnostics (Batch 16)
- A Trampa MK6 kept rebooting on throttle until the rider unplugged the hall loom—FOC would not even complete with the sensor block connected—pointing to Wheelway’s erratic hall boards and reinforcing Artem’s advice to rerun tests sensorless and inspect for stray solder that can reset the MCU.【F:data/vesc_help_group/text_slices/input_part000.txt†L21535-L21643】【F:data/vesc_help_group/text_slices/input_part000.txt†L21666-L21684】
- Wheelway’s replacement boards continue to ship with mismatched SS41/43 sensors; even when wired A/B/C correctly they desync within ~20 km, so the group now recommends bench-testing every hall with 5 V on the bench before sealing a motor and keeping a sensorless profile as backup.【F:data/vesc_help_group/text_slices/input_part000.txt†L21687-L21726】【F:data/vesc_help_group/text_slices/input_part000.txt†L21783-L21888】

### Charging Hardware & Pack Conductors (Batch 16)
- Xiaomi’s stock GX16-3 charge inlet is only comfortable around 3 A because the internal JST pigtail overheats; riders either parallel pins on a GX16-4 for 6–8 A or swap to XT30 pigtails with 16–18 AWG silicone leads to keep resistance and heat in check.【F:data/vesc_help_group/text_slices/input_part000.txt†L21739-L21788】【F:data/vesc_help_group/text_slices/input_part000.txt†L21790-L21808】
- Artem walked through nickel cross-section math (30.4 mm × 0.15 mm ≈ 4.56 mm²) to show why thin bus strips cap safe series current around 20 A—anything higher demands either copper busbars or thicker nickel to curb sag on 12 S commuter packs.【F:data/vesc_help_group/text_slices/input_part000.txt†L21855-L21875】
- Heavy users still blast 15–25 A into dual GX16 ports on large packs, but they monitor connector temps and accept accelerated wear, contrasting with commuters who prefer slower 0.2–0.3 C overnight balancing for longevity.【F:data/vesc_help_group/text_slices/input_part000.txt†L21810-L21849】

### Display Integration & Power Modes (Batch 16)
- Koxx is shipping a €60 SmartController board (motherboard + shield) for builders comfortable with coding and SMD work; it keeps the Vsett/Zero QS-S4 display via UART but currently drives only a single VESC on the open-source firmware, with dual-motor support reserved for the commercial “pro” release.【F:data/vesc_help_group/text_slices/input_part000.txt†L22102-L22133】
- The board expects momentary buttons and custom cabling, so Liam plans to reuse the Vsett dual-button pod while handling speed-mode UART commands for both controllers to avoid overheating a single rear hub.【F:data/vesc_help_group/text_slices/input_part000.txt†L22115-L22144】

### Spintend Ubox V2 Updates & High-Amp Experiments (Batch 16)
- Artem outlined Ubox V2 upgrades—resettable fuses on every aux rail, isolated 3.3 V logic, dedicated 12 V lighting/horn/brake outputs, fan header, CAN power insert for 4WD, and an external NRF/BLE slot with swappable antennas—eliminating the need for custom firmware to stay under 3.44 V logic limits.【F:data/vesc_help_group/text_slices/input_part000.txt†L22549-L22555】
- Face de Pin Sucé confirmed the 300 A firmware lets stock Ubox hardware push ~250 A phase and 420 A ABS in open-air installs, but Artem still cautions against exceeding ~130 A phase on sealed decks without serious cooling or tire upgrades.【F:data/vesc_help_group/text_slices/input_part000.txt†L22458-L22544】【F:data/vesc_help_group/text_slices/input_part000.txt†L22560-L22568】

### Security, Telemetry & Remote BMS Ideas (Batch 16)
- Builders are prototyping SIM7600 4G/GPS modules and even BMW automotive tracker boards inside the battery, interfacing over UART to shut packs down remotely while combining gyro triggers, sirens, and NFC unlocks for theft deterrence.【F:data/vesc_help_group/text_slices/input_part000.txt†L22620-L22658】
- Artem now favours hiding the tracker within the pack enclosure so thieves cannot disable it quickly, pairing it with high-current MOSFET cutoffs driven by the SmartController expansion he and koxx are exploring.【F:data/vesc_help_group/text_slices/input_part000.txt†L22620-L22662】

### Brake & Fork Hardware Experiments (Batch 16)
- Zoom calipers continue to disappoint, pushing riders toward Nutt, Magura MT5e, Shimano Saint, or even 3 mm reinforced 160 mm rotors that survive repeated 120→0 km/h stops—though Magura reservoirs crack under extreme loads, so Saints or Hope calipers with thick rotors are the current favourites.【F:data/vesc_help_group/text_slices/input_part000.txt†L22666-L22744】
- Monorim fork swaps require custom torque arms, thin-head bolts, and stacked stainless shims; the team is sharing CAD and photo references so 140–160 mm discs clear the square legs without grinding through the casting.【F:data/vesc_help_group/text_slices/input_part000.txt†L22794-L22843】
- Koxx is redesigning SmartController enclosures with taller internal walls and TPU cable glands to survive a five-minute hose test, offering a template for weather-sealing other scooter electronics.【F:data/vesc_help_group/text_slices/input_part000.txt†L22864-L22874】

### Frame & Pack Fabrication Highlights (Batch 7)
- Ninebot rental frames hide factory silicone, lockable battery latches, and swappable pack harnesses—making them attractive donors for high-power conversions once brake mounts are adapted for disc hardware.【F:data/vesc_help_group/text_slices/input_part000.txt†L9201-L9214】
- Boosted Rev tear-downs show room for only ~60×21700 cells (12 S5P) plus an under-slung controller, pushing builders toward charge-only BMS + fuse strategies when ANT units exceed the 100 mm × 40 mm deck envelope.【F:data/vesc_help_group/text_slices/input_part000.txt†L9000-L9025】【F:data/vesc_help_group/text_slices/input_part000.txt†L9235-L9263】
- Tudor’s VSETT-sourced 1200 W hubs with 50 H magnets will pair with 17 S 40T packs, but he and Mirono warn about inflated AliExpress freight unless parts are forwarded or negotiated ahead of time.【F:data/vesc_help_group/text_slices/input_part000.txt†L9077-L9112】

### Rotor Spacers & Brake Alignment (Batch 17)
- Tall brake adapters should use a one-piece ring spacer instead of stacked washers so axial loads don’t rock the disc bolts; 5 mm steel rings have proven stable on custom Blade hubs where 1.7 mm shim stacks wandered.【F:data/vesc_help_group/text_slices/input_part000.txt†L22903-L22941】【F:data/vesc_help_group/text_slices/input_part000.txt†L23098-L23112】
- Reversed Monorim forks with double spacers on the lower axle clear Blade 1200 W hubs without bending the legs, but the wider stance highlights how DIY mounts still need precision machining to keep calipers square.【F:data/vesc_help_group/text_slices/input_part000.txt†L23100-L23112】
- Builders are budgeting CNC time for rotor shims after discovering that 6-hole aftermarket rims rarely align with Xiaomi 5-hole spacers, reinforcing the need for bespoke hardware when mixing OEM and custom hubs.【F:data/vesc_help_group/text_slices/input_part000.txt†L22935-L22942】

### Acoustic Alerts & Control Pods (Batch 17)
- Compact 12 V sirens such as the GREATZT QSI-4840 module (≈€2.76) deliver 120–125 dB and shrink to roughly 30 × 20 mm once the case is trimmed, letting riders tuck alarms behind OEM screens or inside side panels via the Ubox horn output.【F:data/vesc_help_group/text_slices/input_part000.txt†L22999-L23098】
- Cycling horns with detachable PCBs measure about 35 × 30 × 20 mm and offer friendlier 110 dB tones for pedestrian use, so scooter builds now pair a “gentle” bar button with the siren-grade channel for traffic conflicts.【F:data/vesc_help_group/text_slices/input_part000.txt†L23080-L23097】
- Riders seeking CAN-enabled button pods are requesting integrated transceivers so only a four-wire trunk (power, ground, CAN_H, CAN_L) runs through the stem, simplifying installs versus discrete analog harnesses for each light, horn, and turn signal.【F:data/vesc_help_group/text_slices/input_part000.txt†L23705-L23731】

### Motor Thermal Management & Magnet Care (Batch 17)
- Ferrofluid primarily cools rotor magnets by wicking heat to the rim; it barely shifts winding temperatures, which are driven by turn length, wire gauge, and current. Builders now treat 80–100 °C as the safe magnet ceiling while accepting 120 °C+ windings for short bursts.【F:data/vesc_help_group/text_slices/input_part000.txt†L23282-L23299】
- Vsett/Blade-style ventilated rims deliberately trade shorter stators for stronger airflow; Artem is experimenting with relocating hub thermistors into the air gap so the sensor reports magnet temperature rather than coil hot spots.【F:data/vesc_help_group/text_slices/input_part000.txt†L23290-L23305】
- Riders pushing delta-wound Xiaomi hubs beyond 80 °C noticed temporary demagnetisation and sagging launch torque, underscoring the need for real-time temperature telemetry before extending high-current pulls.【F:data/vesc_help_group/text_slices/input_part000.txt†L23148-L23188】

### Frame & Voltage Safety for Xiaomi Builds (Batch 17)
- Veterans warn that 16 S dual-motor targets will snap an M365 stem unless the chassis is completely reworked with dual brakes, suspension, and reinforced decks—costs that rival a stock Vsett 9/9+ with safer geometry.【F:data/vesc_help_group/text_slices/input_part000.txt†L23370-L23440】
- Xiaomi decks can squeeze 13 S 6 P packs if the controller lives externally, but AWD conversions usually require backpack or rack-mounted batteries plus AWG6 cabling, eroding the platform’s portability advantage.【F:data/vesc_help_group/text_slices/input_part000.txt†L23382-L23393】【F:data/vesc_help_group/text_slices/input_part000.txt†L23394-L23415】
- Builders comparing Blade 10D and Mantis motors still favour the Xiaomi Pro for novelty, yet concede that Ninebot G30 frames offer better packaging for dual VESCs and larger packs when stealth is less critical.【F:data/vesc_help_group/text_slices/input_part000.txt†L23372-L23393】

### Lighting QA & Power Distribution (Batch 17)
- AliExpress “20 W” projector pods often pull only 10–14 W at 48 V; riders now meter input current, document the wattage shortfall, and file disputes rather than trusting catalog specs.【F:data/vesc_help_group/text_slices/input_part000.txt†L23782-L23833】【F:data/vesc_help_group/text_slices/input_part000.txt†L23860-L23899】
- Trusted 15 W single-colour projectors remain the baseline for scooter low beams, while dual-beam units that split wattage between high/low outputs deliver iPhone-flashlight levels of light unless paired with separate drivers.【F:data/vesc_help_group/text_slices/input_part000.txt†L23820-L23839】
- Riders are budgeting inline fuses and step-down space when adding 12 V lighting because the Spintend single lacks a native auxiliary rail and can only source horn power through its low-current output.【F:data/vesc_help_group/text_slices/input_part000.txt†L22999-L23008】【F:data/vesc_help_group/text_slices/input_part000.txt†L23846-L23858】

### High-Amp Connectors & Wiring Practice (Batch 17)
- XT150 bullets and AS150U battery leads offer ~0.20 mΩ resistance—about three times lower than MT60/XT60 plugs—while adding spark suppression and spare signal pins for BMS or tracker hookups, making them the new standard for 90–150 A phase runs.【F:data/vesc_help_group/text_slices/input_part000.txt†L23732-L23745】【F:data/vesc_help_group/text_slices/input_part000.txt†L24371-L24388】
- Mirono’s Vsett packs use DynaVolt-built BAK 2600 mAh cells that stay near ambient at 30 A (≈2.3 C), suggesting Chinese “house brand” 14 S 6 P modules can be repurposed if riders respect the original BMS limits.【F:data/vesc_help_group/text_slices/input_part000.txt†L23912-L23925】
- Solder joints are being treated as mechanical fillers rather than primary conductors: builders twist or fold AWG12 leads to double the contact area inside bullets before flooding with solder, acknowledging that even silver-bearing alloys conduct 2–5× worse than copper.【F:data/vesc_help_group/text_slices/input_part000.txt†L24100-L24120】

### BMS Service, Charging & Safety (Batch 17)
- Inmotion LF8 rental packs expose B+ and B− pads under the silicone-potted BMS; bypassers now solder directly to the nickel busbars while emphasising that discharge without supervision or a secondary BMS is risky.【F:data/vesc_help_group/text_slices/input_part000.txt†L24011-L24033】
- Face de Pin Sucé’s 16 S 10 P Molicel P42A pack tolerates 47 A fast-charging when paired with an external power stage, setting a benchmark for active-cooled pit chargers on high-capacity builds.【F:data/vesc_help_group/text_slices/input_part000.txt†L24365-L24375】
- Riders frustrated with Daly smart BMS units that lack manual charge/discharge toggles are switching to ANT’s 320 A platform for compact decks, noting smoother remote control and better packaging despite higher cost.【F:data/vesc_help_group/text_slices/input_part000.txt†L24390-L24400】

### CAN Lighting & Accessory Control (Batch 17)
- Koxx’s 6 cm × 3 cm CAN lighting board drives a 10 A budget per channel (front, rear, addressable LEDs) from selectable 5 V or 12 V rails and daisy-chains for turn signals, giving VESC scooters a plug-and-play lighting backbone.【F:data/vesc_help_group/text_slices/input_part000.txt†L23689-L23708】
- Ongoing CAN-bus reverse-engineering now enumerates VESC nodes and reads live status frames; the remaining task is mapping extended-frame writes for current and speed limits so SmartController firmware can enforce mode profiles over CAN alone.【F:data/vesc_help_group/text_slices/input_part000.txt†L24321-L24329】
- Artem is sketching a stem-mounted connector board that muxes OEM throttle/brake UART into CAN, leaving just two to four wires down the steering column while a deck module switches lights, horn, and addressable strips.【F:data/vesc_help_group/text_slices/input_part000.txt†L24327-L24333】

### Spintend Logistics & Accessory Updates (Batch 17)
- Spintend opened Ubox V2 sales at $300 with the same price as V1 but no onboard Bluetooth, reflecting signal issues inside metal decks and reinforcing the need for external dongles in sealed enclosures.【F:data/vesc_help_group/text_slices/input_part000.txt†L24331-L24346】
- Frequent ADC board failures—and the €37 shipping plus on-delivery VAT—have riders pooling group orders for spares while some choose to power throttles directly from 3.3 V rails to avoid the adapter entirely.【F:data/vesc_help_group/text_slices/input_part000.txt†L24338-L24353】
- AS150-style anti-spark connectors with auxiliary signal pins are being adopted so hidden trackers or smart BMS links share the main battery umbilical without extra connectors or resistance hit.【F:data/vesc_help_group/text_slices/input_part000.txt†L24378-L24388】

### Brake Upgrades & Lever Interfaces (Batch 18)
- Xtech hydraulic conversions still rely on mineral oil—Mirono bled his calipers with dual syringes and quickly abandoned the idea of using water after seeing the trapped bubbles.【F:data/vesc_help_group/text_slices/input_part000.txt†L24413-L24418】
- Artem’s freshly delivered Shimano M7120 four-piston set (≈€155 for the pair without rotors) brings stiffer one-finger levers and extra thermal mass that he plans to migrate from his trial bike to the scooter if he decides four pistons are overkill off-road.【F:data/vesc_help_group/text_slices/input_part000.txt†L24423-L24432】
- Riders comparing Magura MT5 kits with Shimano quads note that the MT5 bundle at ~€192 including discs is compelling if you add independent pads and aluminium levers; the Bosch MT5e variant retains a built-in brake switch for lights but costs more than the mechanical-lever-and-Magura-caliper mix some have adopted.【F:data/vesc_help_group/text_slices/input_part000.txt†L24436-L24483】
- Brake-light integration drives lever choices: one member keeps Nutt levers for the switch while running Magura calipers, and others point to the MT5e’s HIGO harness as the cleanest plug-and-play option when budget allows.【F:data/vesc_help_group/text_slices/input_part000.txt†L24480-L24527】

### Wheel Swaps & Spacer Fitment (Batch 18)
- Wheelway rear rims bolt into Xiaomi frames once you enlarge the dropout holes and add ~1 mm spacers so the hub bearings clamp squarely; skipping the shims leaves the wheel floating in the wider frame channel.【F:data/vesc_help_group/text_slices/input_part000.txt†L24529-L24537】
- Even bargain AliExpress spacers can work—the 5 g aluminium rings Mirono sourced simply need to resist compression because the axle bolts carry the braking load.【F:data/vesc_help_group/text_slices/input_part000.txt†L25884-L25899】

### ANT BMS Configuration & Daly Lessons (Batch 18)
- Face de Pin Sucé continues to vouch for ANT’s 320 A 20 S smart BMS—he has run about ten units personally—while acknowledging the enclosure is larger than lower-current models that Artem prefers for 60–100 A decks.【F:data/vesc_help_group/text_slices/input_part000.txt†L24400-L24411】
- Mirono confirmed that ANT quietly added a discharge/charge toggle behind the “I’m sure” confirmation inside the parameter menu, giving riders a software way to shut packs down without digging for breakers.【F:data/vesc_help_group/text_slices/input_part000.txt†L25154-L25159】
- July 2021 and newer ANT boards refuse to accept settings from the legacy Android/iOS apps—builders must install the refreshed client, though the update still speaks to older hardware once paired.【F:data/vesc_help_group/text_slices/input_part000.txt†L24635-L24649】
- Daly smart BMS owners remain frustrated that manual output control often requires factory programming; Mirono resorted to an inline breaker to reset trips because his unit would not honour on/off commands.【F:data/vesc_help_group/text_slices/input_part000.txt†L24654-L24665】
- Mixing stock batteries with cheap common-port Daly packs continues to blow controllers—the group reiterates that regen must never face an open negative loop, so anyone paralleling packs needs non-interrupting discharge paths or regen-disabled firmware.【F:data/vesc_help_group/text_slices/input_part000.txt†L24960-L24969】

### Controller Experiments & QC (Batch 18)
- Raphael and others are pushing Xiaomi/M365 controllers toward 20 S–30 S duty by moving the power stage to external MOSFET boards, tweaking gate resistors, and authoring custom firmware because the stock STM32F1 lacks RAM and compute headroom at 125 V; without those changes the controller oscillates violently at high ERPM.【F:data/vesc_help_group/text_slices/input_part000.txt†L24895-L24958】
- Spintend’s latest single revised its CAN harness so the 5 V line can wake the second controller, added extra thermal pads, yet still ships without case bolts or with stray solder balls—customers now inspect and photograph every unit before installation.【F:data/vesc_help_group/text_slices/input_part000.txt†L24683-L24749】

### Spintend Single Integration & Controls (Batch 18)
- The single Ubox shares its eight-pin JST between the ADC throttle board and Bluetooth module; koxx advises repinning the connector and borrowing ground elsewhere because the CAN header cannot host UART accessories.【F:data/vesc_help_group/text_slices/input_part000.txt†L24761-L24779】【F:data/vesc_help_group/text_slices/input_part000.txt†L25161-L25169】
- Happy Giraffe’s throttle cut-out traced back to the ADC adapter’s 3.3 V/5 V slide switch—he now epoxies it in place and warns that flipping it while powered can brick the daughterboard, a sentiment koxx echoes after killing multiple units.【F:data/vesc_help_group/text_slices/input_part000.txt†L25225-L25254】

### Fault Diagnosis & Regen Tuning (Batch 18)
- Traction-control style “anti-slip” belongs on dual setups only; leaving it enabled on a single Spintend made Happy Giraffe’s scooter cut power at low speed with red/green blink codes until Artem highlighted the misconfiguration.【F:data/vesc_help_group/text_slices/input_part000.txt†L25452-L25469】
- Without Bluetooth logging, riders still have options—Spintend stores the last fault until power-down, so koxx recommends popping the deck after an event and checking VESC Tool’s terminal via USB before cycling the controller.【F:data/vesc_help_group/text_slices/input_part000.txt†L25486-L25507】
- Regen behaviour mirrors throttle math: phase current dictates low-speed braking strength while the battery limit and pack voltage cap how much power actually returns; extra phase amps above what the pack can absorb simply burn as heat in the MOSFETs.【F:data/vesc_help_group/text_slices/input_part000.txt†L25550-L25599】

### Motor Cooling, Ferrofluid & Efficiency (Batch 18)
- The crew reaffirmed that hub magnets mostly warm via convection from the copper windings—direct electromagnetic losses are negligible compared with coil heating—so ferrofluid is used to wick that heat into the rotor shell where airflow can shed it.【F:data/vesc_help_group/text_slices/input_part000.txt†L25632-L25678】
- Artem pegs real-world BLDC outrunners around 86 % efficient in block-commutation and higher under FOC, contrasting with 40–60 % brushed motors; keeping a motor near its rpm “sweet spot” matters more than brute-forcing phase amps on small scooter hubs.【F:data/vesc_help_group/text_slices/input_part000.txt†L25679-L25699】
- HeroDasH demonstrated ferrofluid application with magnetic bottles that pull the liquid straight into the magnet gaps, cautioning against overfilling because excess increases drag; Mirono pointed others to ebikes.ca’s simulator for visualising how kv and resistance tweaks shift the efficiency curve.【F:data/vesc_help_group/text_slices/input_part000.txt†L25723-L25748】

### Voltage Strategy & High-Voltage Tradeoffs (Batch 18)
- Moving from 16 S to 20 S trims current for the same wattage and adds ~2.5 km/h per added series cell, but Artem warns that 100 V-rated FETs carry ~33 % higher Rds(on) than 75 V parts and that pack length, insulation, and voltage safety all get tougher at 20 S.【F:data/vesc_help_group/text_slices/input_part000.txt†L25857-L25875】
- Ralf adds that chasing extreme speed on low voltage drives currents to impractical levels, so designers should balance motor coil geometry, series/parallel splits, and pack packaging rather than fixating on a single voltage target.【F:data/vesc_help_group/text_slices/input_part000.txt†L25883-L25883】

### Cell Testing & Selection (Batch 19)
- High-current discharge tests need Kelvin/4-wire measurement—thin alligator clips dropped a P42A to a false 1.9 V at 20 A until the team probed directly at the cell tabs—so clamp meters at the battery and upgrade the leads before condemning cells.【F:data/vesc_help_group/text_slices/input_part000.txt†L25901-L25926】
- Samsung 35E cells stay efficient below ~7 A each, 4 P packs of 40T can sustain 80 A with copper interconnects, and riders chasing lowest sag beyond 20 A per cell now favour Molicel P42A, turning to Vapcell T50/Samsung 50S only when they can justify the ~13 % Wh premium.【F:data/vesc_help_group/text_slices/input_part000.txt†L25932-L25935】【F:data/vesc_help_group/text_slices/input_part000.txt†L26055-L26078】
- Artem’s EU sourcing comparison notes P42A outperforming 40T at 20–30 A, LG/Samsung 50G as the 7–10 A efficiency leader, Samsung 50S (Vapcell T50) matching P42A output at twice the price, and bulk 30T/35E/50G cells landing around €2.5–€4 when bought through community channels.【F:data/vesc_help_group/text_slices/input_part000.txt†L27150-L27186】

### Connector & Harness Upgrades (Batch 19)
- Builders are moving to Amass AS150U anti-spark plugs—with 8 AWG pigtails and 75 A ratings—to eliminate the voltage drop and heat they saw on XT60/XT90 pairs when feeding dual VESC builds.【F:data/vesc_help_group/text_slices/input_part000.txt†L26027-L26045】【F:data/vesc_help_group/text_slices/input_part000.txt†L26243-L26257】
- Spintend duals recorded ~500 A phase and 11 kW bursts; the crew now treats XT90 as temporary, recommending XT150 or AS150 once phase amps live above 150 A to avoid the 200–300 A desoldering events others have logged.【F:data/vesc_help_group/text_slices/input_part000.txt†L26141-L26160】【F:data/vesc_help_group/text_slices/input_part000.txt†L26235-L26252】
- JK BMS retrofits leave the pack with 8 AWG tails into AS150U mains and silicone charge leads so the smart board’s shunts and active protections aren’t throttled by high-resistance wiring.【F:data/vesc_help_group/text_slices/input_part000.txt†L26622-L26629】

### Controller Cooling & Mounting Practices (Batch 19)
- Dual Spintend installs on Weped chassis hit 80 °C while delivering ~500 A phase, highlighting how little margin sealed decks have at five-figure wattages without improved FET interfaces.【F:data/vesc_help_group/text_slices/input_part000.txt†L26141-L26147】
- Extended debates ended with consensus: bolt the controller flat to the aluminium chassis with quality thermal paste; remote radiator boxes, thick spacers, or long external runs add heat, resistance, and failure points compared to a well-clamped deck or custom footrest mount.【F:data/vesc_help_group/text_slices/input_part000.txt†L26307-L26380】
- Opening vents alone only delays thermal cutback—direct deck contact and fresh compound were the proven fixes for 75 A battery / 190 A phase Ubox settings that otherwise crept toward shutdown.【F:data/vesc_help_group/text_slices/input_part000.txt†L26480-L26550】

### BMS Integration & Regen Behavior (Batch 19)
- JK’s compact smart BMS lets riders independently enable charge, discharge, and balancing, reports harness resistance, and still leaves room for GPS/4G trackers when rewired with silicone pigtails and AS150 mains inside 16 S scooter packs.【F:data/vesc_help_group/text_slices/input_part000.txt†L26622-L26633】【F:data/vesc_help_group/text_slices/input_part000.txt†L26757-L26770】
- Disabling the charge FET on that common-port BMS blocks regen, making VESC log 72 V spikes even though the pack sits at 65 V; re-enabling charge restores braking and the controller simply idles in UVP mode if regen is rejected.【F:data/vesc_help_group/text_slices/input_part000.txt†L27213-L27225】

### Smart Controls, Lighting & Accessories (Batch 19)
- Koxx’s CAN lighting daughterboard now handles configurable LED strips for brakes and turn signals, but it expects an external 5 V/12 V feed and exposes a programming header plus extra inputs for steering-column buttons.【F:data/vesc_help_group/text_slices/input_part000.txt†L26110-L26138】
- Polish-made triggers from e-bikestuff ship with a 0.96–4.31 V sweep, zero deadband, and VESC-adjustable endpoints, giving riders a premium alternative to Xiaomi/Zero throttles if they can stomach the shipping cost.【F:data/vesc_help_group/text_slices/input_part000.txt†L26665-L26690】【F:data/vesc_help_group/text_slices/input_part000.txt†L26728-L26729】
- Lock-ring grip pods with tactile turn buttons deliver Vsett-style controls for a fraction of the OEM price, trading extra mass for better ergonomics on commuter handlebars.【F:data/vesc_help_group/text_slices/input_part000.txt†L26710-L26725】

### Frame, Components & Logistics (Batch 19)
- Ninebot G30 rental chassis remain coveted: non-folding stems, dual brakes, oil suspension, thicker tubing, and 10 kg of extra steel swallow 13 S 5 P 21700 packs and 1.2 kW hubs without flexing like stock Xiaomi frames.【F:data/vesc_help_group/text_slices/input_part000.txt†L26583-L26608】
- Community salvage runs continue to surface Dualtron, Etwow, and Xiaomi donor parts—complete with 60 V packs and heavy-duty motors—illustrating how group buys and friendships keep premium frames affordable.【F:data/vesc_help_group/text_slices/input_part000.txt†L26959-L27062】

### Maintenance & Safety Notes (Batch 19)
- Breaking a bead with dish soap and dusting the tube in talc/baby powder made roadside tire swaps painless and cut inner-tube chafing on reassembly.【F:data/vesc_help_group/text_slices/input_part000.txt†L26881-L26890】
- Riders reminded each other that regen-only setups are unsafe on 20 S builds; keep mechanical brakes in spec before trusting wheel-locking e-brakes at 50–65 km/h.【F:data/vesc_help_group/text_slices/input_part000.txt†L26940-L26947】
- Kelly KLS controllers often refuse USB connections—plan on using the BLE module or legacy Windows XP drivers when configuring a scooter with that hardware.【F:data/vesc_help_group/text_slices/input_part000.txt†L26951-L26956】

### Build Progress & Performance Logs (Batch 19)
- Artem’s Vsett 9 refresh now runs dual 650 W hubs on a 16 S 8 P Samsung 35E pack with a dual Ubox, SmartController integration, LED spacers, and a GPS/4G tracker; the build hits 50 km/h in 5.5 s with only 3.6 V sag at 27 A battery and 80–85 A phase per motor.【F:data/vesc_help_group/text_slices/input_part000.txt†L26744-L26758】【F:data/vesc_help_group/text_slices/input_part000.txt†L27147-L27170】【F:data/vesc_help_group/text_slices/input_part000.txt†L27224-L27230】
- That project also exposed rear-motor sync issues above 85 A phase—likely a failed MOSFET or sensor wiring—prompting diagnostics via VESC logs and sensorless detections before raising current limits further.【F:data/vesc_help_group/text_slices/input_part000.txt†L27322-L27398】

### High-Voltage Experiments & Motor Limits (Batch 20)
- Face de Pin Sucé confirmed that feeding a Citycoco’s 800 W hub with 26 S and 100 A cooked the motor during an uphill pull, underscoring how quickly overvolting small scooter hubs can destroy windings.【F:data/vesc_help_group/text_slices/input_part000.txt†L27405-L27406】
- Koxx relies on VESC Tool phase-current graphs to expose blown MOSFETs, giving builders a simple bench check before chasing intermittent drive faults on custom controllers.【F:data/vesc_help_group/text_slices/input_part000.txt†L27408-L27412】

### Sensorless Setup & Fault Diagnostics (Batch 20)
- Running “sensorless” detection with hall plugs still connected can misbehave—Face de Pin Sucé recommends unplugging the halls and re-detecting to guarantee a clean sensorless profile.【F:data/vesc_help_group/text_slices/input_part000.txt†L27420-L27427】
- Mirono’s past DRV faults manifested as loud BLDC-only operation until he recalibrated FOC, while Face de Pin Sucé ultimately traced his own error to a dead DRV chip—use these symptoms to separate firmware slips from hardware failures.【F:data/vesc_help_group/text_slices/input_part000.txt†L27428-L27432】
- When Spintend’s external ADC module reads nonsense, the crew now bypasses it temporarily: feed 3.3 V, signal, and ground straight from the VESC to the throttle/brake for testing, but avoid slamming 5 V accessories into the 3.3 V ADC rail to prevent board damage.【F:data/vesc_help_group/text_slices/input_part000.txt†L27530-L27548】
- A Wheelway controller that lost braking and only crawled at 20 A was ultimately blamed on a missing phase or loose motor lead—if a scooter brakes when you blip the throttle, inspect phase wiring and hall orientation before retuning FOC again.【F:data/vesc_help_group/text_slices/input_part000.txt†L27891-L27907】
- Artem’s JK smart BMS cut both charge and discharge because a balance lead wasn’t soldered; the pack cycled through “short circuit” and “low voltage” states until the loose wire restored proper cell readings, so inspect every tap after high-heat soldering.【F:data/vesc_help_group/text_slices/input_part000.txt†L27881-L27883】

### Field Weakening & Performance Tuning (Batch 20)
- Field weakening on VESC triggers at a user-set duty cycle; Face de Pin Sucé runs 100 A at 90 % duty to spin a hub from 38 kERPM to 53 kERPM—about 40 % more rpm—but it still yanks ~20 A battery while dumping heat, so reserve it for short bursts on cool motors.【F:data/vesc_help_group/text_slices/input_part000.txt†L27589-L27625】
- Dropping acceleration ramping time to 0.05 s sharpens launches for riders who want more snap than VESC’s default smoothing provides.【F:data/vesc_help_group/text_slices/input_part000.txt†L27596-L27600】
- Artem reminded everyone that field weakening only makes sense if the motor is still running cool; otherwise the overload simply accelerates failure instead of adding meaningful top speed.【F:data/vesc_help_group/text_slices/input_part000.txt†L27642-L27647】
- Koxx replicated the gains on bench videos and noted the feature can be layered onto Xiaomi controllers running VESC firmware, but they’re still validating road behaviour before recommending production profiles.【F:data/vesc_help_group/text_slices/input_part000.txt†L27953-L27962】

### Motor Temperature Monitoring & Sensor Placement (Batch 20)
- Artem’s Vsett build logs emphasize installing 100 kΩ NTC probes inside the hub to monitor winding temperature; the shell can feel barely warm while the coils hit 90 °C, so hand checks alone are misleading compared with the stock controller’s behaviour.【F:data/vesc_help_group/text_slices/input_part000.txt†L27122-L27143】【F:data/vesc_help_group/text_slices/input_part000.txt†L27328-L27341】
- Pairing FOC controllers with those sensors shows how much cooler they run versus square-wave Minimotors hardware—Mirono’s old controllers cooked motors faster, whereas the dual Ubox setup keeps temperatures manageable even when phase amps climb.【F:data/vesc_help_group/text_slices/input_part000.txt†L27138-L27143】

### Phase Current Limits & Fault Symptoms (Batch 20)
- The crew treats 120–130 A phase per motor (160 A ABS max) as a realistic target for dual Spintend builds; if a hub starts “stuttering” above ~85 A, assume a blown MOSFET or loose phase lead rather than simply backing off current and inspect with VESC logs or sensorless detection runs.【F:data/vesc_help_group/text_slices/input_part000.txt†L27247-L27318】【F:data/vesc_help_group/text_slices/input_part000.txt†L27352-L27378】
- Hall disconnects combined with fresh detection cycles remain the go-to diagnostic step, and running sensorless temporarily can confirm whether the issue sits in the controller stage or the hall harness.【F:data/vesc_help_group/text_slices/input_part000.txt†L27247-L27307】【F:data/vesc_help_group/text_slices/input_part000.txt†L27378-L27389】

### Square-Wave vs. FOC Launch Behaviour (Batch 20)
- Square-wave aftermarket controllers remain attractive at ~€80 for a dual kit with dash, but they punch 150–200 A phase at launch, feel abrupt to new riders, and run noisier than VESC-based FOC setups despite their simplicity.【F:data/vesc_help_group/text_slices/input_part000.txt†L27268-L27299】
- FOC ramps torque more gently yet maintains pressure past 10 km/h, letting AWD scooters stay controllable at 80–95 A phase per wheel; riders still toggle eco modes for guests to soften the initial shove.【F:data/vesc_help_group/text_slices/input_part000.txt†L27247-L27283】

### Display, Firmware & Control Integration (Batch 20)
- Vsett-style displays feed logic power back into the controller via the blue “DS” pin; the display MOSFET doubles as the on/off switch, only wakes after the RFID tag is accepted, and chats with the controller every 500 ms while receiving commands every 200 ms.【F:data/vesc_help_group/text_slices/input_part000.txt†L27641-L27678】
- The dual-motor button shares a harness with the controller—Artem continuity-tested the DS line from button to display and ECU, concluding it toggles the slave drive while the display merely mirrors status on its indicator.【F:data/vesc_help_group/text_slices/input_part000.txt†L27658-L27683】
- Xiaomi controllers now run Koxx’s VESC-based firmware with BLE support; auto-detection already works, sensorless mode is next, and the STM32 only uses about 30 % CPU, opening a path to 100 V/100 A performance on €25 hardware once RAM/flash limits are addressed.【F:data/vesc_help_group/text_slices/input_part000.txt†L27718-L27738】【F:data/vesc_help_group/text_slices/input_part000.txt†L27821-L27845】
- The companion Android beta looks cleaner than stock VESC Tool but still mixes certain motor parameters, so testers are keeping it off daily riders until those quirks and sensorless launches are solved.【F:data/vesc_help_group/text_slices/input_part000.txt†L27813-L27819】【F:data/vesc_help_group/text_slices/input_part000.txt†L27846-L27868】

### Controller Cooling & Deck Interface (Batch 20)
- Luis’ 100 km/h hill pulls pushed his dual Ubox to ~65 °C before he ever added thermal paste; the crew plans a before/after rerun bolting the controller flat to the deck with paste to prove how much the aluminium tray can wick away on summer commutes.【F:data/vesc_help_group/text_slices/input_part000.txt†L26527-L26547】
- Builders warn that exposed copper/nickel links oxidise quickly—Mirono’s deck connector turned black outdoors, raising resistance and heat—so keep joints sealed or rework them before chasing higher phase currents.【F:data/vesc_help_group/text_slices/input_part000.txt†L26659-L26664】

### Battery Packaging & Busbar Design (Batch 20)
- Rental G30 conversions easily swallow “thick” 13 S 5 P 21700 packs, but sourcing 220 mm heat-shrink inside the EU is tough; Artem keeps limited stock while others hunt overseas, so plan packaging early when scaling beyond commuter-sized batteries.【F:data/vesc_help_group/text_slices/input_part000.txt†L26576-L26586】
- Mirono’s honeycomb layout forced an entire 5 P group through a single 8 mm nickel strip; Artem’s fix is to rebuild with sheet bussing or at least five 7–8 mm straps in parallel (0.25–0.30 mm thick) so each series bridge handles ≥35–40 A without hot spots before stepping up to 20 S.【F:data/vesc_help_group/text_slices/input_part000.txt†L26824-L26876】

### Waterproofing & Deck Maintenance (Batch 20)
- Rental-frame builds stay dry by packing silica gel in the enclosure and sealing lids with automotive engine sealant; the silicone peels open by hand for service yet keeps water out far better than leaving the deck loose or chasing bespoke gaskets.【F:data/vesc_help_group/text_slices/input_part000.txt†L26790-L26818】

### Power Accessories & BMS Configuration (Batch 20)
- Ubox’s onboard 12 V rail can comfortably feed ≈1.5 A, letting riders power wireless light switches or Artem’s tiny 20 × 11 × 11 mm speed-limiter relay without an extra DC-DC converter—just wire 12 V, ground, and the normally-closed lead as shown.【F:data/vesc_help_group/text_slices/input_part000.txt†L27554-L27569】
- Builders stuck waiting on 7–16 S ANT stock are successfully running the 8–20 S model on 16 S packs, with no observed downsides beyond possible MOSFET resistance changes.【F:data/vesc_help_group/text_slices/input_part000.txt†L27572-L27579】
- Artem’s balance-lead failure shows why to reflow every tap when a pack starts tripping protections—one cold joint can make the BMS miscount cells and alternately flag short circuits and undervoltage.【F:data/vesc_help_group/text_slices/input_part000.txt†L27881-L27883】

### Battery Sourcing & Cell Comparisons (Batch 20)
- Artem’s 16 S 8 P Samsung 35E pack fits a Vsett 9/10 deck once the spacer grows the cavity to roughly 155 mm × 400 mm—up from the stock ~48 mm height—and the cell was chosen because it holds energy well up to ~7 A continuous draw.【F:data/vesc_help_group/text_slices/input_part000.txt†L27147-L27153】
- Community price checks put Samsung 30T cells around €2.50, 35E at €3.40, and 50G or 50S at €4–4.5 with deeper discounts on larger quantities, beating typical NKON retail pricing.【F:data/vesc_help_group/text_slices/input_part000.txt†L27160-L27180】
- Artem’s discharge testing shows Molicel P42A outperforms Samsung 40T at both 20 A and 30 A, while 50G excels in the 7–15 A band and 50S matches P42A at higher loads albeit at roughly double the price—use these curves to match cells to expected current draw.【F:data/vesc_help_group/text_slices/input_part000.txt†L27165-L27173】

### Motor Supply & Frame Upgrades (Batch 20)
- Face de Pin Sucé is winding down repair work to focus on VESC, motor, and frame development but can still source heavy-duty hubs (e.g., 75 mm magnet/110 mm stator units with 10 mm² phase wires) that were selling for about €750 a pair.【F:data/vesc_help_group/text_slices/input_part000.txt†L27040-L27080】
- Rion/Weped FF-spec motors are available through the same channel at roughly €340 each in France, though rising freight charges can erase the bargain for international buyers.【F:data/vesc_help_group/text_slices/input_part000.txt†L27090-L27103】

### Controller Cooling & Maintenance Reminders (Batch 20)
- Vsett owners swapping to dual Ubox controllers noted the stock Minimotors square-wave ESCs ran motors noticeably hotter; repasting the Ubox to the deck is still recommended even if it requires battery removal to access mounting blocks.【F:data/vesc_help_group/text_slices/input_part000.txt†L27130-L27146】

### ADC Troubleshooting Tips (Batch 20)
- When Spintend’s ADC adaptor returns erratic readings, confirm the 5 V/3.3 V selector is firmly set, then temporarily bypass the board with the VESC’s 3.3 V rail for diagnostics—keeping throttle travel short to avoid overstressing 5 V sensors—and reconnect the adaptor once wiring is verified.【F:data/vesc_help_group/text_slices/input_part000.txt†L27520-L27548】
- Builders cautioned that hot-plugging 5 V throttles into the 3.3 V ADC pins can instantly brick the module; isolate power before rewiring and avoid full-sweep tests when running direct-to-VESC experiments.【F:data/vesc_help_group/text_slices/input_part000.txt†L27530-L27545】

### Charging Equipment & Battery Safety (Batch 20)
- A budget “5 A” AliExpress charger stayed in constant-current mode at 4.3 A from empty to full, never tapering and risking 4.3 A into already-full cells—avoid these CC-only bricks unless you have a smart BMS clamping per-cell voltage.【F:data/vesc_help_group/text_slices/input_part000.txt†L27755-L27780】
- Artem’s active-balancing BMS shuffles up to 600 mA once cells drift more than 0.01 V, keeping deviations within 3–7 mV during discharge and cutting charge if any cell crosses 4.22 V—without those safeguards a single weak group could creep toward 4.35 V and degrade rapidly.【F:data/vesc_help_group/text_slices/input_part000.txt†L27770-L27778】
- That lightweight charger is only useful for travel quick-charges: it’s tiny (~600 g) but still outputs 67.6 V unloaded and never enters CV, so swap to branded YZPower-style supplies with adjustable voltage/amps for daily use.【F:data/vesc_help_group/text_slices/input_part000.txt†L27758-L27781】【F:data/vesc_help_group/text_slices/input_part000.txt†L27794-L27802】

### Controller Roadmap (Batch 20)
- Face de Pin Sucé is prototyping a next-generation VESC that aims for 200 A continuous capability, giving the crew hope for a native high-current option without resorting to third-party industrial drives.【F:data/vesc_help_group/text_slices/input_part000.txt†L27549-L27549】
- Riders comparing beta and production Spintend Ubox singles report minor hardware tweaks—extra silicone pads, revised layouts, and easier assembly/repair steps—but they’re double-checking pinouts before swapping harnesses to avoid damaging the refreshed boards.【F:data/vesc_help_group/text_slices/input_part000.txt†L27930-L27939】

### Build Progress & Component Notes (Batch 20)
- Face de Pin Sucé’s custom high-power platform already touched 134 km/h on 15 S with dual Ubox controllers and is targeting 20 S, while new 75 mm hubs are headed for a Weped SS running a 21 S 11 P Molicel pack—illustrating the hardware margin needed for 140 km/h goals.【F:data/vesc_help_group/text_slices/input_part000.txt†L27447-L27515】【F:data/vesc_help_group/text_slices/input_part000.txt†L27704-L27716】
- The group weighed a massive hub at 6.5 kg bare motor, confirming how much mass ultra-low-kV scooters carry to deliver steady torque up to ~58 km/h on 16 S packs.【F:data/vesc_help_group/text_slices/input_part000.txt†L27849-L27856】【F:data/vesc_help_group/text_slices/input_part000.txt†L27893-L27894】
- Flipsky’s 75/200 is effectively an A200S clone with historic heat issues; Face de Pin Sucé is eager to see whether modern builds solve the thermal limitations before trusting it at high battery amps.【F:data/vesc_help_group/text_slices/input_part000.txt†L27914-L27922】
- Tudor is refitting a Vsett 10 with a 100 V VESC and planning a 22 S battery while keeping a Xiaomi Max on upgraded 1400 W hubs—he’s already seen those FLJ motors hit 14 kW peaks on 16 S without overheating at 150 A phase, hinting at the headroom dual setups can exploit.【F:data/vesc_help_group/text_slices/input_part000.txt†L27964-L28024】
- Vsett 10+ spares continue to surface, and Paolo shared 6 mm (≈9 AWG) motor leads rated for 3 kW continuous per hub, giving others a sourcing lead for high-current harnesses.【F:data/vesc_help_group/text_slices/input_part000.txt†L27923-L27999】

### Controller Diagnostics & Field-Weakening Tests (Batch 20)
- Use VESC Tool phase-current graphs to spot dead MOSFETs: a failed DRV shows noisy hall behaviour, forces BLDC-only operation, and triggers shutdown over 10 % throttle until the controller is repaired.【F:data/vesc_help_group/text_slices/input_part000.txt†L27404-L27433】
- When switching to sensorless mode for troubleshooting, disconnect hall leads and rerun detection—leaving halls attached sometimes prevents a clean handover.【F:data/vesc_help_group/text_slices/input_part000.txt†L27420-L27433】
- Bench tests with 90 % duty field weakening pulled 100 A phase (≈20 A battery) to jump from 38 kERPM to 53 kERPM at 1.2 kW, confirming the feature adds ~40 % speed but generates heavy heat and poor efficiency on scooters.【F:data/vesc_help_group/text_slices/input_part000.txt†L27601-L27625】【F:data/vesc_help_group/text_slices/input_part000.txt†L27642-L27648】

### Harness & Display Reverse Engineering (Batch 20)
- The Vsett “DS” lead feeds display power back into the controller once the RFID tag authenticates; the throttle itself stays analog while CAN-like serial messages handle modes and indicators at 200–500 ms intervals.【F:data/vesc_help_group/text_slices/input_part000.txt†L27632-L27679】
- Dual-motor enable traces share continuity between the button, display, and controller, so retrofitters must keep the signal intact when repinning harnesses for VESC conversions.【F:data/vesc_help_group/text_slices/input_part000.txt†L27658-L27669】

### Accessory Power & ADC Troubleshooting (Batch 20)
- Spintend’s 12 V rail can feed remote relay receivers (~1.5 A), enabling wireless lighting switches, but beta users warn to confirm module draw before ditching DC-DC converters.【F:data/vesc_help_group/text_slices/input_part000.txt†L27554-L27571】
- ADC daughterboards remain sensitive: hot-plugging 5 V throttles risks killing the module, so falls back to direct 3.3 V wiring should only be attempted after expert guidance.【F:data/vesc_help_group/text_slices/input_part000.txt†L27511-L27548】

### Charger & BMS Selection (Batch 20)
- Riders running 16 S packs are resorting to 8–20 S ANT Smart BMS units when 7–16 S versions are out of stock without seeing obvious downsides, though they suspect higher-voltage variants may use different MOSFETs.【F:data/vesc_help_group/text_slices/input_part000.txt†L27571-L27580】
- Beware budget “4.3 A” chargers that never taper to constant voltage—one unit stayed at 4.4 A even 0.06 V before full charge, risking overvoltage on the highest cell despite refund-worthy quality issues.【F:data/vesc_help_group/text_slices/input_part000.txt†L27770-L27803】

## Open Questions / Follow-ups
- Document a repeatable method for drying or resealing Daly BMS units that arrive fully potted so riders can recover from moisture events without replacing £80 boards.【F:data/vesc_help_group/text_slices/input_part000.txt†L6520-L6620】
- Publish a Ubox accessory-power note confirming the 12 V rail’s sustained current limit and safe wiring for wireless light relays and speed-limit switches so riders stop guessing at load capacity.【F:data/vesc_help_group/text_slices/input_part000.txt†L27554-L27569】
- Map the Vsett “DS” harness, RFID wake logic, and dual-motor indicator wiring so future retrofits don’t misroute the display’s return power into controller inputs.【F:data/vesc_help_group/text_slices/input_part000.txt†L27641-L27683】
- Draft a troubleshooting checklist for JK/ANT smart BMS installs that highlights balance-lead continuity tests after soldering so false short/undervoltage trips get resolved quickly.【F:data/vesc_help_group/text_slices/input_part000.txt†L27881-L27883】
- Create a charger vetting guide that flags constant-current-only “5 A” bricks and recommends CV-capable alternatives plus power-meter checks before daily use.【F:data/vesc_help_group/text_slices/input_part000.txt†L27755-L27781】
- Publish a Kelvin four-wire cell testing guide so 20 A discharge checks measure at the cell tabs instead of through hot, high-resistance clip leads that mimic 1.9 V sag on healthy cells.【F:data/vesc_help_group/text_slices/input_part000.txt†L25901-L25926】
- Publish an ANT Smart BMS quick-start covering the post-July 2021 app requirement and the hidden charge/discharge toggle so installers aren’t locked out of configuration or manual pack shutdowns.【F:data/vesc_help_group/text_slices/input_part000.txt†L24635-L24649】【F:data/vesc_help_group/text_slices/input_part000.txt†L25154-L25159】
- Write a note on sharing Spintend’s single-ESC UART header between the ADC board and Bluetooth module, including 3.3 V/5 V switch handling and strain relief to prevent board failures.【F:data/vesc_help_group/text_slices/input_part000.txt†L24761-L24779】【F:data/vesc_help_group/text_slices/input_part000.txt†L25225-L25254】
- Draft a CNC template and torque spec for one-piece Xiaomi/Blade rotor spacers so tall adapters stop relying on loose washer stacks.【F:data/vesc_help_group/text_slices/input_part000.txt†L22903-L22942】
- Draft a Xiaomi/Ninebot charge-port upgrade note covering GX16-4 pin paralleling, JST replacement, and XT30 retrofits so 6–8 A charging doesn’t cook factory pigtails.【F:data/vesc_help_group/text_slices/input_part000.txt†L21739-L21888】
- Capture JK Smart BMS setup guidance (charge/discharge toggles, regen behaviour, and recommended AS150 wiring) so builders don’t disable regen by accident or choke the new hardware with undersized leads.【F:data/vesc_help_group/text_slices/input_part000.txt†L26622-L26633】【F:data/vesc_help_group/text_slices/input_part000.txt†L27213-L27225】
- Draft a lighting power guide for Ubox/Spintend builds covering relay wiring, accessory-current budgets, and why throttle 5 V rails can’t feed add-on lamps without risking regulator failure—now noting that single Spintend ESCs lack a 12 V rail, so buck converters and fusing are mandatory.【F:data/vesc_help_group/text_slices/input_part000.txt†L16921-L16943】【F:data/vesc_help_group/text_slices/input_part000.txt†L17986-L18013】【F:data/vesc_help_group/text_slices/input_part000.txt†L18956-L18988】
- Capture a troubleshooting memo for Spintend anti-slip settings, regen tuning, and post-fault log retrieval so single-motor riders avoid needless power cuts and know how to extract diagnostics without BLE.【F:data/vesc_help_group/text_slices/input_part000.txt†L25452-L25507】【F:data/vesc_help_group/text_slices/input_part000.txt†L25550-L25599】
- Publish a CAN lighting board quick-start (pinout, firmware register map, CAN-button harness) so builders can replicate koxx’s 10 A accessory hub without reverse-engineering long frames.【F:data/vesc_help_group/text_slices/input_part000.txt†L23689-L23731】【F:data/vesc_help_group/text_slices/input_part000.txt†L24321-L24333】
- Publish a Wheelway hall QC checklist and temperature-sensor retrofit (metal-debris cleaning, SS41F sourcing, 30 AWG PTFE routing) so Xiaomi conversions stop losing halls within the first 25 km, plus voltage-divider guidance for 5 V levers that overdrive 3.3 V ADCs.【F:data/vesc_help_group/text_slices/input_part000.txt†L16966-L17029】【F:data/vesc_help_group/text_slices/input_part000.txt†L17250-L17305】【F:data/vesc_help_group/text_slices/input_part000.txt†L17545-L17566】【F:data/vesc_help_group/text_slices/input_part000.txt†L19234-L19280】
- Create a headlight benchmarking sheet capturing tested wattage vs. claims and recommending trustworthy vendors for 15–25 W projector pods.【F:data/vesc_help_group/text_slices/input_part000.txt†L23782-L23839】【F:data/vesc_help_group/text_slices/input_part000.txt†L23860-L23899】
- Assemble a Xiaomi motor sourcing matrix comparing Blade 10, Zero 10X, and Boyueda/Laotie hubs (axle spacing, disc offset, kv, phase-current tolerance) before riders commit to €150–€250 imports.【F:data/vesc_help_group/text_slices/input_part000.txt†L17036-L17067】【F:data/vesc_help_group/text_slices/input_part000.txt†L17145-L17193】
- Draft a safety brief for Inmotion LF8 BMS bypasses covering solder points, insulation, and monitoring requirements so renters don’t run packs unprotected.【F:data/vesc_help_group/text_slices/input_part000.txt†L24011-L24033】
- Publish a SmartController wiring and dual-VESC mode guide so Vsett/Zero riders can keep the OEM display without overheating a single rear hub.【F:data/vesc_help_group/text_slices/input_part000.txt†L22102-L22144】
- Package a hall-detection troubleshooting workflow (full-charge detection, warm stators, manual 70 A sweeps) so riders can eliminate launch “clonks” without bricking new configs.【F:data/vesc_help_group/text_slices/input_part000.txt†L18463-L18495】
- Compare Daly vs. ANT smart BMS usability (manual toggles, packaging, telemetry) to recommend when riders should budget the pricier platform for compact decks.【F:data/vesc_help_group/text_slices/input_part000.txt†L24390-L24400】【F:data/vesc_help_group/text_slices/input_part000.txt†L24400-L24411】【F:data/vesc_help_group/text_slices/input_part000.txt†L24635-L24665】
- Write an ADC protection memo for single-VESC scooters (shielding, no hot-plugging, regen spike mitigation) so converter boards survive throttle/brake integration experiments.【F:data/vesc_help_group/text_slices/input_part000.txt†L18335-L18382】【F:data/vesc_help_group/text_slices/input_part000.txt†L18423-L18444】
- Publish a tubeless mounting guide for 10″ scooter rims that covers bead prep, lubrication, safe clamping pressures, and when to abandon butchered tires for split-rim conversions.【F:data/vesc_help_group/text_slices/input_part000.txt†L18668-L18755】
- Document tubeless rim dent repair vs. replacement steps for 10″ scooters, including sealant limits and when to scrap the hub after major curb strikes.【F:data/vesc_help_group/text_slices/input_part000.txt†L17940-L18007】
- Produce a ferrofluid application and maintenance guide (dosage, cleanup, efficiency trade-offs) based on the group’s magnet-heating discussion and bottle applicator tips.【F:data/vesc_help_group/text_slices/input_part000.txt†L25632-L25678】【F:data/vesc_help_group/text_slices/input_part000.txt†L25723-L25748】
- Capture safe regen current ramps for Spintend controllers—ideally with oscilloscope traces—to verify Artem’s “battery Ah equals max regen amps” guideline under different wheel sizes.【F:data/vesc_help_group/text_slices/input_part000.txt†L7299-L7345】【F:data/vesc_help_group/text_slices/input_part000.txt†L7426-L7434】
- Test Spintend’s rheostatic brake module with different pack voltages to quantify how the extra 10 A sink alters regen budgets and MOSFET temperatures before recommending production wiring diagrams.【F:data/vesc_help_group/text_slices/input_part000.txt†L12811-L12821】
- Prototype a hall-effect brake lever mod (pot placement, mechanical linkages, firmware scaling) that delivers true analog regen without sacrificing premium hydraulic hardware.【F:data/vesc_help_group/text_slices/input_part000.txt†L7100-L7212】
- Characterise Ubox V2 thermal headroom at 200–300 A phase with deck-mounted fans, copper plates, and different tires before recommending new firmware limits.【F:data/vesc_help_group/text_slices/input_part000.txt†L22458-L22568】
- Document how to embed 4G/GPS tracker boards (SIM7600, BMW modules) inside scooter packs and tie them into SmartController cutoffs for theft deterrence.【F:data/vesc_help_group/text_slices/input_part000.txt†L22620-L22662】
- Track the production release of Spintend’s single-channel controller (final dimensions, IMU support, pricing) and confirm whether the external USB idea makes it into retail units.【F:data/vesc_help_group/text_slices/input_part000.txt†L7442-L7459】【F:data/vesc_help_group/text_slices/input_part000.txt†L7732-L7772】
- Investigate whether Koxx’s weak sensorless launches stem from a damaged Flipsky power stage or if firmware tuning alone can close the torque gap versus his shunted Minimotors ESC.【F:data/vesc_help_group/text_slices/input_part000.txt†L7583-L7900】
- Compile throttle failure modes on Xiaomi/Zero-style triggers and identify rugged replacements (e.g., Spintend) plus wiring best practices to avoid intermittent pulses mid-ride.【F:data/vesc_help_group/text_slices/input_part000.txt†L7546-L7578】
- Publish a customs/VAT playbook that captures the June–July 2021 experiences—Luxembourg freight routes, €24 Belgian handling fees, and the new AliExpress IOSS flow—to help EU buyers minimise surprise surcharges post-IOSS rollout.【F:data/vesc_help_group/text_slices/input_part000.txt†L7036-L7073】【F:data/vesc_help_group/text_slices/input_part000.txt†L8321-L8332】
- Document the structural and waterproofing steps needed to replicate Mirono’s 260-cell deck extender (mounting, sealing, wiring slack) so long-range riders can safely package 15 S 17 P batteries on Xiaomi/Ninebot frames.【F:data/vesc_help_group/text_slices/input_part000.txt†L6888-L6935】
- Evaluate long-term durability of plexiglass deck lids and Artem’s LED spacer concept, including gasket compression and load sharing, before recommending clear covers for commuter scooters.【F:data/vesc_help_group/text_slices/input_part000.txt†L12968-L13011】
- Capture definitive guidance on Spintend’s ADC adapter switch positions (NO/NC, 3.3 V vs 5 V) and compatible brake connectors so riders can wire MT5e/CMe5/Shimano levers correctly the first time.【F:data/vesc_help_group/text_slices/input_part000.txt†L8270-L8330】
- Map Rowan’s proposed 4WD switch wiring (grounding the slave switch lead, tapping 12 V from the horn output) to confirm safe implementation on dual Spintend decks.【F:data/vesc_help_group/text_slices/input_part000.txt†L8388-L8393】
- Reverse-engineer the Ninebot rental battery lock harness and brake-mount adapter so hot-swappable packs and disc conversions can be replicated on other fleet frames.【F:data/vesc_help_group/text_slices/input_part000.txt†L9201-L9214】
- Benchmark Daly’s slim 120 A boards against ANT smart BMS units for heat rise and deck fitment to decide when charge-only + fuse is the safer packaging compromise on Boosted-class scooters.【F:data/vesc_help_group/text_slices/input_part000.txt†L9232-L9263】【F:data/vesc_help_group/text_slices/input_part000.txt†L9380-L9399】
- Document recyclable kraftplex/PETG pack jackets and compare them with traditional fish paper so EU builders can satisfy recycling guarantees without trapping excess heat.【F:data/vesc_help_group/text_slices/input_part000.txt†L9599-L9649】
- Validate Artem’s 25 mm accordion welding workflow (including RePackr balancing) by producing a step-by-step jig guide for 15 S scooter packs.【F:data/vesc_help_group/text_slices/input_part000.txt†L9683-L9731】
- Compile discharge decision trees contrasting 48X, 50G, P42A, and 50E cells across 10–20 A loads with expected pack temperatures so riders can size 12 S Xiaomi upgrades confidently.【F:data/vesc_help_group/text_slices/input_part000.txt†L10442-L10485】【F:data/vesc_help_group/text_slices/input_part000.txt†L10634-L10658】
- Create a CAN/battery power sequencing checklist for 4WD Spintend installs to prevent repeat CAN-transceiver failures when controllers wake at different times.【F:data/vesc_help_group/text_slices/input_part000.txt†L10290-L10351】
- Capture the Boosted Rev throttle pinout and voltage range so other VESC builders can replicate koxx’s analog brake integration without trial and error.【F:data/vesc_help_group/text_slices/input_part000.txt†L10882-L10894】
- Confirm whether Daly LCD-only BMS units can expose a remote discharge reset (or accept the Bluetooth dongle retrofit) so sealed decks aren’t forced open after undervoltage trips.【F:data/vesc_help_group/text_slices/input_part000.txt†L15647-L15684】【F:data/vesc_help_group/text_slices/input_part000.txt†L19140-L19172】
- Document the SIM-enabled remote BMS activation process Artem described (5 V precharge, charger wake-up, shutoff behaviour) before more builders adopt that platform.【F:data/vesc_help_group/text_slices/input_part000.txt†L18837-L18854】
- Produce a Ninebot G30 hall-sensor cross-reference (SS41F vs. R43 pinouts, orientation diagrams, EU sourcing) to stop repeated failed replacements.【F:data/vesc_help_group/text_slices/input_part000.txt†L16405-L16535】
- Quantify resistance/temperature differences between 3 mm solid-core and stranded AWG10 leads over 15–50 cm runs to validate the claimed ~40 % ampacity boost for high-current scooter packs.【F:data/vesc_help_group/text_slices/input_part000.txt†L15706-L15738】
- Publish a SmartDisplay bring-up checklist that isolates USB ground paths (or leans on BLE/Wi-Fi) so developers stop sacrificing 3.3 V rails when debugging dual VESC installs.【F:data/vesc_help_group/text_slices/input_part000.txt†L11633-L11705】
- Compile a connector upgrade guide for backpack and external packs, covering AS120 mains, 4 mm bullets, MR60 limits, and direct-solder strategies to keep 80–120 A routes cool on long leads.【F:data/vesc_help_group/text_slices/input_part000.txt†L13746-L13819】
- Document safe voltage-dividing or adapter-board options for MiniMotors EYE throttles so builders never feed 4 V into 3.3 V VESC ADC pins.【F:data/vesc_help_group/text_slices/input_part000.txt†L11903-L11907】
- Evaluate the JKBMS active-balancer platform (firmware, telemetry, thermal behavior) as a compact alternative to Daly/ANT for 16 S–20 S scooter packs.【F:data/vesc_help_group/text_slices/input_part000.txt†L11081-L11093】
- Draft guidance on paralleling dissimilar packs (capacity, BMS limits, current thresholds) so dual-battery Wolf builds avoid repeated 115 A “short” trips.【F:data/vesc_help_group/text_slices/input_part000.txt†L11826-L11854】
- Assemble an EU compliance cheat sheet covering stealth motor covers, engraving rules, and speed-limited firmware talking points for dual-motor sleepers.【F:data/vesc_help_group/text_slices/input_part000.txt†L12306-L12321】
- Turn the rental lock servo wiring/waterproofing thread into a reference so builders can re-use or delete the latch without compromising ingress protection.【F:data/vesc_help_group/text_slices/input_part000.txt†L11269-L11312】
- Scope firmware or SmartDisplay macro work that delivers reliable cruise control on Spintend setups to reduce rider fatigue on long-range throttles.【F:data/vesc_help_group/text_slices/input_part000.txt†L11901-L11930】
- Publish a VESC telemetry setup guide that walks through counting rotor magnets and measuring loaded wheel diameter so range and speed data stay trustworthy without relying on laggy GPS traces.【F:data/vesc_help_group/text_slices/input_part000.txt†L13901-L13915】
- Ship a Spintend single connectivity cheat sheet covering Bluetooth add-ons, CAN linking, and when extra ADC boards are warranted so riders stop missing modules or miswiring dual singles.【F:data/vesc_help_group/text_slices/input_part000.txt†L14211-L14233】【F:data/vesc_help_group/text_slices/input_part000.txt†L14894-L14915】
- Document resistor-divider or adapter-board wiring for 5 V hall throttles/brakes to keep STM32 ADC pins under 3.3 V and avoid repeat failures.【F:data/vesc_help_group/text_slices/input_part000.txt†L14233-L14260】
- Stress-test hot-glue, silicone ribs, and honeycomb spacers for dense scooter packs so we can recommend retention methods that survive 80 °C cells and vibration.【F:data/vesc_help_group/text_slices/input_part000.txt†L14327-L14339】【F:data/vesc_help_group/text_slices/input_part000.txt†L14716-L14727】
- Compile a vendor-vetting checklist for bargain controller listings, using the €140 “Spintend” case and ongoing STM32 shortages as red flags riders should verify before paying.【F:data/vesc_help_group/text_slices/input_part000.txt†L14758-L14772】
- Create a Monorim brake adapter template (torque arm, shim stack, bolt specs) so 140–160 mm discs fit without grinding fork legs.【F:data/vesc_help_group/text_slices/input_part000.txt†L22794-L22843】
- Capture field-weakening enablement steps and current ceilings once VESC Tool 5.3 leaves beta so builders know when the extra 8 km/h is safe to activate.【F:data/vesc_help_group/text_slices/input_part000.txt†L15031-L15033】
- Map Vsett 9/10 motor voltage expectations, split-rim service steps, and shipping options so 48 V riders know what to expect before jumping to 60 V hubs.【F:data/vesc_help_group/text_slices/input_part000.txt†L15035-L15108】
- Write a Daly shutdown/back-EMF recovery SOP—with moisture inspections and solder-ball cleaning—to prevent repeats of the VESC failure that followed a BMS trip.【F:data/vesc_help_group/text_slices/input_part000.txt†L15292-L15400】
- Publish an accessory wiring quick-reference (fuse sizing, wire gauge, load math) for 48 V lighting runs so builders stop oversizing harnesses or skipping inline protection.【F:data/vesc_help_group/text_slices/input_part000.txt†L19990-L20099】
- Document a Spintend single cooling retrofit (fan placement, copper spacers, deck airflow, surface prep) before recommending 130 A settings to Dualtron and Spider owners chasing high regen.【F:data/vesc_help_group/text_slices/input_part000.txt†L20190-L20299】
- Compile Blade hub fitment drawings (axle span, disc offset, hardware specs) so Xiaomi fork swaps are repeatable without re-measuring every delivery.【F:data/vesc_help_group/text_slices/input_part000.txt†L20527-L20536】
- Track the Ubox Pro/100 V launch readiness and verify revised units ship clean (no shavings/solder balls) with hardened I/O before advocating upgrades.【F:data/vesc_help_group/text_slices/input_part000.txt†L20490-L20506】【F:data/vesc_help_group/text_slices/input_part000.txt†L20940-L20950】
- Capture RMA shipping guidance and capacitor-upgrade options for Spintend singles so riders can choose faster couriers and prevent repeat electrolytic failures.【F:data/vesc_help_group/text_slices/input_part000.txt†L20741-L20786】【F:data/vesc_help_group/text_slices/input_part000.txt†L20872-L20888】
