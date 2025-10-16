# Makerbase Controllers Brand Dossier

## TL;DR

- Aluminum-PCB 75100 boards remain the go-to budget dual-controller option for 60 V commuters, but they only stay reliable when capped around 70 A battery / 170–180 A phase and kept below ≈22 S; bumping currents higher has popped freshly installed units in a single launch. [^1][^2][^3]
- Community veterans still warn that Makerbase boxes ship with stray solder, weak DC/DC rails, and inconsistent shunt calibration—treat every unit as a kit: open it, add proper heatsinking, and plan fallbacks to 3Shul or Spintend hardware if you need more than ≈50 A battery per controller. [^4][^5]
- Paulo flagged that the legacy dual 100/100 ran counterfeit or second-hand STM chips sourced during the shortage—those boards glitched on firmware newer than 5.2 and the quality cloud still hangs over early 84100 production until supply chains are verified.[^6]
- 2023 clone batches arrived with watery thermal paste, uneven pads, and even dead CAN buses; shops now budget time to repaste, reflow power leads, and bench-test comms before mixing them with Flipsky hardware. [^7]
- MakerBase’s new 75 V/100 A bargain controller mimics Flipsky pricing but lacks proven QC or Bluetooth, so riders are waiting on tear-downs before trusting it on high-amp builds despite the marketing push.[^8]
- Clone “bargains” continue to overheat beyond ~110 A and ship without warranty cover, pushing veterans toward Spintend or proven MakerX hardware until detailed teardowns confirm component quality.[^9]
- Pandalgns is still hammering 84 200 boards around 350 A battery on 60 V packs while eyeing 22 S upgrades—treat the hardware as consumable unless you’re ready to accept recall-level risk.[^10]
- The 84100 HP revision adds Bluetooth, thicker leads, and a higher-voltage stack, yet it still expects a normally-closed ignition switch and proves happiest near 60–80 A battery / 150–180 A phase with regen kept under ~84 V; plan the 1 MΩ ignition mod and keep thermal logs if you stretch toward triple-digit speeds. [^11][^12][^13][^14]
- Izuna’s community firmware patch rescues the aluminum-case 75100 V2 voltage-sense bug, and riders peg the refreshed controller at roughly €75 delivered—about half the cost of Spintend’s 12-fet hardware—so budget builds can stay on Makerbase gear if they accept the missing extras Spintend ships stock.[^15]
- Recent field reports show the 84xxx HP family surviving 22 S testing and sustained high current so long as phase insulation, BMS behavior, and chassis grounding are squared away—most catastrophic failures traced back to shorts, not silicon. [^16]
- Sideways heatsink screws on the 84 V housings choke airflow—owners expect to add thermal pads or external plates before chasing the advertised 200 A limits.[^17]
- 84200/84100 decks still need airflow and chassis mass to keep up with Spintend/Ubox installs—treat Makerbase housings as heat spreaders, not sealed bricks, or they roast quickly on 84 V builds.[^18]

## Product Line Cheat Sheet

| Model | Practical Pack Window | Working Envelope & Use Case | Notable Traits & Caveats |
| --- | --- | --- | --- |
| 75100 (Alu PCB) | 48–84 V (≤22 S with regen trimmed) | ≈60–70 A battery, 160–180 A phase once clamped to metal; budget dual-motor CAN builds for G30/Vsett frames | Requires CAN linking for duals, disable regen above ~22 S, inspect firmware headers (often mislabeled as HW75300), and expect duty ripple if firmware/tool versions drift. [^1][^19] |
| 75200 V2 | 16–22 S (marketing up to 24 S) | ≈90–110 A battery combined in dual installs when cooled; suits mid-power scooters needing native key input | Roughly 130 × 68 × 28 mm with onboard shutdown lead; still needs heatsink trimming in tight decks and thorough thermal paste refresh. [^20][^21] |
- Expect sustained fade once you push around 250 A phase / 150 A battery—Shlomozero’s 75200 started tapering there even with MOSFET telemetry near 100–110 °C, so treat those figures as the practical ceiling without major cooling changes.[^75200-fade]
| 60100 HP | ≤15 S commuters | ≤50 A battery on single-motor city builds; reliable regen on Navee N65/Ninebot conversions once the dash is bypassed | Retains OEM dashboards with rewiring, but voltage headroom and 60 V component ratings limit regen spikes—experiments suggest INA241 current-sense swaps could unlock 14–20 S if Makerbase keeps the line alive.[^22][^23] |
| 84100 HP | 60–84 V (≤20 S recommended) | ≈60–80 A battery, 150–180 A phase for Zero/Nami dual builds; higher only with extensive cooling and telemetry | Ships with NC ignition logic, integrated Bluetooth, sacrificial 0 Ω links, and benefits from the 1 MΩ pull-down mod plus active thermal management before chasing 100 km/h logs. [^12][^24][^25][^11] |

## Voltage, Current & Regen Guardrails

- Keep regen ceilings conservative on 22 S packs: riders log 75100 and 84100 boards failing when negative current stacks back-EMF above ~84 V, so either disable e-brake or cap battery regen under −10 A on high-voltage builds. [^13][^26]
- Builders trying to mask weak Laotie packs by running 22 S accept that the aluminum 75×00 hardware only pushes about half the battery amps it reports and that staying safe means disabling electronic brakes altogether; treat those experiments as limp-home strategies, not headroom gains. [^27]
- Expect the 75200 to soft-cap after sustained pulls: even with thermal cut set around 100–110 °C, riders saw 250 A phase / 150 A battery tunes fade during extended runs, pointing to internal current limiting once the enclosure heat soaks. [^28]
- Single-controller sleepers still work: a lone 75200 driving a 22×3 70 H hub launched cleanly around the 10 kW mark once cooling and cabling were sized correctly, reinforcing that the hardware can anchor single-motor builds when envelopes stay realistic.[^29]
- BMS settings are not a safety net—slow-trip Daly boards still let surges vaporize Makerbase gate drivers. Shorten trip delays and log every cutoff instead of assuming rated limits will save a fault. [^30]
- Firmware reports battery current plus field-weakening draw; budget 10 A of FW as additional pack load so commuter cells stay within safe C-rates. [^31][^32]
- Treat 23 S marketing with skepticism—community testers still cap Makerbase hardware at ≤20–22 S even on the 84100 because component tolerances and regen spikes remain the primary failure points. [^33][^34]
- Veteran tuners now label 22 S experiments “suicide” unless you derate current, skip MTPA/field weakening, or upgrade the MOSFETs—stock hardware keeps popping when riders apply full 22 S output without significant rework. [^35]
- Verified 22 S survivors all shared meticulous harness audits—phase shorts to the chassis, not voltage itself, killed the lone documented 84200 HP board—so bake insulation checks and BMS regression tests into every high-voltage install. [^16]
- ALU 75×100 boards default to ~30 kHz zero-vector frequency and riders warn against pushing higher; the same thread debunked rumours that STM32F405 ADC pins tolerate steady 5 V throttle inputs—stick to 3.3 V rails or add dividers.[^36]
- Cap absolute current near 250–300 A even on aluminum-PCB 75100s—ABS abuse around 450–500 A shredded one board, and clones with weaker MOSFET bins start overheating past ≈110 A battery anyway. [^37]
- Treat higher pack voltage as a hardware change: one aluminum 75100 that behaved on 16 S instantly shorted both motors at the first throttle input on 22 S, reinforcing that regen spikes and MOSFET limits demand full component audits before raising voltage.[^38]
- JPPL is still squeezing roughly 60 A battery per side, 300 A shared pack current, and ~420 A absolute out of well-cooled units, but treats those numbers as the ceiling for hand-picked controllers rather than a new baseline.[^39]
- Leave ≥5 V of headroom between pack max and BMS high-voltage cutoff; Paolo’s rear 75100 accelerated uncontrollably before an over-voltage trip killed the logic board when the cutoff sat at the ESC limit. [^40]

## Reliability & Incoming Inspection

- Open every new board: veterans keep finding loose capacitors, missing thermal paste, and even epoxy jumpers on fresh shipments; reglue caps and retorque hardware before install. [^41][^42]
- Replace the watery factory paste with full-coverage pads or quality paste before loading the controller—Paolo keeps seeing clone 75100s arrive with barely any contact area, which explains early thermal throttling. [^43]
- Mirko’s 15 mm aluminum baseplate plus open deck airflow held dual-controller 190 A phase / 70 A battery runs near 52 °C, underscoring how enclosure design matters as much as MOSFET choice when stretching Makerbase hardware.[^44]
- Don’t piggyback the regulator enable pin—tying accessories straight into the EN pad without isolation browns the gate drivers, so stick with proper antispark hardware and protect the 12 V rail before experimenting with remote switches.[^45]
- Builders pressed for rain protection are potting 84100 logic boards with conformal coat and printed covers instead of full epoxy so they can still service ADC pins and wiring between storms.[^46]
- Makerbase 75/200 boards ship with Huayi HYG015N10NS1TA MOSFETs; stick with the same package when repairing blown phases so switching losses and thermal margins stay predictable.[^47]
- Makerbase Lite riders dropped core temps roughly 25 °C by replacing the factory 5 mm interface with 0.5 mm thermal pads and bolting the case directly to aluminum—treat thick stock pads as insulation, not a heatsink bridge.[^48]
- Makerbase is teasing an epoxy-backed control board that mirrors the G300 layout; the community wants upgraded MOSFETs and better thermal paths before trusting the claimed 300 A rating.[^49]
- Giuseppe’s supposedly refreshed 75100 V2 still died mysteriously, reminding shops that some batches remain flaky enough to warrant factory diagnostics or outright RMAs before redeploying them on customer scooters.[^50]
- Hurriicane’s aluminum-PCB 75100 V2 booted fine over SWD but stayed dark on pack voltage until he traced a missing 12 V feed to one EG3112 gate driver—expect constant undervoltage faults until the buck regulator or trace is repaired.[^51]
- Bench-test CAN alongside the 12 V rail: multiple “V2” clones shipped with dead CAN transceivers despite tri-shunt markings, and sudden first-launch deaths usually track back to firmware or 12 V supply faults rather than MOSFET legs. Reflow power leads, disable phase filters, rerun detection, and confirm network health before hitting the street. [^52]
- Add bulk capacitance to the 12 V (and where accessible, 5 V/3.3 V) rails—the retrofit prevents infamous brownouts when BMSs trip or accessories spike load, especially on resin-potted boards.[^53][^54]
- Resin-potted 75100s still need the ignition/12 V cutoff fix; builders now tack capacitors onto exposed 5 V/3.3 V rails or sneak them into the harness because random key-off events keep nuking MOSFET drivers otherwise.[^55]
- Budget gate-driver spares and scope time—dead EG3112s have been shorting the 5 V rail after MOSFET pops, so techs now replace the drivers alongside FETs and verify clean gate waveforms before sealing the case again.[^56]
- Debate over the boxed 75100’s factory shunts persists: some builders still rip them out as “trash” that misreport current while others find the aluminium revision strong once reworked, so budget time either to replace the shunt stack or to tune around its quirks.[^57]
- Add bulk capacitance to the 12 V (and where accessible, 5 V/3.3 V) rails—the retrofit prevents infamous brownouts when BMSs trip or accessories spike load, especially on resin-potted boards. [^58][^59]
- Clean residual solder paste before second-guessing ignition dividers; leftover “lotfett” kept a 10 kΩ link from latching until the board was scrubbed and reassembled.[^60]
- Resist the urge to replace the stock ring of small electrolytics with a couple of larger cans when chasing deck clearance—Izuna’s G30 conversion trimmed the bank to ≈2,000 µF with two low-profile caps and had to reterminate 8 AWG battery leads after desoldering struggles, underscoring the response hit and extra labor involved.[^61]
- MakerBase Express hides its Wi‑Fi aerial under the combined Bluetooth antenna—recent Express batches arrive with no external whip at all—so plan add-on antennas if you need remote telemetry, and keep insulating hall PCBs after Pandalgns traced repeated failures to shorts that cooked CAN regulators.[^62][^63]
- Meter throttle outputs on the bench and clamp them to ≤3.3 V before plugging into the ADC rail; builders just reiterated that 3.5 V already flirts with the MCU’s ceiling on MakerBase hardware.[^64]
- Insulate the logic and Bluetooth stack with Kapton or similar dielectric film; one 75100 nearly lost its 3.3 V rail to static discharge until the owner lined the enclosure, underscoring how fragile the low-voltage supply remains.[^kapton_static]
- After any short or desoldered component event, confirm the onboard 5 V regulator is still alive—one 75100 V2 kept running after repairs but lost its 5 V rail entirely and now needs an external converter or replacement regulator before the logic stage is trustworthy again.[^65]
- Document MOSFET and driver replacements: hot-plug failures often kill only part of a parallel set, so replace all devices on that leg and confirm 12 V/5 V rails before reassembly. [^66][^67]
- Never solder live Makerbase boards—energised 75200 repairs burst into flames immediately, so disconnect packs, strip old paste, and thread-lock covers after every service session.[^68]
- Expect excess paste and even blobs of glue on recent 75200 batches; scrape the surplus, repaste, and thread-lock the small screws so the case reassembles without crushing pads. [^69]
- If launches turn noisy, start with firmware and detection—fresh 75100 installs have quieted immediately after rerunning hall/phase detection and verifying telemetry before chasing hardware faults.[^70]
- Verify shunt calibration with clamp meters or smart-BMS telemetry; many 75100s deliver only half the programmed battery amps until you correct the scaling. [^71]
- **Audit replacement wiring gauges.** Repairs that reuse 1.5 mm² house wire have already melted, shorting battery leads and blowing MOSFETs—inspect gate drivers and only fit higher-spec devices such as NCEP15T14 after the harness is sized correctly.[^72]
- r0005 firmware assumes only a single shunt per phase—owners still strip two resistors from the factory three-high stacks and need 500 °C hot air plus iron follow-up to clear the solder so current readings stay accurate.[^73]
- Reflash shunt mods immediately—swapping the factory stack to ≈1.7 mΩ without updating firmware halved reported current until a 6.02 write restored scaling, so treat hardware tweaks as firmware work as well. [^74]
- Expect wiring faults, not silicon, to kill repaired boards—recent failures traced back to hall shorts and melted leads that took the new 84100 HP down mid-ride even without a BMS cutoff.[^75]
- Clamp BLE modules, SmartDisplay bridges, or other add-ons with real thermal adhesive or machined brackets; boxed 75×100 units still ship with genuine STM32 MCUs but rely on compression to keep accessory heatsinks seated until proper glue arrives.[^76]
- Bench-test at both low and full pack voltage before installation—one 75 100 that happily booted on 3 S refused to wake on 13–16 S even after reflashing, pointing to high-voltage hardware faults that warrant an immediate RMA instead of more firmware experiments. [^77]
- Budget 84xxx samples with the bottom-facing heatsink still demand custom brackets and active airflow—the case shortens overall height but cooks quickly unless you relocate the controller or add forced cooling. [^78]
- Avoid shrink-wrapping the baseplate—enclosing the aluminum shell trapped heat on a Xiaomi build until the owner cut ventilation back into the case.[^79]
- **Log thermal differences between housings.** Aluminum-shelled 75100s stayed near ambient during 30 min, 45 km/h rides at 11 °C when airflow reached the fins, while boxed versions still overheated around 35 A—proof that enclosure choice matters as much as tuning.[^80][^81]
- Skip hard potting unless you accept throwaway repairs—silicone (e.g., 705 RTV) still lets you service ADC pins, add capacitors, or reflash firmware, whereas epoxy-sealed 75100s trap the MCU and driver rails under resin and make ignition or capacitor fixes nearly impossible. [^82][^83]
- Builders chasing splash protection now CAD PLA+/PETG housings and jet-duct side pods for Xiaomi deck installs, sealing seams with silicone or dielectric epoxy so aluminum-PCB 75100s survive rain without suffocating their heatsinks.[^printed_housings]
- Log intermittent ignition latch pop-open events; they sometimes self-resolve, hinting at marginal wiring or moisture, but still deserve a ticket before they strand the rider.[^84]
- **Diagnose dead 5 V rails promptly.** One 75100 Alu board ran on 3.3 V throttle power but measured only 0.3 V on the sensor rail, losing hall detection—classic evidence of a blown DC/DC stage requiring repair before reconnecting sensors.[^dead_5v]
- **Reflow sloppy MCU solder joints.** Intermittent-boot 75 100 Alu boards were revived by reflowing the GD32 MCU after inspection revealed joints ranging from starved pads to heavy blobs, stabilizing CAN, ABS limits, and USB connectivity.[^mcu_reflow]
- **Replace cracked MOSFETs with hotplate technique.** Aluminum-PCB repairs require heating the entire sink, checking diode drops as it cools, and verifying gate drivers before reassembly—hot air alone cannot remove devices cleanly.[^mosfet_hotplate]

## Setup & Commissioning Checklist

1. **Flash matching firmware/tool pairs.** Makerbase boards frequently ship misidentified (e.g., reporting as HW75300); desktop VESC Tool flashing plus phase-filter disable after detection stabilizes idle behavior. [^85][^86]
2. **Inspect ignition logic before wiring switches.** 75100 units expect a momentary latch—bridge 5 V to the AD15 enable pin for roughly a second to turn on (three seconds to shut down), add a 10 kΩ/100 kΩ divider to hold the EN pin above 1.5 V at minimum pack voltage, and set the ADC shutdown timer so the controller actually unlatches—while 84100HP controllers need a normally-closed switch or the documented 1 MΩ pull-down to mimic Ubox-style keys. If an ignition-mod board still reboots randomly, lower the pull-down resistance further so the enable pin stays latched instead of floating. [^87][^88][^89][^90][^91]
3. **Leverage the 75200 VCC selector when pairing smart BMS keys.** The latest boards ship with a 3.3 V/5 V selector and SW pins that tie directly into LLT key outputs, letting the BMS precharge and toggle the controller daily without rewiring harness power—enable the controller’s DC/DC control mode when reusing OEM switches. [^92][^93]
4. **Log both controllers on CAN.** Always `Read` active configs before writing; mismatched IDs or version drift can silently overwrite both nodes during tuning. [^94]
5. **Link CAN before pairing dashboards.** Makerbase dual-drive owners remind newcomers to wire CAN high/low between controllers (no shared positive) so both nodes synchronise before Bluetooth or dash pairing.[^can_first]
6. **Trim sensorless shunt stacks when needed.** PuneDir cured 75100 V2 cogging by removing the parallel shunts down to one per phase, flashing the 0.0005 Ω firmware (or 75_300_r2 v5.1), and rerunning detection at ≈10 A with the Ortega observer—and he still removes the extra shunts after repairs so current telemetry stays honest.[^95][^96]
6. **Stage regen after thermal validation.** Start with mechanical brakes, then add modest battery regen while watching bus voltage—random 12 V rail dropouts usually trace back to aggressive negative current. [^97][^98]
7. **Clamp controllers to metal with fresh paste.** Aluminum cases shed heat only when bolted to frames or external plates; cramped decks that rely on air gaps have cooked MOSFETs even at moderate logs. [^99][^100]
8. **Swap observers if detection misbehaves.** MXUS/Ninebot hybrids that cog on 84100HP hardware smooth out once riders abandon Mxlemming for Ortega (no lambda) and rerun detection before re-tuning PI gains. [^101]
9. **Persist configs after every tuning session.** Mobile and desktop VESC Tool builds are still wiping Makerbase settings—re-run the motor wizard when needed, then explicitly `Write Motor Config` and `Write App Config`, and keep the bootloader handy for corrupted saves to stop ABS_overcurrent faults from returning after a reboot.[^102][^103]
10. **Document mixed hall/sensorless baselines before winter rides.** Dual 75×100 builds ran smoothly with ≈87 mΩ phase resistance, ≈310 µH flux linkage, 100 A phase, and 35 A battery per controller while leaving the front motor sensorless and the rear on halls—rerun detection as temperatures swing to keep cold-weather behaviour predictable.[^104]
11. **Expect high Rs readings on older hubs.** Makerbase 84100HP builds regularly detect ~55 mΩ on 45 H Mantis motors; treat those numbers as normal for low-kV windings instead of chasing phantom wiring faults.[^105]

## Wiring & Accessory Integration

- Power throttles from the 3.3 V rail and use resistor dividers for 5 V hall inputs; direct 5 V feeds have already killed STM32 ADC stages on Makerbase boards. [^106][^107]
- Makerbase 84 200 controllers happily wake from external dashboard/key switches—reuse the display’s power button circuit instead of hot-wiring pack leads, but log the wiring so the logic rail doesn’t back-feed accessories.[^108]
- Makerbase harness accessory headers use JST-GH 1.27 mm pitch—plan pigtails accordingly when integrating dashboards or brake sensors. [^109]
- Label the NRF Bluetooth header, hall plug, power-button leads, and comm-port 3.3 V/GND/ADC1 before adding dashboards—the crew just refreshed the colour map after repeated miswires cooked MakerX ADC daughterboards.[^110]
- Pair ADC adapters or dashboards with external relays if you need a real kill switch; the ADC lighting bridge only sources a few amps and cannot isolate the battery. [^111][^112]
- Keep horn/lighting loads small on the ADC harness—the Makerbase/Spintend “horn” pin sources only a couple of amps, so 35 W halogens belong on a dedicated DC/DC rail with the controller output simply driving a relay.[^adc_load]
- Publish a wiring card for every build: power BLE modules from the controller’s regulated 5 V, daisy-chain UART between dual controllers without cross-wiring TX/RX, and pin the throttle’s hall wires correctly before first power-up—recent field failures all traced back to inverted reference leads or shared 5 V rails that yanked controllers into limited mode.[^113][^114]
- For binary accessories or mower-style implements, bridge the throttle shunt’s red/white leads with ~10 kΩ or configure the ADC app with a pulldown so a normally-open switch maps cleanly between 0 % and 100 % duty.[^binary_accessory]
- The ADC Adapter V3 breakout keeps ignition, lighting, and accessory rails tidy—feed the board from the Makerbase controller, map ADC channel 9 to “control,” and let the adapter provide fused taps instead of back-powering through the BMS.[^adc_adapter]
- For NC ignition builds on the 84100HP, document the 1 MΩ pull-down and confirm the switch actually opens the STM32 input—builders have destroyed keys by wiring normally-open hardware without the mod. [^89][^115]
- 75100 V2 signal looms use JST-PH and XHB families—log the exact housings before ordering spares so replacement throttle and hall leads seat correctly. [^116]
- Rewire suspect throttles to the 3.3 V rail; Paolo’s Wolf revival only came back after ditching a 5 V feed that had crept into the harness. [^117]

## When to Choose Alternatives

- Projects demanding sustained ≥90 A battery or >200 A phase per motor should step up to Spintend 85/250, Tronic, or 3Shul hardware—pushing Makerbase past those envelopes repeatedly ends in MOSFET or gate-driver failures. [^22][^118]
- Riders unwilling to rework QC issues (thermal paste, capacitor staking, ignition mods) or lacking access to repair tooling should default to Ubox or 3Shul platforms with stronger support ecosystems. [^4][^119]
- Budget builds that cannot stomach downtime still migrate to Spintend, Tronic, or Seven controllers—community veterans treat Makerbase 84xxx boards as consumables when chasing 300 A-class logs or waiting on higher-spec revisions.[^alt_consumable]

## Source Notes

- Makerbase reliability notes, firmware quirks, and ignition wiring guidance consolidate the VESC Help Group reviews covering 2024–2025 slices on firmware misidentification, ADC voltage safety, and ignition latch requirements for 75100/84100HP controllers.[^120][^121][^122]
- Thermal management, regen tuning, and accessory integration recommendations pull from the same Smart Repair logs detailing paste refreshes, 12 V rail dropouts, and ADC adapter limits when pushing Makerbase hardware near its current ceiling.[^123][^94][^101]
[^printed_housings]: Community CAD drops document PLA+/PETG housings and jet-duct side pods that add splash protection for Makerbase 75100 decks while keeping airflow over the aluminum PCB. Source: knowledge/notes/input_part005_review.md, L72 to L72
[^can_first]: Makerbase dual-drive owners advising to wire CAN high/low between controllers before pairing BLE modules so both nodes stay in sync. Source: knowledge/notes/input_part012_review.md, L359 to L360
[^adc_load]: Makerbase/Spintend horn outputs sourcing only a couple of amps—insufficient for 35 W halogens—so riders trigger relays and power lights from dedicated converters. Source: knowledge/notes/input_part012_review.md, L97 to L98
[^adc_adapter]: Roby MacGyver’s ADC Adapter V3 workflow for keyed ignition, fused lighting, and profile control on Makerbase hardware without back-powering the BMS. Source: knowledge/notes/input_part011_review.md, L687 to L687
[^alt_consumable]: Veterans treating Makerbase 84xxx controllers as consumables while they chase 300 A logs or wait for higher-rated hardware, steering commuters to Spintend, Tronic, or Seven alternatives instead. Source: knowledge/notes/input_part012_review.md, L374 to L378. Source: knowledge/notes/input_part012_review.md, L397 to L398
[^kapton_static]: Kapton isolation preventing static discharge from killing a Makerbase 75100’s 3.3 V rail after the Bluetooth module touched the case. Source: knowledge/notes/input_part008_review.md, L45 to L45
[^binary_accessory]: Makerbase 75×100 owners bridging throttle shunt leads or adding ADC pulldowns to drive binary accessories with clean 0/100 % duty behaviour. Source: knowledge/notes/input_part006_review.md, L197 to L197
[^dead_5v]: Makerbase 75100 Alu board with dead 5 V rail losing hall detection until DC/DC stage repair. Source: knowledge/notes/input_part004_review.md, L325 to L325
[^mcu_reflow]: GD32 MCU reflow fixing intermittent boot on 75 100 Alu boards with poor factory solder joints. Source: knowledge/notes/input_part004_review.md, L294 to L294
[^mosfet_hotplate]: Hotplate technique for replacing cracked G015N10 MOSFETs on aluminum-PCB Makerbase boards. Source: knowledge/notes/input_part004_review.md, L282 to L282

## References

[^1]: Source: knowledge/notes/input_part004_review.md, L201 to L205
[^2]: Source: knowledge/notes/input_part004_review.md, L219 to L219
[^3]: Source: knowledge/notes/input_part004_review.md, L226 to L229
[^4]: Source: knowledge/notes/input_part005_review.md, L17 to L19
[^5]: Source: knowledge/notes/input_part005_review.md, L18 to L19
[^6]: Source: data/vesc_help_group/text_slices/input_part009.txt, L15886 to L15919
[^7]: Source: knowledge/notes/input_part003_review.md, L225 to L226
[^8]: Source: data/vesc_help_group/text_slices/input_part003.txt, L11390 to L11498
[^9]: Source: data/vesc_help_group/text_slices/input_part003.txt, L12384 to L12441
[^10]: Source: knowledge/notes/input_part012_review.md, L407 to L407
[^11]: Source: knowledge/notes/input_part007_review.md, L15 to L15
[^12]: Source: knowledge/notes/input_part007_review.md, L45 to L46
[^13]: Source: knowledge/notes/input_part007_review.md, L14 to L14
[^14]: Source: knowledge/notes/input_part009_review.md, L43 to L45
[^15]: Source: knowledge/notes/input_part007_review.md, L23 to L23
[^16]: Source: knowledge/notes/input_part014_review.md, L18 to L19
[^17]: Source: knowledge/notes/input_part007_review.md, L320 to L322
[^18]: Source: knowledge/notes/input_part007_review.md, L509 to L509
[^19]: Source: knowledge/notes/input_part004_review.md, L219 to L229
[^20]: Source: knowledge/notes/input_part005_review.md, L399 to L400
[^21]: Source: knowledge/notes/input_part007_review.md, L25 to L25
[^75200-fade]: Source: knowledge/notes/input_part013_review.md†L706-L706
[^22]: Source: knowledge/notes/input_part005_review.md, L19 to L19
[^23]: Source: knowledge/notes/input_part005_review.md, L194 to L197
[^24]: Source: knowledge/notes/input_part007_review.md, L168 to L168
[^25]: Source: knowledge/notes/input_part009_review.md, L43 to L44
[^26]: Source: knowledge/notes/input_part005_review.md, L152 to L152
[^27]: Source: knowledge/notes/input_part005_review.md, L105 to L107
[^28]: Source: knowledge/notes/input_part013_review.md, L705 to L706
[^29]: Source: knowledge/notes/input_part006_review.md, L340 to L340
[^30]: Source: knowledge/notes/input_part004_review.md, L361 to L363
[^31]: Source: knowledge/notes/input_part004_review.md, L227 to L227
[^32]: Source: knowledge/notes/input_part005_review.md, L208 to L208
[^33]: Source: knowledge/notes/input_part009_review.md, L113 to L113
[^34]: Source: knowledge/notes/input_part005_review.md, L106 to L106
[^35]: Source: knowledge/notes/input_part013_review.md, L781 to L781
[^36]: Source: knowledge/notes/input_part006_review.md, L187 to L187
[^37]: Source: knowledge/notes/input_part003_review.md, L106 to L114
[^38]: Source: data/vesc_help_group/text_slices/input_part004.txt, L6459 to L6464
[^39]: Source: knowledge/notes/input_part011_review.md, L423 to L430
[^40]: Source: knowledge/notes/input_part003_review.md, L161 to L161
[^41]: Source: knowledge/notes/input_part004_review.md, L229 to L229
[^42]: Source: knowledge/notes/input_part004_review.md, L434 to L434
[^43]: Source: data/vesc_help_group/text_slices/input_part003.txt, L24174 to L24207
[^44]: Source: data/vesc_help_group/text_slices/input_part003.txt, L12443 to L12494
[^45]: Source: knowledge/notes/input_part003_review.md, L88 to L88
[^46]: Source: data/vesc_help_group/text_slices/input_part009.txt, L11847 to L11854
[^47]: Source: knowledge/notes/input_part009_review.md, L85 to L85
[^48]: Source: knowledge/notes/input_part009_review.md, L92 to L92
[^49]: Source: knowledge/notes/input_part011_review.md, L430 to L435
[^50]: Source: knowledge/notes/input_part011_review.md, L435 to L442
[^51]: Source: knowledge/notes/input_part011_review.md, L344 to L351
[^52]: Source: data/vesc_help_group/text_slices/input_part003.txt, L24182 to L24304
[^53]: Source: data/vesc_help_group/text_slices/input_part005.txt, L24020 to L24070
[^54]: Source: data/vesc_help_group/text_slices/input_part005.txt, L24662 to L24694
[^55]: Source: data/vesc_help_group/text_slices/input_part005.txt, L24611 to L24703
[^56]: Source: knowledge/notes/input_part005_review.md, L211 to L213
[^57]: Source: knowledge/notes/input_part006_review.md, L341 to L341
[^58]: Source: knowledge/notes/input_part005_review.md, L448 to L451
[^59]: Source: knowledge/notes/input_part005_review.md, L510 to L510
[^60]: Source: knowledge/notes/input_part006_review.md, L45 to L45
[^61]: Source: knowledge/notes/input_part013_review.md†L605-L605
[^62]: Source: knowledge/notes/input_part013_review.md, L60 to L60
[^63]: Source: knowledge/notes/input_part013_review.md, L383 to L385
[^64]: Source: knowledge/notes/input_part013_review.md, L503 to L505
[^65]: Source: knowledge/notes/input_part012_review.md, L399 to L400
[^66]: Source: knowledge/notes/input_part004_review.md, L303 to L303
[^67]: Source: knowledge/notes/input_part004_review.md, L363 to L363
[^68]: Source: data/vesc_help_group/text_slices/input_part003.txt, L25812 to L25847
[^69]: Source: data/vesc_help_group/text_slices/input_part003.txt, L25888 to L25910
[^70]: Source: knowledge/notes/input_part006_review.md, L370 to L370
[^71]: Source: knowledge/notes/input_part005_review.md, L75 to L76
[^72]: Source: knowledge/notes/input_part005_review.md, L76 to L78
[^73]: Source: knowledge/notes/input_part006_review.md, L202 to L202
[^74]: Source: knowledge/notes/input_part007_review.md, L39 to L39
[^75]: Source: knowledge/notes/input_part007_review.md, L436 to L437
[^76]: Source: knowledge/notes/input_part006_review.md, L47 to L47
[^77]: Source: knowledge/notes/input_part004_review.md, L82 to L83
[^78]: Source: knowledge/notes/input_part007_review.md, L37 to L37
[^79]: Source: knowledge/notes/input_part007_review.md, L356 to L359
[^80]: Source: data/vesc_help_group/text_slices/input_part005.txt, L22528 to L22535
[^81]: Source: data/vesc_help_group/text_slices/input_part005.txt, L23900 to L23909
[^82]: Source: knowledge/notes/input_part005_review.md, L429 to L429
[^83]: Source: knowledge/notes/input_part005_review.md, L582 to L584
[^84]: Source: knowledge/notes/input_part006_review.md, L52 to L52
[^85]: Source: knowledge/notes/input_part004_review.md, L204 to L204
[^86]: Source: knowledge/notes/input_part004_review.md, L159 to L159
[^87]: Source: knowledge/notes/input_part011_review.md, L699 to L702
[^88]: Source: knowledge/notes/input_part011_review.md, L525 to L526
[^89]: Source: knowledge/notes/input_part007_review.md, L45 to L45
[^90]: Source: knowledge/notes/input_part006_review.md, L143 to L143
[^91]: Source: knowledge/notes/input_part006_review.md, L36 to L36
[^92]: Source: knowledge/notes/input_part006_review.md, L15801 to L15835
[^93]: Source: knowledge/notes/input_part006_review.md, L15969 to L15973
[^94]: Source: knowledge/notes/input_part009_review.md, L91 to L97
[^95]: Source: knowledge/notes/input_part007_review.md, L360 to L361
[^96]: Source: knowledge/notes/input_part007_review.md, L402 to L402
[^97]: Source: knowledge/notes/input_part004_review.md, L367 to L367
[^98]: Source: knowledge/notes/input_part005_review.md, L232 to L232
[^99]: Source: knowledge/notes/input_part005_review.md, L18 to L18
[^100]: Source: knowledge/notes/input_part007_review.md, L272 to L272
[^101]: Source: knowledge/notes/input_part014_review.md, L125 to L125
[^102]: Source: data/vesc_help_group/text_slices/input_part005.txt, L22499 to L22544
[^103]: Source: data/vesc_help_group/text_slices/input_part005.txt, L23016 to L23034
[^104]: Source: knowledge/notes/input_part006_review.md, L38 to L43
[^105]: Source: knowledge/notes/input_part009_review.md, L94 to L94
[^106]: Source: knowledge/notes/input_part004_review.md, L202 to L202
[^107]: Source: knowledge/notes/input_part004_review.md, L251 to L251
[^108]: Source: knowledge/notes/input_part012_review.md, L384 to L384
[^109]: Source: knowledge/notes/input_part004_review.md, L328 to L328
[^110]: Source: knowledge/notes/input_part013_review.md, L406 to L409
[^111]: Source: knowledge/notes/input_part005_review.md, L459 to L461
[^112]: Source: knowledge/notes/input_part005_review.md, L498 to L498
[^113]: Source: data/vesc_help_group/text_slices/input_part003.txt, L19880 to L19926
[^114]: Source: data/vesc_help_group/text_slices/input_part003.txt, L20790 to L20831
[^115]: Source: knowledge/notes/input_part007_review.md, L167 to L167
[^116]: Source: knowledge/notes/input_part003_review.md, L169 to L169
[^117]: Source: knowledge/notes/input_part003_review.md, L157 to L157
[^118]: Source: knowledge/notes/input_part007_review.md, L24 to L24
[^119]: Source: knowledge/notes/input_part004_review.md, L487 to L487
[^120]: Source: knowledge/notes/input_part004_review.md, L159 to L487
[^121]: Source: knowledge/notes/input_part011_review.md, L699 to L728
[^122]: Source: knowledge/notes/input_part007_review.md, L45 to L168
[^123]: Source: knowledge/notes/input_part005_review.md, L17 to L584
