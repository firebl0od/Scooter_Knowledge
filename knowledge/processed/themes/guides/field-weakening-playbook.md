# Field Weakening Tuning

## Overview

Field weakening (FW) is an advanced tuning technique that allows motors to exceed their base speed by injecting negative d-axis current to counter back-EMF. While it can provide 10-15% speed gains, FW significantly increases heat generation and reduces efficiency. This guide covers when to use field weakening, how to configure it safely, and why it's often better to increase voltage instead. Proper FW tuning requires careful monitoring and conservative limits.

## What You'll Learn

- How field weakening works and its trade-offs
- When FW is appropriate vs. other speed upgrades
- Safe configuration procedures and current limits
- Thermal management requirements
- VESC firmware version compatibility
- Monitoring and logging during FW operation
- Common mistakes and failure modes
- Duty cycle vs. throttle position triggering

## ⚡ What is Field Weakening?

Field weakening (FW) trades efficiency for top speed by weakening the magnetic field, allowing higher RPM. Think of it as "overdriving" your motor.

## ⚠️ Critical FW Warnings

🔴 **Efficiency Loss**: Expect ~25% higher power consumption during FW operation
🔴 **Heat Generation**: Both motor and controller run hotter
🔴 **Current Spikes**: Can push controllers beyond safe limits
🔴 **MOSFET Stress**: >40A FW on budget controllers kills MOSFETs

## 📋 Quick Reference: FW Current Limits by Controller

| Controller Class | Safe FW Current | Absolute Max FW | Notes |
|------------------|----------------|-----------------|-------|
| Budget (Flipsky, Makerbase) | 20-30A | 40A | Above 40A kills boards |
| Mid-range (Spintend) | 30-40A | 60A | Needs MOSFET upgrade for >40A |
| Premium (3Shul, Tronic) | 40-60A | 80A+ | Still needs cooling |

💡 **Pro Tip**: Start with 20A FW current and work up based on thermal testing. Monitor controller temps closely.

## 🔧 Related Guides

- [Motor Configuration](motor_configuration.md) - Understanding motor Kv and winding
- [Motor Controller Tuning](motor_controller_tuning.md) - Controller pairing
- [Battery Current Tuning](battery_current_tuning.md) - Total current budget planning

## Key Principles

- Treat field weakening (FW) as a last-mile speed tool: it trades torque and efficiency for extra ERPM, rapidly heating motors and controllers, so only enable it once the drive system runs cool at target duty cycles.[^1][^2][^3]
- Expect diminishing returns on commuter voltages.
  - 16 S Vsett logs only gained ~8 km/h when adding 30 A per motor (69→76 km/h) while pack draw doubled, so higher series count remains the cleaner path to top speed.[^1]
- New tuners are better off raising voltage or revisiting gearing.
  - Telegram veterans keep hammering that hub-motor limits make FW a bad shortcut when you can solve speed with hardware instead of dumping more heat into the drivetrain.[^2]
- Plan a post-beta checklist once VESC Tool 5.3 lands stable—capture enablement steps, duty triggers, and current ceilings before telling builders to chase the extra ~8 km/h.[^fw53_rollout]
- Stable implementations rely on firmware 5.3-era builds, instrumented temperature and voltage logging, and conservative regen; high-voltage packs or 24S conversions demand extra surge headroom because regen spikes can brick controllers when FW is active.[^4][^5]
- Start with single-digit or 10–30 A FW setpoints validated by telemetry; riders jumping to 55–60 A routinely saturate hubs within an hour unless they raise phase current carefully, add cooling, and watch logs for current overshoot.[^6][^7]
- Most builds arm FW against duty cycle.
  - not throttle position
  - so expect the controller to inject current around 90 % duty and yank roughly the same extra 20 A from the battery while it fights back-EMF; reserve those bursts for cool motors only.[^3]
- Face de Pin Sucé’s test bench confirmed 100 A of FW current at a 90 % duty trigger can spin a hub from 38 kERPM to 53 kERPM (~40 % more rpm) but still drags ~20 A battery while dumping heat.
  - treat it as a short sprint tool on cool motors rather than a cruising aid.[^4]
- European race organisers now cap packs at 22 S (≈35 kW nominal), so teams chase torque with stator area, FW amps, and lighter chassis while daily commuters still hover around 2.4 kW until higher-current 20 S batteries arrive.[^5]

## How Field Weakening Works

- FW injects negative d-axis current to cancel back-EMF so the motor surpasses its natural base speed, which inherently reduces torque-per-amp and wastes power as heat.[^1]
- Because hub shells lag far behind winding temperature, rely on embedded thermistors or data-derived proxies rather than external probes when judging FW headroom.[^2]
- Bench experiments show ~40 % ERPM gains demanded 100 A phase for only 20 A battery, yet the setup ran hot and inefficient.
  - highlighting why FW is reserved for brief top-speed pulls rather than everyday cruising.[^3]
- Third-party firmware like XESC’s can quietly add extra battery amps when you request FW, but stock VESC obeys the configured current limits and simply shifts the stator angle.
  - don’t expect the same “free” boost unless you raise the limits yourself.[^xesc_fw]

## Prerequisites & Safeguards

1. **Firmware:** Confirm VESC Tool firmware 5.3 (or newer) on every controller; VESC Tool 3.01 only exposes FW sliders once controllers run 5.03, and Spintend is still steering riders toward 5.2 binaries until its customised 5.3 builds soak.[^fw-503]
2. **Voltage Headroom:** Disable regen or add external suppression when testing 24S packs on hardware like the FlipSky 75100.
  - regen spikes plus FW have already killed controllers during BMS cutoffs.[^4]
3. **Instrumentation:** Log motor temps, phase/battery currents, and duty cycle. Shell temps or single shunts under-report FW stress, and FW can even lift battery draw above configured limits until you rerun detection.[^2][^8]
4. **Mechanical Readiness:** Inspect frames, bearings, and tires before extending top speed. Dual 84100 Zero 10X builds at 60 A FW need ongoing frame checks to catch stem or hub fatigue.[^6]
5. **Thermal Margin:** If motors already approach their thermal ceiling, raise pack voltage or change windings instead.
  - FW on commuter hubs like Xiaomi’s 250 W core has cooked stators even at moderate voltage.[^6][^9]

## Configuration Workflow

1. **Baseline Tune:** Run standard motor detection, confirm smooth sensorless transitions, and road-test without FW to verify the observer and throttle feel.[^7][^10]
2. **Enable FW Incrementally:** Increase `Field Weakening Current` in 5–10 A steps. Dual 84100 setups typically settle near 15–30 A per controller for 100 km/h GPS runs, while heavier 72 V builds may stretch toward 40–55 A once cooling and battery delivery are proven.[^7][^11][^12]
   - Rosheee staggers activation—rear FW at 87.5–89.5 % duty, front at 93 % with a 97 % max—and adds ~25 % to the ADC throttle curve so both controllers avoid simultaneous current spikes.[^rosheee_fw]
   - If current telemetry looks wrong after MOSFET work, inspect for lifted source legs or shunts before blaming firmware; Yoann’s mis-soldered leg mimicked sensor faults until it was reflowed.[^84]
3. **Pair with quicker ramps judiciously.** Dropping acceleration ramping to 0.05 s sharpens launches alongside FW, but only apply it if the chassis and rider can tolerate the snappier response without spinning tires.[^6]
4. **Re-verify Current Limits:** After each change, check live logs for battery spikes above set limits and rerun detection if overshoot appears.
  - the VESC Tool wizard reset resolved a 60 A ceiling breach on one build.[^8]
5. **Test Regen:** Perform controlled braking drills to confirm bus voltage stays within component ratings; log against Spintend’s ≈100 V ceiling so 80–100 km/h stops with FW don’t spike the DC link beyond the hardware limit.[^13]
6. **Fault Review:** After hard pulls, run the `faults` command and inspect absolute current headroom (200–250 A for 120–130 A phase tunes) to avoid ABS cut-outs at high duty cycle.[^fw-faults]
7. **Duty Cycle Discipline:** Keep maximum duty near firmware defaults (~95 %); stretching toward 99–100 % has produced abrupt cut-outs above 70 km/h on FW-enabled builds.[^fw-duty]
   - Commuter builds that never hit 80 % duty can lower the FW trigger and tweak Lisp caps so FW still engages; `lekrsu` even enables VSS speed estimation on sensorless Flipsky 75200 M365s because VESC already leverages back-EMF once the wheel clears ~5 km/h.[^85]
8. **Duty-trigger experiments:** Genuine FW sliders stay locked behind firmware 5.3, so early adopters sideload 300 A bins and set duty-cycle triggers around 70 % to push past the 95–98 % plateau.
  - treat those settings as advanced-only until thermals and voltage headroom are proven.[^7]
5. **Test Regen:** Perform controlled braking drills to confirm bus voltage stays within component ratings; Spintend riders retain regen at 80–100 km/h with FW but still watch bus voltage for surprises.[^13]
6. **Fault Review:** After hard pulls, run the `faults` command and inspect absolute current headroom (200–250 A for 120–130 A phase tunes) to avoid ABS cut-outs at high duty cycle.[^14]
7. **Duty Cycle Discipline:** Keep maximum duty near firmware defaults (~95 %); stretching toward 99–100 % has produced abrupt cut-outs above 70 km/h on FW-enabled builds.[^15]

## Operating Benchmarks

| Platform | Pack & Motor | Phase / Battery | FW Current | Notes |
| --- | --- | --- | --- | --- |
| Zero 10X dual 84100 | 20 S LY hubs | 120 A phase / 55 A battery each | 30 A | BEMF decoupling + `mxlemming` observer hit 100 km/h without overheating; pushing to 60 A battery and 40 A FW dropped 0–50 km/h to ~2.8 s but risked cooking 50 H hubs in summer heat.[^6][^7][^zero-fw]
| Segway GT2 dual Spintend 85150 | 19 S9 P EVE 50E | 150 A phase / 60 A battery each | 30 A | Cells are bottleneck; plan for stronger pack before raising FW.[^10]
| Wolf King GT Pro dual Ubox 150 | 72 V pack, 50 A windings | 210 A phase / 50 A battery each | 55 A | Freewheels ≈77 mph, road ≈66 mph; Rosheee gained ~20 km/h at 50–55 A FW but warned 16 S builds taper once phase amps roll off near top speed.
  - reinforce the deck before chasing the gains.[^11][^wolf_fw_return]
| Halo 60 V stunt hub | 60 V single hub | 350 A phase | 125 A | Airborne testing caused runaway RPM—cap FW drastically when wheels can unload.[^12]
| Vsett high-speed build | 22 S 22×3 hubs | 80 A FW | 200 A battery split | Needs aggressive cooling; FW masks intermittent cut-outs from mechanical issues.
  - 16 S Monorim/Vsett commuters cap duty near 96–99 % with FW limited to ≈30 A per motor to keep ABS happy while still chasing 100 km/h.[^8][^12][^16]
| Commuter Xiaomi/Ninebot hubs | 13–20 S small stators | ≤40 A phase typical | Avoid FW | Stock hubs overheat or fail even with 4 A FW—prioritize motor upgrades instead.[^9][^17]
| NAMI hotdog (100 H rear / 70 H front) | 22 S 11 P P45 pack | 500 A phase / 550 A absolute | 100 % front FW to sync speeds | Traction control mandatory.
  - rear lifts the front even at 120 km/h while stators stay ~61 °C during 40 kW pulls.[^hotdog_fw]

## Risk Controls & Telemetry

- **Thermal Watch:** Riders pushing 16 S commuter packs noted 150 °C stators at only 35 A FW, reinforcing that ferrofluid or temperature probes are mandatory if you insist on FW in enclosed hubs.[^18]
- **Budget battery amps alongside FW.** Once a hub reaches its KV ceiling, FW draws roughly the same extra current on both the battery and phase sides, so packs and cooling need the same headroom you would budget for hard launches.[^fw_amp_pair]
- Makerbase 75100 aluminum boards are frying MOSFETs when riders hold 35 A FW on top of 130 A phase and 35 A battery during long 95–100 km/h pulls.
  - cap FW around 20 A on air-cooled builds or switch to the aluminum-PCB/vented variants.[^9]
- **Disable FW before steep descents.** VESC hub riders have locked wheels by lightly tapping brakes around 50 km/h while FW held them at the non-FW speed ceiling.
  - either roll off FW or ease into braking before dropping big hills.[^10]
- **Measure on the windings, not the shell.** External hub housings lag far behind the copper temperature, 100 A battery draw never equals 100 A phase, and on-winding thermistors expose the real ceiling—treat 25–40 % FW promises and “3.5 kW max BBSHD” claims as marketing until the motor designer provides validated data.[^11][^fw_shell_lag]
- **Log both battery and phase currents.** Riders keep flagging confusion around battery-vs-phase limits and note that layering extra D-axis amps for FW audibly raises motor noise, so plan tunes around both data channels instead of assuming one value tells the whole story.[^fw_current_logging]
- **Embedded sensors only.** Shell probes lag winding heat badly—plant thermistors inside the motor before trusting FW headroom.[^12]
- **Ignore 70 A FW “single-motor” recipes.** Veterans immediately shot down suggestions like 70 A of FW layered on 120 A battery limits because the combo risks blowing controllers or saturating single-motor stators.[^13]
- **Little FOCer burnout case study.** A 100 A battery / 200 A phase tune with 37 A FW killed a Little FOCer after a brief field-weakening run.
  - its owner now caps phase near 150 A and is migrating to 12-FET controllers for dual-motor duty.[^14]
- **Zero-FW still has a cost.** Dropping FW to zero saved energy but forced higher phase current for the same speed, driving controller temps from 46 °C to 55 °C in just 15 minutes.
  - log thermal response whenever you reshuffle FW allocations.[^15]
- **Plan AWD for single-drive heat saturation:** 3.6 kW single-motor builds backed off FW after hot-weather pulls saturated hubs and triggered plans for AWD conversions to spread load.[^16]
- **Expect softer launches than Kelly even with aggressive FW.** Pumping 250 A+ phase into IPM hubs still delivers weaker 0 km/h torque than Kelly controllers, so chase hall tuning and ramp tweaks before blaming firmware.[^17]
- **Dial FW back when the observer complains.** Mixed-wind Zero 10X builds survived highway pulls only after the crew told Shlomozero10 to drop FW toward ~20 A, raise phase current to ≈120 A at 30–35 kHz, and swap to the `mxlemming` observer.
  - log duty and temps after every tweak so similar setups do not cook mismatched hubs.[^fw-coaching]
- **Budget D-axis current carefully.** Field-weakening tuning demands proper D-axis current allocation, continuous thermal monitoring, and conservative safe percentages; commuter hubs typically limit FW to 15–25% of total current budget while drag builds may push 30–40%, but every configuration requires temperature logging to validate thermal headroom.[^fw-d-axis]
- **Voltage Monitoring:** Keep oscilloscope or high-speed logging on regen-heavy tests—22 S Spintend builds disable regen entirely when extending pack voltage to avoid BMS-induced surges.[^19]
- **Validate gains before chasing higher FW.** Happy Giraffe’s single-Ubox tests saw only ~3 km/h gains going from 10 A to 40 A FW while battery draw stayed near 45 A; peers reminded Gigolo Joe that more phase or pack voltage beats stacking FW when motors have not yet hit duty-cycle limits.[^fw-plateau]
- **Fault Masking:** Sudden current drops or pothole-induced cut-outs that disappear when FW is enabled can signal mechanical faults (loose magnets, wiring) rather than firmware bugs; investigate hardware first.[^16]
- **Watch traction-control temps.** Jan’s tests with FW and traction control enabled doubled controller temperatures and cut peak power from ~18 kW to ~13 kW, so budget airflow or soften slip targets before committing to TC-assisted FW pulls.[^18]
- **Noise & Surging:** If throttle jitters appear above 80 % duty after enabling 20 A FW on single-motor builds, roll FW back—operators traced the behavior directly to FW injection.[^20]
- **Air resistance wins past ~50 A battery.** Street builds running more than ~50 A battery during FW saw limited top-speed gains because aero drag dominates once the ERPM ceiling is reached.
  - log results at multiple current levels before tolerating extra heat.[^19]
- **Duty-cycle trigger awareness:** Remember FW starts at the configured duty threshold, so cold-weather commuters who never exceed ≈90 % duty can leave FW configured without seeing it engage, while summer hill pulls will trigger it early and dump heat fast.[^3]
- **5.3 beta isn’t a free lunch.** Firmware 5.3 beta adds roughly +8 km/h when riders request about 20 A of FW, but they still only toggle it above a set speed to preserve launch torque and keep controller temperatures in check on small hubs.[^20]
- **Overspeed Discipline:** Avoid free-spinning wheels at high FW. Halo stunt crews saw runaway RPM off-load and controller stress at 125 A FW.[^12]
- **Front-lift control:** Hotdog 100 H rear builds demand traction control or front FW assistance; otherwise the rear lifts the front well past 120 km/h even while stators only hit ~61 °C, so validate TC before public-road tests.[^hotdog_fw]
- **PWM frequency trade-offs:** Dropping zero-vector PWM toward 16–20 kHz cools the controller but pushes heat into the motor, while 30–40 kHz relieves motor temps at the cost of hotter FETs.
  - log both motor and controller temperatures during experiments.[^21][^22]
- **Tame 6.06 sensorless chatter with zero-vector tweaks.** Riders on firmware 6.06 are logging smoother sensorless handoffs once they nudge zero-vector frequency and duty timing alongside FW ramps, so add those adjustments to any vibration-troubleshooting checklist before blaming hardware.[^23]
- **Duty-cycle guardrails:** Modern hardware survives 98–99 % duty for a small top-speed bump (~4 %), but riders still treat 100 % as off-limits to avoid runaway faults.
  - treat FW tuning and duty increases as paired changes.[^24]
- **Track-day planning:** Paris-bound teams compared FW-enabled 16 S builds against base 16 S setups that free-spin near 80 km/h.
  - treat FW as the fallback after exploring higher-voltage packs or rewound hubs for sustained 100 km/h targets.[^25]
- **Traction heuristics:** Dual-drive riders accept 2–3 kERPM slip thresholds but often prefer reshaping power-per-ERPM curves instead of leaning on FW-backed traction control; front-only TC remains the safest option after rear controllers tripped at >300 A during FW pulls and crews now enable traction control on the front controller first to avoid fresh MOSFET surges.[^26][^27][^front_tc]
- **Treat FW cut-outs as catastrophic events.** Little Focer/Tronic 250 stacks that repeated 37 A FW pulls around 20 kW eventually “killed everything,” so pair conservative FW settings with ample battery headroom and stop testing the moment faults appear.[^fw-kills]
- **3Shul TC behaviour:** On 22 S dual LY 33×2 builds, 3Shul’s traction control shunted torque rearward.
  - testers disabled it temporarily to explore the ~126 km/h ceiling with 70 % FW before re-enabling TC for sane traction limits.[^28]
- **Mind saturation and hall health.** A Halo 60H stuttered at 15–20 km/h when pushed to 350 A phase with 125 A FW; adding temperature sensing, trimming phase amps, and keeping saturation compensation around 10–15 % prevented false diagnoses of phase shorts.[^29]
- **Log saturation-comp targets when chasing 300 A+.** The current review segment calls for documenting how much saturation compensation riders add as they balance 300 A phase and aggressive FW.
  - keep the tuning notes with your high-power profiles so teammates don’t reuse stale values on fresh hardware.[^30]
- **Observer & ABS interplay:** Mxlemming observers with ~125 A FW demanded higher ABS headroom (~420 A) to stop overcurrent faults at 300 A phase, while milder 30 A FW still tripped ABS on sticky launches.
  - log ABS thresholds anytime you swap observers.[^31]
- **Mixed pole-count drivetrains:** Pairing a 40-pole front with a 30-pole rear confuses traction control; racers often disable TC and preload the bars instead, relying on rider weight to settle launches.[^32]

## D-Axis Budgeting & Thermal Monitoring

- Keep FW d-axis current near 10–15 % of rated phase amps on commuter hubs and review logs after each ride; drag builds stretching toward 40 % demand redundant thermal sensors and immediate cooldown laps.[^33]
- Tie FW experiments to real-time stator and MOSFET telemetry so rising temperatures trigger manual rollback before firmware limits intervene; log both currents to confirm FW isn’t masking battery or ESR bottlenecks.[^33]

## Decision Guide: Voltage vs. Field Weakening

- **Choose Higher Voltage / Different Windings When:** You need sustained highway speed, the motor already runs hot without FW, or you’re targeting >120 km/h.
  - builders hitting 118 km/h on 22×3 hubs without FW prove gearing changes scale better than stacking FW amps.[^11][^21]
- **Match winding choice to your target speed before touching FW.** 22/3 stators deliver ferocious launch torque but stall near 120 km/h without FW, while 33/2 winds scale for highway pulls if you can feed the extra battery and phase current—pick the geometry that meets your duty-cycle goals instead of leaning on FW as a crutch.[^winding-fw]
- **Use Field Weakening When:** The pack and controller have proven thermal headroom, the chassis can handle added speed, and you only need short bursts to overtake or extend top speed marginally (≈5–15 km/h gains). Riders logging 85 km/h on 20 S singles with 30 A FW treat it as a momentary boost, not a permanent setting.[^11][^22]
- **Dial zero-vector frequency with FW.** Sensorless 6.06 tunes smooth out once zero-vector frequency hovers around 16 kHz; combine that with 5–10 A FW ramps to tame launch vibration before chasing higher duty-cycle gains.[^34]
- **Keep phase headroom for saturation compensation.** Shlomozero’s 90 H hubs respond best with 300–400 A phase and conservative 10–15 A FW; pushing FW when phase amps are already maxed leaves no headroom for saturation compensation and quickly overheats 300 A-class controllers.[^35][^36]
- **Never Use FW When:** Working on small commuter hubs or unfinished builds lacking thermistor feedback.
  - multiple riders fried stock motors at single-digit FW currents and now avoid the feature entirely.[^9][^17]
- **Expect hard limits when hardware caps phase current.** Stone Gasm’s 20×70 kV build only gained ≈19 km/h of freewheel speed with 25 A FW (66 → 84 km/h) and plateaued around 96 km/h even with the 35 A ceiling, underscoring that gearing or voltage changes.
  - not more FW
  - unlock the next tier of speed.[^37]

## Troubleshooting Checklist

- **Battery Current Overshoot:** Rerun detection/wizard, verify sensor calibration, and ensure battery limits exceed expected FW-induced draw.[^8]
- **ABS Overcurrent Trips:** Increase absolute current headroom, inspect phase connectors, and confirm observer stability before adding more FW.[^14]
- **Uncommanded Brake or Cut-Outs:** Review handbrake/UART mappings and wiring; FW magnifies regen spikes that can trip miswired systems.[^4][^23]
- **Runaway spin after throttle close:** One 75100 kept spinning with FW enabled even after releasing the throttle.
  - log firmware versions and report anomalies so regressions can be reproduced and patched, and be ready to dial FW back or raise pack voltage instead of chasing 90–110 A FW currents on Ortega observers just to gain top speed.[^38][^39]
- **Persistent Motor Heating:** Back FW down 5–10 A, improve heat sinking (direct-to-deck mounts, fresh thermal paste), or reduce phase amps before the stator saturates.[^6][^11][^18]

## Source Notes

[^1]: Field-weakening theory and trade-offs between torque, efficiency, and heat.[^40]
[^2]: Hub shell temperature lag and the need for embedded sensing.[^41]
[^3]: Bench data showing ~40 % ERPM gains with major heat penalties.[^42][^6]
[^4]: 24S Flipsky failures tied to regen spikes with FW active.[^43]
[^fw-503]: VESC Tool 3.01 only exposes FW controls on firmware 5.03, and Spintend asked riders to remain on 5.2 until its customised 5.3 builds complete soak testing.[^44][^45]
[^6]: 60 A FW on dual 84100 builds driving high heat and frame inspection needs.[^46]
[^7]: PuneDir’s stable 30 A FW baseline with `mxlemming` observer and 100 km/h GPS results.[^47][^48]
[^fw-coaching]: Crew feedback urged Shlomozero to roll FW back toward 20 A, raise phase current to ~120 A at 30–35 kHz, and rely on the `mxlemming` observer so mixed 50 H hubs survive highway pulls.[^49]
[^8]: FW letting battery current exceed configured limits until detection reruns.[^50]
[^9]: Xiaomi hub failure from modest FW and voltage experiments.[^51]
[^10]: Segway GT2 dual 85150 telemetry at 30 A FW highlighting pack limits.[^52]
[^11]: Wolf King GT Pro and similar high-power builds using 55 A FW for ~66 mph road speeds.[^53][^54]
[^12]: Halo runaway RPM and general caution for unloaded FW testing.[^55]
[^13]: High-speed regen viability with FW and the need to log bus voltage.[^56]
[^winding-fw]: Source: knowledge/notes/input_part010_review.md†L508-L509
[^fw-faults]: Using the `faults` command and raising absolute current headroom (≈200–250 A for 120–130 A phase tunes) to prevent ABS overcurrent trips during FW pulls.[^57][^58]
[^fw-duty]: Duty-cycle ceiling warnings for FW-enabled builds.
[^front_tc]: Traction-control guidance to set front-only TC first so rear controllers avoid fresh MOSFET surges.[^134]
[^rosheee_fw]: Rosheee’s dual-motor FW stagger (rear 87.5–89.5 % duty, front 93 % with 97 % max) plus +25 % throttle scaling.[^135]
[^fw_amp_pair]: Field-weakening current draw mirroring on battery and phase sides once a hub reaches its KV ceiling.[^136]
  - stretching toward 99–100 % caused abrupt cut-outs above 70 km/h.[^59][^60][^24]
[^fw-plateau]: Field-weakening tests that delivered only ~3 km/h gains from 10 A to 40 A FW until motors hit duty-cycle limits, reinforcing the need for more phase current or voltage instead of piling on FW amps.[^61]
[^13]: High-speed regen remains viable at 80–100 km/h under heavy FW because the load collapses back EMF quickly, but riders still log bus voltage to confirm headroom.[^62]
[^14]: Using the `faults` command and absolute current headroom to manage FW-induced spikes.[^63]
[^15]: Duty-cycle ceiling warnings for FW-enabled builds.[^64][^60][^24]
[^16]: FW masking mechanical faults in high-speed Vsett builds and needing inspections.[^65]
[^17]: Haku’s decision to abandon FW after killing commuter hubs at 4 A.[^66]
[^18]: Max G2 and similar commuter hubs hitting 150 °C stators with FW.[^67]
[^19]: 22 S Ubox/Spintend configurations disabling regen to survive higher voltage.[^68]
[^phase_launch]: Pandalgns reminded builders that high launch torque is tied to phase current; as speed rises the controller naturally drifts toward the battery limit, so staged limits or higher battery amps extend the hard-acceleration window.[^69]
[^20]: FW-induced throttle jitter on single-controller builds once 20 A is applied.[^70]
[^fw-kills]: FW-induced shutdowns have spiked components and “killed everything” on Little Focer/Tronic 250 stacks when riders pushed 37 A of FW without battery headroom.[^71]
[^21]: 22×3 hub builds freewheeling around 118 km/h without FW after pack upgrades.[^72]
[^22]: 20 S single-motor package delivering 85 km/h with ~30 A FW as a short-burst aid.[^73]
[^23]: Firmware or wiring faults causing sudden full braking after FW-enabled firmware updates.[^74]
[^24]: Riders now log high-speed (80–100 km/h) FW regen drills to confirm bus voltage stays under Spintend limits before trusting the setup on public roads.[^75]
[^hotdog_fw]: NAMI 100 H rear / 70 H front builds logging 500 A phase, 550 A absolute, 100 % front FW, and ~61 °C stators while traction control keeps the rear from lifting the front at 120 km/h.[^76][^77]

## Field-Weakening Tuning Details

- **Tune FW gently with long ramps.** The same hub quit stuttering once sensorless transition was raised from 500 to ~3,000 eRPM, then ran smoothly with 20 A of field weakening, duty capped around 85–89%, and an 800 ms FW ramp to soften current spikes above 55 km/h.[^fw_ramp]
- **FW ramp tuning for heavy riders.** Zak's Raiden 7 log showed sluggish throttle release until the FW ramp was stretched to 400 ms (others prefer 600 ms) and duty ceiling trimmed to ~97%.
  - practical guardrails for heavier riders chasing extra top speed without runaway torque requests.[^fw_heavy]
- **Field-weakening amps add to battery current.** Firmware reports battery current plus field-weakening draw; budget 10 A of FW as additional pack load so commuter cells stay within safe C-rates.[^fw_battery_budget]
- **Flipsky boards ignore battery-current limits once FW engages.** Mentors warned that Flipsky ignores the "battery current max" slider once FW engages, so bypassed 16 S G30 batteries should keep FW at zero (or very low) until riders log real pack current and prove the cells survive the extra draw and heat.[^flipsky_fw_ignore]
- **Avoid `mxm` observers on tiny hubs.** Small commuter motors driven by Flipsky 75200s have smoked controllers when `mxm` observers and heavy FW were stacked; raise voltage or reduce FW instead of forcing low-inductance hubs past their comfort zone.[^78]

## MOSFET Failures Under High FW

- **Stock 85150 MOSFETs overheat with heavy FW.** Stock Spintend 85150 MOSFETs overheat quickly once you layer 45 A of field weakening on top of 105–120 A battery and 150–175 A phase requests; riders chasing higher ERPMs swap in HY/HSBL Toll packages with hotplate reflow or back FW down to ~50 A at 87% duty.[^fw_mosfet]

## Source Notes (continued)

[^fw_ramp]: Field-weakening ramp tuning to soften current spikes.[^79][^80]
[^fw_heavy]: FW ramp settings for heavy riders to prevent runaway torque.[^81]
[^fw_battery_budget]: Field-weakening impact on total battery current draw.[^82]
[^flipsky_fw_ignore]: Flipsky controllers ignoring battery current limits during field weakening.[^83]
[^fw_mosfet]: Spintend 85150 MOSFET failures under high field-weakening loads.[^79]

[^fw_shell_lag]: Source: knowledge/notes/input_part006_review.md†L452-L457
[^fw_current_logging]: Source: knowledge/notes/input_part006_review.md†L455-L456

## References

[^1]: Source: knowledge/notes/input_part003_review.md†L149-L149
[^2]: Source: knowledge/notes/input_part007_review.md†L502-L502
[^3]: Source: knowledge/notes/input_part000_review.md†L653-L655
[^4]: Source: knowledge/notes/input_part000_review.md†L742-L752
[^5]: Source: knowledge/notes/input_part006_review.md†L127-L128
[^6]: Source: knowledge/notes/input_part000_review.md†L654-L654
[^7]: Source: data/vesc_help_group/text_slices/input_part001.txt†L7166-L7194
[^8]: Source: data/vesc_help_group/text_slices/input_part003.txt†L7443-L7500
[^9]: Source: knowledge/notes/input_part005_review.md†L197-L197
[^10]: Source: knowledge/notes/input_part006_review.md†L207-L207
[^11]: Source: knowledge/notes/input_part006_review.md†L454-L456
[^12]: Source: knowledge/notes/input_part006_review.md†L457-L457
[^13]: Source: knowledge/notes/input_part006_review.md†L357-L357; data/vesc_help_group/text_slices/input_part005.txt†L24644-L24651
[^14]: Source: knowledge/notes/input_part008_review.md†L128-L128
[^15]: Source: knowledge/notes/input_part012_review.md†L151-L151
[^16]: Source: knowledge/notes/input_part008_review.md†L16099-L16129
[^17]: Source: knowledge/notes/input_part005_review.md†L38-L38
[^18]: Source: knowledge/notes/input_part002_review.md†L51-L52
[^19]: Source: data/vesc_help_group/text_slices/input_part001.txt†L10537-L10629
[^20]: Sources: knowledge/notes/input_part000_review.md†L351-L351; knowledge/notes/input_part013_review.md†L709-L709
[^21]: Source: data/vesc_help_group/text_slices/input_part003.txt†L10215-L10280
[^22]: Source: data/vesc_help_group/text_slices/input_part003.txt†L10383-L10407
[^23]: Source: knowledge/notes/input_part012_review.md†L301-L301
[^24]: Source: data/vesc_help_group/text_slices/input_part003.txt†L11586-L11610
[^25]: Source: data/vesc_help_group/text_slices/input_part003.txt†L7472-L7500
[^26]: Source: data/vesc_help_group/text_slices/input_part003.txt†L9688-L9748
[^27]: Source: data/vesc_help_group/text_slices/input_part003.txt†L19680-L19699
[^28]: Source: data/vesc_help_group/text_slices/input_part009.txt†L10292-L10324
[^29]: Source: knowledge/notes/input_part012_review.md†L152-L152
[^30]: Source: knowledge/notes/input_part012_review.md†L302-L302
[^31]: Source: knowledge/notes/input_part012_review.md†L63-L63
[^32]: Source: knowledge/notes/input_part012_review.md†L64-L64
[^33]: Source: knowledge/notes/input_part006_review.md†L510-L510
[^34]: Source: knowledge/notes/input_part012_review.md†L301-L302
[^35]: Source: knowledge/notes/input_part012_review.md†L302-L304
[^36]: Source: knowledge/notes/input_part012_review.md†L344-L344
[^37]: Source: knowledge/notes/input_part013_review.md†L30-L30
[^38]: Source: knowledge/notes/input_part008_review.md†L311-L311
[^39]: Source: data/vesc_help_group/text_slices/input_part009.txt†L1309-L1331
[^40]: Source: knowledge/notes/input_part006_review.md†L408-L423
[^41]: Source: knowledge/notes/input_part006_review.md†L423-L436
[^42]: Source: knowledge/notes/input_part000_review.md†L727-L727
[^fw53_rollout]: Source: knowledge/notes/input_part000_review.md†L806-L806
[^43]: Source: knowledge/notes/input_part001_review.md†L111-L112
[^44]: Source: data/vesc_help_group/text_slices/input_part001.txt†L2706-L2975
[^45]: Source: data/vesc_help_group/text_slices/input_part001.txt†L4000-L4052
[^46]: Source: knowledge/notes/input_part009_review.md†L43-L43
[^47]: Source: knowledge/notes/input_part009_review.md†L44-L44
[^48]: Source: knowledge/notes/input_part009_review.md†L179-L179
[^49]: Source: knowledge/notes/input_part009_review.md†L389-L390
[^50]: Source: knowledge/notes/input_part009_review.md†L117-L117
[^51]: Source: knowledge/notes/input_part009_review.md†L93-L93
[^52]: Source: knowledge/notes/input_part010_review.md†L293-L293
[^53]: Source: knowledge/notes/input_part013_review.md†L65-L65
[^54]: Source: knowledge/notes/input_part013_review.md†L599-L599
[^55]: Source: knowledge/notes/input_part012_review.md†L28-L28
[^56]: Source: knowledge/notes/input_part005_review.md†L463-L465
[^57]: Source: data/vesc_help_group/text_slices/input_part001.txt†L2840-L2872
[^58]: Source: data/vesc_help_group/text_slices/input_part001.txt†L3796-L3808
[^59]: Source: data/vesc_help_group/text_slices/input_part001.txt†L4944-L4953
[^60]: Source: knowledge/notes/input_part003_review.md†L104-L104
[^61]: Source: data/vesc_help_group/text_slices/input_part001.txt†L4053-L4148
[^62]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24644-L24651
[^63]: Source: knowledge/notes/input_part001_review.md†L139-L139
[^64]: Source: knowledge/notes/input_part001_review.md†L160-L160
[^65]: Source: knowledge/notes/input_part013_review.md†L741-L741
[^66]: Source: knowledge/notes/input_part011_review.md†L301-L301
[^67]: Source: knowledge/notes/input_part005_review.md†L368-L372
[^68]: Source: knowledge/notes/input_part010_review.md†L419-L419
[^69]: Source: data/vesc_help_group/text_slices/input_part013.txt†L356-L357
[^70]: Source: knowledge/notes/input_part013_review.md†L709-L709
[^71]: Source: knowledge/notes/input_part009_review.md†L353-L355
[^72]: Source: knowledge/notes/input_part013_review.md†L88-L88
[^73]: Source: knowledge/notes/input_part013_review.md†L145-L145
[^74]: Source: knowledge/notes/input_part001_review.md†L219-L219
[^75]: Source: knowledge/notes/input_part005_review.md†L608-L608
[^76]: Source: knowledge/notes/input_part014_review.md†L8930-L8933
[^77]: Source: knowledge/notes/input_part014_review.md†L10001-L10055
[^78]: Source: knowledge/notes/input_part009_review.md†L87-L87
[^79]: Source: knowledge/notes/input_part004_review.md†L20-L20
[^80]: Source: knowledge/notes/input_part004_review.md†L97-L97
[^81]: Source: knowledge/notes/input_part004_review.md†L336-L336
[^82]: Source: knowledge/notes/input_part004_review.md†L570-L570
[^83]: Source: knowledge/notes/input_part004_review.md†L315-L315
[^134]: Source: knowledge/notes/input_part003_review.md†L505-L505
[^135]: Source: knowledge/notes/input_part003_review.md†L599-L599
[^136]: Source: knowledge/notes/input_part003_review.md†L600-L600
[^79]: Source: data/vesc_help_group/text_slices/input_part004.txt†L1197-L1253
[^80]: Source: data/vesc_help_group/text_slices/input_part004.txt†L1247-L1259
[^81]: Source: data/vesc_help_group/text_slices/input_part004.txt†L23716-L23735
[^82]: Source: data/vesc_help_group/text_slices/input_part004.txt†L1247-L1259
[^83]: Source: data/vesc_help_group/text_slices/input_part004.txt†L21108-L21182
[^84]: Source: knowledge/notes/input_part010_review.md†L403-L404
[^85]: Source: knowledge/notes/input_part010_review.md†L405-L405
[^fw-d-axis]: Source: knowledge/notes/input_part006_review.md†L510-L510
