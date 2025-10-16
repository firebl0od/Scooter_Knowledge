# VESC Scooter Motor & Controller Tuning (Part 007 Extracts)

## Hub Motor & Winding Selection

- Default production hubs remain 60H 22/3 windings; Nami's 17/4 stock motors trade top speed for brutal launches just under 100 km/h, while 33/2 rewinds are the crew's choice where circuits reward higher peak speed.[^hub-lineup]
- Mixing dissimilar windings (e.g., 22×3 rear with 33×2 front) reliably causes tuning conflicts thanks to mismatched Kv, so builds should stay symmetrical.[^mixed-windings]
- QS90 inrunners with IPM gearing are attractive for lower hub temps and more torque, but advertised wattage claims still need to be validated against factory specs.[^qs90]
- 65 H 33/2 hubs demand ≥12-fet controllers plus application-specific harnesses.
  - generic 10 AWG silicone overheats inside the axle and stock phases already run hot when paired with big controllers.[^65h-requirements]
- TCP-branded hubs with the latest 70 mm magnet stack still tuck into 11 in rims, so plan packaging around that diameter instead of assuming you need a 12 in shell.[^hub-magnet-stack]
- Rosheee's dyno and road runs showed a single 16 s 6 p M50LT pack with a 60 A BMS outrunning dual 50 H hubs from 0–30 km/h; builders trade some top speed because 65 H stators have lower Kv.[^65h-performance]

## Controller Selection & Limits

- Makerbase's 84100 HP remains the high-value choice versus Spintend: expect ~150 A phase from its six-FET aluminum-PCB stack, solid thermals, and Bluetooth, but no performance leap beyond Spintend.[^84100]
- Makerbase’s 84100 HP ships with a normally closed ignition lead and field logs show it happily holding 200 A phase in free air.
  - rewire the lead for Zero-style harnesses or pair it with an NC key, and treat the replaceable 0 Ω links as sacrificial fuses that protect the logic rails.[^84100-nc]
- Makerbase 75100 V2 units run about €75 delivered versus ~€150 for Spintend 12-fet controllers; Izuna's custom firmware already fixes the aluminum-case voltage readout bug.[^75100-pricing]
- Makerbase 75200 V2 now includes a built-in shutdown input, sparing budget builds from external antisparks.[^75200-shutdown]
- Makerbase engineers are now iterating an 84 V/200 A INA241 board in the open via esk8.news threads.
  - expect layout tweaks and firmware revisions before treating the higher-voltage lineup as production-ready.[^1]
- Fardriver controllers deliver multi-kiloamp capability (up to 2,600 A) and appear on production Weped Sonic builds; VESC hardware is still pricier and more delicate at those power levels.[^fardriver]
  - Benchmark the scooter-sized 450 A units before recommending them—current owners are still asking whether typical hub motors survive those targets and how usable the tuning software feels.[^fardriver-450a]
- Nucular 24F controllers remain scarce, heavy, and four-figure purchases; builders favor the 3Shul C700 as a more practical high-power upgrade path.[^nucular]
- Dual-motor controllers house two linked boards sharing a heatsink, making them viable for dual 500 W Monorim setups so long as each phase channel stays inside spec (Gabe reports 75 km/h sustained without overheating).[^dual-esc]
- Race crews cap competition scooters at 22 s because today's 30 s hardware can't feed equivalent battery amps; 22 s 18 p packs remain the winning compromise.[^race-voltage]
- Spintend 85 V/250 A controllers stay attractive for packaging.
  - they slide under skid pans, keep 20 s battery caps, and let riders redeploy Nucular 24Fs elsewhere, but expect deck spacers or external mounts to clear their height.[^spintend-85250]
- Gabe still sees XESC controllers eke out more top speed than equivalently tuned VESCs on stock Laotie hardware, but 13 S commuters plateau near 35 km/h while 20 S+ tunes demand MP2 packaging tricks to fit the cells.[^xesc-speed]
- Most scooter-focused controllers still rely on low-side shunts; three-phase current sensing only helps extremely low-inductance or high-ERPM machines and will not rescue noisy HFI hubs on its own.[^low-side-shunt]

## Current & Voltage Guardrails

- Keep regen voltage below ~84 V on 80100/84100 hardware when running high-voltage packs—above that the hardware becomes fragile even if throttle operation is fine.[^regen-threshold]
- On Ubox builds, set absolute current only 10–20 % above motor current; explore observer options, reduce observer gain by half, tweak inductance by ~20 %, experiment with PWM frequency, and avoid slow-ABS to stop over-current oscillations without neutering torque.[^abs-oc]
- Phase amps, not motor Kv, create launch torque: Deadword's 75100/Ninebot G30 regained punch only after raising motor current beyond 35 A (within safe hardware limits).[^phase-amps]
- Rochee's testing on Jesús's Rion confirmed that extreme phase amps and field-weakening reintroduce grinding noises and cutouts; backing phase current down keeps 24 s builds reliable.[^phase-ceiling]
- When ride logs show the hub is already saturating, follow Yoann's example and dial current back.
  - hardware changes move the needle more than piling on phase amps once the stator is tapped out.[^saturation-logging]
- Mirono’s CL-series caution still stands: auto-detected regen mirrors drive current, so hand-tune motor/brake amps before hard launches or you will spike hardware.
  - newcomers should expect manual setup or choose simpler controllers.[^2]
- Makerbase 80100 hardware only hits the advertised 250 A phase once you flash no-limit firmware; stock builds plateau around 150–160 A even with ample cooling.[^3]
- NetworkDir is comfortable adding about 15 A of field weakening on healthy dual 75100 Mantis builds for a modest speed bump without overstressing the hardware.[^mantis-fw15]

## Thermal Management & Cooling

- Aim to keep MOSFETs at or below 70 °C (100 °C absolute ceiling); reapply thermal paste when controllers climb too quickly.[^mosfet-limits]
- Track riders warn that deck-mounted fans can't cool sealed controller bays alone.
  - bridge controller heat into the chassis with external heatsinks, dual intake/exhaust airflow, and take cues from Weped's twin 30 Ah 40T packs feeding opposing fans at 145 km/h.[^cooling-bays]
- Jan's thick aluminum "alubox" enclosures run only ~5 °C over ambient, proving the value of mass and conductivity in controller housings.[^alubox]
- Makerbase's bottom-facing heatsink enclosure needs custom mounting and active airflow; expect thermal limits unless you rework the case.[^makerbase-heatsink]
- Skip thermal glue when mounting Makerbase 84100HP controllers.
  - clamp them with paste, sand the ridged base flat if needed, or open the deck so airflow can reach the heatsink just like Ninebot’s stock layout.[^4]
- Leave ventilation paths around deck-mounted controllers.
  - shrink-wrapping a Makerbase baseplate trapped heat until the VESC overheated, while simply leaving bolted airflow restored normal temps.[^5]
- Ferrofluid/Statorade dramatically improves hub cooling by filling the stator-magnet air gap, but confirm flash points and magnet demag thresholds (budget hubs can lose strength above ~80 °C).[^statorade]
- Even acceleration-focused riders on 22/3 winds are capping controller temps around 60 °C and spacing summer pulls.
  - log temps and respect those soft ceilings before asking for more current.[^thermal-60c]

## Wiring, Harnesses & Mechanics

- Upgrade GT2 or Lonnyo hub leads to ~8 mm² cabling, warming thick silicone jackets with low heat before bending so the larger phases seat cleanly.[^gt2-leads]
- Replace corroded XT60s outright; when soldering bullet connectors, heat the connector (not the wire) so solder flows, then slide the molded cover to shield the last ~3 mm before shrinking insulation.[^soldering]
- For hall chattering Monorim builds, re-detect halls, raise the sensored→sensorless handoff to ~3,000 ERPM, and switch observers to Ortega for clean transitions.[^monorim-chatter]
- Stay in hall-sensor mode when pushing high phase current; Mxlemming observers can launch at 150 A on 10 s 5 p packs but saturate sooner than Ortega, so revisit observer and current-coupling parameters when saturation appears.[^hall-mode]
- Investigate hall sensor "absent" errors by checking the thin hall leads and verifying continuity with a multimeter's beep mode before rerunning setup.[^hall-diagnostics]
- Once the motor profile is dialled, rerun hall detection without repeating full motor detection to validate repairs quickly—AYO#74 treats it as a post-service sanity check.[^hall-redetect]
- Wheelway 1 000 W hubs that chatter above ~70 A phase usually clear up after rerunning detection with higher phase-current limits, raising the power-loss estimate toward 1 kW, shortening phase leads, or ultimately stepping to LY 60H 22/3 motors for more torque headroom.[^wheelway-fix]
- Before re-energizing suspect controllers, beep-test between pack leads and every phase to catch shorts, confirm 5 V accessory output, isolate hall supplies with dual 1N4148 diodes if needed, and inspect resettable fuses guarding the Ubox's 12 V/5 V/3.3 V rails.[^prepower-checks]
- Cold-soldered phase leads can melt and short, killing FETs; test each MOSFET drain-to-source, inspect both sides of the board, and verify Bluetooth plus the 5 V rail before reconnecting.[^phase-meltdown]
- Zero owners mounting paired VESCs should enlarge bolt holes gradually, strip paint to use the chassis as a heat bridge, clamp with hardware and threadlocker, refresh thermal pads with paste, and avoid insulating foam stuffing.[^zero-mounting]
- Mixing Makerbase 75100s with FlipSky 75100s on a shared CAN bus pops transceivers thanks to mismatched termination.
  - stick to homogeneous pairs or rework resistor networks before linking them.[^6]
- Use mechanical fasteners rather than brazing when bonding heatsinks to frames; aluminum brazing demands specialty flux, risks galvanic corrosion, and is best reserved as a last resort.[^brazing]
- When designing external heatsinks, drop the sink through the deck, drill and tap for anchors, and bolt the controller directly with paste so airflow can reach the fins.[^external-heatsink]
- Older Lonnyo hubs only leave 7–8 mm of axle clearance.
  - plan to strip factory leads, thread thicker phase cables, and add extra sleeving between conductors so the bundle sheds heat instead of cooking insulation.[^lonnyo-clearance]

## Battery & BMS Interactions

- Regen failures on Zero ESCs traced to leaving JK smart-BMS charge FETs disabled; confirm both charge and discharge paths before high-voltage tests.[^bms-charge]
- JK's optional cellular tracker module is bulky enough that owners plan to tuck it inside pack shrink or add wireless charging to avoid constant disassembly.[^jk-tracker]
- PuneDir's mixed Zero pack (20 s 7 p internal + 20 s 4 p booster) chews capacity fast under high phase current; peers advise moving each controller toward 100 A battery current and upgrading to 60–65 H motors before chasing more torque.[^mixed-pack]
- Ferrotec APG1110 remains the ferrofluid benchmark, but Supermagnete's 10 mL bottles are proven EU-friendly sources for Xiaomi and G30 hubs.[^ferrofluid-sourcing]

## Instrumentation & Controls

- Yoann's dual Spintend 85 V/250 A Nami conversion highlighted weak launch torque, clunking under load, GNSS vs. VESC speed gaps (~30 km/h) even with wheel diameter entered, and noisy Spiny 2 throttle voltage (likely from routing beside phase leads).
  - log everything during shakedowns.[^nami-conversion]
- Spin Y throttles work on Spintend and Ubox setups: Version 1 needs custom JST-1.0 leads into ADC2/COMM2, while Version 2 simplifies wiring with a four-conductor harness.[^spiny]
- NetworkDir and PuneDir are building an open-source VESC display with profile switching and GitHub-hosted code, plus mounts for 22 mm bars to ease commuter adoption.[^open-display]
- Vsett display retermination: drill a tiny hole, lever the ultrasonically welded shell apart, resolder or reroute the six-wire harness (mind RX/TX orientation), reseal with quality two-part adhesive, and reapply the throttle sticker with warm air.[^vsett-display]
- `lekrsu` warns that leaving Xiaomi/Laotie builds on wizard defaults makes them feel sluggish; enable his “rocket fuel” tune, tighten acceleration ramp time, and be ready to dial ramping back if wheelspin returns.[^rocket-fuel]
  - Traction-control riders now drop positive ramp delay to effectively zero so launch response stays sharp without masking slip elsewhere in the tune.[^ramp-zero]
- Incline readouts need an IMU; Ubox includes a gyroscope so it self-levels on boot, whereas bare VESCs without IMUs cannot show accurate slope.[^imu]
- Capture VESC Tool logs whenever behaviour feels odd—the TCP hub issue Yoann spotted only has a root-cause plan because he committed to record full logs for the group.[^vesc-logging]
- Swap the 01C (10 kΩ) temp-sense resistor into recent Makerbase 75100 V2 runs so motor telemetry stops reporting bogus numbers before thermal limits bite.[^75100-tempfix]
- Enable Spintend traction control directly in VESC Tool’s ADC tab (local controller only), log the slip behaviour, and remember the NRF header hosts the Bluetooth module while ADC1 carries the throttle signal.[^tc-adc]
- If sensorless scooters still stutter off the line, expect to kick-start them—sensorless control cannot hold from zero speed without hall sensors.[^sensorless-kick]
- SmartESC firmware on Xiaomi Pro controllers only mimics the VESC Tool UI—the ST-based boards still lack full VESC feature depth, so temper open-tuning expectations.[^smartesc-warning]
- Before blaming firmware for traction hiccups, inspect fork and neck harnesses for pinched wires at full steering lock; damaged leads often mimic controller faults.[^fork-harness]
- Negative throttle ramping keeps torque on after you release the lever; switch back to the natural curve to kill the dead zone without upsetting launches.[^negative-ramp]
- Regen throttles mapped to “current no reverse” on ADC2 should be calibrated with 30 pole pairs and GPS cross-checks so dash speed stays honest while tuning braking torque.[^regen-dash]
- Centered-throttle KERS setups go smoother when you calibrate ADCs with the wheel in the air, leave the config page open while sweeping the lever, and then stage negative battery/motor currents so regen ramps in without overloading the pack.[^kers-setup]
- VESC Tool’s state-of-charge gauge simply interpolates between 4.2 V and 3.3 V per cell (≈66 V on 20 S), so raise controller cutoffs a touch above the BMS limit to avoid surprise throttling when the dash calls the pack “empty.”[^7]

## Safety & Fault Recovery

- Temper regen/battery limits on Makerbase 75100 V2 controllers when stretching to 100 V packs—Rogerio destroyed one by braking a 22 s build at ~5 km/h.[^regen-75100]
- Remember to disable the VESC Tool hand test after verifying throttle/brake mapping; leaving it armed blocks normal control inputs on the next power cycle.[^hand-test]
- Burnout-induced controller deaths get a full autopsy now: beep between pack and phases to confirm no hard short, check that the motor spins freely, and expect multiple shorted FETs on the aluminium power board.[^burnout-autopsy]
- Avoid opening controllers while short-circuit protection is active and never mix MOSFETs across 6-fet and 12-fet Spintend boards; if you must ride while repairs are pending, detune to smaller controllers and lean on mechanical brakes instead of regen-only stops.[^burnout-repair]
- Keep spare STM32 MCUs on hand for aging FlipSky 75100s.
  - Asyan4ik lost a logic chip without warning yet had the controller running again within an hour after swapping the $30 part.[^8]

## Track & Chassis Notes

- Dual intake/exhaust fans alone can't stabilize controller bays; integrate external heatsinks and tie them thermally into the chassis.[^cooling-bays]
- Yamal confirmed Nami will sell rolling chassis (~€1,200) with motors (~€800) but stock swingarms only fit up to 70H hubs, so 75H/90H conversions need arm spreading and mount rework.[^nami-chassis]
- PuneDir sourced a €250 donor chassis with suspension but peers warned the frame looked weak—inspect bargain frames thoroughly before pairing them with high-torque drivetrains.[^donor-frame]
- Purpose-built tubeless rims (e.g., RFP customs) and Amass 8 mm bullets are recommended after racers lost a tire mid-ride; match connectors to thicker phase leads.[^tubeless]
- Adjust Vsett 11 fork tube height to increase steering angle and calm high-speed braking oscillations without resorting to dampers.[^vsett-fork]
- Dual-disc brakes on Zero/Vsett/Teverun/Kaabo typically keep both rotors on the left; swapping sides needs adapters and usually only works with budget calipers.
  - premium Magura/Hope sets stay left-mounted.[^dual-disc]
- Track crews still avoid monoarm forks on high-power scooters despite motorcycle examples—dual legs remain the safer choice when stability is the priority.[^monofork]
- Miniwalker’s race win underscored how lighter packs help on technical circuits; big batteries reduce sag but add enough mass to slow lap times when rider skill is equal.[^light-pack]
- Even die-hard drag builders concede most race scooters use chain drives today—treat belt-drive concepts as experimental until they prove durability.[^chain-drive]
- 🇪🇸AYO#74 trims traction-control strength toward 80 % and raises the activation band to ~4 000 ERPM after the front spun past 135 km/h on his 33×2/70 H build; expect to revisit slip targets once steering-cam sensors return.[^tc-highspeed]

---
[^hub-lineup]: knowledge/notes/input_part007_review.md lines 12-16.
[^mixed-windings]: knowledge/notes/input_part007_review.md lines 44-45.
[^qs90]: knowledge/notes/input_part007_review.md lines 46-47.
[^65h-requirements]: knowledge/notes/input_part007_review.md lines 38-39.
[^65h-performance]: knowledge/notes/input_part007_review.md lines 65-65.
[^84100]: knowledge/notes/input_part007_review.md lines 15-15.
[^84100-nc]: knowledge/notes/input_part007_review.md lines 201-202.
[^75100-pricing]: knowledge/notes/input_part007_review.md lines 23-23.
[^75200-shutdown]: knowledge/notes/input_part007_review.md lines 25-25.
[^fardriver]: knowledge/notes/input_part007_review.md lines 40-40.
[^fardriver-450a]: Source: knowledge/notes/input_part010_review.md†L706-L706
[^nucular]: knowledge/notes/input_part007_review.md lines 34-34.
[^dual-esc]: knowledge/notes/input_part007_review.md lines 35-35.
[^race-voltage]: knowledge/notes/input_part007_review.md lines 36-36.
[^regen-threshold]: knowledge/notes/input_part007_review.md lines 14-14.
[^abs-oc]: knowledge/notes/input_part007_review.md lines 19-19.
[^phase-amps]: knowledge/notes/input_part007_review.md lines 70-70.
[^phase-ceiling]: knowledge/notes/input_part007_review.md lines 71-71.
[^mosfet-limits]: knowledge/notes/input_part007_review.md lines 45-45.
[^cooling-bays]: knowledge/notes/input_part007_review.md lines 26-26.
[^alubox]: knowledge/notes/input_part007_review.md lines 46-46.
[^makerbase-heatsink]: knowledge/notes/input_part007_review.md lines 37-37.
[^statorade]: knowledge/notes/input_part007_review.md lines 64-64.
[^gt2-leads]: knowledge/notes/input_part007_review.md lines 22-22.
[^soldering]: knowledge/notes/input_part007_review.md lines 100-100.
[^monorim-chatter]: knowledge/notes/input_part007_review.md lines 17-17.
[^hall-mode]: knowledge/notes/input_part007_review.md lines 18-18.
[^hall-diagnostics]: knowledge/notes/input_part007_review.md lines 20-20.
[^hall-redetect]: knowledge/notes/input_part010_review.md†L428-L428
[^low-side-shunt]: knowledge/notes/input_part010_review.md†L633-L633
[^wheelway-fix]: knowledge/notes/input_part010_review.md†L634-L634
[^mantis-fw15]: knowledge/notes/input_part010_review.md†L657-L659
[^smartesc-warning]: knowledge/notes/input_part010_review.md†L658-L659
[^prepower-checks]: knowledge/notes/input_part007_review.md lines 32-32.
[^phase-meltdown]: knowledge/notes/input_part007_review.md lines 31-31.
[^zero-mounting]: knowledge/notes/input_part007_review.md lines 28-28.
[^brazing]: knowledge/notes/input_part007_review.md lines 94-94.
[^external-heatsink]: knowledge/notes/input_part007_review.md lines 99-99.
[^bms-charge]: knowledge/notes/input_part007_review.md lines 27-27.
[^jk-tracker]: knowledge/notes/input_part007_review.md lines 74-74.
[^mixed-pack]: knowledge/notes/input_part007_review.md lines 75-75.
[^ferrofluid-sourcing]: knowledge/notes/input_part007_review.md lines 76-76.
[^nami-conversion]: knowledge/notes/input_part007_review.md lines 21-21.
[^spiny]: knowledge/notes/input_part007_review.md lines 63-63.
[^open-display]: knowledge/notes/input_part007_review.md lines 96-96.
[^vsett-display]: knowledge/notes/input_part007_review.md lines 93-93.
[^rocket-fuel]: knowledge/notes/input_part010_review.md†L426-L427
[^ramp-zero]: Source: knowledge/notes/input_part010_review.md†L535-L536
[^imu]: knowledge/notes/input_part007_review.md lines 30-30.
[^regen-75100]: knowledge/notes/input_part007_review.md lines 13-13.
[^hand-test]: knowledge/notes/input_part010_review.md†L429-L429
[^nami-chassis]: knowledge/notes/input_part007_review.md lines 88-88.
[^donor-frame]: knowledge/notes/input_part007_review.md lines 89-89.
[^tubeless]: knowledge/notes/input_part007_review.md lines 90-90, 166-166.
[^hub-magnet-stack]: knowledge/notes/input_part007_review.md lines 105-105.
[^spintend-85250]: knowledge/notes/input_part007_review.md lines 139-140.
[^saturation-logging]: knowledge/notes/input_part007_review.md lines 104-104.
[^thermal-60c]: knowledge/notes/input_part007_review.md lines 123-123.
[^lonnyo-clearance]: knowledge/notes/input_part007_review.md lines 122-126.
[^vesc-logging]: knowledge/notes/input_part007_review.md lines 103-103.
[^75100-tempfix]: knowledge/notes/input_part007_review.md line 233.
[^tc-adc]: Source: knowledge/notes/input_part010_review.md L539-L539
[^sensorless-kick]: Source: knowledge/notes/input_part010_review.md L540-L540
[^fork-harness]: Source: knowledge/notes/input_part010_review.md L538-L538
[^negative-ramp]: knowledge/notes/input_part007_review.md line 264.
[^regen-dash]: knowledge/notes/input_part007_review.md line 273.
[^kers-setup]: knowledge/notes/input_part007_review.md line 274.
[^monofork]: knowledge/notes/input_part007_review.md lines 116-116.
[^light-pack]: knowledge/notes/input_part007_review.md lines 161-161.
[^chain-drive]: knowledge/notes/input_part007_review.md lines 168-168.
[^tc-highspeed]: knowledge/notes/input_part010_review.md†L461-L463
[^vsett-fork]: knowledge/notes/input_part007_review.md lines 84-84.
[^dual-disc]: knowledge/notes/input_part007_review.md lines 85-85.
[^burnout-autopsy]: Source: knowledge/notes/input_part010_review.md†L526-L528
[^burnout-repair]: Source: knowledge/notes/input_part010_review.md†L527-L528


## References

[^1]: Source: knowledge/notes/input_part007_review.md†L360-L362
[^2]: Source: knowledge/notes/input_part007_review.md†L383-L386
[^3]: Source: knowledge/notes/input_part007_review.md†L387-L388
[^4]: Source: knowledge/notes/input_part007_review.md†L312-L316
[^5]: Source: knowledge/notes/input_part007_review.md†L376-L379
[^6]: Source: knowledge/notes/input_part007_review.md†L369-L375
[^7]: Source: knowledge/notes/input_part007_review.md†L379-L383
[^8]: Source: knowledge/notes/input_part007_review.md†L362-L365

[^xesc-speed]: knowledge/notes/input_part010_review.md†L616-L616
