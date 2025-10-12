# Varla / Zero 10X Battery Upgrade Brief

## Purpose & Scope
This brief helps Varla Eagle One and Zero 10X owners who have already installed, or plan to install, a Spintend Ubox V2 dual controller. It focuses on upgrading the stock 52 V battery system so the scooter can sustain 60–70 km/h cruise speeds without tripping the battery management system (BMS) or starving the controllers.

## Stock Pack Diagnosis
- **Cell topology:** OEM packs use a 14S6P layout (≈52 V nominal) built from 3,000 mAh-class cells such as Samsung 32IR, yielding ≈18 Ah capacity but only ~50–70 A of safe continuous discharge for the entire pack.¹ ²
- **Real-world limits:** When paired with a Ubox V2 (75 V, 100 A ×2), the stock pack tops out near 60–70 km/h because it can deliver only ≈10 A per cell before the BMS clamps output. Meaningful speed gains require a higher-current battery.³
- **Frame constraints:** Zero 10X-class decks are cramped; OEM electronics boxes also pool water, so any upgrade plan must account for extra volume, sealing, and thermal mass.⁴

## Upgrade Targets
| Goal | Minimum Requirement | Rationale |
| --- | --- | --- |
| Sustained 60–70 km/h cruise | 20S6P or larger using ≥4.5 Ah high-discharge cells (e.g., P45B, P42A, 50S) | Raises pack voltage to ≈72 V nominal and doubles continuous wattage headroom vs. stock.¹ ⁵ |
| Peak battery output | ≥140 A continuous with ≥200 A short bursts | Matches community-proven dual-Ubox tuning while leaving thermal margin.⁶ |
| BMS capability | Smart BMS rated ≥200 A discharge with configurable charge/regen limits | Prevents premature cutoffs during regen or field-weakening pulls.³ ⁷ |
| Wiring & connectors | Dual QS8/QS10 (battery) + XT150 or 8 AWG phase looms; waterproof pass-throughs | Eliminates the QS8 short/overheat cases seen on undersized harnesses.⁸ |

## Pack Architecture & Cell Selection
1. **Series count:** Moving to 20S (~84 V full charge) is the community’s “magic number” for meaningful speed improvements; 52 V packs demand excessive phase current for the same result.⁹
2. **Parallel groups:** A 20S7P pack built from modern 21700 cells provides ~30 Ah while keeping per-cell current below 8 A during 200 A system bursts.¹ ⁰
3. **Chemistry picks:**
   - **Samsung 50S / Molicel P45B:** High-discharge cells that comfortably support 10 A+ continuous per cell, critical for dual-drive launches.¹ ⁰
   - **LG M26 / rewrapped Xiaomi cells:** Only acceptable for budget builds; expect ~40 A per half-pack and plan for future upgrades.¹¹
4. **Mechanical layout:** Holderless “W” layouts, thin epoxy isolators, and 45 mm deck extenders make 20S7P possible inside Zero 10X decks, but only with meticulous insulation and strain relief.¹² ¹³

## BMS, Harness, and Safety Requirements
- **BMS headroom:** Size discharge and regen thresholds to stay ahead of controller cutoffs; Daly-style boards trip around 2.7 V/cell, so program the Ubox battery cutoffs accordingly.⁷
- **Harness insulation:** Triple heat-shrink, fish paper between nickel layers, and plexiglass or epoxy shields over balance leads prevent chafing in wet decks.¹³ ¹⁴
- **Connector upgrades:** Budget 20 S builds still need 8 AWG equivalents; dual 20 S packs assembled from repurposed modules only produce ~17.5 Ah per half, so expect to parallel leads or upsize wiring immediately.¹¹ ¹⁵
- **Charging gear:** Adjustable 0–120 V lab chargers must be verified internally and wired wall-first to avoid arc flashes across XT plugs.¹⁶

## Controller Integration Checklist
1. **Firmware parity:** Confirm both Ubox controllers run matching firmware before uploading XML profiles; mismatches lock out parameter edits until reflashed.¹⁷
2. **Thermal mounting:** Repaste controllers, hard-mount them to aluminum decks or dedicated heatsinks, and plan airflow paths. Modern Ubox aluminum singles are markedly more reliable than legacy 100 V boards, but dual units have failed when 250 A battery spikes hit inadequately cooled installs.⁶
3. **ADC accessory boards:** Log brake-light behavior and ADC V2 board health; firmware 6.0 updates have latched brake inputs after water exposure, so document reflash and diagnostic workflows.¹⁸
4. **Disable phase filters after detection:** Spintend confirmed the motor-wizard phase filter should only be used during detection—leaving it active during rides reintroduces noise and ABS overcurrent faults.[^phase-filter]
4. **Hall sensors & traction:** Fit hall-equipped front motors or enable HFI only after verifying detection values; hall-less Dualtron fronts under-pull current versus sensored rears, making traction control tuning uneven.¹⁹
5. **CAN synchronization:** Balance battery and phase amps across both controllers and run proper 120 Ω termination to avoid bus faults during high-load pulls.²⁰
6. **Exploit CAN power sync:** Spintend 85-series controllers share a CAN power line, letting one ignition button wake both units once the harness is linked—wire it correctly before removing redundant switches.²⁶

## Mechanical & Handling Considerations
- **Stem & chassis stress:** Stock stems crack at cable ports, and legacy twin-stem frames wobble above 60 km/h without dampers, reinforced handlebars, and balanced phase currents.²¹ ²²
- **Suspension & clearance:** Machined swingarm axles and upgraded pivots are required for 11" hubs; failing to rework clearances twists calipers or fouls springs.²³
- **Waterproofing:** Resin-coat controller boxes or reroute harnesses—stock enclosures collect water and corrode upgrades quickly.⁴
- **Earless 85/240 mounting:** New cases still ship without tabs; plan printed brackets, retapped threads, or adhesive adapters before rough roads shake loose under-deck installs.²⁷

## Validation & Logging
1. **Instrumentation:** Pair VESC Tool live data with Dragy/GPS logging while dialing wheel diameter (Zero 10X hubs calibrate near 250 mm).²⁴
2. **Thermal runs:** Log stator and case temps after Statorade refills; large case-to-sensor deltas mean the thermal path still needs work before pushing higher currents.²⁵
3. **Ride audits:** Start with 2:1 phase-to-battery ratios (e.g., 70 A batt / 160 A phase per motor), verify sag stays <10 %, and increment cautiously.⁶
4. **Safety drills:** Test regen at low speeds, ensure mechanical brakes stop the scooter with regen disabled, and rehearse BMS cutoff recovery so unexpected trips do not leave the rider without propulsion.⁷

## Pre-Delivery Checklist
- [ ] Pack IR logged, cells balanced within 10 mV, and smart BMS firmware updated.
- [ ] QS8/QS10 battery connectors torqued, XT150 (or better) phase bullets insulated, and harness strain relief verified.
- [ ] Controller heatsinks repasted, temp sensors mapped in VESC Tool, and fan/duct mounts installed if using enclosed decks.
- [ ] Firmware, traction control, and field-weakening settings exported to versioned XML profiles.
- [ ] Waterproofing audit complete (gaskets, conformal coating, silica packs) and deck drains cleared.
- [ ] Baseline ride logs (launch, 60 km/h cruise, regen stop) archived with GPS overlays.

## Source Notes
[^1]: Zero 10X decks shipped with 52 V 18.5 Ah packs built from Samsung 32IR cells. 【F:knowledge/notes/input_part006_review.md†L179-L179】
[^2]: Stock pack discharge limits and chronic chassis complaints for Zero 10X-class scooters. 【F:knowledge/notes/input_part006_review.md†L136-L136】
[^3]: Varla Eagle One (Zero 10X clone) with Ubox V2 dual controller plateauing at 60–70 km/h on the OEM battery. 【F:knowledge/notes/input_part004_review.md†L347-L352】
[^4]: Zero 10X electronics boxes pooling water and the need for comprehensive sealing during VESC swaps. 【F:knowledge/notes/input_part006_review.md†L221-L229】
[^5]: Community guidance that 20 S packs are the “magic number” for high-speed scooters, whereas 48–52 V builds demand disproportionate current. 【F:knowledge/notes/input_part004_review.md†L357-L365】
[^6]: Ubox dual-controller spike failures near 250 A battery and the emphasis on improved aluminum-board reliability when adequately cooled. 【F:knowledge/notes/input_part004_review.md†L233-L238】
[^7]: Daly smart-BMS cutoff thresholds around 2.7 V/cell and the need to align controller limits. 【F:knowledge/notes/input_part003_review.md†L517-L519】
[^8]: QS8 short incidents during high-power builds and the reminder to upsize connectors for motorcycle-class conversions. 【F:knowledge/notes/input_part010_review.md†L44-L52】
[^9]: Voltage vs. current discussion emphasizing 20 S as the breakpoint for top-speed goals. 【F:knowledge/notes/input_part004_review.md†L357-L365】
[^10]: Zero 10X builders fitting 20 S7P packs with 45 mm spacers and highlighting the need for higher-grade chemistry over budget cells. 【F:knowledge/notes/input_part008_review.md†L13-L20】【F:knowledge/notes/input_part008_review.md†L333-L341】
[^11]: Budget cell and wiring math showing repurposed modules only supply ~40 A per half-pack. 【F:knowledge/notes/input_part004_review.md†L236-L242】
[^12]: Holderless pack layouts with deck extenders enabling dense 20 S builds. 【F:knowledge/notes/input_part008_review.md†L13-L20】
[^13]: Triple insulation, epoxy sheets, and careful lead routing for Zero 10X high-voltage packs. 【F:knowledge/notes/input_part007_review.md†L278-L285】【F:knowledge/notes/input_part009_review.md†L18-L23】
[^14]: Pack builders stacking dual G30 modules and over-insulating balance leads for Zero 10X conversions. 【F:knowledge/notes/input_part007_review.md†L260-L266】
[^15]: Recommendation for 8 AWG equivalents on 100 A scooters and expectations when using repurposed cells. 【F:knowledge/notes/input_part004_review.md†L236-L242】
[^16]: Adjustable charger inspection and safe connection sequence guidance. 【F:knowledge/notes/input_part004_review.md†L301-L301】
[^17]: Firmware alignment requirements for Makerbase/Makerbase-derived boards reporting as 75_100 but needing 75_100_V2 firmware. 【F:knowledge/notes/input_part004_review.md†L327-L327】【F:knowledge/notes/input_part004_review.md†L479-L479】
[^18]: ADC V2 board failures causing latched brake inputs and the need for diagnostics after firmware updates. 【F:knowledge/notes/input_part004_review.md†L365-L373】
[^19]: Dualtron front motor underperformance without hall sensors compared to sensored rears. 【F:knowledge/notes/input_part004_review.md†L350-L355】
[^20]: Zero 10X CAN harness experiments confirming 120 Ω termination requirements. 【F:knowledge/notes/input_part006_review.md†L21-L27】
[^21]: Reports of stems cracking at cable ports and the need for hydraulic brakes plus regen on tuned builds. 【F:knowledge/notes/input_part005_review.md†L283-L286】
[^22]: Handling limits of Zero 10X twin-stem frames even after 10 kW upgrades, reinforcing the need for dampers and balanced currents. 【F:knowledge/notes/input_part008_review.md†L315-L322】
[^23]: Swingarm machining requirements for 11" hub swaps and pivot upgrades. 【F:knowledge/notes/input_part006_review.md†L34-L42】【F:knowledge/notes/input_part006_review.md†L214-L222】
[^24]: Wheel-diameter calibration and GPS logging workflow for Zero 10X builds. 【F:knowledge/notes/input_part007_review.md†L368-L374】
[^25]: Statorade temperature observations showing persistent case-to-sensor deltas. 【F:knowledge/notes/input_part004_review.md†L320-L327】
[^26]: Spintend 85-series CAN power line allows a single ignition button to wake linked controllers once harnessed properly.【F:knowledge/notes/input_part011_review.md†L19016-L19035】
[^27]: Latest earless 85/240 housings forced riders to print brackets, retap threads, or glue adapters so the controllers survive long-travel suspensions.【F:knowledge/notes/input_part012_review.md†L20537-L20587】
[^phase-filter]: Phase-filter toggles exist to stabilize motor detection—disable them after setup to avoid noise and ABS overcurrent faults on Spintend controllers.【F:knowledge/notes/input_part004_review.md†L31-L31】
