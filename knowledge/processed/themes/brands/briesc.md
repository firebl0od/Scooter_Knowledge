# Briesc Controller Snapshot
## TL;DR

- Italian-built single Briesc controllers are already holding 150 A battery / 350 A phase on bench-tested builds without heatsinks, logging roughly 55 °C case temps at those loads—proof the compact package has real headroom once airflow is planned.[^1]
- The platform ships without integrated Bluetooth, so budget an external dongle or SmartDisplay pass-through even though the controller hardware can sit in tight decks that previously relied on Makerbase 75100-class gear.[^1]

## Field Notes

- Riders flashing Vedder firmware onto ultra-small BLE boards found the range unusable; pair Briesc installs with the proven €2 modules or SmartDisplay bridges until an official wireless option ships.[^2]

# Briesc 100/200 Controller Snapshot

- Dual Briesc 100/200 prototypes sit between C700 and C1000 hardware—Simone has already logged 210 A battery / 420 A phase per side on scooters while lab tests touched 900 A phase without failure.[^3]
- The current focus is oil-cooled QS273-class hubs; smaller scooter builds should budget serious thermal management before expecting similar current envelopes.[^3]

## Commissioning Notes

- Treat the platform as pre-production: document temperature sensors, bus reinforcement, and cooling before letting riders chase 250 A battery targets on 40PL packs.[^4][^3]
- Pair the controllers with JK 200 A smart BMS units or equivalent so discharge logging keeps pace with the current these stacks can deliver at 22 S.[^5]

## Open Questions

- Community still needs scooter-sized telemetry to confirm how the 100/200 behaves away from QS273 dynos—log sustained thermal performance once smaller hubs are tested.[^3]

## References

[^1]: Source: knowledge/notes/input_part005_review.md, L346 to L349
[^2]: Source: knowledge/notes/input_part005_review.md, L346 to L347
[^3]: Source: knowledge/notes/input_part010_review.md, L347 to L348
[^4]: Source: knowledge/notes/input_part010_review.md, L327 to L329
[^5]: Source: knowledge/notes/input_part010_review.md, L376 to L377
