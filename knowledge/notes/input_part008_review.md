# input_part008.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part008.txt`, continuing into `data/vesc_help_group/text_slices/input_part009.txt` (lines 1-4,500)
- Coverage: 2024-04-15T15:15 through 2024-08-15T00:34 (lines 1-23,260 in part008 plus the first 4,500 lines of part009)
- Next starting point: Resume at 2024-08-15T00:35 (input_part009 line ~4,501).

## Key Findings

### Battery Architecture & Materials
- Builders debating 20s20p packs concluded that pure nickel can work when individual cells are limited to ~5 A; copper only becomes necessary if the layout cannot provide enough parallel cross-section, reinforcing the need to compute current paths rather than relying on cell count alone.【F:data/vesc_help_group/text_slices/input_part008.txt†L14-L38】
- PuneDir pairs large packs with 200 A ANT/JK BMS options and has even used a 100 A JK on a 70 A-rated battery, showing the community tendency to oversize BMS hardware for reliability headroom.【F:data/vesc_help_group/text_slices/input_part008.txt†L14-L21】
- Complex holderless layouts fit 20s7p (21700) batteries plus dual controllers in a Zero 10X only by adding a 45 mm deck extender and meticulous insulation—evidence that internal 20s packs demand custom machining or spacers.【F:data/vesc_help_group/text_slices/input_part008.txt†L168-L200】
- Copper-enhanced busbars (e.g., Wellgo nickel-copper laminate) run about $150 shipped for a 20s10p pack when sourced via Alibaba; builders solder copper wire onto welded nickel after the fact to lower resistance without heating cells directly.【F:data/vesc_help_group/text_slices/input_part008.txt†L742-L767】
- High-current moto projects are wiring three BMS units in parallel so enormous 20s24p packs can share hundreds of amps safely, a reminder that protection hardware often scales alongside the cell count.【F:data/vesc_help_group/text_slices/input_part008.txt†L13914-L13920】
- Patrick’s recent discharge testing puts Eve 40PL prismatic cells ahead of Molicel P45B/P50B for 100 A bursts—the 40PL held 3.0 V for 62 s while the P45B drooped to 2.78 V after 44 s—informing cell choices for 20 kW+ scooters.【F:data/vesc_help_group/text_slices/input_part008.txt†L14330-L14331】
- Copper strip sourcing is becoming volatile—AliExpress rolls of 0.1 × 200 × 5,000 mm laminate jumped from ~€15 to €45 within weeks—so some builders are shelving copper-heavy busbars and reverting to nickel layouts unless they can justify the premium.【F:data/vesc_help_group/text_slices/input_part008.txt†L16198-L16204】

### Wiring & Phase Leads
- Heavy scooters such as QS273 builds are jumping from melted stock leads to 7 AWG or thicker phase wire, while others confirm 10 AWG is the practical minimum for 60H/70H-class motors when space allows.【F:data/vesc_help_group/text_slices/input_part008.txt†L7-L14】【F:data/vesc_help_group/text_slices/input_part008.txt†L1095-L1101】
- Community members warn that simply soldering bulk material onto cell ends is a poor conductor upgrade—reinforce strips with copper wire instead of puddling solder on the cell cans.【F:data/vesc_help_group/text_slices/input_part008.txt†L759-L767】
- Makerbase 75xxx riders chasing low-speed bogs found the culprit was often phase bullets that weren’t fully seated—checking continuity end-to-end and reseating the copper strands in each plug cleared the “won’t accelerate without FW” behavior before digging into firmware.【F:data/vesc_help_group/text_slices/input_part008.txt†L16468-L16506】

### Thermal Management & Heatsinking
- Spintend controllers are viewed as dissipating roughly half the heat of comparable Tronic units, yet even higher-end ESCs like the 84100 still run hot when pushed to ~180 A, underscoring the need for large external heatsinks and fresh thermal paste.【F:data/vesc_help_group/text_slices/input_part008.txt†L133-L165】
- Riders report Nucular 12-FET controllers handling 210 A at 48 °C when simply clamped to deck aluminum, showing the payoff of robust MOSFET packages and good contact pressure.【F:data/vesc_help_group/text_slices/input_part008.txt†L160-L166】
- Routine desktop maintenance advice (reapplying thermal paste every ~2 years, cleaning heatsinks) is being applied to ESC care, reinforcing the parallel between PC cooling and VESC thermal upkeep.【F:data/vesc_help_group/text_slices/input_part008.txt†L166-L173】
- Single-drive NAMI builds on steep climbs still push a lone Tronic 250 to ~60 °C, while dual-drive riders on similar hardware stay below 40 °C, highlighting how load sharing and solid thermal mounting change real-world temperature ceilings.【F:data/vesc_help_group/text_slices/input_part008.txt†L4871-L4886】
- Community mounting notes for Spintend’s aluminum 6-FET units call for sandwiching the controller against a 3–5 mm aluminum plate with thermal paste on both interfaces; copper plates are discouraged because galvanic corrosion outweighs any marginal conductivity gain once the ESC is already bonded to aluminum.【F:data/vesc_help_group/text_slices/input_part008.txt†L10241-L10253】

### Controller Reliability & Power Interrupts
- Multiple builders note that MKSESC 84/200 HP units can blow MOSFETs whenever a BMS trips under load, whereas Spintend Ubox and 3Shul hardware tend to survive; mitigation includes avoiding BMS-triggered cutoffs, running lower currents, or paralleling packs.【F:data/vesc_help_group/text_slices/input_part008.txt†L688-L705】
- CL350-class controllers appear more tolerant of brief supply interruptions, especially when supplemented with additional 12 V capacitance, hinting at design differences in input filtering.【F:data/vesc_help_group/text_slices/input_part008.txt†L700-L704】
- Riders weighing alternatives now call the Ubox 85/150 a safer bet than Makerbase 84/200 HP hardware, citing the latter’s persistent issues despite lower pricing.【F:data/vesc_help_group/text_slices/input_part008.txt†L10669-L10671】
- Field reports confirm that Spintend controllers simply coast when pack BMSes trip, unlike Makerbase 72500 units that can lock the wheel and back-drive regen into already stressed MOSFETs.【F:data/vesc_help_group/text_slices/input_part008.txt†L10608-L10622】
- PuneDir’s repaired 75100 failing days after a resin potting job underscores that flooding aluminum PCBs with encapsulant can trap heat or complicate future fixes; his unit ran 3 000 km before being loaned out and destroyed soon after.【F:data/vesc_help_group/text_slices/input_part008.txt†L11370-L11380】
- Rosheee’s teardown of a CL350 board revealed rough aluminum-PCB soldering and rework-quality concerns, reinforcing the need to inspect high-end ESCs before installation or ship them to trusted repairers.【F:data/vesc_help_group/text_slices/input_part008.txt†L11592-L11618】【F:data/vesc_help_group/text_slices/input_part008.txt†L11623-L11635】
- Ubox V2 owners who snap the ignite JST off the PCB are hand-soldering replacements sourced from LCSC; the nearby slow-blow fuse feeding that header measures roughly 125 V/≤1 A (Littelfuse footprint), so matching it avoids boot issues after the repair.【F:data/vesc_help_group/text_slices/input_part008.txt†L16377-L16405】
- Intermittent ABS overcurrent faults have been traced to loose hall looms—if shaking the harness breaks detection, the cable needs strain relief or re-termination before hunting for firmware bugs.【F:data/vesc_help_group/text_slices/input_part008.txt†L16552-L16556】
- Moisture intrusion can spoof Ubox FET-temperature telemetry: one rider saw readings jump to 190 °C at full throttle until the enclosure was warmed up and cleaned with alcohol, after which the sensor tracked normally again.【F:data/vesc_help_group/text_slices/input_part008.txt†L17122-L17236】
- Makerbase 75200 riders hitting 20 km/h ceilings ultimately found Lisp dash scripts or aggressive 70 A field-weakening limits clamping ERPM; reinstalling the script, lowering FW, and rechecking duty/ERPM caps restored full speed without changing hardware.【F:data/vesc_help_group/text_slices/input_part008.txt†L17505-L17558】
- Face de Pin Sucé reported a race scooter that lost its 3Shul powerboard (NTC failure) was restored with a replacement module, noting the latest production looks cleaner—evidence the platform is serviceable but still prone to sensor-board deaths.【F:data/vesc_help_group/text_slices/input_part008.txt†L11824-L11828】
- Benur Lgl’s Ubox/3Shul combo misread a Lonnyo 70H’s temperature until he verified the probe, prompting reminders to confirm the exact NTC part before blaming firmware when 10 k probes show nonsense data.【F:data/vesc_help_group/text_slices/input_part008.txt†L11784-L11788】
- Yoann’s dual Spintend build lost hall detection on one side even after swapping controllers, pointing to damaged hall sensors or cabling and reinforcing sensor checks before escalating to ESC RMAs.【F:data/vesc_help_group/text_slices/input_part008.txt†L12462-L12471】
- Crimeware nearly lost a Makerbase 75100 to static electricity until a sheet of Kapton isolated the logic section, underscoring how vulnerable the platform is without added dielectric barriers.【F:data/vesc_help_group/text_slices/input_part008.txt†L13167-L13174】
- Fresh Makerbase 84100 HP samples arrive with isolated hardware, copper shunts, glued logic stacks, and 8 AWG pigtails, yet riders remain cautious because the phase-sampling layout leaves little thermal or packaging margin up front.【F:data/vesc_help_group/text_slices/input_part008.txt†L13381-L13383】
- New Ubox 85/150 units ship with warranty firmware capped near 130 A phase/180 A absolute until owners flash the 100/250 profile, so expect to unlock them before serious tuning.【F:data/vesc_help_group/text_slices/input_part008.txt†L13486-L13490】

### Motor Maintenance & Cleaning
- For contaminated Bafang BBSHD mid-drives, the recommended workflow is compressed air first, followed by brake cleaner or alcohol applied sparingly with lint-free cloths; avoid microfiber wipes that shed fibers, and be cautious around PCB adhesives and magnet glue.【F:data/vesc_help_group/text_slices/input_part008.txt†L977-L1015】
- Brake cleaner residue evaporates quickly, but builders still plan to dry stators with compressed air and ensure windings aren’t left soaked to protect insulation.【F:data/vesc_help_group/text_slices/input_part008.txt†L1003-L1014】

### Maintenance Fixes & Fabrication Tricks
- JPPL’s fix for ovalized folding-clamp bushings involves shimming the pins with thin metal (even tuna-can strips) or heat-shrink sleeves and securing every clamp screw with Loctite so the top plate stops wallowing out again.【F:data/vesc_help_group/text_slices/input_part008.txt†L12589-L12611】
- When sourcing 3D printers for scooter fixtures, veterans steered newcomers away from Ender 3 V3 SE wobble issues and toward discounted Bambu Lab A1/A1 Mini units that print reliably out of the box for tooling jobs.【F:data/vesc_help_group/text_slices/input_part008.txt†L11910-L11957】
- PuneDir’s free steering damper only behaved after swapping engine oil for lighter hydraulic fluids—veterans recommended 10W/60 shock oil or Citroën LHM+ to keep seals intact while restoring adjustability.【F:data/vesc_help_group/text_slices/input_part008.txt†L13738-L13748】

### Fitment & Drivetrain Notes
- Discussions confirm that VSETT 11+ frames can physically accommodate up to ~90H rear motors (≈170 mm dropout) but remain limited by narrower front dropouts (~145 mm), constraining mixed 70H/90H upgrades without machining.【F:data/vesc_help_group/text_slices/input_part008.txt†L1162-L1178】
- Stock VSETT throttles and controllers demand significant rewiring for smooth behavior; riders replacing Kelly and YYK square-wave units note drastic improvements in control feel with modern FOC setups despite added configuration effort.【F:data/vesc_help_group/text_slices/input_part008.txt†L606-L646】【F:data/vesc_help_group/text_slices/input_part008.txt†L1124-L1144】

### Suspension, Frames & Big-Chassis Options
- Dualtron Thunder owners swapping to NAMI chassis praise hydraulic dampers for comfort while crediting elastomer suspension blocks with high-speed stability, framing the choice as comfort vs. control when upgrading legacy frames.【F:data/vesc_help_group/text_slices/input_part008.txt†L1224-L1233】
- Janobike X11/X20 shells have been stretched to host 23s10p–24s packs plus Kelly controllers, with PMT T41 11" slicks and 75H hub motors fitting once the deck is widened—evidence that large-capacity conversions demand both enclosure machining and tire clearance planning.【F:data/vesc_help_group/text_slices/input_part008.txt†L1255-L1288】
- Builders eyeing QS138 motorcycle conversions expect ~30–40 kW potential but are reminded that controller and battery limits (≥300 A phase, quality cells) dictate achievable torque; cheap LG M26 cells sag badly compared with P45B/P42A-class packs.【F:data/vesc_help_group/text_slices/input_part008.txt†L2084-L2223】【F:data/vesc_help_group/text_slices/input_part008.txt†L2379-L2416】
- Jan reiterated that violent wobbles stem from poor steering geometry: his G30 builds only stayed planted past 130 km/h after Speedfork geometry changes, whereas stock and C-suspension frames still shake despite dampers.【F:data/vesc_help_group/text_slices/input_part008.txt†L14142-L14179】

### Motor Selection Updates
- Face de Pin Sucé reiterated that 70H hubs favor higher kv while 75H adds torque, and 80H demands at least 22S packs for race use—guidance that helps teams choose between top speed and punch when widening arms for bigger motors.【F:data/vesc_help_group/text_slices/input_part008.txt†L12385-L12418】
- Klima owners planning 72 V conversions confirmed the chassis ships with 10×3.5" hubs, may rub at 11", and could house Spintend 85/150s in the stock controller bay; they’re scouting higher-torque 10" drop-ins and temperature-sensor upgrades before pushing wheelies on Bay Area hills.【F:data/vesc_help_group/text_slices/input_part008.txt†L12510-L12537】
- Power-chasing G30 builders agreed that a compact 20s6p pack made from high-discharge cells already supports ~35 kW once cabling is uprated, making double-decker 12p stacks unnecessary unless you can manage the extra heat and routing complexity.【F:data/vesc_help_group/text_slices/input_part008.txt†L14190-L14215】

### Traction Control & Tire Selection
- Traction control helps rein in front-wheel slip up to ~55 mph, but riders also cut front phase amps to keep dual-drive builds manageable.【F:data/vesc_help_group/text_slices/input_part008.txt†L1425-L1431】
- Xuancheng 12" slicks are deemed budget-friendly yet inadequate for high-power launches; peers steer riders toward CST or PMT rubber, while 11x3.5" alternatives broaden the contact patch for scooters that can fit them.【F:data/vesc_help_group/text_slices/input_part008.txt†L1434-L1451】
- Rural riders rotating between slicks and Xuancheng Stradale tires note the latter’s durability on gravel access roads, reserving PMTs for track use.【F:data/vesc_help_group/text_slices/input_part008.txt†L2318-L2320】
- NetworkDir is chasing wider 10" tires after discovering that CST 10×3 rubber wobbles violently from 0–40 km/h if traction control is disabled, underscoring how tire profile interacts with electronic aids at launch.【F:data/vesc_help_group/text_slices/input_part008.txt†L4103-L4109】
- Zero 10X and Mantis riders swapping CST 90/65-6s for Tuovt 90/55-6 rubber report noticeably better grip and acceleration on true 6" rims, warning that oversized 6.5" casings pinch split rims and look sloppy; Tuovt 13s remain sketchy in the wet.【F:data/vesc_help_group/text_slices/input_part008.txt†L13397-L13435】
- Vsett 9 owners fighting pinch flats are doubling heavy-duty Ulip tubes, dusting them with baby powder during install, and eyeing 3D-printed bead covers to protect the tube crease on split rims.【F:data/vesc_help_group/text_slices/input_part008.txt†L14628-L14637】【F:data/vesc_help_group/text_slices/input_part008.txt†L14633-L14641】

### Early August Updates (input_part009 lines 1-1,500)

#### Accessory Wiring & Dash Integration
- Smart Repair confirmed the Spintend ADC adapter can share a single lamp by diode-isolating the “reverse” output and paralleling the final feed with the headlight circuit after noting that the brake channel sources battery-positive while the headlight pin provides the return path.【F:data/vesc_help_group/text_slices/input_part009.txt†L46-L95】
- 🇪🇸AYO#74 cautioned that tapping the auxiliary port beside the CAN header leaves lights powered until the controller is switched off, so builders should add a latching switch or take power from the dashboard harness instead.【F:data/vesc_help_group/text_slices/input_part009.txt†L74-L77】
- Once the light wiring was stable, Smart Repair ran the Spintend ADC bridge on ADC1/2 while keeping the M365 dash on the UART header, showing the dash and lighting adapter can coexist without CAN injection.【F:data/vesc_help_group/text_slices/input_part009.txt†L257-L301】

#### Race Prep & Motor Cooling
- Давно пора logged that his single-motor Inokim overheated during daytime heats and only stayed on pace at night by icing the hub between sessions; he plans to switch to PMT slicks but still lacks ideal rubber for the R6 rim, underlining the need for better tire and cooling support on 19 S race setups.【F:data/vesc_help_group/text_slices/input_part009.txt†L60-L68】

#### Battery Building & Quality Control
- PuneDir is mixing grey and purple LG M26 wraps after matching internal resistance across every 10-cell group, reinforcing that color variants can be combined when IR is verified.【F:data/vesc_help_group/text_slices/input_part009.txt†L32-L35】
- Patrick and Tristan documented a €270 resale pack with unsecured nickel, missing insulation, and a seller who refused refunds—evidence that community members still encounter dangerous “pro” batteries and should demand build photos before paying.【F:data/vesc_help_group/text_slices/input_part009.txt†L260-L370】
- PuneDir stripped his earlier welds and restarted the build because reused cells were no longer taking welds reliably, stressing that it’s safer to rebuild from bare cans than trust compromised nickel.【F:data/vesc_help_group/text_slices/input_part009.txt†L1022-L1027】
- The same pack uses double steel strip plus nickel to carry roughly 7–8 A per cell across a 17 p M26 block, illustrating the current limits when steel is part of the stack.【F:data/vesc_help_group/text_slices/input_part009.txt†L1044-L1062】
- Patrick’s new 20 s layout seats a silicone-bonded thermistor, ASA‑CF printed holders, and a triangular bus pattern so both leads exit the same side—an approach that trades filament cost and heated-chamber printing for a more rigid internal pack.【F:data/vesc_help_group/text_slices/input_part009.txt†L1031-L1041】

#### Pack Logistics & Charging
- Noname runs three differently sized packs on separate BMS boards and notes they usually balance each other, but if one BMS trips under heavy load the remaining packs see a sudden surge that can kill them—highlighting why parallel packs still need coordinated protections.【F:data/vesc_help_group/text_slices/input_part009.txt†L472-L475】
- Yamal ordered a 20 A adjustable charger for upcoming long rides, giving builders another high-current option to vet for road trips.【F:data/vesc_help_group/text_slices/input_part009.txt†L963-L965】

#### Controller & Firmware Tuning
- NetworkDir advised Flipsky 75200 users to disable the built-in phase filter, rerun detection with the Mxlemming observer, and cap phase/motor/battery currents at roughly 120 A/120 A/50–60 A (−5 A regen) to stop idle heating on 20 mΩ hubs.【F:data/vesc_help_group/text_slices/input_part009.txt†L768-L795】
- For 17 S commuter builds he suggested braking budgets around −40 A phase and −5 A battery to stay within JBD 100 A BMS limits.【F:data/vesc_help_group/text_slices/input_part009.txt†L994-L1018】
- Jason reminded testers to disable regen when powering controllers from a bench PSU—back-EMF from field weakening had previously destroyed his supply when regen stayed active.【F:data/vesc_help_group/text_slices/input_part009.txt†L1130-L1135】

#### Projects & Fitment Notes
- PuneDir’s Hyosung “Puneron” build now spins a 72 T/9 T sprocket set, giving a reference ratio for other large-wheel conversions chasing dirt-bike torque.【F:data/vesc_help_group/text_slices/input_part009.txt†L189-L191】
- GABE demonstrated that a Xiaomi Pro 2 can swallow a 13 s8 p, 104-cell pack (≈1.15 kWh) plus side-mounted BMS modules when the ESC is moved, illustrating the space savings of asymmetrical stacking.【F:data/vesc_help_group/text_slices/input_part009.txt†L1067-L1086】

### Early August Updates (input_part009 lines 1,501-3,000)

#### Controller & Power Electronics Debates
- Riders debating the Spintend 85/150 reminded that it only ships with 100 V-rated components and has mostly been validated on 20 S packs; Paolo lost one at 20 S when stacking a high-kV hub with MTPA and field-weakening, reinforcing the need to respect voltage spikes near its ceiling.【F:data/vesc_help_group/text_slices/input_part009.txt†L1522-L1539】
- Paolo cautioned that several boutique Chinese MOSFETs ship with “too good to be true” specs—JJMicro parts in particular measured wildly off their datasheets—so he now trusts Huayi-sourced FETs for high-power ESC builds.【F:data/vesc_help_group/text_slices/input_part009.txt†L1541-L1554】
- Jan’s 35 kW-on-10" debate concluded that such peaks are only realistic with water-cooled 45 kV hubs, low switching frequency, and premium cells like P50B/40PL; even then traction becomes the limiting factor on small-contact-patch tires.【F:data/vesc_help_group/text_slices/input_part009.txt†L1574-L1606】
- Raphaël and Paolo agreed that Spintend’s stock MOSFETs lag behind alternatives—calling the new light model’s 2 mΩ devices “worse” than baseline HY parts—so racers eye drop-in swaps when chasing higher sustained current.【F:data/vesc_help_group/text_slices/input_part009.txt†L2491-L2499】

#### Sensorless & Configuration Tips
- Mirono confirmed that sensorless VESC setups remain viable in FOC mode as long as riders give the wheel a push to seed detection; HFI experimentation can remove the push-start, but most still prefer a rolling launch.【F:data/vesc_help_group/text_slices/input_part009.txt†L1713-L1720】

### Mid-August Updates (input_part009 lines 3,001-4,500)

#### Controller Limits & Failures
- PuneDir pressed the Makerbase 84100 HP for 120 A battery but veterans capped it near 60–80 A battery and ~135 A phase after watching one burn at 160 A, pushing him toward 85/250-class hardware once customs allow imports.【F:data/vesc_help_group/text_slices/input_part009.txt†L3010-L3024】
- Chen Simhony’s Inokim OX motor only detected after selecting the “large outrunner” template, and rosheee later flagged that his CAN bus plus hall/temperature wiring were faulting—evidence that 3Shul installs still need hands-on sensor validation even when firmware loads correctly.【F:data/vesc_help_group/text_slices/input_part009.txt†L3064-L3079】【F:data/vesc_help_group/text_slices/input_part009.txt†L3231-L3242】
- PuneDir’s shunt-modded “€25 ESC” drives a 45 H inrunner past 260–280 A phase but coughs between 25–50 km/h because the square-wave controller is saturating the 1 kW hub; riders advised detuning phase limits or upgrading to a FOC VESC before the traces explode again.【F:data/vesc_help_group/text_slices/input_part009.txt†L3492-L3524】【F:data/vesc_help_group/text_slices/input_part009.txt†L3826-L3833】
- Yamal’s Little FOCer failed after a 37 A field-weakening run at 100 A battery/200 A phase, reinforcing his usual 150 A phase ceiling and motivating a switch to 12‑FET controllers that survive dual-motor duty without FW abuse.【F:data/vesc_help_group/text_slices/input_part009.txt†L3615-L3622】【F:data/vesc_help_group/text_slices/input_part009.txt†L3729-L3733】【F:data/vesc_help_group/text_slices/input_part009.txt†L4370-L4385】
- Builders catalogued more Makerbase/Flipsky detection failures—Hall ERPM flips, bogus inductance numbers, and hard braking events—so Paolo now measures Rs/Ls with external tools before typing values into VESC Tool, warning newcomers not to trust “auto” results.【F:data/vesc_help_group/text_slices/input_part009.txt†L3854-L3867】

#### Battery Cells & BMS Practices
- NetworkDir previewed Molicel’s XA-series race cells (≈2.6 Ah, ~1.5–2 mΩ, 125 A charge/250 A discharge) while noting Eve 40PL still leads the market at ~3 mΩ but suffers low capacity—useful guardrails for riders planning 30 S5 P drag packs.【F:data/vesc_help_group/text_slices/input_part009.txt†L3099-L3124】
- 🇪🇸AYO#74’s 22 S11 P LG M50LT pack supports about 14.5 A per cell, but he’s already planning a like-for-like rebuild with P45B to unlock ~495 A discharge once the current pack ages out.【F:data/vesc_help_group/text_slices/input_part009.txt†L3350-L3355】
- Jason walked newcomers through balance-lead routing: keep the JST plugged in while laying wires, tape the loom to hold curves, and a mispinned lead usually just keeps the BMS off until it’s corrected—practical tips for tidy harnesses.【F:data/vesc_help_group/text_slices/input_part009.txt†L3834-L3848】
- GABE reiterated that ANT BMS looms must always reference the main pack negative first before stepping up cell taps, warning that skipping the ground pin risks frying the board.【F:data/vesc_help_group/text_slices/input_part009.txt†L3375-L3387】

#### Pack Assembly & Tooling Notes
- Cihan hunted for thermally conductive foam to cradle a deck pack, but the group recommended cutting small insulating pads just to stop rattles and leaving air gaps so heat can still escape.【F:data/vesc_help_group/text_slices/input_part009.txt†L3051-L3055】
- PuneDir’s steel battery box missed the Hyosung frame opening by 1 cm, stranding his build and underscoring the value of templating enclosures before welding or ordering heavy shells.【F:data/vesc_help_group/text_slices/input_part009.txt†L3281-L3320】
- Turkey-based builders endorsed the €25 “purple PCB” 12 V spot-welder board when it’s fed by a 72 Ah car battery—it handles 0.2 mm nickel reliably but likely lacks the current to weld 0.15 mm copper, prompting searches for capacitor-based rigs that aren’t blocked by customs.【F:data/vesc_help_group/text_slices/input_part009.txt†L4259-L4274】

#### Charging & Connector Choices
- Talk of 40 C fast charging turned into a reality check: even 20 S6 P packs would need ~11 kW from three-phase mains, far beyond the 10 A household circuits many riders have, so XA3-class cells still demand industrial infrastructure for minutes-long fills.【F:data/vesc_help_group/text_slices/input_part009.txt†L3275-L3296】
- Andrei Albert suggested swapping fragile GX16 charge ports for IP67-rated Cnlinko LP16 connectors, while Yamal countered that XT60s remain adequate for 20 A charging—offering two vetted pathways depending on weather sealing needs.【F:data/vesc_help_group/text_slices/input_part009.txt†L4161-L4169】

#### Supply Chain & Component Access
- Turkish members confirmed the new €30 import ceiling effectively blocks direct orders of scooters, motors, and welders—expect to pay 2–3× local markups or work through licensed importers who can legally clear higher-value shipments.【F:data/vesc_help_group/text_slices/input_part009.txt†L4218-L4237】【F:data/vesc_help_group/text_slices/input_part009.txt†L4241-L4244】
- Even when shipping frames without batteries, Jan warned that airlines flag scooter parts over 100 Wh, so expect slow and costly ground freight for cross-border chassis trades.【F:data/vesc_help_group/text_slices/input_part009.txt†L4348-L4365】

#### Controller Mods & Future Testing
- Yamal noted that Spanish resellers already retrofit Ubox 85/150 units with 100 V MOSFETs (mirroring Raphaël’s lab upgrades), and he wants structured track testing to compare those against Tronic X12 units that hold 400 A+ phase without drama.【F:data/vesc_help_group/text_slices/input_part009.txt†L4431-L4437】【F:data/vesc_help_group/text_slices/input_part009.txt†L4494-L4498】
- Raphaël recounted that Tronic 250Rs still dislike 100 V packs—Tronic even delisted them—so racers are pivoting toward X12 or Seven controllers while salvaging parts from retired NAMI builds for Surron conversions.【F:data/vesc_help_group/text_slices/input_part009.txt†L4433-L4437】【F:data/vesc_help_group/text_slices/input_part009.txt†L4491-L4498】
- When chaining two 10 S packs in series, VESC Tool should still be configured for 20 S so cutoff logic and telemetry match the combined voltage rather than the per-pack rating.【F:data/vesc_help_group/text_slices/input_part009.txt†L2622-L2624】

#### Battery Welding, Safety & Tooling
- Glitter’s 811H spot welder arrived with MOSFET faults for haku, charged only to 5.4 V, and still welds 0.2 mm copper-on-nickel after repairs—evidence that QC can lag behind the advertised 1.8 kA capability.【F:data/vesc_help_group/text_slices/input_part009.txt†L1801-L1808】
- Community testing shows kWeld handles 0.15 mm copper sandwiches at ~75 J but overheats during continuous runs, and it can trip overcurrent faults if builders parallel multiple LiPos or capacitor banks without tuning the firmware limits.【F:data/vesc_help_group/text_slices/input_part009.txt†L1804-L1838】
- Paolo has shifted heavy pack fabrication to TIG welding with pulse controllers, arguing that it avoids spot-welder thermal sag and unlocks thicker bus work at a fraction of the duty cycle he used to run on resistance welders.【F:data/vesc_help_group/text_slices/input_part009.txt†L1844-L1853】
- Builders swapping old nickel off reclaimed cells warned against grinding—one friend ignited a cell instantly after over-sanding—and haku’s photo log shows erratic arc blasts when his Glitter welder misfires on 0.2 mm copper/steel stacks, underscoring the fire risk of unstable welders.【F:data/vesc_help_group/text_slices/input_part009.txt†L1864-L1876】
- Gabe and others reiterated that Glitter’s 801D tops out around 0.1 mm copper while the 801H’s beefier MOSFET array can stretch to 0.2 mm, so copper-heavy builds should budget for the higher-end unit if customs allow it.【F:data/vesc_help_group/text_slices/input_part009.txt†L2428-L2431】【F:data/vesc_help_group/text_slices/input_part009.txt†L2054-L2057】

#### Pack Layout, Insulation & Harnessing
- Patrick found that 10 mm² output leads were too stiff for his new pack and is dropping to dual 6 mm² conductors, while PuneDir’s M26-based 10 p groups are being fully mirrored with extra nickel to keep 80 A targets symmetric rather than reinforcing only the “red” side of the layout.【F:data/vesc_help_group/text_slices/input_part009.txt†L1739-L1759】
- PuneDir is layering plexiglass and fish paper between every series plane before heat-shrinking, then feeding twin packs (20 S10 P and 20 S7 P) through triple XT60 harnesses to hit 150 A bursts—demonstrating how isolation stacks plus redundant connectors tame mixed-chemistry builds.【F:data/vesc_help_group/text_slices/input_part009.txt†L2025-L2035】【F:data/vesc_help_group/text_slices/input_part009.txt†L2325-L2369】
- Patrick’s oversized JBD smart BMS forced him to silicone-isolate outputs and reprint deck spacers, illustrating how datasheet thickness omits screw heads and heatsinks that can blow up packaging plans.【F:data/vesc_help_group/text_slices/input_part009.txt†L2041-L2049】
- Battery builders reiterated that copper will oxidize unless sealed, that nickel-plated steel remains the go-to companion strip for copper sandwiches, and that 8 mm nickel is ample for 18650 positive rings while 0.2 mm copper is overkill unless you truly draw >50 A from 6 P strings.【F:data/vesc_help_group/text_slices/input_part009.txt†L2146-L2149】【F:data/vesc_help_group/text_slices/input_part009.txt†L2609-L2614】
- Haku’s 3D-printed holders plus fishpaper tape layers gave cihan a template for insulating every cell face and perimeter before wrapping the pack—an approach that pairs round terminal gaskets with wide fish tape to keep copper sheets from contacting can walls.【F:data/vesc_help_group/text_slices/input_part009.txt†L2763-L2776】

#### BMS Apps, Monitoring & Shunt Experiments
- Patrick’s run-in with the JBD mobile app highlights two quirks: the interface inherits the phone’s language (producing broken German translations) and it silently enforces a 15 mV minimum balance delta unless you disable “softlock” through the admin app or switch to English.【F:data/vesc_help_group/text_slices/input_part009.txt†L2115-L2137】
- PuneDir’s €25 clone ESC surfaced with a 280 A shunt limit; Paolo walked through measuring the millivolt drop with a bench supply and applying Ohm’s law to retarget ~25 A, noting that standard multimeters can’t resolve the sub-milliohm resistor without a load.【F:data/vesc_help_group/text_slices/input_part009.txt†L2909-L2987】

### Makerbase ESC Failures & Repair Attempts
- A fresh Makerbase 84100 HP locked both motors while coasting, echoing earlier 75100 deaths tied to hall shorts and melted motor leads; the owner now distrusts the platform despite temporary recovery.【F:data/vesc_help_group/text_slices/input_part008.txt†L1463-L1508】
- Post-mortem chat highlights that the 84100 HP senses current via phase shunts rather than resistors, uses the same MOSFET set as older 75100 boards, and may ship with questionable component quality—fueling suspicions about counterfeit silicon.【F:data/vesc_help_group/text_slices/input_part008.txt†L1550-L1569】
- DIY repairs involve swapping MOSFETs and gate drivers harvested from scrap controllers, but ripped traces and repeated failures push riders toward Spintend or 3Shul replacements instead of another Makerbase warranty cycle.【F:data/vesc_help_group/text_slices/input_part008.txt†L1573-L1592】【F:data/vesc_help_group/text_slices/input_part008.txt†L1632-L1639】
- Later chats reiterate that repaired FlipSky/Makerbase 75xxx boards can still brake unexpectedly if upstream logic fails, so builders replace STM MCUs and gate drivers together, watch for wrong auto-detection values (e.g., 450 µH inductance), and sometimes relocate the motor to the rear to minimize crash risk when an ESC seizes.【F:data/vesc_help_group/text_slices/input_part008.txt†L5071-L5088】

### Battery Building & BMS Lessons
- Pack builders warn that piercing a cell or leaving it compromised invites cascading failures; pierced EV cells can trigger chain reactions if reused, so damaged cells should be scrapped immediately.【F:data/vesc_help_group/text_slices/input_part008.txt†L1809-L1816】
- Wiring 20s8p builds exposed common mistakes: swapping internal pack polarity or reversing balance leads leaves the first series group reading 0 V and can cook BMS components, stressing the need to land B− before balance taps and to verify sockets stepwise (3.5 V, 7 V, etc.).【F:data/vesc_help_group/text_slices/input_part008.txt†L1980-L2018】【F:data/vesc_help_group/text_slices/input_part008.txt†L2035-L2059】
- High-current packs rely on doubled 6 AWG leads or laminated copper straps, but builders caution that poor routing becomes a fire hazard and PETG enclosures can soften if heavy leads are soldered in after assembly.【F:data/vesc_help_group/text_slices/input_part008.txt†L1957-L1977】【F:data/vesc_help_group/text_slices/input_part008.txt†L2341-L2345】
- Honeycomb fish-paper layouts let Xiaomi Pro 2 owners squeeze 20s5p internally without spacers, but the group stresses that holderless builds demand meticulous insulation and that bag batteries max out near 20s6p unless you accept risky 7p stacking.【F:data/vesc_help_group/text_slices/input_part008.txt†L4862-L4864】【F:data/vesc_help_group/text_slices/input_part008.txt†L4851-L4854】
- Riders mapping G30 deck space argue you can barely fit ~112–120 horizontal 21700 cells, equating to ~17s8p with careful copper folding, yet veterans warn that published photos often hide compromised BMS placement and that mixing aged gray and purple LG M26 variants can upset pack balance.【F:data/vesc_help_group/text_slices/input_part008.txt†L5121-L5156】【F:data/vesc_help_group/text_slices/input_part008.txt†L5218-L5232】
- Salvaged vape cells show severe imbalance and unknown provenance; even hobby experiments concede the cells are “pocket size cancer,” reinforcing why the group discourages reusing disposable packs in serious builds.【F:data/vesc_help_group/text_slices/input_part008.txt†L4792-L4815】
- Recent 18650 guidance steers builders toward 8 mm pure nickel so the positive vent ring remains exposed; stretching to 10 mm offers minimal resistance gains yet risks blocking the CID release path.【F:data/vesc_help_group/text_slices/input_part008.txt†L11290-L11334】
- Vet AliExpress “pure nickel” listings carefully—veterans report many hide nickel-plated steel in the fine print—and leave holder channels or fish-paper gaps so any vented gas can escape instead of ballooning a potted pack.【F:data/vesc_help_group/text_slices/input_part008.txt†L11323-L11335】【F:data/vesc_help_group/text_slices/input_part008.txt†L11406-L11424】
- A Spanish NAMI build now parallels LG 40T strings with extra LG M50LT sticks to stretch range, but peers caution that mixing 5 Ah and 4 Ah cells in one parallel demands conservative draw and a smart BMS (150 A in this case) to keep the weaker chemistry from overheating or drifting out of balance.【F:data/vesc_help_group/text_slices/input_part008.txt†L17040-L17056】【F:data/vesc_help_group/text_slices/input_part008.txt†L17105-L17156】【F:data/vesc_help_group/text_slices/input_part008.txt†L17194-L17199】
- Budget “smart” BMS boards remain a packaging trade-off: the latest no-name unit was twice the size of an ANT despite lower amp ratings, while the 21s 100 A JBD still fits between 18650 rows and only cost €45 during the AliExpress sale, making it attractive where width matters.【F:data/vesc_help_group/text_slices/input_part008.txt†L17098-L17118】

### Charging & Touring Logistics
- A VESC-swapped NIU NQi is happily fast-charging at ~33 A/67 V (≈2.2 kW) on public stations through its 28p pack—roughly 1.17 A per cell—showing the practical ceiling before the owner adds a second charger for quicker turnarounds.【F:data/vesc_help_group/text_slices/input_part008.txt†L13822-L13826】
- Riders are sparring over fast-charge limits: a 90 Ah touring pack drawing 33 A (~0.37 C) drew criticism from builders who cap their 12 p packs near 0.1 C to preserve cycle life, even though the cells are spec’d for more aggressive 1 C bursts.【F:data/vesc_help_group/text_slices/input_part008.txt†L16237-L16266】
- That same NIU rider logged a 274 km (170.4 mi) day ride in just under 12 hours, illustrating how even 2.2 kW charging still forces multi-hour stops and careful route planning for long-distance tours.【F:data/vesc_help_group/text_slices/input_part008.txt†L16268-L16270】【F:data/vesc_help_group/text_slices/input_part008.txt†L17160-L17189】
- Happy Giraffe keeps warning that generic DC bench supplies lack the CV taper and balancing finesse of real chargers; using them as pack chargers is “stupid” unless you accept shortened battery life and incomplete top balancing on cheap BMS boards.【F:data/vesc_help_group/text_slices/input_part008.txt†L16694-L16700】

### Emerging Controller Platforms & Telemetry
- FOCforever previewed SEVEN’s upcoming TOLL (18 MOSFET) and TOLT (30 MOSFET) controllers in 100/135/150 V trims featuring multilayer PCBs packed with thermal vias, modular VESC Express daughterboards, and pending CNC housings plus a matching CNC twist throttle and even a 400 V variant on the roadmap.【F:data/vesc_help_group/text_slices/input_part008.txt†L14004-L14020】【F:data/vesc_help_group/text_slices/input_part008.txt†L14015-L14020】
- The same update revealed Tronic’s X12 board: ~20 kW capability from 12 FETs, eleven electrolytic caps, bundled 6 AWG phase leads, onboard ESP32/VESC Express, and color-coded voltage options (100 V blue, 24 S red, 150 V violet), highlighting the leap over cap-starved 250/250R units.【F:data/vesc_help_group/text_slices/input_part008.txt†L14022-L14055】【F:data/vesc_help_group/text_slices/input_part008.txt†L14029-L14033】【F:data/vesc_help_group/text_slices/input_part008.txt†L14051-L14055】
- Engineers reminded the group that VESC Tool often reports “VESC amps” higher than instrumented phase current, so tuning should leave margin rather than chasing the app’s peak numbers.【F:data/vesc_help_group/text_slices/input_part008.txt†L14119-L14126】

### Displays & Instrumentation
- NetworkDir’s SimpleVescDisplay project gives riders an ESP32 dash that saves odometer data on-board, adding to the ecosystem of CAN-ready screens such as Nextion, Davega, Voyage’s Megan, and Veethree panels that need custom firmware blocks to display VESC telemetry.【F:data/vesc_help_group/text_slices/input_part008.txt†L13411-L13417】【F:data/vesc_help_group/text_slices/input_part008.txt†L13436-L13448】【F:data/vesc_help_group/text_slices/input_part008.txt†L13483-L13484】

### Showcase Builds & Custom Frames
- Face de Pin Sucé unveiled a race-prepped scooter running a 22S11P pack, C350 controller, Hope Tech4 V4 brakes, and in-house–wound motors, highlighting the bespoke component level in European race paddocks.【F:data/vesc_help_group/text_slices/input_part008.txt†L2483-L2493】
- Simone is mixing NAMI Viper and Rion chassis cues to host a 22S10P pack, noting the fork had to be machined to clear 70H hubs and 3 mm discs, underscoring the fabrication required for oversized drivetrains.【F:data/vesc_help_group/text_slices/input_part008.txt†L2592-L2599】
- JPPL ordered a Titaone X10 carbon frame and warned that à la carte spares are “crazy expensive,” suggesting prospective builders budget for high replacement costs even when buying the bare chassis.【F:data/vesc_help_group/text_slices/input_part008.txt†L3033-L3056】

### VESC Displays & Instrumentation
- Mihail is prototyping a VESC touch display with LVGL, CAN-bus control, profile switching, and an onboard regulator that steps pack voltage to 5 V, and has 120 surplus 480×320 IPS panels wired via ESP32-S3 for future builds.【F:data/vesc_help_group/text_slices/input_part008.txt†L2501-L2507】【F:data/vesc_help_group/text_slices/input_part008.txt†L2583-L2587】
- Chris Culver already runs an LVGL-based dashboard and offered help, implying reusable firmware may exist for similar display projects.【F:data/vesc_help_group/text_slices/input_part008.txt†L2985-L2990】

### Xiaomi/Ninebot Dash Scripting & Field-Weakening Lessons
- Unlocking Ninebot “secret mode” still depends on holding full brake and throttle while double-tapping the dash button; failing to exit walk mode leaves the scooter capped near 20 km/h, and removing the LISP script while still locked freezes the limit in place.【F:data/vesc_help_group/text_slices/input_part008.txt†L17726-L17760】【F:data/vesc_help_group/text_slices/input_part008.txt†L17791-L17799】
- The 6.05 ADC branch introduces fixed field-weakening and wattage parameters (`secret-sport-fw`, `secret-sport-watts`) plus a lower recommended throttle resistor (≈470 Ω); users added RC filtering across the hall supply to stop the headlight from pulling the brake voltage low.【F:data/vesc_help_group/text_slices/input_part008.txt†L17811-L17827】
- Riders caution that these dash scripts can randomly kill power mid-ride—keep throttle wiring hardwired once configuration is done and treat the display primarily as instrumentation.【F:data/vesc_help_group/text_slices/input_part008.txt†L18340-L18344】

### Regen Braking & Control Tuning
- For 20s6p Samsung 32E packs, experienced tuners recommend capping VESC e-brake at roughly −40 A motor / −8 A battery (stretching to −15 A only after verifying BMS limits) because the −65 A defaults are unnecessarily aggressive.【F:data/vesc_help_group/text_slices/input_part008.txt†L17921-L17927】
- The same conversation highlighted how G30 throttle smoothing is governed by exponential filters in VESC Tool; reducing those values quickens initial response once regen limits are sane.【F:data/vesc_help_group/text_slices/input_part008.txt†L17935-L17952】

### Thermal Management Updates
- Benur Lgl’s 20s12p C350 race build relies on a finned aluminum radiator and copper-backed Arctic Gel interface; he reports ~55 °C peaks even while pushing ~38.5 kW and 850 A phase, reinforcing the value of rigid heatsink enclosures over clip-on fans.【F:data/vesc_help_group/text_slices/input_part008.txt†L17927-L17978】
- Ubox Alu Lite owners learned that 5 mm thermal pads are too insulating—swap to thinner pads or paste to avoid 70 °C spikes, and remember that heatpipes have finite watt capacity before performance collapses.【F:data/vesc_help_group/text_slices/input_part008.txt†L18030-L18066】【F:data/vesc_help_group/text_slices/input_part008.txt†L18082-L18084】

### Frame Geometry & High-Speed Handling
- Race builders still rate Dualtron Thunder as the most forgiving >150 km/h chassis thanks to adjustable arm angles and shortened stems, whereas GT2 and Inmotion RS need CNC work but reward riders with stable steering above 90 km/h; NAMI frames excel for long-range/off-road when paired with dampers instead of chasing top speed.【F:data/vesc_help_group/text_slices/input_part008.txt†L18177-L18239】【F:data/vesc_help_group/text_slices/input_part008.txt†L18407-L18419】【F:data/vesc_help_group/text_slices/input_part008.txt†L18594-L18599】
- Singapore’s looming PEV restrictions pushed riders to brainstorm stealth options such as disguising scooters as e-bikes with faux pedals, or commuting across the Malaysian border for unrestricted riding.【F:data/vesc_help_group/text_slices/input_part008.txt†L18225-L18239】

### Battery Projects, Packaging, & Components
- Jiabada’s copper 17s/50 A smart BMS ships in under a week and is small enough to share deck space with 17s6p LG packs in Xiaomi Pro 2 builds; internal decks measure ~119 mm and still require rail grinding or extensions for 21700 cells plus BMS clearance.【F:data/vesc_help_group/text_slices/input_part008.txt†L18601-L18624】【F:data/vesc_help_group/text_slices/input_part008.txt†L18597-L18600】
- Builders targeting 20s12p or 24s12p G30 conversions plan to stack externals or relocate VESCs outside the deck; lack of warranty above 20s remains the norm, so designs include vertical BMS mounting and removable 2s booster packs charged via RC gear.【F:data/vesc_help_group/text_slices/input_part008.txt†L18630-L18654】【F:data/vesc_help_group/text_slices/input_part008.txt†L18472-L18486】
- LG M26 cells comfortably feed 20 A ebike controllers when arranged 6p (~3 A per cell); builders reserve higher-discharge chemistries (P45B, 40H) for scooter packs and recycle surplus LG cells into Pro 2 range extenders.【F:data/vesc_help_group/text_slices/input_part008.txt†L18619-L18623】【F:data/vesc_help_group/text_slices/input_part008.txt†L18641-L18654】
- A Turkish G30LP priced around $700 already carries 20s5p plus a 3s6p external and a 23s-ready controller—valued as a turnkey high-voltage commuter by local veterans.【F:data/vesc_help_group/text_slices/input_part008.txt†L18371-L18380】

### KWeld & Shop Power Tips
- Car batteries sag after only a handful of welds; hobbyists now favor CNHL 4S 9.5 Ah hardcase packs or similar high-C LiPos to sustain kWeld’s 2 kA pulses without undervoltage faults, while old RC packs or power banks run too hot even with added heatsinks.【F:data/vesc_help_group/text_slices/input_part008.txt†L18440-L18467】【F:data/vesc_help_group/text_slices/input_part008.txt†L18441-L18442】

### Small-Format & Youth Builds
- Converting kid scooters from brushed controllers to VESC mini 6-FETs requires at least 7s supply; when budgets are tight, RC brushed ESCs covering 1S–18S/0.5–500 A exist but often cost as much as Flipsky solutions unless you select programmable Hobbywing/Traxxas units.【F:data/vesc_help_group/text_slices/input_part008.txt†L18138-L18169】
- Haku’s refurbishment notes show that swapping lead-acid packs for 5S lithium and keeping top speed near 15 mph preserves safety while still giving children “real” throttles and lighting upgrades.【F:data/vesc_help_group/text_slices/input_part008.txt†L18115-L18136】【F:data/vesc_help_group/text_slices/input_part008.txt†L18729-L18757】

### Spintend & High-Voltage Planning
- Spintend’s 100 V mini remains limited to ~22S, so riders eye Tronic X12 for true 26S builds; adding detachable 2S boosters without BMS supervision demands RC chargers plus inline fuses or active balancers for safety.【F:data/vesc_help_group/text_slices/input_part008.txt†L18472-L18488】

- To minimize latency and preserve failsafe behavior, Mihail plans to leave throttle and brake sensors hard-wired to the ESC instead of routing them through CAN, even though the display PCB breaks those signals out.【F:data/vesc_help_group/text_slices/input_part008.txt†L2586-L2591】

### Braking Strategy & Regen Usage
- Riders experimenting with regen-heavy setups report -80 A electronic braking can nearly lift them over the bars, leading some to run regen-only while others stress the value of Spinny tuning to modulate force.【F:data/vesc_help_group/text_slices/input_part008.txt†L2522-L2538】
- Heavy scooters quickly chew through budget pads; veterans recommend full-metallic options (e.g., Galfer) and caution that bargain compounds from AliExpress often underperform despite marketing claims.【F:data/vesc_help_group/text_slices/input_part008.txt†L2539-L2567】
- Discussions about fitting motorcycle-caliber hardware (dual calipers per lever, Brembo swaps) conclude that weight and ergonomics remain trade-offs, though moto parts boost heat capacity for regen-averse riders.【F:data/vesc_help_group/text_slices/input_part008.txt†L2520-L2536】

### July 11–19 2024 Addendum (Lines 18,761–20,260)

#### Data Logging, Dashboards & App Support
- Riders confirmed VESC Tool keeps logging while the mobile app is backgrounded, so GPS apps can sit in the foreground during speed runs; one test was staged at 200 A phase in 28 °C ambient.【F:data/vesc_help_group/text_slices/input_part008.txt†L18743-L18750】
- GPS overlays can drift dramatically at high speed—one rider saw a 7 km discrepancy versus the VESC dash—so they now enable VESC log recording directly for trustworthy speed traces.【F:data/vesc_help_group/text_slices/input_part008.txt†L19613-L19622】
- The official Android APK is available for free once you “purchase” VESC Tool for €0 on vesc-project.com and download it from the purchased-files page, avoiding sketchy mirrors.【F:data/vesc_help_group/text_slices/input_part008.txt†L19580-L19592】
- Builders suggest sealing exposed USB‑C cutouts on Ubox and similar controllers after water ingress spoofed temperature readings earlier in the file; relocating the port and silicone-sealing the original opening prevented a repeat failure.【F:data/vesc_help_group/text_slices/input_part008.txt†L19849-L19850】

#### Controller Hardware, Firmware & Reliability
- AliExpress’ 48‑MOSFET “1200 A” controller listing appears to bundle a 40S4P Samsung 50S pack (~2.96 kWh) yet likely runs non-VESC firmware; veterans note the board is overbuilt for the battery’s ~140 A continuous capability and question assembly quality.【F:data/vesc_help_group/text_slices/input_part008.txt†L18795-L18811】
- Multiple owners urged against Makerbase’s 75200 V2, citing poor motor detection and recommending the Ubox 85/150 or Lite as safer drop-ins.【F:data/vesc_help_group/text_slices/input_part008.txt†L18833-L18836】
- NetworkDir highlighted wildly inaccurate current sensing on 75100 hardware and published 5 mΩ shunt replacement firmware to regain proper readings, warning that stock “fake” shunts appear tuned simply to clamp current.【F:data/vesc_help_group/text_slices/input_part008.txt†L19318-L19378】
- A Makerbase 75100 lost its 3.3 V rail after the Bluetooth module touched the aluminum enclosure; the unit no longer boots or lights the module even though the FETs survived, underscoring the fragility of the logic supply.【F:data/vesc_help_group/text_slices/input_part008.txt†L18981-L19011】
- Another 75100 failed outright after roughly 2,000 km despite never exceeding 60 °C and only drawing ~10 A, adding to the anecdotal evidence of random Flipsky/Makerbase deaths.【F:data/vesc_help_group/text_slices/input_part008.txt†L20241-L20267】
- Dual Spintend controllers on an SNSC frame simultaneously shorted after stray solder balls bridged phases, motivating thorough PCB inspections before final assembly even on higher-end ESCs.【F:data/vesc_help_group/text_slices/input_part008.txt†L19169-L19180】
- PuneDir warned that the Ubox Lite’s onboard ESD protector will blow if one battery lead is pulled while CAN remains connected, so power loops must be broken symmetrically.【F:data/vesc_help_group/text_slices/input_part008.txt†L19632-L19632】
- Builders swapping Zero 10X and Mantis hubs were told to measure stator resistance with VESC Tool and mount the lower‑kV (higher resistance) motor on the rear to maximize launch torque.【F:data/vesc_help_group/text_slices/input_part008.txt†L19779-L19786】

#### Battery Packs, Charging & BMS Practices
- PuneDir grabbed a 200 A JK smart BMS for upcoming high-power builds, continuing the trend toward oversized protection hardware.【F:data/vesc_help_group/text_slices/input_part008.txt†L19347-L19348】
- Charging math for 20S10P Samsung 40T packs landed at ~2 A per cell with a 20 A charger—well under the 6 A spec—so the crew signed off on the rate while reminding riders that balancing tapers the final 30–60 minutes.【F:data/vesc_help_group/text_slices/input_part008.txt†L19350-L19378】
- Tenpower 40TG cells were pushed to 40 A per cell in 4P blocks (≈160 A battery) without overheating, but limited 7S companion packs tripped BMS overcurrent, highlighting the need to size every parallel group for the target phase amps.【F:data/vesc_help_group/text_slices/input_part008.txt†L19029-L19078】
- GABE is redesigning a Xiaomi Pro 2 around a 24S12P (≈5 kWh) internal pack with optional 4S boosters, explicitly rejecting external battery bricks despite the warranty implications.【F:data/vesc_help_group/text_slices/input_part008.txt†L20283-L20284】
- PuneDir’s upcoming 20S20P LG M26 pack (planned 160–200 A draw) may still need active cooling for 100–120 km/h trips because the cells’ internal resistance and frame weight stack load on long pulls.【F:data/vesc_help_group/text_slices/input_part008.txt†L19742-L19758】
- Noname described NIU’s OEM module sandwiched between aluminum plates with silicone pads tying into the lid, a packaging trick others can copy for even heat spread.【F:data/vesc_help_group/text_slices/input_part008.txt†L19772-L19774】
- GX16 charge ports are rated roughly 5 A continuous, so higher-rate chargers need beefier connectors or dual inlets.【F:data/vesc_help_group/text_slices/input_part008.txt†L19851-L19858】
- Riders compared AliExpress fast chargers: the classic red fan-cooled unit actually feeds ~10 A through most BMSes, while newer adjustable 20 A supplies stay quieter and cover 4S–24S packs; both links were shared for sourcing.【F:data/vesc_help_group/text_slices/input_part008.txt†L18930-L18945】
- Using a BMS as the primary power switch remains controversial—Shlomozero wanted to shut accessories off through an ANT BMS, but others stressed that dedicated ignition leads on each VESC offer cleaner behavior for dual-drive builds.【F:data/vesc_help_group/text_slices/input_part008.txt†L19639-L19655】

#### Thermal Management & Long-Pull Operation
- The SNSC chassis under one Ubox proved too warped for paste alone; the owner now preloads the controller with thick pads (or graphene sheets when budget allows) and is considering thermal glue to flatten hot spots.【F:data/vesc_help_group/text_slices/input_part008.txt†L19863-L19880】
- Race telemetry logged 171 °C stator temps, reminding teams that even well-cooled hubs can roast during competition when airflow stalls.【F:data/vesc_help_group/text_slices/input_part008.txt†L19244-L19248】
- Builders debating 32S Seven controllers noted that voltage without adequate cooling just shifts the thermal burden—bigger packs, thermal plates in the airstream, or active cooling are mandatory for 60 km+ nonstop blasts.【F:data/vesc_help_group/text_slices/input_part008.txt†L19740-L19758】

#### Motor Selection, Tuning & Field-Weakening
- Extended discussions reiterated that motor kV strictly defines RPM per volt: lower kV grants torque at sane voltages, while chasing high-kV windings demands far more current (and battery/ESC headroom) to regain launch force; riders are rethinking 32S upgrades accordingly.【F:data/vesc_help_group/text_slices/input_part008.txt†L19882-L19927】
- Builders experimenting with Flipsky field-weakening still find it less effective than higher-end controllers, and some are backing off aggressive FW to limit heat and erratic detection on budget hardware.【F:data/vesc_help_group/text_slices/input_part008.txt†L19859-L19866】
- The 65H crowd reaffirmed that these motors wake up only when fed ~150–200 A battery current per side; anything below ~60 A batt per motor leaves torque on the table even with field-weakening enabled.【F:data/vesc_help_group/text_slices/input_part008.txt†L19059-L19127】

#### Accessories, Controls & Chassis Bits
- Cheap AliExpress steering dampers keep snapping when over-tightened; European racers instead point to Bitubo or other motorcycle-grade units for NAMI installs if budgets allow.【F:data/vesc_help_group/text_slices/input_part008.txt†L19464-L19475】
- Riders hunting more comfortable cockpits found the Vsett 9 seat via Alien Rides after AliExpress came up empty, and are eyeing cargo racks with removable baskets to stash auxiliary packs.【F:data/vesc_help_group/text_slices/input_part008.txt†L19624-L19630】【F:data/vesc_help_group/text_slices/input_part008.txt†L19787-L19789】
- Thumb-throttle swaps gravitated toward the inexpensive “300X” units (5 V compatible) as a reliable upgrade path for both scooters and e-bikes.【F:data/vesc_help_group/text_slices/input_part008.txt†L20211-L20218】
- Covering LED headlights or dash accessories in silicone after wiring prevents accidental shorts—one rider blew a bar light instantly by touching the PSU leads together mid-test.【F:data/vesc_help_group/text_slices/input_part008.txt†L18755-L18763】

### Charger & Accessory Sourcing
- Mirono recommended a €120–€160 adjustable charger line from AliExpress for 10S–16S packs, preferring it over repurposed server PSUs that failed after a few months of rewiring, while peers endorsed Huawei GTK units as reliable CC/CV alternatives.【F:data/vesc_help_group/text_slices/input_part008.txt†L2603-L2613】
- Members searching for cleaner control hardware highlighted Tusk’s Compact Control Switch as a premium but durable lighting cluster option when standard scooter switchgear feels flimsy.【F:data/vesc_help_group/text_slices/input_part008.txt†L3160-L3161】
- Patrick’s hands-on with the Xtar VC8 charger shows only slots 1–4 offer storage/capacity testing at 0.5 A, whereas the pricier VC8S enables all eight bays at 1 A, so builders who condition whole 8p strings consistently should budget for the S revision.【F:data/vesc_help_group/text_slices/input_part008.txt†L11657-L11658】

### May 14–22 Controller & Chassis Updates (Lines 7,201–8,700)
- Racers warned that Makerbase Ubox 85/250 controllers keep failing on 22 s packs even with regen disabled, while C350 units have survived full-race weekends at that voltage so long as regen stays off; CL350 hardware reportedly runs hotter, and frustrated 3Shul owners shared the official Drive with CL350 V3 firmware sources because vendor support was unresponsive.【F:data/vesc_help_group/text_slices/input_part008.txt†L7246-L7307】
- Multiple Tronic 250 buyers received five new units with dead CAN rails and now wire dual throttles by feeding one ESC the full three-pin plug and sharing only signal plus ground to the second, explicitly keeping the 3.3 V rails isolated to avoid burning accelerators while waiting on replacements.【F:data/vesc_help_group/text_slices/input_part008.txt†L7204-L7208】【F:data/vesc_help_group/text_slices/input_part008.txt†L7565-L7587】
- Battery builders slammed dual 80H hub swaps that rely on just 20s4p packs, suggesting 70H/50H combinations or split windings with doubled 6 AWG phase leads when chasing 200 A+, and stressing that heavy motors demand proportionally larger energy storage.【F:data/vesc_help_group/text_slices/input_part008.txt†L7533-L7574】
- DIYers considering split-battery layouts were reminded that running two smaller packs in series through one BMS introduces timing mismatches—several fried hardware by pushing 72 V through paired 36 V modules despite using triple 6 AWG leads—so they now favor single-pack mock-ups before welding.【F:data/vesc_help_group/text_slices/input_part008.txt†L7500-L7526】
- For temperature sensing, riders confirmed cheap 10 kΩ B3950 NTC probes wired between hall ground and the thermistor lead work well on hub motors, with polarity irrelevant because the sensor is a resistor.【F:data/vesc_help_group/text_slices/input_part008.txt†L7458-L7459】
- A dual Ubox V2 that lost sensorless detection after outdoor mounting was traced to a cracked A6 diode feeding the EG3112 gate driver; owners plan to replace or bridge the diode and noted the mediocre stock soldering on that rail.【F:data/vesc_help_group/text_slices/input_part008.txt†L7732-L7822】
- One 75100 owner reported the motor kept spinning when field weakening was active even after closing the throttle, underscoring the need to capture firmware regressions for Vedder in a consolidated issue report.【F:data/vesc_help_group/text_slices/input_part008.txt†L8091-L8097】
- High-output Ninebot and GT2 projects now target 26s8p P42A batteries delivering 320–560 A through Tronic X12s, but builders are already fighting thermal issues until the dual Ubox controllers are clamped to aluminum and wheel diameter/kv are tuned for the higher pack voltage.【F:data/vesc_help_group/text_slices/input_part008.txt†L8231-L8429】
- Thermal experiments showed aluminum PCBs can keep a 3.2 kW setup near 29 °C, and MXlemming tuning on 30 s gear cut controller temps from 80 °C to ~60 °C at ~150 A, although some racers found the algorithm unusable on high-power hubs because it reduced top speed.【F:data/vesc_help_group/text_slices/input_part008.txt†L8453-L8486】
- Cell hunters spotted Molicel’s new P50B (5 Ah/65 A) alongside rumors of XA3 21700 cells capable of 50 A, offering future pack options beyond P45B but with unproven cycle life so far.【F:data/vesc_help_group/text_slices/input_part008.txt†L8338-L8350】
- Zero 10X tuners showcased a 10 kW, 72 V Ubox build with traction control disabled for tire noise yet capped real-world speed near 60 km/h for stability, reinforcing the handling limits of legacy twin-stem frames.【F:data/vesc_help_group/text_slices/input_part008.txt†L8281-L8289】
- Frame and service chatter favored the suspension-equipped Ninebot Max G2 over a rigid G30 for vibration longevity, praised SNSC rental frames for surviving 80 km/h guardrail impacts with only peripheral damage, detailed DNM shock fitment plus 13"×7" tire swaps, and shared a lever-free hub tire removal method to avoid rim scratches.【F:data/vesc_help_group/text_slices/input_part008.txt†L8669-L8692】
- Wiring refresher: Flipsky 75350 users confirmed throttle stays on ADC1, the brake switch on ADC2 with “Current No Reverse Brake ADC2” configured, while hall 5 V rails should not be tied between controllers unless absolutely necessary.【F:data/vesc_help_group/text_slices/input_part008.txt†L8293-L8303】【F:data/vesc_help_group/text_slices/input_part008.txt†L8646-L8648】

### June 4–10 Dual-VESC Debates & Klima Planning (Lines 11,651–13,150)
- Community tests show the Xtar VC8S is the only version that lets all eight bays run storage/capacity cycles at 1 A, making it the preferred conditioning charger over the half-capable VC8 for large pack work.【F:data/vesc_help_group/text_slices/input_part008.txt†L11657-L11658】
- Mixed-brand 75-series controllers can share CAN if they run identical firmware builds, but riders leaning on Spintend’s ADC splitters for single/dual modes lose traction control, prompting calls for Lisp-based toggles that keep CAN alive.【F:data/vesc_help_group/text_slices/input_part008.txt†L11914-L11959】【F:data/vesc_help_group/text_slices/input_part008.txt†L12459-L12566】
- Zero/Vsett owners surfaced real failures—like a ripped 10X phase/hall loom and Spintend hall dropout—that underline the need for better strain relief, sensor diagnostics, and documented pinouts when converting rental frames to VESC hardware.【F:data/vesc_help_group/text_slices/input_part008.txt†L11830-L11833】【F:data/vesc_help_group/text_slices/input_part008.txt†L12075-L12079】【F:data/vesc_help_group/text_slices/input_part008.txt†L12462-L12471】
- Race tuners reiterated motor selection heuristics (70H for speed, 75H/80H for torque with ≥22S) while Klima riders mapped the limits of its 10×3.5" chassis and controller bay before chasing 72 V wheelie builds, keeping the group focused on matching frames, motors, and packs.【F:data/vesc_help_group/text_slices/input_part008.txt†L12385-L12418】【F:data/vesc_help_group/text_slices/input_part008.txt†L12510-L12537】
- JPPL’s quick repair for worn folding-clamp bushings—shimming pins with thin metal or heat-shrink and torquing every screw—added a field-service trick that keeps high-power stems tight without replacing the ring.【F:data/vesc_help_group/text_slices/input_part008.txt†L12589-L12610】

### Field Weakening & Control Tuning
- Rosheee logged back-to-back pulls comparing pure current control, MTPA, and +40 A field weakening on dual Ubox hardware, showing how 16s6p test packs respond when FW is introduced at ~90 % duty cycle.【F:data/vesc_help_group/text_slices/input_part008.txt†L4220-L4237】
- Izuna’s MP2 v0.5 repeatedly tripped ABS overcurrent around 70 km/h despite 200 A phase limits, improving only after cutting battery current and switching to hall sensors, which underscores how firmware sample modes and hardware current limits interact on high-speed runs.【F:data/vesc_help_group/text_slices/input_part008.txt†L4913-L4920】【F:data/vesc_help_group/text_slices/input_part008.txt†L5250-L5258】

### PuneRon Prototype & Custom Drivetrains
- PuneDir’s “PuneRon” differential-scooter mock-up runs 60H motors geared 13/73 (moving to 13/80) and already hit 90 km/h on a borrowed Zero battery; he noted Makerbase 84100s survived accidental XT60 disconnects mid-ride but wants bigger sprockets for acceleration.【F:data/vesc_help_group/text_slices/input_part008.txt†L4273-L4286】【F:data/vesc_help_group/text_slices/input_part008.txt†L4714-L4728】
- The build team is machining 6 mm steel rear sprockets locally, planning water-cooled motor endplates, and debating whether drilled stators plus belt drives or steel chainrings give the best durability for 200 A setups.【F:data/vesc_help_group/text_slices/input_part008.txt†L4791-L4859】【F:data/vesc_help_group/text_slices/input_part008.txt†L5387-L5403】
- Battery packaging experiments suggest the frame bag holds ~5 L—enough for 20s6p with holders—while Zero 10X decks can accommodate 20s7p of LG M26 cells but leak under 60–70 A loads, prompting future upgrades to higher-grade chemistry.【F:data/vesc_help_group/text_slices/input_part008.txt†L4851-L4854】【F:data/vesc_help_group/text_slices/input_part008.txt†L5163-L5177】
- By late June the Hyosung RX125 chassis had a removable belly pan ready for a 20s20p pack; PuneDir is cutting a 72T rear sprocket and eyeing a Makerbase 84200 with radiator-fed water cooling to hold ~200 A battery and (optimistically) 300 A phase once the controllers restock.【F:data/vesc_help_group/text_slices/input_part008.txt†L16890-L16900】【F:data/vesc_help_group/text_slices/input_part008.txt†L17248-L17250】【F:data/vesc_help_group/text_slices/input_part008.txt†L17288-L17334】【F:data/vesc_help_group/text_slices/input_part008.txt†L17330-L17366】

### Spin-Y Throttle & Dashboard Integration
- Dualtron owners debugging the Spin-Y2 thumb throttle discovered the signal only registered after moving the lead to ESC B’s ADC1 port and feeding it 5 V instead of 3.3 V, implying ESC A’s ADC1 is disabled by default in some Ubox firmware revisions.【F:data/vesc_help_group/text_slices/input_part008.txt†L4290-L4390】
- Xiaomi Pro 2 riders running dual 75100s reuse the stock dash via custom scripts, keeping the throttle on a direct ADC input for traction control while splicing lighting into AUX power with series resistors to protect LEDs.【F:data/vesc_help_group/text_slices/input_part008.txt†L5018-L5046】
- When fitting Spin-Y throttles to Makerbase 75100s, the group now measures the signal lead before plugging it into ADC—anything above ~3.8 V risks killing the STM MCU, so they pre-check the harness while powering it from the controller’s 5 V rail.【F:data/vesc_help_group/text_slices/input_part008.txt†L16607-L16619】
- 1Zuna’s dash Lisp still needs a 1 k–1.2 k pull-down inline with the button harness to stop ghost presses; builders are soldering the resistor into the loom instead of reworking the PCB to keep the dash compatible with both G30 and Makerbase ESCs.【F:data/vesc_help_group/text_slices/input_part008.txt†L17098-L17158】

### Vsett & Zero Platform Notes
- NetworkDir’s Zero 10X 50H hub uses the same 16×4 shell seen on some Vsett swaps, and his failure came from a ripped phase/hall harness—reinforcing the need for strain relief and inspection when up-rating motors in those decks.【F:data/vesc_help_group/text_slices/input_part008.txt†L11830-L11833】
- Vsett 10+ owners considering Spintend upgrades highlighted Bluetooth telemetry, speed-limit removal, and auxiliary 3 S packs as the big wins, but they’re still seeking documentation on reusing stock lighting and accessory ports before committing.【F:data/vesc_help_group/text_slices/input_part008.txt†L11958-L11959】【F:data/vesc_help_group/text_slices/input_part008.txt†L12060-L12061】
- Apo’s request for the Vsett 10+ main-harness pinout and Shlomozero’s hunt for ADC adapters and alternative Ubox sellers show builders still need reference diagrams and sourcing options to finish these conversions.【F:data/vesc_help_group/text_slices/input_part008.txt†L12075-L12079】

### Tire & Wheel Fitment Debates
- The group keeps steering 10" Zero/VSETT owners toward CST 10×3 or PMT 10×3.5 rubber, calling Xuancheng slicks soft but short-lived above 4 kW without traction control and warning that 10" rims look undersized with 165 mm rotors.【F:data/vesc_help_group/text_slices/input_part008.txt†L5000-L5034】【F:data/vesc_help_group/text_slices/input_part008.txt†L5593-L5599】
- Fork swaps to 145 mm travel assemblies slightly improve trail numbers on Zero 10X builds, though riders still rely on dampers and balanced phase currents (≈60 % rear) to tame wobble during launches.【F:data/vesc_help_group/text_slices/input_part008.txt†L5330-L5340】
- Recent feedback says Tuovt 90/55-6 lasts far longer on broken pavement than PMT rubber—PMT grips harder but its soft carcass “gets fucked instantly” on rough roads—so commuters are defaulting to Tuovt unless they ride smooth circuits.【F:data/vesc_help_group/text_slices/input_part008.txt†L17491-L17495】

### Dual-VESC Integration & Traction Control
- Builders mixing Makerbase, Flipsky, and other 75-series hardware report CAN works reliably only when both controllers share the exact VESC firmware compilation (e.g., 6.02 with 6.02); mismatched vendor apps or pinouts can brick communications, so they sanity-check sockets before tying packs together.【F:data/vesc_help_group/text_slices/input_part008.txt†L11914-L11959】
- Spintend’s ADC v2/v3 throttle splitter forces each controller to run standalone, which kills traction control and telemetry; riders debating CAN-cut switches or anti-spark toggles are instead leaning toward Lisp scripts or direct button wiring that preserves CAN where possible.【F:data/vesc_help_group/text_slices/input_part008.txt†L12459-L12480】【F:data/vesc_help_group/text_slices/input_part008.txt†L12543-L12566】
- Dual-motor builds that spin the front tire above ~100 A phase are taming launches by enabling Motor Current Scale profiles alongside traction control, letting them soften initial torque without losing top-end power.【F:data/vesc_help_group/text_slices/input_part008.txt†L17032-L17039】

### Cell Market Updates (May)
- Builders compare gray versus purple LG M26 inventory, reporting 14 mΩ IR on fresh Turkish stock versus >30 mΩ on older MH1 pulls, and reiterate that Samsung 35E/YR1035-class cells show lower resistance but can’t match high-current Molicels.【F:data/vesc_help_group/text_slices/input_part008.txt†L5201-L5233】
- Salvaged Navee N65 packs show leaking cells around 900 km, leading riders to plan full replacements with Aspilsan 18650s or sell the platform entirely rather than chase venting risks.【F:data/vesc_help_group/text_slices/input_part008.txt†L5544-L5590】

### Cell Market Updates
- Lisa confirmed EVE 40PL cylindrical pouches are available direct from the factory via Alibaba at roughly $4.35 per cell (minimum 50 units plus ~$100 shipping), making them attractive for bulk buyers despite steep logistics costs.【F:data/vesc_help_group/text_slices/input_part008.txt†L2681-L2699】
- Builders in high-tariff regions are stuck with €1 LG M26 cells versus €5–€11 for EVE or Molicel options, prompting debates about tolerating the sag temporarily and reselling later versus pausing builds until premium cells are affordable.【F:data/vesc_help_group/text_slices/input_part008.txt†L4111-L4135】

### Geometry, Stability & Safety Incidents
- Multiple riders called out Vsett 10+ and other C-fork scooters for instability above ~80 km/h, citing fatal crashes, wobble-prone geometry, and the need for better trail figures or dampers to stay upright at triple-digit speeds.【F:data/vesc_help_group/text_slices/input_part008.txt†L3106-L3158】
- PuneDir and others described personal tank-slapper experiences (78 km/h on a Zero) to stress how quickly oscillations escalate, especially with lighter riders or poor tires.【F:data/vesc_help_group/text_slices/input_part008.txt†L3173-L3183】
- NetworkDir shared that traction control around 80 000 ERPM differential preserves CST 10×3 tires, whereas disabling TC shreds them within days—framing TC as both a safety and tire-wear mitigation tool.【F:data/vesc_help_group/text_slices/input_part008.txt†L3589-L3602】
- Kirill countered the doom posts by listing production scooters with inherently stable geometry (Segway GT1/GT2, ST1/ST2, Inmotion RS, large Wepeds, Monorim-modded G30s, NAMI Blast), clarifying that C-fork wobble is model-specific rather than inevitable.【F:data/vesc_help_group/text_slices/input_part008.txt†L3120-L3126】

### High-Power Controller & Motor Experiments
- Hurriicane showcased a Pro 2 motor rewound for thicker conductors that can gulp 24 kW at 60 V without overheating, paired with 3Schul V4 controllers driving Lonnyo 70H speed hubs for tunnel-speed testing at 71 V.【F:data/vesc_help_group/text_slices/input_part008.txt†L2991-L3015】
- Riders eyeing AliExpress QS268-class 90H hubs debated whether 400 A phase specs translate to 30 kW in practice, with veterans warning that controller limits and rim sizing cap real output despite marketing claims.【F:data/vesc_help_group/text_slices/input_part008.txt†L3019-L3024】
- Field reports from Begode K-series owners note Spintend 85/250 controllers can tow fellow EUCs ~8 miles without thermal drama, reinforcing the platform’s durability when cooled properly.【F:data/vesc_help_group/text_slices/input_part008.txt†L3663-L3666】
- Raphael’s race testing found the G300 overheating toward 90 °C on hub motors that keep a R350 around 40 °C, and highlighted that aluminum PCBs tend to fail safe (tripping BMS) whereas FR4 boards can burn outright when MOSFETs short—supporting R350/C350 picks for 22 S race scooters and R500 upgrades for 500 A-class moto builds.【F:data/vesc_help_group/text_slices/input_part008.txt†L10686-L10690】

### Build Planning & Budget Discipline
- Veterans encouraged riders facing supply or budget crunches to stretch project timelines instead of compromising on core components, sharing examples of slow builds that avoided regrets and advising against rushing purchases just to stay on schedule.【F:data/vesc_help_group/text_slices/input_part008.txt†L4117-L4137】

### Mini-Bike & Fiido L3 Conversions
- Fiido L3 tear-downs showed the stock controller floating loose without a heatsink and limited to roughly 25 A, so jumping straight to 20s test packs without pre-charging the controller capacitors can pop the factory BMS; builders recommend matching voltages before connecting higher-voltage VESC hardware.【F:data/vesc_help_group/text_slices/input_part008.txt†L5858-L5875】
- After dialing battery current back to ~20 A and traction control to 20/20 A, a 60 A phase cap with +FW delivered 45 km/h and repeatable wheelies while keeping the hub cool, underscoring the importance of conservative current ramps on compact minibikes.【F:data/vesc_help_group/text_slices/input_part008.txt†L5915-L5922】
- The disassembly confirmed Fiido’s packs are heavily sealed—cells were locked under glued busbars and soldered fasteners, and a tripped protection board left entire parallel groups at 0 V—so refurb attempts require full BMS removal rather than quick cap swaps.【F:data/vesc_help_group/text_slices/input_part008.txt†L6009-L6016】【F:data/vesc_help_group/text_slices/input_part008.txt†L6443-L6449】

### Controller & Harness Diagnostics
- PuneDir recovered a “0 V CAN bus” fault on a surviving Makerbase 84100 by tracing a shorted CAN_H/L pair and confirmed the transceiver IC was intact, pointing to wiring damage from earlier MOSFET failures rather than silicon loss.【F:data/vesc_help_group/text_slices/input_part008.txt†L5882-L5903】
- Cengiz documented how to integrate an ignition/key switch with the Makerbase regulator: pull the EN pin to ground through 10 kΩ, then lift it with a 10 kΩ/100 kΩ divider instead of battery voltage when the switch closes, which protects the linear stage from over-voltage.【F:data/vesc_help_group/text_slices/input_part008.txt†L6460-L6464】

### Dual Controller & Dashboard Troubleshooting
- Lisa’s dual 75100 setup sounded rough even after disabling phase filters, and the 1Zuna CAN dashboard stopped reporting speed, suggesting further motor detection and CAN scaling checks are needed on 6.05 firmware before trusting road data.【F:data/vesc_help_group/text_slices/input_part008.txt†L6023-L6030】
- A second report from the same rider noted that the dual-ADC script let the rear motor run past 20 km/h limits while the front obeyed settings, implying the dual-controller Lisp needs explicit speed caps on both CAN nodes when repurposed for Ninebot G30 conversions.【F:data/vesc_help_group/text_slices/input_part008.txt†L6244-L6248】
- For on-the-fly 2WD toggles, NetworkDir recommended either Spintend’s ADC adapter (fed from the VESC’s 12 V rail) or a small Arduino running the VESC UART `setCurrent` example to drop the front motor to 0 A when a handlebar switch is pressed.【F:data/vesc_help_group/text_slices/input_part008.txt†L11488-L11502】

### Battery Fabrication & Adhesives
- Builders leaning on 3M marine adhesive to bond parallel groups warned it cures rock-solid—expect mechanical removal or fresh holders instead of assuming it will peel free during rework—and even minor pack notches demand sub-millimetre tolerances once glue is applied.【F:data/vesc_help_group/text_slices/input_part008.txt†L6076-L6089】
- Salvaged military packs revealed soldered busbars and even fasteners, reinforcing that salvagers should budget time for full desoldering or dremel work rather than assuming bolts will back out cleanly.【F:data/vesc_help_group/text_slices/input_part008.txt†L6443-L6449】

### Spot Welding Tools
- Cihan priced the Docreate DO-02 capacitor welder around $108 shipped to Turkey (less with coupons) and gathered teardown videos confirming ~0.36 mΩ ESR capacitors; peers suggested the foot-pedal version for thicker leads and called out Glitter 801D as a workable alternative if only 0.1–0.15 mm nickel is needed.【F:data/vesc_help_group/text_slices/input_part008.txt†L11290-L11337】【F:data/vesc_help_group/text_slices/input_part008.txt†L11517-L11520】

### High-Capacity G30 Experiments
- Ambitious plans for internal 20s12p P42A stacks prompted reminders that a G30 deck typically fits ~120 cells; exceeding that demands stacked modules, tall spacers, remote ESC mounting, and acceptance of 65–70 kg curb weights plus suspension geometry changes.【F:data/vesc_help_group/text_slices/input_part008.txt†L7087-L7133】
- Veterans recommended mocking the pack volume in cardboard or prints before buying cells and highlighted that heavier builds will likely require laser-cut forks or spacer systems similar to French race G30s to clear 11" tyres.【F:data/vesc_help_group/text_slices/input_part008.txt†L6550-L6561】【F:data/vesc_help_group/text_slices/input_part008.txt†L7087-L7137】

### Tire Selection & Race vs. Street Usage
- Track-focused riders praised Xuancheng slicks for turn-in but conceded the thin carcass feels like a “0.005 condom” on rough urban pavement, while CST-patterned 11" options retain cornering confidence with more puncture resistance for daily use.【F:data/vesc_help_group/text_slices/input_part008.txt†L6900-L6917】
- NetworkDir’s testing suggested 3.5" rubber rarely seats cleanly on Zero/Vsett rims without looking tractor-wide, so experimenting with pressure and rim width is essential before chasing 70 km/h corner grip claims.【F:data/vesc_help_group/text_slices/input_part008.txt†L6908-L6913】

### Copper Protection & Busbar Coatings
- Battery builders debated nickel versus copper busbars: copper cuts voltage sag even on capacity cells but corrodes fast, so several plan to nickel-plate copper straps at home or try zinc-rich sprays to stave off electrocorrosion without sacrificing conductivity.【F:data/vesc_help_group/text_slices/input_part008.txt†L6920-L6959】

### Cell Sourcing & Storage Notes
- Recent bulk buys netted unused Molicel P42A stock for about $1.80 per cell delivered, with veterans suggesting 30 % state-of-charge storage in refrigeration to stretch shelf life until the packs are built.【F:data/vesc_help_group/text_slices/input_part008.txt†L6474-L6475】【F:data/vesc_help_group/text_slices/input_part008.txt†L6651-L6658】

### Controller Support & Firmware Availability
- 22s builders warned that Makerbase Ubox 85/250s regularly fail even without regen at that voltage, while the C350 platform has run full race weekends on 22s provided regen is disabled and the CL350 is avoided for heat reasons; several racers offered discount help but stressed proper wiring before blaming the hardware.【F:data/vesc_help_group/text_slices/input_part008.txt†L7189-L7213】【F:data/vesc_help_group/text_slices/input_part008.txt†L7208-L7213】
- 3Shul owners struggling to locate firmware were pointed to an official Drive share that contains the CL350 V3 sources so they can compile a 6.2-capable build, even though the vendor site does not advertise the files.【F:data/vesc_help_group/text_slices/input_part008.txt†L7300-L7309】

### Tronic 250 CAN-Bus Failures
- Five freshly purchased Tronic 250 units arrived with dead CAN rails; the stop-gap was to run identical throttle signals into both controllers but isolate the 3.3 V rails (only ground the second controller) to avoid burning the accelerator until replacement CAN hardware arrives, highlighting slow warranty loops.【F:data/vesc_help_group/text_slices/input_part008.txt†L7233-L7240】【F:data/vesc_help_group/text_slices/input_part008.txt†L7565-L7588】

### Motor Selection for High-Power Builds
- French builders are shoehorning dual 80H hubs and individual 20s4p packs into custom CNC G30 frames, but race teams cautioned that pairing 80H motors with such small batteries is inefficient; they favor 70H rears with lighter fronts on 20s packs and note that well-tuned 70H setups have beaten 80H machines in both circuit and drag events.【F:data/vesc_help_group/text_slices/input_part008.txt†L7381-L7398】【F:data/vesc_help_group/text_slices/input_part008.txt†L7533-L7556】

### Temperature Monitoring Tips
- For motor temperature sensing, riders recommended inexpensive MF52B/MF52D 10 kΩ B3950 NTC probes wired between hall ground and the thermistor input, noting polarity is irrelevant and the parts behave reliably with VESC hardware.【F:data/vesc_help_group/text_slices/input_part008.txt†L7445-L7461】

### Ubox Gate-Driver Diode Failures
- A dual Ubox 100/100 owner traced failed motor detection to a cracked A6 diode feeding the EG3112 gate driver; community advice was to bridge the open pad temporarily or replace the diode outright because the part only filters noise on the 12 V rail.【F:data/vesc_help_group/text_slices/input_part008.txt†L7778-L7795】【F:data/vesc_help_group/text_slices/input_part008.txt†L7813-L7822】

### High-Voltage Battery Ambitions
- Rosheee is pushing a 20s6p G30 past 130 km/h and planning a 26s8p (≈32 Ah, 560–700 A) pack for the GT2, noting overcurrent faults around 320 A on the rear controller and the likely need for external parallel modules to reach 9p while keeping the frame sleeper-clean.【F:data/vesc_help_group/text_slices/input_part008.txt†L7440-L7441】【F:data/vesc_help_group/text_slices/input_part008.txt†L8153-L8164】【F:data/vesc_help_group/text_slices/input_part008.txt†L8175-L8183】

### International Cell Pricing Leads
- ElectricPowa offered bulk Samsung 50E and P42A lots out of Spain for €3.20 and €2.90 respectively, will ship to the United States, and cautioned that logistics may erase the bargain for overseas buyers.【F:data/vesc_help_group/text_slices/input_part008.txt†L7720-L7729】

### SNSC Rental Availability
- Riders in Europe report Segway Ninebot SNSC frames handling well over 200 kg loads and note the SNSC 2.0 chassis is about 1.3 kg heavier than a G30, but US builders struggle to source them outside of occasional auctions or rental fleet sales.【F:data/vesc_help_group/text_slices/input_part008.txt†L8703-L8717】

### Controller Choices for Heavy Scooters
- While Dualtron square-wave controllers will run Vsett 11 motors, experienced builders warn their low PWM frequency runs hotter and lacks regen above 50 % state-of-charge; community advice steers riders toward sinewave alternatives such as Teverun/Kaabo hardware or Spintend’s Ubox 80/150 for 250 A-class performance, with repeated shop failures cited as a reason to avoid Flipsky/Makerbase units on 200 kg builds.【F:data/vesc_help_group/text_slices/input_part008.txt†L8728-L8756】

### Zero 10X Suspension Setup
- Community tuning guidance pegs Zero 10X shocks at 165 mm/1,500 lb in the rear and 135–150 mm/1,500 lb up front, with lighter riders (~70 kg) still preferring stiffer springs for high-speed asphalt stability; heavier racers (~78 kg) report success with 1,250–1,800 lb combinations depending on terrain.【F:data/vesc_help_group/text_slices/input_part008.txt†L9081-L9108】【F:data/vesc_help_group/text_slices/input_part008.txt†L9138-L9144】

### Throttle and Regen Safeguards
- Builders confirm Makerbase 84100 controllers can survive sudden supply disconnects (e.g., an XT60 unplugged at 60 km/h) but still explore fail-safes such as setting maximum throttle voltage in VESC Tool rather than adding pull-down resistors, since ADC adapters cap around 2.1 V output anyway.【F:data/vesc_help_group/text_slices/input_part008.txt†L9113-L9134】
- Regen discussions emphasize keeping battery regen within cell charge specs (≈3 A per cell for 5p packs) and limiting phase braking current to ~70 % of forward phase limits, ramping changes gradually and pairing strong regen with a dedicated throttle to preserve brake pads.【F:data/vesc_help_group/text_slices/input_part008.txt†L9539-L9557】

### Manual Motor Tuning Tips
- When small hub motors auto-detect unusually high inductance on a Ubox Lite 100 V/100 A, riders override the value to ~300 µH (or as low as 150–200 µH) to calm jitter and restore torque, highlighting the need to validate FOC detection results on undersized motors.【F:data/vesc_help_group/text_slices/input_part008.txt†L9308-L9323】

### FarDriver Performance Reports
- A dual FarDriver ND72450 Roadrunner build limited to half of its battery’s capability still pushes 450 A phase, maintains cool motors, and records 32.4 kW peaks with working field-weakening and regen—performance the builder found more effortless than comparable Tronic setups.【F:data/vesc_help_group/text_slices/input_part008.txt†L9328-L9360】

### Brake Hardware Lessons
- A Brakestuff rotor failure after only a handful of races sparked debate: some blame the twin-ring design for uneven heating, others defend the brand but concede the design may need venting revisions to prevent flipping/warping under race heat loads.【F:data/vesc_help_group/text_slices/input_part008.txt†L9470-L9498】
- Zero/Vsett owners tighten wobbly folding clamps by protecting the nuts with a rag and using channel locks—accepting that the joint may no longer fold tool-free once torqued properly.【F:data/vesc_help_group/text_slices/input_part008.txt†L9374-L9380】

### Battery Market Notes
- Bulk-tested EVE 40P samples show 5–7 mΩ internal resistance and cooler operation than P42A cells, making 40P/40PL attractive high-current options when authentic stock is available.【F:data/vesc_help_group/text_slices/input_part008.txt†L9153-L9169】【F:data/vesc_help_group/text_slices/input_part008.txt†L9828-L9834】
- Resellers are clearing welded-but-unused Samsung 50E lots for roughly $0.80 per cell at 2 k unit volumes, while Molicel P42A pulls can land near $1.80 when sourced from decommissioned robot packs.【F:data/vesc_help_group/text_slices/input_part008.txt†L9810-L9823】【F:data/vesc_help_group/text_slices/input_part008.txt†L9802-L9808】

### Long-Distance Touring Logistics
- Long-range Vsett riders plan 125–200 mile weekend routes by chaining J1772 car chargers (via adapters and ~2 kW Huawei supplies), accepting 10 mph average speed including four partial charges and noting Spintend 85/250 controllers stayed cool over 320 km of mixed riding.【F:data/vesc_help_group/text_slices/input_part008.txt†L9650-L9677】【F:data/vesc_help_group/text_slices/input_part008.txt†L10110-L10163】
- A 16s6p Sanyo pack paired with dual Spintend 85/250 controllers delivers roughly 10.8 kW and 54 mph while keeping focus on voltage monitoring rather than full telemetry dashboards.【F:data/vesc_help_group/text_slices/input_part008.txt†L10140-L10161】

### Packaging References
- Builders quoting Zero 10X belly dimensions cite roughly 123 × 32 × 50 cm of internal volume with stock components removed, using the measurement to validate 38 cm-long replacement packs and dual-controller layouts.【F:data/vesc_help_group/text_slices/input_part008.txt†L10094-L10096】

### Miscellaneous Requests
- Racers comparing premium brake setups are searching for silicone potting compounds similar to the factory G30 controller fill to ruggedize aftermarket electronics.【F:data/vesc_help_group/text_slices/input_part008.txt†L9475-L9477】

### Late-July Pack Reinforcement Lessons
- 🇪🇸AYO#74 confirmed that a Nami can swallow a 22s11p pack when an ~8 mm deck riser is added, keeping the profile nearly stock while freeing space for the extra series row.【F:data/vesc_help_group/text_slices/input_part008.txt†L21751-L21757】
- Paolo flagged weak current paths on crimeware’s 20s build and urged doubling the nickel where both parallels meet; the group said their 22s revision uses ~0.60 mm pure nickel reinforcement to stiffen those joints.【F:data/vesc_help_group/text_slices/input_part008.txt†L21765-L21783】

### Firmware & Telemetry Updates
- Rosheee pointed Chris Culver to Vedder’s GitHub and shared the latest `ubox_v2_75.bin` (V31) for Ubox V2 75/100 units after confirming 6.02 is the current public firmware; he also teased paid support for an MKS 84200HP build.【F:data/vesc_help_group/text_slices/input_part008.txt†L21808-L21837】
- NetworkDir published the Dualtron EY2 firmware hex and noted the EY1/EY2/EY4 cluster runs WCH CH582M MCUs that flash via WCHISPStudio, while the Bluetooth-equipped EY variants expose multiple BLE services for accessory dashboards.【F:data/vesc_help_group/text_slices/input_part008.txt†L22147-L22153】
- Oreo huzky demoed a CarPlay install that mirrors VESC telemetry when paired with a jailbroken iPhone or custom Android script, giving riders a higher-visibility dash option.【F:data/vesc_help_group/text_slices/input_part008.txt†L21909-L21916】

### Diagnostics & Controls
- Face de Pin Sucé coached a 5 V short diagnosis—disconnect accessories and trace each lead—before Lekrsu reminded the rider to recalibrate throttle min/max even if the signal flickers.【F:data/vesc_help_group/text_slices/input_part008.txt†L21838-L21845】
- Shlomo shared the Adapter V2 manual and highlighted the target ~0.8 V idle reading so riders stop when they see a 3 V baseline on Spintend’s ADC bridge.【F:data/vesc_help_group/text_slices/input_part008.txt†L21846-L21848】
- Chris Culver is scouting 60–72 V-capable wheel swaps for M365 decks and asked whether sharing ADC1 for throttle and regen still drives the brake light on a Ubox V2 after frying his ADC v2 adapter—open questions for documentation.【F:data/vesc_help_group/text_slices/input_part008.txt†L22198-L22200】

### Kelly Harness & Track Prep Debates
- Medhi Cantin is chasing 10 mm bullet connectors for the Kelly 7230’s doubled phase leads because 4 AWG pairs overfill standard 8 mm bullets; Face de Pin Sucé countered that it’s safer to rewire with slimmer conductors than to force oversized plugs, underscoring the value of right-sizing harnesses instead of brute-force connector swaps.【F:data/vesc_help_group/text_slices/input_part008.txt†L22045-L22049】
- Paolo, NetworkDir, and Yamal reminded Medhi that even “FW” Kelly variants are just field-weakening firmware and still trail modern VESCs with MTPA/FW controls; multiple racers echoed that they’ve migrated from Kelly to dual-VESC stacks for better reliability before returning to the track.【F:data/vesc_help_group/text_slices/input_part008.txt†L21982-L22012】

### Spintend 85/150 Reliability Watch
- Jhonny Nuñez’s 85/150 arrived with a 100 A nameplate, then detonated three input capacitors mid-ride and melted the CAN harness that backfeeds 12 V from the partner controller—he’s pursuing an RMA while the group debates whether the mislabeled units are a downgraded batch.【F:data/vesc_help_group/text_slices/input_part008.txt†L21862-L21874】【F:data/vesc_help_group/text_slices/input_part008.txt†L21902-L21904】

### Brake & Chassis Maintenance
- Yamal’s rear pads wore unevenly because the rotor floats high in the caliper; peers suggested adding spacers and re-centering the clamp before the disc is grooved, reinforcing the need for hardware alignment after aftermarket conversions.【F:data/vesc_help_group/text_slices/input_part008.txt†L22056-L22066】

### Battery Build Setbacks & Plans
- PuneDir scrapped a batch of water-soaked LG M26 cells (20–30 cycles, destined for a 20s20p Puneron pack) rather than risk corrosion-induced failures, while others nudged him toward cleaner stock despite the cost hit.【F:data/vesc_help_group/text_slices/input_part008.txt†L22080-L22100】
- He pivoted to a fresh 20s10p assembly and kept forging ahead with M26 inventory while planning cosmetic Husqvarna bodywork for the build.【F:data/vesc_help_group/text_slices/input_part008.txt†L22156-L22157】【F:data/vesc_help_group/text_slices/input_part008.txt†L22196-L22237】
- PuneDir’s earlier 20 km high-speed shakedown in 37 °C heat shows the M26 pack can survive sustained pulls but deserves active temperature monitoring.【F:data/vesc_help_group/text_slices/input_part008.txt†L21934-L21941】

### Ride Planning & Comfort
- Noname logged a 144 mile Vsett ride (11.5 hours moving time) and spotted 6 mile odometer drift, blaming an incorrect wheel diameter and noting his OEM controller died near 2,400 miles—good prompts to calibrate telemetry before century rides.【F:data/vesc_help_group/text_slices/input_part008.txt†L22118-L22124】
- Haku and Noname reiterated that Alibaba-derived frames can take months to ship and rarely include seat options, complicating long-distance comfort planning.【F:data/vesc_help_group/text_slices/input_part008.txt†L21919-L21933】【F:data/vesc_help_group/text_slices/input_part008.txt†L22223-L22225】

### Thermal Management & Tire Choices
- Mirono noted summer ambient heat forces him to de-rate power or risk rider overheating, favoring 12-FET downsized builds when full leathers aren’t practical.【F:data/vesc_help_group/text_slices/input_part008.txt†L22164-L22176】
- Давно пора is testing 10" PMT slicks against CST stockers on a 19s Inokim setup with a 2 kW Cotycoco controller, resorting to ice packs and ferrofluid to keep the hub alive during races—data that will help set cooling expectations for small motors pushed past 35 A battery limits.【F:data/vesc_help_group/text_slices/input_part008.txt†L22247-L22263】

### Rental Platform & High-Power Build Notes (Lines 14,651–16,150)
- Crimeware’s crash anecdote underscores why SNSC rental frames remain prized for VESC swaps—the scooter wedged a car during impact without bending the chassis, reinforcing the platform’s reputation for overbuilt tubes versus consumer G30 shells.【F:data/vesc_help_group/text_slices/input_part008.txt†L14765-L14796】
- Z P’s SNSC 2.0 build brief shows the power envelope riders target: 84 V packs at ~300 A continuous, with Jan advising dual Spintend 85/250 controllers despite cost because cheaper ESCs are likely to fail long before the frame does.【F:data/vesc_help_group/text_slices/input_part008.txt†L14799-L14807】
- PuneDir is stacking a 20s6p auxiliary pack on a Zero 10X already running a 20s7p internal battery and 84 100 ESCs, illustrating how external bricks plus steering dampers are used to chase more current without gutting the deck layout.【F:data/vesc_help_group/text_slices/input_part008.txt†L15121-L15135】
- Gabe’s 11″ G30 conversion mock-up highlights the structural risks of extended dropouts: drilling new axle holes alters leverage paths, so peers recommend welded U-channel reinforcements or remaining on 10″ PMT tires to keep geometry stable above 120 km/h.【F:data/vesc_help_group/text_slices/input_part008.txt†L15146-L15210】

### Controls, Tires, and Suspension Updates
- Builders swapping moto bars onto scooters pointed PuneDir toward 22 mm full-twist throttles (AliExpress options, Surron assemblies, Domino clones) while warning that motorcycle-style grips feel different when riders stand and shift weight.【F:data/vesc_help_group/text_slices/input_part008.txt†L14832-L14858】【F:data/vesc_help_group/text_slices/input_part008.txt†L14899-L14907】
- PuneDir shared a printable Zero 10X steering-damper mount (Cults3D ZIP) that others thanked for taming high-speed shimmy without bespoke machining.【F:data/vesc_help_group/text_slices/input_part008.txt†L14914-L14918】
- Zero 10X owners debating a 150 mm EXA rear shock and higher field-weakening learned that 60 A battery per motor with 40 A FW delivered 0–50 km/h in ~2.8 s but risks overheating 50 H hubs; community advice is to prioritize phase current and temperature monitoring instead of piling on FW in summer heat.【F:data/vesc_help_group/text_slices/input_part008.txt†L15941-L15975】【F:data/vesc_help_group/text_slices/input_part008.txt†L16115-L16137】
- Tire chatter favored Tuovt 90/55-6 for Zero 10X frames over Xuancheng clones unless mixing PMT slicks/Stradale front and Xuancheng rears, with riders comparing 10″ versus 11″ fitment, rim widths, and wet-weather trade-offs before committing to new rubber.【F:data/vesc_help_group/text_slices/input_part008.txt†L15990-L16038】

### Battery & BMS Insights (June 22–26)
- Zero 10X pack builders canvassed the group for 20s6p BMS options and landed on ANT or JBD smart boards when they need 40 A charging with unrestricted discharge; cheaper Dollatek 20s units exist but are rated closer to 40 A continuous, making them marginal for the requested 60 A draw.【F:data/vesc_help_group/text_slices/input_part008.txt†L15872-L15884】
- PuneDir and Cengiz debated Aspilsan A28 versus LG M26 cells, noting 10–15 A draws push the Turkish cells above 90 °C while LG packs stay nearer 40 °C, so sustained 60 A pack output still demands plenty of parallel strings or higher-grade chemistry.【F:data/vesc_help_group/text_slices/input_part008.txt†L15885-L15938】
- Haku reminded long-range NIU riders that liquidation lots of Samsung 50E/M50LT cells occasionally surface for ~$150 per 11s10p module—cheap bulk sources that could feed 10 kWh conversions if seized before stock disappears.【F:data/vesc_help_group/text_slices/input_part008.txt†L15773-L15799】

### Performance & Safety Highlights
- Teverun 7260R owners continue to snap rear axles—the latest failure reinforces prior warnings that the casting leaves little safety margin for high-torque launches unless riders retrofit stronger hardware.【F:data/vesc_help_group/text_slices/input_part008.txt†L15444-L15559】
- Jhonny Nuñez clocked 118 km/h on dual Spintend 85/150 controllers limited to 80 A battery and 160 A phase, crediting auxiliary fans for keeping MOSFET temps under 20 °C; peers want more telemetry before pitting the setup against Tronic 250 units.【F:data/vesc_help_group/text_slices/input_part008.txt†L16050-L16087】
- Mirono and Shlomozero flagged how 3.6 kW single-drive builds saturate hubs in hot weather: without temp sensors they’re backing off field-weakening or planning AWD conversions to spread load.【F:data/vesc_help_group/text_slices/input_part008.txt†L16099-L16129】
- Long-distance NIU planning remains grueling—Noname’s 140+ mile asylum run requires a 2:1 riding-to-charging ratio with multiple one- to three-hour stops, underscoring the need for faster on-road charging solutions for seated scooters.【F:data/vesc_help_group/text_slices/input_part008.txt†L15756-L15767】

### Early July Safety & Build Updates (Lines 16,151–17,650)
- Copper-strip inflation, 0.37 C fast-charging debates, and a 274 km day ride highlight how long-range riders are juggling budget constraints with endurance charging plans on 90 Ah-class packs.【F:data/vesc_help_group/text_slices/input_part008.txt†L16198-L16266】【F:data/vesc_help_group/text_slices/input_part008.txt†L17160-L17189】
- NAMI builders continue to push boundaries—one mixed LG 40T strings with M50LT add-ons under a 150 A BMS while aiming dual Spintend 85/150 controllers at 130 kg riders—prompting peers to warn about capacity mismatches, hall-cable strain, and moisture-triggered sensor glitches.【F:data/vesc_help_group/text_slices/input_part008.txt†L17040-L17056】【F:data/vesc_help_group/text_slices/input_part008.txt†L17105-L17236】
- PuneDir’s Hyosung-based Puneron now sports a removable belly pan for 20s20p, a 72T rear sprocket, and planned radiator-driven cooling so a Makerbase 84200 can attempt ~200 A battery and 300 A phase once the controller returns to stock.【F:data/vesc_help_group/text_slices/input_part008.txt†L16890-L16900】【F:data/vesc_help_group/text_slices/input_part008.txt†L17248-L17366】
- Dashboard tinkering continues: Spin-Y throttle installs now verify the ADC line stays below ~3.8 V, and 1Zuna dash users are soldering 1 k–1.2 k resistors into the loom to eliminate ghost button presses while keeping compatibility with Makerbase and G30 ESCs.【F:data/vesc_help_group/text_slices/input_part008.txt†L16607-L16619】【F:data/vesc_help_group/text_slices/input_part008.txt†L17098-L17158】
- Tire chatter keeps evolving—Zero/VSETT riders are defaulting to Tuovt 90/55-6 for mixed pavement while leaving softer PMT slicks for smoother courses, and dual-motor builds are leaning on Motor Current Scale plus TC to keep front rubber from vaporizing at 100 A+ launches.【F:data/vesc_help_group/text_slices/input_part008.txt†L17491-L17495】【F:data/vesc_help_group/text_slices/input_part008.txt†L17032-L17039】

### Dash & Regen Lessons (Lines 17,651–19,150)
- Lisa reiterated the dual-brake unlock needed to exit Ninebot “walk/anti-theft” profiles—hold the brake, pin the throttle, and double-tap the dash button—to regain secret mode speed, while the default 6.05 ADC script applies extra field-weakening that keeps the motor pushing until builders trim the `secret-sport` values in Lisp.【F:data/vesc_help_group/text_slices/input_part008.txt†L17730-L17767】【F:data/vesc_help_group/text_slices/input_part008.txt†L17831-L17847】
- Dash-induced hall noise resurfaced: mixing the headlight and brake halls on the same loom droops voltage, so riders are adding the documented GitHub fix—a ~470 Ω resistor plus a small decoupling cap between the 3.3 V and ground rails—and retuning to stop phantom inputs.【F:data/vesc_help_group/text_slices/input_part008.txt†L17818-L17827】
- Happy Giraffe recommended capping regen around −40 A motor/−8 A battery (−15 A only if the pack can take it) on a 20s6p Samsung 32E G30 build, warning that the script’s earlier −65 A target is both harsh on the BMS and responsible for choppy e-brake feel.【F:data/vesc_help_group/text_slices/input_part008.txt†L17912-L17926】
- Veteran builders cautioned that the dual-motor dash script can still “kill you randomly,” advising riders to keep throttle wiring hardwired and treat the display as telemetry until the intermittent cut-outs are solved.【F:data/vesc_help_group/text_slices/input_part008.txt†L18340-L18344】

### Thermal & Controller Experiments
- A fresh Ubox Lite install hit ~70 °C when clamped with a 5 mm pad; Jan and Jason urged switching to the thinnest possible interface or straight thermal paste, citing their own 2–3 kW pulls that stay near ambient when paired with copper plates and quality compounds like Arctic Gel.【F:data/vesc_help_group/text_slices/input_part008.txt†L18030-L18075】
- PuneDir’s stopgap 25 € square-wave controller auto-detects phases via two bridged wires and reportedly packs 100 V FETs, but the group still framed it as a temporary fix beside proven Kelly or VESC hardware.【F:data/vesc_help_group/text_slices/input_part008.txt†L18015-L18037】【F:data/vesc_help_group/text_slices/input_part008.txt†L18956-L18966】
- Mini Spintend users confirmed the aluminum 6-FET board needs at least a 7 s supply, nudging kid-scooter conversions toward higher-voltage brushed ESCs when they want to stay below that threshold.【F:data/vesc_help_group/text_slices/input_part008.txt†L18131-L18140】【F:data/vesc_help_group/text_slices/input_part008.txt†L18261-L18275】

### High-Power Build Notes
- Benur Lgl’s C350-powered scooter now runs dual controllers on a 20s12p 33×2 pack, reports 38.5 kW peaks and 150–160 km/h GPS bursts at ~850 A phase, and relies on a stainless enclosure plus Fun Trott fenders to keep the chassis tidy.【F:data/vesc_help_group/text_slices/input_part008.txt†L17951-L17966】【F:data/vesc_help_group/text_slices/input_part008.txt†L17954-L17958】
- Rage Mechanics previewed a sub-38 kg race build tuned for 20 kW events, underscoring how short stems, dual dampers, and aggressive weight-saving are defining the team’s 2024 lineup.【F:data/vesc_help_group/text_slices/input_part008.txt†L18709-L18710】【F:data/vesc_help_group/text_slices/input_part008.txt†L18949-L18953】
- Yamal’s 200 A field tests on a Nami reinforced that big scooters often run faster and cooler with field-weakening disabled once battery and phase current are properly balanced.【F:data/vesc_help_group/text_slices/input_part008.txt†L18318-L18327】

### Battery & Pack Planning
- Jan measured the G30 deck opening at roughly 119 mm, advising builders to grind ~0.5 mm per side and consider vertical BMS mounting if they chase 22–24 s packs or 12p layouts without external rails.【F:data/vesc_help_group/text_slices/input_part008.txt†L18616-L18654】
- A Turkish seller’s Teverun 7260R listing at €1,200 with a replaced battery sparked interest as a budget 72 V project base, even if the “defective” flag and water-damage history warrant close inspection before purchase.【F:data/vesc_help_group/text_slices/input_part008.txt†L18334-L18338】
- Builders are experimenting with Tenpower 40TG cells—Hackintoshhh pulled 65 A per cell (≈260 A from a 4p block) while citing the 40 A datasheet rating—highlighting the need to log temperatures before embracing them for sustained 150 A packs.【F:data/vesc_help_group/text_slices/input_part008.txt†L19028-L19052】
- LG M26 questions resurfaced alongside 17 s BMS deliveries and copper-strip improvisation, with veterans steering ebike conversions toward ~3 A per cell continuous until testing proves higher limits safe.【F:data/vesc_help_group/text_slices/input_part008.txt†L18688-L18699】【F:data/vesc_help_group/text_slices/input_part008.txt†L18616-L18623】

### Charging & Accessory Notes
- Riders compared adjustable AliExpress chargers capable of 36–84 V and up to 20 A output, flagging the fan noise but keeping them on the shortlist for rapid touring kits.【F:data/vesc_help_group/text_slices/input_part008.txt†L18940-L18945】
- Yamal highlighted the long-running red rental-fleet charger that delivers a realistic 10 A through most BMS boards while teasing quieter, voltage-selectable replacements for future upgrades.【F:data/vesc_help_group/text_slices/input_part008.txt†L18931-L18933】【F:data/vesc_help_group/text_slices/input_part008.txt†L18940-L18943】

### Troubleshooting & Support Alerts
- Makerbase owners reported Bluetooth daughterboards overheating and killing the 3.3 V rail when the antenna tab touched the aluminum case; Thierry recommended checking every supply rail, swapping TX/RX, and escalating to the vendor once the blue LED stays dark.【F:data/vesc_help_group/text_slices/input_part008.txt†L18981-L19011】
- Lonnyo motor shoppers noted shrinking AliExpress availability for US buyers, pushing the community to monitor alternative distributors or stockpile spares before current batches vanish.【F:data/vesc_help_group/text_slices/input_part008.txt†L18979-L18980】

### Late July Updates (Lines 20,261–21,760)

#### Controller Reliability & Selection
- Rogerio’s Makerbase 75100 died after ~2,000 km while cruising at only ~10 A, Lisa reiterated that her 75200 “never worked,” and PuneDir reported a Makerbase board that caught fire while stationary—reinforcing the push toward premium ESCs for anything above commuter power levels.【F:data/vesc_help_group/text_slices/input_part008.txt†L20261-L20267】【F:data/vesc_help_group/text_slices/input_part008.txt†L20512-L20517】【F:data/vesc_help_group/text_slices/input_part008.txt†L21382-L21395】
- NetworkDir steered a Dualtron Victor owner away from Makerbase/Flipsky and toward Spintend’s dual Ubox 100 V/100 A kit plus the ADC v3 lighting module, noting the better thermal behavior and accessory support when targeting ~5 kW per motor.【F:data/vesc_help_group/text_slices/input_part008.txt†L20763-L20786】
- Jason’s MP2 board plans clarify the hardware envelope: six MOSFETs per phase (18 total) rated for ~300 A continuous if current is kept near 100 A per FET, with hardware overcurrent tripping around 450 A—useful context for 30 s conversions weighing MP2 versus Tronic stacks.【F:data/vesc_help_group/text_slices/input_part008.txt†L20788-L20799】
- Builders comparing Spintend offerings concluded the newer 100 V/100 A units run cooler than the purple 75/100x2 versions, and the refreshed aluminum housings offer swap-friendly modules should one side fail.【F:data/vesc_help_group/text_slices/input_part008.txt†L20964-L20977】
- Yamal reminded riders that Little FOCer/Tronic 250 hardware shares a design lineage and stays happy around 150 A per controller, but repeated 200 A pushes “kill” the boards—evidence that even boutique ESCs need current headroom.【F:data/vesc_help_group/text_slices/input_part008.txt†L21370-L21374】
- Gordan’s Surron on a Flipsky 75350 now delivers ~19 kW bursts and steady 15 kW pulls after taming firmware-induced spikes, proving the controller can hang with 80 km/h launches once tuning is dialed.【F:data/vesc_help_group/text_slices/input_part008.txt†L21421-L21436】

#### Battery Engineering & Packaging
- Paolo is TIG-welding a 20s6p Molicel P45B pack, highlighting that high-current scooters still rely on welded copper busbars rather than nickel for low-resistance builds.【F:data/vesc_help_group/text_slices/input_part008.txt†L20698-L20700】
- FrizerSeb’s 20s5p concept with 0.3 mm copper strip was talked down—the community noted the laminate’s weld area is nickel and recommended thinner copper or sandwich welding instead of paying the weight/price penalty.【F:data/vesc_help_group/text_slices/input_part008.txt†L20898-L20916】【F:data/vesc_help_group/text_slices/input_part008.txt†L20943-L20951】
- A teardown of a 24s20p EVE 40PL pack for a Langfeite GT2s exposed 0.15 mm nickel, dual JK 200 A BMS boards, no cell holders, and minimal insulation—serving as a checklist of what to avoid on 7 kWh builds.【F:data/vesc_help_group/text_slices/input_part008.txt†L21517-L21527】
- 🇪🇸AYO#74’s Nami shows 22s11p LG M50LT (242 cells) can fit with a ~8 mm deck riser and honeycomb layout, keeping everything under the stock lid with minimal visual impact.【F:data/vesc_help_group/text_slices/input_part008.txt†L21735-L21757】
- Noname’s NIU commuter now runs the stock 17s35 Ah pack plus a Vsett 16s42 Ah module and an extra 16s21 Ah spare, with the ignition powering lights while a push-button wakes the dual Spintend 85/250 stack.【F:data/vesc_help_group/text_slices/input_part008.txt†L20854-L20860】
- PuneDir is eyeing a 20s6p P42A pack with copper reinforcement for his Zero, acknowledging the frame only fits ~20s7p internally and planning saddlebag add-ons for long trips.【F:data/vesc_help_group/text_slices/input_part008.txt†L21617-L21664】

#### Charging & Long-Range Logistics
- Noname’s 131-mile NIU ride logged ~11 hours on the road and multiple lengthy charging stops, underscoring the need for higher-current roadside solutions for seated scooters.【F:data/vesc_help_group/text_slices/input_part008.txt†L20818-L20833】
- The same rider lean-stacks 30 A Huawei rectifiers for J1772 sessions, recommending the 4875G1 adjustable units (0–100 V, up to 50 A at 220 V) while warning that US 110 V outlets halve the output.【F:data/vesc_help_group/text_slices/input_part008.txt†L21532-L21559】
- Haku and Noname discussed lily-pad charging strategies, with the NIU’s JK BMS trimming charge current above ~10 A on the stock pack—useful for planning dual-pack fast-charge limits.【F:data/vesc_help_group/text_slices/input_part008.txt†L21536-L21544】

#### Vehicle Projects & Fitment Notes
- Builders planning a Vsett 10+ hub swap into a G30 with a Monorim rear end were pointed to the Zero 10X rear bracket/arm kit for a cleaner disc-brake conversion than custom plates.【F:data/vesc_help_group/text_slices/input_part008.txt†L20808-L20831】
- NetworkDir identified the giant 24s20p pack as destined for a Langfeite GT2s, confirming that even rental-style chassis are being stuffed with 7 kWh bricks.【F:data/vesc_help_group/text_slices/input_part008.txt†L21517-L21527】
- 🇪🇸AYO#74 is waiting on motors to finish a Tronic X12-powered build and shared new chassis photos, hinting at more high-voltage Nami experiments in the pipeline.【F:data/vesc_help_group/text_slices/input_part008.txt†L21715-L21738】

#### Safety & Policy Watch
- NYC riders report mounting enforcement against unregistered scooters, EUCs, and gas scooters—motivating some to keep plated mopeds for street use and reserve hot-rodded G30s for paths.【F:data/vesc_help_group/text_slices/input_part008.txt†L21022-L21034】
- A widely shared elevator fire video traced to an e-bike with questionable Ultrafire cells prompted renewed reminders about isolating packs, venting enclosures, and respecting building bans after the rider reportedly died from smoke inhalation.【F:data/vesc_help_group/text_slices/input_part008.txt†L21466-L21490】

#### Troubleshooting & Tuning Tips
- Riders pushing field-weakening found that raising motor phase current from 120 A to 160 A gained another 4–6 km/h after FW caused post-throttle oscillations, a reminder to tune current limits before maxing FW sliders.【F:data/vesc_help_group/text_slices/input_part008.txt†L20758-L20759】
- Dualtron Victor telemetry around 44 A battery draw aligns with the stock 25 A-per-controller design; calibrating JK BMS shunts and switching to VESC hardware were floated as the next steps for more speed with less heat/noise.【F:data/vesc_help_group/text_slices/input_part008.txt†L20763-L20786】
- Spintend Ubox Lite lacks a native 12 V rail, but the ADC v3 adapter happily runs from an external DC-DC—handy for lighting harnesses when upgrading from stock controllers.【F:data/vesc_help_group/text_slices/input_part008.txt†L21040-L21094】
- Matthew’s 18s Spintend 85/150 regen cutout was traced to BMS voltage ceilings; adjusting the BMS cutoff start/end (≈76.6 V) instead of the controller resolved the over-voltage fault.【F:data/vesc_help_group/text_slices/input_part008.txt†L21320-L21347】
- Removing the G30 dash (or at least desoldering the Bluetooth module) noticeably lowers idle draw on VESC-converted Ninebots, helping stretch parked runtime for alarmed builds.【F:data/vesc_help_group/text_slices/input_part008.txt†L21588-L21595】
- Rotatooor confirmed VESC speed reporting continues even without hall sensors—likely via back-EMF estimation—though geared hubs that freewheel off throttle may still need external sensors or GPS for coasting speed readouts.【F:data/vesc_help_group/text_slices/input_part008.txt†L21580-L21608】
- Multiple riders coached Alex through a Spiny Y2 throttle that reboots the controller, suggesting firmware reflashes, BMS checks, motor re-detection, and verifying ADC wiring before suspecting hardware faults.【F:data/vesc_help_group/text_slices/input_part008.txt†L21613-L21706】

### Early August Pack Fabrication & FW Debates (Lines 23,661–23,760 & part009 1,301-1,400)
- Ubox 80/150 owners experimenting with 90–110 A field-weakening under Ortega observers ran into runaway coast when releasing the throttle; peers reiterated that adding series voltage or taller gearing is safer than maxing FW current to chase 86 km/h targets.【F:data/vesc_help_group/text_slices/input_part009.txt†L1309-L1331】
- GABE confirmed a 10s8p internal pack still fits the Xiaomi Pro 2 deck with only a slim spacer and the OEM heatsink when cells are stacked cleanly, but PuneDir warned to leave the supplemental 3s module on its own BMS instead of wiring both bricks to one controller harness.【F:data/vesc_help_group/text_slices/input_part009.txt†L1312-L1323】
- Builders resurfaced copper-laminate handling tips—0.15 mm sheet cuts cleanly by keeping scissors near the pivot and finishing edges with a rubber mallet—reinforcing how to prep busbars without specialized shears.【F:data/vesc_help_group/text_slices/input_part009.txt†L1343-L1352】
- CPU-grade thermal paste remains an acceptable stand-in for controller mounting jobs when boutique compounds are unavailable, provided surfaces are clean before clamping the enclosure.【F:data/vesc_help_group/text_slices/input_part009.txt†L1337-L1338】
- Honeycomb pack makers are pairing hot glue with fishpaper, Kapton, and silicone spacers to hold air gaps between series groups so insulation, not adhesive blobs, carries the structure—plus tape wraps once the battery is closed up.【F:data/vesc_help_group/text_slices/input_part009.txt†L1355-L1384】

## Follow-ups
- Compile a MOSFET selection note comparing Huayi, JJMicro, and Spintend stock devices so racers know which swaps actually survive 200 A+ abuse on 85/150-class controllers.【F:data/vesc_help_group/text_slices/input_part009.txt†L1541-L1554】【F:data/vesc_help_group/text_slices/input_part009.txt†L2491-L2499】
- Document the JBD mobile app’s language inheritance and “softlock” behavior so builders can reliably change balance thresholds without guessing through mistranslated menus.【F:data/vesc_help_group/text_slices/input_part009.txt†L2115-L2137】
- Capture an updated welding safety guide that contrasts Glitter 80x-series spot welders with TIG pulse rigs and spells out precautions for copper stacks so newcomers avoid cell punctures and welder misfires.【F:data/vesc_help_group/text_slices/input_part009.txt†L1801-L1876】【F:data/vesc_help_group/text_slices/input_part009.txt†L1844-L1853】
- Write a Spintend ADC lighting wiring note that covers diode isolation, the high-side brake feed, and sharing the UART header with an M365 dash without breaking light control.【F:data/vesc_help_group/text_slices/input_part009.txt†L46-L95】【F:data/vesc_help_group/text_slices/input_part009.txt†L74-L77】【F:data/vesc_help_group/text_slices/input_part009.txt†L257-L301】
- Draft a buyer checklist for third-party packs so the community can spot loose nickel, missing insulation, and refund dodges like the €270 resale failure before handing over cash.【F:data/vesc_help_group/text_slices/input_part009.txt†L260-L370】
- Capture guidance for running multiple packs/BMS in parallel safely, including how to prevent the cascade failures Noname warned about when one board trips under heavy load.【F:data/vesc_help_group/text_slices/input_part009.txt†L472-L475】
- Build a Flipsky 75200 V2 quick-setup guide that calls out disabling the phase filter, rerunning detection with Mxlemming, and the current limits that keep 20 mΩ hubs from cooking at idle.【F:data/vesc_help_group/text_slices/input_part009.txt†L768-L795】
- Evaluate the AliExpress 20 A charger Yamal sourced so we know whether to recommend it for long tours once field-tested.【F:data/vesc_help_group/text_slices/input_part009.txt†L963-L965】
- Capture any firmware or configuration fixes shared for the Spintend Spinny V2 “full brake on release” fault once a root cause is identified.【F:data/vesc_help_group/text_slices/input_part008.txt†L902-L908】
- Produce a Spiny Y2 throttle troubleshooting guide that walks through ADC wiring, firmware calibration, and BMS checks so riders can stop the controller from rebooting when the lever is pressed.【F:data/vesc_help_group/text_slices/input_part008.txt†L21613-L21706】
- Publish a Ubox Lite accessory-power note showing how to feed Spintend’s ADC v3 adapter from an external DC-DC without ground-loop issues now that more builders are swapping from stock controllers.【F:data/vesc_help_group/text_slices/input_part008.txt†L21040-L21094】
- Track whether the MKSESC 84/200 HP failures receive a definitive manufacturer patch or hardware revision to prevent BMS-cut damage.【F:data/vesc_help_group/text_slices/input_part008.txt†L688-L705】
- Gather detailed wiring photos/layouts for the showcased Zero 10X and Blade motor builds to document successful high-density pack routing.【F:data/vesc_help_group/text_slices/input_part008.txt†L168-L200】【F:data/vesc_help_group/text_slices/input_part008.txt†L1040-L1053】
- Document best practices for Makerbase 84xxx repairs (trace reinforcement, shunt mods, gate driver parts, and static shielding) if the community converges on a reliable rework recipe.【F:data/vesc_help_group/text_slices/input_part008.txt†L1550-L1592】【F:data/vesc_help_group/text_slices/input_part008.txt†L13167-L13174】
- Capture a vetted BMS wiring checklist or diagram that reflects the group’s lessons learned about sequence-sensitive balance lead installation.【F:data/vesc_help_group/text_slices/input_part008.txt†L1980-L2059】
- Revisit Mihail’s LVGL dashboard once the CAN profile management is live and reusable firmware or hardware BOMs are published.【F:data/vesc_help_group/text_slices/input_part008.txt†L2501-L2587】
- Monitor outcomes from the Vsett/Titaone high-speed builds for concrete geometry fixes (trail adjustments, dampers, tire choices) that tame wobble at >80 km/h.【F:data/vesc_help_group/text_slices/input_part008.txt†L3106-L3183】【F:data/vesc_help_group/text_slices/input_part008.txt†L3033-L3056】
- Build a Makerbase 84100 HP current envelope (battery/phase/temperature) so riders stop repeating the 160 A failure seen in Chile and know when to budget for 85/250-class replacements.【F:data/vesc_help_group/text_slices/input_part009.txt†L3010-L3024】
- Document a troubleshooting path for shunt-modded square-wave controllers that cough at mid-speed, outlining the limits of the €25 ESC and when to migrate the Puneron project to FOC hardware.【F:data/vesc_help_group/text_slices/input_part009.txt†L3492-L3524】【F:data/vesc_help_group/text_slices/input_part009.txt†L3826-L3833】
- Publish an ANT BMS wiring crib sheet that highlights the “main ground first” rule and balance-lead order so new pack builders do not short boards during harness assembly.【F:data/vesc_help_group/text_slices/input_part009.txt†L3375-L3387】【F:data/vesc_help_group/text_slices/input_part009.txt†L3834-L3848】
- Capture a Makerbase/Flipsky manual-detection workflow (resistance/inductance measurement tools, sanity ranges) to replace the unreliable auto-tune values that have triggered lockups and crashes.【F:data/vesc_help_group/text_slices/input_part009.txt†L3854-L3867】
- Track high-discharge cell data (Eve 40PL vs. Molicel XA/P45B) so the group can publish an updated drag-racing cell comparison once the new batches ship beyond the waitlist stage.【F:data/vesc_help_group/text_slices/input_part009.txt†L3099-L3124】【F:data/vesc_help_group/text_slices/input_part009.txt†L4407-L4449】
- Compare IP67 Cnlinko LP16 charge ports against the status-quo XT60 installs—wire gauges, mounting footprints, and touring abuse—to recommend a ruggedized connector path for 20 A+ charging.【F:data/vesc_help_group/text_slices/input_part009.txt†L4161-L4169】
- Outline legal/financial paths for Turkish builders facing the €30 import cap so they can source controllers, welders, and packs without 200 % markups or customs seizures.【F:data/vesc_help_group/text_slices/input_part009.txt†L4218-L4237】
- Evaluate the €25 purple-PCB spot welder with capacitor banks (or alternative 12 V kits) so customs-limited builders have a repeatable solution that matches 0.2 mm nickel performance without hauling car batteries indoors.【F:data/vesc_help_group/text_slices/input_part009.txt†L4259-L4274】
- Draft a test plan comparing 100 V-upgraded Ubox 85/150s against Tronic X12 controllers (thermal rise, sustained phase current, CAN behavior) once hardware is on track for circuit laps.【F:data/vesc_help_group/text_slices/input_part009.txt†L4431-L4437】【F:data/vesc_help_group/text_slices/input_part009.txt†L4494-L4498】
- Follow up on MP2 ABS overcurrent troubleshooting once firmware fixes or configuration guides emerge for 200 A+ setups.【F:data/vesc_help_group/text_slices/input_part008.txt†L4913-L4920】【F:data/vesc_help_group/text_slices/input_part008.txt†L5250-L5258】
- Capture PuneRon’s finalized water-cooling layout and sprocket machining notes once the steel gear set is tested above 200 A.【F:data/vesc_help_group/text_slices/input_part008.txt†L4791-L4858】【F:data/vesc_help_group/text_slices/input_part008.txt†L5387-L5403】
- Log proven resistor values or harness diagrams for reusing Xiaomi Pro 2 lighting with dual VESC conversions so future builders avoid LED failures.【F:data/vesc_help_group/text_slices/input_part008.txt†L5032-L5045】
- Document safe bring-up procedures for Fiido L3 packs when pairing them with higher-voltage VESC controllers so the BMS isn’t shocked by charged input caps.【F:data/vesc_help_group/text_slices/input_part008.txt†L5858-L5875】
- Track fixes or configuration advice for 1Zuna’s dual-controller dash scripts so both motors respect speed caps on Ninebot builds.【F:data/vesc_help_group/text_slices/input_part008.txt†L6023-L6030】【F:data/vesc_help_group/text_slices/input_part008.txt†L6244-L6248】
- Capture detailed wiring diagrams for Makerbase ignition/EN pin mods (including resistor divider values) to simplify future regulator integrations.【F:data/vesc_help_group/text_slices/input_part008.txt†L6460-L6464】
- Verify practical G30 deck layouts beyond ~120 internal cells and note any spacer/fork patterns that successfully house 20s≥10p modules without compromising handling.【F:data/vesc_help_group/text_slices/input_part008.txt†L6550-L6561】【F:data/vesc_help_group/text_slices/input_part008.txt†L7087-L7137】
- Publish reinforcement guidance for extended G30/SNSC dropouts when fitting 11″ motors so builders know when to weld versus bolt-on arms.【F:data/vesc_help_group/text_slices/input_part008.txt†L15146-L15210】
- Summarize reliable paths for sourcing/compiling 3Shul firmware (including the shared Drive repo) and collect field data on which 3Shul/C350 variants hold up at 22s with and without regen.【F:data/vesc_help_group/text_slices/input_part008.txt†L7189-L7213】【F:data/vesc_help_group/text_slices/input_part008.txt†L7300-L7309】
- Document a repeatable repair guide for Tronic 250 CAN-bus failures, including replacement transceivers and safe throttle sharing practices while parts are on order.【F:data/vesc_help_group/text_slices/input_part008.txt†L7565-L7588】
- Capture a wiring note for low-cost MF52B/MF52D thermistors (pinouts, potting, routing) so builders can confidently add motor temperature sensing.【F:data/vesc_help_group/text_slices/input_part008.txt†L7445-L7461】
- Record EG3112 gate-driver supply fixes for Ubox 100/100 controllers—bridging versus diode replacement—and confirm long-term reliability once repairs are tested.【F:data/vesc_help_group/text_slices/input_part008.txt†L7778-L7795】【F:data/vesc_help_group/text_slices/input_part008.txt†L7813-L7822】
- Track Rosheee’s forthcoming GT2 26s8p testing for overcurrent fixes, cooling upgrades, and any structural changes needed to house external parallel modules cleanly.【F:data/vesc_help_group/text_slices/input_part008.txt†L8153-L8164】【F:data/vesc_help_group/text_slices/input_part008.txt†L8175-L8183】
- Map reliable SNSC 2.0 sourcing channels (auctions, fleet resale programs, EU distributors) for builders outside Europe who are trying to obtain the heavier-duty rental frames.【F:data/vesc_help_group/text_slices/input_part008.txt†L8703-L8717】
- Compile a Zero 10X spring guide that ties rider weight to proven 135–165 mm shock options and lists suppliers for the 1,250–2,000 lb coils riders recommend.【F:data/vesc_help_group/text_slices/input_part008.txt†L9081-L9108】【F:data/vesc_help_group/text_slices/input_part008.txt†L9138-L9144】
- Capture a regen setup playbook covering battery/phase current limits, dedicated throttle wiring, and firmware settings that reflect the group’s latest best practices.【F:data/vesc_help_group/text_slices/input_part008.txt†L9539-L9557】
- Follow up on the Brakestuff rotor incident to document root cause, revised designs, or alternative race-ready discs that avoid flipping/warping under heat.【F:data/vesc_help_group/text_slices/input_part008.txt†L9470-L9498】
- Document proven field kits for J1772-based scooter charging (adapter part numbers, portable chargers, and route-planning tips) used on 100 + mile rides.【F:data/vesc_help_group/text_slices/input_part008.txt†L9650-L9677】
- Draft a Kelly 7230 harness guide that balances wire gauge, bullet-connector sizing, and strain relief so doubled phase leads don’t outgrow 8 mm hardware.【F:data/vesc_help_group/text_slices/input_part008.txt†L22045-L22049】
- Identify silicone potting compounds and application techniques that mimic the OEM G30 controller encapsulant for aftermarket electronics hardening.【F:data/vesc_help_group/text_slices/input_part008.txt†L9475-L9477】
- Capture Spintend mounting best practices (plate thickness, thermal paste, corrosion barriers) for the aluminum 6-FET units before more riders bolt them straight to mixed metals.【F:data/vesc_help_group/text_slices/input_part008.txt†L10241-L10253】
- Compile a 20s6p BMS cheat sheet (ANT vs. JBD vs. Dollatek) that clarifies continuous and peak current limits for Zero 10X-class builds drawing ~60 A.【F:data/vesc_help_group/text_slices/input_part008.txt†L15872-L15884】
- Publish a quick reference for disabling a front motor mid-ride via Spintend’s ADC adapter or the VESC UART `setCurrent` Arduino sketch, including wiring, supply voltage, and firmware settings.【F:data/vesc_help_group/text_slices/input_part008.txt†L11488-L11502】
- Compare mid-priced spot welders (Docreate DO-02, foot-pedal variants, Glitter 801D) for 0.1–0.2 mm nickel work so pack builders can pick reliable equipment within a $60–$120 budget.【F:data/vesc_help_group/text_slices/input_part008.txt†L11290-L11337】【F:data/vesc_help_group/text_slices/input_part008.txt†L11517-L11520】
- Validate mini Spintend current ceilings and thermal behavior around the suggested 150 A phase limit before recommending it for 20 kW builds.【F:data/vesc_help_group/text_slices/input_part008.txt†L11288-L11311】【F:data/vesc_help_group/text_slices/input_part008.txt†L11294-L11296】
- Publish a Vsett 10+ harness pinout and accessory reuse guide so Spintend/Ubox swaps can retain lights and controls without guesswork.【F:data/vesc_help_group/text_slices/input_part008.txt†L12075-L12079】
- Capture a dual/single motor toggle workflow that keeps CAN traction control alive—whether via Lisp scripting or logic switches—to avoid the trade-offs seen with standalone ADC adapters.【F:data/vesc_help_group/text_slices/input_part008.txt†L12459-L12566】
- Document a hall-sensor diagnostic checklist for Lonnyo/Spintend builds when detection suddenly fails despite controller swaps.【F:data/vesc_help_group/text_slices/input_part008.txt†L12462-L12471】
- Research drop-in 10" high-torque motors and temperature-sensor upgrades suitable for Nami Klima 72 V conversions before riders commit to wheelie-focused packs.【F:data/vesc_help_group/text_slices/input_part008.txt†L12510-L12537】
- Track field data from SEVEN’s TOLL/TOLT controllers and CNC throttle once testers publish logs or release dates.【F:data/vesc_help_group/text_slices/input_part008.txt†L14004-L14020】
- Gather telemetry logs that compare dual Spintend 85/150 setups with Tronic 250 controllers once testers share more than peak-speed screenshots.【F:data/vesc_help_group/text_slices/input_part008.txt†L16050-L16087】
- Capture a safe workflow for lifting the Ubox 85/150 warranty limits (130 A phase/180 A absolute) without voiding coverage or bricking the controller.【F:data/vesc_help_group/text_slices/input_part008.txt†L13486-L13490】
- Gather wiring diagrams for multi-BMS pack layouts now that riders are paralleling three boards on 20s24p builds.【F:data/vesc_help_group/text_slices/input_part008.txt†L13914-L13920】
- Capture remediation steps for the Langfeite GT2s 24s20p pack (cell holders, insulation, busbar upgrades) before more builders copy the risky 0.15 mm-nickel layout.【F:data/vesc_help_group/text_slices/input_part008.txt†L21517-L21527】
- Log Tuovt 90/55-6 wet-weather performance and long-term wear data as more riders report back.【F:data/vesc_help_group/text_slices/input_part008.txt†L13397-L13435】
- Source printable Vsett 9 rim liners or other proven pinch-flat mitigations for split rims once a design emerges.【F:data/vesc_help_group/text_slices/input_part008.txt†L14628-L14637】
- Document NIU fast-charging harnesses (ports, wire gauge, protections) for VESC-converted mopeds tapping 30 A+ J1772 stations.【F:data/vesc_help_group/text_slices/input_part008.txt†L13822-L13826】
- Track whether Teverun 7260R owners identify durable replacement axles or frame reinforcements after repeated breakages.【F:data/vesc_help_group/text_slices/input_part008.txt†L15444-L15559】
- Publish a throttle-signal safety checklist that walks builders through measuring Spin-Y/analog inputs before connection so controller ADC pins never see more than ~3.8 V.【F:data/vesc_help_group/text_slices/input_part008.txt†L16607-L16619】
- Capture hall-harness strain-relief or diagnostic steps that prevent ABS overcurrent faults triggered by loose sensor looms.【F:data/vesc_help_group/text_slices/input_part008.txt†L16552-L16556】
- Summarize lessons learned from mixed-chemistry NAMI packs (LG 40T plus M50LT add-ons) so future builds understand safe discharge limits, balancing strategies, and why many riders still discourage blending 4 Ah and 5 Ah cells in one parallel group.【F:data/vesc_help_group/text_slices/input_part008.txt†L17040-L17156】【F:data/vesc_help_group/text_slices/input_part008.txt†L17194-L17199】
- Document 🇪🇸AYO#74’s 22s11p Nami deck layout (honeycomb pattern, ~8 mm riser, wiring channels) so others can replicate the 242-cell fitment without guessing clearances.【F:data/vesc_help_group/text_slices/input_part008.txt†L21735-L21757】
- Track Medhi Cantin’s Kelly-vs-VESC racetrack data once his scooter is buttoned up to quantify any gap versus modern dual-VESC builds.【F:data/vesc_help_group/text_slices/input_part008.txt†L21982-L22012】
- Verify real-world Makerbase 84200 availability and current ceilings—especially for water-cooled installs targeting 200 A battery and 300 A phase—before endorsing it as a Puneron upgrade path.【F:data/vesc_help_group/text_slices/input_part008.txt†L17288-L17366】
- Capture a reproducible fix or mitigation for the dual-motor dash script cut-out so riders can safely use the G30 secret-mode display without random throttle loss.【F:data/vesc_help_group/text_slices/input_part008.txt†L18340-L18344】
- Log thermal/voltage data from Tenpower 40TG packs when pulling 200 A+ so the community knows whether the cells survive sustained 40–65 A per cell use cases.【F:data/vesc_help_group/text_slices/input_part008.txt†L19028-L19052】
- Document repair steps for Makerbase Bluetooth daughterboards that overheat and collapse the 3.3 V rail when the antenna contacts the lid.【F:data/vesc_help_group/text_slices/input_part008.txt†L18981-L19011】
- Benchmark the adjustable 20 A AliExpress chargers for noise, accuracy, and longevity before adding them to the recommended touring kit list.【F:data/vesc_help_group/text_slices/input_part008.txt†L18940-L18945】
- Track whether Spintend clarifies the 85/150 “100 A” nameplate and CAN backfeed failure root cause, and document any retrofit parts before riders parallel the controllers again.【F:data/vesc_help_group/text_slices/input_part008.txt†L21862-L21874】【F:data/vesc_help_group/text_slices/input_part008.txt†L21902-L21904】
- Draft an Adapter V2 throttle-calibration guide that highlights the expected ~0.8 V idle, wiring order, and troubleshooting steps when riders read 3 V baselines on the ADC bridge.【F:data/vesc_help_group/text_slices/input_part008.txt†L21846-L21848】
- Add a brake-alignment checklist covering rotor spacing, washer stacks, and pad wear diagnostics for rear conversions like Yamal’s uneven caliper setup.【F:data/vesc_help_group/text_slices/input_part008.txt†L22056-L22066】
- Publish a Vsett odometer calibration note (wheel circumference math plus firmware menus) so 100+ mile riders stop seeing 5–10 % distance drift after controller swaps.【F:data/vesc_help_group/text_slices/input_part008.txt†L22118-L22124】
- Document the Dualtron EY1/EY2/EY4 flashing workflow (CH582M drivers, WCHISPStudio steps, BLE service map) for riders experimenting with custom dashboards.【F:data/vesc_help_group/text_slices/input_part008.txt†L22147-L22153】
- Collect thermal data and mitigation tips for 10″ PMT race setups on small hubs—including ferrofluid volumes and between-heat cooldown tactics—to prevent the ice-pack scramble described by Давно пора.【F:data/vesc_help_group/text_slices/input_part008.txt†L22247-L22263】
