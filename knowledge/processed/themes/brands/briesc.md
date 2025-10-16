# Briesc Controller Snapshot
## TL;DR
- Italian-built single Briesc controllers are already holding 150 A battery / 350 A phase on bench-tested builds without heatsinks, logging roughly 55 °C case temps at those loads—proof the compact package has real headroom once airflow is planned.【F:knowledge/notes/input_part005_review.md†L346-L349】
- The platform ships without integrated Bluetooth, so budget an external dongle or SmartDisplay pass-through even though the controller hardware can sit in tight decks that previously relied on Makerbase 75100-class gear.【F:knowledge/notes/input_part005_review.md†L346-L349】
## Field Notes
- Riders flashing Vedder firmware onto ultra-small BLE boards found the range unusable; pair Briesc installs with the proven €2 modules or SmartDisplay bridges until an official wireless option ships.【F:knowledge/notes/input_part005_review.md†L346-L347】
# Briesc 100/200 Controller Snapshot
- Dual Briesc 100/200 prototypes sit between C700 and C1000 hardware—Simone has already logged 210 A battery / 420 A phase per side on scooters while lab tests touched 900 A phase without failure.【F:knowledge/notes/input_part010_review.md†L347-L348】
- The current focus is oil-cooled QS273-class hubs; smaller scooter builds should budget serious thermal management before expecting similar current envelopes.【F:knowledge/notes/input_part010_review.md†L347-L348】
## Commissioning Notes
- Treat the platform as pre-production: document temperature sensors, bus reinforcement, and cooling before letting riders chase 250 A battery targets on 40PL packs.【F:knowledge/notes/input_part010_review.md†L327-L329】【F:knowledge/notes/input_part010_review.md†L347-L348】
- Pair the controllers with JK 200 A smart BMS units or equivalent so discharge logging keeps pace with the current these stacks can deliver at 22 S.【F:knowledge/notes/input_part010_review.md†L376-L377】
## Open Questions
- Community still needs scooter-sized telemetry to confirm how the 100/200 behaves away from QS273 dynos—log sustained thermal performance once smaller hubs are tested.【F:knowledge/notes/input_part010_review.md†L347-L348】
