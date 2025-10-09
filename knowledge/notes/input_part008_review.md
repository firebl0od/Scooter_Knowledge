# input_part008.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part008.txt`
- Coverage: 2024-04-15T15:15 through 2024-05-14T02:10 (lines 1-7200)
- Next starting point: Resume at 2024-05-14T02:11 (line ~7201).

## Key Findings

### Battery Architecture & Materials
- Builders debating 20s20p packs concluded that pure nickel can work when individual cells are limited to ~5 A; copper only becomes necessary if the layout cannot provide enough parallel cross-section, reinforcing the need to compute current paths rather than relying on cell count alone.【F:data/vesc_help_group/text_slices/input_part008.txt†L14-L38】
- PuneDir pairs large packs with 200 A ANT/JK BMS options and has even used a 100 A JK on a 70 A-rated battery, showing the community tendency to oversize BMS hardware for reliability headroom.【F:data/vesc_help_group/text_slices/input_part008.txt†L14-L21】
- Complex holderless layouts fit 20s7p (21700) batteries plus dual controllers in a Zero 10X only by adding a 45 mm deck extender and meticulous insulation—evidence that internal 20s packs demand custom machining or spacers.【F:data/vesc_help_group/text_slices/input_part008.txt†L168-L200】
- Copper-enhanced busbars (e.g., Wellgo nickel-copper laminate) run about $150 shipped for a 20s10p pack when sourced via Alibaba; builders solder copper wire onto welded nickel after the fact to lower resistance without heating cells directly.【F:data/vesc_help_group/text_slices/input_part008.txt†L742-L767】

### Wiring & Phase Leads
- Heavy scooters such as QS273 builds are jumping from melted stock leads to 7 AWG or thicker phase wire, while others confirm 10 AWG is the practical minimum for 60H/70H-class motors when space allows.【F:data/vesc_help_group/text_slices/input_part008.txt†L7-L14】【F:data/vesc_help_group/text_slices/input_part008.txt†L1095-L1101】
- Community members warn that simply soldering bulk material onto cell ends is a poor conductor upgrade—reinforce strips with copper wire instead of puddling solder on the cell cans.【F:data/vesc_help_group/text_slices/input_part008.txt†L759-L767】

### Thermal Management & Heatsinking
- Spintend controllers are viewed as dissipating roughly half the heat of comparable Tronic units, yet even higher-end ESCs like the 84100 still run hot when pushed to ~180 A, underscoring the need for large external heatsinks and fresh thermal paste.【F:data/vesc_help_group/text_slices/input_part008.txt†L133-L165】
- Riders report Nucular 12-FET controllers handling 210 A at 48 °C when simply clamped to deck aluminum, showing the payoff of robust MOSFET packages and good contact pressure.【F:data/vesc_help_group/text_slices/input_part008.txt†L160-L166】
- Routine desktop maintenance advice (reapplying thermal paste every ~2 years, cleaning heatsinks) is being applied to ESC care, reinforcing the parallel between PC cooling and VESC thermal upkeep.【F:data/vesc_help_group/text_slices/input_part008.txt†L166-L173】
- Single-drive NAMI builds on steep climbs still push a lone Tronic 250 to ~60 °C, while dual-drive riders on similar hardware stay below 40 °C, highlighting how load sharing and solid thermal mounting change real-world temperature ceilings.【F:data/vesc_help_group/text_slices/input_part008.txt†L4871-L4886】

### Controller Reliability & Power Interrupts
- Multiple builders note that MKSESC 84/200 HP units can blow MOSFETs whenever a BMS trips under load, whereas Spintend Ubox and 3Shul hardware tend to survive; mitigation includes avoiding BMS-triggered cutoffs, running lower currents, or paralleling packs.【F:data/vesc_help_group/text_slices/input_part008.txt†L688-L705】
- CL350-class controllers appear more tolerant of brief supply interruptions, especially when supplemented with additional 12 V capacitance, hinting at design differences in input filtering.【F:data/vesc_help_group/text_slices/input_part008.txt†L700-L704】

### Motor Maintenance & Cleaning
- For contaminated Bafang BBSHD mid-drives, the recommended workflow is compressed air first, followed by brake cleaner or alcohol applied sparingly with lint-free cloths; avoid microfiber wipes that shed fibers, and be cautious around PCB adhesives and magnet glue.【F:data/vesc_help_group/text_slices/input_part008.txt†L977-L1015】
- Brake cleaner residue evaporates quickly, but builders still plan to dry stators with compressed air and ensure windings aren’t left soaked to protect insulation.【F:data/vesc_help_group/text_slices/input_part008.txt†L1003-L1014】

### Fitment & Drivetrain Notes
- Discussions confirm that VSETT 11+ frames can physically accommodate up to ~90H rear motors (≈170 mm dropout) but remain limited by narrower front dropouts (~145 mm), constraining mixed 70H/90H upgrades without machining.【F:data/vesc_help_group/text_slices/input_part008.txt†L1162-L1178】
- Stock VSETT throttles and controllers demand significant rewiring for smooth behavior; riders replacing Kelly and YYK square-wave units note drastic improvements in control feel with modern FOC setups despite added configuration effort.【F:data/vesc_help_group/text_slices/input_part008.txt†L606-L646】【F:data/vesc_help_group/text_slices/input_part008.txt†L1124-L1144】

### Suspension, Frames & Big-Chassis Options
- Dualtron Thunder owners swapping to NAMI chassis praise hydraulic dampers for comfort while crediting elastomer suspension blocks with high-speed stability, framing the choice as comfort vs. control when upgrading legacy frames.【F:data/vesc_help_group/text_slices/input_part008.txt†L1224-L1233】
- Janobike X11/X20 shells have been stretched to host 23s10p–24s packs plus Kelly controllers, with PMT T41 11" slicks and 75H hub motors fitting once the deck is widened—evidence that large-capacity conversions demand both enclosure machining and tire clearance planning.【F:data/vesc_help_group/text_slices/input_part008.txt†L1255-L1288】
- Builders eyeing QS138 motorcycle conversions expect ~30–40 kW potential but are reminded that controller and battery limits (≥300 A phase, quality cells) dictate achievable torque; cheap LG M26 cells sag badly compared with P45B/P42A-class packs.【F:data/vesc_help_group/text_slices/input_part008.txt†L2084-L2223】【F:data/vesc_help_group/text_slices/input_part008.txt†L2379-L2416】

### Traction Control & Tire Selection
- Traction control helps rein in front-wheel slip up to ~55 mph, but riders also cut front phase amps to keep dual-drive builds manageable.【F:data/vesc_help_group/text_slices/input_part008.txt†L1425-L1431】
- Xuancheng 12" slicks are deemed budget-friendly yet inadequate for high-power launches; peers steer riders toward CST or PMT rubber, while 11x3.5" alternatives broaden the contact patch for scooters that can fit them.【F:data/vesc_help_group/text_slices/input_part008.txt†L1434-L1451】
- Rural riders rotating between slicks and Xuancheng Stradale tires note the latter’s durability on gravel access roads, reserving PMTs for track use.【F:data/vesc_help_group/text_slices/input_part008.txt†L2318-L2320】
- NetworkDir is chasing wider 10" tires after discovering that CST 10×3 rubber wobbles violently from 0–40 km/h if traction control is disabled, underscoring how tire profile interacts with electronic aids at launch.【F:data/vesc_help_group/text_slices/input_part008.txt†L4103-L4109】

### Makerbase ESC Failures & Repair Attempts
- A fresh Makerbase 84100 HP locked both motors while coasting, echoing earlier 75100 deaths tied to hall shorts and melted motor leads; the owner now distrusts the platform despite temporary recovery.【F:data/vesc_help_group/text_slices/input_part008.txt†L1463-L1508】
- Post-mortem chat highlights that the 84100 HP senses current via phase shunts rather than resistors, uses the same MOSFET set as older 75100 boards, and may ship with questionable component quality—fueling suspicions about counterfeit silicon.【F:data/vesc_help_group/text_slices/input_part008.txt†L1550-L1569】
- DIY repairs involve swapping MOSFETs and gate drivers harvested from scrap controllers, but ripped traces and repeated failures push riders toward Spintend or 3Shul replacements instead of another Makerbase warranty cycle.【F:data/vesc_help_group/text_slices/input_part008.txt†L1573-L1592】【F:data/vesc_help_group/text_slices/input_part008.txt†L1632-L1639】
- Later chats reiterate that repaired FlipSky/Makerbase 75xxx boards can still brake unexpectedly if upstream logic fails, so builders replace STM MCUs and gate drivers together, watch for wrong auto-detection values (e.g., 450 µH inductance), and sometimes relocate the motor to the rear to minimize crash risk when an ESC seizes.【F:data/vesc_help_group/text_slices/input_part008.txt†L5071-L5088】

### Battery Building & BMS Lessons
- Pack builders warn that piercing a cell or leaving it compromised invites cascading failures; pierced EV cells can trigger chain reactions if reused, so damaged cells should be scrapped immediately.【F:data/vesc_help_group/text_slices/input_part008.txt†L1809-L1816】
- Wiring 20s8p builds exposed common mistakes: swapping internal pack polarity or reversing balance leads leaves the first series group reading 0 V and can cook BMS components, stressing the need to land B− before balance taps and to verify sockets stepwise (3.5 V, 7 V, etc.).【F:data/vesc_help_group/text_slices/input_part008.txt†L1980-L2018】【F:data/vesc_help_group/text_slices/input_part008.txt†L2035-L2059】
- High-current packs rely on doubled 6 AWG leads or laminated copper straps, but builders caution that poor routing becomes a fire hazard and PETG enclosures can soften if heavy leads are soldered in after assembly.【F:data/vesc_help_group/text_slices/input_part008.txt†L1957-L1977】【F:data/vesc_help_group/text_slices/input_part008.txt†L2341-L2345】
- Honeycomb fish-paper layouts let Xiaomi Pro 2 owners squeeze 20s5p internally without spacers, but the group stresses that holderless builds demand meticulous insulation and that bag batteries max out near 20s6p unless you accept risky 7p stacking.【F:data/vesc_help_group/text_slices/input_part008.txt†L4862-L4864】【F:data/vesc_help_group/text_slices/input_part008.txt†L4851-L4854】
- Riders mapping G30 deck space argue you can barely fit ~112–120 horizontal 21700 cells, equating to ~17s8p with careful copper folding, yet veterans warn that published photos often hide compromised BMS placement and that mixing aged gray and purple LG M26 variants can upset pack balance.【F:data/vesc_help_group/text_slices/input_part008.txt†L5121-L5156】【F:data/vesc_help_group/text_slices/input_part008.txt†L5218-L5232】
- Salvaged vape cells show severe imbalance and unknown provenance; even hobby experiments concede the cells are “pocket size cancer,” reinforcing why the group discourages reusing disposable packs in serious builds.【F:data/vesc_help_group/text_slices/input_part008.txt†L4792-L4815】

### Showcase Builds & Custom Frames
- Face de Pin Sucé unveiled a race-prepped scooter running a 22S11P pack, C350 controller, Hope Tech4 V4 brakes, and in-house–wound motors, highlighting the bespoke component level in European race paddocks.【F:data/vesc_help_group/text_slices/input_part008.txt†L2483-L2493】
- Simone is mixing NAMI Viper and Rion chassis cues to host a 22S10P pack, noting the fork had to be machined to clear 70H hubs and 3 mm discs, underscoring the fabrication required for oversized drivetrains.【F:data/vesc_help_group/text_slices/input_part008.txt†L2592-L2599】
- JPPL ordered a Titaone X10 carbon frame and warned that à la carte spares are “crazy expensive,” suggesting prospective builders budget for high replacement costs even when buying the bare chassis.【F:data/vesc_help_group/text_slices/input_part008.txt†L3033-L3056】

### VESC Displays & Instrumentation
- Mihail is prototyping a VESC touch display with LVGL, CAN-bus control, profile switching, and an onboard regulator that steps pack voltage to 5 V, and has 120 surplus 480×320 IPS panels wired via ESP32-S3 for future builds.【F:data/vesc_help_group/text_slices/input_part008.txt†L2501-L2507】【F:data/vesc_help_group/text_slices/input_part008.txt†L2583-L2587】
- Chris Culver already runs an LVGL-based dashboard and offered help, implying reusable firmware may exist for similar display projects.【F:data/vesc_help_group/text_slices/input_part008.txt†L2985-L2990】
- To minimize latency and preserve failsafe behavior, Mihail plans to leave throttle and brake sensors hard-wired to the ESC instead of routing them through CAN, even though the display PCB breaks those signals out.【F:data/vesc_help_group/text_slices/input_part008.txt†L2586-L2591】

### Braking Strategy & Regen Usage
- Riders experimenting with regen-heavy setups report -80 A electronic braking can nearly lift them over the bars, leading some to run regen-only while others stress the value of Spinny tuning to modulate force.【F:data/vesc_help_group/text_slices/input_part008.txt†L2522-L2538】
- Heavy scooters quickly chew through budget pads; veterans recommend full-metallic options (e.g., Galfer) and caution that bargain compounds from AliExpress often underperform despite marketing claims.【F:data/vesc_help_group/text_slices/input_part008.txt†L2539-L2567】
- Discussions about fitting motorcycle-caliber hardware (dual calipers per lever, Brembo swaps) conclude that weight and ergonomics remain trade-offs, though moto parts boost heat capacity for regen-averse riders.【F:data/vesc_help_group/text_slices/input_part008.txt†L2520-L2536】

### Charger & Accessory Sourcing
- Mirono recommended a €120–€160 adjustable charger line from AliExpress for 10S–16S packs, preferring it over repurposed server PSUs that failed after a few months of rewiring, while peers endorsed Huawei GTK units as reliable CC/CV alternatives.【F:data/vesc_help_group/text_slices/input_part008.txt†L2603-L2613】
- Members searching for cleaner control hardware highlighted Tusk’s Compact Control Switch as a premium but durable lighting cluster option when standard scooter switchgear feels flimsy.【F:data/vesc_help_group/text_slices/input_part008.txt†L3160-L3161】
- DIYers are building multi-voltage lighting harnesses with dedicated DC/DC rails, zener clamps, and weatherproof USB-C plugs to run blinkers, heated gear, chargers, and auxiliary lights from high-voltage packs without overloading a single converter.【F:data/vesc_help_group/text_slices/input_part008.txt†L3526-L3529】【F:data/vesc_help_group/text_slices/input_part008.txt†L3618-L3624】【F:data/vesc_help_group/text_slices/input_part008.txt†L4100-L4108】
- Kelly controllers include a 12 V accessory rail, but users still add converters for lighting and confirm that rear brake lights wired to the Pro 2 dash need ~100 Ω resistors when running off VESC AUX power to avoid burning LEDs.【F:data/vesc_help_group/text_slices/input_part008.txt†L4781-L4784】【F:data/vesc_help_group/text_slices/input_part008.txt†L5032-L5045】

### Field Weakening & Control Tuning
- Rosheee logged back-to-back pulls comparing pure current control, MTPA, and +40 A field weakening on dual Ubox hardware, showing how 16s6p test packs respond when FW is introduced at ~90 % duty cycle.【F:data/vesc_help_group/text_slices/input_part008.txt†L4220-L4237】
- Izuna’s MP2 v0.5 repeatedly tripped ABS overcurrent around 70 km/h despite 200 A phase limits, improving only after cutting battery current and switching to hall sensors, which underscores how firmware sample modes and hardware current limits interact on high-speed runs.【F:data/vesc_help_group/text_slices/input_part008.txt†L4913-L4920】【F:data/vesc_help_group/text_slices/input_part008.txt†L5250-L5258】

### PuneRon Prototype & Custom Drivetrains
- PuneDir’s “PuneRon” differential-scooter mock-up runs 60H motors geared 13/73 (moving to 13/80) and already hit 90 km/h on a borrowed Zero battery; he noted Makerbase 84100s survived accidental XT60 disconnects mid-ride but wants bigger sprockets for acceleration.【F:data/vesc_help_group/text_slices/input_part008.txt†L4273-L4286】【F:data/vesc_help_group/text_slices/input_part008.txt†L4714-L4728】
- The build team is machining 6 mm steel rear sprockets locally, planning water-cooled motor endplates, and debating whether drilled stators plus belt drives or steel chainrings give the best durability for 200 A setups.【F:data/vesc_help_group/text_slices/input_part008.txt†L4791-L4859】【F:data/vesc_help_group/text_slices/input_part008.txt†L5387-L5403】
- Battery packaging experiments suggest the frame bag holds ~5 L—enough for 20s6p with holders—while Zero 10X decks can accommodate 20s7p of LG M26 cells but leak under 60–70 A loads, prompting future upgrades to higher-grade chemistry.【F:data/vesc_help_group/text_slices/input_part008.txt†L4851-L4854】【F:data/vesc_help_group/text_slices/input_part008.txt†L5163-L5177】

### Spin-Y Throttle & Dashboard Integration
- Dualtron owners debugging the Spin-Y2 thumb throttle discovered the signal only registered after moving the lead to ESC B’s ADC1 port and feeding it 5 V instead of 3.3 V, implying ESC A’s ADC1 is disabled by default in some Ubox firmware revisions.【F:data/vesc_help_group/text_slices/input_part008.txt†L4290-L4390】
- Xiaomi Pro 2 riders running dual 75100s reuse the stock dash via custom scripts, keeping the throttle on a direct ADC input for traction control while splicing lighting into AUX power with series resistors to protect LEDs.【F:data/vesc_help_group/text_slices/input_part008.txt†L5018-L5046】

### Tire & Wheel Fitment Debates
- The group keeps steering 10" Zero/VSETT owners toward CST 10×3 or PMT 10×3.5 rubber, calling Xuancheng slicks soft but short-lived above 4 kW without traction control and warning that 10" rims look undersized with 165 mm rotors.【F:data/vesc_help_group/text_slices/input_part008.txt†L5000-L5034】【F:data/vesc_help_group/text_slices/input_part008.txt†L5593-L5599】
- Fork swaps to 145 mm travel assemblies slightly improve trail numbers on Zero 10X builds, though riders still rely on dampers and balanced phase currents (≈60 % rear) to tame wobble during launches.【F:data/vesc_help_group/text_slices/input_part008.txt†L5330-L5340】

### Cell Market Updates (May)
- Builders compare gray versus purple LG M26 inventory, reporting 14 mΩ IR on fresh Turkish stock versus >30 mΩ on older MH1 pulls, and reiterate that Samsung 35E/YR1035-class cells show lower resistance but can’t match high-current Molicels.【F:data/vesc_help_group/text_slices/input_part008.txt†L5201-L5233】
- Salvaged Navee N65 packs show leaking cells around 900 km, leading riders to plan full replacements with Aspilsan 18650s or sell the platform entirely rather than chase venting risks.【F:data/vesc_help_group/text_slices/input_part008.txt†L5544-L5590】

### Cell Market Updates
- Lisa confirmed EVE 40PL cylindrical pouches are available direct from the factory via Alibaba at roughly $4.35 per cell (minimum 50 units plus ~$100 shipping), making them attractive for bulk buyers despite steep logistics costs.【F:data/vesc_help_group/text_slices/input_part008.txt†L2681-L2699】
- Builders in high-tariff regions are stuck with €1 LG M26 cells versus €5–€11 for EVE or Molicel options, prompting debates about tolerating the sag temporarily and reselling later versus pausing builds until premium cells are affordable.【F:data/vesc_help_group/text_slices/input_part008.txt†L4111-L4135】

### Geometry, Stability & Safety Incidents
- Multiple riders called out Vsett 10+ and other C-fork scooters for instability above ~80 km/h, citing fatal crashes, wobble-prone geometry, and the need for better trail figures or dampers to stay upright at triple-digit speeds.【F:data/vesc_help_group/text_slices/input_part008.txt†L3106-L3158】
- PuneDir and others described personal tank-slapper experiences (78 km/h on a Zero) to stress how quickly oscillations escalate, especially with lighter riders or poor tires.【F:data/vesc_help_group/text_slices/input_part008.txt†L3173-L3183】
- NetworkDir shared that traction control around 80 000 ERPM differential preserves CST 10×3 tires, whereas disabling TC shreds them within days—framing TC as both a safety and tire-wear mitigation tool.【F:data/vesc_help_group/text_slices/input_part008.txt†L3589-L3602】
- Kirill countered the doom posts by listing production scooters with inherently stable geometry (Segway GT1/GT2, ST1/ST2, Inmotion RS, large Wepeds, Monorim-modded G30s, NAMI Blast), clarifying that C-fork wobble is model-specific rather than inevitable.【F:data/vesc_help_group/text_slices/input_part008.txt†L3120-L3126】

### High-Power Controller & Motor Experiments
- Hurriicane showcased a Pro 2 motor rewound for thicker conductors that can gulp 24 kW at 60 V without overheating, paired with 3Schul V4 controllers driving Lonnyo 70H speed hubs for tunnel-speed testing at 71 V.【F:data/vesc_help_group/text_slices/input_part008.txt†L2991-L3015】
- Riders eyeing AliExpress QS268-class 90H hubs debated whether 400 A phase specs translate to 30 kW in practice, with veterans warning that controller limits and rim sizing cap real output despite marketing claims.【F:data/vesc_help_group/text_slices/input_part008.txt†L3019-L3024】
- Field reports from Begode K-series owners note Spintend 85/250 controllers can tow fellow EUCs ~8 miles without thermal drama, reinforcing the platform’s durability when cooled properly.【F:data/vesc_help_group/text_slices/input_part008.txt†L3663-L3666】

### Build Planning & Budget Discipline
- Veterans encouraged riders facing supply or budget crunches to stretch project timelines instead of compromising on core components, sharing examples of slow builds that avoided regrets and advising against rushing purchases just to stay on schedule.【F:data/vesc_help_group/text_slices/input_part008.txt†L4117-L4137】

### Mini-Bike & Fiido L3 Conversions
- Fiido L3 tear-downs showed the stock controller floating loose without a heatsink and limited to roughly 25 A, so jumping straight to 20s test packs without pre-charging the controller capacitors can pop the factory BMS; builders recommend matching voltages before connecting higher-voltage VESC hardware.【F:data/vesc_help_group/text_slices/input_part008.txt†L5858-L5875】
- After dialing battery current back to ~20 A and traction control to 20/20 A, a 60 A phase cap with +FW delivered 45 km/h and repeatable wheelies while keeping the hub cool, underscoring the importance of conservative current ramps on compact minibikes.【F:data/vesc_help_group/text_slices/input_part008.txt†L5915-L5922】
- The disassembly confirmed Fiido’s packs are heavily sealed—cells were locked under glued busbars and soldered fasteners, and a tripped protection board left entire parallel groups at 0 V—so refurb attempts require full BMS removal rather than quick cap swaps.【F:data/vesc_help_group/text_slices/input_part008.txt†L6009-L6016】【F:data/vesc_help_group/text_slices/input_part008.txt†L6443-L6449】

### Controller & Harness Diagnostics
- PuneDir recovered a “0 V CAN bus” fault on a surviving Makerbase 84100 by tracing a shorted CAN_H/L pair and confirmed the transceiver IC was intact, pointing to wiring damage from earlier MOSFET failures rather than silicon loss.【F:data/vesc_help_group/text_slices/input_part008.txt†L5882-L5903】
- Cengiz documented how to integrate an ignition/key switch with the Makerbase regulator: pull the EN pin to ground through 10 kΩ, then lift it with a 10 kΩ/100 kΩ divider instead of battery voltage when the switch closes, which protects the linear stage from over-voltage.【F:data/vesc_help_group/text_slices/input_part008.txt†L6460-L6464】

### Dual Controller & Dashboard Troubleshooting
- Lisa’s dual 75100 setup sounded rough even after disabling phase filters, and the 1Zuna CAN dashboard stopped reporting speed, suggesting further motor detection and CAN scaling checks are needed on 6.05 firmware before trusting road data.【F:data/vesc_help_group/text_slices/input_part008.txt†L6023-L6030】
- A second report from the same rider noted that the dual-ADC script let the rear motor run past 20 km/h limits while the front obeyed settings, implying the dual-controller Lisp needs explicit speed caps on both CAN nodes when repurposed for Ninebot G30 conversions.【F:data/vesc_help_group/text_slices/input_part008.txt†L6244-L6248】

### Battery Fabrication & Adhesives
- Builders leaning on 3M marine adhesive to bond parallel groups warned it cures rock-solid—expect mechanical removal or fresh holders instead of assuming it will peel free during rework—and even minor pack notches demand sub-millimetre tolerances once glue is applied.【F:data/vesc_help_group/text_slices/input_part008.txt†L6076-L6089】
- Salvaged military packs revealed soldered busbars and even fasteners, reinforcing that salvagers should budget time for full desoldering or dremel work rather than assuming bolts will back out cleanly.【F:data/vesc_help_group/text_slices/input_part008.txt†L6443-L6449】

### High-Capacity G30 Experiments
- Ambitious plans for internal 20s12p P42A stacks prompted reminders that a G30 deck typically fits ~120 cells; exceeding that demands stacked modules, tall spacers, remote ESC mounting, and acceptance of 65–70 kg curb weights plus suspension geometry changes.【F:data/vesc_help_group/text_slices/input_part008.txt†L7087-L7133】
- Veterans recommended mocking the pack volume in cardboard or prints before buying cells and highlighted that heavier builds will likely require laser-cut forks or spacer systems similar to French race G30s to clear 11" tyres.【F:data/vesc_help_group/text_slices/input_part008.txt†L6550-L6561】【F:data/vesc_help_group/text_slices/input_part008.txt†L7087-L7137】

### Tire Selection & Race vs. Street Usage
- Track-focused riders praised Xuancheng slicks for turn-in but conceded the thin carcass feels like a “0.005 condom” on rough urban pavement, while CST-patterned 11" options retain cornering confidence with more puncture resistance for daily use.【F:data/vesc_help_group/text_slices/input_part008.txt†L6900-L6917】
- NetworkDir’s testing suggested 3.5" rubber rarely seats cleanly on Zero/Vsett rims without looking tractor-wide, so experimenting with pressure and rim width is essential before chasing 70 km/h corner grip claims.【F:data/vesc_help_group/text_slices/input_part008.txt†L6908-L6913】

### Copper Protection & Busbar Coatings
- Battery builders debated nickel versus copper busbars: copper cuts voltage sag even on capacity cells but corrodes fast, so several plan to nickel-plate copper straps at home or try zinc-rich sprays to stave off electrocorrosion without sacrificing conductivity.【F:data/vesc_help_group/text_slices/input_part008.txt†L6920-L6959】

### Cell Sourcing & Storage Notes
- Recent bulk buys netted unused Molicel P42A stock for about $1.80 per cell delivered, with veterans suggesting 30 % state-of-charge storage in refrigeration to stretch shelf life until the packs are built.【F:data/vesc_help_group/text_slices/input_part008.txt†L6474-L6475】【F:data/vesc_help_group/text_slices/input_part008.txt†L6651-L6658】

### Controller Support & Firmware Availability
- 22s builders warned that Makerbase Ubox 85/250s regularly fail even without regen at that voltage, while the C350 platform has run full race weekends on 22s provided regen is disabled and the CL350 is avoided for heat reasons; several racers offered discount help but stressed proper wiring before blaming the hardware.【F:data/vesc_help_group/text_slices/input_part008.txt†L7189-L7213】【F:data/vesc_help_group/text_slices/input_part008.txt†L7208-L7213】
- 3Shul owners struggling to locate firmware were pointed to an official Drive share that contains the CL350 V3 sources so they can compile a 6.2-capable build, even though the vendor site does not advertise the files.【F:data/vesc_help_group/text_slices/input_part008.txt†L7300-L7309】

### Tronic 250 CAN-Bus Failures
- Five freshly purchased Tronic 250 units arrived with dead CAN rails; the stop-gap was to run identical throttle signals into both controllers but isolate the 3.3 V rails (only ground the second controller) to avoid burning the accelerator until replacement CAN hardware arrives, highlighting slow warranty loops.【F:data/vesc_help_group/text_slices/input_part008.txt†L7233-L7240】【F:data/vesc_help_group/text_slices/input_part008.txt†L7565-L7588】

### Motor Selection for High-Power Builds
- French builders are shoehorning dual 80H hubs and individual 20s4p packs into custom CNC G30 frames, but race teams cautioned that pairing 80H motors with such small batteries is inefficient; they favor 70H rears with lighter fronts on 20s packs and note that well-tuned 70H setups have beaten 80H machines in both circuit and drag events.【F:data/vesc_help_group/text_slices/input_part008.txt†L7381-L7398】【F:data/vesc_help_group/text_slices/input_part008.txt†L7533-L7556】

### Temperature Monitoring Tips
- For motor temperature sensing, riders recommended inexpensive MF52B/MF52D 10 kΩ B3950 NTC probes wired between hall ground and the thermistor input, noting polarity is irrelevant and the parts behave reliably with VESC hardware.【F:data/vesc_help_group/text_slices/input_part008.txt†L7445-L7461】

### Ubox Gate-Driver Diode Failures
- A dual Ubox 100/100 owner traced failed motor detection to a cracked A6 diode feeding the EG3112 gate driver; community advice was to bridge the open pad temporarily or replace the diode outright because the part only filters noise on the 12 V rail.【F:data/vesc_help_group/text_slices/input_part008.txt†L7778-L7795】【F:data/vesc_help_group/text_slices/input_part008.txt†L7813-L7822】

### High-Voltage Battery Ambitions
- Rosheee is pushing a 20s6p G30 past 130 km/h and planning a 26s8p (≈32 Ah, 560–700 A) pack for the GT2, noting overcurrent faults around 320 A on the rear controller and the likely need for external parallel modules to reach 9p while keeping the frame sleeper-clean.【F:data/vesc_help_group/text_slices/input_part008.txt†L7440-L7441】【F:data/vesc_help_group/text_slices/input_part008.txt†L8153-L8164】【F:data/vesc_help_group/text_slices/input_part008.txt†L8175-L8183】

### International Cell Pricing Leads
- ElectricPowa offered bulk Samsung 50E and P42A lots out of Spain for €3.20 and €2.90 respectively, will ship to the United States, and cautioned that logistics may erase the bargain for overseas buyers.【F:data/vesc_help_group/text_slices/input_part008.txt†L7720-L7729】

## Follow-ups
- Capture any firmware or configuration fixes shared for the Spintend Spinny V2 “full brake on release” fault once a root cause is identified.【F:data/vesc_help_group/text_slices/input_part008.txt†L902-L908】
- Track whether the MKSESC 84/200 HP failures receive a definitive manufacturer patch or hardware revision to prevent BMS-cut damage.【F:data/vesc_help_group/text_slices/input_part008.txt†L688-L705】
- Gather detailed wiring photos/layouts for the showcased Zero 10X and Blade motor builds to document successful high-density pack routing.【F:data/vesc_help_group/text_slices/input_part008.txt†L168-L200】【F:data/vesc_help_group/text_slices/input_part008.txt†L1040-L1053】
- Document best practices for Makerbase 84xxx repairs (trace reinforcement, shunt mods, gate driver parts) if the community converges on a reliable rework recipe.【F:data/vesc_help_group/text_slices/input_part008.txt†L1550-L1592】
- Capture a vetted BMS wiring checklist or diagram that reflects the group’s lessons learned about sequence-sensitive balance lead installation.【F:data/vesc_help_group/text_slices/input_part008.txt†L1980-L2059】
- Revisit Mihail’s LVGL dashboard once the CAN profile management is live and reusable firmware or hardware BOMs are published.【F:data/vesc_help_group/text_slices/input_part008.txt†L2501-L2587】
- Monitor outcomes from the Vsett/Titaone high-speed builds for concrete geometry fixes (trail adjustments, dampers, tire choices) that tame wobble at >80 km/h.【F:data/vesc_help_group/text_slices/input_part008.txt†L3106-L3183】【F:data/vesc_help_group/text_slices/input_part008.txt†L3033-L3056】
- Follow up on MP2 ABS overcurrent troubleshooting once firmware fixes or configuration guides emerge for 200 A+ setups.【F:data/vesc_help_group/text_slices/input_part008.txt†L4913-L4920】【F:data/vesc_help_group/text_slices/input_part008.txt†L5250-L5258】
- Capture PuneRon’s finalized water-cooling layout and sprocket machining notes once the steel gear set is tested above 200 A.【F:data/vesc_help_group/text_slices/input_part008.txt†L4791-L4858】【F:data/vesc_help_group/text_slices/input_part008.txt†L5387-L5403】
- Log proven resistor values or harness diagrams for reusing Xiaomi Pro 2 lighting with dual VESC conversions so future builders avoid LED failures.【F:data/vesc_help_group/text_slices/input_part008.txt†L5032-L5045】
- Document safe bring-up procedures for Fiido L3 packs when pairing them with higher-voltage VESC controllers so the BMS isn’t shocked by charged input caps.【F:data/vesc_help_group/text_slices/input_part008.txt†L5858-L5875】
- Track fixes or configuration advice for 1Zuna’s dual-controller dash scripts so both motors respect speed caps on Ninebot builds.【F:data/vesc_help_group/text_slices/input_part008.txt†L6023-L6030】【F:data/vesc_help_group/text_slices/input_part008.txt†L6244-L6248】
- Capture detailed wiring diagrams for Makerbase ignition/EN pin mods (including resistor divider values) to simplify future regulator integrations.【F:data/vesc_help_group/text_slices/input_part008.txt†L6460-L6464】
- Verify practical G30 deck layouts beyond ~120 internal cells and note any spacer/fork patterns that successfully house 20s≥10p modules without compromising handling.【F:data/vesc_help_group/text_slices/input_part008.txt†L6550-L6561】【F:data/vesc_help_group/text_slices/input_part008.txt†L7087-L7137】
- Summarize reliable paths for sourcing/compiling 3Shul firmware (including the shared Drive repo) and collect field data on which 3Shul/C350 variants hold up at 22s with and without regen.【F:data/vesc_help_group/text_slices/input_part008.txt†L7189-L7213】【F:data/vesc_help_group/text_slices/input_part008.txt†L7300-L7309】
- Document a repeatable repair guide for Tronic 250 CAN-bus failures, including replacement transceivers and safe throttle sharing practices while parts are on order.【F:data/vesc_help_group/text_slices/input_part008.txt†L7565-L7588】
- Capture a wiring note for low-cost MF52B/MF52D thermistors (pinouts, potting, routing) so builders can confidently add motor temperature sensing.【F:data/vesc_help_group/text_slices/input_part008.txt†L7445-L7461】
- Record EG3112 gate-driver supply fixes for Ubox 100/100 controllers—bridging versus diode replacement—and confirm long-term reliability once repairs are tested.【F:data/vesc_help_group/text_slices/input_part008.txt†L7778-L7795】【F:data/vesc_help_group/text_slices/input_part008.txt†L7813-L7822】
- Track Rosheee’s forthcoming GT2 26s8p testing for overcurrent fixes, cooling upgrades, and any structural changes needed to house external parallel modules cleanly.【F:data/vesc_help_group/text_slices/input_part008.txt†L8153-L8164】【F:data/vesc_help_group/text_slices/input_part008.txt†L8175-L8183】
