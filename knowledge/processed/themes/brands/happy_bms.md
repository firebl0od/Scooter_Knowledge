# Happy BMS Platform Dossier

## Quick Facts
| Topic | Details |
| --- | --- |
| Supported chemistries | 9–15 S lithium-ion packs with embedded coulomb counting | 
| Continuous discharge ceiling | 44 A (internal fuses pop ≈60 A) |
| Charging envelope | Defaults to 3 A, configurable to 5.5 A via Embedden tools |
| Form factor | Compact Xiaomi-compatible PCB with XT30/XT60 harness options |
| Channel & price | Sold direct by Denis Yurev around €69 plus shipping |

## Product Overview
- Developed as Denis and Happy Giraffe’s smart BMS alternative to Daly clones, the board supports 9–15 S packs, speaks Xiaomi telemetry, and ships with a red status LED plus USB/UART tooling for app access.【F:knowledge/notes/denis_all_part02_review.md†L1233-L1233】【F:knowledge/notes/denis_all_part02_review.md†L1595-L1595】
- Happy BMS happily powers oversized packs beyond its nominal 32 Ah rating—the state-of-charge display simply bottoms out early while ~3 Ah remain, so riders plan range using voltage once the counter saturates.【F:knowledge/notes/denis_all_part02_review.md†L16-L17】【F:knowledge/notes/denis_all_part02_review.md†L399-L401】
- Current handling is fixed: the board trips a second after crossing ~44 A and its fuses blow near 60 A, making it unsuitable for 3 kW (50–60 A) ambitions without external contactors or a different BMS.【F:knowledge/notes/denis_all_part02_review.md†L73-L74】【F:knowledge/notes/denis_all_part02_review.md†L322-L323】
- Charging defaults to a conservative 3 A limit to protect Xiaomi charge leads; the Embedden BMS Tool raises that cap to 5.5 A when thicker harnesses are installed.【F:knowledge/notes/denis_all_part02_review.md†L476-L477】
- Packs remain asleep until a charger is connected and balancing can occur at any state of charge; expect ≈0.6 %/day self-discharge on stored batteries and wake them with a quick top-up before rides.【F:knowledge/notes/denis_all_part02_review.md†L376-L376】【F:knowledge/notes/denis_all_part02_review.md†L479-L481】

## Integration Guidance
- Pair Happy BMS with Rita or XiaoDash by downgrading BLE firmware and logging live current—Rita still enforces ~30 A while Happy monitors pack temperature (charging pauses near 40 °C and resumes once it cools to ≈35 °C).【F:knowledge/notes/denis_all_part02_review.md†L11-L12】【F:knowledge/notes/denis_all_part02_review.md†L316-L316】【F:knowledge/notes/denis_all_part02_review.md†L55-L57】
- Charging through the XT30 discharge lead bypasses over-voltage protection and should only happen under direct supervision with a voltmeter on the pack.【F:knowledge/notes/denis_all_part02_review.md†L185-L186】
- Happy BMS tolerates 54.6 V chargers on 14 S packs—it simply stops early until the proper charger arrives—so range is reduced but cells remain safe.【F:knowledge/notes/denis_all_part02_review.md†L108-L108】
- Use common-port wiring for external packs and keep external protection inline—Happy BMS will still block output if shorts are detected, but it cannot replace fuses or Rita’s diode isolation on its own.【F:knowledge/notes/denis_all_part02_review.md†L64-L65】【F:knowledge/notes/denis_all_part02_review.md†L532-L532】
- Follow the official wiring diagram when regrouping cells—builders who doubled balance wires or misordered leads instantly popped Daly boards and would have done the same on Happy without the documentation.【F:knowledge/notes/denis_all_part02_review.md†L374-L376】
- Expect the display to hit 0 % before the pack is empty on large builds; rely on voltage logs or XiaoDash telemetry for accurate range planning.【F:knowledge/notes/denis_all_part02_review.md†L16-L17】【F:knowledge/notes/denis_all_part02_review.md†L399-L401】

## Troubleshooting & Commissioning
| Symptom | Likely Cause | Resolution |
| --- | --- | --- |
| Pack shows voltage but no output | Board ships asleep until first charge pulse | Connect a charger briefly to wake the discharge MOSFETs.【F:knowledge/notes/denis_all_part02_review.md†L376-L376】 |
| Charging stalls below pack voltage | Input supply under 47 V on 48 V builds | Use a true 48 V CC/CV charger; Xiaomi bricks at 42 V leave the BMS idle.【F:knowledge/notes/denis_all_part02_review.md†L396-L397】 |
| Error 24 or BLE faults after flashing | Firmware flashed without a 10 S reference pack | Flash with a lower-voltage pack connected, then reconfigure cell count in the Embedden app.【F:knowledge/notes/denis_all_part02_review.md†L543-L544】 |
| Repeated fuse trips above 44 A | Overcurrent beyond design envelope | Reinforce wiring and step up to Daly/ANT-class boards for ≥50 A builds.【F:knowledge/notes/denis_all_part02_review.md†L73-L74】 |
| Coulomb counter misreads LiFePO₄ packs | Firmware assumes 4.1 V lithium-ion chemistry | Charge cells above 3.5 V to recalibrate or monitor via the included web/USB tools.【F:knowledge/notes/denis_all_part02_review.md†L1670-L1671】 |
| Daly/clone died after balance wiring mistake | Misordered or doubled sense wires during install | Rewire per Happy documentation—negative first, confirm each voltage step with a meter, and avoid stacking two wires on one pad.【F:knowledge/notes/denis_all_part02_review.md†L374-L376】 |

## Logistics & Availability
- Happy BMS cannot currently ship to Indonesia or Vietnam; riders use freight forwarders or substitute JBD smart boards paired with ScooterHacking Utility when local customs block deliveries.【F:knowledge/notes/denis_all_part02_review.md†L1586-L1587】
- Denis quotes roughly €290 for a turnkey 13S3P pack with Happy BMS compared with DIY NKON builds, highlighting the labor and QA premium when outsourcing packs.【F:knowledge/notes/denis_all_part02_review.md†L253-L253】
- Field deployments confirm reliable operation in 10S7P Ninebot Max G2 packs and 48 V Pro/Pro 2 conversions once XiaoDash sliders are set to 13 cells and 20 Ah.【F:knowledge/notes/denis_all_part02_review.md†L116-L117】【F:knowledge/notes/denis_all_part02_review.md†L1625-L1626】

## Safety Notes
- Respect the 44 A ceiling and keep regen below ~30 A—Denis and Happy repeatedly warn that exceeding those limits trips error 39, overheats packs, or explodes Rita on higher-voltage builds.【F:knowledge/notes/denis_all_part02_review.md†L618-L618】
- Never rely on charge-port power for accessories; build DC/DC harnesses off the discharge rails to preserve Happy BMS protections.【F:knowledge/notes/denis_all_part02_review.md†L70-L71】
- Maintain waterproofing: seal deck seams, grease bearings, and inspect harnesses after heavy rain to avoid latent shorts that Happy BMS will flag as persistent faults.【F:knowledge/notes/denis_all_part02_review.md†L553-L553】【F:knowledge/notes/denis_all_part02_review.md†L536-L536】
