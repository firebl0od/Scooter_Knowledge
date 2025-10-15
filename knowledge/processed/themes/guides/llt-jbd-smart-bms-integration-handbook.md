# LLT/JBD Smart BMS Integration Handbook

## TL;DR
- LLT/JBD smart boards remain the community’s compact, configurable baseline: integrated Bluetooth, programmable limits, and a 20 A soft-start pre-charge protect controllers without consuming deck space.[^1]
- Treat physical packaging as a design constraint—21s 100 A cases still expand to ~27 mm once fasteners and heatsinks are counted, so plan spacers, insulation, and harness routing before cells are welded.[^2][^3]
- Tune regen and discharge envelopes around the BMS instead of the motor: conservative −5 A/−40 A regen budgets, ≤200 A discharge on 18s7p packs, and verified Xiaoxiang settings prevent the MOSFET blowouts and charge-FET trips riders keep reporting.[^4][^5][^20][^21]

---

## Why Pick LLT/JBD Instead of Other Smart BMS Platforms?
- **Balanced feature set for commuters.** Riders praise the LLT/JBD family for compact housings, configurable temperature and current limits, gentle capacitor pre-charge, and built-in Bluetooth/UART telemetry that drop into cramped decks without rewiring the entire harness.[^1]
- **Predictable passive balancing.** Expect roughly 100–160 mA of passive bleed—enough for 6–8 p scooter modules once charge rates are sane—while JK is still the only widely available active balancer.[^6]
- **Survivable current headroom.** Builders routinely cap 18s7p Sony VTC6A packs near 200 A with JBD hardware on 20 kW projects and note that headline 15 kW “limits” rarely matter in practice.[^20]
- **Alternatives carry their own baggage.** JK hardware continues to cook balance resistors and leave buyers stranded on warranty, Daly boards bleed at just ~30 mA, and budget smart-BMS listings without real protection expose builders to liability.[^8][^9]
- **Real-world trips prove the protection.** A JK smart BMS recently cut a 20 S build at ~60 A when a short developed, saving the pack but stranding the rider—proof the protection works, and a reminder to stage lower-current limp modes or backup packs if you rely on JK hardware.[^10]
- **Security needs manual discipline.** Cloud-linked apps can let vandals tweak limits; veterans keep LLT/JBD packs offline or locked to default credentials when unattended.[^10]

## Community-Vetted Board Options
| Board | Series Support | Proven Continuous Envelope | Packaging & Integration Notes |
| --- | --- | --- | --- |
| JBD 10–17S 100 A (slim case) | 10–17 S | Zero 10X dual-controller conversions hold ≈60 A charge and ≈100 A discharge comfortably when cabling is sized correctly.[^11][^13] | Chosen when space is tight because it preserves Bluetooth/UART telemetry in the smallest deck-friendly shell.[^1][^11] |
| JBD 21S 100 A narrow-body | 15–21 S | Suitable for commuter regen budgets around −5 A battery / −40 A phase when paired with 17 S/20 S packs.[^4] | Real-world thickness hits ~27 mm once screws and sinks are counted; still fits between 18650 rows and sold for ~€45 during AliExpress sales.[^2][^3] |
| JBD-SP17S005 150 A class | 17 S | Replace or uprate regen if repeated charge-overcurrent trips persist—voltage sag can trip the charge FET even with sane settings.[^5] | Keep spares on hand; lingering trips after a swap often point to controller-side faults or logging gaps.[^5] |
| Jiabada 230 A (575 A peak) | 6–21 S (verify before 22 S) | Gives dual Spintend 80100 builds ample thermal headroom, but treat 230 A as the design limit and confirm firmware before stretching voltage.[^7][^12] | Dual-sided heatsinks need isolation from nearby cells, and listings conflict on true 22 S support—confirm before committing the pack layout.[^7][^12] |

## Pre-Installation Planning
- **Map deck geometry early.** Xiaomi Pro 2 builders report just 10.5–11 cm of internal deck width; many relocate the BMS into stem spacers or external bays before welding cells.[^15]
- **Budget vertical clearance.** Once screw heads and silicone pads are added, JBD shells swell beyond spec—print spacers or add silicone isolation pads before final assembly.[^3][^16]
- **Lay out insulation stacks.** Silicone or fishpaper isolators under the output studs and between series planes keep repasted heatsinks from chafing cells.[^3][^16]
- **Stage harness and sense-lead routing.** Dry-fit the balance loom, confirm reach to each parallel group, and label identical white leads before the pack is sealed.[^14][^17]

## Wiring & Commissioning Workflow
1. **Land B− before balance taps.** Builders who connected sense leads first saw zero-voltage groups until the missing parallels were tied back in—attach B−, then walk the harness up the stack while verifying voltages stepwise.[^14][^17]
2. **Leverage the built-in pre-charge.** The LLT/JBD soft-start caps controller inrush around 20 A; power the system once to confirm, then decide whether an external antispark is still necessary.[^1]
3. **Size the charge path.** Zero 10X conversions targeting 40 A charging lean on ANT/JBD boards; underspec’d bargain units plateau near 40 A continuous and run hot.[^13]
4. **Document connector pinouts.** AliExpress harness diagrams move around—archive the vendor image alongside your wiring notes so future repairs aren’t guesswork.[^13]
5. **Bridge telemetry before sealing the deck.** Snap the CAN adapter into the VESC harness (120 Ω bus termination intact) so BMS voltage, current, and alarms flow into dashboards without reopening the battery box.[^25]

## Configuration, UX & Security Notes
- **Switch phones to English for full menus.** The Xiaoxiang/JBD apps inherit handset language and hide the “Softlock” toggle plus balance thresholds unless you install the admin APK or change locale first.[^18]
- **Lower Softlock before fine-balancing.** Disable the 15 mV guard or set the delta deliberately; otherwise the app silently ignores tighter thresholds during top balancing.[^18]
- **Keep the pack offline when parked.** JBD’s cloud portal can expose your scooter to remote limit changes, so veterans either avoid the online portal altogether or leave default credentials untouched.[^10]
- **Log everything.** Photograph BMS settings after each session—some builders keep CSV exports—to backtrack when firmware or phone updates scramble parameters.[^10][^18]
- **Sanity-check system parameters when series counts drift.** A 22 S ANT/JBD install read as 23 S until the owner rewrote the series-voltage and capacity fields from scratch, so treat unexpected telemetry as a configuration error before chasing wiring faults.[^param_sanity]

## Current, Regen & Thermal Guardrails
- **Start regen conservatively.** 17 S commuters stay near −5 A battery / −40 A phase until pack temps and JBD logs prove the hardware can absorb more without tripping protection.[^4]
- **Respect pack-specific discharge caps.** Even 20 kW builds park 18s7p VTC6A packs around 200 A battery to keep cells and BMS FETs in a safe thermal envelope.[^20]
- **Raise BMS regen limits before hard braking tests.** A 75200 rider toasted MOSFETs when the BMS still thought 60–70 A was the ceiling; bump Xiaoxiang charge-current limits (e.g., 100 A) before dialing in VESC brake amps and voltage caps.[^21]
- **Investigate recurring charge-FET trips.** Persistent JBD-SP17S005 faults even after sane settings usually point to sag or controller spikes—swap the BMS and comb logs before assuming firmware bugs.[^5]

## Telemetry & Maintenance
- **Feed BMS data into dashboards.** The plug-in CAN bridge shares pack voltage, current, and alarms over the scooter’s existing harness, making fault correlation far easier in VESC Tool or CAN-based displays.[^25]
- **Use active balancers sparingly.** External active boards can equalise large packs in about an hour, whereas the onboard JBD bleeders need days; deploy them during rebuilds, then rely on the smart BMS for day-to-day drift.[^19]
- **Schedule periodic harness checks.** Silicone-isolated output studs and repasted heatsinks should be inspected every service interval to ensure vibration hasn’t crushed insulation.[^16]

## Charging Infrastructure Updates
- **Adjustable supplies cover odd pack voltages.** Builders chasing 21 S charging have adopted programmable 22 S/18 A supplies paired with ANT sleep timers so dormant packs don’t drift while waiting for the next ride.[^adj_supply]
- **Multi-voltage bricks plug stock gaps.** When premium 21 S chargers disappear, the community leans on 16–24 S/20 A switchable supplies—worth flagging for travel kits that need one brick for multiple scooters.[^multi_brick]
- **Mind discharge-less BMS designs.** Jason’s new 32 S-capable board omits discharge FETs entirely, effectively passing unlimited current; treat it as a monitoring tap and keep downstream fusing intact.[^no_fet]

## Troubleshooting & Field Failures
- **Watch for JK→JBD retrofit triggers.** Owners burnt by JK resistor failures now default to JBD or ANT hardware; keep spare boards so you can swap without waiting on overseas RMAs.[^9]
- **Do not bypass discharge FETs.** A bypassed scooter lit its rear controller at just 35–40 km/h when the unprotected pack dumped full current—full-protection smart BMS hardware with proper fusing is non-negotiable on 20 S builds.[^22]
- **Upgrade after close calls.** Riders who survived BMS bypass incidents immediately budgeted ~$100 for ANT/JBD replacements and rewired temp sensors correctly to prevent repeat brownouts.[^23]
- **Verify vendor voltage claims.** Jiabada’s “6–22 S” listings actually document 6–21 S support; confirm firmware before building 22 S stacks or commission dual-BMS architectures.[^12]
- **Log and share failure data.** Community troubleshooters can only help if you export Xiaoxiang logs, especially when chasing intermittent charge overcurrent or regen spikes.[^5][^18]
- **Treat charger LEDs as advisory only.** Xiaomi/OEM chargers have stayed green while pushing 42 V into 10 S packs—always confirm pack voltage with a meter before assuming the BMS is finished balancing.[^charger-led]
- **Load-test suspicious externals.** Bargain 10 S packs that collapse under light draws leave the stock battery carrying the ride; run them solo at low amperage before trusting the BMS telemetry or mixing them in parallel.[^sag_test]

## Deployment Checklist
- [ ] Measure deck cavity height/width and confirm the BMS plus insulation clears cells and harnesses.[^3][^15]
- [ ] Dry-fit the balance loom, label every lead, and record the intended series order before welding.[^14][^17]
- [ ] Program charge/discharge/temperature limits, then screenshot every settings page for your maintenance log.[^10][^18]
- [ ] Run a low-current shakedown with regen capped (≤−5 A battery) while monitoring Xiaoxiang logs for FET or voltage alarms.[^4][^5]
- [ ] Integrate the CAN adapter or UART telemetry before sealing the battery so future diagnostics don’t require a full teardown.[^25]

---

## Source Notes
[^1]: LLT/JBD smart BMS units earn praise for compact enclosures, configurable protection limits, gentle ~20 A capacitor pre-charge, and Bluetooth/UART telemetry that simplify cramped scooter installations.【F:knowledge/notes/input_part007_review.md†L192-L192】【F:knowledge/notes/input_part007_review.md†L261-L261】
[^2]: Riders highlighted the 21s 100 A JBD’s narrow footprint and ~€45 sale pricing when width, not height, constrained their builds.【F:knowledge/notes/input_part008_review.md†L189-L189】
[^3]: Community measurements show the so-called “100 A” JBD case grows to roughly 27 mm thick once screws and heatsinks are counted, forcing silicone shims and spacer reprints in tight decks.【F:knowledge/notes/input_part009_review.md†L318-L318】
[^4]: 17 S commuter tuning guidance keeps regen near −5 A battery / −40 A phase to stay within the JBD 100 A board’s comfort zone.【F:knowledge/notes/input_part008_review.md†L104-L104】
[^5]: Tristan’s JBD-SP17S005 pack logged charge-overcurrent trips from voltage sag, with Smart Repair recommending a full BMS swap when sane settings still triggered faults.【F:knowledge/notes/input_part011_review.md†L659-L660】
[^6]: Mirono reminded shoppers that JK is the only active-balancing option, while LLT/JBD passive bleeders sit around 100–160 mA—enough for most high-current scooter packs.【F:knowledge/notes/input_part007_review.md†L179-L179】
[^7]: Builders pairing dual Spintend 80100s with Jiabada’s 230 A smart BMS isolate its dual-sided heatsinks from cells to preserve thermal headroom on 20s8p projects.【F:knowledge/notes/input_part007_review.md†L180-L180】
[^8]: Group consensus contrasted JK, ANT, and LLT/JBD offerings—emphasising active balancing and software quality on premium boards while warning that no-name units without real protection invite liability.【F:knowledge/notes/input_part005_review.md†L323-L323】
[^9]: JK smart BMS hardware has cooked balance resistors within a day and left riders with minimal warranty relief, prompting many to switch to ANT or JBD charge/discharge boards.【F:knowledge/notes/input_part007_review.md†L175-L176】
[^10]: JK smart BMS boards have already tripped at ≈60 A when shorts developed, saving packs but leaving riders stranded until they rebuilt with lower-current hardware or secondary packs.【F:knowledge/notes/input_part012_review.md†L249-L249】
[^10]: Leaving smart-BMS apps online invites tampering—JBD’s cloud portal and ANT’s password handling can let outsiders modify limits—so veterans keep packs offline or locked to defaults when parked.【F:knowledge/notes/input_part009_review.md†L33-L33】
[^11]: Mirono steered dual-controller G30 conversions toward the slim 10–17 S 100 A JBD board as the smallest smart option that still exposes UART/Bluetooth telemetry.【F:knowledge/notes/input_part007_review.md†L262-L262】
[^12]: Crimekillz noted Jiabada’s “6–22 S” documentation actually caps support at 21 S, so builders confirm firmware limits before trusting those boards in 22 S stacks.【F:knowledge/notes/input_part007_review.md†L64-L64】
[^13]: Zero 10X pack builders comparing 20s6p options settled on ANT or JBD smart boards to secure 40 A charging plus unrestricted discharge, flagging cheaper units as marginal for 60 A draws.【F:knowledge/notes/input_part008_review.md†L524-L524】
[^14]: Misrouting identical white sense leads on a JBD harness produced zero-volt readings until the parallels were retied to the correct terminal—proof that labeling and continuity checks matter.【F:knowledge/notes/input_part009_review.md†L261-L261】
[^15]: Xiaomi Pro 2 deck measurements around 10.5–11 cm wide left only millimetres for extra electronics, so builders often relocate the BMS into shoulder spacers or bags.【F:knowledge/notes/input_part007_review.md†L185-L185】
[^16]: Patrick ended up silicone-isolating the oversized JBD output studs and reprinting deck spacers once the real-case thickness became apparent.【F:knowledge/notes/input_part008_review.md†L165-L165】
[^17]: Wiring logs remind builders to land B− before balance taps and verify each voltage step when assembling 20s8p packs to avoid frying the BMS during first power-up.【F:knowledge/notes/input_part008_review.md†L181-L181】
[^18]: JBD’s mobile app mirrors phone language and hides the Softlock toggle plus sub-15 mV balance settings unless you install the admin APK or switch the handset to English.【F:knowledge/notes/input_part009_review.md†L323-L323】【F:knowledge/notes/input_part008_review.md†L170-L170】
[^19]: External active balancers can equalise large packs in about an hour, whereas relying on JBD’s onboard balancing would take days—handy during rebuilds but unnecessary once the pack is stable.【F:knowledge/notes/input_part009_review.md†L27-L27】
[^20]: Builders keep LLT/JBD boards on 20 kW projects by capping ≈200 A battery on 18s7p Sony VTC6A packs, noting that the published 15 kW figure is conservative with proper cooling.【F:knowledge/notes/input_part006_review.md†L200-L200】
[^21]: Morten Jensen’s blown 75200 MOSFET traced to regen limits below the JBD ceiling—raising Xiaoxiang charge current (e.g., to 100 A) and keeping VESC max regen voltage within pack limits prevented repeats.【F:knowledge/notes/input_part013_review.md†L703-L703】
[^22]: A rider who bypassed discharge protection watched a rear controller ignite at 35–40 km/h, reinforcing the need for full-protection smart BMS units and fuses on high-power scooters.【F:knowledge/notes/input_part012_review.md†L368-L368】
[^23]: After that fire, builders budgeted high-current ANT/JBD boards (~US $100) and rewired temperature leads correctly instead of running charge-only BMS hardware.【F:knowledge/notes/input_part012_review.md†L369-L369】
[^25]: A plug-in CAN adapter now lets LLT/JBD smart BMS boards stream telemetry over the existing scooter harness, simplifying monitoring inside VESC Tool or CAN dashboards.【F:knowledge/notes/input_part006_review.md†L365-L365】
[^charger-led]: GABE documented a Xiaomi charger remaining green while still delivering 42 V to a 10 S pack, reinforcing the need to verify voltage and logs instead of trusting indicator lights alone.【F:knowledge/notes/input_part011_review.md†L18-L18】
[^sag_test]: Denis’ workshop found cheap “13 Ah” externals sagged immediately, forcing the internal pack to do all the work—test suspect packs alone at low load before trusting their specs or paralleling them with healthy batteries.【F:knowledge/notes/denis_all_part02_review.md†L5499-L5526】
[^adj_supply]: Adjustable 22 S/18 A supplies paired with ANT sleep timers keep 21 S packs topped without drifting when scooters sit for weeks between rides.【F:knowledge/notes/input_part012_review.md†L11401-L11411】
[^multi_brick]: Switchable 16–24 S/20 A bricks fill in when premium 21 S chargers are unavailable, giving one charger that can service multiple scooter voltages.【F:knowledge/notes/input_part012_review.md†L11792-L11797】
[^no_fet]: Jason’s 32 S-capable BMS variant deletes discharge FETs entirely, effectively leaving downstream hardware as the only short-circuit protection.【F:knowledge/notes/input_part012_review.md†L19339-L19342】
[^param_sanity]: Rewriting the series-count and amp-hour fields cleared a JBD pack that suddenly reported 23 S on a 22 S build, highlighting how mis-set parameters skew telemetry before any wiring fault is found.【F:knowledge/notes/input_part013_review.md†L304-L304】
