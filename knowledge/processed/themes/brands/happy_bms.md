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

- Developed as Denis and Happy Giraffe’s smart BMS alternative to Daly clones, the board supports 9–15 S packs, speaks Xiaomi telemetry, and ships with a red status LED plus USB/UART tooling for app access.[^1][^2]
- Happy BMS happily powers oversized packs beyond its nominal 32 Ah rating—the state-of-charge display simply bottoms out early while ~3 Ah remain, so riders plan range using voltage once the counter saturates.[^3][^4]
- Current handling is fixed: the board trips a second after crossing ~44 A and its fuses blow near 60 A, making it unsuitable for 3 kW (50–60 A) ambitions without external contactors or a different BMS.[^5][^6]
- Charging defaults to a conservative 3 A limit to protect Xiaomi charge leads; the Embedden BMS Tool raises that cap to 5.5 A when thicker harnesses are installed.[^7]
- Packs remain asleep until a charger is connected and balancing can occur at any state of charge; expect ≈0.6 %/day self-discharge on stored batteries and wake them with a quick top-up before rides.[^8][^9]

## Integration Guidance

- Pair Happy BMS with Rita or XiaoDash by downgrading BLE firmware and logging live current—Rita still enforces ~30 A while Happy monitors pack temperature (charging pauses near 40 °C and resumes once it cools to ≈35 °C).[^10][^11][^12]
- Charging through the XT30 discharge lead bypasses over-voltage protection and should only happen under direct supervision with a voltmeter on the pack.[^13]
- Happy BMS tolerates 54.6 V chargers on 14 S packs—it simply stops early until the proper charger arrives—so range is reduced but cells remain safe.[^14]
- Use common-port wiring for external packs and keep external protection inline—Happy BMS will still block output if shorts are detected, but it cannot replace fuses or Rita’s diode isolation on its own.[^15][^16]
- Follow the official wiring diagram when regrouping cells—builders who doubled balance wires or misordered leads instantly popped Daly boards and would have done the same on Happy without the documentation.[^17]
- Expect the display to hit 0 % before the pack is empty on large builds; rely on voltage logs or XiaoDash telemetry for accurate range planning.[^3][^4]

## Troubleshooting & Commissioning

| Symptom | Likely Cause | Resolution |
| --- | --- | --- |
| Pack shows voltage but no output | Board ships asleep until first charge pulse | Connect a charger briefly to wake the discharge MOSFETs.[^8] |
| Charging stalls below pack voltage | Input supply under 47 V on 48 V builds | Use a true 48 V CC/CV charger; Xiaomi bricks at 42 V leave the BMS idle.[^18] |
| Error 24 or BLE faults after flashing | Firmware flashed without a 10 S reference pack | Flash with a lower-voltage pack connected, then reconfigure cell count in the Embedden app.[^19] |
| Repeated fuse trips above 44 A | Overcurrent beyond design envelope | Reinforce wiring and step up to Daly/ANT-class boards for ≥50 A builds.[^5] |
| Coulomb counter misreads LiFePO₄ packs | Firmware assumes 4.1 V lithium-ion chemistry | Charge cells above 3.5 V to recalibrate or monitor via the included web/USB tools.[^20] |
| Daly/clone died after balance wiring mistake | Misordered or doubled sense wires during install | Rewire per Happy documentation—negative first, confirm each voltage step with a meter, and avoid stacking two wires on one pad.[^17] |

## Logistics & Availability

- Happy BMS cannot currently ship to Indonesia or Vietnam; riders use freight forwarders or substitute JBD smart boards paired with ScooterHacking Utility when local customs block deliveries.[^21]
- Denis quotes roughly €290 for a turnkey 13S3P pack with Happy BMS compared with DIY NKON builds, highlighting the labor and QA premium when outsourcing packs.[^22]
- Field deployments confirm reliable operation in 10S7P Ninebot Max G2 packs and 48 V Pro/Pro 2 conversions once XiaoDash sliders are set to 13 cells and 20 Ah.[^23][^24]

## Safety Notes

- Respect the 44 A ceiling and keep regen below ~30 A—Denis and Happy repeatedly warn that exceeding those limits trips error 39, overheats packs, or explodes Rita on higher-voltage builds.[^25]
- Never rely on charge-port power for accessories; build DC/DC harnesses off the discharge rails to preserve Happy BMS protections.[^26]
- Maintain waterproofing: seal deck seams, grease bearings, and inspect harnesses after heavy rain to avoid latent shorts that Happy BMS will flag as persistent faults.[^27][^28]

## References

[^1]: Source: knowledge/notes/denis_all_part02_review.md, L1233 to L1233
[^2]: Source: knowledge/notes/denis_all_part02_review.md, L1595 to L1595
[^3]: Source: knowledge/notes/denis_all_part02_review.md, L16 to L17
[^4]: Source: knowledge/notes/denis_all_part02_review.md, L399 to L401
[^5]: Source: knowledge/notes/denis_all_part02_review.md, L73 to L74
[^6]: Source: knowledge/notes/denis_all_part02_review.md, L322 to L323
[^7]: Source: knowledge/notes/denis_all_part02_review.md, L476 to L477
[^8]: Source: knowledge/notes/denis_all_part02_review.md, L376 to L376
[^9]: Source: knowledge/notes/denis_all_part02_review.md, L479 to L481
[^10]: Source: knowledge/notes/denis_all_part02_review.md, L11 to L12
[^11]: Source: knowledge/notes/denis_all_part02_review.md, L316 to L316
[^12]: Source: knowledge/notes/denis_all_part02_review.md, L55 to L57
[^13]: Source: knowledge/notes/denis_all_part02_review.md, L185 to L186
[^14]: Source: knowledge/notes/denis_all_part02_review.md, L108 to L108
[^15]: Source: knowledge/notes/denis_all_part02_review.md, L64 to L65
[^16]: Source: knowledge/notes/denis_all_part02_review.md, L532 to L532
[^17]: Source: knowledge/notes/denis_all_part02_review.md, L374 to L376
[^18]: Source: knowledge/notes/denis_all_part02_review.md, L396 to L397
[^19]: Source: knowledge/notes/denis_all_part02_review.md, L543 to L544
[^20]: Source: knowledge/notes/denis_all_part02_review.md, L1670 to L1671
[^21]: Source: knowledge/notes/denis_all_part02_review.md, L1586 to L1587
[^22]: Source: knowledge/notes/denis_all_part02_review.md, L253 to L253
[^23]: Source: knowledge/notes/denis_all_part02_review.md, L116 to L117
[^24]: Source: knowledge/notes/denis_all_part02_review.md, L1625 to L1626
[^25]: Source: knowledge/notes/denis_all_part02_review.md, L618 to L618
[^26]: Source: knowledge/notes/denis_all_part02_review.md, L70 to L71
[^27]: Source: knowledge/notes/denis_all_part02_review.md, L553 to L553
[^28]: Source: knowledge/notes/denis_all_part02_review.md, L536 to L536
