# input_part013.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part013.txt`
- Coverage:
  - Batch 1: 2025-06-04T18:16:49 through 2025-06-06T22:55:51 (lines 1-1135)
  - Batch 2: 2025-06-07T00:00:56 through 2025-06-10T23:33:08 (lines 1136-2200)
  - Batch 3: 2025-06-10T23:33:49 through 2025-06-15T00:40:45 (lines 2201-3700)
  - Batch 4: 2025-06-15T18:32:54 through 2025-06-20T06:07:53 (lines 3701-5200)
  - Batch 5: 2025-06-20T06:07:54 through 2025-06-26T15:05:55 (lines 5201-6700)
  - Batch 6: 2025-06-26T15:30:52 through 2025-06-30T10:53:03 (lines 6701-8200)
- Next starting point: line 8201 (2025-06-30T10:53:17 and later)

## Key Findings

### Field-Weakening Behaviour & Phase Current Expectations
- Stone Gasm only gained ≈19 km/h of freewheel speed by adding 25 A of field weakening (66 → 84 km/h), and even at the 35 A hardware ceiling the setup topped out near 96 km/h on a 20×70 kv motor—pointing to diminishing returns or configuration limits that need deeper tuning.【F:data/vesc_help_group/text_slices/input_part013.txt†L30-L31】
- Pandalgns reminded builders that high launch torque is tied to phase current; as speed rises and load drops, the controller naturally pulls phase amps back toward the battery limit, so staged limits or higher battery amperage are the usual levers for extending the strong-acceleration window.【F:data/vesc_help_group/text_slices/input_part013.txt†L356-L357】
- ✨🇪🇸عمر laid out his dual-motor baseline at 180 A battery / 270 A phase on the rear and 150 A / 250 A up front, noting that the back hub already hints at thermal stress—while A.P. is testing 220 A phase, 280 A absolute and 30 A of FW for further benchmarking.【F:data/vesc_help_group/text_slices/input_part013.txt†L2267-L2270】【F:data/vesc_help_group/text_slices/input_part013.txt†L2405-L2407】
- Yamal later dialed his own configuration down to 150 A battery / 250 A phase per controller after a Ubox shutdown that he attributes to debris intrusion rather than overcurrent, underscoring the need to harden exposed enclosures when running outdoor tests.【F:data/vesc_help_group/text_slices/input_part013.txt†L3362-L3375】

### Ninebot G2 Conversion Roadmap
- Jose is selling an Ice Q to finance a Ninebot G2 Max on VESC control: target configuration is a single Q5 Evo rear hub, Magura MT7 caliper with Shimano Deore lever, and a 20 S 6 P Molicel battery aimed at “definitive” performance without registration or insurance costs.【F:data/vesc_help_group/text_slices/input_part013.txt†L202-L214】【F:data/vesc_help_group/text_slices/input_part013.txt†L205-L214】
- Unlocking the stock firmware likely hinges on an ST-Link V2; Jose is confident it can derestrict the controller but still needs guidance on the process.【F:data/vesc_help_group/text_slices/input_part013.txt†L221-L226】 
- Weight balance keeps the build single-motor: Jose wants lighter steering and easier wheelies, while recommending Monorim forks with an EXA damper (all M6 hardware) for the front end and reattaching the OEM mudguard with a simple two-bolt/two-sleeve bracket plus a 3D-printed support after VESC swaps.【F:data/vesc_help_group/text_slices/input_part013.txt†L230-L233】【F:data/vesc_help_group/text_slices/input_part013.txt†L337-L343】【F:data/vesc_help_group/text_slices/input_part013.txt†L586-L588】
- Diego is already running 16 S on the stock controller by uprating its capacitors and plans to evaluate 18–20 S VESC electronics once he confirms the pack volume the compartment can accept.【F:data/vesc_help_group/text_slices/input_part013.txt†L343-L346】
- Smart Repair flagged that GT/G2 swingarms cap out around 125 mm dropouts and can swallow roughly 208 cells before major chassis surgery, setting expectations for higher-voltage conversions.【F:data/vesc_help_group/text_slices/input_part013.txt†L514-L516】【F:data/vesc_help_group/text_slices/input_part013.txt†L535-L538】
- ‘lekrsu’ confirmed you can stretch the Max G2 rear from 115 mm to roughly 150 mm by swapping in ≈10 mm bushings and longer shoulder bolts, keeping the stock screws but relying on softer bushings (e.g., copper/brass) so the frame tabs don’t gall themselves.【F:data/vesc_help_group/text_slices/input_part013.txt†L2733-L2749】

### Controller, Motor & Wiring Upgrades
- LonnYo’s 65H 17×4 hub remains the go-to motor recommendation; ‘lekrsu’ advises contacting the factory via its website or WhatsApp (or ordering through James) to secure custom wind options.【F:data/vesc_help_group/text_slices/input_part013.txt†L348-L353】
- Smart Repair’s Tronic X12 build runs 24 S for just under 30 kW peak, while Rob Ver highlights that the X12 and Ubox 240 share 331 A MOSFETs (four per phase) and that he caps his 80H motor at 200 A battery / 310 A phase, keeping a 70H at 190 A/190 A to respect the silicon limits.【F:data/vesc_help_group/text_slices/input_part013.txt†L364-L369】
- Legacy 85250 controllers tolerated 150 A battery and 360 A phase for Smart Repair, but the current X12 logic rail only supplies 5 V at 150 mA—insufficient for some peripherals without a separate step-down stage.【F:data/vesc_help_group/text_slices/input_part013.txt†L370-L371】【F:data/vesc_help_group/text_slices/input_part013.txt†L474-L475】
- Rob swapped Nami phase leads to 10 AWG after melting the factory harness, now running 116 A battery and 240 A phase without the previous overheating, reinforcing the case for heavier-gauge wiring in high-power builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L475-L486】
- Builders debating Ubox and Tronic FET swaps noted that higher-spec Infineon “tolt” packages should be paired with larger input capacitors to keep thermal performance under control when stretching to 22 S installs.【F:data/vesc_help_group/text_slices/input_part013.txt†L412-L423】
- Mixing Thunder 2 controllers (60 A rear, 45 A front) is workable: Jose and Noname confirm speed stays voltage-limited, though total thrust drops and matching shunt mods or sourcing a second 60 A board may be preferable.【F:data/vesc_help_group/text_slices/input_part013.txt†L544-L556】【F:data/vesc_help_group/text_slices/input_part013.txt†L551-L555】

### MakerBase & Peripheral Integration Lessons
- Rogerio Figueiredo’s MakerBase 75200 (running FW 6.05) would not feed telemetry to his Flipsky display until he experimented with power sequencing; he ultimately revived the screen but warns that applying 5 V before 12 V repeatedly nuked two Spintend ADC daughterboards.【F:data/vesc_help_group/text_slices/input_part013.txt†L2375-L2387】【F:data/vesc_help_group/text_slices/input_part013.txt†L3190-L3193】
- Smart Repair suggested bypassing the finicky Flipsky unit entirely by flashing the open-source ESP32 “SimpleVescDisplay” project and 3D-printing its handlebar mount, offering a more controllable telemetry stack.【F:data/vesc_help_group/text_slices/input_part013.txt†L2923-L2924】
- Noname recapped the MakerBase harness mapping—NRF header for Bluetooth, the Hall plug for motor sensors, power button leads to the switch, and the comm port supplying 3.3 V/GND/ADC1 for throttles—while Pandalgns confirmed the typical red/black/signal wiring for hall throttles into ADC1.【F:data/vesc_help_group/text_slices/input_part013.txt†L2797-L2797】【F:data/vesc_help_group/text_slices/input_part013.txt†L2925-L2926】

### Tires, Tubes & Ride Prep
- Noname credits Ulip tubes dusted with baby powder—and a “no burnouts” policy—for limiting punctures to three flats in four years, whereas haku still prefers tubeless and warns manual pumps struggle to seat beads without powered assist.【F:data/vesc_help_group/text_slices/input_part013.txt†L595-L608】
- Arsenus Pro adds that tubeless feasibility is rim-specific: G30 rims with Chaoyang tires are difficult to seal, but Bolt-hub conversions with Ulip rubber seat cleanly.【F:data/vesc_help_group/text_slices/input_part013.txt†L609-L611】

### Battery Sourcing & Pack Logistics
- Vapcell’s EVE 40PL pricing sits near €2.2 per cell with DHL shipping quoted at ~€150 to Germany (≈€229 to Switzerland) and 3–5 day delivery when stock is available, though air shipments can fluctuate based on factory inventory.【F:data/vesc_help_group/text_slices/input_part013.txt†L890-L899】【F:data/vesc_help_group/text_slices/input_part013.txt†L933-L999】
- NKON remains the premium option thanks to matched production batches and documentation that simplify tax handling, whereas Vapcell orders can mix manufacture dates and voltages—necessitating individual top-ups with chargers like the Miboxer C4 before assembly.【F:data/vesc_help_group/text_slices/input_part013.txt†L925-L971】
- Jose can source lightly-used Molicel P45B cells at roughly €1.2 each from Stark Varg motorcycle packs, offering an alternative for budget builds if the long-term health checks pan out.【F:data/vesc_help_group/text_slices/input_part013.txt†L1030-L1036】
- Rob Ver urges a pivot to tabless cell formats to cut internal resistance; his pack reportedly runs only ~3 °C above ambient after hard riding, underscoring the thermal gains available from newer cell tech.【F:data/vesc_help_group/text_slices/input_part013.txt†L1037-L1041】
- Pandalgns is mid-way through a Halo Knight T107 Pro refresh with dual MKS 84200HPs, 22 S 10 P P45B packs, and HM 3000 W 60 H hubs re-loomed with 12 AWG leads—highlighting the packaging headroom once the swingarm is spaced out for 150 mm dropouts.【F:data/vesc_help_group/text_slices/input_part013.txt†L3150-L3168】

### Tooling Questions & Troubleshooting Watchlist
- Basti hit repeated VESC Tool 6.06 motor setup wizard errors on HW No-Limit hardware and is seeking root-cause guidance.【F:data/vesc_help_group/text_slices/input_part013.txt†L169-L170】
- Martin Kaktits needs axle-friendly insulation alternatives to PTFE for 6 mm² phase leads; the community hasn’t supplied a tested substitute yet.【F:data/vesc_help_group/text_slices/input_part013.txt†L172-L172】
- Pandalgns initially logged a “Serial port error” and flickering power after a smoky startup—symptoms later tied to the hall-board short detailed in Batch 2; note the pattern for future diagnostics.【F:data/vesc_help_group/text_slices/input_part013.txt†L1107-L1108】【F:data/vesc_help_group/text_slices/input_part013.txt†L1673-L1675】
- Smart Repair is evaluating MakerBase Express boards but notes the apparent lack of a WiFi antenna out of the box, which could limit remote telemetry unless an add-on is identified.【F:data/vesc_help_group/text_slices/input_part013.txt†L1112-L1112】

### Batch 5 Highlights (lines 5201–6700)

#### Safety, Controls & Telemetry Reminders
- S1m 0n reiterated that hall throttles should never exceed ≈3.3 V at the signal pin—3.5 V is already flirting with the MCU’s ADC ceiling—so builders need to meter their throttles and adjust resistor ladders before plugging into MakerBase or Ubox hardware.【F:data/vesc_help_group/text_slices/input_part013.txt†L5211-L5213】
- After haku’s car crash, Noname reminded everyone that regen braking only works properly when the BMS “charge” path is enabled, a subtlety that can leave scooters with weak e-brakes if the charge FET is open.【F:data/vesc_help_group/text_slices/input_part013.txt†L5489-L5491】
- Smart Repair dropped a fresh G2↔VESC bridge demo, signalling that the adapter hardware for swapping Ninebot dashboards over to CAN is now field-ready.【F:data/vesc_help_group/text_slices/input_part013.txt†L5620-L5621】
- Yamal is targeting 150–175 A battery and 250–300 A phase per controller on his G2 Max once the bridge is in play, underscoring the need for a proper telemetry workflow before he leans on those limits.【F:data/vesc_help_group/text_slices/input_part013.txt†L5655-L5658】
- Yamal also discovered that CAN-bus summaries in VESC Tool aggregate both controllers, making it hard to view per-side data when each hub is near 250 A—he’s looking for a way to expose individual stats on dual-stack builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L6488-L6493】

#### Motors, Controllers & Build Planning
- Rogerio and Arnau compared Dualtron Victor and Vsett 10 hubs, agreeing that the Victor’s 45 H wind favours RPM while the Vsett stator delivers more torque—useful context for pairing with a MakerBase 75200 when chasing 95–100 km/h on 72 V packs.【F:data/vesc_help_group/text_slices/input_part013.txt†L5254-L5271】
- Mattia reported that dual Ubox 85240 controllers on a Wolf King GT frame happily pull up to 350 A phase when fed by a 54 Ah P42A pack, but the front dropout caps him at 140 mm, forcing a smaller 70 H front hub until he reworks the chassis.【F:data/vesc_help_group/text_slices/input_part013.txt†L6163-L6176】
- Face de Pin Suce shared specs for the 37.2 kg RM-Light: C350 drivetrain, 22 S 4 P tabless battery, RM-X 2024 rear motor, smaller front hub, Beringer BR4VE brakes, and ≈25 kW top output (130–140 km/h) despite the compact pack—solid benchmarking for ultralight race builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L6333-L6334】
- skrtt relayed that Spanish Thunder builds are hitting 140 km/h using 22 S 11 P P45B packs with 100/75 A battery and 250/220 A phase on G300 hardware, indicating what local teams are squeezing out of high-voltage setups.【F:data/vesc_help_group/text_slices/input_part013.txt†L6654-L6684】

#### Firmware, Displays & Accessory Wiring
- Chen Simhony is hunting for the 6.06 beta firmware for dual 75100s and wants confirmation that the G2 bridge works with Flipsky hardware, signalling follow-up firmware packaging work for that stack.【F:data/vesc_help_group/text_slices/input_part013.txt†L5627-L5634】
- Rogerio finally stabilised his Flipsky Voyage display by moving telemetry leads from TX/RX to the secondary TX2/RX2 headers on the MakerBase board—he notes the harness was miswired on his first attempt and that the replacement leads are short enough to need extensions.【F:data/vesc_help_group/text_slices/input_part013.txt†L6220-L6227】
- Anthony Meza is exploring Spintend Spinny throttles and Davega displays; he now understands the RX/TX wiring and appreciates that the Rion CNC throttle he’s emulating is just a hall unit in premium housing, which should temper expectations about performance gains from hardware swaps alone.【F:data/vesc_help_group/text_slices/input_part013.txt†L6065-L6114】【F:data/vesc_help_group/text_slices/input_part013.txt†L6363-L6377】
- Mirono is diagnosing a throttle that spikes to ~2 V only during VESC boot, suggesting the need for better filtering or shielding around ADC1 when controllers initialise peripherals.【F:data/vesc_help_group/text_slices/input_part013.txt†L6378-L6381】

#### Battery, Regen & Thermal Notes
- Nobrrr urged everyone to refresh the community battery reference with modern high-power cells (EVE 40PL/50PL, Molicel P50B, BAK 45D), while Patrick vouched for Mooch’s lab data, reinforcing our need to curate an up-to-date power-cell table.【F:data/vesc_help_group/text_slices/input_part013.txt†L5661-L5666】
- Haku walked Anthony through estimating pack limits on a Samsung 48G-based 20 S 8 P battery—roughly 150 A continuous before BMS bottlenecks—before steering him toward dual Spintend 85/150 controllers for a 10 kW K-Cloud scooter, pending confirmation of the pack’s discharge spec.【F:data/vesc_help_group/text_slices/input_part013.txt†L6065-L6200】
- S1m 0n is experimenting with ferrofluid and found that overfilling overheats the motor; only a hair-thin film between magnets is needed, as Paolo and Arnau reminded him to chase torque by increasing phase current (up to ~120 A with a 150 A absolute) when the MakerBase 84100 feels weak off the line.【F:data/vesc_help_group/text_slices/input_part013.txt†L6230-L6247】
- cihan’s headset stiffened after carbon paste contaminated the bearing; 🇪🇸AYO#74🏁 recommends cleaning and re-greasing or swapping bearings entirely, highlighting that friction modifiers can masquerade as dampers but eventually chew up the races.【F:data/vesc_help_group/text_slices/input_part013.txt†L6526-L6533】

#### Open Questions & Troubleshooting Watchlist
- S1m 0n is still waiting on clarity about VESC Tool backup formats (XML vs C vs UUID) so he knows which files to export for disaster recovery.【F:data/vesc_help_group/text_slices/input_part013.txt†L5211-L5211】
- Adrian Geanca wants best practices for linking four VESCs over CAN on a 4WD platform, including power-switch sequencing for the 75100 Pro v2 units.【F:data/vesc_help_group/text_slices/input_part013.txt†L6072-L6074】
- chris needs a method to invert his MakerBase 84100HP key-switch logic because the hardware closes opposite of the desired direction, and rewiring alone didn’t help.【F:data/vesc_help_group/text_slices/input_part013.txt†L6685-L6688】
- Patrick’s MP2 v0.6 build is reporting incorrect pack voltage even after he rechecked for shorts and flashed firmware, so we should audit the sense-divider calibration or known errata before he rides it.【F:data/vesc_help_group/text_slices/input_part013.txt†L6691-L6695】
- Mirono’s noisy throttle-at-boot behaviour (above) remains unresolved and deserves a deeper dive alongside shielding guidance.【F:data/vesc_help_group/text_slices/input_part013.txt†L6378-L6381】

### Batch 4 Highlights (lines 3701–5200)

#### Dual MakerBase Amp Budget & Thermal Watchouts
- ✨🇪🇸عمر confirmed his Nami Viper is running paired MakerBase 100 A controllers at 200 A battery / 310 A phase (380 A ABS) per hub, while warning that the pack is already flirting with heat soak—evidence that the dual stack can deliver ~400 A battery and 620 A phase combined if the battery and cooling cooperate.【F:data/vesc_help_group/text_slices/input_part013.txt†L3707-L3734】
- The crew reiterated that big 22×3 builds can keep 300 A phase / 200 A battery on a single hub without immediate drama, but thermal headroom is the gating factor—haku still wants denser packs (adding another parallel group) before pushing the combination harder.【F:data/vesc_help_group/text_slices/input_part013.txt†L4491-L4500】【F:data/vesc_help_group/text_slices/input_part013.txt†L5168-L5170】

#### App/Motor Configuration Persistence Tips
- Matthew re-explained the VESC Tool workflow—always click **Read**, edit, then **Write** (M for motor, A for app)—after multiple riders noted their throttle limits reverting; Anthony’s runaway-on-stand incident underscores how skipping the write step or hitting “Default” can reset safety-critical current caps.【F:data/vesc_help_group/text_slices/input_part013.txt†L4112-L4127】
- Noname and Pandalgns reminded newcomers to record throttle min/max voltages and verify live ADC readings before blaming hardware when inputs feel unresponsive.【F:data/vesc_help_group/text_slices/input_part013.txt†L4110-L4115】

#### 12 V Accessory Power & Lighting Questions
- francois schempers is feeding a 2.5 A headlight from dual 12 V outputs; ‘lekrsu’ suspects both taps land on the same buck, warned that 30 W is aggressive, and suggested continuity checks before paralleling them.【F:data/vesc_help_group/text_slices/input_part013.txt†L4085-L4103】
- haku asked whether 12 V tail and brake lights can be driven from the Spintend “Spinny” ADC v2 harness, leaving the compatibility details unresolved for now.【F:data/vesc_help_group/text_slices/input_part013.txt†L5127-L5127】

#### External Battery Pairing Debate
- cihan is drafting a high-capacity parallel pack (small internal C-rate plus larger 2 C external) and floated using an ideal diode to block backflow; Noname countered that matching voltages and direct paralleling typically self-balances within ~1 A, and cautioned that regen current simply splits between packs—limiting total regen to the sum of both batteries remains the safer lever.【F:data/vesc_help_group/text_slices/input_part013.txt†L5118-L5136】
- Noname’s own tests on mismatched 17 S/16 S packs showed throttle cutouts when an ideal diode was inserted, nudging the team toward either pre-balancing or accepting light equalization currents instead of diode blocks.【F:data/vesc_help_group/text_slices/input_part013.txt†L5133-L5136】

#### Marketplace & Component Notes
- Lisa listed a 22×3 60 H hub with PMT 10×3 tires for €200, reporting 81 km/h on 20 S/80 A and describing it as a medium-KV compromise between 16×4 and 33×2 options; S1m 0n pressed for axle thread specs (likely M14 from LY/Phobeliu), and Lisa flagged that some mounting screws are missing.【F:data/vesc_help_group/text_slices/input_part013.txt†L4929-L4947】
- Follow-up chat confirmed the motor uses LY’s Phoebeliu sister brand, includes a temp sensor, and currently has shortened phase leads from prior duty in a G30 rear arm—useful fitment caveats for prospective buyers.【F:data/vesc_help_group/text_slices/input_part013.txt†L5100-L5114】

#### Project Updates & Safety Gaps
- Arnau Martinez Casals just finished a 16 S single-motor daily using a 100 V 100 A controller, testing 90 A phase / 130 A ABS on a 17×4 50 H hub, and is seeking guidance on the true safe ceiling—data we should collect before he leans harder on the Victor pack.【F:data/vesc_help_group/text_slices/input_part013.txt†L4996-L5002】
- haku continues to flog the Peak G30V2: dual Ubox 100 V (v2) controllers on a 20 S 3 P pack, no mechanical brakes yet (only dual-way e-brake throttles), and plans for a future 22×3 dual-motor frame once he adds Magura MT5 hardware—flagging a critical safety gap while the current frame relies on sandals-and-regen stops.【F:data/vesc_help_group/text_slices/input_part013.txt†L5155-L5199】

### Batch 6 Highlights (lines 6701–8200)

#### Controller Assembly & Power Interfaces
- 🇪🇸AYO#74 reminded newcomers to start conservatively—e.g., 100 A phase / 120 A absolute—and to tailor VESC parameters to their specific battery, voltage, and motor data to prevent avoidable hardware damage.【F:data/vesc_help_group/text_slices/input_part013.txt†L6701-L6702】
- Patrick’s MP2 build thread highlighted common bring-up checks: verify that no passives are missing, confirm the 5 V and 3.3 V rails stay solid while spinning, probe the 12 V buck input from the top side, and double-check the VIN-sense path if current draw looks off.【F:data/vesc_help_group/text_slices/input_part013.txt†L6703-L6755】
- Dualtron Achilleus found the G300’s power button harness only uses three leads on UART2; 🇪🇸AYO#74 advised repinning four-wire Spintend switches to 5 V/SW/GND and configuring the on/off logic inside the controller menu.【F:data/vesc_help_group/text_slices/input_part013.txt†L6855-L6874】【F:data/vesc_help_group/text_slices/input_part013.txt†L7722-L7724】
- 🇪🇸AYO#74 also spotted a brake rotor mounted upside-down and suggested flipping it to improve heat shedding during hard stops.【F:data/vesc_help_group/text_slices/input_part013.txt†L7394-L7403】

#### Motor Wiring & Thermal Management
- Eduuuuuuuuu plans to upsize thin OEM phase leads; 🇪🇸AYO#74 recommended load-testing on a long hill, keeping any motor you can’t touch for 10 seconds under lower phase current, and choosing AWG 11 silicone conductors when AWG 10 physically will not fit through the axle.【F:data/vesc_help_group/text_slices/input_part013.txt†L7336-L7359】
- Paolo reinforced that “AWG” only specifies gauge—silicone cable is typically tinned copper and bulkier than PVC—so builders should focus on conductor material and strand count when sourcing replacements.【F:data/vesc_help_group/text_slices/input_part013.txt†L7348-L7353】

#### Tires, Wheels & Braking
- skrtt’s struggle to seat split-rim tubeless tires prompted tips to cinch the carcass with ratchet straps and hit it with a strong compressor while chasing leaks along the bead.【F:data/vesc_help_group/text_slices/input_part013.txt†L6784-L6803】
- The group compared tread options: Shlomozero10’s faux-PMT Ulip tires wore quickly even at 28 psi, PMT Stradales dislike burnout abuse, and Noname noted a 10×3 carcass only wraps ≈30 inches of rubber—there’s simply not much material to burn through—while true 90/60×6.5 alternatives are scarce outside PMT or XuanCheng molds.【F:data/vesc_help_group/text_slices/input_part013.txt†L6902-L6939】【F:data/vesc_help_group/text_slices/input_part013.txt†L6940-L6940】

#### Ride Planning & Field Reports
- Noname kicks off a week-long, 480 km Pennsylvania adventure with four riders and a chase vehicle, budgeting roughly 20 mph cruising, van support for the lone 60 mi gravel stretch, and nightly stops to keep batteries cool.【F:data/vesc_help_group/text_slices/input_part013.txt†L7095-L7127】
- Packing lists for the trip include a Segway C80, Begode Q3, Vsett 10, Begode Master Pro, and EX30 EUCs plus camping gear for five, all wedged into the chase rig for quick swaps.【F:data/vesc_help_group/text_slices/input_part013.txt†L7713-L7719】
- Daily ride logs already show 69 miles of crushed-stone trail with another 70 planned, hammock camping between legs, and onlookers quizzing the team about their Segway C80 support bike.【F:data/vesc_help_group/text_slices/input_part013.txt†L8153-L8159】【F:data/vesc_help_group/text_slices/input_part013.txt†L8214-L8214】

#### Firmware & Platform Notes
- Yusuf asked for turnkey firmware, and Matthew steered him toward direct-from-manufacturer VESC hardware (Spintend Ubox 85× series, Flipsky) instead of pricey AliExpress resellers, noting the value of official support when chasing 13 kW per controller.【F:data/vesc_help_group/text_slices/input_part013.txt†L7533-L7539】
- cihan’s F2 Pro tuning recap: SHU firmware requires an ST-Link flash, stock packs sag badly below ~65 % SOC, field weakening can push 45 km/h but higher kV means less torque, and traction control remains handy on icy commutes even if summer riders ignore it.【F:data/vesc_help_group/text_slices/input_part013.txt†L8121-L8144】
- ’lekrsu’ added that Segway’s stock firmware artificially clamps speed and that the F2 Pro motor sits near 19 kV, framing expectations for anyone considering external packs or firmware swaps.【F:data/vesc_help_group/text_slices/input_part013.txt†L8183-L8184】

#### High-Power Build Updates
- Dualtron Achilleus is marrying a Sonken chassis with dual 22×3 hubs (23.5/25 kV), 21 S 11 P P45B packs, and paired G300s—highlighting the packaging gymnastics required when 127 mm stators meet stock suspension hardware.【F:data/vesc_help_group/text_slices/input_part013.txt†L7754-L7760】【F:data/vesc_help_group/text_slices/input_part013.txt†L7758-L7759】
- Yamal continues to push large-frame hardware, reporting that an 80 H hub on 500 A phase / 300 A battery now delivers the punch he previously expected only from 33/2 speed motors once the Kelly-powered build received a proper discharge pack.【F:data/vesc_help_group/text_slices/input_part013.txt†L8170-L8176】

### Batch 2 Highlights (lines 1136–2200)

#### MakerBase Express Hardware & Configuration Notes
- Smart Repair confirmed the MakerBase Express uses a shared antenna for WiFi and Bluetooth, explaining why builders cannot spot a discrete RF whip on the PCB.【F:data/vesc_help_group/text_slices/input_part013.txt†L1112-L1153】
- Pandalgns outlined the desktop VESC Tool workflow for cloning configurations—save motor/app profiles from the working controller and load them onto the fresh unit once it is on the CAN bus—after A.P. asked how to replicate a MakerBase setup from Android.【F:data/vesc_help_group/text_slices/input_part013.txt†L2144-L2146】

#### Field-Weakening & Current Budget Lessons
- Gt Pro Karl is running dual Ubox 150s at 72 V with custom 250 A firmware, 210 A phase per motor, 50 A battery per side, and 55 A of field weakening; ‘lekrsu’ reiterated that phase amps collapse toward the battery limit at speed and warned that free-spinning with high FW is a fast way to cook controllers.【F:data/vesc_help_group/text_slices/input_part013.txt†L1154-L1217】
- Smart Repair is testing 450 A phase / 200 A battery with 10 % saturation compensation (no BEMF) on a dual-controller setup, reporting stable ABS behavior so far while planning to dial compensation back incrementally.【F:data/vesc_help_group/text_slices/input_part013.txt†L1798-L1802】
- The same crew compared safe envelopes for 85 250/240 hardware: Smart Repair caps absolute pushes at 380 A phase, 480 A abs, and 200 A battery, emphasizing that cooling prep—cleaning paint from the frame and adding thermal mass—largely dictates how hard the controllers can be run.【F:data/vesc_help_group/text_slices/input_part013.txt†L2094-L2117】

#### Failure Analysis & Packaging Tweaks
- Pandalgns ultimately traced their intermittent shutoffs to a front-motor hall board that had peeled loose and was shorting against the rotor housing; re-gluing the sensor board restored stability and cleared the “serial port” dropout symptoms.【F:data/vesc_help_group/text_slices/input_part013.txt†L1673-L1675】【F:data/vesc_help_group/text_slices/input_part013.txt†L1806-L1824】
- Izuna is reworking an MKS 84200HP by swapping six small electrolytics for two lower-profile caps (≈2000 µF total) so the controller fits in a G30 battery bay, noting the trade-off in bulk capacitance, and later upgraded the unit to 8 AWG battery leads after desoldering struggles.【F:data/vesc_help_group/text_slices/input_part013.txt†L1547-L1548】【F:data/vesc_help_group/text_slices/input_part013.txt†L1691-L1692】
- Smart Repair recommends slipping a 50 × 100 × 10 mm aluminum plate between the Ninebot G2 frame and the ESC with thermal paste—and stripping paint first—to keep customer builds below 50 °C even on steel chassis.【F:data/vesc_help_group/text_slices/input_part013.txt†L2126-L2129】

## Follow-up Questions / Actions
- Document the ST-Link V2 workflow (pinout, firmware dump, safety steps) required to derestrict the Ninebot G2 controller before Jose and Yamal proceed.【F:data/vesc_help_group/text_slices/input_part013.txt†L221-L226】
- Capture proven insulation options or sleeving techniques for 6 mm² phase wires that survive tight axle bends without the fragility of PTFE jackets.【F:data/vesc_help_group/text_slices/input_part013.txt†L172-L172】
- Track resolution steps for Basti’s HW No-Limit motor wizard failure on VESC Tool 6.06, including firmware versions or configuration tweaks that clear the error.【F:data/vesc_help_group/text_slices/input_part013.txt†L169-L170】
- Document a preventative fix for Pandalgns’s hall-board short (adhesives, strain relief, inspection steps) so other dual-motor builds can avoid the same shutdown loop.【F:data/vesc_help_group/text_slices/input_part013.txt†L1673-L1675】【F:data/vesc_help_group/text_slices/input_part013.txt†L1806-L1824】
- Verify whether MakerBase Express boards need antenna or shielding tweaks to maintain strong WiFi/Bluetooth connectivity given the shared RF trace design.【F:data/vesc_help_group/text_slices/input_part013.txt†L1112-L1153】
- Summarize practical battery-versus-phase current ratios for MakerBase 75100/75200 users so they can translate controller limits into motor-friendly settings quickly.【F:data/vesc_help_group/text_slices/input_part013.txt†L1154-L1217】【F:data/vesc_help_group/text_slices/input_part013.txt†L2086-L2090】
- Turn Smart Repair’s Ninebot G2 heat-spreader advice into a step-by-step guide (surface prep, plate sourcing, paste application) for the build handbook.【F:data/vesc_help_group/text_slices/input_part013.txt†L2126-L2129】
- Capture a reliable power-sequencing guide for Flipsky displays on MakerBase/Spintend hardware so builders stop back-powering the 5 V rail and blowing ADC daughterboards.【F:data/vesc_help_group/text_slices/input_part013.txt†L2375-L2387】【F:data/vesc_help_group/text_slices/input_part013.txt†L3190-L3193】
- Document enclosure-sealing or debris-screening practices that keep Ubox and similar controllers from ingesting grit during light-duty rides, per Yamal’s unexplained shutdown.【F:data/vesc_help_group/text_slices/input_part013.txt†L3362-L3375】
- Outline the Max G2 dropout-widening process (‘lekrsu’ bushings, bolt lengths, torque checks) so future conversions can replicate the 150 mm spacing safely.【F:data/vesc_help_group/text_slices/input_part013.txt†L2733-L2749】
- Detail safe ways to parallel 12 V accessory feeds (current limits, wiring, fuse guidance) on MakerBase/Spintend builds so riders aren’t overloading shared bucks.【F:data/vesc_help_group/text_slices/input_part013.txt†L4085-L4103】
- Research whether Spinny/ADC v2 harnesses can source sufficient current for dual-function 12 V tail/brake lights and outline any required relays or firmware hooks.【F:data/vesc_help_group/text_slices/input_part013.txt†L5127-L5127】
- Gather controller and battery envelope data to answer Arnau’s 100 V 100 A single-motor current ceiling question before he exceeds his 17×4 hub and Victor pack limits.【F:data/vesc_help_group/text_slices/input_part013.txt†L4996-L5002】
- Summarize best practices for mixing internal/external packs with ideal diodes or other current blockers so cihan’s parallel battery plan avoids regen-induced surges or BMS stress.【F:data/vesc_help_group/text_slices/input_part013.txt†L5118-L5136】
- Clarify what the different VESC Tool backup formats store (XML vs C vs UUID) and where those exports live so S1m 0n can create a reliable recovery bundle.【F:data/vesc_help_group/text_slices/input_part013.txt†L5211-L5211】
- Capture guidance for wiring four VESCs over CAN (ID assignment, power sequencing, watchdogs) for Adrian’s 4WD 75100 Pro v2 project.【F:data/vesc_help_group/text_slices/input_part013.txt†L6072-L6074】
- Document how to invert key-switch logic on MakerBase 84100HP hardware without rewiring the harness so chris can correct his reverse-acting switch.【F:data/vesc_help_group/text_slices/input_part013.txt†L6685-L6688】
- Investigate MP2 v0.6 voltage-sense calibration steps (divider values, firmware defines) to resolve Patrick’s inaccurate pack readings before he rides.【F:data/vesc_help_group/text_slices/input_part013.txt†L6691-L6695】
- Provide shielding or filtering recommendations that prevent Mirono’s boot-time throttle spikes around 2 V on ADC1.【F:data/vesc_help_group/text_slices/input_part013.txt†L6378-L6381】
- Build an MP2 bring-up checklist (component verification, buck-rail measurements, VIN-sense probing) to help Patrick finish debugging his freshly assembled board.【F:data/vesc_help_group/text_slices/input_part013.txt†L6703-L6755】
- Outline how to adapt four-wire Spintend power buttons to the G300 (connector repin, UART2 mapping, on/off menu settings).【F:data/vesc_help_group/text_slices/input_part013.txt†L6855-L6874】【F:data/vesc_help_group/text_slices/input_part013.txt†L7722-L7724】
- Document the regen-braking configuration workflow for Flipsky 75100 controllers so newcomers like fry the guy have a reference instead of scattered chat replies.【F:data/vesc_help_group/text_slices/input_part013.txt†L7394-L7399】
