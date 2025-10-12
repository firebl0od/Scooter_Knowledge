# VESC Labs High-Voltage Portfolio (2025 Launch)

## TL;DR
- August 2025 saw VESC Labs debut the Maxim 120 V family alongside the dual-channel VESC Duet (100 V peak, 150 A phase per side) and a matching smart BMS, signalling an official high-voltage stack from Vedder’s team and sparking immediate price-to-performance debates against Chinese imports.【F:knowledge/notes/input_part014_review.md†L25-L27】
- Datasheet drops highlight STM32F4 control silicon, exposed capacitor bays for ventilation, and integrated balancing, but early adopters still question whether the roughly €530 Duet bundle justifies the current headroom relative to similarly priced competitors.【F:knowledge/notes/input_part014_review.md†L26-L27】
- Compact e-moped builders now weigh the Minim 100 V’s tidy harnessing (≈180 A phase, ~35 A battery) against higher-battery-limit FarDriver boxes, forcing a choice between polished VESC firmware and trapezoidal brute force.【F:knowledge/notes/input_part014_review.md†L203-L204】
- Community labs plan teardowns and telemetry comparisons—JPPL’s “VESC museum” already lines up Thor, MakerX, Tronic, and Ennoid controllers to benchmark Maxim hardware once shipments land.【F:knowledge/notes/input_part014_review.md†L27-L27】

## Product Line Snapshot
| Product | Voltage Window | Continuous Phase / Battery Guidance | Distinguishing Features | Ideal Use Cases |
| --- | --- | --- | --- | --- |
| Maxim 120 V | Up to 120 V packs | Targeted at high-voltage single-motor builds (field data pending) | Official Vedder hardware with documented capacitor arrays and STM32F4 control | Flagship race scooters needing native VESC support |
| VESC Duet | 100 V peak dual | 150 A phase per side (bundle pricing around €530) | Dual stack with vented capacitor bays and integrated balancing channels | Dual-motor commuters seeking turnkey CAN coordination |
| Smart BMS | 120 V-class | Matching the Maxim ecosystem (current limits TBD) | Capacitor-equipped management with VESC-native telemetry | Builders wanting a single-vendor control + BMS stack |
| Minim 100 V | 100 V packs | ≈180 A phase / ~35 A battery | Compact footprint for e-mopeds; firmware-aligned with VESC Tool | Lightweight scooters or mopeds prioritizing tidy harnessing |

## Launch & Competitive Context
- Early adopters are benchmarking Maxim/Duet pricing against Tronic, Spintend, and FarDriver options while planning teardown logs to verify FET choices, capacitor count, and MCU resources versus launch claims.【F:knowledge/notes/input_part014_review.md†L25-L27】
- Community curators such as JPPL maintain comparison fleets spanning Thor, MakerX, Tronic, and Ennoid controllers, ensuring consistent testbeds once Maxim and Seven 18 shipments arrive.【F:knowledge/notes/input_part014_review.md†L27-L27】

## Integration & Field Priorities
- Document Maxim/Duet installations with photos of capacitor bay airflow paths and thermal interface choices to validate how the vented design performs in enclosed decks.【F:knowledge/notes/input_part014_review.md†L26-L27】
- Log CAN behavior when mixing Duet or Minim controllers with VESC Express or third-party telemetry; early Seven 18 bundles needed separate Express modules to handshake reliably, highlighting the value of validating Maxim interoperability before field deployment.【F:knowledge/notes/input_part014_review.md†L27-L27】【F:knowledge/notes/input_part014_review.md†L146-L148】
- Capture duty cycle, phase current, and battery sag data on Minim vs. FarDriver builds so commuters can decide whether firmware polish outweighs the higher current ceiling of trapezoidal controllers.【F:knowledge/notes/input_part014_review.md†L203-L204】
