# input_part002.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part002.txt`
- Coverage: 2022-04-14 04:47 through 2022-05-31 11:04 (lines 1-14000)
- Latest detailed pass: 2022-05-26 01:34 through 2022-05-31 11:04 (lines 12501-14000, logged 2025-10-20)
- Next starting point: 2022-05-31T11:04:45 onward (line 14001 and later)

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

## Follow-up Ideas
- Add a Samsung 50E safety note covering the 5 P 130 A failure, BMS 180 A cutoff, and recommended 20S6P/20S7P replacement packs plus deck reinforcement options.【F:data/vesc_help_group/text_slices/input_part002.txt†L12529-L12583】【F:data/vesc_help_group/text_slices/input_part002.txt†L12538-L12548】
- Summarize copper strip sourcing and welding best practices (0.15 mm plated strip ratings, sandwich stacks, argon-assisted weld cautions).【F:data/vesc_help_group/text_slices/input_part002.txt†L12622-L12654】【F:data/vesc_help_group/text_slices/input_part002.txt†L13624-L13640】
- Publish Magura pad longevity guidance (Kool Stop D170S swap, wet-bite expectations) and an Xtech rain-behavior troubleshooting tip sheet.【F:data/vesc_help_group/text_slices/input_part002.txt†L13161-L13197】【F:data/vesc_help_group/text_slices/input_part002.txt†L13151-L13182】
- Write a uBox Bluetooth recovery checklist covering USB reflashing, bootloader reinstalls, UART toggles, and Android sideload steps.【F:data/vesc_help_group/text_slices/input_part002.txt†L13177-L13277】
- Fold the Danish dyno stop into the legal-mode quick reference so riders can cite the €400/€200 fine outcome and 29 km/h profile strategy.【F:data/vesc_help_group/text_slices/input_part002.txt†L13294-L13323】
- Capture zero-vector frequency tuning guidance (30 → 20 kHz example) alongside ferrofluid/vented-cover precautions.【F:data/vesc_help_group/text_slices/input_part002.txt†L13653-L13668】【F:data/vesc_help_group/text_slices/input_part002.txt†L13748-L13758】
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
