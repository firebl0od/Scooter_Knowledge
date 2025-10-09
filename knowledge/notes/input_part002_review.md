# input_part002.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part002.txt`
- Coverage: 2022-04-14 04:47 through 2022-05-07 13:12 (lines 1-8000)
- Latest detailed pass: 2022-04-26 18:33 through 2022-05-07 11:24 (lines 5000-8000, refreshed 2025-10-14)
- Next starting point: 2022-05-07T13:12 onward (line 8001 and later)

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

### Firmware & Toolchain Updates
- Vedder’s VESC firmware 6.0 entered beta, with early adopters reporting noticeable changes versus 5.3 and encouraging others to review the public Git changelog before flashing.【F:data/vesc_help_group/text_slices/input_part002.txt†L1841-L1853】
- Builders compiling from source noted that fresh firmware binaries exceed Ubox single MCU flash limits unless paired with an updated VESC Tool build, prompting local toolchain rebuilds.【F:data/vesc_help_group/text_slices/input_part002.txt†L2125-L2127】

### Battery Configuration & Regen Guidance
- Artem walked a Vsett 10+ owner running a 16S5P Samsung 35E pack through safe limits—40 A battery, 140–150 A phase (170 A absolute) and ≤−17 A regen—highlighting that higher current mostly improves mid-speed acceleration and requires accurate hall wiring for speed telemetry.【F:data/vesc_help_group/text_slices/input_part002.txt†L2195-L2333】
- He reiterated that 35E cells tolerate about 1 C regenerative bursts but degrade quickly under faster charging, advocating ≤0.5 C routine charging and lower when time allows.【F:data/vesc_help_group/text_slices/input_part002.txt†L2339-L2344】
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

### Dual-VESC Coordination & Field-Weakening Behavior
- Gigolo Joe’s dual setup initially misbehaved because both controllers were left in default CAN roles; setting master ID 0 and slave ID 1 restored synchronized throttle sharing regardless of which unit the hall signal feeds.【F:data/vesc_help_group/text_slices/input_part002.txt†L7167-L7172】
- Field weakening keeps motors spinning briefly after throttle release by design to avoid wheel lock, a trait experienced riders flagged as normal for VESC implementations even if other scooters coast down faster.【F:data/vesc_help_group/text_slices/input_part002.txt†L7173-L7177】

### Controller Choices for New Kaabo Builds
- Rosheee immediately lists the Minimotors 2 × 50 A square-wave electronics from his freshly delivered Kaabo, while peers debate whether uBox cooling—or alternative controllers entirely—will ultimately bottleneck the platform’s “monster” hub motors.【F:data/vesc_help_group/text_slices/input_part002.txt†L7499-L7600】
- Paolo and Кирилл caution that uBox can easily overdrive stock motors if limits aren’t dialed back, whereas Minimotors’ square-wave punch comes at the cost of heat, inefficiency, and poor low-speed modulation.【F:data/vesc_help_group/text_slices/input_part002.txt†L7504-L7588】

### Salvaging & Repairing Stock Hardware
- Federico77 documents reviving a burnt G30 ECU shunt by hammering copper wire flat and soldering it in place, a low-cost fix fellow “Genoese” builders can replicate while hunting scarce D-series boards with extra capacitors.【F:data/vesc_help_group/text_slices/input_part002.txt†L6797-L6816】
- Mirko Boni’s refreshed G30 pairs Magura brakes with a 10S + 6S pack on the stock BMS; riders praise the stopping power and note that high-speed Ninebot builds still rely on factory electronics when mechanical upgrades keep pace.【F:data/vesc_help_group/text_slices/input_part002.txt†L6303-L6310】

## Follow-up Ideas
- Document real-world testing of the owl headlights (current draw, thermal behaviour, beam cutoff) once multimeter data is gathered.
- Capture validated VESC settings for 17 S/20 S builds that balance performance with cell longevity, including thermal sensor placement guidance.
- Prototype button layouts for Artem’s throttle module and evaluate reach/accidental presses during riding; align with ADC adapter pinouts.
- Investigate alternative enclosure manufacturing (e.g., CNC or resin prints) with cost/lead-time comparisons for the smart display project.
- Stress-test or replace 3D-printed G30 brake adapters to confirm they survive repeated hard stops, or source CNC alternatives.【F:data/vesc_help_group/text_slices/input_part002.txt†L3214-L3249】
- Map Flipsky 75100 firmware variants (Jaykup V2 5.3 bin, Paolo’s no-limit builds, 3-shunt releases) and note which hardware revs they suit, plus document the stock-firmware burnout reports for reference.【F:data/vesc_help_group/text_slices/input_part002.txt†L5345-L5397】【F:data/vesc_help_group/text_slices/input_part002.txt†L6054-L6080】
- Summarize connector upgrade options (Higo L1019 vs. XT150/XT90) with ampacity guidelines and practical crimp/solder steps for Paolo’s controller audience.【F:data/vesc_help_group/text_slices/input_part002.txt†L5005-L5089】【F:data/vesc_help_group/text_slices/input_part002.txt†L5955-L6008】
- Catalog Kelly hall/phase wiring permutations that minimize no-load amps and collect reliable reflashing guidance for 72150 owners.【F:data/vesc_help_group/text_slices/input_part002.txt†L6513-L6668】
- Capture Kaabo stock BMS thermal limits and realistic amp ceilings so uBox adopters can set conservative starting points before chasing 200 A per motor.【F:data/vesc_help_group/text_slices/input_part002.txt†L7533-L7600】
- Evaluate whether PMT race tires justify tubeless conversions for commuter riders or if higher pressures and newer yellow-badge batches already deliver the needed grip/durability balance.【F:data/vesc_help_group/text_slices/input_part002.txt†L6722-L6755】
- Diagram Kaabo Wolf harness quirks (grey/white limiter loops, glued controller mounts, P-setting dependencies) so controller swaps don’t miss hidden speed caps or require destructive disassembly.【F:data/vesc_help_group/text_slices/input_part002.txt†L7192-L7270】
- Publish a quick reference on safely depowering Minimotors controllers (capacitor discharge, connector order) after the bench “puff” incident to prevent repeat damage.【F:data/vesc_help_group/text_slices/input_part002.txt†L6991-L7050】
- Map the Wolf lighting PCB pinout (orange/brown feeds, 12 V step-down) for anyone retaining OEM lights alongside third-party ADC boxes or direct-pack accessories.【F:data/vesc_help_group/text_slices/input_part002.txt†L7980-L8084】
- Draft a uBox adapter quick-start (ADC mode, throttle ports, firmware expectations) so first-time installers can validate configuration before suspecting wiring faults.【F:data/vesc_help_group/text_slices/input_part002.txt†L5005-L5024】
- Capture an ESC service checklist covering thermal paste selection, connector torque, and ferrofluid safety so future rebuilds avoid premature dry-out or splash hazards.【F:data/vesc_help_group/text_slices/input_part002.txt†L5027-L5058】【F:data/vesc_help_group/text_slices/input_part002.txt†L5828-L5920】
