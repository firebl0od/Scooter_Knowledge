# Battery, Phase & Regen Current Mastery

## Why This Guide Exists
Taming current limits is the difference between a scooter that rips for years and one that torches controllers, packs, or riders. The chat logs surface dozens of real-world failures—BMS trips, blown caps, runaway regen—that all trace back to sloppy current planning. This playbook distills the community’s hard-won lessons into a repeatable workflow you can hand to teammates or clients.

## Build Prerequisites
1. **Healthy pack & BMS:** Log internal resistance and balance status before tuning. Parallel packs with mismatched protections can surge into one another when a single BMS trips, so size discharge and regen around the weakest board.¹
2. **Trustworthy wiring & connectors:** QS8/QS10 or AS150-class connectors and 6 mm²+ phase leads are the expectation above ~250 A phase. Revisit solder joints, pad pressure, and thermal interface materials before chasing higher numbers.²
3. **Accurate motor data:** Do not rely on auto-detection when values look suspicious (e.g., ERPM flips, inductance jumps). Measure Rs/Ls with external tools or re-run detection on known-good hardware before editing limits.³
4. **Cooling strategy:** Deck-mounted plates, fresh thermal paste, and airflow matter as much as MOSFET specs. Gutted aluminum cases and machined mounts are the baseline once you exceed 60 A battery.⁴

## Step-by-Step Tuning Workflow
1. **Baseline detection & calibration**
   - Warm the motor and pack, disable the phase filter on Flipsky 75xxx units, and rerun detection with the `mxlemming` observer before touching currents.⁵
   - Validate halls and 5 V rails after detection—many “mystery faults” are just dead sensor power.⁶
2. **Set conservative currents**
   - Start with a 2:1 to 3:1 phase-to-battery ratio (e.g., 40 A battery / 110 A phase on 16 S commuter packs).⁵ ⁷
   - Remember phase amps spike at launch for torque, but battery current is what punishes the BMS—running 150 A phase with 10 A battery feels punchy for a moment yet still respects battery watts, so log both sides of the bridge before chasing headline numbers.【F:knowledge/notes/input_part002_review.md†L675-L676】
   - Match current targets across front/rear controllers to avoid free-spinning the lighter wheel.⁸
   - Treat dual-motor 16 S7 P Samsung 50E packs as roughly 140 A systems: hold each controller near 70 A battery and add ducted airflow up front before nudging limits higher.²³
   - Stock Vsett 10+ packs with 25.6 Ah LG MH1/MJ1 cells still sag hard past ~60 A; repeated 70–80 A sport-mode pulls trigger BMS cut-outs and shorten range even when logs briefly show 78 A success—plan upgrades or derate expectations before cranking limits.【F:knowledge/notes/input_part002_review.md†L67-L68】
   - Artem guides Vsett 10+ owners on 16 S5 P Samsung 35E packs to stay near 40 A battery with 140–150 A phase (170 A absolute) and cap regen around −17 A; the higher current mainly sharpens mid-speed thrust once halls report clean speed data.【F:data/vesc_help_group/text_slices/input_part002.txt†L2195-L2344】
- NKON builders considering 16 S5 P packs are still weighing Samsung 40T against LG M50LT—plan to lab-test M50LT cells around 15 A and keep a high-power discharger handy before trusting the cheaper option.【F:knowledge/notes/input_part002_review.md†L310-L313】
- LG M50T cells continue to disappoint at real-world 10 A limits while the promised 15 A M50LT remains scarce—most Wolf owners now spec P42A/P45B parallels despite the price bump to hold sustained power.【F:data/vesc_help_group/text_slices/input_part002.txt†L8830-L8853】【F:data/vesc_help_group/text_slices/input_part002.txt†L9011-L9016】
- Budget ebike builds still rely on €1.70 LG MH1 cells for lightweight packs, with plans to migrate to 21700 formats once wallets recover—size current limits accordingly.【F:knowledge/notes/input_part002_review.md†L310-L313】
   - Kaabo Wolf owners sketching 20S7P decks (≈160 × 470 × 75 mm) debate JK’s JK-B1A24S-15P active-balancing BMS versus charge-only rigs paired with detachable JK balancers; many settle on a main fuse plus VESC undervoltage cutoffs when discharge FETs will not fit.【F:knowledge/notes/input_part002_review.md†L312-L312】
   - Stock Kaabo 35 S Wolf GT packs shipped with LG M50LT cells that sag like Samsung 50G, pushing riders toward silicone seams, extra wrap layers, and water ingress checks before raising current targets.【F:knowledge/notes/input_part002_review.md†L311-L311】
   - Stock Kaabo 16S5P LG M50T-class packs still yank 150–155 A even when controllers are capped at 60 A each, dropping pack voltage by ~15 V—budget higher-discharge cells or a pack rebuild before chasing more current. 【F:knowledge/notes/input_part002_review.md†L269-L269】
   - Lishen 48X parallels hold roughly 6–7 V sag at 130–150 A (≈14 A per cell) while Samsung 50S stays stable closer to 23 A per cell but costs nearly triple—plan chemistry swaps or parallel counts around the desired current rather than assuming 5 Ah cells can do it all.【F:knowledge/notes/input_part002_review.md†L463-L465】
   - Molicel P42A/P45B parallels stay cooler at 20–25 A than Samsung 50S, but the 50S commands 2–3× the price; plan the chemistry upgrade alongside current goals instead of assuming stock cells will hold. 【F:knowledge/notes/input_part002_review.md†L270-L270】
   - Mooch’s test data pegs Molicel P45B at 4.5 Ah with 50 A burst/35 A continuous capability—expect ~$8 pricing once supply stabilises and remember even 4p Xiaomi packs can flirt with 200 A battery current if deck cooling is improved.【F:knowledge/notes/input_part002_review.md†L313-L313】
   - Frame power as battery volts × amps; phase current only shapes launch torque and will clamp once phase watts exceed what the pack can deliver.【F:knowledge/notes/input_part002_review.md†L69-L69】
   - Keep Artem’s relationship in mind: `I_phase = I_batt × V_batt ÷ V_motor`, so phase torque fades as ERPM climbs—log both currents to confirm your battery caps aren’t starving the tune mid-pull.[^phase_equation]
3. **Log, ride, iterate**
   - Capture VESC Tool live data plus Dragy/GPS logs, note duty-cycle ceilings, and adjust wheel circumference so controller and GPS speeds agree.⁹
   - Watch battery sag and motor temps; if the pack drops >10 % under your target load, reduce battery current or improve the pack.¹⁰
   - Use paired GPS and VESC logs—dual Nucular Vsett 10+ runs confirmed 0–60 km/h in 4.75 s, 0–80 km/h in 7.5 s, and ~10.7 kW draw (78 A rear / 70 A front battery, 200 A/130 A phase), giving you a real benchmark for consistent pulls.【F:knowledge/notes/input_part002_review.md†L96-L98】
   - Cross-check real-time power with an external meter or SmartDisplay—unfiltered VESC telemetry overshoots true watts by 10 kW or more on aggressive pulls.²⁴
   - Treat VESC Tool’s state-of-charge gauge as a rough helper—it linearly maps 4.2–3.3 V per cell (≈66 V on 20 S), so keep your cutoffs a few volts above the BMS trip to prevent surprise throttling once the display reads “empty.”²⁵
4. **Layer in regen**
   - Add regen after forward currents stabilize. Keep battery regen gentler than your discharge target (−5 A to −10 A is plenty for commuter packs) and ramp up slowly to avoid BMS or controller cutoffs.⁵ ¹¹
5. **Optional: field weakening & traction control**
   - Activate FW only once thermals are understood. Expect it to draw nearly the same extra amps you request on both battery and phase channels.¹²
   - On dual drives, enable traction control on the front controller first and monitor for MOSFET surges when grip returns.¹³

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
- **Treat commuter cells gently.** Samsung 35E parallels cope with roughly 1 C regen bursts but degrade quickly under faster charging—keep routine charging near 0.5 C whenever schedules allow.【F:data/vesc_help_group/text_slices/input_part002.txt†L2339-L2344】
- **Spot pack abuse early.** Hammering 16 S5 P Samsung 50G packs to 120 A+ (≈24 A per cell) has melted shrink wrap, tripped BMSes, and spiked controller temps to 70 °C; pivot to higher-discharge cells like P42A/P45B, monitor core temps, and keep charge rates near 1 C to preserve longevity.【F:knowledge/notes/input_part002_review.md†L91-L94】
- **Stagger braking inputs.** Pair mechanical brakes with modest regen; runaway regen has bricked 75100 logic boards when negative current spikes hit unstable hardware.¹⁸
- **Throttle & ramp tuning.** Shorten positive ramp to ~0.1 s and sculpt throttle curves once your current caps are dialed—especially on controllers that feel soft off the line.¹⁹

## Field-Weakening & High-Speed Notes
- Expect only modest top-speed gains (e.g., +8 km/h on 16 S builds) while battery draw jumps from 4 kW to 7 kW. Higher voltage or higher-Kv motors are usually better investments.¹²
- Sensorless chatter and long phase cables exaggerate FW-induced current spikes; keep leads short and add halls where possible.³ ²⁰
- Document duty-cycle ceilings—modern hardware tolerates 98–99 % duty, but stay below 100 % to avoid runaway faults.²¹
- Spintend 85150 hardware has already sacrificed MOSFETs when riders layered 45 A of FW on top of 105/120 A battery and 150/175 A phase at 20 S—budget HY/HSBL swaps or back FW down before chasing higher ERPM. 【F:knowledge/notes/input_part014_review.md†L21-L21】
- Expect roughly 25 % higher losses once field weakening kicks in and be ready for large current spikes during high-speed pulls.【F:knowledge/notes/input_part002_review.md†L70-L70】
- Traction control still needs tuning—enable it on both controllers over CAN, but log case temperature because the current algorithm has doubled controller temps and cut peak power from ~18 kW to ~13 kW on heavy scooters even as it protects front tyres.【F:knowledge/notes/input_part002_review.md†L50-L52】
- PWM experiments dropping zero-vector frequency to 16–20 kHz can feel punchier, yet some riders saw hotter FETs; start around 16–18 kHz and audit DRV temps before chasing high-kV hub gains.【F:knowledge/notes/input_part002_review.md†L72-L74】
- Rob Ver’s 85/240 build touched 35 kW and 132 km/h on 22×3 hubs with ~80 A of FW, yet a 22 S BMS failure during a 320 A launch still blew MOSFETs—treat high-FW pulls as consumable unless pack protection is rock-solid.[^fw_bms]

## Troubleshooting Cheatsheet
| Symptom | Likely Cause | Fix |
| --- | --- | --- |
| Controller idles hot or chatters at low speed | Phase filter enabled, bad detection values | Disable filter, rerun detection with `mxlemming`, verify Rs/Ls manually.⁵ |
| Regen kills power but forward throttle is fine | BMS trip or controller ABS limit too low | Reduce regen, raise ABS max (≤300 A on 75-series), ensure BMS thresholds align.¹⁴ ¹⁸ |
| Phase amps plateau far below target | Motor saturation, long phase leads, or firmware clamp | Shorten leads, add halls, log saturation, or flash no-limit firmware (with cooling).¹² ²⁰ ¹⁶ |
| USB disconnects during hard pulls | ADC noise, poor shielding | Use shielded looms, keep 5 V accessories off logic rails, or log over CAN instead.²² |
| Random controller death after BMS cutoff | Fragile logic rails on Flipsky hardware | Keep cutoff ≥5 V above pack max, avoid sudden pack disconnects, add soft-start contactors.¹⁸ |

## Continuous Improvement
- Maintain a build sheet with firmware versions, connector choices, and current settings for every scooter you service.
- Archive VESC Tool XML profiles alongside ride logs so you can roll back when experiments fail.
- Share postmortems—photos, temperature logs, scope captures—with the community to keep the guardrail table honest.

## Source Notes
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
[^13]: Traction-control cautions to prevent MOSFET surges.【F:knowledge/notes/input_part003_review.md†L505-L506】【F:knowledge/notes/input_part011_review.md†L475-L477】
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
[^fw_bms]: Rob Ver’s Spintend 85/240 logged 35 kW peaks and 132 km/h on 22×3 hubs with ~80 A FW, but a 22 S BMS failure during a 320 A launch still destroyed MOSFETs—reinforcing the need for pack protection when stacking FW on high-current pulls.【F:knowledge/notes/input_part012_review.md†L436-L436】
[^26]: Spintend 85/250 riders holding 22 S builds near 200 A battery / 300 A phase for reliability despite higher firmware ceilings.【F:knowledge/notes/input_part012_review.md†L253-L254】【F:knowledge/notes/input_part012_review.md†L334-L334】
[^phase_equation]: Artem formalised the `I_phase = I_batt × V_batt ÷ V_motor` relationship, reminding tuners that battery amps rise toward the configured limit as ERPM climbs and that output power cannot exceed input watts.【F:knowledge/notes/input_part000_review.md†L3770-L3818】
