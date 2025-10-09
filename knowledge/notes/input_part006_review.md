# input_part006.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part006.txt`
- Coverage: 2023-11-19T23:17 through 2023-12-11T13:10 (lines 1-6700)
- Next starting point: line 6701 (2023-12-11T13:10:31 and later)

## Key Findings

### High-Voltage Scooter Builds & Controller Marketing
- Slack Core “R” trims are advertised as 28S powerhouses, yet early builds reportedly relied on bulky Kelly controllers whose wattage claims simply multiply peak pack voltage by phase current—mirroring Kelly’s own marketing math.【F:data/vesc_help_group/text_slices/input_part006.txt†L1-L30】
- Riders retrofitting commuter frames (e.g., Ninebot G30) to 22S remind newcomers that a lone series string (22s1p) cannot sustain load; without parallel capacity the pack sags and the upgrade under-delivers.【F:data/vesc_help_group/text_slices/input_part006.txt†L61-L64】

### Component Quality & Fitment Notes
- Vsett 9 owners describe mechanical discs that demand constant adjustment and unpredictable electronic braking spikes at top speed, reinforcing the call to move commuter builds to hydraulic systems.【F:data/vesc_help_group/text_slices/input_part006.txt†L44-L52】
- Premium Iscooting and Wanda P1237 tires arrive with flat spots and weak inner rings, whereas Ulip and Xuancheng remain the budget-friendly replacements of choice for dependable casings.【F:data/vesc_help_group/text_slices/input_part006.txt†L108-L139】

### Brake System Experimentation
- Rosheee’s wet-track torture test boiled 360 °C-rated fluid in a Magura MT7/Trickstuff front stack (100 € rotor, four-piston caliper) and forced leaks, yet the rear MT8 on a Trickstuff Dächle HD rotor with Kool Stop copper pads stayed composed—front systems need more thermal mass or cooling for repeat 100 km/h stops.【F:data/vesc_help_group/text_slices/input_part006.txt†L140-L153】
- Downhill racers note rear circuits usually run cooler thanks to larger oil volumes and warn that thinning rotors can fracture around 60 km/h, so flogged braking hardware should be retired early.【F:data/vesc_help_group/text_slices/input_part006.txt†L141-L146】

### Firmware & Control Behavior
- XESC firmware secretly adds pack amps to maintain torque when field weakening is applied (e.g., +7 A), while VESC honors the requested limits—explaining why XESC riders see surprise BMS shutdowns when they assume static current draw.【F:data/vesc_help_group/text_slices/input_part006.txt†L153-L157】

### Track Testing & SmartDisplay Integration
- Face de Pin Sucé logs 22S wet-track sessions near 120 km/h and prefers running the rear controller as SmartDisplay master on dual setups; nearby kart tracks reportedly allow scooter rentals with minimal notice for repeatable testing grounds.【F:data/vesc_help_group/text_slices/input_part006.txt†L161-L181】

### Controller Reliability Troubleshooting
- Adding a keyed ignition to a VESC 75100 introduced random reboots until the floating enable pin was pulled lower with a stronger resistor—budget for proper pull-downs whenever grafting external switches onto maker boards.【F:data/vesc_help_group/text_slices/input_part006.txt†L183-L194】

### Battery Fabrication & Tooling Tips
- Glitter 811H spot welders can fuse 0.2 mm copper-to-nickel sandwiches but readily blow through nickel unless power is reduced; sharp electrodes and practice on dead cells are strongly encouraged before tackling live packs.【F:data/vesc_help_group/text_slices/input_part006.txt†L324-L366】
- KWELD operators report super-capacitor banks above four parallel cans trip over-current faults; dual Meanwell LRS-350s feed an 8.1 V charger with switchable resistors for controlled charge/discharge, and active cooling for weld pens is under evaluation to fight heat soak.【F:data/vesc_help_group/text_slices/input_part006.txt†L368-L384】

### Community Expertise & Hardware Roadmaps
- YouTuber “De-bodgery” (EV Components Review) joined the chat, offering teardown expertise and plans to commercialize the “Mr. Snippy” strip tool—giving the group direct access to failure-analysis insights.【F:data/vesc_help_group/text_slices/input_part006.txt†L335-L343】
- FOCforever is co-developing the Tronic 2000 with Infineon’s TOLT MOSFET modules; even 54 devices push gate-driver limits, yet the package enables multilayer PCBs without IMS and better thermal headroom than TO-220 designs.【F:data/vesc_help_group/text_slices/input_part006.txt†L500-L519】
- Builders are planning a 100H drag motor using QS273 stators, stronger N50 magnets, and a move into a 12 000 sq ft lab to prototype Ultra Bee-class inrunner alternatives—expect future high-voltage motor experiments from the community.【F:data/vesc_help_group/text_slices/input_part006.txt†L611-L629】

### CAN Bus Failures After Ignition Mods
- Makerbase 75100 ALU boards lost CAN communications after resin potting and keyed ignition mods; one controller still showed 3.7 V on CANH while its mate sat at 0 V, pointing to a blown transceiver from poor ground referencing.【F:data/vesc_help_group/text_slices/input_part006.txt†L630-L755】
- Paolo suspects the shared positive/no ground ignition wiring let return currents flow through CAN, stressing future builders to common grounds before energizing external power buttons.【F:data/vesc_help_group/text_slices/input_part006.txt†L744-L755】
- Builders observed intermittent recovery when pressing stock micro connectors and ultimately ditched the factory plug for soldered or JST leads, citing vibration failures in sub-2 mm housings on scooters.【F:data/vesc_help_group/text_slices/input_part006.txt†L708-L717】

### Brake, Dashboard, and Control Hardware Notes
- Magura MT5e levers ship with aluminum blades and easy reed-switch retrofits, making them sturdier upgrades when plastic lever housings crack on budget assemblies.【F:data/vesc_help_group/text_slices/input_part006.txt†L792-L799】
- Compact dual-controller seekers compared MakerX G300 to 3Shul CL/C350 units, praising the latter’s palm-sized (135 × 75 × 45 mm) footprint but insisting on thermal paste across the baseplate for meaningful heat transfer.【F:data/vesc_help_group/text_slices/input_part006.txt†L797-L808】
- Xiaomi dashboard Lisp tinkerers confirmed the turn-on resistor can live mid-harness under heat-shrink, easing packaging constraints in retrofits.【F:data/vesc_help_group/text_slices/input_part006.txt†L790-L795】

### Sensor Calibration & Firmware Sharing
- NetworkDir published Makerbase 75100 V2 firmware binaries (6.05 with/without limits) and floated a delivery bot, helping riders without toolchains flash vetted configs quickly.【F:data/vesc_help_group/text_slices/input_part006.txt†L777-L786】
- Mirono shared a quick calibration hack—divide the shunt value by three when VESC Tool reports battery amps at one-third of reality—but emphasized verifying with clamp meters or smart BMS data before trusting the fix.【F:data/vesc_help_group/text_slices/input_part006.txt†L809-L821】
- Android support remains inconsistent: Samsung A-series owners on Android 13 cannot run the same VESC Tool beta that others operate on Android 13/14, highlighting the need to document Knox security and minimum OS requirements.【F:data/vesc_help_group/text_slices/input_part006.txt†L1187-L1215】

### Vendor Reliability & Sales Logistics
- Spintend’s Black Friday drop sold out instantly and rekindled complaints about limited stock, missing IOSS VAT handling, and stray solder balls that once shorted capacitors—buyers now budget extra time to inspect new controllers.【F:data/vesc_help_group/text_slices/input_part006.txt†L876-L947】【F:data/vesc_help_group/text_slices/input_part006.txt†L955-L964】
- EU members considered bulk orders (e.g., via Jamessoderstrom) to amortize shipping and taxes but noted each controller still requires solder-ball cleanup before delivery.【F:data/vesc_help_group/text_slices/input_part006.txt†L952-L963】

### Charging & Battery Handling Safety
- Builders still see sizable sparks when connecting 20S packs battery-first; the recommended sequence remains mains-first, then pack, ideally via relay-equipped chargers or precharge leads to protect BMS hardware.【F:data/vesc_help_group/text_slices/input_part006.txt†L965-L1108】
- Gabe Enzo’s miswired battery short destroyed a relative’s BMS, underscoring the need to continuity-check 36 V harnesses and avoid powering bare ESCs without protection during bench tests.【F:data/vesc_help_group/text_slices/input_part006.txt†L1084-L1108】

### Reference Drops & Mod Guides
- Happy Giraffe reposted connector current charts, nickel-strip reinforcement rules, and resistor-divider recipes for Makerbase/Flipsky ignition mods, plus reminders to precharge before touching battery leads directly to control boards.【F:data/vesc_help_group/text_slices/input_part006.txt†L1162-L1183】
- The same dump bundled sourcing links for QS273 hubs, Magura brakes, Ant BMS units, chargers, harness hardware, and lighting that should be migrated into a formal resource catalog.【F:data/vesc_help_group/text_slices/input_part006.txt†L1184-L1190】

### QS273 & MP2 Calibration Debrief (Lines 1240-1554)
- Mirono measured roughly 10 mΩ phase-to-phase on a QS273, then spoofed phase resistance with a 10 mΩ series resistor to satisfy detection plausibility checks after Paolo recovered archived MP2 screenshots.【F:data/vesc_help_group/text_slices/input_part006.txt†L1262-L1288】
- Magnet-count confusion (estimates of 46 poles vs. reality) left speed telemetry wildly off during garden drag tests; Mirono flagged the need to log accurate pole counts before publishing benchmarks.【F:data/vesc_help_group/text_slices/input_part006.txt†L1427-L1525】
- Short garden pulls showed MP2 packs hitting low-speed torque limits and suggested that speed calibration plus longer test loops are required before sharing performance numbers.【F:data/vesc_help_group/text_slices/input_part006.txt†L1485-L1510】

### MTPA & Controller Behavior Debates
- Riders reported mixed results from Maximum Torque Per Amp: hub owners saw ~10 km/h gains by raising `iq_target`, but veterans warned it ignores battery amp limits and mainly benefits IPM motors, not QS273 hubs.【F:data/vesc_help_group/text_slices/input_part006.txt†L1510-L1554】
- Happy Giraffe noted IPM case studies where MTPA lowered motor temps, yet others stressed that test conditions must be controlled and that Makerbase firmware already reports higher RT amps than older Flipsky hardware when set identically.【F:data/vesc_help_group/text_slices/input_part006.txt†L1565-L1591】【F:data/vesc_help_group/text_slices/input_part006.txt†L1793-L1803】
- NetworkDir’s Makerbase binaries delivered the expected amps while LLT telemetry lagged, motivating requests to capture shunt measurements properly instead of relying on default scaling.【F:data/vesc_help_group/text_slices/input_part006.txt†L2191-L2206】

### Ninebot G30 Sleeper Projects & Regional Context
- Builders shared strategies for stuffing 20S6P/22S packs, dual controllers, and 11–12" hubs into G30 frames using 30 mm deck risers, dropout spacers, custom shafts, and repeated tear-downs to achieve stealthy sleepers.【F:data/vesc_help_group/text_slices/input_part006.txt†L1293-L1361】【F:data/vesc_help_group/text_slices/input_part006.txt†L1670-L1689】
- EU riders contrasted strict licensing with the “wild west” U.S. environment, motivating stealth paint, compact packaging, and even faux Euro plates to avoid unwanted attention.【F:data/vesc_help_group/text_slices/input_part006.txt†L1335-L1370】【F:data/vesc_help_group/text_slices/input_part006.txt†L1939-L1944】
- Jan’s custom LED tail/headlight builds leveraged neopixel rings and bespoke firmware, inspiring others to document printable mounts alongside controller and battery upgrades.【F:data/vesc_help_group/text_slices/input_part006.txt†L1753-L1780】

### Makerbase Dash Scripts & SmartDisplay Workflows
- Sombre_enfant confirmed older Xiaomi dashboard Lisp scripts no longer enumerate CAN peers on VESC 6.05 beta 23; Izuna advised reverting firmware or adopting the updated script tailored for newer betas.【F:data/vesc_help_group/text_slices/input_part006.txt†L1380-L1396】
- SmartDisplay dual setups still lean on Makerbase 75100s; when LLT dashboards bug out mid-ride, riders capture data with VESC Tool or consider Ant BMS telemetry for persistent watt/amp logging.【F:data/vesc_help_group/text_slices/input_part006.txt†L1606-L1619】【F:data/vesc_help_group/text_slices/input_part006.txt†L2201-L2204】

### Makerbase CAN-Bus Repairs & Power Mods
- PuneDir cataloged a repair flow for 75100 ALU boards: reflash both ESCs, inspect the 100 kΩ bias resistor across the MCP2551, swap the CAN transceiver, and verify the STM if comms stay dead.【F:data/vesc_help_group/text_slices/input_part006.txt†L1851-L1854】
- Ignition-induced cutoffs were tamed by adding 220 µF caps on the 12 V rail, 50 µF near gate drivers, and ensuring dual controllers power down simultaneously or via CAN switches to prevent one unit backfeeding the other.【F:data/vesc_help_group/text_slices/input_part006.txt†L2050-L2113】【F:data/vesc_help_group/text_slices/input_part006.txt†L2134-L2141】
- External DC/DC retrofits (first 12 V, then 5 V) kept scooters rolling while waiting for replacement SCT2A23A regulators, though repeated shorts highlighted the need for better diagnostics before injecting voltage into suspected faults.【F:data/vesc_help_group/text_slices/input_part006.txt†L1890-L1898】【F:data/vesc_help_group/text_slices/input_part006.txt†L2162-L2185】
- Konstantin later supplied replacement part numbers (Silergy SY8120/8121, RYCHIP RY3820E buck converters, CESD5V0D7 TVS) to streamline future repairs.【F:data/vesc_help_group/text_slices/input_part006.txt†L2306-L2311】

### Makerbase Fatigue & Missing Components (Lines 2401-2520)
- Long-time users vented about ALU boards being nearly irreparable, citing missing op-amps, toasted hall 5 V rails, and CAN boards that only revived after replacing absent INA181 current-sense amplifiers.【F:data/vesc_help_group/text_slices/input_part006.txt†L2405-L2510】
- Multiple failures pushed builders toward Ubox or Spintend replacements, while PuneDir kept experimenting with external 12 V/5 V supplies just to keep Makerbase hardware limping along.【F:data/vesc_help_group/text_slices/input_part006.txt†L2413-L2444】【F:data/vesc_help_group/text_slices/input_part006.txt†L2474-L2520】

### Dashboard Lisp & VESC Tool Tips
- Santiago’s Makerbase dashboard froze until caps were added to the SmartDisplay harness and the scooter profile was reactivated inside VESC Tool instead of editing Lisp code directly.【F:data/vesc_help_group/text_slices/input_part006.txt†L2459-L2514】
- Later in the slice, another rider fixed ABS over-current errors by re-enabling the Slow ABS Current Limit after each FOC detection and trimming throttle ramp times—useful reminders when defaults reset during setup.【F:data/vesc_help_group/text_slices/input_part006.txt†L3651-L3652】

### Bluetooth Security & Builder Onboarding
- Veteran members warned that open VESC Bluetooth adapters let bystanders change configs; enabling the “Pairing Done” flag, limiting proximity, or even swapping to custom ESP32 Wi-Fi firmware were suggested stopgaps.【F:data/vesc_help_group/text_slices/input_part006.txt†L2530-L2557】
- Her0DasH recommends wiring a handlebar button to cut Bluetooth power entirely when parking, while Happy Giraffe documented how the pairing flag can also lock out owners if misconfigured—USB recovery is mandatory.【F:data/vesc_help_group/text_slices/input_part006.txt†L2534-L2545】【F:data/vesc_help_group/text_slices/input_part006.txt†L2546-L2553】

### Entry-Level Upgrade Coaching & Adaptive Mobility
- Newcomer “Bitchass mother Bungle” received guidance to avoid mixing worn 36 V packs in series, focus on healthier 48 V batteries or a single VESC upgrade, and repurpose spare hubs for a friend’s bike rather than chasing AWD too soon.【F:data/vesc_help_group/text_slices/input_part006.txt†L2522-L2590】
- The same thread spun into creative wheelchair tow conversions, with members sharing historical scooter-hitch kits and encouraging solid locking mounts plus redundant restraints before hauling family members.【F:data/vesc_help_group/text_slices/input_part006.txt†L2689-L2762】

### Battery Sag & Cell Comparisons (Lines 2575-2600)
- The crew reiterated that voltage sag stems from internal resistance and nickel layouts; Samsung 40T cells handle ~25 A comfortably while Molicel P42A/P45B remain the better choice above 30 A bursts.【F:data/vesc_help_group/text_slices/input_part006.txt†L2575-L2595】
- Active balancing BMS units become critical when charging to only 90–95 %, and larger parallel counts remain the simplest way to slow degradation.【F:data/vesc_help_group/text_slices/input_part006.txt†L2598-L2600】【F:data/vesc_help_group/text_slices/input_part006.txt†L3848-L3860】

### Tooling & Measurement Nuggets
- NetworkDir highlighted a programmable milli-ohm meter capable of 1.8 mΩ resolution with USB scripting support for automated cell logging, and haku flagged budget-friendly capacitor-based spot welders that need minor mods for reliability.【F:data/vesc_help_group/text_slices/input_part006.txt†L3028-L3047】【F:data/vesc_help_group/text_slices/input_part006.txt†L3645-L3648】

### Controller Brand Debates & Race Insights (Lines 3188-3414)
- Ongoing banter compared Tronic, 3Shul, Makerbase, and G300 controllers—Rage Mechanics flexed a 22S10P dual XHS75 build peaking near 33 kW, while Rosheee defended sticking with Tronic despite repeated capacitor blowouts.【F:data/vesc_help_group/text_slices/input_part006.txt†L3188-L3341】
- Heated exchanges over “curry ESC” insults underscored strained vendor relations and the importance of professional communication when requesting firmware drops.【F:data/vesc_help_group/text_slices/input_part006.txt†L3349-L3395】

### Teverun Pouch Cell Hype vs. Reality
- Teverun 7260R owners bragged about 900 A blade cells with minimal sag, but Paolo and PuneDir dismissed the marketing, noting the packs are single-parallel, likely 8 C at best, heavier than cylindrical builds, and far less impact-resistant.【F:data/vesc_help_group/text_slices/input_part006.txt†L3495-L3577】
- Follow-up chatter weighed Molicel-based 20S14P packs (~630 A peak) against the pouch option, concluding cylindrical cells still win for safety and packaging flexibility despite slightly lower advertised C-rates.【F:data/vesc_help_group/text_slices/input_part006.txt†L3570-L3585】

### Brake Upgrades & Zoom Caliper Warnings
- Zoom hydraulic brakes were universally panned for high-power scooters; Shimano Saint, Hope Tech4 V4, Trickstuff, or even 3 mm stainless rotors were championed for builds chasing 250–300 A charge/discharge spikes.【F:data/vesc_help_group/text_slices/input_part006.txt†L3609-L3640】【F:data/vesc_help_group/text_slices/input_part006.txt†L3677-L3698】
- Jan recounted demagnetizing Magura calipers after 800 °C track abuse and recommended 160 mm+ rotors at 3 mm thickness for sustained racing duty cycles.【F:data/vesc_help_group/text_slices/input_part006.txt†L3688-L3703】

### Rion & High-End Scooter Reality Checks
- Riders praised 100 V Tronic 250R Rions as “perfect toys,” yet track veterans called out carbon flex, 140 mm brake fade, and on/off throttle behavior that make stock Rions unfit for serious racing without major reinforcement.【F:data/vesc_help_group/text_slices/input_part006.txt†L3657-L3702】
- Subsequent debate compared pouch vs. cylindrical builds in boutique scooters, with many noting Rion phase wiring lags far behind mainstream Segway GT2 hardware.【F:data/vesc_help_group/text_slices/input_part006.txt†L3703-L3793】

### Charging Habits, Wire Gauge & Pack Builds
- Gabe Enzo’s “Alzheimer issue” on macOS VESC Tool 6.02/6.05 drove him to Windows, while peers reiterated thicker phase leads cut waste heat and that heat equals lost performance.【F:data/vesc_help_group/text_slices/input_part006.txt†L3798-L3813】
- Simone showcased a 20S4P Samsung 30T pack claiming 150 A nominal/400 A burst; the group reminded builders that instantaneous current claims hinge on thermal limits, BMS ratings, and good welding practice—especially when debating copper vs. nickel bus bars.【F:data/vesc_help_group/text_slices/input_part006.txt†L3814-L3892】

### Shop Tooling, Fabrication & Printing Notes
- Copper-to-nickel welding experiments on 0.2 mm stacks proved finicky even at 25 % welder power, and veterans recommend welding copper directly to copper or cells to avoid brittle nickel interfaces.【F:data/vesc_help_group/text_slices/input_part006.txt†L1626-L1667】【F:data/vesc_help_group/text_slices/input_part006.txt†L2145-L2149】
- Budget soldering kits lack the thermal mass for pack work; the crew favors 80 W+ irons or branded stations, plus higher-end screw-terminal controllers like the 3Shul CL series for reliable wiring serviceability.【F:data/vesc_help_group/text_slices/input_part006.txt†L1581-L1593】【F:data/vesc_help_group/text_slices/input_part006.txt†L1699-L1705】
- PETG emerged as the go-to filament for outdoor scooter prints, with ASA/ABS reserved for climates hitting ~48 °C; builders caution against prolonged UV exposure without shielding.【F:data/vesc_help_group/text_slices/input_part006.txt†L2318-L2327】

### Battery Selection, Magnet Repair & Emerging Cells
- Magnet mishaps should be addressed with dedicated adhesives rather than generic epoxies; regluing cracked hub magnets is only a stopgap and merits inclusion in maintenance FAQs.【F:data/vesc_help_group/text_slices/input_part006.txt†L1903-L1919】
- Battery buyers weighed Samsung 40T, Molicel P42A/P45B, and 30T trade-offs (pricing, 45 A peak claims, internal resistance 7–9 mΩ) while noting Slack Core’s 20S9P packs already ship 40Ts—useful context for matching 350 A BMS hardware.【F:data/vesc_help_group/text_slices/input_part006.txt†L1940-L1995】
- EVE’s teased 21700 40PL cell (223 Wh/kg, 100 A discharge, 5 Ah) sparked skepticism about marketing vs. real cycle life, reinforcing the need for verification before integrating into builds.【F:data/vesc_help_group/text_slices/input_part006.txt†L2219-L2267】

### Makerbase Diagnostics & Knowledge Dumps
- Mirono argued Makerbase hardware behaves like a sturdier Flipsky successor, though real-world logs showed LLT dashboards under-reporting amps and spurred calls to measure shunts accurately or adjust firmware configs.【F:data/vesc_help_group/text_slices/input_part006.txt†L2201-L2208】【F:data/vesc_help_group/text_slices/input_part006.txt†L2191-L2206】
- PuneDir’s schematic critiques revealed inaccurate silkscreen references on 12 V/5 V regulators, prompting the team to maintain up-to-date documentation for ALU vs. box variants.【F:data/vesc_help_group/text_slices/input_part006.txt†L2339-L2349】

### Telemetry, Safety & Support Threads
- Face de Pin Sucé’s 65 kW CL1400 pulls kept ESC temps near 51 °C while the motor “chilled,” yet peers cautioned that sharing telemetry without braking specs can mask risk envelopes.【F:data/vesc_help_group/text_slices/input_part006.txt†L2368-L2374】【F:data/vesc_help_group/text_slices/input_part006.txt†L1540-L1592】
- Mirono, PuneDir, and sombre_enfant diagnosed missing-phase stutter on Makerbase fronts, typically tied to dead gate drivers, weak cells, or CAN desync—reminding builders to verify hardware after raising amp limits.【F:data/vesc_help_group/text_slices/input_part006.txt†L2119-L2134】【F:data/vesc_help_group/text_slices/input_part006.txt†L2363-L2379】
- Tronic 240R owners experiencing cutoffs at speed were urged to rely on official VESC Tool diagnostics rather than third-party telemetry apps when fresh detections trigger rear-motor noise or non-response at high RPM.【F:data/vesc_help_group/text_slices/input_part006.txt†L2379-L2400】

### Battery Busbar Debates & Pack Layout (Lines 3901-3924)
- Gabe Enzo questioned whether copper strips are easier than full sheets for pack tops, but Mirono prefers sheet stock because it covers the entire cell cap and costs less than pre-cut copper, noting low-power (7–9 kW) builds may not need copper at all if layouts and current targets stay modest.【F:data/vesc_help_group/text_slices/input_part006.txt†L3904-L3917】
- External cell plates and holders sparked disagreement: Gabe skips plastic holders to save height, while others cautioned that external parallel connections demand careful layout to avoid imbalance myths and packaging issues.【F:data/vesc_help_group/text_slices/input_part006.txt†L3920-L3924】

### MP2 Telemetry & Temperature Sensor Compatibility (Lines 3964-4012)
- Mirono’s budget Bluetooth module logged 300 A pulls without dropping packets, reinforcing that MP2 setups can stay connected under heavy load even as Paolo rated Makerbase 75200 hardware worse than MP2 for reliability.【F:data/vesc_help_group/text_slices/input_part006.txt†L3964-L3990】
- Builders confirmed VESCs expect two-wire thermistors, recommending 10 kΩ NTC probes over 100 kΩ parts or KTY sensors unless the controller firmware explicitly supports them, and reminding newcomers to share the temp lead with controller ground.【F:data/vesc_help_group/text_slices/input_part006.txt†L3994-L4012】

### Controller Fault Diagnostics & PI Tuning (Lines 4051-4233)
- Mirono reported persistent phase-filter errors on throttle lift-off, prompting JPPL to suggest iterating current-loop KP/KI gains in 500–1000 point steps to trade torque aggressiveness for smoothness once current and input limits are dialed.【F:data/vesc_help_group/text_slices/input_part006.txt†L4051-L4053】【F:data/vesc_help_group/text_slices/input_part006.txt†L4210-L4231】
- JPPL also shared industrial tuning references (Technosoft/Ingenia guides) for riders wanting deeper control theory context after controller swaps such as Kelly-to-Wolf motor conversions.【F:data/vesc_help_group/text_slices/input_part006.txt†L4221-L4232】

### Tubeless Split Rims & Tire Sealing (Lines 4244-4265)
- First-time tubeless split-rim owners were advised to inspect the central rubber ring, cinch the carcass with zip ties, and blast it with CO₂ or a strong compressor to seat the bead—acknowledging these rims are finicky to seal compared with tube setups.【F:data/vesc_help_group/text_slices/input_part006.txt†L4244-L4267】

### Suspension Geometry & Steering Stability (Lines 4271-4300)
- Members panned double steering dampers on Teverun 7260R builds, arguing the fork geometry already lacks trail; Segway GT girder arms, Inmotion RS forks, or moto-style straight forks with proper trail were held up as safer high-speed templates.【F:data/vesc_help_group/text_slices/input_part006.txt†L4271-L4300】

### Display & Dashboard Options (Lines 4501-4560)
- UKC1 TFT displays need custom Lisp firmware to speak CAN with VESCs, whereas VSETT dashboards work with the AK script; several riders default to ruggedized phones or Metr Pro units for richer telemetry despite the extra battery drain.【F:data/vesc_help_group/text_slices/input_part006.txt†L4501-L4560】

### Cell Testing & IR Measurement Practices (Lines 4740-4785)
- Fresh Samsung 40T shipments measured 10–11 mΩ on four-wire meters; Mirono recommends keeping high-current pack cells under ~30–50 mΩ and sees specialized meters as most valuable for reclaimed cells rather than brand-new stock.【F:data/vesc_help_group/text_slices/input_part006.txt†L4740-L4785】
- Veterans noted that true low-resistance readings require Kelvin probes or AC injectors; otherwise lead resistance can overshadow cell impedance and waste time when vetting new cells.【F:data/vesc_help_group/text_slices/input_part006.txt†L4748-L4772】

### Brake & Control Quirks (Lines 4803-4852)
- Riders debugging reverse pulses when pulling analog brakes were reminded to use the “ADC2 brake no reverse” mode so idle regen doesn’t jerk the wheel backwards at a stop.【F:data/vesc_help_group/text_slices/input_part006.txt†L4803-L4852】

### Observer Drift & Low-Temperature Compensation (Lines 4839-4864)
- Cold-weather MP2 users saw the observer lose track when the system switched sensorless; suggested mitigations included enabling the temperature compensator, extending hall sensor usage, or manually trimming phase resistance until the motor warms up.【F:data/vesc_help_group/text_slices/input_part006.txt†L4839-L4864】

### Packaging & Thermal Management for Dual VESC Builds (Lines 4870-4921)
- Gabe sketched dual-VESC mounts clamped to an aluminium “brick” inside a Xiaomi frame; peers recommended splitting controllers across the frame or external heatsinks, reminded him that 20S packs may still need external bags, and emphasized matching hall sensors for clean startups.【F:data/vesc_help_group/text_slices/input_part006.txt†L4870-L4923】

### Cell Sourcing & Pricing Reality Checks (Lines 4929-4933)
- Paolo urged buyers to avoid sourcing cells directly from China despite attractive $2.15–$2.25 quotes, citing higher risk and shipping premiums even though manufacturing still happens there, while EU members noted domestic factories ease compliance.【F:data/vesc_help_group/text_slices/input_part006.txt†L4929-L4933】

### Legal Compliance & Suspension Debates (Lines 5201-5319)
- Jan restated Switzerland’s micromobility limits—500 W, 20 km/h, ≤ 50 V, fixed reflectors, and no blinkers—to explain why local police impound faster builds, prompting veterans to insist on dual hydraulics once speeds exceed 40 km/h.【F:data/vesc_help_group/text_slices/input_part006.txt†L5204-L5274】
- Mirono and others again trashed Monorim trapezoid forks as profit-driven compromises, pointing riders at Segway’s GT2 geometry or Dereza/Konyk conversions when chasing high-speed stability.【F:data/vesc_help_group/text_slices/input_part006.txt†L5218-L5253】

### Battery Packaging & Volume Planning (Lines 5443-5907)
- G30/Pro2 modders compared 2 L vs. 3 L battery boxes, concluding 20S3P barely fits a 3 L enclosure and that external BMS mounting sacrifices weatherproofing even if it frees deck volume for 20S7P Molicel packs.【F:data/vesc_help_group/text_slices/input_part006.txt†L5443-L5462】【F:data/vesc_help_group/text_slices/input_part006.txt†L5467-L5476】
- Follow-up measurements pegged the stock G30 frame at ~120 internal 21700 slots (plus 60 in the neck) before spacers, so builders planning 20S10P need risers or auxiliary enclosures despite dreams of fully internal packs.【F:data/vesc_help_group/text_slices/input_part006.txt†L5873-L5889】【F:data/vesc_help_group/text_slices/input_part006.txt†L5900-L5907】

### Controller Cooling & Enclosure Strategy (Lines 5713-5759)
- Group consensus dismissed stick-on fans: bolt the VESC base to a solid aluminium plate, add thermal paste, or even pot the PCB in dielectric epoxy instead of relying on airflow inside a closed deck.【F:data/vesc_help_group/text_slices/input_part006.txt†L5713-L5744】
- Builders also reminded each other that tidy cable routing still allows dual controllers inside compact decks if every harness is planned, reserving exterior mounts for true space shortages.【F:data/vesc_help_group/text_slices/input_part006.txt†L5754-L5759】

### Firmware Beta Instability & Lisp Script Maintenance (Lines 5911-6079 & 6520-6533)
- Izuna and Ion spent the week hot-patching Makerbase dashboards after VESC Tool BETA 23 broke ADC scripts; the fix involved reverting to hand-built 6.05 binaries, adding button debouncing, and filing CAN regressions with Vedder.【F:data/vesc_help_group/text_slices/input_part006.txt†L5911-L6045】【F:data/vesc_help_group/text_slices/input_part006.txt†L6056-L6079】
- Later tests confirmed older 6.05 BETA 15 builds remain the stable baseline for dual setups until Vedder resolves CAN-cmd crashes introduced after October 2022.【F:data/vesc_help_group/text_slices/input_part006.txt†L6520-L6533】

### Retail Fires & German-Market Detunes (Lines 5808-6002)
- Footage of an IO Hawk warehouse fire resurfaced doubts about their reworked Kaabo/Vsett packs, with locals noting German-spec models drop to 13S–14S batteries, lower-power controllers, and steep prices despite corrosion issues out of the box.【F:data/vesc_help_group/text_slices/input_part006.txt†L5808-L5999】

### Ferrofluid Cooling & Phase-Wire Limits (Lines 6017-6125 & 6374-6464)
- Mirono reiterated that genuine Statorade (5–6 ml per hub) is the safe ferrofluid benchmark—more just adds drag and heat—while Happy Giraffe warned to watch magnet temps above 80 °C when using it for cooling.【F:data/vesc_help_group/text_slices/input_part006.txt†L6017-L6035】
- Xiaomi and Blade owners compared motor lead gauges, deciding stock 18 AWG enamel wires tolerate brief 100 A ESC surges but that serious 3.5 kW builds should step up to 15–10 AWG phase leads and add temp sensors before chasing 170 A phase targets.【F:data/vesc_help_group/text_slices/input_part006.txt†L6095-L6125】【F:data/vesc_help_group/text_slices/input_part006.txt†L6374-L6464】

### Field-Weakening Brake Hazards (Lines 6268-6311)
- A Shitsky 75100 rider documented the wheel “locking” near base speed when releasing the throttle under field weakening, reinforcing the need to tune regen ramps—or disable FW—on low-power scooters to avoid sudden traction loss at ~50 km/h.【F:data/vesc_help_group/text_slices/input_part006.txt†L6268-L6311】

### 3D Printing Ramp-Up & Filament Selection (Lines 5459-6573)
- Bambu Lab X1C owners encouraged newcomers to lean on Fusion 360 for CAD, Bambu Studio for slicing, and to dry PETG/nylon spools, noting carbon-fiber-filled filaments stay conductive and demand extra care around packs.【F:data/vesc_help_group/text_slices/input_part006.txt†L5459-L5463】【F:data/vesc_help_group/text_slices/input_part006.txt†L6553-L6588】

### Troubleshooting Dual-VESC Start-Up Jitter (Lines 6656-6660)
- A Vsett 10+ owner running dual Spintend 80/100s reported the rear motor stuttering on take-off, pointing future reviewers to inspect hall solder joints and CAN cabling when secondary controllers lag the master.【F:data/vesc_help_group/text_slices/input_part006.txt†L6656-L6660】

## Follow-ups / Open Questions
- Capture Glitter 811H best-practice weld settings (power vs. strip thickness) so builders stop blowing through nickel when transitioning to copper stacks.【F:data/vesc_help_group/text_slices/input_part006.txt†L324-L366】
- Document SmartDisplay dual-controller recipes (master/slave current splits, traction control values) shared during the 22S wet-track tests for repeatable setups.【F:data/vesc_help_group/text_slices/input_part006.txt†L161-L181】
- Track the Tronic 2000/TOLT project for release timelines, gate-driver strategies beyond 54 MOSFETs, and thermal practices applicable to DIY controllers.【F:data/vesc_help_group/text_slices/input_part006.txt†L500-L519】
- Publish a Makerbase ignition/CAN retrofit guide covering connector swaps, resistor and capacitor mods, and safe shutdown ordering before powering dual stacks.【F:data/vesc_help_group/text_slices/input_part006.txt†L630-L755】【F:data/vesc_help_group/text_slices/input_part006.txt†L2050-L2141】
- Test the shared Makerbase firmware binaries, log default shunt calibration factors, and verify Android/VESC Tool compatibility across Samsung A-series and Xiaomi dashboards.【F:data/vesc_help_group/text_slices/input_part006.txt†L777-L821】【F:data/vesc_help_group/text_slices/input_part006.txt†L1187-L1215】
- Triage Happy Giraffe’s resource dump—and Konstantin’s later BOM additions—into structured sourcing/how-to pages for quick reference (connectors, regulator replacements, magnet adhesives).【F:data/vesc_help_group/text_slices/input_part006.txt†L1162-L1190】【F:data/vesc_help_group/text_slices/input_part006.txt†L2306-L2311】
- Build a QS273/MP2 tuning checklist that captures magnet counts, speed-sensor calibration, drag-race data logging, and guardrails for when MTPA is safe on hub motors.【F:data/vesc_help_group/text_slices/input_part006.txt†L1262-L1554】
- Consolidate Makerbase repair anecdotes into a troubleshooting flow (caps, regulators, CAN transceivers, external DC/DC wiring) so repeat failures like PuneDir’s are easier to diagnose.【F:data/vesc_help_group/text_slices/input_part006.txt†L1851-L2149】
- Expand the battery guide with 40T/P42A/P45B pricing vs. performance comparisons plus notes on emerging cells (EVE 40P/40PL, 58E) and vetted magnet adhesives for maintenance.【F:data/vesc_help_group/text_slices/input_part006.txt†L1903-L1995】【F:data/vesc_help_group/text_slices/input_part006.txt†L2219-L2267】
- Capture repeatable steps for the VESC Tool BETA 23 CAN/Lisp regression so we can recommend known-good firmware/script pairs until Vedder ships a fix.【F:data/vesc_help_group/text_slices/input_part006.txt†L5911-L6079】【F:data/vesc_help_group/text_slices/input_part006.txt†L6520-L6533】
- Document field-weakening braking safeguards (regen ramping, FW disable thresholds) for sub-1 kW scooters to prevent the wheel-stall behavior reported here.【F:data/vesc_help_group/text_slices/input_part006.txt†L6268-L6311】
- Summarize PETG/CF filament handling (drying, conductivity, printer settings) for battery or enclosure prints so newcomers avoid conductive plastics in live-pack areas.【F:data/vesc_help_group/text_slices/input_part006.txt†L6553-L6588】
- Follow up with the Vsett 10+ dual Spintend owner once hall/CAN checks are done to confirm whether the rear motor jitter was wiring, detection, or hardware related.【F:data/vesc_help_group/text_slices/input_part006.txt†L6656-L6660】
- Document best practices for locking down VESC Bluetooth (pairing workflows, hardware kill switches, Wi-Fi alternatives) before publishing dual-controller setup guides.【F:data/vesc_help_group/text_slices/input_part006.txt†L2530-L2557】
- Capture a teardown of the Rage Mechanics 22S10P dual XHS75 build (33 kW logs, thermal management, SmartDisplay deltas) to benchmark against Tronic/3Shul claims.【F:data/vesc_help_group/text_slices/input_part006.txt†L3315-L3336】
- Verify Teverun 7260R pouch-cell claims with instrumented discharge and charge testing (C-rate, weight, enclosure safety) before recommending the chemistry over cylindrical alternatives.【F:data/vesc_help_group/text_slices/input_part006.txt†L3495-L3585】
- Build a braking reference for 250 A+ scooters comparing Zoom, Shimano Saint, Hope Tech4, Magura, and Trickstuff performance including rotor sizing and fade behavior.【F:data/vesc_help_group/text_slices/input_part006.txt†L3609-L3703】
- Investigate macOS-specific bugs in VESC Tool 6.02/6.05 that corrupt settings and document Windows/Linux workarounds until an upstream fix lands.【F:data/vesc_help_group/text_slices/input_part006.txt†L3798-L3805】
- Publish copper sheet vs. strip guidance for mid-power pack builds so newcomers understand when nickel alone suffices and how to package external busbars safely.【F:data/vesc_help_group/text_slices/input_part006.txt†L3904-L3924】
- Compile an MP2 temperature-sensor compatibility table (NTC vs. KTY values, wiring diagrams, firmware expectations) for quick reference during controller swaps.【F:data/vesc_help_group/text_slices/input_part006.txt†L3964-L4012】
- Draft a tubeless split-rim sealing checklist (gasket inspection, tie-down methods, inflation tools) for the resources hub.【F:data/vesc_help_group/text_slices/input_part006.txt†L4244-L4267】
- Turn the UKC1/VSETT display integration chatter into a step-by-step guide covering required Lisp scripts and CAN wiring caveats.【F:data/vesc_help_group/text_slices/input_part006.txt†L4501-L4560】
- Validate low-temperature observer and hall handoff settings on MP2 builds, documenting resistance tweaks or compensator use that prevent cold-start desync.【F:data/vesc_help_group/text_slices/input_part006.txt†L4839-L4864】
