# VESC ADC & Accessory Power Integration Playbook

## TL;DR
- Wire throttles, brakes, and regen controls straight into the controller’s ADC pins and keep everything on 3.3 V logic—dash adapters and 5 V accessories routinely add lag or kill channels when they fail.[^1][^2][^4]
- Treat the Spintend/MakerX auxiliary board as a low-current signal bridge: its ~12 V/3 A rail can light LEDs or run logic, but headlamps, horns, and pumps still need a dedicated DC/DC or relay-fed supply.[^3][^9][^10][^11]
- Map and validate every analog input inside VESC Tool before sealing the deck; enabling ADC control blocks bench FWD/REV overrides, so miswired harnesses must be fixed before ride testing.[^7][^8][^13]
- Protect logic rails by isolating accessory power, adding pull-down failsafes, and avoiding shared 5 V lines between controllers—shorts or ground loops keep blowing MOSFET drivers and display boards.[^14][^16][^17][^19]

## Signal & Power Budget Cheatsheet
| Channel | Voltage | Continuous Current | Typical Uses | Guardrails |
| --- | --- | --- | --- | --- |
| ADC1 / ADC2 (signal) | 3.3 V reference | ≈1 mA (input) | Throttle, brake, regen slider | Stay on 3.3 V hall outputs or add dividers/pull-downs so open circuits fall to zero.[^1][^4][^19] |
| Spintend ADC v3 accessory rail | 12 V (buck) | ≈3 A total | Tail lights, brake triggers, small relays | Parallel 18 W lamps already flirt with the limit—push heavier loads through an external converter.[^3][^10] |
| Controller logic rail | 5 V from onboard DC/DC | <0.5 A budget | Displays, hall sensors, footpads | Never back-feed from other controllers or dashes; a single short can blow the logic board.[^14][^16] |
| External DC/DC (recommended) | Pack → 12 V/5 V | Sized to load | Headlights, horns, pumps, fans | Use relays or MOSFETs triggered by the ADC board for safe switching.[^9][^11][^15] |

## Wiring Recipes
### Throttles & Brakes
1. **Direct hall wiring:** Route throttle and brake halls straight to ADC1/ADC2 signal, 3.3 V, and ground to keep control even when the OEM dash is removed.[^1] Keep the sensors on the controller’s 3.3 V rail—feeding 5 V halls directly into STM32 ADCs has already killed logic stages.【F:knowledge/notes/input_part000_review.md†L82-L84】
2. **Spin-Y & other multi-button throttles:** Version 1 units need custom JST‑1.0 leads into ADC2/COMM2; version 2 ships with a four-conductor harness that lands cleanly on the adapter board.[^2]
3. **Spin-Y2 quirks on dual Ubox:** Some firmware ships with ESC A’s ADC1 disabled—moving the Spin-Y2 lead to ESC B’s ADC1 and feeding it 5 V restored output on Dualtron conversions.【F:knowledge/notes/input_part008_review.md†L337-L337】
4. **Spintend adapter v3 harness:** Modern boards arrive with keyed plugs—no more screw terminals—so match the supplied loom instead of hand-crimping tiny JST shells.[^3]
5. **MakerX footpads & 3.3 V-only sensors:** Confirm both ADC rails output 3.3 V before blaming pads; swapping to 5 V kills the hall board.[^4]
6. **Interpret ADC counts, not raw voltage:** VESC Tool reports hall inputs as 0–4095 counts—track the delta between idle and full throw, and if readings compress, repeat the test with a stable 5 V source to rule out noisy 3.3 V regulators before replacing sensors; Spintend’s adapter manual expects ~0.8 V idle, so stop and rewire if a channel sits near 3 V.[^22][^adapter-idle]
7. **Pre-measure Spin-Y signal voltage:** Makerbase 75100 owners now meter the Spin-Y signal before plugging into ADC—anything above ~3.8 V risks killing the STM32, so test the harness while powering it from the controller’s 5 V rail.【F:knowledge/notes/input_part008_review.md†L339-L339】
8. **Troubleshoot Spin-Y2 reboots systematically:** When the Spin-Y2 throttle reboots a Spintend build, work through firmware reflashes, BMS health checks, a fresh motor detection, and ADC wiring inspection before blaming the hardware; that sequence solved Alex’s repeat cut-outs.【F:knowledge/notes/input_part008_review.md†L617-L623】
8. **Filter noise in software first:** Builders tamed runaway triggers by compressing throttle activation to ~0.83–1.2 V inside VESC Tool rather than rewiring hardware; chassis grounding tricks have also helped but carry short-to-frame risk if insulation fails.[^adc-noise]
8. **Fail-safe defaults:** Add a pull-down resistor from throttle signal to ground so any broken wire snaps to zero instead of ghost acceleration.[^19]
9. **Legacy dash retention:** Leaving throttle through a dash adapter adds perceptible lag; many builders keep the dash for display only and wire throttles directly to the controller instead.[^20]
10. **Refresh mappings after downtime.** Scooters that sat for months have thrown false brake/throttle behaviour until riders reran the ADC wizard and removed stale inversion flags inside VESC Tool.[^storage-cal]
11. **Monitor brake sensors.** Dead brake halls make some VESC scooters pulse the motor every second or two under throttle, so replace failed sensors before ride testing.【F:knowledge/notes/input_part000_review.md†L39-L39】

### Regen Buttons & Variable Brakes
- **Momentary button recipe:** Wire the button between ADC2 signal and the 3.3 V rail; avoid series resistors because they created “stuck brake” faults in testing.[^6]
- **Analog lever mapping:** Run the ADC calibration wizard, keep the window open while sweeping the lever, then assign the channel to “Current (No Reverse)” so regen ramps in with negative motor/battery limits.[^7][^8]

### Lighting, Horns & Aux Loads
- **Use the adapter as logic, not power:** The horn output only sources a couple of amps—enough for low-power buzzers but not vintage 35 W halogens—so trigger a relay or MOSFET that pulls from a beefier DC/DC converter.[^9][^10]
- **85250 & Ubox installs:** Route brake-light logic through the ADC breakout, but feed lamps from a separate converter so you don’t brown out the controller when multiple 12 V loads fire at once.[^11]
- **Share lamps carefully:** Builders isolated the Spintend adapter’s “reverse” feed with a diode and paralleled the final lead with the headlight circuit so a single lamp could serve both functions without back-feeding the controller.[^spintend-diodes]
- **Mind the CAN-adjacent aux port:** The auxiliary pin beside the CAN header stays hot until the controller shuts down—pull switched power from the dash harness if you don’t want lights glowing with the scooter off.[^aux-port]
- **TF100 & OEM switch pods:** Reuse factory throttles by landing the red/black hall power and the green signal lead on a 3.3 V ADC input; this preserves dash ergonomics without custom PCBs.[^12]
- **Skip illuminated combo pods:** Backlit handlebar switches feed accessory voltage into the signal lines and confuse the ADC board unless you gut the lighting—treat them as incompatible without a full rewire.[^24]
- **Avoid parasitic taps:** Pulling 12 V from internal headlight pins (e.g., X12) drags the logic rail and costs range—draw pack power into a dedicated converter instead.[^15]
- **Protect logic rails:** Shorting auxiliary leads straight on the controller board has already destroyed logic stages; isolate accessories and fuse every feed.[^16]
- **Fuse the adapter output:** One builder shorted the 12 V rail on a brand-new Spintend 85240 while wiring lights and killed the buck stage; add inline fuses or external bucks so a single mistake doesn’t scrap the controller.[^16][^23]
- **Treat buttons as triggers only:** The ADC adapter does not replace a loop key or smart-BMS latch; plan a real kill switch for theft deterrence or maintenance.[^17][^18]
- **Dash coexistence proven:** The same build ran the Spintend ADC bridge on ADC1/ADC2 while keeping the Xiaomi dash on UART, confirming the adapter and stock display can share the harness when power is planned correctly.[^dash-coexist]
- **Reuse Xiaomi dashes safely:** Dual 75100 Xiaomi Pro 2 builds keep the stock dash for telemetry, wire the throttle straight to ADC for traction control, and splice lighting into AUX power with series resistors to protect LEDs.【F:knowledge/notes/input_part008_review.md†L338-L338】
- **Add pull-downs to custom dash buttons:** 1Zuna’s CAN dash needed a 1 k–1.2 k resistor inline with the button harness to stop ghost presses; solder it into the loom so the dash works on both G30 and Makerbase ESCs.【F:knowledge/notes/input_part008_review.md†L340-L340】

## Configuration & Validation Workflow
1. **Bench prep:** Wire controls with the pack off, confirm continuity, and verify 3.3 V and 5 V rails before powering up.
2. **Calibrate ADC inputs:** In VESC Tool, run the ADC mapping wizard for each channel, noting min/max values and checking that neutral centers correctly.[^7]
3. **Assign app functions:** Map ADC1 to throttle, ADC2 to “Current No Reverse” for regen, and ensure throttle curves or safe-start options suit the rider.[^8]
4. **Cap speeds per CAN node when scripting dual controllers:** Dual-ADC Lisp scripts let one 75100 run past 20 km/h limits until builders set explicit speed caps on both CAN addresses for Ninebot conversions.【F:knowledge/notes/input_part008_review.md†L391-L391】
4. **Understand bench limitations:** Once ADC control is enabled, the manual FWD/REV buttons in VESC Tool stop working—switch the app to UART or disable ADC temporarily for bench spins.[^13]
5. **Write configs explicitly:** Mobile reconnects and desktop wizards can wipe ADC settings unless you press “Write Motor Config” and “Write App Config” after every change.[^21]
6. **Log shakedowns:** Capture CAN or USB logs on the first rides to confirm commanded vs. actual current and verify regen ramps without triggering BMS cutoffs.[^11]
7. **Plan speed telemetry when running sensorless.** VESC back-EMF estimation continues to report speed without halls, but freewheeling geared hubs may still need external sensors or GPS once you coast off throttle—verify your logging plan before pulling sensors entirely.【F:knowledge/notes/input_part008_review.md†L617-L623】

## Small-Format & Youth Scooter Notes
- Mini VESC 6-FET controllers still need at least 7 S supply to replace brushed ESCs cleanly; when budgets are tight, programmable Hobbywing or Traxxas brushed ESCs cover 1 S–18 S / 0.5–500 A but often cost as much as entry VESC hardware.【F:knowledge/notes/input_part008_review.md†L240-L241】
- Refurbishing lead-acid kid scooters with 5 S lithium and keeping top speed near 15 mph preserves safety while adding real throttles and lighting upgrades—validate throttle wiring on ADCs before handing scooters back to families.【F:knowledge/notes/input_part008_review.md†L241-L242】

## Safety & Troubleshooting Checklist
- **Separate controller rails:** Do not tie CAN-connected controllers’ 5 V rails together unless they share the same ignition path; mismatched power buttons have already killed hardware.[^14]
- **Keep kill-switch redundancy:** Combine Safe Start, loop keys, and/or smart-BMS latches so thieves or techs can de-energise the scooter without relying on ADC buttons alone.[^17]
- **Watch for brownouts:** Builds that still depend on Makerbase/Flipsky rails should budget extra capacitance or buffer packs—the same rail that feeds ADC accessories is the one that dies during BMS trips.[^10]
- **If a channel dies:** Check for 3.3 V on the sensor, rerun ADC mapping, inspect JST orientation, and confirm the pull-down still measures the expected resistance.[^7][^19]
- **Verify CAN dashboards after firmware tweaks:** Dual 75100 riders heard rough motors and lost CAN speed readings until they reran motor detection and rescaled dashboards on firmware 6.05.【F:knowledge/notes/input_part008_review.md†L390-L390】
- **Document 2WD toggles clearly:** On-the-fly two-wheel-drive switches either feed Spintend’s ADC adapter from the 12 V rail or drive an Arduino running the UART `setCurrent` example to drop the front motor to 0 A when pressed.【F:knowledge/notes/input_part008_review.md†L392-L392】
- **Map Flipsky 75350 controls carefully:** Keep throttle on ADC1 and the brake switch on ADC2 with “Current No Reverse Brake ADC2” enabled, and avoid tying 5 V hall rails between controllers unless absolutely necessary.【F:knowledge/notes/input_part008_review.md†L317-L317】

## Source Notes
[^1]: Routing throttle and brake halls directly into ADC1/ADC2 preserves control without the OEM dash.【F:knowledge/notes/input_part012_review.md†L11-L13】
[^2]: Spin Y throttle versions and wiring expectations for Spintend/Ubox adapters.【F:knowledge/notes/input_part007_review.md†L47-L47】
[^3]: Spintend v3 adapter now ships with keyed harness connectors.【F:knowledge/notes/input_part007_review.md†L221-L221】
[^4]: MakerX S100 footpads require the controller’s 3.3 V rail and fail on 5 V feeds.【F:knowledge/notes/input_part012_review.md†L255-L255】
[^6]: Regen button tied directly between ADC2 and 3.3 V without series resistors eliminated false braking faults.【F:knowledge/notes/input_part012_review.md†L13-L13】
[^7]: ADC calibration workflow and reminder to let VESC Tool find neutral before assigning functions.【F:knowledge/notes/input_part012_review.md†L93-L94】
[^8]: Regen mapping best practices from community quick-start guides.【F:knowledge/notes/input_part007_review.md†L239-L240】
[^9]: Horn output current limit cautions on Makerbase/Spintend harnesses.【F:knowledge/notes/input_part012_review.md†L97-L97】
[^10]: Spintend ADC aux outputs top out around 12 V / 3 A and need DC/DC help for bigger loads.【F:knowledge/notes/input_part005_review.md†L58-L58】
[^11]: Smart Repair’s 85250 guidance—use the ADC board for logic and a DC/DC converter for lamp current.【F:knowledge/notes/input_part012_review.md†L173-L173】
[^12]: TF100 throttle wiring recipe using the controller’s 3.3 V hall supply.【F:knowledge/notes/input_part012_review.md†L174-L174】
[^13]: Enabling ADC control disables manual FWD/REV overrides inside VESC Tool until you switch apps.【F:knowledge/notes/input_part012_review.md†L137-L137】
[^14]: CAN-linked controllers should not share 5 V rails; doing so has already killed boards.【F:knowledge/notes/input_part007_review.md†L226-L226】
[^15]: Drawing accessory power from the X12 headlight feed drags the logic rail and wastes energy.【F:knowledge/notes/input_part012_review.md†L395-L395】
[^16]: Shorting controller auxiliary leads has destroyed logic boards, proving the need for isolated accessory supplies.【F:knowledge/notes/input_part012_review.md†L248-L248】
[^17]: Builders still rely on loop keys, smart-BMS buttons, and Safe Start—ADC boards alone do not provide a true kill switch.【F:knowledge/notes/input_part005_review.md†L348-L350】
[^18]: Spintend’s ADC adapter v2 only ferries 5 V/12 V accessory power and cannot act as an anti-spark or ignition switch.【F:knowledge/notes/input_part005_review.md†L254-L254】
[^19]: Pull-down resistors on throttle lines guarantee a zero output if the signal wire opens.【F:knowledge/notes/input_part007_review.md†L223-L223】
[^20]: Routing throttle through dash adapters adds noticeable lag; direct ADC wiring restores responsiveness.【F:knowledge/notes/input_part007_review.md†L225-L225】
[^21]: VESC Tool can wipe ADC settings after reconnects unless you explicitly write both motor and app configs.【F:knowledge/notes/input_part005_review.md†L573-L573】
[^22]: Hall-diagnostics workflow focusing on ADC count deltas and re-testing with a clean 5 V rail when noisy 3.3 V supplies flatten readings.【F:knowledge/notes/input_part001_review.md†L15-L16】
[^23]: Shorting the Spintend 85240 aux rail to ground killed the unfused buck regulator, reinforcing the need for inline fuses or external converters when powering lighting from the adapter.【F:knowledge/notes/input_part011_review.md†L659-L660】
[^24]: Illuminated AliExpress switch pods leak voltage into ADC signal lines and require major rewiring to behave.【F:knowledge/notes/input_part010_review.md†L74-L77】
[^spintend-diodes]: Smart Repair’s wiring log shows the Spintend ADC adapter happily sharing a single lamp when the reverse feed is diode-isolated and paralleled with the headlight output.【F:knowledge/notes/input_part008_review.md†L84-L86】
[^aux-port]: 🇪🇸AYO#74 warned that the auxiliary port beside the CAN header stays powered until shutdown, so tapping it leaves lights on unless you add a dedicated switch.【F:knowledge/notes/input_part008_review.md†L85-L85】
[^dash-coexist]: The same build ran the Spintend adapter on ADC1/ADC2 and left the Xiaomi dash on UART without conflicts once wiring was tidied.【F:knowledge/notes/input_part008_review.md†L86-L86】
[^adc-noise]: Compressing throttle activation windows to ~0.83–1.2 V cleared ADC-trigger noise on Spintend builds; some riders grounded the chassis for extra stability but warn the practice risks shorts if insulation fails.【F:knowledge/notes/input_part014_review.md†L85-L86】
[^adapter-idle]: Spintend’s adapter manual targets ~0.8 V idle readings—seeing ~3 V idle means the channel is wired wrong and will act like a stuck brake.【F:knowledge/notes/input_part008_review.md†L21846-L21848】
[^storage-cal]: Re-running the ADC wizard and clearing stale inversion flags resolved Xiaomi brake/throttle glitches after long storage.【F:knowledge/notes/input_part011_review.md†L16211-L16217】
