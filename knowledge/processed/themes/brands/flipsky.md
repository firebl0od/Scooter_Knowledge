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
| 75100 (aluminum board revisions) | 75 V single | ≤80 A battery, ≤270 A phase, ≤300 A absolute; frequent thermal throttling above 80 °C without repasting | Inspect 12 V rail solder joints and repaste MOSFET pads before loading the unit.¹ |
| 75200 / 75200 Pro V2 | 75–84 V dual or single | Disable phase filter, rerun detection with `mxlemming`; start around 50–60 A battery, 120 A phase; regen −5 A battery on commuter hubs | Idle heating and chatter disappear after manual detection plus conservative current caps.² |
| 75350 / 7550 twins | 75 V dual | Comfortable around 60 A battery / 200 A phase per controller when hard-mounted to metal decks | Stock kits pair best with deck-mounted heat spreaders and matched firmware builds.³ |
| 84100 / 85200 variants | 84–100 V single/dual | Field reports stay near 60–80 A battery and ≤135 A phase; higher targets have produced instant failures | Treat datasheet numbers as marketing until community tear-downs confirm component upgrades.⁴ |
| FT85KS ("non-VESC" branch) | 85 V single | Runs Flipsky toolchain but diverges from open-source firmware; validation pending | Expect limited community support and incompatible firmware builds out of the box.⁵ |

## Reliability & Failure Patterns
- **Random early deaths remain common.** Multiple riders still see Flipsky stages fail within weeks—even under modest load—so budget time for burn-in and consider stocking spares before customer deployments.⁶
- **4.2 hardware taps out early.** Pushing phase current to 150 A on 4.2 boards triggered repeated `fault_code_drv` errors and left BLDC mode as the only fallback, underscoring how quietly MOSFETs degrade when you exceed the published envelope.【F:knowledge/notes/input_part000_review.md†L379-L379】
- **New enclosures still need help.** Upcoming GT100 and revised 75100 enclosures ship with higher-spec Magnachip FETs and tidier cases, yet riders warn performance still hinges on clamping the housing directly to the frame or stripping covers for tighter thermal contact.【F:knowledge/notes/input_part000_review.md†L494-L496】
- **Capacitor banks are a recurring weak link.** Units have dropped to 14 V readings on 20 S packs after repeated capacitor explosions; simple cap swaps rarely hold.⁷
- **Rectangular-case 75100s arrive half-finished.** Shops keep finding floating bus capacitors, dry thermal interfaces, and misreported firmware IDs (HW75300) on the new aluminium enclosures—open every unit, re-torque hardware, add paste, and verify IDs before loading customer profiles.【F:knowledge/notes/input_part004_review.md†L229-L229】
- **Pack cut-offs still brick 75100s.** NetworkDir is now warning Xiaomi Pro 2 owners that BMS-induced shutoffs continue to kill Makerbase/Flipsky 75100s, steering newcomers toward dual Spintend Ubox hardware instead.【F:knowledge/notes/input_part010_review.md†L32-L33】
- Matte continues to see controllers die within a month and Jason lost one to a single hard pull before his Ninebot BMS intervened—treat Flipsky hardware as disposable unless cooling and conservative current limits are dialed.【F:knowledge/notes/input_part011_review.md†L465-L465】
- **Capacitor banks are a recurring weak link.** Units have dropped to 14 V readings on 20 S packs after repeated capacitor explosions; veterans like ‘lekrsu’ and Haku pin the failures on bargain components rather than layout, so simple cap swaps rarely hold.⁷
- **Water-cooled 75350s still need plumbing.** The nose-inlet/optional-pump/rear-outlet loop the plate was designed for keeps heat moving; bolting the cooler onto another spreader starves flow and wastes the upgrade, which is why e-foil builders stick with full loops bathed in 20 °C water.【F:knowledge/notes/input_part006_review.md†L302-L302】
- **Regen cutoffs can brick controllers.** Aggressive negative current spikes triggered logic-board shutdowns on otherwise healthy 75100s; tune regen ramps gently and log results before releasing builds.⁸
- **Inspect the 12 V feed before loading ABS tests.** A cold-soldered auxiliary lead burned the DC/DC on a front-mounted 75100; once reworked the aluminum board survived 270 A phase, 450 A absolute, and 100 A battery pulls—proof that low-voltage joints must be solid before stress testing.【F:data/vesc_help_group/text_slices/input_part003.txt†L9018-L9054】
- **Track hardware revisions.** Riders have already compared at least three aluminum-board revisions and now bolt 75100s directly to machined plates to sustain 270 A phase / 450 A absolute / 100 A battery splits on dual setups.【F:data/vesc_help_group/text_slices/input_part003.txt†L9584-L9604】
- **Repaste before chasing numbers.** Even singles hit ~80 °C until builders redo MOSFET paste/pad stacks and dial battery/phase limits back to respect LLT BMS ceilings.【F:data/vesc_help_group/text_slices/input_part003.txt†L9741-L9750】【F:data/vesc_help_group/text_slices/input_part003.txt†L9747-L9757】
- **Firmware support is community-driven.** Izuna pushed 6.0 beta binaries with custom VESC Tool builds to quiet high-throttle oscillations, coordinating GitHub Actions artifacts for testers rather than waiting on official releases.【F:data/vesc_help_group/text_slices/input_part003.txt†L10460-L10478】
- **Buffer the low-voltage rails.** Riders now treat extra capacitance on the 12 V, 5 V, and even 3.3 V rails as mandatory—Konstantin’s teardown and Mirono’s field fixes both tied the infamous cut-off to undersized caps, and the mod applies even to resin-potted boards.【F:data/vesc_help_group/text_slices/input_part005.txt†L24020-L24070】【F:data/vesc_help_group/text_slices/input_part005.txt†L24662-L24694】
- **Water-cooled resin builds remain experimental.** New potted 75× boards with INA181 current sensors and water loops promise better cut-off behaviour, but veterans still warn that MOSFET-to-heatsink transfer is the bottleneck until someone logs sustained high-power runs.【F:data/vesc_help_group/text_slices/input_part005.txt†L23967-L23995】
- Firmware updates can scramble voltage limits. A commuter chasing 84 V cut-outs confirmed the pack was still 20 S, flashed the no-limit firmware via the PC tool, reset the max input voltage, then reran the input wizard to regain throttle before exploring LCD4 dash integrations.【F:knowledge/notes/input_part011_review.md†L55-L56】
- **Firmware 5.3 introduced a brake-lock scare.** One 75100 flashed to 5.3 locked the wheel at ~45 km/h despite unchanged current limits; double-check UART handbrake scripts, phase insulation, and wiring before road tests after a firmware jump.【F:data/vesc_help_group/text_slices/input_part001.txt†L25875-L25943】
- **Firmware 6.0 remains unstable on 75100 hardware.** Self-compiled VESC 6.0 builds made motors jitter until riders reverted to 5.3 binaries, underscoring that the 75100 still lacks official 6.0 support despite the updated Lisp-based app.【F:data/vesc_help_group/text_slices/input_part002.txt†L11299-L11319】【F:data/vesc_help_group/text_slices/input_part002.txt†L11369-L11379】
- **75100 provenance drama.** Community sleuthing ties the 75100 PCB to a student project that Flipsky allegedly cloned without fixing layout flaws; rumours of the original designer reclaiming rights surfaced after official listings disappeared, even though AliExpress resellers still show stock.【F:data/vesc_help_group/text_slices/input_part001.txt†L10395-L10571】
- **Hall/5 V rail fragility.** Lost hall detections often trace back to a dead 5 V rail—confirm sensor power after every detection failure, especially when rotor hardware can pinch the loom and short the rail outright as Mirono experienced.⁹[^mirono-hall]
- **V2 shunt stacks cook themselves.** Banggood-sourced 75100 V2 boards arrive with triple-stacked 2 W resistors that desolder once phase current climbs; Paolo now swaps in single 0.5 mΩ copper shunts and treats firmware gain recalibration as mandatory to keep readings sane.【F:knowledge/notes/input_part002_review.md†L423-L423】【F:knowledge/notes/input_part002_review.md†L441-L441】
- **Stock firmware isn’t enough.** Fresh V2 hardware keeps failing on acceleration until riders flash vetted binaries matched to the board’s shunt count (Jaykup’s open-source 5.3 build for three-shunt revisions, Paolo’s “no-limit” bin for legacy boards) and monitor temps closely.【F:knowledge/notes/input_part002_review.md†L422-L424】【F:knowledge/notes/input_part002_review.md†L442-L443】
- **Tear-down first, always.** Photos keep showing undersized housings, unsecured bus capacitors, and single-shunt sensing—clean stray solder balls, restake caps with silicone, and consider shunt upgrades before chasing >120 A.[^hardware-audit]
- **QA misses extend beyond electronics.** Replacement controllers have arrived missing faceplate screws or hiding solder beads that later short logic boards; customers ended up machining their own hardware and filing PayPal claims when support stalled, underscoring why every unit needs a full tear-down before power-up.【F:data/vesc_help_group/text_slices/input_part001.txt†L1984-L2176】【F:data/vesc_help_group/text_slices/input_part001.txt†L2182-L2231】
- **7550 capacitor grenades persist.** Fresh hardware has launched capacitors during the very first motor detection even on stock settings—treat “300 A” marketing claims skeptically and bench-burn every controller before field use.【F:data/vesc_help_group/text_slices/input_part001.txt†L9640-L9679】
- **Logic-stage failures crop up without MOSFET damage.** Multiple 7550s have stopped spinning motors despite clean detection traces; vendors traced the issue to dead STM32/USB sections, so budget time for RMA escalation even when power stages look healthy.[^logic_fail]
- **USB tuning crashes.** Several riders traced VESC Tool lockups under load to poor USB isolation on 75100 boards; if tethered sessions trigger faults, fall back to older PC builds or wireless tuning during road tests.【F:data/vesc_help_group/text_slices/input_part001.txt†L21516-L21532】
- **Firmware mismatches plague fresh aluminum boards.** Multiple 75100 ALU units shipped with 75_300_R2 firmware, unwritable voltage limits, ABS overcurrent trips, and BLE dropouts until owners reflashed matching bootloader/firmware pairs, raised max-voltage ceilings, and enabled slow ABS limiters.[^fw_mismatch]
- **Know the MOSFET package.** Flipsky and Makerbase 75200 repairs now confirm Infineon N015N10 TOLL devices on the power stage; hot-air plus preheat (or even an iron) is needed to lift them without tearing pads when replacing cracked parts.【F:data/vesc_help_group/text_slices/input_part004.txt†L7866-L7889】
- **TFT dash pairing remains fragile.** Budget 75100 revisions howl or stall when TFT displays run post-5.02 firmware; builders keep the dashes on 6.0x, juggle UART ports, and rerun motor detection until the combo stops faulting.【F:knowledge/notes/input_part006_review.md†L203-L203】
- **CAN failures can be soft.** Some 75200 builds lost CAN comms but regained function after factory defaults and rerunning detection—try simple resets before swapping hardware.[^can_soft]
- **Loose capacitors fail under vibration.** Repaired 75100s died from unsecured bus caps; stake every capacitor and refuse to power boards outside the 4–20 S window.[^cap_stake]
- **Parameter persistence bugs.** Wattage and regen limits spontaneously reset to 500–700 W on some units until reflashing; suspect flash wear and document write/readback cycles.[^param_persist]
- **Pack-side protections can mimic controller faults.** Scooters that free-spin but die under rider load often have BMS current limits set too low—raise pack capability or relax thresholds before blaming the VESC.[^bms_trip]
- **Sensorless starts need aggressive tuning.** One 7550 only cleared “hashed” torque after phase current climbed toward 90 A, BLDC switching jumped to 20 kHz/35 kHz, and the rider accepted kick-starts around 11 km/h; lingering doubts about shunt or MOSFET health reinforce the brand’s sensorless fragility.[^sensorless_hash]

## Pre-Flight QA Checklist
1. **Open the enclosure.** Verify 12 V converter solder joints, clean stray shavings, and apply full-coverage thermal pads/paste before the first power-up.¹
2. **Inspect harnesses.** Many aluminum-board units ship with JST-PH/XHB hybrids; map each plug and label replacements before installation day.¹⁰
3. **Log idle current and aux rails.** Confirm the logic stage draws microamps at rest and that any display or PAS accessories respect the servo header’s voltage tolerance.¹¹
4. **Conformal coat selectively.** Spot-protect exposed copper after inspection, but keep pads and connectors serviceable for future repairs.¹²

## Tuning Guardrails
- **Stay on the warrantied firmware unless you accept the risk.** Flipsky’s official 100 A battery profile still delivers ~147 A phase bursts but keeps warranty support; the 300 A package voids coverage.[^fw_profiles]
- **Use Izuna’s firmware toolkit for clean flashes.** His 75/100 V bundle covers bootloader, custom .bin, and Xiaomi BLE dash wiring so you can update over USB without ST-Link; follow his calibration checklist immediately after flashing.【F:knowledge/notes/input_part002_review.md†L32-L33】
- **Calibrate pack voltage after flashing.** Fresh 75100 V2 boards often read ~2 V high until you run the calibration routine—cross-check with a multimeter before assuming the firmware is wrong.【F:knowledge/notes/input_part002_review.md†L33-L34】
- **Match firmware to the shunt layout.** Paolo, Jaykup, and koxx now publish separate binaries—and even Docker build images—for single- and triple-shunt V2 hardware; flashing the wrong target skews current limits and invites thermal runaway.【F:knowledge/notes/input_part002_review.md†L422-L423】【F:knowledge/notes/input_part002_review.md†L442-L442】
- **Manual detection beats wizard defaults.** Measure Rs/Ls with trusted meters and rerun detection on warmed motors; inaccurate auto-detect values have produced rough starts and ABS faults.¹³
- **Re-detect before raising current on hub swaps.** 75200 Pro riders chasing >60 A on 65 H hubs killed jerkiness by rerunning the hub template and halving observer gain plus sensorless ERPM targets before lifting limits—treat it as required maintenance whenever firmware or motors change.【F:knowledge/notes/input_part006_review.md†L301-L301】
- **Disable the phase filter and switch observers.** Flipsky 75200 V2 installs stop idling hot once the phase filter is off, the `mxlemming` observer is active, and phase current is trimmed near 80–120 A.²
- **Cap absolute current at or below 300 A.** Teardown autopsies of 75100 boards that saw 450–500 A absolute ended in toasted MOSFETs—set `ABS Max Current` conservatively and verify logs after every firmware update.¹⁴
- **Balance front/rear outputs.** Dual-drive builds stay predictable when battery and phase currents match across controllers; upping the rear ratio alone can free-spin fronts.¹⁵
- **Respect motor-side limits.** Magic Pie 5 hubs, for example, regained launch torque at ~120 A phase while battery stayed near 25 A—chasing more just overheats the motor.¹⁶
- **Field-weakening realities.** FW toggles remain locked to 5.2/5.3 firmware, so plan on SWD flashing beta binaries; BLDC mode is missing entirely on the 75100 branch, and attempting to drop in 75300 images still crashes VESC Tool.[^fw-lockout]
- **Sensorless transitions still hiccup.** Expect a light “tah” or surge as the 75100 swaps to sensorless near 2 000 ERPM; ERPM tweaks alone rarely fix it, so budget time for PID tuning and data logging before declaring a motor fault.【F:data/vesc_help_group/text_slices/input_part001.txt†L1696-L1889】
- **Treat 24 S + field weakening as experimental.** Riders have already blown controllers when regen spikes landed on 24 S packs with FW active; keep FW disabled or derate regen if you insist on running 75100 hardware at that voltage.【F:data/vesc_help_group/text_slices/input_part001.txt†L1699-L1720】【F:data/vesc_help_group/text_slices/input_part001.txt†L1904-L1909】
- **Log faults before rebooting.** When ABS overcurrent trips, run the `faults` command and lift absolute current headroom (200–250 A for 120–130 A phase tunes) instead of power-cycling blindly; noise-induced observer errors hide in those traces.【F:data/vesc_help_group/text_slices/input_part001.txt†L2840-L2872】【F:data/vesc_help_group/text_slices/input_part001.txt†L3796-L3808】
- **Firmware caps remain stubborn.** Community logs still show a ~110 A phase plateau on 75100 hardware even when higher numbers are saved—breaking past it demands firmware rebuilds and shunt/MOSFET mods, so set expectations accordingly.【F:data/vesc_help_group/text_slices/input_part001.txt†L1803-L1857】【F:data/vesc_help_group/text_slices/input_part001.txt†L2093-L2140】【F:data/vesc_help_group/text_slices/input_part001.txt†L2370-L2417】

### Suggested Current Targets
| Use Case | Battery Current | Phase Current | Regen (Battery / Phase) | Notes |
| --- | --- | --- | --- | --- |
| 20 S commuter hub (20 mΩ class) | 50–60 A | 100–120 A | −5 A / −40 A | Start here after disabling the phase filter; monitor idle temp.² |
| 16 S mid-power pack (LLT/JBD BMS) | 40 A continuous, 50 A burst | 110–130 A | −7 A / −15 A | Keeps pack and BMS within published limits for 35E/P42A parallels.² ¹³ |
| Dual 75100 sport build | 70–80 A per controller | 220–270 A | −10 A / −60 A | Requires repaste, machined mounts, and aggressive logging.¹¹ ¹⁴ |
| Heavy 3 kW hub swap (Magic Pie, 65H) | 25–40 A | 120–150 A | −5 A / −30 A | Watch for saturation beyond ~150 A; upgrade motors before raising limits.¹⁶ ¹⁷ |

## Ecosystem & Accessories
- **Spintend BLE modules plug straight in.** When the stock Bluetooth dongle is missing, Spintend’s module drops onto the 75100 header without rewiring, giving builders another telemetry option while they source official replacements.【F:knowledge/notes/input_part002_review.md†L35-L35】
- **Displays:** The yellow ESP32 “Smart Display” clones work once flashed with SimpleVescDisplay firmware; stock apps remain unstable.⁶ ¹¹
<<<<<<< HEAD
=======
- Flipsky’s own yellow ESP32 display remains under evaluation, but riders point to the open-source SimpleVescDisplay firmware as the safer path until the bundle proves itself.【F:knowledge/notes/input_part011_review.md†L466-L466】
- **Upcoming dashboards:** Rage Mechanics previewed a native SmartDisplay UI in late 2022 alongside a 3.5 in navigation prototype and a Waze overlay proof-of-concept for Spintend CAN feeds—plan firmware support before promising customers integrated maps.²¹
- **Mobile app regressions:** Flipsky’s Android app briefly dropped GPS logging on FW 5.3—keep trusted APK archives so you can sideload stable builds when updates regress features.【F:knowledge/notes/input_part003_review.md†L227-L227】
>>>>>>> pr-149
- **Pedal assist & aux controls:** PAS harnesses expect a four-wire split (5 V, GND, signal, brake/enable) with cadence routed to ADC1. Confirm servo-pin voltage limits before powering sensors.¹¹
- **Lighting rails:** Fuse every 12 V accessory lead—shorted aux rails have killed fresh controllers.¹²
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
[^8]: Regen-triggered shutdown anecdotes on 75100 hardware.【F:knowledge/notes/input_part011_review.md†L764-L765】【F:knowledge/notes/input_part011_review.md†L58-L60】
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
[^fw_profiles]: Official 100 A firmware keeps warranty support and still outputs ~147 A phase, whereas the 300 A package voids warranty coverage.【F:knowledge/notes/input_part000_review.md†L42-L42】
[^20]: Power-switching workarounds for 75100 hardware, including XT90S loop keys, QS8 pre-charge connectors, and preferences for controllers with onboard latching buttons when running dual units.【F:knowledge/notes/input_part001_review.md†L29-L31】
[^mirono-hall]: Mirono’s shorted hall harness against a brake rotor killed the 5 V rail on a Flipsky 4.2 and confirmed the boards lack inline protection, reinforcing routing discipline and the need for spares.【F:knowledge/notes/input_part002_review.md†L421-L421】
[^hardware-audit]: Tear-down photos continue to show undersized housings, unsecured capacitors, and single-shunt sensing on 75100 boards—clean solder balls, restake caps with silicone, and plan shunt upgrades before exceeding 120 A.【F:knowledge/notes/input_part001_review.md†L37-L39】
[^fw-lockout]: Field-weakening remains gated to firmware 5.2/5.3 flashed via SWD on 75100 hardware; BLDC mode is disabled and sideloading 75300 images still crashes VESC Tool.【F:knowledge/notes/input_part001_review.md†L33-L35】
[^sensorless-surge]: Sensorless transition chatter, firmware ceilings, and 24 S field-weakening caution all stem from early 2022 rider logs detailing the 75100’s behaviour at 2 000 ERPM, regen-induced voltage spikes, and the hard-coded phase cap near 110 A.【F:data/vesc_help_group/text_slices/input_part001.txt†L1696-L2417】
[^logic_fail]: Flipsky 7550 controllers that lost motor drive despite clean detections were traced to dead STM32/USB logic stages, prompting coordinated vendor follow-up.【F:knowledge/notes/input_part000_review.md†L88-L88】
[^bms_trip]: Load-dependent shut-downs on Flipsky 7550 builds often point to BMS current limits rather than controller faults; successful fixes raise pack capacity or adjust protection thresholds.【F:knowledge/notes/input_part000_review.md†L70-L70】
[^sensorless_hash]: Source: knowledge/notes/input_part000_review.md, lines 193-194.
[^group-buy]: Coordinated orders leverage Flipsky’s one-time 20 % discount code, which support can manually reopen if the 24-hour window is missed.【F:knowledge/notes/input_part000_review.md†L30-L32】
[^starter-kit]: Community starter list pairs twin 7550 controllers with Bluetooth v6, CAN cabling, anti-spark switches for ≥20 S packs, and spare JST leads for halls, throttle, and brake wiring.【F:knowledge/notes/input_part000_review.md†L31-L33】
[^wiring-supplies]: Builders pre-stock XT60/XT90 plugs, JST assortments, and 4–6 mm motor bullet connectors to keep conversions moving.【F:knowledge/notes/input_part000_review.md†L33-L33】
[^budget-plan]: Expect roughly €940 including VAT for a dual-controller upgrade and plan insurance or reserve funds accordingly.【F:knowledge/notes/input_part000_review.md†L34-L34】
[^fw_mismatch]: Flipsky 75100 ALU firmware mismatch issues requiring bootloader and firmware pair reflashing.【F:knowledge/notes/input_part004_review.md†L60-L60】【F:knowledge/notes/input_part004_review.md†L327-L327】
[^can_soft]: Flipsky 75200 CAN communication soft failures resolved with factory defaults.【F:knowledge/notes/input_part004_review.md†L89-L89】
[^cap_stake]: Loose bus capacitors and low-voltage bench test failures on repaired 75100 units.【F:knowledge/notes/input_part004_review.md†L312-L312】
[^param_persist]: Parameter persistence issues with wattage/regen limits resetting on 75100 boards.【F:knowledge/notes/input_part004_review.md†L283-L283】
