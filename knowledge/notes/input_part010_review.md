# input_part010.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part010.txt`
- Coverage: 2024-10-10 12:51:46 through 2024-10-27 21:20:42 (lines 1-6700)
- Next starting point: line 6701 (2024-10-27T21:20:XX and later)

## Key Findings

### High-Voltage Thunder/LY Build Planning
- Andrei and Yamal compared LY Thunder swingarm conversions using 75H–90H hub motors; Yamal prefers 75/80H cans because the 90H integrates the rim, complicating service, while Andrei is targeting a 24S pack on 80H motors and wide (≈90 mm) rims for top-speed testing on a private 10 km straight.【F:data/vesc_help_group/text_slices/input_part010.txt†L12-L89】
- The same project confirmed 24S/9P Molicel P45 cells due to enclosure limits, with peers curious about achievable top speed versus rim width drag.【F:data/vesc_help_group/text_slices/input_part010.txt†L41-L83】

### Tire Fitment & Traction Notes
- China PMT “Stradale” tires have held up ~2 months on Thunder arms; Andrei shared an AliExpress link for 100/55-6.5 tubeless tires (≈RON 132) while others warned 90/65-6 rubber may rub mantis/Zero 10 mudguards and calipers.【F:data/vesc_help_group/text_slices/input_part010.txt†L97-L130】
- AYO#74’s race scooter is on dual 33×2 inch, 70H motors with 150 A front / 200 A rear phase limits; the front still spins at ~133 km/h, highlighting the need for traction management before adding more current.【F:data/vesc_help_group/text_slices/input_part010.txt†L418-L436】

### Battery Construction Practices
- NetworkDir commissioned a 24S 20P pack of Samsung 40PL cells for ~40 kW peaks; the builder noted external case temps stay near 50 °C but needs embedded NTC sensors to confirm internal heat and avoid overstressing rewound 70H/90H motors.【F:data/vesc_help_group/text_slices/input_part010.txt†L320-L355】【F:data/vesc_help_group/text_slices/input_part010.txt†L349-L357】
- Jan recommended insulated flat copper bus bars and mindful cable routing because double-decker 21700 layouts leave little headroom for conductors, especially when mounting Seven VESCs inside Ninebot G30 decks.【F:data/vesc_help_group/text_slices/input_part010.txt†L377-L395】
- Gabe’s experience with an 801D spot welder shows that re-welding the same location can crater Molicel cans, effectively scrapping ~€70 of cells; he now plans to leave previous copper in place or replace the affected cells outright.【F:data/vesc_help_group/text_slices/input_part010.txt†L117-L118】【F:data/vesc_help_group/text_slices/input_part010.txt†L434-L439】【F:data/vesc_help_group/text_slices/input_part010.txt†L456-L464】

### ES3 Folding Pack Build & Safety Lessons
- Haku documented folding a “world’s fastest ES3” battery: the folded busbars require Kapton/fish paper and epoxy plates between layers plus attention to balance lead spacing to avoid shorts; Noname advised using insulating board before bending and spacing paper to prevent balance wire chafing.【F:data/vesc_help_group/text_slices/input_part010.txt†L606-L690】
- The completed 20S12P pack fit a printed enclosure, but Haku noted BMS wiring congestion and plans for crimped parallel leads once tools arrive, highlighting the need for strain relief and routing room in compact builds.【F:data/vesc_help_group/text_slices/input_part010.txt†L876-L958】【F:data/vesc_help_group/text_slices/input_part010.txt†L1356-L1444】
- A later QS8 connector short caused a burn and molten copper splash, reinforcing the importance of de-energizing packs during connector work and wearing PPE; peers recommended covering wounds immediately and reducing BMS output current before handling leads.【F:data/vesc_help_group/text_slices/input_part010.txt†L1484-L1588】

### Vehicle Incidents & Component Durability
- PuneDir’s ~70 km/h collision with a car bent the Zero 10X extender, damper, and handlebar but left the frame serviceable; protective gear prevented injury, and replacement extender parts are inexpensive but 3D-printed pieces may warrant aluminum upgrades for resilience.【F:data/vesc_help_group/text_slices/input_part010.txt†L706-L812】【F:data/vesc_help_group/text_slices/input_part010.txt†L1326-L1386】
- Subsequent inspection showed the Zero chassis largely intact, supporting community claims that the platform can survive mid-speed crashes if structural components (stem, fork bolts) are inspected and replaced as needed.【F:data/vesc_help_group/text_slices/input_part010.txt†L874-L1016】

### Instrumentation & Firmware Tooling
- NetworkDir’s ESP32-based Simple VESC Display (SVD) was ported to the ESP32-2432S028R touchscreen, with offers to help others flash firmware over UART and future CAN bus support; components sourced via AliExpress include the display, wiring harness, and open-source code.【F:data/vesc_help_group/text_slices/input_part010.txt†L1186-L1281】
- Jerome (St0fzuiger) built a DIY VESC Express logger, documenting that the ESP32-C3 Mini’s SPI pins are remapped in VESC firmware and sharing part links (SD reader, CAN transceiver, GPS). He also wrote an expanded Lisp script (“FullLog_Express.lisp”) to log additional CAN data and clarified CAN bus daisy-chaining for dual controllers.【F:data/vesc_help_group/text_slices/input_part010.txt†L1880-L2099】【F:data/vesc_help_group/text_slices/input_part010.txt†L2140-L2267】
- Patrick continued reporting macOS VESC Tool 6.0.5 connection crashes (works on iOS/Android/Windows), underscoring an unresolved regression for Apple Silicon users.【F:data/vesc_help_group/text_slices/input_part010.txt†L1048-L1055】【F:data/vesc_help_group/text_slices/input_part010.txt†L1996-L2004】

### Controller & Powertrain Planning
- Multiple builders debated controller options: Yamal is targeting 22S11P Samsung packs with dual Ubox 85/250 or Seven controllers in Dualtron Thunder/NAMI frames but highlighted enclosure length limits (~51.8 cm) and elevator constraints, prompting custom box or longer-frame considerations.【F:data/vesc_help_group/text_slices/input_part010.txt†L2008-L2190】【F:data/vesc_help_group/text_slices/input_part010.txt†L2248-L2364】
- Discussions compared Fardriver, Tronic, NUCC, and Spintend controllers; consensus favored VESC ecosystem for customization despite higher cost, while acknowledging Fardriver’s size and paid firmware updates as trade-offs.【F:data/vesc_help_group/text_slices/input_part010.txt†L1684-L1788】【F:data/vesc_help_group/text_slices/input_part010.txt†L1824-L1910】
- Matthew reported a Spintend Ubox 85150 failure on a 16S7P + 2S6P setup (field weakening 80%, 120 A fuse) after epoxy-mounting the controller to the frame, with community suggestions to inspect for BMS cuts, gather photos, and avoid permanent mounting without service access.【F:data/vesc_help_group/text_slices/input_part010.txt†L2336-L2409】【F:data/vesc_help_group/text_slices/input_part010.txt†L2409-L2455】

### Supply Chain & Component Notes
- EU riders discussed sourcing high-discharge cells: Molicel P42/P45 availability is constrained with long waitlists, pushing builders toward Samsung 40PL or alternative vendors (Miro, Finn, James) for bulk orders.【F:data/vesc_help_group/text_slices/input_part010.txt†L1376-L1436】
- AliExpress links circulated for QS8 connectors, CNC rims, ESP32 displays, and 3D-printed Zero folding kit upgrades, reflecting reliance on Chinese suppliers but with caution about communication delays and customs limitations in regions like Israel and Turkey.【F:data/vesc_help_group/text_slices/input_part010.txt†L934-L1016】【F:data/vesc_help_group/text_slices/input_part010.txt†L2054-L2165】【F:data/vesc_help_group/text_slices/input_part010.txt†L2212-L2304】

### Controller & Tooling Insights
- Patrick’s 30S 6P 40PL Ninebot G30 project fits ANT 850 A peak or Seven VESC controllers under the deck; Seven’s centered battery terminals free space for heavy-gauge cabling compared with 85250 ESCs.【F:data/vesc_help_group/text_slices/input_part010.txt†L180-L385】
- VESC Tool 6.0.5 crashes on macOS (M2) whenever Patrick attempts Bluetooth or TCP connections, even after a full OS restore, implying a software regression that needs upstream reporting or reverting to a prior release.【F:data/vesc_help_group/text_slices/input_part010.txt†L408-L416】
- Standard 4 mm phase leads on 60H-class motors are reportedly safe to ~180 A; Yamal cautions that exceeding 200 A invites failures, reinforcing the push to upsize leads when targeting race-level phase currents.【F:data/vesc_help_group/text_slices/input_part010.txt†L472-L495】

### Segway GT VESC Conversions & Cooling Support (Lines 2701-3090)
- Jerome’s GT1D “Golden Shower Power” build now runs GT2 hub motors with dual 85/150 VESCs and a 19S9P EVE 50E pack, holding factory dash/buttons via drop-in wiring bridges; he is shepherding EU/US group buys so others can replicate the swap without cutting harnesses.【F:data/vesc_help_group/text_slices/input_part010.txt†L2701-L2738】
- Jan released a printable radiator and spacer kit for GT2 cockpits, and Jerome noted each conversion is dialed for ~6 kW per motor today with ambitions to push 26S (≈27 kW peaks), underscoring the need for added cooling when stepping beyond 19S.【F:data/vesc_help_group/text_slices/input_part010.txt†L2739-L2763】

### GT2 Motor Rewinds & Pack Packaging Options (Lines 2773-2860)
- Kirill rewinds GT2 stators with ≈6 mm² copper, ≈8 mm² phase leads, upgraded magnets, and Statorade to survive 22S setups; his demo runs 22S8P P42A packs, and he confirmed the chassis can host ~200 cells (e.g., 28S7P 21700s or 14S14P 5.5 Ah layouts) if insulation space is reserved.【F:data/vesc_help_group/text_slices/input_part010.txt†L2773-L2794】
- Builders reaffirmed that VESC swaps can retain OEM lighting/dash by isolating motor connectors while hall/phase mapping stays stock, making reversions easy if needed.【F:data/vesc_help_group/text_slices/input_part010.txt†L2714-L2738】【F:data/vesc_help_group/text_slices/input_part010.txt†L3320-L3334】

### Race Scooter Power & Traction Lessons (Lines 2801-3560)
- AYO#74’s Dualtron racer deploys 22S11P Molicel P45 modules (~92 V) and dual controllers for ~50 kW peaks, but a broken CAN harness forces standalone VESCs without traction control, letting the front 33×2 70H spin during 139 km/h GPS pulls; he trusts a 420 A/1020 A ANT BMS to absorb bursts.【F:data/vesc_help_group/text_slices/input_part010.txt†L2801-L2856】【F:data/vesc_help_group/text_slices/input_part010.txt†L3408-L3485】
- NetworkDir and Lekrsu advised backing up configs, disabling MTPA on e-scooter hubs, and matching motor detection parameters per controller when CAN sync is down to avoid asymmetrical torque limits.【F:data/vesc_help_group/text_slices/input_part010.txt†L2760-L2800】【F:data/vesc_help_group/text_slices/input_part010.txt†L3320-L3334】【F:data/vesc_help_group/text_slices/input_part010.txt†L3490-L3574】

### Lead-Acid Scooter Conversion Plans (Lines 2705-3478)
- PuneDir’s 48 V lead-acid scooter weighs ~80 kg and uses ethernet cable for phase wiring, motivating a full tear-down, rewire, and 23S/20 kW VESC conversion before chasing speed; peers flagged the stock components as unfit for >100 A discharge.【F:data/vesc_help_group/text_slices/input_part010.txt†L2705-L2709】【F:data/vesc_help_group/text_slices/input_part010.txt†L2764-L2772】【F:data/vesc_help_group/text_slices/input_part010.txt†L3451-L3478】

### Wiring & Component Upgrades (Lines 3320-3778)
- Patrick received 10 mm² silver-plated motor leads in fiberglass sleeves (≈5.5 mm OD after stripping a layer) to replace LY phases, accepting minor machining to route the thicker cable because the quality outweighed the vendor’s mis-ship of the larger gauge.【F:data/vesc_help_group/text_slices/input_part010.txt†L3451-L3464】【F:data/vesc_help_group/text_slices/input_part010.txt†L3478-L3510】
- Ongoing reminders from Haku, NetworkDir, and others emphasized locking axle hardware, ziptie-managing phase exits, and logging rides before raising phase current beyond ~300 A so regen limits and thermal cutoffs stay in sync across dual controllers.【F:data/vesc_help_group/text_slices/input_part010.txt†L3320-L3574】【F:data/vesc_help_group/text_slices/input_part010.txt†L3610-L3689】

### Seated Mini-Bike Tuning & Thermal Management (Lines 3520-4115)
- Haku’s dual LY 70H (33×2) minibike went from sluggish to “bucks me off” after lifting phase limits to 280–300 A (ABS 360–390 A, battery 250 A) on a 12P P42A/575 A BMS pack, but short pulls already raise stator temps toward 67 °C, so he’s adopting mxlemming observers, temp cutoffs (~85 °C), and data logging to balance torque and heat.【F:data/vesc_help_group/text_slices/input_part010.txt†L3520-L3689】【F:data/vesc_help_group/text_slices/input_part010.txt†L3690-L3710】
- The build still needs brake alignments, thicker rotors, lighting, and phase harness cleanup; he’s also exploring 30S upgrades, Statorade, and parallel 40T packs while tracking voltage sag (82 V→76 V) during aggressive launches.【F:data/vesc_help_group/text_slices/input_part010.txt†L3590-L3839】【F:data/vesc_help_group/text_slices/input_part010.txt†L3850-L4115】

### Brake Rotor Upgrades & Lighting Reminders (Lines 4201-4360)
- Haku’s noisy caliper led to a rotor health check: stock 2 mm discs wear quickly under Magura pads, so Yamal pointed him to 3 mm Galfer-style 160 mm rotors (≈€30) but warned that fixed spacers limit flipping directionally slotted rotors, reinforcing the need to verify caliper clearance before swapping.【F:data/vesc_help_group/text_slices/input_part010.txt†L4257-L4284】
- The same chat highlighted the lack of OEM lighting on his minibike; Yamal urged wiring headlights instead of riding dark, underscoring that nighttime testing should include auxiliary lighting for safety.【F:data/vesc_help_group/text_slices/input_part010.txt†L4305-L4308】

### Emerging Motor Options & Pricing Checks (Lines 4320-4388 & 4840-4889)
- Sotion’s 72 V “H02” 10 kW hub kit (with optional swingarm) resurfaced as an off-the-shelf upgrade for Razor minibikes, though Noname noted missing magnet specs and ~1500–2500 rpm rating differences compared with LY 70H hubs; builders want third-party testing before adopting it over known LY units.【F:data/vesc_help_group/text_slices/input_part010.txt†L4320-L4346】
- PuneDir is still searching for a sturdier motor (≥60H) for his lead-acid moto conversion, prompting offers of 50H spares and advice to overvolt the existing 27 mm stator carefully while watching temps to avoid burning it up.【F:data/vesc_help_group/text_slices/input_part010.txt†L4339-L4388】
- Andrei Albert confirmed his swingarm build will pair dual 80H hubs with a 24S9P Molicel P45 pack and 3Shul controller, keeping only the battery and step-downs in the deck—useful packaging context for others attempting full 24S conversions.【F:data/vesc_help_group/text_slices/input_part010.txt†L4854-L4873】

### Zero 10X Field-Weakening Debate & FW Alternatives (Lines 4397-4480)
- Shlomozero10’s Zero 10X lost ≈7 km/h of top speed after raising phase current to 100 A and field weakening (FW) to 60 A per controller; peers suggested testing without FW, trying higher voltage (20S) instead, and tracking Wh/km plus motor temps because 60 A FW severely stresses 50H hubs on 16S packs.【F:data/vesc_help_group/text_slices/input_part010.txt†L4397-L4480】
- FreehandZ calculated that the existing 30 Kv hubs and 16S battery cap theoretical speed near 82 km/h at nominal voltage, so chasing 100 km/h safely likely requires more series cells rather than heavier FW settings.【F:data/vesc_help_group/text_slices/input_part010.txt†L4451-L4480】

### World-Record GT Insights & Instrumentation (Lines 4487-4562)
- Pandalgns is iterating new housings for NetworkDir’s Simple VESC Display, while Face de Pin Sucé shared RAFTOR’s 173 km/h Dragy run, noting they custom-built the motors and still rely on wheel-speed calculations for the dash because GPS drops in tunnels—pointing to demand for higher-rate GPS logging on high-speed builds.【F:data/vesc_help_group/text_slices/input_part010.txt†L4487-L4562】

### Profile Management & Tooling Tips (Lines 4557-4813)
- Haku discovered that reusing identical Spintend Bluetooth modules lets his son’s profile overwrite his own settings; Давно Пора advised isolating power or phones when swapping profiles to avoid accidentally unleashing adult power levels on a kid’s scooter.【F:data/vesc_help_group/text_slices/input_part010.txt†L4557-L4595】
- Noname walked him through using a bolt extractor or Dremel slot to remove a rounded ES3 stem bolt without drilling into the battery bay, highlighting best practices for tight quarters around live packs.【F:data/vesc_help_group/text_slices/input_part010.txt†L4802-L4813】

### Minibike Thermal Limits & Controller Settings (Lines 4672-4751 & 5027-5090)
- Repeated 20 kW pulls pushed Haku’s 33×2 minibike motors to the VESC’s 85 °C thermal cutoff, prompting NetworkDir to recommend ferrofluid and increasing zero-vector frequency to ~35 kHz (Motor Config → FOC → Advanced) to trade a bit of torque for lower motor heating; they also reminded him to confirm BMS current limits if he expects 40 kW peaks.【F:data/vesc_help_group/text_slices/input_part010.txt†L4672-L4728】
- NetworkDir cautioned that MTPA tuning performs poorly on high-Kv hubs, favoring low-Kv motors plus higher pack voltage when seeking both acceleration and efficiency—a datapoint for future tuning guides.【F:data/vesc_help_group/text_slices/input_part010.txt†L4743-L4751】
- Haku’s subsequent highway shakedown on the “wepoor” minibike hit ~65 mph (≈24 kW) before temps rose, with 4 kWh of battery delivering ~40 miles when cruising 50–65 mph; he plans ferrofluid and a parallel Samsung 40T pack to chase 80 mph runs once cooling is improved.【F:data/vesc_help_group/text_slices/input_part010.txt†L5027-L5090】

### Lead-Acid Moped Conversion & External Pack Wiring (Lines 5201-5352)
- PuneDir’s lead-acid moto peaks at ~27 mph with a 27H hub and 48 V/20 Ah SLA pack; he’s eyeing a 20S 60 Ah two-layer battery and VESC swap but dreads the fabrication workload.【F:data/vesc_help_group/text_slices/input_part010.txt†L5201-L5223】【F:data/vesc_help_group/text_slices/input_part010.txt†L5216-L5231】
- Haku urged replacing the stock speed-limited MCU with a VESC, ditching the lead-acid mass, and paralleling removable packs via QS8/QS10 connectors and 6 AWG leads while warning against burnouts without fenders because debris is hard to remove.【F:data/vesc_help_group/text_slices/input_part010.txt†L5329-L5349】
- NetworkDir recommended Pro 2 motors over 27H hubs and corrected PuneDir’s assumption about pole counts (>45 poles is unrealistic), reinforcing the need to verify stator specs before investing in rewinds.【F:data/vesc_help_group/text_slices/input_part010.txt†L5501-L5508】

### Control Modes, BMS Selection & Stock Display Considerations (Lines 5305-5334)
- Alin Ciobanu asked about triggering two 75100 controllers with a single button while Lekrsu lamented the overwhelming BMS options on the market, highlighting the need for wiring diagrams and curated BMS recommendations for dual-ESC builds.【F:data/vesc_help_group/text_slices/input_part010.txt†L5305-L5309】
- Dimos experienced throttle lag in current-control mode; Her0DasH and Shlomozero10 confirmed many riders prefer duty-cycle control and that single-switch dual-controller setups are doable with careful wiring, offering peer validation for alternative input schemes.【F:data/vesc_help_group/text_slices/input_part010.txt†L5309-L5316】
- PuneDir wants to reuse the stock speedometer on his moto; Haku redirected him to NetworkDir for firmware support, suggesting CAN/UART translation may be required before reusing OEM dashboards with VESCs.【F:data/vesc_help_group/text_slices/input_part010.txt†L5323-L5327】

### Motor Cooling & Brake Hardware Lessons (Lines 5510-5552)
- Haku’s 33×2 minibike already overheats during 65 mph cruising, prompting curiosity about ferrofluid; Face de Pin Sucé warned that ferrofluid can unglue magnets and instead showcased fan-assisted motors prepared for Spain’s race circuit.【F:data/vesc_help_group/text_slices/input_part010.txt†L5510-L5519】
- The same workshop favors premium Galfer/Trickstuff 160 mm rotors (≈€40) because cheaper 2 mm discs warp under race loads, emphasizing that braking upgrades should match heat output from high-phase builds.【F:data/vesc_help_group/text_slices/input_part010.txt†L5520-L5552】

### Cold-Weather Riding Prep & Charging Logistics (Lines 5701-5799 & 6070-6087)
- Riders compared winter routines: Noname advocated heated gloves, socks, and layered jackets while reminding that cold weather saps battery range even as motors run cooler; Yamal is insulating controllers with plastic covers before rainy season commuting.【F:data/vesc_help_group/text_slices/input_part010.txt†L5701-L5773】
- Yamal’s 22S builds rely on 20 A chargers and 50 Ah packs for long rides, while Haku noted his 50 Ah Molicel pack still takes overnight on a 5 A charger and is seeking faster options—useful context for sizing charge ports on large scooters.【F:data/vesc_help_group/text_slices/input_part010.txt†L5823-L5860】【F:data/vesc_help_group/text_slices/input_part010.txt†L6078-L6087】

### Minibike Data Logging, Thermal Feedback & Ramp Settings (Lines 6091-6554)
- Finn confirmed VESC Tool’s logging toggle captures ride data for offline analysis, nudging Haku to benchmark his ~77 mph runs after he resolves app crashes.【F:data/vesc_help_group/text_slices/input_part010.txt†L6091-L6106】
- NetworkDir flagged MOSFET temps exceeding 60 °C because Haku mounted dual 84/200 controllers on thin steel, urging aluminum heatsinks, better thermal paste, and ferrofluid before chasing 90 mph goals on 250 A battery settings.【F:data/vesc_help_group/text_slices/input_part010.txt†L6112-L6163】
- Removing acceleration ramp time unleashed instant torque and front-wheel slip; Haku now plans to reintroduce limited ramp on the front channel, illustrating how ramp settings materially change traction on 33×2 hubs.【F:data/vesc_help_group/text_slices/input_part010.txt†L6494-L6514】
- The group debated safe phase currents for 84/200 vs 84/250 controllers, with anecdotes of 300–350 A on 33×2 windings before saturation, underscoring the need for logging to avoid overcurrent failures.【F:data/vesc_help_group/text_slices/input_part010.txt†L6528-L6562】

### Lighting, Accessory Power & Controller Outputs (Lines 6416-6491)
- AYO#74 mapped the 75100v2 accessory header: pins 20/22 supply 12 V/3 A for LEDs, grounds are available on pins 2/6/10/14/18/23/24, and brake logic (pin 7 > 1.5 V) can drive a MOSFET for switched brake lights—useful documentation of Spintend IO.【F:data/vesc_help_group/text_slices/input_part010.txt†L6416-L6425】
- Noname recommended using a 12 V automotive USB adapter tied into the scooter’s DC-DC output when riders ask for 5 V charging, avoiding delicate taps off VESC logic rails.【F:data/vesc_help_group/text_slices/input_part010.txt†L6483-L6491】

### LY Motor Sourcing & Factory Contacts (Lines 6032-6048)
- Shlomozero10 confirmed the Kaabo 7260R runs LY motors and sought 65H 10" hubs; Jan shared Lonnyo’s direct WhatsApp (+86 151 6855 5189) and urged bypassing AliExpress middlemen for custom orders, with Finn offering an April 2024 catalog.【F:data/vesc_help_group/text_slices/input_part010.txt†L6032-L6048】

### Kugoo G4 Upgrade Guidance (Lines 6601-6616)
- For a single 2 kW Kugoo G4 moving from 16S to 20S, Finn suggested a Spintend Ubox Lite and potentially swapping to a Vsett display since native Kugoo integration is lacking—important for riders weighing display compatibility when changing controllers.【F:data/vesc_help_group/text_slices/input_part010.txt†L6601-L6616】

### Laotie Harness Rebuild Support (Lines 6681-6700)
- After cutting his Laotie’s entire control harness, Haku solicited wiring help; Pandalgns confirmed the JP display pinout and offered private assistance plus reference photos, illustrating community support channels for resurrecting JP-controlled frames.【F:data/vesc_help_group/text_slices/input_part010.txt†L6681-L6700】

### Dual 50H G30 Planning & PETG Holder Design (Lines 6728-6790)
- Finn is reviving his Dual 50H G30 project and weighing 16S6P internals against jumping to 20S or a 22S hybrid (16S internal + 6S external), noting that a standard Ubox Lite up front and Ubox 85150 in the rear can tolerate 22S if regen is disabled, though routing eight runs of 10 AWG through the stem is daunting.【F:data/vesc_help_group/text_slices/input_part010.txt†L6728-L6769】
- He highlighted PETG battery holder behavior—P42A cans are ~0.25 mm narrower than 40P so tight pockets can relax with heat—and Pandalgns is drafting a fully enclosed 16S Xiaomi case with BMS access ports, reinforcing the need to balance cell retention with serviceability when printing packs.【F:data/vesc_help_group/text_slices/input_part010.txt†L6773-L6789】

### Thermal Interface & Watercooling Debate (Lines 6826-7018)
- Haku currently sandwiches dual 84/200 controllers on a thin steel plate between the pack and deck using a thick budget thermal paste layer, prompting concerns about heat soak and limited airflow ahead of the front tire; relocating to a dedicated heatsink or improving airflow remains on his to-do list.【F:data/vesc_help_group/text_slices/input_part010.txt†L6808-L6811】【F:data/vesc_help_group/text_slices/input_part010.txt†L6826-L6836】【F:data/vesc_help_group/text_slices/input_part010.txt†L6882-L6887】
- Community suggestions ranged from drilling vent access and adding small radiators or pump-assisted loops to simply re-mounting the controllers with better convection, with cautions about leak risk, added mass, and ensuring any water loop can’t drip on live electronics; Lieven reminded that liquid loops increase surface area dramatically if executed well.【F:data/vesc_help_group/text_slices/input_part010.txt†L6981-L7010】【F:data/vesc_help_group/text_slices/input_part010.txt†L7003-L7008】【F:data/vesc_help_group/text_slices/input_part010.txt†L7017-L7018】

### Motor Cooling Experiments & Diagnostics (Lines 7312-7357)
- Haku floated welding fins onto LY motor covers and drilling angled vents, but Noname warned that without ferrofluid the stator-to-cover air gap limits gains and open ports invite magnetic debris; Finn and Lieven advocated active airflow or even watercooled stators for serious heat extraction.【F:data/vesc_help_group/text_slices/input_part010.txt†L7312-L7352】
- Her0DasH highlighted the VESC Tool “hand test” for validating inputs before riding and reminded users to disable it afterward to avoid unexpected behavior, underscoring overlooked safety checks during tuning sessions.【F:data/vesc_help_group/text_slices/input_part010.txt†L7320-L7329】

### PuneDir Battery Builds & Charger Safety (Lines 6899-6906, 7121-7135, 7233-7247, 7563-7569)
- PuneDir showcased a 16S7P Molicel M26 pack that upgrades an OEM 13S scooter to 16S, reinforcing demand for custom retrofits that still honor original enclosures.【F:data/vesc_help_group/text_slices/input_part010.txt†L6899-L6906】
- He asked about using an 84 V (20S) charger on that 16S pack with a JK BMS capping cells at 4.0 V; peers urged caution, pointing out the constant-current/constant-voltage mismatch and unknown behavior of forcing a lower-voltage pack to drag down a 20S charger.【F:data/vesc_help_group/text_slices/input_part010.txt†L7121-L7135】
- PuneDir and NetworkDir clarified their moped dash taps phase-derived speed data, but after a late-night wiring session PuneDir accidentally fed 55 V into the screen’s sensing lead, destroying both the dash and an ignition board—he’s reverting to the stock ESC until replacements arrive.【F:data/vesc_help_group/text_slices/input_part010.txt†L7233-L7247】【F:data/vesc_help_group/text_slices/input_part010.txt†L7563-L7570】

### Display & Telemetry Options (Lines 6937-6990, 6962-6971, 7701-7707, 8174-8178)
- Shlomozero flagged a new Flipsky TFT display with GPS and mode control, reviving debates about third-party dashboards for VESC builds.【F:data/vesc_help_group/text_slices/input_part010.txt†L6937-L6952】
- NetworkDir explained that their current custom screen needs UART (RX/TX/GND/5 V), while the next revision will speak native CAN like a Trampa display and may host VESC Express modules once ESP32-C3 supply issues are sorted.【F:data/vesc_help_group/text_slices/input_part010.txt†L6962-L6971】
- Raphael and NetworkDir later contrasted CAN bus reliability with UART dropouts on high-power scooters, hinting at a forthcoming affordable CAN-based “yellow” display and DIY VESC Express panel builds.【F:data/vesc_help_group/text_slices/input_part010.txt†L7701-L7707】
- JPPL pointed Haku to Voyage Systems’ Megan dash for premium lighting integration, adding another CAN-friendly option for builders chasing polished cockpits.【F:data/vesc_help_group/text_slices/input_part010.txt†L8174-L8179】

### Controller & Firmware Guidance (Lines 7181-7255, 7700-7735)
- Rogerio mistook SmartESC firmware for native VESC on Xiaomi Pro 4 controllers; ‘lekrsu’ clarified it’s an ST-based stack using the VESC app as a GUI, preventing confusion for riders hunting for drop-in VESC conversions.【F:data/vesc_help_group/text_slices/input_part010.txt†L7231-L7247】
- For a dual-75100 Mantis on 60 V, NetworkDir okayed field weakening at 15 A, giving owners a concrete baseline for nudging top speed without cooking the hardware.【F:data/vesc_help_group/text_slices/input_part010.txt†L7248-L7251】
- GABE asked if 22S would overstress Spintend 100 V/100 A FETs; Her0DasH cautioned against aggressive KERS at high charge, while NetworkDir confirmed 22S can work with mindful settings—guidance crucial for extreme Xiaomi conversions.【F:data/vesc_help_group/text_slices/input_part010.txt†L7720-L7735】

### Tire Traction & Pressure Lessons (Lines 7136-7150)
- After a Ninebot F2 Pro low-side on polished asphalt, cihan questioned whether 40–48 psi pressures hurt traction; Noname stressed that lower pressure increases contact patch but reduces ground pressure, while stock CST compound and surface conditions likely caused the slide, suggesting experimentation to find a personal sweet spot.【F:data/vesc_help_group/text_slices/input_part010.txt†L7136-L7150】

### Brake Rotor Quality & Caliper Alignment (Lines 7574-7600)
- Face de Pin Sucé criticized Sonken’s vented discs for bending under race heat, echoing Jan’s warning that the design repeats Brakestuff’s abandoned inner-ring pattern and needs proper tempering; Her0DasH recounted a catastrophic rotor failure that ripped a scooter C-arm, and AYO#74 reminded riders to correct high Hope caliper alignment to avoid uneven braking loads.【F:data/vesc_help_group/text_slices/input_part010.txt†L7574-L7600】

### Suspension Upgrades on the Weepor (Lines 6998-6999, 8194-8199)
- Haku’s Weepor still bottoms out under his weight; he’s eyeing stiffer EXA 150 mm shocks after confirming the stock setup’s excessive travel during manual compression tests.【F:data/vesc_help_group/text_slices/input_part010.txt†L6998-L7001】【F:data/vesc_help_group/text_slices/input_part010.txt†L8194-L8199】

## Open Questions / Follow-ups
- Capture the exact motor winding data (pole count, Kv) for the 24S Thunder builds once testing starts to contextualize top-speed claims.【F:data/vesc_help_group/text_slices/input_part010.txt†L12-L89】
- Verify internal temperatures on the 24S 20P 40PL pack with embedded NTCs before endorsing 35–40 kW pulls, and document any thermal management mods.【F:data/vesc_help_group/text_slices/input_part010.txt†L320-L357】
- Report the VESC Tool 6.0.5 macOS crash to Vedder’s team and note any workarounds (older versions, CLI flashing, etc.) for M2 users.【F:data/vesc_help_group/text_slices/input_part010.txt†L408-L416】
- Assess mudguard/caliper clearance when fitting 90/65-6 tires on Zero 10/Mantis frames and log any required spacers or trimming.【F:data/vesc_help_group/text_slices/input_part010.txt†L97-L130】
- Capture final test results from Rage Mechanic’s RM-X top-speed runs once shared, including Dragy data and thermal observations.【F:data/vesc_help_group/text_slices/input_part010.txt†L1228-L1281】【F:data/vesc_help_group/text_slices/input_part010.txt†L1502-L1560】
- Follow up on Haku’s ES3 pack after the QS8 short: confirm pack integrity, wound recovery, and any design changes (fuse, pre-charge) before road testing.【F:data/vesc_help_group/text_slices/input_part010.txt†L1484-L1588】
- Track Yamal’s planned Thunder/NAMI builds to document enclosure mods, controller selection, and custom LY motor specs once components arrive.【F:data/vesc_help_group/text_slices/input_part010.txt†L2008-L2190】【F:data/vesc_help_group/text_slices/input_part010.txt†L2478-L2564】
- Log cooling performance once Jerome or Jan publish data from the printed GT2 radiator or 26S conversions so others know safe current limits for the GT platform.【F:data/vesc_help_group/text_slices/input_part010.txt†L2739-L2763】
- Document whether AYO#74 restores CAN/traction control on the 22S11P racer and whether the 420 A BMS sustains repeated 50 kW pulls without overheating.【F:data/vesc_help_group/text_slices/input_part010.txt†L2801-L2856】【F:data/vesc_help_group/text_slices/input_part010.txt†L3408-L3485】
- Capture PuneDir’s lead-acid conversion details (battery architecture, phase harness replacement, target controller) once the teardown begins.【F:data/vesc_help_group/text_slices/input_part010.txt†L2705-L2709】【F:data/vesc_help_group/text_slices/input_part010.txt†L3451-L3478】
- Document whether PuneDir completes the VESC swap on the lead-acid moto, including QS10 parallel connectors, 6 AWG runs, and any OEM display integration once NetworkDir supplies firmware guidance.【F:data/vesc_help_group/text_slices/input_part010.txt†L5201-L5352】【F:data/vesc_help_group/text_slices/input_part010.txt†L5323-L5327】
- Capture whether Finn settles on 16S, 20S, or 22S for the Dual 50H G30 and document the final wiring/weight trade-offs once the build resumes.【F:data/vesc_help_group/text_slices/input_part010.txt†L6728-L6769】
- Revisit Haku’s minibike after brake upgrades, Statorade, and parallel-pack experiments to record sustained current draw, temperature trends, and voltage sag under repeated launches.【F:data/vesc_help_group/text_slices/input_part010.txt†L3590-L3839】【F:data/vesc_help_group/text_slices/input_part010.txt†L3850-L4115】
- Check back once Haku remounts the dual 84/200 controllers on aluminum and restores acceleration ramp limits to see if MOSFET temps drop below 60 °C while maintaining traction.【F:data/vesc_help_group/text_slices/input_part010.txt†L6112-L6163】【F:data/vesc_help_group/text_slices/input_part010.txt†L6494-L6514】
- Log temperature results if Haku relocates the controllers or trial-runs a watercooling loop so others understand the payoff vs. added mass/complexity.【F:data/vesc_help_group/text_slices/input_part010.txt†L6808-L6811】【F:data/vesc_help_group/text_slices/input_part010.txt†L6981-L7010】
- Verify fitment and braking performance once the 3 mm Galfer-style rotors are installed on the minibike; document any spacer or caliper alignment changes required.【F:data/vesc_help_group/text_slices/input_part010.txt†L4257-L4284】
- Test whether isolating Bluetooth modules (or powering one scooter at a time) prevents Spintend profile cross-talk before letting kids ride, and capture any firmware fixes from Spintend.【F:data/vesc_help_group/text_slices/input_part010.txt†L4557-L4595】
- Log results after raising zero-vector frequency and adding ferrofluid to Haku’s motors to see if thermal headroom improves during 60–80 mph pulls.【F:data/vesc_help_group/text_slices/input_part010.txt†L4672-L4728】【F:data/vesc_help_group/text_slices/input_part010.txt†L5027-L5090】
- Track Andrei’s 24S9P + 3Shul 80H build for final controller placement, enclosure machining, and ride data once the weekend work wraps up.【F:data/vesc_help_group/text_slices/input_part010.txt†L4854-L4873】
- Capture the final wiring diagram and thermal performance of the 12 V brake light output once AYO#74 or others finish MOSFET-switched LED testing on the 75100v2 harness.【F:data/vesc_help_group/text_slices/input_part010.txt†L6416-L6425】
- Record how PuneDir hardens the moped dash after the 55 V over-voltage incident (protective resistors, isolated supplies, replacement hardware).【F:data/vesc_help_group/text_slices/input_part010.txt†L7233-L7247】【F:data/vesc_help_group/text_slices/input_part010.txt†L7563-L7570】
- Track upcoming CAN-based display launches (NetworkDir’s “yellow” unit, Voyage Megan) and document installation notes or compatibility quirks once someone deploys them.【F:data/vesc_help_group/text_slices/input_part010.txt†L6962-L6971】【F:data/vesc_help_group/text_slices/input_part010.txt†L7701-L7707】【F:data/vesc_help_group/text_slices/input_part010.txt†L8174-L8179】
- Verify whether Spintend 100 V/100 A hardware survives 22S use with regenerative braking limited and share safe KERS or phase current settings once validated.【F:data/vesc_help_group/text_slices/input_part010.txt†L7720-L7735】
- Note any tire pressure or compound changes cihan makes to regain wet-polished traction on the Ninebot F2 Pro and whether the fall led to additional mitigation tips.【F:data/vesc_help_group/text_slices/input_part010.txt†L7136-L7150】
- Document the outcome of Haku’s planned EXA shock swap on the Weepor, including changes in squat, launch traction, and rider comfort.【F:data/vesc_help_group/text_slices/input_part010.txt†L6998-L7001】【F:data/vesc_help_group/text_slices/input_part010.txt†L8194-L8199】

