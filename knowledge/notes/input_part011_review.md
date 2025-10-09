# input_part011.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part011.txt`
- Coverage: 2024-12-19T23:46:45 through 2025-01-14T11:31:24 (lines 1-7150)
- Next starting point: line 7151 (2025-01-14T11:31:24 and later)

## Key Findings

### Jetson Motor Hall Troubleshooting & Sensorless Tuning
- haku’s Jetson hub motor would not pass VESC hall detection despite clean operation on the stock ESC; GABE advised re-running Motor Wizard after rewiring and checking hall continuity/solder joints to avoid impedance that can distort the sensor signals.【F:data/vesc_help_group/text_slices/input_part011.txt†L1-L112】
- Jason recommended enabling VSS (sensorless zero-start) and setting the ERPM loop to 0 so the scooter can launch without halls while diagnostics continue.【F:data/vesc_help_group/text_slices/input_part011.txt†L70-L76】
- Re-checking the hall sensors with the magnet/voltage test confirmed they toggled correctly, prompting a full reset and fresh motor detection that finally brought the sensors online.【F:data/vesc_help_group/text_slices/input_part011.txt†L324-L385】
- Even with halls working, the Jetson motor still shudders under heavy load or once hot; haku measured ~493 µH inductance and 175 mΩ winding resistance, noted 20 S battery / 30 A settings, and estimated ~3 kW peaks at 70 A phase—numbers the group questioned given the thermal saturation observed on climbs.【F:data/vesc_help_group/text_slices/input_part011.txt†L82-L118】【F:data/vesc_help_group/text_slices/input_part011.txt†L453-L503】
- Follow-up testing shows the Jetson overheats once the stator is heat-soaked, so haku is capping output around 1.6 kW and still fighting a high-voltage fault even with VESC Tool limited to 85 V; the pack is a 20 S 3 P Samsung 35E stack, and Raphaël Foujiwara warned him to stay off 22 S despite mixed advice. Finn added that his Flipsky 75100 died instantly after a BMS cutoff, reinforcing the need for clean power delivery.【F:data/vesc_help_group/text_slices/input_part011.txt†L951-L1176】

### Battery Builds, BMS Quirks & Packaging Experiments
- GABE is fabricating a transferable pack for an ebike and Ninebot Pro using salvaged cells, keeping the harness modular while his welder is down, and double-checking JBD BMS behavior after his Xiaomi charger stayed green despite delivering 42 V to a 10 S pack.【F:data/vesc_help_group/text_slices/input_part011.txt†L344-L433】【F:data/vesc_help_group/text_slices/input_part011.txt†L676-L678】
- Later he outlined a 20 S 3 P P42A build (bag fits 6 S + 2 S subpacks) and spacer/heatsink ideas for the M4 Pro 2 deck while sourcing files he lost during a PC reset.【F:data/vesc_help_group/text_slices/input_part011.txt†L811-L826】【F:data/vesc_help_group/text_slices/input_part011.txt†L958-L960】
- In this tranche he mocked up the 20 S 2 P P42A pack for a folding ebike, debated adding a 10 mm deck spacer as a heatsink after losing the original CAD, and diagnosed his sunk welder (error E02 with a burnt MOSFET board) while scavenging reclaimed cells into a solderless 14 S pack for interim use.【F:data/vesc_help_group/text_slices/input_part011.txt†L923-L1421】

### Pedal-Assist & Control Inputs on Flipsky Hardware
- JPPL reminded that Flipsky pedal-assist harnesses usually require splitting the main loom into a four-wire PAS interface (5 V, GND, signal, and often a brake/enable line), with the PAS signal routed to ADC1 while regen throttles can sit on ADC2.【F:data/vesc_help_group/text_slices/input_part011.txt†L447-L696】
- Another builder confirmed PAS only worked once the hall output produced ~1.5 V high / ~0 V low on ADC1, cautioning that releasing throttle after regen could briefly re-activate drive if filtering isn’t tuned.【F:data/vesc_help_group/text_slices/input_part011.txt†L684-L696】

### After-Sales Support Reality for 3Shul/Spintend Controllers
- Face de Pin Sucé and Raphaël Foujiwara discussed the limits of unpaid support: self-installed controllers aren’t warrantied, the CAN connector is a Molex MicroClasp, and sustaining after-sale help would require pricing controllers closer to €900 like Torp TC500 rather than ~€400 C350 units.【F:data/vesc_help_group/text_slices/input_part011.txt†L640-L709】【F:data/vesc_help_group/text_slices/input_part011.txt†L671-L675】
- Raphaël contrasted the 3Shul C350 (more capacitance, upgraded MOSFETs, 400 A phase / 200 A battery rating) with the R350 (CNC case, smart latch, 12 V 3 A aux rail, 350 A phase / 250 A battery), noting both are often run at 400 A even though that sits beyond the safe comfort zone.【F:data/vesc_help_group/text_slices/input_part011.txt†L679-L709】

### Replacement Power Stages & Voltage Limits
- haku ordered two replacement power stages (~$70 each) instead of sending damaged hardware back, receiving boards populated with HY-branded MOSFETs that Raphaël negotiated for Spintend; Raphaël cautioned the unmodified stages should stay on ≤20 S (≈400 A phase) because 21–22 S builds risk failures without his HF filter mods.【F:data/vesc_help_group/text_slices/input_part011.txt†L827-L858】

### Matthew’s G30LP Overhaul & 40 mph Flutter Diagnostics
- Matthew is chasing a “flutter” power loss near 40 mph on a Ninebot G30LP running a single Ubox 85150 at 18 S with 90 A battery, 150 A phase, and 70 A field-weakening; the issue persists even with FW disabled, prompting video logs and settings dumps for review.【F:data/vesc_help_group/text_slices/input_part011.txt†L982-L1248】
- His rebuild targets a 16 S 14 P (~63 Ah) pack with dual 60 V sources, upgraded lighting/signals, and a longer-travel steering damper. Thermal epoxy bonds the controller base to the deck for heat sinking, usually keeping the VESC near 40 °C (peaks around 60 °C on repeated WOT pulls) after an earlier BMS cut shorted a slave controller.【F:data/vesc_help_group/text_slices/input_part011.txt†L1186-L1199】【F:data/vesc_help_group/text_slices/input_part011.txt†L1206-L1236】

### Ubox Firmware Limits & High-Voltage Workarounds
- Smart Repair asked whether the Ubox ADC expansion allows simultaneous UART and analog inputs, and Adri reported that his Ubox 85 V 250 A pair trips a fixed 82 V ceiling even when the software limit is raised for a 92 V battery. Community advice was to flash the `no_hw_limit.bin` firmware to bypass the baked-in ceiling.【F:data/vesc_help_group/text_slices/input_part011.txt†L1546-L1555】

### Tronic Controller Growing Pains vs. 3Shul Benchmarks
- yoann tsobanoglou said tuning Tronic hardware remains frustrating—motor detection often fails to find halls, phase-amp limits are ignored, battery amps trigger chaos, and audible gate noise persists—so he still prefers 3Shul packages that tolerate 500 A phase just as readily.【F:data/vesc_help_group/text_slices/input_part011.txt†L1892-L1899】

### MP2 Open-Source Hardware Status
- Jason confirmed his aluminum MP2 board design is already open-sourced (logic and power boards on GitHub) but still “far from perfect,” so he’s withholding sales until he can shrink the PCB and add capacitance; builders must fully assemble the bare boards themselves.【F:data/vesc_help_group/text_slices/input_part011.txt†L2009-L2044】【F:data/vesc_help_group/text_slices/input_part011.txt†L2051-L2052】

### Voltage Fault Fixes on Ubox and Flipsky Hardware
- Ric.R.M.’s single Ubox 80 threw an over-voltage error after updating to VESC 6.05; reflashing `no limits` alone didn’t help, but setting the correct battery voltage cured the fault for his 20 S, 28 Ah pack rated 100 A.【F:data/vesc_help_group/text_slices/input_part011.txt†L1729-L1759】
- Another rider on Flipsky hardware saw cut-outs near 84 V, initially suspecting 21 S voltage; GABE urged staying ≤20 S and using the PC tool to flash no-limit firmware, while a second multimeter reading confirmed the pack was standard 72 V (20 S).【F:data/vesc_help_group/text_slices/input_part011.txt†L2424-L2443】
- The same rider later regained throttle response by re-running the input wizard after the firmware swap, and is now investigating how to integrate an LCD4 display alongside the VESC app.【F:data/vesc_help_group/text_slices/input_part011.txt†L2453-L2457】

### MKS “84HP” Controller Expectations & MOSFET Packages
- Pandalgns unboxed a pair of MKS 84HP controllers (6 AWG leads, sizeable heatsinks) and asked about safe current—manufacturer guidance lists 200 A continuous / 300 A peak, while his Flipsky 84100 experience suggests 350–400 A phase might remain comfortable.【F:data/vesc_help_group/text_slices/input_part011.txt†L2664-L2676】【F:data/vesc_help_group/text_slices/input_part011.txt†L2688-L2691】
- The group identified HYGO15N10 TOLL-pack MOSFETs (100 V, 380 A max) on the boards, matching the special-order Spintend power stages haku received; validation will depend on real-world stress tests once the Halo scooter is buttoned up.【F:data/vesc_help_group/text_slices/input_part011.txt†L2700-L2754】
- Xiaomi dual-motor shakedowns at 14 S and 180 A phase kept the controllers cool so far, hinting that the large housings may dissipate heat well, though long-term durability is unproven.【F:data/vesc_help_group/text_slices/input_part011.txt†L2753-L2755】

### Deck Integration & Thermal Management for the Halo Build
- Pandalgns cut the Halo deck to recess both controllers while leaving the finned bases proud for airflow; Noname advised adding a deck mat to reduce snagging while still pressing the heatsinks against aluminum for conduction.【F:data/vesc_help_group/text_slices/input_part011.txt†L3121-L3140】
- Sealant (silicone vs. Sikaflex vs. epoxy) and whether to flush-mount the radiators remain open decisions until the scooter is reassembled and riding stance confirmed.【F:data/vesc_help_group/text_slices/input_part011.txt†L3124-L3139】

### High-Current Connector & Wiring Safety Lessons
- For a 20 S 10 P P45B pack targeting ~450 A, QS8 anti-spark plugs were preferred over XT90s to fit dual outputs and 6 AWG leads without crowding.【F:data/vesc_help_group/text_slices/input_part011.txt†L2953-L2960】
- Matthew’s XT60 vaporized when he accidentally paralleled packs, while Noname saw a QS8 back-shell short under a 500 A BMS—cautionary tales that prompted recommendations for inline fuses, test bulbs, and slow verification before connecting high-energy systems.【F:data/vesc_help_group/text_slices/input_part011.txt†L2984-L3004】

### Dual Ubox Mode Mismatch & Lisp/Profiles Workarounds
- Smart Repair’s Dualtron GT1 pairs a Ubox 250 rear with a Ubox 150 front via Spintend’s bridge, which mirrors battery current to both units; Lisp attempts to halve the 150’s current or rely on Q-axis limits either faulted or were overwritten whenever ride modes changed.【F:data/vesc_help_group/text_slices/input_part011.txt†L3145-L3152】【F:data/vesc_help_group/text_slices/input_part011.txt†L3250-L3260】
- Suggestions ranged from leveraging VESC profiles (percentage-based power caps) to disabling the suspect phase filter or injecting CAN-bus overrides so the slave scales incoming setpoints independently.【F:data/vesc_help_group/text_slices/input_part011.txt†L3268-L3323】【F:data/vesc_help_group/text_slices/input_part011.txt†L3299-L3303】
- Enabling CAN “Value” status frames and logging each controller separately in VESC Express finally surfaced the missing motor and MOSFET temperatures, giving Smart Repair diagnostics while he continues searching for a lasting current-split solution.【F:data/vesc_help_group/text_slices/input_part011.txt†L3892-L3910】

### Dashboards, BLE Modules & VESC Express Options
- NetworkDir detailed how one Bluetooth module can service dual VESCs over CAN, or be replaced with ESP32/NRF dashboards (e.g., repurposed Ninebot units) by flashing Vedder’s `nrf51_vesc` firmware via Spintend’s programming pads and wiring 3.3 V plus RX/TX.【F:data/vesc_help_group/text_slices/input_part011.txt†L3795-L3839】
- Smart Repair is exploring a touchscreen dash so the GT bridge can keep handling mode changes while throttle/brake run directly to the ESC; he may contract the UI work if coding the display exceeds his bandwidth.【F:data/vesc_help_group/text_slices/input_part011.txt†L3840-L3858】【F:data/vesc_help_group/text_slices/input_part011.txt†L3943-L3957】

### GABE’s MP2, G30, and M365 Project Queue
- GABE plans to resurrect his G30 with MP2 boards at up to 24 S, budget tyres, and donated hydraulic brakes once he repairs a failed welder and reinstalls lost BMS resistors.【F:data/vesc_help_group/text_slices/input_part011.txt†L3282-L3286】
- He is also packing a 20 S 2 P battery into an M365 deck with a fresh Essential motor, juggling CNC mount work and school deadlines while aiming for 60 km/h without field weakening.【F:data/vesc_help_group/text_slices/input_part011.txt†L3860-L3896】
- A Fiido L3 seat-clamp bolt snapped and the dropout design chewed phase leads, pushing him away from that platform toward Xiaomi-based sit-down builds.【F:data/vesc_help_group/text_slices/input_part011.txt†L3478-L3494】

### Battery Cells, Chargers & Thermal Interface Debates
- Matthew sought feedback on Samsung 50S cells; haku cautioned that advertised discharge numbers are optimistic, whereas Patrick and عمر argued 50S remains the best value if Bak 45D cells aren’t handy.【F:data/vesc_help_group/text_slices/input_part011.txt†L3592-L3612】【F:data/vesc_help_group/text_slices/input_part011.txt†L3625-L3643】
- Andrei and Yamal compared adjustable 20 S/24 S chargers—AliExpress options proved fragile above 84 V, WANPTEK benchtops are limited to 3 A, and Huawei telecom supplies are robust but expensive and bulky.【F:data/vesc_help_group/text_slices/input_part011.txt†L3362-L3399】
- Riders swapped thermal interface tips, highlighting 13 W/mK Iceberg pads from Amazon, inexpensive GD900 paste, and thin adhesive tapes to mate Spintend/Ubox bases to decks.【F:data/vesc_help_group/text_slices/input_part011.txt†L3418-L3427】【F:data/vesc_help_group/text_slices/input_part011.txt†L3435-L3437】

### Jason’s MP2-Powered Nami GT Stress Tests
- Jason is already hitting 200 A phase / 120 A battery peaks on his MP2-powered Nami GT and continues to raise limits while hunting for stronger packs to push the controllers harder.【F:data/vesc_help_group/text_slices/input_part011.txt†L3675-L3685】

### Dualtron Thunder Upgrade Plans & Speed Targets
- Shlomozero10 is outfitting a Thunder chassis with 60H motors, a 72 V 36 Ah (8 C) PowerPacks battery, and dual Flipsky 75200 Pro V2 controllers; Face de Pin Sucé expects that combo to reach 115–120 km/h with a 65 kg rider, while other owners report stock Thunder 2 controllers at 60–65 A battery and ~102 km/h GPS when shunted.【F:data/vesc_help_group/text_slices/input_part011.txt†L2254-L2293】【F:data/vesc_help_group/text_slices/input_part011.txt†L2287-L2323】

### Jetson, Peak G30 & Wepoor Project Updates
- haku fitted four-piston calipers to his 72 V Jetson build and is debating moving from dual 85/150s to Mini Ubox or reassigning 100/100 V2 controllers so higher-power units can live on a Peak G30 mini BMX that may receive P42A or 40T packs plus a 300 A ANT BMS.【F:data/vesc_help_group/text_slices/input_part011.txt†L2338-L2368】【F:data/vesc_help_group/text_slices/input_part011.txt†L2472-L2491】
- He installed Spintend’s HY MOSFET replacement power stage, improvised missing thermal interface material, and still needs to cut heatsinks and locate his CAN cable before pushing the refreshed controller.【F:data/vesc_help_group/text_slices/input_part011.txt†L2550-L2567】
- Jetson upgrades continue with generic hydraulic brakes (a big improvement over cable), while his Wepoor scooter awaits VESC work once the garage is cleared.【F:data/vesc_help_group/text_slices/input_part011.txt†L2543-L2570】

### Aspirations for Mega-Controllers & High-Phase Builds
- haku, Yamal, and Noname daydreamed about 3Shul “1000” units and Fardriver ND722600/842600 stages (advertised up to 2600 A phase), comparing them against 1800 A-phase Vesco setups and noting China-only availability, questionable software quality, and cost as barriers.【F:data/vesc_help_group/text_slices/input_part011.txt†L2587-L2649】

### Smart Repair’s GT1 Dual-Ubox Diagnostics & Speed Targets
- NetworkDir suggested disabling the phase filter after Andrei’s GT1 continued cutting out, and Smart Repair detailed his current mix: rear 70H 22×3 motor on a Ubox 250 at 170 A battery/250 A phase/60 A FW, plus a front GT1 motor on a Ubox 150 at 170 A battery/120 A phase/30 A FW—limits he fears will cook the smaller controller because the Spintend bridge mirrors battery amps across both ESCs.【F:data/vesc_help_group/text_slices/input_part011.txt†L4151-L4239】
- Even with field weakening disabled he only sees ~80–85 km/h despite the 29 KV rear motor that should pencil out to 110–115 km/h on-road; dual status logging confirms the GT1 front hub and 70H rear are both active, so he is eyeing gearing, traction control tweaks, and new brake mounts while he waits on discs.【F:data/vesc_help_group/text_slices/input_part011.txt†L4249-L4287】

### Battery Cell Debates, TVS Diode Sourcing & Wiring Math
- GABE reiterated that Tesla M50LT cells lack peak current versus P45B options, then asked for a replacement part number for the GEE TVS diode on his controller board; Smart Repair recommended a Vishay SMCJ12A as a drop-in 12 V TVS candidate.【F:data/vesc_help_group/text_slices/input_part011.txt†L4173-L4223】【F:data/vesc_help_group/text_slices/input_part011.txt†L4500-L4506】
- Martin Kaktits struggled to reconcile AWG-to-mm² charts until Smart Repair reminded him not to confuse diameters with area, pointing to reference tables that show paired 14 AWG conductors equate to roughly 11 AWG cross-section.【F:data/vesc_help_group/text_slices/input_part011.txt†L4401-L4414】

### Moderation Reminders & Group Culture Drift
- francois schempers restated the group’s zero-tolerance stance on divisive topics after repeated political jabs, promising swifter moderation alongside Miro to keep discussions focused on VESC projects.【F:data/vesc_help_group/text_slices/input_part011.txt†L4461-L4508】

### Halo T107 Pro Field-Weakening Tests, Displays & 20S Battery Plans
- Pandalgns keeps stress-testing dual MKS 84-series controllers in the Halo: in-air pulls with the stock 60 V 100 A pack hit a claimed 230 km/h before excessive field weakening stalled the wheel, prompting him to brake it by foot; he plans a 20 S 10 P P45B pack to raise discharge headroom and expects traction control will be mandatory once that pack is installed.【F:data/vesc_help_group/text_slices/input_part011.txt†L5176-L5184】【F:data/vesc_help_group/text_slices/input_part011.txt†L5532-L5556】
- He is also researching VESC compatibility for QS-S4 dashboards and found GitHub pinouts for the MKS 84100/84200 harnesses to guide a potential LispBM integration.【F:data/vesc_help_group/text_slices/input_part011.txt†L5024-L5050】
- Deck fabrication continues with welded battery plates and tight clearances, while the community debates welding techniques (TIG vs. MIG) and surface prep to avoid weak joints on the Halo and Yamal’s Nami frame repairs.【F:data/vesc_help_group/text_slices/input_part011.txt†L5192-L5218】【F:data/vesc_help_group/text_slices/input_part011.txt†L5219-L5228】

### Thor400-32S Launch Reactions & Water-Resistance Tips
- JPPL shared Tolt’s Thor400-32S spec sheet—32 S support, 400 A absolute max, ESP32 telemetry, and Thor300-compatible packaging—while Raphaël Foujiwara doubted the 12 V/5 A aux rail and current claims given the compact busbars, planning a MOSFET teardown to validate the marketing.【F:data/vesc_help_group/text_slices/input_part011.txt†L4857-L4898】
- Builders asking about weatherproofing Ubox hardware were advised to use conformal coating and silicone-seal every connector, though some called the donor scooter “china trash” and opted to transplant full Ubox setups instead of reusing stock electronics.【F:data/vesc_help_group/text_slices/input_part011.txt†L4905-L4955】

### Scooter Geometry, Stability & High-Speed Benchmarks
- Community chatter questioned the safety of Zero 10X and Dualtron builds above 100 km/h, with Jan warning that many OEMs neglect proper rake/trail for small wheels while NetworkDir and others compared motorcycle geometry to scooters; meanwhile PuneDir circulated a 99+ km/h Zero 10X run and Yamal highlighted Andrei’s 182 km/h speedometer clip, emphasizing the need for robust braking setups.【F:data/vesc_help_group/text_slices/input_part011.txt†L4155-L4185】【F:data/vesc_help_group/text_slices/input_part011.txt†L5167-L5231】

### haku’s Return & Wepoor HY Powerstage Tests
- After a temporary ban haku rejoined, reporting 200 A battery/300 A phase per wheel on the HY-powered Wepoor and targeting 90 mph once tuning and aero are refined, contrasting the setup with his heat-soaked Jetson project.【F:data/vesc_help_group/text_slices/input_part011.txt†L5587-L5637】

### Halo Deck Extender Packaging & Hall Sensor Diagnostics
- Pandalgns split the Halo’s new carbon-fiber deck extender into a lower battery drawer and upper electronics bay, relocating the headlights into the extender for easier service while chasing fitment errors that required re-drilling mounting holes.【F:data/vesc_help_group/text_slices/input_part011.txt†L6025-L6045】【F:data/vesc_help_group/text_slices/input_part011.txt†L6051-L6056】
- His rear motor runs cleanly but the front halls repeatedly fail detection, leading him to ask whether any 120° hall board will drop in; Jason confirmed VESC hardware can generally accommodate any 120° sensor plate as long as wiring order matches.【F:data/vesc_help_group/text_slices/input_part011.txt†L6094-L6108】【F:data/vesc_help_group/text_slices/input_part011.txt†L6344-L6347】

### Lighting & Accessory Power Without ADC Modules
- haku wants to power Jetson lighting without the Spintend ADC expander because of space limits, prompting Noname to recommend a dedicated DC-DC converter instead of loading the ADC rail and to share swappable USB lighting options with long runtimes.【F:data/vesc_help_group/text_slices/input_part011.txt†L5770-L5824】
- The group compared bar lights ranging from Magicshine units that charge while operating to flashlight-plus-mount setups using removable 21700 packs for convenient charging rotations.【F:data/vesc_help_group/text_slices/input_part011.txt†L5787-L5810】

### Delivery Range Planning & Anti-Theft Precautions
- haku is considering Uber Eats work and may build higher-capacity packs or carry swappable batteries after Noname calculated that 5 Ah-class cells only add ~0.8 kWh versus P42A baselines; Noname advised gauging shift length before committing to a rebuild.【F:data/vesc_help_group/text_slices/input_part011.txt†L6033-L6066】【F:data/vesc_help_group/text_slices/input_part011.txt†L6067-L6076】
- European couriers described low gig earnings (≈€20/h peak down to “slavery” after DoorDash bought Wolt) and emphasized heavy chain-and-padlock security when leaving scooters unattended in cities.【F:data/vesc_help_group/text_slices/input_part011.txt†L6117-L6129】【F:data/vesc_help_group/text_slices/input_part011.txt†L6273-L6285】

### Regenerative Charging Concepts for Mopeds
- Давно пора proposed running a Flipsky in DC mode to pull energy from spare 17 S 20 Ah packs into a 72 V 90 Ah delivery moped via regen, hoping to avoid removing the main battery twice per shift; others suggested a high-input DC-DC converter instead, noting prior 1.8 kW models failed prematurely.【F:data/vesc_help_group/text_slices/input_part011.txt†L5969-L5978】【F:data/vesc_help_group/text_slices/input_part011.txt†L5987-L5994】

### Brake Hardware Upgrades & Sensor Integration
- Yamal is swapping to 3 mm Kaabo Wolf discs after stock rotors warped, while 🇪🇸AYO#74🏁 confirmed the thicker rotors last longer in Wolf motors; later Yamal asked whether Trampa 100/250 controllers genuinely support 250 A battery where JPPL reiterated the manufacturer’s continuous rating.【F:data/vesc_help_group/text_slices/input_part011.txt†L5934-L5944】【F:data/vesc_help_group/text_slices/input_part011.txt†L5995-L6001】
- Smart Repair wants an ADC script to toggle ride profiles via brake/throttle button combos and separately sought a hydraulic lever with an integrated three-pin hall sensor for Spintend inputs, requests still unanswered in-thread.【F:data/vesc_help_group/text_slices/input_part011.txt†L5932-L5936】【F:data/vesc_help_group/text_slices/input_part011.txt†L6320-L6321】

### Field-Weakening Limits on Budget Hubs
- عمر’s 14 S M365 build running a Kugoo M4 hub stalls near 50 km/h even with 25 A of field weakening, hinting the motor’s design or thermal load caps speed despite higher voltage; he also lacks motor thermistor feedback, reporting -66 °C readings in logs.【F:data/vesc_help_group/text_slices/input_part011.txt†L6058-L6091】

### MP2 Builds & High-Voltage Ambitions
- Jason’s single-motor MP2 scooter currently tortures a 16 S 6 P Samsung MH1 pack at 80–90 A launches, so he’s targeting a 30 S 4 P Molicel 50S upgrade to sustain 600 A phase bursts on 17×4 or 33×2 motors once his experimental 18 FET TOLL-stage ESC issues are resolved.【F:data/vesc_help_group/text_slices/input_part011.txt†L6348-L6393】
- Yamal advocated sourcing second-hand high-discharge cells or 40T/50S packs to keep pace with MP2 torque, while Jason acknowledged cost as the limiting factor despite contacts in the battery industry.【F:data/vesc_help_group/text_slices/input_part011.txt†L6367-L6379】

### Mobile Telemetry & TCP Bridge Workarounds
- Pixel users found VESC Tool’s TCP bridge drops when the screen sleeps; Jason’s workaround is disabling every battery optimization and allowing unrestricted background usage, while JPPL suggested third-party screen-off utilities or Android settings that keep the app alive without the display on.【F:data/vesc_help_group/text_slices/input_part011.txt†L6278-L6288】【F:data/vesc_help_group/text_slices/input_part011.txt†L6289-L6298】

### Spintend Hardware Reliability & Sourcing Choices
- Arnau Martinez Casals blew a dual 100 V 100 A Alubox at 20 S with 50 A battery / 130 A phase settings; Spintend is upgrading him to an 85 V 150 A unit under warranty if he pays the difference, but he is confirming whether it tolerates full 20 S without regenerative spikes.【F:data/vesc_help_group/text_slices/input_part011.txt†L6482-L6488】
- Franchesco Carofano compared the legacy and “new, smaller” 85 V 250 A single Ubox housings before purchasing; Noname vouched for the older revision (he owns three) while haku prefers proven hardware over the refreshed model despite liking its footprint.【F:data/vesc_help_group/text_slices/input_part011.txt†L6449-L6468】
- haku is tempted to test 22 S on HY-branded Spintend stages now living in his Wepoor but recognizes thermal management should be solved first.【F:data/vesc_help_group/text_slices/input_part011.txt†L6315-L6318】

### Insurance & Regulatory Concerns in EU Builds
- Spanish riders expect certification requirements to tighten by January 2027; Yamal and Pandalgns discussed staying compliant through private insurance that currently permits any power level while they enjoy a two-year window before potential enforcement.【F:data/vesc_help_group/text_slices/input_part011.txt†L6473-L6505】

### Community Health & Injury Notes
- GABE warned how repeated crashes left his knee in bad shape and now relies on dual chain locks to secure bikes, reinforcing the need for physical recovery plans alongside scooter projects.【F:data/vesc_help_group/text_slices/input_part011.txt†L6265-L6276】

### Makerbase Controller Troubleshooting & Bring-Up Safety
- Luis’s MKS 84 HP powers up reliably on 36 V but trips immediately on a 13 S pack; the group advised checking for a missing ignition resistor/anti-spark path and reading the stored fault log once it can stay online at low voltage.【F:data/vesc_help_group/text_slices/input_part011.txt†L7171-L7207】
- Several members recommended bringing suspect hardware up on a current-limited bench supply (≈30–50 mA CC) before connecting a full battery so shorts or firmware issues do not cascade into MOSFET damage.【F:data/vesc_help_group/text_slices/input_part011.txt†L7407-L7419】
- Makerbase Lite owners confirmed the ignition rail can drive a DC-DC converter for light phone charging, but warned that high draw should be avoided and that only the full 75150 exposes a native 12 V tap.【F:data/vesc_help_group/text_slices/input_part011.txt†L7430-L7446】

### Halo Dual-Motor Setup & Display Control
- Pandalgns’ Halo build runs 300 A phase per end but still under-delivers because the hall sensors on the front motor read as faulty, forcing sensorless starts and dramatic wheelspin even when he biases torque rearward; he is debating per-motor phase reductions and whether the AK QS-S4 script can mix asymmetric limits.【F:data/vesc_help_group/text_slices/input_part011.txt†L7264-L7275】
- Later in the week he struggled to trace the T107 Pro handlebar loom to find brake-signal conductors for rear-light triggers, highlighting a documentation gap on Smart Repair’s accessory harnesses.【F:data/vesc_help_group/text_slices/input_part011.txt†L8500-L8507】

### Tronic, Spintend & FarDriver Notes
- Mirono inventoried three Tronic boards (250R, T12T, X12) and questioned their switch wiring and advertised 500 A peaks, underscoring ongoing uncertainty about Tronic’s product matrix versus what ships from stock.【F:data/vesc_help_group/text_slices/input_part011.txt†L7293-L7303】
- Face de Pin Sucé reiterated that the 18 FET G300 overheat faster than 12 FET IMS units once riders push beyond street tuning, so he now steers budget buyers toward Spintend 85/250s or the C350 for true 22 S / 400 A phase support.【F:data/vesc_help_group/text_slices/input_part011.txt†L8404-L8415】【F:data/vesc_help_group/text_slices/input_part011.txt†L8398-L8401】
- Rosheee flagged Tronic’s X12 bundle discount (two units for $598 or singles at $450) and confirmed recent stock handles up to 26 S, which may tempt riders weighing high-voltage alternatives to Spintend or FarDriver ND72360 builds.【F:data/vesc_help_group/text_slices/input_part011.txt†L8590-L8603】【F:data/vesc_help_group/text_slices/input_part011.txt†L8346-L8348】

### Display & Protocol Integrations
- NetworkDir told a Dualtron Victor owner that keeping the OEM display/throttle on VESC requires custom Lisp for the Dualtron CAN/UART protocol—possibly by adapting the open VSETT script—and urged them to favor Spintend Ubox 80100 hardware over Flipsky/Makerbase when investing in that effort.【F:data/vesc_help_group/text_slices/input_part011.txt†L8001-L8012】
- JPPL and Shlomozero compared LED strip densities (WS2815 vs COB WS2811) and mounting orientation for deck spacers, providing references for brighter, evenly diffused underglow lighting on Dualtron builds.【F:data/vesc_help_group/text_slices/input_part011.txt†L8627-L8650】

### Battery & BMS Builds
- Jerome (St0fzuiger) finished a 20 S 9 P EVE 40P pack for his Nami GT2, pairing it with Daly’s 100Balance BMS (soft-limited to ~225 A) and 0.2 mm copper busbars; he estimates the stock GT2 motors comfortably absorb ~7 kW continuous or 10 kW bursts before heat becomes a concern.【F:data/vesc_help_group/text_slices/input_part011.txt†L8509-L8525】
- Dualtron Achilleus received custom 22 S Spintend drives built with HY MOSFETs but is postponing testing until the scooter is reassembled, leaving open questions about 22 S reliability on those revisions.【F:data/vesc_help_group/text_slices/input_part011.txt†L7788-L7798】

### Chargers & High-Voltage Support Gear
- Noname showcased a 4 kW Huawei telecom-based charger ($330 on AliExpress with app-only discounts) capable of programmable voltage/current outputs from 48 V up to 168 V, noting it shares internals with rebranded Guli/Pidzoom/Hou-Nin units that other members already use for 126 V packs.【F:data/vesc_help_group/text_slices/input_part011.txt†L8535-L8557】
- Jason is benchmarking FarDriver ND72360 hardware as a removable, bottom-mount controller option for 30 S scooters, hinting at future comparisons against Spintend’s 85/250 once his ADC quirks are solved.【F:data/vesc_help_group/text_slices/input_part011.txt†L8346-L8350】

### Performance Bottlenecks Still Under Review
- Nawfal’s dual-motor build on MKS 84 HPs stalls at ~41 km/h in air despite 52 V packs and higher phase limits, suggesting firmware gating or fake shunts—members advised validating pole counts, firmware, and hardware integrity while others noted similar caps on 75100 units until shunt mods were performed.【F:data/vesc_help_group/text_slices/input_part011.txt†L8094-L8121】【F:data/vesc_help_group/text_slices/input_part011.txt†L8122-L8139】
- Mattia wired a second throttle to ADC2 for regen on a Kaabo Wolf King GT and asked about driving a brake light from that signal; peers believe a small LED load should not distort the analog voltage but recommended a dedicated adapter for reliability.【F:data/vesc_help_group/text_slices/input_part011.txt†L8196-L8205】【F:data/vesc_help_group/text_slices/input_part011.txt†L8206-L8211】

## Follow-ups / Open Questions
- Continue review from line 8651 onward (2025-01-22T11:37:41 and later) to capture the remainder of input_part011.txt through March 2025.
- Track whether haku resolves the Jetson high-voltage fault and finds sustainable cooling/output for the 20 S Jetson build.
- Document if GABE replaces or repairs the failed welder board, recovers the missing M4 Pro 2 spacer CAD, and finishes the modular battery builds.
- Capture the resolution to Matthew’s throttle flutter and any tuning changes that solve it.
- Note whether Adri (or others) confirms success with `no_hw_limit.bin` on the Ubox 85 V controllers or identifies alternative firmware tweaks.
- Follow up on Ric.R.M. and “No” to see if their no-limit firmware installs stay stable once voltage settings and throttle calibrations are dialed, and whether the LCD4 display integration succeeds.
- Watch for Smart Repair’s documentation on pairing ESP32 touchscreens with Ubox controllers and any guidance on Mini Ubox reliability for mid-power builds.
- Capture performance data once Pandalgns runs the dual MKS 84HP controllers in the Halo chassis (phase/battery limits, thermal behaviour, firmware stability).
- Track Smart Repair’s success balancing the Ubox 250/150 pair—whether via profiles, Lisp/CAN overrides, or future bridge firmware updates—and whether the CAN logging changes surface the dropout cause.
- Follow GABE’s G30/M365 rebuild milestones (welder repair, MP2 assembly, hydraulic brake install) and whether the Fiido L3 failure leads to broader guidance on bolt/clamp upgrades.
- Note any definitive verdicts on Samsung 50S vs. Bak 45D cells for high-current scooters, and practical sources for adjustable 20 S/24 S chargers above 10 A.
- Verify if GABE sources the recommended TVS diode or alternative fix for the damaged GEE board and whether future logs confirm the part works as intended.
- Document whether Pandalgns successfully maps the QS-S4 display to VESC via LispBM and how the interface behaves once the 20 S 10 P pack is live.
- Capture independent testing of the Thor400-32S claims (aux rails, thermal performance, current capacity) once JPPL or Raphaël publish teardown data.
- Monitor welding repairs on Yamal’s Nami and Pandalgns’ Halo deck for durability feedback after road testing, especially under wet-weather loads.
- Track whether Pandalgns restores front-hall sensing on the Halo (sensor replacement, wiring, or firmware) and whether the deck extender withstands road testing.
- See if Smart Repair receives guidance on ADC-based profile toggles or sources a hall-enabled hydraulic lever compatible with Spintend controllers.
- Monitor outcomes of Давно пора’s regenerative charging experiment or alternative DC-DC solutions for courier battery swaps.
- Note Jason’s progress on the 30 S MP2 pack, the 18 FET TOLL-stage debug, and any data on 600 A phase experiments.
- Confirm if Arnau’s warranty replacement tolerates 20 S without regen faults and whether Franchesco reports differences between the legacy and compact 85/250 housings.
- Watch EU legal developments affecting high-power scooters and whether private insurance remains sufficient for Halo-class builds.
- Capture whether Luis identifies the root cause of the MKS 84 HP 48 V shutdown (e.g., missing pre-charge, shunt fault, or firmware issue) and records any fault logs.
- Follow Mirono’s validation of the Tronic 250R/T12T/X12 specs, including whether updated documentation clarifies their off-pin/ignition wiring and peak current claims.
- Track NetworkDir’s or others’ progress on Dualtron display Lisp scripts and confirm if luffydnoob keeps the stock throttle once porting is complete.
- Revisit Nawfal’s MKS 84 HP speed cap to see if firmware, pole count, or hardware changes restore 80 km/h performance.
- Log Jerome’s GT2 road tests once the 20 S 9 P pack and 100Balance BMS are paired with Smart Repair’s harnesses.
- Note community feedback on the 4 kW Huawei/Guli telecom chargers (thermal behavior, CAN/app quirks, DC-input support) after extended use.
