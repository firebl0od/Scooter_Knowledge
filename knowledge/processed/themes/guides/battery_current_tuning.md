# Battery, Phase & Regen Current Mastery

## Why This Guide Exists

Taming current limits is the difference between a scooter that rips for years and one that torches controllers, packs, or riders. The chat logs surface dozens of real-world failures.
  - BMS trips, blown caps, runaway regen
  - that all trace back to sloppy current planning. This playbook distills the community’s hard-won lessons into a repeatable workflow you can hand to teammates or clients.

## Build Prerequisites

1. **Healthy pack & BMS:** Log internal resistance and balance status before tuning. Parallel packs with mismatched protections can surge into one another when a single BMS trips, so size discharge and regen around the weakest board.¹
2. **Balance capability matters:** Daly smart BMS units only balance at ≈30 mA; fast-charge builds should plan external 4 A balancers and verify you never back-feed the board while it sleeps. JK/LLT hardware remains the go-to when you need stronger balancing, CAN/RS485 logging, or reliable Bluetooth wake-ups.[^1][^2]
3. **ESC cutoffs must exceed BMS trips.** If the controller’s battery cutoff sits below the pack’s protection threshold, the BMS will sever power mid-load.
  - raise VESC cutoffs a few volts so the ESC idles before the pack hard-resets.[^3]
4. **Trustworthy wiring & connectors:** QS8/QS10 or AS150-class connectors and 6 mm²+ phase leads are the expectation above ~250 A phase. Revisit solder joints, pad pressure, and thermal interface materials before chasing higher numbers, remembering that AS150 anti-sparks only tame the initial plug-in arc and do nothing for motor phases, while QS8 discharge leads carrying ~350 A peaks need 6 AWG when a single connector handles the load (8 AWG suffices when the pack splits across two leads).²[^4]
5. **Avoid mismatched parallels:** Keep battery mains single and appropriately sized; short AWG14 leads tolerate ~40 A bursts, but paralleling thin wires or leaving cold solder joints invites uneven current sharing and hotspots. QS8 terminations also demand heavy tips, generous flux, and clean shrink to avoid vibration fatigue.[^5][^6]
6. **Accurate motor data:** Do not rely on auto-detection when values look suspicious (e.g., ERPM flips, inductance jumps). Measure Rs/Ls with external tools or re-run detection on known-good hardware before editing limits.³
7. **Cooling strategy:** Deck-mounted plates, fresh thermal paste, and airflow matter as much as MOSFET specs. Gutted aluminum cases and machined mounts are the baseline once you exceed 60 A battery.⁴
2. **Balance capability matters:** Daly smart BMS units only balance at ≈30 mA; fast-charge builds should plan external 4 A balancers and verify you never back-feed the board while it sleeps. JK/LLT hardware remains the go-to when you need stronger balancing, CAN/RS485 logging, or reliable Bluetooth wake-ups, and JK owners now tighten delta triggers to ≈0.01 V with ~0.2 A active shuttling so 7 p bricks stay aligned without cooking resistors.[^jk-delta]
2. **ESC cutoffs must exceed BMS trips.** If the controller’s battery cutoff sits below the pack’s protection threshold, the BMS will sever power mid-load.
  - raise VESC cutoffs a few volts so the ESC idles before the pack hard-resets.[^3]
3. **Trustworthy wiring & connectors:** QS8/QS10 or AS150-class connectors and 6 mm²+ phase leads are the expectation above ~250 A phase. Revisit solder joints, pad pressure, and thermal interface materials before chasing higher numbers.²
4. **Accurate motor data:** Do not rely on auto-detection when values look suspicious (e.g., ERPM flips, inductance jumps). Measure Rs/Ls with external tools or re-run detection on known-good hardware before editing limits.³
5. **Cooling strategy:** Deck-mounted plates, fresh thermal paste, and airflow matter as much as MOSFET specs. Gutted aluminum cases and machined mounts are the baseline once you exceed 60 A battery.⁴

## Step-by-Step Tuning Workflow

1. **Baseline detection & calibration**
   - Warm the motor and pack, disable the phase filter on Flipsky 75xxx units, and rerun detection with the `mxlemming` observer before touching currents.⁵
   - Validate halls and 5 V rails after detection—many “mystery faults” are just dead sensor power.⁶
- Calibrate handheld IR meters with ~20 mΩ shunts or resistor networks before binning cells; expect fresh P42A near 8 mΩ, Samsung 50S around 10 mΩ, and first-gen 50E in the low-20 mΩ range.
  - absolute values drift but spreads stay useful.[^7]
2. **Set conservative currents**

- Start with a 2:1 to 3:1 phase-to-battery ratio (e.g., 40 A battery / 110 A phase on 16 S commuter packs).⁵ ⁷
- Remember that phase amps spike at low speed for torque while BMS stress follows battery current—150 A phase on 10 A battery feels dramatic but still burns more watt-hours from the pack once controller losses are counted.[^phase_low_speed]
- Vsett 10 riders chasing 20 S performance hold roughly 75/195 A rear and 70/125 A front (battery/phase) while logging ~175 °F windings; lighter 16 S G30 builds still stay under 80 °C at 9–11 kW thanks to a 20 kg weight advantage.[^vsett_dualtron]
- Traction hinges on tyre pressure—~40 psi PMT E-Fire vs. softer slick settings—and field-weakening plus temp sensors are mandatory before exploring 14 kW pulls or dual 90 A battery limits on 20 S tunes.[^traction_checks]
- 16 S 5 P Samsung 35E packs stay healthy around 40 A continuous (50 A bursts) with 110–125 A phase and ABS caps near 180 A; keep regen gentle (~7 A battery / 15 A motor) so commuter cells don’t overheat.[^16s35e]
- Cold-weather logs showed 16 S 6 P LG MJ1 parallels sagging roughly 12 % at 10 A per cell while Samsung 35E strings tolerated the same load with less drop, so riders pick chemistries with winter headroom before raising limits.[^mj1_sag]
- Budget field-weakening draw in your battery limit.
  - real rides show 65 A-limited 6 P packs sagging instantly when FW amps pile on top of throttle demand.[^8]
- Match current targets across front/rear controllers to avoid free-spinning the lighter wheel.⁸
- MakerX vs. Flipsky tuning clinics still steer single-motor riders toward ~60 A battery and 180–200 A phase ceilings until thermal logs prove headroom.[^9]
- Stock Vsett 10+ packs built around 25.6 Ah LG MH1/MJ1 cells stay happiest near 60 A; pushing 70–80 A in sport mode triggers sag, sub-20-mile range, and BMS cut-outs even if short logs show 78 A peaks.[^vsett-pack]
- For 16 S5 P Samsung 35E commuters, Artem caps battery at 40 A (≈150 A phase absolute 170 A) with regen ≤−17 A, noting that extra current only improves mid-speed punch and depends on accurate hall telemetry.[^vsett-35e]
   - Heavy single-motor builds chasing 90 km/h stick near 120 A phase and 80–85 A battery with 16 kHz zero-vector and MTPA enabled; treat those numbers as the practical ceiling without upgraded cooling.[^10]
   - 17 S dual Spintend builds that overheat packs and trims settle around 2×120 A phase, 2×90 A battery, and 2×180 A absolute, while the same chassis on 16 S rides closer to 2×100 A phase and 2×60 A battery once thermal logs dictate the final envelope.[^11]
   - Treat dual-motor 16 S7 P Samsung 50E packs as roughly 140 A systems: hold each controller near 70 A battery and add ducted airflow up front before nudging limits higher.²³
- Calculate pack ESR.
  - including the cells, BMS FETs, harness runs, and nickel busbars
  - before setting current ceilings; nominal voltage × amps ignores the sag you’ll see under load, and LiFePO₄’s flat curve makes coulomb counters more trustworthy than voltage-based gauges.[^12]
- Pair coulomb counters or BMS-integrated amp-hour logs with ride notes so LiFePO₄ commuters see true consumption; the flatter discharge curve hides low-voltage cutoffs until it is too late, whereas coulomb math catches when ESR or wiring losses erode usable capacity.[^12]
- Size packs by watt-hours at the target load, not nominal amp-hours: six parallels of 21700 roughly equal seven 18650s for volume, 12 S of VTC6 matches 13 S of 35E for sag, and Samsung 35E or LG MH1 stay cost-effective under ≈7 A per cell.[^wh_math]
- For 12 S 5 P Xiaomi decks pulling 60–80 A, Samsung 48X or 50G deliver more usable energy at 15 A than P42A while staying cool; Samsung 50E overheats once cell current tops 10–12 A, so reserve it for gentler builds.[^48x_choice]
- 21700 availability and copper busbars now let Tudor’s crew stack 17 S 6 P 40T/50G arrays that tolerate high discharge despite €5–€7 per cell EU pricing.
  - plan current targets around chemistry cost as well as thermal headroom.[^21700_push]
- Molicel P45B still anchors the premium high-current slot, yet plenty of builders stick with cheaper Samsung/LG long-range cells unless they truly need 35–40 A per cell or aggressive fast-charging workflows—proof that chemistry budgets should track the actual current profile, not hype.[^p45b_trade]
- Keep Artem’s relationship in mind: `I_phase = I_batt × V_batt ÷ V_motor`, so phase torque fades as ERPM climbs.
  - log both currents to confirm your battery caps aren’t starving the tune mid-pull.[^phase_equation]
- Rosheee’s 16 S 5 P Samsung 50G experiment already logged ~199 A battery through a 60 A Daly BMS, underscoring how aggressively the crew is pushing 10–12 A-rated cells before migrating to a 20 S 6 P pack.[^50g_abuse]
- Field-weakening still trades efficiency for speed.
  - expect roughly 25 % higher losses and noticeable current spikes once it kicks in, which is why top-speed pulls suddenly heat controllers and packs.[^fw-losses]
- Treat 45 A-per-cell marketing cautiously.
  - P42A/P45B packs live closer to 30–38 A per cell in the real world, and builders rely on temperature probes and potting because scooters rarely sustain full load outside brief 100 km/h pulls.[^13]
   - For daily commuters, finish charges around 90 % if the BMS still balances there—you’ll quadruple pack lifespan versus living at 100 %.[^14]
3. **Log, ride, iterate**

- Capture VESC Tool live data plus Dragy/GPS logs, note duty-cycle ceilings, and adjust wheel circumference so controller and GPS speeds agree.⁹
- Screen-record smart-BMS or XMatic telemetry while you test—Yamal and Yoann log ~286–290 A battery peaks so the crew can vet discharge ceilings without guessing from feel alone.[^xmatic-logging]
- Watch battery sag and motor temps; if the pack drops >10 % under your target load, reduce battery current or improve the pack.¹⁰
- Face de Pin Sucé’s 20 S6 P 40T pack still hit 332 A/21.4 kW, but peaks beyond ~55 A per parallel need to stay under three seconds to avoid runaway sag.[^40t_peaks]
- Pre-heating 20 S packs with 35–40 A charges lifted cell temps toward 45 °C for winter pulls; the same builds reported 8 A chargers couldn’t achieve similar heat soak.[^winter_heat]
- Compare sag against ambient: mild-weather Vsett runs only dropped 6–8 V at 60 A battery while 10 °C packs diving to 325 A lost ~19 V, underlining the need for temperature-adjusted expectations.[^sag_comparison]
- Treat 22 S sag as a health tell: race scooters logging 4–8 V drop under peak load are in the safe zone, while anything beyond ~10 V calls for pack or wiring triage before raising current limits.[^sag-guardrail]
- Cranking `iQ target` for harder launches can still trip pack protection.
  - logs show some BMS boards dropping output to zero when the requested torque outpaces battery capability, so treat that setting as additive load on the cells.[^15]
- Expect extra sag in winter—Mirono logs an additional 3–4 V drop near 1 °C and eases battery current to save range and pack temperature.[^cold-sag]
- NetworkDir’s 72 V race brick still lives at 100–120 A despite 8–10 V droop, proving you can run droopy packs if the BMS thresholds stay clear and logs confirm temps remain under control.[^race-droop]
- Cross-check real-time power with an external meter or SmartDisplay—unfiltered VESC telemetry overshoots true watts by 10 kW or more on aggressive pulls.²⁴
- Remember that phase current alone doesn’t define power; veterans called out logs boasting huge phase amps while battery current stayed flat.
  - energy still comes from pack voltage × battery amps, and PWM waveforms muddy simple √3 conversions, so log both channels before chasing bragging rights.[^16]
- Treat VESC Tool’s state-of-charge gauge as a rough helper.
  - it linearly maps 4.2–3.3 V per cell (≈66 V on 20 S), so keep your cutoffs a few volts above the BMS trip to prevent surprise throttling once the display reads “empty.”²⁵
- Stage controller low-voltage cutoffs above the BMS limit so power tapers before the protection opens; pair that with temp logging on marginal packs so sag-induced heating doesn’t sneak up mid-ride.[^cutoff-margin]
- Use phase-current behaviour as a health check: dual Spintend builds hold 120–130 A phase per motor (≈160 A ABS) happily.
  - if a hub starts stuttering above ~85 A, dig for a blown MOSFET or loose phase lead instead of simply backing off current.[^17]
- Sensorless hubs that bog or howl when phase current crosses ~200 A usually need fresh detection values more than higher current limits.
  - one enduro rider regained speed by trimming inductance targets and re-running detection instead of chasing 550 A phase fantasies.[^18]
4. **Layer in regen**
   - Add regen after forward currents stabilize. Keep battery regen gentler than your discharge target (−5 A to −10 A is plenty for commuter packs) and ramp up slowly to avoid BMS or controller cutoffs.⁵ ¹¹
- Match the pack’s charge hardware before cranking brake force—raise smart-BMS charge limits (e.g., 100 A on JBD boards) and set VESC’s max regen voltage below the pack ceiling so braking wattage doesn’t spike controllers or MOSFETs.[^regen-guardrail]
- ≥21 S packs demand extra headroom.
  - keep regen targets under −50 A and leave a few volts of pack margin to avoid the overvoltage spikes documented on 23 S builds.[^19]
   - Dual-motor commuters start around −30 A battery/−80 A phase on the rear and −25 A/−55 A up front; log stator temps during shakedowns before increasing braking torque.[^regen_baseline]
   - A 10 S 2 P P42A pack still logged 2.55 kW regen spikes and rapid controller heating, so monitor MOSFET and hub temperatures whenever you experiment with aggressive braking profiles.[^regen_bursts]
5. **Optional: field weakening & traction control**
   - Activate FW only once thermals are understood. Expect it to draw nearly the same extra amps you request on both battery and phase channels.¹²
- Treat the extra FW amps as additive to your battery limit.
  - if you budget 100 A battery and add 25 A FW, logs will still show ≈125 A at the pack.[^20]
   - On dual drives, enable traction control on the front controller first and monitor for MOSFET surges when grip returns.¹³
   - September 2022 track work showed traction-control launches heating Ubox singles faster than manual pulls; budget extra heatsinking or relax slip targets during long straights.[^tc_heat_2022]
- Nami tuners treat 12-FET Ubox stacks as reliable only up to roughly 300 A phase / 350 A battery combined.
  - pushing harder has correlated with sudden failures even on fresh hardware.[^21]
   - Pair controller targets with cell capability: 20 S10 P P42A packs can momentarily deliver ~450 A, but sustained draws demand temperature monitoring and margin for pack aging.[^22]

## Hardware Guardrail Table

| Controller | Typical Pack | Battery Current (per controller) | Phase Current | Regen (Battery / Phase) | Notes |
| --- | --- | --- | --- | --- | --- |
| Flipsky 75100 | 16–20 S hubs | 60–80 A | 220–270 A | −10 A / −60 A | Absolute max ≤300 A; repaste and hard-mount before testing.⁴ ¹⁴ |
| Flipsky 75200 Pro V2 | 20 S commuters | 50–60 A | 100–120 A (idle fix), up to 150 A with cooling | −5 A / −40 A | Requires phase-filter disable + `mxlemming` observer to prevent idle heating.⁵ |
| MakerX single (GO-FOC HI100) | 16–20 S duals | 60 A | 200 A | −8 A / −45 A | Runs cooler than equivalent Flipsky hardware when bolted to metal decks.⁴ |
| Spintend Ubox 85/150 | 20–22 S duals | 80–100 A (≈200 A max on 22 S) | 250–300 A | −12 A / −60 A | Firmware clamps phase ≈350 A; community keeps 22 S tunes near 200 A battery / 300 A phase for longevity.¹⁵ ²⁶ |
| Spintend 85250 V2 (early data) | 20–22 S race builds | 175–200 A target until long-term 22 S logs land | 300 A comfortable, 350 A experimental | Match regen to the battery plan | Riders expect the V2 hardware to survive 22 S (~92 V) but are still hunting long-term validation before committing flagship builds.[^85250-v2] |
| Spintend 85/250 cheat sheet | 22 S race scooters | ≈200 A battery baseline (260 A only for testing) | 300 A comfortable, 350 A runs but not “safe” | Match regen to the battery plan | Yamal’s crew treats ≈300 A phase / 200 A battery as the reliable ceiling and logs any 260 A experiments so the reference sheet stays current.[^23]|
| Makerbase 84100 HP | 20 S singles | 60–80 A | ≤135 A | −8 A / −35 A | Higher settings have produced instant failures—treat datasheet peaks as marketing.³ |
| Boutique Tronic X12 | 22–24 S race | 100 A (stock firmware) | 400 A phase, ABS ≈600 A limit | −15 A / −80 A | No-limit firmware lifts ABS but demands extensive cooling and logging.¹⁶ |

## Regen & Braking Best Practices

- **Respect BMS limits.** Daly and ANT boards trip around 2.7 V/cell; match VESC cutoff and regen so the BMS stays ahead of controller protection.¹¹ ¹⁷
- **Treat BMS trips as controller killers.** Mid-ride Daly shutdowns have back-fed voltage spikes into VESC MOSFETs.
  - probe pack voltage before and after disconnects, wake latched boards with a charger, and raise regen thresholds so emergency braking doesn’t exceed the pack’s charge headroom.[^24]
- New 60 A Daly hardware now enforces under/over-current trips mid-ride instead of staying latched on.
  - set firmware ceilings below the fresh hardware thresholds before trusting them on high-speed pulls.[^25]
- **Stagger braking inputs.** Pair mechanical brakes with modest regen; runaway regen has bricked 75100 logic boards when negative current spikes hit unstable hardware.¹⁸
- **Leave regen enabled for lever brakes.** Zeroing battery regen also disables lever-based e-brakes; keep a small negative current target and shape throttle curves inside ADC apps instead.[^26]
- **Throttle & ramp tuning.** Shorten positive ramp to ~0.1 s and sculpt throttle curves once your current caps are dialed—especially on controllers that feel soft off the line.¹⁹
- **Log phase vs. battery regen ratios.** Recent 65 H/85250 builds run ≈90 A phase regen per motor, while Matthew is experimenting with 120 A phase / 20 A battery targets.
  - he’s revisiting those numbers carefully after prior “kabooms” blamed on aggressive negative current limits.[^27]
- **Document regen heuristics from the latest 65 H builds.** Recent 85250 logs show Noname holding ≈90 A phase regen per motor while Matthew experiments with 120 A phase / 20 A battery targets.
  - record the ratios before others repeat the “kabooms” blamed on aggressive negative currents.[^27]

## Pack Protection & Monitoring

- **Running pack-only is risky.** Riders skipping BMS boards to “save space” saw cell drift and failures within months.
  - if you insist on BMS-less packs, log every group, schedule manual balancing, and accept the elevated fire risk.[^28]
- **Charge-only boards aren’t immunity.** Charge-only ANT 40 A stacks still let cells spike toward 40 A each during burnouts, so add temperature sensors and plan manual monitoring before bypassing discharge FETs.[^29]
- **Expect a little ANT drift even in storage.** Owners still see roughly 0.5–0.8 V of pack settle after charging and now use latching throttles or breakers to keep VESC standby draw from draining winter builds.[^ant_settle]
- **Match Daly cutoffs to controller settings.** Field reports put Daly smart-BMS trips near 2.7 V per cell, so align VESC cutoffs to avoid mid-ride brownouts while still protecting the pack.[^daly_cutoff]
- **Respect ANT precharge limits.** The onboard precharge FET taps out near 20 A; add external resistors or buttons for cold starts instead of raising firmware limits and cooking the device.[^30][^31]
- **Wake sleepy BMS boards with a charger.** Happy/Xiaomi protections sometimes latch off after inrush events.
  - tickle the charge port briefly before condemning the controller.[^32]
- **Audit bargain packs before trusting them.** One Amazon 20 S brick stalled at 81.8 V with mixed 4.1/3.8 V groups.
  - proof that low-cost assemblies and bargain chargers can ship wildly unbalanced.[^amazon-pack]

## Charging & Charger Vetting

- Match charger voltage to the pack instead of counting on the battery to drag a higher-voltage supply down; PuneDir’s 16 S build highlighted the CC/CV mismatch risk when trying to charge with an 84 V brick clamped by the BMS.[^charger-mismatch]
- **Adopt gentle charge rates for longevity.** Commuters sip 43.2 Ah packs at ~3 A (≈0.008 C), keep 6 P Molicel bricks under ≈8 A, and focus on limiting cell heat even when math says 0.2 C should be safe.[^slow_charge]
- **Audit adjustable chargers.** The Celler-branded 20 S bench supply landed on voltage with steady thermals, but log fan duty and case temps during long charges before endorsing it for customers.[^33]
- **Replace sketchy 22 S supplies.** Refurbished Meanwell stacks have failed under load.
  - source purpose-built 22 S chargers or vetted lab supplies instead of gambling on patched industrial gear.[^34]
- **Document CC/CV verification for brick chargers.** Stock Wate/YZPOWER units have arrived with sloppy current regulation; meter output current through the constant-current and constant-voltage phases and reject bricks that never taper before 4.2 V per cell.[^cccv_wate]
  - Pair every adjustable bench supply with a pre-charge checklist (wall outlet → charger → pack) so voltage trim mistakes or live-plug arcs do not spike the controller.[^cccv_wate]
- **Isolation test series chargers.** Before stacking power supplies, meter the earth-to-output resistance; only run them in series once you confirm floating outputs and add fuses on both legs.[^35]
- **Acceptance test every bench supply.** Check ground continuity, breaker reset behaviour, and voltage accuracy under load before deploying adjustable chargers to customers.[^36]
- **Label Meanwell-style VR pots.** Adjust VR1 for output voltage, VR2 for current, and VR3 for cutoff while the charger powers a partially discharged pack.
  - always tune under load to avoid overshoot.[^37]
- **Budget time for slow stock chargers.** A 1.75–2 A Zero 10X brick legitimately needs ≈11 hours to refill an 18.2 Ah pack from ~50 V to 54 V.
  - long sessions aren’t automatically a failure sign.[^slow-brick]

## Field-Weakening & High-Speed Notes

- Expect only modest top-speed gains (e.g., +8 km/h on 16 S builds) while battery draw jumps from 4 kW to 7 kW.
  - VSETT 10 telemetry showed ~30 A of field weakening per motor only lifting speed from 69 km/h to ~76 km/h while doubling power draw, so higher voltage or higher-Kv motors remain better investments.¹²[^38]
- Field tests comparing FW vs. pure gearing runs confirmed the efficiency penalty.
  - riders planned October track sessions to validate the trade-off on 16 S builds before committing to new tunes.[^39]
- Sensorless chatter and long phase cables exaggerate FW-induced current spikes; keep leads short and add halls where possible.³ ²⁰
- Document duty-cycle ceilings—modern hardware tolerates 98–99 % duty, but stay below 100 % to avoid runaway faults.²¹
- FW engages on duty cycle, not speed, so it can fire at zero eRPM on hill starts.
  - disable it on commuter packs unless you have current headroom and instrumentation.[^40]
- Bypassed 16 S commuter packs still feel FW amps; keep FW near zero (≤10 A) until pack-current logs prove the cells can absorb the extra draw without sagging below 3.6 V per cell.[^41][^42]
- Riders chasing speed-triggered FW are waiting on firmware hooks.
  - the community wants duty-based FW that delays engagement until the wheel is rolling to prevent hill-start overheating.[^43]
- Spintend 85150 hardware has already sacrificed MOSFETs when riders layered 45 A of FW on top of 105/120 A battery and 150/175 A phase at 20 S.
  - budget HY/HSBL swaps or back FW down before chasing higher ERPM. [^44]
- Rob Ver’s 85/240 build touched 35 kW and 132 km/h on 22×3 hubs with ~80 A of FW, yet a 22 S BMS failure during a 320 A launch still blew MOSFETs.
  - treat high-FW pulls as consumable unless pack protection is rock-solid.[^fw_bms]

## Troubleshooting Cheatsheet

| Symptom | Likely Cause | Fix |
| --- | --- | --- |
| Controller idles hot or chatters at low speed | Phase filter enabled, bad detection values | Disable filter, rerun detection with `mxlemming`, verify Rs/Ls manually.⁵ |
| Motor cooks during bench tests | Open-loop duty-cycle experiments without load | Use gradual ramps; a 300 A open-loop stunt already destroyed a Rage Mechanics motor and highlighted the risk of duty sweeps on bare wheels.[^open_loop_burnout] |
| Regen kills power but forward throttle is fine | BMS trip or controller ABS limit too low | Reduce regen, raise ABS max (≤300 A on 75-series), ensure BMS thresholds align.¹⁴ ¹⁸ |
| Phase amps plateau far below target | Motor saturation, long phase leads, or firmware clamp | Shorten leads, add halls, log saturation, or flash no-limit firmware (with cooling).¹² ²⁰ ¹⁶ |
| Mid-drive e-bike stalls around 16 km/h | Conservative motor-current limits or mismatched ERPM settings | Raise motor current toward ~80 A phase / 20 A battery, verify wheel size/gear ratios, and log duty cycle while watching for BMS cut-outs.[^45] |
| USB disconnects during hard pulls | ADC noise, poor shielding | Use shielded looms, keep 5 V accessories off logic rails, or log over CAN instead.²² |
| Random controller death after BMS cutoff | Fragile logic rails on Flipsky hardware | Keep cutoff ≥5 V above pack max, avoid sudden pack disconnects, add soft-start contactors.¹⁸ |

## Continuous Improvement

- Maintain a build sheet with firmware versions, connector choices, and current settings for every scooter you service.
- Archive VESC Tool XML profiles alongside ride logs so you can roll back when experiments fail.
- Share postmortems—photos, temperature logs, scope captures—with the community to keep the guardrail table honest.

## Source Notes

[^xmatic-logging]: Screen-recording XMatic/smart-BMS telemetry captured ~286–290 A battery peaks for Yoann and Yamal while chasing discharge limits.[^46]
[^jk-delta]: JK smart BMS owners now leave active balancing enabled, tighten delta thresholds to roughly 0.01 V, and cap shuttle current around 0.2 A so even 7 p packs stay aligned without cooking resistors.[^47]
[^cold-sag]: Winter test logs showed 3–4 V of extra sag at 1 °C, so Mirono trims battery amps in the cold to preserve range and pack temperature.[^48]
[^race-droop]: NetworkDir’s 72 V 29.8 Ah race pack still survives 100–120 A pulls despite 8–10 V sag as long as the BMS threshold stays clear and temps remain logged.[^49]
[^cutoff-margin]: Happy Giraffe keeps controller cutoffs above the BMS threshold and logs motor temps so sag-triggered heating doesn’t surprise riders mid-run.[^50]
[^amazon-pack]: Amazon bargain 20 S pack arrived at 81.8 V with mixed 4.1 V/3.8 V groups, proving low-cost assemblies can ship badly unbalanced when chargers/BMSs are cheap.[^51]
[^slow-brick]: Zero 10X owners clock ~11 hours for a 1.75–2 A stock charger to refill an 18.2 Ah pack from ~50 V to 54 V.
  - long charge times alone aren’t proof of pack failure.[^52]
[^cccv_wate]: Charger QA request covering Wate/YZPOWER bricks with sloppy CC/CV behaviour plus the reminder to stage wall → charger → pack when energising adjustable supplies so trim errors do not over-voltage a scooter. Source: data/vesc_help_group/text_slices/input_part005.txt†L24033-L24058; L24046-L24055.
[^1]: Parallel-pack surge warnings when mixed BMS boards trip under load.[^53]
[^mj1_sag]: LG MJ1 vs. Samsung 35E sag comparison at 10 A per cell in 16 S packs.[^66]
[^40t_peaks]: Face de Pin Sucé’s 332 A burst on a 20 S6 P 40T pack and the <3 s guidance for ~55 A-per-parallel peaks.[^90]
[^winter_heat]: Winter pre-heating routine charging 20 S packs at 35–40 A to reach ~45 °C before high-load pulls.[^91]
[^sag_comparison]: Contrasting mild-weather 6–8 V sag at 60 A vs. 19 V drop in 10 °C packs during 325 A launches.[^92]
[^ant_settle]: ANT smart-BMS packs settling 0.5–0.8 V after charge and the recommendation to isolate VESC standby draw with latching switches.[^62]
[^daly_cutoff]: Daly smart-BMS cutoff behaviour around 2.7 V/cell and the need to align VESC limits to prevent brownouts.[^75]
[^2]: Connector and heatsink best practices for high-current builds.[^54][^55]
[^3]: Manual detection workflow and bad auto-tune case studies.[^56]
[^4]: Thermal rework expectations and MakerX vs. Flipsky mounting comparisons.[^57][^58]
[^5]: Phase-filter disable plus `mxlemming` observer fix for Flipsky 75200 V2 idle heating.[^59]
[^6]: Hall-detection failures tied to 5 V rails on Flipsky hardware.[^60]
[^7]: 16 S commuter current baseline (40 A battery / 110 A phase) and BMS limits.[^61][^62]
[^8]: Current-balancing guidance for dual-drive builds.[^63]
[^9]: Logging and calibration workflow (duty-cycle ceilings, GPS alignment).[^64][^65]
[^10]: Battery sag benchmarks on high-power packs.[^66]
[^11]: BMS cutoff coordination and regen guardrails for commuter packs.[^62][^61]
[^12]: Field-weakening trade-offs on 16–20 S builds.[^67][^68]
[^13]: Traction-control cautions to prevent MOSFET surges.[^69][^70][^71]
[^14]: 75100 absolute-current failure case (450–500 A) reinforcing ≤300 A limits.[^72]
[^15]: Spintend 85/250 firmware clamps and CAN power behavior.[^73]
[^16]: Tronic X12 firmware limits and overmodulation plans.[^74]
[^17]: Daly smart-BMS trip voltage and cutoff coordination guidance.[^75]
[^18]: Regen-induced shutdown anecdotes and advice to keep cutoffs above pack voltage.[^76][^77]
[^19]: Makerbase ignition & throttle ramp tuning advice for sharper launches.[^78]
[^20]: Phase-lead length and sensorless chatter impacting current delivery.[^79]
[^21]: Duty-cycle ceiling observations on modern hardware.[^65]
[^22]: ADC noise, throttle shielding, and USB instability troubleshooting.[^80][^81]
[^23]: Dual 16 S7 P Samsung 50E build logs showing ~140 A pack limits, 70 A per-controller tuning, and the need for supplemental front-mounted airflow.[^82]
[^24]: VESC real-time power traces exaggerate true battery watts without ≥100 ms filtering.
  - SmartDisplay logging keeps readings honest during high-current tests.[^83]
[^25]: VESC Tool interpolates state-of-charge between 4.2 V and 3.3 V per cell (~66 V empty on 20 S), so riders set cutoffs slightly above their BMS trips to avoid surprise throttling.[^84]
[^27]: Face de Pin Sucé’s race logs pegged healthy 22 S sag at 4–8 V while warning that >10 V signals trouble; Yamal’s 20 S dual-controller commuter records 10–13 V dips at 200 A per side but keeps pack and ESC temps controlled through active monitoring.[^85]
[^28]: ’lekrsu’ reiterated that VESC Tool’s state-of-charge percentage is unreliable without Vedder’s own BMS, pushing riders to watch real-time voltage when lowering per-cell cutoffs toward ~3 V.[^86]
[^fw_bms]: Rob Ver’s Spintend 85/240 logged 35 kW peaks and 132 km/h on 22×3 hubs with ~80 A FW, but a 22 S BMS failure during a 320 A launch still destroyed MOSFETs.
  - reinforcing the need for pack protection when stacking FW on high-current pulls.[^87]
[^26]: Spintend 85/250 riders holding 22 S builds near 200 A battery / 300 A phase for reliability despite higher firmware ceilings.[^88][^89]
[^80]: Front-controller “local” throttle wiring keeps lever speed sync’d across dual ESCs before CAN propagation.[^90]
[^phase_equation]: Artem formalised the `I_phase = I_batt × V_batt ÷ V_motor` relationship, reminding tuners that battery amps rise toward the configured limit as ERPM climbs and that output power cannot exceed input watts.[^91]
[^16s35e]: Source: knowledge/notes/input_part000_review.md, line 144.
[^wh_math]: Source: knowledge/notes/input_part000_review.md, line 225.
[^48x_choice]: Source: knowledge/notes/input_part000_review.md, line 226.
[^21700_push]: Source: knowledge/notes/input_part000_review.md, line 227.
[^p45b_trade]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24380-L24405
[^regen_baseline]: Source: knowledge/notes/input_part000_review.md, line 255.
[^regen_bursts]: Source: knowledge/notes/input_part000_review.md, line 256.
[^tc_heat_2022]: Traction-control heat audit on 20 September 2022 showed Ubox singles running hotter under automated slip control than manual launches, prompting plans for better cooling or softer slip targets during long straights.[^92]
[^open_loop_burnout]: A 23 September 2022 300 A open-loop burnout destroyed a Rage Mechanics motor, reinforcing the need to ease into duty-cycle sweeps instead of jumping straight to full output without load.[^93]
[^vsett-pack]: Vsett 10+ riders log the stock 25.6 Ah LG MH1/MJ1 pack sagging and tripping BMS protection above ~60 A despite brief 78 A readings in sport mode.[^94]
[^vsett-35e]: Artem advised a Vsett 10+ owner on 16 S5 P Samsung 35E cells to hold battery at 40 A, phase 140–150 A (170 A absolute), and regen ≤−17 A to preserve pack health while keeping speed telemetry accurate.[^95]
[^fw-losses]: Field weakening still costs roughly 25 % efficiency and raises current spikes when it engages, explaining sudden heat increases during high-speed pulls.[^96]


## References

[^1]: Source: data/vesc_help_group/text_slices/input_part004.txt†L16369-L16419
[^2]: Source: data/vesc_help_group/text_slices/input_part004.txt†L18865-L18868
[^3]: Source: knowledge/notes/input_part004_review.md†L311-L311
[^4]: Source: knowledge/notes/input_part005_review.md†L258-L262
[^5]: Source: knowledge/notes/input_part005_review.md†L263-L266
[^6]: Source: knowledge/notes/input_part005_review.md†L267-L271
[^7]: Source: knowledge/notes/input_part004_review.md†L145-L147
[^8]: Source: data/vesc_help_group/text_slices/input_part004.txt†L8000-L8056
[^9]: Source: knowledge/notes/input_part003_review.md†L97-L97
[^10]: Source: knowledge/notes/input_part003_review.md†L100-L100
[^11]: Source: data/vesc_help_group/text_slices/input_part001.txt†L25366-L25439
[^12]: Source: knowledge/notes/input_part006_review.md†L503-L503
[^13]: Source: knowledge/notes/input_part006_review.md†L308-L308
[^14]: Source: knowledge/notes/input_part007_review.md†L307-L307
[^15]: Source: knowledge/notes/input_part006_review.md†L147-L147
[^16]: Source: data/vesc_help_group/text_slices/input_part005.txt†L23317-L23373
[^17]: Source: knowledge/notes/input_part000_review.md†L663-L664
[^18]: Source: knowledge/notes/input_part012_review.md†L15-L15
[^19]: Source: data/vesc_help_group/text_slices/input_part004.txt†L12557-L12583
[^20]: Source: data/vesc_help_group/text_slices/input_part004.txt†L10300-L10305
[^21]: Source: knowledge/notes/input_part012_review.md†L148-L148
[^22]: Source: knowledge/notes/input_part012_review.md†L150-L150
[^23]: Source: data/vesc_help_group/text_slices/input_part012.txt†L15288-L15307
[^24]: Source: knowledge/notes/input_part000_review.md†L356-L356
[^25]: Source: knowledge/notes/input_part003_review.md†L202-L203
[^26]: Source: knowledge/notes/input_part004_review.md†L329-L329
[^27]: Source: data/vesc_help_group/text_slices/input_part012.txt†L13576-L13595
[^28]: Source: data/vesc_help_group/text_slices/input_part004.txt†L9921-L9939
[^29]: Source: knowledge/notes/input_part006_review.md†L311-L311
[^30]: Source: data/vesc_help_group/text_slices/input_part004.txt†L5880-L5893
[^31]: Source: data/vesc_help_group/text_slices/input_part004.txt†L5933-L5940
[^32]: Source: knowledge/notes/input_part004_review.md†L301-L302
[^33]: Source: data/vesc_help_group/text_slices/input_part004.txt†L19666-L19710
[^34]: Source: data/vesc_help_group/text_slices/input_part004.txt†L9300-L9374
[^35]: Source: data/vesc_help_group/text_slices/input_part004.txt†L10020-L10045
[^36]: Source: data/vesc_help_group/text_slices/input_part004.txt†L12090-L12105
[^37]: Source: data/vesc_help_group/text_slices/input_part004.txt†L17519-L17544
[^38]: Source: knowledge/notes/input_part003_review.md†L205-L205
[^39]: Source: knowledge/notes/input_part003_review.md†L75-L75
[^40]: Source: knowledge/notes/input_part004_review.md†L362-L362
[^41]: Source: knowledge/notes/input_part004_review.md†L315-L315
[^42]: Source: knowledge/notes/input_part004_review.md†L386-L386
[^43]: Source: data/vesc_help_group/text_slices/input_part004.txt†L17680-L17718
[^44]: Source: knowledge/notes/input_part014_review.md†L21-L21
[^45]: Source: knowledge/notes/input_part006_review.md†L33-L33
[^46]: Source: knowledge/notes/input_part007_review.md†L108-L108
[^47]: Source: knowledge/notes/input_part007_review.md†L205-L205
[^48]: Source: knowledge/notes/input_part007_review.md†L211-L211
[^49]: Source: knowledge/notes/input_part007_review.md†L212-L212
[^50]: Source: knowledge/notes/input_part007_review.md†L228-L228
[^51]: Source: knowledge/notes/input_part007_review.md†L206-L206
[^52]: Source: knowledge/notes/input_part007_review.md†L225-L225
[^53]: Source: knowledge/notes/input_part008_review.md†L98-L104
[^54]: Source: knowledge/notes/input_part003_review.md†L512-L513
[^55]: Source: knowledge/notes/input_part003_review.md†L496-L497
[^56]: Source: knowledge/notes/input_part009_review.md†L111-L129
[^57]: Source: knowledge/notes/input_part003_review.md†L436-L438
[^58]: Source: knowledge/notes/input_part003_review.md†L470-L474
[^59]: Source: knowledge/notes/input_part008_review.md†L103-L106
[^60]: Source: knowledge/notes/input_part011_review.md†L569-L571
[^sag-guardrail]: Source: knowledge/notes/input_part013_review.md†L702-L702
[^regen-guardrail]: Source: knowledge/notes/input_part013_review.md†L703-L703
[^85250-v2]: Source: knowledge/notes/input_part013_review.md†L710-L710
[^61]: Source: knowledge/notes/input_part008_review.md†L103-L105
[^62]: Source: knowledge/notes/input_part003_review.md†L517-L519
[^63]: Source: knowledge/notes/input_part003_review.md†L449-L449
[^64]: Source: knowledge/notes/input_part003_review.md†L447-L452
[^65]: Source: knowledge/notes/input_part003_review.md†L451-L452
[^66]: Source: knowledge/notes/input_part003_review.md†L506-L507
[^67]: Source: knowledge/notes/input_part003_review.md†L447-L448
[^68]: Source: knowledge/notes/input_part003_review.md†L184-L184
[^69]: Source: knowledge/notes/input_part003_review.md†L505-L506
[^70]: Source: knowledge/notes/input_part011_review.md†L475-L477
[^71]: Source: knowledge/notes/input_part006_review.md†L65-L65
[^72]: Source: knowledge/notes/input_part003_review.md†L474-L474
[^73]: Source: knowledge/notes/input_part011_review.md†L456-L458
[^74]: Source: knowledge/notes/input_part011_review.md†L730-L733
[^75]: Source: knowledge/notes/input_part003_review.md†L519-L519
[^76]: Source: knowledge/notes/input_part011_review.md†L764-L765
[^77]: Source: knowledge/notes/input_part011_review.md†L15-L15
[^78]: Source: knowledge/notes/input_part011_review.md†L726-L728
[^79]: Source: knowledge/notes/input_part009_review.md†L120-L122
[^80]: Source: knowledge/notes/input_part001_review.md†L144-L147
[^81]: Source: knowledge/notes/input_part001_review.md†L489-L489
[^82]: Source: knowledge/notes/input_part001_review.md†L19-L21
[^83]: Source: knowledge/notes/input_part014_review.md†L2140-L2154
[^84]: Source: knowledge/notes/input_part007_review.md†L334-L334
[^85]: Source: knowledge/notes/input_part013_review.md†L702-L702
[^86]: Source: knowledge/notes/input_part013_review.md†L701-L701
[^87]: Source: knowledge/notes/input_part012_review.md†L436-L436
[^88]: Source: knowledge/notes/input_part012_review.md†L253-L254
[^89]: Source: knowledge/notes/input_part012_review.md†L334-L334
[^90]: Source: knowledge/notes/input_part003_review.md†L577-L577
[^91]: Source: knowledge/notes/input_part003_review.md†L578-L578
[^92]: Source: knowledge/notes/input_part003_review.md†L579-L579
[^90]: Source: knowledge/notes/input_part014_review.md†L150-L153
[^91]: Source: knowledge/notes/input_part000_review.md†L3770-L3818
[^92]: Source: knowledge/notes/input_part003_review.md†L71-L71
[^93]: Source: knowledge/notes/input_part003_review.md†L72-L72
[^94]: Source: knowledge/notes/input_part002_review.md†L67-L68
[^phase_low_speed]: Source: knowledge/notes/input_part002_review.md†L17616-L17630
[^vsett_dualtron]: Source: knowledge/notes/input_part002_review.md†L17303-L17405
[^traction_checks]: Source: knowledge/notes/input_part002_review.md†L17413-L17475
[^50g_abuse]: Source: knowledge/notes/input_part002_review.md†L20685-L20700
[^slow_charge]: Source: knowledge/notes/input_part002_review.md†L20002-L20021
[^95]: Source: data/vesc_help_group/text_slices/input_part002.txt†L2195-L2344
[^96]: Source: knowledge/notes/input_part002_review.md†L69-L70
[^charger-mismatch]: Source: knowledge/notes/input_part010_review.md†L445-L446
