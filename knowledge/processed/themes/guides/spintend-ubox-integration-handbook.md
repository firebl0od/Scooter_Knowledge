# Spintend Ubox Integration Handbook

## Overview

The Spintend Ubox is a popular dual-motor VESC controller for electric scooters, offering high power in a compact package. However, it requires careful QC inspection, proper thermal management, and disciplined setup procedures to avoid common failures. This handbook covers pre-delivery inspection, installation, configuration, thermal management, and troubleshooting based on extensive field experience.

## What You'll Learn

- Pre-delivery QC inspection procedures
- Proper thermal management and mounting
- Power-up sequences and safety protocols
- Accessory wiring (lighting, cruise, BLE)
- Current limit configuration
- Common failure modes and prevention
- CAN bus synchronization for dual setups
- Shipping, warranty, and support considerations

## ⚠️ Critical QC Warning

🔴 **Inspect BEFORE power-up!** Multiple Uboxes have shipped with solder balls, missing hardware, or phase wires touching the case. Full disassembly and photography before first power-on is non-negotiable—Spintend honors RMAs when you document QC issues.

## 📋 Quick Reference: Ubox Specifications

| Model | Voltage | Phase Current | Battery Current | Bluetooth | Best For |
|-------|---------|---------------|----------------|-----------|----------|
| Dual 75V (red case) | 20S-22S max | ~120A per motor | 25-30A per motor | ✅ Yes | Standard dual-motor builds |
| Dual Lite | 18S-20S | ~150A per motor | 20-25A per motor | ✅ Yes | Budget dual-motor |
| Single | 20S-22S | ~180A | 30-40A | ❌ No (needs bridge) | Single-motor conversions |
| 12-FET (85V/240A) | 24S max | ~240A | ~85A | ✅ Yes | High-power builds (~26kW) |

💡 **Pro Tip**: The Lite boards are realistically 150A-per-motor hardware despite dual housing. Plan upgrades to full Spin tend or 3Shul if you need more than ~120A sustained per motor.

## 📋 Pre-Delivery QC Checklist (Budget 1-2 Hours)

- [ ] **Full disassembly**: Remove case, inspect for solder balls, flux residue, loose screws
- [ ] **Photograph internals**: Document serial numbers and condition before power-up
- [ ] **Check phase lead insulation**: Verify silicone isn't cut by case edges
- [ ] **Verify MOSFET thermal contact**: Ensure pads touch MOSFETs evenly
- [ ] **Document hardware revision**: Note PCB color (FR4 vs aluminum), FET type
- [ ] **Test current-sense offsets**: Power on bench, verify readings are sane (not 30 or 4000 counts)
- [ ] **Check standby draw**: Should be ~20mA with switch off, no LED glow
- [ ] **Verify connector pinouts**: Especially important for used/revised units

## 🔧 Related Guides
- [Controller Setup](controller_setup.md) - VESC configuration basics
- [Motor Controller Tuning](motor_controller_tuning.md) - Current limit tuning
- [High-Power VESC Reliability](high-power-vesc-scooter-reliability-guide.md) - Build planning

## Key Principles

- Treat every unit as a kit: tear it down before energising, photograph QC issues for support, and follow VESC-safe power-up rituals (precharge, discharge caps, avoid hot-plugging) to prevent latent shorts or MCU damage.[^1][^2][^3]
- Spintend says the red 75 V dual still uses its best FETs and is teasing a 66 × 83 × 29 mm single-100 V controller to bridge current supply gaps while resale units circulate; brass baseplate concepts were shelved in favour of aluminium or copper spreaders.[^single_proto][^brass_swap]
- Clamp the case hard to a heat sink and budget active airflow if phase current will exceed ~120 A per channel; pad thickness and surface prep matter more than exotic materials.[^4][^5][^6][^7]
- Treat the Lite boards as ~150 A-per-motor hardware even in dual housings; `lekrsu`’s reminders keep traction upgrades realistic until you step up to full-size Spintend or 3Shul stages.[^lite-phase-cap]
- Keep regen conservative.
  - match battery regen amps to pack capacity, disable traction-control modes on single-motor builds, and check faults via USB before power-cycling if Bluetooth is absent.[^8][^9][^10]
- Plan accessories around the power rails you actually have: the dual exposes cruise/lighting outputs and a 12 V rail, but the single requires external buck converters and careful ADC board wiring.[^11][^12][^13][^14]
- Expect shipping delays without premium couriers; EU buyers still face VAT unless orders route through AliExpress IOSS or arrive mis-declared, so document deliveries for smoother RMAs.[^15][^16][^17]
- Synchronise controller power-ups before linking CAN and budget an external BLE bridge for singles.
  - the current batches still ship without Bluetooth and can pop transceivers if one side wakes late.[^can-cite][^single-ble]
- Treat the built-in alarm as a failsafe only: if the remote misses handshake at boot the Ubox will scream while still energising the hub, so wire brake interlocks or auxiliary sirens for theft deterrence.[^ubox-alarm]
- Spintend’s refreshed 12‑FET (85 V/240 A) board simply doubles the proven 6‑FET layout, so budget ≈26 kW practical ceiling and plan to buy through trusted resellers like James Soderstrom to skip month-long factory queues.[^138]

## Pre-Delivery QC & Bench Setup

1. **Full Disassembly:** Crack the enclosure to inspect for solder balls, missing hardware, or flux residue before the first power-on.
  - multiple riders received “sealed” units with conductive debris or missing faceplate screws.[^1][^2]
2. **Tear down second-hand singles.** Used single-channel Uboxes have surfaced with loose solder balls, uneven MOSFET pad contact, and even the case cutting through silicone on a phase lead, so clean, re-insulate, and reassemble before trusting a pre-owned unit.[^1]
3. **Document Everything:** Photograph the internals and keep serials handy; Spintend has honoured RMAs after fires and board failures when owners supplied teardown evidence.[^18]
4. **Note hardware revisions:** Production singles now ship with extra silicone pads, tidier layouts, and easier-to-service connectors compared with beta boards.
  - still verify pinouts before repurposing older harnesses so refreshed logic stages aren’t back-powered.[^single-rev]
5. **Bench Rules:** Wire the entire harness before energising, precharge ≥20 S packs, discharge bus caps after unplugging, keep ADC inputs ≤3.3 V, and eliminate ground loops to avoid repeat STM32 deaths.[^3]
6. **Skip USB-only power.** Powering a Ubox over USB-C without the main pack has triggered destructive ground loops.
  - stick to Bluetooth/Wi‑Fi for configuration unless the controller is fully energised and sharing the same ground.[^2]
7. **Initial Power Tests:** Bring the controller up on a fused bench supply with the BMS discharge FET enabled; if regen previously latched undervoltage faults, confirm the pack’s protection MOSFETs are awake before running detection.[^19]
8. **Detection housekeeping:** Enable the phase-filter checkbox only during motor detection—leaving it on while riding reintroduces noise and ABS overcurrent faults.[^phase-filter]
9. **Screen current-sense offsets:** Before installing, power each single on the bench and confirm the current-sense op-amps report sane offsets (hundreds of counts, not 30 or 4,000); multiple “new” boards arrived with shorted amplifiers that later blew input capacitors and XT60s under normal reconnects.[^offset-screening]
10. **Log the hardware revision.** The latest single board swaps to an aluminium PCB with G015N10 MOSFETs.
  - stick with the matching gate network instead of random FET swaps or you’ll destabilise the driver.[^g015n10]
11. **Document standby draw and LED behaviour.** Expect roughly 20 mA idle consumption with the latching button off; any illuminated switch LED indicates wiring backfeeding the logic rail and needs chasing before sealing the deck.[^3]
2. **Document Everything:** Photograph the internals and keep serials handy; Spintend has honoured RMAs after fires and board failures when owners supplied teardown evidence.[^18]
3. **Note hardware revisions:** Production singles now ship with extra silicone pads, tidier layouts, and easier-to-service connectors compared with beta boards.
  - still verify pinouts before repurposing older harnesses so refreshed logic stages aren’t back-powered.[^single-rev]
- Artem paused the 100 V single rollout to swap a flawed brass heat spreader for copper and is consulting on bare aluminum casings with better thermal flow, so expect improved cooling but longer lead times on the next batch.[^4][^5]
4. **Bench Rules:** Wire the entire harness before energising, precharge ≥20 S packs, discharge bus caps after unplugging, keep ADC inputs ≤3.3 V, and eliminate ground loops to avoid repeat STM32 deaths.[^3]

- Skip “quick taps” on bare QS8s.
  - without an anti-spark or precharge lead the inrush still arcs across the capacitor bank. Builders even disable BMS discharge first, yet sporadic flashes persist, so document a consistent connect/disconnect sequence for every build.[^qs8_arcing]
4. **Initial Power Tests:** Bring the controller up on a fused bench supply with the BMS discharge FET enabled; if regen previously latched undervoltage faults, confirm the pack’s protection MOSFETs are awake before running detection.[^19]
5. **Detection housekeeping:** Enable the phase-filter checkbox only during motor detection—leaving it on while riding reintroduces noise and ABS overcurrent faults.[^phase-filter]
6. **Reset hall handoff targets if launches shudder.** Lower hall interpolation toward ~300 eRPM, force sensorless to ~400 eRPM, recalibrate PID offsets, and try the “natural” throttle map before re-running geared drivetrains that stumble off the line.[^6]
7. **Screen current-sense offsets:** Before installing, power each single on the bench and confirm the current-sense op-amps report sane offsets (hundreds of counts, not 30 or 4,000); multiple “new” boards arrived with shorted amplifiers that later blew input capacitors and XT60s under normal reconnects.[^offset-screening]
8. **Log the hardware revision.** The latest single board swaps to an aluminium PCB with G015N10 MOSFETs.
  - stick with the matching gate network instead of random FET swaps or you’ll destabilise the driver.[^g015n10]

## Thermal Management & Mounting

- **Firmware Limits:** Stock firmware starts derating around 75–85 °C and shuts down near 100 °C, so increase cutbacks only after verifying thermistor calibration.[^4]
- **Legacy V1 vs. early V2 thermals:** The “def edition” V1 hardware runs cooler than early V2 betas in the same scooter, yet Paolo notes resin-encapsulated MOSFETs still bottleneck heat transfer because only thin PCB copper touches the case.
  - unlike Little FOCer or Tronic designs that clamp straight to the FET tab
  - and handheld IR guns under-read junction temps unless you expose the FETs or use a pro camera.[^7][^8]
- **Interface Upgrades:** Replacing spongy pads with copper shims or thicker (≈1 mm) thermal sheets plus quality paste dropped MOSFET temps 15–20 °C during 100–140 A runs when the case was clamped directly to the deck.[^5][^6]
- **Pad compression matters on singles.** Riders pegged 65–75 °C MOSFET temps at only 50–60 A battery until they replaced the factory 0.5 mm pads with stiffer 1 mm material or swapped cases to improve clamp pressure, and thicker Thermal Grizzly stacks cut peaks from ~67 °C at 45 A/110 A to ≈61 °C at 50 A/130 A while enabling 150 A launches without errors.[^single-pad]
- **Pick proven interface consumables.** Builders chasing tighter pad stacks favour 13 W/mK Iceberg silicone pads, budget GD900 paste, and thin adhesive thermal tapes to mate the baseplate to the deck once stock pads are missing or contaminated.
  - cheap office foam simply insulates the controller.[^9]
- **Airflow & Deck Prep:** Add 40–90 mm 12 W fans between stacked boards, cut intake/exhaust slots in the deck, sand paint off mounting faces, and clamp copper bars or aluminium spreaders to the case with quality paste when regen pushes single-Ubox stacks past 65–70 °C.[^7]
- **Strip insulating layers before sealing.** Support now recommends peeling heat-shrink from the MOSFET bank, sanding paint off decks, adding stick-on sinks, and even packing thermal paste/grease baths when enclosures must stay sealed to pull more heat into the chassis.[^single-pad]
- **Orientation affects cooling.** Mount the enclosure upside down so the MOSFET half of the split case sits against metal.
  - otherwise the transistor side cooks while the logic half stays cool.[^single-orientation]
- **Deck coupling experiments.** Happy Giraffe’s logs show 110 A phase launches dropping from 68 °C to the mid-40s once the case was bolted directly to bare metal or tied into copper heat pipes, while exposed boards on 1 cm aluminium slabs shed heat rapidly if you insulate the logic section against shorts.[^single-heatpipes]
- **Spot hardware differences by voltage class.** Early 75 V betas shipped with exposed copper busbars while some 100 V batches hid higher-Rds(on) FETs under resin and even arrived with loose solder balls.
  - open every case and plan extra heatsinking or thicker housings if you draw a resin-packed revision.[^10]
- **Short-term overcurrent mods:** Artem’s 19 S experiment sanded paint from the lid, added a 3 mm copper block, drilled vent holes for a fan, or even relocated the controller outside the deck.
  - treat these as temporary measures before detuning currents for daily use.[^11]
- **Cap endurance currents until cooling is upgraded.** Noname’s 100-mile single-Ubox commute stays below 45 °C by capping phase around 80 A and battery draw near 155 A while he prototypes larger heatsinks and even water-cooling before raising limits.
  - treat thermal headroom as the gating factor, not just MOSFET specs.[^12]
- **Document Lite belly-plate mounting.** Finn keeps Ubox Lite temps under 50 °C at 160 A phase / 90 A battery by replacing stock pads with Arctic MX4 and bolting the controller through its M2 bosses into a 3 mm aluminium belly plate.
  - treat it as the baseline for compact frames.[^13]
- **Water-cooling option:** Matthew’s custom water-cooled base plate on a 100/100 drops FET temps from ~54 °C back to ~40 °C within a minute during 35 °C ambient pulls at 130 A phase.
  - proof that external radiators can rescue commuters stuck with minimal deck airflow.[^14]
- **Mock up MP2 decks before ordering parts.** Patrick is printing a custom heatsink so an uncased 85/240 (≈40 mm tall plus an 8 mm fin stack) fits inside an MP2 Pro 2; he’ll road-test a 150 A layout with a 17×4 delta motor before adding an external 20 S 2 P booster once clearances check out.[^mp2_pro2]
- **Thunder 2 dual-G300 cooling.** JPPL and Shlomozero are 3D-printing radiator mounts, polishing aluminium plates, and reusing dead 75200 fins to bolt heatsinks onto Thunder 2 dual-controller installs—share STL files and insulation checks so others can replicate the cooling stack safely.[^thunder_heatsink]
- **Template custom fins before cutting metal.** After burning multiple 85/250 controllers on his Wepoor, Haku is mocking up aluminium fin stacks, mounting strips, and potential CNC runs so the 12‑FET stage finally has dedicated airflow and mechanical reinforcement inside the deck.[^wepoor_fins]
- **Expected Benchmarks:** Well-mounted duals have logged ~100 A battery / 130 A phase at ≈45 °C, while poor contact in sealed Weped decks let cases soar to 80 °C during 500 A combined pulls.
  - plan extra cooling above those loads. Square-wave Zero 11X controllers still out-launch under-cooled 60 V Ubox setups until phase limits rise and airflow improves, underscoring the need for fans in cramped decks.[^6][^20][^zero-launch]
- **Strip paint before mounting enclosures.** GT-series decks that mount Ubox Lite/MP2 controllers against painted steel trap heat.
  - grind to bare metal, add thermal glue or pads, and avoid single PETG brackets that leave cases at ~64 °C under load.[^15]
- **Plan hardware for earless cases.** 85/240 housings still ship without mounting ears and rely on tiny M2.5 hardware, so riders print brackets, retap threads, or glue adapters before long-travel suspensions knock under-deck mounts loose; ’lekrsu even 3D-printed a charger-mount adapter and slipped a 0.5 mm thermal pad under the Lite case when bolts were scarce.[^31][^lite_mount]
- **Skip silicone potting.** Rob Ver now seals controllers with covers and perimeter silicone instead of insulation gel because potted boards become impossible to service once a MOSFET fails.[^no_potting]
- **Repurpose retired baseplates.** Builders are bolting dead 75/200 heatsinks under live controllers.
  - stacking aluminium shims and thin pads or even radiators tied into Dualtron side plates
  - to add surface area without redesigning the deck.[^baseplate_spreader]
- **Use the 85240 passthroughs carefully.** The case exposes top-exit slots for phase leads; reroute wiring through them only after shielding the foam insulation pads so they do not tear or short against the enclosure.[^85240_passthrough]

## Power Limits, Regen & Current Planning

- **Current Envelope:** Treat 120–130 A phase per motor (≈160 A ABS max) as the practical ceiling for daily dual setups; sensor stutter above ~85 A usually signals failed MOSFETs or loose leads, not tuneable instability.[^21]
- **Single 85/200 field log:** A well-mounted aluminium single held 100 A battery, 200 A phase, and 60–70 A field-weakening on a 20 S MXUS bike without rising above ambient when bonded to a 20 mm baseplate.
  - proof the compact case works if you clamp it properly.[^16]
- **Stock guardrails:** Community logs keep single 100/100 controllers near 130 A phase and factory 85150 hardware near 220 A phase unless silicon and cooling are upgraded.
  - expecting more without rework simply burns MOSFETs.[^phase_guardrail]
- **Smart Repair’s 85 250/240 baseline:** The latest field comparisons cap customer tunes around 200 A battery, 380 A phase, and 480 A absolute once decks are stripped to bare metal and backed with extra thermal mass; skipping the prep still cooks controllers at those numbers.[^85250_envelope]
- **Single 100/100 baselines:** Lonnyo 65 H commuters now hover around 130–135 A phase, 85–90 A battery, and 150–180 A absolute on single Ubox 100/100 stacks, trimming duty to 98 % and kicking in FW around 88 % to eliminate stutter before heat creeps past 40 °C.[^u100_daily]
- **Regen Discipline:** Bench testing shows that even –5 A battery regen can trip controllers on unloaded wheels; cap regen amps to roughly the pack’s amp-hour rating plus a small overhead so the FETs absorb the excess.[^8]
- **Raise Absolute Max when faults persist.** Dual 100/100 owners clearing 200 A overcurrent faults in VESC Tool Mobile now toggle inactivity shutdown (App Config → General) and bump `ABS Max Current` above their commanded peak once wiring checks out.[^17]
- **High-Voltage Safeguards:** Dual owners run ~2×135 A phase / 2×71 A battery within 70 °C so long as regen stays off during full-charge launches and higher-voltage packs (17 S+) are bled a few percent before re-enabling braking.[^22]
- **Respect the 17 S ceiling:** Spintend support calls 17 S the safe maximum.
  - with regen disabled
  - and warns that 18 S attempts have repeatedly failed despite isolated success stories.[^18]
- **Single-case cooling reality:** The single board still bolts MOSFETs to the removable lid, so plan auxiliary heatsinks or step up to dual-channel housings if you need more than ~30 A continuous or 100 A peaks.[^19]
- **22 S experiments demand regen discipline.** Builders chasing 22 S/150 A tunes on 85/150 hardware disable regen or upgrade MOSFETs and capacitor banks; Smart Repair confirmed stock silicon only survives 22 S when braking stays mechanical, and veterans point voltage-hungry riders toward Rage Mechanics’ C350 once 30 S capability is mandatory.[^22s_mod]
- **Know the Ubox 100/100 envelope.** Smart Repair still caps the single at 22 S with regen disabled on the e-brake input; it ships at 135 A phase / 180 A absolute without ST-Link pads or beefy 12 V rails, so budget external regulation for accessories.[^u100-guardrails]
- **Preserve bulk capacitance when downsizing.** Deck-limited MKS 84200HP installs still need ≥2,800 µF on the DC link.
  - catalog compact capacitor options and mounting strategies before trimming the bank just to make the enclosure fit.[^20]
- **Current sharing proof point.** Dual builds have logged 180 A phase / 130 A battery on the rear and 150 A/90 A up front while holding FETs near 39 °C when pads are clamped flat.
  - use these as sanity checks that your thermal stack-up is working.[^dual-current]
- **Trace survival limit.** Field logs show 220–250 A bursts still blowing dual-Ubox traces even after copper-block and fan mods, so cap sustained pulls nearer 200 A per channel and prioritise airflow or external mounting before chasing higher duty cycles.[^21][^22]
- **ABS still clamps 100 V duals.** Rosheee’s 115 km/h logs show the 100 V uBox trips ABS overcurrent near ~140 A absolute, even when Daly packs stay happy.
  - expect firmware protection to cut power at high ERPM and plan current headroom accordingly.[^23]
- **Stock Kaabo packs sag hard under duals.** Twin controllers capped at 120 A battery still spiked to ~150 A and pulled 15 V from the factory 16 S pack, reinforcing the need for sturdier cells and connectors before chasing 6 kW+ on OEM batteries.[^24]
- **Duty & Field Weakening:** Keep field-weakening reserved for cooled builds; previous fires stemmed from wizard runs on fresh installs, so validate base detection and duty-cycle ramps before layering FW or traction aids.[^18][^23]
- **Kelly migration playbook:** Rosheee’s move to Kelly KLS7230 controllers demanded 0 AWG QS10 connectors, dual-to-single phase splices, and TIG-welded terminations to handle the paired phase leads each motor expects.
  - budget time and tooling before abandoning VESC hardware for Kelly stacks.[^25][^26]
- **Dual-bridge loads mirror across controllers.** Smart Repair’s GT1 build logs 170 A battery / 250 A phase on the rear Ubox 250 and 170 A battery / 120 A phase on the front Ubox 150; because the Spintend bridge mirrors battery amps to both ESCs he expects the smaller controller to overheat unless gearing or traction control sheds load.
  - disable the phase filter after motor detection and watch the front hub temps when mixing dissimilar hardware.[^27]
- **Voyage-displayed ABS OCP faults still demand VESC Tool checks.** Arnau’s new 85 V/150 A unit threw ABS overcurrent alarms immediately until Jason suggested connecting over USB to inspect the absolute-current ceiling; treat third-party displays as status indicators, not diagnostic replacements.[^28]
- **Document fresh warranty cases.** Franchesco’s 85 V/250 A flashed internally within metres on a 20 S 42 Ah Molicel pack tuned for 150 A battery / 250 A phase (350 A absolute); the community urged him to collect MOSFET photos and avoid reapplying power until Spintend responds.[^29]
- **Expect commuter hubs to need more current.** Maike-branded “3000 W” dual hubs stayed near 25 km/h until motor current climbed toward 140 A (≈70 A battery) and the owner improved thermal coupling with frame-mounted pads or fans.
  - stock 16 S packs with dual XT60s still bottleneck upgrades.[^30]

## Controls, Accessories & IO

- **Harness staging:** JPPL is finishing a “medium” plug-and-play loom that feeds dual Thor 300 controllers with shared 12 V accessories, VESC Express telemetry, lighting, horn, and Spintend power buttons—built for ≤300 A phase 20 S setups so dual-drive owners can wire once and focus on tuning.[^thor_harness]
- **Remote & Cruise:** The bundled 2.4 GHz remote offers cruise, horn, and light controls via the receiver, reducing parallel looms compared with bare PPM throttles.[^11]
- **CNC throttle status:** Early production CNC throttles cleared tolerance checks and will ship once the final countersunk hardware arrives, with anodised and black batches staged after QC approves the mounting kit.[^31]
- **Cruise troubleshooting:** If the remote beeps but never holds speed, confirm the PPM switch channel toggles in VESC Tool, match firmware between paired controllers, and ensure the accessory rail stays above 5 V when cruise engages.[^32]
- **Brake Inputs:** The ADC daughterboard supports normally-open/closed levers and selectable 5 V or 3.3 V rails.
  - set the switches before plugging Magura/Shimano sensors to avoid shorting hall supplies.[^13]
- **Dial torque sensors with the trim pot.** Builders tweak ADC v1 trim pots until torque-sensor outputs sit near 3.3 V so the VESC can blend torque and thumb throttles without runaway or dead zones on 21 S frames.[^33]
- **Use pre-crimped signal jumpers.** Refreshed harnesses switch to GH1.25 signal plugs; pre-crimped jumpers beat DIY crimping when adding CAN bridges or button pods to the newer looms.[^17]
- **Lighting Power:** Dual controllers expose a ≈1.5 A 12 V rail for lighting relays, but singles lack this output; budget fused DC-DC converters instead of stealing from the fan header.[^12][^14]
- **Harness power sharing:** Rosheee now feeds a pair of Rion controllers from the dual-Ubox harness with twin 20 S 7 P packs, underscoring the need to balance precharge and connector sizing when mixing controller families on one scooter.[^34]
- **Adapter V2 shortcuts:** Hold the left brake and throttle during boot to toggle the built-in “power limit” scaler; the board beeps for restricted/unrestricted confirmation, supports mixed hall + switch brake inputs for lighting, yet still can’t enforce a hard 25 km/h cap on the road.[^adapter_v2]
- **Remember to switch the app to ADC.** Multimeter tests show throttle voltage on the adapter even when VESC Tool ignores it—set the input mode to ADC before tearing the loom apart.[^adapter_mode]
- **ADC lighting headroom:** The adapter already flashes LED strips for turn indicators, so custom amber side strips mostly need channel routing rather than bespoke firmware.
  - just stay within the ≈3 A rail and isolate heavier lamps on an external converter.[^adc_lighting]
- **Follow the factory wiring map.** One owner cleared stuck buttons only after repinning the ADC lighting board to match Spintend’s published diagram, a reminder to verify loom order before chasing firmware ghosts.[^adc_wiring]
- **Blinker channel limits:** Sequential LED strips cannot share the blinker output without extra logic, so some builders rewire lighting looms from scratch to keep the adapter’s tiny signal wires safe.[^sequential_led]
- **Dualtron LED adapters:** Mario-supplied Dualtron motors arrive with only two wires for decorative LEDs, so installers must adapt the factory three-wire harness if they expect OEM-style lighting behaviour.[^dualtron_leds]
- **Spin Y-2 throttle checklist:** Batch-two throttles still leave the factory without calibration on occasion.
  - verify which ADC port is populated (older looms expect ADC2, current harnesses ship pinned for ADC3), remap the side buttons before adding regen or lighting loads, keep phase leads equal-length when shortening looms, and log a pre/post-calibration throttle curve so customer bikes ship with crisp response when wired directly to the ESC instead of detouring through displays.[^35][^36]
- **Single-button wake behaviour:** Leave the dual-controller interconnect in place when wiring a shared latching switch.
  - the harness will power both 100 V/100 A units together, while unplugging it isolates a controller for diagnostics but prevents one-button wake-ups.[^dual_switch]
- **Horn channel expectations:** The horn terminal happily drives compact 12 V siren boards (e.g., GREATZT QSI-4840); riders trim the plastic shell to a ≈30 × 20 mm module and mount it behind the dash so the alarm wakes with the scooter instead of relying on battery-powered noisemakers.[^horn-siren]
- **CAN & Anti-Slip:** Updated harnesses let one single wake another over CAN, yet anti-slip belongs on dual configurations.
  - leaving it active on a solo motor causes low-speed cut-outs with red/green blink codes.[^10][^24]
- **Bench-start requirements:** Ubox 100/100 controllers refuse to boot from USB-C alone.
  - wire the latching 16 mm start button or a proper low-voltage switch instead of relying on the BMS as a master disconnect.[^start-button]
- **Secure the ADC switches.** Warranty cleanups now include removing stray solder balls, upgrading to 1 mm pads before reassembly, and gluing the ADC adapter’s slide switch in the 5 V position to stop intermittent throttle brownouts.[^adc-service]
- **SmartDisplay ecosystem:** NFC-enabled Zero-style throttles with UART RFID drop into VSETT looms and pair cleanly with SmartDisplay pass-through; CAN “police mode” presets remain in test, aiming to mute the front motor while leaving rear torque for roadside compliance.[^nfc-throttle][^police-mode]

## Pending Field Reports

- Verify whether Arnau’s warranty replacement survives 20 S with regen enabled and note any differences Franchesco reports between the legacy and compact 85/250 housings before updating the reliability guidance.[^arnau-warranty]
- Gather Finn’s long-term data on the 85/150 beta boards—cooling with 3 mm baseplates, external heatsinks, and safe current ceilings—before recommending those revisions for production builds.[^finn-beta]

## Firmware, Logging & Fault Recovery

- **Version Discipline:** Stick with Spintend’s vetted firmware packages (e.g., 100 A battery limit files) unless you have cooling to exploit the 300 A hardware bins; mismatched binaries raise noise and reliability issues.[^25]
- **Heed support’s 5.3 guidance:** Spintend is still telling riders to remain on 5.2 until its customised 5.3 binaries finish soak testing, so archive configs and be ready for SWD recovery before flashing betas.[^fw53_support]
- **Expect V2 logic tweaks.** The latest single boards add self-resetting fuses on every 5 V/12 V/3.3 V rail, but the ADC daughterboard still faults when 5 V throttles hit the 3.3 V MCU input and VESC Tool 3.01 crashes during calibration.
  - stick with Tool 3.00/firmware 5.2 until Spintend issues patched binaries.[^adc-v2]
- **Red USB-C fix:** A FW 5.3 regression misreported pack voltage on red USB-C duals.
  - flash Artem’s corrected `VESC_UBOX_75_100_TYPEC_R2_3.3V_100A_FW5.3.bin`, then wait 5–8 s after boot before reconnecting VESC Tool or you’ll chase phantom disconnections.[^fw53-red-usbc]
- **Purple USB-C handshake:** Purple shells often reconnect after reseating the USB-C lead and giving the controller several seconds to finish booting; keep 5.2 firmware handy before escalating to ST-Link recovery.[^37]
- **SWD rescue path:** When USB flashing still fails, pop the lid, clip onto the SWD header (reset pin unused), and confirm the N1/N2 LEDs stay lit before reflashing bootloader and firmware; a dark pair points to a dead STM32 that needs replacement.[^swd-led-check]
- **Dual-Ubox recovery workflow:** Dead ESCBs have come back by bridging CAN to the healthy controller’s SWD pads, flashing over the bundled four-pin CAN lead, and confirming 3.3 V throttle wiring before escalation.
  - Windows STM32 drivers remain mandatory for the rescue.[^38][^39]
- **Mxlemming observer wins on GT2 hubs.** Ubox V2 running firmware 6.0 held steady torque and near-lab voltage readings on Segway GT2 hubs after the detection wizard auto-switched to the Mxlemming observer with lambda compensation.
  - log the before/after traces whenever you swap observers.[^40]
- **6.05 fixes configuration resets.** Spintend replaced a dual 75100 stack that blew its capacitors at 72 V/150 A BMS load and shipped matching firmware/app 6.05 updates.
  - owners report the refresh stopped random configuration resets and left the scooter running smoother than before.[^41][^42]
- **Unofficial 300 A bins:** Community Micro-USB and USB‑C binaries lift the single’s 100 A factory ceiling to 300 A but void warranty.
  - install only if you have the airflow, copper interfaces, and logs to prove the MOSFETs survive the extra load.[^43][^44]
- **Hardware voltage ceilings linger.** Some 85/250 pairs still trip an 82 V hard cap even after raising software limits; flashing the vendor `no_hw_limit.bin` clears the baked-in ceiling for 92 V packs before you chase higher charge voltages.[^45]
- **Reconfirm voltage limits after updates.** A single Ubox 80 threw over-voltage faults on 6.05 firmware until the battery max input was reset.
  - the no-limit firmware alone was not enough, so double-check pack settings whenever you flash new builds.[^46]
- **Document the “no hardware limits” flash.** Ubox 100/100 Lite owners are leaning on Vedder’s 6.05 binary that removes the 135 A phase clamp.
  - capture the firmware link, proven 170 A phase / 150 A battery logs, and the thermal caveats before anyone flashes blind or tries the mobile workflow mid-ride.[^47][^48]
- **BLE Options:** Official BLE dongles arrive pre-flashed and tax-paid via AliExpress, while DIY NRF boards need extra programming; keep at least one link for live tuning even if you prefer wired sessions.[^26]
- **Built-in Bluetooth range.** Production singles that ship with the integrated BLE module keep telemetry stable for roughly 50 m line-of-sight.
  - enough to cover pits without external antennas.[^49]
- **NRF quick-start:** When the NRF header is the only free UART, flash a generic NRF51 via USB, solder it to the dedicated header, and power-cycle to pair.
  - no need to steal the ADC adapter’s UART pads.[^50]
- **Fault Retrieval:** If Bluetooth is absent, the controller retains the last fault until shutdown—connect via USB before cycling power so valuable diagnostics aren’t lost.[^10]

## Known Field Failures & Mitigations

- **Continuity-check every harness.** A v2 80 V single shipped with its Bluetooth lead reversed and killed the module immediately.
  - probe polarity and confirm JST orientation before first power to avoid sacrificial electronics.[^27]
- **Investigate surging with hardware checks first.** Sudden sensorless surges or oscillations usually trace back to loose phase plugs or damaged harnesses.
  - share CSV logs and tug-test connectors before blaming firmware.[^sensorless-harness]
- **0.6 V on SWD VCC means the MCU is done.** Support issued RMAs as soon as the SWD header only showed ~0.6 V instead of 3.3 V; treat sub-1 V readings as proof the logic stage needs factory service, not more bench work.[^swd_vcc]
- **Diagnose ADC adapters before blaming firmware.** VSETT 11+ owners logged CAN dropouts, stuck brake beeps, and latched brake inputs when ADC V2 boards half-failed after 6.0 updates; reflash, reseat grounds, and isolate the adapter before pursuing RMAs.[^28]
- **Keep throttles on the 3.3 V rail and mount adapters close.** Routing halls through 5 V accessory pins or long unshielded runs has blown STM32 inputs; park the ADC board beside the controller, use divider networks, and rely on Vedder’s detach timeout to hand control back to hardware cleanly.[^29]
- **Treat thermal spikes as potential moisture ingress.** Riders seeing 190 °C MOSFET readings traced the fault to condensation inside the case.
  - warm the enclosure, dry the PCB, and reseal gaskets before raising firmware cutoffs.[^30]
- **Power both controllers before linking CAN.** Rowan’s 4WD scooter blew a CAN transceiver and a power switch when one Ubox woke late.
  - sync power buttons or isolate the bus before hot-plugging.[^can-cite]

## Logistics & Support Notes

- **Warranty Responsiveness:** Spintend has replaced fire-damaged units and keeps spare power/logic boards on hand, which contrasts with poorer experiences on competing FlipSky hardware.[^18]
- **Shipping Choices:** Direct orders sometimes arrive underdeclared (sub-$30) and dodge VAT, but DHL eCommerce frequently delays or loses parcels; veterans now pay for FedEx or AliExpress Standard to avoid customs limbo.[^15][^16]
- **EU VAT reality:** Accessories still ship without prepaid VAT, leaving riders with €30 import bills on €20 parts; lobby Spintend for IOSS handling or bake the extra cost into quotes for EU customers.[^51]
- **Document capacitor failures.** DHL eCommerce returns have taken five weeks and multiple single-Ubox RMAs cite repeat capacitor blowouts; paying for FedEx and filming unboxings gives leverage when escalating support tickets.[^52]
- **EU VAT Planning:** Accessories shipped without prepaid VAT trigger €30 fees on €20 parts—push for IOSS channels or budget the surcharge when ordering spares.[^17]
- **US distribution hub.** Recent 85/240 batches now ship from a New Jersey warehouse, and sub-$1,000 orders have cleared without added tariffs, cutting replacement lead times for North American riders.[^32]
- **AliExpress IOSS shift.** Expect 21–24 % VAT to be collected upfront on AliExpress, but the move eliminates the €10–€24 postal handling fees that used to ambush EU deliveries.[^ioss-update]
- **Integrated BMS watch.** Builders are lobbying Spintend for an in-house BMS after comparing Daly’s slim 120 A boards with ANT’s bulkier smart units.
  - deck space under 25 mm is still precious.[^bms-lobby]
- **Ubox Pro horizon.** Spintend’s Pro variant is in final 100 V testing, but veterans plan to tear down every unit for stray solder or debris after finding contamination in earlier runs.[^53][^54]

## Wheel & Brake Fitment Notes

- Detachable 110 mm Spintend rims seat 13×5.00-6.5 tyres cleanly, but the 7"-wide 7260R tread still lacks compatible shells. Hope Tech GR4 calipers clear 3 mm rotors, yet most owners stick with 160 mm discs around 2.7–3 mm thick to preserve clearance and keep a single spare rotor size on hand.[^rim_fitment]

## Source Notes

[^1]: Controllers routinely arrive with debris; open and inspect before powering up.[^55]
[^2]: Replacement units have shipped missing screws or with solder splatter, reinforcing the teardown-first habit.[^56][^57]
[^3]: Seven golden rules for safe VESC power-up and wiring discipline.[^58]
[^4]: Default thermal derating and shutdown thresholds for Ubox firmware.[^59]
[^5]: Copper shims and improved interfaces cutting MOSFET temperature roughly 20 %.[^60]
[^6]: Pad compression tweaks keeping MOSFETs near 45 °C at ~100 A battery / 130 A phase, plus data on thicker stock pads in new harness revisions.[^61][^62]
[^single-pad]: Single-Ubox owners logged 65–75 °C MOSFETs at 50–60 A battery until they swapped the 0.5 mm factory pads for stiffer 1 mm interfaces, added stick-on sinks, sanded decks, packed thermal grease baths, or stepped up to Thermal Grizzly pads that dropped peaks from ~67 °C at 45 A/110 A to ≈61 °C at 50 A/130 A while enabling 150 A launches.[^63][^64][^65][^66][^67]
[^single-orientation]: Mounting the case upside down keeps the MOSFET side hard against the chassis; leaving it upright lets the logic half stay cool while the transistor bank overheats.[^68]
[^single-heatpipes]: Bolting the case straight to bare metal or tying it into copper heat pipes dropped MOSFET temps from ~68 °C to 25–44 °C at 110 A phase, and bare boards on 1 cm aluminium slabs shed heat quickly so long as every exposed trace is insulated.[^69][^70]
[^7]: Active cooling tactics for dual singles overheating under heavy regen, including 40–90 mm 12 W fans, deck venting, and copper bar clamps to improve case coupling.[^71][^44]
[^8]: Regen bench tests tripping controllers and the amp-hour-based cap guideline.[^72]
[^9]: Regen-to-capacity rule of thumb reiterated during community tuning sessions.[^73]
[^10]: Post-fault USB checks and anti-slip misconfiguration behaviour on single-motor builds.[^74]
[^11]: Remote-integrated cruise, horn, and lighting outputs reducing harness complexity.[^75][^76]
[^12]: Onboard 12 V rail capacity for accessories on dual controllers.[^77]
[^13]: ADC board switch options for Magura and Shimano brake sensors.[^78]
[^14]: Single-channel controllers lack a 12 V rail, necessitating external buck converters.[^79]
[^15]: Underdeclared parcels and bundled remote features noted in EU shipments.[^76]
[^16]: Courier reliability comparisons and RMA shipping delays via DHL eCommerce.[^80][^81]
[^17]: EU VAT frustrations and calls for IOSS handling on accessories.[^82]
[^18]: Warranty cases following catastrophic failures and continued community support.[^83][^84]
[^19]: Smart-BMS precharge and discharge FET requirements before successful motor detection.[^85]
[^20]: Thermal extremes logged on poorly mounted duals at ~500 A phase combined.[^86]
[^21]: Practical phase-current ceilings and fault symptoms at higher demand.[^87]
[^22]: Dual 135 A phase / 71 A battery operating envelope and regen cautions on 17 S packs.[^88]
[^22s_mod]: Source: knowledge/notes/input_part011_review.md†L525-L526
[^23]: Early fire incidents during detection runs and the caution to validate baseline tuning before advanced features.[^83]
[^mini_cap]: haku and Yamal capped dual mini Spintend stacks near 200 A battery (≈300 A phase) per motor after 500 A pushes tripped protections despite cool case temperatures.[^90]
[^connector_plan]: Yamal is pairing 8 mm Amass bullets with Juliet signal connectors while wiring his dual-controller builds, giving a tidy shared CAN/power loom for 80 H projects.[^91]
[^baseplate_spreader]: JPPL and Shlomozero are reusing dead 75/200 baseplates as auxiliary heatsinks, stacking aluminium spacers and pad layers or bolting radiator blocks into Dualtron side plates for extra surface area.[^92]
[^85240_passthrough]: Source: knowledge/notes/input_part011_review.md†L530-L530
  - builders reroute wiring through them only after protecting the foam insulation pads.[^93]
[^thor_harness]: Source: knowledge/notes/input_part011_review.md†L529-L529
[^mp2_pro2]: Source: knowledge/notes/input_part011_review.md†L551-L552
[^wepoor_fins]: Source: knowledge/notes/input_part011_review.md†L683-L684
[^thunder_heatsink]: Source: data/vesc_help_group/text_slices/input_part011.txt, L20246 to L20261
[^24]: CAN wake wiring updates and anti-slip recommendations for multi-controller builds.[^62][^94]
[^25]: Official firmware packages with 100 A vs. 300 A limits and the need for matching cooling.[^95]
[^fw53_support]: Spintend support is still advising riders to hold on firmware 5.2 until its customised 5.3 binaries complete soak testing, so only flash the betas if you can recover from detection failures.[^96]
[^adc-v2]: V2 singles now ship with self-resetting fuses on every 5 V/12 V/3.3 V rail, yet the ADC loop still faults if a 5 V throttle feeds the 3.3 V MCU input and VESC Tool 3.01 crashes during calibration, so builders roll back to Tool 3.00 on firmware 5.2 until fixes land.[^97]
[^sensorless-harness]: Sensorless surging and runaway pulses have repeatedly traced back to loose phase connectors or damaged harnesses.
  - inspect hardware and share CSV logs before blaming firmware.[^98]
[^26]: BLE dongle sourcing and plug-and-play advantages over generic NRF boards.[^99]
[^27]: Harness polarity failure that destroyed a Bluetooth module on first power-up.[^100]
[^adc-service]: Warranty cleanups now pull stray solder balls, fit 1 mm pads before closing the case, and glue the ADC switch in the 5 V position to stop intermittent throttle failures.[^66][^101]
[^28]: ADC adapter V2 fault progression—CAN dropouts, brake beeps, and recovery workflow after firmware 6.0 updates.[^102]
[^29]: ADC placement, detach-timeout behaviour, and the 3.3 V throttle guidance preventing STM32 input failures.[^103][^104][^105]
[^30]: Moisture-driven MOSFET temperature spikes that vanished after warming and drying the enclosure.[^106]
[^31]: 85/240 mounting anecdotes covering custom brackets, retapped threads, and thermal pad tweaks to secure earless housings.[^107][^108][^109]
[^32]: Spintend 85/240 shipments now staging through a New Jersey hub for faster, low-tariff deliveries into the United States.[^110][^111]
[^g015n10]: New single-board revisions ship on aluminium PCBs with G015N10 MOSFET stacks and tuned gate networks.
  - stick with the factory parts instead of improvising swaps.[^112]
[^u100-guardrails]: Smart Repair reiterated that the Ubox 100/100 tops out at 22 S, ships with 135 A phase / 180 A absolute limits, and should keep regen off the e-brake path unless you’re ready to swap FETs; it also omits ST-Link pads and beefy 12 V rails compared with 85xxx units.[^113]
[^start-button]: The same teardown confirmed the 100/100 refuses to boot from USB-C.
  - wire the latching 16 mm start button or another 5 V trigger instead of depending on the BMS as a master switch.[^114]
[^zero-launch]: Stock Zero 11X square-wave controllers still beat 60 V Ubox launches until phase limits rise and airflow improves, making active cooling a prerequisite for parity.[^115]
[^single-rev]: Production single-channel Uboxes now include extra silicone pads and cleaner layouts compared with beta boards, but builders still verify harness pinouts before reuse to avoid damaging refreshed logic stages.[^116]
[^phase-filter]: Motor-wizard phase filters should be disabled after detection to avoid noise and ABS overcurrent faults on Spintend controllers.[^117]
[^arnau-warranty]: Pending confirmation that Arnau’s warranty replacement tolerates 20 S with regen and any differences between legacy versus compact 85/250 housings. Source: knowledge/notes/input_part011_review.md†L904-L904
[^finn-beta]: Awaiting Finn’s long-term 85/150 beta data on cooling mods and safe current ceilings before broad deployment. Source: knowledge/notes/input_part011_review.md†L908-L908
[^nfc-throttle]: NFC-enabled Zero-style throttles with UART RFID modules plug into VSETT harnesses and align with SmartDisplay pass-through plans.[^118]
[^police-mode]: CAN “police mode” presets are being prototyped so SmartDisplay buttons can disable the front motor while leaving rear torque for roadside checks.[^119]
[^ioss-update]: AliExpress’ IOSS rollout adds 21–24 % VAT upfront but removes the €10–€24 postal handling fees across much of the EU.[^120]
[^bms-lobby]: Riders are pressing Spintend for an integrated BMS after comparing Daly’s slimmer 120 A layout with ANT’s bulkier smart units and touch displays.[^121]
[^single-ble]: The single-channel Spintend still ships without Bluetooth modules, so riders rely on SmartDisplay pass-through or external dongles and power both controllers before plugging in CAN to avoid ground loops.[^122]
[^ubox-alarm]: Spintend bakes an alarm into the Ubox that sounds whenever the remote handshake fails at boot yet still allows the motors to drive, nudging builders toward physical interlocks for theft defence.[^123]
[^dual-current]: Riders logging simultaneous front/rear data on dual builds reported 180 A phase / 130 A battery rear and 150 A/90 A front at ≈39 °C MOSFETs when thermal pads were clamped properly.[^124]
[^horn-siren]: GREATZT QSI-4840 siren boards shrink to ≈30 × 20 mm once trimmed and tie directly into the horn output, giving 120–125 dB alerts without battery-powered accessories.[^125]
[^adapter_v2]: Adapter V2 adds a brake+throttle boot shortcut to scale throttle, audible feedback for restricted/unrestricted modes, and mixed hall/switch brake support, though it can’t enforce 25 km/h in real rides.[^126]
[^adapter_mode]: The adapter shows throttle voltage even when VESC Tool ignores it; switching the app to ADC restores control without rewiring.[^127]
[^swd_vcc]: Spintend support treats ~0.6 V on the SWD header as a dead MCU and authorised RMAs once logs confirmed the low voltage.[^128]
[^fw53-red-usbc]: Artem published a fixed FW 5.3 BIN for red USB-C Uboxes that restores accurate voltage telemetry and advised waiting 5–8 s after boot plus re-flashing both firmware and bootloader if disconnects persist.[^129][^130]
[^swd-led-check]: Community recovery threads now escalate to SWD flashing with the bundled CAN lead, verifying the N1/N2 LEDs stay lit while reflashing bootloader and firmware; dark LEDs usually confirm a dead STM32 that needs hardware replacement.[^131]
[^qs8_arcing]: Plugging Ubox controllers without QS8 anti-sparks still dumps inrush into capacitors even when builders disable the BMS discharge FET first.
  - document safe connect/disconnect sequences instead of “quick tapping” the connector.[^132]
[^adc_lighting]: The Spintend ADC board already drives LED strips for turn indicators, so custom amber lighting mainly needs channel routing while heavier loads move to an external converter.[^133]
[^adc_wiring]: Source: knowledge/notes/input_part012_review.md, line 434.
[^lite_mount]: Source: knowledge/notes/input_part012_review.md, lines 429 and 475.
[^no_potting]: Source: knowledge/notes/input_part012_review.md, line 488.
[^sequential_led]: Source: knowledge/notes/input_part012_review.md, line 491.
[^dualtron_leds]: Source: knowledge/notes/input_part012_review.md, line 492.
[^dual_switch]: Leaving the dual-controller interconnect cable in place lets a single latching switch wake both Spintend 100 V/100 A units; unplugging it isolates one controller but stops shared-button startups.[^134]
[^phase_guardrail]: Community tuning still caps Spintend 100/100 controllers near 130 A phase and stock 85150 hardware around 220 A phase unless silicon and cooling are upgraded.[^135]
[^85250_envelope]: Source: knowledge/notes/input_part013_review.md†L601-L601
[^rim_fitment]: Detachable 110 mm Spintend rims favour 13×5.00-6.5 tyres; Hope Tech GR4 calipers clear 3 mm rotors, but most owners stick with 160 mm, ≈2.7–3 mm discs to maintain clearance and common spares.[^136][^137]


## References

[^1]: Source: data/vesc_help_group/text_slices/input_part001.txt†L20826-L20905
[^2]: Source: data/vesc_help_group/text_slices/input_part001.txt†L20906-L20947
[^3]: Source: data/vesc_help_group/text_slices/input_part001.txt†L25713-L25761
[^single_proto]: Source: data/vesc_help_group/text_slices/input_part002.txt†L25558-L25571
[^brass_swap]: Source: data/vesc_help_group/text_slices/input_part002.txt†L25573-L25595
[^4]: Source: data/vesc_help_group/text_slices/input_part002.txt†L26880-L26918
[^5]: Source: data/vesc_help_group/text_slices/input_part002.txt†L26994-L27020
[^6]: Source: knowledge/notes/input_part004_review.md†L30-L30
[^7]: Source: data/vesc_help_group/text_slices/input_part002.txt†L9000-L9010
[^8]: Source: data/vesc_help_group/text_slices/input_part002.txt†L9408-L9446
[^9]: Source: knowledge/notes/input_part011_review.md†L107-L108
[^10]: Source: data/vesc_help_group/text_slices/input_part001.txt†L25795-L25855
[^11]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11156-L11164
[^12]: Source: knowledge/notes/input_part009_review.md†L301-L302
[^13]: Source: data/vesc_help_group/text_slices/input_part012.txt†L13678-L13718
[^14]: Source: knowledge/notes/input_part013_review.md†L390-L392
[^15]: Source: data/vesc_help_group/text_slices/input_part012.txt†L8651-L8673
[^16]: Source: knowledge/notes/input_part005_review.md†L217-L217
[^17]: Source: knowledge/notes/input_part005_review.md†L325-L327
[^18]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11165-L11186
[^19]: Source: data/vesc_help_group/text_slices/input_part002.txt†L9689-L9697
[^20]: Source: knowledge/notes/input_part013_review.md†L104-L104
[^21]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11588-L11605
[^22]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11633-L11670
[^23]: Source: knowledge/notes/input_part002_review.md†L493-L495
[^24]: Source: knowledge/notes/input_part002_review.md†L495-L505
[^25]: Source: data/vesc_help_group/text_slices/input_part002.txt†L27399-L27403
[^26]: Source: data/vesc_help_group/text_slices/input_part002.txt†L27429-L27488
[^27]: Source: knowledge/notes/input_part011_review.md†L123-L134
[^28]: Source: knowledge/notes/input_part011_review.md†L275-L279
[^29]: Source: knowledge/notes/input_part011_review.md†L418-L424
[^30]: Source: knowledge/notes/input_part004_review.md†L354-L354
[^31]: Source: data/vesc_help_group/text_slices/input_part002.txt†L27108-L27132
[^32]: Source: data/vesc_help_group/text_slices/input_part004.txt†L11970-L12020
[^33]: Source: knowledge/notes/input_part005_review.md†L241-L241
[^34]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11901-L11969
[^35]: Source: knowledge/notes/input_part014_review.md†L51-L52
[^36]: Source: data/vesc_help_group/text_slices/input_part014.txt†L7040-L7097
[^37]: Source: data/vesc_help_group/text_slices/input_part002.txt†L9986-L10030
[^38]: Source: data/vesc_help_group/text_slices/input_part002.txt†L27404-L27465
[^39]: Source: data/vesc_help_group/text_slices/input_part002.txt†L27466-L27508
[^40]: Source: data/vesc_help_group/text_slices/input_part004.txt†L4282-L4290
[^41]: Source: data/vesc_help_group/text_slices/input_part009.txt†L9910-L9928
[^42]: Source: data/vesc_help_group/text_slices/input_part009.txt†L10129-L10129
[^43]: Source: data/vesc_help_group/text_slices/input_part000.txt†L20181-L20187
[^44]: Source: data/vesc_help_group/text_slices/input_part000.txt†L20190-L20299
[^45]: Source: knowledge/notes/input_part011_review.md†L37-L38
[^46]: Source: knowledge/notes/input_part011_review.md†L53-L54
[^47]: Source: data/vesc_help_group/text_slices/input_part012.txt†L15090-L15106
[^48]: Source: data/vesc_help_group/text_slices/input_part012.txt†L15365-L15383
[^49]: Source: knowledge/notes/input_part005_review.md†L218-L218
[^50]: Source: data/vesc_help_group/text_slices/input_part004.txt†L8813-L8818
[^51]: Source: data/vesc_help_group/text_slices/input_part001.txt†L20979-L21033
[^52]: Source: data/vesc_help_group/text_slices/input_part000.txt†L20741-L20888
[^53]: Source: data/vesc_help_group/text_slices/input_part000.txt†L20490-L20506
[^54]: Source: data/vesc_help_group/text_slices/input_part000.txt†L20940-L20950
[^55]: Source: knowledge/notes/input_part000_review.md†L359-L359
[^56]: Source: knowledge/notes/input_part001_review.md†L119-L119
[^57]: Source: knowledge/notes/input_part001_review.md†L240-L240
[^58]: Source: knowledge/notes/input_part001_review.md†L463-L463
[^59]: Source: knowledge/notes/input_part000_review.md†L102-L102
[^60]: Source: knowledge/notes/input_part000_review.md†L129-L129
[^61]: Source: knowledge/notes/input_part000_review.md†L130-L130
[^62]: Source: knowledge/notes/input_part000_review.md†L583-L583
[^63]: Source: data/vesc_help_group/text_slices/input_part001.txt†L7354-L7531
[^64]: Source: data/vesc_help_group/text_slices/input_part001.txt†L7489-L7529
[^65]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8079-L8101
[^66]: Source: data/vesc_help_group/text_slices/input_part001.txt†L10015-L10090
[^67]: Source: data/vesc_help_group/text_slices/input_part001.txt†L10139-L10202
[^68]: Source: data/vesc_help_group/text_slices/input_part001.txt†L10273-L10314
[^69]: Source: data/vesc_help_group/text_slices/input_part001.txt†L9226-L9351
[^70]: Source: data/vesc_help_group/text_slices/input_part001.txt†L9333-L9348
[^71]: Source: knowledge/notes/input_part000_review.md†L475-L475
[^72]: Source: knowledge/notes/input_part000_review.md†L176-L177
[^73]: Source: knowledge/notes/input_part000_review.md†L177-L177
[^74]: Source: knowledge/notes/input_part000_review.md†L590-L591
[^75]: Source: knowledge/notes/input_part000_review.md†L110-L110
[^76]: Source: knowledge/notes/input_part000_review.md†L146-L146
[^77]: Source: knowledge/notes/input_part000_review.md†L687-L687
[^78]: Source: knowledge/notes/input_part000_review.md†L206-L206
[^79]: Source: knowledge/notes/input_part000_review.md†L460-L460
[^80]: Source: knowledge/notes/input_part000_review.md†L451-L451
[^81]: Source: knowledge/notes/input_part000_review.md†L485-L485
[^82]: Source: knowledge/notes/input_part001_review.md†L469-L469
[^83]: Source: knowledge/notes/input_part000_review.md†L62-L62
[^84]: Source: knowledge/notes/input_part000_review.md†L183-L183
[^85]: Source: knowledge/notes/input_part000_review.md†L168-L170
[^86]: Source: knowledge/notes/input_part000_review.md†L614-L614
[^87]: Source: knowledge/notes/input_part000_review.md†L662-L663
[^88]: Source: knowledge/notes/input_part001_review.md†L840-L840
[^89]: Source: knowledge/notes/input_part011_review.md†L524-L526
[^90]: Source: knowledge/notes/input_part011_review.md†L558-L559
[^91]: Source: knowledge/notes/input_part011_review.md†L589-L589
[^92]: Source: knowledge/notes/input_part011_review.md†L532-L534
[^93]: Source: knowledge/notes/input_part011_review.md†L530-L530
[^94]: Source: knowledge/notes/input_part000_review.md†L590-L590
[^95]: Source: knowledge/notes/input_part000_review.md†L42-L42
[^96]: Source: data/vesc_help_group/text_slices/input_part001.txt†L4000-L4052
[^97]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8424-L8453
[^98]: Source: data/vesc_help_group/text_slices/input_part001.txt†L3757-L3810
[^99]: Source: knowledge/notes/input_part001_review.md†L174-L174
[^100]: Source: knowledge/notes/input_part004_review.md†L287-L287
[^101]: Source: data/vesc_help_group/text_slices/input_part001.txt†L10139-L10343
[^102]: Source: knowledge/notes/input_part004_review.md†L351-L352
[^103]: Source: knowledge/notes/input_part004_review.md†L286-L286
[^104]: Source: knowledge/notes/input_part004_review.md†L18-L18
[^105]: Source: knowledge/notes/input_part004_review.md†L202-L202
[^106]: Source: knowledge/notes/input_part004_review.md†L474-L474
[^107]: Source: knowledge/notes/input_part012_review.md†L20537-L20541
[^108]: Source: knowledge/notes/input_part012_review.md†L20575-L20583
[^109]: Source: knowledge/notes/input_part012_review.md†L20581-L20587
[^110]: Source: knowledge/notes/input_part012_review.md†L17321-L17325
[^111]: Source: knowledge/notes/input_part012_review.md†L18632-L18638
[^112]: Source: knowledge/notes/input_part004_review.md†L115-L115
[^113]: Source: knowledge/notes/input_part012_review.md†L19186-L19195
[^114]: Source: knowledge/notes/input_part012_review.md†L19300-L19318
[^115]: Source: knowledge/notes/input_part000_review.md†L103-L103
[^116]: Source: knowledge/notes/input_part000_review.md†L738-L740
[^117]: Source: knowledge/notes/input_part004_review.md†L31-L31
[^118]: Source: knowledge/notes/input_part000_review.md†L241-L241
[^119]: Source: knowledge/notes/input_part000_review.md†L203-L203
[^120]: Source: knowledge/notes/input_part000_review.md†L211-L211
[^121]: Source: knowledge/notes/input_part000_review.md†L212-L212
[^122]: Source: knowledge/notes/input_part000_review.md†L298-L298
[^123]: Source: knowledge/notes/input_part000_review.md†L302-L307
[^124]: Source: knowledge/notes/input_part000_review.md†L326-L333
[^125]: Source: data/vesc_help_group/text_slices/input_part000.txt†L23001-L23039
[^126]: Source: knowledge/notes/input_part002_review.md†L19-L21
[^127]: Source: knowledge/notes/input_part002_review.md†L22-L22
[^128]: Source: knowledge/notes/input_part002_review.md†L42-L44
[^129]: Source: knowledge/notes/input_part002_review.md†L122-L124
[^130]: Source: knowledge/notes/input_part002_review.md†L150-L152
[^131]: Source: knowledge/notes/input_part002_review.md†L152-L152
[^132]: Source: data/vesc_help_group/text_slices/input_part014.txt†L7189-L7200
[^133]: Source: data/vesc_help_group/text_slices/input_part014.txt†L6907-L6913
[^134]: Source: data/vesc_help_group/text_slices/input_part014.txt†L10605-L10633
[^135]: Source: data/vesc_help_group/text_slices/input_part014.txt†L10587-L10605
[^136]: Source: data/vesc_help_group/text_slices/input_part014.txt†L10409-L10492
[^137]: Source: data/vesc_help_group/text_slices/input_part014.txt†L10613-L10619
[^138]: Source: knowledge/notes/input_part010_review.md†L401-L401
[^lite-phase-cap]: Source: knowledge/notes/input_part010_review.md†L601-L601
