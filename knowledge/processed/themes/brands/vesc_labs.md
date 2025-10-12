# VESC Labs High-Voltage Portfolio (2025 Launch)

## TL;DR
- August 2025 introduced VESC Labs' Maxim 120 V controllers, the dual-channel VESC Duet (100 V peak, 150 A phase per side), and a capacitor-rich smart BMS, giving Vedder's team an in-house answer to high-voltage scooter demands.[^1]
- First-look datasheets confirm STM32F4-class control, exposed capacitor bays for airflow, and integrated balancing, yet riders question whether the ~€530 Duet bundle delivers enough current headroom versus similarly priced Chinese hardware.[^2]
- Compact commuters are weighing the Minim 100 V (≈180 A phase, ~35 A battery) against small FarDriver boxes that ship with higher battery limits, trading firmware polish for raw current.[^3]

## Product Line Snapshot
| Product | Voltage Window | Continuous Phase / Battery Guidance | Distinguishing Features | Ideal Use Cases |
| --- | --- | --- | --- | --- |
| Maxim 120 V | Up to 120 V packs | Targeted at high-voltage single-motor builds (field data pending) | Official Vedder hardware with documented capacitor arrays and STM32F4 brain | Flagship race scooters needing native VESC support |
| VESC Duet | 100 V peak dual | 150 A phase per side (bundle pricing around €530) | Dual stack with vented capacitor bays and integrated balancing channels | Dual-motor commuters seeking turnkey CAN coordination |
| Smart BMS | 120 V-class | Matching the Maxim ecosystem (current limits TBD) | Capacitor-equipped management with VESC-native telemetry | Builders wanting a single-vendor control + BMS stack |
| Minim 100 V | 100 V packs | ≈180 A phase / ~35 A battery | Compact footprint for e-mopeds; firmware-aligned with VESC Tool | Lightweight scooters or mopeds prioritizing tidy harnessing |

## Launch & Competitive Context
- Early adopters are benchmarking Maxim/Duet pricing against Tronic, Spintend, and FarDriver options, with many planning teardown logs to verify FET part numbers, capacitor count, and MCU resources versus marketing claims.[^1][^2][^4]
- Community curators (e.g., JPPL's "VESC museum") maintain comparison fleets spanning Thor, MakerX, Tronic, and Ennoid controllers, ensuring consistent testbeds once Maxim and Seven 18 shipments arrive.[^5]

## Integration & Field Priorities
- Document Maxim/Duet installations with photos of capacitor bay airflow paths and thermal interface choices to validate how the vented design performs in enclosed decks.[^2][^4]
- Log CAN behavior when mixing Duet or Minim controllers with VESC Express or third-party telemetry, noting that earlier Seven 18 bundles still required separate Express modules to handshake reliably.[^4][^6]
- Capture duty cycle, phase current, and battery sag data on Minim vs. FarDriver builds so commuters can decide whether firmware polish outweighs the higher current ceiling of trapezoidal controllers.[^3]

## Source Notes
[^1]: Launch summary covering Maxim 120 V, VESC Duet, and the companion smart BMS, plus initial community pricing debates.【F:knowledge/notes/input_part014_review.md†L25-L25】
[^2]: Datasheet observations noting STM32F4 control, exposed capacitor bays, integrated balancing, and bundle pricing concerns.【F:knowledge/notes/input_part014_review.md†L26-L26】
[^3]: Comparison of Minim 100 V current limits with small FarDriver controllers for compact e-moped builds.【F:knowledge/notes/input_part014_review.md†L203-L203】
[^4]: Follow-up actions urging teardown documentation for Maxim/Duet hardware to verify capacitor, FET, and MCU choices.【F:knowledge/notes/input_part014_review.md†L213-L213】
[^5]: Community "VESC museum" inventories maintained for comparative testing once new controllers arrive.【F:knowledge/notes/input_part014_review.md†L27-L27】
[^6]: Reports that Seven 18 bundles still required a separate VESC Express module over CAN to obtain telemetry, signalling ongoing firmware/pin-map work before broader deployment.【F:knowledge/notes/input_part014_review.md†L146-L148】
