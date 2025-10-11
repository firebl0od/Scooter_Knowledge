# input_part012.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part012.txt`
- Coverage: 2025-04-11T15:10:28 through 2025-05-12T02:04:04 (lines 6,900–14,379)
- Next starting point: Continue `input_part012.txt` at 2025-05-12T02:04:07 (line 14,380)

## Key Findings

### Controller Identification, Wiring, and Start-Up Behavior
- Controller UIDs are hardware-tied, but serial numbers can be edited; riders route throttle and brake directly into ADC1/ADC2 to keep those signals even without a dash daughterboard.【F:data/vesc_help_group/text_slices/input_part012.txt†L6928-L6935】
- Builders treat the ignition/switch input as a 5 V logic trigger rather than battery voltage when waking the controller, so plan low-voltage switching or a relay accordingly.【F:data/vesc_help_group/text_slices/input_part012.txt†L7247-L7289】【F:data/vesc_help_group/text_slices/input_part012.txt†L7502-L7502】
- Dual-drive tuning exposed how a weak or mismatched hall sensor skews current detection (160 A vs. 144 A) and upsets acceleration; verifying hall health beat blaming detection math. The same thread confirmed simple regen buttons by tying ADC2 to 3.3 V through the switch—large series resistors only caused faults.【F:data/vesc_help_group/text_slices/input_part012.txt†L7876-L7889】
- Sensorless launches remain inconsistent: HFI/VSS works once rolling but true zero-speed starts still chatter, so several riders cap launch torque or push off manually to avoid unintended take-offs.【F:data/vesc_help_group/text_slices/input_part012.txt†L7705-L7712】【F:data/vesc_help_group/text_slices/input_part012.txt†L7854-L7855】
- A sensorless enduro owner found phase current beyond ~200 A caused 5–10 km/h bogging and noise; the group suggested lowering motor inductance settings and iterating carefully before chasing 550 A phase targets.【F:data/vesc_help_group/text_slices/input_part012.txt†L8341-L8391】

### Decks, Frames, and Chassis Packaging
- Mirko’s Dualtron upgrade required machining—rear forks must be enlarged, so budget time for permanent metal work rather than drop-in swaps.【F:data/vesc_help_group/text_slices/input_part012.txt†L6972-L6974】
- Rage Mechanics’ extended deck runs €410 (black) or €470 (carbon) with 672 mm overall length and ~622 mm usable space once the 25 mm front/rear lips are subtracted.【F:data/vesc_help_group/text_slices/input_part012.txt†L7083-L7104】
- The same crew warned against FastRide decks for poor tolerances and called Sonken swingarms overbuilt, hard to install, and locked to the stock Dualtron pole geometry—go Rage Mechanics or RFP instead.【F:data/vesc_help_group/text_slices/input_part012.txt†L7107-L7116】
- French racer Medhi Cantin is hand-building billet 7075 frames around dual Kelly 7230S controllers, underscoring how much fabrication time (≈1 year) goes into competitive stand-up scooters.【F:data/vesc_help_group/text_slices/input_part012.txt†L7340-L7379】

### Powertrain, Performance, and Battery Planning
- Spintend’s single Ubox 85 V 240 A unit still pushes an 80H hub to ~95 km/h, making it a viable high-speed commuter controller without going dual-motor.【F:data/vesc_help_group/text_slices/input_part012.txt†L7131-L7136】
- PMT Junior tires feel “glued” on G2 builds, but Mirko won’t ride 90 km/h without a steering damper—expect to budget for damping hardware once speeds climb.【F:data/vesc_help_group/text_slices/input_part012.txt†L7145-L7173】
- Jason’s G30 project already houses a 30 S pack around a 65H 17×4 motor and he is plotting a fully internal 40 S/3 P layout, showing the packaging ceiling for Max conversions with careful component placement.【F:data/vesc_help_group/text_slices/input_part012.txt†L7997-L8008】【F:data/vesc_help_group/text_slices/input_part012.txt†L8221-L8222】
- Custom-order magnets for 65H stators returned only ~5 km/h at 20 S, so Paolo recommends spending on better stator cores or wiring instead of premium magnet swaps.【F:data/vesc_help_group/text_slices/input_part012.txt†L7856-L7862】
- Halo Knights see ~105–110 km/h at 60 V, yet 350 A phase and 125 A field weakening send the wheel into runaway RPM off-load; keep airborne testing mild to avoid freewheel overspeed and controller stress.【F:data/vesc_help_group/text_slices/input_part012.txt†L8095-L8107】
- Heavy riders (≈110 kg) running 100 A battery / 200 A phase / 300 A ABS on dual 85/240s noted rear-motor cutouts, hinting at drivetrain wear limits under sustained torque.【F:data/vesc_help_group/text_slices/input_part012.txt†L8363-L8369】

### Brakes, Wheels, and Tires
- 3 mm × 170 mm rotors noticeably stiffen braking, but riders doubt they’ll clear many calipers—fully retract pistons before installation and expect to true minor shipping bends after only a few stops.【F:data/vesc_help_group/text_slices/input_part012.txt†L8024-L8047】【F:data/vesc_help_group/text_slices/input_part012.txt†L8121-L8124】
- Magura lever assemblies remain fragile; their plastic hardware can snap by hand, so several owners swap to Saint or other metal levers before trusting 3 mm rotors.【F:data/vesc_help_group/text_slices/input_part012.txt†L8031-L8059】
- Fresh rotors pair well with resurfaced pads—the group jokingly formed a “sanded pad club” to tame bedding squeal and keep performance consistent.【F:data/vesc_help_group/text_slices/input_part012.txt†L8095-L8104】
- Tire sourcing is still regional: ULIP 90/60‑6 clones are an affordable alternative when PMT Juniors cost ~€130 locally, but riders still favor PMT for outright grip when shipping cooperates.【F:data/vesc_help_group/text_slices/input_part012.txt†L8166-L8187】
- A punctured front tire forced a 4 km walk; riders now keep multiple spares (e.g., C3 slicks) on hand to avoid rim damage when high-speed casings fail.【F:data/vesc_help_group/text_slices/input_part012.txt†L8150-L8158】

### MP2 Assembly and High-Current Wiring Practices
- Seasoned builders solder copper busbars first, mount FETs second, and terminate phase wires last; leaded solder flows around 200 °C on a hotplate, but keep electrolytic capacitors off the plate to avoid damage.【F:data/vesc_help_group/text_slices/input_part012.txt†L7723-L7738】【F:data/vesc_help_group/text_slices/input_part012.txt†L7813-L7820】
- Proven conductor stack: 8 AWG battery leads and three 12 AWG runs per phase (~10 mm²). 6 AWG physically fits only after stripping strands, which risks bridging FET legs and makes rework miserable once the hardware’s ~420 A protection is tripped.【F:data/vesc_help_group/text_slices/input_part012.txt†L7728-L7762】【F:data/vesc_help_group/text_slices/input_part012.txt†L7790-L7914】
- Builders who accidentally leave boards on the hotplate briefly reported no immediate PCB damage, but the scare reinforced double-checking preheat routines before moving to solder prep.【F:data/vesc_help_group/text_slices/input_part012.txt†L8313-L8329】

### Connectors, Tools, and Harness Tips
- Manual JST crimpers provide better results than ratcheting tools that crush insulation and hide the contact—crimp the conductor first, then the strain relief for reliable MP2/75100 harnesses.【F:data/vesc_help_group/text_slices/input_part012.txt†L7190-L7197】
- MakerX 75100 V2 signal leads use JST-PH (2.0 mm) rather than larger JST-XH shells, so match tooling and housing size accordingly.【F:data/vesc_help_group/text_slices/input_part012.txt†L8015-L8047】

### Firmware Stability and Telemetry Mods
- Upgrading a Spintend 100 V controller from VESC Tool 6.05 to 6.06 left the motor motionless until the owner reverted to 6.05; peers suggest capping phase current near 130 A and ABS near 180 A on 50H motors until 6.06 proves stable.【F:data/vesc_help_group/text_slices/input_part012.txt†L8200-L8241】
- Another rider also bailed out of 6.06 after repeated reflashes—high temperatures still produced scratching noises, so he resumed 6.05 for reliability.【F:data/vesc_help_group/text_slices/input_part012.txt†L8217-L8217】
- Relocating and shielding the VESC Express antenna delivered rock-solid BLE across two concrete walls, highlighting how much range depends on antenna placement rather than firmware tweaks.【F:data/vesc_help_group/text_slices/input_part012.txt†L8245-L8247】
- Field testing the VESC Express logger outdoors returned GPS HDOP around 0.7, confirming decent positional accuracy once antennas have clear sky view.【F:data/vesc_help_group/text_slices/input_part012.txt†L8210-L8213】

### Additional Findings (Lines 8,400–9,899)

#### Motor and Drivetrain Upgrades
- Authentic 90H hubs ship with longer magnets; if the housing stamping looks generic, measuring magnet length is the quickest way to confirm a real 90H before tearing the motor apart.【F:data/vesc_help_group/text_slices/input_part012.txt†L8463-L8466】
- Dual 65H builds have phase leads that choke inside the axle—owners trying to run 300–400 A per controller found one motor already nicked internally and recommend replacing both the phase and hall looms with the thickest conductors that will physically fit to keep phase targets above 200 A safe.【F:data/vesc_help_group/text_slices/input_part012.txt†L8703-L8707】

#### Controller Packaging, Cooling, and Input Mapping
- Segway GT-series decks can house Ubox Lite, 85250, or even an MP2 controller; a stock G2 has just enough room to mount an 85240 on the back wall. Painted steel enclosures act as thermal insulators, so riders grind back to bare metal, add thermal glue, and avoid single PETG brackets that leave controllers running at ~64 °C under load.【F:data/vesc_help_group/text_slices/input_part012.txt†L8651-L8673】
- When calibrating analog controls, run the ADC mapping routine instead of hardcoding 5 V and 3.3 V ranges—let VESC Tool find center, then wire ADC2 if you want proportional regen instead of brake-from-center behavior.【F:data/vesc_help_group/text_slices/input_part012.txt†L8458-L8459】【F:data/vesc_help_group/text_slices/input_part012.txt†L8699-L8701】
- Most VESC peripherals expect 3.3 V logic; confirm accessory requirements before reusing 5 V sensors to avoid detection issues.【F:data/vesc_help_group/text_slices/input_part012.txt†L9137-L9138】

#### Lighting, Accessories, and Diagnostics
- The ADC horn channel on Makerbase/Spintend harnesses only sources a couple of amps—feeding a vintage 12 V 35 W halogen (≈3 A) risks cooking the board. Use a DC/DC converter for lighting power and let the button trigger a relay or the controller’s low-current line instead.【F:data/vesc_help_group/text_slices/input_part012.txt†L8876-L8897】
- To count motor magnets without disassembly, short two phases together and rotate the wheel—the number of detents equals the magnet count.【F:data/vesc_help_group/text_slices/input_part012.txt†L9128-L9130】

#### Telemetry and Remote Access
- Switching VESC Express from AP to station mode lets a home router hand out the IP address, eliminating flaky TCP discovery on laptops and enabling remote access to the ESC whenever the vehicle is powered.【F:data/vesc_help_group/text_slices/input_part012.txt†L8911-L8938】

#### Tires, Chassis, and Track Use
- Xeuancheng and ULIP 11" tires are viable PMT alternatives when shipping is prohibitive—expect to trim brake mounts on some frames, and stock up when AliExpress runs discounts.【F:data/vesc_help_group/text_slices/input_part012.txt†L9545-L9552】【F:data/vesc_help_group/text_slices/input_part012.txt†L9597-L9600】
- Track-focused NAMI builds see ~100 km/h without field weakening on 65H motors, underscoring how much speed is already available once geometry and tires are sorted.【F:data/vesc_help_group/text_slices/input_part012.txt†L9731-L9738】

#### Controller Reliability, Alternatives, and Testing
- A Shitsky 75350 paired with a 20 S 13 P LG M58T pack delivered 500 A phase / 235 A battery, 127 km/h top speed, and ~57 Wh/km efficiency on a Sur-Ron while limiting voltage sag to ~7 V—proof that the budget controller can survive ~32 kW peaks with proper copper busbar builds.【F:data/vesc_help_group/text_slices/input_part012.txt†L9165-L9176】
- Shorted phases on MKS 84100HP units torch XT60s instantly; expect one phase to read 0 Ω when the MOSFET stack fails. Builders source replacement MOSFETs from distributors like LCSC rather than AliExpress to avoid counterfeits, even if shipping eclipses the silicon cost.【F:data/vesc_help_group/text_slices/input_part012.txt†L9334-L9362】
- Multiple Spintend 85 V 250 A controllers arrived DOA or died within weeks at 200 A motor / 170 A battery settings, prompting owners to budget for Seven or 3Shul replacements despite the higher price tag.【F:data/vesc_help_group/text_slices/input_part012.txt†L9803-L9827】
- Spintend confirmed the 85/250 run is discontinued; the 85/240 offers similar performance, but riders needing more headroom are pivoting to X12 or Seven platforms instead of chasing scarce stock.【F:data/vesc_help_group/text_slices/input_part012.txt†L9533-L9552】【F:data/vesc_help_group/text_slices/input_part012.txt†L9590-L9594】
- MK8 Pro controllers ship with undersized capacitors and aren’t recommended for high-power scooters unless you redesign the wiring and pack to tame spikes.【F:data/vesc_help_group/text_slices/input_part012.txt†L9850-L9853】
- Open-source hardware continues to expand: the community just published the untested six-MOSFET “Baguette ESC” for contributors who want a lightweight controller starting point.【F:data/vesc_help_group/text_slices/input_part012.txt†L9520-L9522】

#### Battery Planning and Charging
- Custom 20 S 5 P packs around 65H 17×4 motors are landing at 31.5 Ah (≈90 A battery capability); builders juggle whether to stick with dual 16 S packs for 63 Ah range, step to 20 S for more speed, or jump all the way to 32 S depending on controller health (85150 vs. 85250).【F:data/vesc_help_group/text_slices/input_part012.txt†L9780-L9794】
- Oversized copper busbar packs can comfortably accept 1.5 kW charging, refilling a 20 S Sur-Ron battery from ~40 % to 90 % over lunch while keeping cell currents near 18–19 A thanks to 260-cell layouts.【F:data/vesc_help_group/text_slices/input_part012.txt†L9170-L9207】

#### Safety and Operations
- Fatal solo crashes inside the community are a stark reminder to stay helmeted and respect scooter limits even after extensive tuning work.【F:data/vesc_help_group/text_slices/input_part012.txt†L9268-L9301】

### Additional Findings (Lines 9,900–11,399)

#### Safety and Reliability Incidents
- A Le Mans racer rag-dolled after his front motor cut out mid-corner, underscoring how traction losses from controller faults can be as dangerous as poor tire choice when pushing race pace.【F:data/vesc_help_group/text_slices/input_part012.txt†L9900-L9909】
- Another rider slid out while taking a turn too fast but escaped with minor damage, reinforcing the need for post-crash self-checks before resuming a ride.【F:data/vesc_help_group/text_slices/input_part012.txt†L10056-L10065】
- Owners warned that an 85 V 240 A Ubox with a blown capacitor should be sidelined immediately—even if it still powers up—until repaired or swapped to a single-controller setup to avoid cascading failures.【F:data/vesc_help_group/text_slices/input_part012.txt†L10122-L10143】

#### Build and Chassis Updates
- Ayo finished Jamaludin’s Nami refresh by machining custom bushings to replace stacks of washers, taming cable noise, and rechecking brake alignment before handoff—evidence that tidying tolerances is as critical as bolt-on part swaps.【F:data/vesc_help_group/text_slices/input_part012.txt†L9947-L9989】
- Spain’s Nami community shared photos of first-generation chassis cracking near welds and contrasted them with the reinforced 72/40 frames, giving buyers a visual checklist for spotting the latest gussets before committing to used frames.【F:data/vesc_help_group/text_slices/input_part012.txt†L10609-L10623】
- Jason traced a persistently unbalanced 30 S pack to moisture ingress that soaked a parallel group, reminding builders to inspect weatherproofing after rain rides before cells drift too far out of balance.【F:data/vesc_help_group/text_slices/input_part012.txt†L10491-L10505】

#### Controller Supply, Support, and Diagnostics
- Smart Repair confirmed Spintend has ended 85/250 production in favor of the 85/240, prompting riders who depend on the higher-rated board to explore alternatives or stock spares while inventory remains.【F:data/vesc_help_group/text_slices/input_part012.txt†L9930-L9939】
- Hackintosh is trying to buy every broken Spintend logic board he can find, while Shlomozero weighed swapping in a new 85240 logic board—collective signs that DIY repair is still the only path to keep the bigger controllers alive in regions with slow shipping.【F:data/vesc_help_group/text_slices/input_part012.txt†L10709-L10757】
- Builders troubleshooting dead motors highlighted how enabling ADC inputs blocks manual FWD/REV commands in VESC Tool; switching the control app to UART (or disabling ADC) restored bench spins, which is easy to miss when dual controllers share CAN and throttle lines.【F:data/vesc_help_group/text_slices/input_part012.txt†L10246-L10262】
- After repeated hall faults, Pandalgns regained smooth launches by reconfiguring his scooter for sensorless operation and later noted that burned hall looms can masquerade as loose phase leads—check sensors before chasing imagined shorts.【F:data/vesc_help_group/text_slices/input_part012.txt†L10284-L10311】【F:data/vesc_help_group/text_slices/input_part012.txt†L10385-L10393】
- Matthew is still hunting a reliable laptop-based recovery path for bricked 85150s even after buying extra gear, signalling a documentation gap for ST-Link alternatives and merged firmware packages.【F:data/vesc_help_group/text_slices/input_part012.txt†L10630-L10646】

#### Tuning Practices and Performance Benchmarks
- Jamaludin’s 80H dual-motor Nami already felt “crazy soft” on just 100 A battery / 200 A phase, yet he plans to stay at or below a 350 A battery nominal and 300 A phase because Ubox owners report 12-FET stacks are only “safe” to ~300 A before failures spike.【F:data/vesc_help_group/text_slices/input_part012.txt†L10143-L10170】
- Riders compared these heuristics with haku’s reminder that 20 S10 P P42A packs can momentarily deliver ~450 A, reinforcing the need to pair current targets with cell capability and temperature monitoring.【F:data/vesc_help_group/text_slices/input_part012.txt†L10154-L10166】
- Field weakening remains a trade-off: dropping FWK to zero saved energy but forced higher phase current for speed, raising controller temps from 46 °C to 55 °C in just 15 minutes—use FW only when you need the extra top-end.【F:data/vesc_help_group/text_slices/input_part012.txt†L10882-L10888】
- Pandalgns pushed a Halo 60H to 350 A phase with 125 A FW, but the motor stuttered at 15–20 km/h; others suggested temp sensing or lower phase current, reinforcing that saturation compensation (10–15 %) and hall health matter before simply adding amps.【F:data/vesc_help_group/text_slices/input_part012.txt†L10916-L10946】【F:data/vesc_help_group/text_slices/input_part012.txt†L11045-L11053】

#### Power Infrastructure and Fabrication
- Jason built a J1772 adapter harness using 12 AWG silicone leads plus 2.5 mm² wire to feed both XT60 and AC outlets, then noted he still needed 2.74 kΩ and 1.3 kΩ resistors to satisfy charge-station handshakes—handy specs for anyone planning 3 kW public charging on road trips.【F:data/vesc_help_group/text_slices/input_part012.txt†L10580-L10588】【F:data/vesc_help_group/text_slices/input_part012.txt†L11100-L11129】
- Laser-cut 14 mm torque arms replaced stock 12 mm hardware for upcoming QS hub swaps, showing how much fabrication margin dual-sport conversions need when axles step up in diameter.【F:data/vesc_help_group/text_slices/input_part012.txt†L10903-L10908】
- Noname’s e-moped project is moving to a QS260 12" hub and retaining dual 85/250 controllers, hinting at realistic 60 mph gearing for seated VESC builds without abandoning scooter-style packaging.【F:data/vesc_help_group/text_slices/input_part012.txt†L10180-L10185】【F:data/vesc_help_group/text_slices/input_part012.txt†L11111-L11124】

#### Battery Maintenance and Planning
- Yamal found his pack unbalanced after sitting for two months, while Jason’s 30 S pack needs a cell swap and rewrap after moisture exposure—together they illustrate why periodic cycling and post-rain inspections are essential before leaning on high-power profiles again.【F:data/vesc_help_group/text_slices/input_part012.txt†L10504-L10513】【F:data/vesc_help_group/text_slices/input_part012.txt†L10491-L10503】
- Riders debated future builds such as 30 S6 P Max conversions and 65H hubs in 11" frames, concluding that minor swingarm milling plus shims make oversized stators feasible if you plan battery and controller space first.【F:data/vesc_help_group/text_slices/input_part012.txt†L10578-L10587】【F:data/vesc_help_group/text_slices/input_part012.txt†L11033-L11054】

### Additional Findings (Lines 11,400–12,879)

#### Charging, BMS Management, and Accessory Power
- Riders chasing budget 21 S charging are leaning on adjustable 22 S/18 A AliExpress supplies and pairing them with ANT BMS sleep timers so packs don’t drift after a month offline.【F:data/vesc_help_group/text_slices/input_part012.txt†L11401-L11411】
- Another crew highlighted multi-voltage 16–24 S/20 A chargers as a flexible option when the premium 21 S bricks are out of stock.【F:data/vesc_help_group/text_slices/input_part012.txt†L11792-L11797】

#### Firmware, Dash Tools, and Telemetry
- 1zuna’s G30 dash Lisp errors were traced to stale desktop installs—reinstalling VESC Tool before flashing resolved the script upload.【F:data/vesc_help_group/text_slices/input_part012.txt†L11421-L11426】
- Limited-mode lockouts on mobile disappeared once riders matched the VESC Tool app to the controller’s 6.06 firmware; sideloading the APK is required outside the official store.【F:data/vesc_help_group/text_slices/input_part012.txt†L11511-L11517】
- VESC Express modules that failed to enumerate over USB showed up instantly after connecting via CAN and running the ESP flasher inside VESC Tool, so builders now start there before assuming bad hardware.【F:data/vesc_help_group/text_slices/input_part012.txt†L11592-L11619】

#### Motor Control, Field Weakening, and Sensorless Behavior
- Aggressive field-weakening that caused vibration on 6.06 betas eased by experimenting with zero-vector frequency (≈40–45 kHz) and V0/V7 interpolation, underscoring how observer and ZVF tuning interact at higher FW levels.【F:data/vesc_help_group/text_slices/input_part012.txt†L11526-L11540】
- A G30 rider confirmed a severed hall lead as the culprit for a dead front hub—VESC sensorless fallback kept the scooter rideable until repairs, illustrating how dual setups can limp on one healthy motor.【F:data/vesc_help_group/text_slices/input_part012.txt†L11421-L11429】
- Owners running hall-less 75100 builds reiterated that true zero-speed torque still needs a push start; low-speed smoothness varies wildly by motor and is helped by keeping a hall-equipped axle in dual setups.【F:data/vesc_help_group/text_slices/input_part012.txt†L11803-L11810】【F:data/vesc_help_group/text_slices/input_part012.txt†L11833-L11841】【F:data/vesc_help_group/text_slices/input_part012.txt†L12821-L12823】

#### Lighting, Controls, and Harness Integration
- To power more than two 12 V loads on 85250s, Smart Repair recommends routing lights through the ADC breakout so the controller feeds brake-light logic while a DC/DC handles actual lamp current; the same thread documents Express setup pains and confirms the Spin-Y2 throttle’s compatibility once that adapter is in place.【F:data/vesc_help_group/text_slices/input_part012.txt†L11592-L11619】【F:data/vesc_help_group/text_slices/input_part012.txt†L11608-L11612】
- Later in the slice, Giuseppe’s TF100 throttle question produced a wiring recipe—use the red/black hall supply plus the green signal lead on a 3.3 V input—to reuse the scooter dash without custom PCBs.【F:data/vesc_help_group/text_slices/input_part012.txt†L12802-L12818】

#### Tires, Wheels, and Brake Upkeep
- Continuous burnouts shredded “snake” pattern street tires in hot 48 °C climates, pushing riders back to PMT Juniors or at least to regular rotations before cords show.【F:data/vesc_help_group/text_slices/input_part012.txt†L11432-L11458】
- Cheap carcasses often need the bead mold flash scuffed away for a proper seal, and one slow leak was traced to a wood splinter embedded under the tire—confirming bead hygiene matters as much as compound choice.【F:data/vesc_help_group/text_slices/input_part012.txt†L11798-L11802】
- A Vsett rotor bent in traffic reminded the group to carry spares and rely on e-brakes when mechanical rotors warp mid-ride.【F:data/vesc_help_group/text_slices/input_part012.txt†L11614-L11627】

#### Battery Builds, Frames, and Packaging
- Thunder frame conversions fitting 22 S 11 P packs rely on crossing cell columns; even veterans admit 11 P is tight and recommend settling for 10 P unless you’re prepared for precision machining.【F:data/vesc_help_group/text_slices/input_part012.txt†L11620-L11637】
- Smart Repair’s dual X12 project shows how fast packaging snowballs: the 70H rear/GT1 front mix already needs AWG10 phase leads through the axle and creative BMS placement to clear a 26 S upgrade.【F:data/vesc_help_group/text_slices/input_part012.txt†L12170-L12199】【F:data/vesc_help_group/text_slices/input_part012.txt†L12183-L12189】
- Shlomozero relayed specs for Russia’s 26 S 64 Ah RTV Ultra billet scooter—dual 3Shul controllers, 115 mm stators, 11×PMT130 tires, ≈40 kW peaks, and six-month lead times—providing a benchmark for turnkey superbikes.【F:data/vesc_help_group/text_slices/input_part012.txt†L11812-L11819】
- Noname’s Niu-based e-moped (32 S 20 P Samsung 35E, QS260 45H, dual 85/250 VESC) now sprints 0–68 mph in 18 s, proving commuter mopeds can match highway pace with a single high-end controller stack.【F:data/vesc_help_group/text_slices/input_part012.txt†L11855-L11873】

#### Diagnostics, Thermal Performance, and Safety
- Motor temperature cutbacks that appeared after 15 minutes on a modest 48 V 800 W hub turned out to be bad sensor selection—switching away from NTC 100 k or disabling the probe until the thermistor value is confirmed with a multimeter avoids limp mode during rides.【F:data/vesc_help_group/text_slices/input_part012.txt†L12064-L12100】
- Pandalgns’ 60 V logs show ~10–11 kW “air power” at 100 A battery, 350 A phase, and 125 A FW, while Smart Repair reminds that limited torque keeps duty cycle down compared with high-torque stators.【F:data/vesc_help_group/text_slices/input_part012.txt†L12157-L12174】
- Shlomozero’s dual 90 H setup recorded 58 °C rear / 48 °C front after a 24 km hill session in 25 °C weather, giving a reference point for 75 200/85 150 heat soak on 10 % grades.【F:data/vesc_help_group/text_slices/input_part012.txt†L12839-L12848】
- Builders planning ferrofluid refreshes on Segway hubs suggested applying it sparingly between magnets while adding a dedicated temp probe so elevated watts don’t go unnoticed.【F:data/vesc_help_group/text_slices/input_part012.txt†L12661-L12665】

### Additional Findings (Lines 12,880–14,379)

#### Touring Range, Charging, and Weather Planning
- Jason’s mountain ride pushed his 30 S 6 P pack to 3 V/cell on steep climbs; regen down the descent only clawed back a few percent, reinforcing how quickly elevation drains small packs.【F:data/vesc_help_group/text_slices/input_part012.txt†L12886-L12907】
- He now leans on public chargers or an EV adapter once rain clears, topping to ~80–85 % before continuing; Yamal carries a fast charger into cafés on >100 km routes and sees ~100 km range from a 20 S 10 P pack in mild weather.【F:data/vesc_help_group/text_slices/input_part012.txt†L12890-L12945】
- Jason wants his next pack to accept the full 26 A/3.2 kW output of his “2900 W” charger, acknowledging he already overdraws its nameplate rating.【F:data/vesc_help_group/text_slices/input_part012.txt†L12919-L12922】

#### Rainproofing, Motor Fluids, and Stuck Hardware
- Riding custom builds in heavy rain still risks electronics; Yamal keeps modified scooters out of storms and reserves wet rides for stock Ninebots.【F:data/vesc_help_group/text_slices/input_part012.txt†L12963-L12967】
- Before adding ferrofluid, Matthew drills only a shallow breather hole in sealed hubs (marking the bit depth) and reseals with clear RTV, while Noname adds a temperature sensor for ongoing monitoring.【F:data/vesc_help_group/text_slices/input_part012.txt†L12974-L12975】
- Members free rounded Thunder fasteners by cutting a slot with a Dremel/rotary tool, hammering in an oversized flat-head (“Thor head”) bit, or heating the screw until the Loctite lets go.【F:data/vesc_help_group/text_slices/input_part012.txt†L13074-L13090】

#### Deck Swaps, Wiring, and Motor Fitment
- Skrtt is transplanting a Thunder box onto a Dualtron Victor to gain deck width for larger packs; he confirms the Victor mounts share the Thunder’s 7.5 cm spacing and paid ~€200 for the assembly instead of machining a custom deck.【F:data/vesc_help_group/text_slices/input_part012.txt†L13095-L13140】
- Thunder swingarms remain the go-to for fitting 70 H or 11" motors on Victors, though tires alone can step to 11" before the motors arrive.【F:data/vesc_help_group/text_slices/input_part012.txt†L13131-L13207】
- Jason shortened his 17×4 phase wires to cut about 3 mΩ of resistance and can launch reliably at 140 A phase without tripping ABS overcurrent; he now caps MP2 settings at 100 A battery / 250 A phase after a 300 A test blew MOSFETs.【F:data/vesc_help_group/text_slices/input_part012.txt†L13096-L13343】
- When 11" tires barely kiss the fork, riders grind the contact point or seat the axle at the dropout tip for detection runs; unplugging phases alone doesn’t require a fresh motor detection—miswired phases simply spin backwards.【F:data/vesc_help_group/text_slices/input_part012.txt†L13561-L13621】

#### Tire Sourcing, Repairs, and Burnout Wear
- Haku’s 6.5" options range from fake PMT “Stardale” clones to 100/55-6.5 TOUVT casings, while Yamal continues to praise Xuancheng PMTs despite recent 50 % AliExpress price hikes.【F:data/vesc_help_group/text_slices/input_part012.txt†L13208-L13233】【F:data/vesc_help_group/text_slices/input_part012.txt†L13154-L13155】
- Muc-Off tubeless sealant squelches most slow leaks when injected through the valve core, but stubborn holes may still need tubes or internal patches after checking for debris with a rag.【F:data/vesc_help_group/text_slices/input_part012.txt†L13383-L13410】
- The group debated plugs vs. patches for scooter tires: Matthew prefers patches for longevity, while Noname notes multi-plug off-road fixes can hold for years; everyone agrees to scuff the carcass and let cement tack before bonding.【F:data/vesc_help_group/text_slices/input_part012.txt†L13411-L13469】【F:data/vesc_help_group/text_slices/input_part012.txt†L13863-L13871】
- Tire smoke output during burnouts depends on tread makeup, wheel speed, and weight—lighter 6.5" builds shed less rubber than heavier Weeped-style setups, and “gender reveal” compounds can exaggerate the effect.【F:data/vesc_help_group/text_slices/input_part012.txt†L13825-L13833】
- Valve cores remain consumables on tubeless conversions; damaged stems or rushed cement work will reopen leaks until replaced and properly cured.【F:data/vesc_help_group/text_slices/input_part012.txt†L13791-L13795】【F:data/vesc_help_group/text_slices/input_part012.txt†L13863-L13871】

#### Controller Setup, Express Connectivity, and Regen Limits
- Smart Repair clarified the VESC Express flash path: plug Express into USB without connecting, open the ESP Programmer panel (bottom left), select the COM port, flash, then cable Express to the ESC over CAN for normal use.【F:data/vesc_help_group/text_slices/input_part012.txt†L13156-L13164】
- Users seeing dead USB-C ports still access real-time data by pairing Express over CAN/Bluetooth, but configuration changes require a direct USB session to the ESC itself.【F:data/vesc_help_group/text_slices/input_part012.txt†L13399-L13427】
- Regen tuning anecdotes varied: Noname runs 90 A phase regen per motor, while Matthew is eyeing 120 A phase / 20 A battery regen for a 65 H 17×4 on an 85250, mindful of prior “kabooms” blamed on excessive braking current.【F:data/vesc_help_group/text_slices/input_part012.txt†L13576-L13595】

#### Thermal Management and Cooling
- Jason resurrected his MP2 after a MOSFET failure and now treats 100 A battery / 250 A phase as the sustainable ceiling on 150 V packs; earlier 300 A phase tests detonated the board while chasing sensor cogging.【F:data/vesc_help_group/text_slices/input_part012.txt†L13320-L13343】
- Finn keeps an Ubox Lite under 50 °C while pushing 160 A phase / 90 A battery by replacing the stock pads with Arctic MX4 and bolting through the controller’s M2 mounting bosses into a 3 mm aluminum belly plate.【F:data/vesc_help_group/text_slices/input_part012.txt†L13678-L13718】
- Matthew’s DIY water loop dropped his VESC case from 90 °C cutbacks to ~26–28 °C during 45 mph pulls; Noname is planning a moped-sized radiator, pump, and expansion tank to scale the approach.【F:data/vesc_help_group/text_slices/input_part012.txt†L13700-L13766】
- Swapping in higher-grade thermal paste on heavy builds shaved another ~5 °C, but riders still prioritize airflow before adding liquid cooling complexity.【F:data/vesc_help_group/text_slices/input_part012.txt†L14340-L14347】

#### Motor Control Experiments and Sensorless Starts
- Pandalgns combined an 84100 with a 75100 V2 to revive a Halo and is iterating on HFI, saturation compensation, and start-current reductions so sensorless Janobike T10 motors launch smoothly without blowing hall sensors again.【F:data/vesc_help_group/text_slices/input_part012.txt†L13739-L13751】
- The team continues to trade hall-less tuning notes, with Matthew studying Vedder’s HFI walkthroughs but preferring to experiment on cheaper Zcougar hardware before applying new parameters to premium builds.【F:data/vesc_help_group/text_slices/input_part012.txt†L13742-L13748】

#### Performance Benchmarks, Batteries, and Packaging
- Riders gauged Lonnyo 80 H stators: the 22/3 winding is roughly 34.8 KV, good for ~141 km/h free spin at 80 V, but dual motors or lighter rims are recommended if you expect meaningful 11" acceleration.【F:data/vesc_help_group/text_slices/input_part012.txt†L13310-L13317】
- Pandalgns is measuring halo swingarms for up to 200 mm openings to host 80 H hubs, while Yamal notes stock forks run 170–175 mm and can be special-ordered at 155 mm for 60 H builds.【F:data/vesc_help_group/text_slices/input_part012.txt†L13850-L13862】
- Noname’s 20 S 32 P Samsung 35E moped pack logs 67 mi rides while discharging to 72 V (~48 %) yet leaves the bike ~350 lb; he’d now pick a 32 S 20 P layout with a Seven controller for better torque-to-weight, possibly adding a 4 S 20 P booster for another 20 mi.【F:data/vesc_help_group/text_slices/input_part012.txt†L14312-L14364】
- Jason is routing waterproof grooves into axle exits to keep water from shorting his 65 H motors after repeated wet rides.【F:data/vesc_help_group/text_slices/input_part012.txt†L13547-L13558】

#### Finishes and Fabrication Notes
- Powder coating remains the most durable option for exposed frames, but aluminum must be sanded or blasted to remove its oxide layer before primer or powder will stick.【F:data/vesc_help_group/text_slices/input_part012.txt†L13365-L13392】
- Finn laser-cut a 3 mm aluminum G30 belly pan to shield batteries and create a flat mounting surface for thermal interfaces and hardware additions.【F:data/vesc_help_group/text_slices/input_part012.txt†L13711-L13718】

## Follow-Up Questions / To-Do
- Draft a wiring cheat sheet covering 5 V ignition switches, direct-ADC brake/throttle routing, and simple regen-button wiring so new builders avoid resistor-induced faults.
- Document adjustable 21–22 S charger picks and ANT BMS sleep-timer workflows so stored packs don’t drift while offline.
- Capture a pictorial guide for Rage Mechanics deck swaps, including the fork-enlargement work and any tooling required for clean installs.
- Document Medhi Cantin’s billet-frame/Kelly 7230S race build so we can reference fabrication timelines, component choices, and packaging tricks.
- Convert the MP2 assembly sequence and hotplate precautions into a repeatable SOP with photos, temperature checkpoints, and MOSFET leg reinforcement tips.
- Map 3 mm rotor fitment tricks (piston resets, lever upgrades, bedding procedure) and note which calipers clear 170 mm discs without machining.
- Benchmark PMT Junior vs. ULIP tire grip, wear, and availability so riders can choose replacements after punctures.
- Track VESC Tool 6.06 regression reports (sensorless bogging, ABS faults) so we can advise when it’s safe to leave 6.05.
- Gather more data on sensorless high-phase setups to see if inductance tweaks or hall retrofits solve the >200 A bogging reports.
- Capture a magnet-length inspection guide for 90H hubs and document safe methods for re-looming 65H phase/hall bundles through tight axles.
- Build a Segway GT-series controller packaging note covering Ubox/MP2 fitment, thermal interface prep, and mounting hardware that keeps case temps below 60 °C.
- Publish an ADC calibration cheatsheet (mapping workflow, ADC2 regen wiring, 3.3 V logic expectations) to prevent stuck-brake complaints.
- Write a lighting power primer that steers riders toward DC/DC-fed relays instead of driving 35 W halogens directly from ADC outputs.
- Document the VESC Express station-mode/network workflow so laptops find TCP hubs without manual IP entry.
- Capture a VESC Tool troubleshooting note that covers fresh desktop installs, firmware-version matching for the mobile app, and the ESP-flasher path for Express modules that refuse USB enumeration.
- Assemble a repair playbook for MKS 84100HP and Spintend 85/250 failures (phase-resistance triage, vetted MOSFET sources, and when to switch to Seven/X12-class controllers).
- Trace the Le Mans front-motor cutout to document telemetry, redundancy options, and rider checks that prevent repeat race incidents.
- Capture Nami frame-generation cues (reinforcement photos, washer-to-bushing swap steps, brake alignment tips) so owners can verify upgrades and quiet their builds.
- Publish an 85/240 capacitor triage and parts-sourcing brief that explains when to retire hardware, how to inspect logic boards, and which replacements remain available after the 85/250 sunset.
- Write a hall-diagnosis and sensorless-fallback guide covering ADC app settings, hall harness testing, and safe launch tuning for burned sensors.
- Add zero-vector-frequency/field-weakening tuning tips to that sensorless guide so riders know how to tame vibration on 6.06.
- Summarize field-weakening vs. phase-current trade-offs—including saturation compensation targets—so riders can chase top speed without overcooking controllers at 300 A+.
- Produce a J1772 adapter reference (wire gauges, resistor values, enclosure ideas) for riders planning 3 kW EV-charger stops on tour builds.
- Turn the Thunder/X12 packaging lessons into a case study that walks through crossed-cell layouts, AWG10 axle limits, fork widening for 70H fronts, and BMS placement on 26 S upgrades.
- Publish a quick reference on cleaning tire beads, checking for debris, and carrying rotor spares after the latest slow-leak and bent-disc reports.
- Write up a ferrofluid-application and temp-probe checklist for Segway-class hubs before the next maintenance day.
- Capture a touring checklist that covers EV charger adapters, café-friendly fast-charging etiquette, and trip-planning for small packs so riders avoid 3 V/cell sag on mountain routes.
- Draft a rainproofing guide that highlights which components to relocate or seal before riding custom scooters in storms.
- Document the drill-and-seal ferrofluid fill method (bit depth marking, RTV choice, temp-sensor add-ons) before we recommend it broadly.
- Add a quick-reference for rescuing rounded fasteners (Dremel slotting, oversized flat-head/“Thor head” drivers, heat) for Thunder/Victor chassis work.
- Outline the Victor-to-Thunder deck swap, including mount spacing checks, swingarm swaps for 70 H hubs, and wiring reroutes after phase-lead shortening.
- Summarize 6.5" tire sourcing, sealant use, and patch-vs-plug decision points so burnout builds stay reliable despite price spikes.
- Expand the VESC Express guide with flashing screenshots, USB-C troubleshooting, and expectations for CAN-only telemetry sessions.
- Collect regen-current heuristics (phase vs. battery) from recent 65 H/85250 builds to prevent brake-induced controller failures.
- Capture Lite and MP2 thermal-mitigation case studies (Arctic MX4 swaps, belly-plate mounting, air vs. liquid cooling) for the controller SOP library.
- Log halo swingarm and fork spacing options (155–200 mm) for accommodating Lonnyo 80 H hubs without excessive machining.
- Turn Noname’s 20 S 32 P moped pack into a packaging brief that balances range, curb weight, and controller selection for seated builds.
