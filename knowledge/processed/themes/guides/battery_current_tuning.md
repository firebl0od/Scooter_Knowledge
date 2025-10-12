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
   - Match current targets across front/rear controllers to avoid free-spinning the lighter wheel.⁸
3. **Log, ride, iterate**
   - Capture VESC Tool live data plus Dragy/GPS logs, note duty-cycle ceilings, and adjust wheel circumference so controller and GPS speeds agree.⁹
   - Watch battery sag and motor temps; if the pack drops >10 % under your target load, reduce battery current or improve the pack.¹⁰
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
| Spintend Ubox 85/150 | 20 S duals | 80–100 A | 250–300 A | −12 A / −60 A | Firmware clamps phase ≈350 A; keep within 300 A for reliability.¹⁵ |
| Makerbase 84100 HP | 20 S singles | 60–80 A | ≤135 A | −8 A / −35 A | Higher settings have produced instant failures—treat datasheet peaks as marketing.³ |
| Boutique Tronic X12 | 22–24 S race | 100 A (stock firmware) | 400 A phase, ABS ≈600 A limit | −15 A / −80 A | No-limit firmware lifts ABS but demands extensive cooling and logging.¹⁶ |

## Regen & Braking Best Practices
- **Respect BMS limits.** Daly and ANT boards trip around 2.7 V/cell; match VESC cutoff and regen so the BMS stays ahead of controller protection.¹¹ ¹⁷
- **Stagger braking inputs.** Pair mechanical brakes with modest regen; runaway regen has bricked 75100 logic boards when negative current spikes hit unstable hardware.¹⁸
- **Throttle & ramp tuning.** Shorten positive ramp to ~0.1 s and sculpt throttle curves once your current caps are dialed—especially on controllers that feel soft off the line.¹⁹

## Field-Weakening & High-Speed Notes
- Expect only modest top-speed gains (e.g., +8 km/h on 16 S builds) while battery draw jumps from 4 kW to 7 kW. Higher voltage or higher-Kv motors are usually better investments.¹²
- Sensorless chatter and long phase cables exaggerate FW-induced current spikes; keep leads short and add halls where possible.³ ²⁰
- Document duty-cycle ceilings—modern hardware tolerates 98–99 % duty, but stay below 100 % to avoid runaway faults.²¹
- Spintend 85150 hardware has already sacrificed MOSFETs when riders layered 45 A of FW on top of 105/120 A battery and 150/175 A phase at 20 S—budget HY/HSBL swaps or back FW down before chasing higher ERPM. 【F:knowledge/notes/input_part014_review.md†L21-L21】

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
[^12]: Field-weakening trade-offs on 16–20 S builds.【F:knowledge/notes/input_part003_review.md†L447-L448】【F:knowledge/notes/input_part003_review.md†L24684-L24692】
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
