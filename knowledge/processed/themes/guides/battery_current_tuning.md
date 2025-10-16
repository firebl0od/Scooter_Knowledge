# Battery, Phase & Regen Current Mastery

## Why This Guide Exists
Taming current limits is the difference between a scooter that rips for years and one that torches controllers, packs, or riders. The chat logs surface dozens of real-world failures—BMS trips, blown caps, runaway regen—that all trace back to sloppy current planning. This playbook distills the community’s hard-won lessons into a repeatable workflow you can hand to teammates or clients.

## Build Prerequisites
1. **Healthy pack & BMS:** Log internal resistance and balance status before tuning. Parallel packs with mismatched protections can surge into one another when a single BMS trips, so size discharge and regen around the weakest board.¹
2. **Balance capability matters:** Daly smart BMS units only balance at ≈30 mA; fast-charge builds should plan external 4 A balancers and verify you never back-feed the board while it sleeps. JK/LLT hardware remains the go-to when you need stronger balancing, CAN/RS485 logging, or reliable Bluetooth wake-ups.【F:data/vesc_help_group/text_slices/input_part004.txt†L16369-L16419】【F:data/vesc_help_group/text_slices/input_part004.txt†L18865-L18868】
3. **ESC cutoffs must exceed BMS trips.** If the controller’s battery cutoff sits below the pack’s protection threshold, the BMS will sever power mid-load—raise VESC cutoffs a few volts so the ESC idles before the pack hard-resets.【F:knowledge/notes/input_part004_review.md†L311-L311】
4. **Trustworthy wiring & connectors:** QS8/QS10 or AS150-class connectors and 6 mm²+ phase leads are the expectation above ~250 A phase. Revisit solder joints, pad pressure, and thermal interface materials before chasing higher numbers, remembering that AS150 anti-sparks only tame the initial plug-in arc and do nothing for motor phases, while QS8 discharge leads carrying ~350 A peaks need 6 AWG when a single connector handles the load (8 AWG suffices when the pack splits across two leads).²【F:knowledge/notes/input_part005_review.md†L258-L262】
5. **Avoid mismatched parallels:** Keep battery mains single and appropriately sized; short AWG14 leads tolerate ~40 A bursts, but paralleling thin wires or leaving cold solder joints invites uneven current sharing and hotspots. QS8 terminations also demand heavy tips, generous flux, and clean shrink to avoid vibration fatigue.【F:knowledge/notes/input_part005_review.md†L263-L266】【F:knowledge/notes/input_part005_review.md†L267-L271】
6. **Accurate motor data:** Do not rely on auto-detection when values look suspicious (e.g., ERPM flips, inductance jumps). Measure Rs/Ls with external tools or re-run detection on known-good hardware before editing limits.³
7. **Cooling strategy:** Deck-mounted plates, fresh thermal paste, and airflow matter as much as MOSFET specs. Gutted aluminum cases and machined mounts are the baseline once you exceed 60 A battery.⁴
2. **Balance capability matters:** Daly smart BMS units only balance at ≈30 mA; fast-charge builds should plan external 4 A balancers and verify you never back-feed the board while it sleeps. JK/LLT hardware remains the go-to when you need stronger balancing, CAN/RS485 logging, or reliable Bluetooth wake-ups, and JK owners now tighten delta triggers to ≈0.01 V with ~0.2 A active shuttling so 7 p bricks stay aligned without cooking resistors.[^jk-delta]
2. **ESC cutoffs must exceed BMS trips.** If the controller’s battery cutoff sits below the pack’s protection threshold, the BMS will sever power mid-load—raise VESC cutoffs a few volts so the ESC idles before the pack hard-resets.【F:knowledge/notes/input_part004_review.md†L311-L311】
3. **Trustworthy wiring & connectors:** QS8/QS10 or AS150-class connectors and 6 mm²+ phase leads are the expectation above ~250 A phase. Revisit solder joints, pad pressure, and thermal interface materials before chasing higher numbers.²
4. **Accurate motor data:** Do not rely on auto-detection when values look suspicious (e.g., ERPM flips, inductance jumps). Measure Rs/Ls with external tools or re-run detection on known-good hardware before editing limits.³
5. **Cooling strategy:** Deck-mounted plates, fresh thermal paste, and airflow matter as much as MOSFET specs. Gutted aluminum cases and machined mounts are the baseline once you exceed 60 A battery.⁴

## Step-by-Step Tuning Workflow
1. **Baseline detection & calibration**
   - Warm the motor and pack, disable the phase filter on Flipsky 75xxx units, and rerun detection with the `mxlemming` observer before touching currents.⁵
   - Validate halls and 5 V rails after detection—many “mystery faults” are just dead sensor power.⁶
   - Calibrate handheld IR meters with ~20 mΩ shunts or resistor networks before binning cells; expect fresh P42A near 8 mΩ, Samsung 50S around 10 mΩ, and first-gen 50E in the low-20 mΩ range—absolute values drift but spreads stay useful.【F:knowledge/notes/input_part004_review.md†L145-L147】
2. **Set conservative currents**
- Start with a 2:1 to 3:1 phase-to-battery ratio (e.g., 40 A battery / 110 A phase on 16 S commuter packs).⁵ ⁷
- 16 S 5 P Samsung 35E packs stay healthy around 40 A continuous (50 A bursts) with 110–125 A phase and ABS caps near 180 A; keep regen gentle (~7 A battery / 15 A motor) so commuter cells don’t overheat.[^16s35e]
- Budget field-weakening draw in your battery limit—real rides show 65 A-limited 6 P packs sagging instantly when FW amps pile on top of throttle demand.【F:data/vesc_help_group/text_slices/input_part004.txt†L8000-L8056】
- Match current targets across front/rear controllers to avoid free-spinning the lighter wheel.⁸
- MakerX vs. Flipsky tuning clinics still steer single-motor riders toward ~60 A battery and 180–200 A phase ceilings until thermal logs prove headroom.【F:knowledge/notes/input_part003_review.md†L97-L97】
- Stock Vsett 10+ packs built around 25.6 Ah LG MH1/MJ1 cells stay happiest near 60 A; pushing 70–80 A in sport mode triggers sag, sub-20-mile range, and BMS cut-outs even if short logs show 78 A peaks.[^vsett-pack]
- For 16 S5 P Samsung 35E commuters, Artem caps battery at 40 A (≈150 A phase absolute 170 A) with regen ≤−17 A, noting that extra current only improves mid-speed punch and depends on accurate hall telemetry.[^vsett-35e]
   - Heavy single-motor builds chasing 90 km/h stick near 120 A phase and 80–85 A battery with 16 kHz zero-vector and MTPA enabled; treat those numbers as the practical ceiling without upgraded cooling.【F:knowledge/notes/input_part003_review.md†L100-L100】
   - 17 S dual Spintend builds that overheat packs and trims settle around 2×120 A phase, 2×90 A battery, and 2×180 A absolute, while the same chassis on 16 S rides closer to 2×100 A phase and 2×60 A battery once thermal logs dictate the final envelope.【F:data/vesc_help_group/text_slices/input_part001.txt†L25366-L25439】
   - Treat dual-motor 16 S7 P Samsung 50E packs as roughly 140 A systems: hold each controller near 70 A battery and add ducted airflow up front before nudging limits higher.²³
- Calculate pack ESR—including the cells, BMS FETs, harness runs, and nickel busbars—before setting current ceilings; nominal voltage × amps ignores the sag you’ll see under load, and LiFePO₄’s flat curve makes coulomb counters more trustworthy than voltage-based gauges.【F:knowledge/notes/input_part006_review.md†L503-L503】
- Pair coulomb counters or BMS-integrated amp-hour logs with ride notes so LiFePO₄ commuters see true consumption; the flatter discharge curve hides low-voltage cutoffs until it is too late, whereas coulomb math catches when ESR or wiring losses erode usable capacity.【F:knowledge/notes/input_part006_review.md†L503-L503】
- Size packs by watt-hours at the target load, not nominal amp-hours: six parallels of 21700 roughly equal seven 18650s for volume, 12 S of VTC6 matches 13 S of 35E for sag, and Samsung 35E or LG MH1 stay cost-effective under ≈7 A per cell.[^wh_math]
- For 12 S 5 P Xiaomi decks pulling 60–80 A, Samsung 48X or 50G deliver more usable energy at 15 A than P42A while staying cool; Samsung 50E overheats once cell current tops 10–12 A, so reserve it for gentler builds.[^48x_choice]
- 21700 availability and copper busbars now let Tudor’s crew stack 17 S 6 P 40T/50G arrays that tolerate high discharge despite €5–€7 per cell EU pricing—plan current targets around chemistry cost as well as thermal headroom.[^21700_push]
- Keep Artem’s relationship in mind: `I_phase = I_batt × V_batt ÷ V_motor`, so phase torque fades as ERPM climbs—log both currents to confirm your battery caps aren’t starving the tune mid-pull.[^phase_equation]
- Field-weakening still trades efficiency for speed—expect roughly 25 % higher losses and noticeable current spikes once it kicks in, which is why top-speed pulls suddenly heat controllers and packs.[^fw-losses]
- Treat 45 A-per-cell marketing cautiously—P42A/P45B packs live closer to 30–38 A per cell in the real world, and builders rely on temperature probes and potting because scooters rarely sustain full load outside brief 100 km/h pulls.【F:knowledge/notes/input_part006_review.md†L308-L308】
   - For daily commuters, finish charges around 90 % if the BMS still balances there—you’ll quadruple pack lifespan versus living at 100 %.【F:knowledge/notes/input_part007_review.md†L307-L307】
3. **Log, ride, iterate**
- Capture VESC Tool live data plus Dragy/GPS logs, note duty-cycle ceilings, and adjust wheel circumference so controller and GPS speeds agree.⁹
- Screen-record smart-BMS or XMatic telemetry while you test—Yamal and Yoann log ~286–290 A battery peaks so the crew can vet discharge ceilings without guessing from feel alone.[^xmatic-logging]
- Watch battery sag and motor temps; if the pack drops >10 % under your target load, reduce battery current or improve the pack.¹⁰
- Cranking `iQ target` for harder launches can still trip pack protection—logs show some BMS boards dropping output to zero when the requested torque outpaces battery capability, so treat that setting as additive load on the cells.【F:knowledge/notes/input_part006_review.md†L147-L147】
- Expect extra sag in winter—Mirono logs an additional 3–4 V drop near 1 °C and eases battery current to save range and pack temperature.[^cold-sag]
- NetworkDir’s 72 V race brick still lives at 100–120 A despite 8–10 V droop, proving you can run droopy packs if the BMS thresholds stay clear and logs confirm temps remain under control.[^race-droop]
- Cross-check real-time power with an external meter or SmartDisplay—unfiltered VESC telemetry overshoots true watts by 10 kW or more on aggressive pulls.²⁴
- Remember that phase current alone doesn’t define power; veterans called out logs boasting huge phase amps while battery current stayed flat—energy still comes from pack voltage × battery amps, and PWM waveforms muddy simple √3 conversions, so log both channels before chasing bragging rights.【F:data/vesc_help_group/text_slices/input_part005.txt†L23317-L23373】
- Treat VESC Tool’s state-of-charge gauge as a rough helper—it linearly maps 4.2–3.3 V per cell (≈66 V on 20 S), so keep your cutoffs a few volts above the BMS trip to prevent surprise throttling once the display reads “empty.”²⁵
- Stage controller low-voltage cutoffs above the BMS limit so power tapers before the protection opens; pair that with temp logging on marginal packs so sag-induced heating doesn’t sneak up mid-ride.[^cutoff-margin]
- Use phase-current behaviour as a health check: dual Spintend builds hold 120–130 A phase per motor (≈160 A ABS) happily—if a hub starts stuttering above ~85 A, dig for a blown MOSFET or loose phase lead instead of simply backing off current.【F:knowledge/notes/input_part000_review.md†L663-L664】
4. **Layer in regen**
   - Add regen after forward currents stabilize. Keep battery regen gentler than your discharge target (−5 A to −10 A is plenty for commuter packs) and ramp up slowly to avoid BMS or controller cutoffs.⁵ ¹¹
   - ≥21 S packs demand extra headroom—keep regen targets under −50 A and leave a few volts of pack margin to avoid the overvoltage spikes documented on 23 S builds.【F:data/vesc_help_group/text_slices/input_part004.txt†L12557-L12583】
   - Dual-motor commuters start around −30 A battery/−80 A phase on the rear and −25 A/−55 A up front; log stator temps during shakedowns before increasing braking torque.[^regen_baseline]
   - A 10 S 2 P P42A pack still logged 2.55 kW regen spikes and rapid controller heating, so monitor MOSFET and hub temperatures whenever you experiment with aggressive braking profiles.[^regen_bursts]
5. **Optional: field weakening & traction control**
   - Activate FW only once thermals are understood. Expect it to draw nearly the same extra amps you request on both battery and phase channels.¹²
   - Treat the extra FW amps as additive to your battery limit—if you budget 100 A battery and add 25 A FW, logs will still show ≈125 A at the pack.【F:data/vesc_help_group/text_slices/input_part004.txt†L10300-L10305】
   - On dual drives, enable traction control on the front controller first and monitor for MOSFET surges when grip returns.¹³
   - September 2022 track work showed traction-control launches heating Ubox singles faster than manual pulls; budget extra heatsinking or relax slip targets during long straights.[^tc_heat_2022]

## Hardware Guardrail Table
| Controller | Typical Pack | Battery Current (per controller) | Phase Current | Regen (Battery / Phase) | Notes |
| --- | --- | --- | --- | --- | --- |
| Flipsky 75100 | 16–20 S hubs | 60–80 A | 220–270 A | −10 A / −60 A | Absolute max ≤300 A; repaste and hard-mount before testing.⁴ ¹⁴ |
| Flipsky 75200 Pro V2 | 20 S commuters | 50–60 A | 100–120 A (idle fix), up to 150 A with cooling | −5 A / −40 A | Requires phase-filter disable + `mxlemming` observer to prevent idle heating.⁵ |
| MakerX single (GO-FOC HI100) | 16–20 S duals | 60 A | 200 A | −8 A / −45 A | Runs cooler than equivalent Flipsky hardware when bolted to metal decks.⁴ |
| Spintend Ubox 85/150 | 20–22 S duals | 80–100 A (≈200 A max on 22 S) | 250–300 A | −12 A / −60 A | Firmware clamps phase ≈350 A; community keeps 22 S tunes near 200 A battery / 300 A phase for longevity.¹⁵ ²⁶ |
| Makerbase 84100 HP | 20 S singles | 60–80 A | ≤135 A | −8 A / −35 A | Higher settings have produced instant failures—treat datasheet peaks as marketing.³ |
| Boutique Tronic X12 | 22–24 S race | 100 A (stock firmware) | 400 A phase, ABS ≈600 A limit | −15 A / −80 A | No-limit firmware lifts ABS but demands extensive cooling and logging.¹⁶ |

## Regen & Braking Best Practices
- **Respect BMS limits.** Daly and ANT boards trip around 2.7 V/cell; match VESC cutoff and regen so the BMS stays ahead of controller protection.¹¹ ¹⁷
- **Treat BMS trips as controller killers.** Mid-ride Daly shutdowns have back-fed voltage spikes into VESC MOSFETs—probe pack voltage before and after disconnects, wake latched boards with a charger, and raise regen thresholds so emergency braking doesn’t exceed the pack’s charge headroom.【F:knowledge/notes/input_part000_review.md†L356-L356】
- New 60 A Daly hardware now enforces under/over-current trips mid-ride instead of staying latched on—set firmware ceilings below the fresh hardware thresholds before trusting them on high-speed pulls.【F:knowledge/notes/input_part003_review.md†L202-L203】
- **Stagger braking inputs.** Pair mechanical brakes with modest regen; runaway regen has bricked 75100 logic boards when negative current spikes hit unstable hardware.¹⁸
- **Leave regen enabled for lever brakes.** Zeroing battery regen also disables lever-based e-brakes; keep a small negative current target and shape throttle curves inside ADC apps instead.【F:knowledge/notes/input_part004_review.md†L329-L329】
- **Throttle & ramp tuning.** Shorten positive ramp to ~0.1 s and sculpt throttle curves once your current caps are dialed—especially on controllers that feel soft off the line.¹⁹

## Pack Protection & Monitoring
- **Running pack-only is risky.** Riders skipping BMS boards to “save space” saw cell drift and failures within months—if you insist on BMS-less packs, log every group, schedule manual balancing, and accept the elevated fire risk.【F:data/vesc_help_group/text_slices/input_part004.txt†L9921-L9939】
- **Charge-only boards aren’t immunity.** Charge-only ANT 40 A stacks still let cells spike toward 40 A each during burnouts, so add temperature sensors and plan manual monitoring before bypassing discharge FETs.【F:knowledge/notes/input_part006_review.md†L311-L311】
- **Respect ANT precharge limits.** The onboard precharge FET taps out near 20 A; add external resistors or buttons for cold starts instead of raising firmware limits and cooking the device.【F:data/vesc_help_group/text_slices/input_part004.txt†L5880-L5893】【F:data/vesc_help_group/text_slices/input_part004.txt†L5933-L5940】
- **Wake sleepy BMS boards with a charger.** Happy/Xiaomi protections sometimes latch off after inrush events—tickle the charge port briefly before condemning the controller.【F:knowledge/notes/input_part004_review.md†L301-L302】
- **Audit bargain packs before trusting them.** One Amazon 20 S brick stalled at 81.8 V with mixed 4.1/3.8 V groups—proof that low-cost assemblies and bargain chargers can ship wildly unbalanced.[^amazon-pack]

## Charging & Charger Vetting
- **Audit adjustable chargers.** The Celler-branded 20 S bench supply landed on voltage with steady thermals, but log fan duty and case temps during long charges before endorsing it for customers.【F:data/vesc_help_group/text_slices/input_part004.txt†L19666-L19710】
- **Replace sketchy 22 S supplies.** Refurbished Meanwell stacks have failed under load—source purpose-built 22 S chargers or vetted lab supplies instead of gambling on patched industrial gear.【F:data/vesc_help_group/text_slices/input_part004.txt†L9300-L9374】
- **Isolation test series chargers.** Before stacking power supplies, meter the earth-to-output resistance; only run them in series once you confirm floating outputs and add fuses on both legs.【F:data/vesc_help_group/text_slices/input_part004.txt†L10020-L10045】
- **Acceptance test every bench supply.** Check ground continuity, breaker reset behaviour, and voltage accuracy under load before deploying adjustable chargers to customers.【F:data/vesc_help_group/text_slices/input_part004.txt†L12090-L12105】
- **Label Meanwell-style VR pots.** Adjust VR1 for output voltage, VR2 for current, and VR3 for cutoff while the charger powers a partially discharged pack—always tune under load to avoid overshoot.【F:data/vesc_help_group/text_slices/input_part004.txt†L17519-L17544】
- **Budget time for slow stock chargers.** A 1.75–2 A Zero 10X brick legitimately needs ≈11 hours to refill an 18.2 Ah pack from ~50 V to 54 V—long sessions aren’t automatically a failure sign.[^slow-brick]

## Field-Weakening & High-Speed Notes
- Expect only modest top-speed gains (e.g., +8 km/h on 16 S builds) while battery draw jumps from 4 kW to 7 kW—VSETT 10 telemetry showed ~30 A of field weakening per motor only lifting speed from 69 km/h to ~76 km/h while doubling power draw, so higher voltage or higher-Kv motors remain better investments.¹²【F:knowledge/notes/input_part003_review.md†L205-L205】
- Field tests comparing FW vs. pure gearing runs confirmed the efficiency penalty—riders planned October track sessions to validate the trade-off on 16 S builds before committing to new tunes.【F:knowledge/notes/input_part003_review.md†L75-L75】
- Sensorless chatter and long phase cables exaggerate FW-induced current spikes; keep leads short and add halls where possible.³ ²⁰
- Document duty-cycle ceilings—modern hardware tolerates 98–99 % duty, but stay below 100 % to avoid runaway faults.²¹
- FW engages on duty cycle, not speed, so it can fire at zero eRPM on hill starts—disable it on commuter packs unless you have current headroom and instrumentation.【F:knowledge/notes/input_part004_review.md†L362-L362】
- Bypassed 16 S commuter packs still feel FW amps; keep FW near zero (≤10 A) until pack-current logs prove the cells can absorb the extra draw without sagging below 3.6 V per cell.【F:knowledge/notes/input_part004_review.md†L315-L315】【F:knowledge/notes/input_part004_review.md†L386-L386】
- Riders chasing speed-triggered FW are waiting on firmware hooks—the community wants duty-based FW that delays engagement until the wheel is rolling to prevent hill-start overheating.【F:data/vesc_help_group/text_slices/input_part004.txt†L17680-L17718】
- Spintend 85150 hardware has already sacrificed MOSFETs when riders layered 45 A of FW on top of 105/120 A battery and 150/175 A phase at 20 S—budget HY/HSBL swaps or back FW down before chasing higher ERPM. 【F:knowledge/notes/input_part014_review.md†L21-L21】
- Rob Ver’s 85/240 build touched 35 kW and 132 km/h on 22×3 hubs with ~80 A of FW, yet a 22 S BMS failure during a 320 A launch still blew MOSFETs—treat high-FW pulls as consumable unless pack protection is rock-solid.[^fw_bms]

## Troubleshooting Cheatsheet
| Symptom | Likely Cause | Fix |
| --- | --- | --- |
| Controller idles hot or chatters at low speed | Phase filter enabled, bad detection values | Disable filter, rerun detection with `mxlemming`, verify Rs/Ls manually.⁵ |
| Motor cooks during bench tests | Open-loop duty-cycle experiments without load | Use gradual ramps; a 300 A open-loop stunt already destroyed a Rage Mechanics motor and highlighted the risk of duty sweeps on bare wheels.[^open_loop_burnout] |
| Regen kills power but forward throttle is fine | BMS trip or controller ABS limit too low | Reduce regen, raise ABS max (≤300 A on 75-series), ensure BMS thresholds align.¹⁴ ¹⁸ |
| Phase amps plateau far below target | Motor saturation, long phase leads, or firmware clamp | Shorten leads, add halls, log saturation, or flash no-limit firmware (with cooling).¹² ²⁰ ¹⁶ |
| Mid-drive e-bike stalls around 16 km/h | Conservative motor-current limits or mismatched ERPM settings | Raise motor current toward ~80 A phase / 20 A battery, verify wheel size/gear ratios, and log duty cycle while watching for BMS cut-outs.【F:knowledge/notes/input_part006_review.md†L33-L33】 |
| USB disconnects during hard pulls | ADC noise, poor shielding | Use shielded looms, keep 5 V accessories off logic rails, or log over CAN instead.²² |
| Random controller death after BMS cutoff | Fragile logic rails on Flipsky hardware | Keep cutoff ≥5 V above pack max, avoid sudden pack disconnects, add soft-start contactors.¹⁸ |

## Continuous Improvement
- Maintain a build sheet with firmware versions, connector choices, and current settings for every scooter you service.
- Archive VESC Tool XML profiles alongside ride logs so you can roll back when experiments fail.
- Share postmortems—photos, temperature logs, scope captures—with the community to keep the guardrail table honest.

## Source Notes
[^xmatic-logging]: Screen-recording XMatic/smart-BMS telemetry captured ~286–290 A battery peaks for Yoann and Yamal while chasing discharge limits.【F:knowledge/notes/input_part007_review.md†L108-L108】
[^jk-delta]: JK smart BMS owners now leave active balancing enabled, tighten delta thresholds to roughly 0.01 V, and cap shuttle current around 0.2 A so even 7 p packs stay aligned without cooking resistors.【F:knowledge/notes/input_part007_review.md†L205-L205】
[^cold-sag]: Winter test logs showed 3–4 V of extra sag at 1 °C, so Mirono trims battery amps in the cold to preserve range and pack temperature.【F:knowledge/notes/input_part007_review.md†L211-L211】
[^race-droop]: NetworkDir’s 72 V 29.8 Ah race pack still survives 100–120 A pulls despite 8–10 V sag as long as the BMS threshold stays clear and temps remain logged.【F:knowledge/notes/input_part007_review.md†L212-L212】
[^cutoff-margin]: Happy Giraffe keeps controller cutoffs above the BMS threshold and logs motor temps so sag-triggered heating doesn’t surprise riders mid-run.【F:knowledge/notes/input_part007_review.md†L228-L228】
[^amazon-pack]: Amazon bargain 20 S pack arrived at 81.8 V with mixed 4.1 V/3.8 V groups, proving low-cost assemblies can ship badly unbalanced when chargers/BMSs are cheap.【F:knowledge/notes/input_part007_review.md†L206-L206】
[^slow-brick]: Zero 10X owners clock ~11 hours for a 1.75–2 A stock charger to refill an 18.2 Ah pack from ~50 V to 54 V—long charge times alone aren’t proof of pack failure.【F:knowledge/notes/input_part007_review.md†L225-L225】
[^1]: Parallel-pack surge warnings when mixed BMS boards trip under load.【F:knowledge/notes/input_part008_review.md†L98-L104】
[^2]: Connector and heatsink best practices for high-current builds.【F:knowledge/notes/input_part003_review.md†L512-L513】【F:knowledge/notes/input_part003_review.md†L496-L497】
[^3]: Manual detection workflow and bad auto-tune case studies.【F:knowledge/notes/input_part009_review.md†L111-L129】
[^4]: Thermal rework expectations and MakerX vs. Flipsky mounting comparisons.【F:knowledge/notes/input_part003_review.md†L436-L438】【F:knowledge/notes/input_part003_review.md†L470-L474】
[^5]: Phase-filter disable plus `mxlemming` observer fix for Flipsky 75200 V2 idle heating.【F:knowledge/notes/input_part008_review.md†L103-L106】
[^6]: Hall-detection failures tied to 5 V rails on Flipsky hardware.【F:knowledge/notes/input_part011_review.md†L569-L571】
[^7]: 16 S commuter current baseline (40 A battery / 110 A phase) and BMS limits.【F:knowledge/notes/input_part008_review.md†L103-L105】【F:knowledge/notes/input_part003_review.md†L517-L519】
[^8]: Current-balancing guidance for dual-drive builds.【F:knowledge/notes/input_part003_review.md†L449-L449】
[^9]: Logging and calibration workflow (duty-cycle ceilings, GPS alignment).【F:knowledge/notes/input_part003_review.md†L447-L452】【F:knowledge/notes/input_part003_review.md†L451-L452】
[^10]: Battery sag benchmarks on high-power packs.【F:knowledge/notes/input_part003_review.md†L506-L507】
[^11]: BMS cutoff coordination and regen guardrails for commuter packs.【F:knowledge/notes/input_part003_review.md†L517-L519】【F:knowledge/notes/input_part008_review.md†L103-L105】
[^12]: Field-weakening trade-offs on 16–20 S builds.【F:knowledge/notes/input_part003_review.md†L447-L448】【F:knowledge/notes/input_part003_review.md†L184-L184】
[^13]: Traction-control cautions to prevent MOSFET surges.【F:knowledge/notes/input_part003_review.md†L505-L506】【F:knowledge/notes/input_part011_review.md†L475-L477】【F:knowledge/notes/input_part006_review.md†L65-L65】
[^14]: 75100 absolute-current failure case (450–500 A) reinforcing ≤300 A limits.【F:knowledge/notes/input_part003_review.md†L474-L474】
[^15]: Spintend 85/250 firmware clamps and CAN power behavior.【F:knowledge/notes/input_part011_review.md†L456-L458】
[^16]: Tronic X12 firmware limits and overmodulation plans.【F:knowledge/notes/input_part011_review.md†L730-L733】
[^17]: Daly smart-BMS trip voltage and cutoff coordination guidance.【F:knowledge/notes/input_part003_review.md†L519-L519】
[^18]: Regen-induced shutdown anecdotes and advice to keep cutoffs above pack voltage.【F:knowledge/notes/input_part011_review.md†L764-L765】【F:knowledge/notes/input_part011_review.md†L15-L15】
[^19]: Makerbase ignition & throttle ramp tuning advice for sharper launches.【F:knowledge/notes/input_part011_review.md†L726-L728】
[^20]: Phase-lead length and sensorless chatter impacting current delivery.【F:knowledge/notes/input_part009_review.md†L120-L122】
[^21]: Duty-cycle ceiling observations on modern hardware.【F:knowledge/notes/input_part003_review.md†L451-L452】
[^22]: ADC noise, throttle shielding, and USB instability troubleshooting.【F:knowledge/notes/input_part001_review.md†L144-L147】【F:knowledge/notes/input_part001_review.md†L489-L489】
[^23]: Dual 16 S7 P Samsung 50E build logs showing ~140 A pack limits, 70 A per-controller tuning, and the need for supplemental front-mounted airflow.【F:knowledge/notes/input_part001_review.md†L19-L21】
[^24]: VESC real-time power traces exaggerate true battery watts without ≥100 ms filtering—SmartDisplay logging keeps readings honest during high-current tests.【F:knowledge/notes/input_part014_review.md†L2140-L2154】
[^25]: VESC Tool interpolates state-of-charge between 4.2 V and 3.3 V per cell (~66 V empty on 20 S), so riders set cutoffs slightly above their BMS trips to avoid surprise throttling.【F:knowledge/notes/input_part007_review.md†L334-L334】
[^27]: Face de Pin Sucé’s race logs pegged healthy 22 S sag at 4–8 V while warning that >10 V signals trouble; Yamal’s 20 S dual-controller commuter records 10–13 V dips at 200 A per side but keeps pack and ESC temps controlled through active monitoring.【F:knowledge/notes/input_part013_review.md†L702-L702】
[^28]: ’lekrsu’ reiterated that VESC Tool’s state-of-charge percentage is unreliable without Vedder’s own BMS, pushing riders to watch real-time voltage when lowering per-cell cutoffs toward ~3 V.【F:knowledge/notes/input_part013_review.md†L701-L701】
[^fw_bms]: Rob Ver’s Spintend 85/240 logged 35 kW peaks and 132 km/h on 22×3 hubs with ~80 A FW, but a 22 S BMS failure during a 320 A launch still destroyed MOSFETs—reinforcing the need for pack protection when stacking FW on high-current pulls.【F:knowledge/notes/input_part012_review.md†L436-L436】
[^26]: Spintend 85/250 riders holding 22 S builds near 200 A battery / 300 A phase for reliability despite higher firmware ceilings.【F:knowledge/notes/input_part012_review.md†L253-L254】【F:knowledge/notes/input_part012_review.md†L334-L334】
[^80]: Front-controller “local” throttle wiring keeps lever speed sync’d across dual ESCs before CAN propagation.【F:knowledge/notes/input_part014_review.md†L150-L153】
[^phase_equation]: Artem formalised the `I_phase = I_batt × V_batt ÷ V_motor` relationship, reminding tuners that battery amps rise toward the configured limit as ERPM climbs and that output power cannot exceed input watts.【F:knowledge/notes/input_part000_review.md†L3770-L3818】
[^16s35e]: Source: knowledge/notes/input_part000_review.md, line 144.
[^wh_math]: Source: knowledge/notes/input_part000_review.md, line 225.
[^48x_choice]: Source: knowledge/notes/input_part000_review.md, line 226.
[^21700_push]: Source: knowledge/notes/input_part000_review.md, line 227.
[^regen_baseline]: Source: knowledge/notes/input_part000_review.md, line 255.
[^regen_bursts]: Source: knowledge/notes/input_part000_review.md, line 256.
[^tc_heat_2022]: Traction-control heat audit on 20 September 2022 showed Ubox singles running hotter under automated slip control than manual launches, prompting plans for better cooling or softer slip targets during long straights.【F:knowledge/notes/input_part003_review.md†L71-L71】
[^open_loop_burnout]: A 23 September 2022 300 A open-loop burnout destroyed a Rage Mechanics motor, reinforcing the need to ease into duty-cycle sweeps instead of jumping straight to full output without load.【F:knowledge/notes/input_part003_review.md†L72-L72】
[^vsett-pack]: Vsett 10+ riders log the stock 25.6 Ah LG MH1/MJ1 pack sagging and tripping BMS protection above ~60 A despite brief 78 A readings in sport mode.【F:knowledge/notes/input_part002_review.md†L67-L68】
[^vsett-35e]: Artem advised a Vsett 10+ owner on 16 S5 P Samsung 35E cells to hold battery at 40 A, phase 140–150 A (170 A absolute), and regen ≤−17 A to preserve pack health while keeping speed telemetry accurate.【F:data/vesc_help_group/text_slices/input_part002.txt†L2195-L2344】
[^fw-losses]: Field weakening still costs roughly 25 % efficiency and raises current spikes when it engages, explaining sudden heat increases during high-speed pulls.【F:knowledge/notes/input_part002_review.md†L69-L70】
