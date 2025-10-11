# input_part006.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part006.txt`
- Coverage: 2023-12-11T13:10 through 2024-01-17T00:07 (lines 6700-18699; this pass added 17200-18699)
- Next starting point: line 18700 (2024-01-18T00:07 and later)

## Key Findings

### Braking, Handling & Suspension
- Riders reiterate that the front brake carries most stopping power—rear-only braking slides easily—so performance builds prioritise strong front hydraulics and dual electronic braking where possible.【F:data/vesc_help_group/text_slices/input_part006.txt†L6701-L6704】
- Shimano “resin only” 160 mm rotors are flagged as unsuitable for 72 V scooters; builders recommend 2 mm rotors designed for metallic pads plus full-hydraulic calipers to avoid fade at higher speeds.【F:data/vesc_help_group/text_slices/input_part006.txt†L7206-L7233】
- Vsett 10+ owners tracing a loud “clunk” between braking and throttle transitions usually find a loose axle or missing hub washers after bearing swaps; tightening hardware and adding proper torque washers/arms eliminates the knock.【F:data/vesc_help_group/text_slices/input_part006.txt†L7282-L7572】
- Suspension debates pit budget Monorim kits against European-made Konyk/Dereza arms: Monorim pricing stays low by using weaker castings, while the handcrafted alternatives cost ~€100 per end but deliver better travel and durability for <60 km/h use.【F:data/vesc_help_group/text_slices/input_part006.txt†L7288-L7444】
- G30 swingarms can crack at the deck cut-outs under ~130 kg riders; fabricators are modelling reinforcement plates to spread loads around the rear fork bracket.【F:data/vesc_help_group/text_slices/input_part006.txt†L7800-L7806】

### CAN Dash Integration & Firmware Workflow
- Vedder’s `code_server` library offers a more reliable CAN command path than `can-cmd`, automatically retrying failed frames up to five times, but it requires flipping RX/TX wiring when moving from Flipsky to UBOX controllers and flashing `slave_esc.lisp` on every CAN slave ESC.【F:data/vesc_help_group/text_slices/input_part006.txt†L6739-L6804】
- Makerbase dashboards that worked on Flipsky often crash on Spintend/UBOX swaps until the BLE and dash harnesses have their RX/TX wires swapped to match the new pinout; once aligned, the legacy 6.0 scripts operate on 6.02/6.2 firmware without ADC inputs.【F:data/vesc_help_group/text_slices/input_part006.txt†L6757-L7216】
- Persistent Makerbase dash reboots on Vsett conversions are traced to inadequate filtering on the 5 V rail; adding electrolytic bulk capacitance (≈220 µF on the bus plus ~50 µF near the drivers) and correcting misplaced pull-up resistors stabilises the display under high current spikes.【F:data/vesc_help_group/text_slices/input_part006.txt†L7573-L7841】

### Battery Layouts, Materials & Tooling
- Stock G30 frames can hide 20s6p packs internally, and aggressive layouts (removing the OEM ESC and machining rails) stretch to 20s9p, but veterans warn convoluted busbars worsen amp distribution and structural integrity—simple rectangular stacks remain safest for first-time builders.【F:data/vesc_help_group/text_slices/input_part006.txt†L6972-L7266】
- Builders insist on pure nickel (or copper) for high-current packs; nickel-plated steel is ~6× more resistive and only acceptable for low-draw storage walls, so sourcing from trusted vendors such as Nkon is advised.【F:data/vesc_help_group/text_slices/input_part006.txt†L7200-L7407】
- Copper interconnects thicker than 0.1 mm quickly defeat hobby shears; the crew outsources laser/water-jet cutting or invests in Glitter welders rather than attempting car-battery weld hacks, which risk weak joints and blown cells.【F:data/vesc_help_group/text_slices/input_part006.txt†L7243-L7858】
- Makerbase 75100 ALU boards still benefit from additional DC-link capacitance (≥220 µF plus small 16 V caps on the gate drivers) and correct undervoltage limits to avoid the recurring “MOS die” failures reported on early hardware.【F:data/vesc_help_group/text_slices/input_part006.txt†L7816-L7841】

### Motor & Controller Tuning
- Zero 10X 1200 W hub motors fed by 68 V, 59 A batteries saturate around 7–8 kW, but the practical ceiling is ~4 kW unless stator temps stay under 80 °C; dual-motor CAN setups share the load far better than a single hub when chasing top speed.【F:data/vesc_help_group/text_slices/input_part006.txt†L7323-L7334】
- Mid-drive e-bike swaps that stall at 16 km/h typically have conservative motor-current limits or mismatched ERPM calculations; raising motor current to ~80 A phase/20 A battery, verifying wheel size/gear ratios, and logging duty cycle helps unlock 30–40 km/h while monitoring for BMS cut-outs.【F:data/vesc_help_group/text_slices/input_part006.txt†L7441-L7542】
- Fitting 11 inch hubs on Zero 10X frames is feasible only after machining the swingarm axle; otherwise clearance and alignment suffer.【F:data/vesc_help_group/text_slices/input_part006.txt†L7246-L7255】

### Charging, Storage & Energy Management
- G30-class Ninebots accept Segway’s 5 A fast charger via the 8 mm barrel connector, but BMS firmware cuts charging if current exceeds ~8 A; smaller F-series and Xiaomi packs generally top out at 4 A continuous, so adjustable lab supplies must honour those limits.【F:data/vesc_help_group/text_slices/input_part006.txt†L7856-L7874】
- Riders debate warehouse SOC habits: while some new scooters arrive at 70–100 % charge, logistics rules still require ~30–50 % for compliant long-term storage, making it wise to check packs on arrival and balance them before hard use.【F:data/vesc_help_group/text_slices/input_part006.txt†L6995-L7004】【F:data/vesc_help_group/text_slices/input_part006.txt†L7069-L7084】
- Winter commuters rely on heated battery bags or external heaters to keep packs above ~10 °C and avoid cold-weather sag, particularly on Molicel-equipped builds.【F:data/vesc_help_group/text_slices/input_part006.txt†L6738-L6773】

### Scooter Model Guidance & Market Notes
- For North American shoppers, the Xiaomi Pro 2 (12.4 Ah, 300 W front motor) and Segway G30 remain the minimum viable commuter scooters; Segway F-series and many supermarket clones ship with weak frames, sensorless motors, and scarce spare parts.【F:data/vesc_help_group/text_slices/input_part006.txt†L6946-L7011】【F:data/vesc_help_group/text_slices/input_part006.txt†L8003-L8026】
- Nami, NIU, and Segway P-series scooters may look premium but often lack aftermarket parts; veterans advise confirming component availability (or sticking to proven G-series/Xiaomi platforms) before recommending them to family.【F:data/vesc_help_group/text_slices/input_part006.txt†L7986-L8016】
- N65/S65 decks can host dual VESCs and roughly 100 21700 cells with modest spacers, though squeezing 120×18650 cells plus a 150 A JK BMS demands aggressive packaging.【F:data/vesc_help_group/text_slices/input_part006.txt†L7948-L7966】

### Fabrication, PPE & Shop Practices
- PETG is the go-to filament for outdoor battery carriers—odorless and tougher than PLA—yet printers should stay out of sleeping areas and receive ample support/brim adhesion to prevent long prints from delaminating.【F:data/vesc_help_group/text_slices/input_part006.txt†L7180-L7190】【F:data/vesc_help_group/text_slices/input_part006.txt†L7519-L7570】
- Working aluminium or PETG parts throws fine particulates; builders wear gloves, wash thoroughly, and avoid eating until cleaned up to limit microplastic exposure.【F:data/vesc_help_group/text_slices/input_part006.txt†L8048-L8054】
- Full-face helmets and winter balaclavas are treated as consumables—riders budget $120+ for protective lids and keep them on even indoors when moving between shops to avoid theft and stay warm in −15 °C conditions.【F:data/vesc_help_group/text_slices/input_part006.txt†L7888-L7939】

### Additional Findings (Lines 8200-9699)

#### Certification & Market Conditions
- Riders swapping import notes stress that European sellers expect UL-certified battery packs, and they worry pending laws could mirror U.S. safety pushes that limit gray-market scooters.【F:data/vesc_help_group/text_slices/input_part006.txt†L8200-L8213】
- Dutch riders remind travelers that stand-up scooters remain illegal without seats, so visiting enthusiasts should plan for enforcement despite locals still spotting Xiaomi units around Venlo.【F:data/vesc_help_group/text_slices/input_part006.txt†L9168-L9176】

#### Battery Packs & Power Delivery
- Stock Vsett 9+/10+ and Kugoo G4 packs sag heavily under load; owners report factory “50 A” drivetrains pairing controllers and batteries right at their current ceiling, leading to range, speed, and wobble disappointments until higher-discharge cells or fresh packs are installed.【F:data/vesc_help_group/text_slices/input_part006.txt†L8414-L8426】
- Builders highlight that premium scooters rarely ship with true high-discharge cells beyond brands like Nami, motivating DIY upgrades such as 20s3p Molicel sleeper builds or full 20s9p 21700 conversions when packaging space allows.【F:data/vesc_help_group/text_slices/input_part006.txt†L8425-L8444】【F:data/vesc_help_group/text_slices/input_part006.txt†L9241-L9241】
- A 3 L Wildman battery bag barely holds 56×21700 cells, so hybrid internal/external layouts (e.g., 12p internal, 8p in a bag) and precise nickel planning are needed when stretching beyond stock decks.【F:data/vesc_help_group/text_slices/input_part006.txt†L9684-L9688】
- Packing advice emphasizes verifying nickel purity and layering: builders caught steel masquerading as nickel strip and recommend precut busbars or stacked pure nickel to hit 5 kW targets without copper.【F:data/vesc_help_group/text_slices/input_part006.txt†L9070-L9073】

#### Controllers, Firmware & Diagnostics
- Spintend ALU controllers ship with tiny accessory connectors and, on newer 85/200 batches, dual 10 AWG outputs feeding a single 8 mm bullet—owners lean on quality crimpers, heavy soldering, or larger bullets to seat the cables without overheating the joint.【F:data/vesc_help_group/text_slices/input_part006.txt†L8244-L8245】【F:data/vesc_help_group/text_slices/input_part006.txt†L9567-L9568】【F:data/vesc_help_group/text_slices/input_part006.txt†L9624-L9624】
- Troubleshooting tips include metering the Ubox V2’s 12 V rail before blaming loads, re-running motor detection after hardware swaps, and confirming hall harnesses when Vsett 10+ sensors are unplugged mid-setup.【F:data/vesc_help_group/text_slices/input_part006.txt†L8531-L8533】【F:data/vesc_help_group/text_slices/input_part006.txt†L9000-L9003】【F:data/vesc_help_group/text_slices/input_part006.txt†L9247-L9249】
- Riders using Vedder’s `code_server` reiterate its reliability for CAN dashboards compared with legacy scripts as long as firmware is current and telemetry logs are captured during faults for later review.【F:data/vesc_help_group/text_slices/input_part006.txt†L9162-L9164】【F:data/vesc_help_group/text_slices/input_part006.txt†L9593-L9599】【F:data/vesc_help_group/text_slices/input_part006.txt†L9675-L9677】
- 3Shul CL controllers continue to struggle above ~120 V: one CL350 detonated indoors after charging to 120 V despite 126 V marketing claims, and veterans warn EUC users that the hardware only offers ~135 V FET headroom (22 s max without regen) versus the 160–200 V margin their 30 s packs demand.【F:data/vesc_help_group/text_slices/input_part006.txt†L9603-L9635】【F:data/vesc_help_group/text_slices/input_part006.txt†L9649-L9651】

#### Chassis, Suspension & Fabrication
- Aluminum aftermarket decks require skilled TIG work, intermittent cooling, and proper PPE; many builders instead drill new bolt patterns, confirm alloys with magnet/weight checks, or outsource to fabricators to avoid weak welds on load-bearing scooter frames.【F:data/vesc_help_group/text_slices/input_part006.txt†L8811-L8843】
- Fitting oversized hubs on G30s means inverting and cold-setting steel forks or machining torque-specific spacers; improvised aluminum dropouts need torque washers or CNC inserts to keep high-power axles from spinning out.【F:data/vesc_help_group/text_slices/input_part006.txt†L8572-L8577】【F:data/vesc_help_group/text_slices/input_part006.txt†L9453-L9458】
- Monorim conversions benefit from upgraded bushings/washers or custom-machined spacers to handle 3 kW-class motors without slop, and some builders consider swapping to Konyk arms for easier torque-arm integration.【F:data/vesc_help_group/text_slices/input_part006.txt†L9412-L9425】【F:data/vesc_help_group/text_slices/input_part006.txt†L9490-L9498】
- DIYers cleaning corroded hubs advocate mechanical methods (drill-mounted wire brushes) over chemical baths to strip rust without residue, especially when the motor’s still worth salvaging.【F:data/vesc_help_group/text_slices/input_part006.txt†L8491-L8502】

#### 3D Printing & Materials
- PETG and CF-PETG parts hold up for deck spacers and mounts, but carbon-filled filaments need ≥0.6 mm hardened-steel nozzles, heated chambers, and possibly dryers to counter brittleness—PLA survives in dry storage yet deforms in high-heat climates like Las Vegas.【F:data/vesc_help_group/text_slices/input_part006.txt†L8256-L8277】
- Epoxy, cyanoacrylate, or specialty plastic glues bond PETG/PLA prints without melting them, giving commuters options for reinforcing phone mounts and other accessories.【F:data/vesc_help_group/text_slices/input_part006.txt†L8405-L8490】

#### Wheels, Tires & Brakes
- Suspension tuners juggle premium brake hardware: Magura/ TRP setups expect 2.0–2.3 mm rotors, and buying left/right-specific four-piston calipers matters when sourcing AliExpress Brembo clones for right-hand drive scooters.【F:data/vesc_help_group/text_slices/input_part006.txt†L9541-L9558】【F:data/vesc_help_group/text_slices/input_part006.txt†L9617-L9618】
- Xiaomi sleepers swapping to PMT 10×3 or CST 10×2 tubes should verify valve orientation and bushing stacks, as mis-bent stems and asymmetrical frames complicate fitting dual 60H/50H hubs on Pro 2 chassis.【F:data/vesc_help_group/text_slices/input_part006.txt†L9068-L9070】【F:data/vesc_help_group/text_slices/input_part006.txt†L9636-L9640】

#### Racing & Performance Benchmarks
- European race organizers now cap packs at 22 s (≈35 kW nominal limits) after previously allowing unlimited voltage, so teams chase torque via motor stator sizing, field weakening current, and lighter builds instead of simply stacking series cells.【F:data/vesc_help_group/text_slices/input_part006.txt†L9056-L9103】
- Street riders trading logs cite that 30 kW street pulls are attainable on QS motors with FarDriver/Tronic hardware, but daily commuters often settle around 2.4 kW until higher-current 20 s batteries arrive.【F:data/vesc_help_group/text_slices/input_part006.txt†L9660-L9674】

### Additional Findings (Lines 9700-11199)

#### Ergonomics & Accessories
- Riders warn that bolt-on saddles move weight rearward, making speed bumps harder to unload and raising the risk of bottoming out; they also note 2.5 L frame bags are shorter but wider than 3 L options, so check foot room before buying.【F:data/vesc_help_group/text_slices/input_part006.txt†L9720-L9735】

#### Suspension & Frames
- Nami Viper owners report no aftermarket shock matches the platform’s force/stroke requirements—most units run nearly solid, stressing the rider and chassis—so even premium MTB dampers feel too soft.【F:data/vesc_help_group/text_slices/input_part006.txt†L9856-L9877】
- Monorim front suspensions can chew through clamp spacers; builders are redesigning the block and adding an extender so Sokil/Konyk stem clamps clear the fork arms while keeping the folding lock functional.【F:data/vesc_help_group/text_slices/input_part006.txt†L9951-L9955】

#### Battery & Charging Practices
- If a smart BMS is shut down over BLE, simply applying a charger wakes it, but riders reiterate that over-volting packs (e.g., using an 84 V charger on 42 V/54.6 V batteries) can kill the BMS outright and risk fire because the board is not a transformer.【F:data/vesc_help_group/text_slices/input_part006.txt†L9765-L9779】
- Swapping tired 29E packs for 20s10p Samsung 40T builds dramatically reduces sag—one rider expects roughly 7 V less drop, good for almost 10 % more top speed when voltage-limited—though the higher discharge capability will pull heavy current from controllers.【F:data/vesc_help_group/text_slices/input_part006.txt†L9835-L9835】【F:data/vesc_help_group/text_slices/input_part006.txt†L9962-L9968】

#### Controllers, Firmware & Diagnostics
- Makerbase/Flipsky 75 × 100 boards can be ignition-switched by adding a 10 kΩ/100 kΩ divider to the EN pin per Cengiz’s guide, keeping the pin above 1.5 V at minimum pack voltage.【F:data/vesc_help_group/text_slices/input_part006.txt†L9932-L9938】
- A dual-motor lawn mower refit confirmed Makerbase 75100s cover 1200 W/60 V blades: the owner will parallel on/off switches, skip physical throttles, and save hundreds versus OEM ESCs while still having CAN linking if desired.【F:data/vesc_help_group/text_slices/input_part006.txt†L10004-L10038】
- Legacy VESC 4.12 hardware struggles with FOC—its DRV chips fault—so users fall back to BLDC mode when running high-voltage builds.【F:data/vesc_help_group/text_slices/input_part006.txt†L10433-L10439】
- Cranking `iQ target` for more launch torque can trip the battery BMS and drop pack voltage to zero, signalling the pack cannot supply the demanded current.【F:data/vesc_help_group/text_slices/input_part006.txt†L10445-L10452】
- Xiaomi M365 dashboard users need the 6_05_adc branch of the community script to fix braking/current bugs on VESC 6.05; GitHub updates may lag a few minutes after pushes, so re-download if the fix fails initially.【F:data/vesc_help_group/text_slices/input_part006.txt†L11138-L11177】
- Vsett 10+ logs that cap phase current early often point to resistive wiring or conservative undervoltage cutoffs—battery sag around 5 V at 70 % SOC is expected, but extra drop may stem from configuration issues.【F:data/vesc_help_group/text_slices/input_part006.txt†L10809-L10826】

#### Motors & Performance
- G30 hub motors can manage 80 km/h solo and ~98 km/h in dual configurations, yet a single motor pulling a 90 kg rider and 75 kg passenger up hills at 40 A cooked its insulation, underscoring their thermal limits.【F:data/vesc_help_group/text_slices/input_part006.txt†L10042-L10057】
- Lonnyo 70H hubs use 6003 (rotor) and 6008 (stator side) bearings; 22×3 windings favour torque while 33×2 pursue speed, and even 400 A phase cannot guarantee burnouts on grippy 11″ PMTs without mid-drive assistance.【F:data/vesc_help_group/text_slices/input_part006.txt†L10183-L10209】【F:data/vesc_help_group/text_slices/input_part006.txt†L10752-L10767】
- Racers estimate that with dual 70 mm hubs you still plateau near 150 km/h at sea level regardless of 22 s vs. 30 s because phase-current limits, not pack voltage, cap acceleration.【F:data/vesc_help_group/text_slices/input_part006.txt†L10540-L10555】
- Holding 158 km/h on a streamlined build draws roughly 26–28 kW, whereas doubling speed from 100 km/h would demand ~52–64 kW due to cubic aero losses, so gearing alone cannot replace power headroom.【F:data/vesc_help_group/text_slices/input_part006.txt†L10528-L10537】【F:data/vesc_help_group/text_slices/input_part006.txt†L10514-L10520】
- 3Shul CL controllers advertise 32 s capability, but riders report safe operation tops out around 29–30 s without regen because the 135 V FETs have little spike headroom and the onboard 12 V DC/DC sags below 1 A, necessitating external supplies.【F:data/vesc_help_group/text_slices/input_part006.txt†L10550-L10594】

#### Regulation & Market
- Some regions are mandating rider license plates and still enforcing 250 W/25 km/h caps, pushing enthusiasts toward stealth builds or motorcycle licensing to stay legal.【F:data/vesc_help_group/text_slices/input_part006.txt†L10058-L10078】

#### Wheels, Tires & Brakes
- PMT 110/55 R6.5 slicks feel mushy at the 2.2 bar sidewall rating; experienced riders inflate to ~3.5 bar without issues for sharper handling.【F:data/vesc_help_group/text_slices/input_part006.txt†L10772-L10795】

#### Fabrication & Shop Practice
- Veterans suggest budgeting for professional welders when mixing steel and aluminium work—learning MIG still leaves you needing mills, fixturing, and material-specific skills for scooter frame mods.【F:data/vesc_help_group/text_slices/input_part006.txt†L10800-L10804】

### Additional Findings (Lines 11200-12699)

#### Security, Travel & Regulations
- Riders dealing with theft attempts on G30s rely on multiple physical locks—e.g., pairing a bike U-lock with a heavy Kryptonite chain—and warn that electric locks alone are easily defeated in crowded cities.【F:data/vesc_help_group/text_slices/input_part006.txt†L11201-L11211】
- Community members emphasise that scooters left outdoors in Paris disappear quickly; keep the vehicle within sight and comply with the 25 km/h cap, lights, and bike-lane rules enforced in the city, even if enforcement is looser elsewhere in France.【F:data/vesc_help_group/text_slices/input_part006.txt†L12135-L12145】

#### Tires, Wheels & Suspension
- Technicians keep commuter tires at ≥20 psi to prevent the “permanently flat” behaviour seen on neglected Xiaomi fleets, and heavy riders targeting 60 km/h travel push rear pressures toward 3.6 bar to stave off repeat punctures.【F:data/vesc_help_group/text_slices/input_part006.txt†L11224-L11226】【F:data/vesc_help_group/text_slices/input_part006.txt†L12465-L12469】
- Zero 10X veterans flag chronic chassis problems—snapping steering poles, harsh suspension, cramped battery bays, and weak motors—while recommending Vsett/Ninebot alternatives unless buyers plan to overhaul the frame.【F:data/vesc_help_group/text_slices/input_part006.txt†L11620-L11636】
- Vsett 9 owners like the removable battery and hydraulic brakes but still battle 8.5″ tube tires that feel outdated and fragile for 2024 builds.【F:data/vesc_help_group/text_slices/input_part006.txt†L11637-L11650】

#### Maintenance & Service
- Ninebot F2 Pro hubs arrive nearly dry; owners simply pack the stock bearings with quality grease (no oil) during the first service rather than replacing them, especially for riders heavier than the OEM’s 80 kg baseline.【F:data/vesc_help_group/text_slices/input_part006.txt†L11300-L11336】
- Travellers bring spare tubes and hand tools on long rides because hotel stairs, missing elevators, and rear flats remain routine when running high-power builds abroad.【F:data/vesc_help_group/text_slices/input_part006.txt†L12360-L12373】【F:data/vesc_help_group/text_slices/input_part006.txt†L12460-L12468】

#### Batteries & Charging
- Ninebot F2 Pro BMS firmware enforces a 2.4 A ceiling—charging at 2.5 A stops the process—so adjustable supplies must stay within that limit.【F:data/vesc_help_group/text_slices/input_part006.txt†L11685-L11685】
- Builders are packaging 13s10p Samsung 40T packs inside Vsett 9+ decks and planning 20s6p plus parallel 20s5p MH1 add-ons (≈72 V, 32 Ah, 100 A continuous) when space is tight, accepting mixed chemistries so long as pack wiring and BMS balancing are coordinated.【F:data/vesc_help_group/text_slices/input_part006.txt†L11894-L11919】【F:data/vesc_help_group/text_slices/input_part006.txt†L12012-L12030】

#### Controllers, Lighting & Electronics
- Makerbase ALU 75×100 boards default to ~30 kHz zero-vector frequency; owners experimenting with 31 kHz still caution against exceeding the design margins, and they dispute Facebook claims that STM32F405 ADC pins tolerate sustained 5 V throttle signals.【F:data/vesc_help_group/text_slices/input_part006.txt†L11314-L11333】【F:data/vesc_help_group/text_slices/input_part006.txt†L11362-L11370】
- Spintend 12 F controllers are rated around 250 A battery/450 A phase with robust cooling—claims of 400 A per side are viewed as marketing—so dual setups will torque-slip the front wheel long before hitting 900 A combined output.【F:data/vesc_help_group/text_slices/input_part006.txt†L11922-L11930】
- Stock Xiaomi/M365 LEDs expect roughly 6.7 V at 170 mA with proper current limiting; after overdriving them to 11 V, builders either add the correct series resistor, switch to scooter-rated 12–90 V lamps, or adopt 6–12 V Magicshine ME-STVZO units that draw ≤1.5 A from the VESC’s 12 V rail.【F:data/vesc_help_group/text_slices/input_part006.txt†L12168-L12219】
- Xiaomi rear lamps paired with Spintend ADC adapters want a clean 5 V, 120 mA feed; misconfiguration in input setup can make the brake lever behave like both throttle and brake, so riders redo the calibration in current mode and hand-edit the brake values afterward.【F:data/vesc_help_group/text_slices/input_part006.txt†L12113-L12116】【F:data/vesc_help_group/text_slices/input_part006.txt†L12213-L12222】

#### Fabrication, Tools & 3D Printing
- PETG battery holders crack when printed wet or too fast; seasoned builders dry filament, cut speeds toward 80–120 mm/s with 0.6 mm nozzles, run 240–260 °C hotends, and tune retraction/fan settings before trusting the parts to hold 21700 cells.【F:data/vesc_help_group/text_slices/input_part006.txt†L11233-L11266】【F:data/vesc_help_group/text_slices/input_part006.txt†L11870-L11879】【F:data/vesc_help_group/text_slices/input_part006.txt†L12440-L12456】
- Packing twin 12 AWG leads into QS8 shells often leaves the lid ajar; builders resort to copious flux, full wetting of both conductors, and layered heat-shrink if the plastic cover refuses to latch cleanly.【F:data/vesc_help_group/text_slices/input_part006.txt†L12058-L12097】

#### Motors & Components
- Riders hunting water-resistant drop-in motors for Wolf King GTs note that repeated rust inside stock housings likely stems from poor seals or towing overloads, so inspections focus on bearing condition and ingress protection before sourcing replacements.【F:data/vesc_help_group/text_slices/input_part006.txt†L12392-L12411】

### Additional Findings (Lines 12700-14199)

#### Controllers, Dashboards & Firmware
- Makerbase’s boxed 75×100 controllers continue to ship with triple-stacked phase shunts; owners who flash the r0005 firmware strip two resistors from each sandwich to restore accurate current sensing, though the rework demands 500 °C hot air and iron heat to clear the solder.【F:data/vesc_help_group/text_slices/input_part006.txt†L12728-L12735】
- Cheap Flipsky 75100 revisions pair poorly with TFT dashes above firmware 5.02—the displays behave only on 6.0x while the controller howls and stalls—so riders are experimenting with alternate UART ports and repeated motor detection to reconcile the combo.【F:data/vesc_help_group/text_slices/input_part006.txt†L13850-L13888】
- G30 dash brake buttons stop ghost-triggering once the pull-up is dropped to ≈470 Ω; 1 kΩ parts or oversized bulk caps on the 5 V rail induce lock-mode glitches and risk overstressing the regulator.【F:data/vesc_help_group/text_slices/input_part006.txt†L13892-L13905】
- Xiaomi OEM buttons feed 36 V into the dash harness, so VESC swaps rely on resistive dividers into the 3.3 V input, occasionally adding diodes to clamp 5 V lines that float high during regen braking.【F:data/vesc_help_group/text_slices/input_part006.txt†L13908-L13935】
- Wiring brake contactors on ADC2 simply routes the switch’s positive lead into the ADC so long as the signal stays under 3.3 V; integrated dividers on some harnesses let riders safely share 5 V logic without external converters.【F:data/vesc_help_group/text_slices/input_part006.txt†L13563-L13582】
- VESC hubs on steep descents can lock if field-weakening is active—riders report that even a light brake touch at 50 km/h can freeze the wheel at the non-FW speed ceiling—so disabling FW or easing into braking prevents the skid.【F:data/vesc_help_group/text_slices/input_part006.txt†L13074-L13099】

#### Batteries & Powertrains
- A 3 L Wildman frame bag physically fits roughly 56 round cells without honeycomb spacing; builders planning 20s8p packs lean toward bespoke aluminium enclosures or internal deck extensions to reclaim volume.【F:data/vesc_help_group/text_slices/input_part006.txt†L13250-L13258】【F:data/vesc_help_group/text_slices/input_part006.txt†L13256-L13258】
- Nickel strip overheats around 8 A per cell on high-output packs, nudging experienced builders toward double-layer nickel or full copper busbars despite the higher tooling cost.【F:data/vesc_help_group/text_slices/input_part006.txt†L13287-L13295】
- Spot-welder upgrades such as the Sunko 801D or Glitter-capable rigs handle copper better than budget 801A units; veterans advise buying once or borrowing quality welders instead of fighting underpowered gear.【F:data/vesc_help_group/text_slices/input_part006.txt†L13592-L13607】
- Delivery couriers squeeze 22–30 €/h in cities where electricity is cheap, making oversized packs and reliable chargers financially worthwhile for gig riders.【F:data/vesc_help_group/text_slices/input_part006.txt†L13685-L13685】
- High-discharge builds often bypass BMS discharge FETs while retaining ~40 A charge-only boards, acknowledging that most failures happen during charging but still monitoring temperatures for safety.【F:data/vesc_help_group/text_slices/input_part006.txt†L14056-L14060】

#### Scooter Platforms & Ride Dynamics
- Kaabo hub motors are notorious for water ingress; sealing the shell seam with RTV and packing bearings with lithium grease keeps rust at bay on otherwise salvageable units.【F:data/vesc_help_group/text_slices/input_part006.txt†L12812-L12816】
- Zero 10X-class chassis ship with 52 V 18.5 Ah packs built from Samsung 32IR cells, cramped bays, laggy speedometers, and no field-weakening—owners cap at ~55 km/h until they retrofit 20s7p batteries, dampers, and VESCs.【F:data/vesc_help_group/text_slices/input_part006.txt†L13645-L13655】
- Swapping a G30 hub onto a Xiaomi frame requires reversing the Monorim fork and extending phase leads, but the transplant yields 100 km/h-class potential when paired with 20s9p packs and stout ESCs.【F:data/vesc_help_group/text_slices/input_part006.txt†L12963-L12976】【F:data/vesc_help_group/text_slices/input_part006.txt†L13964-L13970】
- Magnet codes like “60H” describe the stator magnet length in millimetres; riders mix 60H and 65H hubs (often in 22/3 windings) to balance torque and speed while targeting dual-motor upgrades.【F:data/vesc_help_group/text_slices/input_part006.txt†L14013-L14021】

#### Fabrication, Materials & Tooling
- Tinmorry PETG-CF prints emerge significantly tougher and less flexible than standard PETG thanks to real chopped fibres, whereas powder-filled blends offer little benefit; some builders even turn the parts on lathes post-print.【F:data/vesc_help_group/text_slices/input_part006.txt†L13393-L13401】
- Riders chasing copper busbars budget for Glitter or kWeld setups (plus capacitors and PSU) because cutting and welding thick copper quickly exceeds the capability of improvised tools.【F:data/vesc_help_group/text_slices/input_part006.txt†L13294-L13307】
- Controller waterproofing often devolves into scraping off thermal paste with hand tools before recoating components in silicone, but peers warn that excessive sealant can complicate later repairs.【F:data/vesc_help_group/text_slices/input_part006.txt†L13686-L13695】

#### Operations & Maintenance
- Gig riders emphasize keeping scooters compact—G30s and Xiaomi sleepers slip onto trains and buses without hassle—while oversized dual-motor platforms demand extra planning for storage and transit.【F:data/vesc_help_group/text_slices/input_part006.txt†L12950-L13024】
- Owners chasing burnout-ready performance still favour modest 20s10p-class packs with regen capability, valuing torque and thermal resilience over absolute top speed for city use.【F:data/vesc_help_group/text_slices/input_part006.txt†L14020-L14048】

### Additional Findings (Lines 14200-15699)

#### Drivetrains, Controllers & Telemetry
- Riders tracking Weped updates report that current Sonic models ship with QS hubs and Fardriver controllers, while OEMs still resist VESC adoption because low-cost BLDC controllers are simpler to deploy despite the performance trade-offs.【F:data/vesc_help_group/text_slices/input_part006.txt†L14242-L14357】
- An ESP32-2432S028 display paired with a tweaked TFT_eSPI library provides a budget VESC dash, and community members shared printable housings so the module survives scooter vibration.【F:data/vesc_help_group/text_slices/input_part006.txt†L14402-L14450】
- Makerbase 75×100 boards can run binary accessories: users bridge the throttle shunt’s red and white leads with ~10 kΩ or configure the ADC app with a pulldown so a normally-open switch maps to 0/100 % duty—handy for mower blades or fans.【F:data/vesc_help_group/text_slices/input_part006.txt†L14577-L14635】
- Xiaomi lighting mods hinge on firmware 6.05: beta builds aren’t available on macOS yet, so tinkerers port scripts that drive the rear lamp via PPM output plus a logic MOSFET because LISPy PWM helpers don’t exist.【F:data/vesc_help_group/text_slices/input_part006.txt†L14840-L14858】【F:data/vesc_help_group/text_slices/input_part006.txt†L14843-L14848】
- Makerbase’s VESC 75200 V2 earns praise as an 84 V, 200 A controller that costs roughly €105 yet handles high-power scooter builds reliably.【F:data/vesc_help_group/text_slices/input_part006.txt†L14947-L14951】
- Builders stick with JBD smart BMSs even on 20 kW projects, noting that peaks above the labelled 15 kW rarely matter and recommending ≈200 A limits for 18s7p Sony VTC6A packs to stay within safe thermal envelopes.【F:data/vesc_help_group/text_slices/input_part006.txt†L15152-L15169】
- A fresh manual details how to flash €4 WT51822 Bluetooth modules for VESC telemetry, lowering the cost of adding wireless dashboards to scooters.【F:data/vesc_help_group/text_slices/input_part006.txt†L14736-L14736】

#### Battery Construction & Safety
- Printing transparent PETG battery carriers demands drastic speed cuts (≈13 mm/s), restrained cooling, and post-polish to avoid haze—stock Bambu profiles overheat and cloud the parts.【F:data/vesc_help_group/text_slices/input_part006.txt†L14255-L14334】
- Xiaomi Pro 2 decks hide a choke point: the entry slot is narrower than the interior cavity, so 20s4p packs need extenders or careful BMS placement to slide in or out safely.【F:data/vesc_help_group/text_slices/input_part006.txt†L14427-L14433】
- Salvaged-cell sorting by hobby IR testers proves unreliable; veterans recommend spending ~€20 on a dedicated meter instead of trusting handheld ESR toys.【F:data/vesc_help_group/text_slices/input_part006.txt†L14412-L14416】
- Copper sandwich packs still favour KWeld or Glitter 811-class welders; early 811 batches suffered MOSFETs stuck “on,” so builders test on dead cells, avoid nickel-plated strip on copper, add flux only if the pack stays unsealed, and stick to ≈0.2 mm copper for consistent joints.【F:data/vesc_help_group/text_slices/input_part006.txt†L14700-L14713】【F:data/vesc_help_group/text_slices/input_part006.txt†L15172-L15224】【F:data/vesc_help_group/text_slices/input_part006.txt†L15288-L15324】
- Reports of a Blade/Teverun pack igniting despite premium branding reinforce storage discipline—never “top up” unattended packs and segregate scooters to limit collateral fire damage.【F:data/vesc_help_group/text_slices/input_part006.txt†L14738-L14752】
- New high-capacity cylindrical cells such as the teased “VX40” could displace P45B pricing once they reach the scooter aftermarket, prompting builders to monitor availability.【F:data/vesc_help_group/text_slices/input_part006.txt†L15346-L15355】

#### Fabrication, Tools & Components
- Modders removing G30 rail lips lean on ½″ belt sanders, sequential drilling with cutting fluid, and solid workbenches—steady fixturing matters more than owning a floor drill press, though metric bits still require online sourcing in the US.【F:data/vesc_help_group/text_slices/input_part006.txt†L14895-L14920】
- Compact cable locks offer no real theft deterrence; city riders treat 8 mm hardened chains as the entry point for securing high-value scooters.【F:data/vesc_help_group/text_slices/input_part006.txt†L14925-L14928】
- Zero 10X suspension pivots need lathe work or off-the-shelf bushings (≈8 mm shafts); resin printers deliver precise replacements but at the cost of slow build times.【F:data/vesc_help_group/text_slices/input_part006.txt†L15229-L15250】【F:data/vesc_help_group/text_slices/input_part006.txt†L15227-L15233】
- Magnetic pogo-pin connectors could speed VESC swaps or charging, yet builders caution that unkeyed layouts can short 200 W chargers, so designs must enforce polarity and isolation.【F:data/vesc_help_group/text_slices/input_part006.txt†L14952-L14975】

#### Builds, Waterproofing & Operations
- Converting a Xiaomi 1S to dual motors means extending the rear arm to clear the added hub, and riders warn that ditching the front brake leaves only regen plus a rear disc—unsafe for high-speed use without further upgrades.【F:data/vesc_help_group/text_slices/input_part006.txt†L14600-L14628】
- Pro 2 builders confirm 20s4p is doable with extenders while others settle for 15s4p; mixed internal/external packs must account for stem weight and balance when chasing 20s9p ambitions.【F:data/vesc_help_group/text_slices/input_part006.txt†L15330-L15345】【F:data/vesc_help_group/text_slices/input_part006.txt†L15285-L15288】
- 11×3″ tyres can mount on 6″ Monorim fronts, but the rear fit is unproven without axle extenders, so clearance checks are mandatory before ordering rubber.【F:data/vesc_help_group/text_slices/input_part006.txt†L15233-L15238】
- Zero 10X electronics boxes readily pool water; some technicians pour epoxy over ESCs and harnesses or fully resin-coat VESC swaps, supplementing with silica bags, yet continued leaks show the need for comprehensive sealing plans. Others explore 20s-capable stock ESC reflashes from specialists like Cengiz as an alternative to full VESC swaps.【F:data/vesc_help_group/text_slices/input_part006.txt†L15419-L15446】【F:data/vesc_help_group/text_slices/input_part006.txt†L15441-L15446】【F:data/vesc_help_group/text_slices/input_part006.txt†L15664-L15688】

### Additional Findings (Lines 15700-17199)

#### Controller Setup & Power Switching
- Dual-VESC conversions on G30- and Mantis-class scooters run a single dashboard over CAN; veterans call mixed setups (stock G30 controller plus one VESC) “the jankiest” route and urge flashing community firmware on Flipsky 75200 Pro units so VESC Tool recognises the hardware.【F:data/vesc_help_group/text_slices/input_part006.txt†L15766-L15769】【F:data/vesc_help_group/text_slices/input_part006.txt†L15881-L15902】
- Latest Makerbase 75200 revisions expose a VCC selector that defaults to 3.3 V for throttle/brake logic and includes SW pins that tie neatly into LLT smart-BMS “key” outputs; riders toggle the controllers daily through the BMS instead of rewiring harness power, and they prefer enabling the controller’s internal DC/DC control mode when repurposing OEM switches.【F:data/vesc_help_group/text_slices/input_part006.txt†L15801-L15835】【F:data/vesc_help_group/text_slices/input_part006.txt†L15969-L15973】
- Because 75×100 boards stay energised, installers rely on antispark switches or smart BMS precharge rather than inline deck toggles—direct battery disconnects arc Daly-class BMS FETs and can shock the controller, so builders leave the units powered or add proper MOSFET switchgear.【F:data/vesc_help_group/text_slices/input_part006.txt†L16846-L16888】
- Field-weakening on Makerbase/Flipsky 75200s remains a 60–70 A exercise even for drag builds; exceeding that envelope exacerbates heat and reliability issues.【F:data/vesc_help_group/text_slices/input_part006.txt†L16226-L16236】
- Flipsky 75100 owners bump the “max voltage” slider under Motor → General → Advanced when jumping beyond 84 V packs, keeping the firmware from hard-faulting 19s builds.【F:data/vesc_help_group/text_slices/input_part006.txt†L16841-L16845】
- VESC Express modules now bake in BLE passwords and Wi-Fi gateways for 6.xx hardware, but documentation is sparse, prompting calls for clearer setup guides when securing scooters against opportunistic Bluetooth pairing.【F:data/vesc_help_group/text_slices/input_part006.txt†L17011-L17019】
- Vsett owners can keep the stock dash by loading the community script or fall back to 10 kΩ NTCs tied between hall-ground and an extra conductor to log motor temperatures on dual builds.【F:data/vesc_help_group/text_slices/input_part006.txt†L16973-L16976】

#### Batteries, Cells & Connectors
- High-output commuters still find 300 A smart BMS units cost-prohibitive; many settle on LLT’s 100 A models for 20s8p dual-80100 builds, pairing them with winter sales to stretch budgets.【F:data/vesc_help_group/text_slices/input_part006.txt†L15977-L15989】
- Budget BAK 2600 mAh cells surface for Xiaomi conversions at ~€0.50, but the community flags their ~40 mΩ IR and limits them to ~20 A loads or light riders to avoid premature sag.【F:data/vesc_help_group/text_slices/input_part006.txt†L16020-L16028】
- When calculators spit out 300+ A targets, builders abandon twin XT90 leads for QS8 antisparks, 4 AWG cabling, and ring terminals—XT90s stay relegated to charging ports and sub-100 A cruise loads.【F:data/vesc_help_group/text_slices/input_part006.txt†L16088-L16134】
- Copper-and-nickel sandwiches continue to be the go-to for ≥20 kW packs: Glitter 811-class welders need tuning around 0.1–0.2 mm copper with 0.15 mm nickel backers, while thicker strip simply splatters or deforms cells.【F:data/vesc_help_group/text_slices/input_part006.txt†L16593-L16619】
- Turkish Aspilsan 18650 cells (2.9 Ah, ~25 A pulse) are entering Zero 10X battery upgrades; builders still cap continuous draw around 15–20 A per cell to respect their 5 C rating.【F:data/vesc_help_group/text_slices/input_part006.txt†L16993-L17009】

#### Scooter Platforms, Components & Maintenance
- Zero 10X frames earn criticism for cramped decks, weak sealing, and suspect welds—riders in wetter climates now default to Vsett 10+ or G30 platforms unless they plan full chassis overhauls with custom stems, packs, and UBox controllers.【F:data/vesc_help_group/text_slices/input_part006.txt†L15920-L15959】
- Zero-branded tube tires reportedly “always explode”; importing replacement motors into Turkey remains difficult, so riders experiment with 50H hubs, custom forks, and even bespoke suspension to keep Ninebot conversions rolling.【F:data/vesc_help_group/text_slices/input_part006.txt†L16175-L16199】
- Cleanly restoring rusted Kaabo hub motors is feasible with mechanical abrasion, IPA rinse, and fresh silicone sealing—an example build documents before/after photos after extensive brushing and drying.【F:data/vesc_help_group/text_slices/input_part006.txt†L16370-L16405】
- Community machinists are considering bespoke torque washers and stem bushings for 50H/65H motors; until then, builders keep scanning AliExpress for M14 hardware while planning CNC batches to stop axle spin-out.【F:data/vesc_help_group/text_slices/input_part006.txt†L16442-L16461】

#### Fabrication, Tools & Safety Culture
- Riders warn that adding deck fans or open air scoops to Burn-E class scooters invites water ingress; sealed housings plus precharge discipline beat ad-hoc cooling hacks.【F:data/vesc_help_group/text_slices/input_part006.txt†L16908-L16910】
- Metal-milled decks remain rare because billet machining adds cost without measurable strength gains—proper welding and reinforcement plates stay the realistic path for titanium or aluminium frames.【F:data/vesc_help_group/text_slices/input_part006.txt†L16962-L16969】
- Makers chasing battery craftsmanship invest in proper lathes or enlist machine shops rather than improvising drill presses, acknowledging the precision required for spacers, bushings, and copper tooling.【F:data/vesc_help_group/text_slices/input_part006.txt†L16231-L16247】

#### Powertrains & Voltage Planning
- Racers continue to debate pack voltage: while 21s setups are theoretically fine if every component is rated, veterans still recommend 20s for easier charger sourcing and fewer exotic parts.【F:data/vesc_help_group/text_slices/input_part006.txt†L17022-L17059】
- Spintend dual-200A boxes underperform compared with single 250A units in some builds, reinforcing the value of right-sizing controllers rather than doubling lower-spec hardware.【F:data/vesc_help_group/text_slices/input_part006.txt†L16836-L16840】

### Additional Findings (Lines 17200-18699)

#### Controllers, Power & Cooling
- Nucular 12F owners report the onboard auxiliary rail cannot sustain 60 W headlights—large loads triggered random shutdowns until they added an isolated supply—and they remind newcomers the platform is still warrantied only around 20 s/100 V despite its protections, so VESC swaps remain attractive for higher-voltage scooters.【F:data/vesc_help_group/text_slices/input_part006.txt†L17234-L17244】
- The same crowd explains Nucular’s “charge through the ESC” trick: feed a lower-voltage source through the hub motor windings to use them as a transformer, a capability that predated affordable >20 s chargers but now requires careful documentation.【F:data/vesc_help_group/text_slices/input_part006.txt†L17245-L17250】
- Builders demonstrate that VESCs can stage low/high brake lighting with a simple dual-relay module—one relay drops a resistor for running lights while the other drives the brake circuit—matching the flexibility riders sought on Nucular setups.【F:data/vesc_help_group/text_slices/input_part006.txt†L17388-L17389】
- Flipsky 75200 Pro users chasing >60 A motor current on 65 H hubs found the motors jerking until they reran detection with the hub-motor template and halved observer gain/sensorless ERPM targets; afterwards, the drivetrain pulled smoothly at higher amp limits.【F:data/vesc_help_group/text_slices/input_part006.txt†L17619-L17635】【F:data/vesc_help_group/text_slices/input_part006.txt†L17950-L17953】
- Water-cooled Flipsky 75350s need the intended plumbing—an inlet at the nose, optional pump, and rear outlet—because bolting the plate to another heat spreader kills transfer efficiency; the design suits power-hungry e-foils that already bathe the hull in 20 °C water.【F:data/vesc_help_group/text_slices/input_part006.txt†L17705-L17735】
- When clamping ESCs to metal decks, riders favour thermal paste over pads to maximise contact and keep controller temperatures down.【F:data/vesc_help_group/text_slices/input_part006.txt†L17994-L17996】

#### Battery Construction & Cells
- High-power pack builders stack 0.1 mm copper with 0.15 mm overlays (or copper/nickel sandwiches) to chase 320–800 A draws, noting their cells can output ~900 A continuous even if the smart BMS only tolerates 800 A for 30–60 s bursts.【F:data/vesc_help_group/text_slices/input_part006.txt†L17365-L17381】
- Glitter 801/811 welders will join 0.1–0.2 mm copper if you cap it with nickel or plated steel; running pure copper alone either fails or blows holes, so most crews still finish with nickel top plates for strength.【F:data/vesc_help_group/text_slices/input_part006.txt†L17273-L17297】
- Riders distrust marketing that rates P42A/P45B cells at 45 A continuous—real-world packs hover near 30–38 A per cell, demand temperature sensors, and benefit from potting when scooters only see a few seconds of full load outside 100 km/h runs.【F:data/vesc_help_group/text_slices/input_part006.txt†L17427-L17466】
- Upgrading commuter bikes from 13 s 6 p 35E bricks to 20 s 5 p high-discharge packs nets roughly 60 % more capacity and less voltage sag, with riders planning spare modules to maintain agility.【F:data/vesc_help_group/text_slices/input_part006.txt†L17489-L17498】
- Xiaomi Pro 2 builders have confirmed the deck swallows 12 s 8 p (≈96 cells) and even accommodates dual QS8 battery leads when honeycomb inserts are removed, though packing tight radii with 6 AWG requires careful routing.【F:data/vesc_help_group/text_slices/input_part006.txt†L17551-L17563】
- Some race-style scooters run charge-only ANT 40 A BMS boards while bypassing discharge FETs, relying on thermal monitoring when letting individual cells momentarily touch 40 A apiece.【F:data/vesc_help_group/text_slices/input_part006.txt†L17980-L17985】

#### Motors & Drivetrains
- Community logs confirm stock Vsett hubs have survived 10–12 kW pushes, and dual Nucular 12F builds peaked around 14 kW before controller limits intervened.【F:data/vesc_help_group/text_slices/input_part006.txt†L17229-L17236】
- Lonnyo 70 H-class motors hold roughly 12 kW without overheating, yet even 350 A battery limits struggle to break rear traction on 33×2 windings—front tyres still spin first during burnout attempts.【F:data/vesc_help_group/text_slices/input_part006.txt†L17524-L17535】
- Laotie 60 H hubs use ~50 mm magnets and claim ~4.5 kW ratings; Vsett 10 motors share the 50 mm stator and bolt into G30 swingarms, but there is still no tubeless 10″ variant, pushing riders toward heavier 11″ upgrades.【F:data/vesc_help_group/text_slices/input_part006.txt†L17666-L17679】
- Zero 10X motors run lower-kV, torque-focused windings than Vsett 10+ hubs, so swapping between the two platforms changes both top speed and feel despite similar axle widths.【F:data/vesc_help_group/text_slices/input_part006.txt†L17990-L17992】

#### Lighting, Visibility & Accessories
- High-mounted scooter headlights can dazzle low cars; even when beam patterns look focused, riders double-check aim to avoid blinding traffic.【F:data/vesc_help_group/text_slices/input_part006.txt†L17626-L17633】
- Veterans steer commuters toward Magicshine and other certified lamps, judging setups by lux instead of headline lumens after measuring “25 W” AliExpress units pulling only ~18 W at 12 V (and surviving brief 48 V feeds).【F:data/vesc_help_group/text_slices/input_part006.txt†L17846-L17851】

#### Riding Practices & Regulations
- Running 70–80 km/h on rigid G30 builds is considered feasible only on smooth, well-known roads; riders stress wearing full gear because any unexpected bump will send a stiff chassis “Superman” over the bars.【F:data/vesc_help_group/text_slices/input_part006.txt†L17633-L17657】
- Bolt-on saddles remain uncomfortable on stand-up scooters and raise the bars, so most testers abandon seated riding after short Xiaomi Pro trials.【F:data/vesc_help_group/text_slices/input_part006.txt†L17338-L17342】
- Enthusiasts expect tighter enforcement as highway antics increase, with some regions already signalling 2027 timelines for broader regulation updates.【F:data/vesc_help_group/text_slices/input_part006.txt†L17362-L17363】【F:data/vesc_help_group/text_slices/input_part006.txt†L17937-L17939】

#### Connectors, Maintenance & Consumables
- Builders increasingly adopt QS8/QS10/QS12 antispark connectors to carry 110–200 A+, even stuffing dual 12 AWG or 6 AWG leads per shell, while relegating XT30/XT90 hardware to sub-100 A duties.【F:data/vesc_help_group/text_slices/input_part006.txt†L17557-L17568】【F:data/vesc_help_group/text_slices/input_part006.txt†L17884-L17904】
- After resealing enclosures with custom gaskets, riders pressure-wash their decks to confirm waterproofing before road use.【F:data/vesc_help_group/text_slices/input_part006.txt†L17871-L17888】
- Xiaomi fleet mechanics recommend CST V3 tyres (and avoid soft nylon/Xuan patterns) to stop repeat blowouts, sourcing them cheaply via Alibaba when local stock dries up.【F:data/vesc_help_group/text_slices/input_part006.txt†L17920-L17929】
- QS12 anti-spark connectors are emerging as the next step for extreme current builds thanks to their larger contact area and reduced heat rise.【F:data/vesc_help_group/text_slices/input_part006.txt†L17948-L17952】

## Follow-Up Tasks
- Document a repeatable wiring guide (with photos) for flipping RX/TX and adding 5 V filtering when migrating Makerbase dashboards between controller families.
- Capture precise G30 deck measurements and reinforcement plate CAD to support 130 kg riders without cracking the rear cut-outs.
- Validate Ninebot/Xiaomi BMS charge-current enforcement by logging real-time input current across 2 A–6 A chargers.
- Compile an aluminium deck reinforcement playbook (bolt patterns vs. TIG welding, required tooling, PPE) for Laotie/G30 aftermarket frames.
- Analyse 3Shul CL350 failure reports to establish safe voltage headroom for 30 s EUC packs and document mitigation steps.
- Produce a connector prep guide for Spintend 85/200 controllers covering micro-signal crimping and twin-10 AWG termination into 8 mm bullets.
- Release an updated Monorim front spacer/extender design (STL + instructions) that clears Sokil clamps without sacrificing the folding lock.
- Write a tuning note on using `iQ target` and similar torque-boost features without tripping pack BMS protections on commuter packs.
- Document a Makerbase 75100 constant-RPM configuration for lawn equipment or other on/off applications, including safety interlocks.
- Publish a Ninebot F2 Pro front-hub service guide covering bearing regreasing, grease selection, and reassembly checks.
- Assemble a city locking and anti-theft checklist for high-value scooters, including physical deterrents and storage practices for Paris-class environments.
- Draft wiring instructions for integrating Magicshine ME-STVZO 100 lux lights (or similar 6–12 V units) with the VESC 12 V accessory rail and brake signalling.
- Capture a photo-led rework guide for the Makerbase boxed 75×100 shunt “sandwich,” including resistor removal order and post-mod firmware settings.
- Produce a troubleshooting matrix for Flipsky 75100 + TFT pairings above firmware 5.02, covering UART port swaps, detection reruns, and known working firmware mixes.
- Publish a G30 dash brake-button wiring note that specifies resistor values, filtering options, and safe 5 V rail capacitance limits when integrating with VESCs.
- Write a flashing guide for WT51822-based Bluetooth modules that documents pinouts, firmware steps, and recommended housings for reliable VESC telemetry.
- Compile a Glitter/kWeld safety checklist outlining dead-cell pretests, acceptable copper thicknesses, and mitigation steps for stuck-MOS batches.
- Produce a Zero/Blade waterproofing playbook covering epoxy potting, silica placement, and evaluation of 20s-ready stock ESC services versus VESC swaps.
- Map the Xiaomi Pro 2 battery bay choke point and capture extender/BMS packaging templates for internal 20s builds.
- Draft an LLT smart-BMS key-mode wiring note for Makerbase 75×100 controllers, covering SW-pin use and safe precharge practices.
- Produce an amperage-to-connector sizing cheat sheet (XT90 vs QS8, recommended wire gauges, ring terminals) for 300 A-class scooter builds.
- Capture Glitter/811 welder tuning profiles for copper/nickel sandwiches to reduce blow-through on high-power battery packs.
- Draft a Nucular auxiliary-power retrofit note that shows how to offload ≥60 W lighting loads to isolated supplies without tripping the controller.【F:data/vesc_help_group/text_slices/input_part006.txt†L17234-L17244】
- Create a Flipsky 75200 Pro diagnostic guide covering observer-gain and sensorless-ERPM tuning when hub motors jitter above 60 A.【F:data/vesc_help_group/text_slices/input_part006.txt†L17619-L17635】【F:data/vesc_help_group/text_slices/input_part006.txt†L17950-L17953】
- Summarise CST V3 sourcing and upkeep tips for Xiaomi/M365 fleets replacing failure-prone OEM tyres.【F:data/vesc_help_group/text_slices/input_part006.txt†L17920-L17929】
