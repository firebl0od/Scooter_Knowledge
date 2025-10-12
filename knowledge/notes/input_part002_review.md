# input_part002.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part002.txt`
- Coverage: 2022-04-14 04:47 through 2022-08-16 13:19 (lines 1-27621)
- Latest detailed pass: 2022-05-26 01:34 through 2022-08-16 13:19 (lines 12501-27621, logged 2025-10-24)
- Next starting point: Awaiting the next export after line 27621

## Key Findings

### Controller Supply Crunch & Wishlist Features
- Riders are still waiting on replacement controllers from retailers such as Fastride and considering PayPal disputes after weeks without updates, underscoring how backorders remain a bottleneck.【F:data/vesc_help_group/text_slices/input_part002.txt†L5-L18】
- High-power VESC demand centres on 100 V-capable hardware that can deliver 80–100 A battery and 250 A phase per channel; members see Paolo’s upcoming VESC as competition for the elusive Nucular 12F and criticize current options like the $1 300 BAC4000.【F:data/vesc_help_group/text_slices/input_part002.txt†L9-L35】

### Artem’s Bidirectional Throttle Project
- Artem’s latest throttle prototype integrates brake + throttle in one housing, uses an onboard MCU to manage a single sensor for either unidirectional or bidirectional control, and can output either 5 V or 3.3 V so it works with stock controllers and VESCs without an external ADC adapter.【F:data/vesc_help_group/text_slices/input_part002.txt†L66-L95】
- He is targeting a $45–$55 price point with high-quality plastic, 0.2 mm enclosure tolerances, conformal-coated PCBs, and side mounting that shields the locking screw from weather.【F:data/vesc_help_group/text_slices/input_part002.txt†L96-L129】

### Spintend Adapter V2 Capabilities & Limits
- The Adapter V2 adds a throttle-scaling “power limit” mode toggled by holding the left brake and throttle during power-on, includes audible feedback for restricted/unrestricted states, and supports combining hall and switch brake sensors for proportional lighting control, though riders doubt it can enforce a true 25 km/h cap in real riding.【F:data/vesc_help_group/text_slices/input_part002.txt†L149-L170】
- Ubox firmware is adding extras like stop-light outputs and an iOS app, but some members still call the 100 V hardware a “failure,” keeping pressure on Spintend to iterate.【F:data/vesc_help_group/text_slices/input_part002.txt†L171-L175】
- First-time uBox users remind each other that the adapter will not register throttle movement until VESC Tool’s input mode is set to ADC, even if a multimeter shows the voltage changing, so setup checks should come before rewiring the harness.【F:data/vesc_help_group/text_slices/input_part002.txt†L5005-L5024】

### Magura Fluid & Brake Hardware Lessons
- Riders confirmed that DOT 5/5.1 attacks the silicone seals inside Magura and Shimano systems, pushing the group back to mineral oil and spotlighting Trickstuff Bionol’s 300–420 °C boiling range as a downhill-friendly alternative for scooters that routinely cook stock fluids.【F:data/vesc_help_group/text_slices/input_part002.txt†L23240-L23321】
- Jagwire Pro and other aftermarket hoses are preferred over stock Magura lines, but extending short bicycle levers still demands the correct olives and barbs at each end to avoid leaks once the line is re-terminated.【F:data/vesc_help_group/text_slices/input_part002.txt†L23337-L23385】
- Builders are adding hall sensors or reed switches to any hydraulic lever for proportional regen or kill-switch duty, freeing them from the handful of OEM sensored brake options on the market.【F:data/vesc_help_group/text_slices/input_part002.txt†L23385-L23394】

### Brake Cleaning & Storage Recovery
- After flood-soaked brakes seized, the crew advised stripping pads and attacking rust with dedicated brake cleaner instead of WD-40 or silicone sprays, which can swell seals and still leave corrosion behind; PTFE lubes are reserved for finishing touches once the hardware is dry.【F:data/vesc_help_group/text_slices/input_part002.txt†L23832-L23857】

### VESC Firmware & Voltage Calibration Updates
- Izuna packaged a full 75/100 V firmware toolkit—bootloader flash, custom .bin, and basic setup steps—so Flipsky owners can update via USB without ST-Link while keeping Xiaomi BLE dashboards working through the documented UART wiring and Lisp script.【F:data/vesc_help_group/text_slices/input_part002.txt†L23525-L23542】
- Flipsky 75100 V2 boards still read pack voltage roughly 2 V high until calibrated, prompting riders to cross-check with a multimeter after flashing Izuna’s builds.【F:data/vesc_help_group/text_slices/input_part002.txt†L23465-L23472】
- Spintend’s Bluetooth module plugs straight into Flipsky controllers, giving builders another telemetry option when the stock BLE dongle is missing or unreliable.【F:data/vesc_help_group/text_slices/input_part002.txt†L23614-L23616】

### VESC Tool Access & Remote Detection Hiccups
- Mirono urged riders to switch to sensorless detection when hall tests fail, while ToBeAsIAm traced repeated spin-direction issues to software quirks and the extra resistance of a temporary 5 m battery lead during setup.【F:data/vesc_help_group/text_slices/input_part002.txt†L27501-L27511】
- Paying €2 for the Android VESC Tool still grates on some members, though others note the fee simply covers Google Play distribution.【F:data/vesc_help_group/text_slices/input_part002.txt†L27505-L27512】
- Implementing an ignition switch on the VESC harness was reported as a worthwhile quality-of-life upgrade for repeated bench sessions.【F:data/vesc_help_group/text_slices/input_part002.txt†L27518-L27518】

### Spintend Hardware Support Updates
- Spintend’s uBox relies on JST pigtails across the harness, confirming connector families for riders stockpiling spares.【F:data/vesc_help_group/text_slices/input_part002.txt†L27513-L27516】
- A failed MCU showed just 0.6 V on the SWD VCC pin instead of 3.3 V, and Spintend support requested an RMA—highlighting that sub-1 V readings at the header are a strong indicator of a dead controller that needs factory service.【F:data/vesc_help_group/text_slices/input_part002.txt†L27519-L27520】

### Hub Cooling Fluid Experiments
- Riders floated filling stators with automatic transmission fluid (ATF) to soak the coils, but veterans warned the cable gland and bearings would leak, whereas ferrofluid remains the most controllable option for transferring heat across the rotor air gap.【F:data/vesc_help_group/text_slices/input_part002.txt†L27520-L27533】
- Some are considering a hybrid fill—ferrofluid near the magnet track plus a light ATF layer—yet the group is holding out for real-world temperature data before endorsing the practice.【F:data/vesc_help_group/text_slices/input_part002.txt†L27530-L27533】

### VESC Traction Control Feedback
- Traction control must be enabled on both controllers over CAN with a minimum ERPM delta, and veterans credit it with longer front-tyre life by suppressing spin on launch.【F:data/vesc_help_group/text_slices/input_part002.txt†L27535-L27541】
- Jan reported that the current algorithm doubled controller temperatures and cut peak power from ~18 kW to ~13 kW, sparking debate over whether proportional torque trimming needs refinement for heavy scooters.【F:data/vesc_help_group/text_slices/input_part002.txt†L27542-L27557】

### Controller Cooling Strategies & Limits
- Upsizing VESC heat spreaders remains the go-to, with builders comparing compact 100 V boards to older Yuanking 72 V 80 A bricks and planning sabvoton-style casings or external heatsinks instead of chasing water loops.【F:data/vesc_help_group/text_slices/input_part002.txt†L27545-L27560】【F:data/vesc_help_group/text_slices/input_part002.txt†L27561-L27565】
- A billet-aluminium cradle dropped case temps from 80 °C to 45 °C on the bench, yet skeptics noted it mainly adds thermal mass unless airflow or finning is added to reject the stored heat.【F:data/vesc_help_group/text_slices/input_part002.txt†L27566-L27585】

### Emerging DIY Electronics Projects
- Asyan4ik swapped a dead OEM controller for a VESC capped at 150–160 A phase and 80 A battery while iterating on antispark layouts, offering a real-world ceiling for enclosed builds.【F:data/vesc_help_group/text_slices/input_part002.txt†L27586-L27591】
- Ofek’s first custom PCB is only suited for low-power accessories until he adds more MOSFETs for sustained 90 A use, underscoring the challenge of scaling DIY power stages safely.【F:data/vesc_help_group/text_slices/input_part002.txt†L27594-L27603】
- Konstantin is pairing an aluminium-backed motor controller with a VESC 75200 and second prop motor for a future flying-scooter mashup, hinting at crossover demand for high-current hardware beyond ground builds.【F:data/vesc_help_group/text_slices/input_part002.txt†L27604-L27610】
- Francois teased a revised lighting board with four MOSFET channels, giving scooter builders headroom for higher-draw LED strips and brake lights.【F:data/vesc_help_group/text_slices/input_part002.txt†L27534-L27534】

### Detection Troubleshooting Reminders
- When FOC detection results conflict with initial parameters and trigger ABS overcurrent faults, the group recommends re-running the automatic detection routine (FOC → Measure R L λ) before assuming hardware issues.【F:data/vesc_help_group/text_slices/input_part002.txt†L27619-L27621】

### Battery Limits & Phase/Battery Amp Math
- Vsett 10+ owners reiterated that the stock 25.6 Ah LG MH1/MJ1 pack is happiest near 60 A; pushing 70–80 A in sport mode delivers big sag, sub-20-mile range, and frequent BMS cut-outs despite brief success at 78 A logs.【F:data/vesc_help_group/text_slices/input_part002.txt†L23640-L23666】
- The group now frames motor power as battery volts × amps, reminding riders that phase current merely shapes the launch curve and will be throttled once phase watts exceed available battery watts.【F:data/vesc_help_group/text_slices/input_part002.txt†L23668-L23729】
- Field weakening still trades efficiency for speed—expect roughly 25 % higher losses and large current spikes once it kicks in, which explains sudden heat rises during high-speed pulls.【F:data/vesc_help_group/text_slices/input_part002.txt†L23727-L23742】

### PWM Frequency Experiments & Cooling Warnings
- Rosheee’s push to drop the zero-vector frequency to 16–20 kHz for extra punch sparked debate: some see cooler motors and stronger launch, while others report hotter FETs and prefer the 16–18 kHz compromise for long commutes.【F:data/vesc_help_group/text_slices/input_part002.txt†L23884-L23905】
- High-Kv hubs chasing 20 kHz PWM are now adding small copper heatsinks to the DRV chip and checking motor R/L time constants, acknowledging that beyond ~15 kHz actual PWM the windings cannot respond any faster.【F:data/vesc_help_group/text_slices/input_part002.txt†L23947-L23952】

### Firmware & QC Cautions
- Ubox firmware 5.3 draws noticeably more battery current than 5.2, so riders raising rear limits are also bumping front-motor amps or reverting firmware to stop surprise BMS shutdowns.【F:data/vesc_help_group/text_slices/input_part002.txt†L24157-L24169】
- Early adopters eyeing VESC 6.0 on uBox hardware plan to keep SWD programmers handy; Spintend has not endorsed the jump, and beta users are warned to expect manual recovery if the flash bricks the controller.【F:data/vesc_help_group/text_slices/input_part002.txt†L24213-L24243】
- Fresh batches show fewer solder balls, yet Artem still inspects every side of a uBox before installation because stray splashes remain the most common cause of mysterious shorts.【F:data/vesc_help_group/text_slices/input_part002.txt†L24192-L24197】

### Vendor Delays & Repair Attempts
- Fastride’s months-long silence on €800 Kelly controller orders has riders threatening chargebacks, visiting the Paris storefront in person, and warning others to leave public reviews before wiring funds.【F:data/vesc_help_group/text_slices/input_part002.txt†L24128-L24436】
- Artem’s attempt to raise a stock Vsett controller to 60 V now focuses on the current-sense network and primary buck converter, illustrating which components fail first when over-volted.【F:data/vesc_help_group/text_slices/input_part002.txt†L24388-L24406】
- Rosheee’s latest Rion controller repair—new MOSFETs followed by an immediate “motor wizard” boom—shows that latent shorts can survive component swaps and that full diagnostics are needed before reapplying pack power.【F:data/vesc_help_group/text_slices/input_part002.txt†L24459-L24499】

### Lighting Experiments & Validation Requests
- Night riders are testing dual-color “owl” auxiliary lights (≈25 W per lamp), with Artem urging amperage checks via multimeter to verify whether the claimed 25 W/channel is real and noting a new 12–85 V variant that may suit direct-pack wiring.【F:data/vesc_help_group/text_slices/input_part002.txt†L320-L343】
- Users compare beam patterns, advocate higher mounting angles to reduce pavement shadows, and consider mixing existing low-beam lamps with the new spots for staggered coverage.【F:data/vesc_help_group/text_slices/input_part002.txt†L344-L385】
- Follow-up bench tests show each “owl” lamp actually draws ~19.5 W at 11.8 V (1.65 A per emitter), though wiring both the white and yellow LEDs together can spike toward 40 W—more than some 12 V rails can supply—prompting requests for night riding footage before declaring success.【F:data/vesc_help_group/text_slices/input_part002.txt†L1855-L1899】

### Battery Abuse, Thermal Risks & Voltage Strategy
- Rosheee’s 16S5P Samsung 50G pack is being pushed to 120 A+ combined battery current (≈24 A per cell), causing 70 °C controller readings, melted heat-shrink, and BMS shutdowns; switching to a 17S6P 40T pack delivered more range and lower sag but still peaks near 190 A.【F:data/vesc_help_group/text_slices/input_part002.txt†L409-L512】
- Artem warns that repeatedly exceeding the 50G’s 15 A rating accelerates IR growth and heat, recommends monitoring both cables and cell cores, and reminds builders that the VESC “battery current” limit effectively caps watts (voltage × amps), so higher series counts can hit the same power with less current stress.【F:data/vesc_help_group/text_slices/input_part002.txt†L567-L636】
- Members suggest pivoting to Molicel P42A/P45B-class cells, targeting ≤60 °C pack temps, and respecting 1 C charge rates even for Samsung 21700s to preserve longevity.【F:data/vesc_help_group/text_slices/input_part002.txt†L603-L633】【F:data/vesc_help_group/text_slices/input_part002.txt†L1587-L1594】

### Performance Logging & Vsett Motor Data
- A dual-Nucular Vsett 10+ logged 0–60 km/h in 4.75 s and 0–80 km/h in 7.5 s while drawing ~10.7 kW (78 A rear/70 A front battery, 200 A/130 A phase), with repeat 4.85 s pulls confirming consistency.【F:data/vesc_help_group/text_slices/input_part002.txt†L800-L839】
- Artem catalogued stock Vsett 10+ motor specs (105 mm × 51.4 mm stator, 30 magnets, 0.3 mm airgap) and cautioned that factory phase wires (~4 mm²) are undersized for repeated 200 A bursts despite built-in thermistors.【F:data/vesc_help_group/text_slices/input_part002.txt†L840-L865】

### Controller Comparisons & Availability Updates
- Riders praise dual Nucular 12Fs for staying ~5 °C above ambient even under heavy load and lament renewed shortages driven by supply chain and geopolitical issues, reinforcing why many are experimenting with Spintend and Paolo’s hardware instead.【F:data/vesc_help_group/text_slices/input_part002.txt†L1200-L1242】
- Artem reiterates that pack wattage, not just current, explains why a 17 S setup at 180 A battery limit can out-power a 20 S build set to 135 A, highlighting the need to review total battery limits when comparing logs.【F:data/vesc_help_group/text_slices/input_part002.txt†L1253-L1257】

### Firmware Settings & MTPA Caution for Hub Motors
- After a Spintend tune-up triggered a failure while experimenting with observer offsets, the group revisited Maximum Torque per Ampere (MTPA): several riders stress that both VESC and Nucular documentation restrict MTPA to interior permanent-magnet motors, as hub motors may lose low-end punch or overheat if negative Id current is injected.【F:data/vesc_help_group/text_slices/input_part002.txt†L1440-L1527】

### Accessory Integration & Manufacturing Constraints
- Artem is scoping a modular throttle mount with integrated buttons (e.g., 3-position switch plus momentary control) to consolidate mode, lighting, and indicator inputs, but ergonomics, accidental presses, and quick-release requirements drive ongoing iteration.【F:data/vesc_help_group/text_slices/input_part002.txt†L1646-L1689】
- Parallel chats on enclosure production show 3D-printed SLS quotes of $1 900 for 20 display shells—far more than CNC aluminium—prompting the team to seek alternative suppliers and potentially redesign housings for manufacturability.【F:data/vesc_help_group/text_slices/input_part002.txt†L1562-L1579】
- Continued prototyping emphasizes index-finger reach limits: Artem plans to 3D-print samples before committing to multi-button rear layouts and is aiming to place horn and cruise toggles behind the throttle where they remain accessible without breaking grip.【F:data/vesc_help_group/text_slices/input_part002.txt†L1700-L1776】
- Community builders such as Foujiwara showcase alternative integrated throttles/displays managed over VESC CAN, spurring interest in availability, ADC usage, and pricing compared to Artem’s pipeline.【F:data/vesc_help_group/text_slices/input_part002.txt†L2358-L2389】
- Later discussions weigh whether Xiaomi-style thumb throttles truly require Spintend’s ADC adapter or just a pull-down resistor, with veterans recommending simple solder-in fixes unless leveraging smart display integrations.【F:data/vesc_help_group/text_slices/input_part002.txt†L3100-L3119】

### Kaabo Hub Lighting Harness & Switch Powering
- Kaabo’s hub junction box expects pack voltage on the orange feed and returns 12 V for blinkers, so riders tapping the board without the stock display must jumper battery positive into the hub PCB and reuse the handlebar switch harness rather than relying on the controller jumper alone.【F:data/vesc_help_group/text_slices/input_part002.txt†L8001-L8088】
- Luis and Rosheee confirm the board’s internal DC-DC handles the 12 V lighting rails; builders without a multimeter should add one before rewiring to avoid misidentifying the orange/brown pair.【F:data/vesc_help_group/text_slices/input_part002.txt†L8031-L8074】

### Enforcement & Legal-Mode Tactics
- Belgian riders report scooters confiscated and cases escalated to lawyers when caught around 50 km/h; the pragmatic mitigation is to pre-configure a 25–30 km/h profile in VESC Tool so roadside checks show a compliant mode even if a high-speed profile exists for private use.【F:data/vesc_help_group/text_slices/input_part002.txt†L9502-L9552】
- Local enforcement looks harder on reckless behavior than outright speed—maintaining lane discipline, yielding properly, and avoiding pavements helps riders avoid stops while regulations continue to evolve.【F:data/vesc_help_group/text_slices/input_part002.txt†L9519-L9536】

### Red USB-C Ubox Voltage Fix & Support Workflow
- Spintend confirmed a firmware regression in FW 5.3 that misreads voltage on red USB-C Uboxes; Artem shared the corrected BIN (`VESC_UBOX_75_100_TYPEC_R2_3.3V_100A_FW5.3.bin`) and recommends flashing it immediately to restore accurate telemetry before chasing hardware faults.【F:data/vesc_help_group/text_slices/input_part002.txt†L9594-L9599】
- Dual-Ubox owners still seeing disconnects are told to wait 5–8 s after boot before connecting and to try the alternate USB-C port; if VESC Tool continues to fail, power-cycling and reflashing both firmware and bootloader through USB resolves most cases.【F:data/vesc_help_group/text_slices/input_part002.txt†L10006-L10030】

### Raphaël’s Dual-VESC Prototype Requirements
- Raphaël’s first dual-VESC board uses 12 TO-247 MOSFETs per motor (24 total) in a 110 × 110 mm footprint, targets 100 V operation, and aims for ~400 A phase / 300 A battery per channel at 60 % duty provided the copper busbars and 6 oz-class PCB can shed the heat.【F:data/vesc_help_group/text_slices/input_part002.txt†L9616-L9649】
- Component scarcity dominates pricing: just the MOSFET set costs ≈€200 and dual STM32 MCUs run €60, pushing the projected sale price well above €1 000 unless production is heavily automated.【F:data/vesc_help_group/text_slices/input_part002.txt†L9650-L9669】
- The team refuses to cheap out on gate drivers or amplifiers despite supply pressure, contrasting their spec with Spintend’s silent downgrade from 4 A Infineon drivers to 1.5 A generics in the cost-reduced V2 hardware.【F:data/vesc_help_group/text_slices/input_part002.txt†L9674-L9684】

### Spintend Hardware Changes & Single-Ubox Cooling Limits
- Spintend’s V2 dual controller removed the BLE daughterboard and now relies on weaker 1.5 A gate drivers, reinforcing why riders should temper expectations for sustained high duty cycles compared with the original BOM.【F:data/vesc_help_group/text_slices/input_part002.txt†L9677-L9684】
- The single Ubox enclosure still mounts MOSFETs on the lid, halving thermal mass when bolted to frames; even fans concede it was designed for one-wheel applications around 30 A continuous, not for dual-motor scooters chasing 100 A peaks.【F:data/vesc_help_group/text_slices/input_part002.txt†L9685-L9697】

### Repair Notes: Sabvoton Failures vs. MakerX Build Quality
- Fresh Sabvoton 72150s continue arriving DOA—throttle loops, sloppy Kapton layering, and poor hall detection sent one buyer back to VESC after Falconpev refused support following a disputed motor shipment.【F:data/vesc_help_group/text_slices/input_part002.txt†L9713-L9726】【F:data/vesc_help_group/text_slices/input_part002.txt†L10259-L10276】
- MakerX’s Mini FOC teardown shows three copper shunts per phase, silicone pads with full FET contact, and isolated analog grounds for the logic rail; even sensorless starts run quietly while awaiting the hall harness, making it an appealing Kelly alternative when paired with proper torque arms.【F:data/vesc_help_group/text_slices/input_part002.txt†L9747-L9852】【F:data/vesc_help_group/text_slices/input_part002.txt†L9800-L9850】
- Flux should not be scorched off joints—the crew reminds builders it guards against oxide formation during soldering, so reflow repairs on controllers should reapply flux instead of baking boards bare.【F:data/vesc_help_group/text_slices/input_part002.txt†L9701-L9706】

### Torque Arms, Rotor Clearance & Brake Fitment
- Ebike conversions powered by VESCs demand quality rear torque arms before road testing; improvised washers can lever the axle out within meters, so riders now postpone shakedowns until machined clamps arrive.【F:data/vesc_help_group/text_slices/input_part002.txt†L9835-L9859】【F:data/vesc_help_group/text_slices/input_part002.txt†L10335-L10342】
- Magura MT7/MT5 calipers barely clear 2.9 mm Kaabo rotors—new pads and thicker 3 mm discs overwhelm the pocket, explaining why many stick with stock Zoom calipers or 2.0 mm rotors unless custom spacers are machined.【F:data/vesc_help_group/text_slices/input_part002.txt†L10049-L10090】
- Riders exploring tubeless slicks note that traditional split-rim tyre swaps remain faster in the field; tubeless plugs seal but roadside repairs demand more time and tools than standard tubes.【F:data/vesc_help_group/text_slices/input_part002.txt†L10182-L10197】

### Cell Selection, Pack Layout & BMS Debates
- NKON shoppers weighing 100 A peaks lean toward Molicel 40T despite price, treating LG M50LT as a budget backup until high-current tests confirm it avoids 15 V sag seen on older 50G builds.【F:data/vesc_help_group/text_slices/input_part002.txt†L9879-L9900】
- Budget ebike packs still rely on LG MH1 at €1.70 per cell, but riders accept the limited current for lightweight builds and plan to upgrade to 21700 formats once wallets recover.【F:data/vesc_help_group/text_slices/input_part002.txt†L10368-L10387】
- Kaabo Wolf owners sketch 20S7P decks at 160 × 470 × 75 mm and debate running charge-only BMS wiring with external JK active balancers versus installing a flat ANT or JK unit capable of 150 A continuous balancing current.【F:data/vesc_help_group/text_slices/input_part002.txt†L10550-L10613】

### Spintend Flashing & Recovery Workflow
- Persistent “cannot read VESC firmware” faults on Spintend singles often trace to corrupted firmware; the recommended fix is a clean USB flash with only power, button, and USB connected, followed by a bootloader reinstall if detection still fails.【F:data/vesc_help_group/text_slices/input_part002.txt†L10027-L10321】
- When USB enumeration dies entirely, riders pop the lid to access the SWD header, use the published “How to flash firmware through SWD interface” PDF, and verify the two top LEDs (N1/N2) remain lit—if they’re dark, the STM32 is likely toast and needs replacement.【F:data/vesc_help_group/text_slices/input_part002.txt†L10203-L10344】

### Controller Support & Reliability Reports
- Sabvoton buyers recount spending two days with no manuals or throttle response, concluding the €300 controller is junk compared with a VESC that spun the motor in 15 minutes.【F:data/vesc_help_group/text_slices/input_part002.txt†L10259-L10268】
- Kelly KLS7230 firmware mismatches manifest as 380 A phase limits on some units while others cap at 320 A; support only engages when customers escalate publicly, so builders swap controllers between motors to isolate hardware before filing tickets.【F:data/vesc_help_group/text_slices/input_part002.txt†L10500-L10534】
- Retailers like Fastride rarely respond to remote buyers, making local pickup or DIY repairs the safer path for warranty-sensitive builds.【F:data/vesc_help_group/text_slices/input_part002.txt†L10503-L10509】

### Kaabo Wolf Waterproofing Lessons
- A Wolf deck inspection showed water pooled under a 20S pack, soaking Tudor’s LG M50LT 35S module despite shrink wrap and reminding riders that Minimotors’ sealing is minimal—multiple silicone layers and Kapton wraps are needed around series bridges and BMS leads.【F:data/vesc_help_group/text_slices/input_part002.txt†L10549-L10572】
- Builders now pre-emptively add drain checks and dielectric grease before chasing 20S8P upgrades so future floods cannot wick into cell groups.【F:data/vesc_help_group/text_slices/input_part002.txt†L10550-L10579】

### Little FOCer V3.1 Arrivals & Rion Builds
- Rosheee secured Little FOCer V3.1 boards rated for dual 290 A phase (320 A absolute) with 190 A battery limits, planning to drop them into his Ninebot G30/Rion hybrid while waiting on a 450 A Rion controller shipment—evidence boutique 100 V hardware is finally shipping again.【F:data/vesc_help_group/text_slices/input_part002.txt†L10655-L10680】

### ANT Displays & MakerX MOSFET Limits
- With few dedicated VESC displays available, riders are mounting ANT BMS panels as secondary dashboards to surface pack telemetry alongside MakerX-based builds.【F:data/vesc_help_group/text_slices/input_part002.txt†L10912-L10926】
- MakerX’s NECP045N85GU MOSFETs measure ~1.8 mΩ, suitable for high-power bursts but not sustained scooter loads; Paolo warns they’re the same parts Flipsky used in failure-prone runs, so continuous current should stay conservative unless additional cooling is added.【F:data/vesc_help_group/text_slices/input_part002.txt†L10917-L10924】

### High-Discharge Cell Outlook (P45B vs. 50S & 48X)
- Mooch’s P45B test results excite builders: 4 P groups could support 150–200 A battery currents with manageable 80 °C peaks, offering a higher-capacity alternative to Samsung 50S once pricing drops below the projected $8 per cell.【F:data/vesc_help_group/text_slices/input_part002.txt†L10930-L10945】
- Veterans still rate Samsung 48X for moderate 12 A-per-cell builds, citing months of riding with ≤30 °C pack temps and near-perfect balancing when paired with active balancers.【F:data/vesc_help_group/text_slices/input_part002.txt†L10950-L10956】

### Sensorless Firmware & Brake Sensor Wiring Questions
- Upcoming VESC firmware promises better HFI starts so scooters can launch sensorless with only a gentle push, yet Paolo cautions halls remain essential for preventing saturation in high-torque FOC tunes.【F:data/vesc_help_group/text_slices/input_part002.txt†L10970-L10978】
- Builders wiring dual brake throttles ask for resistor values on Zoom/Nut switches; Paolo’s guidance is to match the expected output voltage for the controller input, highlighting the need for a reference chart in the documentation set.【F:data/vesc_help_group/text_slices/input_part002.txt†L10979-L10982】

### Ubox High-Speed Cutouts & Cooling Reality Checks
- Rosheee’s 16S5P G30 build touches 115 km/h but triggers ABS overcurrent limits on 100 V firmware, reinforcing that the 140 A absolute ceiling and firmware behavior—not the BMS—cause power cuts at high ERPMs.【F:data/vesc_help_group/text_slices/input_part002.txt†L8355-L8380】【F:data/vesc_help_group/text_slices/input_part002.txt†L8401-L8405】
- Subsequent battery logs show Kaabo’s pack drooping 15 V when twin Uboxes spike to 150 A despite a 120 A limit, motivating connector and cell upgrades for sustained output.【F:data/vesc_help_group/text_slices/input_part002.txt†L8972-L8985】
- Paolo reminds the group that laser thermometers aimed at heatsinks under-read MOSFET junction temps; accurate checks require bare-die access or pro-grade IR cameras, explaining why better heat transfer needs controller designs with direct FET-to-baseplate contact (e.g., Little FOCer, Tronic).【F:data/vesc_help_group/text_slices/input_part002.txt†L9409-L9448】

### DIY Hub Cooling With Wired PC Heatsinks
- Mirono wrapped low-cost PC heatsinks around his hub using thermal tape and four stainless-wire loops tightened 90° apart so each bank stayed clamped; a 30 € investment delivered noticeably cooler side covers after a 15‑minute pull (~80 °C controller) without vibration issues, and he plans thermal-camera validation before refining orientation.【F:data/vesc_help_group/text_slices/input_part002.txt†L21513-L21586】
- Riders compared the DIY approach to commercial Turbinator kits that run €135–€200 shipped to the EU, concluding the homebrew path is far cheaper while everyone waits for restocks.【F:data/vesc_help_group/text_slices/input_part002.txt†L21795-L21813】

### Segway GT2 Ride Feedback & Fitment Options
- Kirill’s demo run on Segway’s GT2 highlights a factory 14S pack feeding dual 1 400 W motors that hold 70 km/h down to ~10 % SOC, a 1.5 m wheelbase that stays stable one-handed, and enough clearance to accept 180 mm rotors with Magura calipers—while staying street-legal in Switzerland at about €4 000.【F:data/vesc_help_group/text_slices/input_part002.txt†L21875-L21908】

### Kaabo & Vsett Hardware Service Lessons
- Luis confirmed Kaabo hubs ship with dual 6003 bearings while Rosheee measured stock phase leads around 5 mm² (≈10 AWG) and proved that 3×6 mm² conductors plus halls will squeeze through the axle on 2 000 W-class stators, especially with 110/55‑6.5 tyres creating extra caliper space.【F:data/vesc_help_group/text_slices/input_part002.txt†L21909-L21918】【F:data/vesc_help_group/text_slices/input_part002.txt†L22074-L22079】
- Flipping the Wolf’s fork legs left/right opens enough room to mount 180 mm rotors with Maguras up front, but the rear still lacks caliper bosses so owners expect fabrication work.【F:data/vesc_help_group/text_slices/input_part002.txt†L22142-L22158】
- Kaabo’s motor terminations appear spot-welded “Kryptonian” solder blobs several centimetres long, forcing builders to snip and splice instead of desoldering; Vsett and Ninebot G30 stators are far easier to rewire for 6 mm² upgrades.【F:data/vesc_help_group/text_slices/input_part002.txt†L22353-L22390】
- Paolo flagged 65 mm‑wide 10‑inch motors with 10 mm² phase leads and 155 mm dropouts as a potential upgrade path over stock Vsett hubs, though he questions whether the price premium beats jumping to 11‑inch platforms for stability gains.【F:data/vesc_help_group/text_slices/input_part002.txt†L22304-L22337】

### Spintend CNC Throttle Launch Updates
- Artem confirmed the full-CNC throttle will list at $59 (presale) with an optional $17 top-button module, housing an onboard MCU that handles 3.3 V bidirectional output, a 5 V-scaled mode for legacy controllers, a discrete e-brake trigger above 20 % back-travel, and a dedicated cruise-toggle input; add-on modules remain removable for riders who only want the lever.【F:data/vesc_help_group/text_slices/input_part002.txt†L21818-L21847】【F:data/vesc_help_group/text_slices/input_part002.txt†L21931-L21938】【F:data/vesc_help_group/text_slices/input_part002.txt†L22353-L22355】
- Early adopters already placed 360 of the 1 000 pre-order units in production, with Spintend offering 4PX (DPD/DHL) logistics and pledging to retrofit button choices post-purchase if needed.【F:data/vesc_help_group/text_slices/input_part002.txt†L22230-L22278】【F:data/vesc_help_group/text_slices/input_part002.txt†L22286-L22291】
- Beta testers praise thumb-actuated regen for slashing mechanical pad wear, yet koxx warns that shielded cabling may be mandatory to keep 3.3 V ADC lines quiet above ~100 A phase, citing past noise-induced throttle glitches on powerful VESC builds.【F:data/vesc_help_group/text_slices/input_part002.txt†L21937-L21957】
- The group contrasted the project with Rion’s $200 thumb wheel, which reportedly ships late, binds instead of returning to neutral, and sits awkwardly low on the bar, reinforcing demand for an ergonomic alternative.【F:data/vesc_help_group/text_slices/input_part002.txt†L21950-L21985】

### Controller Cooling, Mounting & Legacy Knowledge
- Konstantin shared photos of Flipsky’s 75100 revision using an aluminum-backed PCB, a new 4.5–100 V DC-DC module, and GH1.25 harnessing, prompting Paolo and Artem to debate whether board-level heat spreading beats Spintend’s copper-top plate approach; Artem advised bolting the copper slab straight to a deck if you keep the cheaper single Ubox.【F:data/vesc_help_group/text_slices/input_part002.txt†L22585-L22603】【F:data/vesc_help_group/text_slices/input_part002.txt†L22662-L22669】
- A dual-controller build mounted hardware on plexiglass with thick thermal pads to absorb road vibration before it reaches the PCBs, a tactic others are considering for street scooters.【F:data/vesc_help_group/text_slices/input_part002.txt†L22532-L22537】
- Veterans reminded newcomers that Adaptto controllers ended production years ago; modern Nuculars have superseded them with encoder support, higher power density, and independent logging per controller, so dual setups still require two files when analyzing temps.【F:data/vesc_help_group/text_slices/input_part002.txt†L22460-L22473】【F:data/vesc_help_group/text_slices/input_part002.txt†L22538-L22555】

### Flipsky 75100 Failure Forensics & Thermal Mods
- Mirono and sombre_enfant concluded recent 75100 blow-ups stem from aggressive ABS max overcurrent thresholds (~190–450 A) and insufficient snubbing, urging extra capacitance and acknowledging that induced voltage spikes after BMS cut-outs can murder MOSFETs even without regen events.【F:data/vesc_help_group/text_slices/input_part002.txt†L26014-L26033】
- Artem’s testing of the aluminum-PCB 75100 shows it can hold 200 A phase / 100 A battery with a measured slow thermal rise, suggesting repacking it against the scooter deck with quality paste and active airflow can sustain ~180 A/70 A continuous once heat transfer paths are shortened.【F:data/vesc_help_group/text_slices/input_part002.txt†L26064-L26109】
- Ofek’s 75100 V2 still hits a 75 °C thermal cut at only 5.5 kW until MOSFET swaps, high-quality pads/paste, and better airflow are added, while Izuna advocates HUASHUO HSP0076A FET retrofits and copper-backed heatsinks to stop the die from spiking faster than the sink can wick heat away.【F:data/vesc_help_group/text_slices/input_part002.txt†L26618-L26696】
- Group consensus is to clamp MOSFETs directly to aluminum mass with the thinnest paste film possible, avoid stacked interfaces, and target larger surface area plus heat pipes when chasing 12–16 kW pulls that otherwise overwhelm 75100-class sinks.【F:data/vesc_help_group/text_slices/input_part002.txt†L26708-L26849】

### Thermal Interface Materials & Pad Selection Debates
- Riders compared high-end TIM options, noting Thermal Grizzly Hydronaut (≈14 W/m·K) and Alphacool/SARCON XR-m (17 W/m·K) pads perform measurably better than commodity silicone, while liquid-metal compounds are rejected for being electrically conductive and corrosive to aluminum heatsinks.【F:data/vesc_help_group/text_slices/input_part002.txt†L26851-L26938】
- Beryllium-oxide pastes offer extreme conductivity (~300 W/m·K) but are considered too toxic for scooter work, whereas graphene pads promise 62 W/m·K yet prove fragile and still risk shorting components.【F:data/vesc_help_group/text_slices/input_part002.txt†L26944-L27029】
- Spintend’s own thermal pads continue to outperform DIY swaps in the field, implying material choice and install technique matter as much as pad specs when taming dual-Ubox temperatures.【F:data/vesc_help_group/text_slices/input_part002.txt†L27038-L27066】

### Makerbase MKSESC & Low-Cost VESC Variants
- Makerbase’s MKSESC 75100 arrives without thermal paste and uses inexpensive shunt overlays plus Magnachip MDP10N027 MOSFETs, making immediate rework (TIM application, conformal inspection) a must before high-amp service.【F:data/vesc_help_group/text_slices/input_part002.txt†L27142-L27205】
- Owners confirm the board ships with EG3112 gate drivers and a budget buck converter, advising builders to secure datasheets, stock spare driver ICs/FETs, and plan for manual ignition or antispark solutions because the hardware lacks a low-current enable lead.【F:data/vesc_help_group/text_slices/input_part002.txt†L27174-L27268】

### VESC Setup Troubleshooting & Firmware Notes
- Swapping TX/RX leads or re-enabling Bluetooth comms through VESC Tool fixes the “missing module” error that hits Spintend UARTs after firmware updates, while ADC throttles may land on unexpected channels (VAL2) depending on vendor wiring.【F:data/vesc_help_group/text_slices/input_part002.txt†L26222-L26279】【F:data/vesc_help_group/text_slices/input_part002.txt†L27334-L27368】
- Makerbase app users report the Android wizard is too opaque for throttle/brake assignment; the group recommends finishing configuration on a PC, saving via VESC Tool, and optionally flashing Izuna’s latest firmware for corrected 75100 voltage calibration once hardware ID mismatches (75_300_R2) are resolved.【F:data/vesc_help_group/text_slices/input_part002.txt†L27369-L27428】

### Spintend Single 100 V Roadmap & Quality Control
- Artem delayed the single-Ubox 100 V launch to swap a flawed brass heat spreader for copper and is now consulting on future “naked” aluminum casings plus improved thermal dynamics across Spintend’s lineup, signaling better out-of-box cooling but longer wait times.【F:data/vesc_help_group/text_slices/input_part002.txt†L26880-L26918】【F:data/vesc_help_group/text_slices/input_part002.txt†L26994-L27020】
- Early CNC throttle production units passed tolerance checks and are entering QC, with black/anodized variants shipping once the final countersunk hardware arrives.【F:data/vesc_help_group/text_slices/input_part002.txt†L27108-L27132】

### Hub Cooling Validation & Ferrofluid Choices
- Mirono’s DIY hub wrap—thermal-tape fins plus ferrofluid—kept a bag-mounted VESC case near ambient (≈42 °C heatsink in 34 °C weather) and proved the hub shell now matches coil temps, confirming heat is escaping the stator efficiently.【F:data/vesc_help_group/text_slices/input_part002.txt†L27288-L27324】【F:data/vesc_help_group/text_slices/input_part002.txt†L27471-L27523】
- Riders debate branded Statorade versus generic ferrofluids: premium mixes claim optimized viscosity, yet budget ferrofluid still yields major gains unless pushing “Rosheee-level” power, provided heatsinks create a solid path from stator to air.【F:data/vesc_help_group/text_slices/input_part002.txt†L27496-L27523】

### Dual-Ubox Fault Recovery & Service Logistics
- A rider lost ESCB on a dual Ubox after only 300 m; the team diagnosed a dead STM32 or corrupted flash, recommending CAN-bridged SWD reflashing per Spintend’s manual (RST line unused) and confirming 3.3 V throttle wiring was correct before escalation.【F:data/vesc_help_group/text_slices/input_part002.txt†L27404-L27465】
- Missing SWD harnesses can be substituted with the included four-pin CAN cable because the reset pin is unused, though Windows STM32 drivers may be required to complete the recovery in VESC Tool.【F:data/vesc_help_group/text_slices/input_part002.txt†L27466-L27508】

### High-Power Kelly Controller Transitions
- Rosheee is migrating Kaabo builds from dual Uboxes to Kelly KLS7230s, noting the need for 0 AWG QS10 connectors, dual-to-single phase splicing, and likely TIG-welded terminations to tame the twin leads each phase requires.【F:data/vesc_help_group/text_slices/input_part002.txt†L27399-L27403】【F:data/vesc_help_group/text_slices/input_part002.txt†L27429-L27488】

### Charging Gear, Consumables & Cooling Debates
- Mirono keeps gambling on budget 0–90 V/5 A AliExpress chargers (≈€76 shipped) but lines up disputes if delivery slips, while others argue the Grin Satiator is worth the premium to dodge repeated support battles.【F:data/vesc_help_group/text_slices/input_part002.txt†L22438-L22450】
- Rosheee priced genuine Statorade at roughly CHF 21 per 10 ml after import taxes and continues parceling 10 ml tubes to the group; Her0DasH couples ferrofluid fills with machined “windmill” fans and stripped paint to open cooling channels around the stator edges.【F:data/vesc_help_group/text_slices/input_part002.txt†L22679-L22735】
- Riders noted that paying a ~10 % premium for ferrofluid or hubsinks is justified when it yields 15–30 % more continuous performance, especially on €200 hubs.【F:data/vesc_help_group/text_slices/input_part002.txt†L22651-L22660】

### BMS & Wiring Troubleshooting Notes
- Francois’ attempt to parallel an additional R001 shunt into his BMS backfired, leaving a hot component that only cooled when the balance lead was removed, underscoring the risk of doubling current limits without re-engineering the sense circuit.【F:data/vesc_help_group/text_slices/input_part002.txt†L22681-L22685】
- Three-metre phase extensions on a Flipsky test rig violently flexed under load, a visceral reminder that long, poorly restrained leads will experience strong Lorentz forces once the controller starts pushing real amps.【F:data/vesc_help_group/text_slices/input_part002.txt†L22890-L22924】

### Ubox Firmware & Over-Voltage Checks
- Troubles on a single Ubox 75/100 surfaced after flashing the dual-controller firmware and leaving the absolute voltage limit at 72 V—once the team restored the correct single-unit firmware and raised the over-voltage trip closer to 85–90 V, the scooter stopped brown-out shutting after launches.【F:data/vesc_help_group/text_slices/input_part002.txt†L22955-L22999】

### Controller Options Beyond Spintend
- Members weigh Tronic/Little FOCer hardware against Spintend: Tronic claims 100 A battery/250 A phase at 21 S but costs ≈€400 per controller, needs DIY heatsinks, and shares a TO-247 FET stack with Little FOCer, while YYK square-wave units survive repeated shorts albeit without VESC configurability.【F:data/vesc_help_group/text_slices/input_part002.txt†L8204-L8271】【F:data/vesc_help_group/text_slices/input_part002.txt†L8620-L8690】
- Demand still outstrips supply—Little FOCer runs out of stock, Tronic requires long lead times, and riders debate sealing dual Little FOCers versus reordering Uboxes—highlighting the ongoing controller drought past the 8000-line mark.【F:data/vesc_help_group/text_slices/input_part002.txt†L8204-L8269】【F:data/vesc_help_group/text_slices/input_part002.txt†L8662-L8690】

### Track Builds & Rion Limitations
- Racers comparing Rion chassis with custom G30s point out brake fade, flexy frames, and tall centers of gravity that make Rions sketchy on tight circuits such as Angerville; suggested fixes include dual throttles, external controller mounts, and ferrifluid-cooled Vsett motors paired with strong Magura setups.【F:data/vesc_help_group/text_slices/input_part002.txt†L8720-L8783】
- Organisers share that French kart tracks host regular scooter days for €25–35, while Swiss riders are still negotiating local access—context for anyone planning test-and-tune trips.【F:data/vesc_help_group/text_slices/input_part002.txt†L9165-L9186】

### BMS Practices, Pack Handling & Connector Choices
- Daly-style BMS units routinely pass 180 A+ spikes without intervening, so several builders bypass discharge FETs entirely, lean on VESC voltage cutoffs, or switch to Bluetooth BMS boards strictly for charge control.【F:data/vesc_help_group/text_slices/input_part002.txt†L8785-L8810】
- Daly’s Bluetooth variant can toggle outputs in-app without sparks, giving antispark-free builds a safe way to de-energise the harness when parking.【F:data/vesc_help_group/text_slices/input_part002.txt†L9452-L9459】
- A mishandled Mirono pack shows that fish paper, Kapton, and shrink still need foam blocks or brackets—deck rails wore through multiple insulation layers once the owner slid the battery in loosely—underscoring the need for retention hardware and delivery photos.【F:data/vesc_help_group/text_slices/input_part002.txt†L9080-L9159】
- QS8 connectors deliver roughly 70 A continuous yet remain bulky and expensive; riders chasing compact battery bays often substitute 8 mm bullet plugs while keeping XT90S for lower-current projects because they plateau near 45 A continuous.【F:data/vesc_help_group/text_slices/input_part002.txt†L8930-L8947】
- Flipsky 75100 owners without antispark switches simply unplug XT90S leads between rides or accept the controller’s ≈5 mA standby draw, illustrating how low-idle current still matters when storing high-voltage scooters for weeks.【F:data/vesc_help_group/text_slices/input_part002.txt†L9327-L9334】

### Kaabo Pack Limits & Cell Debates
- Rosheee’s Kaabo pack still surges to 150–155 A even with battery limits set to 60 A per controller, dragging voltage by ~15 V and confirming the stock 16S5P LG M50T-class cells are undersized for dual-Ubox pulls.【F:data/vesc_help_group/text_slices/input_part002.txt†L8972-L8985】
- Builders weigh alternatives such as Molicel P42A/P45B or Samsung 50S, noting that 50S pricing is 2–3× higher while P-series cells stay cooler under 20–25 A loads—a reminder to budget for chemistry upgrades when targeting 120 A+ battery draw.【F:data/vesc_help_group/text_slices/input_part002.txt†L8992-L9016】【F:data/vesc_help_group/text_slices/input_part002.txt†L8830-L8854】

### Controller Thermal Lessons & Cooling Experiments
- Ubox V1 “def edition” hardware runs noticeably cooler than early V2 betas in the same scooter, yet Paolo cautions that resin-encapsulated MOSFETs still bottleneck heat transfer because only thin PCB copper contacts the case—unlike Little FOCer or Tronic designs that clamp directly to the FET tab.【F:data/vesc_help_group/text_slices/input_part002.txt†L9000-L9010】【F:data/vesc_help_group/text_slices/input_part002.txt†L9408-L9425】
- The crew warns that handheld IR thermometers aimed at heatsinks under-read junction temps; accurate checks require exposed FET surfaces or pro-grade thermal cameras, otherwise riders risk overestimating their cooling mods.【F:data/vesc_help_group/text_slices/input_part002.txt†L9434-L9446】

### Carbon & Additive Manufacturing Ideas
- Rosheee is collaborating with a Formula 1 composites engineer on carbon-fibre G30 fenders and aluminium heat-spreader spacers, but veterans flag carbon’s brittleness and the risk of wheel lock if a mudguard shatters under torsion.【F:data/vesc_help_group/text_slices/input_part002.txt†L9360-L9395】
- New STL/3MF files for ground-down G30 frames were released to the group, ensuring builders can print reinforcement pieces after heavy deck modifications.【F:data/vesc_help_group/text_slices/input_part002.txt†L9491-L9499】

### Enforcement & Public Perception
- Swiss media reported a 133 km/h Wolf Warrior seizure, prompting reminders that police can confiscate scooters outright and levy heavy fines—one more reason builders keep stealth commuter projects alongside race-only machines.【F:data/vesc_help_group/text_slices/input_part002.txt†L9471-L9489】
- Belgian riders described confiscations for 50 km/h use and noted that flipping between 30 km/h and “escape” profiles on VESC builds remains the only practical mitigation short of fully registering scooters as mopeds, underscoring the value of compliant mode presets.【F:data/vesc_help_group/text_slices/input_part002.txt†L9502-L9510】

### Firmware & Toolchain Updates
- Vedder’s VESC firmware 6.0 entered beta, with early adopters reporting noticeable changes versus 5.3 and encouraging others to review the public Git changelog before flashing.【F:data/vesc_help_group/text_slices/input_part002.txt†L1841-L1853】
- Builders compiling from source noted that fresh firmware binaries exceed Ubox single MCU flash limits unless paired with an updated VESC Tool build, prompting local toolchain rebuilds.【F:data/vesc_help_group/text_slices/input_part002.txt†L2125-L2127】

### Red Ubox USB-C Voltage Fix & Recovery Tools
- Spintend confirmed a firmware defect that mis-reported pack voltage on red USB-C Uboxes running FW 5.3; Artem shared an updated `.bin` and asked owners to flash over USB to restore accurate readings.【F:data/vesc_help_group/text_slices/input_part002.txt†L9594-L9599】
- Community support threads captured the follow-up workflow for purple Uboxes: keep 5.2 binaries on hand, reseat the USB-C lead, and wait several seconds before reconnect attempts, otherwise VESC Tool reports “could not read fw” until the controller completes boot.【F:data/vesc_help_group/text_slices/input_part002.txt†L9986-L10030】
- When USB reflashing fails, riders now reference Spintend’s SWD guide, check for the twin green “N1/N2” LEDs, and resort to ST-Link programming if the MCU stops enumerating—a step that effectively diagnoses dead STM32s on single Uboxes sold second-hand.【F:data/vesc_help_group/text_slices/input_part002.txt†L10119-L10149】【F:data/vesc_help_group/text_slices/input_part002.txt†L10305-L10343】

### Raphaël’s Dual-VESC Prototype & Component Economics
- Raphaël detailed his dual-channel design (12 × 300 A MOSFETs per motor, 100 V, 400 A phase / 300 A battery goals) in a 110 × 110 mm footprint, highlighting the need for thick copper busbars and high-end drivers to stay efficient at 60 % duty—putting the bill of materials well above €1 000 before labor.【F:data/vesc_help_group/text_slices/input_part002.txt†L9614-L9658】
- Supply-chain pressure remains intense: STM32 MCUs alone run ~€30 each and Infineon gate drivers have doubled since COVID, so Paolo’s lower-cost board still struggles to hit a €500 price target per channel without sacrificing quality components.【F:data/vesc_help_group/text_slices/input_part002.txt†L9661-L9676】

### Spintend V2 Downgrades & Single-Ubox Cooling Limits
- Raphaël confirmed that Ubox V2 units quietly swapped 4 A Infineon gate drivers for 1.5 A generics and dropped the BLE board to shave cost, aligning with rider complaints that the “economical” revision lags prior hardware under heavy load.【F:data/vesc_help_group/text_slices/input_part002.txt†L9677-L9688】
- Riders reiterated that the single Ubox’s case splits starve MOSFETs of thermal mass; the board is oriented for one-wheel duty where 100 A peak / 30 A continuous is considered acceptable, so scooter builders still bolt on auxiliary heatsinks or favor dual-channel alternatives.【F:data/vesc_help_group/text_slices/input_part002.txt†L9689-L9697】

### MakerX VESC Teardowns, Sabvoton Failures & Recovery Steps
- Mirono’s teardown of a MakerX dual controller showed tidy soldering, three copper shunts per phase, and thermal pads bonding FETs to the shell—contrasting a DOA Sabvoton whose Kapton-isolated MOSFETs and looped throttle wiring left him without vendor support or documentation.【F:data/vesc_help_group/text_slices/input_part002.txt†L9699-L9738】【F:data/vesc_help_group/text_slices/input_part002.txt†L9826-L9863】
- Riders now favor MakerX’s isolated low-voltage domains and improved CAN connectors after seeing the Sabvoton struggle to detect halls or respond to throttle until reflashed, with VESC Tool recovery taking minutes compared to days of unanswered support tickets.【F:data/vesc_help_group/text_slices/input_part002.txt†L9799-L9859】

### Ebike Mounting, Torque Arms & Brake Fitment
- Clamp-on and 3D-printed brackets let MakerX controllers sit under bicycle downtubes, but veterans warn to add tight-fitting torque arms before riding—thin dropouts or extra washers can let hub motors slip even at garden-speed test runs.【F:data/vesc_help_group/text_slices/input_part002.txt†L9821-L9859】【F:data/vesc_help_group/text_slices/input_part002.txt†L10729-L10757】
- Magura MT series calipers tolerate roughly 2 mm rotors; Kaabo’s 2.89 mm discs barely clear new pads, so riders keep spare Zoom calipers or dress rotors down when experimenting with 3 mm aftermarket options.【F:data/vesc_help_group/text_slices/input_part002.txt†L10045-L10117】

### Cell Selection, Pack Layouts & Balancing Strategies
- NKON shoppers weighing 16S5P ebike packs debated Samsung 40T vs. LG M50LT, ultimately planning to lab-test M50LT cells at 15 A before trusting them and keeping a high-power discharger handy for characterization.【F:data/vesc_help_group/text_slices/input_part002.txt†L9879-L9920】
- Kaabo Wolf GT owners discovered their stock 35S packs use LG M50LT cells that sag like Samsung 50G; ongoing waterproofing plans now add silicone seams and multiple wrap layers to stop puddle ingress.【F:data/vesc_help_group/text_slices/input_part002.txt†L10550-L10576】
- Builders targeting 20S7P footprints (160 × 470 × 75 mm) compared JK’s JK-B1A24S-15P active-balancing BMS against charge-only rigs with detachable JK balancers, concluding that a main-line fuse plus VESC undervoltage cutoffs can substitute for discharge FETs when space is scarce.【F:data/vesc_help_group/text_slices/input_part002.txt†L10603-L10654】【F:data/vesc_help_group/text_slices/input_part002.txt†L10621-L10632】
- Mooch’s P45B test data (4.5 Ah, 50 A burst / 35 A continuous) reignited interest in high-discharge 21700s; the crew expects ~$8 pricing once stock stabilizes and sees 4p Xiaomi packs hitting 150–200 A battery current with manageable heat if deck cooling is added.【F:data/vesc_help_group/text_slices/input_part002.txt†L10930-L10955】

### Little FOCer V3.1 Arrivals & Rion Builds
- Rosheee secured Little FOCer V3.1 units rated for dual 290 A phase / 320 A absolute with 190 A battery limits, planning to drop them into his G30/Rion hybrid while the factory Rion controller shipment catches up—evidence that boutique controllers are finally shipping again albeit in small batches.【F:data/vesc_help_group/text_slices/input_part002.txt†L10655-L10680】

### Nucular Potting & Display Usability
- Nucular 24F buyers recommend ordering the potted variant for waterproofing, vibration damping, and a longer three-year warranty while accepting the added service difficulty; seasoned users note the stock display is powerful but notoriously complex to navigate without practice.【F:data/vesc_help_group/text_slices/input_part002.txt†L10888-L10911】

### BMS Displays & Budget Telemetry
- ANT’s external display is gaining traction as a low-cost VESC dash alternative; riders plan to mount the screen for live pack voltage/current readouts when standalone VESC displays remain scarce or expensive.【F:data/vesc_help_group/text_slices/input_part002.txt†L10912-L10916】

### Kelly, Sabvoton & Support Limitations
- Kelly’s KLS7230 firmware inconsistencies (320–380 A phase caps) and sparse email support pushed Paolo back toward VESC builds after weeks of unanswered diagnostics, mirroring Mirono’s decision to abandon Sabvoton hardware for MakerX controllers.【F:data/vesc_help_group/text_slices/input_part002.txt†L10491-L10534】【F:data/vesc_help_group/text_slices/input_part002.txt†L9699-L9859】

### Sensorless & HFI Roadmap
- MakerX owners without hall cables lean on upcoming VESC HFI improvements for zero-speed torque, but veterans still highlight hall sensors or encoders for maximum launch force until the new firmware proves itself.【F:data/vesc_help_group/text_slices/input_part002.txt†L9800-L9805】【F:data/vesc_help_group/text_slices/input_part002.txt†L10862-L10875】
- Paolo and Luis continue reinforcing that hall failures are common on high-power hubs, so carrying spare sensors or migrating to encoder-ready controllers remains part of their reliability checklist.【F:data/vesc_help_group/text_slices/input_part002.txt†L10838-L10850】
### Battery Configuration & Regen Guidance
- Artem walked a Vsett 10+ owner running a 16S5P Samsung 35E pack through safe limits—40 A battery, 140–150 A phase (170 A absolute) and ≤−17 A regen—highlighting that higher current mostly improves mid-speed acceleration and requires accurate hall wiring for speed telemetry.【F:data/vesc_help_group/text_slices/input_part002.txt†L2195-L2333】
- He reiterated that 35E cells tolerate about 1 C regenerative bursts but degrade quickly under faster charging, advocating ≤0.5 C routine charging and lower when time allows.【F:data/vesc_help_group/text_slices/input_part002.txt†L2339-L2344】

### Ubox Dual 100 V High-Power Setup & Voltage Limits
- Artem’s attempt to run a dual Ubox at 180 A phase/60 A battery on the rear and 120 A/50 A on the front (19 S) relies on sanding paint off the case, adding a 3 mm copper block, and even drilling for a fan or moving the controller outside—mods the group treats as short-duration solutions before dialing current back for daily use.【F:data/vesc_help_group/text_slices/input_part002.txt†L11156-L11164】
- Spintend support reiterated that 17 S is the practical ceiling (with regen disabled), calling 18 S unsafe; veterans echoed that 17 S builds survive while warning newcomers off 18 S despite brief successes.【F:data/vesc_help_group/text_slices/input_part002.txt†L11165-L11186】
- Real-world logs show 220–250 A bursts blowing dual-Ubox traces even after copper block and fan mods, so riders cap sustained pulls nearer 200 A per channel and prioritise airflow or external mounting before chasing higher duty cycles.【F:data/vesc_help_group/text_slices/input_part002.txt†L11588-L11605】【F:data/vesc_help_group/text_slices/input_part002.txt†L11633-L11670】
- Rosheee now powers a pair of Rion controllers from the Ubox harness using dual 20 S 7 P packs, underscoring the need to balance wiring, precharge and connector choices when mixing controller platforms on one scooter.【F:data/vesc_help_group/text_slices/input_part002.txt†L11901-L11953】【F:data/vesc_help_group/text_slices/input_part002.txt†L11960-L11969】

### Spot-Welding Losses & KWeld Power Sources
- KWeld’s stock 8 AWG leads can still sag—builders measured roughly 3 kW lost at the lugs and responded by shortening cables, stacking CNHL LiPos for ~1 600 A hits, or even borrowing car batteries to keep weld energy high.【F:data/vesc_help_group/text_slices/input_part002.txt†L11188-L11209】
- Rosheee noted that overly long cables and cold joints cause tip heating even when the silicone wire stays cool, prompting renewed focus on trimming leads and refreshing soldered lugs before tackling copper “sandwich” busbars.【F:data/vesc_help_group/text_slices/input_part002.txt†L11191-L11198】

- Repeated 80–90 km/h stops roasted 120 mm rotors and overheated Magura MT8s, so the crew now defaults to dual front brakes or 203 mm discs whenever scooters weigh enough to demand highway-speed braking margins.【F:data/vesc_help_group/text_slices/input_part002.txt†L11088-L11137】
- When calipers need a millimetre of offset, riders prefer cutting thin shim plates (nickel strip, spare torque-arm washers) instead of stacking round washers that can flex and loosen under braking loads.【F:data/vesc_help_group/text_slices/input_part002.txt†L11406-L11455】
- Shimano RT66/RT86, Magura Storm HC, Galfer, and other EU-sourced rotors top the shopping lists; AliExpress specials are avoided for 70 km/h builds despite tempting prices.【F:data/vesc_help_group/text_slices/input_part002.txt†L12102-L12151】

### Torque Arm Reinforcement for High-Power Hubs
- Ebike builders fitting VESCs to slim dropouts now file torque-arm slots for an interference fit and add pinch bolts so 10 mm steel clamps carry virtually all axle load instead of the frame alone.【F:data/vesc_help_group/text_slices/input_part002.txt†L11337-L11360】
- Tightening guidance emphasises short-handled sockets and incremental torque so 22 mm axle nuts and thin dropouts are not overstressed during setup.【F:data/vesc_help_group/text_slices/input_part002.txt†L11432-L11435】

- The group is standardising on hall-effect retrofits—gluing magnets to levers and pairing them with A1324LUA sensors—to gain proportional regen on any brake, keeping Bafang reed kits as simple on/off backups.【F:data/vesc_help_group/text_slices/input_part002.txt†L11240-L11283】
- Left-hand throttles are being wired for progressive regen while right hands stay on drive duty; VESC input mapping even lets riders cap an auxiliary on/off lever at ~10 A for panic stops.【F:data/vesc_help_group/text_slices/input_part002.txt†L11249-L11257】
- Without native locks, some experiment with breakers or even shorting motor phases as a parking brake, acknowledging the maneuver can halt a wheel instantly but risks harsh engagement if misused.【F:data/vesc_help_group/text_slices/input_part002.txt†L11269-L11298】

- Paolo advises swapping thermal pads for thin Kapton plus paste on CNC-machined housings to maximise contact, reserving pads for uneven castings where gap filling matters more.【F:data/vesc_help_group/text_slices/input_part002.txt†L11037-L11042】
- Riders tweaking CNC motor coolers add thin washers so air can pass beneath the plate, and confirm Laotie ES19 hubs share the same bolt pattern as Vsett 10 motors—handy for printing dual-sided heatsinks.【F:data/vesc_help_group/text_slices/input_part002.txt†L11045-L11076】
- Dual Ubox owners report that potting compound, deck-mounted clamps with fresh paste, and even heat pipes into thick aluminium plates shave 20 °C off, yet 220–250 A surges still blow traces—reinforcing the need for airflow or external mounting on extreme builds.【F:data/vesc_help_group/text_slices/input_part002.txt†L11480-L11520】【F:data/vesc_help_group/text_slices/input_part002.txt†L11588-L11605】【F:data/vesc_help_group/text_slices/input_part002.txt†L11633-L11670】【F:data/vesc_help_group/text_slices/input_part002.txt†L11686-L11699】【F:data/vesc_help_group/text_slices/input_part002.txt†L12494-L12499】
- Even potted Nucular 12Fs see cooler operation than bare front controllers, reinforcing the value of potting compounds or aluminium mounting plates when decks permit.【F:data/vesc_help_group/text_slices/input_part002.txt†L11491-L11507】

### MakerX Continuous-Current Reality
- MakerX Hi200 claims of 200 A continuous draw skepticism: Mirono’s unit hits ~70 °C after 30 minutes at 45 A battery/150 A phase while stored inside a bag, suggesting extra heatsinking and shorter motor leads are required before targeting higher limits.【F:data/vesc_help_group/text_slices/input_part002.txt†L12320-L12345】
- Riders comparing marketing highlight that without upside-down mounting on thermal paste the units overheat rapidly, so verifying MOSFET part numbers and cooling paths is essential before trusting 100 V/200 A brochures.【F:data/vesc_help_group/text_slices/input_part002.txt†L12324-L12354】

### Tubeless Tire Service & Supply Chain Warnings
- Rosheee flagged a 16 % jump in tire pricing tied to disrupted Russian/Ukrainian rubber feedstocks and urged stocking spares before shortages bite.【F:data/vesc_help_group/text_slices/input_part002.txt†L11187-L11187】
- Changing 11″ tubeless tires on non-split Wolf rims proved far tougher than video guides suggest, driving the team to circulate specific tutorials and extra tools before attempting the job again.【F:data/vesc_help_group/text_slices/input_part002.txt†L11745-L11759】

### Spin-Y Throttle Finalization & Module Options
- Artem locked in the Spin-Y throttle design: bidirectional 3.3 V output for VESCs, separate 5 V single-ended output, dedicated e-brake loop, onboard cruise button, and optional dual 12 mm button module fed through the same six-core harness with room for future accessories.【F:data/vesc_help_group/text_slices/input_part002.txt†L12390-L12452】
- He is targeting a €45–€55 price for the high-quality plastic shell and kept the button pod optional so riders who hate overhead switches can run the bare throttle without wasted space.【F:data/vesc_help_group/text_slices/input_part002.txt†L11402-L11408】【F:data/vesc_help_group/text_slices/input_part002.txt†L12402-L12412】
- Modular caps let riders delete the buttons for a slimmer profile or swap in mixed 16 mm/12 mm layouts once suitable three-position switches are sourced, keeping ergonomics tight against the brake clamp.【F:data/vesc_help_group/text_slices/input_part002.txt†L12408-L12445】

### Lighting Power & Horn Setup
- Mirono’s auxiliary lighting plan needs more than 3 A at 12 V, so he is paralleling two buck converters rather than carrying a separate pack—while Paolo counters that an external battery remains the simplest route.【F:data/vesc_help_group/text_slices/input_part002.txt†L12063-L12068】【F:data/vesc_help_group/text_slices/input_part002.txt†L12069-L12095】
- Riders keep the stock Xiaomi bell for polite alerts but back it up with 120 dB electronic horns or square-wave buzzers tied to controller outputs when traffic ignores acoustic warnings.【F:data/vesc_help_group/text_slices/input_part002.txt†L11814-L11822】【F:data/vesc_help_group/text_slices/input_part002.txt†L12070-L12078】

### Precharge & Power Button Wiring Lessons
- Spintend’s latching button expects reversed logic compared with Rosheee’s car-style switch (always on when pressed), forcing him to rework the +/− pins and LED leads before the controller would shut off cleanly.【F:data/vesc_help_group/text_slices/input_part002.txt†L12159-L12179】
- A 1 kΩ resistor proved too slow and too hot for pre-charging big controllers, so the consensus shifted toward lower-value resistors or proper anti-spark circuits paired with quick connection routines.【F:data/vesc_help_group/text_slices/input_part002.txt†L12457-L12463】
- Rosheee ultimately documented the correct polarity for his power-on button while stacking 17 W/mK interface pads and heat pipes, a reminder that mechanical cooling mods and switch wiring must be planned together.【F:data/vesc_help_group/text_slices/input_part002.txt†L12494-L12499】

### Firmware & Toolchain Constraints
- Flipsky 75100 owners who self-compiled VESC 6.0 hit jittering motors until reverting to 5.3 binaries, with peers pointing out that the 75100 hardware still lacks official 6.0 support and bemoaning the Lisp-based app architecture.【F:data/vesc_help_group/text_slices/input_part002.txt†L11299-L11319】【F:data/vesc_help_group/text_slices/input_part002.txt†L11369-L11379】
- Follow-on comparisons of 20S9P P42A/40T packs show 6–8 V sag at 135–148 A loads as acceptable when kept under ~10% of pack voltage, while 21S Sony VTC6A builds still drop ~7 V at 200 A, underscoring the role of series count and cell choice.【F:data/vesc_help_group/text_slices/input_part002.txt†L2443-L2479】

### Component Availability & Sourcing Notes
- Artem and others are struggling to replace Spintend’s discontinued 500 W water pumps, with 350 W substitutions seen as unstable and prompting disputes over bait-and-switch fulfillment during Chinese lockdowns.【F:data/vesc_help_group/text_slices/input_part002.txt†L2691-L2716】
- Group members warn that some AliExpress “chargers” are actually constant-current power supplies lacking CV taper or cutoff, risking overcharge if left unattended overnight.【F:data/vesc_help_group/text_slices/input_part002.txt†L2721-L2724】
- Ant-branded smart BMS units win praise for compact 80 A footprints and Bluetooth telemetry, but riders remain skeptical of their 150 A peak claims versus more proven (though pricier) JK BMS hardware.【F:data/vesc_help_group/text_slices/input_part002.txt†L2758-L2792】
- Discussions of oversized 130 mm hub motors for Weped platforms highlight packaging challenges, cost, and potential benefits of gearing experiments to recapture torque without excess heat.【F:data/vesc_help_group/text_slices/input_part002.txt†L2730-L2808】

### Rental Hardware Teardowns
- Ninebot G30 rental frames arrive overbuilt with added mass, red thread-lock, and MJ1 packs; recovering these scooters often involves reviving deeply discharged cells whose rental BMS boards prioritized anti-theft telemetry over cell protection.【F:data/vesc_help_group/text_slices/input_part002.txt†L1705-L1717】【F:data/vesc_help_group/text_slices/input_part002.txt†L2830-L2846】

### Controller Benchmarks & MOSFET Debates
- Enthusiasts are cataloging MOSFET part numbers across controllers (Nucular, Vsett, Ubox), debating Rds(on) claims below 2 mΩ and comparing performance to readily available Chinese alternatives such as HUASHUO HSP0076A devices.【F:data/vesc_help_group/text_slices/input_part002.txt†L2629-L2692】
- Spintend users continue flipping hardware—new 75 V and 100 V Ubox kits with ADC boards and thermal pads—while flagging measurement quirks (e.g., Flipsky hall auto-detection causing stutter until parameters are entered manually).【F:data/vesc_help_group/text_slices/input_part002.txt†L2601-L2686】【F:data/vesc_help_group/text_slices/input_part002.txt†L3120-L3138】

### Battery Welding & Mixed-Metal Reliability
- Builders debating copper-nickel “sandwich” busbars note that without shielding from air or using tin interfaces, weld joints can crack over time due to incompatible metals; sealed packs or pure-nickel tabs are preferred when Sunko-grade welders struggle with copper.【F:data/vesc_help_group/text_slices/input_part002.txt†L1640-L1645】

### Ninebot G30 Brake Retrofits & Frame Mods
- New arrivals show 3D-printed rear brake adapters with a 1 cm aluminium reinforcement ring for the Ninebot G30, drawing skepticism about PLA strength and prompting calls for CNC’d metal parts if riders expect the mount to survive repeated hard stops at 60 km/h and beyond.【F:data/vesc_help_group/text_slices/input_part002.txt†L3214-L3249】
- Experienced owners note that 10 × 3 in tyres require trimming the rear fender and prefer routing the rear brake hose internally instead of the inverted Magura mod to avoid wobble, highlighting practical fitment tweaks for wide-tyre builds.【F:data/vesc_help_group/text_slices/input_part002.txt†L3536-L3551】

### Deck Space & Battery Spacer Experiments
- Builders circulate oversized 3D-printed deck spacers that claim room for up to four Xiaomi Pro packs (~270 cells), yet veterans warn about relying on plastic trays and sparse M3 hardware to secure 30 kg of cells and note that such expansions quickly exceed the chassis’ stock brakes, suspension, and drivetrain.【F:data/vesc_help_group/text_slices/input_part002.txt†L4757-L4795】
- Artem reminds riders that premium decks like the Vsett 10+ already house 20S9P 21700 packs without spacers, while others joke that 18650 configurations are becoming obsolete as higher-density cells dominate performance builds.【F:data/vesc_help_group/text_slices/input_part002.txt†L4793-L4799】

### Controller Output Debates & Thermal Limits
- Rosheee and Adam spar over pushing Spintend uBox and Nucular setups, with Rosheee citing 17S6P Samsung 40T packs delivering dual 90 A battery limits and 200 A phase, while Adam argues that hardware without sufficient thermal headroom simply throttles or fails—underscoring the need to validate controller temperature logs before boasting about current settings.【F:data/vesc_help_group/text_slices/input_part002.txt†L4200-L4306】
- Adam later clarifies he values VESC firmware but sees the hardware gap for sustained ≥15 kW outputs as the real issue, framing Paolo’s high-power controller project as the bridge between VESC features and heavy-load reliability.【F:data/vesc_help_group/text_slices/input_part002.txt†L4723-L4726】

### Battery Layout Tools & Copper Pack Finishing
- The crew trades battery-layout resources: RePackr and the e4bike.ru configurator help visualize cell counts, but Artem cautions they only “guesstimate” and miss vertical stacking optimizations, so CAD remains essential for precision triangle packs.【F:data/vesc_help_group/text_slices/input_part002.txt†L4813-L4857】
- For copper busbars, Artem advises working with gloves, spraying Kontakt 60 on welds, and sealing with Kapton/fish paper/heatshrink to prevent corrosion, while Mirono pushes “copper sandwich” stacks and others debate tinning layers for longevity.【F:data/vesc_help_group/text_slices/input_part002.txt†L4825-L4835】
- Beginners asking about short protection get reminded that smart BMS units react far faster than external fuses, doubling as charge balancers and reinforcing why high-current builds still rely on BMS safeguards.【F:data/vesc_help_group/text_slices/input_part002.txt†L4868-L4888】

### Flipsky Failures, Firmware & Tooling
- Mirono shorted hall wires against a brake rotor, killing a Flipsky 4.2 VESC’s 5 V rail and confirming the hardware lacks inline protection—motivating better harness routing or spare controller plans.【F:data/vesc_help_group/text_slices/input_part002.txt†L4703-L4721】
- Gigolo Joe shares jaykup’s open-source Flipsky 75100 V2 firmware and source files while Paolo compiles fresh “no-limit” BINs for both single-shunt and newer three-shunt boards; koxx even publishes a Docker image for easier local builds, stressing the need to match firmware to shunt hardware.【F:data/vesc_help_group/text_slices/input_part002.txt†L5367-L5406】【F:data/vesc_help_group/text_slices/input_part002.txt†L6008-L6033】
- Earlier in the thread, Banggood-sourced V2s arrive with triple-stacked 2 W shunts and minimal heatsinking, prompting Paolo to caution that only copper 0.5 mΩ replacements keep calibration intact and that firmware recalibration is risky without proper tools.【F:data/vesc_help_group/text_slices/input_part002.txt†L5191-L5274】
- Artem warns that Flipsky’s in-house 75100 V2 PCB already burned during acceleration on stock firmware, suggesting early-batch reliability may be fading and reinforcing the call for vetted binaries and thermal monitoring.【F:data/vesc_help_group/text_slices/input_part002.txt†L6054-L6059】

### High-Power Single Motor Builds & Cooling Mods
- Gigolo Joe documents an Inokim OX rewound motor on 16S/20S packs pulling 9–12 kW peaks with 180 A phase and 100 A battery limits, but admits the six TO-220 MOSFETs hit 96 °C on 10 km speed runs despite custom CPU-style heatsinks, framing active cooling as the limiting factor for budget ESCs.【F:data/vesc_help_group/text_slices/input_part002.txt†L5421-L5499】
- Follow-up logs highlight that even reinforced V1 units eventually fail from prolonged field-weakening or detection routines, reminding builders that $100 controllers need conservative settings or spares ready.【F:data/vesc_help_group/text_slices/input_part002.txt†L6054-L6079】

### Connector Upgrades & Current Bottlenecks
- Adam dissects the Higo L1019 harness: while the cable bundles 11 AWG phase leads and seven signal wires neatly, the solid 2.5 mm bullets struggle above ~160 A phase, so he replaces them with 6 mm XT150 bullets for high-power Vsett applications.【F:data/vesc_help_group/text_slices/input_part002.txt†L6000-L6039】【F:data/vesc_help_group/text_slices/input_part002.txt†L6101-L6101】
- Artem confirms NAMI scooters ship with 6 mm bullets and XT90 battery connectors, offering a sturdier benchmark for riders spec’ing Paolo’s upcoming controllers or targeting 200 A phase builds.【F:data/vesc_help_group/text_slices/input_part002.txt†L6050-L6063】
- Builders swapping to XT150 bullets highlight flattening the phase wire against the barrel so copper, not solder, carries current, often omitting the plastic housings on motor leads and bundling the bullets with the Higo 6-pin hall harness under heat-shrink.【F:data/vesc_help_group/text_slices/input_part002.txt†L5077-L5080】【F:data/vesc_help_group/text_slices/input_part002.txt†L5996-L5999】
- Follow-up comparisons note that 6 mm bullets from different brands can vary in length/diameter, Julet knockoffs use soft plastics with brittle conductors, and genuine Higo connectors remain the safer choice when mixing hall and temperature wires alongside high-current phases.【F:data/vesc_help_group/text_slices/input_part002.txt†L5965-L5980】
- For ferrofluid-treated hubs, riders seat the rim between their feet to reinsert the stator smoothly after injecting fluid through the magnet gap, sealing XT150 terminations with Kapton to manage both cooling and service access.【F:data/vesc_help_group/text_slices/input_part002.txt†L5916-L5920】【F:data/vesc_help_group/text_slices/input_part002.txt†L5938-L6005】

### Re-pass Highlights for Lines 5000–6500 (26 Apr – 2 May 2022)
- First-time uBox adapter users kept missing throttle input until VESC Tool’s input mode was switched to ADC; the chat stresses validating ADC mode and matching the adapter’s 5 V/3.3 V toggle before suspecting wiring faults.【F:data/vesc_help_group/text_slices/input_part002.txt†L5005-L5024】
- Members compared thermal pastes for controller service, warning that cheap AliExpress compounds dry out quickly while Arctic MX-4–class grease retains performance longer—worth the small premium when resealing ESCs.【F:data/vesc_help_group/text_slices/input_part002.txt†L5027-L5058】
- The crew reiterated that bare XT60 bullets or 4 mm connectors choke high-phase builds; 6 mm XT150 bullets (ideally flattened onto the conductor) are the minimum for heavily-modded Xiaomi/Vsett setups, and overheated plugs can trim peak power by ≈20 %.【F:data/vesc_help_group/text_slices/input_part002.txt†L5061-L5089】
- Flipsky 75100 V2 boards ship with stacked low-wattage shunts that overheat or desolder if builders try triple-stacking copper; Paolo recommends sourcing single 0.5 mΩ copper shunts instead and notes the V2 hardware diverges enough to demand care with firmware gain settings.【F:data/vesc_help_group/text_slices/input_part002.txt†L5207-L5259】
- Community firmware support now spans Jaykup’s shared 5.3 V2 binary, Paolo’s “no limit” V1 build, and a custom 3-shunt bin; the group is trading source files and Docker tips so riders can recompile safely rather than brute-force shunt mods.【F:data/vesc_help_group/text_slices/input_part002.txt†L5345-L5397】【F:data/vesc_help_group/text_slices/input_part002.txt†L5900-L5988】
- Gigolo Joe’s single-motor logs reaffirm that 75100 V1 can burst past 9–12 kW but still thermal-throttles around 96 °C, while Paolo reports V2 units running cooler yet still failing on stock firmware during hard launches—fueling concern that quality varies between revisions.【F:data/vesc_help_group/text_slices/input_part002.txt†L5800-L5845】【F:data/vesc_help_group/text_slices/input_part002.txt†L6054-L6080】
- Blade motor servicing tips include prying stubborn covers evenly, resealing with silicone, injecting ferrofluid through the magnet gap while wearing eye protection, and bracing the rim between your feet to avoid slamming the stator back into place.【F:data/vesc_help_group/text_slices/input_part002.txt†L5828-L5895】【F:data/vesc_help_group/text_slices/input_part002.txt†L5916-L5920】
- Higo L1019 harnesses impress with 11 AWG leads and seven conductors but their 2.5 mm solid bullets still bottleneck ≈200 A phase builds, prompting many to splice in XT150 leads while keeping Higo shells for signals; genuine Higo parts hold up better than Julet clones when crimping hall looms.【F:data/vesc_help_group/text_slices/input_part002.txt†L6003-L6008】【F:data/vesc_help_group/text_slices/input_part002.txt†L5955-L5980】
- Battery planners weighed 48X vs. Samsung 50S/50G packs: 48X stays balanced with minimal sag (~6–7 V at 130–150 A) but is a 14 A-per-cell chemistry, whereas Paolo’s 21S7P Sony pack drops 8–9 V at ~193 A, supporting the view that 25 A-class cells can be pushed harder but cost more and run warmer.【F:data/vesc_help_group/text_slices/input_part002.txt†L6183-L6221】
- Kelly owners observed BMS trips from battery-current overshoot and shared torque-speed screenshots; suggested mitigations include lowering motor amps, checking auto-detected phase angles, and trimming throttle dead-zones so the ESC stops surging after throttle release.【F:data/vesc_help_group/text_slices/input_part002.txt†L5815-L5820】【F:data/vesc_help_group/text_slices/input_part002.txt†L6198-L6230】
- QS hub builders confirmed VESC firmware can read KTY83 sensors, clearing the way for aggressive field-weakening experiments on 5T motors without giving up temperature telemetry.【F:data/vesc_help_group/text_slices/input_part002.txt†L6295-L6300】

### Re-pass Highlights for Lines 6500–8000 (2 – 7 May 2022)
- Paolo’s Kelly 72150 saga confirms that hall/phase mismatches can pull 200 A+ even with wheels in the air, overheating 7 AWG phase leads and 8 mm bullets until every one of the ~32 hall/phase permutations is tested—reinforcing why VESC/Nucular auto-alignment is prized.【F:data/vesc_help_group/text_slices/input_part002.txt†L6500-L6674】
- Nucular’s reputation stems from hand-assembled batches with 2–3 year warranties and effectively zero random failures reported by long-time group members, but the crew notes small production runs protect IP from Chinese copycats and cap availability.【F:data/vesc_help_group/text_slices/input_part002.txt†L6679-L6682】
- Builders eye the open-source BESC platform yet flag that thick-copper PCBs cost ~€100 for five boards, component sourcing is pricey, and assembly effort only pays off for high-power ebikes versus scooters.【F:data/vesc_help_group/text_slices/input_part002.txt†L6683-L6716】
- Fresh PMT tire testing shows quieter rides and huge grip gains, but Paolo argues tubeless conversions unlock low-pressure performance and that newer yellow-logo batches fit better than early runs—topics earmarked for deeper validation.【F:data/vesc_help_group/text_slices/input_part002.txt†L6722-L6751】
- Federico documents hammering copper busbars flat to resurrect a burnt G30 ECU shunt while comparing “D” series boards with extra capacitors, providing a repeatable template for budget Ninebot repairs.【F:data/vesc_help_group/text_slices/input_part002.txt†L6797-L6821】
- Dual uBox owners debating forced-air mods conclude that flipped fans without a proper heatsink do little; bolting cases to aluminium with thermal paste still matters more than cutting deck vents.【F:data/vesc_help_group/text_slices/input_part002.txt†L6820-L6869】
- Kaabo Wolf teardowns reveal controllers glued into the chassis, 10 AWG battery looms, skinny 2.5 mm² phase leads on high-kV Wolf X motors, and speed limits enforced by grey/white harness loops plus P-settings—steps riders must reverse before swapping in VESCs.【F:data/vesc_help_group/text_slices/input_part002.txt†L7192-L7270】
- The same tear-down logged QS8 gaps, XT90 bundling hacks, and 4 AWG upgrade plans while reminding techs to discharge controller capacitors before unplugging anything after a Wolf controller “puffed” on the bench.【F:data/vesc_help_group/text_slices/input_part002.txt†L6991-L7050】【F:data/vesc_help_group/text_slices/input_part002.txt†L7235-L7269】
- Wolf lighting harness maps show the hub PCB stepping pack voltage down to 12 V, with orange/brown leads feeding the switchgear—useful when retaining stock lights alongside Spintend ADC boxes.【F:data/vesc_help_group/text_slices/input_part002.txt†L7980-L8084】
- Mirko’s Monorim tuning notes now include spring-rate guidance (250 lb for ≈95 kg riders) and confirmation that steering dampers eliminate 55 km/h wobbles if the vertical hinge screws stay tight.【F:data/vesc_help_group/text_slices/input_part002.txt†L7102-L7141】

### High-Capacity Cell Debates & Sag Benchmarks
- Riders contrast Samsung 50G/50S, Molicel P42A/P45B, and Lishen 48X cells, trading price quotes (≈€12 for 50S, <€4.5 aspirational for 48X) and pointing out that 5 Ah 30 A cells remain elusive; Paolo and Artem note 48X excels around 14 A per cell while 50S sustains ≈23 A before 10% sag.【F:data/vesc_help_group/text_slices/input_part002.txt†L6111-L6193】
- A 20S9P 48X pack reports 6–7 V sag at 130–150 A with cell temps under 27 °C, reinforcing why builders chase active balancing and high parallel counts; Paolo’s 21S7P Sony setup sees ~9 V sag at 193 A, highlighting realistic performance for “25 A-class” cells.【F:data/vesc_help_group/text_slices/input_part002.txt†L6168-L6222】
- Subsequent planning chats weigh the cost of chasing 5 Ah cells (≈€12 for Samsung 50S) against the practicality of dual-pack swaps, with riders praising 48X packs for staying balanced without active balancers yet accepting their 14 A per-cell comfort zone while Paolo’s Sabvoton builds tolerate ~27 A per Sony cell at ~9 V sag.【F:data/vesc_help_group/text_slices/input_part002.txt†L6120-L6222】

### Kelly Controller Hall/Phase Troubleshooting
- Paolo’s Kelly 72150 struggles with high no-load current until peers share hall/phase rewiring charts and recommend iterating all 32 combinations, mirroring Endless Sphere guides that document Chinese controllers’ weak auto-detection compared to VESC and Nucular tooling.【F:data/vesc_help_group/text_slices/input_part002.txt†L6509-L6674】
- Owners warn that mismatched hall order overheats phase leads even off-load, while Nucular’s identification angle check and Kelly reflashing cables are cited as guardrails before writing the hardware off as a “scam.”【F:data/vesc_help_group/text_slices/input_part002.txt†L6513-L6668】
- Earlier Blade logs show Kelly firmware overshooting battery current—triggering BMS cutouts and throttle kick-on—until riders clone each other’s torque-speed tables and trim motor amps, illustrating how differently the Kelly regulates limits compared to uBox profiles.【F:data/vesc_help_group/text_slices/input_part002.txt†L5639-L5699】【F:data/vesc_help_group/text_slices/input_part002.txt†L5814-L5819】

### QS & Wolf X Motor Planning
- QS205 owners confirm KTY83 sensors work with VESC firmware, enabling high-torque 5T builds so long as phase limits increase beyond 250 A and wheel size stays manageable; the group estimates ~250 Nm with 18″ moto tires when paired with robust controllers.【F:data/vesc_help_group/text_slices/input_part002.txt†L6295-L6333】
- Paolo unboxes a high-kV Wolf X motor with only 2.5 mm² phase leads and jokes about 36 V packs spinning to 72 km/h, signaling upcoming rewinds or harness upgrades before serious power tests.【F:data/vesc_help_group/text_slices/input_part002.txt†L7192-L7203】

### High-Power Single-Motor Logs & Firmware Experiments
- Gigolo Joe’s rewound single-motor build on a Flipsky 75100 V1 runs 110–130 A battery, 250 A phase, and 80 A field weakening, logging ~13 kW bursts but driving MOSFET temps into the 90 °C range—he plans to flash Paolo’s “no 250 A cap” firmware to see if the controller can stretch further.【F:data/vesc_help_group/text_slices/input_part002.txt†L6990-L7052】
- Paolo recounts a 14 kW single-motor uBox pull that ended in fireworks, underscoring how paper-taped repairs and open decks only buy so much thermal headroom for budget ESCs.【F:data/vesc_help_group/text_slices/input_part002.txt†L7071-L7087】

### Suspension & Steering Upgrades for Ninebot Builders
- Mirko Boni finalizes a G30 build with Magura brakes, a 10S + 6S pack on the stock BMS, and a Monorim kit; he recommends 250 lb EXA 291R shocks for ~95 kg riders after reporting 55 km/h wobble cured by a steering damper tightened vertical pivot screws.【F:data/vesc_help_group/text_slices/input_part002.txt†L6303-L6310】【F:data/vesc_help_group/text_slices/input_part002.txt†L7102-L7139】
- Community members share AliExpress sourcing links (~€70) and remind heavy riders to tune spring preload rather than overspec shocks immediately.【F:data/vesc_help_group/text_slices/input_part002.txt†L7108-L7129】

### Enclosure Venting & Deck Cooling Hacks
- D J carves large side vents into a scooter deck for “fresh air,” drawing mixed reviews about the limited open area but illustrating how extreme airflow mods remain common among high-power uBox owners.【F:data/vesc_help_group/text_slices/input_part002.txt†L7161-L7166】
- Luis reminds Kaabo owners that closing the deck quickly drives controllers past 80 °C, so many run with covers ajar or cutouts in place until more robust thermal solutions arrive.【F:data/vesc_help_group/text_slices/input_part002.txt†L7535-L7558】

-### Kaabo Hub Lighting Harness & DC-DC Behavior
- The Wolf lighting junction expects full pack voltage on the orange feed and returns regulated 12 V for blinkers, so riders bypassing the stock display must jumper battery positive into the hub board and reuse the switch harness rather than relying on the controller jumper alone.【F:data/vesc_help_group/text_slices/input_part002.txt†L8000-L8088】【F:data/vesc_help_group/text_slices/input_part002.txt†L8273-L8280】
- Because the board labels orange/brown without context, Luis urges confirming polarity with a multimeter before rewiring; otherwise riders risk chasing phantom faults when the handlebar switch simply isn’t energized.【F:data/vesc_help_group/text_slices/input_part002.txt†L8052-L8074】
- Rosheee double-checked that the PCB feeds both 84 V headlight rails and a 12 V branch for blinkers and brake lights, so any direct-pack retrofit must respect both supply levels when mixing OEM lamps with VESC swaps.【F:data/vesc_help_group/text_slices/input_part002.txt†L8273-L8279】

### Ubox High-Speed Limits, Logs & Cooling Reality
- Rosheee’s 115 km/h pulls show the 100 V uBox tripping ABS overcurrent near the 140 A absolute ceiling, confirming high-ERPM cutouts stem from firmware protection rather than the Daly BMS.【F:data/vesc_help_group/text_slices/input_part002.txt†L8355-L8405】
- Even with battery current capped at 120 A per controller, twin uBoxes spike to ~150 A and sag Kaabo’s pack by 15 V, highlighting the need for sturdier cells and connectors when chasing 6 kW+ on stock packs.【F:data/vesc_help_group/text_slices/input_part002.txt†L8972-L8985】
- The “definitive edition” uBox runs cooler than early betas, yet Paolo reminds builders that resin-insulated MOSFETs conduct poorly into the case and consumer IR thermometers under-read die temps—accurate checks need pro-grade cameras or exposed FET surfaces.【F:data/vesc_help_group/text_slices/input_part002.txt†L9000-L9010】【F:data/vesc_help_group/text_slices/input_part002.txt†L9411-L9446】

### Controller Alternatives & Availability Pressure
- Tronic 250 units promise 100 A battery and 250 A phase at up to 21 S for about €400 each, but community reports flag rapid heating and the dual-stack price (~€1 100 with SmartDisplay) versus perpetually back-ordered Nucular 12F kits.【F:data/vesc_help_group/text_slices/input_part002.txt†L8200-L8216】
- Little FOCer boards share Tronic’s TO-247 topology yet ship bare, forcing buyers to fabricate aluminum heatsinks, while YYK square-wave controllers survive repeated shorts albeit without VESC configurability—illustrating why riders still default to Spintend when other options are sold out.【F:data/vesc_help_group/text_slices/input_part002.txt†L8621-L8690】
- Shopfronts reselling Tronic hardware stretch marketing claims (e.g., “250 A continuous”), reinforcing the need to verify real limits before spending €800+ on boutique controllers.【F:data/vesc_help_group/text_slices/input_part002.txt†L9059-L9065】

### Battery Limits, Cell Debates & Pack Planning
- Kaabo’s stock 16 S 5 P Samsung 50G pack hits 150 A despite 120 A limits, adding 15 V of sag; riders plan 20 S 7–10 P Molicel upgrades and log that even 5 P samples show alarming droop at high load.【F:data/vesc_help_group/text_slices/input_part002.txt†L8972-L8991】【F:data/vesc_help_group/text_slices/input_part002.txt†L9004-L9016】
- LG M50T cells are repeatedly labeled “crap” 10 A parts compared with the promised 15 A M50LT variant, pushing Wolf owners toward P42A/P45B class cells for sustained power even at higher cost.【F:data/vesc_help_group/text_slices/input_part002.txt†L8830-L8853】【F:data/vesc_help_group/text_slices/input_part002.txt†L9011-L9016】
- Rosheee’s “design v2” G30 build touts 16 S 5 P range while trimming deck weight, underscoring how packaging changes accompany chemistry swaps.【F:data/vesc_help_group/text_slices/input_part002.txt†L9024-L9033】

### BMS Bypass, Balancing & Switch Control
- Daly charge/discharge units are pushed to 180 A peaks yet accused of offering “no protection,” prompting several riders to bypass discharge entirely, rely on VESC voltage limits, and even yank Daly boards off 17 S packs once they trust their logging.【F:data/vesc_help_group/text_slices/input_part002.txt†L8785-L8809】
- Bluetooth-enabled Daly/JK units let builders toggle outputs without sparks, alleviating anti-spark worries when the hardware lacks a physical switch.【F:data/vesc_help_group/text_slices/input_part002.txt†L9452-L9459】

### Sensor Integration & Telemetry Workarounds
- Without a VESC-compatible BMS, Rosheee mapped a deck-mounted thermistor onto the motor-temp input so he could monitor battery bay heat, acknowledging it disables true battery-temp compensation and merely mirrors readings in the motor channel.【F:data/vesc_help_group/text_slices/input_part002.txt†L8306-L8323】

### Battery Protection & Installation Failures
- A shredded 13 S 5 P pack shows what happens when a battery slides on the Ninebot rails: even triple insulation (fish paper, Kapton, heat-shrink) can wear through without proper padding or clamps.【F:data/vesc_help_group/text_slices/input_part002.txt†L9071-L9153】
- Mirono and Her0DasH advocate rigid spacers, craftplex plates, or full cases to keep packs fixed, while others explore stainless or fiberglass enclosures that can survive being tossed without bruising cells.【F:data/vesc_help_group/text_slices/input_part002.txt†L9145-L9245】

### Track Days, Enforcement & Build Priorities
- Track prep wish-lists include external controller mounts, water-cooled dual Vsett motors, ferrite-treated hubs, dual front Maguras, and widened cockpits so a “beastmod G30” can survive timed laps without puffing stock parts.【F:data/vesc_help_group/text_slices/input_part002.txt†L8711-L8783】
- European crews now book kart circuits for €25–35 practice sessions, while Swiss police impounded a 133 km/h Wolf Warrior—complete with fines and potential jail—reminding builders to balance racing ambitions with legal risk.【F:data/vesc_help_group/text_slices/input_part002.txt†L9170-L9187】【F:data/vesc_help_group/text_slices/input_part002.txt†L9470-L9489】

-### Connectors, Accessories & Shared Assets
- QS8 battery plugs are derided as bulky 120 A parts compared with inexpensive HXT 8 mm bullets that flatten onto the conductor so copper, not solder, carries the load; the crew also warns XT90 realistically handles ~45 A continuous despite its nameplate.【F:data/vesc_help_group/text_slices/input_part002.txt†L8929-L8941】
- Vsett 9 owners shopping 5.5 mm banana sets were steered toward XT150 housings because their 6 mm bullets run cooler at the scooter’s ~35–40 A battery and 95 A phase targets while staying easy to service.【F:data/vesc_help_group/text_slices/input_part002.txt†L8174-L8185】
- Riders share fresh G30 frame brace files (`middle.stl`, `front/left/right/rear.3mf`) to reinforce ground decks after heavy grinding, making it easier to repeat high-power conversions.【F:data/vesc_help_group/text_slices/input_part002.txt†L9494-L9499】
- Budget locks from big-box chains (e.g., €5 Action models) are dismissed as décor rather than security, with veterans urging solid chains and padlocks when leaving high-power scooters unattended.【F:data/vesc_help_group/text_slices/input_part002.txt†L9044-L9047】

### Firmware Utilities & BLE Modules
- Vedder’s GitHub still hosts the NRF51 firmware builders need for legacy BLE daughterboards; SirGeoff pointed to `nrf51_vesc_ble_16k_16m_rx11_tx9_led3.bin` and accompanying pinout docs so latecomers can flash modules without hunting unofficial hex dumps.【F:data/vesc_help_group/text_slices/input_part002.txt†L8383-L8389】

### Carbon Bodywork & Custom Cooling Concepts
- A carbon-fiber specialist friend is sketching Kaabo fenders and CNC’d aluminium spacers with heat pipes, yet Paolo reiterates that without direct MOSFET-to-baseplate contact, exotic coolers offer marginal gains over Spintend’s resin-bound layout.【F:data/vesc_help_group/text_slices/input_part002.txt†L9381-L9431】

### Samsung 50E Abuse & Battery Mount Failures
- Rosheee’s Kaabo pack testing shows that pulling 130 A from a Samsung 50E 5 P module destroyed a 3D-printed battery frame and triggered 177 A peaks until the BMS cut out at 180 A, underscoring how far the load exceeded the chemistry’s ~50 A practical ceiling.【F:data/vesc_help_group/text_slices/input_part002.txt†L12529-L12583】
- Group feedback labels 50E cells an 8 A “real-world” part—saggy even at 15 A—while recommending higher-current packs such as 20S6P/20S7P upgrades for the G30 and Kaabo platforms to avoid repeat meltdowns.【F:data/vesc_help_group/text_slices/input_part002.txt†L12538-L12541】【F:data/vesc_help_group/text_slices/input_part002.txt†L12604-L12607】

### Deck Packaging & Controller Fitment Notes
- Zero 10X owners measured 360 × 133 × 62 mm under the carbon deck, confirming room for bespoke 20S6P and 20S7P packs plus space to relocate controllers once rails are removed.【F:data/vesc_help_group/text_slices/input_part002.txt†L12538-L12548】
- A Flipsky 75100 can sit inside a Dualtron Mini with the stock case but thermal throttles around 75 °C when limited to 35 A battery, highlighting the need for external cooling or lower current targets in compact frames.【F:data/vesc_help_group/text_slices/input_part002.txt†L12550-L12558】

### Copper Busbar Sourcing & Welding Techniques
- Builders found 0.15 mm nickel-plated copper strip in 8 mm widths rated for ~15 A per cell, noting it outperforms pure nickel but still favors “copper sandwich” busbars or sheet stock when currents exceed 25 A per parallel group.【F:data/vesc_help_group/text_slices/input_part002.txt†L12622-L12645】【F:data/vesc_help_group/text_slices/input_part002.txt†L12649-L12654】
- Directly spot-welding thick copper remains risky: without inert gas the joint oxidizes, .2 mm copper sticks to probes, and the heat needed endangers cells, so the consensus is copper plate plus nickel- or steel-topped tabs for reliable bonds.【F:data/vesc_help_group/text_slices/input_part002.txt†L13624-L13640】

### Brake Pad Performance & Wet-Weather Behavior
- Heavy scooters chew through stock Magura pads in <500 km; riders now standardize on full-metallic Kool Stop D170S sets to keep MT5/MT7 brakes alive under gritty conditions.【F:data/vesc_help_group/text_slices/input_part002.txt†L13161-L13177】【F:data/vesc_help_group/text_slices/input_part002.txt†L13195-L13197】
- Xiaomi Xtech calipers can grab harder when the rotor is wet, surprising new riders and prompting fresh bleeding and bedding procedures so modulation stays predictable after rain.【F:data/vesc_help_group/text_slices/input_part002.txt†L13151-L13158】【F:data/vesc_help_group/text_slices/input_part002.txt†L13175-L13182】

### uBox Bluetooth Recovery & UART Setup
- When the uBox BLE module refuses to pair, the fix is still to connect over USB, flash both firmware and bootloader from the shared Google Drive, and only then retry phone pairing—5.3 remains flaky for some, so validated 5.2 binaries stay in rotation.【F:data/vesc_help_group/text_slices/input_part002.txt†L13177-L13211】
- After reflashing, builders double-check UART/BLE toggles inside VESC Tool (desktop first, then Android sideload) and reboot the controller before reconnecting, otherwise the module never advertises despite the blue LED.【F:data/vesc_help_group/text_slices/input_part002.txt†L13215-L13277】

### Enforcement Case Study: Dyno Verification
- A Danish rider was fined €400 (reduced to €200 for students) when police strapped his scooter to a dyno, but a 29 km/h VESC profile and polite cooperation prevented confiscation—reinforcing the value of proof-of-compliance modes even when true top speed is far higher.【F:data/vesc_help_group/text_slices/input_part002.txt†L13294-L13323】

### Controller Cooling & Frequency Tweaks
- Dropping zero-vector frequency from 30 kHz to 20 kHz on an Inokim OX cut VESC MOSFET temps by ~30 °C while sustaining 72 V/250–300 A pulls, showing how PWM parameters can matter as much as hardware swaps for thermal headroom.【F:data/vesc_help_group/text_slices/input_part002.txt†L13653-L13668】
- Paolo’s “hole-drilled” hub strategy still pairs with ferrofluid, but he warns vented covers must stay dry before reapplication—otherwise the fluid hardens and ruins the stator.【F:data/vesc_help_group/text_slices/input_part002.txt†L13748-L13758】

### Kelly Controller Power Mapping & Cable Limits
- Track riders confirmed Kelly KLS controllers report phase/battery current as the same percentage; 7212S units labeled 50 A battery in fact delivered 120 A for sustained pulls, and 7218S builds hit 240 A at 115 km/h until cooling became the bottleneck.【F:data/vesc_help_group/text_slices/input_part002.txt†L13783-L13843】
- Even 10 mm² motor leads run hot during 350 A hill climbs, prompting plans for thicker phase wiring and reminders that cable resistance can undo expensive controller upgrades if it is left stock.【F:data/vesc_help_group/text_slices/input_part002.txt†L13888-L13915】

### Spintend ABS Over-Current Mitigation
- Rosheee relayed Spintend support’s fix for FW 5.3 ABS trips: enable the ABS feature in VESC Tool and lower the current filter constant to stop false over-current cutouts at high ERPM.【F:data/vesc_help_group/text_slices/input_part002.txt†L13921-L13928】

### Magura Brake Options & Steel-Braided Lines
- Riders comparing MT5e/MT7 kits confirmed the calipers share the same casting while the MT7 lever adds bite-point adjustment and four individual pads, pushing commuters to source the aluminium one-finger HC levers instead of plastic sensor blades for harder stops.【F:data/vesc_help_group/text_slices/input_part002.txt†L14131-L14156】
- Rosheee’s “Stahlflex” brake hoses (≈€90 for both wheels) stay firm under heat, but others stress matching the hose ID to each brand’s banjo outlet so Magura, Shimano, or Hope fittings seal correctly.【F:data/vesc_help_group/text_slices/input_part002.txt†L14100-L14115】【F:data/vesc_help_group/text_slices/input_part002.txt†L14703-L14726】
- EBC’s sintered pads remain the group’s go-to upgrade when stock compounds glaze during track sessions.【F:data/vesc_help_group/text_slices/input_part002.txt†L14145-L14146】

### Hub Temperature & Hall Troubleshooting
- One builder shared hub-thermistor placement tips—nest the probe between windings and secure only the lead with silicone—so the sensor survives heat cycles without insulating the tip.【F:data/vesc_help_group/text_slices/input_part002.txt†L14118-L14124】
- Mirono’s surging resolved after reordering hall wires from 2-1-3 back to 1-2-3 and lowering the sensorless handover from 2000 to 1200 ERPM, confirming VESC auto-detect can pass with mis-sequenced halls yet still misfire at high load.【F:data/vesc_help_group/text_slices/input_part002.txt†L14506-L14532】【F:data/vesc_help_group/text_slices/input_part002.txt†L14820-L14824】

### Firmware & Controller Safety Alerts
- Artem reiterated that Ubox hardware can burn on FW 5.3 due to a current-sensing regression; he advises sticking with 5.2 or reducing amp limits until Spintend finishes its investigation.【F:data/vesc_help_group/text_slices/input_part002.txt†L14654-L14672】
- Gigolo Joe logged a Flipsky 75100 V2 running 20 S (≈77 V) on FW 5.03 at 160 A phase / 110 A battery without field weakening, noting the controller reads pack voltage a few volts low—a detail to remember when budgeting margin at 20 S.【F:data/vesc_help_group/text_slices/input_part002.txt†L14944-L14966】

### Rion/Tronic MOSFET Support Gaps
- Rosheee’s Rion/Tronic controller lost a single MOSFET, yet support demanded a full return instead of sharing parts; Konstantin traced the device to NCE’s NCEP01T30T, which is only available via preorder batches, complicating self-repair.【F:data/vesc_help_group/text_slices/input_part002.txt†L15160-L15357】
- Builders worry poor solder wetting on the high-current traces helped trigger the failure and suspect shipping the unit back could void coverage without guaranteeing a fix.【F:data/vesc_help_group/text_slices/input_part002.txt†L15274-L15294】【F:data/vesc_help_group/text_slices/input_part002.txt†L15320-L15331】

### ANT BMS Android Tooling
- Konstantin distributed the latest ANT mobile resources (user guide plus `mybms_v1.3.0_20211116.apk`) after VBMS stopped working, giving Android users a sideloadable option for configuring new boards.【F:data/vesc_help_group/text_slices/input_part002.txt†L15096-L15104】

### Cooling Experiments & Case Contact Lessons
- Happy Giraffe reminded single-uBox owners that only the upper shell touches the MOSFETs, so flipping the case and using thermal paste matters more than polishing the base; extra blocks without contact do little.【F:data/vesc_help_group/text_slices/input_part002.txt†L14824-L14828】
- Others are stacking 500 g aluminium slabs, vapor chambers, and even external radiators onto Uboxes and Tronics to chase 400 A bursts, while acknowledging the hand-soldered construction still limits reliability.【F:data/vesc_help_group/text_slices/input_part002.txt†L14932-L14941】【F:data/vesc_help_group/text_slices/input_part002.txt†L15296-L15324】

### Geared Hub & Brake Orientation Debates
- Happy Giraffe pitched Grin’s GMAC geared hub as a commuter upgrade: light unsprung mass, integrated torque arm, silent nylon gears, and strong regen at ≤80 A battery thanks to the planetary reduction.【F:data/vesc_help_group/text_slices/input_part002.txt†L15335-L15372】
- Vsett riders worry their right-side Magura calipers put the branded “lip” into the airflow; no one has proven a performance loss yet, but several consider swapping swingarms or banjo fittings to restore the standard rear-facing orientation for better cooling.【F:data/vesc_help_group/text_slices/input_part002.txt†L15380-L15490】

### Dualtron Adapter & Pad Maintenance Notes
- Dualtron owners are using the Carbonrevo adapter to push Magura calipers outward so the body clears wide tires while converting the stock 44 mm rotor bolt pattern to the 48 mm standard, often paired with a banjo swap that moves the hose to the opposite side for clearance.【F:data/vesc_help_group/text_slices/input_part002.txt†L15504-L15545】
- D170S sintered pads continue to be the wet-weather favourite; riders credit straight-line 30 → 0 km/h repeats (20–30 cycles per brake) for bedding them in and note that spraying water over noisy pads mainly flushes contamination rather than adding true bite.【F:data/vesc_help_group/text_slices/input_part002.txt†L15528-L15561】
- For mechanical setups, the TRP Spyke dual-piston caliper remains the go-to upgrade and can share Xiaomi-style brake levers with e-brake switches for commuters chasing simple maintenance.【F:data/vesc_help_group/text_slices/input_part002.txt†L15571-L15579】

### Battery Handling Mishaps & High-Current Targets
- A dropped Nordbot 13 S pack lost an entire parallel pair, forcing a downgrade to 12 S and highlighting why dense wraps, cell insulators, and cautious transport matter even after a pack survives 65 A delta-mod pulls.【F:data/vesc_help_group/text_slices/input_part002.txt†L15601-L15619】
- Builders chasing 450 A controllers report 250 A hardware running too hot, so they are speccing larger MOSFET stages, 20 S6 P 40T packs, and high-current connectors such as HXT8 to survive 260 A bursts without melting harnesses.【F:data/vesc_help_group/text_slices/input_part002.txt†L15704-L15839】

### Copper Busbar & Pack Layout Guidance
- Spot welders warned that bridging 16 S8 P packs with only two cells in series throttles current and overheats the interconnect; adding multiple jumpers or second-layer plates spreads load so each parallel group discharges evenly.【F:data/vesc_help_group/text_slices/input_part002.txt†L15901-L15938】
- Best practice is to solder main leads to copper before welding, fold the strip over as a doubled busbar, cover as many cell tops as possible, and insulate with fish paper or Kapton before closing the pack—steps now being relayed to new K-weld adopters.【F:data/vesc_help_group/text_slices/input_part002.txt†L15955-L16033】

### Active Balancer Field Experience
- JK’s smart BMS is confirmed at 150 A continuous, 300 A peak with a 1 A active balancer that keeps packs within 0.001 V after 100+ days, though the unit is physically large compared to ANT boards despite the latter’s lauded harness quality and app support.【F:data/vesc_help_group/text_slices/input_part002.txt†L16102-L16113】【F:data/vesc_help_group/text_slices/input_part002.txt†L16107-L16108】

### Horn & Alarm Hardware
- Riders comparing horns landed on USB‑C rechargeable units that double as motion alarms, while laughing at 328 dB marketing claims—physics caps airborne sound around 194 dB, so expect loud but not world-ending output.【F:data/vesc_help_group/text_slices/input_part002.txt†L16127-L16154】

### Spintend Firmware 6.0 Support Update
- Spintend’s engineer confirmed uBox hardware is now merged into stock VESC FW 6.0, eliminating the custom 5.3 branch and covering both the older micro-USB dual boards and newer USB‑C revisions.【F:data/vesc_help_group/text_slices/input_part002.txt†L16156-L16179】

### High-Current BMS & Cooling Debates
- Konstantin showcased a 220 A-rated BMS using −2 AWG leads for multi-motor scooters, sparking discussion about integrating controllers into sealed heatsink enclosures so MOSFETs see direct airflow rather than isolated aluminium blocks.【F:data/vesc_help_group/text_slices/input_part002.txt†L16181-L16258】
- Rosheee is pursuing a vapor-chamber spacer with 30 cm heatpipes inside a G30 deck, while peers stress that every extra interface adds thermal resistance and that direct MOSFET-to-case contact still wins for sustained climbs.【F:data/vesc_help_group/text_slices/input_part002.txt†L16819-L17000】

### Blade Split Rims & Wheel Service
- Some Blade-style split rims refuse to separate because the cover wasn’t drilled or the hub shoulder binds; technicians recommend sourcing 12 mm washers/nuts for the 110–112 mm axle spread and checking for manufacturing defects before resorting to full motor tear-downs.【F:data/vesc_help_group/text_slices/input_part002.txt†L16275-L16315】

### Ferrofluid Service & Torque Sensor Prep
- Ferrofluid can be injected with the wheel assembled—the magnets wick it into the gap—and upcoming torque-sensor installs may require bonding the bike frame to ground through a fused (≈100 mA) strap to tame EMI.【F:data/vesc_help_group/text_slices/input_part002.txt†L16455-L16465】

### G30 Build Planning & Battery Mounts
- Rosheee is keeping the 16 S5 P pack in his G30 until a 20 S6 P replacement arrives and confirmed that the 17 S holder STL came from Tudor, so other builders will need to request that print if they plan similar upgrades.【F:data/vesc_help_group/text_slices/input_part002.txt†L16466-L16495】

### Nucular Controller Availability & Mounting
- Nucular 24F controllers remain scarce but second-hand units run 500 A phase / 300 A battery without overheating when mounted externally; potted cases stay waterproof, so riders are urged to embrace external mounting instead of burying them beside hot packs.【F:data/vesc_help_group/text_slices/input_part002.txt†L16538-L16579】

### Tronic Warranty & QC Concerns
- Frustrated Tronic owners are threatening chargebacks after weeks without replacement boards, documenting burnt MOSFETs, inconsistent soldering between units, and reminders that swapping QS8 connectors can void warranty claims.【F:data/vesc_help_group/text_slices/input_part002.txt†L16501-L16678】【F:data/vesc_help_group/text_slices/input_part002.txt†L16796-L16811】

### Magura Install Hacks & Aftermarket Parts
- Magura MT5 single-pad kits ship without pad screws, so riders are trimming M4×25 mm bolts to suit, and Jagwire’s Hyflow + Hope quick-connect kit supplies sealed M6/M5 washers that relocate the banjo to the outer face—critical for tight decks like the Ninebot G30 where only a few millimetres separate caliper and tyre.【F:data/vesc_help_group/text_slices/input_part002.txt†L16718-L16788】【F:data/vesc_help_group/text_slices/input_part002.txt†L16729-L16755】

### Vapor-Chamber Controller Cooling Trials
- Rosheee is testing a G30 deck rebuild that sandwiches the uBox controller against springs, thermal pads, a vapor chamber, and long heatpipes tied into an aluminium spacer so forced airflow shoots straight across the hottest MOSFET pairs.【F:data/vesc_help_group/text_slices/input_part002.txt†L17000-L17035】
- Follow-up rides show the ducted path keeping the controller cold but shifting most heat into the battery plate, so the team is weighing whether low-cost heatpipes could rupture and make things worse despite the gains.【F:data/vesc_help_group/text_slices/input_part002.txt†L17025-L17055】【F:data/vesc_help_group/text_slices/input_part002.txt†L18464-L18488】

### PETG Print Tuning & Enclosure Workflows
- Artem finally dialed PETG stringing down after ~€300 of tweaks, now pushing 0.3 mm layers at 0.4 mm width and ~140 mm/s (≈14 mm³/s), and reports that fast two-day roll turnover avoids the need for filament drying on the current tooling.【F:data/vesc_help_group/text_slices/input_part002.txt†L17040-L17055】【F:data/vesc_help_group/text_slices/input_part002.txt†L17104-L17107】

### Burned Motorcycle Conversion Blueprint
- Francois sourced a €600 fire-damaged donor bike with intact chassis and plans to gut the fuel tank for LiFePO₄ or Tesla 5 S modules (≈5 kW each) that can be water-cooled, noting Belgian homologation hurdles and the need for cross-border paperwork to legalize the electric swap.【F:data/vesc_help_group/text_slices/input_part002.txt†L17066-L17087】

### Blade/Achilleus Frame & Hardware Feedback
- Blade axles can ship in either M12×1.25 or M14×1.5 threads depending on batch, so owners are double-checking hardware mixes, while Paolo confirms he’ll lock the hinge solid on his donor chassis to avoid wobble.【F:data/vesc_help_group/text_slices/input_part002.txt†L17100-L17137】
- Retail technicians describe the Achilleus frame as larger than a Thunder but still prone to wobble unless the hinge is overtightened; Speedtrott hinges rarely fail, yet the smaller 40 mm motors were a weak point on those scooters.【F:data/vesc_help_group/text_slices/input_part002.txt†L17114-L17147】

### Magura Brake Upgrade Field Notes
- Riders praise MT5/MT7 calipers paired with Kool Stop sintered pads and Magura MDR-C 2 mm rotors for “crazy” bite, noting the HC3-style bite-point knob on MT7 levers eliminates hex tools and lets them tune on the trail.【F:data/vesc_help_group/text_slices/input_part002.txt†L17154-L17243】
- The Hope/Jagwire banjo kit supplies all necessary washers except an M6×20 mm banjo bolt, and builders recommend reinforcing lines with steel-braided “fuckeria” hoses for track use after boiling Shimano rotors and experiencing brake fade at an estimated 350–450 °C fluid temperature.【F:data/vesc_help_group/text_slices/input_part002.txt†L17178-L17275】

### High-Power Vsett vs Dualtron Tuning
- Vsett 10 owners are running 75/195 A rear and 70/125 A front (battery/phase) on 20 S packs, logging 175 °F winding temps and strong traction thanks to stiff 1800/2000 lb springs, while Rosheee’s 16 S G30 stays under 80 °C even at ~9–11 kW because the scooter weighs ~20 kg less.【F:data/vesc_help_group/text_slices/input_part002.txt†L17303-L17455】【F:data/vesc_help_group/text_slices/input_part002.txt†L17375-L17405】
- Both teams agree traction hinges on tyre pressure (≈40 psi PMT E-Fire vs lower slick pressures) and that temp sensors plus field-weakening management are mandatory before trying 14 kW speed runs on 20 S with 2×90 A battery limits.【F:data/vesc_help_group/text_slices/input_part002.txt†L17413-L17475】

### Motor Temperature Monitoring & Service Tips
- Installing 100 kΩ (B3950) NTC probes is as simple as tying one lead to hall ground and the other to the VESC temp input, but routing the extra wire through the axle is tricky unless you swap to a Higo L1019 harness with 3×11 AWG phase cores and eight signal pins.【F:data/vesc_help_group/text_slices/input_part002.txt†L17487-L17501】
- Stuck hub bearings often need a proper puller; improvised cuts on the axle shoulder risk permanent damage, so riders shared puller photos and warned rusted races won’t slide off without the right tool.【F:data/vesc_help_group/text_slices/input_part002.txt†L17502-L17534】

### Ferrofluid & Motor Cooling Mods
- Fresh ferrofluid fills (≈10–12 mL) made motor covers noticeably warmer after just a five-minute ride, confirming better heat transfer, but veterans stressed scooter hubs only need ~5 mL and must be resealed with silicone to stop leaks.【F:data/vesc_help_group/text_slices/input_part002.txt†L17545-L17562】【F:data/vesc_help_group/text_slices/input_part002.txt†L18000-L18025】
- Riders are debating aftermarket cooling aids—from €100 Turbinators hub sinks to custom CNC fins inspired by Ghost_911’s Inokim OX—to keep 200 A phase builds alive without paying for new motors.【F:data/vesc_help_group/text_slices/input_part002.txt†L17693-L17712】【F:data/vesc_help_group/text_slices/input_part002.txt†L18255-L18308】

### Battery Packaging & Shrink Wrap Practices
- Packing experts now double-layer shrink wrap (mixing lighter “Albert” sleeves with thicker “Denis” stock) and add intermediate padding so balance leads don’t abrade during shipping; hair dryers work in a pinch but a heat gun gives cleaner seams.【F:data/vesc_help_group/text_slices/input_part002.txt†L17563-L17589】
- Artem reminds builders that packs should never move in the enclosure—if shrink is wearing through, it indicates poor clamping rather than bad material.【F:data/vesc_help_group/text_slices/input_part002.txt†L17603-L17609】

### Phase vs Battery Current Guidance
- Mirono and Happy Giraffe reiterated that phase amps spike at low speed for torque, but BMS stress comes from battery current, so it’s possible (though unwise) to run 150 A phase with only 10 A battery, and phase watts will always trail battery watts after controller losses.【F:data/vesc_help_group/text_slices/input_part002.txt†L17616-L17630】【F:data/vesc_help_group/text_slices/input_part002.txt†L18235-L18248】

### Rotor Adapter & Torque-Arm Troubleshooting
- A 203 mm adapter on Mirono’s ebike left the caliper too high because the axle wasn’t fully seated; even dual torque arms couldn’t stop the wheel from popping out when the frame was tilted, so Happy Giraffe recommended custom-fabbed arms that sit flush on the dropout before torqueing.【F:data/vesc_help_group/text_slices/input_part002.txt†L17631-L17682】

### Electric Motorcycle Range & Aerodynamics Planning
- Converting a 20 kWh, 20 S motorcycle for 100 km/h cruising could yield ~350 km range if aerodynamics are optimized, and the group stressed that a 15 kWh pack with a fairing may outlast a 20 kWh brick on open roads.【F:data/vesc_help_group/text_slices/input_part002.txt†L17960-L17983】
- Riders also discussed relocating seats and accessories to cut drag and revisited lithium grease vs other lubricants for easy-to-clean finishes after full rebuilds.【F:data/vesc_help_group/text_slices/input_part002.txt†L17984-L18045】

### Slack Core Frame Review
- Artem praised the Slack Core scooter’s forged-aluminium neck geometry but flagged a thin lower joint that will crack under a 100 kg rider unless reinforced, urging the team to revisit titanium usage and load paths before production.【F:data/vesc_help_group/text_slices/input_part002.txt†L18046-L18124】

### Monorim AWD Conversion & Pack Sizing Advice
- Converting a Monorim front end to accept Blade 10" hubs requires flipping the suspension sides, fitting longer axles with washer stacks, or carefully bending 16 mm per arm; dual motors need at least 6 P of Samsung 50E/50G cells or stronger to safely feed 40 A battery per wheel.【F:data/vesc_help_group/text_slices/input_part002.txt†L18055-L18109】
- Daly 60–80 A BMS units can cover short 180 A peaks in 5 P packs, but Rosheee urged builders to go 6 P if the controller must live inside the deck and to remember that 50E cells are marginal for Blade-class torque without copper bus reinforcement.【F:data/vesc_help_group/text_slices/input_part002.txt†L18088-L18108】【F:data/vesc_help_group/text_slices/input_part002.txt†L18123-L18144】

### Cell Selection & Availability Debate
- Artem still recommends P42A-class cells for 25 A-per-cell builds, rating Samsung 48X as only a slight upgrade over 50G and highlighting M50LT Gen 2 for 0–15 A commuter packs, while others chase scarce 50E/Molicel stock across Europe.【F:data/vesc_help_group/text_slices/input_part002.txt†L18123-L18224】
- A 20 S9P Samsung 48X pack costs about $5.75 per cell delivered from Canada, supports 150 A bursts (~17.2 A/cell), and returns 40–80 mile range depending on riding style—underscoring the trade-offs between amp headroom and Wh/€ compared with cheaper Molicels.【F:data/vesc_help_group/text_slices/input_part002.txt†L17924-L17948】

### Bearing Choices & Heat Management
- For high-speed scooter hubs, riders prefer 2RS seals as a balance between protection and rolling resistance; ZZ offers the least drag but no sealing, while RSH adds drag with little benefit, and overheated Vsett bearings after 17 000 km suggest timely swaps.【F:data/vesc_help_group/text_slices/input_part002.txt†L18111-L18234】

### Motor Cooling Hardware Experiments
- Builders are prototyping long aluminium heatsinks, CNC motor collars, and even industrial CNC-made fins to rival Grin’s hubsinks, debating FalconPEV high-speed motors (potentially different windings such as 17×4 vs 33×2) and whether higher-Kv options actually run cooler under the same current.【F:data/vesc_help_group/text_slices/input_part002.txt†L18255-L18333】
- QS Motor’s 10"–17" hub lineup (4000 W–12 000 W) plus Kelly KLS controllers with six hall sensors remain the aspirational benchmark for multi-kilowatt scooter conversions despite €1 000 price tags.【F:data/vesc_help_group/text_slices/input_part002.txt†L18317-L18346】

### Chemistry & Charging Considerations
- Lipoly pouch packs promise huge C-rates but introduce mounting, wiring, and charging headaches because most hobby chargers top out at 6–7 S, forcing riders to break series links each charge; even with a BMS, puncture risk makes 20 kg RC packs a hard sell versus cylindrical Li-ion or LiFePO₄ bricks.【F:data/vesc_help_group/text_slices/input_part002.txt†L18407-L18421】
- Lifepo₄ packs stay attractive for crash resilience in motorcycles, yet riders still compare Wh/L penalties against Samsung 48X or similar Li-ion cells before locking in a chemistry.【F:data/vesc_help_group/text_slices/input_part002.txt†L18405-L18421】

### Controller Heat Measurement Cautions
- Happy Giraffe cautions that heat-sink surface probes on a uBox don’t reflect MOSFET junction temps, so builders shouldn’t draw conclusions from plate readings alone; Rosheee now treats the battery as the primary heat source and logs VESC telemetry instead of chasing heat-sink deltas.【F:data/vesc_help_group/text_slices/input_part002.txt†L18427-L18488】


### Vapor-Chamber Controller Cooling Trials
- Rosheee is testing a G30 deck rebuild that sandwiches the uBox controller against springs, thermal pads, a vapor chamber, and long heatpipes tied into an aluminium spacer so forced airflow shoots straight across the hottest MOSFET pairs.【F:data/vesc_help_group/text_slices/input_part002.txt†L17000-L17035】
- Follow-up rides show the ducted path keeping the controller cold but shifting most heat into the battery plate, so the team is weighing whether low-cost heatpipes could rupture and make things worse despite the gains.【F:data/vesc_help_group/text_slices/input_part002.txt†L17025-L17055】【F:data/vesc_help_group/text_slices/input_part002.txt†L18464-L18488】

### PETG Print Tuning & Enclosure Workflows
- Artem finally dialed PETG stringing down after ~€300 of tweaks, now pushing 0.3 mm layers at 0.4 mm width and ~140 mm/s (≈14 mm³/s), and reports that fast two-day roll turnover avoids the need for filament drying on the current tooling.【F:data/vesc_help_group/text_slices/input_part002.txt†L17040-L17055】【F:data/vesc_help_group/text_slices/input_part002.txt†L17104-L17107】

### Burned Motorcycle Conversion Blueprint
- Francois sourced a €600 fire-damaged donor bike with intact chassis and plans to gut the fuel tank for LiFePO₄ or Tesla 5 S modules (≈5 kW each) that can be water-cooled, noting Belgian homologation hurdles and the need for cross-border paperwork to legalize the electric swap.【F:data/vesc_help_group/text_slices/input_part002.txt†L17066-L17087】

### Blade/Achilleus Frame & Hardware Feedback
- Blade axles can ship in either M12×1.25 or M14×1.5 threads depending on batch, so owners are double-checking hardware mixes, while Paolo confirms he’ll lock the hinge solid on his donor chassis to avoid wobble.【F:data/vesc_help_group/text_slices/input_part002.txt†L17100-L17137】
- Retail technicians describe the Achilleus frame as larger than a Thunder but still prone to wobble unless the hinge is overtightened; Speedtrott hinges rarely fail, yet the smaller 40 mm motors were a weak point on those scooters.【F:data/vesc_help_group/text_slices/input_part002.txt†L17114-L17147】

### Magura Brake Upgrade Field Notes
- Riders praise MT5/MT7 calipers paired with Kool Stop sintered pads and Magura MDR-C 2 mm rotors for “crazy” bite, noting the HC3-style bite-point knob on MT7 levers eliminates hex tools and lets them tune on the trail.【F:data/vesc_help_group/text_slices/input_part002.txt†L17154-L17243】
- The Hope/Jagwire banjo kit supplies all necessary washers except an M6×20 mm banjo bolt, and builders recommend reinforcing lines with steel-braided “fuckeria” hoses for track use after boiling Shimano rotors and experiencing brake fade at an estimated 350–450 °C fluid temperature.【F:data/vesc_help_group/text_slices/input_part002.txt†L17178-L17275】

### High-Power Vsett vs Dualtron Tuning
- Vsett 10 owners are running 75/195 A rear and 70/125 A front (battery/phase) on 20 S packs, logging 175 °F winding temps and strong traction thanks to stiff 1800/2000 lb springs, while Rosheee’s 16 S G30 stays under 80 °C even at ~9–11 kW because the scooter weighs ~20 kg less.【F:data/vesc_help_group/text_slices/input_part002.txt†L17303-L17455】【F:data/vesc_help_group/text_slices/input_part002.txt†L17375-L17405】
- Both teams agree traction hinges on tyre pressure (≈40 psi PMT E-Fire vs lower slick pressures) and that temp sensors plus field-weakening management are mandatory before trying 14 kW speed runs on 20 S with 2×90 A battery limits.【F:data/vesc_help_group/text_slices/input_part002.txt†L17413-L17475】

### Motor Temperature Monitoring & Service Tips
- Installing 100 kΩ (B3950) NTC probes is as simple as tying one lead to hall ground and the other to the VESC temp input, but routing the extra wire through the axle is tricky unless you swap to a Higo L1019 harness with 3×11 AWG phase cores and eight signal pins.【F:data/vesc_help_group/text_slices/input_part002.txt†L17487-L17501】
- Stuck hub bearings often need a proper puller; improvised cuts on the axle shoulder risk permanent damage, so riders shared puller photos and warned rusted races won’t slide off without the right tool.【F:data/vesc_help_group/text_slices/input_part002.txt†L17502-L17534】

### Ferrofluid & Motor Cooling Mods
- Fresh ferrofluid fills (≈10–12 mL) made motor covers noticeably warmer after just a five-minute ride, confirming better heat transfer, but veterans stressed scooter hubs only need ~5 mL and must be resealed with silicone to stop leaks.【F:data/vesc_help_group/text_slices/input_part002.txt†L17545-L17562】【F:data/vesc_help_group/text_slices/input_part002.txt†L18000-L18025】
- Riders are debating aftermarket cooling aids—from €100 Turbinators hub sinks to custom CNC fins inspired by Ghost_911’s Inokim OX—to keep 200 A phase builds alive without paying for new motors.【F:data/vesc_help_group/text_slices/input_part002.txt†L17693-L17712】【F:data/vesc_help_group/text_slices/input_part002.txt†L18255-L18308】

### Battery Packaging & Shrink Wrap Practices
- Packing experts now double-layer shrink wrap (mixing lighter “Albert” sleeves with thicker “Denis” stock) and add intermediate padding so balance leads don’t abrade during shipping; hair dryers work in a pinch but a heat gun gives cleaner seams.【F:data/vesc_help_group/text_slices/input_part002.txt†L17563-L17589】
- Artem reminds builders that packs should never move in the enclosure—if shrink is wearing through, it indicates poor clamping rather than bad material.【F:data/vesc_help_group/text_slices/input_part002.txt†L17603-L17609】

### Phase vs Battery Current Guidance
- Mirono and Happy Giraffe reiterated that phase amps spike at low speed for torque, but BMS stress comes from battery current, so it’s possible (though unwise) to run 150 A phase with only 10 A battery, and phase watts will always trail battery watts after controller losses.【F:data/vesc_help_group/text_slices/input_part002.txt†L17616-L17630】【F:data/vesc_help_group/text_slices/input_part002.txt†L18235-L18248】

### Rotor Adapter & Torque-Arm Troubleshooting
- A 203 mm adapter on Mirono’s ebike left the caliper too high because the axle wasn’t fully seated; even dual torque arms couldn’t stop the wheel from popping out when the frame was tilted, so Happy Giraffe recommended custom-fabbed arms that sit flush on the dropout before torqueing.【F:data/vesc_help_group/text_slices/input_part002.txt†L17631-L17682】

### Electric Motorcycle Range & Aerodynamics Planning
- Converting a 20 kWh, 20 S motorcycle for 100 km/h cruising could yield ~350 km range if aerodynamics are optimized, and the group stressed that a 15 kWh pack with a fairing may outlast a 20 kWh brick on open roads.【F:data/vesc_help_group/text_slices/input_part002.txt†L17960-L17983】
- Riders also discussed relocating seats and accessories to cut drag and revisited lithium grease vs other lubricants for easy-to-clean finishes after full rebuilds.【F:data/vesc_help_group/text_slices/input_part002.txt†L17984-L18045】

### Slack Core Frame Review
- Artem praised the Slack Core scooter’s forged-aluminium neck geometry but flagged a thin lower joint that will crack under a 100 kg rider unless reinforced, urging the team to revisit titanium usage and load paths before production.【F:data/vesc_help_group/text_slices/input_part002.txt†L18046-L18124】

### Monorim AWD Conversion & Pack Sizing Advice
- Converting a Monorim front end to accept Blade 10" hubs requires flipping the suspension sides, fitting longer axles with washer stacks, or carefully bending 16 mm per arm; dual motors need at least 6 P of Samsung 50E/50G cells or stronger to safely feed 40 A battery per wheel.【F:data/vesc_help_group/text_slices/input_part002.txt†L18055-L18109】
- Daly 60–80 A BMS units can cover short 180 A peaks in 5 P packs, but Rosheee urged builders to go 6 P if the controller must live inside the deck and to remember that 50E cells are marginal for Blade-class torque without copper bus reinforcement.【F:data/vesc_help_group/text_slices/input_part002.txt†L18088-L18108】【F:data/vesc_help_group/text_slices/input_part002.txt†L18123-L18144】

### Cell Selection & Availability Debate
- Artem still recommends P42A-class cells for 25 A-per-cell builds, rating Samsung 48X as only a slight upgrade over 50G and highlighting M50LT Gen 2 for 0–15 A commuter packs, while others chase scarce 50E/Molicel stock across Europe.【F:data/vesc_help_group/text_slices/input_part002.txt†L18123-L18224】
- A 20 S9P Samsung 48X pack costs about $5.75 per cell delivered from Canada, supports 150 A bursts (~17.2 A/cell), and returns 40–80 mile range depending on riding style—underscoring the trade-offs between amp headroom and Wh/€ compared with cheaper Molicels.【F:data/vesc_help_group/text_slices/input_part002.txt†L17924-L17948】

### Bearing Choices & Heat Management
- For high-speed scooter hubs, riders prefer 2RS seals as a balance between protection and rolling resistance; ZZ offers the least drag but no sealing, while RSH adds drag with little benefit, and overheated Vsett bearings after 17 000 km suggest timely swaps.【F:data/vesc_help_group/text_slices/input_part002.txt†L18111-L18234】

### Motor Cooling Hardware Experiments
- Builders are prototyping long aluminium heatsinks, CNC motor collars, and even industrial CNC-made fins to rival Grin’s hubsinks, debating FalconPEV high-speed motors (potentially different windings such as 17×4 vs 33×2) and whether higher-Kv options actually run cooler under the same current.【F:data/vesc_help_group/text_slices/input_part002.txt†L18255-L18333】
- QS Motor’s 10"–17" hub lineup (4000 W–12 000 W) plus Kelly KLS controllers with six hall sensors remain the aspirational benchmark for multi-kilowatt scooter conversions despite €1 000 price tags.【F:data/vesc_help_group/text_slices/input_part002.txt†L18317-L18346】

### Chemistry & Charging Considerations
- Lipoly pouch packs promise huge C-rates but introduce mounting, wiring, and charging headaches because most hobby chargers top out at 6–7 S, forcing riders to break series links each charge; even with a BMS, puncture risk makes 20 kg RC packs a hard sell versus cylindrical Li-ion or LiFePO₄ bricks.【F:data/vesc_help_group/text_slices/input_part002.txt†L18407-L18421】
- Lifepo₄ packs stay attractive for crash resilience in motorcycles, yet riders still compare Wh/L penalties against Samsung 48X or similar Li-ion cells before locking in a chemistry.【F:data/vesc_help_group/text_slices/input_part002.txt†L18405-L18421】

### Controller Heat Measurement Cautions
- Happy Giraffe cautions that heat-sink surface probes on a uBox don’t reflect MOSFET junction temps, so builders shouldn’t draw conclusions from plate readings alone; Rosheee now treats the battery as the primary heat source and logs VESC telemetry instead of chasing heat-sink deltas.【F:data/vesc_help_group/text_slices/input_part002.txt†L18427-L18488】

### Magura Brake Hardware & Setup Updates
- Riders comparing pad compounds found Kool Stop sintered pads deliver immediate bite with minimal noise on 1.91 mm rotors, whereas full-metal sets stay loud until heated and chew through thin discs quickly.【F:data/vesc_help_group/text_slices/input_part002.txt†L18501-L18540】
- Storm HC rotors measure about 1.9 mm new and get swapped near 1.8 mm; the crew weighed MDR-C 160 mm, MDR-P 180 mm, and Trickstuff 2.05 mm options to add thermal mass when squeezing MT5 calipers into cramped scooter forks.【F:data/vesc_help_group/text_slices/input_part002.txt†L19214-L19415】
- To stop thicker rotors with Kool Stop pads from rubbing, riders set Magura reach adjusters fully out, bleed with the supplied piston blocks while holding the caliper above the lever as they close ports, and align by eye rather than clamping the lever shut.【F:data/vesc_help_group/text_slices/input_part002.txt†L19418-L19505】
- Logan four-piston calipers on NAMI scooters deliver stopping power on par with Magura MT units, so owners only swap if they prefer Magura lever feel or pad choices.【F:data/vesc_help_group/text_slices/input_part002.txt†L19882-L19887】

### Hub Cooling & Ferrofluid Management
- Stick-on heatsinks and leftover thermal pads on hub shells proved ineffective; scooter tyres block ebike-focused Turbinators, so purpose-made hubsinks with firm clamping and paste remain the only reliable add-on cooling option.【F:data/vesc_help_group/text_slices/input_part002.txt†L18600-L18635】
- Artem reiterated that 6.1" × 50 mm hubs need roughly 6–7 mL of ferrofluid per motor, while 3 mL underfills the gap and 10 mL adds drag and elevates controller temps, leaving 5–7 mL as the sweet spot.【F:data/vesc_help_group/text_slices/input_part002.txt†L19091-L19091】【F:data/vesc_help_group/text_slices/input_part002.txt†L19846-L19861】
- Builders seal covers with silicone, inspect for rust, and stock 100 mL bottles (Grin Tech or Nexun.pl) so they can top off leaks without drilling vent holes.【F:data/vesc_help_group/text_slices/input_part002.txt†L18993-L19004】【F:data/vesc_help_group/text_slices/input_part002.txt†L19864-L19879】

### Battery & Enclosure Fabrication Lessons
- Artem squeezed a 60 V 30 Ah 21700 pack into a Vsett 9 by interlocking dual 5 mm aluminium rods and tuning PETG prints to ±0.05 mm on circular features, keeping mass centred in the deck.【F:data/vesc_help_group/text_slices/input_part002.txt†L18687-L18696】
- Smooth PEI beds bond too aggressively to PETG; bumping Z offset by 0.1 mm or printing on glass, textured PEI, FR4, or glue-stick barriers prevents ripping the coating when producing scooter enclosures.【F:data/vesc_help_group/text_slices/input_part002.txt†L19661-L19664】
- Vsett pack builders confirmed the deck rails must be removed entirely to fit longer bricks instead of trimming cells to nestle inside the stock channels.【F:data/vesc_help_group/text_slices/input_part002.txt†L19667-L19682】

### Controller Thermal Management & Charging
- Potting a Ubox with thermally conductive compound drops internal temperatures by about 30 % by coupling the PCB to the housing, though Paolo notes FR4 boards still bottleneck heat compared with unobtainable aluminium cores.【F:data/vesc_help_group/text_slices/input_part002.txt†L19733-L19749】
- For DIY waterproofing, riders favour resin potting compounds that flow through gaps and improve thermal conductivity better than silicone when protecting controllers.【F:data/vesc_help_group/text_slices/input_part002.txt†L19670-L19678】
- Nucular owners rely on the charge-through-phase feature: a 56 V, 2 kW server PSU on 120 V mains yields roughly 15 A, and any source below pack voltage—from spare scooter batteries to EV posts—can top up via the controller.【F:data/vesc_help_group/text_slices/input_part002.txt†L19957-L20000】

### Display & Control Integrations
- Artem shared an open-source TTGO T-Display dashboard for ESP32/RP2040 variants that parses VESC telemetry over BLE, giving scooters a configurable wireless cluster.【F:data/vesc_help_group/text_slices/input_part002.txt†L18713-L18727】
- Xiaomi’s BLE display keeps stock-style modes, telemetry, and VESC Tool access when paired with a separate Bluetooth module, making it a drop-in option for stealth builds.【F:data/vesc_help_group/text_slices/input_part002.txt†L19188-L19193】
- Spintend’s ADC adapter offers switchable 5 V/3.3 V outputs and filtering; veterans suggest buying direct for warranty support and note Spintend’s LCD throttle can bypass the board where convenient.【F:data/vesc_help_group/text_slices/input_part002.txt†L19972-L19990】

### Build Planning & Component Selection
- Mirko’s G30 dual-motor plan pairs a 16S6P VTC6A pack with dual Uboxes, targeting ~70 A rear/55 A front battery current and 135 A phase per side while warning that 90 A battery current overheats a single Ubox; ferrofluid keeps Blade motors alive, and shell IR readings remain misleading.【F:data/vesc_help_group/text_slices/input_part002.txt†L18811-L18929】
- Existing Vsett 10+ logs show 80 A battery and 225 A phase on the rear motor holding below ~185 °F when 6–7 mL of ferrofluid is present.【F:data/vesc_help_group/text_slices/input_part002.txt†L18872-L18882】
- The crew stocks 100 mL ferrofluid bottles, prefers Nexun’s EU supply to avoid Canadian import delays, and feeds the fluid through magnet gaps instead of drilling ports.【F:data/vesc_help_group/text_slices/input_part002.txt†L18993-L19004】
- Ninebot sleeper builds aimed at 40 km/h stay on 13 S packs with low-Kv Gen6 or FLJ rear motors, skipping suspension swaps unless comfort demands it at that speed.【F:data/vesc_help_group/text_slices/input_part002.txt†L19756-L19771】
- PMT tyre shoppers quoted €53–58 for Stradale sizes in Italy versus €48 plus €19 shipping from Fastride, with Paolo steering commuters toward the slightly softer Junior compound for grip without major range loss.【F:data/vesc_help_group/text_slices/input_part002.txt†L19775-L19804】
- SKF clarified that C3-clearance 2Z bearings leave extra race spacing for thermal expansion, making them suitable for racing hubs despite minimal sealing compared with 2RS options.【F:data/vesc_help_group/text_slices/input_part002.txt†L19835-L19839】
- Rosheee ordered ten open-hardware BESC PCBs alongside Goldenmotor Vector controllers to prototype higher-power VESC alternatives beyond the usual Kelly and Nucular lineup.【F:data/vesc_help_group/text_slices/input_part002.txt†L19648-L19657】

### Charging Practices & 50G Pack Stress Signals
- Daily riders treat slow charging as longevity insurance: 43.2 Ah packs sip 3 A overnight (~0.008 C), 6 P Molicel bricks stay under ~8 A, and Paolo reminds everyone that cell heat is the real killer even when the math suggests 0.2 C is “safe.”【F:data/vesc_help_group/text_slices/input_part002.txt†L20002-L20021】
- Rosheee’s 16S5P Samsung 50G experiment peaked at ~199 A battery current through a 60 A Daly BMS, underscoring how far builders are pushing 10–12 A-rated cells and why he is migrating to a 20S6P pack within weeks.【F:data/vesc_help_group/text_slices/input_part002.txt†L20685-L20700】

### Ferrofluid Application, Sealing & Bearing Service
- Artem’s recipe for 10″ hubs with 50 mm magnets is a measured 5–6 mL streaked between each pair of magnets; more than ~7 mL drags on spin-down, cuts torque, and can send uBox temperatures past 70 °C within minutes.【F:data/vesc_help_group/text_slices/input_part002.txt†L20094-L20116】【F:data/vesc_help_group/text_slices/input_part002.txt†L20543-L20579】
- Sealant matters: riders run a thin bead of RTV (Loctite-branded where available) around both motor cover seams, axle exits, and even screw heads after spotting ferrofluid weeping through unsealed threads.【F:data/vesc_help_group/text_slices/input_part002.txt†L20262-L20328】
- Updated Vsett 10+ service notes call for SKF 6202/6004 2RSH wheel bearings (prefer C3 clearance), 20×28×6 and 15×25×5 simmerings, 16287 2RS swingarm bearings, and 30×41×6.5 36°×45° headset bearings to banish the rusted metal-shield races seen on stock hardware.【F:data/vesc_help_group/text_slices/input_part002.txt†L20580-L20591】

### Controller Mounting & Heat-Sinking Material Choices
- Mount uBox v2s to solid aluminium plates instead of tucking them inside G30 decks: Mirko measured ≈10 °C higher temps when bolting to the steel footrest, while Paolo and Rosheee confirmed aluminium bottom plates and thermal paste beat in-frame mounting every time.【F:data/vesc_help_group/text_slices/input_part002.txt†L20212-L20235】【F:data/vesc_help_group/text_slices/input_part002.txt†L20520-L20542】
- Stainless “inox” slabs are a dead end for 75100 cooling—after breaking drill bits in a 2 kg plate, the group switched to 5 mm 6061 aluminium, considered adding heat pipes, and noted copper oxidises too quickly for exposed scooter builds.【F:data/vesc_help_group/text_slices/input_part002.txt†L20620-L20655】【F:data/vesc_help_group/text_slices/input_part002.txt†L20959-L20965】
- Rosheee’s deck-mounted clamp still relies on a 5 mm aluminium spreader, proving even casual testing hits 199 A battery draw and demanding real thermal mass rather than cosmetic covers.【F:data/vesc_help_group/text_slices/input_part002.txt†L20680-L20689】

### Magura Piston Maintenance & Bleeding Tips
- To stop persistent rotor rub on MT5/MT7 calipers, Adam now removes the bleed blocks, pushes all four pistons out halfway with a syringe, lubricates the seals with fresh mineral oil, and centres the caliper before the first lever pull so the pistons settle evenly.【F:data/vesc_help_group/text_slices/input_part002.txt†L20741-L20809】
- Magura stock Royal Blood boils near 120 °C, so Paolo reserves Shimano or Brembo mineral oil for repeated 100 → 0 km/h stops and watches rotor temps climb past 110 °C even on flat routes.【F:data/vesc_help_group/text_slices/input_part002.txt†L20728-L20753】

### Wiring, Connectors & Soldering Fixes
- JST-SM 3-pin leads from AliExpress match the uBox V2 harness, but builders insist on setting the Spintend ADC adapter to 5 V mode, routing every signal before applying pack voltage, and lowering motor autodetect amps if the defaults look aggressive.【F:data/vesc_help_group/text_slices/input_part002.txt†L20810-L20832】
- Factory Flipsky 75100 power leads arrived as near-cold joints; the crew now trims insulation so the wire bottoms out in the bullet, fully floods the cup with solder, and flattens the strands onto the PCB pad with ceramic tweezers before heat-shrinking.【F:data/vesc_help_group/text_slices/input_part002.txt†L21055-L21084】
- Dual Flipsky setups still rely on CAN: swap TX/RX if detection fails, and when limping on a single controller disconnect the slave’s CAN and battery leads (phases/halls can stay but full isolation is safer).【F:data/vesc_help_group/text_slices/input_part002.txt†L21442-L21487】

### Sensor Modes, HFI Updates & Firmware Recognition
- Mirono cured low-speed cogging by lowering the hall-to-sensorless switchover from 2 000 to ~1 200 ERPM—slow enough for Vsett hubs to keep sync—while others remind newcomers that halls usually drop out around 2 500 ERPM anyway.【F:data/vesc_help_group/text_slices/input_part002.txt†L21201-L21224】【F:data/vesc_help_group/text_slices/input_part002.txt†L21233-L21257】
- Vedder’s latest HFI refinements promise hall-less launches, already running on Xiaomi ESC ports, and Spintend uBox now shows up inside VESC Tool’s official hardware directory after the Onside Ring submission.【F:data/vesc_help_group/text_slices/input_part002.txt†L21212-L21411】
- Full sensorless starts still need a kick on 20 S setups, so riders add hall looms to legacy hubs and monitor firmware logs for “brbrbr” oscillations that hint at bad autodetected flux or inductance values.【F:data/vesc_help_group/text_slices/input_part002.txt†L21195-L21211】【F:data/vesc_help_group/text_slices/input_part002.txt†L21257-L21310】

### SmartDisplay Lighting Bus & OTA Features
- Francois’ CAN light board now drives 5 V/12 V front, rear, brake, and turn outputs and rides along every SmartDisplay OTA push, giving unified error feedback for Kelly and VESC installs.【F:data/vesc_help_group/text_slices/input_part002.txt†L24506-L24515】
- SmartDisplay writes configurable speed/phase limits over CAN or UART, exposes almost every setting through the display or iOS/Android apps, and ships Wi-Fi firmware updates; the beta batch is capped at 15 units for 300 € with assembly slated for August.【F:data/vesc_help_group/text_slices/input_part002.txt†L25099-L25145】【F:data/vesc_help_group/text_slices/input_part002.txt†L25176-L25182】

### uBox Battery Limits & Wiring Reality
- Dualtron riders trying 150 A battery per Ubox v2 found the controllers, 10 AWG leads, and XT150 connectors overheating or current-limiting, prompting the group to cap setups near 70–90 A per ESC despite stout 20 S packs.【F:data/vesc_help_group/text_slices/input_part002.txt†L24622-L24692】
- Oversized phase wires can short against axle exits; veterans stick with 11 AWG Higo looms that survive 80/225 A settings without cutting the insulation.【F:data/vesc_help_group/text_slices/input_part002.txt†L24711-L24715】

### Spintend Single-100 V Prototype & Thermal Plate Fix
- Spintend confirmed the red 75 V dual still uses its best FETs and teased a 66 × 83 × 29 mm single-100 V controller aimed at filling the supply gap while resale units circulate in the group.【F:data/vesc_help_group/text_slices/input_part002.txt†L25558-L25571】
- Early renders with a brass baseplate were scrapped after riders flagged its poor conductivity and galvanic corrosion risk; aluminium (or copper) heat spreaders are back on the table.【F:data/vesc_help_group/text_slices/input_part002.txt†L25573-L25595】

### Spin-Y Throttle Production & Customisation
- Artem approved the CNC Spin-Y throttle samples, plans first-week-of-August shipping, and smoothed the return spring with high-viscosity lubricant while targeting a lighter 4 g wheel revision.【F:data/vesc_help_group/text_slices/input_part002.txt†L25207-L25271】
- Most buyers voted for black housings with raw aluminium accents so they can anodize locally, yet renders now cover black, silver, red, and even orange combinations to satisfy custom colour requests.【F:data/vesc_help_group/text_slices/input_part002.txt†L25744-L25761】【F:data/vesc_help_group/text_slices/input_part002.txt†L25788-L25799】

### Conformal Coating & Potting Guidance
- MG Chemicals 422C silicone conformal coating earned top marks for waterproofing controllers so long as builders mask plugs and keep MOSFETs/MCUs bare for heat transfer before dunk tests.【F:data/vesc_help_group/text_slices/input_part002.txt†L25480-L25505】
- The crew still treats full potting as a double-edged sword—great for cooling and sealing, but brutal on repairs—so experiments stay on sacrificial hardware.【F:data/vesc_help_group/text_slices/input_part002.txt†L25482-L25489】

### Battery Fires & Smart BMS Safeguards
- Dejan’s storage-room blaze (likely started by a neighbour’s charger) reinforced the habit of charging scooters outside living spaces and leaning on smart BMS features such as over-charge, over-current, and staged over-voltage cut-offs.【F:data/vesc_help_group/text_slices/input_part002.txt†L25631-L25669】
- Artem still recommends Ant, LLT, and JK units for their protections and apps, while Konstantin warns that some models allow 180 A surges or enforce 2.8 V cut-offs—proof that every BMS needs validation before high-power duty.【F:data/vesc_help_group/text_slices/input_part002.txt†L25670-L25699】
- Follow-up teardown of Dejan’s Monorim pack highlighted how marginal 60 A BMS boards and thin 10 AWG leads overheat even when the FETs survive, motivating thicker wiring on replacements.【F:data/vesc_help_group/text_slices/input_part002.txt†L25701-L25719】

### High-Current VESC Roadmap
- Mirono spotted an 18-FET open-source VESC with 500 A shunts in testing—enticing budget-minded riders hunting for alternatives to scarce Nucular gear.【F:data/vesc_help_group/text_slices/input_part002.txt†L25526-L25530】

### Flipsky 75100 Failures & Clone Market
- Sudden BMS cut-outs continue to blow 75100 MOSFETs; Izuna now stocks HUASHUO HSP0076A spares, reflows factory solder joints, and reminds peers that battery amps above 120 A demand serious heatsinking.【F:data/vesc_help_group/text_slices/input_part002.txt†L25886-L25937】
- AliExpress “75100” clones mirror Flipsky layouts save for Rubycon capacitors, and once taxes land the price gap narrows to only a few euros.【F:data/vesc_help_group/text_slices/input_part002.txt†L25938-L25949】

### Thermal Imaging Calibration
- FLIR phone cameras need emissivity tweaks—black anodised aluminium reads well near ε ≈ 0.9, while polished copper sits near 0.04—otherwise scooter heat maps become meaningless.【F:data/vesc_help_group/text_slices/input_part002.txt†L25844-L25858】

## Follow-up Ideas
- Publish a Spintend SWD-diagnostics note documenting the 0.6 V VCC symptom and outlining when to request an RMA versus trying local repairs.【F:data/vesc_help_group/text_slices/input_part002.txt†L27519-L27520】
- Add a wiring cheat sheet that maps every JST family on the uBox harness so builders can order spares without guessing pin pitch or lock style.【F:data/vesc_help_group/text_slices/input_part002.txt†L27513-L27516】
- Benchmark VESC traction-control heat and power trade-offs on heavy dual-motor scooters to see if firmware curve tweaks are needed beyond the current proportional torque trim.【F:data/vesc_help_group/text_slices/input_part002.txt†L27535-L27557】
- Test ferrofluid-plus-ATF fill strategies (leak paths, drag, temp delta) before recommending liquid-cooling hybrids for hub motors.【F:data/vesc_help_group/text_slices/input_part002.txt†L27520-L27533】
- Review third-party regen dump boards (e.g., 10 A brake resistor modules) to show why they cannot absorb scooter-level regen and outline safer alternatives before riders spend money on them.【F:data/vesc_help_group/text_slices/input_part002.txt†L23156-L23163】
- Publish a SmartDisplay CAN lighting harness guide that covers the 5 V/12 V board outputs, OTA update chain, and how controller error codes propagate through the display.【F:data/vesc_help_group/text_slices/input_part002.txt†L24506-L24515】【F:data/vesc_help_group/text_slices/input_part002.txt†L25099-L25145】
- Document safe dual-Ubox wiring limits—battery/phase ceilings, 10 AWG lead upgrades, XT150 constraints, and phase-wire routing—to stop newcomers from dialling 150 A battery per controller.【F:data/vesc_help_group/text_slices/input_part002.txt†L24622-L24692】【F:data/vesc_help_group/text_slices/input_part002.txt†L24711-L24715】
- Summarise Spintend’s single-100 V prototype (dimensions, target use cases, thermal plate material changes) so buyers know what to expect when pre-orders open.【F:data/vesc_help_group/text_slices/input_part002.txt†L25558-L25595】
- Create a Spin-Y throttle install sheet that captures CNC vs. plastic options, lubrication tips, and colour/anodizing workflows before shipments start in August.【F:data/vesc_help_group/text_slices/input_part002.txt†L25207-L25271】【F:data/vesc_help_group/text_slices/input_part002.txt†L25744-L25799】
- Draft a conformal coating checklist (masking, cure schedule, post-test inspections) plus potting trade-offs for waterproofing controllers.【F:data/vesc_help_group/text_slices/input_part002.txt†L25480-L25505】
- Package the Dejan fire lessons into a BMS safety note covering smart-feature expectations, validation tests, and wiring upgrades for 60 A-class boards.【F:data/vesc_help_group/text_slices/input_part002.txt†L25631-L25719】
- Write a Flipsky 75100 survival memo with HUASHUO MOSFET swaps, solder reflow steps, BMS cut-out warnings, and clone identification cues.【F:data/vesc_help_group/text_slices/input_part002.txt†L25886-L25949】
- Draft a Makerbase MKSESC 75100 prep checklist covering TIM application, driver/MOSFET spares, ignition workarounds, and UART/Bluetooth quirks before riders drop it into 14 S scooters.【F:data/vesc_help_group/text_slices/input_part002.txt†L27142-L27268】【F:data/vesc_help_group/text_slices/input_part002.txt†L27334-L27428】
- Add a FLIR/emissivity cheat sheet so builders calibrate thermal cameras before trusting hub or heatsink temperature maps.【F:data/vesc_help_group/text_slices/input_part002.txt†L25844-L25858】
- Publish a Trickstuff Bionol brake-fluid brief that covers Magura seal compatibility, boiling points, and sourcing so riders stop experimenting with DOT fluids that dissolve silicone components.【F:data/vesc_help_group/text_slices/input_part002.txt†L23240-L23328】
- Add a Magura hose extension how-to listing the correct olives, barbs, and bleed routine when lengthening bike-spec levers for scooter builds.【F:data/vesc_help_group/text_slices/input_part002.txt†L23337-L23385】
- Create a brake decontamination guide comparing brake cleaner, PTFE products, and WD-40 for water-damaged calipers so owners avoid seal-swelling solvents.【F:data/vesc_help_group/text_slices/input_part002.txt†L23832-L23857】
- Summarize Izuna’s Flipsky firmware/bootloader package and Xiaomi BLE wiring so new owners can flash 75/100 V controllers without bricking them.【F:data/vesc_help_group/text_slices/input_part002.txt†L23525-L23542】
- Document the Flipsky 75100 V2 voltage-offset quirk and calibration routine to stop the ~2 V telemetry error after firmware updates.【F:data/vesc_help_group/text_slices/input_part002.txt†L23465-L23472】
- Package the dual-Ubox SWD recovery process—including CAN-bridge wiring, driver installs, and failure codes—so owners can revive dead ESCB stages without shipping controllers overseas.【F:data/vesc_help_group/text_slices/input_part002.txt†L27404-L27508】
- Capture the latest Vsett 10+ stock-pack limits (≈60 A safe zone, heavy sag at 70–80 A) and explain how phase/battery power math should guide FOC tuning.【F:data/vesc_help_group/text_slices/input_part002.txt†L23640-L23729】
- Write a cautionary note on flashing VESC 6.0 builds to uBox hardware, including SWD recovery steps and current support status.【F:data/vesc_help_group/text_slices/input_part002.txt†L24213-L24243】
- Outline a diagnostic workflow for over-volting stock Vsett controllers (current-sense network, primary buck regulator) before attempting 60 V conversions.【F:data/vesc_help_group/text_slices/input_part002.txt†L24388-L24406】
- Record lessons from Rosheee’s Rion MOSFET swap failure to emphasize staged power-up and short checks when reviving blown controllers.【F:data/vesc_help_group/text_slices/input_part002.txt†L24459-L24499】
- Build a uBox vapor-chamber retrofit guide covering spring preload, heatpipe isolation, and failure inspection steps before recommending the deck mod widely.【F:data/vesc_help_group/text_slices/input_part002.txt†L17000-L17055】【F:data/vesc_help_group/text_slices/input_part002.txt†L18464-L18488】
- Capture PETG enclosure print settings (layer height, volumetric flow, roll change cadence) so others can reproduce Artem’s low-stringing profile.【F:data/vesc_help_group/text_slices/input_part002.txt†L17040-L17055】
- Draft a Blade/Achilleus teardown showing axle thread verification and hinge locking methods to eliminate wobble complaints.【F:data/vesc_help_group/text_slices/input_part002.txt†L17100-L17147】
- Document Vsett vs Dualtron traction tuning (spring rates, tyre pressures, field weakening limits) using the 20S/14kW experiments as case studies.【F:data/vesc_help_group/text_slices/input_part002.txt†L17303-L17475】
- Produce a Monorim dual-motor conversion manual (axle extensions, torque-arm fab, pack sizing, Daly BMS wiring).【F:data/vesc_help_group/text_slices/input_part002.txt†L18055-L18144】
- Compare scooter ferrofluid fill volumes, sealing methods, and aftermarket hub coolers to set best-practice targets for 200 A builds.【F:data/vesc_help_group/text_slices/input_part002.txt†L17545-L17562】【F:data/vesc_help_group/text_slices/input_part002.txt†L18255-L18308】
- Add a DIY hub-fin wrap case study showing how thermal tape, ferrofluid, and wire clamps performed in 34 °C ambient so others can replicate the proven layout.【F:data/vesc_help_group/text_slices/input_part002.txt†L27288-L27324】【F:data/vesc_help_group/text_slices/input_part002.txt†L27471-L27523】
- Outline Slack Core frame reinforcement options for the thin lower joint Artem flagged, with load-path calculations for 100 kg riders.【F:data/vesc_help_group/text_slices/input_part002.txt†L18046-L18124】
- Publish a lithium-pack selection matrix comparing 48X, 50E, M50LT, P42A, and pouch chemistries for 20S scooters and e-moto builds.【F:data/vesc_help_group/text_slices/input_part002.txt†L17924-L18421】
- Publish a Magura brake upgrade memo covering MT5/MT7 lever options, four-pad swaps, and the pros/cons of steel-braided “Stahlflex” hoses with correct banjo sizing.【F:data/vesc_help_group/text_slices/input_part002.txt†L14100-L14156】【F:data/vesc_help_group/text_slices/input_part002.txt†L14703-L14726】
- Add a hall-diagnostics quick guide that captures the 1-2-3 wiring requirement and ERPM switchover tuning so others avoid the vibration trap Mirono hit.【F:data/vesc_help_group/text_slices/input_part002.txt†L14506-L14532】【F:data/vesc_help_group/text_slices/input_part002.txt†L14820-L14824】
- Issue a FW 5.3 safety bulletin for Ubox owners (symptoms, mitigation, recommended limits) and track Spintend’s fix progress.【F:data/vesc_help_group/text_slices/input_part002.txt†L14654-L14672】【F:data/vesc_help_group/text_slices/input_part002.txt†L24157-L24169】
- Create a Flipsky 75100 20 S checklist (voltage headroom, accurate telemetry, cooling needs) using Gigolo Joe’s data point.【F:data/vesc_help_group/text_slices/input_part002.txt†L14944-L14966】
- Document the NCEP01T30T cross-reference, sourcing status, and solder touch-up steps so Tronic owners can attempt in-field MOSFET replacements before shipping controllers overseas.【F:data/vesc_help_group/text_slices/input_part002.txt†L15160-L15357】【F:data/vesc_help_group/text_slices/input_part002.txt†L15274-L15294】
- Mirror the ANT BMS APK/User guide in the repo and add sideload instructions for riders locked out of the old VBMS app.【F:data/vesc_help_group/text_slices/input_part002.txt†L15096-L15104】
- Evaluate whether the heavy Ubox heat-block builds measurably drop junction temps or if better case contact delivers more benefit than sheer mass.【F:data/vesc_help_group/text_slices/input_part002.txt†L14824-L14828】【F:data/vesc_help_group/text_slices/input_part002.txt†L14932-L14941】
- Clarify Magura caliper orientation guidance for Vsett conversions (lip direction, airflow, banjo swaps) once empirical data arrives.【F:data/vesc_help_group/text_slices/input_part002.txt†L15380-L15490】
- Add a Samsung 50E safety note covering the 5 P 130 A failure, BMS 180 A cutoff, and recommended 20S6P/20S7P replacement packs plus deck reinforcement options.【F:data/vesc_help_group/text_slices/input_part002.txt†L12529-L12583】【F:data/vesc_help_group/text_slices/input_part002.txt†L12538-L12548】
- Summarize copper strip sourcing and welding best practices (0.15 mm plated strip ratings, sandwich stacks, argon-assisted weld cautions).【F:data/vesc_help_group/text_slices/input_part002.txt†L12622-L12654】【F:data/vesc_help_group/text_slices/input_part002.txt†L13624-L13640】
- Publish Magura pad longevity guidance (Kool Stop D170S swap, wet-bite expectations) and an Xtech rain-behavior troubleshooting tip sheet.【F:data/vesc_help_group/text_slices/input_part002.txt†L13161-L13197】【F:data/vesc_help_group/text_slices/input_part002.txt†L13151-L13182】
- Write a uBox Bluetooth recovery checklist covering USB reflashing, bootloader reinstalls, UART toggles, and Android sideload steps.【F:data/vesc_help_group/text_slices/input_part002.txt†L13177-L13277】
- Fold the Danish dyno stop into the legal-mode quick reference so riders can cite the €400/€200 fine outcome and 29 km/h profile strategy.【F:data/vesc_help_group/text_slices/input_part002.txt†L13294-L13323】
- Capture zero-vector frequency tuning guidance (30 → 20 kHz example) alongside ferrofluid/vented-cover precautions.【F:data/vesc_help_group/text_slices/input_part002.txt†L13653-L13668】【F:data/vesc_help_group/text_slices/input_part002.txt†L13748-L13758】【F:data/vesc_help_group/text_slices/input_part002.txt†L23884-L23952】
- Draft a Kelly KLS tuning cheat sheet (percent-to-amp mapping, realistic thermal limits, wiring upgrades) for 7212S/7218S builds.【F:data/vesc_help_group/text_slices/input_part002.txt†L13783-L13856】【F:data/vesc_help_group/text_slices/input_part002.txt†L13888-L13915】
- Document Spintend ABS current-filter tweaks for FW 5.3 so riders can stop false over-current trips.【F:data/vesc_help_group/text_slices/input_part002.txt†L13921-L13928】
- Publish a Kaabo Wolf lighting harness quick reference (pinout, expected voltages, switch routing) so VESC swaps retain OEM accessories safely.【F:data/vesc_help_group/text_slices/input_part002.txt†L8000-L8088】【F:data/vesc_help_group/text_slices/input_part002.txt†L8273-L8280】
- Document uBox absolute-current tuning and reliable MOSFET temperature measurement methods to keep high-ERPM builds from false-tripping or cooking hardware.【F:data/vesc_help_group/text_slices/input_part002.txt†L8355-L8405】【F:data/vesc_help_group/text_slices/input_part002.txt†L9411-L9446】
- Compare Spintend, Tronic, Little FOCer, YYK, and Kelly controllers for 100 V-class scooters, including pricing, supply timelines, and real thermal headroom.【F:data/vesc_help_group/text_slices/input_part002.txt†L8200-L8216】【F:data/vesc_help_group/text_slices/input_part002.txt†L8621-L8690】
- Produce a Kaabo battery reinforcement guide covering cell upgrades, connector swaps, padding, and moisture mitigation before riders chase 150 A+ pulls.【F:data/vesc_help_group/text_slices/input_part002.txt†L8830-L8853】【F:data/vesc_help_group/text_slices/input_part002.txt†L9071-L9153】
- Outline best practices for charge-only BMS setups, Daly/JK Bluetooth toggles, and balancing schedules when discharge protection is bypassed.【F:data/vesc_help_group/text_slices/input_part002.txt†L8785-L8809】【F:data/vesc_help_group/text_slices/input_part002.txt†L9452-L9459】
- Evaluate enclosure materials (craftplex, stainless, fiberglass) and mounting hardware that keep scooter packs stationary without chewing through insulation.【F:data/vesc_help_group/text_slices/input_part002.txt†L9145-L9245】
- Assemble a track-day checklist that covers waterproofing, brake and cooling upgrades, plus a legal risk brief for jurisdictions policing high-speed scooters.【F:data/vesc_help_group/text_slices/input_part002.txt†L8711-L8783】【F:data/vesc_help_group/text_slices/input_part002.txt†L9470-L9489】
- Capture connector-upgrade instructions (QS8 vs. HXT/XT90) and integrate the shared G30 brace files into the build documentation repository.【F:data/vesc_help_group/text_slices/input_part002.txt†L8929-L8941】【F:data/vesc_help_group/text_slices/input_part002.txt†L9494-L9499】
- Validate whether carbon bodywork and heat-pipe spacers can materially improve uBox cooling or if resources should shift toward controllers with direct FET mounting.【F:data/vesc_help_group/text_slices/input_part002.txt†L9381-L9431】
- Package the red Ubox USB-C firmware fix and SWD recovery workflow into a troubleshooting note so second-hand buyers can revive misreporting units.【F:data/vesc_help_group/text_slices/input_part002.txt†L9594-L10343】
- Summarize Raphaël’s dual-VESC component requirements and cooling expectations to benchmark future high-current controller projects.【F:data/vesc_help_group/text_slices/input_part002.txt†L9614-L9697】
- Draft a MakerX vs. Sabvoton teardown comparison that includes torque-arm requirements, hall sensor routing, and brake fitment caveats for ebike conversions.【F:data/vesc_help_group/text_slices/input_part002.txt†L9699-L10117】
- Build a Kaabo Wolf waterproofing checklist that addresses M50LT cell limits, deck sealing layers, and active-balancer or JK BMS retrofit guidance.【F:data/vesc_help_group/text_slices/input_part002.txt†L10550-L10632】
- Capture ANT display setup steps and note alternative telemetry options until dedicated VESC dashboards are more available.【F:data/vesc_help_group/text_slices/input_part002.txt†L10912-L10916】
- Draft an enforcement/legal-mode quick reference covering 25–30 km/h profiles, behavior-based policing anecdotes, and documentation riders should carry in EU crackdowns.【F:data/vesc_help_group/text_slices/input_part002.txt†L9502-L9536】
- Publish a Zoom/Nut brake sensor wiring table (resistor values vs. expected output voltages) so dual brake throttles can be integrated without guesswork.【F:data/vesc_help_group/text_slices/input_part002.txt†L10979-L10982】
- Compile a dual-Ubox high-power prep note covering copper blocks, fan openings, potting, deck-mount paste practices, and shared-battery wiring before riders chase 180 A/19 S builds.【F:data/vesc_help_group/text_slices/input_part002.txt†L11156-L11186】【F:data/vesc_help_group/text_slices/input_part002.txt†L11588-L11670】【F:data/vesc_help_group/text_slices/input_part002.txt†L11901-L11953】
- Create a KWeld best-practices sheet (lead length, lug prep, supply options) drawing on the 3 kW loss anecdote so pack builders hit consistent weld energy.【F:data/vesc_help_group/text_slices/input_part002.txt†L11188-L11209】
- Draft a rotor-spacing and torque-arm shim guide showing when to use nickel strip plates, how hard to torque 22 mm nuts, and which 203 mm rotors hold up at 70 km/h.【F:data/vesc_help_group/text_slices/input_part002.txt†L11088-L11137】【F:data/vesc_help_group/text_slices/input_part002.txt†L11406-L11435】【F:data/vesc_help_group/text_slices/input_part002.txt†L12102-L12151】
- Write a hall-regen retrofit how-to (A1324LUA wiring, dual-throttle tuning, panic-regen caps) so builders can reproduce the left-hand brake throttle setups.【F:data/vesc_help_group/text_slices/input_part002.txt†L11240-L11283】【F:data/vesc_help_group/text_slices/input_part002.txt†L11249-L11257】
- Produce a MakerX cooling and validation checklist covering realistic continuous currents, mounting orientation, and MOSFET ID verification.【F:data/vesc_help_group/text_slices/input_part002.txt†L12320-L12354】
- Assemble a lighting-power cheat sheet comparing dual 3 A buck converters versus auxiliary packs and outlining horn wiring strategies.【F:data/vesc_help_group/text_slices/input_part002.txt†L11814-L11822】【F:data/vesc_help_group/text_slices/input_part002.txt†L12063-L12078】
- Publish a Spin-Y throttle pinout and module guide (six-core harness, cruise line reuse, optional 16 mm switch module) ahead of production.【F:data/vesc_help_group/text_slices/input_part002.txt†L12390-L12452】
- Capture precharge and latching-button wiring examples showing Spintend polarity expectations, acceptable resistor values, and how to integrate external heat sinks without pinching leads.【F:data/vesc_help_group/text_slices/input_part002.txt†L12159-L12179】【F:data/vesc_help_group/text_slices/input_part002.txt†L12457-L12499】
- Create a Wolf tubeless tire change SOP that references the shared tool/video tips for non-split rims and stock-up guidance.【F:data/vesc_help_group/text_slices/input_part002.txt†L11745-L11759】【F:data/vesc_help_group/text_slices/input_part002.txt†L11786-L11794】
- Produce a Spin-Y throttle wiring and module pinout one-pager covering the six-core harness, cruise line, and button options.【F:data/vesc_help_group/text_slices/input_part002.txt†L12390-L12452】
- Recommend anti-spark/precharge component selections (resistor values, switch wiring) based on the 1 kΩ failure anecdote and power-button notes.【F:data/vesc_help_group/text_slices/input_part002.txt†L12159-L12179】【F:data/vesc_help_group/text_slices/input_part002.txt†L12457-L12499】
- Summarize Flipsky 75100’s current VESC 6.0 limitations and list workarounds until official support lands.【F:data/vesc_help_group/text_slices/input_part002.txt†L11299-L11319】【F:data/vesc_help_group/text_slices/input_part002.txt†L11369-L11379】
