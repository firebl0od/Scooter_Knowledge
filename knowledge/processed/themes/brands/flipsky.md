# Flipsky Controllers Brand Dossier

## TL;DR
- Budget-friendly VESC hardware that can deliver 20–30 kW peaks, but quality control remains inconsistent and requires hands-on inspection before trust.
- Treat 75100/75200-class units as 300 A absolute-max controllers unless you invest heavily in cooling, QA, and conservative regen ramping.
- Document every change—firmware, wiring, displays, and aux power mods—to survive support escalations and keep commuter builds reliable.

## Bulk Purchasing Playbook
- **Group discount coordination.** Organise one-off bulk orders around Flipsky’s 20 % coupon and be ready to email support for a manual reset when the 24-hour window lapses so late buyers can still join the batch.[^group-buy]
- **Starter kit baseline.** Dual-drive converts typically order two 7550 controllers, the v6 Bluetooth module, CAN harnesses, anti-spark switch for ≥20 S packs, and spare JST looms for halls, throttles, and brakes to cover the first wave of installs.[^starter-kit]
- **Stock the consumables.** XT60/XT90 connectors, JST assortments, and 4–6 mm motor bullets disappear quickly during conversions—have them on the workbench before controllers arrive.[^wiring-supplies]
- **Budget expectations.** Two premium controllers plus VAT and shipping land around €940; remind riders to factor insurance or replacement reserves into the upgrade plan.[^budget-plan]

## Product Line Cheat Sheet
| Model | Nominal System | Community-Validated Envelope | Notes |
| --- | --- | --- | --- |
| 75100 (aluminum board revisions) | 75 V single | ≤80 A battery, ≤270 A phase, ≤300 A absolute; frequent thermal throttling above 80 °C without repasting | Inspect 12 V rail solder joints, note the new 4.5–100 V DC-DC plus GH1.25 harnessing, and repaste the MOSFET pads while hard-mounting the aluminum-backed PCB to the deck.¹ [^21] |
| 75200 / 75200 Pro V2 | 75–84 V dual or single | Disable phase filter, rerun detection with `mxlemming`; start around 50–60 A battery, 120 A phase; regen −5 A battery on commuter hubs | Idle heating and chatter disappear after manual detection plus conservative current caps.² |
| 75350 / 7550 twins | 75 V dual | Comfortable around 60 A battery / 200 A phase per controller when hard-mounted to metal decks | Stock kits pair best with deck-mounted heat spreaders and matched firmware builds.³ |
| 84100 / 85200 variants | 84–100 V single/dual | Field reports stay near 60–80 A battery and ≤135 A phase; higher targets have produced instant failures | Treat datasheet numbers as marketing until community tear-downs confirm component upgrades.⁴ |
| FT85KS ("non-VESC" branch) | 85 V single | Runs Flipsky toolchain but diverges from open-source firmware; validation pending | Expect limited community support and incompatible firmware builds out of the box.⁵ |

## Reliability & Failure Patterns
- **Random early deaths remain common.** Multiple riders still see Flipsky stages fail within weeks—even under modest load—so budget time for burn-in and consider stocking spares before customer deployments.⁶
- **Capacitor banks are a recurring weak link.** Units have dropped to 14 V readings on 20 S packs after repeated capacitor explosions; simple cap swaps rarely hold.⁷
- **Regen cutoffs can brick controllers.** Aggressive negative current spikes triggered logic-board shutdowns on otherwise healthy 75100s; tune regen ramps gently and log results before releasing builds.⁸
- **Hall/5 V rail fragility.** Lost hall detections often trace back to a dead 5 V rail—confirm sensor power after every detection failure.⁹ Mirono’s rotor-short incident on a 4.2 board burned the rail outright, reinforcing the need to secure and insulate hall looms around brake rotors.【F:knowledge/notes/input_part002_review.md†L421-L421】
- **Banggood triple-stack shunts mislead tuning.** Recent V2 shipments arrived with three 2 W shunts piled together and minimal heatsinking; swap to single 0.5 mΩ copper parts and recalibrate carefully or the firmware gains drift and cook the hardware.【F:knowledge/notes/input_part002_review.md†L423-L424】
- **ABS Max overshoot still kills MOSFETs.** Recent autopsies traced 75100 explosions to 190–450 A ABS Max thresholds compounded by weak snubbing; add bus capacitance and avoid relying on BMS cut-outs as safety nets because the resulting voltage spikes torch FETs even without regen. [^22]
- **Plan for thermal upgrades out of the box.** Aluminum-board units survive 200 A phase / 100 A battery bursts only after repacking against the deck with quality paste, airflow, and—on HUASHUO HSP0076A swaps—copper-backed heatsinks that keep die temps from outracing the shell. [^23]
- **Clamp directly to aluminum mass.** Builders chasing 12–16 kW pulls found stacked pads and thick interfaces let the die outrun the case—sand surfaces, spread the thinnest paste film you can, and add heat pipes or larger plates so the enclosure becomes the heat sink. [^24]
- **Compact decks still overheat.** A 75100 shoehorned into a Dualtron Mini thermal-throttled around 75 °C with only 35 A battery available—budget external heatsinks or lower current targets when mounting inside cramped housings.【F:data/vesc_help_group/text_slices/input_part002.txt†L12550-L12558】
- **Voltage telemetry skews low on FW 5.03.** A 20 S build pulling 160 A phase / 110 A battery logged pack voltage several volts under reality, so leave extra margin when tuning near hardware limits until calibration is confirmed.【F:data/vesc_help_group/text_slices/input_part002.txt†L14944-L14966】

## Pre-Flight QA Checklist
1. **Open the enclosure.** Verify 12 V converter solder joints, clean stray shavings, and apply full-coverage thermal pads/paste before the first power-up.¹
2. **Inspect harnesses.** Many aluminum-board units ship with JST-PH/XHB hybrids; map each plug and label replacements before installation day.¹⁰
3. **Log idle current and aux rails.** Confirm the logic stage draws microamps at rest and that any display or PAS accessories respect the servo header’s voltage tolerance.¹¹
4. **Conformal coat selectively.** Spot-protect exposed copper after inspection, but keep pads and connectors serviceable for future repairs.¹²

## Tuning Guardrails
- **Manual detection beats wizard defaults.** Measure Rs/Ls with trusted meters and rerun detection on warmed motors; inaccurate auto-detect values have produced rough starts and ABS faults.¹³
- **Leverage Izuna’s USB toolkit.** The community-packaged bundle flashes the bootloader and 75/100 V firmware over USB so 75100 owners can update without an ST-Link, but plan a multimeter check afterward because V2 boards read roughly 2 V high until you run voltage calibration.[^izuna-toolkit]
- **Match firmware to shunt hardware.** Jaykup’s open-source V2 binaries, Paolo’s “no-limit” releases, and koxx’s Docker build scripts simplify flashing, but only when you pick the correct single- or triple-shunt target—mis-matched gains on Banggood triple-stack shunts have already cooked calibration.【F:knowledge/notes/input_part002_review.md†L422-L424】
- **Disable the phase filter and switch observers.** Flipsky 75200 V2 installs stop idling hot once the phase filter is off, the `mxlemming` observer is active, and phase current is trimmed near 80–120 A.²
- **Cap absolute current at or below 300 A.** Teardown autopsies of 75100 boards that saw 450–500 A absolute ended in toasted MOSFETs—set `ABS Max Current` conservatively and verify logs after every firmware update.¹⁴
- **Exploit the new PCB for sustained current.** The aluminum-backed revision holds roughly 180 A phase / 70 A battery continuous once you bolt it directly to the deck with fresh paste and direct airflow; loose mounting wastes the upgrade. [^21]
- **Balance front/rear outputs.** Dual-drive builds stay predictable when battery and phase currents match across controllers; upping the rear ratio alone can free-spin fronts.¹⁵
- **Respect motor-side limits.** Magic Pie 5 hubs, for example, regained launch torque at ~120 A phase while battery stayed near 25 A—chasing more just overheats the motor.¹⁶

### Suggested Current Targets
| Use Case | Battery Current | Phase Current | Regen (Battery / Phase) | Notes |
| --- | --- | --- | --- | --- |
| 20 S commuter hub (20 mΩ class) | 50–60 A | 100–120 A | −5 A / −40 A | Start here after disabling the phase filter; monitor idle temp.² |
| 16 S mid-power pack (LLT/JBD BMS) | 40 A continuous, 50 A burst | 110–130 A | −7 A / −15 A | Keeps pack and BMS within published limits for 35E/P42A parallels.² ¹³ |
| Dual 75100 sport build | 70–80 A per controller | 220–270 A | −10 A / −60 A | Requires repaste, machined mounts, and aggressive logging.¹¹ ¹⁴ |
| Heavy 3 kW hub swap (Magic Pie, 65H) | 25–40 A | 120–150 A | −5 A / −30 A | Watch for saturation beyond ~150 A; upgrade motors before raising limits.¹⁶ ¹⁷ |

## Ecosystem & Accessories
- **Displays:** The yellow ESP32 “Smart Display” clones work once flashed with SimpleVescDisplay firmware; stock apps remain unstable.⁶ ¹¹
- **Pedal assist & aux controls:** PAS harnesses expect a four-wire split (5 V, GND, signal, brake/enable) with cadence routed to ADC1. Confirm servo-pin voltage limits before powering sensors.¹¹
- **Lighting rails:** Fuse every 12 V accessory lead—shorted aux rails have killed fresh controllers.¹²
- **Cross-brand BLE option:** Spintend’s Bluetooth module plugs straight into the Flipsky UART header, giving riders a drop-in telemetry link when the stock dongle is missing.[^spintend-ble]
- **Profile switching:** Community ESP32 scripts now debounce CAN messages and validate voltage before toggling 1WD/2WD modes; adopt the revised code to avoid divide-by-zero bugs.¹²
- **Power switching:** 75100-class boards ship without a low-voltage enable, so owners run XT90S loop keys or external anti-spark hardware; 20 S packs still arc without real pre-charge, making QS8 connectors or dedicated pre-charge adapters mandatory and pushing some builders toward controllers with onboard latching buttons.[^20]

## When to Reach for Alternatives
- **Need high uptime or warranty responsiveness?** MakerX singles and Spintend duals handle similar current with fewer early failures and better support pipelines.¹⁸
- **Planning >20 S packs or 300 A+ phase?** Rage Mechanics C350, Thor 300, or Tronic X12 platforms offer headroom without relying on unofficial firmware or component swaps.¹⁹
- **Shipping customer builds.** Unless you can burn-in spares and absorb failures, steer production scooters toward controllers with proven QC and documented repair channels.⁶

## Source Notes
[^1]: Converter repair anecdotes, aluminum-board revision notes, and repaste requirements for 75100 units.【F:knowledge/notes/input_part003_review.md†L435-L439】
[^2]: Phase-filter disable, `mxlemming` observer workflow, and commuter current caps for 75200 V2 installs.【F:knowledge/notes/input_part008_review.md†L103-L106】【F:knowledge/notes/input_part009_review.md†L47-L47】
[^3]: MakerX vs. Flipsky current envelopes and heat comparisons on dual installs.【F:knowledge/notes/input_part003_review.md†L470-L474】
[^4]: Field reports on Makerbase/Flipsky 84xxx limits and failures under elevated currents.【F:knowledge/notes/input_part009_review.md†L118-L126】
[^5]: Community skepticism about the FT85KS “non-VESC” controller variant.【F:knowledge/notes/input_part011_review.md†L668-L669】
[^6]: Ongoing QC complaints and display experiments around Flipsky controllers.【F:knowledge/notes/input_part011_review.md†L452-L454】
[^7]: Repeated capacitor explosions and component-quality concerns on 20 S builds.【F:knowledge/notes/input_part011_review.md†L753-L755】
[^8]: Regen-triggered shutdown anecdotes on 75100 hardware.【F:knowledge/notes/input_part011_review.md†L764-L765】
[^9]: Hall-detection failures tied to 5 V rail issues.【F:knowledge/notes/input_part011_review.md†L569-L571】
[^10]: Harness part-number cataloging for aluminum 75100 revisions.【F:knowledge/notes/input_part003_review.md†L520-L520】
[^11]: PAS integration threads and standby-draw measurements on Flipsky hardware.【F:knowledge/notes/input_part011_review.md†L484-L486】【F:knowledge/notes/input_part001_review.md†L913-L916】
[^12]: Aux-rail shorts, conformal-coating practices, and CAN profile-switch debugging notes.【F:knowledge/notes/input_part011_review.md†L723-L724】【F:knowledge/notes/input_part011_review.md†L460-L461】
[^13]: Manual detection guidance and warnings about bad auto-tune values.【F:knowledge/notes/input_part009_review.md†L111-L129】
[^14]: ABS failure case reinforcing the 300 A absolute ceiling.【F:knowledge/notes/input_part003_review.md†L474-L474】
[^15]: Current-balancing advice for dual-drive stability.【F:knowledge/notes/input_part003_review.md†L449-L449】
[^16]: Magic Pie current ratio tuning example on 75100 hardware.【F:knowledge/notes/input_part003_review.md†L508-L508】
[^17]: Saturation discussions and traction-control cautions at high phase currents.【F:knowledge/notes/input_part011_review.md†L475-L477】
[^18]: Comparative MakerX reliability vs. Flipsky on similar amperage builds.【F:knowledge/notes/input_part003_review.md†L470-L470】
[^19]: Spintend 22 S debates and recommendations to step up to C350/Thor-class controllers for higher voltage/current plans.【F:knowledge/notes/input_part011_review.md†L512-L514】
[^20]: Power-switching workarounds for 75100 hardware, including XT90S loop keys, QS8 pre-charge connectors, and preferences for controllers with onboard latching buttons when running dual units.【F:knowledge/notes/input_part001_review.md†L29-L31】
[^21]: Aluminum-backed 75100 revisions add a 4.5–100 V DC-DC stage, GH1.25 harnessing, and hold ~180 A phase / 70 A battery continuous once bolted to the deck with fresh paste and airflow.【F:knowledge/notes/input_part002_review.md†L203-L205】【F:knowledge/notes/input_part002_review.md†L209-L211】
[^22]: ABS Max thresholds near 190–450 A and insufficient snubbing were linked to recent 75100 failures when BMS cut-outs induced voltage spikes.【F:knowledge/notes/input_part002_review.md†L207-L208】
[^23]: HUASHUO HSP0076A retrofits and copper-backed heatsinks kept modified 75100 dies from spiking under 5.5 kW loads once thermal pads/paste were refreshed and airflow improved.【F:knowledge/notes/input_part002_review.md†L209-L210】
[^24]: Community consensus now favours clamping MOSFETs straight to aluminum with the thinnest paste film, larger surface area, and heat pipes when targeting 12–16 kW pulls.【F:knowledge/notes/input_part002_review.md†L211-L212】
[^group-buy]: Coordinated orders leverage Flipsky’s one-time 20 % discount code, which support can manually reopen if the 24-hour window is missed.【F:knowledge/notes/input_part000_review.md†L30-L32】
[^starter-kit]: Community starter list pairs twin 7550 controllers with Bluetooth v6, CAN cabling, anti-spark switches for ≥20 S packs, and spare JST leads for halls, throttle, and brake wiring.【F:knowledge/notes/input_part000_review.md†L31-L33】
[^wiring-supplies]: Builders pre-stock XT60/XT90 plugs, JST assortments, and 4–6 mm motor bullet connectors to keep conversions moving.【F:knowledge/notes/input_part000_review.md†L33-L33】
[^budget-plan]: Expect roughly €940 including VAT for a dual-controller upgrade and plan insurance or reserve funds accordingly.【F:knowledge/notes/input_part000_review.md†L34-L34】
[^izuna-toolkit]: Izuna shared a USB-only toolkit (bootloader + firmware) so Flipsky 75/100 V owners can flash without ST-Link, but 75100 V2 boards still read pack voltage ≈2 V high until you perform calibration in VESC Tool.【F:knowledge/notes/input_part002_review.md†L32-L35】
[^spintend-ble]: When stock BLE dongles are missing, Spintend’s Bluetooth module plugs directly into Flipsky controllers as a drop-in telemetry replacement.【F:knowledge/notes/input_part002_review.md†L35-L35】
