# Throttle and Brake Signal Integration

## Brake Sensor Requirements
- Faulty or missing brake sensors can cause rhythmic surging every one to two seconds under throttle, so maintaining functional brake inputs is critical before road testing.[^brake_surge]

## Proportional Braking Hardware
- Most OEM scooter levers ship as digital on/off switches; swapping to hall-based levers (Xiaomi-style or custom SS49E housings epoxied to hydraulic bodies) gives SmartDisplay/ADC stacks an analog pull to blend regen with mechanical braking instead of pulsing the motor.[^analog_braking]
- Magura’s MT5e line still defaults to a microswitch—builders are pivoting to Shimano Deore M6100/M6120 kits or adding hall-effect pucks while configuring the Spintend ADC board’s normally-open/closed toggles for compatibility.[^magura_options]
- Recent comparisons peg Shimano’s four-piston Saint/M7120 kits (~€155 without rotors) as the stiffest one-finger lever option, while MT5 bundles (≈€192 with discs) remain attractive if you add metal lever blades and separate pads; keep in mind that Magura reservoirs can crack under extreme downhill loads.【F:knowledge/notes/input_part000_review.md†L568-L569】
- When instrumenting lever output, power the hall assembly with 5 V and probe the signal wire under load; multimeters alone show no activity without the supply rail energized.[^lever_power]
- Magura confirmed the MT5e lever family ships in two SKUs—2700985 (normally closed) and 2700984 (normally open/Higo “Closer”)—and the Spintend ADC board lets you flip between switch or hall sensing plus 5 V/3.3 V output, so match the lever code before terminating harnesses.[^mt5e_skus]
- Brake-light integration still drives lever choice: some riders keep Nutt levers solely for the switch while running Magura calipers, whereas the MT5e’s HIGO harness remains the cleanest plug-and-play option when budgets allow.【F:knowledge/notes/input_part000_review.md†L570-L570】
- Front-only regen testing on light scooters still locks wheels on low-traction surfaces; veterans either limit the front battery target or disable it entirely once “Shigura” hybrids are installed.[^front_regen]
- Lock-ring grip pods with tactile turn buttons mimic VSETT controls at a fraction of OEM cost, trading a bit of mass for better commuter ergonomics once wired into the ADC board.【F:knowledge/notes/input_part000_review.md†L646-L648】

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
- Xiaomi hall levers happily share 5 V/GND rails with other sensors, but pairing them directly with normally-open Magura hydraulics leaves floating outputs—add a hall puck to the hydraulic lever or dedicate separate channels.[^mixed_levers]

## Throttle & Harness Maintenance
- Sudden surging that mimics hall dropout has traced back to cracked plastic throttles; soldering hall connectors directly and upgrading to higher-quality throttles restored smooth acceleration on high-current builds.[^throttle_failure]

## Regen Safety Guidelines
- Bench testing confirmed that even light regen (-15 A motor / -5 A battery) can trip controllers when wheels spin unloaded—treat test benches like live rides and disable regen until a real pack is connected.[^bench_trip]
- Cap battery regen near the pack’s amp-hour value (e.g., ≤50 A on a 50 Ah pack) and leave roughly 15 A of extra controller “reverb” overhead so the FETs, not the cells, dissipate surges during aggressive braking.[^regen_ratio]
- Laboratory power supplies lack internal resistance, so unloaded regen spikes can exceed supply voltage; rely on real batteries or load banks when validating braking tunes.[^lab_supply]
- Koxx’s baseline for dual-motor commuters lands near −30 A battery/−80 A phase on the rear and −25 A/−55 A on the front, balancing strong braking with controller safety; log stator temps during early shakedowns.[^baseline_regen]
- Field tests on a 10 S 2 P P42A pack produced 2.55 kW regen bursts and rapid motor/MOSFET heating, reinforcing why aggressive profiles need live temperature logging rather than bench guesses.[^regen_heat]
- Riders reminded each other that regen-only configurations are unsafe on 20 S builds—keep mechanical brakes adjusted and in service before trusting wheel-locking e-brakes at 50–65 km/h.【F:knowledge/notes/input_part000_review.md†L666-L668】

## Throttle Voltage Maps & Calibration
- Boosted Rev thumbwheels measure ≈1.6 V at full brake, 2.54 V at neutral, and 3.3 V wide open once wired to VESC ADC inputs, delivering enough regen that some riders rarely touch mechanical brakes.[^boosted_profile]
- Sensor suites that mix ADC throttles and SmartDisplay UART stay stable when the loom uses shielded cable tied to controller ground and routed away from phase leads, which also eliminated cruise-control jitter at 120 A phase.[^shielded_looms]
- Polish-built hall triggers from e-bikestuff ship with a 0.96–4.31 V sweep, zero deadband, and VESC-adjustable endpoints—premium alternatives to Xiaomi/Zero throttles if you can stomach shipping costs.【F:knowledge/notes/input_part000_review.md†L640-L646】


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
