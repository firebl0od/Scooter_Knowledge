# Field Weakening Tuning Playbook

## TL;DR
- Treat field weakening (FW) as a last-mile speed tool: it trades torque and efficiency for extra ERPM, rapidly heating motors and controllers, so only enable it once the drive system runs cool at target duty cycles.[^1][^2][^3]
- Stable implementations rely on firmware 5.3-era builds, instrumented temperature and voltage logging, and conservative regen; high-voltage packs or 24S conversions demand extra surge headroom because regen spikes can brick controllers when FW is active.[^4][^5]
- Start with single-digit or 10–30 A FW setpoints validated by telemetry; riders jumping to 55–60 A routinely saturate hubs within an hour unless they raise phase current carefully, add cooling, and watch logs for current overshoot.[^6][^7]

## How Field Weakening Works
- FW injects negative d-axis current to cancel back-EMF so the motor surpasses its natural base speed, which inherently reduces torque-per-amp and wastes power as heat.[^1]
- Because hub shells lag far behind winding temperature, rely on embedded thermistors or data-derived proxies rather than external probes when judging FW headroom.[^2]
- Bench experiments show ~40 % ERPM gains demanded 100 A phase for only 20 A battery, yet the setup ran hot and inefficient—highlighting why FW is reserved for brief top-speed pulls rather than everyday cruising.[^3]

## Prerequisites & Safeguards
1. **Firmware:** Confirm VESC Tool firmware 5.3 (or newer) on every controller; earlier releases hide FW parameters entirely or crash during detection.[^5]
2. **Voltage Headroom:** Disable regen or add external suppression when testing 24S packs on hardware like the FlipSky 75100—regen spikes plus FW have already killed controllers during BMS cutoffs.[^4]
3. **Instrumentation:** Log motor temps, phase/battery currents, and duty cycle. Shell temps or single shunts under-report FW stress, and FW can even lift battery draw above configured limits until you rerun detection.[^2][^8]
4. **Mechanical Readiness:** Inspect frames, bearings, and tires before extending top speed. Dual 84100 Zero 10X builds at 60 A FW need ongoing frame checks to catch stem or hub fatigue.[^6]
5. **Thermal Margin:** If motors already approach their thermal ceiling, raise pack voltage or change windings instead—FW on commuter hubs like Xiaomi’s 250 W core has cooked stators even at moderate voltage.[^6][^9]

## Configuration Workflow
1. **Baseline Tune:** Run standard motor detection, confirm smooth sensorless transitions, and road-test without FW to verify the observer and throttle feel.[^7][^10]
2. **Enable FW Incrementally:** Increase `Field Weakening Current` in 5–10 A steps. Dual 84100 setups typically settle near 15–30 A per controller for 100 km/h GPS runs, while heavier 72 V builds may stretch toward 40–55 A once cooling and battery delivery are proven.[^7][^11][^12]
3. **Re-verify Current Limits:** After each change, check live logs for battery spikes above set limits and rerun detection if overshoot appears—the VESC Tool wizard reset resolved a 60 A ceiling breach on one build.[^8]
4. **Test Regen:** Perform controlled braking drills to confirm bus voltage stays within component ratings; Spintend riders retain regen at 80–100 km/h with FW but now log every pass to ensure bus voltage never exceeds controller limits before trusting high-speed braking.[^13][^24]
5. **Fault Review:** After hard pulls, run the `faults` command and inspect absolute current headroom (200–250 A for 120–130 A phase tunes) to avoid ABS cut-outs at high duty cycle.[^14]
6. **Duty Cycle Discipline:** Keep maximum duty near firmware defaults (~95 %); stretching toward 99–100 % has produced abrupt cut-outs above 70 km/h on FW-enabled builds.[^15]

## Operating Benchmarks
| Platform | Pack & Motor | Phase / Battery | FW Current | Notes |
| --- | --- | --- | --- | --- |
| Zero 10X dual 84100 | 20 S LY hubs | 120 A phase / 55 A battery each | 30 A | BEMF decoupling + `mxlemming` observer hit 100 km/h without overheating; 60 A FW overheated motors within an hour.[^6][^7]
| Segway GT2 dual Spintend 85150 | 19 S9 P EVE 50E | 150 A phase / 60 A battery each | 30 A | Cells are bottleneck; plan for stronger pack before raising FW.[^10]
| Wolf King GT Pro dual Ubox 150 | 72 V pack, 50 A windings | 210 A phase / 50 A battery each | 55 A | Freewheels ≈77 mph, road ≈66 mph; requires reinforced deck and custom firmware.[^11]
| Halo 60 V stunt hub | 60 V single hub | 350 A phase | 125 A | Airborne testing caused runaway RPM—cap FW drastically when wheels can unload.[^12]
| Vsett high-speed build | 22 S 22×3 hubs | 80 A FW | 200 A battery split | Needs aggressive cooling; FW masks intermittent cut-outs from mechanical issues.[^12][^16]
| Commuter Xiaomi/Ninebot hubs | 13–20 S small stators | ≤40 A phase typical | Avoid FW | Stock hubs overheat or fail even with 4 A FW—prioritize motor upgrades instead.[^9][^17]
| NAMI hotdog (100 H rear / 70 H front) | 22 S 11 P P45 pack | 500 A phase / 550 A absolute | 100 % front FW to sync speeds | Traction control mandatory—rear lifts the front even at 120 km/h while stators stay ~61 °C during 40 kW pulls.[^hotdog_fw]

## Risk Controls & Telemetry
- **Thermal Watch:** Riders pushing 16 S commuter packs noted 150 °C stators at only 35 A FW, reinforcing that ferrofluid or temperature probes are mandatory if you insist on FW in enclosed hubs.[^18]
- **Voltage Monitoring:** Keep oscilloscope or high-speed logging on regen-heavy tests—22 S Spintend builds disable regen entirely when extending pack voltage to avoid BMS-induced surges.[^19]
- **Fault Masking:** Sudden current drops or pothole-induced cut-outs that disappear when FW is enabled can signal mechanical faults (loose magnets, wiring) rather than firmware bugs; investigate hardware first.[^16]
- **Noise & Surging:** If throttle jitters appear above 80 % duty after enabling 20 A FW on single-motor builds, roll FW back—operators traced the behavior directly to FW injection.[^20]
- **Overspeed Discipline:** Avoid free-spinning wheels at high FW. Halo stunt crews saw runaway RPM off-load and controller stress at 125 A FW.[^12]
- **Front-lift control:** Hotdog 100 H rear builds demand traction control or front FW assistance; otherwise the rear lifts the front well past 120 km/h even while stators only hit ~61 °C, so validate TC before public-road tests.[^hotdog_fw]
- **Respect hardware cooling.** Standard 6×TO-220 Makerbase 75100 boards have already burned MOSFETs when pushed to 35 A FW with 130 A phase on air cooling—cap FW nearer 20 A unless you upgrade to the aluminum-PCB/vented versions or add serious heatsinking.【F:knowledge/notes/input_part005_review.md†L206-L208】

## Decision Guide: Voltage vs. Field Weakening
- **Choose Higher Voltage / Different Windings When:** You need sustained highway speed, the motor already runs hot without FW, or you’re targeting >120 km/h—builders hitting 118 km/h on 22×3 hubs without FW prove gearing changes scale better than stacking FW amps.[^11][^21]
- **Use Field Weakening When:** The pack and controller have proven thermal headroom, the chassis can handle added speed, and you only need short bursts to overtake or extend top speed marginally (≈5–15 km/h gains). Riders logging 85 km/h on 20 S singles with 30 A FW treat it as a momentary boost, not a permanent setting.[^11][^22]
- **Never Use FW When:** Working on small commuter hubs or unfinished builds lacking thermistor feedback—multiple riders fried stock motors at single-digit FW currents and now avoid the feature entirely.[^9][^17]

## Troubleshooting Checklist
- **Battery Current Overshoot:** Rerun detection/wizard, verify sensor calibration, and ensure battery limits exceed expected FW-induced draw.[^8]
- **ABS Overcurrent Trips:** Increase absolute current headroom, inspect phase connectors, and confirm observer stability before adding more FW.[^14]
- **Uncommanded Brake or Cut-Outs:** Review handbrake/UART mappings and wiring; FW magnifies regen spikes that can trip miswired systems.[^4][^23]
- **Persistent Motor Heating:** Back FW down 5–10 A, improve heat sinking (direct-to-deck mounts, fresh thermal paste), or reduce phase amps before the stator saturates.[^6][^11][^18]

## Source Notes
[^1]: Field-weakening theory and trade-offs between torque, efficiency, and heat.【F:knowledge/notes/input_part006_review.md†L408-L423】
[^2]: Hub shell temperature lag and the need for embedded sensing.【F:knowledge/notes/input_part006_review.md†L423-L436】
[^3]: Bench data showing ~40 % ERPM gains with major heat penalties.【F:knowledge/notes/input_part000_review.md†L726-L726】【F:knowledge/notes/input_part000_review.md†L654-L654】
[^4]: 24S Flipsky failures tied to regen spikes with FW active.【F:knowledge/notes/input_part001_review.md†L111-L112】
[^5]: Firmware 5.3 requirement for exposing FW controls.【F:knowledge/notes/input_part001_review.md†L135-L135】
[^6]: 60 A FW on dual 84100 builds driving high heat and frame inspection needs.【F:knowledge/notes/input_part009_review.md†L43-L43】
[^7]: PuneDir’s stable 30 A FW baseline with `mxlemming` observer and 100 km/h GPS results.【F:knowledge/notes/input_part009_review.md†L44-L44】【F:knowledge/notes/input_part009_review.md†L179-L179】
[^8]: FW letting battery current exceed configured limits until detection reruns.【F:knowledge/notes/input_part009_review.md†L117-L117】
[^9]: Xiaomi hub failure from modest FW and voltage experiments.【F:knowledge/notes/input_part009_review.md†L93-L93】
[^10]: Segway GT2 dual 85150 telemetry at 30 A FW highlighting pack limits.【F:knowledge/notes/input_part010_review.md†L293-L293】
[^11]: Wolf King GT Pro and similar high-power builds using 55 A FW for ~66 mph road speeds.【F:knowledge/notes/input_part013_review.md†L65-L65】【F:knowledge/notes/input_part013_review.md†L599-L599】
[^12]: Halo runaway RPM and general caution for unloaded FW testing.【F:knowledge/notes/input_part012_review.md†L28-L28】
[^13]: High-speed regen viability with FW and the need to log bus voltage.【F:knowledge/notes/input_part005_review.md†L463-L465】
[^14]: Using the `faults` command and absolute current headroom to manage FW-induced spikes.【F:knowledge/notes/input_part001_review.md†L139-L139】
[^15]: Duty-cycle ceiling warnings for FW-enabled builds.【F:knowledge/notes/input_part001_review.md†L160-L160】
[^16]: FW masking mechanical faults in high-speed Vsett builds and needing inspections.【F:knowledge/notes/input_part013_review.md†L741-L741】
[^17]: Haku’s decision to abandon FW after killing commuter hubs at 4 A.【F:knowledge/notes/input_part011_review.md†L301-L301】
[^18]: Max G2 and similar commuter hubs hitting 150 °C stators with FW.【F:knowledge/notes/input_part005_review.md†L368-L372】
[^19]: 22 S Ubox/Spintend configurations disabling regen to survive higher voltage.【F:knowledge/notes/input_part010_review.md†L419-L419】
[^20]: FW-induced throttle jitter on single-controller builds once 20 A is applied.【F:knowledge/notes/input_part013_review.md†L709-L709】
[^21]: 22×3 hub builds freewheeling around 118 km/h without FW after pack upgrades.【F:knowledge/notes/input_part013_review.md†L88-L88】
[^22]: 20 S single-motor package delivering 85 km/h with ~30 A FW as a short-burst aid.【F:knowledge/notes/input_part013_review.md†L145-L145】
[^23]: Firmware or wiring faults causing sudden full braking after FW-enabled firmware updates.【F:knowledge/notes/input_part001_review.md†L219-L219】
[^24]: Riders now log high-speed (80–100 km/h) FW regen drills to confirm bus voltage stays under Spintend limits before trusting the setup on public roads.【F:knowledge/notes/input_part005_review.md†L608-L608】
[^hotdog_fw]: NAMI 100 H rear / 70 H front builds logging 500 A phase, 550 A absolute, 100 % front FW, and ~61 °C stators while traction control keeps the rear from lifting the front at 120 km/h.【F:knowledge/notes/input_part014_review.md†L8930-L8933】【F:knowledge/notes/input_part014_review.md†L10001-L10055】
