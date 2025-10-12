# VESC Labs High-Voltage Portfolio (2025)

## TL;DR
- VESC Labs entered the ≥100 V arena with the Maxim 120 V controllers, the dual-channel VESC Duet, and a capacitor-rich smart BMS, finally giving builders an official Vedder-designed alternative to Chinese high-voltage ESCs.【F:knowledge/notes/input_part014_review.md†L25-L27】
- Early documentation shows STM32F4 control silicon, exposed capacitor bays, and a ~€530 bundle price, so communities are dissecting whether the feature set justifies the premium over entrenched X12/Spintend options.【F:knowledge/notes/input_part014_review.md†L26-L27】
- The companion Minim 100 V platform and Express logger extend the ecosystem downward, but their lower current ceilings and immature logging firmware mean riders still benchmark them against FarDriver boxes and stay on VESC Tool 6.05 for reliable data capture.【F:knowledge/notes/input_part014_review.md†L138-L140】【F:knowledge/notes/input_part014_review.md†L203-L203】

## Product Line Snapshot
| Product | Target Pack / Current Envelope | Distinguishing Traits | Deployment Watchpoints |
| --- | --- | --- | --- |
| Maxim 120 V (single) | 120 V-class packs, high phase currents (community expects ≥300 A once validated) | First official high-voltage Vedder controller with modular capacitor bay and shunt-based sensing; shares footprint cues with Spintend 85150-class hardware.【F:knowledge/notes/input_part014_review.md†L25-L27】 | Validate capacitor thermal performance and FET selection once teardown data lands; price pressure from X12/Seven imports makes proof-of-reliability essential.【F:knowledge/notes/input_part014_review.md†L25-L27】 |
| VESC Duet (dual) | ≤100 V packs, ≈150 A phase per side | Dual board with integrated balancing channels and exposed venting—positioned as an officially supported alternative to Ubox duals.【F:knowledge/notes/input_part014_review.md†L25-L27】 | Confirm MCU peripheral headroom and per-side cooling before dropping into cramped decks; early adopters question whether specs justify the bundle cost.【F:knowledge/notes/input_part014_review.md†L26-L27】 |
| Smart BMS | High-voltage Vedder builds needing logged balancing | Ships alongside Maxim/Duet launch to give builders an official CAN-balancing solution; intended to complement Express telemetry stacks.【F:knowledge/notes/input_part014_review.md†L25-L27】 | Audit balancing current, discharge handling, and integration scripts as soon as firmware lands—communities are wary after ANT/JK inconsistencies.【F:knowledge/notes/input_part014_review.md†L25-L27】 |
| Minim 100 V | Compact e-mopeds and stealth builds around 35 A battery / ~180 A phase | Offers tidy harnessing and native VESC firmware for small-frame scooters where full Maxim hardware is overkill.【F:knowledge/notes/input_part014_review.md†L203-L203】 | Expect head-to-head testing with FarDriver “little boxes” that deliver higher battery current at lower cost; prove whether Minim’s control fidelity offsets the amperage gap.【F:knowledge/notes/input_part014_review.md†L203-L203】 |
| VESC Express | Peripheral CAN/logger board for Maxim-family stacks | Supports OTA updates and SD logging to unify controller and BMS telemetry, marketed as the preferred path over third-party dashes.【F:knowledge/notes/input_part014_review.md†L138-L140】 | Firmware 6.06 currently restarts logs every ~3 s, so teams are holding on 6.05 until the bug is patched; plan external 5 V/12 V rails when pairing with low-current controller accessories.【F:knowledge/notes/input_part014_review.md†L138-L140】 |

## Deployment Checklist for Early Adopters
1. **Stage firmware rollouts carefully.** Keep Maxim/Duet pilots on the same 6.05 baseline that preserves Express logging stability before experimenting with 6.06.x betas.【F:knowledge/notes/input_part014_review.md†L138-L140】
2. **Instrument capacitor and FET thermals.** Capture teardown imagery and thermal logs during first rides to confirm whether the exposed capacitor bay actually vents heat better than sealed X12 housings.【F:knowledge/notes/input_part014_review.md†L25-L27】
3. **Budget auxiliary power rails.** Until controller-side regulators are characterized, assume Express needs its own DC/DC supply so lighting and telemetry don’t brown out on Maxim or Duet installations.【F:knowledge/notes/input_part014_review.md†L138-L140】
4. **Benchmark Minim against FarDriver.** Log identical ride segments to quantify whether Minim’s smoother control loop outweighs FarDriver’s higher battery current for the same chassis.【F:knowledge/notes/input_part014_review.md†L203-L203】

## Procurement and Community Signals
- Veteran builders are eager to slot Maxim/Maxim+ units into “VESC museum” comparison racks alongside MakerX, Tronic, Ennoid, and Thor hardware, ensuring standardized shootouts once shipments clear customs.【F:knowledge/notes/input_part014_review.md†L27-L27】
- Pricing debates center on whether the €500+ sticker secures enough reliability and support versus importing Seven or Spintend controllers with comparable current ratings; expect teardown-driven reviews to shape adoption curves.【F:knowledge/notes/input_part014_review.md†L26-L27】

## Source Notes
[^1]: Launch specs and ecosystem overview for Maxim 120 V controllers, VESC Duet, and the companion smart BMS released in August 2025.【F:knowledge/notes/input_part014_review.md†L25-L27】
[^2]: Early documentation detailing STM32F4 control, exposed capacitor bays, and bundle pricing, plus community skepticism about value versus Chinese alternatives.【F:knowledge/notes/input_part014_review.md†L26-L27】
[^3]: Express logging instability on VESC Tool 6.06 and guidance to remain on 6.05 until the restart bug is fixed.【F:knowledge/notes/input_part014_review.md†L138-L140】
[^4]: Minim 100 V current envelope and trade-offs compared with compact FarDriver controllers.【F:knowledge/notes/input_part014_review.md†L203-L203】
[^5]: Community plans to benchmark Maxim-family hardware alongside existing controller collections once units arrive.【F:knowledge/notes/input_part014_review.md†L27-L27】
