# VESC ADC & Accessory Power Integration Playbook

## TL;DR

- Wire throttles, brakes, and regen controls straight into the controller’s ADC pins and keep everything on 3.3 V logic.
  - dash adapters and 5 V accessories routinely add lag or kill channels when they fail, and even hall throttles that creep toward 3.5 V need resistor tweaks before they clip the MCU’s ADC ceiling.[^1][^1][^2][^4]
- Publish explicit resistor-divider and adapter wiring diagrams for any 5 V hall throttles or brakes headed toward STM32 inputs so installers stop improvising values that over-voltage ADC pins.[^divider_docs]
- Xiaomi-style throttles and hall brakes stay healthy when powered from the controller’s 3.3 V rail with matched resistor dividers; feeding 5 V without clamps has already over-volted STM32 inputs, and ’lekrsu’ is still warning newcomers that direct 5 V on ADC1/ADC2 will cook the STM32 even if the throttle “works” initially.[^2][^3]
- Treat the Spintend/MakerX auxiliary board as a low-current signal bridge: its ~12 V/3 A rail can light LEDs or run logic, but headlamps, horns, and pumps still need a dedicated DC/DC or relay-fed supply.[^3][^9][^10][^11]
- Insulate the adapter, strain-relieve looms, and bench-test polarity before energising accessories; a shorted 12 V fan lead already cooked a Spintend ADC board and combo switch pods have back-fed horn voltage into signal lines until riders swapped to full-pin motorcycle pods.[^adc_inspection]
- Profile toggles still need proper routing.
  - shorting ADC1 to ground with a momentary switch only works after moving the throttle to ADC2 and wiring the three-position “gear” toggle correctly, otherwise builders keep burning MakerX ADC daughterboards.[^4][^5][^6][^7]
- Map and validate every analog input inside VESC Tool before sealing the deck; enabling ADC control blocks bench FWD/REV overrides, so miswired harnesses must be fixed before ride testing.[^7][^8][^13]
- Spintend adapter installs still need VESC Tool set to **ADC** input mode and the board’s 5 V/3.3 V toggle aligned with the throttle harness before blaming wiring.
  - several “dead throttle” reports came down to the wrong app mode or voltage switch.[^8]
- Most VESC peripherals expect 3.3 V logic—confirm accessory requirements before reusing 5 V sensors or you’ll chase detection issues later.[^9]
- Protect logic rails by isolating accessory power, adding pull-down failsafes, and avoiding shared 5 V lines between controllers.
  - shorts or ground loops keep blowing MOSFET drivers and display boards.[^14][^16][^17][^19]
- Follow Koxx’s latest survival checklist: never hot-plug accessories with the main pack live, ban raw 5 V throttles from STM32 ADC pins, and shield every ADC/UART run so voltage spikes can’t cook daughterboards.[^10]
- Spintend’s ADC expander can script one-touch 1WD/2WD toggles, but you must isolate CAN or power between controllers or the “sleeping” unit keeps mirroring battery current.[^spintend_toggle]
- Xiaomi dashes stay stable on VESC firmware 6.05 when you add a 1 kΩ resistor inline with the UART lead; leave the stock harness otherwise and expect the dash to coexist with direct-hall throttles.[^11]
- Dualtron riders trying to keep the OEM dash on VESC must script the CAN/UART protocol (often by adapting the open VSETT Lisp), and veterans steer those projects toward Spintend Ubox hardware instead of Flipsky/Makerbase so the investment lands on a robust controller platform.[^12]
- Ubox V2 boards now carry self-reset fuses on 5 V/12 V/3.3 V rails, yet VESC Tool 3.01 still crashes mid-calibration if 5 V throttles hit the STM32 input.
  - stick to 3.00/5.2 firmware or add voltage dividers before final assembly.[^13]

## Signal & Power Budget Cheatsheet

| Channel | Voltage | Continuous Current | Typical Uses | Guardrails |
| --- | --- | --- | --- | --- |
| ADC1 / ADC2 (signal) | 3.3 V reference | ≈1 mA (input) | Throttle, brake, regen slider | Stay on 3.3 V hall outputs or add dividers/pull-downs so open circuits fall to zero.[^1][^4][^19] |
| Spintend ADC v3 accessory rail | 12 V (buck) | ≈3 A total | Tail lights, brake triggers, small relays | Parallel 18 W lamps already flirt with the limit.
  - push heavier loads through an external converter.[^3][^10] |
| Controller logic rail | 5 V from onboard DC/DC | <0.5 A budget | Displays, hall sensors, footpads | Never back-feed from other controllers or dashes; a single short can blow the logic board and even 5 V throttle feeds have cooked STM32 ADC stages.[^5][^14][^16] |
| External DC/DC (recommended) | Pack → 12 V/5 V | Sized to load | Headlights, horns, pumps, fans | Use relays or MOSFETs triggered by the ADC board for safe switching.[^9][^11][^15] |
| Makerbase Lite ignition rail | ≈12 V logic tap | Light accessory top-ups | The rail can wake a phone charger but trips on heavier loads.
  - treat it as a trigger for a dedicated buck, not a lighting supply.[^14] |

> **Field note:** When deck space is tight, riders still power headlights from a dedicated buck instead of the ADC rail; Noname’s Jetson build proved a stand-alone DC-DC keeps Spintend’s accessory outputs in reserve while USB-rechargeable bar lights offer long runtime without tapping controller power.[^15]

## Wiring Recipes

### Throttles & Brakes

1. **Direct hall wiring:** Route throttle and brake halls straight to ADC1/ADC2 signal, 3.3 V, and ground to keep control even when the OEM dash is removed.[^1] Keep the sensors on the controller’s 3.3 V rail.
  - feeding 5 V halls directly into STM32 ADCs has already killed logic stages.[^16]
1. **Verify MakerBase harness pinouts before rewiring.** Some 75100 looms shipped with cut or mislabelled conductors; Paolo only recovered throttle on his Wolf GT after tracing 3.3 V, ground, and ADC1 correctly before rerunning calibration.[^makerbase_pinout]
1. **Roll back firmware if ADC channels vanish.** Xiaomi throttles that lost response on beta firmware came back after downgrading to VESC 6.02, rerunning the motor/ADC wizards, and explicitly writing both app and motor configs before power-cycling.[^17][^18]
1. **Document the colour map in every quick-start.** Spell out which conductors carry 5 V, ground, and signal, list the negative motor/battery current limits riders must set for regen, and call out the CAN IDs/master roles when a single throttle feeds dual VESCs so newcomers avoid phantom faults.[^19]
2. **Clamp 5 V inputs.** Xiaomi/Boosted-style throttles swing ≈0.8–4.1 V from a 5 V rail; drop them through a 1 kΩ/2 kΩ divider or use the ADC adapter so the STM32 never sees more than 3.3 V.[^voltage-divider]
2. **Match lever logic.** Magura’s MT5e ships in normally-closed (2700985) and normally-open (2700984) variants, and the Spintend ADC board can flip between switch and hall sensing with onboard toggles plus 5 V/3.3 V selection.
  - confirm the lever SKU before crimping harnesses.[^25]
3. **Spin-Y & other multi-button throttles:** Version 1 units need custom JST‑1.0 leads into ADC2/COMM2; version 2 ships with a four-conductor harness that lands cleanly on the adapter board.[^2]
- Dualtron riders debugging Spin-Y2 throttles found ESC A’s ADC1 dormant—moving the plug to ESC B’s ADC1 and feeding it 5 V finally registered the signal.[^spin_y2_adc1]
3. **QS-S4 throttles wire like any hall lever.** Land 3.3 V, signal, and ground on the ADC harness, then recalibrate SOC maths.
  - controllers still read pack voltage while dashboards may show 13 % after a cold-weather BMS cut near freezing.[^20]
- 🇪🇸✨عمر still ranks the Spin-Y2 as the premium hall-with-regen option on Xiaomi-class builds, while Haku points budget riders to a $3 AliExpress thumb throttle that has survived months on a Peak G30.
  - use the high-end pod when you want dual-action mapping and keep the cheap spare for commuter spares.[^21]
- When fitting Spin-Y throttles to Makerbase 75100s, meter the signal line before landing it on ADC—anything over ≈3.8 V risks killing the STM32 MCU, so power the harness from the controller’s 5 V rail while you test.[^spin_y_signal_check]
- 1Zuna’s Xiaomi dash Lisp still needs a 1 k–1.2 kΩ pull-down on the button harness to stop ghost presses; builders now solder the resistor inline so the dash works with both G30 and Makerbase controllers.[^dash_pulldown]
3. **Spintend adapter v3 harness:** Modern boards arrive with keyed plugs—no more screw terminals—so match the supplied loom instead of hand-crimping tiny JST shells.[^3]
4. **Flip the ADC app mode first:** When the throttle shows activity but VESC Tool still ignores input, switch the App to “ADC” and confirm the adapter’s 5 V/3.3 V toggle matches your hall sensors before tearing the harness apart.[^8]
4. **Blinker/lighting channels:** The adapter already drives LED strips for turn indicators; repurpose the outputs for custom amber lighting and move heavier lamps to an external buck to stay within the ≈3 A rail.[^spintend_led]
4. **Makerbase accessory headers use GH 1.27 mm.** Izuna confirmed the tiny Makerbase harness lands on GH-series plugs.
  - order JST-GH pigtails instead of trying to force JST-PH shells onto the board.[^22]
4. **MakerX footpads & 3.3 V-only sensors:** Confirm both ADC rails output 3.3 V before blaming pads; swapping to 5 V kills the hall board.[^4]
5. **Publish a MakerX S100 footpad checklist.** The latest review segment asks for explicit pinout and 3.3 V verification steps.
  - bundle regulator checks, connector orientation, and ADC routing in your wiring docs so teams stop misdiagnosing dead sensors.[^23][^24]
5. **Trim dual-hall start voltage.** Dual-controller Vsett builds needed manual tweaks to throttle start voltage after calibration so brake and throttle channels stay stable across master/slave VESCs.[^25]
5. **Interpret ADC counts, not raw voltage:** VESC Tool reports hall inputs as 0–4095 counts.
  - track the delta between idle and full throw, and if readings compress, repeat the test with a stable 5 V source to rule out noisy 3.3 V regulators before replacing sensors; Spintend’s adapter manual expects ~0.8 V idle, so stop and rewire if a channel sits near 3 V.[^22][^adapter-idle]
6. **Filter noise in software first:** Builders tamed runaway triggers by compressing throttle activation to ~0.83–1.2 V inside VESC Tool rather than rewiring hardware; chassis grounding tricks have also helped but carry short-to-frame risk if insulation fails.[^adc-noise]
6. **Fail-safe defaults:** Add a pull-down resistor from throttle signal to ground so any broken wire snaps to zero instead of ghost acceleration.[^19]

- **Watch boot-time spikes.** A throttle that briefly jumps to ~2 V only during controller boot points to poor filtering or shielding around ADC1.
  - clean up harness routing or add filtering before chasing firmware ghosts.[^26]
- **Prototype curve throttles carefully.** Early scroll-wheel “curve throttle” builds dedicate forward travel to acceleration and reverse travel to regen, giving smooth proportional braking once firmware supports dual-action mapping.
  - keep wiring modular so you can fall back to proven hall throttles mid-test.[^27]
- **Artem’s bidirectional throttle is nearing production.** The MCU-driven pod merges brake and throttle into one housing, lets riders switch between uni- and bidirectional curves off a single hall, and exposes both 5 V and 3.3 V outputs so it drops into stock controllers or VESCs without the ADC adapter; expect $45–$55 pricing once the injection-moulded shells land.[^28]
- **Emergency dual-channel mapping needs firmware.** Happy Giraffe mirrored ADC1 onto ADC2 by rebuilding `app_adc.c`; use it only as a stopgap brake-to-throttle hack and plan a proper wiring fix once soldering tools are available.[^29]
- **Dual-profile throttles still need firmware help.** Stock VESC mappings ignore ADC2, and even Lisp scripts cannot override the app cleanly.
  - combine dual throttles into one channel or remap firmware inputs if you want “legal/illegal” modes on the fly.[^30]
- **Three-speed scripts need clean analog rails.** ’lekrsu’ shared an ADC2 gear-shift script for Xiaomi builds but still refuses to run it on his noisy analog harness.
  - bench-test noise levels before publishing how-tos built around that code.[^31][^32]
- **Shield noisy harnesses:** High-phase-current builds needed shielded throttle looms and 5 V→3.3 V adapter boards (e.g., Spintend’s filter) to stop hall noise from overwhelming the ADC rail long-term.[^33]
- **Beware 300X throttle EMI.** عمر’s Tronic X12 surged violently after swapping to a 300X throttle until he separated throttle/CAN/Bluetooth looms, reverted to BLDC for testing, and added a ~2 kΩ pull-down on the signal to tame hall noise coupling into the CAN harness.[^34]
- **Pick flexible multi-core looms.** Shared-ground 24–26 AWG cables or slim AliExpress harnesses keep throttle/brake/start wiring tidy through cramped passthroughs; stiff Ethernet looms fatigue quickly on Xiaomi/VSETT decks.[^35]
- **Treat Spinny throttles like premium hall units.** Spintend’s CNC trigger is still a hall throttle under the billet shell, so wire it like any hall input and expect Davega displays to share RX/TX pins on the same harness once the pinout is corrected.[^36][^37]
7. **Legacy dash retention:** Leaving throttle through a dash adapter adds perceptible lag; many builders keep the dash for display only and wire throttles directly to the controller instead.[^20]
8. **Refresh mappings after downtime.** Scooters that sat for months have thrown false brake/throttle behaviour until riders reran the ADC wizard and removed stale inversion flags inside VESC Tool.[^storage-cal]
9. **Plan for short harnesses and three-speed toggles.** Early Spin-Y batches shipped with limited cable length and optional ADC v2 three-speed leads; document extension routing and ensure cruise-control wiring lands on the correct pins before sealing the deck.[^spin_wiring]
9. **Monitor brake sensors.** Dead brake halls make some VESC scooters pulse the motor every second or two under throttle, so replace failed sensors before ride testing.[^38]

- **Respect hall voltage levels.** Wheelway and Xiaomi hall boards still output 4.8–4.9 V, so native VESC inputs need proper voltage dividers or rare 3.3 V sensors; two-wire brake cut-offs simply short 5 V to signal for on/off stops with no proportional control.[^39]
7. **Shield noisy looms.** Running ADC throttles and SmartDisplay UART over shielded cable tied to controller ground cleared 120 A jitter, and separating signal bundles from phase wires kept FOC noise out of high-amp Ubox builds.[^signal-shield]
8. **Fail-safe defaults:** Add a pull-down resistor from throttle signal to ground so any broken wire snaps to zero instead of ghost acceleration.[^19]
9. **Legacy dash retention:** Leaving throttle through a dash adapter adds perceptible lag; many builders keep the dash for display only and wire throttles directly to the controller instead.[^20]
10. **Refresh mappings after downtime.** Scooters that sat for months have thrown false brake/throttle behaviour until riders checked the hardware-mode switch, reran the ADC wizard, and removed stale inversion flags inside VESC Tool.[^storage-cal]
11. **Monitor brake sensors.** Dead brake halls make some VESC scooters pulse the motor every second or two under throttle, so replace failed sensors before ride testing.[^38]
12. **Keep hall brakes separate.** Do not tie two hall levers to one ADC input.
  - floating outputs land at different voltages and can latch regen; dedicate one channel per lever and leave the spare brake mechanical if you run out of inputs.[^40]

### Pedal Assist (PAS)

- **Split the loom correctly.** Flipsky PAS harnesses expect a four-wire breakout (5 V, ground, cadence signal, and often a brake/enable lead) with the signal routed to ADC1 while a regen throttle lives on ADC2; plan the split before sealing the controller cavity so you do not lose throttle redundancy.[^41]
- **Validate hall swing.** PAS sensors only register once the hall output toggles roughly 0–1.5 V on ADC1; if regen releases bounce the signal, tighten filtering so the throttle does not re-engage after braking.[^42]
- **Makerbase/Flipsky quirks.** Current 75100 Pro V2 firmware only exposes a quadrature PAS mode, so adapting three-wire cadence sensors needs an intermediary microcontroller, and the servo header’s 5 V tolerance is still unconfirmed.
  - test before powering accessories straight from that pin.[^43]
- **Three-wire PAS on Flipsky hardware.** Share 5 V and ground with the throttle, land the PAS signal on ADC1, keep the throttle on ADC2, and terminate everything in soldered JST shells instead of temporary terminal blocks so vibration does not shake the joints loose.[^flipsky-3wire-pas]

### Regen Buttons & Variable Brakes

- **Momentary button recipe:** Wire the button between ADC2 signal and the 3.3 V rail; avoid series resistors because they created “stuck brake” faults in testing.[^6]
- **Analog lever mapping:** Run the ADC calibration wizard, keep the window open while sweeping the lever, then assign the channel to “Current (No Reverse)” so regen ramps in with negative motor/battery limits.[^7][^8]
- **Dedicated regen controls cut heat.** Riders running hall brake levers or second throttles for regen report far lower rotor temperatures and brake fade, provided mechanical brakes stay ready for emergencies and high-voltage packs with limited headroom; most builds still rely on auxiliary halls because proportional regen remains tied to spare throttles instead of the main lever.[^44][^45]
- **Publish 75100 regen & PAS workflows.** Flipsky 75100 owners are still chasing paid Lisp gigs just to restore regen and pedal-assist scripts.
  - capture the step-by-step so newcomers aren’t stuck without braking on fresh installs.[^46][^47]
- **Scroll-wheel demand is back.** Spintend and Rion riders are prototyping dual-spring scroll throttles that split 70 % throttle/30 % regen travel or add pressure sensors under the trigger to recover the Rion Curve feel once production restarts.[^48][^49]
- **Production curve throttles on the roadmap.** Spintend is evaluating a thumbwheel that mimics Rion’s dual-action throttle ergonomics, signalling that proportional regen hardware may ship as an official accessory instead of a one-off prototype.[^50]
- **Hall-based levers:** Pair Xiaomi hall levers or custom SS49E/A1324LUA + magnet housings with the SmartDisplay/ADC board to unlock proportional braking.
  - digital on/off microswitches pulse the motor and feel unnatural once regen replaces cable brakes; builders now glue magnets to stock levers and share STL brackets to retrofit halls anywhere.[^analog-halls][^regen-halls]
- **Left-hand throttles for regen:** Many crews wire a spare left-hand thumb throttle to ADC2 for progressive regen while leaving the right-hand unit for drive; VESC input mapping even lets an auxiliary on/off lever cap panic-stop regen around 10 A for safer emergency grabs.[^51]
- **Hydraulic mix-and-match:** When swapping Ninebot G30 front levers, move the factory hall sensor and magnet into the hydraulic body so proportional regen survives the upgrade.[^ninebot-hall]
- **Scroll-wheel throttles:** Thumbwheel throttles work well as dedicated regen controls.
  - Mirono’s Ubox build runs ~80 A phase / 15 A battery for a smooth 47 km/h eco mode while still craving BLDC punch at launch.[^52][^53]
- **Front-only caution:** Riders running “Shigura” hybrids keep front regen low or disabled; abrupt ramps can lock a lightly loaded front tyre on wet pavement.[^26]
- **ADC2 brake inputs remain limited.** Stock firmware ignores the second analog channel for braking logic.
  - plan to recompile with remapped inputs or stick to simple current-control modes if you need dual analog brakes.[^54]
- **Boosted Rev mapping:** Expect ≈1.6 V full brake, 2.54 V neutral, and 3.3 V wide open on Boosted Rev thumbwheels once mapped to VESC ADC inputs, delivering strong regen with minimal mechanical braking.[^boosted-map]

### Dash & Display Options

- Xiaomi Pro 2 builders running dual 75100s keep the stock dash by relocating the ESC and splicing lighting into AUX power while custom scripts bridge the UART header—proof the dash and lighting can coexist with direct ADC throttles.[^xiaomi_dash_dual75100]
- **CrowPanel touch dashboards free up IO.** Builders moving to CrowPanel’s 5" 800×480 ESP32-S3 display route the VESC BMS over CAN and dedicate UART to the dash; plan for LVGL-based touch controls plus extra GPIO for profile switching when the stock dash already consumes UART.[^55]

### Profile & Gear Switching

- **Dual throttles on CAN need careful routing.** Keep both controllers in VESC CAN mode, land the throttle on the master using `ADC+UART`, and let CAN mirror torque to the slave; independent front/rear throttles require separate CAN buses plus phase caps on the front motor to tame slip.[^56]
- **Document throttle reassignment before adding gear toggles.** Builders shorting ADC1 to ground with a momentary switch.
  - without moving the throttle signal to ADC2
  - have repeatedly blown MakerX ADC3 daughterboards. Treat profile toggles as signal bridges that need proper wiring diagrams and pull-downs before testing.[^gear-toggle]
- **Validate community scripts before publishing.** ’lekrsu’s Xiaomi Pro 2 “gear shift” macro maps ADC2 as a mode selector but he cannot run it himself due to noisy analog lines; bench-test the workflow before sharing it beyond early adopters.[^xiaomi-gear-script]
- **Latching profile toggles:** ADC2 can host a latching switch that feeds a distinct voltage, letting commuters flip between limited and unlimited profiles with the five-press brake logic while leaving ADC1 dedicated to throttle.[^57]
- For on-the-fly 2WD toggles, builders either feed Spintend’s ADC adapter from the controller’s 12 V rail or script a small Arduino on the UART `setCurrent` example so a handlebar switch drops the front motor to 0 A.[^setcurrent_toggle]

### Lighting, Horns & Aux Loads

- **Use the adapter as logic, not power:** The horn output only sources a couple of amps.
  - enough for low-power buzzers but not vintage 35 W halogens
  - so trigger a relay or MOSFET that pulls from a beefier DC/DC converter.[^9][^10]
- **Remember the Spintend switch cluster sources 12 V on every lead.** Plan NO/NC relays or alternative switchgear when you need ground-referenced signals, otherwise horn and light circuits back-feed the controller inputs.[^spintend_cluster]
- **Keep 12 V fans off the board:** Spintend ADC adapters have already died when builders powered shrouds directly from the rail.
  - treat it strictly as a signal bridge and feed cooling gear from standalone bucks.[^58]
- **85250 & Ubox installs:** Route brake-light logic through the ADC breakout, but feed lamps from a separate converter so you don’t brown out the controller when multiple 12 V loads fire at once.[^11]
- **Treat the Ubox fan header as temperature-only.** The 12 V header driving the stock fan is thermostatic.
  - firmware cannot toggle it
  - so plan external bucks or constant 12 V rails for lighting if you need manual control.[^59]
- **TF100 & OEM switch pods:** Reuse factory throttles by landing the red/black hall power and the green signal lead on a 3.3 V ADC input; this preserves dash ergonomics without custom PCBs.[^12]
- **Skip illuminated combo pods:** Backlit handlebar switches feed accessory voltage into the signal lines and confuse the ADC board unless you gut the lighting.
  - treat them as incompatible without a full rewire.[^24]
- **Avoid parasitic taps:** Pulling 12 V from internal headlight pins (e.g., X12) drags the logic rail and costs range—draw pack power into a dedicated converter instead.[^15]
- **Protect logic rails:** Shorting auxiliary leads straight on the controller board has already destroyed logic stages; isolate accessories and fuse every feed.[^16]
- **Check your multimeter mode before probing.** Accidentally measuring resistance on a live harness has shorted throttle rails and fried ADC inputs.
  - double-check the dial before touching controller pins.[^60]
- **Fuse the adapter output:** One builder shorted the 12 V rail on a brand-new Spintend 85240 while wiring lights and killed the buck stage; add inline fuses or external bucks so a single mistake doesn’t scrap the controller.[^16][^23]
- **Respect the adapter’s voltage ceiling.** The board is only rated for roughly 60 V kill loops—use it to mirror low-voltage latches while heavy pack isolation stays on a loop key, contactor, or smart BMS.[^61]
  - JK and ANT power buttons can share the adapter ground safely, but keep every trigger on the logic side and never backfeed full pack voltage into the daughterboard.[^61]
- **Treat buttons as triggers only:** The ADC adapter does not replace a loop key or smart-BMS latch; plan a real kill switch for theft deterrence or maintenance.[^17][^18]
- **Lean on the adapter for logic features, not efficiency gains.** The Spintend ADC board remains the quickest way to wire kill-switch logic or single-motor limp modes, but veterans note dual-motor operation stays more efficient at a given current draw.
  - reserve single-motor toggles for fault recovery, not everyday riding.[^62]
- **Leverage DAC outputs.** Spintend 75/300 firmware can repurpose the PPM pin into a DAC brake-light feed, but expect to lean on community firmware drops until official docs land.[^31]

## Configuration & Validation Workflow

1. **Bench prep:** Wire controls with the pack off, confirm continuity, and verify 3.3 V and 5 V rails before powering up.
   - Disconnect secondary controllers during Spintend throttle calibration to keep the CAN bus quiet, then confirm 60 Ω across the pair before plugging the slave back in.[^can_calibration]
2. **Calibrate ADC inputs:** In VESC Tool, run the ADC mapping wizard for each channel, noting min/max values and checking that neutral centers correctly.[^7]
3. **Assign app functions:** Map ADC1 to throttle, ADC2 to “Current No Reverse” for regen, and ensure throttle curves or safe-start options suit the rider.[^8]

- Even with the new NRF headers on recent VESC hardware, firmware still blocks simultaneous ADC, UART display, PAS, and cruise-control inputs.
  - plan one control path per profile until Vedder lifts the limit.[^63]
4. **Understand bench limitations:** Once ADC control is enabled, the manual FWD/REV buttons in VESC Tool stop working—switch the app to UART or disable ADC temporarily for bench spins.[^13]
5. **Write configs explicitly:** Mobile reconnects and desktop wizards can wipe ADC settings unless you press “Write Motor Config” and “Write App Config” after every change.[^21]
6. **Document firmware overrides.** If you merge ADC channels in `app_adc.c` (e.g., mirroring ADC2 to ADC1 as an emergency throttle), capture the patch and share it with the owner so future firmware updates preserve the fail-safe.
  - and publish the wiring/code diff so torque-sensor bikes can add redundant throttles without guesswork.[^64][^65]
7. **Log shakedowns:** Capture CAN or USB logs on the first rides to confirm commanded vs. actual current and verify regen ramps without triggering BMS cutoffs.[^11]

## Safety & Troubleshooting Checklist

- Lisa’s dual 75100 build still sounded rough after disabling phase filters, and the 1Zuna CAN dashboard stopped reporting speed—rerun detection, verify CAN scaling, and confirm firmware 6.05 mappings before trusting telemetry.[^dual75100_noise]
- Dual-ADC scripts have let rear motors ignore 20 km/h limits while the front obeys; bake speed caps into both CAN nodes whenever you adapt Ninebot macros to dual-controller scooters.[^dual_adc_speed_caps]
- **Mount adapters beside the controller.** Parking the ADC board near the ESC and running shielded cables kept long throttle runs quiet; Vedder’s mid-June firmware now times out detach scripts (~3 s) so Xiaomi dash integrations hand inputs back automatically once the ADC board is unplugged.[^66][^67][^68]
- **Power MakerX BLE modules from the communication header.** Pull 5 V and ground from the comm port and borrow UART2 TX/RX so Jaykup firmware stops browning out the module without overloading the 3.3 V rail.[^makerx_ble]
- **Chase “missing module” faults at the harness first.** After firmware updates, swap the UART TX/RX pair or re-enable Bluetooth in VESC Tool before assuming hardware failure; several Spintend adapters came back online immediately, and their throttles landed on VAL2 until the app mapping was refreshed.[^69][^70]
- **Separate controller rails:** Do not tie CAN-connected controllers’ 5 V rails together unless they share the same ignition path; mismatched power buttons have already killed hardware.[^14]
- **Disconnect before rewiring.** Builders keep blowing ADC daughterboards by hot-plugging throttles and accessories.
  - always kill the battery before touching the harness or you’ll spike converters despite heat-shrink and shielding.[^71][^72]
- **Seat the adapter switches before testing.** If the Spintend board reads erratically, confirm the 5 V/3.3 V selector and NO/NC toggles are firmly latched, then bypass the board with the controller’s 3.3 V rail only for short diagnostic sweeps.
  - full travel on 5 V sensors while direct-wired has already killed modules.[^73][^74]
- **Keep kill-switch redundancy:** Combine Safe Start, loop keys, and/or smart-BMS latches so thieves or techs can de-energise the scooter without relying on ADC buttons alone.[^17]
- **Watch for brownouts:** Builds that still depend on Makerbase/Flipsky rails should budget extra capacitance or buffer packs.
  - the same rail that feeds ADC accessories is the one that dies during BMS trips.[^10]
- **Cold-weather cutouts aren’t wiring faults.** 20 S BMS boards can open at roughly 15 % state of charge when cells are near freezing.
  - verify pack temperature and discharge curves before blaming the throttle wiring.[^75]
- **If a channel dies:** Check for 3.3 V on the sensor, rerun ADC mapping, inspect JST orientation, and confirm the pull-down still measures the expected resistance.[^7][^19]
- **Bypass the adapter when debugging.** When the external ADC module starts spitting nonsense, feed 3.3 V, signal, and ground straight from the controller to the throttle/brake to prove the harness.
  - just never slam 5 V accessories onto the STM32’s 3.3 V rail during the test.[^76]
- **Clamp high-voltage throttles.** MiniMotors EYE triggers swing ≈0.8–4.1 V from a 5 V rail—drop a resistor divider or use the ADC adapter before landing them on STM32 pins.[^28]
- **Mind mixed levers.** Xiaomi hall brakes share 5 V/GND safely, but paralleling them with normally-open Magura hydraulics leaves floating signals unless you add a hall puck to the hydraulic lever.[^32]
- **One lever, one channel.** Sharing an ADC input between hall levers leaves each at a different float voltage and creates stuck-brake faults.
  - wire them independently or drop the extra hall.[^hall-split]

## Source Notes

[^1]: Routing throttle and brake halls directly into ADC1/ADC2 preserves control without the OEM dash.[^77]
[^2]: Spin Y throttle versions and wiring expectations for Spintend/Ubox adapters.[^78]
[^spin_y2_adc1]: Source: knowledge/notes/input_part008_review.md†L337-L337
[^spin_y_signal_check]: Source: knowledge/notes/input_part008_review.md†L339-L339
[^dash_pulldown]: Source: knowledge/notes/input_part008_review.md†L340-L340
[^xiaomi_dash_dual75100]: Source: knowledge/notes/input_part008_review.md†L338-L338
[^setcurrent_toggle]: Source: knowledge/notes/input_part008_review.md†L392-L392
[^dual75100_noise]: Source: knowledge/notes/input_part008_review.md†L390-L390
[^dual_adc_speed_caps]: Source: knowledge/notes/input_part008_review.md†L391-L391
[^3]: Spintend v3 adapter now ships with keyed harness connectors.[^79]
[^4]: MakerX S100 footpads require the controller’s 3.3 V rail.
  - missing the regulated feed leaves the sensor dead even when wiring diagrams look correct.[^80]
[^6]: Regen button tied directly between ADC2 and 3.3 V without series resistors eliminated false braking faults.[^81]
[^7]: ADC calibration workflow and reminder to let VESC Tool find neutral before assigning functions.[^82]
[^8]: Regen mapping best practices from community quick-start guides.[^83]
[^9]: Horn output current limit cautions on Makerbase/Spintend harnesses.[^84]
[^10]: Spintend ADC aux outputs top out around 12 V / 3 A and need DC/DC help for bigger loads.[^85][^86]
[^11]: Smart Repair’s 85250 guidance—use the ADC board for logic and a DC/DC converter for lamp current.[^87]
[^12]: TF100 throttle wiring recipe using the controller’s 3.3 V hall supply.[^88]
[^13]: Enabling ADC control disables manual FWD/REV overrides inside VESC Tool until you switch apps.[^89]
[^14]: CAN-linked controllers should not share 5 V rails; doing so has already killed boards.[^90]
[^15]: Drawing accessory power from the X12 headlight feed drags the logic rail and wastes energy.[^91]
[^16]: Shorting controller auxiliary leads has destroyed logic boards, proving the need for isolated accessory supplies.[^92][^93]
[^17]: Builders still rely on loop keys, smart-BMS buttons, and Safe Start—ADC boards alone do not provide a true kill switch.[^94]
[^18]: Spintend’s ADC adapter v2 only ferries 5 V/12 V accessory power, is rated for ≈60 V pack input, and cannot act as an anti-spark or ignition switch.
  - route kill switches through a smart BMS or loop key instead.[^95][^96]
[^19]: Pull-down resistors on throttle lines guarantee a zero output if the signal wire opens.[^97]
[^20]: Routing throttle through dash adapters adds noticeable lag; direct ADC wiring restores responsiveness.[^98]
[^21]: VESC Tool can wipe ADC settings after reconnects unless you explicitly write both motor and app configs.[^99]
[^22]: Hall-diagnostics workflow focusing on ADC count deltas and re-testing with a clean 5 V rail when noisy 3.3 V supplies flatten readings.[^100]
[^artem-bidir]: Artem’s MCU-based throttle prototype combines throttle/brake travel, supports bi- or unidirectional mapping from a single sensor, and includes selectable 5 V/3.3 V outputs at a $45–$55 target price.[^28]
[^23]: Shorting the Spintend 85240 aux rail to ground killed the unfused buck regulator, reinforcing the need for inline fuses or external converters when powering lighting from the adapter.[^101]
[^24]: Illuminated AliExpress switch pods leak voltage into ADC signal lines and require major rewiring to behave.[^102]
[^spintend_toggle]: Spintend ADC expander scripts for 1WD/2WD toggles demand CAN or power isolation so sleeping controllers stop mirroring battery current.[^103][^104]
[^spintend-diodes]: Smart Repair’s wiring log shows the Spintend ADC adapter happily sharing a single lamp when the reverse feed is diode-isolated and paralleled with the headlight output.[^105]
[^aux-port]: 🇪🇸AYO#74 warned that the auxiliary port beside the CAN header stays powered until shutdown, so tapping it leaves lights on unless you add a dedicated switch.[^106]
[^dash-coexist]: The same build ran the Spintend adapter on ADC1/ADC2 and left the Xiaomi dash on UART without conflicts once wiring was tidied.[^107][^108]
[^adc-high-side]: VESC ADC harness brake outputs source battery positive, so pair anodes with the function pins and common grounds or isolation diodes to combine lighting modes safely.[^109]
[^adc-noise]: Compressing throttle activation windows to ~0.83–1.2 V cleared ADC-trigger noise on Spintend builds; some riders grounded the chassis for extra stability but warn the practice risks shorts if insulation fails.[^110]
[^adapter-idle]: Spintend’s adapter manual targets ~0.8 V idle readings.[^111][^adapter-idle-source]
  - seeing ~3 V idle means the channel is wired wrong and will act like a stuck brake.[^111]
[^spintend_led]: Spintend’s ADC adapter already drives LED strips for turn indicators, so builders can route custom amber lighting through existing outputs and keep heavier loads on a dedicated converter.[^112]
[^adc_inspection]: Spintend ADC survival log documenting a shorted 12 V fan lead, the need to insulate adapters, and the move to full-pin motorcycle pods after combo switches back-fed horn voltage.[^72]
[^spintend_cluster]: Spintend switch-cluster teardown noting each output sources 12 V, so logic-level controller inputs require relays or alternate switchgear.[^72]
[^storage-cal]: Re-running the ADC wizard and clearing stale inversion flags resolved Xiaomi brake/throttle glitches after long storage.[^113]
[^analog-halls]: Hall-based brake levers (Xiaomi or custom SS49E builds) let SmartDisplay/ADC boards blend braking force; digital microswitch levers pulse the motor instead of delivering progressive regen.[^114]
[^regen-halls]: Builders glue magnets to levers and pair them with A1324LUA sensors for proportional regen retrofits on any brake.[^115]
[^25]: Magura MT5e lever SKU guidance plus Spintend ADC toggle support for normally-open or normally-closed brake sensors.[^116]
[^26]: Riders debating “Shigura” hybrids warned that front-only regen should be limited or disabled to avoid low-traction lockups.[^25][^rev-cite]
[^27]: Shielded ADC and UART looms tied to controller ground eliminated 120 A cruise-control jitter and reduced FOC noise on Ubox builds.[^signal-shield]
[^28]: MiniMotors Eye throttles output ≈0.8–4.1 V from a 5 V rail, so dividers or adapter boards must clamp the signal below 3.3 V.[^signal-clamp]
[^29]: Boosted Rev thumbwheel voltage map delivering strong regen without relying on mechanical brakes.[^boosted-map]
[^30]: Ninebot builders move the stock hall sensor and magnet into aftermarket levers to keep proportional regen with hydraulic fronts.[^ninebot-hall]
[^31]: Spintend 75/300 firmware can remap the PPM pin into a DAC-driven brake light even though official documentation is still pending.[^117]
[^32]: Xiaomi hall levers coexist on 5 V/GND rails, but pairing them directly with normally-open Magura hydraulics leaves floating signals until a hall puck is added.[^signal-clamp]
[^voltage-divider]: Xiaomi-style throttles and levers output ≈0.8–4.1 V from a 5 V rail, so builders add 1 kΩ/2 kΩ dividers or the ADC adapter to clamp signals under 3.3 V before landing on STM32 pins.[^118]
[^makerbase_pinout]: Paolo’s Wolf GT rebuild documented cut/mislabelled MakerBase 75100 conductors and confirmed throttle recovery only after mapping 3.3 V, ground, and ADC1 before rerunning calibration.[^73]
[^can_calibration]: Spintend adapter manual guidance to unplug the slave controller and confirm 60 Ω CAN impedance before throttle calibration prevents error floods.[^74]
[^makerx_ble]: MakerX Jaykup firmware users now power BLE modules from the communication header (5 V/ground + UART2 TX/RX) to avoid browning out the 3.3 V rail.[^75]
[^divider_docs]: Capture and publish divider/adapter schematics for 5 V hall inputs so builders stop over-volting STM32 ADC channels during installs.[^knowledge802]
[^hall-split]: Hall brake handles float at different voltages when paralleled.
  - dedicate one ADC channel per lever and leave the spare brake mechanical if you run out of inputs.[^40]
[^signal-shield]: Running shielded control looms tied to controller ground and routed away from phase wires removed 120 A jitter on Spintend Ubox installs.[^119]
[^signal-clamp]: MiniMotors throttle voltage span and Xiaomi/Magura compatibility lessons shared during ADC integration deep dives.[^120][^121]
[^boosted-map]: Boosted Rev ADC readings (~1.6 V brake to 3.3 V WOT) that yield strong regen and reduced reliance on mechanical brakes.[^122]
[^ninebot-hall]: Ninebot G30 builders transplant the OEM hall puck and magnet into new levers to preserve proportional regen after hydraulic upgrades.[^123]
[^rev-cite]: Shimano Saint + Magura hybrid discussions cautioning against aggressive front regen on low-traction surfaces.[^124]

## Little FOCer & Compact Controller Specifics

- **Little FOCer throttles belong on 3.3 V.** Feeding ADC1 from 5 V left a Little FOCer scooter stuck at WOT; veterans reiterated that idle should sit around 0.6–0.9 V and WOT near 2.5–3.3 V, with halls staying on 5 V while the throttle uses the 3.3 V rail to protect the STM32 input.[^little_focer_3v3]

## VESC Latch & Key Switch Integration

- **Understand VESC latch quirks before wiring key switches.** The logic rail is live whenever the pack is connected, and tying the 5 V switch pin to ground turns the controller off.
  - unlike Flipsky aluminums, which still need external contactors or BMS gating to avoid MOSFET stress.[^vesc_latch]

## ADC App Timeout Safeguards

- **ADC adapter placement and firmware safeguards.** Long throttle runs stayed quiet when riders mounted Spintend's ADC adapter beside the controller (or used shielded cable) and fed 5 V halls through resistor dividers; Vedder's mid-June patch now timeouts ADC-detach scripts so Xiaomi dash integrations can safely hand inputs back to hardware control.[^adc_timeout]

## Brake Light Wiring

- **Understand brake light output behavior.** One rider's 12 V tail lamp powered up via the ADC V2 adapter (ground/12 V/brake leads) but never entered brake mode, underscoring the need to clarify how the board sinks brake current and which firmware settings drive the output.[^brake_light_wiring]
- **Remember the ADC harness switches positive.** The brake output sources pack voltage and shares ground with the headlight, so tie lamp anodes to the function pins and cathodes to ground; add diodes or resistors when combining tail and brake channels to prevent backfeeding.[^adc-high-side]

## Connector & Meter Safety Reminders

- **Probe before you plug.** Three-pin throttle harnesses expect a 5 V or 3.3 V feed, ground, and a ≤3.3 V signal.
  - meter the pins before connecting and double-check the multimeter range so continuity mode doesn’t short the rail while you test.[^125]
- **Match connector families to current.** The crew now caps XT90 service around ~100 A bursts (10–20 s) and steps up to XT150 or QS8 anti-spark plugs above 120 A so housings and resistors survive launch current; roll that rule of thumb into build checklists.[^126]

## Source Notes (continued)

[^little_focer_3v3]: Little FOCer throttle voltage requirements and WOT prevention.[^127][^128]
[^vesc_latch]: VESC latch behavior and key switch wiring considerations.[^129]
[^adc_timeout]: ADC adapter placement, shielding, and firmware timeout safeguards.[^66]
[^brake_light_wiring]: Brake light wiring confusion on ADC V2 adapter.[^130]


## References

[^1]: Source: data/vesc_help_group/text_slices/input_part013.txt†L5211-L5213
[^2]: Source: knowledge/notes/input_part004_review.md†L202-L202
[^3]: Source: knowledge/notes/input_part013_review.md†L329-L334
[^4]: Source: data/vesc_help_group/text_slices/input_part013.txt†L17274-L17280
[^5]: Source: data/vesc_help_group/text_slices/input_part013.txt†L17767-L17776
[^6]: Source: data/vesc_help_group/text_slices/input_part013.txt†L17838-L17843
[^7]: Source: data/vesc_help_group/text_slices/input_part013.txt†L18297-L18305
[^8]: Source: knowledge/notes/input_part002_review.md†L437-L439
[^9]: Source: knowledge/notes/input_part012_review.md†L101-L101
[^10]: Source: knowledge/notes/input_part000_review.md†L461-L464
[^knowledge802]: Source: knowledge/notes/input_part000_review.md†L802-L802
[^11]: Source: knowledge/notes/input_part011_review.md†L333-L341
[^12]: Source: data/vesc_help_group/text_slices/input_part011.txt†L8001-L8012
[^13]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8424-L8453
[^14]: Source: knowledge/notes/input_part011_review.md†L372-L377
[^15]: Source: knowledge/notes/input_part011_review.md†L318-L332
[^16]: Source: knowledge/notes/input_part000_review.md†L82-L84
[^17]: Source: data/vesc_help_group/text_slices/input_part005.txt†L21844-L21933
[^18]: Source: data/vesc_help_group/text_slices/input_part005.txt†L22481-L22495
[^19]: Source: knowledge/notes/input_part013_review.md†L105-L105
[^20]: Source: data/vesc_help_group/text_slices/input_part005.txt†L23069-L23093
[^21]: Source: knowledge/notes/input_part010_review.md†L321-L322
[^22]: Source: knowledge/notes/input_part004_review.md†L328-L328
[^23]: Source: knowledge/notes/input_part012_review.md†L312-L312
[^24]: Source: knowledge/notes/input_part012_review.md†L329-L329
[^25]: Source: knowledge/notes/input_part009_review.md†L270-L270
[^26]: Source: data/vesc_help_group/text_slices/input_part013.txt†L6378-L6381
[^27]: Source: knowledge/notes/input_part001_review.md†L504-L505
[^28]: Source: knowledge/notes/input_part002_review.md†L15-L17
[^29]: Source: knowledge/notes/input_part003_review.md†L165-L165
[^30]: Source: data/vesc_help_group/text_slices/input_part004.txt†L3814-L3833
[^31]: Source: data/vesc_help_group/text_slices/input_part013.txt†L18155-L18160
[^32]: Source: data/vesc_help_group/text_slices/input_part013.txt†L18483-L18487
[^33]: Source: data/vesc_help_group/text_slices/input_part001.txt†L3494-L3605
[^34]: Source: knowledge/notes/input_part011_review.md†L435-L437
[^35]: Source: data/vesc_help_group/text_slices/input_part001.txt†L6481-L6504
[^36]: Source: data/vesc_help_group/text_slices/input_part013.txt†L6065-L6114
[^37]: Source: data/vesc_help_group/text_slices/input_part013.txt†L6363-L6377
[^38]: Source: knowledge/notes/input_part000_review.md†L39-L39
[^39]: Source: knowledge/notes/input_part000_review.md†L518-L524
[^40]: Source: knowledge/notes/input_part000_review.md†L335-L337
[^41]: Source: knowledge/notes/input_part011_review.md†L22-L23
[^42]: Source: knowledge/notes/input_part011_review.md†L23-L24
[^43]: Source: knowledge/notes/input_part011_review.md†L496-L498
[^72]: Source: knowledge/notes/input_part003_review.md†L513-L515
[^73]: Source: knowledge/notes/input_part003_review.md†L554-L554
[^74]: Source: knowledge/notes/input_part003_review.md†L553-L553
[^75]: Source: knowledge/notes/input_part003_review.md†L552-L553
[^flipsky-3wire-pas]: Source: knowledge/notes/input_part010_review.md†L703-L704
[^44]: Source: knowledge/notes/input_part001_review.md†L512-L514
[^45]: Source: knowledge/notes/input_part001_review.md†L646-L647
[^46]: Source: knowledge/notes/input_part013_review.md†L206-L206
[^47]: Source: knowledge/notes/input_part013_review.md†L212-L212
[^48]: Source: knowledge/notes/input_part001_review.md†L552-L553
[^49]: Source: knowledge/notes/input_part001_review.md†L580-L581
[^50]: Source: knowledge/notes/input_part001_review.md†L648-L648
[^51]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11240-L11257
[^52]: Source: data/vesc_help_group/text_slices/input_part000.txt†L17625-L17654
[^53]: Source: data/vesc_help_group/text_slices/input_part000.txt†L18388-L18395
[^54]: Source: data/vesc_help_group/text_slices/input_part004.txt†L8138-L8144
[^55]: Source: knowledge/notes/input_part011_review.md†L343-L349
[^56]: Source: data/vesc_help_group/text_slices/input_part004.txt†L9519-L9545
[^57]: Source: knowledge/notes/input_part013_review.md†L775-L775
[^58]: Source: data/vesc_help_group/text_slices/input_part003.txt†L15008-L15017
[^59]: Source: knowledge/notes/input_part001_review.md†L508-L510
[^60]: Source: data/vesc_help_group/text_slices/input_part013.txt†L5805-L5813
[^61]: Spintend ADC adapter reminder that the kill loop is limited to ≈60 V and should only switch JK/ANT-style logic buttons while real pack isolation stays on external hardware. Source: data/vesc_help_group/text_slices/input_part005.txt†L24198-L24224; L24281-L24282.
[^62]: Source: knowledge/notes/input_part014_review.md†L5313-L5316
[^63]: Source: knowledge/notes/input_part005_review.md†L434-L436
[^64]: Source: knowledge/notes/input_part003_review.md†L248-L248
[^65]: Source: data/vesc_help_group/text_slices/input_part003.txt†L21692-L21726
[^66]: Source: knowledge/notes/input_part004_review.md†L286-L286
[^67]: Source: data/vesc_help_group/text_slices/input_part004.txt†L16000-L16009
[^68]: Source: data/vesc_help_group/text_slices/input_part004.txt†L16959-L16968
[^69]: Source: data/vesc_help_group/text_slices/input_part002.txt†L26222-L26279
[^70]: Source: data/vesc_help_group/text_slices/input_part002.txt†L27334-L27368
[^71]: Source: data/vesc_help_group/text_slices/input_part000.txt†L18335-L18382
[^72]: Source: data/vesc_help_group/text_slices/input_part000.txt†L18423-L18444
[^73]: Source: knowledge/notes/input_part000_review.md†L707-L715
[^74]: Source: knowledge/notes/input_part000_review.md†L748-L748
[^75]: Source: knowledge/notes/input_part005_review.md†L432-L434
[^76]: Source: knowledge/notes/input_part000_review.md†L648-L648
[^77]: Source: knowledge/notes/input_part012_review.md†L11-L13
[^78]: Source: knowledge/notes/input_part007_review.md†L47-L47
[^79]: Source: knowledge/notes/input_part007_review.md†L221-L221
[^80]: Source: knowledge/notes/input_part012_review.md†L357-L359
[^81]: Source: knowledge/notes/input_part012_review.md†L13-L13
[^82]: Source: knowledge/notes/input_part012_review.md†L93-L94
[^83]: Source: knowledge/notes/input_part007_review.md†L239-L240
[^84]: Source: knowledge/notes/input_part012_review.md†L104-L104
[^85]: Source: knowledge/notes/input_part005_review.md†L58-L58
[^86]: Source: knowledge/notes/input_part009_review.md†L15-L15
[^87]: Source: knowledge/notes/input_part012_review.md†L173-L173
[^88]: Source: knowledge/notes/input_part012_review.md†L181-L181
[^89]: Source: knowledge/notes/input_part012_review.md†L137-L137
[^90]: Source: knowledge/notes/input_part007_review.md†L226-L226
[^91]: Source: knowledge/notes/input_part012_review.md†L395-L395
[^92]: Source: knowledge/notes/input_part012_review.md†L248-L248
[^93]: Source: knowledge/notes/input_part012_review.md†L258-L258
[^94]: Source: knowledge/notes/input_part005_review.md†L348-L350
[^95]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24198-L24224
[^96]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24281-L24282
[^97]: Source: knowledge/notes/input_part007_review.md†L223-L223
[^98]: Source: knowledge/notes/input_part007_review.md†L225-L225
[^99]: Source: knowledge/notes/input_part005_review.md†L410-L413
[^100]: Source: knowledge/notes/input_part001_review.md†L15-L16
[^101]: Source: knowledge/notes/input_part011_review.md†L659-L660
[^102]: Source: knowledge/notes/input_part010_review.md†L74-L77
[^103]: Source: data/vesc_help_group/text_slices/input_part011.txt†L11899-L11907
[^104]: Source: data/vesc_help_group/text_slices/input_part011.txt†L12376-L12381
[^105]: Source: knowledge/notes/input_part008_review.md†L84-L86
[^106]: Source: knowledge/notes/input_part008_review.md†L85-L85
[^107]: Source: knowledge/notes/input_part008_review.md†L86-L86
[^108]: Source: knowledge/notes/input_part009_review.md†L14-L14
[^109]: Source: knowledge/notes/input_part009_review.md†L12-L13
[^110]: Source: knowledge/notes/input_part014_review.md†L85-L86
[^111]: Source: knowledge/notes/input_part008_review.md†L21846-L21848
[^adapter-idle-source]: Source: knowledge/notes/input_part008_review.md†L485-L485
[^112]: Source: data/vesc_help_group/text_slices/input_part014.txt†L6907-L6913
[^113]: Source: knowledge/notes/input_part011_review.md†L16211-L16217
[^114]: Source: knowledge/notes/input_part000_review.md†L113-L113
[^115]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11240-L11283
[^116]: Source: knowledge/notes/input_part000_review.md†L206-L206
[^117]: Source: knowledge/notes/input_part000_review.md†L297-L297
[^118]: Source: knowledge/notes/input_part000_review.md†L335-L336
[^119]: Source: knowledge/notes/input_part000_review.md†L258-L258
[^120]: Source: knowledge/notes/input_part000_review.md†L259-L259
[^121]: Source: knowledge/notes/input_part000_review.md†L299-L299
[^122]: Source: knowledge/notes/input_part000_review.md†L246-L246
[^123]: Source: knowledge/notes/input_part000_review.md†L296-L296
[^124]: Source: knowledge/notes/input_part000_review.md†L207-L207
[^125]: Source: knowledge/notes/input_part013_review.md†L166-L168
[^126]: Source: knowledge/notes/input_part013_review.md†L168-L168
[^127]: Source: knowledge/notes/input_part004_review.md†L18-L18
[^128]: Source: knowledge/notes/input_part004_review.md†L90-L90
[^129]: Source: knowledge/notes/input_part004_review.md†L56-L56
[^130]: Source: knowledge/notes/input_part004_review.md†L352-L352
