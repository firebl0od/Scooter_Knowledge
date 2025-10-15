# input_part012.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part012.txt`
- Coverage: 2025-03-10T21:50:04 through 2025-06-04T01:48:18 (lines 1–21,984); second-pass extraction now extends through line 200
- Next starting point: Resume at line 201

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
- Dualtron Thunder wobble chasers pointed to stacked variables—factory tires that dislike lean, running only a front brake, uncertain wheel centering, and taller arm settings—while critics called out weak collar clamps and flawed steering geometry; start by lowering the chassis, balancing brakes, and upgrading to PMT or Xuangxeng clones before blaming dampers.【F:data/vesc_help_group/text_slices/input_part012.txt†L101-L121】

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
- Dualtron owners reversing banjo orientation price out Fastride’s kit of stainless 2×M8 banjos (~€40 before shipping) and confirm the bundle includes crush washers/O-rings before buying individual hardware elsewhere.【F:data/vesc_help_group/text_slices/input_part012.txt†L187-L200】

### Motor Architecture and Cooling Concepts
- Builders revisiting axial versus radial flux designs noted axial units mount magnets on disks for higher power density while multi-phase hybrids (“raxial flux”) chase even more torque; most production scooters still ship radial-flux hubs because they are cheaper and leave little room for liquid cooling hardware inside the hollow stator.【F:data/vesc_help_group/text_slices/input_part012.txt†L130-L155】
- Promotional videos showing supposedly liquid-cooled radial hubs drew skepticism once veterans spotted only phase leads—no coolant lines—reinforcing that many marketing clips hide passive designs behind flashy renders.【F:data/vesc_help_group/text_slices/input_part012.txt†L149-L155】

### MP2 Assembly and High-Current Wiring Practices
- Seasoned builders solder copper busbars first, mount FETs second, and terminate phase wires last; leaded solder flows around 200 °C on a hotplate, but keep electrolytic capacitors off the plate to avoid damage.【F:data/vesc_help_group/text_slices/input_part012.txt†L7723-L7738】【F:data/vesc_help_group/text_slices/input_part012.txt†L7813-L7820】
- Proven conductor stack: 8 AWG battery leads and three 12 AWG runs per phase (~10 mm²). 6 AWG physically fits only after stripping strands, which risks bridging FET legs and makes rework miserable once the hardware’s ~420 A protection is tripped.【F:data/vesc_help_group/text_slices/input_part012.txt†L7728-L7762】【F:data/vesc_help_group/text_slices/input_part012.txt†L7790-L7914】
- One rider speculated that extra-long leads might wick heat away from the power stage, but peers immediately challenged the claim—treat the idea as unproven until proper testing surfaces.【F:data/vesc_help_group/text_slices/input_part012.txt†L179-L185】

### High-Voltage Aux Power and Detection Lessons
- MP2’s open 12 V DC/DC bricks remain stable on 30 S packs, but their stock transformer footprint is bulky enough that builders are exploring custom windings to shrink the module for tighter scooters.【F:data/vesc_help_group/text_slices/input_part012.txt†L18881-L18888】
- A single X12 driving a 70H motor tripped ABS overcurrent instantly and boiled the stator to ~130 °C even at 250 A phase; raising absolute current limits gave marginal relief, and riders flagged that low-voltage motor detection (e.g., empty packs or Ubox-derived parameters) amplified the issue versus MP2 detections that “just work.”【F:data/vesc_help_group/text_slices/input_part012.txt†L18900-L18959】【F:data/vesc_help_group/text_slices/input_part012.txt†L18931-L18941】
- When motor launches still felt rough, the group advised re-running detection on fresh firmware and noted that the beta X12 hardware behaves differently from the terminal-equipped release, so expect to iterate before chasing 450 A phase on 26 S packs.【F:data/vesc_help_group/text_slices/input_part012.txt†L18994-L19066】【F:data/vesc_help_group/text_slices/input_part012.txt†L19742-L19750】

### Controller Setup and Interfaces
- Smart Repair reiterated that Spintend’s 100/100 maxes out at 22 S and that regen at that voltage is only safe without the e-brake path; otherwise be prepared to swap FETs. Out of the box it ships with a 135 A phase / 180 A absolute ceiling and omits ST-Link pads and beefy 12 V rails compared with 85xxx units.【F:data/vesc_help_group/text_slices/input_part012.txt†L19186-L19195】
- The aluminum “Lite” variant still generates 12 V internally but lacks the dedicated high-current accessory output found on 85150/85250 hardware, so plan external regulation when powering lighting or fans.【F:data/vesc_help_group/text_slices/input_part012.txt†L19262-L19266】
- Ubox 100/100 owners must wire the latching start button (16 mm panel cut-out) because the controller will not boot from USB-C alone; the port is strictly for VESC Tool data, so bench work still needs a pack or supply. Some riders bury the switch and rely on the BMS as a crude master disconnect, but they acknowledge it is a hack.【F:data/vesc_help_group/text_slices/input_part012.txt†L19300-L19318】
- The CAN header can back-feed 5 V lights, yet builders stress adding an inline resistor and note the servo header’s PWM codebase if you want blink or brake behavior instead of an always-on lamp.【F:data/vesc_help_group/text_slices/input_part012.txt†L19323-L19334】【F:data/vesc_help_group/text_slices/input_part012.txt†L19402-L19405】
- Jason’s latest 32 S-capable BMS board omits discharge FETs, effectively giving the pack “infinite” output. That keeps high-power scooters online but shifts all short-circuit protection to downstream hardware.【F:data/vesc_help_group/text_slices/input_part012.txt†L19339-L19342】

### Observers, Mixed Drivetrains, and Traction Control
- Russian builders are pairing Fardriver rear controllers with VESC fronts, splitting the throttle over a CAN-bus Y harness to let each brain manage its own motor while still sharing one input.【F:data/vesc_help_group/text_slices/input_part012.txt†L19592-L19605】
- Riders debating Ortega versus Mxlemming observers found that Mxlemming with ~125 A field weakening needed higher ABS thresholds (~420 A) to avoid overcurrent trips at 300 A phase, while lighter settings (30 A FW) still triggered ABS on high-grip launches.【F:data/vesc_help_group/text_slices/input_part012.txt†L19689-L19724】
- Front 40-pole and rear 30-pole motor mixes still confuse traction control, so some racers forgo TC altogether and instead preload the bar to keep weight over the front tire during hard exits.【F:data/vesc_help_group/text_slices/input_part012.txt†L19528-L19537】【F:data/vesc_help_group/text_slices/input_part012.txt†L19596-L19610】

### Battery, BMS, and Pack Planning
- Medhi Cantin is flogging a 20 S 9 P P45B pack at 900 A burst (650 A for a full minute) but is eyeing 22 S upgrades and tabless 45D/40PL cells to cut voltage sag under 60 A per parallel string.【F:data/vesc_help_group/text_slices/input_part012.txt†L19216-L19238】
- ANT now advertises a 10–32 S smart BMS SKU covering 8–20 S with 220 A continuous / 550 A peak, giving 20 S scooters another option when 7–20 S units are out of stock; even so, Yamal wants 350–400 A continuous headroom for dual 85/25x builds.【F:data/vesc_help_group/text_slices/input_part012.txt†L20178-L20234】
- Large ANT variants start at 61.2 V minimum (17 S), so long-range riders who occasionally dip 20 S packs to 59–60 V either oversize the BMS or accept that “fully open door” behavior with practically no low-voltage cutoff.【F:data/vesc_help_group/text_slices/input_part012.txt†L20185-L20224】
- Yamal is pairing the new 85/240 with an older 85/250 “Viking” controller, but expects to re-drill his heatsink because the refreshed 85/240 chassis moved its mounting pattern.【F:data/vesc_help_group/text_slices/input_part012.txt†L20080-L20086】【F:data/vesc_help_group/text_slices/input_part012.txt†L20234-L20237】

### Wheels, Tires, and Brakes
- 3 mm-thick 180 mm rotors combined with slicks transformed halo builds—riders dropped in 110/50-6.5 clones up front and 90/65-6.5 rears for a rounder profile but warned the cheap “fake PMT” rubber is very soft in summer heat.【F:data/vesc_help_group/text_slices/input_part012.txt†L19916-L19937】【F:data/vesc_help_group/text_slices/input_part012.txt†L19989-L20027】
- Shlomozero runs 220 A phase on the front and still skids at 30 psi; French racers counter with 14 psi PMTs for turn-in grip, underscoring how pressure tuning depends on compound.【F:data/vesc_help_group/text_slices/input_part012.txt†L20313-L20324】

### Build Spotlights and Reliability Signals
- Rob Ver’s latest scooter is an 80H, 22 × 3 setup on 110/100 rims that’s already clocked 132 km/h, demonstrating what wide 123 mm tires and big packs deliver when aero and stance cooperate.【F:data/vesc_help_group/text_slices/input_part012.txt†L20347-L20366】
- Xiaomi 4 Lite owners logged 50 km hammer sessions that left the stock motor smoking, a reminder that extended field-weakening runs will cook commuter-class hubs without cooling mods.【F:data/vesc_help_group/text_slices/input_part012.txt†L20326-L20329】
- Smart Repair finally saw 250 A rear / 140 A front X12 settings hold torque without ABS cutouts after re-detecting the motors, though traction is still limited by the GT1 front hub compared with dual 70H plans.【F:data/vesc_help_group/text_slices/input_part012.txt†L19904-L19937】
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

### Security, Tracking, and Theft Response
- Owners now budget roughly €50 per scooter for layered tracking—pairing Samsung SmartTags with Apple AirTags and planning a GPS IoT beacon for higher-value builds kept one stolen ebike recoverable, though riders still warn against confronting thieves directly.【F:data/vesc_help_group/text_slices/input_part012.txt†L124-L170】

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

### Additional Findings (Lines 14,380–15,879)

#### Fast Charging, Pack Capacity, and BMS Safeguards
- Hyper chargers are becoming common in the group: riders now push 6 kW from EV posts, with charge rates capped either by the battery (Jason) or by the public pedestal (Noname); the hardware itself runs roughly US $400 but some owners have over US $2 k tied up in the setup.【F:data/vesc_help_group/text_slices/input_part012.txt†L14381-L14405】
- Noname’s 32 P Samsung 35E pack holds ≈112 Ah (≈9.4 kWh) and delivers ~70 mi before noticeable voltage drop, making it a real-world benchmark for long-range seated builds.【F:data/vesc_help_group/text_slices/input_part012.txt†L14605-L14628】
- Shlomozero warns that shorting auxiliary leads on a VESC logic board is an expensive mistake—tapping controller power directly can blow a $90 component—so lighting and accessories still need isolated supplies.【F:data/vesc_help_group/text_slices/input_part012.txt†L14647-L14647】
- JK BMS hardware has already saved builds from overcurrent: Noname tripped a 60 A BMS by running 70 A battery on a C80 conversion and now plans a 20 S 3 P pack instead of bypassing protection.【F:data/vesc_help_group/text_slices/input_part012.txt†L15649-L15657】【F:data/vesc_help_group/text_slices/input_part012.txt†L15753-L15756】
- Jason’s copper “sandwich” bus links for a high-current battery look clean but concentrate ~150 A through a narrow junction; he’s consulting PCB trace calculators to ensure enough copper cross-section before final assembly.【F:data/vesc_help_group/text_slices/input_part012.txt†L15851-L15872】

#### Controller Limits, Firmware Tweaks, and Repairs
- Community consensus keeps Spintend 85/250 controllers near 200 A battery / 300 A phase for longevity; several riders run higher currents only with upgraded MOSFETs or heavy cooling, and Yamal flatly calls 350 A “not safe.”【F:data/vesc_help_group/text_slices/input_part012.txt†L14792-L14829】【F:data/vesc_help_group/text_slices/input_part012.txt†L15259-L15307】
- Finn has proven the Ubox 100/100 Lite can deliver ~170 A phase / 90 A battery after flashing Vedder’s no-hardware-limit 6.05 firmware, while others sit around 130 A unless they lift the stock caps—Noname hit ~6–7 kW before deciding a larger controller might be safer.【F:data/vesc_help_group/text_slices/input_part012.txt†L15099-L15106】【F:data/vesc_help_group/text_slices/input_part012.txt†L15365-L15388】
- MakerX S100 footpads need the 3.3 V rail, not 5 V, on their hall outputs; Jason walked Ohad through probing the connector to confirm both ADC lines have reference voltage before blaming the pad itself.【F:data/vesc_help_group/text_slices/input_part012.txt†L15350-L15359】【F:data/vesc_help_group/text_slices/input_part012.txt†L15674-L15674】
- 3Shull owners report the C350 stack reliably handles 400 A phase / 200 A battery at 22 S when installed carefully, and Figiwara is now repairing failed units—three boards were recently returned to service—giving high-power riders another support channel.【F:data/vesc_help_group/text_slices/input_part012.txt†L15233-L15237】【F:data/vesc_help_group/text_slices/input_part012.txt†L15877-L15880】
- The group continues to contrast controller options: Seven units win praise for their beefy signal connectors, while Fardrivers are still recommended only when packaging allows far larger enclosures.【F:data/vesc_help_group/text_slices/input_part012.txt†L14750-L14757】【F:data/vesc_help_group/text_slices/input_part012.txt†L15249-L15251】

#### Frames, Compliance, and Packaging Experiments
- Yamal now keeps his modified Nami out of city centers and uses a sleeper Ninebot to stay under 25 km/h enforcement, underscoring the need for legal profiles in dense areas.【F:data/vesc_help_group/text_slices/input_part012.txt†L14630-L14634】【F:data/vesc_help_group/text_slices/input_part012.txt†L15021-L15022】
- Noname detailed how the Segway C80 moped swallows a 32 P battery: cut the plastic trunk for four 6×10 cell layers, massage the corners, and note the ~165 mm dropout that accepts threaded 10" hubs with drum brakes and sprocket mounts.【F:data/vesc_help_group/text_slices/input_part012.txt†L15770-L15788】
- Tire sizing on these mopeds is confusing—advertised 14" bicycle tires ride on ~10" rims—so sourcing motors by outer diameter (≈350 mm) avoids mismatches when upgrading hubs or sprocket carriers.【F:data/vesc_help_group/text_slices/input_part012.txt†L15792-L15809】
- Scrtt is hunting 75 H hubs for Thunder swingarms and confirmed different stator widths exist, reinforcing the need to double-check axle spacing before ordering high-torque motors.【F:data/vesc_help_group/text_slices/input_part012.txt†L15817-L15818】

#### Operational Notes and Community Resources
- Segway C80 fast-charge tests show the stock 100/100 Lite happily delivers ~6–7 kW at mid-pack SOC, convincing builders they can keep compact scooters relevant if the battery and cooling cooperate.【F:data/vesc_help_group/text_slices/input_part012.txt†L15099-L15106】
- ZT3 delivery scooters are proliferating in Spain; Yamal highlights them as a legal, utility-focused option compared with outlaw Nami builds.【F:data/vesc_help_group/text_slices/input_part012.txt†L15717-L15718】
- Group repair ecosystems continue to mature: Smart Repair awaits Chinese shipments while regional experts like Figiwara take on controller refurbishments to keep scarce hardware running.【F:data/vesc_help_group/text_slices/input_part012.txt†L15218-L15223】【F:data/vesc_help_group/text_slices/input_part012.txt†L15877-L15880】

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
- Summarize the 6 kW hyper-charger setups (hardware cost, EV pedestal limits vs. battery limits) so tour riders can copy reliable fast-charge recipes.
- Document the Ubox 100/100 Lite limit-removal workflow (firmware link, proven current ceilings, and thermal caveats) before more owners flash blindly.
- Capture a MakerX S100 footpad wiring note that highlights the 3.3 V requirement and connector pinout checks.
- Turn Noname’s Segway C80 battery packaging walkthrough (4×6×10 cell stack, 165 mm dropout, drum/sprocket hardware) into a proper retrofit guide.
- Collect 3Shull support contacts (e.g., Figiwara) and outline shipping/repair expectations for riders outside the main service regions.
- Add a quick-reference for rescuing rounded fasteners (Dremel slotting, oversized flat-head/“Thor head” drivers, heat) for Thunder/Victor chassis work.
- Outline the Victor-to-Thunder deck swap, including mount spacing checks, swingarm swaps for 70 H hubs, and wiring reroutes after phase-lead shortening.
- Summarize 6.5" tire sourcing, sealant use, and patch-vs-plug decision points so burnout builds stay reliable despite price spikes.
- Expand the VESC Express guide with flashing screenshots, USB-C troubleshooting, and expectations for CAN-only telemetry sessions.
- Collect regen-current heuristics (phase vs. battery) from recent 65 H/85250 builds to prevent brake-induced controller failures.
- Capture Lite and MP2 thermal-mitigation case studies (Arctic MX4 swaps, belly-plate mounting, air vs. liquid cooling) for the controller SOP library.
- Log halo swingarm and fork spacing options (155–200 mm) for accommodating Lonnyo 80 H hubs without excessive machining.
- Turn Noname’s 20 S 32 P moped pack into a packaging brief that balances range, curb weight, and controller selection for seated builds.
- Capture lessons from the 32 S 20 P Segway moped (weight, charging strategy, desired controller swap) before revisiting longer-range seated conversions.
- Publish an 85/250 current-limit cheat sheet that balances 22 S voltage, 300 A phase ceilings, and when 260 A battery experiments become risky.
- Write a Ubox 100/100 Lite “no hardware limits” flashing walkthrough (including mobile workflows) so owners can safely exceed the stock 135 A phase limit.
- Document the Segway C80 battery-box trimming and shock-bracket notch required to fit four 6×10 cell layers without ruining the plastics.
- Add a JK BMS sizing and thermal note explaining why bypassing a 60 A unit is dangerous and how to spec replacements for 70 A+ goals.
- Evaluate Jason’s copper-sandwich link and publish minimum conductor width/fastener guidance for 150 A battery bridges.
- Create a MakerX S100/Onewheel footpad wiring checklist that confirms 3.3 V supply, ADC routing, and common failure points.

### Additional Findings (Lines 14,380–15,879)

#### High-Capacity Mopeds, Charging, and Range Planning
- Noname’s Segway-based moped now tips the scales around 350 lb before the rider and gear, making it hard to lift over obstacles; he would redo it as a lighter 32 S 20 P build with a Seven controller to regain torque without sacrificing the group’s 50‑mile minimum range.【F:data/vesc_help_group/text_slices/input_part012.txt†L14361-L14364】【F:data/vesc_help_group/text_slices/input_part012.txt†L14372-L14379】
- The crew rides with Hyper Chargers and EV adapters in tow—Noname can pull 6 kW until public posts throttle back, while Jason’s pack is the bottleneck on his charger, reinforcing the need to size battery charge rates to available infrastructure.【F:data/vesc_help_group/text_slices/input_part012.txt†L14372-L14388】
- That moped’s 32 P Samsung 35E pack stores ≈9.4 kWh (112 Ah) and still delivers about 70 mi before noticeable voltage sag, demonstrating the real-world range ceiling for dense seated builds.【F:data/vesc_help_group/text_slices/input_part012.txt†L14605-L14628】

#### Ergonomics, Packaging, and Safety
- The extra-long seat forces the rider to hunch; taller bars or using the passenger pegs to straighten posture improve comfort on long rides.【F:data/vesc_help_group/text_slices/input_part012.txt†L14560-L14568】
- Jason’s hasty MP2-to-ebike transplant wheelied instantly because the rear pack dominated the weight balance; he plans to move to a 14 S 6 P frame-mounted battery and extend the brake/regen wiring to control lift-over events.【F:data/vesc_help_group/text_slices/input_part012.txt†L15111-L15130】

#### Controller Selection, Current Limits, and Cooling
- Paolo warns that despite FarDriver’s apparent stability from oversizing, he still avoids it on scooters, underscoring continued preference for VESC-class gear in compact chassis.【F:data/vesc_help_group/text_slices/input_part012.txt†L14642-L14644】【F:data/vesc_help_group/text_slices/input_part012.txt†L14876-L14879】
- Yamal pegs the Spintend 85/250 sweet spot at ≈300 A phase / 200 A battery on 22 S packs—350 A will run but isn’t “safe,” and only custom builds attempt 260 A battery—and Shlomozero notes 90 H hubs feel best with 300–400 A phase, leaving 500 A to larger Ambrosini or Nucular stacks.【F:data/vesc_help_group/text_slices/input_part012.txt†L15288-L15307】【F:data/vesc_help_group/text_slices/input_part012.txt†L15290-L15297】
- Firmware on Ubox 100/100 Lites defaults to 135 A phase and 180 A absolute, but the community leans on Vedder’s “no hardware limits” 6.05 binary to reach 170 A phase and 150 A+ logs when packs and cooling permit.【F:data/vesc_help_group/text_slices/input_part012.txt†L15090-L15106】【F:data/vesc_help_group/text_slices/input_part012.txt†L15365-L15383】

#### Motor, Wheel, and Frame Fitment
- Skrtt confirmed that worn GT-series rims can be replaced without swapping the hub—“rim only” orders from AliExpress still demand a clean bill of health on the motor itself.【F:data/vesc_help_group/text_slices/input_part012.txt†L14671-L14680】
- Konyk’s conversion kits include the required axle nuts, easing rear motor installs when stock hardware is discontinued.【F:data/vesc_help_group/text_slices/input_part012.txt†L14868-L14874】
- Segway C80 chassis accept 10" hubs with ~165 mm dropout spacing; Noname shoehorned four layers of 6×10 cells under the seat by trimming the plastic tub and would only need to notch the upper shock bracket for a cleaner install, leaving the exterior panels untouched.【F:data/vesc_help_group/text_slices/input_part012.txt†L15770-L15788】
- The same frame ships with threaded sprocket mounts and drum brakes, so future chain or QS/Lonyeo hub swaps remain feasible if sprocket spacing is managed.【F:data/vesc_help_group/text_slices/input_part012.txt†L14868-L14873】【F:data/vesc_help_group/text_slices/input_part012.txt†L15782-L15788】

#### Batteries, BMS Limits, and Thermal Notes
- JK’s 60 A BMS saved Noname when he mistakenly set the VESC to 70 A battery; he now caps output at 60 A/130 A phase, which leaves the motor around 76 °C and plans a new 20 S 3 P pack plus higher-current BMS instead of bypassing protections.【F:data/vesc_help_group/text_slices/input_part012.txt†L15649-L15657】【F:data/vesc_help_group/text_slices/input_part012.txt†L15753-L15756】【F:data/vesc_help_group/text_slices/input_part012.txt†L15784-L15788】
- Jason’s copper “sandwich” link worries him because the entire 150 A path necks down through a tiny joint; his PCB-trace math says 0.2 mm copper needs ≈50 mm width at that current, so he’s reevaluating the connection before final assembly.【F:data/vesc_help_group/text_slices/input_part012.txt†L15851-L15872】

#### Firmware, Wiring, and Diagnostics
- Builders swapping stock dashboards onto MakerX S100s must power the Onewheel footpad with the ESC’s 3.3 V rail on both ADCs and verify the regulator actually reaches the pad—missing the 3.3 V feed leaves the sensor dead even when the wiring diagram is correct.【F:data/vesc_help_group/text_slices/input_part012.txt†L15314-L15357】
- Tap only the logic rails you intend: Shlomozero reminds everyone that shorting accessories off the VESC power bus is a $90 mistake, and even stock G30 throttles expect 3.3 V logic on the MakerX 100/100 rather than 5 V.【F:data/vesc_help_group/text_slices/input_part012.txt†L14647-L14647】【F:data/vesc_help_group/text_slices/input_part012.txt†L15649-L15676】
- When transplanting G30 hubs, color-matching phase leads works across model years, but newer scooters require flipping the “new motor” flag inside the Segway firmware before anything spins.【F:data/vesc_help_group/text_slices/input_part012.txt†L15651-L15655】

#### Repair and Support Signals
- 🇪🇸AYO reports that Figiwara has already revived three failed 3Shull controllers for the race crew, highlighting an emerging repair channel for those premium boards.【F:data/vesc_help_group/text_slices/input_part012.txt†L15877-L15879】

### Additional Findings (Lines 17,380–18,879)

#### Tires, Traction, and Dual-Controller Basics
- Riders vet budget 90/65-6.5 tires by forcing a skid—nylon clones squeal loudly while real rubber heats up and feels sticky after a burnout—before trusting them at speed.【F:data/vesc_help_group/text_slices/input_part012.txt†L17386-L17453】
- Makerbase dual-drive owners reiterated that linking controllers over CAN is the first setup step; share CAN H/L between both units (no positive lead) so the pair synchronizes before pairing Bluetooth modules.【F:data/vesc_help_group/text_slices/input_part012.txt†L17400-L17407】【F:data/vesc_help_group/text_slices/input_part012.txt†L18508-L18510】

#### High-Power Builds and Tuning Benchmarks
- Max Rainlogix’s Thunder (dual Lonnyo 70/110 hubs, Ubox 85/240) hauled two riders up a bridge at 320 A battery without overheating (23–28 °C) using 150/200 A rear and 120/140 A front phase limits plus traction control; earlier 200/300 A tests proved viable but wheelie-prone.【F:data/vesc_help_group/text_slices/input_part012.txt†L17755-L17783】【F:data/vesc_help_group/text_slices/input_part012.txt†L17788-L17790】
- Yamal continues to treat 175 A battery / 300 A phase per controller as the safe daily ceiling on his Nami after past failures, giving newcomers a proven baseline before chasing higher currents.【F:data/vesc_help_group/text_slices/input_part012.txt†L18335-L18360】
- Noname’s Ortega observer recommendation remains the go-to fix for 75 200 launches that stutter under hard throttle, with owners confirming it resolves full-twist lockups on 5 kW hubs.【F:data/vesc_help_group/text_slices/input_part012.txt†L18580-L18587】

#### Battery Fabrication and Protection Practices
- Copper bus links for 450 A packs have worked reliably at 0.2 mm thickness; builders source wide T2 foil and note thinner stock (0.1 mm) is only for low-heat soldering jobs.【F:data/vesc_help_group/text_slices/input_part012.txt†L18181-L18205】
- A rear controller fire at just 35–40 km/h underscored the risk of bypassed BMS hardware—without discharge protection or fuses the pack dumped unchecked current until flames erupted—prompting renewed calls for fuses and quality BMS options such as JBD instead of ANT units.【F:data/vesc_help_group/text_slices/input_part012.txt†L18420-L18467】
- After the incident, Yamal committed to installing a full-protection BMS (shopping high-current ANT/JBD options around US $100) instead of running charge-only boards, reinforcing best practice for 20 S+ builds.【F:data/vesc_help_group/text_slices/input_part012.txt†L18524-L18542】【F:data/vesc_help_group/text_slices/input_part012.txt†L18533-L18546】

#### Instrumentation, Displays, and Harness Notes
- Builders weighing dash upgrades flagged fresh options beyond Davega—the 3Shull display and Trampa units both integrate cleanly with VESC—and keep AliExpress VESC screens as budget fallbacks.【F:data/vesc_help_group/text_slices/input_part012.txt†L18547-L18555】
- Ninebot Vsett wiring questions were answered with a reminder that throttle, brake, lights, and indicators all break out through the main 6-pin display harness, simplifying VESC conversions.【F:data/vesc_help_group/text_slices/input_part012.txt†L18563-L18565】
- Makerbase 84 200 controllers accept keyed power through an external switch or dashboard—users safely repurpose the display’s power button circuit to wake the VESC rather than hot-wiring the pack leads.【F:data/vesc_help_group/text_slices/input_part012.txt†L18610-L18618】

#### Supply Chain and Controller Branding Signals
- European racers confirmed that Ambrosini’s RS500, Rage’s Robers units, and MakerX’s stock G300 share the same hardware despite different labels; price gaps largely come from branding and marketing rather than electrical upgrades.【F:data/vesc_help_group/text_slices/input_part012.txt†L18381-L18399】
- When budget-hunting, veterans still steer newcomers toward Spintend, Tronic, or Seven controllers for proven QC and support, reserving Makerbase 84xxx boards for projects where occasional failures are acceptable.【F:data/vesc_help_group/text_slices/input_part012.txt†L18610-L18618】
- Spintend’s 85/240 shipments now transit a New Jersey hub for U.S. customers, and orders under US $1,000 have arrived without added tariffs, easing access to higher-phase hardware stateside.【F:data/vesc_help_group/text_slices/input_part012.txt†L18632-L18638】

#### Build Spotlights and Performance Benchmarks
- A Swedish “hyper” project is stepping to 22×3 windings with 700 mm bars, a steering damper, and guidance from @jamessoderstrom after clocking 117 km/h on a Rage Mechanics–equipped G30—proof that heavily braced stems and damper hardware are mandatory once commuters pass triple-digit speeds.【F:data/vesc_help_group/text_slices/input_part012.txt†L18184-L18218】
- Rage Mechanics’ RM-Light race scooter (Dualtron Compact frame, 22 S 4 P pack, C350 RM-X rear motor, Beringer brakes, titanium pole) hits 140 km/h yet weighs just 37 kg, but it is strictly a 17-minute track setup rather than a street build.【F:data/vesc_help_group/text_slices/input_part012.txt†L18600-L18609】
- Hackintosh logged 127 km/h and 26.5 kW from his latest scooter, while Arnau catalogued a 23 S 13 P (≈60 Ah) LG M50/M58 battery, giving builders fresh reference points for 96 V-class commuters.【F:data/vesc_help_group/text_slices/input_part012.txt†L18820-L18851】【F:data/vesc_help_group/text_slices/input_part012.txt†L18846-L18851】
### Additional Findings (Lines 15,880–17,379)

#### Controller Networking, Repairs, and Firmware Hygiene
- Figiwara quoted €60 /hr for electronics work and reiterated that linked VESCs share CAN on pins 1/3—if a dual-stack refuses to sync, change the CAN IDs in VESC Tool and reboot both controllers before assuming the transceiver is dead.【F:data/vesc_help_group/text_slices/input_part012.txt†L15888-L15926】
- 🇪🇸AYO’s four freshly “repaired” 3Shull controllers still refuse to boot despite €1,700 invested, underscoring how thin the dependable support network remains for those boards once they fail in the field.【F:data/vesc_help_group/text_slices/input_part012.txt†L16235-L16246】
- A shorted MKSESC 75100 V2 kept running after desoldering the damaged parts but lost its 5 V rail, so the owner is hunting the onboard DC/DC regulator or planning an external converter replacement—evidence that logic rails can remain crippled long after the main power stage survives a fault.【F:data/vesc_help_group/text_slices/input_part012.txt†L16233-L16234】【F:data/vesc_help_group/text_slices/input_part012.txt†L16253-L16253】
- Builders flashing 6.06 betas were reminded that VESC Tool must match controller firmware; download the same beta package on desktop, rebuild/flash both VESCs, and rerun detection to clear “limited mode” warnings on mobile apps.【F:data/vesc_help_group/text_slices/input_part012.txt†L16693-L16700】【F:data/vesc_help_group/text_slices/input_part012.txt†L17080-L17080】

#### Controller Selection, Power Distribution, and Limits
- Smart Repair’s dual X12 build (26 S 8 P P42A, 70H rear plus GT1 front hub) burned both onboard DC/DC stages after a shared relay tied their power buttons together; the X12 only budgets about 0.4 A at 5 V for internal logic, lacks CAN-based shutoff, and hides its 12 V rail off the main harness, so lighting and accessories need a dedicated converter rather than parasitically loading the controller.【F:data/vesc_help_group/text_slices/input_part012.txt†L16099-L16107】【F:data/vesc_help_group/text_slices/input_part012.txt†L16293-L16305】【F:data/vesc_help_group/text_slices/input_part012.txt†L16352-L16378】
- Follow-up probing confirmed the X12 does expose 12 V internally, but siphoning power through the ADC headlight feed drags the logic rail and torpedoes range—route accessories to their own supply instead of stepping down from battery and back up on the dash.【F:data/vesc_help_group/text_slices/input_part012.txt†L16369-L16387】
- 🇸🇪'lekrsu cataloged Ninebot G3 internals: a VCU governs the dash, auto-headlight, gyro-based power assist, single-motor traction control, dormant deck LEDs, and even a light sensor—all unlockable via ST-Link if you want the hardware you already paid for to function.【F:data/vesc_help_group/text_slices/input_part012.txt†L16390-L16407】
- Pandalgns continues to abuse Makerbase 84200s at ~350 A battery on 60 V and is preparing to jump to 22 S while waiting for the higher-rated 100300 model to return from a recall, suggesting the low-cost boards can be treated as consumables when compared with premium controllers.【F:data/vesc_help_group/text_slices/input_part012.txt†L16242-L16252】【F:data/vesc_help_group/text_slices/input_part012.txt†L16269-L16278】
- French racers report the waterproofed 18-FET G300 runs happily on 22 S with roughly 250 A battery / 500 A phase peaks but overheats if you hammer regen, and its continuous current still trails the Spintend 85/250 even though the burst power is stronger—use it as a street or sprint controller, not a sustained hill-climb unit.【F:data/vesc_help_group/text_slices/input_part012.txt†L16861-L16867】
- Yamal’s 22 S shortlist (X12, Seven18, C350, G300, Trampa 100/250, Thor 400, MakerX, 3Shull, Tronic) plus his own 85/250 “Uppsala” Nami tuned at ~300 A phase per 80H motor gives builders a concrete shopping menu when speccing high-voltage scooters.【F:data/vesc_help_group/text_slices/input_part012.txt†L16868-L16887】

#### Custom Builds, Range Logs, and Component Mods
- Smart Repair’s 26 S dual-drive project still needs widened front suspension to accept a 70H hub, illustrating how even seasoned builders must rework chassis geometry once they chase multi-kilowatt 12" motors up front.【F:data/vesc_help_group/text_slices/input_part012.txt†L16099-L16107】
- A German rider converted a NIU from single to dual hub by grafting a Soflow motor into the fork, rewinding the stock rear motor into delta, and feeding both with modified Flipsky 75/100 controllers; the 18 S 7 P (18650 30 A BAK) pack and 95 A/40 A (front) plus 140 A/70 A (rear) tuning now push the moped to about 90 km/h, though repeated 90→0 km/h stops cook its 120 mm rotor without regen assist.【F:data/vesc_help_group/text_slices/input_part012.txt†L16909-L16967】
- Noname logged a 148‑mile day on his NIU conversion—mixing paved roads, dirt, and hikes—and has previously forded 12"-deep water on the Bosch-powered build, hinting at the real-world endurance and environmental abuse these seated VESC rigs can absorb.【F:data/vesc_help_group/text_slices/input_part012.txt†L16984-L17014】
- Spintend’s 85/240 controllers are now shipping out of New Jersey for U.S. buyers, giving North American builders a faster path to higher-phase hardware than direct-from-China orders.【F:data/vesc_help_group/text_slices/input_part012.txt†L17321-L17325】

#### Racing, Strategy, and Rulesets
- Face de Pin Sucé reminded skeptics that E‑Trott championships cap entries at 35 kW and 22 S, so straight-line victories still hinge on launch timing, traffic-light memorization, and pairing the sharpest riders with the legal torque envelope.【F:data/vesc_help_group/text_slices/input_part012.txt†L16726-L16745】【F:data/vesc_help_group/text_slices/input_part012.txt†L16769-L16770】

### Additional Findings (Lines 20,381–21,880)

#### Tires, Rims, and Suspension Packaging
- Builders confirmed jumbo tires will clear swingarms with about 4″ per side but warned that slicks become unforgiving on wet pavement, so rain setups need conservative throttle maps or treaded rubber.【F:data/vesc_help_group/text_slices/input_part012.txt†L20389-L20397】
- Rob Ver’s Vsett 11 runs a 110/100 rim around an 80H hub under the deck; by stretching 80 mm rubber onto 100 mm rims, lowering the suspension, and favoring 130/40 PMTs he keeps tire temps and controller bay temperatures around 40 °C even during hard street use.【F:data/vesc_help_group/text_slices/input_part012.txt†L21047-L21052】【F:data/vesc_help_group/text_slices/input_part012.txt†L21444-L21461】
- Ausias’ speed-wound 70H/80H tubeless motors highlighted why high-travel (150 mm) suspensions force controllers up into the chassis—previous under-deck mounts scraped—while 🇪🇸AYO reminded that tubeless split rims seal with model-specific O-rings sourced from bearing/seal houses.【F:data/vesc_help_group/text_slices/input_part012.txt†L21582-L21615】【F:data/vesc_help_group/text_slices/input_part012.txt†L21649-L21654】
- Ambrosini/LY CNC rims continue to sit near €100–€120 each and expect wider 155 mm axles for 6.5" fitments; riders also confirmed LY harnesses ship with hefty AWG 7–8 phase sleeves.【F:data/vesc_help_group/text_slices/input_part012.txt†L21060-L21075】【F:data/vesc_help_group/text_slices/input_part012.txt†L21726-L21734】【F:data/vesc_help_group/text_slices/input_part012.txt†L21628-L21629】

#### Controller Mounting, Wiring, and Diagnostics
- ’lekrsu keeps Spintend Alu Lite units cool by printing an adapter that bolts into the stock charger mount and adding a 0.5 mm thermal pad, while others fall back to thermal glue; the downside is that 85/240-class boards still lack mounting ears and ship with tiny M2.5 hardware that many riders retap to sturdier screws.【F:data/vesc_help_group/text_slices/input_part012.txt†L20537-L20541】【F:data/vesc_help_group/text_slices/input_part012.txt†L20575-L20583】【F:data/vesc_help_group/text_slices/input_part012.txt†L21036-L21041】
- Flipsky’s 75100 Pro V2 reading as a 75300 in VESC Tool is expected—the original V1 behaved the same—so owners can ignore the label mismatch.【F:data/vesc_help_group/text_slices/input_part012.txt†L20535-L20536】
- Vsett wiring checks pegged orange as pack voltage, pink as the on/off detect line, white as brake, and black as ground; continuity testing before repinning remains best practice.【F:data/vesc_help_group/text_slices/input_part012.txt†L20635-L20637】
- To stay legal in 25 km/h zones, riders keep a “permanent” low-speed profile loaded and simply power-cycle to escape it after police checks, which is faster than digging through VESC Tool on the street.【F:data/vesc_help_group/text_slices/input_part012.txt†L20585-L20592】【F:data/vesc_help_group/text_slices/input_part012.txt†L20613-L20613】
- Regenerative braking requires filling in Motor Current Max Brake/Max Regen; when halls misbehave, inexpensive AliExpress testers let riders validate sensors without dismantling sealed motors, and temperature probes should land on the controller’s temp+GND pins rather than 5 V.【F:data/vesc_help_group/text_slices/input_part012.txt†L20710-L20711】【F:data/vesc_help_group/text_slices/input_part012.txt†L20661-L20684】【F:data/vesc_help_group/text_slices/input_part012.txt†L20677-L20678】
- Spintend’s ADC lighting board must be wired per the manufacturer diagrams—one owner resolved button issues after rewiring to match the factory instructions—and Dimos reiterated that Ortega observers or lower phase amps tame mxlemming overcurrent faults, with saturation compensation as a last resort.【F:data/vesc_help_group/text_slices/input_part012.txt†L20947-L20955】【F:data/vesc_help_group/text_slices/input_part012.txt†L21057-L21059】
- Builders even nitpicked consumables: GB-brand zip ties from U.S. big-box stores crack in cold weather, pushing crews toward industrial nylon or imported bundles for harness retention.【F:data/vesc_help_group/text_slices/input_part012.txt†L20581-L20587】

#### Battery Building and Thermal Practices
- G30 and Vsett builders mapped their packaging ceilings—Forol squeezed 20 S 6 P (and maybe 7 P with printed spacers) into a dual-motor frame, while ’lekrsu warned newcomers not to tuck cell groups below the chassis ledge because the cover and BMS still need that volume.【F:data/vesc_help_group/text_slices/input_part012.txt†L20504-L20512】【F:data/vesc_help_group/text_slices/input_part012.txt†L20584-L20587】
- Yamal is swapping his charge-only 40 A BMS after a 35 km/h brownout, reinforcing that high-power scooters need full-protection boards and tidy temp-sensor wiring (temp-to-temp, GND-to-GND) to avoid mystery cutbacks.【F:data/vesc_help_group/text_slices/input_part012.txt†L20668-L20678】
- Rob Ver’s 22 S 9 P Ampace JP40 pack reports ~45 A continuous/140 A peak per cell with only ~6 V of sag compared with hotter-running Molicels, making the tabless JP40s his go-to for >300 A scooters.【F:data/vesc_help_group/text_slices/input_part012.txt†L20985-L20999】
- The same pack relies on 0.2 mm copper busbars yet stays under 30 °C at 500 A, and his earlier 21 S 9 P LG M58T build—stacked with 0.1 mm copper plus 0.1 mm nickel—still delivers 2×100 A at ~40 °C, showing how thin laminations work when cooling and spacing are dialed.【F:data/vesc_help_group/text_slices/input_part012.txt†L21469-L21479】【F:data/vesc_help_group/text_slices/input_part012.txt†L21564-L21576】
- Rob also proved a 22 S 9 P (≈37 Ah) pack and both controllers fit inside a Vsett 11 deck if you custom-machine spacers down to the last millimetre, though he prefers sleeper aesthetics to dodge EU police scrutiny.【F:data/vesc_help_group/text_slices/input_part012.txt†L21481-L21505】
- Even stock hardware insights matter: a lightly used Segway Max G2 battery with ~50–60 cycles, always stored indoors, sets a baseline for second-hand pack condition.【F:data/vesc_help_group/text_slices/input_part012.txt†L20442-L20444】

#### High-Power Performance and Limits
- Rob Ver’s Spintend 240A on 22 S with 120 V MOSFETs is touching 35 kW and 132 km/h on 22×3 hubs using ~80 A field weakening, but he still bakes tires into burnouts until 60 mph and has already replaced MOSFETs twice—once because a 22 S BMS failed during a 320 A launch.【F:data/vesc_help_group/text_slices/input_part012.txt†L20627-L20633】【F:data/vesc_help_group/text_slices/input_part012.txt†L20758-L20773】
- His older Dualtron chassis also shows the practical ceiling of legacy motors: even with 116 A per controller the GT1 front hub can’t accept more without free-spinning, so he’s hunting 110 slick PMTs and more aggressive weight transfer to hook up.【F:data/vesc_help_group/text_slices/input_part012.txt†L20803-L20810】【F:data/vesc_help_group/text_slices/input_part012.txt†L21005-L21012】
- Smart Repair’s latest build now runs 420 A phase at the rear and only 120 A up front on a GT1 motor, paired with 85 A battery limits, because the front tire still spins at 80 km/h—traction, not controller headroom, is the bottleneck.【F:data/vesc_help_group/text_slices/input_part012.txt†L21777-L21796】
- EU riders keep reminding each other that, despite 22 S packs and 200 A configs, public roads remain capped at 25 km/h and enforcement is tightening, so stealth profiles and disciplined launches matter as much as raw power.【F:data/vesc_help_group/text_slices/input_part012.txt†L20976-L20983】【F:data/vesc_help_group/text_slices/input_part012.txt†L21224-L21252】

#### Market, Legal, and Procurement Notes
- Spain’s 2027 homologation wave is already shaping builds: Thunder 3 scooters stay legal while Nami models likely won’t, and riders expect spotty enforcement as police learn the new lists alongside the long-standing 25 km/h cap.【F:data/vesc_help_group/text_slices/input_part012.txt†L21200-L21236】
- Achilleus Limited editions hover around €3,200 compared with roughly €4,300 for a legal Thunder 3, making the Achilleus a popular VESC-ready base thanks to its roomy deck, Thunder arms, and 11″ tire support straight from the factory.【F:data/vesc_help_group/text_slices/input_part012.txt†L21752-L21776】
- Victor Luxury + owners report about 20 S 8 P capacity once controllers move outside the deck, whereas Achilleus builders can tuck electronics into the stem box they plan to fabricate for legality and stealth.【F:data/vesc_help_group/text_slices/input_part012.txt†L21689-L21719】【F:data/vesc_help_group/text_slices/input_part012.txt†L21712-L21719】
- Anything above 4 kW is still classified as a motorcycle in many EU locales, demanding registration, plates, and insurance—even if local police rarely ticket high-power scooters today.【F:data/vesc_help_group/text_slices/input_part012.txt†L21792-L21797】
- Yamal closed the slice by noting how quickly costs escalate—dual VESC builds, high-discharge cells, premium brakes, and spare vehicles all add up—reinforcing why many keep a second scooter ready while the primary project is torn down.【F:data/vesc_help_group/text_slices/input_part012.txt†L21810-L21812】

### Additional Findings (Lines 21,881–21,984)

#### Battery, Electronics, and Packaging Notes
- Rogerio Figueiredo is riding on a stopgap 16 S 6 P Samsung 50E pack while waiting for his main battery and is troubleshooting a dash display that refuses to show correct data, signaling that generic screens still need custom wiring on VESC swaps.【F:data/vesc_help_group/text_slices/input_part012.txt†L21882-L21890】
- Smart Repair keeps a spare 70H motor on hand but warned the conversion isn’t worth the effort compared with jumping straight to an 80H hub fed by multiple ESCs when hunting for big rear-wheel torque.【F:data/vesc_help_group/text_slices/input_part012.txt†L21899-L21906】
- Rob Ver’s stock-motor Vsett 11 proves that a single Ublox 150 A controller paired with a 21 S 51 Ah LG M58T pack and Dragy logging can push factory 60 V/1,500 W hubs into the 120 km/h range, provided you dedicate one side of the deck to battery mass and the other to controller hardware.【F:data/vesc_help_group/text_slices/input_part012.txt†L21931-L21954】
- Matthew is sizing up Lonnyo 80H 33/2 rear hubs for a Yume Y11+ conversion, reinforcing that the frame can house higher-output RWD drivetrains if you manage the thermal budget and phase current demands.【F:data/vesc_help_group/text_slices/input_part012.txt†L21945-L21950】
- Builders confirmed that LY 11″ rims accept 155 mm axles, expanding options for wider slicks on legacy chassis.【F:data/vesc_help_group/text_slices/input_part012.txt†L21970-L21970】
- Begode Q3 owners reiterated that the stock frame leaves minimal battery space, forcing 3D-printed housings (eventually in glass-filled PETG) and even key relocations to clear the handlebars.【F:data/vesc_help_group/text_slices/input_part012.txt†L21978-L21984】

#### Open Questions and Follow-Ups
- Riders asked whether VESC traction control primarily blocks burnouts or can actively stabilize the chassis mid-lean, so follow-up testing should document how slip detection behaves while cornering.【F:data/vesc_help_group/text_slices/input_part012.txt†L21944-L21944】
- Matthew’s controller begins thermal rollback ~10 °C before the configured limits (throttling at 91 °C and shutting down at 95 °C despite a 105 °C threshold), suggesting the need to verify sensor calibration or firmware clamps in future troubleshooting notes.【F:data/vesc_help_group/text_slices/input_part012.txt†L21959-L21972】

### Supplemental Technical Notes (Lines 20,600–21,984)

#### Controller Mounting and Chassis Packaging
- Spintend’s 100/100 controllers thread into tiny M2.5 bosses and ship without hardware, forcing builders to tap their own screws; the 85/240’s flat case also demands countersinking because the housing omits mounting “ears.”【F:data/vesc_help_group/text_slices/input_part012.txt†L21036-L21042】
- Forol1561’s dual-motor deck walkthrough highlighted how sliding a 20 S pack beneath one ledge frees the opposite ledge for the BMS, slim chargers, or even VESCs, provided every millimetre is planned.【F:data/vesc_help_group/text_slices/input_part012.txt†L21043-L21046】
- Ausias is relocating an 85/240 into a custom 3D-printed enclosure on the chassis flank because his oversize battery monopolises the deck; 150 mm suspension travel previously smashed heatsinks and even a Kelly controller, so he now keeps electronics higher and protected.【F:data/vesc_help_group/text_slices/input_part012.txt†L21582-L21585】【F:data/vesc_help_group/text_slices/input_part012.txt†L21609-L21616】
- Achilleus conversions stay stealthy by machining an aluminium neck box for the VESC hardware so the roomy deck can remain all-battery—a compromise for riders who dislike exposed controllers but still need legal homologation packages.【F:data/vesc_help_group/text_slices/input_part012.txt†L21712-L21719】【F:data/vesc_help_group/text_slices/input_part012.txt†L21758-L21759】

#### Tires, Rims, and Suspension Details
- Rob Ver’s current street setup pairs an LY 80H motor on a 110 mm outer/100 mm inner rim; he stretches 80 mm tyres across the 100 mm bead and dropped the suspension to widen the contact patch, keeping controller temps around 40 °C with the hardware tucked under the deck.【F:data/vesc_help_group/text_slices/input_part012.txt†L21047-L21052】【F:data/vesc_help_group/text_slices/input_part012.txt†L21430-L21444】
- Lonnyo motors continue to ship with stout wiring—Dualtron Achilleus confirmed the phase leads are roughly 7 AWG with ~8 mm sleeving—supporting the high current figures riders are now chasing.【F:data/vesc_help_group/text_slices/input_part012.txt†L21623-L21628】【F:data/vesc_help_group/text_slices/input_part012.txt†L21726-L21727】
- 🇪🇸AYO#74🏁 reminded tubeless converters that the sealing O-ring sits in a machined rail and usually comes from industrial bearing/seal suppliers, but not every motor shell uses the same profile.【F:data/vesc_help_group/text_slices/input_part012.txt†L21647-L21652】

#### Battery Construction and Thermal Practices
- Rob Ver reiterated that 0.2 mm copper laminations keep his 22 S 9 P Ampace JP40 pack under 30 °C even at 500 A, and he continues to favour the cells for their low sag and strength.【F:data/vesc_help_group/text_slices/input_part012.txt†L21469-L21479】
- The same Vsett 11 build fits both controllers in-deck by fabricating scooter-specific spacers; every pack is finished differently, with some staying Kapton-only until there’s clearance for heat-shrink in the cramped shell.【F:data/vesc_help_group/text_slices/input_part012.txt†L21481-L21489】【F:data/vesc_help_group/text_slices/input_part012.txt†L21564-L21575】
- Rob discourages potting controllers with insulation gel because servicing MOSFETs becomes impossible—he prefers a protective cover and perimeter silicone bead—and he swaps the stock rim hardware for higher-grade fasteners before the first ride.【F:data/vesc_help_group/text_slices/input_part012.txt†L21677-L21679】

#### Lighting, Controls, and Accessories
- Builders relying on turn signals and horns continue to lean on Spintend’s ADC adapter board; sequential LED strips can’t share the blinker channel without extra logic, so some riders rewire lighting looms from scratch to avoid the VESC’s tiny signal wires.【F:data/vesc_help_group/text_slices/input_part012.txt†L21330-L21335】
- Mario-supplied Dualtron motors arrive with only two conductors powering the decorative LEDs, meaning installers must adapt the three-wire factory connectors if they want the lighting to behave like stock trim.【F:data/vesc_help_group/text_slices/input_part012.txt†L21668-L21671】
