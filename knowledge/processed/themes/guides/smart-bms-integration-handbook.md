# Smart BMS Integration Handbook

## Overview

Smart BMS selection and integration is critical for safe, reliable battery operation on electric scooters. This guide compares major BMS families (JK, JBD/LLT, ANT, Daly), covers installation procedures, balancing strategies, and common failure modes. Understanding BMS capabilities and limitations helps you choose appropriate hardware and avoid dangerous failures.

## What You'll Learn

- BMS family comparison (JK, JBD/LLT, ANT, Daly)
- Active vs passive balancing trade-offs
- Proper sizing for voltage and current requirements
- Installation and commissioning procedures
- Charge FET and discharge FET management
- Balancing configuration and monitoring
- Common BMS failures and prevention
- When to choose each BMS type

## 🔧 Related Guides

- [Battery Pack Design](battery_pack_design.md) - Cell selection and pack architecture
- [DIY Battery Sourcing & Welding](diy-battery-sourcing-and-welding.md) - Building custom packs
- [Battery Current Tuning](battery_current_tuning.md) - Setting safe discharge/regen limits
- [Power Distribution](power_distribution.md) - Wiring from BMS to controller

## Key Principles

- Oversize protection hardware and choose the right architecture for the pack: JK active-balancing boards bring dual 7 AWG busbars, 1 A or 2 A shuttling variants, and remote toggles, but recent self-burn reports push installers toward JBD/LLT or ANT units when decks are cramped or uptime is critical.[^1][^1][^2][^3]
- Oversize protection hardware and choose the right architecture for the pack: JK active-balancing boards bring dual 7 AWG busbars, per-channel charge/discharge/balance toggles, and harness-resistance telemetry while still leaving room for GPS/4G trackers once rewired with silicone pigtails, but recent self-burn reports push installers toward JBD/LLT or ANT units when decks are cramped or uptime is critical.[^2][^3][^1][^2][^3]
- Silver-case JK 8 p boards now have a habit of burning the same PCB corner even while idle; builders are shelving them until JK issues a fix.[^jk-silver8p]
- Field failures now include JK dashboards freezing the moment the discharge page opens; builders document the fault, prep JBD harness swaps, and treat JK hardware as a risk unless the pack truly needs its active balancing.[^4]
- Charge-overcurrent trips on JBD-SP17S005 boards can masquerade as undervoltage faults—one crew only solved repeated shutdowns after swapping the BMS and remapping ADC inputs when a controller failure wiped hall sensors.[^jbd_charge_trip]
- JK and ANT families remain the consensus picks for high-current scooters, while Daly stays the “worst in the industry” fallback even if it remains widely available.
  - budget headroom accordingly before committing to bargain hardware.[^5]
- Commission every pack like a high-energy experiment.
  - enable both charge and discharge FETs before regen tests, validate balance-lead order, and log first rides because a single BMS cutoff or miswire has already nuked controllers and power stages that survived normal abuse.[^4][^5][^6]
- JK’s 150 A boards carry thick copper planes and dual 7 AWG leads that soak heat; shops lean on 140 W irons, broad tips, and long preheat cycles so solder actually wets both sides without lifting FET pads.[^jk_rework]
- Treat balancing and calibration as routine maintenance: Daly boards need full charge/discharge learning and higher voltage to balance, while JK hardware wakes via the accessory display, runs active shuttling above ~0.015 V delta, and benefits from monthly thermal/IR audits.[^7][^8][^9]
- Artem’s active-balancing platform begins moving roughly 600 mA as soon as cell delta crosses ≈0.01 V, holding groups within about 3–7 mV during discharge and cutting charge above 4.22 V; give those boards true CC/CV chargers so their safeguards aren’t fighting a brick that never tapers.[^artem_balancer]
- Daly smart boards keep brownout-killing ride packs.
  - multiple crews now reserve them for stationary “powerwall” duty after cheap units drained LiPos to 0 V; pick LLT or JK hardware for scooters that see real current swings.[^6]
- Travel-friendly “5 A” bricks that stay at ~4.3 A all the way to full charge are a last-resort quick-charge option only; swap to adjustable YZPower-style supplies for daily use so a smart BMS isn’t forced to absorb constant-current overflow near 4.2 V per cell.[^cc_only]
- ANT owners still note 0.5–0.8 V pack settling after charge; pair those boards with latching throttles or breakers so VESC standby draw doesn’t drain winter storage scooters.[^7]
- ANT units sip microamps with Bluetooth awake while Daly and LLT boards offer configurable sleep timers; trim status LEDs or use LLT’s hardware switch when parking packs for weeks to stop parasitic drain.[^8]
- Pack size influences BMS choice: high-capacity 53 Ah+ builds stick with JK’s active shuttling for fast charging, smaller commuter packs tolerate ANT’s lighter balancing current, and JBD hardware remains feature-parity with LLT once sensors and harnesses are sized correctly.[^9][^10]
- Pending: Capture which ANT class (250/500 A vs. 600 A surge) Pandalgns blesses for the 20 S 10 P Halo pack after welding and shakedowns so the recommendation section reflects proven loads.[^pandalgns-ant]
- Even 20 S ~7 kW builders asking for smart-BMS ideas keep getting steered back to LLT/JBD units, underscoring how often those boards anchor mid-power packs.[^11]

---

## Selection Matrix (2024–2025 Field Data)

| BMS Family | Typical Continuous / Peak Rating | Strengths Observed in the Field | Known Pitfalls & Mitigations |
| --- | --- | --- | --- |
| **JK Smart (active balancer)** | 150 A / 300 A-class packs with dual 7 AWG busbars | Integrated active charge shuttling (≈600 mA), remote charge/discharge toggles, long-range Bluetooth displays, optional cellular tracker with remote lock support, antispark-friendly architecture, plus new 17 S boards rated 60 A continuous / 100 A burst for tight decks.[^1][^10][^jk_tracker][^jk17s] | Multiple batches have cooked balance resistors or frozen after opening the discharge page; even the compact 17 S unit needs airflow and a contingency plan.
  - stage spare boards or prep a JBD swap before sealing the deck.[^12] |
| **JK Smart (active balancer)** | 150 A / 300 A-class packs with dual 7 AWG busbars | Integrated active charge shuttling, remote charge/discharge toggles, long-range Bluetooth displays, optional cellular tracker with remote lock support, antispark-friendly architecture, and active balancing stages built around large capacitors plus dual 7 AWG busbars.[^13][^1][^10][^jk_tracker] | Multiple batches have cooked balance resistors or frozen after opening the discharge page; the shuttle stage only moves ≈600 mA so weigh the gain over passive boards, keep spares, add airflow for the warm copper planes, and prep harnesses for a JBD swap.[^12] |
| **JK Smart (active balancer)** | 150 A / 300 A-class packs with dual 7 AWG busbars | Integrated active charge shuttling, remote charge/discharge toggles, long-range Bluetooth displays, optional cellular tracker with remote lock support, antispark-friendly architecture.[^1][^10][^jk_tracker] | Balance resistors are burning out in days, support responses range from $8 coupons to RMA demands, and many teams are stockpiling ANT/JBD boards as charge-only fallbacks.
  - tighten delta to ≈0.01 V, keep shuttle current near 0.2 A, add airflow, and be ready to swap the board when it cooks; recent benches even froze a JK the moment the app opened the discharge page.[^14][^4] |
| **ANT Smart** | 200 A (70 mm-wide) to 240 A/600 A surge boards | Compact footprint, app-based current ramp controls, simultaneous cell balancing, proven on Weped FS builds and 20 s 7 p side-mounted packs plus the new 10–32 S/220 A SKU for 20 S scooters.[^3][^12][^13][^ant-32s] | Regen kills controllers if charge FETs stay disabled; app pairing quirks persist, discharge toggles can trip Tronic stages, and the larger units stay awake above ~61 V.
  - budget headroom for 20 S packs that dip below 60 V.[^4][^14][^ant-floor] |
| **JK Smart (active balancer)** | 150 A / 300 A-class packs with dual 7 AWG busbars | Integrated active charge shuttling, remote charge/discharge toggles, long-range Bluetooth displays, optional cellular tracker with remote lock support, antispark-friendly architecture.[^1][^10][^jk_tracker] | Multiple batches have cooked balance resistors or frozen after opening the discharge page; the shuttle stage only moves ≈600 mA so weigh the gain over passive boards, keep spares, add airflow for the warm copper planes, and prep harnesses for a JBD swap.[^12] |
| **ANT Smart** | 200 A (70 mm-wide) to 240 A/600 A surge boards | Compact footprint, app-based current ramp controls, simultaneous cell balancing, proven on Weped FS builds and 20 s 7 p side-mounted packs plus the new 10–32 S/220 A SKU for 20 S scooters; 80 A mini boards suit cramped decks though the advertised 150 A peaks remain suspect versus JK hardware.[^15][^3][^12][^13][^ant-32s] | Regen kills controllers if charge FETs stay disabled; app pairing quirks persist, discharge toggles can trip Tronic stages, and the larger units stay awake above ~61 V.
  - budget headroom for 20 S packs that dip below 60 V.[^4][^14][^ant-floor] |
| **ANT Smart** | 200 A (70 mm-wide) to 240 A/600 A surge boards | Compact footprint, app-based current ramp controls, simultaneous cell balancing, proven on Weped FS builds and 20 s 7 p side-mounted packs plus the new 10–32 S/220 A SKU for 20 S scooters.[^3][^12][^13][^ant-32s] | Regen kills controllers if charge FETs stay disabled; app pairing quirks persist, discharge toggles can trip Tronic stages, and the larger units stay awake above ~61 V.
  - budget headroom for 20 S packs that dip below 60 V and open new batches immediately to confirm connectors and serial logos before dispute windows close.[^4][^14][^ant-floor][^ant-proof] |
| **ANT Smart** | 200 A (70 mm-wide) to 240 A/600 A surge boards | Compact footprint, app-based current ramp controls, simultaneous cell balancing, proven on Weped FS builds and 20 s 7 p side-mounted packs plus the new 10–32 S/220 A SKU for 20 S scooters.[^3][^12][^13][^ant-32s] Halo builders pair the 250/500 A tier with 20 S 10 P P45B packs to survive ~400 A launches without cooking controllers.[^16] | Regen kills controllers if charge FETs stay disabled; app pairing quirks persist, discharge toggles can trip Tronic stages, and the larger units stay awake above ~61 V.
  - budget headroom for 20 S packs that dip below 60 V.[^4][^14][^ant-floor] |
| **ANT Smart (8–20 S stopgap)** | Shares firmware and feature set with higher-voltage boards | Field crews run the larger SKU on 16–20 S packs when the 7–16 S version is out of stock; performance matches expectations aside from suspected MOSFET changes, so monitor temps but treat it as a workable substitute.[^17] | Same precautions as other ANT units: keep charge FETs enabled for regen, verify app pairing after updates, and validate thermal headroom before sustained 20 S discharge. |
| **LLT / JBD (passive)** | 60–100 A continuous in slim 10–17 s shells | Gentle pre-charge that protects controller caps, configurable temp limits, compact housings ideal for tight decks, credible JK alternative when space matters.[^3][^15] | Firmware listings exaggerate series counts; confirm real 21 s ceiling, watch balance current (≈100–160 mA), and document harness pinouts to avoid miswired sense leads.[^15][^16][^17] |
| **Daly Smart** | 35–80 A commuter packs | Cheap, ubiquitous, workable for light-duty commuters once calibrated; some riders still rely on them when better boards won’t fit.[^7][^18] | Balancing often waits for ≥4.18 V per cell, SoC drifts until full cycles are logged, display variants refuse to re-enable discharge after a trip (riders coast on regen to wake them), and harness voltage reads wrong until every lead is connected.
  - derate heavily and monitor cell temps monthly.[^7][^19][^20][^daly_remote][^18] |
| **LLT / JBD (passive)** | 60–100 A continuous in slim 10–17 s shells | Gentle pre-charge that protects controller caps, configurable temp limits, compact housings ideal for tight decks, credible JK alternative when space matters.[^3][^15] | Firmware listings exaggerate series counts; confirm real 21 s ceiling, watch balance current (≈100–160 mA), document harness pinouts to avoid miswired sense leads, and keep a local archive while Jiabaida’s own site remains offline and ambiguous about 22 s support.[^15][^16][^17][^jbd-site] |
| **Daly Smart** | 35–80 A commuter packs | Cheap, ubiquitous, workable for light-duty commuters once calibrated; some riders still rely on them when better boards won’t fit.[^7][^18] | Balancing often waits for ≥4.18 V per cell, SoC drifts until full cycles are logged, and users call failure rates a “casino”.
  - derate heavily and monitor cell temps monthly.[^7][^19][^20] |
| **Charge-only + Active Balancer** | Depends on fuse + controller limits | When space is scarce, builders fuse the main lead, rely on VESC undervoltage, and clip JK balancers across the stack to keep cells aligned without discharge FET losses.[^21] | Requires disciplined fusing and logging because discharge faults no longer open automatically; not suitable where regulatory compliance mandates full protection stages.[^21] |

### VESC Tool Integration Status

- **ANT gap today.** ANT smart BMS lines still lack native VESC Tool support, so telemetry lives in the vendor app until Vedder’s Bridge firmware adds CAN bindings.
  - plan fallbacks for logging and regen validation on ANT-equipped packs.[^ant-gap]
- **Third-party CAN bridges exist.** A plug-in adapter now lets LLT/JBD/Jabada boards stream telemetry over CAN to VESCs, simplifying pack monitoring without rewiring the harness.[^19]
- **Emulator limits.** VESC Tool’s internal SoC emulator is a stopgap for dumb dual-BMS packs; it reads pack voltage and coulomb counts but cannot trip contactors or enforce charge ceilings, so treat it as supplemental telemetry, not protection.[^vesc-emulator]
- **30 S-capable options remain scarce.** PuneDir’s 20 S motorcycle conversion hunt boiled down to ANT’s 30 S board or cascading two JK 15 S units, underscoring how few off-the-shelf BMS choices exist above 24 S.[^20]

Field crews frustrated with Daly’s missing toggles and VAT-laden replacements now default to ANT’s 320 A 20 S board for compact decks.
  - the smoother remote control and tighter packaging justify the price bump when downtime hurts more than hardware cost.[^21]

## Commissioning & Wiring Guardrails

1. **Wake the hardware correctly.** JK boards ship asleep.
  - use the €15 display or a 5–7 V bench supply, confirm charge/discharge toggles, and leave the board powered before sealing the pack; crack new units open first to pluck stray solder beads before they rattle loose in sealed packs.[^22][^8]
   - Expect heavy copper work on 150 A-class JK boards: the dual 7 AWG busbars and thick planes soak heat, so stage ≥140 W irons, broad tips, and patient preheat to avoid delaminating FET pads while you tin leads.[^23]
2. **Validate sense-lead order before soldering B−.** Step through the harness at 3.5 V increments; reversing the negative pair has already cooked resistors on new ANT installs.[^5]
   - When rebuilding tired MH1 packs, log per-parallel rest voltage before landing the harness so the new BMS isn’t blamed for sag that predates the swap.[^24]
- Down-populating 30 S ANT harnesses onto 22 S packs returned bogus telemetry until the crew repinned the balance leads and reconfigured the series count.
  - document the pin swap before sealing the deck so voltage readings stay accurate.[^25]
- ANT’s 30 S smart boards still need the series-count and amp-hour fields set manually inside System Parameters.
  - skipping that step leaves one cell group reading zero even when the harness is wired correctly, and Rogerio’s 22 S pack read as 23 S until he re-entered the series and capacity values using Arnau’s screenshot workflow.[^26][^27][^28]
3. **Keep both FET banks enabled for regen tests.** Builders traced repeated ESC deaths to disabled charge FETs on JK smart boards—regen had nowhere to dump energy.[^4]
*Tip:* ANT’s companion app is live on Apple’s App Store, so iPhone-based teams can configure boards without sideloading tools before sealing the deck.[^29]

- Daly display packs have latched their discharge MOSFETs after cells sag to ≈2.7 V; only the Bluetooth app (password 123456) can reopen them, so plan charger access before sealing the deck and remind riders the LCD power button won’t clear a trip.[^30]
- ANT quietly tucked its charge/discharge toggle behind an “I’m sure” confirmation prompt.
  - show owners where it lives so they can shut packs down without yanking breakers.[^31]
- July 2021-and-newer ANT boards ignore the legacy mobile apps; insist on the refreshed client before handover so config writes actually stick.[^32]
*Reminder:* If a smart BMS was shut down over BLE, tapping it with a charger wakes the board.
  - never “test” with an 84 V charger on 42 V/54.6 V packs or you risk blowing the BMS outright.[^33]
4. **Stage first rides with logging.** Riders lost Spintend and Makerbase controllers the moment a BMS tripped under load; gather current and voltage traces to verify the protection stays latched through braking and launches.[^6]
- **Reboot stubborn JK boards.** After a reset, hold the onboard button until the display wakes—the Wi‑Fi password reverts to `1234`, so update credentials before handing the scooter back.[^jk-reset]

- When regen has previously latched undervoltage faults, enable the smart-BMS discharge MOSFET before reconnecting the controller and raise pre-charge targets toward 40 A on large 16 S packs so startups pass self-tests without brownouts.[^precharge40]
- If smart-BMS telemetry suddenly reads nonsense after a teardown, hunt for conductive debris.
  - metal shavings inside the deck have already scrambled SoC calculations until the harness was cleaned and pack curves recalibrated.[^34]
5. **Load-test bargain externals before trusting telemetry.** Denis’ workshop found “13 Ah” packs sagging instantly, leaving the internal battery carrying the ride.
  - bench suspect modules alone before wiring them into a smart-BMS stack.[^cheap-externals]
5. **Oversize connectors and plan airflow.** High-current boards warm noticeably near their limits.
  - route copper planes into moving air or heatsinks, especially on JK units that reinforce traces with bus rods.[^10] Use the teardown window to snake extra temperature-sensor leads and fresh sleeving between phase bundles so heat doesn’t char insulation later.[^sensor-sleeving]
6. **Treat JK warranty support as minimal.** Burned resistor reports are returning coupon offers, so document failures thoroughly and plan to drop in ANT/JBD replacements rather than waiting on slow RMAs.[^jk-warranty]

- Builders already stage JBD harness adapters after seeing JK boards freeze on the discharge screen even with healthy cell telemetry.
  - plan swap space before sealing the deck.[^4]
7. **Log new delta settings.** Finn’s crews now cap JK shuttle current around 0.2 A and tighten balance delta to roughly 0.01 V so 7 p decks stay aligned without roasting resistors.[^jk-delta-smart]
6. **Confirm advertised series support.** JBD listings still misstate 22 s capability; verify firmware revisions before wiring high-voltage packs.[^16]
7. **Plan controller integration.** VESC Bridge V2 is adding native CAN support for JBD/JK/ANT/Daly boards—map harnesses and firmware early so telemetry stays unified once the hardware ships.[^bridge]
  - Jerome has already opened pre-registration for the next VESC Bridge batch so he can scale the parts order; get on the list if your build schedule depends on those harnesses landing soon.[^bridge-prereg]
8. **Treat discharge-less monitor boards cautiously.** Jason’s 32 S-capable design drops discharge FETs entirely; keep downstream fuses/contactors because the BMS will not open on shorts, and he refuses to bench the ~32 S 3 P prototype (same footprint as a 16 S 6 P stack ≈17 × 4 cells) on a G30 until those protections are installed to avoid catastrophic arcs if a controller fails live.[^35][^no-fet-smart]
9. **Document Daly 400 A logic swaps.** Konstantin’s retrofit pairs a Daly shunt frame with an LLT control board to support four KLS7218 controllers.
  - photograph wiring and note the ≈0.05 mΩ shunt stack before replicating.[^36]
- **Verify CAN bus levels.** A healthy JK/ANT CAN pair sits around a 3.3 V differential.
  - readings near 16 V signal a measurement mistake or wiring fault, not a new voltage spec.[^37]
3. **Spoof Xiaomi data lines when swapping in generic boards.** Replacing an OEM M365/Ninebot BMS with a blank third-party unit requires SHFW or XiaoDash BMS emulation.
  - otherwise the ESC throws error 21 because the data line goes silent. Follow ScooterHacking’s guide before buttoning the pack back up.[^38]
4. **Keep both FET banks enabled for regen tests.** Builders traced repeated ESC deaths to disabled charge FETs on JK smart boards—regen had nowhere to dump energy.[^4]
5. **Stage first rides with logging.** Riders lost Spintend and Makerbase controllers the moment a BMS tripped under load; gather current and voltage traces to verify the protection stays latched through braking and launches.[^6]
6. **Load-test bargain externals before trusting telemetry.** Denis’ workshop found “13 Ah” packs sagging instantly, leaving the internal battery carrying the ride.
  - bench suspect modules alone before wiring them into a smart-BMS stack.[^cheap-externals]
7. **Treat Xiaomi emulators as conservative.** Rita-compatible emulator boards still scream “empty” around 3.4 V per cell even with cutoff configured closer to 2.7 V; keep a manual voltage check or buffer so riders don’t strand themselves following the fake 0 % alert.[^39]
8. **Oversize connectors and plan airflow.** High-current boards warm noticeably near their limits.
  - route copper planes into moving air or heatsinks, especially on JK units that reinforce traces with bus rods.[^10]
9. **Confirm advertised series support.** JBD listings still misstate 22 s capability; verify firmware revisions before wiring high-voltage packs.[^16]
10. **Plan controller integration.** VESC Bridge V2 is adding native CAN support for JBD/JK/ANT/Daly boards.
  - map harnesses and firmware early so telemetry stays unified once the hardware ships.[^bridge]
11. **Treat discharge-less monitor boards cautiously.** Jason’s 32 S-capable design drops discharge FETs entirely; keep downstream fuses/contactors because the BMS will not open on shorts.[^no-fet-smart]

## Happy BMS Field Notes

- **Respect the 44 A ceiling.** Denis reiterated that Happy BMS sustains about 44 A; it trips roughly a second after exceeding that and the onboard fuses pop near 60 A, so don’t plan 50–60 A experiments without redundant protection.[^40]
- **Rebuild packs methodically.** When regrouping odd cell counts (e.g., 39 cells for 13 S3 P), split them into parallel blocks before series connections, follow the official wiring diagram, and land balance leads in order to avoid dangerous cross-wiring.[^41]
- **Wake outputs with a charger.** Fresh installs can read pack voltage yet show no XT60 output until a charger briefly excites the board.
  - connect a supply once before testing discharge paths.[^42]
- **Feed enough charger voltage.** Packs that refuse to charge on Xiaomi bricks usually only see 42 V; swap to ≥47 V CC/CV (or a true 48 V supply) so the BMS actually enables charge FETs.[^43]
- **Expect coulomb-counter saturation.** Pairing a 35 A pack with Happy BMS hardware still works because the controller limits output, but the counter pegs at 0 % with roughly 10 % energy remaining.
  - ride with a manual voltage buffer near empty.[^44]
- **Raise the charge ceiling before using 5 A bricks.** Happy BMS blocks chargers above ~3 A until you increase the limit to about 5.5 A inside the Embedden BMS Tool app, a guardrail meant to keep Xiaomi’s skinny charge leads from overheating.[^45]
11. **Document Daly 400 A logic swaps.** Konstantin’s retrofit pairs a Daly shunt frame with an LLT control board to support four KLS7218 controllers.
  - photograph wiring and note the ≈0.05 mΩ shunt stack before replicating.[^36]

## Regen & Current Budgeting

- **Skip series-stacked BMS boards.** Paolo reminded the crew that the showpiece build they admired actually ran a single controller-side BMS.
  - stacking boards in series is a failure recipe, so stick with one brain or parallel packs with their own protections.[^bms-series-warning]
- **Cap braking currents around the BMS charge envelope.** Community testing now caps regen near 120 A and keeps charge/discharge FETs closed so controllers ride through decel events instead of seeing open-circuit spikes.[^6]
- **Expect Daly discharge FETs to ride through surges.** Riders have logged 180 A+ spikes without tripping Daly hardware, prompting some to bypass discharge stages entirely and rely on VESC undervoltage plus charge-only wiring paired with detachable JK balancers when space is tight.[^46][^47]
- **Treat BMS trips as design failures.** Flipsky 75100s and Wepoor power stages died instantly when the pack opened; prioritize parallel groups, pack cooling, and conservative regen so the BMS never has to intervene.
  - and remember that disabling the charge FET on JK’s common-port boards kills regen and forces the controller into UVP with 72 V log spikes until you re-enable it.[^48][^6]
- **Watch Daly charge MOSFETs during hard braking.** Their charge FETs have flipped mid-regen, momentarily cutting power and nearly pitching riders.
  - raise current thresholds and treat antisparks as safety backups rather than replacements for robust BMS logic.[^49]
- **Inline breakers remain the Daly fallback.** When remote toggles refuse to wake a tripped board, builders have restored output by cycling a physical breaker.
  - plan the mounting space and keep access easy.[^50]
- **Expect ANT boards to hard-cut on faults.** ANT smart units drop pack output entirely during over-voltage or surge events, so AYO runs his 16 S commuter only down to ≈2.9 V per cell to avoid nuisance trips mid-ride.[^ant-cutoff]
- **Log trips before bypassing hardware.** One JK board saved a 20 s conversion by tripping at 60 A when the rider pushed 70 A battery; he’s redesigning the pack instead of defeating the protection.[^jk-trip]
- **Size ANT headroom for big builds.** When speccing 20 S 10 P P42B packs, the crew points riders to the 425 A peak / 170 A continuous ANT shell but reminds them those peak numbers last only a few seconds.
  - treat them as surge limits, not cruise ratings.[^51]
- **Spec replacements when you outgrow 60 A.** The same log calls out bypassing as dangerous.
  - size the next JK/JBD unit for ≥70 A goals and budget the thermal headroom instead of leaving the scooter on a tripped 60 A board.[^52]
- **Treat bypass fires as preventable.** A rear-controller blaze at 35–40 km/h traced directly to a bypassed BMS and missing fuses.
  - document discharge protections and fuse sizing so future builds don’t repeat the mistake.[^53]
- **Plan your upgrade path.** After the fire, Yamal started shopping high-current ANT/JBD options (~US $100) instead of running charge-only boards.
  - use his example when coaching riders off minimal protections.[^54]
- **Retire charge-only boards after brownouts.** Yamal binned a 40 A charge-only BMS after a 35 km/h cutoff and rewired the temp sensors (temp-to-temp, GND-to-GND), underscoring that high-power scooters need full protection stages and tidy harnessing.[^charge_only_swap]
- **Oversize protection for big packs.** Large scooters are already paralleling multiple BMS boards or choosing 200 A-class ANT/JK units even for 70 A packs, proving that headroom beats marketing limits when chasing reliability.[^3][^22]
- **Track sag alongside regen.** Laotie “38 Ah” packs sagged ~10 V under load and tripped riders despite 20 % indicated SoC; log live voltage, adjust cutoffs toward 55 V, and avoid raising current ceilings until the pack is rebuilt.[^laotie-sag]
- **Never parallel Daly packs against open negatives.** Common-port Daly units that momentarily open the discharge loop during regen have already blown controllers.
  - leave discharge paths uninterrupted or disable regen when mixing them with stock batteries.[^55]
- **Don’t bypass the BMS for stealth builds.** A “sleeper” M365 running 20 S 2 P and VESC hardware now relies on manual temp checks after disabling BMS protections.
  - treat that as a last resort and rebuild the pack instead of running without safety cutouts.[^56]

## Balancing & Calibration Practices

- **Map delta thresholds to chemistry.** Experienced builders trigger active balancing around 0.015–0.025 V and cap charge at ~4.15 V when longevity outweighs peak range.[^9]
- **Expect Daly balancing to pause early.** Regen-heavy Daly installs routinely show zero charge current once the dashboard calls the pack “full,” even with ≈0.1 V spread; reseat loose sense leads when 4.9 V ghost readings appear after service.[^ip001-daly-bal][^ip001-ghost-voltage]
- **JK active balancers wake above ≈3.5 V.** JK boards resume shuttling whenever cells sit above roughly 3.5 V with ≥0.1 V delta and idle again below that threshold or on fault, so plan top-off routines around those voltage windows.[^ip001-jk-threshold]
- **Wake new JK boards before sealing packs.** Fresh JK shipments arrive in protection mode; power them with the optional display or a higher-voltage bench supply to enable charge/discharge before buttoning up the enclosure.[^ip001-jk-activation]
- **Tie longevity targets to chemistry.** Samsung 40T packs fall to roughly 70 % capacity after ≈500 full cycles at 4.20 V, while Samsung 48X strings are projected near 3,000 cycles when capped around 4.15 V—reinforcing conservative balance thresholds.[^cycle_life]
- **Audit OEM balance behavior.** Ninebot Max G2 packs with passive bleed resistors stay within ≈5 mV, but Navee N65 batteries wander by ~0.7 V because their protective-only BMS rarely balances.
  - swap to JK active boards when consistency matters.[^57]
- **Memorize per-cell math for quick checks.** Riders divide total pack voltage by the series count (e.g., 22 for 22 S builds) and lean on the familiar 3.1–4.2 V window to translate on-the-fly percentage readouts into actionable per-cell health estimates during tours or diagnostics.[^58]
- **Align top-of-charge with the chemistry’s lifespan.** Samsung 40T packs fall to ~70 % capacity after roughly 500 full cycles at 4.20 V, while Samsung 48X packs stretch toward 3,000 moderate-current cycles if capped closer to 4.15 V.
  - demonstrating the payoff of conservative voltage ceilings.[^59]
- **Expect Daly learning cycles.** Their coulomb-counting SoC meters can show 18 % at 4.07 V per cell until they relearn capacity.
  - run full discharge/charge sessions or manually tag 100 % at top-of-charge so telemetry catches up.[^7]
- **Plan for Daly SoC drift.** Packs have reported 31 % at 3.1 V per cell, so log pack voltage alongside app-reported SoC and lean on external telemetry for range planning.[^60]
- **Exploit active shuttling when available.** Artem’s compact active-balancer keeps cells within roughly 3–7 mV by moving up to 600 mA whenever groups drift more than 0.01 V, and it hard-stops charge above 4.22 V.
  - use those protections if you rely on travel chargers with sloppy CV behaviour.[^61]
- **Exploit active shuttling when available.** Artem’s compact active-balancer keeps cells within roughly 3–7 mV by moving up to 600 mA whenever groups drift more than 0.01 V, and builders now confirm JK shuttles roughly the same current in the field while deciding whether the extra complexity beats passive bleeding; it hard-stops charge above 4.22 V.
  - use those protections if you rely on travel chargers with sloppy CV behaviour.[^61][^4]
- **Expect Daly learning cycles.** Their coulomb-counting SoC meters read low for several rides; plan full discharge/charge sessions or manual 100 % resets so telemetry aligns with reality.[^7]
- **Leverage telemetry displays.** JK screens offer long-range Bluetooth and remote toggles, effectively doubling as pack dashboards on scooters lacking dedicated HUD space.[^10]
- **Schedule thermal/IR checks.** JK smart boards run warm near 60 A; monthly infrared sweeps and rest torque checks catch rising resistance before it snowballs.[^10]
- **Plan for BMS heat.** Copper-reinforced JK boards and Daly charge FETs legitimately warm up around their 60 A envelopes; give them airflow and logging instead of assuming every hot-to-the-touch enclosure signals an imminent failure.[^ip001-bms-heat]
- **Document platform quirks.** Ninebot Max G2 packs balance reliably with passive bleeders (~5 mV delta), while Navee N65 packs can drift 0.7 V because their protection-only BMS rarely equalises.
  - budget JK/ANT retrofits when swapping between the two platforms.[^62]
- **Recalibrate VESC SoC after deck work.** Grinding or drilling inside the deck rains conductive dust onto harnesses; vacuum the bay, flush boards with IPA, and then reset coulomb counters or retune voltage curves (or switch to SmartDisplay dashboards) so telemetry lines up once stray metal no longer fools the BMS.[^63]
  - Run the full contamination checklist afterward: vacuum, wipe with 99 % IPA, and inspect for solder whiskers before powering the pack.[^63]
  - Rebuild the VESC Tool voltage curve (or switch to SmartDisplay/JK dashboards) so SoC follows the refreshed BMS math instead of the dust-contaminated baseline.[^63]
  - Re-zero coulomb counters only after the deck is clean and the pack is charged to the new ceiling; this keeps Daly/JBD learning cycles from drifting further.[^63]
- **Evaluate Bribms drop-ins for rentals.** Paolo’s “Bribms” replacement keeps the Ninebot footprint while adding 15 S support, 50–60 A discharge, 100 mA balancing, and Bluetooth telemetry.
  - handy when upgrading shared-fleet frames without redesigning the deck.[^64]

## Storage & Standby Planning

- **Align controller cutoffs with BMS limits.** Keep VESC input-voltage ceilings ~5 V above pack max so Daly and ANT cutoff events do not nuke controller MOSFETs, and pair ANT boards with latching throttles or breakers to curb 0.5–0.8 V post-charge drift during winter storage.[^65][^66]
- **Know when builders bypass discharge FETs.** High-output scooters still run charge-only 40 A boards and route discharge directly to the pack, accepting manual monitoring because most failures happen while charging.[^67]

## Charging Infrastructure Updates

- **Programmable supplies cover odd voltages.** Adjustable 22 S/18 A bricks paired with ANT sleep timers keep 21 S packs topped without drifting when scooters sit for weeks.[^adj_supply_smart]
- **Carry multi-voltage chargers for travel.** Switchable 16–24 S/20 A units fill gaps when premium 21 S chargers are out of stock, letting one brick service multiple scooter voltages.[^multi_brick_smart]
- **Seek CC/CV bricks with adjustable ceilings.** Riders chasing 95 % state-of-charge targets are standardising on programmable supplies, and one BMS recently caught a CC-only converter stuck at 4.3 A even at full voltage.
  - proof that smart-pack safeguards remain essential.[^68]
- **Lab-adjustable CC/CV bricks are in demand.** Builders are actively sourcing adjustable-voltage telecom chargers so they can cap daily charging around 95 % SOC instead of the default 100 %.[^adj_voltage]
- **Let the BMS police cheap supplies.** A smart pack shut down a bargain CC-only brick that kept pushing 4.3 A at full voltage, underscoring why converters still need supervised sessions and logged protections.[^cc_only_trip]
- **Prep telecom PSUs carefully.** Adjustable 100 V/45 A bricks need earth bonding and should be energised before connecting the scooter charge lead to avoid port-sparking mishaps.[^69]
- **Match pilot resistors on Type 2 adapters.** Swapping the pilot to ~880 Ω brought DIY EVSE dongles online reliably.
  - validate wiring before hitting public posts.[^70]
- **Stretching OEM chargers has limits.** Raising Xiaomi bricks to 61.5 V via trim pots still leaves them as CC-only supplies.
  - upgrade output caps and babysit the cutoff when feeding 15 S packs.[^71]

## Troubleshooting & Service Checklist

- **Document anti-theft workflows.** JK’s remote discharge disable doubles as a parking lock; confirm the board re-arms before rides to avoid brownouts.[^23]
- **Install the optional JK display when range demands visibility.** Its long-range Bluetooth, remote charge/discharge toggles, and granular pack telemetry are saving time on high-current builds and becoming standard issue for field diagnostics.[^72]
- **Log balance behavior after storage.** JK units can self-immolate while idle and Daly boards stop balancing once “full”.
  - review app history after downtime before sending the pack back into service.[^2][^19]
- **Set realistic current ceilings.** Even 20 kW builds lean on JBD smart boards and keep 18S7P Sony VTC6A packs near 200 A to stay inside thermal comfort zones.[^73]
- **Verify advertised current on boutique boards.** Jiabada’s 230 A/575 A peak smart BMS pairs cleanly with dual Spintend 80100 controllers, but its dual-sided heatsinks still need isolation plates so they never touch nearby cells.[^jiabada]
- **Fix false low-cell alarms at the source.** ANT 22 S boards flag phantom 2.3 V cells until the harness order and full parameter set are confirmed in the app; circulate the official wiring diagrams and APK when in-app updates stall so owners can reload firmware and clear the warning.[^74][^75]
- **Match TVS replacements carefully.** When GEE-branded TVS diodes fail on ANT boards, Smart Repair substitutes Vishay’s SMCJ12A to restore a 12 V clamp without altering the layout.[^76]
- **Teach recovery procedures.** Publish lead-order diagrams and wake-up checklists so drained JK packs (≈57 V on 20 s) or JBD miswires don’t strand riders without telemetry.[^17][^24]
- **Exploit Daly Bluetooth toggles for safe shutdowns.** The Daly Bluetooth companion app can open outputs without sparks, giving antispark-free builds a tidy way to de-energise harnesses when parking.[^77]
  - the same app can reboot a tripped pack in situ—handy when you cannot disconnect VESCs or balancers.[^daly_reset]
- **Reseat suspect balance leads.** A single cold joint on Artem’s JK install forced the board into alternating “short circuit” and “low voltage” alarms until the tap was reflowed.
  - inspect and re-solder every lead after high-heat work before blaming firmware.[^78][^3]
- **Log mixed-pack behaviour.** Luis’ Wolf Warrior tripped a smart BMS at 115 A while running a 10 S 10 P MJ1 pack in parallel with a 6 P MH1, proving that mismatched chemistries leave little headroom for current spikes and complicate fault tracing.[^mixed_packs]
- **Celebrate near-misses.** Another builder shorted pack leads during a connector swap and walked away because the BMS tripped instantly.
  - keep charge/discharge protections active during experiments.[^connector_trip]
- **Escalate when firmware toggles misbehave.** ANT app glitches that trip discharge FETs or JK UIs that freeze mid-session warrant immediate vendor contact and a fallback BMS plan.[^11][^14]
- **Replace burnt input stages instead of bypassing.** If a mis-plugged harness leaves only ~7 V at the output despite healthy cell groups, assume the BMS input stage cooked and swap the board.
  - bridging fuses after XT90-saver incidents risks runaway faults.[^79]

---

## Source Notes

[^1]: JK smart BMS hardware ships with dual 7 AWG busbars, active balancing, and remote charge/discharge toggles alongside long-range displays.[^80][^81]
[^2]: Field reports detail JK balance resistors burning and boards freezing after opening the discharge page, pushing riders toward alternatives and prompting advice to keep spares ready.[^82]
[^3]: Builders oversize protection.
  - pairing 200 A ANT/JK boards with 70 A packs or fitting 240 A ANT hardware into side-mounted 20 s builds
  - highlighting reliability-driven headroom choices.[^83][^84]
[^4]: JK users traced repeated controller deaths to disabled charge FETs before regen tests, underscoring the need to keep both FET banks active.[^85]
[^5]: Miswired negative sense leads on an ANT install cooked components, reinforcing step-by-step voltage validation before soldering B−.[^86]
[^6]: BMS cutoffs have killed controllers mid-ride, and the community now caps regen near 120 A while logging early shakedowns to ensure protections stay latched.[^87][^88][^89]
[^bms-series-warning]: Paolo warned that stacking BMS units in series is asking for failure.
  - the admired build in question actually used a single controller-side BMS.[^90]
[^7]: Daly smart boards rely on coulomb counting, demand ≥4.18 V to balance, and frequently misreport SoC (e.g., 18 % at 4.07 V) until relearn cycles complete.[^91][^92]
[^8]: JK packs ship in protection mode; installers wake them with a display or bench supply, toggle outputs, and leave the board energized before sealing the enclosure.[^93]
[^9]: Active-balancer veterans target 0.015–0.025 V delta triggers and conservative 4.15 V charge ceilings to balance longevity with usable capacity.[^94]
[^10]: JK boards reinforce traces with copper rods, run warm near their 60 A comfort zone, and provide remote telemetry screens for high-power scooters.[^95][^96]
[^sensor-sleeving]: Yoann reopened his pack to route new temperature-sensor wiring and add extra sleeving between phase leads so the bundle sheds heat instead of cooking insulation.[^97]
[^jk-warranty]: NetworkDir’s JK warranty case yielded only an $8 coupon and a return request after the board burned, so the chat now tells newcomers to skip JK orders and prep replacements.[^98]
[^jk-delta-smart]: Finn’s crew leaves JK active balancing enabled, tightens delta to ~0.01 V, and limits shuttle current to ~0.2 A so 7 p modules stay aligned without roasting resistors.[^99]
[^11]: Recent JK batches self-destructed even while idle or during basic app interactions, earning community warnings to prep JBD swaps as insurance.[^82]
[^jk-silver8p]: Source: knowledge/notes/input_part007_review.md†L408-L408
[^12]: ANT hardware’s simultaneous balancing and compact footprint have proven reliable on long-lived Weped FS packs despite high peak currents.[^100]
[^precharge40]: Source: knowledge/notes/input_part000_review.md, line 170.
[^13]: Side-mounted Vsett builds demonstrate ANT’s 240 A/600 A board fitting alongside controllers, validating the form factor for cramped decks.[^84]
[^14]: ANT discharge toggles and firmware glitches have bricked controllers during commissioning, so riders double-check app states after updates and stage regen conservatively.[^101]
[^ant-pinout]: ANT balance harness pinouts change between the 10 S boards and higher-series hardware; installers keep a screenshot archive before repinning or upgrading to the 425 A/170 A shell to avoid miswiring.[^102][^103]
[^ant-threshold]: ANT riders now match CellHighProtect/Recover to their dash warning voltages so the pack trips and resets exactly where the cockpit already demands a recharge.[^104]
[^ant-cutoff]: ANT BMS trips cut output entirely—AYO runs his 16 S commuter down only to ≈2.9 V per cell to avoid sudden shutdowns mid-ride.[^105]
[^ant-downpopulate]: Down-populating a 30 S ANT BMS onto a 22 S harness returned bogus cell voltages until the builder documented the pin swaps and reconfigured the app for the shorter stack.[^25]
[^ant-32s]: Smart Repair flagged ANT’s new 10–32 S/220 A smart BMS as a viable option when 7–20 S models sell out, giving 20 S scooters fresh inventory to pull from.[^106]
[^ant-floor]: The same thread notes the larger ANT units stay awake above ≈61.2 V, so 20 S packs that dip below 60 V need extra headroom or a different BMS if they expect deep discharge protection.[^107]
[^ant-proof]: Official ANT store promos now ship 20–22 S boards as low as €35–80 but with revised connectors, temp probes, or missing serial logos, so open the case for photos and verification before dispute windows close.[^108]
[^pandalgns-ant]: Pending confirmation of which ANT class Pandalgns approves for the 20 S 10 P Halo pack once welding and shakedown testing finish. Source: knowledge/notes/input_part011_review.md†L914-L914
[^15]: LLT/JBD smart boards earn praise for compact housings, gentle pre-charge, and configurable protections, giving builders a slimmer alternative to JK hardware.[^109]
[^16]: Community members caution that JBD firmware listings overstate maximum series counts.
  - verify the real 21 s ceiling before wiring high-voltage packs.[^110]
[^jbd_limit]: Jiabaida’s own site dropped offline while a “6–22 S” listing quietly documented only 6–21 S support, reinforcing the need to confirm firmware limits before trusting new-stock boards.[^111]
[^jbd-site]: Jiabaida’s storefront remains offline and the ambiguous “6–22 s” product page leaves real series support unclear.
  - archive docs locally until the vendor returns.[^112]
[^jiabada]: Gabe is pairing Jiabada’s 230 A/575 A peak smart BMS with dual Spintend 80100s and QS8 connectors, isolating the dual-sided heatsinks from nearby cells to keep the pack safe.[^113]
[^17]: Harness diagrams and recovery guides remain in demand because miswired JBD/ANT balance leads are a recurring failure point during repairs.[^114]
[^18]: Budget builds continue to rely on Daly smart boards when higher-end options will not fit, accepting the trade-offs for commuter duty.[^115]
[^19]: Daly units often stop balancing once “full,” and riders derate them heavily after repeated over-discharge failures, treating the platform as a gamble.[^116]
[^20]: Monthly IR checks and conservative charge currents help detect rising resistance after Daly-class thermal trips.[^117]
[^21]: Kaabo Wolf builders documented charge-only BMS layouts fused at the main lead while clipping JK active balancers across the stack when discharge FET space was unavailable.[^118]
[^22]: Large motorcycle-class scooters now parallel multiple BMS boards so 20 s 24 p packs can share hundreds of amps safely.[^119]
[^ant-gap]: ANT smart BMS owners still rely on the vendor app because VESC Tool has no native integration yet, leaving CAN telemetry on the roadmap for Bridge/firmware updates.[^120]
[^vesc-emulator]: Riders lean on VESC Tool’s internal BMS emulator to estimate state of charge on dumb dual-BMS packs after entering nominal voltage/capacity, but it cannot close contactors or enforce charge limits.[^121]
[^laotie-sag]: Laotie “38 Ah” packs logged ~10 V sag under load and stranded riders at 52 V despite 20 % indicated SoC; they now log real voltage, raise cutoffs toward 55 V, or plan pack rebuilds before upping current.[^122]
[^23]: JK’s app-controlled discharge disable doubles as an anti-theft toggle once the pack is charged, a workflow riders now bake into parking habits.[^123]
[^24]: Recovery checklists cover JK low-voltage wake-ups around 57 V on 20 s packs and balance-lead troubleshooting so riders don’t lose telemetry after servicing.[^124][^125]
[^jk-reset]: Source: knowledge/notes/input_part007_review.md†L409-L409
[^bridge]: VESC Bridge V2 documentation promises plug-and-play harnesses plus future JK/JBD/ANT/Daly support, making it easier to integrate smart BMS telemetry with controller dashboards once released.[^126]
[^cheap-externals]: Denis’ workshop found cheap “13 Ah” externals sagging immediately, forcing the primary battery to supply all current.
  - test them solo at low load before wiring them into parallel stacks or trusting their telemetry.[^127]
[^no-fet-smart]: Jason’s 32 S-capable BMS board removes discharge FETs entirely, so downstream fusing/contactors remain the only short-circuit protection.[^128]
[^charge_only_swap]: Source: knowledge/notes/input_part012_review.md, line 439.
[^mixed_packs]: Source: knowledge/notes/input_part000_review.md, line 311.
[^connector_trip]: Source: knowledge/notes/input_part000_review.md, line 312.
[^jk-trip]: A JK smart BMS tripped at ~60 A on a C80 build when the rider demanded 70 A battery, proving the protection works and prompting a pack redesign instead of bypassing the board.[^129]
[^jk_tracker]: JK’s optional cellular tracker module adds SIM-powered remote locking, though the module is bulky enough that owners plan for shrink-wrap pockets or inductive charging to avoid tearing packs open.[^130]
[^jbd_charge_trip]: Source: data/vesc_help_group/text_slices/input_part011.txt, L21209 to L21280; L21236 to L21266; L21245 to L21260
[^jk17s]: Source: knowledge/notes/input_part000_review.md, line 319.
[^adj_supply_smart]: Adjustable 22 S/18 A supplies paired with ANT sleep timers keep 21 S packs topped without drifting during long parking stretches.[^131]
[^multi_brick_smart]: Switchable 16–24 S/20 A chargers substitute for premium 21 S bricks when inventory dries up, giving one travel charger for multiple scooter voltages.[^132]
[^ant-latch]: ANT’s 470 A/1050 A smart BMS latched its discharge FETs after an overnight charge and ignored output toggles until a full reset and inspection, underscoring the need for redundant protection when pushing Spintend-class power levels.[^133]
[^daly_remote]: Source: knowledge/notes/input_part000_review.md, line 316.


## References

[^1]: Source: data/vesc_help_group/text_slices/input_part001.txt†L10630-L10922
[^2]: Source: knowledge/notes/input_part000_review.md†L619-L620
[^3]: Source: knowledge/notes/input_part000_review.md†L690-L690
[^4]: Source: knowledge/notes/input_part007_review.md†L329-L334
[^5]: Source: knowledge/notes/input_part009_review.md†L372-L372
[^6]: Source: knowledge/notes/input_part005_review.md†L223-L223
[^7]: Source: data/vesc_help_group/text_slices/input_part003.txt†L16080-L16102
[^8]: Source: data/vesc_help_group/text_slices/input_part003.txt†L7690-L7712
[^9]: Source: data/vesc_help_group/text_slices/input_part003.txt†L10726-L10767
[^10]: Source: data/vesc_help_group/text_slices/input_part003.txt†L11610-L11612
[^11]: Source: knowledge/notes/input_part006_review.md†L49-L49
[^12]: Source: knowledge/notes/input_part007_review.md†L305-L307
[^13]: Source: data/vesc_help_group/text_slices/input_part001.txt†L21264-L21305
[^14]: Source: knowledge/notes/input_part007_review.md†L205-L214
[^15]: Source: data/vesc_help_group/text_slices/input_part002.txt†L2758-L2792
[^16]: Source: knowledge/notes/input_part011_review.md†L46-L46
[^17]: Source: knowledge/notes/input_part000_review.md†L738-L740
[^18]: Source: knowledge/notes/input_part000_review.md†L516-L520
[^19]: Source: knowledge/notes/input_part006_review.md†L404-L404
[^20]: Source: data/vesc_help_group/text_slices/input_part009.txt†L20355-L20374
[^21]: Source: knowledge/notes/input_part000_review.md†L554-L554
[^22]: Source: data/vesc_help_group/text_slices/input_part001.txt†L10630-L10768
[^23]: Source: knowledge/notes/input_part001_review.md†L568-L569
[^24]: Source: knowledge/notes/input_part005_review.md†L420-L422
[^25]: Source: knowledge/notes/input_part009_review.md†L403-L403
[^26]: Source: knowledge/notes/input_part013_review.md†L268-L268
[^27]: Source: knowledge/notes/input_part013_review.md†L281-L281
[^28]: Source: knowledge/notes/input_part013_review.md†L310-L314
[^29]: Source: knowledge/notes/input_part010_review.md†L182-L183
[^30]: Source: knowledge/notes/input_part000_review.md†L368-L368
[^31]: Source: knowledge/notes/input_part000_review.md†L578-L578
[^32]: Source: knowledge/notes/input_part000_review.md†L579-L579
[^33]: Source: knowledge/notes/input_part006_review.md†L140-L140
[^34]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24123-L24169
[^35]: Source: knowledge/notes/input_part011_review.md†L43-L45
[^36]: Source: data/vesc_help_group/text_slices/input_part003.txt†L17062-L17078
[^37]: Source: knowledge/notes/input_part011_review.md†L410-L417
[^38]: Source: knowledge/notes/denis_all_part02_review.md†L79-L80
[^39]: Source: knowledge/notes/denis_all_part02_review.md†L402-L402
[^40]: Source: knowledge/notes/denis_all_part02_review.md†L322-L323
[^41]: Source: knowledge/notes/denis_all_part02_review.md†L374-L375
[^42]: Source: knowledge/notes/denis_all_part02_review.md†L374-L376
[^43]: Source: knowledge/notes/denis_all_part02_review.md†L396-L397
[^44]: Source: knowledge/notes/denis_all_part02_review.md†L399-L401
[^45]: Source: knowledge/notes/denis_all_part02_review.md†L476-L476
[^46]: Source: data/vesc_help_group/text_slices/input_part002.txt†L8785-L8810
[^47]: Source: data/vesc_help_group/text_slices/input_part002.txt†L10603-L10654
[^48]: Source: knowledge/notes/input_part000_review.md†L621-L621
[^49]: Source: knowledge/notes/input_part000_review.md†L369-L369
[^50]: Source: knowledge/notes/input_part000_review.md†L580-L580
[^51]: Source: knowledge/notes/input_part009_review.md†L343-L343
[^52]: Source: knowledge/notes/input_part012_review.md†L327-L327
[^53]: Source: knowledge/notes/input_part012_review.md†L378-L379
[^54]: Source: knowledge/notes/input_part012_review.md†L379-L379
[^55]: Source: knowledge/notes/input_part000_review.md†L581-L581
[^56]: Source: knowledge/notes/input_part011_review.md†L358-L359
[^57]: Source: knowledge/notes/input_part005_review.md†L362-L366
[^58]: Source: knowledge/notes/input_part009_review.md†L328-L328
[^59]: Source: knowledge/notes/input_part001_review.md†L501-L502
[^60]: Source: knowledge/notes/input_part000_review.md†L370-L370
[^61]: Source: knowledge/notes/input_part000_review.md†L716-L723
[^62]: Source: knowledge/notes/input_part005_review.md†L375-L377
[^63]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24124-L24167
[^64]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24621-L24629
[^65]: Source: data/vesc_help_group/text_slices/input_part003.txt†L16080-L16113
[^66]: Source: data/vesc_help_group/text_slices/input_part003.txt†L21224-L21247
[^67]: Source: knowledge/notes/input_part006_review.md†L214-L214
[^68]: Source: knowledge/notes/input_part001_review.md†L504-L506
[^69]: Source: knowledge/notes/input_part003_review.md†L141-L141
[^70]: Source: knowledge/notes/input_part003_review.md†L135-L135
[^71]: Source: knowledge/notes/input_part003_review.md†L142-L142
[^72]: Source: knowledge/notes/input_part001_review.md†L558-L560
[^73]: Source: knowledge/notes/input_part006_review.md†L239-L239
[^jk_rework]: Source: knowledge/notes/input_part001_review.md†L568-L570
[^adj_voltage]: Source: knowledge/notes/input_part001_review.md†L504-L505
[^cc_only_trip]: Source: knowledge/notes/input_part001_review.md†L506-L506
[^cycle_life]: Source: knowledge/notes/input_part001_review.md†L502-L503
[^74]: Source: knowledge/notes/input_part011_review.md†L357-L366
[^75]: Source: knowledge/notes/input_part011_review.md†L366-L374
[^76]: Source: knowledge/notes/input_part011_review.md†L352-L354
[^77]: Source: data/vesc_help_group/text_slices/input_part002.txt†L9452-L9459
[^daly_reset]: Source: knowledge/notes/input_part003_review.md†L528-L528
[^78]: Source: knowledge/notes/input_part000_review.md†L650-L650
[^79]: Source: data/vesc_help_group/text_slices/input_part001.txt†L9186-L9191
[^80]: Source: knowledge/notes/input_part001_review.md†L470-L488
[^81]: Source: knowledge/notes/input_part001_review.md†L560-L560
[^82]: Source: knowledge/notes/input_part007_review.md†L175-L280
[^83]: Source: knowledge/notes/input_part008_review.md†L12-L21
[^84]: Source: knowledge/notes/input_part008_review.md†L489-L503
[^85]: Source: knowledge/notes/input_part007_review.md†L27-L27
[^86]: Source: knowledge/notes/input_part008_review.md†L135-L135
[^87]: Source: knowledge/notes/input_part011_review.md†L15-L62
[^88]: Source: knowledge/notes/input_part011_review.md†L276-L276
[^89]: Source: knowledge/notes/input_part008_review.md†L688-L705
[^90]: Source: knowledge/notes/input_part007_review.md†L164-L164
[^91]: Source: knowledge/notes/input_part001_review.md†L177-L705
[^92]: Source: data/vesc_help_group/text_slices/input_part001.txt†L24932-L24966
[^93]: Source: knowledge/notes/input_part001_review.md†L766-L768
[^94]: Source: knowledge/notes/input_part001_review.md†L502-L502
[^95]: Source: knowledge/notes/input_part001_review.md†L482-L560
[^96]: Source: knowledge/notes/input_part001_review.md†L732-L733
[^97]: Source: knowledge/notes/input_part007_review.md†L126-L126
[^98]: Source: knowledge/notes/input_part007_review.md†L209-L214
[^99]: Source: knowledge/notes/input_part007_review.md†L205-L205
[^100]: Source: knowledge/notes/input_part007_review.md†L286-L286
[^101]: Source: knowledge/notes/input_part010_review.md†L315-L315
[^102]: Source: knowledge/notes/input_part009_review.md†L338-L343
[^103]: Source: knowledge/notes/input_part009_review.md†L373-L373
[^104]: Source: knowledge/notes/input_part009_review.md†L339-L343
[^105]: Source: knowledge/notes/input_part009_review.md†L342-L343
[^106]: Source: knowledge/notes/input_part012_review.md†L20178-L20234
[^107]: Source: knowledge/notes/input_part012_review.md†L20185-L20224
[^108]: Source: knowledge/notes/input_part005_review.md†L385-L386
[^109]: Source: knowledge/notes/input_part007_review.md†L192-L262
[^110]: Source: knowledge/notes/input_part007_review.md†L64-L141
[^111]: Source: knowledge/notes/input_part007_review.md†L64-L64
[^112]: Source: knowledge/notes/input_part007_review.md†L165-L165
[^113]: Source: knowledge/notes/input_part007_review.md†L214-L214
[^114]: Source: knowledge/notes/input_part009_review.md†L453-L469
[^115]: Source: knowledge/notes/input_part001_review.md†L475-L499
[^116]: Source: knowledge/notes/input_part001_review.md†L475-L705
[^117]: Source: knowledge/notes/input_part001_review.md†L662-L705
[^118]: Source: knowledge/notes/input_part002_review.md†L148-L149
[^119]: Source: knowledge/notes/input_part008_review.md†L15-L15
[^120]: Source: knowledge/notes/input_part005_review.md†L101-L106
[^121]: Source: knowledge/notes/input_part005_review.md†L104-L108
[^122]: Source: knowledge/notes/input_part005_review.md†L108-L114
[^artem_balancer]: Source: knowledge/notes/input_part000_review.md†L711-L712
[^cc_only]: Source: knowledge/notes/input_part000_review.md†L709-L712
[^123]: Source: knowledge/notes/input_part009_review.md†L35-L36
[^124]: Source: knowledge/notes/input_part009_review.md†L29-L35
[^125]: Source: knowledge/notes/input_part009_review.md†L467-L469
[^126]: Source: knowledge/notes/input_part011_review.md†L252-L252
[^bridge-prereg]: Source: knowledge/notes/input_part011_review.md†L501-L501
[^127]: Source: knowledge/notes/denis_all_part02_review.md†L5499-L5526
[^128]: Source: knowledge/notes/input_part012_review.md†L19339-L19342
[^129]: Source: knowledge/notes/input_part012_review.md†L15649-L15756
[^130]: Source: knowledge/notes/input_part007_review.md†L58-L58
[^131]: Source: knowledge/notes/input_part012_review.md†L11401-L11411
[^132]: Source: knowledge/notes/input_part012_review.md†L11792-L11797
[^133]: Source: knowledge/notes/input_part014_review.md†L98-L100
[^ip001-daly-bal]: Source: data/vesc_help_group/text_slices/input_part001.txt†L17551-L17690
[^ip001-ghost-voltage]: Source: data/vesc_help_group/text_slices/input_part001.txt†L17796-L17860
[^ip001-jk-threshold]: Source: data/vesc_help_group/text_slices/input_part001.txt†L17579-L17670
[^ip001-jk-activation]: Source: data/vesc_help_group/text_slices/input_part001.txt†L22497-L22572
[^ip001-bms-heat]: Source: data/vesc_help_group/text_slices/input_part001.txt†L19285-L19320
