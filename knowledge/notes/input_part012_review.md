# input_part012.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part012.txt`
- Coverage: 2025-03-10T21:50:04 through 2025-04-11T15:50:32 (lines 1-6925)
- Next starting point: Continue `input_part012.txt` at 2025-04-11T15:52:07 (line 6926)

## Key Findings

### Dualtron Thunder 2 Stability & Brake Fitment Troubleshooting
- Riders fighting 80–90 km/h wobble note the frame is extremely sensitive to arm height, tire quality/pressure, and running only a single front brake; lowering the suspension arms increases straight-line stability while better tires and balanced braking help calm oscillations.【F:data/vesc_help_group/text_slices/input_part012.txt†L80-L121】【F:data/vesc_help_group/text_slices/input_part012.txt†L235-L246】
- Steering play can come from the collar clamp “red rings” if the factory threadlocker lets go—inspect and re-torque or re-glue the stack before chasing other fixes.【F:data/vesc_help_group/text_slices/input_part012.txt†L204-L209】
- For wider rubber (100/55-6.5) riders reverse the Magura banjo fitting and seal the unused port with PTFE tape/copper washers to gain clearance, but even 90/65 tires may rub unless the hose is clocked carefully.【F:data/vesc_help_group/text_slices/input_part012.txt†L235-L269】
- Magura MT5 calipers are happiest on 1.8–2.3 mm rotors; 2.5–3.0 mm discs can be forced to fit but risk pad drag and heat unless you machine the caliper, so consider Zoom/Logan calipers or plan irreversible grinding if you insist on thick rotors.【F:data/vesc_help_group/text_slices/input_part012.txt†L241-L285】【F:data/vesc_help_group/text_slices/input_part012.txt†L499-L507】

### Brake Hardware Sourcing & Maintenance
- Fastride’s Hydro Parts Kit supplies the stainless M8 banjo and sealing hardware needed to swap hose orientation on Dualtron platforms when OEM stock is scarce.【F:data/vesc_help_group/text_slices/input_part012.txt†L187-L199】
- Copper crush washers remain the go-to seal for the reoriented banjo; riders also carry spare bleed screws and olives plus a simple hose-cutting kit (e.g., ZTTO tool) to refresh lines without specialty presses.【F:data/vesc_help_group/text_slices/input_part012.txt†L261-L308】
- For performance pads, Galfer compounds outperform Magura’s Performance/Race sets, though they are pricier; Shimano mineral oil is a safe substitute if Magura-branded fluid is unavailable.【F:data/vesc_help_group/text_slices/input_part012.txt†L315-L320】

### Tire Setup & Pressure Management
- To reseat stubborn 90/65-6.5 tires, cinch the carcass with a ratchet strap or heavy zip ties, inflate up to ~5 bar to pop the beads, then bleed down to 2–3 bar for riding so heat expansion doesn’t push pressures past ~3.5 bar on the road.【F:data/vesc_help_group/text_slices/input_part012.txt†L740-L748】
- Dualtron riders commonly settle around 3.0 bar rear / 2.5 bar front once the bead is seated; oversized Wolf tires can be revived even after a few burnout days by deflating, reseating, and reinflating with the strap trick.【F:data/vesc_help_group/text_slices/input_part012.txt†L745-L753】

### Tracking & Anti-Theft Notes
- Owners double up on Samsung SmartTag 2 and Apple AirTag trackers because Samsung-compatible clones are scarce; pairing Bluetooth tags with an eventual GPS IoT tracker is seen as the most reliable recovery strategy despite the extra €50 hardware cost per vehicle.【F:data/vesc_help_group/text_slices/input_part012.txt†L60-L125】
- Ideas to electrify the frame with pack voltage (~135 VDC) surface periodically but are acknowledged as dangerous, heart-level shock hazards—treat them as off-limits deterrents rather than practical advice.【F:data/vesc_help_group/text_slices/input_part012.txt†L79-L92】

### Controller Configuration & Firmware Recovery
- Makerbase 75200 builds discussed here run 20S packs at 60 A battery / 300 A phase, with field-weakening currents around 80 A to unlock ~200 A motor output; expect heat and stability limits to appear before controller headroom is reached.【F:data/vesc_help_group/text_slices/input_part012.txt†L126-L129】【F:data/vesc_help_group/text_slices/input_part012.txt†L470-L499】
- Field weakening at 20 A per wheel enabled 75 km/h but introduced high-speed instability, leading some to disable FW and consider milder Maximum Torque per Amp (MTPA) tuning that adds torque without the same top-speed push—battery sag will cap the gains on surface-mount hub motors.【F:data/vesc_help_group/text_slices/input_part012.txt†L348-L375】
- When reflashing “3Shul” VESC derivatives lacking a USB jack, solder a stripped USB cable to the board pads per the published pinout; an ST-Link is unnecessary unless the MCU bootloader is corrupt.【F:data/vesc_help_group/text_slices/input_part012.txt†L481-L495】
- Makerbase is releasing a low-cost VESC Express add-on (ESP32, Wi-Fi/Bluetooth, GPS, SD logging) for about €22, providing remote telemetry once stock reaches Europe.【F:data/vesc_help_group/text_slices/input_part012.txt†L470-L474】
- Jerome’s upcoming VESC Bridge V2 for Ninebot G30/G2 promises plug-and-play power-button control with only one connector re-pin on the G2, giving OEM commuters a cleaner conversion harness.【F:data/vesc_help_group/text_slices/input_part012.txt†L552-L552】
- Smart Repair is chasing a recurring low-speed MOSFET failure on a Spintend 85250 logic board that has killed the same devices three times across different motors, indicating the board likely needs bench diagnostics despite the vendor denying defects.【F:data/vesc_help_group/text_slices/input_part012.txt†L900-L901】
- Another NAMI “240” logic board lost a control MOSFET/12 V stage; despite running no 12 V accessories the owner plans to replace the control MOS while Jerome suspects the onboard converter, underscoring vulnerability in the low-voltage supply path.【F:data/vesc_help_group/text_slices/input_part012.txt†L983-L988】
- Riders seeking maximum punch are reminded to raise phase current for torque while keeping battery amps within the pack’s delivery window (e.g., ~50 A on a 60 A battery) to avoid overstressing hardware.【F:data/vesc_help_group/text_slices/input_part012.txt†L910-L912】
- Beta VESC Tool 6.06 firmware is already packaged in the official app update; otherwise compile from Vedder’s repositories—using the terminal build is faster than the Qt GUI for firmware targets such as `ubox_single_80`.【F:data/vesc_help_group/text_slices/input_part012.txt†L916-L935】
- “Spinny” throttles can plug straight into VESC without an external ADC adapter when wired correctly, simplifying minimalist cockpit builds.【F:data/vesc_help_group/text_slices/input_part012.txt†L871-L872】
- 3Shul V4 logic boards need more than USB power to enumerate—feed a small battery pack (even 3–4 S) alongside the data cable or VESC Tool will only see a steady blue LED; Tronic units were the exception that woke from USB alone.【F:data/vesc_help_group/text_slices/input_part012.txt†L1671-L1680】
- When a DIY USB lead still fails, confirm the data pair orientation (swap D+ / D− if needed) and use a full-size cable; bare FTDI/CP2102 adapters may require Windows drivers even though VESC endpoints normally expose a native virtual COM port.【F:data/vesc_help_group/text_slices/input_part012.txt†L1691-L1704】
- Spintend 85150 owners who interrupt a firmware flash should expect to recover with an ST-Link over the exposed SWD pads; phone-based firmware queues can leave the controller in a yellow-light fault state until reflashed.【F:data/vesc_help_group/text_slices/input_part012.txt†L2268-L2272】
- 3Chul-V4R2 logic boards hide a populated 4-pin header that likely breaks out SWDIO/SWCLK plus power and ground—map the pins back to STM32F405 pads (PA13/PA14) with a multimeter, or fall back to UART flashing via Connector 2 (TX/RX, 3.3 V, GND) if the bootloader still responds.【F:data/vesc_help_group/text_slices/input_part012.txt†L2335-L2397】
- JPPL’s notes outline fallback programming paths (UART, SPI, DFU) for 3Shul hardware, but they remain unverified; document the working sequence once someone confirms continuity and bootloader behavior.【F:data/vesc_help_group/text_slices/input_part012.txt†L2335-L2338】【F:data/vesc_help_group/text_slices/input_part012.txt†L2341-L2397】

### Fabrication & Thermal Management Tidbits
- Custom battery enclosures built from free 12-gauge sheet steel stay dimensionally stable under welding heat and should shrug off 9 mm handgun rounds, though edge welds may split if abused; consider them overkill but durable for off-road packs.【F:data/vesc_help_group/text_slices/input_part012.txt†L412-L428】
- Hobby fabricators debating 3D printer upgrades note that complete hot-end assemblies with pre-mounted fans simplify nozzle swaps compared with piecemeal parts, and hardened steel nozzles survive abrasive carbon- or stone-filled filaments better than brass or diamond-coated variants.【F:data/vesc_help_group/text_slices/input_part012.txt†L595-L672】
- Seized NAMI steering-cone nuts may demand torch heat across the full cone before a sector key, 2 m lever, and hammer can break the threadlocker; expect to cut the collar if the adhesive fully migrates into the threads.【F:data/vesc_help_group/text_slices/input_part012.txt†L1787-L1799】

### Brake Sensors & Calibration Checks
- If regen cut-off switches are wired backwards the scooter may crawl away from stops; pull the brake sensor connectors to confirm they release throttle properly before chasing deeper tuning issues, then revisit motor current ramps and wheel diameter (e.g., 92 mm input for correct speed) once the sensors are verified.【F:data/vesc_help_group/text_slices/input_part012.txt†L735-L753】

### Throttle & Switch Configuration
- Dualtron owners can bypass the eco/turbo and single/dual toggles by tying the corresponding wire pairs inside the rear switch pod, locking the scooter into full-turbo or dual-motor mode if a button fails.【F:data/vesc_help_group/text_slices/input_part012.txt†L993-L998】
- Raising the front suspension slightly and adding ~0.10 s positive ramp time tamed Shlomozero’s launches, but 11" builds still need rider weight over the nose and wider 100-section rear tires (upgrading from 90 mm) to keep ~80 km/h wheelspin in check.【F:data/vesc_help_group/text_slices/input_part012.txt†L1040-L1089】
- If throttle inputs feel sluggish even after reducing ramp times, re-run ADC mapping, inspect the duty-cycle limit, and revisit APP settings for filters, safe-start, and throttle curves—the community points lagging riders back to those menus before suspecting hardware faults.【F:data/vesc_help_group/text_slices/input_part012.txt†L1700-L1702】【F:data/vesc_help_group/text_slices/input_part012.txt†L2583-L2592】

### Conversion Fitment & Upgrade Considerations
- Fitting a Vsett 10+ motor into a Ninebot G2 requires relocating the suspension arms outward with bushings and longer shoulder bolts, widening the dropout from the stock 115 mm to roughly 150 mm.【F:data/vesc_help_group/text_slices/input_part012.txt†L902-L907】
- Riders pondering 11" LY hub swaps into Fiido-style bikes are cautioned that small Jetson packs and chassis make high-speed conversions risky “deathtraps,” so plan meaningful battery upgrades before chasing motor swaps.【F:data/vesc_help_group/text_slices/input_part012.txt†L899-L899】【F:data/vesc_help_group/text_slices/input_part012.txt†L951-L952】
- Questions about ferrofluid sourcing remain unanswered—document proven suppliers for hub motor cooling additives.【F:data/vesc_help_group/text_slices/input_part012.txt†L909-L909】
- Simone keeps a customer’s NAMI on Kelly 7212S controllers because stock motors cannot exploit higher-end VESC builds without risking burnout; he treats Flipsky as less robust than Kelly for that duty cycle.【F:data/vesc_help_group/text_slices/input_part012.txt†L1802-L1809】

### High-Power Hub Motor Options
- Weped Sonic S performance debates point toward large-format Sotion or QS hub motors (e.g., QS268 9 kW class) with steep €366 shipping, underscoring the premium components behind 16 kW claims and persistent traction issues.【F:data/vesc_help_group/text_slices/input_part012.txt†L1100-L1119】

### Tire & Wheel Fitment Quick Hits
- 11" × 90/55-6.5 tire swaps typically use a 279 mm circumference setting inside VESC Tool, and sizing up to 100 section widths generally requires the banjo flip noted above to keep hoses from rubbing.【F:data/vesc_help_group/text_slices/input_part012.txt†L728-L741】【F:data/vesc_help_group/text_slices/input_part012.txt†L235-L269】
- To reseat or revive abused 90/65-6.5 tires, cinch the carcass with straps, inflate up to 5 bar for bead seating, then bleed down to ~3/2.5 bar rear/front to account for heat growth on the road.【F:data/vesc_help_group/text_slices/input_part012.txt†L740-L748】
- PMT Junior slicks earn praise for grip while Stradale versions divide opinion (durable for some, puncture-prone for others); budget seekers keep sharing AliExpress finds for 90/65-6.5 through 100/55-6.5 carcasses despite compound compromises.【F:data/vesc_help_group/text_slices/input_part012.txt†L2542-L2567】

### Display & Accessory Ecosystem Updates
- Ev Pro’s RTV display bundle stays closed-source despite leaning on open hardware; pre-orders require a balance payment before August batch shipments, and the team is tooling a carbon “forged” enclosure plus OTA turn-by-turn navigation. Expect to preload VESC profiles on the scooter—runtime programming still depends on VESC Tool rather than the dash itself.【F:data/vesc_help_group/text_slices/input_part012.txt†L1650-L1685】

### BMS Reliability Callouts
- Riders rank ANT and JK smart BMS units above Daly, citing solar-use current capability, yet lingering reports describe ANT packs that keep outputting after the discharge FET is disabled—log testing to confirm the failure mode.【F:data/vesc_help_group/text_slices/input_part012.txt†L1638-L1645】

### Lighting & Low-Voltage Power Notes
- For simple brake lights, tap pack voltage through a robust DC/DC step-down and let the brake sensor switch ground; Spintend’s ADC adapter offers a tidy 5 V trigger but multiple members report the board dying after shorts, while bargain AliExpress regulators sometimes outlive name-brand units on 20 S scooters.【F:data/vesc_help_group/text_slices/input_part012.txt†L2593-L2607】
- High-voltage packs quickly cook undersized converters—some give up after piles of smoked regulators and instead borrow the BMS’s regulated 5 V rail or hunt for converters with proven thermal headroom.【F:data/vesc_help_group/text_slices/input_part012.txt†L2608-L2613】

### Tire Shopping & Compound Feedback
- Community sourcing lists continue to circulate for 10×3.0 and 11" tires (Xuancheng, budget solids), but consensus holds that “cheap and good” rarely overlap; confirm bead dimensions before ordering as many listings lack 6.5"-rim fitment clarity.【F:data/vesc_help_group/text_slices/input_part012.txt†L2526-L2567】

### Community Projects & Supply Chain Tidbits
- DIY builders chasing 650 V MP2-class controllers struggle to source suitable TOLT-packaged MOSFETs and MLCC placement on single-layer IMS boards; consider double-sided FR-4 alternatives despite higher assembly costs to keep cooling and capacitor placement manageable.【F:data/vesc_help_group/text_slices/input_part012.txt†L1281-L1399】

### Bench Talk & Recovery Humor
- Group members debate Ant/JK vs. Daly BMS support experiences, rally around government-contract jokes, and keep exploring oversized field-weakening setups (e.g., 32 S ambitions, 17×4” tires) while acknowledging battery current remains the limiting factor.【F:data/vesc_help_group/text_slices/input_part012.txt†L1638-L1646】【F:data/vesc_help_group/text_slices/input_part012.txt†L1900-L1925】

### Safety Cautions & Community Watch-outs
- Admins flagged Facebook advice about jump-starting a dead 36 V pack with a 60 V charger as dangerous; even if a temporary “wake-up” works, stop near nominal voltage and monitor closely to avoid thermal events.【F:data/vesc_help_group/text_slices/input_part012.txt†L519-L538】

### Spintend Firmware Recovery & ST-Link Diagnostics
- Bricked Spintend 85150 owners are pointed back to the vendor repo for the unrestricted firmware and reminded that the logic board exposes a BOOT0 jumper, simplifying USB recovery before falling back to ST-Link tooling.【F:data/vesc_help_group/text_slices/input_part012.txt†L2784-L2787】
- JPPL confirms the Makerbase/Spintend logic board can be powered directly over the SWD header; if the ST-Link fails to enumerate, verify 3.3 V and ground before adding external battery power.【F:data/vesc_help_group/text_slices/input_part012.txt†L3046-L3048】
- For elusive 3Chul-V4 headers, JPPL walks through continuity checks from STM32 VSS/VDD pins, then maps suspected SWDIO/SWCLK pads to the four-pin header while watching for low-but-nonzero resistance (~3.4 Ω) that still indicates a valid path.【F:data/vesc_help_group/text_slices/input_part012.txt†L3663-L3685】
- Dual-controller riders swapping CAN IDs are warned to “read before write” in VESC Tool; writing blindly can desynchronize CAN IDs and hide the slave until configurations are reset and voltage limits re-entered.【F:data/vesc_help_group/text_slices/input_part012.txt†L4057-L4077】

### High-Voltage Experiments & Field-Weakening Findings
- Spintend’s HY MOSFET 85250 is advertised as 22 S capable, but the seller disclaims warranty above ~85 V pack voltage, and later owners reiterate that stock Ubox hardware can misbehave at 22 S despite the marketing copy.【F:data/vesc_help_group/text_slices/input_part012.txt†L2803-L2810】【F:data/vesc_help_group/text_slices/input_part012.txt†L3926-L3933】
- Jason’s Ninebot G30 build hit 105 km/h on a 30 S pack with 17×4" tires, overmodulation, and 20 A field weakening but saw CAN-logged phase-current ripple, echoing Jerome’s caution that OVM+FW on firmware 1.10 injects noisy current draw.【F:data/vesc_help_group/text_slices/input_part012.txt†L3358-L3366】
- Riders chasing star/delta switching debate dual-controller strategies versus MOSFET-based phase relays; even proponents admit the wiring complexity and fault risk likely limit appeal to niche competition builds.【F:data/vesc_help_group/text_slices/input_part012.txt†L3388-L3416】

### Frame & Suspension Modifications
- Converting a Ninebot G2 to wider 65H tires requires four longer shoulder bolts and copper bushings to relocate the suspension arms, but fabricators warn unsupported long bolts will see shear unless both ends are braced.【F:data/vesc_help_group/text_slices/input_part012.txt†L2834-L2840】
- Repurposing Vsett 10 arms with spacer stacks on other frames risks bending the stock 8 mm pivot pin—plan reinforced spacers or custom hardware instead of piling on washers.【F:data/vesc_help_group/text_slices/input_part012.txt†L3686-L3690】

### High-Speed Stability & Ride Technique
- Halo T107 riders recount 115 km/h wobble events; consensus points to soft tires, rider posture, absent dampers, and the rear swingarm flexing under throttle. One workaround was to keep modest throttle on while feathering the brake to hold geometry until speeds drop.【F:data/vesc_help_group/text_slices/input_part012.txt†L2906-L2928】

### Tubeless Tire Mounting & Wheel Service Tips
- For tubeless swaps, members favor soapy water (or glass cleaner) over lithium grease, then rely on ratchet straps, heavy zip ties, or even CO₂ cartridges to seat stubborn beads before dropping pressures back from 50 psi test fills.【F:data/vesc_help_group/text_slices/input_part012.txt†L3498-L3519】【F:data/vesc_help_group/text_slices/input_part012.txt†L3510-L3515】

### Brake Hardware Fitment Updates
- Attempting to squeeze 2.8 mm Sonken rotors into Magura MT5 calipers leaves near-zero pad clearance; riders either evacuate some fluid, shave pad backing material, or expect drag and heat until the pads wear in—beyond roughly 2.5 mm, compromises stack up quickly.【F:data/vesc_help_group/text_slices/input_part012.txt†L3816-L3843】

### Battery Pack Planning & Cell Debates
- Long-range builders weighing 120-cell packs weigh Samsung 50E energy density against BAK 45D’s higher discharge; community feedback says 45D outpulls P45B slightly yet still trails Samsung on cycle life, pushing many toward balanced 40–45 P arrays instead of exotic 50 P stacks.【F:data/vesc_help_group/text_slices/input_part012.txt†L3428-L3456】
- A 52 V commuter confirmed regen braking fades at 100 % SOC; leaving ~10 % headroom (or lowering regen cutoffs to ~56–58 V on 14 S) keeps kinetic energy from dumping into the MOSFETs.【F:data/vesc_help_group/text_slices/input_part012.txt†L3741-L3756】

### Display & Telemetry Development
- JPPL is extending the open-source SimpleVescDisplay project with CAN battery/duty bars, connection status icons, and touch triggers, promising to share firmware builds once stability improves; customization ranges from novelty “penis battery” requests to full multi-page layouts.【F:data/vesc_help_group/text_slices/input_part012.txt†L3761-L3762】【F:data/vesc_help_group/text_slices/input_part012.txt†L3905-L3910】【F:data/vesc_help_group/text_slices/input_part012.txt†L3930-L3934】【F:data/vesc_help_group/text_slices/input_part012.txt†L3982-L3984】

### Controller Support & Troubleshooting Nuggets
- Multiple users struggling with Flipsky TFT profile buttons learned that without matching VESC Tool scripting the display toggles are cosmetic—profile changes still require CAN/Lisp integration or external microcontrollers.【F:data/vesc_help_group/text_slices/input_part012.txt†L3921-L3949】
- Shimano XT four-piston caliper swaps onto Dualtron Thunder arms with 100/55-6.5 tires remain unresolved as members crowdsource clearance checks and bleed tips, suggesting a future fitment guide could save trial-and-error.【F:data/vesc_help_group/text_slices/input_part012.txt†L3950-L3961】

### Firmware Flashing Support & Community Frustrations
- 🇪🇸AYO#74🏁 still can’t push firmware to new controllers with an ST-Link, drawing public frustration from Meli over vendors shipping boards without clear flashing instructions; helpers confirm the programmer struggles to talk to the STM MCU even with shared pinouts.【F:data/vesc_help_group/text_slices/input_part012.txt†L4249-L4272】【F:data/vesc_help_group/text_slices/input_part012.txt†L4310-L4313】

### Controller Thermal Targets & Cooling Upgrades
- Riders told SchweigePflicht to hold UBOX 85V150A case temps near 50–60 °C (70–80 °C max) and to cut phase/battery amps if heat climbs, underscoring the need for better heatsinking when pushing those packs.【F:data/vesc_help_group/text_slices/input_part012.txt†L4729-L4734】
- Shlomozero toyed with raising PWM switching to 40 kHz for smoother launches but was reminded to verify controller specs, let hardware cool, and dial back phase current when the motor is too hot to touch.【F:data/vesc_help_group/text_slices/input_part012.txt†L4230-L4242】
- Yoann’s ultra-compact build runs a 12 V fan that draws ~0.09 A, scripted in Lisp to kick on at 60 °C alongside custom LED feedback, providing a template for automated spot cooling in cramped bays.【F:data/vesc_help_group/text_slices/input_part012.txt†L4690-L4690】
- Jerome logged ~200 km over two days on three GTs running Spintend UBOX 85150 controllers with VESC Bridges, hitting 110 km/h without thermal faults once the setup was dialed.【F:data/vesc_help_group/text_slices/input_part012.txt†L4692-L4692】

### Wiring Hazards & Safety Reminders
- Francois toasted a controller by letting the power button short to the frame, prompting others to sheath or cap switch leads before bolting them down so pack voltage can’t jump to ground mid-install.【F:data/vesc_help_group/text_slices/input_part012.txt†L4752-L4757】

### Controller Reliability & Replacement Advice
- Makerbase 75100 controllers keep failing unpredictably—even at half power—so the group steers shoppers toward Spintend’s aluminum-cased units, Makerbase’s 84100HP, or MakerX Go-FOC models in the €100–€250 class.【F:data/vesc_help_group/text_slices/input_part012.txt†L4812-L4833】

### Gyro Integration for Self-Balancing Builds
- A onewheel-style project pairing a BMI160 IMU with a 75200 keeps freezing after a few minutes despite firmware swaps, highlighting the need for validated IMU configs and more Russian-language documentation for these VESC conversions.【F:data/vesc_help_group/text_slices/input_part012.txt†L4836-L4849】

### Overmodulation & Field-Weakening Calibration
- Overmodulation settings now hide in the beta VESC Tool (FOC → Advanced); once uncovered, Jerome cautions that running OVM 1.1 plus field weakening injects noisy phase current and prefers 1.05 for clean telemetry.【F:data/vesc_help_group/text_slices/input_part012.txt†L4854-L4871】

### Motor Temperature Monitoring & Sensor Placement
- Builders continue debating safe thermal ceilings: some Lonnyo hubs survive 140–160 °C winding temps after relocating sensors into the coils, while others warn anything beyond ~140 °C risks magnet demagnetization despite high-temp insulation claims.【F:data/vesc_help_group/text_slices/input_part012.txt†L4876-L4889】

### Battery Cell Selection Resources
- Francois dropped a 2025 “ultimate battery cell” spreadsheet ranking 18650/21700/26650 options by power, energy, and cost, keeping Molicel P42A/P45B and Samsung 40T on top for high-performance PEV packs.【F:data/vesc_help_group/text_slices/input_part012.txt†L4710-L4711】

### Telemetry & Accessory Hardware Updates
- Jerome unexpectedly praised Bakerbase’s VESC Express hardware quality but flagged that shrink-wrap blocks accessory connectors and omits a GPS lead; he recommends the 25 Hz BZ121 GPS puck, which still sees 12 satellites when tucked inside plastic bodywork.【F:data/vesc_help_group/text_slices/input_part012.txt†L5178-L5187】

### Battery Bay Fitment Measurements
- Haku measured his deck battery cradle at roughly 330 × 220 × 75 mm, giving pack designers concrete dimensions for fitting dense 40T layouts under the floor.【F:data/vesc_help_group/text_slices/input_part012.txt†L5604-L5604】

### Dnis Brake Integration for GT Platforms
- Jerome is coordinating with Dnis on six-piston calipers that appear to fit Dualtron GT forks with only a thin front spacer; the factory is willing to machine spacers for other geometries and will ship longer hoses on request, but pricing lands around €166 per caliper so riders should plan for full-kit costs.【F:data/vesc_help_group/text_slices/input_part012.txt†L6283-L6294】
- His quickest GT build will pair rear Spintend 85240 and front 85150 controllers with Dnis brakes and GT2 motors, noting that even 160 A phase/80 A battery on the front wheel is tough to manage without weight transfer despite the chassis resisting wobble.【F:data/vesc_help_group/text_slices/input_part012.txt†L6299-L6307】

### Legal Mode & Profile Switching Automation
- German owners need a 20 km/h single-motor profile capped near 600 W to appease roadside inspections; Smart Repair is looking for scripts or hardware that default to the tame profile so officers cannot unlock full power by squeezing the throttle.【F:data/vesc_help_group/text_slices/input_part012.txt†L6323-L6327】
- Yoann is prototyping an ESP-driven profile switch that only toggles when the brake is held, while Jerome notes that an external ESP32 opens more GPIO options than single-button Lisp macros on Makerbase 84100 controllers.【F:data/vesc_help_group/text_slices/input_part012.txt†L6323-L6335】【F:data/vesc_help_group/text_slices/input_part012.txt†L6377-L6386】
- Roby confirmed VESC Tool can already flip profiles from a physical button on the Makerbase 84100 HP, reinforcing the need to document wiring and configuration for legal-mode switches.【F:data/vesc_help_group/text_slices/input_part012.txt†L6309-L6313】

### Battery Pack Repair & Charging Cautions
- Damaged Dualtron U2 packs built with FEV EBX40 cells can’t be patched with Tenpower 40TG replacements—mixing chemistries in-series risks imbalance and thermal runaway, so full parallel groups should be rebuilt with matching stock.【F:data/vesc_help_group/text_slices/input_part012.txt†L6360-L6364】
- Community teardown photos highlight how slim nickel links in some Samsung 50S packs make the advertised 125 A continuous/225 A peak targets unrealistic; expect extreme heating (ΔT ≈ 130 °C) if you actually push those numbers.【F:data/vesc_help_group/text_slices/input_part012.txt†L6377-L6383】
- Jason’s 26 A fast-charge experiment on LG MH1 cells drew 3.1 A per cell—well beyond typical 0.5–1.5 C guidance—prompting the group to dial back current for longevity and safety.【F:data/vesc_help_group/text_slices/input_part012.txt†L6825-L6837】

### High-Voltage Spintend Failure Reports
- Patrick’s dual 22 S Spintend setup has run 22 kW (105 A battery/215 A phase per controller), yet a friend blew two units within a minute at 85 V on a converted NAMI despite 200 A phase limits and regen disabled; Jerome suspects default 1000 V regen ceilings or MOSFET batch differences (JMSH vs HY) could be factors.【F:data/vesc_help_group/text_slices/input_part012.txt†L6386-L6408】【F:data/vesc_help_group/text_slices/input_part012.txt†L6403-L6407】

### Peripheral Integration & Wiring Notes
- Haku is rewiring the Spinny throttle PCB directly into VESC signal pins (matching color codes) to skip the external ADC adapter, suggesting a pinout reference would help future installs.【F:data/vesc_help_group/text_slices/input_part012.txt†L6808-L6816】
- Arnau is mapping the Spintend AluBox UART header to host an M365 BLE dash; Smart Repair pointed him to labeled RX/TX pads, but a step-by-step script-and-wiring walkthrough remains missing.【F:data/vesc_help_group/text_slices/input_part012.txt†L6847-L6873】
- Smart Repair is chasing reliable FOC detection numbers for 11" 70H 22×3 Lonnyo hubs because Spintend 85250 and Sabvoton X12 report drastically different inductance/resistance; Dualtron Achilleus offered to share screenshots and mentioned manually lowering inductance to ~60 µH with related adjustments.【F:data/vesc_help_group/text_slices/input_part012.txt†L6806-L6858】

### Connectivity Troubleshooting
- Oreo’s CL350V4 loses Bluetooth beyond ~5 cm; bonding the controller’s main negative to the chassis apparently restored range, hinting at grounding or shielding issues with the integrated radio.【F:data/vesc_help_group/text_slices/input_part012.txt†L6878-L6879】

## Follow-up Questions
- Document a reliable procedure for reversing and bleeding Magura banjos on Dualtron swingarms (torque specs, washer stack, hose clocking) so riders aren’t guessing mid-job.【F:data/vesc_help_group/text_slices/input_part012.txt†L187-L308】
- Validate long-term rotor temps when running 2.5–3.0 mm discs in Magura calipers with only minimal clearance—do pad chamfers or caliper milling mitigate heat build-up?【F:data/vesc_help_group/text_slices/input_part012.txt†L241-L507】
- Capture safer anti-theft best practices (hidden relays, immobilizers) to discourage experiments with high-voltage deterrent switches.【F:data/vesc_help_group/text_slices/input_part012.txt†L79-L92】
- Track availability and installation notes for Makerbase VESC Express and the Ninebot VESC Bridge once production units land, documenting connector pinouts and firmware support.【F:data/vesc_help_group/text_slices/input_part012.txt†L470-L552】
- Diagnose the root cause of Spintend 85250 MOSFET failures and document board-level checks before additional motors are sacrificed.【F:data/vesc_help_group/text_slices/input_part012.txt†L900-L901】
- Investigate the NAMI “240” logic-board low-voltage stage failure path and document replacement parts or preventative steps.【F:data/vesc_help_group/text_slices/input_part012.txt†L983-L988】
- Identify reliable ferrofluid suppliers, quantities, and application tips for hub motor cooling upgrades.【F:data/vesc_help_group/text_slices/input_part012.txt†L909-L909】
- Outline wiring diagrams or pin references for running Spinny throttles directly on VESC inputs without external ADC adapters.【F:data/vesc_help_group/text_slices/input_part012.txt†L871-L872】
- Detail the hardware kit (bushings, bolt specs) required to fit Vsett 10+ motors into Ninebot G2 swingarms safely.【F:data/vesc_help_group/text_slices/input_part012.txt†L902-L907】
- Capture wiring colors/pinouts for locking Dualtron eco/turbo or dual/single buttons into a fixed mode when switches fail.【F:data/vesc_help_group/text_slices/input_part012.txt†L993-L998】
- Evaluate tire compounds, widths, and ramp-time settings that limit wheelspin on 11" high-power builds targeting 80 km/h launches.【F:data/vesc_help_group/text_slices/input_part012.txt†L1040-L1089】
- Verify which large-format hub motors (Sotion vs. QS268) ship with Weped Sonic S scooters and document real-world power numbers vs. marketing claims.【F:data/vesc_help_group/text_slices/input_part012.txt†L1100-L1119】
- Confirm the exact SWD pinout and working recovery process for 3Chul-V4R2 controllers (UART vs. SWD vs. DFU) so stranded owners can reflash without guesswork.【F:data/vesc_help_group/text_slices/input_part012.txt†L2335-L2397】
- Document reliable brake-light power strategies for 20 S scooters (converter specs, wiring diagrams, fuse placement) that survive vibration and short events.【F:data/vesc_help_group/text_slices/input_part012.txt†L2593-L2613】
- Track Ev Pro RTV display firmware support, profile syncing, and any eventual source-code release obligations tied to its open-hardware baseline.【F:data/vesc_help_group/text_slices/input_part012.txt†L1650-L1685】
- Investigate ANT BMS discharge-disable anomalies to see if firmware revisions or wiring mistakes keep the output FET engaged after shutoff.【F:data/vesc_help_group/text_slices/input_part012.txt†L1638-L1645】
- Compile the community’s step-by-step method for identifying 3Chul/3Shul SWD pads (continuity targets, expected resistance) to streamline future recoveries.【F:data/vesc_help_group/text_slices/input_part012.txt†L3663-L3685】
- Capture proven tubeless mounting workflows (strap placement, pressure limits, leak checks) for fixed-rim scooters that struggle to seat beads at home.【F:data/vesc_help_group/text_slices/input_part012.txt†L3498-L3519】
- Summarize high-speed wobble mitigation for Halo/Laotie frames (dampers, tire pressure, rider stance) so new owners can set up safely before chasing 100 km/h runs.【F:data/vesc_help_group/text_slices/input_part012.txt†L2906-L2928】
- Detail clearance mods or alternative calipers/rotors that let Magura MT5 users run >2.5 mm discs without constant pad drag or overheating.【F:data/vesc_help_group/text_slices/input_part012.txt†L3816-L3843】
- Capture a vendor-verified ST-Link flashing workflow (pinout, power sequencing, tool settings) for the controllers frustrating 🇪🇸AYO#74🏁 so owners aren’t stuck with mute boards.【F:data/vesc_help_group/text_slices/input_part012.txt†L4249-L4272】【F:data/vesc_help_group/text_slices/input_part012.txt†L4310-L4313】
- Map cooling upgrades and safe temperature envelopes for UBOX 85V150A builds—including case heatsinks, airflow, and firmware alarms—so riders can respect the 50–80 °C guidance without guesswork.【F:data/vesc_help_group/text_slices/input_part012.txt†L4729-L4734】【F:data/vesc_help_group/text_slices/input_part012.txt†L4690-L4692】
- Diagnose why BMI160 gyro integrations freeze 75200-based onewheel conversions and document a stable IMU configuration (sample rates, firmware, wiring) for self-balancing projects.【F:data/vesc_help_group/text_slices/input_part012.txt†L4836-L4849】
- Publish connector maps and accessory harness tips for Bakerbase’s VESC Express, including how to add the recommended BZ121 GPS puck without fighting the factory shrink-wrap.【F:data/vesc_help_group/text_slices/input_part012.txt†L5178-L5187】
- Verify long-term magnet health when Lonnyo hubs operate at 140–160 °C windings with relocated sensors and high-temp insulation claims.【F:data/vesc_help_group/text_slices/input_part012.txt†L4876-L4889】
- Document Dnis V6 brake installs on Dualtron GT variants (spacer thickness, hose lengths, reservoir placement) once Jerome’s kits land.【F:data/vesc_help_group/text_slices/input_part012.txt†L6283-L6307】
- Produce a repeatable method to wire and configure legal/boost profiles on Makerbase 84100-class controllers, including brake-interlock logic so inspectors cannot unlock full power roadside.【F:data/vesc_help_group/text_slices/input_part012.txt†L6323-L6335】
- Identify safe sourcing or rebuild paths for damaged FEV EBX40 packs when exact replacement cells are unobtainable.【F:data/vesc_help_group/text_slices/input_part012.txt†L6360-L6364】
- Root-cause the 22 S Spintend blow-ups observed on a NAMI conversion at ~85 V, including regen thresholds, MOSFET bins, and wiring stress tests.【F:data/vesc_help_group/text_slices/input_part012.txt†L6386-L6408】
- Capture validated FOC parameter ranges for 11" 70H Lonnyo motors across popular controllers (Spintend 85250, Sabvoton X12).【F:data/vesc_help_group/text_slices/input_part012.txt†L6806-L6858】
- Publish a plug-and-play wiring diagram plus firmware steps for mounting M365 BLE dashboards on Spintend AluBox builds.【F:data/vesc_help_group/text_slices/input_part012.txt†L6847-L6873】
- Investigate why CL350V4 Bluetooth modules regain range only after frame-ground bonding and whether shielding or antenna mods are safer long-term fixes.【F:data/vesc_help_group/text_slices/input_part012.txt†L6878-L6879】
