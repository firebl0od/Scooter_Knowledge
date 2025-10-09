# input_part001.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part001.txt`
- Coverage: 2021-12-21 02:06:39 through 2022-02-03 23:10:52 (lines 1-8400)
- Next starting point: Continue at 2022-02-03 23:12 onward (line ~8401)

## Key Findings

### MakerX Mini FOC Voltage Headroom & Alternatives
- MakerX Mini FOC owners debating whether a fully charged 13S li-ion (≈54.6 V) is safe were reminded that the controller is specified for 12S; veterans warn the extra series cell leaves little room for regenerative spikes and recommend switching to Spintend or other hardware rated ≥16S when regularly running above 50 V.【F:data/vesc_help_group/text_slices/input_part001.txt†L4-L15】【F:data/vesc_help_group/text_slices/input_part001.txt†L65-L74】
- Spintend single VESC firmware with a 300 A hardware limit file was shared; users stressed it only removes the software ceiling and still requires sensible settings plus adequate cooling, with examples of 80 A battery / 130 A phase targets for single-motor builds.【F:data/vesc_help_group/text_slices/input_part001.txt†L55-L66】【F:data/vesc_help_group/text_slices/input_part001.txt†L125-L138】

### Hall Sensor Diagnostics & Throttle Supply Choices
- Francois measured SS49E hall outputs at both 3.3 V and 5 V rails, noting the VESC app logs show raw ADC counts rather than millivolts—builders should focus on the delta between high/low states instead of the absolute ~200-count value seen during tests.【F:data/vesc_help_group/text_slices/input_part001.txt†L32-L53】
- Riders highlighted that powering halls from a noisy 3.3 V converter can flatten readings; if anomalies persist, repeat measurements with a stable 5 V source to rule out regulator ripple before condemning the sensor.【F:data/vesc_help_group/text_slices/input_part001.txt†L53-L54】

### Battery Pack Experiments & Cooling Practices
- CNHL and GNB high-discharge LiPo packs (140 C–180 C burst ratings) are being used for spot-welding copper/nickel busbars and as booster packs for scooters, though the group jokes they empty after a single launch—expect to parallel multiple packs for sustained runs.【F:data/vesc_help_group/text_slices/input_part001.txt†L175-L227】
- A customer build documented dual motors on a 16S7P Samsung 50E pack (~140 A battery limit). The tuner keeps phase current near 70 A per controller to avoid overheating while leveraging external airflow solutions mounted at the scooter front.【F:data/vesc_help_group/text_slices/input_part001.txt†L240-L256】【F:data/vesc_help_group/text_slices/input_part001.txt†L247-L255】
- Wolf Warrior owners pushing 120 A battery / 440 A phase on dual Ubox controllers reported MOSFET heat rise when the deck is sealed; logging temperature data helps decide whether to add ducted cooling or throttle back during sustained high-speed runs.【F:data/vesc_help_group/text_slices/input_part001.txt†L303-L316】

### Frame Integrity & High-Speed Builds
- Weped GTS scooters ship with 16S6P 50E packs and require thorough pre-delivery rework (front fork alignment, longer hardware) to stay safe at triple-digit speeds; experienced builders retrofit up to 21S11P Molicel packs plus Nucular 24F controllers once the chassis issues are corrected.【F:data/vesc_help_group/text_slices/input_part001.txt†L271-L456】
- VSETT 10+ frames are praised for stem strength, with only two historical rear shock mount failures solved by a manufacturer revision; relocating controllers to the neck opens deck space for 20S9P 21700 batteries.【F:data/vesc_help_group/text_slices/input_part001.txt†L459-L478】
- Xiaomi and Ninebot frames can survive aggressive riding—including 120 km/h runs and off-road abuse—provided owners proactively service stem locks, bearings, and mudguards; many failures stem from user neglect rather than inherent design flaws.【F:data/vesc_help_group/text_slices/input_part001.txt†L367-L599】

### Power Switching Strategies for Flipsky 75100
- Riders rely on XT90S loop keys or pricey external anti-spark switches to safely power the 75100, highlighting the lack of an integrated low-voltage enable input; some resort to trace cuts and custom toggles to break the internal regulator rail.【F:data/vesc_help_group/text_slices/input_part001.txt†L629-L654】
- XT90S plugs prevent connector pitting on modest packs, but high-voltage 20S systems with large input capacitance still arc without a dedicated pre-charge stage; QS8 connectors or bespoke pre-charge adapters are suggested for longevity.【F:data/vesc_help_group/text_slices/input_part001.txt†L660-L681】
- Group consensus is to favor controllers with onboard power switches or dual-channel units like Spintend’s ubox when wiring two 75100s, both to simplify harnessing and to avoid ground-loop headaches.【F:data/vesc_help_group/text_slices/input_part001.txt†L855-L864】

### Field Weakening Firmware Paths & Limitations
- Field weakening is only exposed on firmware 5.2/5.3 builds, forcing 75100 owners to sideload beta binaries via SWD rather than rely on FlipSky’s locked loader; without it, 16S riders plateau near 57 km/h despite ample phase current headroom.【F:data/vesc_help_group/text_slices/input_part001.txt†L627-L751】【F:data/vesc_help_group/text_slices/input_part001.txt†L697-L748】
- Members confirm BLDC mode is disabled altogether on the 75100 firmware branch, triggering VESC Tool crashes—suggesting deeper configuration changes than simple shunt calibration and complicating any attempt to flash 75300 images wholesale.【F:data/vesc_help_group/text_slices/input_part001.txt†L869-L918】

### Hardware Quality & Cooling Workarounds
- Tear-down photos show undersized housings, unsecured bus capacitors, and single shunt sensing on the 75100; owners reinforce caps with silicone, clean stray solder balls, and consider shunt upgrades before pushing beyond 120 A.【F:data/vesc_help_group/text_slices/input_part001.txt†L752-L830】
- Sustained 120 A phase pulls overheat the compact case unless the MOSFET side is clamped directly to the frame with fresh thermal paste; Kapton tape insulates too well, prompting suggestions to substitute mica or mill spacers for tighter thermal coupling.【F:data/vesc_help_group/text_slices/input_part001.txt†L1086-L1099】

### Motor Options & Performance Notes
- Detailed VSETT 9 motor specs (92 mm stator, 15 pole pairs, 0.5 mm air gap) were shared alongside sourcing tips—EU buyers secured units for ~€120 and praised their 10-inch tire comfort due to taller carcass profiles.【F:data/vesc_help_group/text_slices/input_part001.txt†L921-L940】
- Builders debated HM vs LY hub motors: HM-branded units demand ≥50 A for acceptable torque yet run hotter than LY alternatives with similar fork spacing, reinforcing the preference for lower-KV LY motors in high-power conversions.【F:data/vesc_help_group/text_slices/input_part001.txt†L1010-L1031】
- Wolf Warrior hubs were confirmed to come from the same supplier as Rion/Weped units, with 1200 W editions carrying 60 mm magnets while the GT’s 2000 W set moves to 65 mm and 33/43 Kv windings—explaining why Minimotors controllers struggle unless shunted past 50 A or replaced with higher-phase-current VESCs.【F:data/vesc_help_group/text_slices/input_part001.txt†L2543-L2663】

### Fiido & Compact eBike Battery Experiments
- Paolo’s Fiido build targets 16S packs but laments the tiny stock motor leads; other riders suggested 3D-printed spacers to squeeze 21700 cells or external battery bags when printers can’t handle full enclosures.【F:data/vesc_help_group/text_slices/input_part001.txt†L1119-L1148】
- Copper strip reinforcement at 0.2 mm thickness demands high-power soldering gear yet dramatically stiffens the pack busbars, making small “sleeper” e-bikes viable for high-current launches.【F:data/vesc_help_group/text_slices/input_part001.txt†L1154-L1158】

### Frame & Handling Debates at Triple-Digit Speeds
- Riders split on the Rion RX2000: Paolo praises its dual-suspension compatibility and stability without a damper at ~100 km/h, while Face de Pin Sucé considers it twitchy compared with Weped setups and derides oversized Weped columns despite their cornering grip with PMT tires.【F:data/vesc_help_group/text_slices/input_part001.txt†L1163-L1180】
- High-speed crash anecdotes reinforced the need for reinforced handlebars, titanium stems, and wide slicks on tuned Zero 10X frames to ward off wobble when pushing beyond 110 km/h.【F:data/vesc_help_group/text_slices/input_part001.txt†L1957-L1979】

### Parallel Packs & Cell Sourcing Strategies
- Happy Giraffe is paralleling matched 13S6P Samsung 35E packs (identical BMS, similar cycle count) to feed a Xiaomi scooter, reminding others to verify internal resistance before running dual batteries.【F:data/vesc_help_group/text_slices/input_part001.txt†L1582-L1596】
- Builders compared Sony VTC6A, Molicel P42A, and Samsung 30T cells: Sony’s lower voltage sag and heat won praise, but its price is roughly double P42A unless buying ~10 k cells monthly; 30T remains the punchiest albeit with limited capacity.【F:data/vesc_help_group/text_slices/input_part001.txt†L1603-L1655】
- Plus Messenger’s built-in translator became the go-to tool for following Spanish and French tech chats without copy-paste gymnastics.【F:data/vesc_help_group/text_slices/input_part001.txt†L1665-L1689】

### 75100 Sensorless Behavior & Field-Weakening Risks
- A new 75100 owner can’t eliminate a single “tah” when the controller transitions from sensored to sensorless at 2000 ERPM; experimentation across 60 V and 24S setups shows the stutter persists, suggesting PID tuning or logging is needed beyond simple ERPM tweaks.【F:data/vesc_help_group/text_slices/input_part001.txt†L1696-L1889】
- Veterans warned that running 24S on a stock 75100 is survivable only without e-braking or field weakening, since regen-induced back-EMF spikes can exceed component limits and have already destroyed other controllers when BMS protection tripped at high speed.【F:data/vesc_help_group/text_slices/input_part001.txt†L1699-L1720】【F:data/vesc_help_group/text_slices/input_part001.txt†L1904-L1909】

### Firmware Limits & Mod Paths for the 75100
- Multiple logs show the 75100 plateauing around 110 A phase even when higher values are saved; community consensus is that FlipSky hard-coded a 120 A ceiling, and only firmware rebuilds (linked Endless Sphere and esk8 threads) or shunt/MOSFET swaps paired with custom binaries might raise it—albeit with serious hardware risk.【F:data/vesc_help_group/text_slices/input_part001.txt†L1803-L1857】【F:data/vesc_help_group/text_slices/input_part001.txt†L2093-L2140】【F:data/vesc_help_group/text_slices/input_part001.txt†L2370-L2417】
- Paolo argues the stock 0.5 mΩ shunt cannot accurately sense above 120 A regardless of cooling; any attempt to push toward 200 A would require hardware changes and firmware recompilation via the leaked sources.【F:data/vesc_help_group/text_slices/input_part001.txt†L2399-L2412】

### Flipsky QC Failures & Inspection Practices
- Spintend replacement units have arrived missing faceplate screws, forcing customers to machine their own hardware; others found solder splatter inside, underscoring the need for full tear-downs before first power-up despite warranty risks.【F:data/vesc_help_group/text_slices/input_part001.txt†L2023-L2037】
- Paolo’s dual 200 A FSESCs ignited during auto-detection, with post-mortems pointing at loose solder balls shorting logic boards—prompting veterans to insist on cleaning FlipSky controllers and logging temps before riding.【F:data/vesc_help_group/text_slices/input_part001.txt†L1984-L2059】【F:data/vesc_help_group/text_slices/input_part001.txt†L2146-L2176】
- Warranty support remains inconsistent: Paolo resorted to PayPal claims while others endured month-long waits and double VAT charges, strengthening the case for proactive inspection over relying on manufacturer assistance.【F:data/vesc_help_group/text_slices/input_part001.txt†L2182-L2231】

### Zero 10X Limited & External Battery Layouts
- The Zero 10X Limited ships with a Sabvoton controller pair crammed in the deck and a secondary battery strapped to the stem, drawing ridicule for its 40–50 A limits, poor cooling, and overheating pole pack despite dual-pack capacity claims.【F:data/vesc_help_group/text_slices/input_part001.txt†L2464-L2520】
- Riders exploring VESC 75/200 swaps hope to reclaim deck space for batteries, but acknowledge the Limited’s layout requires major rewiring and airflow improvements to handle high-current 20S packs.【F:data/vesc_help_group/text_slices/input_part001.txt†L2489-L2519】

### Kelly 7212/7218 vs Ubox Power Delivery
- Kelly 7212 owners love the launch feel yet Face de Pin Sucé reports pulling 220 A battery on 20S while noting its 12 MOSFET stack and robust cooling outperform a 6-FET Ubox, whereas Paolo reminds that the 7212 is still only ~50 A continuous without airflow and benefits from shunt mods or stepping up to the 7218.【F:data/vesc_help_group/text_slices/input_part001.txt†L2735-L2806】

### Brake Hardware, Rotor Thickness & Data Logging
- Riders questioned caliper placement and rotor hardware at 100 km/h, concluding that thin 1.8 mm bicycle discs deform under heat and recommending 3 mm+ rotors, frequent pad swaps, and even moped-grade hardware for heavy scooters to avoid catastrophic failures.【F:data/vesc_help_group/text_slices/input_part001.txt†L2891-L2943】
- Magura MDR-P rotors paired with MT7 calipers logged 2 g stops (Dragy verified) on a 21S11P Thunder, leading moderators to demand GPS-backed braking data before claiming Shimano Storm HC superiority.【F:data/vesc_help_group/text_slices/input_part001.txt†L2976-L3010】

### Field Weakening Rollout & Firmware 5.3 Hurdles
- VESC Tool 3.01 surfaced on desktop and Android, but users confirmed field weakening controls only appear on firmware 5.03; FlipSky 75100 testers hit motor-detect failures after flashing beta binaries, while Spintend responded that their official 5.3 builds need more soak time and advised staying on 5.2 meanwhile.【F:data/vesc_help_group/text_slices/input_part001.txt†L2706-L2975】【F:data/vesc_help_group/text_slices/input_part001.txt†L4000-L4005】
- Community members recompiled unlocked 5.3 firmware for Spintend singles/duals, warning that hardware variants bias the MCU rails (3.3 V vs 3.44 V) and that flashing over USB has already induced ground-loop failures—prompting a shift toward WiFi/BT bridges and Android file-path workarounds for loading BINs.【F:data/vesc_help_group/text_slices/input_part001.txt†L3326-L3369】【F:data/vesc_help_group/text_slices/input_part001.txt†L4000-L4018】

### Fault Logging, Absolute Current & Sensorless Diagnostics
- When ABS overcurrent trips, veterans insist on running the `faults` command before power-cycling and raising the absolute current limit to give headroom above commanded phase current spikes (e.g., 200–250 A for 120–130 A phase setups) while monitoring logs for noise-induced observer errors.【F:data/vesc_help_group/text_slices/input_part001.txt†L2840-L2872】【F:data/vesc_help_group/text_slices/input_part001.txt†L3796-L3808】
- Sensorless surging on the Ubox was traced to loose phase connectors or harness damage; sharing CSV traces and physically tug-testing plugs were recommended first steps before blaming firmware.【F:data/vesc_help_group/text_slices/input_part001.txt†L3757-L3810】

### Wiring Practices & Signal Conditioning
- Builders mocked dual-phase spaghetti harnesses on high-power hubs and urged recabling to single 8–10 AWG leads with connectors near the motor to cut resistive joints, noting that solder-only splits and multiple XT150s add needless loss.【F:data/vesc_help_group/text_slices/input_part001.txt†L3260-L3305】
- Throttle chatter at high phase currents pushed riders toward shielded signal looms and dedicated 5 V→3.3 V adapter boards (e.g., Spintend’s filter) because raw 5 V hall throttles inject noise that VESC ADCs cannot tolerate long-term.【F:data/vesc_help_group/text_slices/input_part001.txt†L3494-L3605】

### High-KV Motor Demands & Controller Selection
- Paolo’s 43 Kv Rion-sourced hubs have already cooked a VESC 75/200, leading him to favour Kelly or Sabvoton hardware capable of ≥250 A phase to move the rotor at low ERPM and highlighting the danger of running sensorless high-KV loads on compact FOC units.【F:data/vesc_help_group/text_slices/input_part001.txt†L3820-L3856】

### Data Analysis & Logging Tools
- Group members now export ride CSVs via VESC Tool, sift peaks in Excel/Discord, and rely on Android desktop-mode builds; until file access improves, the recommended path is logging on mobile, copying from `Android/data/vedder.vesctool/files`, or bridging the phone to desktop VESC Tool over TCP for firmware updates.【F:data/vesc_help_group/text_slices/input_part001.txt†L3440-L3994】【F:data/vesc_help_group/text_slices/input_part001.txt†L4000-L4018】

### Mobile Firmware Workarounds & Android 11 File Access
- Happy Giraffe documented that Android 11+ blocks the `Android/data` path for VESC Tool, recommending the wireless TCP bridge from phone to desktop as a workaround and confirming that sideloaded BINs and logs remain reachable via `Android/data/vedder.vesctool/files`; XFolder was suggested for file managers that can reach the sandbox without root.【F:data/vesc_help_group/text_slices/input_part001.txt†L4001-L4018】
- Spintend support advised staying on 5.2 firmware until their customized 5.3 builds are validated, highlighting that beta binaries continue to shift hardware behavior between releases.【F:data/vesc_help_group/text_slices/input_part001.txt†L4003-L4052】

### Field Weakening Testing & Duty Cycle Limits
- Happy Giraffe’s single Ubox trials incremented field-weakening current from 10 A to 40 A, logging ~3 km/h gains but showing battery peaks remained near 45 A when base current was capped at 40 A; Face de Pin Sucé argued the feature only helps once motors already reach their load-limited duty cycle, otherwise more phase/battery current delivers better speed per watt.【F:data/vesc_help_group/text_slices/input_part001.txt†L4053-L4123】
- Gigolo Joe’s 5.3 firmware test plateaued around 70 km/h despite 90 A phase commands, with the group reiterating that field weakening multiplies power demand and that voltage increases or motor rewinds yield more sustainable top-speed gains.【F:data/vesc_help_group/text_slices/input_part001.txt†L4124-L4148】
- Riders warned that raising duty cycle limits toward 99–100 % can trigger abrupt cut-outs above 70 km/h, urging others to keep firmware defaults (~95 %) to avoid overmodulating MOSFETs at speed.【F:data/vesc_help_group/text_slices/input_part001.txt†L4944-L4953】

### High-KV Hub Loads & Phase Wiring Upgrades
- Discussions around 25 S, high-Kv hubs stressed that these motors demand ≥250 A phase to slip tires and that 4 mm² factory leads overheat quickly; Face de Pin Sucé and Paolo compared experiences on Thunder and Rion builds, concluding that rewinding expectations must pair with heavier controllers to be viable.【F:data/vesc_help_group/text_slices/input_part001.txt†L4311-L4344】
- Riders shared rewiring techniques for 65 mm magnet hubs, including replacing stock leads with 9–10 AWG silicone cable, burning insulation off windings before soldering, and masking stators to keep debris out during statorade fills.【F:data/vesc_help_group/text_slices/input_part001.txt†L4280-L4294】

### Ubox ADC Failures & STM32 Repair Reality
- Luis Magalhaes’s Ubox “B” side died after throttle noise issues, with diagnostics showing the 3.3 V rail shorted to ground; veterans advised checking resistance between 5 V/3.3 V and ground before attempting reflashes, noting that ADC transients easily kill unprotected STM32s.【F:data/vesc_help_group/text_slices/input_part001.txt†L4386-L4461】
- Koxx outlined required tools—flux, hot air, solder paste, magnification—and suggested replacing the MCU only if users are experienced, otherwise switching to CAN-isolated peripherals or alternate controllers to avoid repeat failures.【F:data/vesc_help_group/text_slices/input_part001.txt†L4462-L4499】

### Brake Mount Hardware & Caliper Alignment
- Sombre_enfant cautioned that M5 hardware on custom brake brackets quickly eggs out the frame under MT7 loads, recommending upsizing mounts to M6/M8 and machining snug aluminum adapters to remove play before hard stops.【F:data/vesc_help_group/text_slices/input_part001.txt†L4671-L4707】

### Spintend 5.3 Release & QC Alerts
- Spintend’s public 5.3 firmware drop drew mixed reactions—some praised smoother acoustics while others stuck to 5.2 until side-by-side validation is done; shared links captured both official downloads and mirrored binaries for field testers.【F:data/vesc_help_group/text_slices/input_part001.txt†L5042-L5059】
- Artem Bulashev’s teardown of a brand-new Ubox V2 revealed dozens of solder balls and flux residue inside the power stage, prompting renewed warnings to fully disassemble, inspect, and clean units—even when they ship “sealed.”【F:data/vesc_help_group/text_slices/input_part001.txt†L5060-L5075】

### Ubox Thermal Management & Connector Reliability
- Happy Giraffe logged 67 °C MOSFET temps and thermal throttling on a single Ubox at 50 A battery / 120 A phase, spurring debate over whether battery current or case contact drives heat; suggestions ranged from bolting controllers to bare metal skid plates to adding active airflow.【F:data/vesc_help_group/text_slices/input_part001.txt†L5101-L5108】【F:data/vesc_help_group/text_slices/input_part001.txt†L5337-L5399】
- Melted XT90 interconnects on dual-Ubox builds were traced to soldered bus bars without copper leads; members recommended upgrading to AS150U/QS8 connectors or hard terminals and routing low-current controls via shielded CAT6A pairs for throttle/start wiring.【F:data/vesc_help_group/text_slices/input_part001.txt†L5231-L5284】

### Thermal Interface Debates & Pad Replacement Options
- Owners compared Spintend’s stock thermal pads with aftermarket 8–16 W/m·K materials, but Paolo noted the MOSFET resin layer limits heat transfer regardless of paste choice; the consensus was to focus on improving mechanical clamping and contact area before chasing exotic pad specs.【F:data/vesc_help_group/text_slices/input_part001.txt†L5320-L5399】

### Ubox Case Prep & Thermal Contact
- Rosheee, Artem, and Happy Giraffe compared mounting methods after one rider hit 67 °C and throttled: sanding paint from the deck, polishing copper plates flat, and reseating thermal pads kept single Ubox cases near 55 °C at 50 A battery / 120 A phase, especially when the controller is bolted directly to a solid metal chassis.【F:data/vesc_help_group/text_slices/input_part001.txt†L5400-L5438】【F:data/vesc_help_group/text_slices/input_part001.txt†L5418-L5437】

### Vsett & Blade Motor Fitment, Pricing, and Logistics
- VSETT 10+ limited-edition hubs slide into Ninebot G30 forks with minimal spreading when spacers are trimmed, preserving stock fenders; riders measured 135 mm fork spacing and reported 80–83 km/h GPS speeds on 16S packs.【F:data/vesc_help_group/text_slices/input_part001.txt†L5520-L5631】
- EU buyers compared sourcing channels: local importers offered dual motors for ~CHF 400 including tires and warranty while AliExpress sellers quoted €150–€200 plus €50–€170 shipping per motor, motivating group buys or forwarders to dodge inflated freight quotes.【F:data/vesc_help_group/text_slices/input_part001.txt†L5695-L5718】【F:data/vesc_help_group/text_slices/input_part001.txt†L6190-L6198】

### Ubox V2 Connectivity, Diagnostics & Phase Lead Rework
- Multiple Ubox V2 orders arrived without the promised Bluetooth daughterboard; owners confirmed the controller expects an external UART BLE module (5 V, RX, TX, GND) and had to escalate with support when none were shipped.【F:data/vesc_help_group/text_slices/input_part001.txt†L5811-L5840】
- Builders troubleshooting noisy ADC readings swapped sensor boards only to see identical faults, prompting checks for damaged STM32 ADC pins and reminding that the add-on button/trigger PCBs run from 5 V not 3.3 V.【F:data/vesc_help_group/text_slices/input_part001.txt†L5856-L5868】
- Artem advised upgrading to 60–80 W irons and broad tips before attempting 10 AWG phase-lead swaps on Ubox hardware; TS80P pencils can desolder stock 12 AWG leads but struggle to tin heavier replacements cleanly.【F:data/vesc_help_group/text_slices/input_part001.txt†L5920-L5938】

### Hydraulic Brake Bleeding & Setup Resources
- Rosheee walked newcomers through shortening Magura hoses, highlighting olives, syringes with vent holes, and linked bleeding tutorials so XDE300 owners could swap calipers and rebleed quickly without specialist tools.【F:data/vesc_help_group/text_slices/input_part001.txt†L5947-L5988】

### GPS Logging Tools & Data Reliability
- Relive ride visualizations routinely over-reported top speed by ~7 km/h compared with VESC logs, especially when GPS lost lock briefly during city rides.【F:data/vesc_help_group/text_slices/input_part001.txt†L6003-L6013】
- Speed View GPS Pro, shared via APK, provides floating dashboards, detailed graphs, and reliable export data for range testing when paired with Ubox telemetry.【F:data/vesc_help_group/text_slices/input_part001.txt†L6414-L6436】

### Motor Selection Guidance for 16S Xiaomi Builds
- Artem cautioned that a 16S5P Samsung 35E pack safely supplies about 50 A; chasing 100 km/h on a single-motor Xiaomi Pro is unrealistic without higher-voltage packs, better brakes, and wider forks, though a VSETT 10+ hub can deliver ~70 km/h on 60 V single-motor setups.【F:data/vesc_help_group/text_slices/input_part001.txt†L6015-L6114】

### High-Power Motor Thermal Debates
- Spintend users compared thermal ceilings: some saw MOSFETs spike to 80 °C within minutes at 100 A phase open-loop, while others logged 4 kW bursts at 60 A battery without issues, underscoring how airflow, duty cycle, and sensor placement skew results.【F:data/vesc_help_group/text_slices/input_part001.txt†L6115-L6331】
- Riders expect VSETT 10+ hubs to stay under ~65 °C even at 50 A battery / 150 A phase when paired with adequate thermal pads or ferrofluid, whereas smaller 45 mm stators saturate sooner and demand conservative duty cycles.【F:data/vesc_help_group/text_slices/input_part001.txt†L6123-L6215】【F:data/vesc_help_group/text_slices/input_part001.txt†L6334-L6338】

### Ferrofluid Cooling Impact
- Adding 6 ml of Statorade to dual 1400 W VSETT motors cut peak temps from ~145 °F (63 °C) to ~104 °F (40 °C) on identical 16S rides, keeping windings under 38 °C ambient despite 37–35 A battery limits; veterans noted the heat shift toward magnets, so long climbs still require monitoring for saturation.【F:data/vesc_help_group/text_slices/input_part001.txt†L6340-L6362】【F:data/vesc_help_group/text_slices/input_part001.txt†L6800-L6821】

### VSETT 10+ Battery Packaging & BMS Options
- A 20S9P Samsung 48x build fits inside the 10+ deck with controllers relocated externally, leaving ~2 mm side clearance inside a 169 mm jig; builders pair it with JK active-balancing BMS boards and waterproof Higo/Julet harnesses for serviceable installs.【F:data/vesc_help_group/text_slices/input_part001.txt†L6371-L6486】【F:data/vesc_help_group/text_slices/input_part001.txt†L6501-L6502】

### Controller-Based Charging & Fast-Charge Concepts
- Nucular owners highlighted the controller’s ability to accept any PSU below pack voltage and charge through the phase leads—e.g., a 3 kW Flatpack2 delivering ~13 A into 20S packs—suggesting future VESC firmware could replicate CC/CV charging with programmable cutoffs around 95 % SOC.【F:data/vesc_help_group/text_slices/input_part001.txt†L6208-L6233】【F:data/vesc_help_group/text_slices/input_part001.txt†L6329-L6336】

### Harness Planning & Connector Advice
- Happy Giraffe sought shielded multi-core looms for throttle, brake, and power-button lines; Koxx recommended 24–26 AWG shared-ground cables or compact AliExpress harnesses, noting that overbuilt Ethernet looms strain Xiaomi passthroughs and that CAN cabling remains the neatest option.【F:data/vesc_help_group/text_slices/input_part001.txt†L6481-L6500】【F:data/vesc_help_group/text_slices/input_part001.txt†L6503-L6504】

### FOC Launch Behavior vs Square-Wave Controllers
- Riders comparing Blade hubs on VESC vs Chinese square-wave ESCs agreed FOC’s power-based throttle feels soft off the line; matching the “kick” of cheap controllers requires higher start current, tuned duty-cycle ramps, or alternative throttle curves to avoid sensorless surges around 25 km/h.【F:data/vesc_help_group/text_slices/input_part001.txt†L6860-L6899】

### Blade Motor Pricing & Xiaomi Fitment Tips
- Blade-branded Longyu 60 V motors were being sourced around €180 each (hub only), with sellers warning that rims and tires add extra cost and that Weped-spec 75 mm versions are scarce outside FastRide’s allocation.【F:data/vesc_help_group/text_slices/input_part001.txt†L6912-L6963】
- Xiaomi G30 conversions require reversing Monorim swingarms, drilling fresh axle slots, and trimming dropouts for security washers; builders showed how bent retainers or cheap sliders can compromise axle bite if left unmodified.【F:data/vesc_help_group/text_slices/input_part001.txt†L7093-L7147】

### Active Balancing & Pack Mixing Cautions
- Some riders skip discharge BMS boards entirely on 20S builds by pairing fuses with JK active balancers, but others still prefer integrated 150 A BMS hardware to retain charge protection while minimizing bottlenecks.【F:data/vesc_help_group/text_slices/input_part001.txt†L6955-L6970】
- Mixing MJ1 and MH1 cells in parallel packs drew pushback because of divergent discharge curves above 8 A per cell, reinforcing the need to keep parallel strings chemistry-matched when chasing 130 A pack output.【F:data/vesc_help_group/text_slices/input_part001.txt†L7100-L7125】

### VESC PID & Startup Tuning Recipes
- Koxx reiterated that poor launch torque on current control stems from ramp timing and PID setup, while community-shared playbooks detail wizard settings (1200 W motor size, unchecked current limits), FOC redetection, 20 kHz switching, hall interpolation tweaks, and aggressive PID gains to claw back low-speed punch on VSETT hubs.【F:data/vesc_help_group/text_slices/input_part001.txt†L6990-L7058】【F:data/vesc_help_group/text_slices/input_part001.txt†L7220-L7256】
- Logs from tuned single-motor setups show 90 kg riders holding full throttle above 30 km/h with 100 A lower current draw compared with stock configs, underscoring the efficiency gains of refined PID and throttle curves.【F:data/vesc_help_group/text_slices/input_part001.txt†L7003-L7028】

### Field-Weakening & Sensorless Experiments
- Owners confirmed that genuine field-weakening controls remain locked behind FW 5.3, leading to sideloading hunts for 300 A binaries and experimentation with duty-cycle triggers around 70 % to extend top speed beyond the 95–98 % duty plateau.【F:data/vesc_help_group/text_slices/input_part001.txt†L7166-L7194】
- Happy Giraffe’s trials highlighted the confusion around Vedder Sensorless Start vs. classic HFI, with VSS hiding under sensorless encoders and requiring motor temperature inputs for the quiet profile, while fallback to hall-only launches still left 5 s 0–30 km/h acceleration on hill starts.【F:data/vesc_help_group/text_slices/input_part001.txt†L7351-L7415】

### Single Ubox Thermal Constraints & Mitigations
- Multiple riders hit 65–75 °C MOSFET readings at just 50–60 A battery on single Ubox installs, blaming poor thermal pad compression; Spintend support confirmed 0.5 mm stock pads and suggested stiffer 1 mm replacements or even case swaps to boost clamp pressure.【F:data/vesc_help_group/text_slices/input_part001.txt†L7354-L7531】【F:data/vesc_help_group/text_slices/input_part001.txt†L8149-L8153】
- Community experiments now include sanding paint from decks, cutting heat-shrink over the MOSFET bank, adding stick-on sinks, and even considering thermal grease baths to pull heat away when enclosures must stay sealed.【F:data/vesc_help_group/text_slices/input_part001.txt†L7489-L7529】【F:data/vesc_help_group/text_slices/input_part001.txt†L8079-L8101】

### Phase Resistance & Connector Rework
- High 53 mΩ phase readings traced back to sloppy XT150 soldering and long lead lengths; the fix is to reflow the strands tight against the connector walls, shorten cable runs, and consider upsizing to 6–8 mm bullets when chasing 100 A peaks.【F:data/vesc_help_group/text_slices/input_part001.txt†L7532-L7599】
- Reference measurements place HM 1600 W hubs around 132 mΩ, Blade motors near 85 mΩ, and Rion-spec hubs at 50 mΩ—useful benchmarks when diagnosing heat from excessive winding resistance.【F:data/vesc_help_group/text_slices/input_part001.txt†L7595-L7600】

### Ferrofluid Sourcing & Conductivity Debate
- Builders compared sourcing statorade directly from Grin vs. cheaper ferrofluids, noting Grin’s product delivers ~30 % winding temperature drops without noticeable drag when dosed at 6 ml, whereas bargain fluids risk conductivity, residue, and magnet damage.【F:data/vesc_help_group/text_slices/input_part001.txt†L7901-L8089】【F:data/vesc_help_group/text_slices/input_part001.txt†L8079-L8109】
- Follow-up testing suggests magnets may run warmer but transfer heat to cases faster, and that proper sealing with automotive silicone prevents leaks even on off-road builds.【F:data/vesc_help_group/text_slices/input_part001.txt†L8038-L8098】

### Controller Upgrade Comparisons
- Nucular owners showcased current-change-speed controls that deliver burnouts on Dualtron builds and praised CAN displays that eliminate phones, while lamenting long lead times for 12F/24F units.【F:data/vesc_help_group/text_slices/input_part001.txt†L8162-L8210】【F:data/vesc_help_group/text_slices/input_part001.txt†L8254-L8269】
- Kelly 7212/7218 discussions highlighted 60 V spike ratings, 120 A boost modes, waterproof housings, and the trade-off of bulky enclosures versus VESC configurability; some riders plan Xiaomi installs with hidden three-speed switches to retain “police” modes.【F:data/vesc_help_group/text_slices/input_part001.txt†L8290-L8338】
- Interest in Sabvoton controllers is rising—builders are ordering kits for 18S scooters but still need ride data before recommending them over VESC or Kelly options.【F:data/vesc_help_group/text_slices/input_part001.txt†L8290-L8400】

### Brake Rotor & Mount Upgrades for VSETT Builds
- Upgrading from stock 140 mm rotors to 160 mm SRAM Cleansweep discs on VSETT 10+ improves braking torque and heat rejection when paired with ceramic pads and IS-to-post adapters; Magura MDR-P options offer even more stiffness if clearance allows.【F:data/vesc_help_group/text_slices/input_part001.txt†L8211-L8243】【F:data/vesc_help_group/text_slices/input_part001.txt†L8220-L8236】
- Builders trading washer stacks for purpose-built brackets or drilling suspension arms stressed aligning pads level to avoid warping rotors under heavy loads, especially when stepping up to 180 mm Magura hardware.【F:data/vesc_help_group/text_slices/input_part001.txt†L8237-L8253】

## Open Questions / Follow-ups
- Gather hard data on MakerX Mini FOC survival rates above 12S, including scope captures of regenerative spikes, to confirm the safe margin (if any) for 13S commuters.【F:data/vesc_help_group/text_slices/input_part001.txt†L4-L65】
- Document a repeatable procedure for validating hall sensors using both 3.3 V and 5 V supplies, including expected ADC count ranges in VESC Tool screenshots.【F:data/vesc_help_group/text_slices/input_part001.txt†L32-L53】
- Capture before/after checklists for Weped GTS mechanical fixes (fork bearings, fastener lengths, steering column alignment) to inform future customers who receive unprepared units.【F:data/vesc_help_group/text_slices/input_part001.txt†L285-L440】
- Prototype a compact pre-charge or solid-state switch solution for 18S–20S scooters that integrates cleanly with 75100 installs, reducing reliance on sacrificial XT90S loop keys.【F:data/vesc_help_group/text_slices/input_part001.txt†L660-L681】
- Validate a firmware path that unlocks field weakening on 75100 hardware without bricking the controller, and quantify the speed gains vs. thermal penalties for 16S and 20S packs.【F:data/vesc_help_group/text_slices/input_part001.txt†L697-L748】【F:data/vesc_help_group/text_slices/input_part001.txt†L1086-L1099】
- Build a comparative datasheet of VSETT-compatible hub motors (HM, LY, stock) covering stator width, winding, and efficiency so retrofitters can match controllers to torque and cooling limits.【F:data/vesc_help_group/text_slices/input_part001.txt†L1010-L1031】
- Capture tuning guidance to smooth 75100 sensored→sensorless transitions (PID expectations, logging procedure) so high-voltage riders can avoid the noted “tah” stutter.【F:data/vesc_help_group/text_slices/input_part001.txt†L1696-L1889】
- Quantify safe operating envelopes for 24S conversions on 75100s, including regen disable strategies and surge suppression to prevent back-EMF induced failures.【F:data/vesc_help_group/text_slices/input_part001.txt†L1699-L1720】【F:data/vesc_help_group/text_slices/input_part001.txt†L1904-L1909】
- Benchmark Sony VTC6A vs. Molicel P42A thermal and voltage sag performance under 30–40 A discharge to validate anecdotal claims before recommending premium cells.【F:data/vesc_help_group/text_slices/input_part001.txt†L1603-L1655】
- Draft an inbound QC checklist for FlipSky/Spintend controllers (fastener audit, solder cleanup, insulation tests) to avoid repeat of the documented solder-ball fires.【F:data/vesc_help_group/text_slices/input_part001.txt†L2023-L2176】
- Evaluate Zero 10X Limited thermal management with relocated controllers and stem-mounted packs to see if the format can safely support 20S conversions.【F:data/vesc_help_group/text_slices/input_part001.txt†L2464-L2519】
- Record controlled brake tests comparing MDR-P vs. Storm HC rotors (temperature, deceleration, fade) to settle the rotor debate for >90 km/h scooters.【F:data/vesc_help_group/text_slices/input_part001.txt†L2891-L3010】
- Publish a safe flashing workflow for Spintend/75100 owners covering rail-voltage checks, wireless bridges, and Android file transfers so users can adopt 5.3 without bricking hardware.【F:data/vesc_help_group/text_slices/input_part001.txt†L3326-L3369】【F:data/vesc_help_group/text_slices/input_part001.txt†L4000-L4018】
- Create a harness retrofit guide that consolidates best practices for rewiring dual-phase motors into single 8–10 AWG leads and selecting shielded control cables with 5 V→3.3 V adapters.【F:data/vesc_help_group/text_slices/input_part001.txt†L3260-L3605】
- Develop a troubleshooting checklist for ABS current faults and sensorless surging that pairs the `faults` log workflow with connector inspections and absolute-current tuning heuristics.【F:data/vesc_help_group/text_slices/input_part001.txt†L2840-L2872】【F:data/vesc_help_group/text_slices/input_part001.txt†L3757-L3810】
- Model controller requirements for 40+ Kv hub motors (phase amps vs. ERPM) to determine when Kelly/Sabvoton-class hardware becomes mandatory over compact VESCs.【F:data/vesc_help_group/text_slices/input_part001.txt†L3820-L3856】
- Package a lightweight Excel/Notebook template that ingests VESC CSV logs, surfaces min/max values automatically, and exports summaries for Discord/Telegram sharing.【F:data/vesc_help_group/text_slices/input_part001.txt†L3440-L3994】
- Compare field-weakening energy cost vs. voltage or gearing changes using repeatable road tests so builders know when the feature is worth enabling.【F:data/vesc_help_group/text_slices/input_part001.txt†L4053-L4148】
- Draft a troubleshooting and protection guide for Ubox/Spintend ADC inputs (resistor dividers, CAN isolation, reflash steps) to prevent STM32 failures like the documented shorted rail.【F:data/vesc_help_group/text_slices/input_part001.txt†L4386-L4499】
- Outline a brake-mount reinforcement procedure (hardware sizing, adapter tolerances) for MT7/MDR-P conversions to stop M5 bolt ovalization on high-power scooters.【F:data/vesc_help_group/text_slices/input_part001.txt†L4671-L4707】
- Produce a cleaning and connector upgrade checklist for incoming Ubox V2 units covering solder-ball inspection, throttle-filter housing, and high-current plug replacements.【F:data/vesc_help_group/text_slices/input_part001.txt†L5060-L5284】
- Capture a paint-removal and thermal mounting checklist for Ubox installs so riders can replicate the 55 °C results seen after sanding decks and reseating pads.【F:data/vesc_help_group/text_slices/input_part001.txt†L5400-L5438】
- Build a sourcing matrix for VSETT and Blade motors summarizing dropout modifications, warranty trade-offs, and shipping costs across EU suppliers vs. AliExpress listings.【F:data/vesc_help_group/text_slices/input_part001.txt†L5520-L5631】【F:data/vesc_help_group/text_slices/input_part001.txt†L5695-L5718】
- Publish an inbound Ubox V2 QA guide that confirms BLE module delivery, verifies ADC rail voltages, and lists adequate soldering gear for 10 AWG lead swaps.【F:data/vesc_help_group/text_slices/input_part001.txt†L5811-L5868】【F:data/vesc_help_group/text_slices/input_part001.txt†L5920-L5938】
- Document a Magura bleed and hose-shortening workflow (parts list, linked videos, torque notes) for XDE300 conversions.【F:data/vesc_help_group/text_slices/input_part001.txt†L5947-L5988】
- Track ferrofluid-treated hub performance over extended rides, logging magnet temps alongside stator data to confirm the long-term benefits seen after the 6 ml Statorade fill.【F:data/vesc_help_group/text_slices/input_part001.txt†L6340-L6362】【F:data/vesc_help_group/text_slices/input_part001.txt†L6800-L6821】
- Explore adapting VESC firmware to emulate Nucular’s PSU-based phase-wire charging with configurable CC/CV thresholds and 95 % SOC cutoffs.【F:data/vesc_help_group/text_slices/input_part001.txt†L6208-L6233】【F:data/vesc_help_group/text_slices/input_part001.txt†L6329-L6336】
- Document a Xiaomi G30 Blade motor swap guide covering Monorim arm flipping, dropout drilling, and axle washer retention to avoid spin-outs.【F:data/vesc_help_group/text_slices/input_part001.txt†L7093-L7147】
- Evaluate JK active-balancer-only powertrains vs. traditional BMS packs to quantify reliability and protection trade-offs on 20S scooters.【F:data/vesc_help_group/text_slices/input_part001.txt†L6955-L6970】
- Package the shared VESC PID/PWM tuning workflow (wizard values, FOC retune, PID gains) into a reproducible checklist with log examples.【F:data/vesc_help_group/text_slices/input_part001.txt†L6990-L7058】【F:data/vesc_help_group/text_slices/input_part001.txt†L7220-L7256】
- Prototype a single-Ubox thermal mod kit (pad thickness, deck sanding, auxiliary sinks) and benchmark MOSFET temps before/after under 60 A loads.【F:data/vesc_help_group/text_slices/input_part001.txt†L7354-L7531】【F:data/vesc_help_group/text_slices/input_part001.txt†L8149-L8153】
- Measure phase resistance after connector rework to validate the recommended solder techniques and compare against HM/Blade/Rion reference data.【F:data/vesc_help_group/text_slices/input_part001.txt†L7532-L7600】
- Compile ferrofluid conductivity lab results to confirm statorade’s insulation claims and outline safe dosing per motor size.【F:data/vesc_help_group/text_slices/input_part001.txt†L7901-L8089】
- Compare Nucular, Kelly, and Sabvoton acceleration settings vs. VESC capabilities to guide controller selections for sleeper Xiaomi and VSETT builds.【F:data/vesc_help_group/text_slices/input_part001.txt†L8162-L8338】【F:data/vesc_help_group/text_slices/input_part001.txt†L8290-L8400】
- Map rotor/bracket combinations (140 → 160 → 180 mm) for VSETT and Xiaomi forks, including sources for IS-to-post adapters and clearance checks.【F:data/vesc_help_group/text_slices/input_part001.txt†L8211-L8253】
- Prototype throttle curves and duty-cycle start ramps that restore square-wave launch feel without overheating Spintend hardware or triggering sensorless surges around 25 km/h.【F:data/vesc_help_group/text_slices/input_part001.txt†L6115-L6331】【F:data/vesc_help_group/text_slices/input_part001.txt†L6860-L6899】
