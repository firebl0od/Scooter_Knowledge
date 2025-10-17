# Varla / Zero 10X Battery Upgrade Brief

## Overview

The Varla Eagle One and Zero 10X are popular dual-motor scooters that benefit significantly from battery and controller upgrades. This guide focuses on upgrading from the stock 52V battery system to a high-performance 20S setup when paired with Spintend Ubox V2 dual controllers. The stock 14S6P pack limits speed to 60-70 km/h due to current restrictions; upgrading to a 20S6P or larger pack with high-discharge cells unlocks sustained highway speeds while maintaining reliability.

## What You'll Learn

- Why the stock 52V battery limits performance
- Recommended battery upgrade specifications (20S6P minimum)
- Cell selection criteria for high-discharge applications  
- BMS and wiring requirements for dual-controller setups
- Controller integration and tuning considerations
- Mechanical packaging and safety requirements

## ⚡ Upgrade Overview

The stock 14S6P (52V) battery limits Varla/Zero10X builds to 60-70 km/h due to current restrictions. Upgrading to 20S6P+ with high-discharge cells unlocks sustained highway speeds.

## 📋 Quick Reference: Upgrade Tiers

| Tier | Pack Config | Cells | Continuous Output | Speed Gain | Difficulty |
|------|------------|-------|------------------|-----------|------------|
| **Budget** | 20S6P | LG M26 rewraps | ~80A | +15-20 km/h | ⭐⭐⭐ |
| **Performance** | 20S7P | Samsung 50S / P42A | ~140A | +20-30 km/h | ⭐⭐⭐⭐ |
| **Endurance** | 20S7P + 20S6P external | P45B / 50PL | ~200A | +20-30 km/h + 2x range | ⭐⭐⭐⭐⭐ |

⚠️ **Critical**: Stock Zero 10X decks are cramped. Budget 4-8 hours for mechanical fitting and waterproofing.

💡 **Pro Tip**: Start with 20S7P internal first. Add external pack only after validating dual-controller tuning and BMS integration.

## 🔧 Related Guides

- [Battery Pack Design](battery_pack_design.md)
- [Spintend Ubox Integration Handbook](spintend-ubox-integration-handbook.md)
- [Power Distribution](power_distribution.md)
- [Controller Setup](controller_setup.md)

## Purpose & Scope

This brief helps Varla Eagle One and Zero 10X owners who have already installed, or plan to install, a Spintend Ubox V2 dual controller. It focuses on upgrading the stock 52 V battery system so the scooter can sustain 60–70 km/h cruise speeds without tripping the battery management system (BMS) or starving the controllers.

## Stock Pack Diagnosis

- **Cell topology:** OEM packs use a 14S6P layout (≈52 V nominal) built from 3,000 mAh-class cells such as Samsung 32IR, yielding ≈18 Ah capacity but only ~50–70 A of safe continuous discharge for the entire pack.¹ ²
- **Real-world limits:** When paired with a Ubox V2 (75 V, 100 A ×2), the stock pack tops out near 60–70 km/h because it can deliver only ≈10 A per cell before the BMS clamps output. Meaningful speed gains require a higher-current battery.³
- **Frame constraints:** Zero 10X-class decks are cramped; OEM electronics boxes also pool water, and long-time owners still report weak motors, harsh suspension, and snapping poles unless the frame is overhauled.
  - plan volume, sealing, and reinforcement together.⁴ [^1]

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
5. **Auxiliary capacity:** PuneDir’s build stacks a 20 S6 P external pack alongside the internal 20 S7 P brick and saddlebag storage to chase endurance targets without gutting the deck, reinforcing the need for modular harnessing.[^2][^3]

## BMS, Harness, and Safety Requirements

- **BMS headroom:** Size discharge and regen thresholds to stay ahead of controller cutoffs; Daly-style boards trip around 2.7 V/cell, so program the Ubox battery cutoffs accordingly and favor ANT or JBD smart boards when you need 40 A charging plus unrestricted discharge on 20 S6 P layouts.[^4]
- **Harness insulation:** Triple heat-shrink, fish paper between nickel layers, and plexiglass or epoxy shields over balance leads prevent chafing in wet decks.¹³ ¹⁴
- **Connector upgrades:** Budget 20 S builds still need 8 AWG equivalents; dual 20 S packs assembled from repurposed modules only produce ~17.5 Ah per half, so expect to parallel leads or upsize wiring immediately.¹¹ ¹⁵
- **Charging gear:** Adjustable 0–120 V lab chargers must be verified internally and wired wall-first to avoid arc flashes across XT plugs.¹⁶

## Controller Integration Checklist

1. **Firmware parity:** Confirm both Ubox controllers run matching firmware before uploading XML profiles; mismatches lock out parameter edits until reflashed.¹⁷
2. **Thermal mounting:** Repaste controllers, hard-mount them to aluminum decks or dedicated heatsinks, and plan airflow paths. Modern Ubox aluminum singles are markedly more reliable than legacy 100 V boards, but dual units have failed when 250 A battery spikes hit inadequately cooled installs.⁶
3. **ADC accessory boards:** Log brake-light behavior and ADC V2 board health; firmware 6.0 updates have latched brake inputs after water exposure, so document reflash and diagnostic workflows.¹⁸
4. **Disable phase filters after detection:** Spintend confirmed the motor-wizard phase filter should only be used during detection.
  - leaving it active during rides reintroduces noise and ABS overcurrent faults.[^phase-filter]
4. **Hall sensors & traction:** Fit hall-equipped front motors or enable HFI only after verifying detection values; hall-less Dualtron fronts under-pull current versus sensored rears, making traction control tuning uneven.¹⁹
5. **CAN synchronization:** Balance battery and phase amps across both controllers and run proper 120 Ω termination to avoid bus faults during high-load pulls.²⁰
6. **Exploit CAN power sync:** Spintend 85-series controllers share a CAN power line, letting one ignition button wake both units once the harness is linked.
  - wire it correctly before removing redundant switches.²⁶
7. **Instrument shunt hacks before copying them.** Adjustable MOSFET shunts tied to the Eco/Turbo switch now deliver “wheelie mode” bursts on stock 10X controllers, but no one has published temperature or survivability logs.
  - and a 12 FET board already blew MOSFETs around 30 A
  - so treat the mod as experimental until documented or move to proven VESC hardware.[^5][^6]

## Mechanical & Handling Considerations

- **Stem & chassis stress:** Stock stems crack at cable ports, and legacy twin-stem frames wobble above 60 km/h without dampers, reinforced handlebars, and balanced phase currents.²¹ ²²
- **Traction control still caps real-world speed:** Even 10 kW, 72 V Ubox builds that disable traction control for tire noise stay near 60 km/h for stability, underscoring the handling ceiling of twin-stem Zero frames.[^7]
- **Damper hardware upgrades:** Print PuneDir’s steering-damper mount (Cults3D ZIP) or budget billet brackets.
  - the add-on calms high-speed shimmy without bespoke machining.[^8]
- **Spring for weight and terrain:** Track riders like 165 mm/1,500 lb rear and 135–150 mm/1,500 lb front shocks, while 70 kg commuters still prefer stiff springs for asphalt stability; heavier racers (≈78 kg) stretch to 1,800 lb combos on rougher surfaces.[^9]
- **Respect FW heat limits:** Dual-motor tunes running 60 A battery per side with 40 A FW hit ~2.8 s 0–50 km/h, but riders warn 50 H hubs overheat quickly in summer.
  - prioritise phase current and monitoring over more FW.[^10][^11]
- **Suspension & clearance:** Machined swingarm axles and upgraded pivots are required for 11" hubs; failing to rework clearances twists calipers or fouls springs.²³
- **Plan on pivot machining.** Zero 10X arms still rely on ~8 mm shafts.
  - expect lathe work or resin-printed bushings to eliminate play when refreshing pivots for high-power duty.[^12]
- **12″ conversions squeeze everything.** PuneDir’s 12″ front swap highlighted limited motor-to-spring clearance, while Paolo noted that true 11″ hubs often strike suspension hardware unless spacers are reworked.
  - measure before ordering big-wheel conversions.[^13][^14]
- **Check drivetrain assumptions.** Some regions still deliver Zero 10X as a single-motor scooter with a dummy front hub.
  - budget for a second powered wheel, harness, and controller instead of assuming dual-drive out of the box.[^15]
- **Plan fork spacing for 11″ hubs.** Paolo’s conversions needed roughly 145 mm between dropouts plus longer axles to seat 11″ 70 H motors; stock 125 mm forks top out around 65 H hubs unless you extend the swingarm or buy a kit such as FalconPEV’s.[^16][^17]
- **Budget bespoke frames for 100 km/h builds.** Riders chasing 100–105 km/h package electronics “French style” inside custom housings, often relocating controllers externally and leaning on ~22 S 11 P packs that approach 9 kW.
  - expect expensive fabrication as the tradeoff for stability at that speed.[^18]
- **FalconPEV swingarms extend 11″ builds.** Their kit gives the fork and rear end the extra length 11″ hubs need, but riders still reinforce the steering assembly to curb cracking once longer arms and high-power motors go on.[^19][^20]
- **Run dual brakes at highway speed.** Riders running 100 km/h pulls on rear-only Nutt calipers and regen keep getting warned.
  - reinstate the front hydraulic brake before more highway tuning sessions.[^21]
- **Waterproofing:** Resin-coat controller boxes or reroute harnesses—stock enclosures collect water and corrode upgrades quickly.⁴
- **Earless 85/240 mounting:** New cases still ship without tabs; plan printed brackets, retapped threads, or adhesive adapters before rough roads shake loose under-deck installs.²⁷
- **Limited edition packaging pitfalls:** The Zero 10X Limited ships dual Sabvoton controllers crammed in the deck with a secondary battery strapped to the stem, starving airflow; expect only 40–50 A before overheating unless you relocate electronics and rewire for higher-current packs.[^22][^23]

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

[^1]: Zero 10X decks shipped with 52 V 18.5 Ah packs built from Samsung 32IR cells. [^24]
[^2]: Stock pack discharge limits and chronic chassis complaints for Zero 10X-class scooters. [^25]
[^3]: Varla Eagle One (Zero 10X clone) with Ubox V2 dual controller plateauing at 60–70 km/h on the OEM battery. [^26]
[^4]: Zero 10X electronics boxes pooling water and the need for comprehensive sealing during VESC swaps. [^27]
[^5]: Community guidance that 20 S packs are the “magic number” for high-speed scooters, whereas 48–52 V builds demand disproportionate current. [^28]
[^6]: Ubox dual-controller spike failures near 250 A battery and the emphasis on improved aluminum-board reliability when adequately cooled. [^29]
[^7]: Daly smart-BMS cutoff thresholds around 2.7 V/cell and the need to align controller limits. [^30]
[^8]: QS8 short incidents during high-power builds and the reminder to upsize connectors for motorcycle-class conversions. [^31]
[^9]: Voltage vs. current discussion emphasizing 20 S as the breakpoint for top-speed goals. [^28]
[^10]: Zero 10X builders fitting 20 S7P packs with 45 mm spacers and highlighting the need for higher-grade chemistry over budget cells. [^32][^33]
[^11]: Budget cell and wiring math showing repurposed modules only supply ~40 A per half-pack. [^34]
[^12]: Holderless pack layouts with deck extenders enabling dense 20 S builds. [^32]
[^13]: Triple insulation, epoxy sheets, and careful lead routing for Zero 10X high-voltage packs. [^35][^36]
[^14]: Pack builders stacking dual G30 modules and over-insulating balance leads for Zero 10X conversions. [^37]
[^15]: Recommendation for 8 AWG equivalents on 100 A scooters and expectations when using repurposed cells. [^34]
[^16]: Adjustable charger inspection and safe connection sequence guidance. [^38]
[^17]: Firmware alignment requirements for Makerbase/Makerbase-derived boards reporting as 75_100 but needing 75_100_V2 firmware. [^39][^40]
[^18]: ADC V2 board failures causing latched brake inputs and the need for diagnostics after firmware updates. [^41]
[^19]: Dualtron front motor underperformance without hall sensors compared to sensored rears. [^42]
[^20]: Zero 10X CAN harness experiments confirming 120 Ω termination requirements. [^43]
[^21]: Reports of stems cracking at cable ports and the need for hydraulic brakes plus regen on tuned builds. [^44]
[^22]: Handling limits of Zero 10X twin-stem frames even after 10 kW upgrades, reinforcing the need for dampers and balanced currents. [^45]
[^23]: Swingarm machining requirements for 11" hub swaps and pivot upgrades. [^46][^47]
[^24]: Wheel-diameter calibration and GPS logging workflow for Zero 10X builds. [^48]
[^25]: Statorade temperature observations showing persistent case-to-sensor deltas. [^49]
[^26]: Spintend 85-series CAN power line allows a single ignition button to wake linked controllers once harnessed properly.[^50]
[^27]: Latest earless 85/240 housings forced riders to print brackets, retap threads, or glue adapters so the controllers survive long-travel suspensions.[^51]
[^phase-filter]: Phase-filter toggles exist to stabilize motor detection.
  - disable them after setup to avoid noise and ABS overcurrent faults on Spintend controllers.[^52]


## References

[^1]: Source: knowledge/notes/input_part006_review.md†L175-L175
[^2]: Source: knowledge/notes/input_part008_review.md†L15121-L15135
[^3]: Source: knowledge/notes/input_part008_review.md†L21617-L21664
[^4]: Source: knowledge/notes/input_part008_review.md†L15872-L15884
[^5]: Source: knowledge/notes/input_part006_review.md†L402-L403
[^6]: Source: knowledge/notes/input_part006_review.md†L403-L405
[^7]: Source: knowledge/notes/input_part008_review.md†L315-L315
[^8]: Source: knowledge/notes/input_part008_review.md†L14914-L14918
[^9]: Source: knowledge/notes/input_part008_review.md†L482-L488
[^10]: Source: knowledge/notes/input_part008_review.md†L15941-L15975
[^11]: Source: knowledge/notes/input_part008_review.md†L16115-L16137
[^12]: Source: knowledge/notes/input_part006_review.md†L253-L253
[^13]: Source: data/vesc_help_group/text_slices/input_part009.txt†L6281-L6299
[^14]: Source: data/vesc_help_group/text_slices/input_part009.txt†L6369-L6371
[^15]: Source: data/vesc_help_group/text_slices/input_part009.txt†L20600-L20610
[^16]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21169-L21180
[^17]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21339-L21348
[^18]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21728-L21744
[^19]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21642-L21663
[^20]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21754-L21755
[^21]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21194-L21218
[^22]: Source: data/vesc_help_group/text_slices/input_part001.txt†L2464-L2520
[^23]: Source: data/vesc_help_group/text_slices/input_part001.txt†L2489-L2519
[^24]: Source: knowledge/notes/input_part006_review.md†L179-L179
[^25]: Source: knowledge/notes/input_part006_review.md†L136-L136
[^26]: Source: knowledge/notes/input_part004_review.md†L347-L352
[^27]: Source: knowledge/notes/input_part006_review.md†L221-L229
[^28]: Source: knowledge/notes/input_part004_review.md†L357-L365
[^29]: Source: knowledge/notes/input_part004_review.md†L233-L238
[^30]: Source: knowledge/notes/input_part003_review.md†L517-L519
[^31]: Source: knowledge/notes/input_part010_review.md†L44-L52
[^32]: Source: knowledge/notes/input_part008_review.md†L13-L20
[^33]: Source: knowledge/notes/input_part008_review.md†L333-L341
[^34]: Source: knowledge/notes/input_part004_review.md†L236-L242
[^35]: Source: knowledge/notes/input_part007_review.md†L278-L285
[^36]: Source: knowledge/notes/input_part009_review.md†L18-L23
[^37]: Source: knowledge/notes/input_part007_review.md†L260-L266
[^38]: Source: knowledge/notes/input_part004_review.md†L301-L301
[^39]: Source: knowledge/notes/input_part004_review.md†L327-L327
[^40]: Source: knowledge/notes/input_part004_review.md†L479-L479
[^41]: Source: knowledge/notes/input_part004_review.md†L365-L373
[^42]: Source: knowledge/notes/input_part004_review.md†L350-L355
[^43]: Source: knowledge/notes/input_part006_review.md†L21-L27
[^44]: Source: knowledge/notes/input_part005_review.md†L283-L286
[^45]: Source: knowledge/notes/input_part008_review.md†L315-L322
[^46]: Source: knowledge/notes/input_part006_review.md†L34-L42
[^47]: Source: knowledge/notes/input_part006_review.md†L214-L222
[^48]: Source: knowledge/notes/input_part007_review.md†L368-L374
[^49]: Source: knowledge/notes/input_part004_review.md†L320-L327
[^50]: Source: knowledge/notes/input_part011_review.md†L19016-L19035
[^51]: Source: knowledge/notes/input_part012_review.md†L20537-L20587
[^52]: Source: knowledge/notes/input_part004_review.md†L31-L31
