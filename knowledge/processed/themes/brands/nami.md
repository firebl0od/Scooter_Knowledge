# NAMI Electric Scooters Brand Dossier

## TL;DR
- Dual-motor load sharing keeps Tronic 250-equipped NAMI builds under ~40 °C on steep climbs, while single-drive hill assaults crest ~60 °C—treat high-power setups as two-controller platforms to stay within thermal margins.[^1]
- The stock 40 Ah module’s eight-way LG M50LT parallel pack is happiest below ~135 A; community pushes toward 200 A/310 A phase quickly overheat hubs and batteries unless the pack is rebuilt and monitored closely.[^2]
- High-speed composure depends on real suspension and damper hardware: NAMI frames reward elastomer blocks plus quality Bitubo-class dampers, whereas cheap AliExpress units snap under race preload.[^3]
- Race-prepped 65H motors already touch ~100 km/h without field-weakening, and GT2 owners have proven 26 S compatibility when controllers and logging are squared away—voltage headroom is no longer the bottleneck.[^4]
- Hotdog builds pairing 100 H rears with 70 H fronts now run 22 S 11 P P45 packs at ≈500 A phase / 550 A absolute, relying on 100 % front FW and aggressive traction control because the rear will lift the front wheel even at 120 km/h despite ~61 °C stator temps.[^hotdog]

## Platform Snapshot
| Focus | Stock Insight | Upgrade Levers |
| --- | --- | --- |
| Wiring & connectors | OEM looms arrive with 6 mm motor bullets, XT90 battery plugs, and durable Higo shells—solid enough for ~200 A phase before upgrades.[^5] | Flatten 6 mm bullets or jump to XT150/QS8 harnesses when targeting higher battery currents or swapping in boutique controllers.[^5] |
| Battery module | GT2 riders document the factory 20 S 9 P LG 40P pack on Daly’s 100Balance BMS, good for ≈225 A bursts with 0.2 mm copper busbars.[^6] | Repack with higher-grade cells or parallel aux packs only after validating thermal spread and BMS headroom.[^2][^3] |
| Controller envelope | Daily riders have restored dual traction on 26 S packs by pairing stock motors with Makerbase X12-class controllers.[^7] | Stealth conversions swap in dual Spintend Lite 100 V/100 A units while retaining the OEM BMS and dash wiring.[^8] |
| Performance baseline | Track builds see ~100 km/h without FW on 65H motors when chassis and tires are dialed.[^4] | Aggregate both controller logs to break past ~19 kW plateaus and verify real system output before chasing higher limits.[^9] |

## Chassis & Handling Priorities
- Keep the platform in its comfort lane: riders still rank Dualtron Thunder geometry for >150 km/h sprints, while NAMI frames shine for long-range and off-road duty when paired with good dampers instead of chasing absolute top speed.[^3]
- Budget steering dampers snap when preloaded for race pace; invest in motorcycle-grade Bitubo or similar hardware before upping currents and tire width.[^10]
- Aftermarket shocks rarely match the Viper’s leverage curve—most MTB units feel nearly solid, so owners are still hunting purpose-built dampers instead of relying on drop-in swaps.【F:knowledge/notes/input_part006_review.md†L97-L97】
- Fabrication escalates quickly—22 S 10 P hybrids inspired by Rion builds required fork machining to clear 70H hubs and 3 mm rotors, so plan machine time before ordering oversized drivetrains.[^11]

## Power & Thermal Guardrails
- Favor dual-drive current splits: the same Tronic 250 hardware that bakes at ~60 °C as a single motor holds near 40 °C when the load is shared across both ends.[^1]
- Treat 200 A battery / 310 A phase experiments as short-lived: even purpose-built dual Spintend setups report hub and pack overheating at those levels.[^2]
- Respect the stock module’s ≈116 A continuous ceiling—AYÓ advises capping peaks near 135 A until the pack is rebuilt or paralleled.[^2]
- Data logging must sum both controllers; otherwise, power traces plateau near 19 kW even while riders believe they’re pushing 170 A/200 A per side.[^9]
- Track NAMI builds already touch triple digits on 65H motors without FW; spend effort on tire compound, suspension balance, and braking instead of chasing voltage for speed alone.[^4]
- Hotdog-class 100 H rears paired with 70 H fronts survive 500 A phase pulls when fed by 22 S 11 P P45 packs, but only with traction control engaged and front-motor FW at 100 % to match wheel speed—expect front-wheel lift at 120 km/h if TC is disabled.[^hotdog]

## Battery Strategy & Pack Building
- Documented GT2 rebuilds pair 20 S 9 P LG 40P packs with Daly smart BMS hardware and thick copper busbars—use this as a template when refreshing commuter modules.[^6]
- Mixed-chemistry packs (LG 40T + LG M50LT) demand conservative discharge ceilings and a robust 150 A smart BMS to keep 4 Ah and 5 Ah sticks in balance; many veterans still discourage blending chemistries at all.[^3]
- OEM BMS retention is viable: Yoann’s customer conversion kept the NAMI BMS while adding dual Spintend Lite controllers for cleaner throttle response without altering the scooter’s appearance.[^8]
- When aiming beyond stock output, log pack temperatures alongside controller data—Omar’s 20 S 10 P 50S build overheated both hubs and cells at 200 A battery, 310 A phase, and 380 A ABS.[^2]
- Yamal’s 22 S 11 P 50PL concept highlights today’s BMS bottleneck—compact smart boards still cap around 500 A continuous, so dual-BMS or pyrofuse plans belong in the design once current heads toward 770 A nominal.[^bms_ceiling]

## Electronics & Accessory Integration
- Start with the proven harness baseline—6 mm bullets and XT90 battery plugs—and only upsize once current goals justify the extra packaging work.[^5]
- Avoid hanging full lighting loads directly off controller accessories: horn outputs only source a few amps, so trigger relays or separate DC/DC rails for halogens and other heavy draws.[^12]
- Document accessory power paths before splicing dashboards or smart displays; riders are still mapping which 5 V/12 V rails share regulators on Ubox and Makerbase logic stages.[^13]

## Reliability Watchlist
- First-generation frames have shown weld cracking; later 72/40 chassis add gussets, giving buyers a visual checklist when sourcing used NAMI decks.[^14]
- Handmade 22 S hybrids need machine work and inspection of fork clearances, and water sealing should be rechecked whenever machining exposes fresh metal.[^11]
- High-voltage experiments above stock (26 S or more) demand validated controllers—confirm CAN, throttle, and hall health before blaming firmware for traction loss.[^7]
- Avoid 12" AliExpress rim swaps without suspension mods—the community expects spring interference and rubbing, so 65 mm front / 80 mm rear LY combinations remain the safe default for wide-hub conversions.[^rim_warning]
- Tubeless Ambrosini rims can burp air after potholes; reseat by pulling the valve core, blasting the bead with a compressor, and cleaning debris before reinflating.[^burp_fix]

## Tires & Wheel Fitment
- PMT’s rain tread in 90 mm and 100 mm widths costs about $80 per tire but remains the go-to upgrade when riders need wet grip over cheaper slicks.[^pmt_rain]


## Build Checklist for New NAMI Projects
1. **Audit the harness** – verify all 6 mm bullets are fully seated, confirm XT90 condition, and plan any XT150/QS8 upgrades before reassembly.[^5]
2. **Baseline the pack** – log temperature and sag on the stock LG M50LT module before chasing new current limits; schedule a rebuild if peaks exceed ~135 A.[^2]
3. **Spec the damper** – install a motorcycle-grade unit and check elastomer blocks before pushing wider tires or higher speed profiles.[^3][^10]
4. **Plan accessory power** – route horns, lights, and smart displays through relays or dedicated converters instead of relying on controller aux rails.[^12][^13]
5. **Aggregate telemetry** – configure logging on both controllers so power, temperature, and fault data capture the full system during tuning sessions.[^9]

## Source Notes
[^1]: Dual vs. single-drive thermal observations on Tronic 250-equipped NAMI builds.【F:knowledge/notes/input_part008_review.md†L24-L31】
[^2]: Omar’s 200 A/310 A Spintend build overheating hubs and AYÓ’s reminder about the stock LG M50LT pack’s ≈116 A continuous rating with ≤135 A peak guidance.【F:knowledge/notes/input_part013_review.md†L118-L123】
[^3]: Mixed-chemistry caution, chassis use-cases, and handling priorities for NAMI frames versus other race platforms.【F:knowledge/notes/input_part008_review.md†L188-L190】【F:knowledge/notes/input_part008_review.md†L227-L236】
[^4]: 65H track benchmarks near 100 km/h without field weakening and 26 S dual-motor success restoring traction on GT2 builds.【F:knowledge/notes/input_part012_review.md†L103-L107】【F:knowledge/notes/input_part011_review.md†L204-L218】
[^5]: OEM connector specifications and upgrade practices for NAMI scooters.【F:knowledge/notes/input_part002_review.md†L430-L445】
[^6]: GT2 pack rebuild using Daly 100Balance BMS, 20 S 9 P LG 40P cells, and copper busbars.【F:knowledge/notes/input_part011_review.md†L204-L206】
[^7]: NAMI GT2 running 26 S packs again with stock motors and Makerbase X12 controllers online.【F:knowledge/notes/input_part011_review.md†L204-L218】
[^8]: Yoann’s stealth dual Spintend Lite conversion retaining the NAMI BMS and stock exterior.【F:knowledge/notes/input_part009_review.md†L253-L256】
[^9]: Dual-controller power logging plateau around 19 kW without aggregated telemetry.【F:knowledge/notes/input_part013_review.md†L454-L459】
[^10]: Reports of cheap steering dampers failing and recommendations for motorcycle-grade replacements on NAMI chassis.【F:knowledge/notes/input_part008_review.md†L293-L296】
[^11]: Fabrication needs when merging NAMI Viper and Rion components for 22 S 10 P builds.【F:knowledge/notes/input_part008_review.md†L205-L208】
[^12]: Controller horn/aux channels sourcing only a few amps—relay heavy lighting loads instead of direct wiring.【F:knowledge/notes/input_part012_review.md†L96-L99】
[^13]: Accessory-rail documentation gaps and current-limit questions on Ubox 85240/85250 harnesses.【F:knowledge/notes/input_part013_review.md†L116-L130】
[^14]: Visual differences between cracked first-gen NAMI frames and reinforced 72/40 chassis.【F:knowledge/notes/input_part012_review.md†L129-L132】
[^hotdog]: Latest NAMI hotdog builds with 100 H rears and 70 H fronts running 22 S 11 P P45 packs, 500 A phase / 550 A absolute limits, 100 % front FW, and ~61 °C stator temps while traction control prevents front-wheel lift beyond 120 km/h.【F:knowledge/notes/input_part014_review.md†L8930-L8933】【F:knowledge/notes/input_part014_review.md†L10001-L10055】
[^bms_ceiling]: 22 S 11 P 50PL pack planning noting today’s smart BMS hardware caps ≈500 A continuous, requiring dual-BMS or pyrofuse strategies when targeting ≈770 A nominal current.【F:knowledge/notes/input_part014_review.md†L2965-L2974】【F:knowledge/notes/input_part014_review.md†L3427-L3434】
[^rim_warning]: Community warning that 12" AliExpress rims interfere with NAMI suspension, so 65 mm front / 80 mm rear LY combos remain the preferred setup.【F:knowledge/notes/input_part014_review.md†L5103-L5113】
[^burp_fix]: Tubeless Ambrosini rims occasionally burp air after potholes; reseat by pulling the valve core and blasting the bead clean with a compressor.【F:knowledge/notes/input_part014_review.md†L4610-L4619】
[^pmt_rain]: PMT rain-specific tires in 90 mm and 100 mm widths cost roughly $80 each but deliver the wet grip racers need versus cheaper slicks.【F:knowledge/notes/input_part014_review.md†L5359-L5399】
