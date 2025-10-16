# Throttle and Brake Signal Integration

## Brake Sensor Requirements

- Faulty or missing brake sensors can cause rhythmic surging every one to two seconds under throttle, so maintaining functional brake inputs is critical before road testing.[^brake_surge]
- Two-wire reed assemblies (Nutt, generic) still need a 5–10 kΩ pull-up to your logic rail when feeding VESC ADC inputs; treat them as dry contacts, not hall sensors, and plan external 12 V feeds if the controller’s accessory rail is weak.[^brake_wiring_basics]

## Proportional Braking Hardware

- Most OEM scooter levers ship as digital on/off switches; swapping to hall-based levers (Xiaomi-style or custom SS49E housings epoxied to hydraulic bodies) gives SmartDisplay/ADC stacks an analog pull to blend regen with mechanical braking instead of pulsing the motor.[^analog_braking]
- Magura’s MT5e line still defaults to a microswitch.
  - builders are pivoting to Shimano Deore M6100/M6120 kits or adding hall-effect pucks while configuring the Spintend ADC board’s normally-open/closed toggles for compatibility.[^magura_options]
- Recent comparisons peg Shimano’s four-piston Saint/M7120 kits (~€155 without rotors) as the stiffest one-finger lever option, while MT5 bundles (≈€192 with discs) remain attractive if you add metal lever blades and separate pads; keep in mind that Magura reservoirs can crack under extreme downhill loads.[^1]
- When instrumenting lever output, power the hall assembly with 5 V and probe the signal wire under load; multimeters alone show no activity without the supply rail energized.[^lever_power]
- Magura confirmed the MT5e lever family ships in two SKUs.
  - 2700985 (normally closed) and 2700984 (normally open/Higo “Closer”)
  - and the Spintend ADC board lets you flip between switch or hall sensing plus 5 V/3.3 V output, so match the lever code before terminating harnesses.[^mt5e_skus]
- Brake-light integration still drives lever choice: some riders keep Nutt levers solely for the switch while running Magura calipers, whereas the MT5e’s HIGO harness remains the cleanest plug-and-play option when budgets allow.[^2]
- Front-only regen testing on light scooters still locks wheels on low-traction surfaces; veterans either limit the front battery target or disable it entirely once “Shigura” hybrids are installed.[^front_regen]
- Lock-ring grip pods with tactile turn buttons mimic VSETT controls at a fraction of OEM cost, trading a bit of mass for better commuter ergonomics once wired into the ADC board.[^3]

## Variable Regen Hardware Experiments

- Builders chasing proportional braking often add a second throttle or dedicated hall-sensor brake lever for regen; VESC firmware still forces a binary choice between cutoff or proportional mode, while Nucular owners remap CAN brake ports so they keep both mechanical cutoffs and variable regen on the same lever.[^regen_hardware]
- Demand for purpose-built controls remains high—Spintend is prototyping a “curve” thumbwheel to mimic Rion’s dual-action throttle so regen scales smoothly without sacrificing the main trigger.[^ip001-curve]
- Dedicated regen levers dramatically cut rotor heat and brake fade, but riders still keep mechanical brakes ready for emergencies—especially at full charge when limited voltage headroom weakens regen authority.[^regen_heatdrop]

## Signal Conditioning Hardware

- The "smartcontroller" accessory intercepts 0–5 V throttle and brake signals, outputs a 0–3.3 V DAC feed to the VESC, and enforces features such as anti-theft throttle lockouts and safe MiniMotors EYE compatibility.[^smartcontroller_overview]
- DIY adopters should budget ~€150 for parts, R&D, and shipping plus their own 3D-printed enclosures and FPC soldering work; upcoming revisions aim for 100 V regulators and native EYE throttle support.[^smartcontroller_costs]
- Switching to a 3.5″ VA TFT with anti-glare glass improves daylight visibility, though the present PNP dimmer burns ~130 mA at idle and heats the PCB to ~52 °C inside the housing.[^smartcontroller_display]

## Voltage Level Management

- Feed VESC ADC pins with the 3.3 V reference (or a level-shift board); direct 5 V throttle outputs risk destroying the STM32 ADC even when sensors like the SS49E prefer 5 V supply.[^adc_limit]
- Operating Honeywell SS49E throttles at 3.3 V introduces ~0.02 V noise that can be handled via software deadband or filtering without resorting to extra capacitors.[^adc_noise]
- Builders who retain 5 V throttle power divide the signal using 1 kΩ/2 kΩ resistors or source native 3.3 V sensors; some bargain throttles output zero volts at 3.3 V and therefore require a dedicated level shifter.[^signal_divider]
- Residual ~0.15 V ripple after scaling can be smoothed through VESC deadband configuration instead of hardware changes.[^signal_deadband]
- MiniMotors EYE triggers swing roughly 0.8–4.1 V, so resistor dividers or ADC adapters must clamp the signal below 3.3 V before it reaches the STM32 input.[^mini_eye]
- Xiaomi hall levers happily share 5 V/GND rails with other sensors, but pairing them directly with normally-open Magura hydraulics leaves floating outputs.
  - add a hall puck to the hydraulic lever or dedicate separate channels.[^mixed_levers]

## Throttle & Harness Maintenance

- Sudden surging that mimics hall dropout has traced back to cracked plastic throttles; soldering hall connectors directly and upgrading to higher-quality throttles restored smooth acceleration on high-current builds.[^throttle_failure]
- Xiaomi-style thumb throttles remain the ergonomic favourite—builders trim their long dead zones by recalibrating VESC min/max voltage and often add left-hand triggers for dedicated regen inputs.[^ip001-xiaomi-cal]
- Cheap AliExpress hall triggers still ship with 20–30 % dead travel and sore thumbs; Domino 270X units feel better yet remain imperfect, underscoring the need for higher-quality halls or curve tuning when chasing precise control.[^ip001-domino]

## Dual-Action Throttle Prototypes

- Scroll-wheel throttles like the Rion Curve remain in high demand; Spintend users are prototyping remotes that relocate the wheel and display to mimic dual-action ergonomics while they wait for production hardware to return.[^scroll_prototype]
- Community experiments split trigger travel into roughly 70 % throttle / 30 % regen or add dual springs, curved magnets, and even pressure sensors under the trigger to deliver proportional braking without sacrificing grip.[^scroll_experiments]

## Regen Safety Guidelines

- Bench testing confirmed that even light regen (-15 A motor / -5 A battery) can trip controllers when wheels spin unloaded.
  - treat test benches like live rides and disable regen until a real pack is connected.[^bench_trip]
- Cap battery regen near the pack’s amp-hour value (e.g., ≤50 A on a 50 Ah pack) and leave roughly 15 A of extra controller “reverb” overhead so the FETs, not the cells, dissipate surges during aggressive braking.[^regen_ratio]
- Laboratory power supplies lack internal resistance, so unloaded regen spikes can exceed supply voltage; rely on real batteries or load banks when validating braking tunes.[^lab_supply]
- Koxx’s baseline for dual-motor commuters lands near −30 A battery/−80 A phase on the rear and −25 A/−55 A on the front, balancing strong braking with controller safety; log stator temps during early shakedowns.[^baseline_regen]
- Field tests on a 10 S 2 P P42A pack produced 2.55 kW regen bursts and rapid motor/MOSFET heating, reinforcing why aggressive profiles need live temperature logging rather than bench guesses.[^regen_heat]
- Recent 22 S tuning notes keep battery regen near 3 A per cell and phase braking around 70 % of forward phase limits, easing adjustments in small increments and pairing strong regen with a dedicated throttle so mechanical brakes stay healthy.[^regen_phase_ratio]
- Riders reminded each other that regen-only configurations are unsafe on 20 S builds.
  - keep mechanical brakes adjusted and in service before trusting wheel-locking e-brakes at 50–65 km/h.[^4]
- Leaving a small negative battery current target keeps lever-based e-brakes alive; setting regen to zero disables the switch entirely, so balance throttle curves with ADC apps on 6.05+ firmware instead of relying on legacy remote settings.[^regen_negative_current]
- Regen ripple around −110 A phase / −15 A battery has already caused brake stutter and voltage spikes—raise battery regen limits gradually, balance currents front to rear, and verify mechanical brakes can take over if electronic braking falters.[^regen_ripple]

## Throttle Voltage Maps & Calibration

- Boosted Rev thumbwheels measure ≈1.6 V at full brake, 2.54 V at neutral, and 3.3 V wide open once wired to VESC ADC inputs, delivering enough regen that some riders rarely touch mechanical brakes.[^boosted_profile]
- Sensor suites that mix ADC throttles and SmartDisplay UART stay stable when the loom uses shielded cable tied to controller ground and routed away from phase leads, which also eliminated cruise-control jitter at 120 A phase.[^shielded_looms]
- Polish-built hall triggers from e-bikestuff ship with a 0.96–4.31 V sweep, zero deadband, and VESC-adjustable endpoints.
  - premium alternatives to Xiaomi/Zero throttles if you can stomach shipping costs.[^5]

## Pedal Assist Integration

- Torque-sensing bottom brackets like the eRider T9N only swing 1.5–3.3 V in quick spikes; add ADC filtering or external microcontroller smoothing when blending PAS with throttle on high-power builds so the controller doesn’t misinterpret short bursts.[^pas_calibration]


[^brake_surge]: Source: knowledge/notes/input_part000_review.md, line 39.
[^analog_braking]: Source: knowledge/notes/input_part000_review.md, line 114.
[^magura_options]: Source: knowledge/notes/input_part000_review.md, line 173.
[^lever_power]: Source: knowledge/notes/input_part000_review.md, line 174.
[^smartcontroller_overview]: Source: knowledge/notes/input_part000_review.md, line 78.
[^smartcontroller_costs]: Source: knowledge/notes/input_part000_review.md, line 79.
[^smartcontroller_display]: Source: knowledge/notes/input_part000_review.md, line 80.
[^adc_limit]: Source: knowledge/notes/input_part000_review.md, line 83.
[^adc_noise]: Source: knowledge/notes/input_part000_review.md, line 83.
[^signal_divider]: Source: knowledge/notes/input_part000_review.md, line 98.
[^signal_deadband]: Source: knowledge/notes/input_part000_review.md, line 99.
[^throttle_failure]: Source: knowledge/notes/input_part000_review.md, line 190.
[^bench_trip]: Source: knowledge/notes/input_part000_review.md, line 177.
[^regen_ratio]: Source: knowledge/notes/input_part000_review.md, line 178.
[^lab_supply]: Source: knowledge/notes/input_part000_review.md, line 179.
[^mt5e_skus]: Source: knowledge/notes/input_part000_review.md, line 207.
[^front_regen]: Source: knowledge/notes/input_part000_review.md, line 208.
[^mini_eye]: Source: knowledge/notes/input_part000_review.md, line 289.
[^mixed_levers]: Source: knowledge/notes/input_part000_review.md, lines 289 and 300.
[^baseline_regen]: Source: knowledge/notes/input_part000_review.md, line 255.
[^regen_heat]: Source: knowledge/notes/input_part000_review.md, line 256.
[^boosted_profile]: Source: knowledge/notes/input_part000_review.md, line 247.
[^shielded_looms]: Source: knowledge/notes/input_part000_review.md, line 261.
[^brake_wiring_basics]: Source: data/vesc_help_group/text_slices/input_part004.txt†L23763-L23771 and L24697-L24700
[^regen_negative_current]: Source: data/vesc_help_group/text_slices/input_part004.txt†L22556-L22580 and L22848-L22891
[^regen_ripple]: Source: data/vesc_help_group/text_slices/input_part004.txt†L18291-L18318 and L18375-L18380
[^pas_calibration]: Source: data/vesc_help_group/text_slices/input_part004.txt†L23944-L23952 and L24084-L24086
[^regen_hardware]: Source: knowledge/notes/input_part001_review.md†L512-L514
[^regen_heatdrop]: Source: knowledge/notes/input_part001_review.md†L514-L514
[^ip001-curve]: Source: knowledge/notes/input_part001_review.md†L646-L648
[^scroll_prototype]: Source: knowledge/notes/input_part001_review.md†L552-L554
[^scroll_experiments]: Source: knowledge/notes/input_part001_review.md†L580-L582
[^ip001-xiaomi-cal]: Source: data/vesc_help_group/text_slices/input_part001.txt†L18296-L18656
[^ip001-domino]: Source: data/vesc_help_group/text_slices/input_part001.txt†L24290-L24311
[^regen_phase_ratio]: Source: knowledge/notes/input_part008_review.md†L447-L448


## References

[^1]: Source: knowledge/notes/input_part000_review.md†L568-L569
[^2]: Source: knowledge/notes/input_part000_review.md†L570-L570
[^3]: Source: knowledge/notes/input_part000_review.md†L646-L648
[^4]: Source: knowledge/notes/input_part000_review.md†L666-L668
[^5]: Source: knowledge/notes/input_part000_review.md†L640-L646
