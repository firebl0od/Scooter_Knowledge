# input_part011.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part011.txt`
- Coverage: 2024-12-19T23:46:45 through 2024-12-22T22:20:01 (lines 1-24520)
- Next starting point: line 24521 (2024-12-22T22:20:35 and later)

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

### Regen Cutoffs & Flipsky Production Risks
- PuneDir confirmed his scooter only dies when regen brake cutoffs trigger, echoing NetworkDir’s warning that selling a $1,500 production build around Flipsky hardware remains a gamble despite the modest 48 V 14 Ah pack spec.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L23020-L23212】
- Finn reiterated that a single BMS cutoff was enough to kill his 75100, reinforcing the need for clean power delivery and cautious regen settings on these controllers.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L23932-L23970】

### Jetson 20 S Pack Faults & Project Sequencing
- Haku’s Jetson build still throws a high-voltage error at free-spin even with the max input set to 85 V, and he noted the VESC reads different pack voltage than the BMS until the scooter is ridden under load.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L23383-L23536】
- The scooter is running a 20 S Samsung 35E pack at only 3 P, so Haku is limiting it to short trips to avoid overheating while he finishes tuning before returning to the Wepoor project.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L23600-L23800】
- Foujiwara has cautioned him against stretching the controllers to 22 S despite conflicting vendor advice, so he plans to stay within the 20 S envelope until trusted MOSFET data says otherwise.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L23832-L23894】

### Thermal Budgets, Mounting, and Ambient Limits
- Paolo advised that ~60 °C controller temps are acceptable, but long-term reliability improves when VESCs are kept under ~70–80 °C even though the silicon is rated well above 100 °C; cooler hardware leaves more thermal headroom for power spikes.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L24088-L24515】
- Matthew is bonding his Ubox 85150 directly to the G30LP deck with thermal epoxy, typically holding ~40 °C in use after a prior mount failure let temps spike toward 80 °C; he suspects a previous BMS cutoff shorted another 85150 and now runs the surviving unit solo.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L24168-L24340】
- Yamal’s own dual-Ubox setup is cruising below 30 °C in winter, but he’s watching how summer heat and the quoted “300 A continuous with efficient cooling” marketing claims align with real-world limits.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L24292-L24515】

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

### Brake Caliper Orientation & Rotor Spacing Options
- Riders chasing right-side hose routing on front brakes found that Magura four-piston calipers can be flipped by swapping to a banjo fitting, while budget options (Zoom, Nutt) already ship in mirrored layouts; Andrei also suggested inserting rotor spacers or axle shims when caliper bodies foul the hub flange.【F:data/vesc_help_group/text_slices/input_part011.txt†L7127-L7162】
- 🇪🇸AYO#74🏁 shared an AliExpress kit with 2–5 mm rotor shims and washers so oversize calipers clear hub hardware without custom machining, giving Dualtron and Kaabo owners an inexpensive path to widen rotor stance.【F:data/vesc_help_group/text_slices/input_part011.txt†L7164-L7166】

### Suspension Fitment Cautions on Laotie Frames
- Crazy scoots confirmed that the Laotie rear linkage only accepts ~130 mm eye-to-eye shocks—dropping in a 150 mm coil over-extends the swingarm and lifts ride height enough to bind the suspension—so replacements should match the stock spacing or relocate mounting points.【F:data/vesc_help_group/text_slices/input_part011.txt†L7359-L7370】

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
- Rosheee flagged Tronic’s X12 bundle discount (two units for $598 or singles at $450) and confirmed recent stock handles up to 26 S, which may tempt riders weighing high-voltage alternatives to Spintend or FarDriver ND72360 builds.【F:data/vesc_help_group/text_slices/input_part011.txt†L8590-L8592】【F:data/vesc_help_group/text_slices/input_part011.txt†L8346-L8348】

### Highway Enforcement Lessons
- haku’s 65 mph cruise on the Wepoor ended with a $130 U.S. federal ticket from a park ranger who classified the scooter as a motorcycle; fellow couriers reminded him that plate and registration requirements vary by jurisdiction, and mislabeling the vehicle (calling it a scooter instead of an e-bike) can trigger confiscation risks.【F:data/vesc_help_group/text_slices/input_part011.txt†L7721-L7756】

### Display & Protocol Integrations
- NetworkDir told a Dualtron Victor owner that keeping the OEM display/throttle on VESC requires custom Lisp for the Dualtron CAN/UART protocol—possibly by adapting the open VSETT script—and urged them to favor Spintend Ubox 80100 hardware over Flipsky/Makerbase when investing in that effort.【F:data/vesc_help_group/text_slices/input_part011.txt†L8001-L8012】

### Battery & BMS Builds
- Jerome (St0fzuiger) finished a 20 S 9 P EVE 40P pack for his Nami GT2, pairing it with Daly’s 100Balance BMS (soft-limited to ~225 A) and 0.2 mm copper busbars; he estimates the stock GT2 motors comfortably absorb ~7 kW continuous or 10 kW bursts before heat becomes a concern.【F:data/vesc_help_group/text_slices/input_part011.txt†L8509-L8525】
- Dualtron Achilleus received custom 22 S Spintend drives built with HY MOSFETs but is postponing testing until the scooter is reassembled, leaving open questions about 22 S reliability on those revisions.【F:data/vesc_help_group/text_slices/input_part011.txt†L7788-L7798】

### Chargers & High-Voltage Support Gear
- Noname showcased a 4 kW Huawei telecom-based charger ($330 on AliExpress with app-only discounts) capable of programmable voltage/current outputs from 48 V up to 168 V, noting it shares internals with rebranded Guli/Pidzoom/Hou-Nin units that other members already use for 126 V packs.【F:data/vesc_help_group/text_slices/input_part011.txt†L8535-L8557】
- Jason is benchmarking FarDriver ND72360 hardware as a removable, bottom-mount controller option for 30 S scooters, hinting at future comparisons against Spintend’s 85/250 once his ADC quirks are solved.【F:data/vesc_help_group/text_slices/input_part011.txt†L8346-L8350】

### Performance Bottlenecks Still Under Review
- Nawfal’s dual-motor build on MKS 84 HPs stalls at ~41 km/h in air despite 52 V packs and higher phase limits, suggesting firmware gating or fake shunts—members advised validating pole counts, firmware, and hardware integrity while others noted similar caps on 75100 units until shunt mods were performed.【F:data/vesc_help_group/text_slices/input_part011.txt†L8094-L8121】【F:data/vesc_help_group/text_slices/input_part011.txt†L8122-L8139】
- Mattia wired a second throttle to ADC2 for regen on a Kaabo Wolf King GT and asked about driving a brake light from that signal; peers believe a small LED load should not distort the analog voltage but recommended a dedicated adapter for reliability.【F:data/vesc_help_group/text_slices/input_part011.txt†L8196-L8205】【F:data/vesc_help_group/text_slices/input_part011.txt†L8206-L8211】

### GT2 & Dualtron Lighting Tweaks
- Rosheee confirmed his NAMI GT2 is happily running 26 S packs again with both stock motors and Makerbase X12 controllers back online, restoring dual-motor traction after earlier faults.【F:data/vesc_help_group/text_slices/input_part011.txt†L8602-L8603】
- JPPL detailed his Dualtron spacer lighting: a custom-cut non-printed 2 cm spacer houses outward-facing 12 V WS2815 addressable strips (≈144 LED/m), offering brighter output than Shlomo’s COB strips and inspiring others to restick their LEDs for better diffusion.【F:data/vesc_help_group/text_slices/input_part011.txt†L8630-L8651】

### Ubox & Makerbase Field Reports
- Andrei’s Dualtron Thunder 2 is running dual MakerX Ubox 100/100 controllers at a conservative 55 A battery / 170 A phase each; Paolo cautioned the resin-side-cooled revisions remain thermally weak compared with metal-backed boards.【F:data/vesc_help_group/text_slices/input_part011.txt†L8663-L8679】
- Giuseppe shared a failed Makerbase 75100 V2 module for diagnosis, prompting reminders that prior batches have suffered unexplained deaths and may require factory support to resolve.【F:data/vesc_help_group/text_slices/input_part011.txt†L8680-L8723】
- JPPL continues to push Makerbase hardware at 60 A battery per side, 300 A pack share, and 420 A absolute current on his builds, indicating some units tolerate sustained high output when well-cooled.【F:data/vesc_help_group/text_slices/input_part011.txt†L9222-L9225】
- Makerbase teased a new epoxy-backed control board that mirrors the G300 layout; community members hope for TOLT MOSFET revisions and more robust thermal paths before trusting 300 A claims.【F:data/vesc_help_group/text_slices/input_part011.txt†L9695-L9727】

### Wepoor Powerstage Failures & Ramp Settings
- Haku has now lost multiple front-end VESC power stages on his Weped Wepoor despite modest 200 A battery / 300 A phase limits, with failures triggered by dead-stop launches while temperatures remained cool—he suspects the ANT BMS or regen spikes and is considering heavier-duty 18 FET hardware.【F:data/vesc_help_group/text_slices/input_part011.txt†L8752-L8800】【F:data/vesc_help_group/text_slices/input_part011.txt†L8920-L8991】【F:data/vesc_help_group/text_slices/input_part011.txt†L9578-L9600】
- Shlomo experimented with extending positive ramp time to 10 s, only to kill prior controllers when the BMS cut out under acceleration; veterans recommend keeping ramping near zero to avoid starvation-induced spikes.【F:data/vesc_help_group/text_slices/input_part011.txt†L8833-L8839】
- Yamal’s ride logs reinforce that peak kW on dual setups still track battery current ceilings once phase amps exceed pack limits, even when temporarily pushing 200 A battery and 180‑200 A phase per side.【F:data/vesc_help_group/text_slices/input_part011.txt†L8983-L8991】

### ANT BMS & CAN Diagnostics
- Mattia’s ANT 22PHB1TB230A pack showed misread low cell voltages until members confirmed his balance wiring and urged a full parameter setup in the ANT app, sharing official wiring diagrams and the direct APK link when firmware updates stalled in-app.【F:data/vesc_help_group/text_slices/input_part011.txt†L9343-L9374】【F:data/vesc_help_group/text_slices/input_part011.txt†L9518-L9574】【F:data/vesc_help_group/text_slices/input_part011.txt†L9814-L9827】【F:data/vesc_help_group/text_slices/input_part011.txt†L9931-L9939】
- CAN bus sanity checks should show ≈3.3 V differential between high and low; AYO’s 16 V reading flagged a measurement mistake until koxx clarified the expected levels.【F:data/vesc_help_group/text_slices/input_part011.txt†L9258-L9260】【F:data/vesc_help_group/text_slices/input_part011.txt†L9394-L9397】

### Fabrication & Tooling Notes
- For aluminum swing-arm swaps (e.g., Teverun suspension on a G30), Noname stressed that stick welders won’t cut it—budget MIG units make a mess, whereas TIG or pro fab shops deliver durable joints; lacking gear, GABE opted to revert to his bolt-on V1 design.【F:data/vesc_help_group/text_slices/input_part011.txt†L9279-L9333】
- High-current wiring jobs benefit from 200‑300 W handheld irons (AliExpress units proven on QS8 connectors) or even 350 W “3 kg” stations; smaller 65 W tools demand risky overdriving to keep up.【F:data/vesc_help_group/text_slices/input_part011.txt†L9405-L9475】【F:data/vesc_help_group/text_slices/input_part011.txt†L9683-L9684】
- Veterans shared welding realities—TIG offers the strongest, cleanest results (even for titanium) but demands expensive multi-process machines, protective gear, and heat management; hobbyists should master MIG basics first before chasing laser or TIG rigs.【F:data/vesc_help_group/text_slices/input_part011.txt†L9601-L9774】【F:data/vesc_help_group/text_slices/input_part011.txt†L9803-L9906】
- GABE’s DIY fork swap uses a spare motor stator as a drilling jig and stock G30 bolts to keep alignment true while opening new mount holes, underscoring the need for precise fixturing when modifying frames.【F:data/vesc_help_group/text_slices/input_part011.txt†L10018-L10037】

### High-Voltage Projects & Hardware Development
- Jason is prototyping a 30 S-ready “JESC” 18‑FET controller for Ninebot G30 frames, targeting a 140 mm envelope with 4 mF of capacitance and SPiN-style pin headers while debating capacitor split placement for clearance.【F:data/vesc_help_group/text_slices/input_part011.txt†L9413-L9462】【F:data/vesc_help_group/text_slices/input_part011.txt†L9601-L9619】
- PuneDir’s 35H QS-style hub sourced through Turkish channels raised clone concerns; peers advised buying direct from China when customs allow to ensure magnet grade authenticity.【F:data/vesc_help_group/text_slices/input_part011.txt†L9477-L9488】
- Jason’s also reverse-engineering Fungineers’ 32 S VESC BMS for an open-source variant, though firmware and hardware hurdles persist.【F:data/vesc_help_group/text_slices/input_part011.txt†L10024-L10033】

### Spintend & Voyage Observations
- Matthew reports his Spintend 85150 caps phase current around 150 A even when commanded to 180 A with a 90 A battery limit, implying firmware-imposed ABS overcurrent ceilings that may need tuning for higher torque builds.【F:data/vesc_help_group/text_slices/input_part011.txt†L9728-L9736】【F:data/vesc_help_group/text_slices/input_part011.txt†L9954-L9955】
- Arnau’s new Voyage-displayed Spintend 85 V/150 A controller immediately threw ABS OCP faults; Jason suspects the absolute current limit is set too low and urged connecting via VESC Tool rather than relying solely on the Voyage screen.【F:data/vesc_help_group/text_slices/input_part011.txt†L9987-L10048】
- Kron Vark is seeking guidance to clear an E10 error on a stock Vsett 10 display and to load Lisp scripts, signaling continued demand for turnkey CAN display support.【F:data/vesc_help_group/text_slices/input_part011.txt†L10062-L10063】

### VESC Bridge V2 Feature Roadmap
- Jerome unveiled the rewritten VESC Bridge V2 hardware, now covering Segway GT1/GT2 plus Ninebot G30/G2 with OTA firmware, plug-and-play harnessing (except halls/phases), anti-theft lockouts, per-motor torque shifting, adjustable regen limits, PowerNine RGB/guard modes, and planned support for JBD/JK/ANT/Daly BMS along with turn-signal I/O and per-motor current caps.【F:data/vesc_help_group/text_slices/input_part011.txt†L10828-L10829】

### Tronic 250 Batch Failures & MP2 Ambitions
- Franchesco shared new photos of scorched Tronic 250 controllers, prompting Jason to chalk recurring deaths up to poor power design while he pushes a 30 S MP2 build targeting 15 kW with 150 A battery limits inside a G30 deck.【F:data/vesc_help_group/text_slices/input_part011.txt†L10553-L10577】

### Thunder Frame Prep, BMS Headroom & Heatsink Use
- Shlomozero debated grinding a Thunder frame bare for thermal contact and bolting paired 75200s directly, but veterans advised keeping the anodization, reusing the stock heatsink plate, and mirroring deck cleanup on the controller side while stressing that battery brownouts can lock the motor if the pack cuts mid-ride.【F:data/vesc_help_group/text_slices/input_part011.txt†L10596-L10604】
- His 20 S 9 P LiShen pack runs a 220 A BMS, with peers suspecting loose wiring rather than the continuous rating when diagnosing intermittent faults.【F:data/vesc_help_group/text_slices/input_part011.txt†L10610-L10613】

### Kaabo King GT Harness Recovery
- عمر confirmed his Kaabo King GT still carried the stock phase leads, later spotted a front hall issue that traced back to an unplugged phase, and eventually revived CAN comms on the legacy 100 V/100 A bridge by leaving the controller powered down overnight.【F:data/vesc_help_group/text_slices/input_part011.txt†L10535-L10537】【F:data/vesc_help_group/text_slices/input_part011.txt†L10609-L10691】【F:data/vesc_help_group/text_slices/input_part011.txt†L10835-L10836】

### Vsett 10 Saturation Troubleshooting
- Morten Jensen’s Vsett 10 motor began saturating at 70 A battery / 140 A phase, so he plans to dial back the motor amps and revisit his parameter limits after the group confirmed the load was excessive for the setup.【F:data/vesc_help_group/text_slices/input_part011.txt†L10852-L10874】

### Adjustable Charger Options
- Noname resurfaced a 2000 W adjustable charger listing (66–93 V up to 23 A or 72–101 V up to 16 A), underscoring how scarce compact high-power chargers remain on AliExpress.【F:data/vesc_help_group/text_slices/input_part011.txt†L10863-L10871】

### Error Codes & Kaabo Brake Adapter Sources
- françois schempers posted a quick-reference list of Voyage/Ninebot error codes (BLE comms through ABS OCP) and urged checking throttle/brake voltages against ground when chasing faults.【F:data/vesc_help_group/text_slices/input_part011.txt†L10948-L10949】
- Mattia sourced rear Magura adapters for the Kaabo Wolf King GT from Javamba after flipping the front hub to mount a left-side caliper proved unworkable for the rear motor.【F:data/vesc_help_group/text_slices/input_part011.txt†L10961-L10963】

### Wepoor Burnouts, BMS Thresholds & Regen Strategy
- Haku lost another CAN-linked VESC on the Wepoor while testing ~400 A limits; NetworkDir warned ANT BMS regen cutoffs can brick controllers and that low-resistance 70H 33×3 motors behave like near-shorts during burnouts, while ‘lekrsu’ urged separating discharge, level-2, and short thresholds to avoid constant short-fault trips.【F:data/vesc_help_group/text_slices/input_part011.txt†L10964-L11027】
- The crew reiterated capping regen near 120 A and ensuring the BMS never severs charge current mid-brake so controllers stay powered through decel events.【F:data/vesc_help_group/text_slices/input_part011.txt†L10993-L11027】

### Phase-Energy Metrics & PWM Efficiency Debate
- Smart Repair clarified that the “15 Ah” reading on Voyage dashboards reflects phase amp-hours, not battery draw; ‘lekrsu’, Jan, and Patrick agreed energy accounting belongs on battery sensors while comparing PWM-frequency trade-offs—many run 30–33 kHz for smooth torque without audible chatter despite the efficiency hit.【F:data/vesc_help_group/text_slices/input_part011.txt†L11045-L11117】

### Ubox 85/250 Failure & Warranty Follow-up
- Franchesco’s freshly installed 85 V/250 A Ubox flashed internally within three meters on a 20 S 42 Ah Molicel pack set for 150 A battery / 250 A phase (350 A absolute), leading peers to request MOSFET photos and advise against powering the smoked unit while he petitions for warranty support.【F:data/vesc_help_group/text_slices/input_part011.txt†L11149-L11156】【F:data/vesc_help_group/text_slices/input_part011.txt†L11268-L11273】

### VESC Express Automation Experiments
- yoann tsobanoglou is cloning Spintend’s green board logic in a smaller form via VESC Express and LispBM—he already triggers brake lights and motor braking over CAN but is chasing minor latency before deploying it broadly.【F:data/vesc_help_group/text_slices/input_part011.txt†L11274-L11275】

### 22×3 vs 33×2 Motor Trade-offs & Range Logs
- Yamal finds dual 22×3 Lonnyo hubs lively yet traction-limited around 200 A per motor without TC, while 33×2 stators demand highway speeds and flawless tuning; he’s budgeting for 80H 33×2 motors with 175 A battery / 300 A phase goals even if that means selling his 22×3 set.【F:data/vesc_help_group/text_slices/input_part011.txt†L11276-L11440】
- Haku estimates his 12 P Wepoor returns roughly 50 miles at 35–50 mph street speeds but drains quickly above 65 mph, whereas Yamal’s 10 P setup sees ~100 km per charge—highlighting how gearing, tire size, and pack capacity govern usable range.【F:data/vesc_help_group/text_slices/input_part011.txt†L11443-L11480】

### Motor Pricing & Clone Vetting
- Patrick priced 65H 22×3 Lonnyo hubs at about $205 each (~€315 landed), while Shlomozero and Finn flagged suspicious “90H” listings likely housing 80–85H stators; Paolo meanwhile is exiting the game by selling four spare 40H torque hubs for €200.【F:data/vesc_help_group/text_slices/input_part011.txt†L11298-L11367】
- Israeli buyers warned that customs duties and confiscation risks can erase any savings on bargain motors despite the tempting price tags.【F:data/vesc_help_group/text_slices/input_part011.txt†L11368-L11371】

### Battery Salvage & Tooling Advice
- GABE plans to Dremel non-leaded solder off reused P42A cells for a low-draw pack, with Matte and Noname recommending carbide burr bits or copper braid while cautioning about overheating cell insulators and suggesting a fresh Bak 45D rebuild instead.【F:data/vesc_help_group/text_slices/input_part011.txt†L11294-L11338】
- Haku pointed to metal cutoff wheels for cleanup, warned tariffs could soon inflate cell costs, and GABE is sourcing 6–7 V TVS diodes to revive his welder before tackling the next battery project.【F:data/vesc_help_group/text_slices/input_part011.txt†L11381-L11394】

### Mijia & Jetson Packaging Notes
- GABE’s Xiaomi Mijia refresh keeps the controller in the stock bay while a 20 S 2 P pack lies along the deck on a 32.5 mm spacer; he prefers 15–16 S for cooler running but is testing 20 S with a temp sensor until spot-welding gear is restored, leaving the scooter compact enough for public transit.【F:data/vesc_help_group/text_slices/input_part011.txt†L10863-L10925】【F:data/vesc_help_group/text_slices/input_part011.txt†L10920-L10958】
- Haku still leans on his 20 S 3 P Samsung 35E Jetson for urban errands (~50-mile range with hydraulic brakes) yet cautions that even small amounts of field weakening can kill the stock hub—he now avoids FW entirely after frying motors at just 4 A.【F:data/vesc_help_group/text_slices/input_part011.txt†L11484-L11512】

### Jetson Project Valuation
- Haku fielded a $400 offer for the custom Jetson (20 S 3 P pack, JBD BMS, Spintend 85/150, hydraulic discs) but may keep it or hand it to family while plotting a pedal-equipped successor that stays legal if regulations tighten.【F:data/vesc_help_group/text_slices/input_part011.txt†L11581-L11613】

### Spintend 85150 Early-Batch Quirks
- Star / Delta Master’s supposedly 85 V/150 A Ubox arrived with a 100 V/100 A silkscreen on the powerstage, pointing to early batches that reused lower-rated boards; Hackintoshhhh confirmed the mismatch and noted replacement stages require drilling because only two of six screws align with the old case.【F:data/vesc_help_group/text_slices/input_part011.txt†L11760-L11770】【F:data/vesc_help_group/text_slices/input_part011.txt†L11778-L11781】

### 22×3 Lonnyo Current Limits & Controller Survival
- Riders pushing 22×3 hubs report ~150 A battery / 300 A phase as the practical ceiling on Spintend 75200 V2 hardware, with race users trimming to ~110 A battery to curb heat and keep room for field-weakening overhead.【F:data/vesc_help_group/text_slices/input_part011.txt†L11784-L11797】

### Wepoor Burnouts, BMS Cutoffs & Regen Safeguards
- Haku’s dual-motor Wepoor continues to pop front stages near 400 A; the crew attributed the twin failures to ANT BMS charge cutoffs and urged separating discharge, level-2, and short thresholds while keeping regen under control instead of simply bypassing protection.【F:data/vesc_help_group/text_slices/input_part011.txt†L11680-L11703】【F:data/vesc_help_group/text_slices/input_part011.txt†L11943-L11970】
- ‘lekrsu’ reiterated that “uncaptured” regen—where the BMS severs the pack mid-brake—is what actually kills controllers, so the fix is raising charge/short trip points rather than disabling braking altogether.【F:data/vesc_help_group/text_slices/input_part011.txt†L11956-L11969】

### Switching Between 1WD and 2WD
- Smart Repair confirmed the Spintend ADC expander can stage a one-touch 1WD/2WD toggle, but doing so requires isolating the CAN bridge because the secondary controller stays awake if it remains on the bus.【F:data/vesc_help_group/text_slices/input_part011.txt†L11899-L11907】【F:data/vesc_help_group/text_slices/input_part011.txt†L12376-L12381】

### 75100 V2 Power-Up Diagnostics
- Hurriicane’s aluminum-PCB 75100 V2 boots over SWD at 3.3 V yet stays dark on pack voltage; probing found one EG3112 gate driver missing its 12 V feed, tripping constant undervoltage faults until the buck regulator is repaired.【F:data/vesc_help_group/text_slices/input_part011.txt†L11880-L11929】【F:data/vesc_help_group/text_slices/input_part011.txt†L11995-L12011】

### Halo Crash After MOSFET Burst
- Pandalgns’s rear controller ejected MOSFET silicon when the front wheel locked at ~20 km/h, launching him over the bars; he now plans to strip both motors, inspect harnesses, and replace the destroyed display before returning the Halo to service.【F:data/vesc_help_group/text_slices/input_part011.txt†L12243-L12264】

### Pack Building & Cell Insulation
- Matte’s latest pack photo set underscores using Kapton plus vulcanized fiber between parallels, with Haku pressing to review the balance-lead routing—the “money shot”—before signing off on workmanship.【F:data/vesc_help_group/text_slices/input_part011.txt†L12401-L12409】

### Teverun & Lonnyo Motor Notes
- JPPL confirmed stock Teverun 7260 scooters ship with 33×2 motors, while the group reiterated shorthand for common Lonnyo windings (33×2 speed, 22×3 standard, 17×4 torque) when planning swaps.【F:data/vesc_help_group/text_slices/input_part011.txt†L12299-L12308】【F:data/vesc_help_group/text_slices/input_part011.txt†L12211-L12219】

### Cheap Battery Failures & Fire Risk
- Eren’s bargain eBay pack began venting, then reignited during a recharge attempt despite freezing temperatures—peers urged him to stop charging, dunk the pack in water, and scrap the cells before the scooter burns entirely.【F:data/vesc_help_group/text_slices/input_part011.txt†L12300-L12345】

### Connector Orientation & QS10 Capacity
- Finn reminded builders to keep female connectors on live battery leads (chargers use male) when debating QS8/QS10 layouts, while others highlighted QS10’s 10 mm bullets and 400 A rating for high-power builds.【F:data/vesc_help_group/text_slices/input_part011.txt†L12536-L12545】【F:data/vesc_help_group/text_slices/input_part011.txt†L12655-L12660】

### Xiaomi Dash Integration
- GABE verified the Xiaomi dash needs a 1 kΩ resistor on the UART line and runs reliably on VESC firmware 6.05, matching Finn and Jason’s field experience.【F:data/vesc_help_group/text_slices/input_part011.txt†L12684-L12706】

### Single-Motor Tuning & Saturation Compensation
- Matthew’s 65 H 22×3 Lonnyo on a single Ubox 85150 stabilized after adding Statorade and limiting saturation compensation to ≤20%, yet the controller still caps phase current near 150 A despite higher software limits—suggesting firmware-imposed ceilings.【F:data/vesc_help_group/text_slices/input_part011.txt†L12982-L12999】

### Multi-Motor CAN Scaling
- Jan and ‘lekrsu’ confirmed VESC Tool handles at least four CAN-linked controllers from one throttle (default parent + three children) and can be extended further, paving the way for Jan’s planned 30 S 18 P kart with four driven wheels plus a separate downforce fan stage.【F:data/vesc_help_group/text_slices/input_part011.txt†L13024-L13061】

### M365 Sleeper Build
- GABE’s “stock-looking” M365 now hides a 20 S 2 P pack and VESC swap that pushes 70 km/h, but he disabled BMS protections to keep it running—promising to monitor cell temps manually to avoid another catastrophic cutoff.【F:data/vesc_help_group/text_slices/input_part011.txt†L12588-L12632】

### CrowPanel Touch Displays & IO Planning
- عمر reminded builders that the dash consumes the UART port while the VESC BMS must sit on CAN, so he stepped up to an ESP32-S3 display to free IO and flagged CrowPanel’s 5-inch 800×480 option as a ready-made LVGL-capable touchscreen for future integrations.【F:data/vesc_help_group/text_slices/input_part011.txt†L13113-L13120】

### Single Ubox 85150 Phase Ceiling Reports
- Matthew’s single 65 H 22×3 Lonnyo on a Spintend Ubox 85150 (FW 6.05) still hard-limits around 150 A phase despite 210‑280 A software targets and a 90 A battery cap; peers suspect firmware or BMS enforcement after a prior 115 A battery pull tripped a cutoff and shorted a controller.【F:data/vesc_help_group/text_slices/input_part011.txt†L13221-L13255】【F:data/vesc_help_group/text_slices/input_part011.txt†L14583-L14584】

### Smart Repair’s Kaabo GT Drivetrain Mix
- Smart Repair’s Wolf/GT hybrid currently runs a 20 S 9 P (~40 Ah) pack with a front Ubox 150 and rear Ubox 250, tops out near 115 km/h because of voltage sag, and is queued for a front 250 A stage plus a rear Tronic X12 swap once the new battery is built.【F:data/vesc_help_group/text_slices/input_part011.txt†L13240-L13250】

### Field-Weakening & Regen Benchmarks
- Shlomozero’s 20 S 9 P Lishen-copper pack drives 22×3 hubs at ~200 A battery and 200 A phase with 60–80 A of field weakening for air spins to ~200 km/h, raising follow-up questions about safe regen limits on the 75200 Pro V2 platform.【F:data/vesc_help_group/text_slices/input_part011.txt†L13324-L13341】

### Small Hub Thermal Limits in High-Voltage Conversions
- GABE vaporized back-to-back 250–300 W scooter hubs by feeding 55–70 A phase at 72 V; without the right Torx driver to add a temp probe he’s capping the last spare to ~35 A phase while searching for a 350 W replacement motor.【F:data/vesc_help_group/text_slices/input_part011.txt†L13618-L13645】

### Lonnyo 100 H Packaging Plans
- Pandalgns is pursuing Lonnyo 100 H 33×2 motors despite limited clearance, budgeting for widened shock mounts and bracket fabrication while teammates pitch pairing them with Seven-series controllers and 40 PL packs once the chassis is opened up.【F:data/vesc_help_group/text_slices/input_part011.txt†L13669-L13680】

### Tronic & Ubox Control Wiring Notes
- Martin’s attempt to reuse a Ninebot dash on Tronic hardware confirmed ADC2 lines live on the MISO pin beside TX, while عمر cautioned that throttle adapters need 3.3 V supply with ground/ADC1/ADC2 correctly pinned to avoid frying the interface.【F:data/vesc_help_group/text_slices/input_part011.txt†L13865-L13880】【F:data/vesc_help_group/text_slices/input_part011.txt†L13973-L13974】

### High-End Brake Options & Heat Considerations
- Riders weighed €1.2 k Trickstuff Maxima kits against Magura MT5/MT7 setups, noting that motorcycle Brembos rarely fit scooter forks and that 150 km/h racing stops mandate larger rotors plus higher-volume master cylinders to survive the heat load.【F:data/vesc_help_group/text_slices/input_part011.txt†L14065-L14115】

### Battery Pack Insulation Without Cell Holders
- David defends triple-layer Kapton between parallel groups when space precludes cell holders, but Patrick and Jason reiterated that wrapping every cell or using holders remains safer than bare “kissing” cells despite the labor penalty.【F:data/vesc_help_group/text_slices/input_part011.txt†L14081-L14085】【F:data/vesc_help_group/text_slices/input_part011.txt†L14276-L14285】

### LVGL Dash & Touch UI Development
- Jason and NetworkDir are prototyping resistive-touch dashboards on the Kaabo GT, leaning on LVGL libraries to add tap-to-change drive modes after early tests exposed finicky touch controllers and missing profile selectors.【F:data/vesc_help_group/text_slices/input_part011.txt†L14223-L14275】

### Mini BMX “Peak G30” Build Parameters
- haku’s mini BMX conversion targets a 20 S 3 P P42A pack feeding dual Spintend 100/100 controllers at roughly 65 A battery and 100 A phase per side; Noname’s Vsett reference (95 A battery, 180 A phase on 50 H hubs) underscores how much extra headroom 4–5 P packs provide.【F:data/vesc_help_group/text_slices/input_part011.txt†L14232-L14267】【F:data/vesc_help_group/text_slices/input_part011.txt†L14243-L14248】

### Nami Overvoltage Readings & ADC Divider Suspicions
- Yamal’s Nami intermittently boots with 84.5 V displayed and zero throttle response despite an 83.6 V charge cap, prompting Jason to suggest checking the ADC divider and voltage-sense calibration on the control board.【F:data/vesc_help_group/text_slices/input_part011.txt†L14510-L14515】

### Spintend 85/150 Beta Cooling Notes
- Finn confirmed the early “85/150” Spintend boards still use 100 V components, run happily at 72 V and ~180 A phase when clamped to a 3 mm aluminum baseplate, and can be extended with custom sheet-aluminum heat spreaders where space allows.【F:data/vesc_help_group/text_slices/input_part011.txt†L14554-L14570】

### RFP Controller Reliability Callout
- عمر and haku praised RFP’s production controllers as the rare set-and-forget option in their fleet—rugged enough for daily Jetson and commuter builds so long as battery current stays moderate.【F:data/vesc_help_group/text_slices/input_part011.txt†L14588-L14590】

### RFP Frame Expansion & Thunder Component Planning
- Yamal confirmed the RFP battery bay is roughly 15 cm longer than stock, making room for dual Tronic Seven-class controllers and a 22 S 11 P Eve 40PL pack as the Thunder build progresses in stages.【F:data/vesc_help_group/text_slices/input_part011.txt†L14641-L14671】
- He plans to evaluate the high-KV speed motors on his Nami first and, if torque or thermal headroom prove lacking, swap to 75H 22/3 hubs while probing ~600 A phase and 350–400 A battery settings per controller.【F:data/vesc_help_group/text_slices/input_part011.txt†L14670-L14672】

### Heatbox Ignition Harness Troubleshooting
- Maximus Brokus’ legacy single Heatbox 100 V/100 A controller only delivered 0.3 V at the ignition port until the group reiterated that the keyed plug has no firmware jumpers—mis-pinning the leads is the typical failure mode.【F:data/vesc_help_group/text_slices/input_part011.txt†L14709-L14719】
- JPPL advised double-checking the three-wire loom because supply positive may not be the red conductor and shared reference photos to verify the pinout.【F:data/vesc_help_group/text_slices/input_part011.txt†L14726-L14730】

### Spintend 85/150 MOSFET Swaps & Current Headroom
- Hackintoshhhh has run a Ubox 85/150 at 160–180 A battery and ~240 A phase since swapping to 500 A-rated Tokmas/JMSh1001ATLQ MOSFETs, noting they run hotter due to higher RDS(on) but have stayed reliable for months.【F:data/vesc_help_group/text_slices/input_part011.txt†L14757-L14816】
- Patrick still pegs the six-FET stage around 230–250 A phase even with hardware mods, dismissing rumors of safe 500 A operation on the 85/150 platform.【F:data/vesc_help_group/text_slices/input_part011.txt†L14751-L14758】【F:data/vesc_help_group/text_slices/input_part011.txt†L14811-L14819】

### Thunder Front 85150 Setup & Cooling Strategies
- Shlomozero plans to dedicate a Ubox 85150 to the Thunder 2’s front 60H motor while the rear draws from a 72 V, 36 Ah (220 A) pack; Matthew confirmed 150 A battery / 230 A phase is achievable if temps stay in check.【F:data/vesc_help_group/text_slices/input_part011.txt†L14930-L14948】
- Their thermal playbook includes generous paste, external heat sinking (even half-exposed plates), fans if space allows, and VESC temperature limits that start throttling before the controller touches ~96 °C during 120–130 km/h attempts.【F:data/vesc_help_group/text_slices/input_part011.txt†L14935-L14958】

### Victor Motor Power Scaling & Hall Debates
- skrtt’s Victor dual-motor swap to a 3Shul C350 should survive 50 A per wheel at 60 V, with haku and Noname reminding that 16×4 windings sip current while 22×3 speed stators demand more amps and temperature monitoring to keep 2–3× nominal power sustainable.【F:data/vesc_help_group/text_slices/input_part011.txt†L14975-L15007】【F:data/vesc_help_group/text_slices/input_part011.txt†L15037-L15071】
- Opinions split on adding halls: haku prefers them for smooth sine starts, while Noname and Mirono argue sensorless launches work if you tolerate kick starts or brief BLDC phases, highlighting trade-offs between convenience and wiring effort.【F:data/vesc_help_group/text_slices/input_part011.txt†L15008-L15034】【F:data/vesc_help_group/text_slices/input_part011.txt†L15530-L15537】

### Reclaimed Stark Cells & 20 S P45B Builds
- Arnau Martinez Casals is assembling 20 S 5 P Molicel P45B packs from Stark’s mis-welded stock—cells arrived wrapped but unwelded—letting him re-stack them without adhesives while chasing higher current draws on 50H 17×4 motors.【F:data/vesc_help_group/text_slices/input_part011.txt†L15080-L15093】
- He’s already clocked 85 km/h without field weakening and plans to raise amperage once the reclaimed pack is finalized.【F:data/vesc_help_group/text_slices/input_part011.txt†L15073-L15082】

### Lonnyo 100H Fitment & Halo Suspension Rework
- Dualtron Achilleus and Pandalgns report the new Lonnyo 100H hubs measure ~183 mm across the dropouts, demanding an extra 33 mm of clearance beyond the Halo’s 150 mm mounts plus bespoke shock brackets to clear the wider stators.【F:data/vesc_help_group/text_slices/input_part011.txt†L15539-L15558】
- Pandalgns is budgeting €200–300 for fabricated shock supports and plans to pair the eventual 100H swap with 3Shul 400 A controllers, 30 S batteries, and chassis reinforcement after finishing the current 60H/20 S stage.【F:data/vesc_help_group/text_slices/input_part011.txt†L15563-L15573】【F:data/vesc_help_group/text_slices/input_part011.txt†L15552-L15553】

### Water Cooling Plans & Ubox Hardening
- Smart Repair outlined an X12 water-cooling loop using a 40 × 80 mm block on the MOSFET bank, PWM-controlled ~800 L/h pump, and a small radiator (fan optional) to keep summer frame temps below 50 °C; the full system should weigh under 1 kg with 300 g coolant, 300 g pump, and ~500 g in hardware.【F:data/vesc_help_group/text_slices/input_part011.txt†L15737-L15941】
- To prevent future water ingress he’s conformal-coating Ubox 250 logic boards, sealing connectors, and adding Kapton where needed after a previous cleaning session bricked an unprotected controller.【F:data/vesc_help_group/text_slices/input_part011.txt†L15962-L15983】

### CAN Harness Interference from 300X Throttle
- عمر’s Tronic X12 setup developed violent surging, ADC spikes, and rogue accelerations after switching from a Spin Y2 to a 300X throttle; separating the throttle, CAN, and Bluetooth harnesses and reverting to BLDC calmed the system while he investigates shielding.【F:data/vesc_help_group/text_slices/input_part011.txt†L15923-L15926】
- Smart Repair recommends adding a ~2 kΩ pull-down on the throttle signal and keeping the control loom away from phase leads to suppress EMI coupling between the new hall sensor and CAN wiring.【F:data/vesc_help_group/text_slices/input_part011.txt†L15943-L15945】

### MP2 Packaging Height & 30 S Ambitions
- Jason measured his MP2 stack at roughly 22–23 mm tall—thin enough for 10" decks—and notes the capacitor “pills” can sit lower if he removes pin headers, at the cost of USB access, while he pursues 30 S packs for 100 km/h goals.【F:data/vesc_help_group/text_slices/input_part011.txt†L15861-L15876】
- He’s already hitting ~73 km/h at 60 V with aggressive field weakening and is weighing whether 22×3 motors would have been a better single-motor choice versus the current 17×4 winding.【F:data/vesc_help_group/text_slices/input_part011.txt†L15891-L15896】【F:data/vesc_help_group/text_slices/input_part011.txt†L15805-L15833】

### Field-Weakening Trade-offs & Motor Selection Debate
- Jan, Mirono, and Jason sparred over field weakening versus higher-KV hubs: proponents like Mirono use FW to stretch top speed when amps remain, while Jan stresses the lost torque could instead feed a faster winding, and Jason admits 17×4 may cap his ambitions despite strong ESCs.【F:data/vesc_help_group/text_slices/input_part011.txt†L15791-L15834】
- francois schempers added that on low-voltage (13 S) setups FW is often the only path past ~50 km/h without buying new batteries and controllers, underscoring the pragmatic vs. ideal trade-off.【F:data/vesc_help_group/text_slices/input_part011.txt†L15893-L15895】

### Spintend 85150 Field Test & Voyage Display Takeaways
- Arnau’s MiniMotor build is holding 60 V with 150 A phase and 80 A battery on a Spintend 85150 using only MTPA—no field weakening—and he’s delighted with the performance so far.【F:data/vesc_help_group/text_slices/input_part011.txt†L17701-L17709】【F:data/vesc_help_group/text_slices/input_part011.txt†L17743-L17749】
- The Voyage “Megan” display bundle (roughly $400) piggybacks on the Metr app to log trips, expose full VESC parameters, and store multiple ride modes, but riders still treat it as rain-only hardware because the enclosure isn’t watertight.【F:data/vesc_help_group/text_slices/input_part011.txt†L17701-L17735】

### Segway GT2/GT3 Platform Reality Check
- Jan reminded builders that the Segway GT2 steers well and has generous packaging, yet the stock stem bearing is fragile and both axles need machining before larger hubs will fit, so upgrades demand chassis work, not just electronics.【F:data/vesc_help_group/text_slices/input_part011.txt†L17797-L17803】
- ’lekrsu’ noted the base GT3 is still a 48 V tube-frame scooter with a cramped bay and legacy controller, whereas the GT3 Pro steps up to 72 V with a deeper chassis; both appear to ship with 11" hubs on a 7.5" rim, so dropout and brake mods remain mandatory for high-power builds.【F:data/vesc_help_group/text_slices/input_part011.txt†L17805-L17839】

### 20 S Mini Build Performance & Limits
- GABE’s 20 S 2 P commuter is happily launching at 75 A phase (~3 kW) while keeping the hub cool, but the short wheelbase forces him to lean forward under 100 A current spikes to avoid looping out.【F:data/vesc_help_group/text_slices/input_part011.txt†L17943-L17966】
- Even with only ~600 Wh on board he’s seeing 20 km of hard riding from 41–81 V, and the deck still has room for a 20 S 7 P pack if he ever wants to trade minimalism for range (with better waterproofing).【F:data/vesc_help_group/text_slices/input_part011.txt†L17990-L18017】

### Ninebot G2 80 km/h Upgrade Checklist
- Community consensus for an 80 km/h Ninebot G2 build includes widening the rear suspension with longer bolts/bushings to 150 mm dropouts, grinding the separator plate, fitting a 65 H 22×3 hub, and moving to at least a 20 S 5–6 P 21700 pack paired with a robust VESC such as an aluminum Ubox 85/150.【F:data/vesc_help_group/text_slices/input_part011.txt†L18290-L18333】【F:data/vesc_help_group/text_slices/input_part011.txt†L18345-L18383】
- Builders warned that Monorim front ends bend, strip threads, and misalign under those loads, so expect to budget for a speed fork or other front suspension swap before adding dual motors or heavy brakes.【F:data/vesc_help_group/text_slices/input_part011.txt†L18389-L18433】
- ’lekrsu’ confirmed the stock dropout is only 115 mm (roughly “Xiaomi size”) and can accept even 90 H or 100 H hubs once widened, while francois shared support-bracket photos and machining contacts for perfectly sized spacers.【F:data/vesc_help_group/text_slices/input_part011.txt†L18453-L18485】

### Flipsky Reliability & Display Oddities
- Multiple riders repeated that Flipsky controllers still suffer random QC failures—Matte sees many die within a month, Jason’s unit shorted FETs after a single pull until the Ninebot BMS intervened, and others only trust them with ample cooling and low current.【F:data/vesc_help_group/text_slices/input_part011.txt†L18600-L18615】
- Mirono is experimenting with Flipsky’s yellow ESP32-style display; no verdict yet, but Jason pointed to the open-source SimpleVescDisplay firmware for anyone flashing their own board instead of buying AliExpress bundles.【F:data/vesc_help_group/text_slices/input_part011.txt†L18617-L18642】

### Spintend 85/250 Current Ceilings & CAN Power Sync
- Dualtron Achilleus reminded everyone that Spintend 85/250 firmware clamps phase at 350 A; you can touch 400 A for under a second, but practical use should stay around 300 A unless you accept thermal and reliability risks.【F:data/vesc_help_group/text_slices/input_part011.txt†L18849-L18858】【F:data/vesc_help_group/text_slices/input_part011.txt†L18939-L18939】
- Shlomozero10’s Thunder 2 build will pair an 85/150 front with an 85/240 rear and a Lishen 21700 pack, and early testing suggests the 85-series CAN power line lets a single button toggle both controllers once linked—handy for 1WD/2WD switches without extra relays.【F:data/vesc_help_group/text_slices/input_part011.txt†L19016-L19035】

### CAN/UART Profile Switching Script Review
- Smart Repair’s AI-generated ESP32 script for 1WD/2WD toggling drew a full code review: francois flagged inverted profile logic, missing debounce, repeated telemetry calls, and divide-by-zero risks before sharing a debounced rewrite that caches voltage, checks library support for CAN IDs, and clarifies UART pin mapping.【F:data/vesc_help_group/text_slices/input_part011.txt†L18920-L18926】【F:data/vesc_help_group/text_slices/input_part011.txt†L19080-L19088】【F:data/vesc_help_group/text_slices/input_part011.txt†L19082-L19088】

### Lonnyo 70H Waterproofing & Bearing Prep
- Smart Repair showed Lonnyo 70H hubs arrive completely unsealed with flimsy bearings, urging riders to swap both bearings and seal the housings before installation to prevent early failures.【F:data/vesc_help_group/text_slices/input_part011.txt†L16325-L16333】
- Jerome recommends Plasti Dip as a reversible waterproof coating for packs and controllers—easier to service than fully siliconed cases—and even shared a sourcing link after his previous bottle dried out.【F:data/vesc_help_group/text_slices/input_part011.txt†L16334-L16338】

### GT Battery Pack Busbar & BMS Layout
- Smart Repair’s current Kaabo GT pack is a self-built 20 S 9 P (≈40 P) Eve 40 setup that sags ~12 V at 500 A phase; the BMS is rated for 550 A battery current and sits ahead of the partition wall for access.【F:data/vesc_help_group/text_slices/input_part011.txt†L16758-L16790】
- To bolster cross-section he bridges nickel with 0.2 mm copper, stacking three 0.2 mm sheets on the positive and negative plates, and plans a 22 S successor once the GT front swaps to a 65 H hub and the rear moves to a Tronic X12.【F:data/vesc_help_group/text_slices/input_part011.txt†L16758-L16783】

### Xiaomi Brake ADC Fault Diagnostics
- KierreKikkeli’s Xiaomi brake/throttle combo triggered runaway behaviour around 85% lever throw; Smart Repair asked for ADC wizard captures, confirmed the wiring uses the stock ADC v2 harness, and reminded him to verify the module’s hardware switch before remapping inputs.【F:data/vesc_help_group/text_slices/input_part011.txt†L16193-L16217】
- After a test clip, Smart Repair suggested removing the “invert” hook and recalibrating the ADC profile inside VESC Tool—an easy-to-miss step when the hardware has sat untouched for months.【F:data/vesc_help_group/text_slices/input_part011.txt†L16211-L16217】

### ABS Limits, Saturation, and Traction Control Ideas
- Arnau’s single Ubox 80 threw ABS overcurrent faults above ~100 A motor; Smart Repair and JPPL reminded him the stock firmware caps phase at ~150 A/ABS 210 A, so flashing the no-limit build and raising ABS to ~240 A with good cooling is required for 100 A battery / 180 A phase targets.【F:data/vesc_help_group/text_slices/input_part011.txt†L17240-L17252】
- francois schempers’ follow-up memo explains how magnetic saturation stops extra torque past ~100 A on smaller hubs and advises limiting phase current or upsizing motors instead of fighting the physics.【F:data/vesc_help_group/text_slices/input_part011.txt†L17315-L17316】
- He also shared an untested, LLM-generated back-EMF traction-control routine—framing external wheel sensors, current imbalance, or filtered back-EMF as alternatives to eRPM-based slip detection while cautioning readers to validate the code themselves.【F:data/vesc_help_group/text_slices/input_part011.txt†L17380-L17383】

### Thunder 3 Certification & 80H Hardware Details
- Yamal reports Minimotors’ Thunder 3 has finally been homologated as Spain’s first 72 V-legal scooter starting January 2027, making certified units essential for future road compliance even if the chassis looks identical to earlier runs.【F:data/vesc_help_group/text_slices/input_part011.txt†L16543-L16558】
- His freshly arrived Lonnyo 80 H motors include hall and temperature sensors, ship without rims for about €736, and demand a 155 mm fork opening—he plans to trial them on the Nami before committing to the larger RFP project.【F:data/vesc_help_group/text_slices/input_part011.txt†L16588-L16608】

### PAS Integration on Flipsky/Makerbase Controllers
- Mirono’s 75100 Pro V2 only exposes a quadrature PAS option in VESC Tool; Finn clarified PAS is just pedal assist while Jason suggested using an Arduino translator if you need to adapt a three-wire cadence sensor to the quadrature input.【F:data/vesc_help_group/text_slices/input_part011.txt†L16610-L16621】
- The same thread highlights uncertainty about the Pro V2 servo pin’s 5 V tolerance—worth confirming before powering external sensors straight from that header.【F:data/vesc_help_group/text_slices/input_part011.txt†L16505-L16505】

### VESC Bridge Pre-Orders & Traction Control Notes
- Jerome opened pre-registration for the upcoming VESC Bridge hardware batch so he can size the parts order before assembling the next run.【F:data/vesc_help_group/text_slices/input_part011.txt†L16029-L16033】
- JPPL reminded riders that VESC traction control “is ok” but sacrifices torque to curb wheelspin, framing expectations for Matte’s query about whether to enable it.【F:data/vesc_help_group/text_slices/input_part011.txt†L16039-L16040】

### Micro-Hub Thermal Limits & Motor Upgrade Options
- GABE warned that doubling pack voltage on Xiaomi/Ninebot hubs without field weakening simply overheats the small stators—his rule of thumb is “20 S hits 55 km/h, but the motor will blow” unless you swap to a wider hub like the Fiido L3 that sheds heat far better.【F:data/vesc_help_group/text_slices/input_part011.txt†L19101-L19139】
- He reiterated that budget scooter ESCs and packs are equally outmatched at those currents, so builders should budget for a full drivetrain refresh instead of chasing speed with stock hardware.【F:data/vesc_help_group/text_slices/input_part011.txt†L19124-L19139】

### Xiaomi/M365 Voltage & Packaging Guidance
- Jason, Hackintoshhhh, and GABE confirmed that the M365 deck can swallow creative 18 S–20 S packs (even 20 S 2 P) when the ESC and BMS are relocated under the footplate, but they still consider 18 S the “sweet spot” for reliability and layout sanity.【F:data/vesc_help_group/text_slices/input_part011.txt†L19142-L19195】
- They cautioned that stem-mounted packs and skinny OEM hubs won’t survive high voltage; upgrading to larger ESx/G30-class motors and sturdier forks is part of any serious sleeper build.【F:data/vesc_help_group/text_slices/input_part011.txt†L19186-L19213】

### Inokim OXO Brake & Nami Race Prep Notes
- David’s hunt for a four-piston front brake on an OXO with the stock swingarm ended with two options: flip a rear arm to mount the caliper underneath or machine a bespoke adapter for the OEM arm.【F:data/vesc_help_group/text_slices/input_part011.txt†L19400-L19403】
- Arnau outlined his upcoming 22 S 10 P P45B Nami build with Ambrosini 75 H motors and a 10 mm aluminum heat spreader, while planning to race the existing G30/Spintend setup until the new pack arrives.【F:data/vesc_help_group/text_slices/input_part011.txt†L19418-L19445】

### Dualtron 75H Saturation & Battery Diagnostics
- Dualtron Achilleus’ Thunder struggled to exceed ~135 A phase despite a 220 A target; francois suspects either battery sag from the 16 S 7 P pack or magnetic saturation, and asked for fresh motor detection logs to confirm.【F:data/vesc_help_group/text_slices/input_part011.txt†L19419-L19476】
- ’lekrsu’ reminded him that VESC tapers phase current as eRPM rises, so plotting battery voltage/current during pulls will reveal whether wiring or saturation is capping torque.【F:data/vesc_help_group/text_slices/input_part011.txt†L19464-L19475】

### High-Current Pack Planning Lessons
- skrtt’s question about pulling 350 A from an 18 S 9 P P45B pack drew reassurance that 40 A per cell is acceptable with good cooling, and that adding series voltage doesn’t change per-cell current stress—only top speed.【F:data/vesc_help_group/text_slices/input_part011.txt†L19742-L19799】
- The crew recommended logging voltage sag and phase limits before redesigning the pack, since motor size and settings often gate performance more than nominal system voltage.【F:data/vesc_help_group/text_slices/input_part011.txt†L19751-L19799】

### Spintend 22 S Mod Debates & Alternatives
- Arnau hopes to push a Spintend 85/150 to 22 S/150 A with MOSFET swaps, but GABE and Jason cautioned that the logic board still tops out around 22 S and that beefier capacitors are mandatory if you chase higher voltage without e-brakes.【F:data/vesc_help_group/text_slices/input_part011.txt†L19970-L20004】【F:data/vesc_help_group/text_slices/input_part011.txt†L19986-L20002】
- Smart Repair later confirmed 22 S is safe on stock MOSFETs/caps provided you disable regen braking, while francois pointed Arnau to Rage Mechanics’ C350 as a 30 S-ready alternative if he outgrows the 6-FET platform.【F:data/vesc_help_group/text_slices/input_part011.txt†L20187-L20204】【F:data/vesc_help_group/text_slices/input_part011.txt†L20003-L20004】

### Dual-Controller Integration & Packaging Updates
- JPPL is finishing a “medium” plug-and-play harness that feeds dual Thor 300 controllers with shared 12 V accessories, VESC Express telemetry, lighting, horn, and Spintend power buttons—all packaged for ≤300 A phase and 20 S systems.【F:data/vesc_help_group/text_slices/input_part011.txt†L19928-L19935】
- Shlomozero confirmed that Spintend 85240 cases have passthrough holes for top-exiting phase leads, letting builders reroute without desoldering as long as they protect the foam insulation pads.【F:data/vesc_help_group/text_slices/input_part011.txt†L19936-L19954】

### Thermal Management Experiments
- Builders are repurposing dead Spintend 75200 baseplates as auxiliary heat spreaders for 85-series controllers; JPPL pairs aluminum spacers, minimal thermal pad thickness, and a custom CNC enclosure while Shlomozero sketches external radiator blocks tied into Dualtron side plates.【F:data/vesc_help_group/text_slices/input_part011.txt†L20180-L20261】
- JPPL also shared MakerWorld STL files for Tronic MOSFET spacers, noting they required sanding to sit flush before clamping everything metal-to-metal for best conduction.【F:data/vesc_help_group/text_slices/input_part011.txt†L20260-L20261】

-### Field Support & Troubleshooting Highlights
- Roby MacGyver learned that Makerbase controllers expose an ignition pin (A15) behind the ADC/DC-DC menu—feed it with a momentary 5 V pulse from the keyswitch, set ADC channel 9 to “control,” and enable the shutdown timer so the VESC latches on/off without back-powering through the BMS.【F:data/vesc_help_group/text_slices/input_part011.txt†L20399-L20454】【F:data/vesc_help_group/text_slices/input_part011.txt†L20652-L20671】
- Jason advised Hugo to raise the ABS overcurrent ceiling when 60 A battery commands trigger cutouts, while francois reminded him to keep ABS roughly 1.5× the phase limit to avoid recurring faults.【F:data/vesc_help_group/text_slices/input_part011.txt†L20441-L20515】

### Sensorless Launch Workarounds for Dual Drives
- With the front hub running sensorless, Martin Kaktits explored delaying that motor until the rear pushes the scooter off the line; Jason recommended fine-tuning VSS first, while francois highlighted HFI or scripting a PWM disable below a set ERPM if rewiring the halls proves impractical.【F:data/vesc_help_group/text_slices/input_part011.txt†L20380-L20396】

### Lonnyo 80H Fitment & Brake Clearance Lessons
- Yamal’s attempt to squeeze Lonnyo 80H hubs into his frame shows the stock swingarm studs are too short for both the motor and brake hardware; he now plans to fabricate longer main bolts so the caliper clears.【F:data/vesc_help_group/text_slices/input_part011.txt†L20643-L20745】
- JPPL echoed that the suspension pivots are easier to space, but the primary arm hardware must grow to keep the axle square once the larger motors are bolted in.【F:data/vesc_help_group/text_slices/input_part011.txt†L20733-L20745】

### Platform & Ownership Updates
- Yamal sold his Dualtron Thunder (and the RFP frame) at a slight profit, picked up a Ninebot G2 for legal-friendly riding, and is pausing the Nami until he fabricates longer steel axles for the swingarms.【F:data/vesc_help_group/text_slices/input_part011.txt†L20953-L21010】
- He’s still logging heavy mileage on the Spintend Nami (≈2,500 km) while planning city moves, highlighting how big-wheel platforms excel on rural routes yet demand ongoing axle upkeep.【F:data/vesc_help_group/text_slices/input_part011.txt†L20996-L21012】

### MP2 Pro 2 Packaging & 85240 Upgrade Plans
- Patrick is prototyping a custom heatsink so an uncased Spintend 85240 (≈40 mm including capacitors plus an 8 mm fin stack) can squeeze into his MP2 Pro 2 deck; he’ll road-test a 150 A setup on a 17×4 delta motor, then add an external 20 S 2 P booster and order the controller once the printed mockups confirm clearance.【F:data/vesc_help_group/text_slices/input_part011.txt†L20933-L20957】

### High-Current Controller Shopping Notes
- Mattia is hunting for a VESC that can sustain 200–250 A battery and ~300 A phase, with peers pointing him toward the Spintend 85240 platform pending confirmation that its MOSFET stack tolerates those peaks.【F:data/vesc_help_group/text_slices/input_part011.txt†L20664-L20671】

### Mini Spintend Current Targets & Cooling
- haku and Yamal agreed to cap the dual mini Spintend stack around 200 A battery per motor (≈300 A phase) and 45 A per P42A cell until better cooling and enclosures are in place, noting that earlier 500 A battery pushes tripped cutoffs despite low controller temps.【F:data/vesc_help_group/text_slices/input_part011.txt†L17615-L17639】

### Voyage Megan Display & Alternatives
- Arnau’s Voyage Megan display bundles a dedicated firmware plus full Metr integration for trip logging and ride-mode storage, but Smart Repair warned the ~$400 unit still isn’t waterproof out of the box.【F:data/vesc_help_group/text_slices/input_part011.txt†L17721-L17740】
- Smart Repair showcased a cheaper Raspberry Pi dashboard build (mark99i’s repo) as a configurable alternative when paired with Spintend hardware.【F:data/vesc_help_group/text_slices/input_part011.txt†L17746-L17752】

### 60 V Performance Check-ins
- Arnau’s latest ride report shows his 60 V build holding 150 A phase / 80 A battery on pure MTPA without field weakening, delivering the response he wanted.【F:data/vesc_help_group/text_slices/input_part011.txt†L17778-L17779】

### Tire Direction & Ninebot GT Platform Notes
- Running a tyre backwards keeps summer grip acceptable but flings water, debris, and hydroplaning forces straight down the centre, so riders should flip tread direction before wet-season use.【F:data/vesc_help_group/text_slices/input_part011.txt†L17783-L17789】
- Jan and ‘lekrsu detailed Segway’s new GT platforms: GT2 frames have space and steering geometry advantages but weak stem bearings, whereas the GT3 Pro upgrades to 72 V electronics in a deeper chassis while the base GT3 stays 48 V with a tube frame and shallower bay.【F:data/vesc_help_group/text_slices/input_part011.txt†L17797-L17816】

### Compact 20 S Packs & Range Logs
- GABE’s 20 S 2 P commuter pack logs roughly 300 Wh per 10 km (about 20 km of aggressive riding from a 600 Wh pack) and still fits 20 S 7 P inside the chassis when waterproofed, confirming the deck volume for future capacity bumps.【F:data/vesc_help_group/text_slices/input_part011.txt†L17990-L18016】

### Rider Safety Incident & Recovery Notes
- A crosswind tossed GABE into a pole at speed, leaving him temporarily unable to walk and nursing fractures despite protective gear—others urged medical scans and highlighted how quickly urban gusts can overwhelm short-wheelbase builds.【F:data/vesc_help_group/text_slices/input_part011.txt†L18213-L18253】

### Xiaomi G2 80 km/h Upgrade Roadmap
- Justiinx B’s 70–80 km/h G2 plan now includes budgeting €500–€800 for a 20 S battery (5–6 P 21700 cells), a 65H 17×4 hub, and a quality VESC such as the Ubox 85/150, with the option to add a second controller later once braking and suspension are uprated.【F:data/vesc_help_group/text_slices/input_part011.txt†L18257-L18278】
- Veterans warned that the G2’s stock monorim hardware bends and strips under power; widening the rear dropout to ~150 mm only needs longer bolts and bushings, but the front suspension should be replaced to avoid failures once larger motors are installed.【F:data/vesc_help_group/text_slices/input_part011.txt†L18430-L18474】

### Hall Debugging & Flipsky QC Signals
- When Mirono’s Flipsky suddenly lost halls, the crew pointed to VESC Tool’s hall-calibration tab (desktop only) and suspected a dead 5 V rail after sensor detection returned zeros.【F:data/vesc_help_group/text_slices/input_part011.txt†L18580-L18599】
- Builders again flagged Flipsky’s uneven quality control—many units fail early unless cooling and assembly are perfect—contrasting Jason’s burned stage with Mirono’s long-lived sample.【F:data/vesc_help_group/text_slices/input_part011.txt†L18593-L18613】

### ESP32 Displays & SimpleVescDisplay Tips
- Mirono’s experiments with the Flipsky CAN display reminded the group that generic ESP32 yellow displays can pipe UART data straight into ADC1 via NetworkDir’s SimpleVescDisplay firmware, giving a budget telemetry option for riders who’ve lost their phones or OEM screens.【F:data/vesc_help_group/text_slices/input_part011.txt†L18617-L18640】

### Spintend 85/250 Capability & Connector Planning
- Dualtron riders confirmed the Spintend 85/250 firmware caps at 350 A phase but can briefly stretch to 400 A; Yamal emphasised its battery-current headroom rivals premium controllers and is pairing it with 8 mm Amass bullets plus Juliet signal connectors for his 80H build.【F:data/vesc_help_group/text_slices/input_part011.txt†L18849-L18865】

### Profile Switching Scripts & Dual-Drive Options
- JPPL outlined quick workarounds for single/dual drive—kill one controller with the power button, break CAN with a switch, disable CAN in software, or bolt on Spintend’s ADC board—while Smart Repair floated an Arduino profile sender for finer control.【F:data/vesc_help_group/text_slices/input_part011.txt†L18981-L18984】【F:data/vesc_help_group/text_slices/input_part011.txt†L18971-L18974】
- francois schempers audited Smart Repair’s AI-generated UART script, advising debounced button handling, cached telemetry, v_in safety checks, and library pin verification before sharing a cleaned version that implements those safeguards for CAN-linked masters/slaves.【F:data/vesc_help_group/text_slices/input_part011.txt†L19080-L19088】

### Dual Spintend Power Sync & Thunder Build Notes
- Shlomozero’s Thunder 2 wiring confirms Spintend 85-series controllers share a CAN “power on” signal, so a single button can wake both units; he’s starting with an 85/150 front and 85/240 rear on Lishen 21700 packs until he sources dual 85/240s.【F:data/vesc_help_group/text_slices/input_part011.txt†L19014-L19035】

### High-Speed Stability & Deck Styling
- Yamal reminded Thunder riders that only the “LaFerrari” stays wobble-free above 130 km/h—others must bias weight forward and fine-tune hardware, while JPPL noted his 11X still needs meticulous hand/part calibration despite running smooth at speed.【F:data/vesc_help_group/text_slices/input_part011.txt†L19041-L19055】

### Controller Availability & Thermal Notes
- JPPL reports the 3Shul G300 still “rocks” if kept cool, while Yamal highlighted Kilian’s continued reliance on the R350, underscoring the split between readily available G300 stock and race-focused Schul hardware in Europe.【F:data/vesc_help_group/text_slices/input_part011.txt†L19070-L19073】

### 72 V E-bike Conversion Cautions
- Morten Jensen’s idea of pushing a 250 W/36 V commuter bike to 72 V drew warnings that doubling voltage without a better motor will overheat micro hubs—GABE suggested sourcing sturdier Fiido hardware or risk torching budget drivetrains.【F:data/vesc_help_group/text_slices/input_part011.txt†L19093-L19099】

### Xiaomi/M365 Voltage Mods & Motor Survivability
- GABE cautioned that simply doubling a Xiaomi/Ninebot build from 10 S to 20 S without field-weakening headroom will cook the stock hub—he’s already sacrificed three motors that way—and recommends swapping to a wider Fiido L3 rear hub for the surface area needed to shed heat.【F:data/vesc_help_group/text_slices/input_part011.txt†L19101-L19133】

### Compact Battery Layouts for Xiaomi Decks
- Yamal and Jason mapped options for reviving a battered M365: any larger 10 S pack helps, 18 S is the “sweet spot” for fit, but 20 S 1–2 P or even a tight 30 S 1 P stack will squeeze in if controllers are relocated (e.g., Ubox 100/100 Lite underneath) and the harness is reworked.【F:data/vesc_help_group/text_slices/input_part011.txt†L19145-L19185】

### High-Discharge Cell Sourcing Constraints
- Jason noted Samsung 50S cells are already €5.3 locally, while 40T or Eve packs now require business licences or grey-market importing—leaving scavenged Lime MH1 modules as his budget fallback and highlighting the need for EU-to-EU private shipments when premium cells are scarce.【F:data/vesc_help_group/text_slices/input_part011.txt†L19190-L19229】【F:data/vesc_help_group/text_slices/input_part011.txt†L19260-L19279】

### 32 S Charge-Only BMS Prototype
- Jason’s 32 S VESC-friendly BMS evaluation board mirrors VFBMS32 topology but inverts the MOSFET orientation (drains tied together, sources commoned), prompting diode-drop concerns and a plan to iterate a smaller production PCB once the eval hardware survives lab testing.【F:data/vesc_help_group/text_slices/input_part011.txt†L19404-L19496】

### Inokim OXO Front Brake Upgrades
- David’s hunt for a four-piston solution on the OXO’s stock front swingarm ended with two options: flip a rear arm to mount the caliper underneath or fabricate a custom adapter plate sized for the OEM fork casting.【F:data/vesc_help_group/text_slices/input_part011.txt†L19400-L19403】

### Arnau’s Nami & G300 Race Prep
- Arnau’s Valencia plans involve a 22 S 10 P P45B pack feeding twin Ambrosini 75H motors via G300 controllers, plus a 10 mm RTR aluminium heat spreader to offset G300 thermal concerns while he waits on the battery build.【F:data/vesc_help_group/text_slices/input_part011.txt†L19418-L19443】

### Dualtron Achilleus Phase-Ceiling Diagnostics
- Dualtron Achilleus can’t exceed ~135 A phase despite 220 A targets; francois suspects saturation or battery sag and asked for fresh motor detection logs, while the rider confirmed a 16 S 7 P pack, Lonnyo 75H motors, and 10 AWG phase leads—pointing to either torque limits or observer tuning gaps.【F:data/vesc_help_group/text_slices/input_part011.txt†L19419-L19453】

### P45B Pack Current Guidance
- skrtt’s proposed 18 S 9 P P45B pack at 350 A battery draw equates to ~40 A per cell—aggressive but sustainable with cooling—so mentors advised staying 18 S if deck space is tight, since jumping to 20 S doesn’t change cell loading and voltage mainly governs top speed.【F:data/vesc_help_group/text_slices/input_part011.txt†L19546-L19568】

### Makerbase Ignition Latching & Launch Tuning
- JPPL confirmed the Makerbase ignition wires expect a momentary switch—touch the leads for ~1 s to latch on and ~3 s to latch off—so Roby MacGyver’s always-on controller needed a pushbutton instead of a maintained jumper.【F:data/vesc_help_group/text_slices/input_part011.txt†L20650-L20671】
- For stronger launches, JPPL suggested dropping APP positive ramping to 0.1 s, blending in throttle-curve gain, and then raising battery and phase current limits within the Motor Configuration → Current tab; Roby’s feedback that the scooter still felt soft highlighted the need to locate the phase-current slider hidden in that menu on Makerbase 75100 firmware.【F:data/vesc_help_group/text_slices/input_part011.txt†L20775-L20785】【F:data/vesc_help_group/text_slices/input_part011.txt†L20827-L20839】

### Tronic X12 Voltage Ambitions & Firmware Caps
- JPPL’s next Tronic X12 build targets a 22 S 10 P Molicel P45 pack (with spare 2 S/4 S blocks ready to experiment at 24 S) and he has already logged 150 km/h on 20 S; the controller’s firmware hard-stops at 600 A absolute unless riders flash a no-limit build, though JPPL feels ~400 A phase per motor with 100 A battery is already livable.【F:data/vesc_help_group/text_slices/input_part011.txt†L20690-L20725】
- Firmware 6.06 beta introduces an overmodulation option JPPL hopes will add more top speed beyond the field-weakening that delivered his prior 151 km/h run.【F:data/vesc_help_group/text_slices/input_part011.txt†L20717-L20724】

### Lonnyo 80 H & Swingarm Hardware Constraints
- Yamal’s attempt to fit Lonnyo 80 H motors showed the caliper can’t be mounted until the swingarm pivot bolts are lengthened; JPPL echoed that both the main axis and suspension hardware need longer studs, while he focuses on sourcing 22 S 10 P packs to keep the 80 H fleet fed.【F:data/vesc_help_group/text_slices/input_part011.txt†L20733-L20745】【F:data/vesc_help_group/text_slices/input_part011.txt†L20787-L20819】
- Yamal ultimately sold his Dualtron Thunder, is dismantling the Nami for steel-axle upgrades, and bought a Ninebot G2 for household duty, signalling a pivot toward lighter platforms while the heavy builds await new hardware.【F:data/vesc_help_group/text_slices/input_part011.txt†L20969-L21010】

### Custom Dropouts & Pack Packaging Experiments
- GABE’s stretched-frame project now concedes only 2 S 6 P can sit behind the fork, so he’s packaging a 22 S 6 P pack internally, pulling the hub forward ~15 cm to restore geometry, and machining the v1 fork dropouts (v2 lacks clearance) to free space for disc brakes.【F:data/vesc_help_group/text_slices/input_part011.txt†L20745-L20788】【F:data/vesc_help_group/text_slices/input_part011.txt†L21202-L21206】
- He plans to angle-grind vent ribs, add four steel beams for structure, and repaint the orange fork sections once the motor placement is finalised, underscoring how deep chassis surgery can be for 22 S sleeper builds.【F:data/vesc_help_group/text_slices/input_part011.txt†L21193-L21206】

### ESP32 Simple Display Bring-up & Wiring
- JPPL’s Simple VESC Display (ESP32) compile errors disappeared after reinstalling the Arduino IDE, selecting the proper board profile, and reflashing; he’s now iterating on custom graphics while confirming the firmware only needs VESC RX/TX plus 5 V (or 3.3 V) and ground, leaving at least one controller COMM port available in dual-drive setups.【F:data/vesc_help_group/text_slices/input_part011.txt†L21121-L21185】【F:data/vesc_help_group/text_slices/input_part011.txt†L21140-L21183】
- Smart Repair recommended jumping straight to VESC Express builds with SD-card and GPS support once the display is stable, and Jason encouraged porting the Express UI to the low-cost yellow-screen hardware for broader adoption.【F:data/vesc_help_group/text_slices/input_part011.txt†L21185-L21190】

### Battery Damage & Storage Lessons
- JPPL discovered three punctured cells in his new 22 S pack—likely overheated while copper busbars were soldered—and noted the scooter had been stored half-covered in rain, pushing him toward a full rebuild rather than trusting compromised cells.【F:data/vesc_help_group/text_slices/input_part011.txt†L21149-L21170】
- Haku’s review of the photos suggested wrapping and enclosure sealing were minimal, reinforcing the need for full insulation and weatherproofing when 400 A packs sit outdoors between rides.【F:data/vesc_help_group/text_slices/input_part011.txt†L21171-L21176】

### Hall Failures & VSS Sensorless Fallbacks
- Arnau’s hall board died with his old 85150, leaving the replacement 100 V controller stuck in noisy sensorless launches; 🇪🇸AYO#74🏁 walked him through enabling VSS (sensorless zero-start) and checking detection parameter symmetry, while reminding him that equalising the displayed observer values matters more than halls for basic operation.【F:data/vesc_help_group/text_slices/input_part011.txt†L21209-L21235】
- When the motor still struggled to self-start, Smart Repair advised checking ADC mappings for phantom brake inputs and considering that tight -amp readings look like charge current to some BMSs, explaining Arnau’s lingering cut-outs once the hall sensors failed.【F:data/vesc_help_group/text_slices/input_part011.txt†L21236-L21268】

### BMS Undervoltage & Charge-FET Failures
- Tristan’s over-current faults on a JBD-SP17S005 pack turned out to be the BMS FETs tripping—voltage sag forced the board to see the event as charge overcurrent—so Smart Repair recommended replacing the BMS entirely when settings look sane yet the cutoff persists.【F:data/vesc_help_group/text_slices/input_part011.txt†L21236-L21261】
- Even after a swap the problem lingered, strengthening the suspicion that controller-side faults or wiring glitches can mimic BMS undervoltage events if logs show negative current spikes.【F:data/vesc_help_group/text_slices/input_part011.txt†L21293-L21297】

### Rion / Tronic Hardware Sightings
- 🇪🇸AYO#74🏁 shared photos of a 100 V Rion X12 controller while Basti listed fresh 33×2 60 H motors with 125 mm dropouts and 4 mm banana leads for €300 delivered inside the EU, giving builders new sourcing leads for high-power drivetrains.【F:data/vesc_help_group/text_slices/input_part011.txt†L21207-L21255】
- Apo’s GT1D gained a second GT1 motor up front and was praised as “an absolute killer,” illustrating how dual-motor upgrades transform otherwise mild OEM platforms.【F:data/vesc_help_group/text_slices/input_part011.txt†L21424-L21428】

### Kaabo GT Build Snapshot
- ✨🇪🇸عمر’s latest setup pairs a 72 V 50 Ah Samsung 50S pack with a Kaabo 2000 W (33/3) hub and Spintend 85 V 240 A controller, anchoring the baseline before he experiments with external packs or higher current caps.【F:data/vesc_help_group/text_slices/input_part011.txt†L21368-L21371】

### Spintend 85240 Aux-Rail Short Lessons
- Shlomozero10 shorted the 12 V auxiliary rail to ground on a brand-new Spintend 85240 while powering lights, killing the controller until the buck regulator and (potentially) power stage are replaced—Haku advised escalating to James Soderstrom for component-level repair guidance before mixing 75200 and 85150 controllers over CAN as a stopgap.【F:data/vesc_help_group/text_slices/input_part011.txt†L21413-L21489】
- The incident reiterates that the aux step-down isn’t fused; tapping it for accessories needs careful insulation or an external buck to avoid destroying the logic board on contact.【F:data/vesc_help_group/text_slices/input_part011.txt†L21441-L21478】

### Custom Heatsink Planning for Spintend Stages
- Haku is templating aluminium fin stacks for his Wepoor’s Spintend 12-FET stage—mocking up cuts, mounting strips, and potential CNC work—after burning through multiple 85/250s, underscoring the need for purpose-built heatsinks when running high phase amps in enclosed decks.【F:data/vesc_help_group/text_slices/input_part011.txt†L21496-L21519】

### Geared Hub Reverse Rotation Fixes
- ToBeAsIAm’s Bafang C961 rear hub spins backward because of phase/hall mismatch; the group suggested tracing the intermediate extension harness (often black/white reversed for direction) or switching to a VESC for easier wire remapping and regen tuning.【F:data/vesc_help_group/text_slices/input_part011.txt†L19574-L19580】

### Flipsky FT85KS “Non-VESC” Controller Watch
- Yamal spotted AliExpress listings for the FT85KS 85 V/250 A controller marketed as “non-VESC”; JPPL confirmed it still runs Flipsky’s tool with auto-detection, but veterans cautioned it’s a divergent design and may lack community firmware support.【F:data/vesc_help_group/text_slices/input_part011.txt†L19696-L19712】

### Throttle-Response Tuning for New VESC Riders
- francois coached Hugo through eliminating a 5 s power lag by lowering throttle ramp time (~0.1–0.2 s per step) and raising `cc_startup_boost_duty` toward 0.04–0.06 for a snappier launch, warning that overshoot can induce current spikes.【F:data/vesc_help_group/text_slices/input_part011.txt†L19734-L19750】

### Mini Blade Custom Build Speed Limits
- SchweigePflicht’s single Mini Blade motor sees 120 km/h free-spin yet only 60 km/h loaded because the 20 S system is split into 13 S+7 S packs with just 55 A battery/80 A phase; peers recommended 100–120 A phase, 170–180 A absolute limits, and better pack balancing (more parallel on the 7 S side) to avoid voltage collapse.【F:data/vesc_help_group/text_slices/input_part011.txt†L19751-L19798】

### G300 Thermal Paste & Layout Findings
- JPPL’s teardown of a new G300 shows an 18-FET stack submerged in excessive thermal compound that conducts into the CNC housing; while messy, it leverages the case as a dual-sided heatsink, so he’s leaving the paste in place for now.【F:data/vesc_help_group/text_slices/input_part011.txt†L19802-L19831】

### JPPL Dual-Controller Harness Kit
- JPPL previewed a plug-and-play harness that pairs dual Thor300 controllers with a Spintend ADC board, VESC Express telemetry, 12 V lighting, horn, and shared on/off control—targeting 300 A-phase builds up to 20 S for riders who want synchronized dual drive without custom wiring.【F:data/vesc_help_group/text_slices/input_part011.txt†L19928-L19935】

### Spintend 85/150 22 S Upgrade Debate
- Arnau hopes to push a Spintend 85/150 to 22 S/150 A battery with Tokmas 500 A FETs, but Jason and GABE cautioned the six-FET powerstage and stock capacitors are the real limit—better to upgrade caps, skip e-brake, or move to an MP2/C350 class controller built for 30 S duty.【F:data/vesc_help_group/text_slices/input_part011.txt†L19984-L20003】

### Spintend ADC Adapter & Accessory Control
- Roby MacGyver learned that adding keyed ignition and lighting to a Makerbase/Spintend setup is easiest with the ADC Adapter V3 (~$30–35 from Spintend); the board exposes accessory power, while VESC Tool lets you clamp speed profiles and map lighting without coding.【F:data/vesc_help_group/text_slices/input_part011.txt†L20105-L20131】

### Shipping & Cooling Logistics for Thunder Builds
- JPPL and Shlomozero are iterating bolt-on heatsinks for Thunder 2 dual G300 installs—3D-printing radiator mounts from standard filament, polishing aluminium plates, and reusing dead 75200 fins—highlighting the need to verify insulation and share STL files for community reuse.【F:data/vesc_help_group/text_slices/input_part011.txt†L20246-L20261】

### Ninebot G2 Suspension & Fork Swaps
- ‘lekrsu’ warned that stock Ninebot G2 suspension arms crack quickly, so his build now runs a replacement front fork (with room for a second 65H motor) while he reinforces the chassis—Yamal confirmed the G2’s larger frame makes it a better city platform than the G30 despite extra moving parts.【F:data/vesc_help_group/text_slices/input_part011.txt†L20407-L20430】

### Waterproofing Nami & G300 Electronics
- Rainy-season riders are boxing in Nami electronics: Jason suggested conformal coating or sealed enclosures with automotive connectors, Lieven repurposes IKEA lunchboxes with silicone grommets, and Arnau noted G300 controllers already arrive with rubber gaskets for splash resistance.【F:data/vesc_help_group/text_slices/input_part011.txt†L20438-L20473】

### Makerbase Ignition & Shutdown Wiring
- JPPL walked Roby through shifting the Makerbase controller’s DC-DC switch (pin 9) into “control” mode, feeding 5 V to the AD15 enable pin via the key switch, and using VESC Tool’s ADC shutdown timer so the unit truly powers off after a delay instead of staying latched on.【F:data/vesc_help_group/text_slices/input_part011.txt†L20452-L20522】

### Makerbase Control Switch & Torque Tuning
- Roby confirmed the Makerbase 75100 needs a momentary switch that briefly shorts the ignition leads (≈1 s to latch on, ≈3 s to power back down) instead of a maintained jumper, and JPPL pointed him at Motor Config → Current → phase-amp limits plus App Config ramping (0.1 s) and throttle-curve gain to soften launch while adding low-end torque.【F:data/vesc_help_group/text_slices/input_part011.txt†L20659-L20671】【F:data/vesc_help_group/text_slices/input_part011.txt†L20827-L20838】

### Tronic X12 Speed Chassis Planning
- JPPL is coating both the logic and power stages for corrosion resistance, then waiting on a 22 S10 P P45B pack; he notes Tronic X12s are firmware-limited to ~600 A phase (650 A only with no-limit firmware), rated for 24 S max, and already pushed his 75/80 H Lonnyo setup to 150 km/h at just 20 S/100 A battery per controller.【F:data/vesc_help_group/text_slices/input_part011.txt†L20678-L20710】

### JPPL Pack Damage & Weatherproofing Lessons
- The new copper busbar pack arrived with three perforated cells—likely from aggressive solder heat—so JPPL is re-testing the 22 S build, evaluating whether to start over, and stressing that the prior 400 A pack was ruined by rain after being parked outside without full enclosure.【F:data/vesc_help_group/text_slices/input_part011.txt†L21149-L21170】

### ESP32 Simple VESC Display Progress
- Reinstalling the Android (Arduino) IDE, choosing the right ESP32 board profile, and wiring RX/TX/GND/5 V let JPPL flash the Simple VESC Display; he’s now experimenting with custom graphics while Smart Repair suggests porting VESC Express with SD/GPS logging, and Jason confirms parameter write support is still pending.【F:data/vesc_help_group/text_slices/input_part011.txt†L21121-L21190】【F:data/vesc_help_group/text_slices/input_part011.txt†L21200-L21201】

### GABE’s 22 S Sleeper Geometry Work
- GABE is shrinking his 22 S commuter frame by pushing the rear assembly ~15 cm forward, adding four internal steel beams, and planning angle-grinder cuts on the v1 forks so disc brakes clear; the revisions leave room for a 22 S6 P internal pack (no external 2 S needed) while he juggles thinner PMT tire options to extend range.【F:data/vesc_help_group/text_slices/input_part011.txt†L20800-L20825】【F:data/vesc_help_group/text_slices/input_part011.txt†L21193-L21206】【F:data/vesc_help_group/text_slices/input_part011.txt†L21355-L21367】

### Drivetrain & BMS Troubleshooting Clinic
- Arnau’s Makerbase 100 V controller lost its hall sensors when an 85/150 failed, leaving the motor hard-starting; 🇪🇸AYO recommended configuring VSS sensing while Smart Repair had Tristan inspect ADC mappings after a JBD-SP17S005 kept tripping undervoltage via charge overcurrent, prompting a BMS swap and renewed debate over JK vs. Daly hardware for >60 A discharge.【F:data/vesc_help_group/text_slices/input_part011.txt†L21209-L21280】【F:data/vesc_help_group/text_slices/input_part011.txt†L21236-L21266】【F:data/vesc_help_group/text_slices/input_part011.txt†L21245-L21260】

### Parts & Build Notes
- Basti flagged new 33×2 60 H hubs with 125 mm dropouts and 4 mm banana phases available in the EU for about €300 shipped, giving builders another option for compact dual drives.【F:data/vesc_help_group/text_slices/input_part011.txt†L21207-L21208】
- عمر shared a Kaabo 33/3 motor build running a 72 V 50 Ah Samsung 50S pack on a Spintend 85/240, underscoring that the controller comfortably supports higher-voltage single-motor setups when paired with stout cells.【F:data/vesc_help_group/text_slices/input_part011.txt†L21368-L21371】

### Spintend 85/240 Aux-Rail Cautionary Tale
- Shlomozero shorted the 12 V auxiliary leads on a brand-new 85/240, leaving it unresponsive and forcing him to consider a buck-board replacement or fall back to mixing a 75/200 with an 85/150 over CAN; James is expected to advise on sourcing the “12 buck” logic board, and the incident highlights the need for fused lighting taps on the aux rail.【F:data/vesc_help_group/text_slices/input_part011.txt†L21413-L21489】

### Makerbase Ignition & Launch Tuning
- Roby MacGyver’s Makerbase 75100 stayed powered until JPPL explained that the AD15 lead needs a 5 V feed through a momentary switch—briefly bridging controller 5 V to AD15 toggles the latch, while VESC Tool’s App → ADC shutdown timer can be set to power the controller down after a chosen delay.【F:data/vesc_help_group/text_slices/input_part011.txt†L20502-L20524】【F:data/vesc_help_group/text_slices/input_part011.txt†L20652-L20671】
- For snappier launches JPPL recommended dropping positive ramping time toward 0.1 s, adding throttle-curve percentage, and confirming higher battery/phase limits in Motor → Current so the 75100 actually delivers the extra torque Roby is chasing.【F:data/vesc_help_group/text_slices/input_part011.txt†L20776-L20785】

### Tronic X12 24 S Plans & Benchmarks
- JPPL is conformal-coating both logic and power boards on his dual X12 stack to protect against moisture, warning that the sealant will be tedious to remove if warranty service is ever required.【F:data/vesc_help_group/text_slices/input_part011.txt†L20677-L20685】
- He has a 22 S 10 P P45 pack en route, keeps spare 2 S/4 S modules to stretch the setup to 24 S, and noted the stock firmware clamps absolute current around 600 A (despite 650 A marketing) unless a no-limit build is flashed.【F:data/vesc_help_group/text_slices/input_part011.txt†L20690-L20705】
- Earlier 20 S runs already hit ~150 km/h with roughly 400 A phase and ~100 A battery per controller, and he expects 24 S plus the new overmodulation option in 6.06 beta to unlock even higher top speed without raising current.【F:data/vesc_help_group/text_slices/input_part011.txt†L20700-L20723】

### Ninebot G2 Pivot & Nami Maintenance
- Yamal confirmed the Lonnyo 80 H swap on his Nami needs longer swingarm bolts to clear the caliper, so he’s sourcing extended hardware before reassembling the wheelset.【F:data/vesc_help_group/text_slices/input_part011.txt†L20733-L20744】
- He sold his Dualtron Thunder (and the RFP frame) to focus on a Ninebot G2 that should arrive within days, partly to motivate his wife to ride while he finishes the Nami’s steel-axle and arm-length upgrades.【F:data/vesc_help_group/text_slices/input_part011.txt†L20969-L20997】
- The outgoing Spintend-powered build has already logged roughly 2,500 km at 200 A battery/phase without failures, underscoring the payoff from meticulous setup even as he contemplates the tamer G2 for daily use.【F:data/vesc_help_group/text_slices/input_part011.txt†L20998-L21013】

### Wepoor Heatsink Fabrication Push
- Haku is hunting for local machinists to trim large aluminium fins so the Spintend stage can mount flush on the Wepoor without CNC costs, with Yamal suggesting removing one fin to create a bolt strip and both agreeing that direct-to-heatsink mounting will cool better than remote brackets.【F:data/vesc_help_group/text_slices/input_part011.txt†L20866-L20903】【F:data/vesc_help_group/text_slices/input_part011.txt†L21313-L21319】【F:data/vesc_help_group/text_slices/input_part011.txt†L21504-L21518】

### High-Current Usage Anecdotes
- Yamal has already logged 2,500 km hammering 200 A battery/phase on his Spintend-powered build without failures—contrasting Haku’s repeated stage deaths and reinforcing the value of clean installs and conservative testing before chasing more power.【F:data/vesc_help_group/text_slices/input_part011.txt†L21460-L21485】

### Mini Hub Spacer Fabrication & Thermal Stack
- GABE is closing the gap on his 250 W commuter hub by sandwiching aluminium plates with thermal paste and having Hackintosh print a 10 mm spacer, aiming to retain acceptable heat transfer despite the thicker adapter.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L21492-L21536】

### Seven VESC Shipments & Review Gap
- Face de Pin Sucé relayed that early Seven VESC units “perform well,” yet a four-month-old order of six controllers has only yielded two deliveries so far, underscoring supply bottlenecks.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L21556-L21585】
- Yoann confirmed Roscheeee bought a pair for a client but kept them back for personal validation, while noting the only coverage so far is an image-based video—there are still no substantive field reviews to benchmark against alternatives.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L21620-L21680】

### Flipsky Capacitor Failures & Component Quality Questions
- David’s Flipsky controller dropped to a 14 V reading on a 20 S pack after a second capacitor explosion, drawing advice that simple cap swaps may not help because subsequent replacements have also failed.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L21296-L21758】
- ‘lekrsu’ and Haku blamed poor component choices rather than layout, reinforcing ongoing skepticism about Flipsky’s parts bin for high-power duty.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L21745-L21823】

### Yamal’s 25 kW Ambitions & Motor Plans
- Haku joked that Yamal’s current setup could push 25 kW before conceding the build lacks motor-temperature sensing; Yamal agreed that stepping up to LY hubs with 10 mm phase leads (plus refreshed bearings and steering axle) is on the wish list once his next project settles.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L21860-L21899】

### M365 Sleeper Rebuild & Welder Downtime
- Stripped threads on the Xiaomi Pro 2 frame forced GABE to migrate the sleeper project into an M365 chassis with intact M3 mounts, where he plans to finish soldering a P42A pack once he buys more solder.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L21901-L21975】
- A blown board in his spot welder now throws an E02 fault; Haku recognised the failure as a MOSFET issue he once solved with upgraded parts, shared that his replacement board only charges to 5.4 V, and even pointed to a heavier Glitter 811H welder as a potential upgrade if repairs stall.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L22311-L22668】

### Flipsky 75100 Regen Cutoff Anecdotes
- PuneDir reported his Flipsky 75100 dies only when regen braking triggers a cutoff—normal battery cutoffs don’t recreate the fault—while Mirono countered that his own unit has survived nine months, highlighting inconsistent field reliability and the need to tame regen ramps on fragile units.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L22755-L23007】

## Follow-ups / Open Questions
- Confirm that GABE’s 10 mm spacer and aluminium stack keep the 250 W hub cool once Hackintosh’s print is in service, and capture any thermal measurements that justify the workaround.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L21492-L21536】
- Log the first substantial field reports on the Seven VESC minis and note whether the outstanding four controllers from the early six-pack order finally ship.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L21556-L21680】
- Track the autopsy on David’s Flipsky failure to see if the repeated capacitor pops reveal a deeper parts-quality issue or prompt a controller swap.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L21296-L21758】
- Capture whether Yamal upgrades to LY motors with 10 mm phases or adds motor-temp sensing before leaning on 25 kW targets.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L21860-L21899】
- Follow GABE’s spot-welder repair or replacement (including the E02 MOSFET fault and the Glitter 811H alternative) so his M365 pack work can resume.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L22311-L22668】
- Document any regen-ramp or firmware tweaks that prevent PuneDir’s Flipsky 75100 from dying on regen brake cutoffs while validating Mirono’s long-term survivability claims.【F:data/raw/telegram_exports/vesc_help_group/input_part011.json†L22755-L23007】
- Publish a Lonnyo 70H sealing/bearing replacement checklist (tools, seals, torque) so builders can replicate Smart Repair’s preventative maintenance.【F:data/vesc_help_group/text_slices/input_part011.txt†L16325-L16333】
- Capture Smart Repair’s finished documentation on the GT pack’s copper-bridged busbars and note whether the 22 S rebuild reduces the 12 V sag he currently sees at 500 A phase.【F:data/vesc_help_group/text_slices/input_part011.txt†L16758-L16790】
- Verify whether KierreKikkeli’s ADC recalibration and hardware-switch check eliminate the Xiaomi brake glitch, and log any additional wiring or filtering tweaks he needed.【F:data/vesc_help_group/text_slices/input_part011.txt†L16193-L16217】
- Confirm Arnau’s Ubox stops tripping ABS after flashing the no-limit firmware, higher ABS ceiling, and any traction-control experiments based on francois’ notes.【F:data/vesc_help_group/text_slices/input_part011.txt†L17240-L17252】【F:data/vesc_help_group/text_slices/input_part011.txt†L17315-L17383】
- Track community validation (or rejection) of the LLM-generated back-EMF traction-control routine before recommending it more broadly.【F:data/vesc_help_group/text_slices/input_part011.txt†L17380-L17383】
- Monitor Yamal’s Thunder 3 homologation steps—registration, insurance, and whether the legal hardware matches the certified 72 V spec once it hits the road.【F:data/vesc_help_group/text_slices/input_part011.txt†L16543-L16558】
- Determine if anyone confirms the 75100 Pro V2 servo header’s voltage tolerance or publishes an Arduino-based PAS adapter guide for three-wire cadence sensors.【F:data/vesc_help_group/text_slices/input_part011.txt†L16505-L16621】
- Capture a Makerbase 75100 control-switch quick-start (momentary button wiring plus ramp/torque presets) once Roby MacGyver dials in his settings.【F:data/vesc_help_group/text_slices/input_part011.txt†L20652-L20838】
- Track JPPL’s rebuild of the 22 S 10 P pack (plus the optional 2 S/4 S extensions for 24 S testing) after the copper-induced cell damage, and document whatever weatherproofing replaces the rain-soaked 400 A version.【F:data/vesc_help_group/text_slices/input_part011.txt†L20690-L20705】【F:data/vesc_help_group/text_slices/input_part011.txt†L21149-L21158】
- Follow GABE’s 22 S sleeper packaging work (dropout cuts, brake clearance, tire choices) until the final geometry and thermal logs are published.【F:data/vesc_help_group/text_slices/input_part011.txt†L20786-L20822】【F:data/vesc_help_group/text_slices/input_part011.txt†L21193-L21206】
- Monitor Haku’s custom heatsink solution on the Wepoor Spintend stage and whether the ANT BMS tweaks keep the new powerstage alive.【F:data/vesc_help_group/text_slices/input_part011.txt†L20840-L20933】【F:data/vesc_help_group/text_slices/input_part011.txt†L21493-L21520】
- Track JPPL’s Simple VESC Display firmware progress and whether the community ports VESC Express with SD/GPS logging onto it.【F:data/vesc_help_group/text_slices/input_part011.txt†L21121-L21190】
- Log outcomes once Arnau restores hall sensing (or finishes the VSS setup) on the Makerbase 100 V/100 A controller.【F:data/vesc_help_group/text_slices/input_part011.txt†L21209-L21280】
- Confirm if Tristan resolves the JBD-SP17S005 BMS cut-outs (replacement hardware, regen settings, or controller tweaks).【F:data/vesc_help_group/text_slices/input_part011.txt†L21237-L21271】
- Capture 🇪🇸AYO#74🏁’s long-term data comparing the Tronic X12 to his 250/250R and the eventual Nami integration settings.【F:data/vesc_help_group/text_slices/input_part011.txt†L21324-L21353】
- Follow Shlomozero’s 85240 repair or interim 75200×85150 CAN pairing to document safe aux-rail tapping practices.【F:data/vesc_help_group/text_slices/input_part011.txt†L21413-L21458】
- Note عمر’s 72 V/50 Ah Kaabo build results once traction and thermal data come back.【F:data/vesc_help_group/text_slices/input_part011.txt†L21368-L21371】
- Watch Yamal’s transition to the Ninebot G2 and the pending Nami axle/arm hardware swap for city commuting.【F:data/vesc_help_group/text_slices/input_part011.txt†L20953-L21012】
- Continue review from line 22101 onward (2025-03-09T23:33 and later) to finish input_part011.txt.
- Track Shlomozero’s Thunder build as he debugs CAN power-sync behaviour and decides whether to run dual 85/240s once the spacer install is proven.【F:data/vesc_help_group/text_slices/input_part011.txt†L19016-L19035】
- Capture Smart Repair’s next revision of the ESP32 profile-switch script (or production hardware) and whether CAN commands stay reliable with debounce and voltage checks in place.【F:data/vesc_help_group/text_slices/input_part011.txt†L18920-L18926】【F:data/vesc_help_group/text_slices/input_part011.txt†L19080-L19088】
- Note whether GABE upsizes the 20 S commuter pack beyond 2 P or adds waterproofing now that he’s confirmed the deck can swallow a 7 P layout.【F:data/vesc_help_group/text_slices/input_part011.txt†L17990-L18017】
- Watch for a documented recipe that gets a Ninebot G2 safely to 80 km/h—dropout hardware, controller choice, and braking—to complement the current crowd-sourced checklist.【F:data/vesc_help_group/text_slices/input_part011.txt†L18290-L18485】
- Confirm whether Yamal’s Thunder build actually squeezes dual Sevens and a 22 S 11 P Eve 40PL pack into the RFP frame and if he ultimately shifts to 75H 22/3 motors after testing torque vs. heat on the Nami.【F:data/vesc_help_group/text_slices/input_part011.txt†L14641-L14672】
- Check that Maximus Brokus resolves the Heatbox ignition-port wiring and capture the correct pinout for future reference.【F:data/vesc_help_group/text_slices/input_part011.txt†L14709-L14730】
- Log Hackintoshhhh’s long-term results running 160–180 A battery on the modded Ubox 85/150, including thermal data on the Tokmas/JMSh1001ATLQ MOSFET swap.【F:data/vesc_help_group/text_slices/input_part011.txt†L14751-L14816】
- Track Shlomozero’s Thunder 2 front-controller experiments (cooling plate, thermal pads, throttle temps) and whether the 85150 holds 230 A phase without derating.【F:data/vesc_help_group/text_slices/input_part011.txt†L14930-L14958】
- Follow skrtt’s Victor build to see if he keeps hall-less operation or retrofits sensors once the C350 is pushing 50 A per motor.【F:data/vesc_help_group/text_slices/input_part011.txt†L14975-L15071】
- Capture Smart Repair’s water-cooling implementation (pump choice, radiator placement, temps) and whether عمر’s 2 kΩ pull-down fully calms the 300X throttle interference.【F:data/vesc_help_group/text_slices/input_part011.txt†L15737-L15945】
- Record Jason’s progress fitting 30 S packs around the 22 mm-tall MP2 stack and whether he swaps to 22×3 motors to reach the desired 100 km/h.【F:data/vesc_help_group/text_slices/input_part011.txt†L15805-L15876】
- Track whether Haku’s ANT BMS threshold tweaks and regen limits stop the Wepoor from nuking front stages—or if he ultimately moves to heavier 18 FET hardware.
- See if Star / Delta Master’s replacement 85150 powerstage survives once the case is re-tapped and whether Hackintoshhhh documents the board swap.
- Capture Smart Repair’s final 1WD/2WD switching recipe (hardware wiring, Lisp/ADC scripts) that avoids CAN conflicts.
- Track Smart Repair’s GT battery rebuild and the planned front Ubox 250 / rear Tronic X12 swap to see if the new pack cures voltage sag.
- Follow Hurriicane’s 75100 V2 repair to confirm the missing 12 V rail fix restores normal boot behavior without further gate-driver damage.
- Document Pandalgns’s Halo rebuild results after inspecting harnesses and replacing the burned controller/display.
- Follow Pandalgns’s Lonnyo 100 H mounting plan—custom shock brackets, wheel clearance, and controller pairing once the hardware arrives.【F:data/vesc_help_group/text_slices/input_part011.txt†L15539-L15573】
- Track GABE’s 22 S sleeper frame work—dropout machining, steel reinforcements, and tire selection—until the 22×3 70 H build is riding.【F:data/vesc_help_group/text_slices/input_part011.txt†L20745-L20822】
- Gather best practices on QS10/QS8 polarity marking and confirm whether QS10 adoption reduces arcing on >300 A builds.
- Note GABE’s long-term data running the Xiaomi dash, high-power M365 pack, and disabled BMS safeguards to ensure the commuter remains safe.
- Monitor GABE’s 250–350 W hub experiments to confirm whether a 35 A phase cap and added temp sensing stop further motor burnouts.
- Record any firmware changes that let Matthew exceed the present ~150 A phase ceiling on single Ubox setups without tripping ABS faults.
- Monitor Jan’s multi-controller kart experiment for insights on throttle coordination, torque vectoring, and fan control over CAN.
- Confirm whether عمر’s Kaabo GT bridge remains stable after the overnight power cycle and if damaged halls or CAN wiring need replacement.
- Follow Franchesco’s warranty claim or teardown on the failed 85 V/250 A Ubox to document root cause and replacement hardware.
- Capture pricing, availability, and feature lock-in once the VESC Bridge V2 enters production (e.g., BMS support, turn-signal I/O, OTA cadence).
- Record yoann tsobanoglou’s latency fixes or release plans for the VESC Express-based control board.
- Capture عمر’s CrowPanel/ESP32 dashboard build notes once the LVGL touchscreen is wired alongside the CAN BMS.
- Monitor Yamal’s 80H 33×2 upgrade decision, including traction-control tuning, battery current settings, and real-world range/speed logs.
- Track Yamal’s investigation into the Nami overvoltage readings (ADC divider checks, voltage calibration).
- Log GABE’s progress finishing the Mijia pack (spot-welding, TVS diode repair, pack monitoring) and any rebuild with fresh cells.
- Note Morten Jensen’s revised Vsett 10 motor settings once he reins in saturation.
- Watch what Haku ultimately does with the Jetson build (sale vs. rebuild) and whether a pedal-assist successor takes shape.
- Determine whether Giuseppe’s Makerbase 75100V2 failure is recoverable (firmware, wiring, or hardware defect) and whether Makerbase issues revised guidance for the epoxy-backed boards.
- Follow up on David’s Inokim OXO brake adapter or swingarm swap to document a repeatable four-piston solution.【F:data/vesc_help_group/text_slices/input_part011.txt†L19400-L19403】
- Track Arnau’s attempt to harden the Spintend 85/150 for 22 S duty (MOSFET/cap upgrades, absolute current limits) and whether he pivots to the C350 alternative.【F:data/vesc_help_group/text_slices/input_part011.txt†L19970-L20053】【F:data/vesc_help_group/text_slices/input_part011.txt†L20187-L20204】
- Confirm whether Tristan eliminates the JBD-SP17S005 undervoltage trips after swapping BMS hardware or adjusting controller regen settings.【F:data/vesc_help_group/text_slices/input_part011.txt†L21236-L21297】
- Monitor JPPL’s dual-controller harness rollout and any published wiring diagrams or component lists once the kit ships.【F:data/vesc_help_group/text_slices/input_part011.txt†L19928-L19935】
- Capture JPPL’s Simple VESC Display refinements and whether his ESP32 graphics package or wiring notes get published alongside the harness kit.【F:data/vesc_help_group/text_slices/input_part011.txt†L21121-L21190】
- Check whether Shlomozero finalizes the Thunder 2 cooling stack using 75200 radiators or other bolt-on heat spreaders, and gather temperature data once the build runs.【F:data/vesc_help_group/text_slices/input_part011.txt†L20201-L20261】
- Log whether Shlomozero revives the shorted Spintend 85240 (buck replacement, powerstage swap, or warranty) before mixing 75200/85150 controllers over CAN.【F:data/vesc_help_group/text_slices/input_part011.txt†L21413-L21489】
- Verify Roby MacGyver’s Makerbase ignition wiring and shutdown settings resolve his always-on controller issue before sharing a quick-start guide.【F:data/vesc_help_group/text_slices/input_part011.txt†L20399-L20454】
- Capture Hugo’s final ABS/phase-current settings after raising the overcurrent threshold to eliminate throttle cutouts.【F:data/vesc_help_group/text_slices/input_part011.txt†L20441-L20515】
- Track ‘lekrsu’s long-term results reinforcing the Ninebot G2 fork and suspension to confirm durability once the second 65H motor is mounted.【F:data/vesc_help_group/text_slices/input_part011.txt†L20407-L20430】
- Document whichever waterproofing approach (conformal coat vs. sealed enclosure) Nami riders adopt so the electronics stay protected without sacrificing serviceability.【F:data/vesc_help_group/text_slices/input_part011.txt†L20438-L20473】
- Capture Haku’s final fix for the Wepoor front powerstage failures—whether ramp tweaks, ANT BMS settings, regen changes, or heavier-duty controllers solve the issue.
- Document Mattia’s ANT BMS setup once the wiring/app configuration stabilizes and note any firmware updates needed beyond the shared APK.
- Track progress on Jason’s 30 S “JESC” controller and open-source 32 S VESC BMS, including physical fitment in G30 decks and firmware milestones.
- Follow Jason and NetworkDir’s LVGL dash/touch profile work until a reproducible setup is published.
- Record how Arnau clears the Spintend 85 V/150 A ABS overcurrent fault on the Voyage display stack and whether Kron Vark resolves the Vsett 10 E10/Lisp integration.
- Track whether haku resolves the Jetson high-voltage fault and finds sustainable cooling/output for the 20 S Jetson build.
- Document if GABE replaces or repairs the failed welder board, recovers the missing M4 Pro 2 spacer CAD, and finishes the modular battery builds.
- Track haku’s mini BMX “Peak G30” build for torque goals, pack sizing, and controller thermal results once it rides.
- Capture the resolution to Matthew’s throttle flutter and any tuning changes that solve it.
- Note whether Adri (or others) confirms success with `no_hw_limit.bin` on the Ubox 85 V controllers or identifies alternative firmware tweaks.
- Follow up on Ric.R.M. and “No” to see if their no-limit firmware installs stay stable once voltage settings and throttle calibrations are dialed, and whether the LCD4 display integration succeeds.
- Watch for Smart Repair’s documentation on pairing ESP32 touchscreens with Ubox controllers and any guidance on Mini Ubox reliability for mid-power builds.
- Capture performance data once Pandalgns runs the dual MKS 84HP controllers in the Halo chassis (phase/battery limits, thermal behaviour, firmware stability).
- Track Smart Repair’s success balancing the Ubox 250/150 pair—whether via profiles, Lisp/CAN overrides, or future bridge firmware updates—and whether the CAN logging changes surface the dropout cause.
- Capture Smart Repair’s documentation if the CrowPanel/ESP32 dash makes it into the GT harness.
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
- Gather Finn’s long-term data on the 85/150 beta boards (3 mm baseplate cooling, external heatsink options, safe current limits).
- Track NetworkDir’s or others’ progress on Dualtron display Lisp scripts and confirm if luffydnoob keeps the stock throttle once porting is complete.
- Revisit Nawfal’s MKS 84 HP speed cap to see if firmware, pole count, or hardware changes restore 80 km/h performance.
- Log Jerome’s GT2 road tests once the 20 S 9 P pack and 100Balance BMS are paired with Smart Repair’s harnesses.
- Note community feedback on the 4 kW Huawei/Guli telecom chargers (thermal behavior, CAN/app quirks, DC-input support) after extended use.
