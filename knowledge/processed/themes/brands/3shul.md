# 3Shul Controllers Brand Dossier

## TL;DR
- C350-class stacks survive full 22 S race weekends around 400 A phase / 200 A battery when regen is disabled and installs are logged carefully, but CL350 revisions still run hotter and demand close inspection before pushing similar loads.¹
- Expect premium capability with boutique support: Raphaël Foujiwara contrasts the C350 and R350 hardware while warning that post-sale help is limited, regional techs charge hourly, and self-installed boards rarely see warranty coverage.² ³
- Marketing headlines about 32 S compatibility outpace field data—community veterans cap CL-series controllers near 29–30 S without regen because the 135 V FET stack leaves little transient headroom and onboard DC/DC rails sag under heavier loads.⁴

## Product Line Cheat Sheet
| Model | Nominal Pack Window | Community Envelope | Differentiators & Caveats |
| --- | --- | --- | --- |
| C350 | 18–22 S | 400 A phase / 200 A battery with regen disabled on well-cooled builds | Upgraded capacitance and MOSFETs relative to early runs; compact footprint for dual installs.¹ ⁵ |
| R350 | 18–22 S | Commonly operated at 400 A phase despite 350 A spec | CNC case with smart latch, integrated 12 V 3 A rail; battery rating shifts to 250 A vs. C350’s 200 A guidance.² |
| CL350 | 18–22 S | Survives 22 S racing but runs hotter; regen off strongly advised | Shares firmware with C350, but reports of elevated case temps and noisier QC push racers toward C350 for endurance.¹ |
| CL500 (preview) | 18–30 S (no regen above ≈30 S) | Targeting ≥500 A phase once released | 12 ToLL FETs on 25.86 mm IMS base, integrated Bluetooth, thicker 200 A bus bars; EU distribution limited to Rage Mechanics.⁶ |
| CL700 / CL1000 (preview) | 18–32 S (marketing) | Awaiting validation; projected 800–1000 A peaks | Teased alongside CL500 with similar packaging and larger ToLL stages aimed at 30 S superbikes; community still awaiting burn-in data.⁶ |

## Voltage & Current Guardrails
- Treat 32 S marketing cautiously: field autopsies of CL350 failures after 120 V charging led veterans to cap the series at ≈29–30 S without regen because 135 V FETs provide thin spike margin.⁴
- Race crews who log every run keep 22 S C350 builds alive by disabling regen entirely, keeping per-wheel battery current near 200 A, and documenting wiring so BMS trips do not hot-cut controllers.¹ ⁵
- Riders stepping beyond 22 S plan for external DC/DC modules—the onboard supplies sag below 1 A once pack voltage climbs, risking brownouts for accessories or logic rails if overloaded.⁴

## Reliability, QC & Support Reality
- Raphaël Foujiwara notes the C350’s beefier capacitance versus the R350’s higher battery rating and 12 V rail, but stresses that unpaid support is unsustainable; Molex MicroClasp CAN connectors and sparse documentation demand technician-level installs.²
- Regional specialists such as Foujiwara now offer paid repairs (≈€60 / hr) and have revived multiple failed boards, yet other owners report spending €1,700 on repairs that still left controllers unbootable—stock spares or fallbacks remain essential.³ ⁷
- Community consensus still praises 3Shul when X12 or MakerX inventory dries up because the capacitor banks tolerate 23 S+ power levels, but buyers factor in minimal transparency and the need to self-verify firmware drops (shared via Drive links).¹ ⁸

## Setup & Commissioning Checklist
1. **Inspect the power stage before first power-up.** Open the enclosure, audit capacitor soldering, and confirm ToLL packages sit flat; recent refreshes tout cleaner assembly but racers still preflight every unit.¹ ⁶
2. **Wire both controllers through the ignition path.** CL350/CL500 owners report that each ESC must see the key-enable line (or a shared 5 V enable) and that damaged Bluetooth daughterboards can short the entire rail until unplugged.⁹
3. **Document CAN pinout and harness polarity.** Miswired CAN leads and reversed Bluetooth connectors have killed modules on arrival—verify MicroClasp orientation and continuity before applying pack voltage.² ⁹
4. **Verify firmware provenance.** Keep local copies of the shared CL350 V3 sources and confirm version parity across dual stacks; unsupported binaries complicate support and hide current-limit tweaks.¹

## Tuning & Operation Guardrails
- **Disable regen when chasing 22 S race loads.** High-voltage weekends that kept regen off avoided the input-spike failures that plagued CL-series boards charged above 120 V.¹ ⁴
- **Respect the 400 A phase comfort zone.** Riders satisfied with 400 A phase / 200 A battery logs see durable performance; attempts to push higher currents without upgraded cooling or MOSFET swaps lead to runaway heat or gate failures.¹ ⁵ ⁸
- **Log temperatures per controller.** Racers differentiate front vs. rear thermal behavior to catch sensor faults and stay under ~70 °C controller temps even when chasing 30 kW bursts.⁸

### Field-Proven Current Targets
| Scenario | Battery Current | Phase Current | Notes |
| --- | --- | --- | --- |
| Dual C350 race scooter (22 S) | ≤200 A per ESC | ~400 A | Requires regen disabled, thorough logging, and inspected wiring to survive full weekends.¹ ⁵ |
| Mixed C350 + R350 commuter | 200–250 A combined | 350–400 A | Pair the R350’s 12 V rail with auxiliary DC/DC for lighting; treat 400 A as an upper practical limit.² ³ |
| Future CL500 superbike (planned) | TBD (aim ≥250 A) | ≥500 A (projected) | Await production burn-in; packaging and bus upgrades imply higher sustained output once validated.⁶ |

## Packaging & Integration Notes
- Rage Mechanics is prepping flatter capacitor layouts and dual-plug revisions for upcoming C350 shipments to fit 100 × 120 × 25 mm bays where Little FOCer and Tronic boards have failed.¹⁰
- Deck builds targeting 30 S batteries rely on ≥10 P parallels (e.g., 40T or 50PL) to keep sag tolerable when controllers pull 200 A each—plan mechanical spacers and thermal paths before welding packs.⁶ ⁸
- Controllers destined for 3D-printed or tight enclosures need rigid mounting: loose boards have fractured ToLL packages under shock loads, underscoring the need for machined brackets and isolation.⁶

## Ecosystem & Accessories
- Riders are evaluating 3Shul’s forthcoming display, multifunction switch pods, and RGB integrations as successors to Davega setups once reliable CAN/BMS data streams are available.¹¹
- Telemetry comparisons show VESC real-time power inflates peaks by ~10 kW without filtering; pairing 3Shul controllers with SmartDisplay or Voyage Megan dashboards offers cross-checks against BMS data for tuning accuracy.⁸ ¹¹

## When to Choose Alternatives
- Builders without access to trusted 3Shul repair pipelines lean toward Spintend 85/250 or Seven 18 controllers despite lower phase limits, trading absolute output for wider distribution and clearer warranty paths.⁸
- Projects that truly require ≥30 S or regen above 22 S consider Thor 400 or FarDriver stages until 3Shul’s CL700/CL1000 hardware publishes validated stress-test data.⁴ ⁶ ⁸

## Source Notes
[^1]: Race reports showing C350 durability at 22 S with regen disabled, contrasted with hotter CL350 behavior and shared firmware repositories. 【F:knowledge/notes/input_part008_review.md†L304-L309】【F:knowledge/notes/input_part008_review.md†L416-L417】
[^2]: Raphaël Foujiwara’s comparison of C350 vs. R350 specs, CAN connector callouts, and support limitations. 【F:knowledge/notes/input_part011_review.md†L26-L28】
[^3]: Regional repair ecosystem details, including €60 /hr service rates, revived boards, and unresolved post-repair failures. 【F:knowledge/notes/input_part012_review.md†L256-L269】【F:knowledge/notes/input_part012_review.md†L388-L389】
[^4]: CL-series voltage ceiling cautions and DC/DC sag observations that cap practical operation near 29–30 S. 【F:knowledge/notes/input_part006_review.md†L71-L72】【F:knowledge/notes/input_part006_review.md†L117-L117】
[^5]: Field data confirming 400 A phase / 200 A battery envelopes for C350 stacks under disciplined logging. 【F:knowledge/notes/input_part012_review.md†L256-L258】
[^6]: CL500/CL700/CL1000 roadmap previews, packaging dimensions, and distribution notes from Rage Mechanics. 【F:knowledge/notes/input_part004_review.md†L288-L295】【F:knowledge/notes/input_part004_review.md†L304-L305】
[^7]: Cases of significant spend on unsuccessful repairs plus reminders that spare controllers remain prudent. 【F:knowledge/notes/input_part012_review.md†L268-L269】【F:knowledge/notes/input_part012_review.md†L389-L389】
[^8]: Community sentiment that 3Shul remains a high-voltage alternative when other controllers are scarce, alongside capacitor durability praise. 【F:knowledge/notes/input_part014_review.md†L11-L20】【F:knowledge/notes/input_part014_review.md†L71-L72】
[^9]: Commissioning guidance covering ignition wiring, Bluetooth shorts, and CAN polarity checks. 【F:knowledge/notes/input_part004_review.md†L288-L295】
[^10]: Packaging refresh teasers describing flatter capacitor layouts and dual connectors for updated C350 deliveries. 【F:knowledge/notes/input_part004_review.md†L304-L305】
[^11]: Emerging accessory ecosystem (displays, switch pods, RGB integration) and telemetry calibration insights. 【F:knowledge/notes/input_part014_review.md†L81-L83】【F:knowledge/notes/input_part014_review.md†L78-L80】
