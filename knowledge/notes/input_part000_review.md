# input_part000.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part000.txt`
- Coverage:
  - Batch 1: 2021-04-02 23:23:16 through 2021-04-03 01:46:36 (lines 1-320)
  - Batch 2: 2021-04-03 01:46:51 through 2021-05-18 17:49:41 (lines 321-2400)
  - Batch 3: 2021-05-18 17:50:23 through 2021-05-28 19:56:29 (lines 2401-3600)
- Next starting point: line 3601 (2021-05-28T19:56:29 and later)

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

## Open Questions / Follow-ups
- Validate whether the 20% Flipsky code can be shared or must be redeemed by the original account holder.【F:data/vesc_help_group/text_slices/input_part000.txt†L147-L152】
- Document wiring steps to integrate the VESC sleep function with the scooter’s stock power button and headlights.【F:data/vesc_help_group/text_slices/input_part000.txt†L66-L109】【F:data/vesc_help_group/text_slices/input_part000.txt†L1113-L1151】
- Gather delta-winding reliability data on VESC hardware, especially regarding voltage spikes and firmware choices (Spintend vs. stock).【F:data/vesc_help_group/text_slices/input_part000.txt†L112-L197】
- Confirm whether the observed Flipsky 7550 cutouts stem from BMS limits or controller faults and capture the eventual fix for reference.【F:data/vesc_help_group/text_slices/input_part000.txt†L1640-L1686】
- Track Spintend’s scooter-focused display/throttle roadmap and any firmware updates that add CAN bus support for noise resilience.【F:data/vesc_help_group/text_slices/input_part000.txt†L1045-L1049】【F:data/vesc_help_group/text_slices/input_part000.txt†L2047-L2067】
- Record real-world fitment data for 16 S 5 P 21700 packs and corresponding deck modifications (spacer heights, enclosure reinforcements).【F:data/vesc_help_group/text_slices/input_part000.txt†L2015-L2085】
- Prototype and validate the recommended low-ESR capacitor add-on for long cable runs, documenting values, placement, and thermal impact.【F:data/vesc_help_group/text_slices/input_part000.txt†L3084-L3090】
- Explore how to replicate VSETT’s low-voltage power tapering inside VESC Tool so battery stress cues remain without smart BMS telemetry.【F:data/vesc_help_group/text_slices/input_part000.txt†L3326-L3334】
