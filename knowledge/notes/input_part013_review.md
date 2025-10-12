# input_part013.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part013.txt`
- Coverage:
  - Batch 1: 2025-06-04T18:16:49 through 2025-06-06T22:55:51 (lines 1-1135)
  - Batch 2: 2025-06-07T00:00:56 through 2025-06-10T23:33:08 (lines 1136-2200)
  - Batch 3: 2025-06-10T23:33:49 through 2025-06-15T00:40:45 (lines 2201-3700)
  - Batch 4: 2025-06-15T18:32:54 through 2025-06-20T06:07:53 (lines 3701-5200)
  - Batch 5: 2025-06-20T06:07:54 through 2025-06-26T15:05:55 (lines 5201-6700)
  - Batch 6: 2025-06-26T15:30:52 through 2025-06-29T10:53:30 (lines 6701-7999)
  - Batch 7: 2025-06-29T10:53:53 through 2025-07-04T22:20:33 (lines 8000-9499)
  - Batch 7 addendum: 2025-07-02T18:22:49 through 2025-07-08T06:22:53 (lines 9001-10500)
  - Batch 8: 2025-07-04T22:26:06 through 2025-07-09T04:40:27 (lines 9500-10999)
  - Batch 9: 2025-07-09T04:48:27 through 2025-07-12T19:57:16 (lines 11000-12499)
  - Batch 10: 2025-07-13T15:08:22 through 2025-07-20T07:28:46 (lines 12500-13999)
  - Batch 11: 2025-07-20T07:29:01 through 2025-07-25T06:44:29 (lines 14000-15499)
  - Batch 12: 2025-07-25T06:44:29 through 2025-07-29T20:13:48 (lines 15500-16999)
  - Batch 13: 2025-07-29T20:32:50 through 2025-08-07T16:24:22 (lines 17000-18499)
  - Batch 14: 2025-08-07T16:30:43 through 2025-08-13T03:12:57 (lines 18500-19999)
  - Batch 15: 2025-08-13T03:56:01 through 2025-08-17T05:12:44 (lines 20000-21499)
  - Batch 16: 2025-08-17T08:17:28 through 2025-08-18T21:59:27 (lines 21500-22235)
  - Next starting point: complete (file ends at line 22235)

## Key Findings

### Batch 1 Highlights (lines 1–1499)

#### Motor Control & Performance
- Stone Gasm’s 20×70 kV setup only gained ≈19 km/h of freewheel speed when he added 25 A of field weakening (66 → 84 km/h) and even at the 35 A hardware cap the build topped out around 96 km/h, underscoring limited FW headroom without gearing or voltage changes.【F:data/vesc_help_group/text_slices/input_part013.txt†L29-L31】
- Dualtron Storm and X2 frames now ship with hall sensors, making VESC swaps less sensor-intensive than earlier generations.【F:data/vesc_help_group/text_slices/input_part013.txt†L160-L165】
- Smart Repair’s Tronic X12 (24 S, ≲30 kW) and Rob Ver’s Ubox 240 builds share 331 A MOSFET limits; Rob caps 80 H hubs at 200 A battery / 310 A phase (70 H at 190 A/190 A) while Smart Repair runs Spintend 85250s at 150 A battery / 360 A phase—practical guardrails for high-current tuning.【F:data/vesc_help_group/text_slices/input_part013.txt†L364-L369】
- Rob cured Nami harness overheating by upgrading to 10 AWG phase leads, now holding 116 A battery and 240 A phase, while noting the Tronic X12 logic rail only supplies 5 V at 150 mA, so heavy peripherals still need an auxiliary buck.【F:data/vesc_help_group/text_slices/input_part013.txt†L474-L486】
- Hackintoshhhh’s MOT1111T-fed Spintend 85250 tolerates 480 A phase bursts per controller once the silicon and cooling are uprated, confirming the headroom available with upgraded hardware.【F:data/vesc_help_group/text_slices/input_part013.txt†L799-L804】
- Builders debating Infineon “TOLL” packages versus taller TOLT MOSFETs found the latter still shed heat better at 22 S+, provided the input capacitance is increased accordingly.【F:data/vesc_help_group/text_slices/input_part013.txt†L787-L797】【F:data/vesc_help_group/text_slices/input_part013.txt†L1082-L1088】

#### Ninebot G2 & Small-Chassis Builds
- Jose’s Ninebot G2 Max sleeper plan pairs a 20 S 6 P Molicel pack, single Q5 Evo rear hub, Magura MT7 caliper with a Shimano Deore lever, and VESC control to stay off the DGT registration list while keeping steering light for wheelies.【F:data/vesc_help_group/text_slices/input_part013.txt†L205-L233】
- Unlocking the stock controller hinges on ST-Link V2 access—Jose is still hunting a guide—while Yamal is waiting to swap in a 3Shul 700/1400 plus dual LY/Lonnyo 100 H hubs on 50PL cells before flashing anything.【F:data/vesc_help_group/text_slices/input_part013.txt†L221-L243】
- Alternate stealth builds lean on LY 65 H 17×4 hubs with Ubox 85/240 controllers and 20 S 5–6 P packs to preserve the factory silhouette, though Jose warns the deck hardware needs careful packaging to hit 6 P cleanly.【F:data/vesc_help_group/text_slices/input_part013.txt†L252-L260】
- Diego validated 16 S on the OEM controller after upgrading its capacitors and is scoping 18–20 S VESC conversions once he confirms compartment volume.【F:data/vesc_help_group/text_slices/input_part013.txt†L343-L346】
- Smart Repair reattaches the G2 swingarm with two bolts plus sleeves and supplements it with a 3D-printed mudguard bracket—simple hardware worth capturing for future conversions.【F:data/vesc_help_group/text_slices/input_part013.txt†L587-L587】

#### Hardware Fitment & Wiring
- Monorim front suspension with an EXA shock is Jose’s go-to for G2 conversions, but he replaces every fastener with quality M6 hardware because the supplied screws strip easily.【F:data/vesc_help_group/text_slices/input_part013.txt†L337-L343】
- Smart Repair caps GT-style decks near 208 cylindrical cells and reminds builders that 125 mm dropouts require major swingarm work for 60 H+ hubs.【F:data/vesc_help_group/text_slices/input_part013.txt†L514-L528】
- Mixing Kaabo Thunder 2 controllers (45 A front / 60 A rear) keeps speed voltage-limited but costs thrust; either shunt the 45 A unit or source a matching board for symmetry.【F:data/vesc_help_group/text_slices/input_part013.txt†L544-L562】
- Martin Kaktits flagged PTFE insulation tearing when 6 mm² leads are pulled through motor axles, so abrasion-resistant sleeving should be part of any thick-phase wiring guide.【F:data/vesc_help_group/text_slices/input_part013.txt†L172-L172】

#### Tires, Tubes & Ride Prep
- Noname logged just three flats in four years by running Ulip tubes dusted with baby powder and banning burnouts, though he still concedes tubeless is superior where rims cooperate.【F:data/vesc_help_group/text_slices/input_part013.txt†L597-L603】
- Manual pumps struggle to seat tubeless tires on G30 rims with Chaoyang rubber, whereas Ulip tires on Bolt hubs inflate cleanly—another reason to budget powered inflators for tubeless work.【F:data/vesc_help_group/text_slices/input_part013.txt†L607-L611】

#### Battery Sourcing & Pack Assembly
- NKON can take a month to deliver popular cells like EVE 40PL, whereas Vapcell ships in 3–5 days via DHL/UPS for ~€150–€229 but often mixes voltages that need individual top-ups before welding.【F:data/vesc_help_group/text_slices/input_part013.txt†L819-L1006】
- Vet Alibaba listings for “Shenzhen Vapcell Technology” to dodge clones; NKON’s matched production lots remain easier for taxes and documentation despite longer waits.【F:data/vesc_help_group/text_slices/input_part013.txt†L946-L1003】
- Jose can strip lightly used Molicel P45B cells from Stark Varg motorcycle packs for roughly €1.2 each if cycle-life checks pan out, while Rob Ver champions tabless cells for keeping pack temps within ≈3 °C of ambient under load.【F:data/vesc_help_group/text_slices/input_part013.txt†L1034-L1041】

#### Controller Diagnostics & Reliability
- MakerBase Express hides its Wi-Fi aerial under the combined BT antenna—explaining the missing whip on new boards—and Pandalgns’ controller failures point to CAN resistors or regulators cooking after a hall-board shorted against the motor shell.【F:data/vesc_help_group/text_slices/input_part013.txt†L1122-L1240】【F:data/vesc_help_group/text_slices/input_part013.txt†L1673-L1674】
- Arnau Martinez Casals logged another Spintend 85250 dropout: the unit stayed powered and discoverable but refused Bluetooth connections, mirroring logic-rail faults other riders are chasing.【F:data/vesc_help_group/text_slices/input_part013.txt†L1490-L1496】
- Basti’s hardware-no-limit controller is throwing VESC Tool 6.06 motor-detection errors, so regression testing the new wizard stays on the troubleshooting list.【F:data/vesc_help_group/text_slices/input_part013.txt†L169-L170】

#### High-Power Builds & Chassis Notes
- GT Pro Karl’s Wolf King GT Pro runs dual Ubox 150s on custom 250 A firmware at 72 V with 50 A battery / 210 A phase per controller, plus 55 A of field weakening for 77 mph freewheel and ≈66 mph road speed; the deck reinforcement keeps the 400 lb-rated chassis housing both controllers and charger.【F:data/vesc_help_group/text_slices/input_part013.txt†L1152-L1265】
- Smart Repair’s rear-biased setup pushes 420 A phase to the back and 120 A up front to balance launch torque with traction—a template for asymmetric tuning.【F:data/vesc_help_group/text_slices/input_part013.txt†L416-L422】

#### Follow-Ups
- Document abrasion-resistant sleeving options for ≥6 mm² phase leads so installers stop shredding PTFE insulation inside axles.【F:data/vesc_help_group/text_slices/input_part013.txt†L172-L172】
- Publish a Ninebot G2 Max VESC conversion guide covering ST-Link flashing, 6 P battery packaging, and suspension/mudguard hardware swaps.【F:data/vesc_help_group/text_slices/input_part013.txt†L205-L260】【F:data/vesc_help_group/text_slices/input_part013.txt†L337-L343】【F:data/vesc_help_group/text_slices/input_part013.txt†L587-L587】
- Compare NKON versus Vapcell procurement workflows (lead times, customs, cell conditioning) so builders can choose suppliers by schedule and QA needs.【F:data/vesc_help_group/text_slices/input_part013.txt†L819-L1006】
- Investigate recurring MakerBase/Spintend logic-rail failures (Pandalgns, Arnau) and draft preventative checks for CAN protection parts and regulator cooling.【F:data/vesc_help_group/text_slices/input_part013.txt†L1122-L1240】【F:data/vesc_help_group/text_slices/input_part013.txt†L1490-L1496】

### Batch 2 Highlights (lines 1500–3000)

#### Controller Reliability & Configuration
- Pandalgns ultimately traced repeated MakerBase cut-outs to a loose hall PCB that shorted against the motor shell and tripped protection—add this to hall-failure diagnostics that mimic logic faults.【F:data/vesc_help_group/text_slices/input_part013.txt†L1552-L1674】
- Matthew’s “dead” 85150 turned out to be a failed power button after a botched firmware update; he and Noname also remind riders that ADC brake strength only rises when regen current is negative and the “ADC2 current no reverse brake” profile is active.【F:data/vesc_help_group/text_slices/input_part013.txt†L1552-L1565】
- Smart Repair runs current-control throttles with 0 s ramping and sees stable performance at 450 A phase, 200 A battery, and 10 % saturation compensation; he’ll reduce compensation gradually to map ABS margins.【F:data/vesc_help_group/text_slices/input_part013.txt†L1799-L1802】
- MakerBase’s revived 100300HP markets 24 S support with 300 A phase/500 A peak using 135 V/305 A FETs in a 24-device stack, but photos omit bulk capacitors—flag a teardown before recommending it for >20 S builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L1923-L1923】
- Smart Repair caps Spintend 85250/85240 controllers near 200 A battery with 380 A phase and 480 A absolute, noting newer 85240s dropped the doubled phase leads, so high-current riders should budget heavier cabling and cooling.【F:data/vesc_help_group/text_slices/input_part013.txt†L2094-L2099】
- Shlomozero is holding 300 A phase and 110 A battery on a Makerbase “shitsky” and plans to replace a 75200 with an 85240 after repairing its logic board, giving more real-world current baselines for mid-season controller swaps.【F:data/vesc_help_group/text_slices/input_part013.txt†L2090-L2090】
- A.P.’s asymmetrical dual build runs 220 A phase, 280 A absolute, and 30 A of field weakening, offering another commuter tuning target.【F:data/vesc_help_group/text_slices/input_part013.txt†L2405-L2406】
- Flipsky Smart Displays continue to misbehave; Smart Repair is steering riders toward the open-source ESP32 SimpleVescDisplay and its printable mount until firmware support improves.【F:data/vesc_help_group/text_slices/input_part013.txt†L2901-L2924】
- Wiring reminders resurfaced: throttles expect 3.3 V/ground/signal into ADC1, and dual-VESC CAN links only need the black/white pair with the secondary mirroring the primary unless separately tuned.【F:data/vesc_help_group/text_slices/input_part013.txt†L2925-L2952】

#### Motor & Performance Benchmarks
- Smart Repair’s 26 S 8 P P42A pack feeds 100 A battery current up front and 200 A at the rear (~102 V), freewheeling around 118 km/h without field weakening on a 22×3 rear mated to a lower-kV Segway GT1 front hub; he expects 130–140 km/h with more runway.【F:data/vesc_help_group/text_slices/input_part013.txt†L1586-L1596】
- Rob Ver’s Vsett build uses a 22 S 9 P Ampace JP4P pack with 80 H rear / 70 H front hubs on 22×3 tires, sees 132 km/h, and runs 80 A of field weakening—the 22×3 combo free-spins near 110 km/h on 22 S before FW extends the ceiling.【F:data/vesc_help_group/text_slices/input_part013.txt†L1906-L1917】
- Omar (✨🇪🇸عمر) pushes 180 A battery / 270 A phase on the rear controller and 150 A / 250 A up front, prompting traction-control and tire-compound discussions to keep fronts planted.【F:data/vesc_help_group/text_slices/input_part013.txt†L2267-L2286】

#### Battery & Power Systems
- Izuna is slimming MKS 84200HP controllers for G30 decks by replacing six stock capacitors (~2,820 µF) with two low-profile cans (~2,000 µF total) laid sideways; Smart Repair warns multiple smaller capacitors handle spikes better than a pair of large ones, so consider auxiliary capacitance elsewhere in the deck.【F:data/vesc_help_group/text_slices/input_part013.txt†L1547-L1665】
- The same controller arrived with unwieldy 6 AWG phase leads that required a 190 °C heatbed plus a TS101 iron to desolder; Izuna swapped to 8 AWG battery cables and will request 10 AWG phases / 8 AWG battery leads on future orders to keep them serviceable.【F:data/vesc_help_group/text_slices/input_part013.txt†L1676-L1766】
- Noname’s 20 S 35 P (700-cell) 18650 pack delivered 96 miles while burning only half its capacity, showing the endurance gains possible when chassis weight tolerates a 10.2 kWh build.【F:data/vesc_help_group/text_slices/input_part013.txt†L1722-L1741】
- D listed a nearly new EVE 50E 20 S 3 P pack (1,080 Wh) with a JBD smart BMS that fits Xiaomi Pro 2, G30, and G2 decks via a spacer, giving a price reference (~€400 shipped from Germany) for boutique drop-in modules.【F:data/vesc_help_group/text_slices/input_part013.txt†L1766-L1766】
- Jose is parting out Stark Varg modules—100 S stacks of P45B/P42A cells delivering ~180 A nominal thanks to 300 V architecture—offering salvage paths for ultra-high-voltage experiments with serious packaging caveats.【F:data/vesc_help_group/text_slices/input_part013.txt†L2611-L2694】

#### Hardware Fitment & Accessories
- Ninebot Max owners can bolt on a Monorim rear footrest kit (~$69 on AliExpress) for an easy stance change without fabrication.【F:data/vesc_help_group/text_slices/input_part013.txt†L1661-L1661】
- Fry the Guy’s Nami Burn E2 swap shows Kaabo 2 kW hubs need rotor spacing to clear the caliper and that ZAITUO 100/65-6.5 tires from Amazon suit the frame—useful notes for Burn E fitment guides.【F:data/vesc_help_group/text_slices/input_part013.txt†L2282-L2297】

#### Follow-Ups
- Benchmark capacitor-downsizing strategies for the MKS 84200HP to restore ≥2,800 µF of bulk capacitance while fitting tight decks, and catalog safe auxiliary-cap options.【F:data/vesc_help_group/text_slices/input_part013.txt†L1547-L1665】
- Expand the throttle/regen quick-start with explicit ADC wiring colors, negative-current brake settings, and dual-VESC CAN guidance so newcomers avoid phantom faults.【F:data/vesc_help_group/text_slices/input_part013.txt†L1559-L1565】【F:data/vesc_help_group/text_slices/input_part013.txt†L2925-L2952】
- Document Flipsky Smart Display failure modes, recommended firmware, and the SimpleVescDisplay swap (parts + STL) for riders needing telemetry now.【F:data/vesc_help_group/text_slices/input_part013.txt†L2901-L2924】

### Batch 3 Highlights (lines 3001–4500)

#### Controller Integration & Reliability
- Rogerio twice blew Spintend ADC daughterboards by powering 5 V before 12 V on the Flipsky Smart Display harness—document the safe sequencing (12 V first) before recommending that pairing.【F:data/vesc_help_group/text_slices/input_part013.txt†L3188-L3193】
- MakerBase X12 firmware silently reverts phase/absolute limits to 120 A unless builders use the read→edit→write workflow; VESC Tool will clamp over-ceiling values after a readback.【F:data/vesc_help_group/text_slices/input_part013.txt†L3656-L3696】
- Anthony’s K-Cloud K14 on dual Flipsky 75100 V2s is throwing “Bad FOC Hall detection” thanks to a failed hall sensor, pushing him toward HFI/sensorless tuning—reinforce hall-diagnostic and sensorless quick-start guides.【F:data/vesc_help_group/text_slices/input_part013.txt†L3751-L3796】
- Matthew still favors twin Spintend 85250s for headroom but saw his 85150 on 18 S overheat above 240 A phase; he settled on 220 A phase, 90 A battery, and 60 A of field weakening to keep temps manageable.【F:data/vesc_help_group/text_slices/input_part013.txt†L3769-L3770】【F:data/vesc_help_group/text_slices/input_part013.txt†L4184-L4184】
- Arnau’s Ubox 250 shut off at 60 V / 120 A with the status LED still green, underscoring the need to capture reset procedures for controllers that silently latch off while telemetry looks healthy.【F:data/vesc_help_group/text_slices/input_part013.txt†L4545-L4549】
- Francois is chasing Ubox 85240 accessory-current specs before wiring a KOX Smart Display, highlighting documentation gaps on the 5 V/12 V rails.【F:data/vesc_help_group/text_slices/input_part013.txt†L4085-L4114】

#### Battery Architecture & Pack Management
- Pandalgns’ Halo Knight T107 Pro runs dual MKS 84200HPs with HM 3000 W 60 H hubs, 12 AWG phases, and a planned 22 S 10 P P45B pack, giving a packaging blueprint for similar chassis.【F:data/vesc_help_group/text_slices/input_part013.txt†L3150-L3168】
- Omar’s dual Spintend build pushes 200 A battery, 310 A phase, and 380 A ABS per controller on a 20 S 10 P 50S pack but overheats battery and hubs, signalling the need for cooling strategies above 300 A phase on NAMI platforms.【F:data/vesc_help_group/text_slices/input_part013.txt†L3707-L3737】
- AYÓ reminded Anthony that NAMI’s stock 40 Ah module is eight-way parallel LG M50LT cells rated ~116 A continuous, advising peaks stay ≤135 A until the pack is rebuilt.【F:data/vesc_help_group/text_slices/input_part013.txt†L3760-L3768】
- Noname daily-rides a Vsett 11 with a 16 S 6 P stem pack, noting the extra mass feels fine on that chassis but would overwhelm a Ninebot G30—guidance for when stem packs remain practical.【F:data/vesc_help_group/text_slices/input_part013.txt†L3920-L3926】
- “Face de Pin Sucé” is fabricating CNC adapters plus a 1 cm steel skid plate to hold a 20 S 5 P Samsung 40T pack and Rage FH60 motor in a G2, illustrating heavy-duty reinforcement tactics for street-legal builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L4557-L4569】
- Murcia’s “Pump” scooter stacks two 16 S modules of 200 A Molicel cells (≈134 V total) feeding a modified Minimotors controller alongside a VESC 75100 V1, showing hybrid VESC/legacy mixes around 20 kW.【F:data/vesc_help_group/text_slices/input_part013.txt†L4441-L4448】
- ’lekrsu’ reiterated that each parallel pack needs its own BMS, voltages must be matched before connecting, packs should equalize naturally (no ideal diodes), and regen limits (e.g., 10 A) belong in VESC Tool rather than dump resistors.【F:data/vesc_help_group/text_slices/input_part013.txt†L4239-L4271】

#### Instrumentation, Accessories & Fabrication
- Pandalgns printed 100 % infill ASA “anti-fall” sliders for deck protection—capture the STL when available for builders seeking crash pucks.【F:data/vesc_help_group/text_slices/input_part013.txt†L3633-L3634】
- The group keeps recommending the SimpleVescDisplay (ESP32) and its handlebar mount STL as a cheap, reliable telemetry replacement (~€10 screen) when OEM displays fail.【F:data/vesc_help_group/text_slices/input_part013.txt†L3859-L3895】
- Francois queried whether twin 12 V Ubox outputs share a buck regulator before paralleling them for a 2.5 A headlight; ’lekrsu’ suspects they do but wants continuity tests, so document accessory-rail verification steps.【F:data/vesc_help_group/text_slices/input_part013.txt†L4085-L4093】
- Rage’s CNC rim for Fastgirl measures 65 mm internal width for 11″ 90/65 tires, matching skrtt’s new 33×2 rim—handy references for tire-fit calculators.【F:data/vesc_help_group/text_slices/input_part013.txt†L4207-L4210】【F:data/vesc_help_group/text_slices/input_part013.txt†L4581-L4587】

#### Follow-Ups
- Draft a Spintend/Flipsky accessory-power checklist covering safe sequencing, ADC board protection, and 5 V/12 V current limits before recommending Smart Display pairings.【F:data/vesc_help_group/text_slices/input_part013.txt†L3188-L3193】【F:data/vesc_help_group/text_slices/input_part013.txt†L4085-L4093】
- Build hall-diagnostic, sensorless-HFI, and MakerBase current-retention guides into the controller setup playbook.【F:data/vesc_help_group/text_slices/input_part013.txt†L3656-L3796】
- Expand the battery chapter with case studies on 20 S high-current packs (P45B/50S), stem-mounted auxiliaries, and parallel-BMS wiring—including regen budgeting and cooling for >300 A phase builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L3150-L3737】【F:data/vesc_help_group/text_slices/input_part013.txt†L4239-L4271】

### Batch 4 Highlights (lines 4501–6000)

#### Motor, Controller & Pack Builds
- Lisa listed a 22×3 60 H hub with PMT 10×3 tires, noting she saw 81 km/h on 20 S at 80 A and that the medium-kV winding sits between 16×4 and 33×2 options; the Phoebeliu/LY motor includes a temp sensor, fits G30 dropouts, typically uses M14 axles, and shipped with short phase leads and a few missing screws.【F:data/vesc_help_group/text_slices/input_part013.txt†L4929-L4945】【F:data/vesc_help_group/text_slices/input_part013.txt†L5239-L5245】
- Arnau Martinez Casals’ new daily scooter runs a 16 S setup with a 17×4 50 H motor, stock Victor 60 V 30 Ah LG M50LT pack, and held 90 A phase / 130 A absolute without issue while he scouts 3D-printed button and charge-port mounts; he’s gauging safe current ceilings for the 100 V 100 A controller stack.【F:data/vesc_help_group/text_slices/input_part013.txt†L4996-L5008】
- Izuna’s MKS 84200HP instantly returned to 20 kW and 120 km/h performance after a swap; routing 6 AWG phase leads made the wiring messy but now lets him hot-swap motors when needed.【F:data/vesc_help_group/text_slices/input_part013.txt†L5030-L5035】
- Smart Repair teased a Ninebot G2 ↔︎ VESC bridge, showing the harness integration work progressing beyond theory.【F:data/vesc_help_group/text_slices/input_part013.txt†L5620-L5620】
- Baartu advertised a turnkey single-motor build—20 S 5 P EVE 40P pack, LY 17×4 65 H hub, Ubox 85150, PMT tires, and Monorim suspension—claiming 10.5 kW, 0–50 km/h in 2.2 s, and 85 km/h with field weakening for €1.5 k, giving price/performance benchmarks for ready-to-ride customs.【F:data/vesc_help_group/text_slices/input_part013.txt†L5687-L5687】
- Haku’s Peak G30V2 prototype is running dual 100 V Ubox V2 controllers on a 20 S 3 P pack, currently relying on two-way throttle-based regen with no mechanical brakes and planning an MT5 front install once a new frame arrives; he’s targeting future dual 22×3 LY motors with 50PL cells for two-wheel burnouts.【F:data/vesc_help_group/text_slices/input_part013.txt†L5156-L5166】【F:data/vesc_help_group/text_slices/input_part013.txt†L5168-L5206】
- Powder-coating hub shells isn’t viable for him after learning the cure oven hits ~400 °F (≈204 °C), risking magnet demag, so high-temp paint or ceramic coatings remain the safer cosmetic path.【F:data/vesc_help_group/text_slices/input_part013.txt†L5205-L5207】【F:data/vesc_help_group/text_slices/input_part013.txt†L5429-L5429】

#### Motor Sourcing & Specs
- Dualtron riders reconfirmed the platform ships with 22/3 windings; Rogerio measured his Victor stator at 50 mm while Arnau contends newer Victors are 45 H and Vsett-10 hubs carry larger magnets and torque windings—useful context when choosing donor motors for VESC swaps.【F:data/vesc_help_group/text_slices/input_part013.txt†L5208-L5220】【F:data/vesc_help_group/text_slices/input_part013.txt†L5347-L5363】
- Arnau has spare DT Spider 2 motors (10″, ~45–50 H) needing axle/nut repairs for €100 each, giving a salvage option for riders with burnt stators.【F:data/vesc_help_group/text_slices/input_part013.txt†L5368-L5374】

#### Battery Parallelisation & Regen Management
- cihan wants to pair a low-C internal pack with a higher-C external module using an ideal diode so regen only backfeeds the larger pack; Noname advises straight paralleling matched voltages, notes regen current splits naturally with higher share to the larger pack, and warns that diode isolation caused throttle cuts when he tied 17 S and 16 S packs—he now just matches voltages or charges down the higher pack.【F:data/vesc_help_group/text_slices/input_part013.txt†L5118-L5136】
- Noname’s 38-mile test consumed roughly 13 V across his twin-pack setup, reinforcing the endurance gains and the need for accurate state-of-charge planning on mixed packs.【F:data/vesc_help_group/text_slices/input_part013.txt†L5134-L5134】
- He also reminded riders that regen is fundamentally phase-current limited and will overheat controllers before healthy packs, so budget regen totals against controller limits, and keep combined regen under the sum of both packs’ capabilities.【F:data/vesc_help_group/text_slices/input_part013.txt†L5131-L5132】【F:data/vesc_help_group/text_slices/input_part013.txt†L5138-L5143】
- Noname’s BMS experience shows regen braking weakens if the charge MOSFET is disabled; enabling the “charge” channel restored his e-brake performance.【F:data/vesc_help_group/text_slices/input_part013.txt†L5488-L5492】

#### Brakes, Wheels & Accessories
- Happy Giraffe machined a custom spacer to fit 203 mm Sur-Ron rotors with Magura brakes on a downhill bicycle frame, a blueprint for mixing moto rotors with bicycle calipers.【F:data/vesc_help_group/text_slices/input_part013.txt†L5040-L5041】
- Skrtt is shaving calipers for 2.3 mm rotors, while 🇪🇸AYO#74 notes thicker discs can work with enough “elevator” spacing, framing acceptable tolerances for oversize rotors on bicycle calipers.【F:data/vesc_help_group/text_slices/input_part013.txt†L5204-L5214】
- Haku clarified that 90/65-6.5 tyres share width with 90/60-6.5 models; the taller second number simply increases sidewall height, useful when chasing more contact patch versus gearing changes.【F:data/vesc_help_group/text_slices/input_part013.txt†L5358-L5364】
- Francois’ G2 build is temporarily riding with a front drum brake and −90 A motor brake until the display arrives, highlighting how far regen alone is being stretched on some conversions.【F:data/vesc_help_group/text_slices/input_part013.txt†L5639-L5653】

#### Connectors, Sensors & Tools
- S1m 0n reminded builders to meter throttles—3-pin harnesses expect 3.3 V/5 V, ground, and a signal ≤3.3 V (3.5 V absolute max) to avoid cooking the ADC stage.【F:data/vesc_help_group/text_slices/input_part013.txt†L5210-L5213】
- Anthony Meza’s throttle tip sets positive ramp time around 0.30 s for a snappy-yet-controlled pull, and he warned that mis-set multimeters (voltage vs. resistance/continuity) can short VESC rails—always confirm dial positions before probing.【F:data/vesc_help_group/text_slices/input_part013.txt†L5805-L5813】
- Happy Giraffe recommends QS8 anti-spark plugs when space allows because their resistors survive higher inrush, while Matthew caps XT90 use to ≈100 A bursts (10–20 s) and suggests XT150/QS8 beyond 120 A to avoid heating connectors.【F:data/vesc_help_group/text_slices/input_part013.txt†L5838-L5845】【F:data/vesc_help_group/text_slices/input_part013.txt†L5936-L5936】
- Happy Giraffe also shared that sensorless FOC with the Ortega observer works “like a charm” up to ~6 kW/60 km/h when hall boards fail, and he prefers the medium inrunner detection preset to limit detection current on heavy hubs.【F:data/vesc_help_group/text_slices/input_part013.txt†L5858-L5864】【F:data/vesc_help_group/text_slices/input_part013.txt†L5926-L5930】

#### Community Benchmarks & References
- Nobrrr and Patrick want the battery-cell masterlist updated with modern 40PL/50PL, P50B, and BAK 45D entries, pointing to Mooch’s independent test archive as the validation source.【F:data/vesc_help_group/text_slices/input_part013.txt†L5768-L5776】
- Cihan is researching whether 30 A of battery-side regen for three seconds is safe for emergency stops from 60 km/h, signalling demand for controller-level braking envelopes.【F:data/vesc_help_group/text_slices/input_part013.txt†L5643-L5651】

#### Follow-Ups
- Capture the Ninebot G2 ↔︎ VESC bridge harness details (pinout, firmware expectations) once Smart Repair publishes them.【F:data/vesc_help_group/text_slices/input_part013.txt†L5620-L5620】
- Build a guidance note on paralleling packs without ideal diodes, covering pre-charge, regen budgeting, and BMS charge-channel checks to preserve braking performance.【F:data/vesc_help_group/text_slices/input_part013.txt†L5118-L5143】【F:data/vesc_help_group/text_slices/input_part013.txt†L5488-L5492】
- Add documentation on acceptable rotor thicknesses, spacer machining, and regen-only braking limits so builders don’t over-rely on electronic brakes without mechanical backups.【F:data/vesc_help_group/text_slices/input_part013.txt†L5204-L5214】【F:data/vesc_help_group/text_slices/input_part013.txt†L5639-L5653】
- Update the connector guide with QS8/XT150 recommendations, throttle-voltage checks, and multimeter safety tips to reduce avoidable controller damage.【F:data/vesc_help_group/text_slices/input_part013.txt†L5210-L5213】【F:data/vesc_help_group/text_slices/input_part013.txt†L5805-L5813】【F:data/vesc_help_group/text_slices/input_part013.txt†L5838-L5845】【F:data/vesc_help_group/text_slices/input_part013.txt†L5936-L5936】

### Batch 5 Highlights (lines 6001–7500)

#### Motor & Controller Builds
- Mattia’s Wolf King GT sleeper is already on dual Ubox 85240s, a 54 Ah Molicel P42A pack, and 6 AWG phase wiring; he caps phase at ≈350 A and plans a 75 H rear / 70 H front swap because the stock 140 mm dropout can’t clear a 75 H hub up front without machining.【F:data/vesc_help_group/text_slices/input_part013.txt†L6163-L6175】
- Makerbase 84100 riders chasing stock Mantis torque need more phase current than the default 90 A: Paolo recommends matching the OEM 150 A phase (or at least 120 A with a 150 A absolute limit) and flashing the no-limits firmware, noting e-brake headroom is tied to the absolute over-current value.【F:data/vesc_help_group/text_slices/input_part013.txt†L6235-L6247】
- CAN-linked controllers report aggregated telemetry—Yamal’s dual 85240/85250 setup shows ~500 A phase even though each controller is only pulling ~250 A—so teams are leaning on Voyage/Ambrosini displays that read each controller individually when they need per-wheel diagnostics.【F:data/vesc_help_group/text_slices/input_part013.txt†L6488-L6497】【F:data/vesc_help_group/text_slices/input_part013.txt†L6607-L6610】
- Noname’s 85/250 single-motor moped build currently limits to 300 A phase / 200 A battery; Jason suggests budgeting 450 A+ phase or stepping up to 18‑fet controllers once funds allow to keep 17×4 acceleration competitive against larger twin-motor rigs.【F:data/vesc_help_group/text_slices/input_part013.txt†L7246-L7256】

#### Battery, Wiring & Telemetry
- 🇪🇸AYO#74 advises upgrading thin factory motor leads to AWG 11 silicone (AWG 10 rarely fits through scooter axles) and using hill-climb hand checks—if you can’t hold the hub for 10 s, drop phase current—to keep Sevillian summer temps in check.【F:data/vesc_help_group/text_slices/input_part013.txt†L7336-L7359】
- Paolo reminds builders that AWG is only a gauge standard: silicone leads are tinned copper and slightly larger OD than PVC, so link shopping lists should call out conductor material as well as gauge.【F:data/vesc_help_group/text_slices/input_part013.txt†L7348-L7354】
- Mirono is chasing a paid Lisp script to run three-wire PAS sensors alongside throttles without an Arduino bridge, signalling demand for maintained VESC Tool integrations beyond the aging community snippets.【F:data/vesc_help_group/text_slices/input_part013.txt†L6505-L6507】

#### Tires, Suspension & Handling
- Carbon paste on a Ninebot headset clamp will lock the steering if it seeps into the bearings; 🇪🇸AYO#74 recommends stripping the paste, replacing the bearings, and monitoring for dirt intrusion rather than riding the extra stiffness like a damper substitute.【F:data/vesc_help_group/text_slices/input_part013.txt†L6526-L6533】
- Seating split tubeless rims is still easiest with ratchet straps plus a high-flow compressor—skrtt’s bead leaked at the sidewalls until he cinched the carcass, while Haku joked about (but didn’t endorse) flammable seating tricks.【F:data/vesc_help_group/text_slices/input_part013.txt†L6838-L6845】【F:data/vesc_help_group/text_slices/input_part013.txt†L6855-L6867】
- Ulip “fake PMT” slicks are wearing rapidly up front even at 26–28 psi; riders are switching to Xuancheng 100/55 or genuine PMT T41s for longevity, accepting that burnouts will still shred any soft compound quickly.【F:data/vesc_help_group/text_slices/input_part013.txt†L6901-L6937】

#### Ride Planning & Logistics
- Noname is staging a 480 km, seven-day ride with four scooters and a chase van, budgeting 20 mph cruise speeds, 30–40 km/h efficiency targets, and 2.6 kW fast-charging on EVE 40P packs—practical data for long-distance VESC touring guides.【F:data/vesc_help_group/text_slices/input_part013.txt†L7087-L7251】
- The U.S. crew’s “jank but clean” ethos still leans on seats and external battery crates, while European racers chase lighter standing decks; documenting both packaging approaches will help new builders reconcile comfort, legality, and style preferences.【F:data/vesc_help_group/text_slices/input_part013.txt†L7210-L7234】【F:data/vesc_help_group/text_slices/input_part013.txt†L7288-L7333】

#### Parts & Vendor Notes
- RM-Light race scooters run 22 S 4 P tabless packs, RM-X 2024 rear motors, Beringer Br4ve brakes, and weigh ≈37 kg, offering a benchmark for lightweight 130–140 km/h builds with premium components.【F:data/vesc_help_group/text_slices/input_part013.txt†L6324-L6334】
- Lonnyo sourcing remains fragmented: builders swap WhatsApp contacts (+86 151 6855 5189), Lonnyo.com, and Lonnyomotor.com while Paolo cautions many listings are resellers—expect to verify vendors directly before wiring funds.【F:data/vesc_help_group/text_slices/input_part013.txt†L7365-L7392】
- Flipsky 75100 users are still begging for a step-by-step regen-brake setup and suspension hardware references, underscoring documentation gaps for popular mid-power conversions.【F:data/vesc_help_group/text_slices/input_part013.txt†L7394-L7399】

#### Follow-Ups
- Add a CAN telemetry note showing how to split per-controller data (Voyage/Ambrosini, CAN IDs, or dual VESC Tool sessions) so builders stop misreading combined phase current.【F:data/vesc_help_group/text_slices/input_part013.txt†L6488-L6497】【F:data/vesc_help_group/text_slices/input_part013.txt†L6607-L6610】
- Document safe tubeless bead-seating workflows for split rims (straps, compressor volume, sealant dosages) and warn against flammable “quick seat” tricks.【F:data/vesc_help_group/text_slices/input_part013.txt†L6838-L6845】【F:data/vesc_help_group/text_slices/input_part013.txt†L6855-L6867】
- Expand the wiring chapter with AWG selection tables (axle fit vs. ampacity), silicone vs. PVC jacket pros/cons, and hill-test procedures for hot climates.【F:data/vesc_help_group/text_slices/input_part013.txt†L7336-L7359】
- Capture 75100 regen setup steps and PAS integration scripts so newcomers aren’t chasing paid Lisp gigs to restore basic braking features.【F:data/vesc_help_group/text_slices/input_part013.txt†L6505-L6507】【F:data/vesc_help_group/text_slices/input_part013.txt†L7394-L7399】

### Batch 6 Highlights (lines 7501–9000)

#### Controller Setup & Reliability
- Matthew steered newcomers toward Spintend’s 85250 and 85150 controllers—highlighting that the 85150 can still deliver ≈13 kW per side—and stressed that ordering direct beats AliExpress markups when you need factory support.【F:data/vesc_help_group/text_slices/input_part013.txt†L7533-L7539】
- Ausias’ 70 H/80 H pairing on dual 85240s prompted Yamal to cap them near 300 A phase per motor, while Matthew reiterated Spintend’s own guardrails of ≈240–250 A battery on 85240/85250 stacks and ≈150 A battery/phase on 85150s, giving a concrete envelope for daily tunes.【F:data/vesc_help_group/text_slices/input_part013.txt†L8242-L8255】
- G300 owners confirmed the power switch ships as a momentary input: you must reconfigure the shutdown mode in VESC Tool (App → General) so a button press actually toggles the controller, otherwise it simply wakes on battery connection.【F:data/vesc_help_group/text_slices/input_part013.txt†L7722-L7724】【F:data/vesc_help_group/text_slices/input_part013.txt†L8535-L8550】【F:data/vesc_help_group/text_slices/input_part013.txt†L8958-L8960】
- Noname revived a “dead” Vsett 11+ pack by unplugging and reseating the multipin BMS harness, a quick reset worth adding to troubleshooting checklists before condemning an idle battery.【F:data/vesc_help_group/text_slices/input_part013.txt†L7962-L7978】

#### Battery, Wiring & Safety
- Dualtron Achilleus builders are stuffing long Sonken/DT shells with 21 S 11 P Molicel packs and even stretching DT3 frames to hold 22 S 9 P P45Bs plus an 85250, illustrating how much deck surgery it takes to house legal-looking yet high-voltage drivetrains.【F:data/vesc_help_group/text_slices/input_part013.txt†L7713-L7719】【F:data/vesc_help_group/text_slices/input_part013.txt†L7754-L7758】【F:data/vesc_help_group/text_slices/input_part013.txt†L8080-L8084】
- Yamal’s commuter pack runs 20 S 10 P cells on 0.1 mm copper and only a 40 A charge-side ANT BMS, prompting peers to warn that riding without discharge protection risks an ESC fire if anything shorts.【F:data/vesc_help_group/text_slices/input_part013.txt†L8840-L8876】
- Hackintoshhhh laminates two 0.1 mm copper-nickel sheets because his Glitter 801D welder cannot reliably attach a single 0.2 mm strip, a practical workaround for builders stuck on mid-tier welders who still need high-current busbars.【F:data/vesc_help_group/text_slices/input_part013.txt†L8919-L8939】

#### Braking, Suspension & Handling
- Mixing Shimano and Magura mineral oils proved safe for multiple riders, and 🇪🇸AYO#74 recommends swapping to a higher-flow bleed needle to firm up MT5 lever feel by reducing the dead zone.【F:data/vesc_help_group/text_slices/input_part013.txt†L7842-L7850】【F:data/vesc_help_group/text_slices/input_part013.txt†L7910-L7910】
- Yamal is testing wheel-centering kits on 80/100 H hubs to calm lean wobble and keep rotors from scraping, giving heavier motors a clearer path into legal chassis.【F:data/vesc_help_group/text_slices/input_part013.txt†L8010-L8013】
- Cihan cured the Ninebot F2 Pro’s braking wobble by pairing sintered-metal pads with a soft, inexpensive rotor—bite skyrockets once warm, and he is content to replace €2 discs as they wear.【F:data/vesc_help_group/text_slices/input_part013.txt†L8828-L8829】
- Eduuuuuuuuu’s “10-second touch test” reminder—if you can’t hold a motor shell for ten seconds, drop phase amps—remains a simple field gauge for riders chasing hill climbs without telemetry.【F:data/vesc_help_group/text_slices/input_part013.txt†L8752-L8753】

#### Lighting, Accessories & Fabrication
- The crew keeps debating headlights: Yamal wants 12 V bars tied into the traction battery to avoid recharging flashlights, Noname wires USB ports onto every build, and Haku plugs cheap AliExpress lightbars through the ADC harness—pointing to a need for a consolidated lighting-power guide.【F:data/vesc_help_group/text_slices/input_part013.txt†L7566-L7589】
- Ausias is commissioning a ventilated yet splash-resistant 3D-printed enclosure after dust caked his under-slung Kelly despite mostly road use, underscoring that bottom-mounted controllers still need filtered airflow paths.【F:data/vesc_help_group/text_slices/input_part013.txt†L8506-L8512】

#### Legalisation, Touring & Community Logistics
- Spanish riders are bracing for 2027 crackdowns: they’re eyeing DGT-listed Dualtron Thunder 3/Achilleus shells, debating €3 k frame swaps, and even downsizing to stealthy singles so police stop targeting them.【F:data/vesc_help_group/text_slices/input_part013.txt†L7522-L7530】【F:data/vesc_help_group/text_slices/input_part013.txt†L8065-L8079】【F:data/vesc_help_group/text_slices/input_part013.txt†L8236-L8269】
- Achilleus/Thunder/DT3 measurements—18.1 cm deck width for DT3/Achilleus versus 22.1 cm on Thunder—help builders gauge how many parallel groups and controllers can hide inside a “legal” shell.【F:data/vesc_help_group/text_slices/input_part013.txt†L8114-L8119】
- Noname’s road-trip prep crammed a Segway C80, Begode Q3, Vsett 10, Master Pro, and EX30 into a chase van alongside camping gear for five riders, offering a real packing list for multi-day scooter tours.【F:data/vesc_help_group/text_slices/input_part013.txt†L7713-L7719】
- Cihan’s Ninebot F2 Pro experience underscores commuter realities: SHU firmware and field weakening can hit 45 km/h but sap range, the low-kV motor bogs below 65 % SOC, traction control makes icy mornings survivable, and front-end hardware needs careful alignment to prevent rotor rub.【F:data/vesc_help_group/text_slices/input_part013.txt†L8088-L8134】

#### Marketplace & Community Support Notes
- Tronic’s main site is flaky, but Omar flagged Protopulse as an EU reseller listing the X12 for about €600, giving builders a verified source while the factory sorts its store.【F:data/vesc_help_group/text_slices/input_part013.txt†L8287-L8314】
- 🇪🇸AYO#74 publicly thanked James Soderstrom for repairing Spintend drivers and even fabricating a missing BLE module, reinforcing who the community leans on for controller RMAs.【F:data/vesc_help_group/text_slices/input_part013.txt†L8983-L8985】

#### Follow-Ups
- Publish a G300 push-button quick-start (App shutdown settings, wiring pinout) so new owners stop hunting scattered chat messages.【F:data/vesc_help_group/text_slices/input_part013.txt†L7722-L7724】【F:data/vesc_help_group/text_slices/input_part013.txt†L8535-L8550】【F:data/vesc_help_group/text_slices/input_part013.txt†L8958-L8960】
- Expand the lighting/accessory chapter with 12 V rail sourcing, USB power taps, and ADC-controlled lightbar wiring—including fuse math—to mirror the crew’s preferred setups.【F:data/vesc_help_group/text_slices/input_part013.txt†L7566-L7589】
- Add a safety brief on charge-only BMS use: outline interim inspections, recommended discharge-side hardware, and failure-case escalation so riders like Yamal can mitigate risk until full BMS protection is restored.【F:data/vesc_help_group/text_slices/input_part013.txt†L8840-L8876】
- Document mineral-oil compatibility tests, high-flow bleed needles, and quick thermal-check heuristics to backstop the brake tuning and “10-second touch” advice gathered in this batch.【F:data/vesc_help_group/text_slices/input_part013.txt†L7842-L7850】【F:data/vesc_help_group/text_slices/input_part013.txt†L7910-L7910】【F:data/vesc_help_group/text_slices/input_part013.txt†L8752-L8753】

### Batch 7 Highlights (lines 9001–10500)

#### Controller Setup & Diagnostics
- Rogerio’s friend cooked a stock-firmware Spintend 85250 in two days on a 20 S Molicel pack at 180 A phase / 80 A battery with regen disabled; the crew now flashes the no-hardware-limits firmware and caps around 150 A battery / 250 A phase while keeping the enclosure clean to avoid repeat failures.【F:data/vesc_help_group/text_slices/input_part013.txt†L9077-L9096】
- Patrick’s 65 H 17×4 delta hub keeps rebooting a Makerbase VESC even with ABS overcurrent cleared at 225 A absolute; others recommend reflashing firmware from scratch after backing up settings because value edits alone may not clear the latent fault.【F:data/vesc_help_group/text_slices/input_part013.txt†L9240-L9299】
- 🇪🇸AYO#74 fixed a runaway-throttle bug on the G300 by updating to firmware 6.3; Arnau notes RTR builds already ship with custom 5.3 firmware and axle swaps need gentle hammering so threads survive reinstall.【F:data/vesc_help_group/text_slices/input_part013.txt†L9654-L9667】
- Mirono’s pedal-assist Lisp script on a Flipsky 75100 V2 locks the motor after high-phase pulls until the motor config is rewritten; the team suspects observer or script-side limits and is testing ceramic-cap noise filters plus lower phase limits as interim mitigations.【F:data/vesc_help_group/text_slices/input_part013.txt†L10188-L10212】

#### Motor Fitment & Thermal Guardrails
- 75 H Lonnyo swaps on Dualtron arms need careful spacing: LY axles vary by up to 5 mm, rim offset favors the brake side, and builders often stack thin washers rather than relying on stock suspension tolerances.【F:data/vesc_help_group/text_slices/input_part013.txt†L9331-L9349】【F:data/vesc_help_group/text_slices/input_part013.txt†L10155-L10159】
- Shlomozero’s 75 H 22/3 hits 80 °C within minutes at 400 A phase, while Paolo reminds riders that 22/3 windings carry 10 fewer parallel strands than 33/2, so anything above ≈250–300 A should stay to short bursts or risk burnout on climbs.【F:data/vesc_help_group/text_slices/input_part013.txt†L9779-L9788】【F:data/vesc_help_group/text_slices/input_part013.txt†L10402-L10404】
- Paolo also flags LY 80 H hubs as twin-stacked 40 H magnets that saturate faster under FOC; the group is steering high-phase builds toward single-magnet 70/75/90 H stators that shed heat more predictably.【F:data/vesc_help_group/text_slices/input_part013.txt†L9671-L9677】
- Arnau’s single-motor Daly build pairs a 75 H 22/3 rear hub with an Ubox 240 at 200 A phase / 100 A battery on a 20 S 6 P P45B pack, cruising at 10 kW with FETs around 36 °C—useful headroom for commuter-focused singles.【F:data/vesc_help_group/text_slices/input_part013.txt†L10221-L10233】

#### Battery, BMS & Power Planning
- ANT 30 S smart BMS units need the series-count and Ah fields set manually in the “System Parameters” menu to read all 22 cells on a 22 S pack; otherwise one string shows zero volts even when the harness is wired correctly.【F:data/vesc_help_group/text_slices/input_part013.txt†L9444-L9452】
- Builders debating 22 S 10 P packs still lean on Molicel P45B cells, but they’re already eyeing 40–50 PL options and even Ampace JP40 for future 30–40 S, low-current builds where higher voltage offsets lower amp draw.【F:data/vesc_help_group/text_slices/input_part013.txt†L10455-L10490】
- Matthew reiterates the 85150 Ubox as the compact 13 kW choice for 20 S commuters, with Spintend’s ADC3 expander or a 20 A 12 V buck handling accessories when the dual 75100’s IO budget is too tight.【F:data/vesc_help_group/text_slices/input_part013.txt†L9453-L9456】

#### Cooling, Sensors & Ride Feel
- Statorade continues to divide the group: Matthew and Noname see rapid drops from 100 °C to ~70 °C after backing off for a few minutes, while Haku warns that sealing air gaps with ferrofluid risks magnet damage on ultra-high-speed motors.【F:data/vesc_help_group/text_slices/input_part013.txt†L10299-L10310】
- Noname’s KTY-83 motor probe spikes instantly with throttle even though the NTC track stays steady, prompting interest in ferrofluid for both thermal damping and noise reduction on high-speed hubs.【F:data/vesc_help_group/text_slices/input_part013.txt†L10245-L10253】
- Yamal’s 20 S dual build is already touching 130 km/h at 150 A battery per controller without maxing settings, reinforcing how little headroom remains before voltage—not phase—caps top speed.【F:data/vesc_help_group/text_slices/input_part013.txt†L9903-L9916】

#### Follow-Ups
- Publish a step-by-step for reflashing Makerbase/Spintend units when ABS trips lead to full controller resets so riders can rule out firmware corruption before swapping hardware.【F:data/vesc_help_group/text_slices/input_part013.txt†L9240-L9299】
- Add a Lonnyo axle and spacer fitment guide (measurements, washer stacks, thread-protection tips) to keep 75 H/80 H installs centered without damaging axle threads.【F:data/vesc_help_group/text_slices/input_part013.txt†L9331-L9349】【F:data/vesc_help_group/text_slices/input_part013.txt†L9655-L9662】【F:data/vesc_help_group/text_slices/input_part013.txt†L10155-L10159】
- Expand the winding chapter with current/thermal envelopes for 22/3 vs 33/2 vs twin-magnet 80 H hubs so builders stop pushing 400 A phase on stators that can’t shed the heat.【F:data/vesc_help_group/text_slices/input_part013.txt†L9779-L9788】【F:data/vesc_help_group/text_slices/input_part013.txt†L10402-L10404】【F:data/vesc_help_group/text_slices/input_part013.txt†L9671-L9677】
- Capture ANT/JBD smart-BMS configuration screenshots (series count, AH, UART pinouts) and script options for piping pack telemetry straight into VESC Tool.【F:data/vesc_help_group/text_slices/input_part013.txt†L9444-L9452】【F:data/vesc_help_group/text_slices/input_part013.txt†L9485-L9485】
- Compare statorade, ferrofluid blends, and alternative cooling strategies for 22/3 race hubs so riders can weigh magnet longevity against the proven 30 °C drops logged here.【F:data/vesc_help_group/text_slices/input_part013.txt†L10299-L10310】【F:data/vesc_help_group/text_slices/input_part013.txt†L10245-L10253】

### Track Prep & Legalization Planning (lines 8000–9499)
- Yamal is lining up wheel-centering kits for 80/100 H hubs because they calm wobble and keep discs off the deck on lean, while Arnau is doubling front calipers after discovering his reference build out-braked his own setup.【F:data/vesc_help_group/text_slices/input_part013.txt†L8010-L8016】
- Dualtron builders compared chassis dimensions—Achilleus matching Thunder width while DT3 stays shorter—and outlined how stretching a DT3 shell fits a 22 S 9 P P45B pack plus an 85250 inside, reinforcing the packaging work needed for legal-yet-powerful builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L8065-L8084】
- Ongoing Spanish crackdowns (and the looming 2027 rule change) are pushing riders to stealthier platforms: they’re weighing Achilleus/T3 frames that appear on the DGT list, debating €3 k frame swaps, and even considering smaller daily scooters to dodge police attention.【F:data/vesc_help_group/text_slices/input_part013.txt†L8020-L8024】【F:data/vesc_help_group/text_slices/input_part013.txt†L8703-L8714】【F:data/vesc_help_group/text_slices/input_part013.txt†L8903-L8915】【F:data/vesc_help_group/text_slices/input_part013.txt†L8952-L8954】

### Spintend & Controller Guardrails (lines 8000–9499)
- Ausias asked how hard to lean on an 85240 pairing 70 H/80 H hubs, and Yamal pegged 300 A phase per motor as the safe ceiling while Matthew reiterated Spintend’s guidance of ≤240–250 A battery on 85250s and ≈150 A/230 A on 85150s.【F:data/vesc_help_group/text_slices/input_part013.txt†L8242-L8255】
- Hackintoshhhh is proving those numbers in practice: his Lime runs 150 A battery / 240 A phase on a stock-fet 85150, about 270 A battery / 400 A phase shared across dual 85250s (≈230 A per wheel), and he still caps throttle to 40 % because 380 A phase makes the scooter undrivable otherwise.【F:data/vesc_help_group/text_slices/input_part013.txt†L8422-L8462】
- Rogerio’s friend torched a stock-firmware Spintend at just 180 A phase / 80 A battery with regen disabled, whereas Yamal’s no-limit flash survives at 150 A battery / 250 A phase—so long as debris stays out of the enclosure—underscoring the need for sealing plus conservative current while testing.【F:data/vesc_help_group/text_slices/input_part013.txt†L9082-L9098】

### Ninebot & Commuter Upgrades (lines 8000–9499)
- cihan catalogued the F2 Pro’s limits: the low-kV motor sags past 65 % SOC on stock firmware, SHU needs an ST-Link flash, field weakening plus higher voltage packs can push 45 km/h, and traction control remains invaluable on icy commutes even if summer riders disable it.【F:data/vesc_help_group/text_slices/input_part013.txt†L8088-L8133】
- ’lekrsu’ added that Segway’s stock code deliberately drags speed and that the hub sits around 19 kV, framing expectations for anyone chasing more top end via firmware swaps or battery work.【F:data/vesc_help_group/text_slices/input_part013.txt†L8183-L8184】
- Sintered pads on a soft, cheap rotor finally stopped the F2 Pro’s braking wobble for cihan; once warm they bite hard, sound like a Voith retarder, and he’s content to burn through €2 rotors for the stability boost.【F:data/vesc_help_group/text_slices/input_part013.txt†L8828-L8829】

### Troubleshooting & Integration Notes (lines 8000–9499)
- Shlomozero’s Tronic 750 throws ABS over-current with the Ortega observer above 500 A phase; Paolo recommends trimming measured inductance by 30–35 %, Martin suggests warm motor detection plus higher hall ERPM, and Yamal reminds Nami owners to shield their exposed electronics after grit killed his last Ubox.【F:data/vesc_help_group/text_slices/input_part013.txt†L8500-L8514】
- Ausias is commissioning a ventilated yet splash-resistant 3D enclosure because his under-slung Kelly collected dust despite avoiding sand, highlighting the need to balance airflow and sealing on bottom-mounted controllers.【F:data/vesc_help_group/text_slices/input_part013.txt†L8508-L8512】
- JPPL documented the MakerX push-button workflow: change the App shutdown method to a timed auto-off so a single press toggles power, and refer to MakerX’s guide for wiring specifics.【F:data/vesc_help_group/text_slices/input_part013.txt†L8958-L8960】
- Patrick’s MakerBase build still reboots mid-ride—ABS triggers at 225 A absolute even after lowering throttle—and peers advised bumping the absolute limit plus re-flashing the same firmware from scratch to clear suspected hardware glitches.【F:data/vesc_help_group/text_slices/input_part013.txt†L9039-L9073】【F:data/vesc_help_group/text_slices/input_part013.txt†L9093-L9096】【F:data/vesc_help_group/text_slices/input_part013.txt†L9290-L9299】
- Rogerio is chasing ANT/JBD telemetry alignment on a 22 S pack: the BMS reports 23 S unless he rewrites system parameters, so he’s rechecking voltage-series and Ah fields per Arnau’s screenshot guidance.【F:data/vesc_help_group/text_slices/input_part013.txt†L9444-L9452】

### Battery & Wheel Fitment Tips (lines 8000–9499)
- Yamal’s commuter pack still runs charge-only ANT protection (40 A), prompting peers to warn that dailying 20 S without a discharge BMS is irresponsible and could nuke the ESC if anything shorts.【F:data/vesc_help_group/text_slices/input_part013.txt†L8854-L8870】
- Hackintoshhhh stacks dual 0.1 mm copper sheets (copper–nickel–copper) because his Glitter 801D can’t weld 0.2 mm pure copper, accepting a slight resistance penalty to keep high-current busbars feasible.【F:data/vesc_help_group/text_slices/input_part013.txt†L8924-L8939】
- Shlomozero’s 75 H fitment test shows Dualtron arms need only a thin washer on the wire side, yet Face de Pin cautions LY axles can vary by >5 mm, so measuring every hub before spacing is mandatory.【F:data/vesc_help_group/text_slices/input_part013.txt†L9119-L9134】【F:data/vesc_help_group/text_slices/input_part013.txt†L9310-L9313】
- Riders debated tubed versus tubeless Lonnyos: tubes are cheaper but risk blowouts under racing heat, and you can’t convert split rims because half the shell is the motor—explaining why many pay extra for tubeless cores.【F:data/vesc_help_group/text_slices/input_part013.txt†L9135-L9156】
- When V asked about Flipsky 75100 duals versus FT85BD, Hackintoshhhh pointed him to Spintend’s 85150, Patrick floated the MP2 as a budget alternative, and Matthew laid out the whole 85 V Ubox lineup plus the ADC3 accessory bridge and its 18 S dual-controller cousin.【F:data/vesc_help_group/text_slices/input_part013.txt†L9435-L9456】

### Batch 8 Highlights (lines 9500–10999)

#### Motor Sourcing & Fitment Lessons
- Cheap AliExpress 60 H hubs advertised as “20×3” windings trade away copper fill for price—’lekrsu’ confirms they use only 20 parallel strands instead of 22, which cuts torque, while Paolo reiterates that LY’s 80 H cores rely on two 40 H magnets that hinder smooth FOC compared with single-piece 70/75/90 H stacks.【F:data/vesc_help_group/text_slices/input_part013.txt†L9672-L9674】【F:data/vesc_help_group/text_slices/input_part013.txt†L9710-L9716】
- Arnau’s axle-swapping notes emphasise removing the lock washer and driving the old axle out with a mallet while protecting the new threads, and riders dealing with misaligned dropouts are adding thin washers to re-center LY hubs—important because several members noted the rims are offset toward the brake side from the factory.【F:data/vesc_help_group/text_slices/input_part013.txt†L9656-L9663】【F:data/vesc_help_group/text_slices/input_part013.txt†L10007-L10014】【F:data/vesc_help_group/text_slices/input_part013.txt†L10152-L10160】

#### Phase-Current, Thermal & Traction Takeaways
- Shlomozero’s 75 H 22/3 test hit 80 °C in just a few minutes at 400 A because of undersized phase cables; Roland and Dualtron Achilleus keep the same hardware below ~200–250 A motor current, and Paolo warns that pushing 300 A for more than a burst—especially uphill—will eventually cook the windings.【F:data/vesc_help_group/text_slices/input_part013.txt†L9778-L9819】【F:data/vesc_help_group/text_slices/input_part013.txt†L10160-L10169】【F:data/vesc_help_group/text_slices/input_part013.txt†L10549-L10555】
- Arnau logged a single-motor 75 H 22/3 build staying below 90 °C at 200 A phase once he corrected the temp-sensor pull-up to 100 kΩ; the setup runs a Ubox 240, 20 S 6 P P45B pack, and an ANT 450 A BMS—useful telemetry for riders eyeing similar Daly-equipped daily builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L10221-L10248】
- Yamal’s commuter baseline remains 20 S with 150 A battery per controller (≈300 A total) and 250 A phase, but he still sees traction control shaving watts, so he prefers manual throttle modulation even as he chases 110–120 km/h without field-weakening; others like Noname are stuck around 220 A phase until they flash Spintend’s hardware-no-limit firmware, which unlocked 260 A launches for Matthew once he bumped past the stock 150 A cap.【F:data/vesc_help_group/text_slices/input_part013.txt†L9909-L9913】【F:data/vesc_help_group/text_slices/input_part013.txt†L10099-L10134】【F:data/vesc_help_group/text_slices/input_part013.txt†L10242-L10265】
- The same configuration already touched 129.8 km/h GPS on 20 S with twin 80 H 33×2 hubs at 150 A battery / 250 A phase per controller, while Shlomozero is testing asymmetric field-weakening (≈50 A rear / 40 A front) after logging 115 km/h with FW disabled—useful benchmarks before riders chase higher voltage.【F:data/vesc_help_group/text_slices/input_part013.txt†L10668-L10682】
- Field-weakening targets continue to vary: Shlomozero can’t break 105 km/h on 75 H/60 H combos even with 50 A FW on the rear, and he’s looking for data-driven observer settings after BT link drops and motor-detection failures crop up at those levels.【F:data/vesc_help_group/text_slices/input_part013.txt†L10170-L10198】【F:data/vesc_help_group/text_slices/input_part013.txt†L10636-L10645】

#### Controller & Firmware Notes
- 🇪🇸AYO#74’s G300 updated cleanly to VESC 6.3, clearing a stuck-throttle bug from 5.3; he also flagged that a six-blink red LED indicates low voltage, and his “off_after_xxx” auto-shutoff still fails, forcing him to kill power through the ANT BMS instead of the front buttons.【F:data/vesc_help_group/text_slices/input_part013.txt†L9654-L9671】【F:data/vesc_help_group/text_slices/input_part013.txt†L10682-L10718】
- He confirmed the twin power buttons simply parallel the two controllers, so anyone relying on the stock harness still needs a BMS/contactors-based kill switch until MakerX ships a firmware fix.【F:data/vesc_help_group/text_slices/input_part013.txt†L10704-L10711】
- ’lekrsu’ reminded builders never to feed 5 V into ADC1/ADC2 because it will cook the STM32—Matthew’s been running the hall throttle from 3.3 V without issue—while the group collected more Ninebot G2 conversion asks about which VESC variant preserves horn/indicator outputs.【F:data/vesc_help_group/text_slices/input_part013.txt†L9702-L9774】【F:data/vesc_help_group/text_slices/input_part013.txt†L10290-L10300】
- Mirono’s Flipsky 75100 V2 with a PAS Lisp script rides normally until he pauses at higher phase amps, at which point the motor just vibrates until he rewrites the motor config—pointing to an unresolved observer or firmware edge case that likely needs a reproducible test plan.【F:data/vesc_help_group/text_slices/input_part013.txt†L10188-L10205】
- Haku, Jason, and Yamal are already planning for 30 S/40 S-class VESCs (e.g., 3Shul CC1000 rated 8–40 S), but nobody can point to an off-the-shelf 40 S BMS yet—highlighting a packaging gap for next-generation torque builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L10495-L10524】

#### Battery, Cooling & Sensor Maintenance
- A Teverun Fighter 11+ pack that only wakes with the charger attached was traced to two dead parallel groups; Jason recommends either rebuilding the entire 60 V 35 Ah module or carefully mixing matched Samsung 50S replacements because swapping a couple of cells won’t restore balance.【F:data/vesc_help_group/text_slices/input_part013.txt†L10636-L10669】
- Matthew continues to vouch for small doses of Statorade (≈4 ml in a 12" hub) after seeing 30 °C temperature drops within minutes, whereas haku warns that sealing the air gap can overheat magnets—evidence we should catalogue in a cooling best-practices note.【F:data/vesc_help_group/text_slices/input_part013.txt†L10299-L10309】
- 🇪🇸AYO#74 is chasing reliable LY motor temperature sensors; haku says the hubs ship with NTC 10 k parts, AG.racing linked a compatible harness, and the team floated repurposing BMS probes when hall-board replacements fail.【F:data/vesc_help_group/text_slices/input_part013.txt†L10722-L10741】

#### Brakes, Wheels & Accessories
- Ausias is experimenting with 3.6 mm rotors on Magura MT5s by milling the caliper “radially” for clearance; even supporters caution that most bicycle brakes expect ≤2.8 mm rotors, so formal documentation on machining tolerances and lever upgrades would help others replicate the mod safely.【F:data/vesc_help_group/text_slices/input_part013.txt†L10752-L10788】
- Matthew shared his regen-friendly cable lever kit (variable pull left/right plus hardened 140 mm rotors) and reminded riders that Spintend’s accessory hub opens extra inputs for those keeping OEM switches on Ninebot conversions.【F:data/vesc_help_group/text_slices/input_part013.txt†L10337-L10346】
- Marketplace hunters continue to chase cheap LY and Lonnyo hubs—$80 AliExpress 60 H cans or $330 direct Lonnyo 65 H motors—but everyone agrees shipping missteps or tariffs can erase those savings quickly.【F:data/vesc_help_group/text_slices/input_part013.txt†L9541-L9551】【F:data/vesc_help_group/text_slices/input_part013.txt†L9708-L9724】

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

### Batch 13 Highlights (lines 17000–18499)

#### Ubox 100/100 Daily Setup & Thermal Management
- Matthew and 'lekrsu' converged on a “daily safe” window of roughly 130–135 A phase with 85–90 A battery and 150–180 A absolute on a single Ubox 100/100 driving a Lonnyo 65 H 17×4—anything higher forces the controller into thermal trouble unless climate and pack voltage are ideal.【F:data/vesc_help_group/text_slices/input_part013.txt†L17015-L17056】【F:data/vesc_help_group/text_slices/input_part013.txt†L17435-L17438】
- Trimming top duty to 98 % (cutoff start 95 %) and starting field-weakening at 88 % eradicated the last bit of stutter on that setup, and the custom water-cooled base plate now drops FET temps from ~54 °C back to 40 °C within a minute even in 35 °C ambient pulls at 130 A phase.【F:data/vesc_help_group/text_slices/input_part013.txt†L17077-L17084】【F:data/vesc_help_group/text_slices/input_part013.txt†L17358-L17363】

#### Brake Systems & Maintenance
- Face de Pin Sucé reminded builders that doubling calipers on a single rotor rarely boosts stopping torque—proper twin-disc hardware matters—while 🆁aphaël 🅵ou🅹iwara framed dual-disc gains as endurance rather than raw bite, so future guides should emphasise equal rotor sizing and lever ratios when cloning MotoGP layouts.【F:data/vesc_help_group/text_slices/input_part013.txt†L17238-L17266】
- Matthew’s emergency-stop story (snaped cable at 40 mph) underlined why regen must complement, not replace, hydraulics; he also noted regen heating shows up in the controller, not the motor, so riders should watch MOSFET temps after long descents.【F:data/vesc_help_group/text_slices/input_part013.txt†L17360-L17380】
- Successful Magura bleeds came from levelling the lever, repeatedly flicking the hose to vent micro-bubbles, and patiently cycling the lever until the feel firms up—mirroring bicycle-service best practices the group plans to document.【F:data/vesc_help_group/text_slices/input_part013.txt†L17434-L17446】

#### Accessory Power & Electrical Integration
- Riders pointed Matthew toward Spintend’s ADC adapter (or Lenco’s equivalent) for brake-light and turn-signal control on the 100/100, reinforcing that most Ubox variants lack native lighting outputs and need a daughter board.【F:data/vesc_help_group/text_slices/input_part013.txt†L17111-L17150】
- His accessory rail now hangs off an external 12 V/20 A buck that feeds a horn, pumps, lights, and fans; Noname’s math helped quantify that such a converter only sips ~4–6 A from a 60 V pack, but horns remain the biggest momentary draw so he’s trimming controller battery amps from 90 A to ~84 A to preserve BMS headroom.【F:data/vesc_help_group/text_slices/input_part013.txt†L17300-L17340】【F:data/vesc_help_group/text_slices/input_part013.txt†L17449-L17477】
- For high-current links the crew still favours XT90s up to ~110 A battery, stepping to dual XT90s or a single QS8 once the Spintend pulls harder—advice worth folding into connector spec sheets.【F:data/vesc_help_group/text_slices/input_part013.txt†L17329-L17333】

#### Battery Packaging & BMS Strategy
- Pandalgns is moving his Halo T107 Pro from a tired 20 S pack (now maxing out at 66.5 V) to a tightly packaged 22 S 10 P P45B block; the drawer extender leaves only millimetres of clearance, so the group recommended offset rows and compression wraps to stop cell abrasion in the new layout.【F:data/vesc_help_group/text_slices/input_part013.txt†L17621-L17635】
- The same builder can’t find an ANT BMS rated above 420 A continuous; peers advised either splitting the load across two BMS units or respecting the datasheet’s 45 A continuous rating per cell and accepting accelerated wear if they pull the full 300–350 A target.【F:data/vesc_help_group/text_slices/input_part013.txt†L17525-L17545】

#### Controls, Instrumentation & Failure Reports
- Multiple riders keep asking whether shorting ADC1 to ground with a momentary switch will cycle VESC profiles; reports of MakerX ADC3 daughterboards burning up sparked calls for a vetted wiring diagram, especially for three-position “gear” toggles that need the throttle moved to ADC2.【F:data/vesc_help_group/text_slices/input_part013.txt†L17274-L17280】【F:data/vesc_help_group/text_slices/input_part013.txt†L17767-L17776】【F:data/vesc_help_group/text_slices/input_part013.txt†L17838-L17843】【F:data/vesc_help_group/text_slices/input_part013.txt†L18297-L18305】
- 'lekrsu' fixed Xiaomi Pro 2 speed telemetry by forcing the motor gear ratio to 1 and shared an ADC2 “gear shift” script, although he can’t run it himself because of noisy analog lines—worth testing before publishing a how-to.【F:data/vesc_help_group/text_slices/input_part013.txt†L18155-L18160】【F:data/vesc_help_group/text_slices/input_part013.txt†L18483-L18487】
- Jason confirmed Lonnyo 75 H motors ship with 10 kΩ NTCs that play nicely with Ubox thermistor scaling; 100 kΩ sensors technically read but lose accuracy at low temperatures, so spec sheets should steer riders toward 10 k replacements.【F:data/vesc_help_group/text_slices/input_part013.txt†L18489-L18495】
- Noname’s dual-pack moped managed to short a QS8 and vaporise the Ignite logic stack the moment he cracked the throttle—despite balanced phase resistances—highlighting how little warning a compromised high-current harness can give before a total controller failure.【F:data/vesc_help_group/text_slices/input_part013.txt†L18312-L18333】【F:data/vesc_help_group/text_slices/input_part013.txt†L18402-L18418】

### Batch 12 Highlights (lines 15500–16999)

#### Controller Limits & Rumoured Hardware
- 🇪🇸AYO#74 and Face de Pin Sucé confirmed that MakerX G300 controllers struggle on 22 S packs above ~320 A phase—saturation and heating appear sooner than on comparable 3Shul units that comfortably handle 200 A battery / 400 A phase—so racers are reverting to the C350 when they need full 22 S torque headroom.【F:data/vesc_help_group/text_slices/input_part013.txt†L15507-L15540】
- JPPL teased a forthcoming MakerX module advertised at 100 V with 1 200 A peak, while Paolo is prototyping a similarly sized 120 V 12‑fet design that is “not soon,” underscoring how speculative the firmware claims remain until hardware ships.【F:data/vesc_help_group/text_slices/input_part013.txt†L15548-L15550】
- K3BAB launched a €20 VESC‑Express (ESP32‑S3) add-on that bridges CAN to BLE/Wi‑Fi and can drive LEDs or BLE remotes, giving builders a drop-in telemetry upgrade over aging SPP dongles.【F:data/vesc_help_group/text_slices/input_part013.txt†L16485-L16488】

#### Motor Hardware & Chassis Fitment
- Dualtron Achilleus twisted a 90 H axle because the Lonnyo shaft is narrower than Thunder arms; the fix is swapping to tighter Victor arms or adding torque hardware, and builders report the 90 H package needs 176 mm openings with little-to-no spacer stack, making tolerance checks mandatory.【F:data/vesc_help_group/text_slices/input_part013.txt†L15577-L15603】【F:data/vesc_help_group/text_slices/input_part013.txt†L16218-L16240】
- Shlomozero’s bent 80 H stator was traced to the dual-magnet/key design; riders note the revised single-magnet 80 H cores fare better, but sustained 400–450 A pulls still demand monitoring despite the addictive torque.【F:data/vesc_help_group/text_slices/input_part013.txt†L16115-L16122】
- Deck packaging comparisons show the Achilleus’ 18.1 cm bay cannot house a 22 S 11 P pack without major surgery, whereas Thunder decks offer 22.1 cm of width and support extended boxes for large parallels, guiding legal build planning.【F:data/vesc_help_group/text_slices/input_part013.txt†L16218-L16240】

#### Power, Charging & Touring Logistics
- Noname logged a 260‑mile, 12‑hour mountain ride by stringing together 45 A roadside charges (roughly 100 mi restored to 74 % in an hour); the pack tolerates 50 A but 70 A “is too much,” so future guides should stress cooling margin when touring at those rates.【F:data/vesc_help_group/text_slices/input_part013.txt†L16054-L16058】【F:data/vesc_help_group/text_slices/input_part013.txt†L16440-L16452】
- The same trip highlighted the value of shaded 50 A stops and spare phones for offline navigation, illustrating practical logistics for multi-state scooter routes.【F:data/vesc_help_group/text_slices/input_part013.txt†L16112-L16121】【F:data/vesc_help_group/text_slices/input_part013.txt†L16347-L16376】
- Yamal captured a 147 km/h pass on his 20 S 10 P Samsung 40 T pack with traction control disabled and plans to chase 160 km/h on 22 S after fitting new slicks, reinforcing the need for fresh tire safety guidance before further tests.【F:data/vesc_help_group/text_slices/input_part013.txt†L15952-L15960】【F:data/vesc_help_group/text_slices/input_part013.txt†L16340-L16398】

#### Accessory Power & Field Fixes
- Riders advised against running both Dualtron headlights and taillights from the Spintend 12 V/3 A rail—past installs only trusted a brake light—so documentation should spell out safe accessory budgets and when to add external bucks.【F:data/vesc_help_group/text_slices/input_part013.txt†L16042-L16046】
- Smart Repair confirmed that mistakenly marking a Spintend BLE module as “paired” can be reversed over USB by clearing the flag, a handy recovery step for field techs.【F:data/vesc_help_group/text_slices/input_part013.txt†L16110-L16111】【F:data/vesc_help_group/text_slices/input_part013.txt†L16461-L16468】

### Batch 11 Highlights (lines 14000–15499)

#### Long-Range Riding & Charging Logistics
- Noname logged an 18-hour Appalachian ride covering roughly 150 miles at 50 mph bursts, noting the VESC stayed cool and musing that a 1 kW generator plus 5 kWh pack could support future coast-to-coast attempts.【F:data/vesc_help_group/text_slices/input_part013.txt†L14000-L14013】
- The crew compared public-charging strategies: J1772 adapters let them feed even 2 A bricks from Level 2 pedestals, but app locks typically release only one handle per session and Tesla plugs still need protocol triggers such as FoCcci boards.【F:data/vesc_help_group/text_slices/input_part013.txt†L14125-L14300】

#### Ninebot F2 Pro & Sensorless Tuning Notes
- ScooterHacking Firmware users confirmed that fully sensorless launches are acceptable—the initial “brr” noise is simply the controller switching from hall emulation—and called out that the F2 Pro’s stock over-current protection trips near 30 A even if higher limits are set in the utility app.【F:data/vesc_help_group/text_slices/input_part013.txt†L14017-L14056】【F:data/vesc_help_group/text_slices/input_part013.txt†L14042-L14067】
- Because the F2’s BMS cannot detect externally paralleled packs, riders planning add-on batteries were advised to share current through the auxiliary pack while respecting the native 25–30 A ceiling to avoid tripping the internal protection mid-ride.【F:data/vesc_help_group/text_slices/input_part013.txt†L14045-L14067】

#### High-Torque Motor Stress & Magnet Construction Lessons
- Builders chasing torque highlighted the 7" LY 90 H hub’s 127 mm stator and 40-magnet rotor, explaining why it hits harder than 110 mm-class 75/80/90 H cans but demands matching 7" tire availability.【F:data/vesc_help_group/text_slices/input_part013.txt†L14065-L14083】
- Multiple 80 H 22×3 motors twisted their stators after 350–500 A phase assaults and 133–144 °C core temps; Paolo warned that prolonged heat softens the laminations’ glue, demagnetises rotors above ≈120 °C, and that LY’s double-magnet stacks exacerbate the risk.【F:data/vesc_help_group/text_slices/input_part013.txt†L14331-L14349】【F:data/vesc_help_group/text_slices/input_part013.txt†L14382-L14395】【F:data/vesc_help_group/text_slices/input_part013.txt†L14576-L14585】
- Race techs such as Face de Pin Sucé said they now wind their own stators—after seeing LY 70/75/80 H units twist under 400 A—and keep traction control mandatory even on custom builds that run 0–100 km/h in about 3.7 s.【F:data/vesc_help_group/text_slices/input_part013.txt†L14616-L14642】
- Leon’s data point shows a single 60 H hub surviving 500 A launches and 107 km/h without field-weakening, underscoring both the torque potential and the heat-management challenge when running smaller rotors that hard.【F:data/vesc_help_group/text_slices/input_part013.txt†L14682-L14736】

#### Race Logistics, Sourcing & Shipping
- European teams discussed exporting race hardware to Israel—Face de Pin Sucé can ship rims and stators separately to dodge customs classification, though it is labour-intensive compared with sourcing straight from China.【F:data/vesc_help_group/text_slices/input_part013.txt†L14762-L14775】
- Ambrosini’s RM-X program continues to rely on stock G300 controllers with factory firmware while supplementing them with in-house motors, highlighting that controller prep—not reflashing—is the current bottleneck for many EU race entrants.【F:data/vesc_help_group/text_slices/input_part013.txt†L14653-L14663】

#### Build Logs & Performance Benchmarks
- Yamal’s 33×2 daily driver keeps delivering 0–100 km/h pulls, ~30 kW peaks, and 11 k rpm spins at 200/300 A limits while he plans traction-control-off testing to chase 140 km/h once new tires arrive.【F:data/vesc_help_group/text_slices/input_part013.txt†L14667-L14678】【F:data/vesc_help_group/text_slices/input_part013.txt†L15388-L15500】
- Dualtron Achilleus pushed a single rear 90 H (127 mm) hub to 330 A phase on an 85 250, reporting roughly 45 % more torque versus his 75 H 110 mm motor and reminding riders that the 90 H requires 7" rubber while 75 H fits 6.5" hoops.【F:data/vesc_help_group/text_slices/input_part013.txt†L14974-L15025】
- Matthew’s logs compare Lonnyo 65 H 22×3 versus 17×4 hubs: 16 S/260 A phase with Statorade holds ~8 kW but needs airflow above 35 mph, whereas the 17×4 setup suits lower-power reliability until he upgrades the Yume Y11+ with higher-torque motors.【F:data/vesc_help_group/text_slices/input_part013.txt†L14844-L15005】
- NAMI owners chasing 170 A battery and 200 A phase still see ~19 kW plateaus unless both VESCs report, suggesting data logging must aggregate dual-controller outputs to capture true system power.【F:data/vesc_help_group/text_slices/input_part013.txt†L14964-L14972】
- KierreKikkeli’s Vsett 10+ lost half its speed after a motor lead repair; corrosion-soaked capacitors inside the Xiaomi-derived Ubox were the culprit, reinforcing the need for conformal coating or enclosure sealing in winter climates.【F:data/vesc_help_group/text_slices/input_part013.txt†L15110-L15236】

#### Controller & Peripheral Updates
- MakerX quietly posted a “K900” firmware package hinting at a forthcoming 96 V controller rated around 800 A battery, 1 200 A motor, and 1 500 A absolute; the community is still treating those numbers as unverified firmware scaffolding rather than shipping specs.【F:data/vesc_help_group/text_slices/input_part013.txt†L14963-L14963】【F:data/vesc_help_group/text_slices/input_part013.txt†L15219-L15224】【F:data/vesc_help_group/text_slices/input_part013.txt†L15411-L15438】
- Matthew is keeping his 100/100 Lite around 16 S, 85–110 A battery, and 20–30 A of field weakening after ’lekrsu warned that the setup runs hot; even with liquid cooling the FETs climb quickly on long hill pulls, so daily riders should log temps and dial FW back when sustained loads are planned.【F:data/vesc_help_group/text_slices/input_part013.txt†L14844-L14854】【F:data/vesc_help_group/text_slices/input_part013.txt†L15041-L15048】
- One Spintend 100/100 owner reported the controller refusing to shut down even with ADC auto-off timers disabled, suggesting a pending troubleshooting note on accessory power bleed or stuck logic rails.【F:data/vesc_help_group/text_slices/input_part013.txt†L14888-L14892】
- NetworkDir showcased a refreshed LVGL dashboard for Ubox builds, warning that earlier display libraries caused burn-in while the current codebase is modular enough to support custom themes once time allows for polishing.【F:data/vesc_help_group/text_slices/input_part013.txt†L14860-L14882】

#### Safety & Policy Reminders
- After witnessing a fatal Las Vegas crash, riders reiterated that untrained scooter users often ignore traffic rules; local police reportedly ticket any micromobility device capable of >35 mph, so high-power builds need compliant riding plans when using public streets.【F:data/vesc_help_group/text_slices/input_part013.txt†L15064-L15090】【F:data/vesc_help_group/text_slices/input_part013.txt†L15084-L15086】

### Batch 7 Highlights (lines 8201–9700)

#### High-Current Tuning & Reliability
- Matthew reminded builders that Spintend 85240/85250 controllers dislike battery limits above ≈240–250 A even if phase current is pushed higher, while Yamal still caps his dual setup around 300 A per motor for everyday use.【F:data/vesc_help_group/text_slices/input_part013.txt†L8242-L8256】
- ✨🇪🇸عمر’s inspection redo killed one controller’s ADC rail until he rewired everything and dropped ABS overcurrent trips to 260 A, highlighting how post-service harness faults can masquerade as firmware issues.【F:data/vesc_help_group/text_slices/input_part013.txt†L8352-L8355】
- Hackintoshhhh is running 150 A battery / 240 A phase on an 85150 and ~270 A battery / 380–400 A phase on an 85250 Lime build, but still limits throttle profiles to 40 % because the scooter becomes unwieldy with full punch.【F:data/vesc_help_group/text_slices/input_part013.txt†L8422-L8462】
- 🆁aphaël 🅵ou🅹iwara cautioned that 70–100 H motors with identical windings only tolerate ~450 A briefly before saturation/heat, and Eduuuuuuuuu confirmed 50 H 17×4 hubs cook themselves past 100 A phase without cooling upgrades.【F:data/vesc_help_group/text_slices/input_part013.txt†L8384-L8385】【F:data/vesc_help_group/text_slices/input_part013.txt†L8727-L8727】
- Rogerio Figueiredo reported a stock-firmware Spintend burning out within two days at 20 S (180 A phase / 80 A battery, no ABS slow ramp), while Yamal’s replacement 240 now cruises at 150 A battery / 250 A phase without drama—underlining the need for conservative defaults when users skip current-smoothing features.【F:data/vesc_help_group/text_slices/input_part013.txt†L9077-L9096】

#### Battery Packs & BMS Logistics
- Yamal is dailying a 20 S 10 P pack on 0.1 mm copper laminations with only a 40 A ANT charge BMS after his discharge unit arrived defective, accepting the fire risk until a replacement ships—friends urged him to restore full protection before another ESC failure.【F:data/vesc_help_group/text_slices/input_part013.txt†L8854-L8876】
- Hackintoshhhh stacks twin 0.1 mm copper sheets because his Glitter 801D welder cannot reliably weld a single 0.2 mm busbar, showing a practical workaround for builders stuck on hobby welders.【F:data/vesc_help_group/text_slices/input_part013.txt†L8924-L8939】
- Paolo noted that MOSFET-based smart BMS boards waste noticeable power and would rather deploy relay-style units when space allows.【F:data/vesc_help_group/text_slices/input_part013.txt†L8979-L8980】
- Rogerio later asked for wiring help on a new BMS harness despite “following the diagram,” signaling a need for clearer connection guides for high-current packs.【F:data/vesc_help_group/text_slices/input_part013.txt†L9388-L9393】

#### Braking, Tires & Ride Comfort
- cihan eliminated Ninebot F2 Pro brake wobble by switching to sintered-metal pads on cheap rotors, trading pad longevity for drastically higher bite once warmed.【F:data/vesc_help_group/text_slices/input_part013.txt†L8828-L8831】
- PMT Junior tires are fetching €60–€70 in Europe; riders praise their grip over Stradales but warn that narrow Dualtron rims make them look skinny and complicate noise diagnosis when chassis vibrations arise.【F:data/vesc_help_group/text_slices/input_part013.txt†L9032-L9068】

#### Packaging, Controls & Legal Builds
- Ausias is commissioning a ventilated yet splash-resistant 3D-printed enclosure for the Spintend controller after finding dust packed into his Kelly harness despite light-duty riding.【F:data/vesc_help_group/text_slices/input_part013.txt†L8512-L8517】
- Yamal and Ausias are sketching “legal” Spanish builds—keeping a Ninebot G2 on single-motor VESC control while stretching Dualtron frames for longer battery boxes—and pricing DGT-compliant frames like the Thunder 3 around €1.5–2 k.【F:data/vesc_help_group/text_slices/input_part013.txt†L8880-L8953】
- JPPL documented the MakerX push-button workflow: set App → General → Shutdown Method to “always on” with a delay (e.g., 5–30 minutes) and reference MakerX’s official power-switch guide so the G300’s momentary switch works as intended.【F:data/vesc_help_group/text_slices/input_part013.txt†L8958-L8960】
- Mirono’s PAS-pin question confirms the community still needs definitive I/O voltage tables for MakerBase accessories when mixing PAS sensors and ADC throttles.【F:data/vesc_help_group/text_slices/input_part013.txt†L8946-L8947】

#### Troubleshooting & Open Questions
- Patrick’s MakerBase build keeps hard-resetting mid-ride even with ABS limits at 225 A and a healthy BMS, suggesting deeper hardware diagnostics beyond simply raising absolute current limits.【F:data/vesc_help_group/text_slices/input_part013.txt†L9039-L9298】
- Multiple riders are chasing proper axle spacers for 75 H 155 mm Lonnyo motors on stock Dualtron suspension arms; Shlomozero’s trial-and-error photos imply uneven washer stacks, and Face de Pin Sucé warned LY axles can vary by 5 mm.【F:data/vesc_help_group/text_slices/input_part013.txt†L9119-L9125】【F:data/vesc_help_group/text_slices/input_part013.txt†L9310-L9371】
- V keeps asking whether a Flipsky 75100 dual or FT85BD suits a stock Vsett 11+, underscoring the demand for a concise controller comparison geared toward mid-power commuters.【F:data/vesc_help_group/text_slices/input_part013.txt†L9230-L9336】
- Rogerio’s MakerBase 75100 success story on a Xiaomi (60 A battery / 180 A phase at 22 S) contrasts with the stock Spintend failure above, offering a datapoint for riders weighing which controller family to trust.【F:data/vesc_help_group/text_slices/input_part013.txt†L9135-L9146】

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
- Document enclosure-sealing or debris-screening practices that keep Ubox and similar controllers from ingesting grit during light-duty rides—Yamal already lost one controller this way—and capture Ausias’s plan for a ventilated 3D Spintend box that balances airflow with splash protection.【F:data/vesc_help_group/text_slices/input_part013.txt†L3362-L3375】【F:data/vesc_help_group/text_slices/input_part013.txt†L8508-L8512】
- Outline the Max G2 dropout-widening process (‘lekrsu’ bushings, bolt lengths, torque checks) so future conversions can replicate the 150 mm spacing safely.【F:data/vesc_help_group/text_slices/input_part013.txt†L2733-L2749】
- Detail safe ways to parallel 12 V accessory feeds (current limits, wiring, fuse guidance) on MakerBase/Spintend builds so riders aren’t overloading shared bucks.【F:data/vesc_help_group/text_slices/input_part013.txt†L4085-L4103】
- Research whether Spinny/ADC v2 harnesses can source sufficient current for dual-function 12 V tail/brake lights and outline any required relays or firmware hooks.【F:data/vesc_help_group/text_slices/input_part013.txt†L5127-L5127】
- Gather controller and battery envelope data to answer Arnau’s 100 V 100 A single-motor current ceiling question before he exceeds his 17×4 hub and Victor pack limits.【F:data/vesc_help_group/text_slices/input_part013.txt†L4996-L5002】
- Summarize best practices for mixing internal/external packs with ideal diodes or other current blockers so cihan’s parallel battery plan avoids regen-induced surges or BMS stress.【F:data/vesc_help_group/text_slices/input_part013.txt†L5118-L5136】【F:data/vesc_help_group/text_slices/input_part013.txt†L11771-L11943】
- Clarify what the different VESC Tool backup formats store (XML vs C vs UUID) and where those exports live so S1m 0n can create a reliable recovery bundle.【F:data/vesc_help_group/text_slices/input_part013.txt†L5211-L5211】
- Capture guidance for wiring four VESCs over CAN (ID assignment, power sequencing, watchdogs) for Adrian’s 4WD 75100 Pro v2 project.【F:data/vesc_help_group/text_slices/input_part013.txt†L6072-L6074】
- Document how to invert key-switch logic on MakerBase 84100HP hardware without rewiring the harness so chris can correct his reverse-acting switch.【F:data/vesc_help_group/text_slices/input_part013.txt†L6685-L6688】
- Investigate MP2 v0.6 voltage-sense calibration steps (divider values, firmware defines) to resolve Patrick’s inaccurate pack readings before he rides.【F:data/vesc_help_group/text_slices/input_part013.txt†L6691-L6695】
- Provide shielding or filtering recommendations that prevent Mirono’s boot-time throttle spikes around 2 V on ADC1.【F:data/vesc_help_group/text_slices/input_part013.txt†L6378-L6381】
- Build an MP2 bring-up checklist (component verification, buck-rail measurements, VIN-sense probing) to help Patrick finish debugging his freshly assembled board.【F:data/vesc_help_group/text_slices/input_part013.txt†L6703-L6755】
- Outline how to adapt four-wire Spintend power buttons to the G300 (connector repin, UART2 mapping, on/off menu settings).【F:data/vesc_help_group/text_slices/input_part013.txt†L6855-L6874】【F:data/vesc_help_group/text_slices/input_part013.txt†L7722-L7724】
- Document the regen-braking configuration workflow for Flipsky 75100 controllers so newcomers like fry the guy have a reference instead of scattered chat replies.【F:data/vesc_help_group/text_slices/input_part013.txt†L7394-L7399】
- Draft a Spintend inspection/rewire checklist that verifies breaker wiring, ADC functionality, and ABS limits so post-service faults like Omar’s 260 A rollback are caught before riding.【F:data/vesc_help_group/text_slices/input_part013.txt†L8352-L8355】
- Expand the Spintend 85××× current envelope guide with community-tested limits (Matthew’s 240–250 A battery cap, Hackintoshhhh’s 270 A setups, Rogerio’s stock burnouts) plus throttle-scaling tips for taming high-power builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L8242-L8462】【F:data/vesc_help_group/text_slices/input_part013.txt†L9077-L9096】
- Publish a safety note on running charge-only BMS wiring and recommend robust replacements so riders aren’t tempted to daily 20 S packs without discharge protection like Yamal.【F:data/vesc_help_group/text_slices/input_part013.txt†L8854-L8876】
- Capture welding strategies for 0.2 mm copper busbars—including stacked 0.1 mm laminations and welder settings—for builders stuck with hobby gear such as the Glitter 801D.【F:data/vesc_help_group/text_slices/input_part013.txt†L8924-L8939】
- Add a Ninebot F2 Pro brake upgrade recipe (sintered pads, rotor sourcing, expected wear) based on cihan’s wobble fix.【F:data/vesc_help_group/text_slices/input_part013.txt†L8828-L8831】
- Write up an 80/100 H wheel-centering and dual-caliper setup guide (kit sourcing, torque, clearance checks) so track-focused Nami/Dualtron builds can copy the wobble fix Arnau and Yamal are lining up.【F:data/vesc_help_group/text_slices/input_part013.txt†L8010-L8016】
- Outline the paperwork and chassis tweaks required to legalise Dualtron/Ninebot builds in Spain, including Thunder 3 pricing and G2 single-motor VESC options.【F:data/vesc_help_group/text_slices/input_part013.txt†L8880-L8953】
- Turn JPPL’s MakerX push-button advice into a quick-start guide so new G300 owners can configure shutdown delays without hunting through chat logs.【F:data/vesc_help_group/text_slices/input_part013.txt†L8958-L8960】
- Produce a washer-spacing diagram for fitting 75 H 155 mm Lonnyo hubs on Dualtron arms, noting LY axle tolerances and common spacer stacks.【F:data/vesc_help_group/text_slices/input_part013.txt†L9119-L9125】【F:data/vesc_help_group/text_slices/input_part013.txt†L9310-L9371】
- Extend the Spintend 85××× current guardrail doc with fresh 85250 V2 data (135 A battery / 300 A phase on stock FETs, Tokmas 120/160 A logs) so riders can set limits without blindly swapping MOSFETs.【F:data/vesc_help_group/text_slices/input_part013.txt†L20408-L20416】【F:data/vesc_help_group/text_slices/input_part013.txt†L20257-L20259】【F:data/vesc_help_group/text_slices/input_part013.txt†L22229-L22235】
- Capture Kaabo storm suspension upgrade notes (GTR 135 mm shock vs. dual-spring stacks) alongside ’lekrsu’s G2 plate/brake-mount redesign so commuters can silence pogo-stick builds safely.【F:data/vesc_help_group/text_slices/input_part013.txt†L20408-L20416】【F:data/vesc_help_group/text_slices/input_part013.txt†L20720-L20737】
- Build a Ninebot G30 deck-widening and battery-build primer that covers rail cutting, 6 P jig requirements, and wiring checks for drop-in commuter packs.【F:data/vesc_help_group/text_slices/input_part013.txt†L21223-L21241】
- Add a quick-reference graphic for wiring 10 kΩ NTC sensors to VESC TEMP/GND so newcomers stop guessing at polarity.【F:data/vesc_help_group/text_slices/input_part013.txt†L20153-L20155】
- Document stem-bolt and frame reinforcement strategies for 200 + lb Yisuntrek/WePoor chassis after LiquorHole’s crash autopsy showed the added fastener saved the scooter.【F:data/vesc_help_group/text_slices/input_part013.txt†L21431-L21483】
- Publish troubleshooting steps for FarDriver/FESC mobile-app crashes (burner email login, BT pairing order) and note that persistent flicker may require returning the unit.【F:data/vesc_help_group/text_slices/input_part013.txt†L20894-L20999】
- Investigate why some G300/Spintend builds only deliver half the commanded phase current and package a calibration checklist (duty caps, shunt scaling) for 6.05 users.【F:data/vesc_help_group/text_slices/input_part013.txt†L20563-L20599】【F:data/vesc_help_group/text_slices/input_part013.txt†L20891-L20935】
- Outline requirements for Yamal’s proposed 60–70 Ah “legal chassis” touring scooter (battery enclosure, waterproofing, fast-charge hardware) so future guides can cover endurance builds, not just drag setups.【F:data/vesc_help_group/text_slices/input_part013.txt†L21308-L21309】
- Draft a Lonnyo 70 H torque-hub cooling and gearing guide (dropout spacing, ferrofluid, tire sizing) so emoped builders stop overheating 220 A single-motor setups.【F:data/vesc_help_group/text_slices/input_part013.txt†L20011-L20052】
- Investigate the root cause of Patrick’s mid-ride MakerBase resets (power rail dips vs. firmware faults) and document a diagnostic workflow.【F:data/vesc_help_group/text_slices/input_part013.txt†L9039-L9298】
- Compare Flipsky 75100 dual and FT85BD controllers for stock Vsett 11+ commuters so recurring questions like V’s get a definitive answer.【F:data/vesc_help_group/text_slices/input_part013.txt†L9230-L9336】
- Draft a wiring diagram and validation steps for Rogerio’s pictured smart BMS harness to prevent misconnection on future 22 S builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L9388-L9393】
- Validate whether the bargain 20×3 AliExpress motors actually match Lonnyo performance (strand gauge, kV, thermal headroom) before the group buys out US overstock.【F:data/vesc_help_group/text_slices/input_part013.txt†L9672-L9724】
- Publish a high-current wiring guide for 75 H 22/3 hubs—phase-lead gauge, connector choices, and cooling checks—so riders don’t repeat Shlomozero’s 400 A overheating experiment.【F:data/vesc_help_group/text_slices/input_part013.txt†L9778-L9819】
- Capture the full G300 maintenance workflow (6.3 flashing steps, red LED fault codes, and auto-off fixes) so 🇪🇸AYO#74 doesn’t have to rely on the ANT BMS as a kill switch.【F:data/vesc_help_group/text_slices/input_part013.txt†L9654-L9671】【F:data/vesc_help_group/text_slices/input_part013.txt†L10682-L10718】
- Document the ANT 30 S BMS parameter map for 22 S packs (series count, capacity fields, wire order) to resolve Rogerio’s misreporting issue.【F:data/vesc_help_group/text_slices/input_part013.txt†L10135-L10156】
- Reproduce Mirono’s Flipsky 75100 V2 PAS failure at high phase current and propose firmware or observer tweaks that stop the post-pause vibration lock-up.【F:data/vesc_help_group/text_slices/input_part013.txt†L10188-L10205】
- Survey available 40 S BMS options (or modular stacks) that can pair with 3Shul’s 8–40 S CC1000 so future 30 S/40 S torque builds aren’t blocked by protection hardware.【F:data/vesc_help_group/text_slices/input_part013.txt†L10495-L10524】
- Detail the machining steps, tolerances, and brake-bleed requirements for running 3.6 mm rotors on Magura MT5/MT7 calipers as Ausias is attempting.【F:data/vesc_help_group/text_slices/input_part013.txt†L10752-L10788】
- Compile quantitative cooling data (temp probes, speed, ambient) comparing Statorade, ferrofluid fills, and dry hubs to resolve the mixed community feedback.【F:data/vesc_help_group/text_slices/input_part013.txt†L10299-L10309】
- Answer riekcn’s Ninebot G2 VESC selection question with a compatibility matrix covering horn/indicator support, wiring adapters, and firmware requirements.【F:data/vesc_help_group/text_slices/input_part013.txt†L10290-L10300】
- Source reliable LY hub temperature sensors or compatible BMS probes and provide installation wiring so 🇪🇸AYO#74 can restore thermal monitoring.【F:data/vesc_help_group/text_slices/input_part013.txt†L10722-L10741】
- Outline a repair or rebuild plan for the Teverun Fighter 11+ 60 V 35 Ah pack that currently only wakes with a charger connected, including cost/effort estimates for replacing two dead parallels of Samsung 50S cells.【F:data/vesc_help_group/text_slices/input_part013.txt†L10636-L10669】
- Turn the Ninebot F2 Pro discussions into a reference on sensorless-only launches, OCP behaviour (~30 A), and how to share load with external packs without tripping the stock BMS.【F:data/vesc_help_group/text_slices/input_part013.txt†L14017-L14067】
- Publish a mitigation guide for twisted 80 H stators—temperature thresholds, phase-current ceilings, and magnet construction differences—so high-power racers can set safer envelopes or upgrade hardware.【F:data/vesc_help_group/text_slices/input_part013.txt†L14331-L14395】【F:data/vesc_help_group/text_slices/input_part013.txt†L14576-L14585】【F:data/vesc_help_group/text_slices/input_part013.txt†L16115-L16122】
- Verify the rumoured MakerX K900/G900 controller specifications against hardware prototypes before builders plan around the 800 A battery / 1 200 A motor claims surfaced in the firmware bundle.【F:data/vesc_help_group/text_slices/input_part013.txt†L14963-L14963】【F:data/vesc_help_group/text_slices/input_part013.txt†L15219-L15224】【F:data/vesc_help_group/text_slices/input_part013.txt†L15411-L15438】
- Troubleshoot the Spintend 100/100 that refuses to shut down even with ADC auto-off disabled and document likely root causes (backfeed, stuck logic rails) plus fixes.【F:data/vesc_help_group/text_slices/input_part013.txt†L14888-L14892】
- Capture best practices for topping up from public EV chargers (adapter types, app locks, etiquette) so long-distance riders can safely replicate the J1772/Tesla workflows discussed.【F:data/vesc_help_group/text_slices/input_part013.txt†L14240-L14300】
- Outline customs-friendly shipping options for race-spec LY/Ambrosini motors headed to Israel, including the stator/rim split strategy Face de Pin Sucé mentioned.【F:data/vesc_help_group/text_slices/input_part013.txt†L14762-L14775】
- Audit the $80 California-stock 60 H hubs (strand count, magnet segmentation, axle tolerances, rim profile) before the community bulk-orders them for VESC conversions.【F:data/vesc_help_group/text_slices/input_part013.txt†L11001-L11055】【F:data/vesc_help_group/text_slices/input_part013.txt†L11417-L11455】
- Publish mounting guidance for Rage Mechanics’ Dualtron Victor/Luxury deck extension—hardware torque, wire routing, and battery clearances—so buyers can safely fit 21 S 6–7 P packs with Ubox controllers.【F:data/vesc_help_group/text_slices/input_part013.txt†L11184-L11218】
- Diagnose 🇪🇸AYO#74’s high-speed cut-outs (pothole-triggered current drop, suspected loose magnets) and capture inspection/repair steps before more 22 S riders hit the same fault.【F:data/vesc_help_group/text_slices/input_part013.txt†L11505-L11600】【F:data/vesc_help_group/text_slices/input_part013.txt†L11733-L11734】
- Create a concise two-wire brake-sensor wiring guide for Spintend/MakerBase hardware, including the VESC settings that cut throttle without forcing regen, to resolve AG.racing’s configuration question.【F:data/vesc_help_group/text_slices/input_part013.txt†L11751-L11794】
- Explain how to tune MakerX G300 controllers on 22 S—current ceilings, firmware prerequisites, and when to stay on 20 S—so builders understand the saturation limits highlighted in the latest testing.【F:data/vesc_help_group/text_slices/input_part013.txt†L15507-L15540】
- Draft torque-arm and deck-clearance guidance for fitting 90 H Lonnyo hubs to Dualtron frames (arm choices, spacer stacks, dropout prep) before more riders twist axles.【F:data/vesc_help_group/text_slices/input_part013.txt†L15577-L15603】【F:data/vesc_help_group/text_slices/input_part013.txt†L16218-L16240】
- Document safe accessory loads for Spintend’s 12 V/3 A rail (typical Dualtron lighting draws, when to add external bucks) so commuters stop overloading the controller supply.【F:data/vesc_help_group/text_slices/input_part013.txt†L16042-L16046】
- Model fast-charging thermal limits for touring packs—drawing on the 45–70 A road-trip logs—to recommend cooling/dwell times for 20 S class batteries.【F:data/vesc_help_group/text_slices/input_part013.txt†L16054-L16058】【F:data/vesc_help_group/text_slices/input_part013.txt†L16440-L16452】
- Publish a single-Ubox 100/100 setup sheet capturing the 130–135 A phase, 85–90 A battery, and 150–180 A absolute guardrails plus the duty/FW tweaks and cooling plate layout that finally stopped Matthew’s stutter and heat spikes.【F:data/vesc_help_group/text_slices/input_part013.txt†L17015-L17084】【F:data/vesc_help_group/text_slices/input_part013.txt†L17358-L17363】
- Turn the dual-disc vs. dual-caliper debate—and Matthew’s regen save—into a braking guide that spells out when dual rotors help, how to size levers/calipers, and why regen can’t replace hydraulics on high-speed builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L17238-L17266】【F:data/vesc_help_group/text_slices/input_part013.txt†L17360-L17380】
- Document 12 V accessory buck sizing (expected pack-side draw, horn surges) alongside connector upgrades so riders know when to step from XT90s to QS8s and how to keep BMS trips at bay.【F:data/vesc_help_group/text_slices/input_part013.txt†L17111-L17150】【F:data/vesc_help_group/text_slices/input_part013.txt†L17329-L17340】【F:data/vesc_help_group/text_slices/input_part013.txt†L17449-L17477】
- Identify >420 A continuous BMS options or dual-BMS architectures for 22 S 10 P P45B packs, including packaging tips for Halo T107 trays that barely clear compression wraps.【F:data/vesc_help_group/text_slices/input_part013.txt†L17525-L17545】【F:data/vesc_help_group/text_slices/input_part013.txt†L17621-L17635】
- Produce a safe ADC profile-switch wiring diagram (momentary vs. three-position) that prevents more burned MakerX ADC boards and clarifies how to relocate throttles when using ADC2 gear scripts.【F:data/vesc_help_group/text_slices/input_part013.txt†L17274-L17280】【F:data/vesc_help_group/text_slices/input_part013.txt†L17767-L17776】【F:data/vesc_help_group/text_slices/input_part013.txt†L17838-L17843】【F:data/vesc_help_group/text_slices/input_part013.txt†L18297-L18305】
- Reverse-engineer Noname’s Ignite meltdown—QS8 short, triple-pack harness, throttle-on detonation—so we can publish a pre-ride continuity and connector inspection checklist for high-current mopeds.【F:data/vesc_help_group/text_slices/input_part013.txt†L18312-L18333】【F:data/vesc_help_group/text_slices/input_part013.txt†L18402-L18418】
- Draft a VESC Tool “battery % vs. voltage” explainer (with lookup tables) so commuters know when to expect soft power limits instead of trusting the inaccurate default SoC gauge.【F:data/vesc_help_group/text_slices/input_part013.txt†L12504-L12530】
- Capture Rage Mechanics’ SmartDisplay integration (bundle pricing, telemetry features, upcoming standalone sale) alongside Jason’s SimpleVescDisplay firmware path so builders know their instrumentation options without buying a full controller kit.【F:data/vesc_help_group/text_slices/input_part013.txt†L21517-L21557】【F:data/vesc_help_group/text_slices/input_part013.txt†L21820-L21824】
- Publish a stem/brake upgrade brief that contrasts the 1.7 kg solid Anatoly stem with Rage’s 0.8 kg titanium alternative and explains when Hope vs. Beringer calipers make sense on Dualtron race builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L21621-L21644】
- Compile Sava vs. PMT 90 mm tire notes (availability, grip, longevity) so riders choosing slicks understand the trade-offs before importing rare sizes.【F:data/vesc_help_group/text_slices/input_part013.txt†L21653-L21676】
- Document how to package a DGT-legal Dualtron Victor long chassis (21 S 7 P/22 S packs, Thunder arms, Ubox controllers) without buying a Thunder 3, including enclosure tolerances around the stock 20 S 10 P battery case.【F:data/vesc_help_group/text_slices/input_part013.txt†L21798-L21806】【F:data/vesc_help_group/text_slices/input_part013.txt†L21838-L21856】
- Write an ANT fast-charging and wiring guide that covers 20 A charge limits, connector choices (XT60 vs. XT90-S), and recommended wire gauges for 100 Ah prismatic packs targeting 270 A bursts.【F:data/vesc_help_group/text_slices/input_part013.txt†L22075-L22116】
- Outline a thermal and traction-control checklist for mixed 70 H/100 H dual-motor setups—field-weakening offsets, ERPM deltas, temp-sensor restoration—so 🇪🇸AYO#74 and peers stop roasting rear hubs past 110 °C.【F:data/vesc_help_group/text_slices/input_part013.txt†L22139-L22178】
- Stress-test MakerBase 75200s at 250 A+ phase to determine whether firmware or hardware causes the long-run power fade Shlomozero logged at 150 A battery.【F:data/vesc_help_group/text_slices/input_part013.txt†L12531-L12533】
- Compare Kaabo and Nami hub upgrades—phase-lead gauge, stator fill, bullet connectors—and document what’s required to let Nami motors survive above 200 A phase without cable damage.【F:data/vesc_help_group/text_slices/input_part013.txt†L12545-L12559】
- Write a Hope Tech/Tesch 3 caliper service note covering piston re-greasing, compatible pad sizes, and bedding so other riders can replicate 🇪🇸AYO#74’s first successful rebuild.【F:data/vesc_help_group/text_slices/input_part013.txt†L12697-L12702】
- Produce a regen safety checklist for 75200-class controllers paired with JBD BMS units—covering allowable battery regen amps, Xiaoxiang config, and VESC voltage caps—to prevent more MOSFET failures like Morten Jensen’s.【F:data/vesc_help_group/text_slices/input_part013.txt†L13850-L13879】
- Survey commercially available 40–50 A chargers, their connector options, and safe charge-rate guidance so racers like Ausias can plan between-session top-ups without abusing their packs.【F:data/vesc_help_group/text_slices/input_part013.txt†L13132-L13148】
- Measure LY tubeless rim runout, bead-seat geometry, and bolt patterns, then recommend machining fixes or alternative rims to stop the vibration and service issues Face de Pin Sucé highlighted.【F:data/vesc_help_group/text_slices/input_part013.txt†L13620-L13646】
- Compile a vetted MP2 controller buying and integration guide (board sources, voltage headroom, connector pinouts) so builders like Patracy don’t get scammed when sourcing 24–36 S-capable hardware.【F:data/vesc_help_group/text_slices/input_part013.txt†L13507-L13516】【F:data/vesc_help_group/text_slices/input_part013.txt†L13598-L13600】【F:data/vesc_help_group/text_slices/input_part013.txt†L13662-L13666】

### Batch 10 Highlights (lines 12500–13999)

#### Battery Management & Regen Safety
- 'lekrsu' reminded builders that VESC Tool’s state-of-charge percentage is notoriously wrong unless you pair it with Vedder’s own BMS, so riders like Noname should ignore the % readout and lean on real-time voltage when they lower per-cell cutoffs to ~3 V.【F:data/vesc_help_group/text_slices/input_part013.txt†L12504-L12530】
- Face de Pin Sucé benchmarked race scooters dropping 4–8 V under a 22 S load and warned that >10 V of sag is excessive, while Yamal’s logs show his 20 S commuter losing 10–13 V when he pulls 200 A per controller yet keeping pack and ESC temperatures in check—useful guardrails for high-current tuning.【F:data/vesc_help_group/text_slices/input_part013.txt†L12852-L12871】
- Morten Jensen’s blown 75200 MOSFET traced back to regen settings: 'lekrsu' stressed that braking wattage still flows into the battery, JBD BMS limits must be raised (e.g., to 100 A) via the Xiaoxiang app, and VESC’s max regen voltage has to stay within pack limits or regen spikes will toast hardware.【F:data/vesc_help_group/text_slices/input_part013.txt†L13850-L13879】

#### Controller Behaviour & Acceleration Tuning
- Shlomozero’s MakerBase 75200 fades after extended runs at 250 A phase / 150 A battery despite a 100–110 °C thermal cut, signalling that the controller may current-limit under sustained stress even when temperatures look safe.【F:data/vesc_help_group/text_slices/input_part013.txt†L12531-L12533】
- Noname solved L000’s weak sub‑20 km/h launch by cutting the PPM positive ramp time from the 0.4 s default to ~0.2 s, reinforcing how throttle ramping shapes off-the-line response on VESC builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L12688-L12691】
- Paolo told rider “V” that sine-wave controllers enforce phase-current limits, so swapping from a 40 A square-wave ESC to VESC feels softer unless you add halls/mxlemming observer and raise phase current targets toward 200 A per controller.【F:data/vesc_help_group/text_slices/input_part013.txt†L13612-L13619】【F:data/vesc_help_group/text_slices/input_part013.txt†L13694-L13699】
- Matthew’s single 85250 on 14 S/35 A battery and 100 A phase surges erratically above ~80 % throttle once he adds 20 A of field weakening, and Paolo confirmed the jitter is FW-induced—evidence to document when advising top-speed tuners.【F:data/vesc_help_group/text_slices/input_part013.txt†L13012-L13044】
- Arnau and Ausias expect the revised Spintend 85250 V2 to tolerate 22 S packs (≈92 V), but the group is still looking for long-term data before committing race builds to that voltage.【F:data/vesc_help_group/text_slices/input_part013.txt†L12981-L12984】

#### Motors, Wheels & Hardware Reliability
- Franchesco and عمر compared high-power hubs: Kaabo 60 H/33×3 stators ship with thicker phase leads and shrug off >200 A, while Nami’s stock motors overheat beyond ~200 A and need upgraded cabling, motivating drivetrain swaps for 300 A builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L12545-L12559】
- 🇪🇸AYO#74 finally cured a sticky Hope brake by disassembling and re-greasing the pistons—his first trouble-free run in four years—and noted the Tesch 3 V4 pads are 2 mm taller than the earlier tablets, which affects spares planning.【F:data/vesc_help_group/text_slices/input_part013.txt†L12697-L12702】
- Yamal’s 33/2 winding continues to impress: his dual-motor setup holds ~49–63 °C motor temps during hard pulls, resetting expectations for how much torque these “speed” winds can deliver.【F:data/vesc_help_group/text_slices/input_part013.txt†L13239-L13247】
- Face de Pin Sucé dissected older Rion frames and found cracked steering heads, flexing plates, under-specced Kelly controllers and fan ducts that blow straight into walls—evidence that modern builds need reinforcement or different chassis.【F:data/vesc_help_group/text_slices/input_part013.txt†L12985-L12994】
- The same reviewer flagged LY’s current tubeless rims for off-center mounting holes, missing bead seats and inverted bolt patterns that force you to pull brake discs to remove the wheel, causing vibration and service headaches at speed.【F:data/vesc_help_group/text_slices/input_part013.txt†L13620-L13646】

#### Builds, Charging & Marketplace Notes
- Ausias is shopping for 40–50 A chargers so he can fully recharge between race sessions; peers pointed out that 20 A units already refill large packs in ~2 h but acknowledged quick-charge hardware is scarce and pricey (>€200).【F:data/vesc_help_group/text_slices/input_part013.txt†L13132-L13148】
- Matthew documented his Ninebot Max G30LP conversion: single Spintend 100/100 Lite with 14 S 20 Ah pack at 40 A battery / 100 A phase, Lonnyo 65 H 17×4 hub with Statorade, dual light bars, water-cooled VESC plate, reinforced Monorim suspension and trunk space for stacking extra 16 S packs.【F:data/vesc_help_group/text_slices/input_part013.txt†L13685-L13687】
- MP2 interest is rising—Patracy wants a 24–36 S capable controller for a 270 V Hyundai generator motor, Hackintoshhhh has seven premade boards available, and the group just outed @JetGlideOfficial as a scammer sharing guitar-pedal photos instead of real hardware.【F:data/vesc_help_group/text_slices/input_part013.txt†L13507-L13516】【F:data/vesc_help_group/text_slices/input_part013.txt†L13598-L13600】【F:data/vesc_help_group/text_slices/input_part013.txt†L13662-L13666】
- Rogerio is hunting an NFC lock for Spintend controllers so he can ditch physical keys, signalling demand for plug-and-play immobilisers on premium VESC builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L13555-L13557】

### Batch 9 Highlights (lines 11000–12499)

#### Budget Hubs, Frames & Packaging
- Haku confirmed the bargain “$80” AliExpress hubs that ship from California are genuine 60 H cores with ~142 mm axles, but they use dual magnet rings and basic 21×3 tube rims—Noname warned the split magnets hurt smooth FOC, so buyers should budget for Ulip tubes and expect tubed rather than split-tubeless shells.【F:data/vesc_help_group/text_slices/input_part013.txt†L11001-L11044】【F:data/vesc_help_group/text_slices/input_part013.txt†L11417-L11455】
- LY told the group it can supply 11‑inch wheels on 130 mm axles, yet Haku and skrtt reiterated that wider 70–75 H Lonnyo stators still demand careful dropout spacing and washer stacks even on minibike frames.【F:data/vesc_help_group/text_slices/input_part013.txt†L11047-L11063】【F:data/vesc_help_group/text_slices/input_part013.txt†L11323-L11354】
- Face de Pin Sucé’s carbon deck extension for Dualtron Victor/Luxury/Compact adds 605 mm of mounting length (≈434 mm usable with a Ubox) and can house a 21 S 6–7 P pack alongside an 85 V 240 A controller, giving Spanish builders a bolt-on path to longer batteries without custom welding.【F:data/vesc_help_group/text_slices/input_part013.txt†L11184-L11218】
- Haku’s strap-assisted Xiaomi pump could not seat 21×3 slicks, and Noname reminded the crew that a high-volume shop compressor is the reliable way to pop those beads—portable inflators rarely deliver the burst those wide rims need even when ratchet straps are used.【F:data/vesc_help_group/text_slices/input_part013.txt†L6788-L6799】【F:data/vesc_help_group/text_slices/input_part013.txt†L11936-L11948】

#### Controller Limits & Firmware Behaviour
- Yamal reiterated that Spintend 85××× units stay reliable around 200 A battery / 300 A phase per controller on 20 S packs, dropping to 175 A battery for longevity, while the flashy “500 A” readouts simply total both controllers; Noname echoed the 200/300 envelope from his 400 lb moped logs.【F:data/vesc_help_group/text_slices/input_part013.txt†L11231-L11253】
- Dualtron Achilleus still tops out near 200 A phase even when 300 A is commanded on a single controller, hinting at shunt calibration limits or duty-cycle ceilings that need correcting before heavier 22 S builds can realise the advertised output.【F:data/vesc_help_group/text_slices/input_part013.txt†L11512-L11518】【F:data/vesc_help_group/text_slices/input_part013.txt†L11551-L11555】
- Haku is eyeing 250 A battery per 85250 for his Peak G30 builds but conceded earlier burnouts came from overheating during burnouts, underscoring the cooling headroom needed before leaning on those numbers.【F:data/vesc_help_group/text_slices/input_part013.txt†L11256-L11330】
- Matthew’s VESC Tool logs still overshoot phase current by ~23 A past a 260 A target and Noname only sees ~220 A despite 300 A commands, reinforcing the need to audit observer and current-sense calibration even after flashing hardware-no-limit firmware.【F:data/vesc_help_group/text_slices/input_part013.txt†L11551-L11555】【F:data/vesc_help_group/text_slices/input_part013.txt†L11696-L11707】【F:data/vesc_help_group/text_slices/input_part013.txt†L12060-L12066】
- Oreo huzky’s Apollo City dual-Lite project highlighted that Spintend’s Alu Lite logic harness uses a keyed multi-pin plug that builders must reuse or source when extending the loom—nobody in the thread had a part number yet, so future writeups should call out the exact connector family.【F:data/vesc_help_group/text_slices/input_part013.txt†L11752-L11762】

#### High-Speed Faults & Thermal Watch
- 🇪🇸AYO#74’s 22 S 70 H setup heats the rear motor/controller quickly and momentarily kills current when potholes strike above 125 km/h; enabling field weakening masks the error, hinting at loose magnets or wiring that needs inspection before the next top-speed run.【F:data/vesc_help_group/text_slices/input_part013.txt†L11505-L11600】【F:data/vesc_help_group/text_slices/input_part013.txt†L11733-L11734】
- He also found Schuls deliver noticeably more torque than G300s with the same parameters, and after lithium-grease maintenance couldn’t stop Hope calipers from sticking, so he’s reverting to Magura “Shigura” hybrids for reliability at race speeds.【F:data/vesc_help_group/text_slices/input_part013.txt†L11614-L11620】【F:data/vesc_help_group/text_slices/input_part013.txt†L11784-L11788】
- Dualtron Achilleus and ✨🇪🇸عمر logged 575 A combined phase on 22 S 11 P P45B packs but still need correct wheel-diameter inputs to match their 11‑inch tires and confirm the drivetrain is delivering the claimed ~38 kW without saturating the rear hub.【F:data/vesc_help_group/text_slices/input_part013.txt†L11779-L11783】【F:data/vesc_help_group/text_slices/input_part013.txt†L11826-L11837】【F:data/vesc_help_group/text_slices/input_part013.txt†L12069-L12093】
- 🇪🇸AYO#74’s LY 70 H rear hub also trips current when potholes hit at speed; Paolo suspects hardware fatigue, so the team is checking magnets, hall boards, and harness strain, which mirrors Fry the Guy’s front-motor “voltage imbalance” drag—evidence that Shul/Lonnyo race hubs need post-impact tear-downs before the next 22 S sprint.【F:data/vesc_help_group/text_slices/input_part013.txt†L11583-L11605】【F:data/vesc_help_group/text_slices/input_part013.txt†L11943-L11948】

#### Brake Maintenance & Service
- Skrtt blew a Magura MT5 lever seal by forcing the pads back without loosening the reservoir screw; earlier chats already warned that mixing oils swells lever seals, so the takeaway is to crack the bleed port before retracting pistons and rebleed with approved mineral oil to keep MT5/MT7 levers alive under race maintenance cadences.【F:data/vesc_help_group/text_slices/input_part013.txt†L7849-L7956】【F:data/vesc_help_group/text_slices/input_part013.txt†L11659-L11678】

#### Battery Planning & Cell Debates
- Yamal is dailying Samsung 40T cells in a 20 S 10 P layout (≈35 A nominal per cell) and reminded Shlomozero that LR2170LA “45 A” Lishens only hold that rating briefly, so matching cell data sheets against real discharge tests remains critical for 300 A builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L11296-L11314】
- Ausias plans to sell his 20 S 10 P P45B Nami pack to upgrade into a 22 S 11 P layout, while Yamal and عمر debated stacking extra parallels on top of the battery box to hit 11 P without crushing controller space—good context for anyone packaging 450 A-capable packs inside the Nami deck.【F:data/vesc_help_group/text_slices/input_part013.txt†L11947-L11956】【F:data/vesc_help_group/text_slices/input_part013.txt†L11968-L11995】
- Mattia’s homemade booster pack threw a fault after two idle weeks until AG.racing spotted a broken balance lead, so any parallel add-on that suddenly refuses to wake should trigger a full balance-wire inspection before chasing BMS swaps.【F:data/vesc_help_group/text_slices/input_part013.txt†L11657-L11658】
- Face de Pin Sucé clarified that Rage’s €999 CL350 dual-pack bundle includes harnessing, contactors, and hardware beyond the €400 single pack, explaining the premium Nami owners pay for a plug-in-ready kit.【F:data/vesc_help_group/text_slices/input_part013.txt†L11654-L11663】

#### Tires, Brakes & Ride Feel
- Haku’s $19 slicks sit flush on the Peak G30 rim, run quietly, and produce heavy burnout smoke, but he expects only a couple of hot-weather weeks of life—prompting plans to stock harder-compound PMTs once testing confirms cornering grip.【F:data/vesc_help_group/text_slices/input_part013.txt†L11840-L11870】
- Noname and skrtt compared PMT Stradale Juniors vs. regular Stradales: Juniors grip harder yet flatten quickly with straight-line riding, so skrtt is waiting on new rims to keep the profile round for daily use.【F:data/vesc_help_group/text_slices/input_part013.txt†L11895-L11908】
- skrtt burst an MT5 lever seal by pushing pistons back without cracking the bleed screw, so pad-swap guides need to stress releasing system pressure (or swapping to metal levers) before compressing calipers.【F:data/vesc_help_group/text_slices/input_part013.txt†L11659-L11678】
- Haku’s Xiaomi inflator couldn’t seat 21×3 tires even with a ratchet strap, reinforcing that serious tubed slick installs demand higher-flow compressors or shop assistance.【F:data/vesc_help_group/text_slices/input_part013.txt†L11936-L11940】

#### Integration & Wiring Notes
- Noname coached cihan to parallel external Ninebot packs before the controller (positive-to-positive, negative-to-negative) while keeping each BMS independent, then upsize the external leads so both packs share current evenly without back-charging each other.【F:data/vesc_help_group/text_slices/input_part013.txt†L11771-L11783】【F:data/vesc_help_group/text_slices/input_part013.txt†L11902-L11943】
- AG.racing’s two-wire brake sensor behaves like an on/off switch, and they’re still hunting for the VESC setting that cuts throttle without enabling regen—highlighting the need for a concise brake-sensor wiring and firmware guide for 75××× builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L11751-L11794】
- Oreo Huzky’s Apollo City Pro commuter now runs dual Spintend Alu Lite controllers on a 13 S 5 P pack for ~60 km/h, and he plans to stretch it to 16 S 8 P once he sources the compact Spintend Lite connector family—intel worth folding into the mid-voltage conversion guides.【F:data/vesc_help_group/text_slices/input_part013.txt†L11752-L11762】

#### Troubleshooting & Diagnostics
- Fry the Guy’s Shul front hub now feels brake-bound while the log flags a “voltage imbalance” fault, so dual-motor checklists should add magnet/phase short inspections after pothole strikes before blaming the controller.【F:data/vesc_help_group/text_slices/input_part013.txt†L11942-L11945】

### Batch 14 Highlights (lines 18500–19999)

#### Trail Access & Public Etiquette
- 🇺🇸 riders just saw “class 1 only” signs pop up on shared paths and even camera monitoring on bridge shortcuts, so they’re dialing back speed, plating heavier builds, or reverting VSETTs to stock profiles to avoid fines while still commuting on modded scooters.【F:data/vesc_help_group/text_slices/input_part013.txt†L18500-L18518】

#### ADC & Configuration Support
- Roby, ’lekrsu’, and Pandalgns confirmed you can repurpose ADC2 as a profile toggle: reuse the five-press brake script logic, wire a latching switch that feeds a distinct voltage into ADC2, and leave ADC1 for the throttle so single/dual-mode scooters can flip between limited and unlimited output without digging through the app.【F:data/vesc_help_group/text_slices/input_part013.txt†L18522-L18537】
- Newcomers like Gerald are pairing MKSESC 75100 controllers with sub‑1 kW commuter hubs and leaning on the group for step-by-step setup help, reinforcing the need for a starter-friendly configuration guide in addition to the YouTube walk-throughs members keep recommending.【F:data/vesc_help_group/text_slices/input_part013.txt†L18541-L18555】

#### Controller Reliability, Voltage & Firmware Limits
- Matthew wants to swap MOSFETs in his Spintend 100/100 to chase 150 A phase on 16 S while keeping battery current near 90 A; Paolo reminded him that switching losses elsewhere still cap gains, even though 90/150 appears safe in practice, and the same crew later re-affirmed those numbers once logs showed temps staying below 62 °C at 130 A phase.【F:data/vesc_help_group/text_slices/input_part013.txt†L18556-L18558】【F:data/vesc_help_group/text_slices/input_part013.txt†L19906-L19909】
- Matthew also summarized the community consensus that Flipsky’s QC remains a gamble—bad units have torched multiple motors—whereas Spintend keeps shipping reliable hardware that comfortably supports ~37 kW dual-motor builds on 20 S packs.【F:data/vesc_help_group/text_slices/input_part013.txt†L18566-L18567】
- Rogerio’s 22 S MakerBase experiment has already claimed controllers, prompting Paolo and ’lekrsu’ to label 22 S operation “suicide” unless you derate current, skip MTPA/field-weakening, or upgrade MOSFETs; they also warned that Spintend 85150s will pop on 20 S with MTPA enabled thanks to voltage spikes.【F:data/vesc_help_group/text_slices/input_part013.txt†L19300-L19319】

#### Thermal Management & Packaging
- Face de Pin Sucé measured G300 heat soak jumping from 45 °C to 60 °C in under six seconds, and Dualtron Achilleus admitted his controller is bolted sideways against plastic rather than the deck, so Paolo and skrtt urged relocating it under the deck with a proper aluminum heat path (or going dual-motor) because fans and MOSFET swaps won’t rescue a badly mounted single 90 H setup.【F:data/vesc_help_group/text_slices/input_part013.txt†L18551-L18619】
- Matthew’s epoxy-bonded 85150s proved that removing mis-mounted controllers means gutting the case and mechanically breaking the epoxy or grinding inner rails before you can refit larger 85× boards—valuable context for anyone inheriting glue-heavy builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L18840-L18844】
- 🇪🇸AYO#74 and Arnau logged that dual 70 H 33×2 hubs on 22 S 11 P packs still force controllers to current-limit after three hard launches when set around 90/100 A, underscoring how quickly race gearing overwhelms cooling even with larger stators.【F:data/vesc_help_group/text_slices/input_part013.txt†L19870-L19882】
- Arnau also cooked a 50 H hub at 60 V/110 A phase while riding without temperature telemetry, a reminder to wire sensors before running single-motor track sessions at sustained top speed.【F:data/vesc_help_group/text_slices/input_part013.txt†L19812-L19818】

#### Supply Chain & Component Intel
- JPPL uncovered that Tronic and Seven controllers now ship straight from a Chinese drone manufacturer: the support team offered immediate stock of X12 Pro 120 V units (~$1.1 k) and quick-turn Seven-18 builds, revealing that both “American” brands were outsourcing production all along.【F:data/vesc_help_group/text_slices/input_part013.txt†L18911-L18941】
- Nobrrr and Paolo cross-referenced MOSFET part numbers to show that 3Shul’s “custom” devices are just ON Semi HSBL009N10T parts (marked N009N10T), giving builders an upgrade path for other controllers that share the same packages.【F:data/vesc_help_group/text_slices/input_part013.txt†L19582-L19588】
- Patrick is organizing a €65 group buy for extended Dualtron rear cartridges/brackets, simplifying how racers mount longer shocks or wider wheels without bespoke machining.【F:data/vesc_help_group/text_slices/input_part013.txt†L19812-L19814】

#### Security, Telemetry & Aux Power
- After a theft in Portugal, the crew compared trackers: Invoxia GPS units remain the €100 gold standard because Bluetooth tags lose coverage away from crowds, while Jason’s DIY LTE tracker stores data in his own Grafana instance, runs on the scooter pack, and falls back to a roaming SIM-powered backup battery when unplugged.【F:data/vesc_help_group/text_slices/input_part013.txt†L19008-L19043】
- Rogerio warned that Spinny/ADC boards powered from external 12 V rails will fry unless you energize the aux supply before waking the controller, so documentation should spell out the correct sequencing for non-Spintend builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L19352-L19355】

#### Touring & Range Benchmarks
- Noname pushed his 300 lb emoped 276–277 mi in a day at 35–50 mph, needing roughly 2 h 45 m of charging plus meal/visit breaks and noting that 100–130 mi legs are the realistic comfort limit without hotel stops—rich energy data for anyone planning long-distance scooter tours.【F:data/vesc_help_group/text_slices/input_part013.txt†L19431-L19505】
- Jason’s 160 km standing ride demanded four to five fast-charge stops because his small-pack build overheats above 25 A of charging, highlighting the trade-offs between lightweight frames and touring ambitions.【F:data/vesc_help_group/text_slices/input_part013.txt†L19466-L19478】

#### Failure Reports & Diagnostics
- Matthew’s Yume Y11 motor failed after a 16 S pull at 180 A battery/phase even though his single 85250 survived; he contrasted that with Lonnyo hubs that shrug off 300 A, reinforcing how smaller OEM cans become the weak link once torque targets climb.【F:data/vesc_help_group/text_slices/input_part013.txt†L19439-L19455】
- Shlomozero’s 85150 cut-out investigation ended with a dead STM32 (no lights, ST-Link unable to connect), and his follow-up 6‑FET Ubox attempt vaporized components at 280 A phase, 550 A absolute, and 60 A of field-weakening—clear guardrails for anyone tempted to overdrive compact controllers.【F:data/vesc_help_group/text_slices/input_part013.txt†L19560-L19599】
- William’s fresh MP2 build sparked, shorted two phases, and left its main MCU “big square chip” scorching hot, so he’s hunting for layout or assembly faults before powering it again.【F:data/vesc_help_group/text_slices/input_part013.txt†L19788-L19789】
- When Shlomozero lost that Ubox he raided a spare Vsett controller to keep his NIU emoped rolling, underscoring the value of drop-in backups for daily commuters.【F:data/vesc_help_group/text_slices/input_part013.txt†L19577-L19580】

#### Handling, Frames & Build Planning
- IMWurden’s budget steering damper introduced a dangerous dead zone, and veterans advised either ditching cheap dampers for wide bars or investing ~$400 in motorcycle-grade units; the same chat praised Nami and LongThunder frames as the stiffest high-power platforms and acknowledged that most generic dampers share the same slop.【F:data/vesc_help_group/text_slices/input_part013.txt†L19904-L19925】
- 🇪🇸AYO#74’s crew keeps logging 147 km/h GPS runs on 22 S 11 P Nami builds, but Paolo calculated they’d need ~65 kW continuous to achieve the claimed 0–100 km/h in 2.5 s, reminding everyone that traction, legality, and efficiency quickly become limiting factors even when the motor survives.【F:data/vesc_help_group/text_slices/input_part013.txt†L19870-L19903】
- Massimo’s 20 S 4 P commuter (LG M50LT, MKSESC 75100 limited to 50 A battery/90 A motor) tops out at 57 km/h because the stock 500 W Monorim motor saturates; he’s already ordering a Lonnyo 60 H hub and planning a custom fork to unlock the performance his controller and battery can deliver.【F:data/vesc_help_group/text_slices/input_part013.txt†L19774-L19799】
- LiquorHole’s 21 kW Yisuntrek R8 build plan calls for 6 AWG cabling with QS8 V2 connectors (10–15 s bursts), Spintend 85250 controllers mounted in the stem with active cooling, and Lonnyo 70 H 33×2 motors (~43–50 kV) because the frame’s 150 mm dropouts can’t accept 75 H axles—actionable packaging intel for similar high-speed projects chasing 78–79 mph GPS speeds.【F:data/vesc_help_group/text_slices/input_part013.txt†L19926-L19940】

### Batch 15 Highlights (lines 20000–21499)

#### Motor Thermal & Gearing Decisions
- Noname’s 10″ Lonnyo 70 H torque hub hits ~70 °C when fed 220 A on his emoped, and swapping to a 12″ 50 H speed winding trims heat but sacrifices torque unless the 230 mm dropouts are widened—reinforcing the need for dedicated cooling (ferrofluid, liquid systems) before chasing 17 kW on compact motors.【F:data/vesc_help_group/text_slices/input_part013.txt†L20011-L20052】
- Dualtron Achilleus compared 90 H stator options: his 40×2, 25 kV hub weighs ~10.5 kg, tolerates 340–400 A phase on 21 S, and still needs heavy field weakening to break 110 km/h, while 90 H 33×2 speed cans stay nearer 30 kV but deliver less launch torque—useful gearing trade-offs for 22×3 builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L20563-L20599】

#### Controller & MOSFET Options
- LiquorHole confirmed Spintend 85250 V2 MOSFETs survive 135 A battery / 300 A phase bursts without swaps—Dxniel has logged 170/300 on stock silicon—and Nobrrr’s Tokmas-equipped units run 120 A battery / 160 A phase cleanly, framing safe current envelopes for buyers debating upgrades.【F:data/vesc_help_group/text_slices/input_part013.txt†L20408-L20416】【F:data/vesc_help_group/text_slices/input_part013.txt†L20257-L20259】
- Paolo is moving Tronic X12 bare boards for ~€350 shipped and reminded the group that Seven-branded controllers still ride on FR-4 PCBs with mediocre cooling, so prospective 22 S racers must budget for enclosure mods or alternate hardware.【F:data/vesc_help_group/text_slices/input_part013.txt†L20261-L20275】【F:data/vesc_help_group/text_slices/input_part013.txt†L20348-L20355】
- Yamal suggested pairing Ubox controllers with upgraded TolT MOSFETs for motorcycle-class packs now that the two U.S. boutique vendors have collapsed, highlighting the shrinking pool of high-power, supportable VESC platforms.【F:data/vesc_help_group/text_slices/input_part013.txt†L21285-L21295】

#### Suspension, Frames & Safety
- Dxniel broke down Kaabo storm-style suspension: the GTR gets a 135 mm shock while cheaper variants rely on twin 40 mm springs sandwiched by bushings and M5 bolts, which matches Noname’s “pogo” complaints about tall spacer stacks on block-sprung forks.【F:data/vesc_help_group/text_slices/input_part013.txt†L20408-L20416】
- Jason measured the Ninebot G30 rear fork at roughly 125 mm between flats, so wider hubs still demand spacer work or dropout machining when planning 20×3 conversions.【F:data/vesc_help_group/text_slices/input_part013.txt†L20141-L20143】
- ’lekrsu’ advised laser-cutting new G2 plates with integrated brake mounts and swapping in G3 springs/bushings to silence rear-end clunks, while torque-arm-grade 5 mm plates remain mandatory for 80 H upgrades.【F:data/vesc_help_group/text_slices/input_part013.txt†L20720-L20737】【F:data/vesc_help_group/text_slices/input_part013.txt†L20725-L20732】
- LiquorHole’s crash post-mortem showed that adding a second stem bolt to the 220 lb Yisuntrek R8 kept the deck upright when the frame folded; he now budgets $1.3 k and ~10 days to source a replacement chassis from Geofought, reminding builders to overbuild stem hardware on heavyweight frames.【F:data/vesc_help_group/text_slices/input_part013.txt†L21431-L21483】

#### Battery & Build Planning
- Paolo listed a 20 S 6 P Molicel P45B pack with full-copper busbars, a 425 A ANT BMS, dual QS8s, and 7 AWG leads for €650—setting a benchmark for turnkey high-current batteries versus DIY costs.【F:data/vesc_help_group/text_slices/input_part013.txt†L20266-L20267】
- Noname coached a new G30 owner to cut deck rails, expect custom jigs for 6 P layouts, and budget soldering gear if they outgrow the stock pack, underscoring the tooling overhead behind Ninebot battery swaps.【F:data/vesc_help_group/text_slices/input_part013.txt†L21223-L21241】
- Haku’s copper-welding experiments confirmed hobby welders handle pure copper busbars up to 0.15 mm reliably but struggle at 0.2 mm, a practical ceiling for builders chasing low-resistance straps without industrial gear.【F:data/vesc_help_group/text_slices/input_part013.txt†L20950-L20955】
- Yamal is drafting a “legal chassis” long-range scooter concept with 60–70 Ah packs, ruggedized enclosures, and fast-charge capability to support mixed dirt/pavement touring, signaling demand for endurance-focused VESC guides alongside track builds.【F:data/vesc_help_group/text_slices/input_part013.txt†L21308-L21309】
- LiquorHole’s Yisuntrek R8 ships with a 100 Ah CATL prismatic pack (rated ~25 kW), 26×14 in deck, and 220 lb curb weight; after the crash he confirmed most electronics survived, making the frame the primary consumable in high-power commuter spills.【F:data/vesc_help_group/text_slices/input_part013.txt†L21431-L21488】

#### Configuration & Troubleshooting
- Oreo Huzky got the definitive answer for wiring 10 kΩ NTC probes—use the VESC TEMP and GND pins—which should land in the sensor quick-start docs.【F:data/vesc_help_group/text_slices/input_part013.txt†L20153-L20155】
- Dualtron Achilleus has to double his commanded phase current on both G300 and Spintend 85 250 controllers, pointing to shunt calibration or duty-cycle caps worth documenting for riders who see similar halved outputs on VESC Tool 6.05.【F:data/vesc_help_group/text_slices/input_part013.txt†L20563-L20599】【F:data/vesc_help_group/text_slices/input_part013.txt†L20891-L20935】
- Yamal detailed his profile strategy: a 23 km/h compliance mode for police stops, a 14 kW “Seven Routes” touring preset, and a “Hot Summer” throttle clamp to keep 20 S Ubox controllers cool during 40 °C commutes—templates other high-power commuters can clone.【F:data/vesc_help_group/text_slices/input_part013.txt†L20691-L20705】
- Noname’s FarDriver app repeatedly crashed and overheated his phone until he created a burner login, while Yamal chased front-hub grinding by reflowing bullet connectors—fresh reminders to document vendor app quirks and to inspect phase joints whenever a motor squeals.【F:data/vesc_help_group/text_slices/input_part013.txt†L20894-L20999】【F:data/vesc_help_group/text_slices/input_part013.txt†L21285-L21291】

### Batch 16 Highlights (lines 21500–22235)

#### Displays & Telemetry
- Rage Mechanics’ display will talk to any VESC, but buyers currently need to purchase the €489 controller bundle; the screen brings Bluetooth/GPS telemetry and even humidity sensing, and the team plans to sell it standalone once production stabilises.【F:data/vesc_help_group/text_slices/input_part013.txt†L21517-L21573】【F:data/vesc_help_group/text_slices/input_part013.txt†L21820-L21824】
- Jason is prototyping a DIY alternative by flashing community firmware onto inexpensive CYD hardware (SimpleVescDisplay), noting that the commodity screen is cheap while the custom code is the heavy lift.【F:data/vesc_help_group/text_slices/input_part013.txt†L21539-L21557】

#### Stems, Brakes & Chassis
- The sought-after Anatoly/Rage stem is a solid 1.7 kg aluminium bar rather than a tube; Rage shaved the weight to ~0.8 kg with a titanium version for their race scooters.【F:data/vesc_help_group/text_slices/input_part013.txt†L21621-L21637】
- Rage still prefers Hope calipers up front because Beringer’s wider bodies are harder to tuck near rims and the €999/pair premium doesn’t justify the modest rear-brake gains.【F:data/vesc_help_group/text_slices/input_part013.txt†L21636-L21644】
- They also stopped using customer-supplied Sonken swingarms after play developed, replacing them with in-house arms on the RM-series prototype so geometry stays tight.【F:data/vesc_help_group/text_slices/input_part013.txt†L21820-L21833】

#### Tires, Handling & Compliance
- Yamal sourced 90 mm Sava slicks from a local motorcycle shop; riders report they’re beefier than Ulip tyres but still trail PMT T41/Juniors for outright grip, and they’re hard to find on AliExpress.【F:data/vesc_help_group/text_slices/input_part013.txt†L21653-L21676】
- Raising the rear ride height without a damper sparked wobble on Dualtrons, whereas correctly balanced geometry can hit 150 km/h damper-free—still rare in Spain where stricter policing is pushing big scooters off the streets.【F:data/vesc_help_group/text_slices/input_part013.txt†L21704-L21715】【F:data/vesc_help_group/text_slices/input_part013.txt†L21708-L21710】

#### Frame & Battery Packaging
- Rage confirmed their long Dualtron Victor chassis fits 21 S 7 P packs (and likely 22 S) alongside Thunder arms, letting riders build a fully certified DGT-legal scooter with 50PL cells, Ubox controllers, and 90–100 H speed hubs without buying a Thunder 3 outright.【F:data/vesc_help_group/text_slices/input_part013.txt†L21838-L21856】【F:data/vesc_help_group/text_slices/input_part013.txt†L21848-L21855】
- Stock Nami Burn-E packs remain 20 S 10 P bricks that fill the plastic enclosure tightly with straight rows rather than zigzags, so retrofits must respect the limited slack around the case.【F:data/vesc_help_group/text_slices/input_part013.txt†L21798-L21806】

#### Battery, Charging & BMS Choices
- Builders debating long-range upgrades weighed 50PL tabless cells against cheaper 50E/50S options, speculated about 20 S 20 P prismatic packs, and noted that WePoor decks max out near 20 S 12 P unless the top rail is milled down.【F:data/vesc_help_group/text_slices/input_part013.txt†L21861-L21876】
- LiquorHole’s 100 Ah prismatic pack pairs well with ANT hardware: the BMS tolerates 20 A fast-charging through XT60 leads (25 A max), trimming a full cycle to ~5 h, and they’re now upsizing from a 325 A to 425 A unit to survive 270 A, 20 S bursts with thicker charge wiring.【F:data/vesc_help_group/text_slices/input_part013.txt†L22075-L22116】

#### Motor Thermal Management & Control
- 🇪🇸AYO#74 plans to swap their overheated rear 70 H for a 100 H 33×2 hub while keeping a 70 H front; Paolo warned that matching wheel speeds will demand more field-weakening, amplifying heat, so traction-control ERPM gaps, rider weight bias, and reliable temp sensors (theirs is broken) must be dialled in to keep the rear under ~110 °C despite 180 mm axles and 70 kg curb weight.【F:data/vesc_help_group/text_slices/input_part013.txt†L22139-L22178】【F:data/vesc_help_group/text_slices/input_part013.txt†L22153-L22161】

#### Failures & Diagnostics
- Rogerio logged yet another Spintend failure—his friend’s unit blew at roughly 250 A—which reinforces the need for conservative guardrails even on refreshed 85××× hardware.【F:data/vesc_help_group/text_slices/input_part013.txt†L22229-L22235】
