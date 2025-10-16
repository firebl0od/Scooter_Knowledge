# NAMI Electric Scooters Brand Dossier

## TL;DR

- Dual-motor load sharing keeps Tronic 250-equipped NAMI builds under ~40 °C on steep climbs, while single-drive hill assaults crest ~60 °C—treat high-power setups as two-controller platforms to stay within thermal margins.[^1]
- The stock 40 Ah module’s eight-way LG M50LT parallel pack is happiest below ~135 A; community pushes toward 200 A/310 A phase quickly overheat hubs and batteries unless the pack is rebuilt and monitored closely.[^2]
- Factory trims matter: the 28 Ah models still ship 1 000 W hubs while the 32–40 Ah versions step up to 1 500 W motors, and crews are now targeting 35–40 kW combined output for the next wave of VESC swaps.[^1]
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
- Aftermarket shocks rarely match the Viper’s leverage curve—most MTB units feel nearly solid, so owners are still hunting purpose-built dampers instead of relying on drop-in swaps.[^2]
- Aftermarket shocks rarely match the Viper’s leverage curve—most MTB units feel nearly solid, so owners are still hunting purpose-built dampers instead of relying on drop-in swaps.[^3]
- Track chassis revisions before trusting hand-me-down frames: V1 “Pringle” necks shipped without reinforcement, mid-generation updates added a metal battery box plus thicker side plates, and the latest “Tesla reinforcement” necks have survived 20 k+ miles once braced—inspect welds before pushing highway power.[^4]
- Fabrication escalates quickly—22 S 10 P hybrids inspired by Rion builds required fork machining to clear 70H hubs and 3 mm rotors, so plan machine time before ordering oversized drivetrains.[^11]
- Kaabo fork swaps remain largely cosmetic: the community confirmed 70 H hubs fit but 75 H is doubtful without extra machining, so most riders stick with stock hardware unless aesthetics trump effort.[^kaabo-swap]
- Riders chasing stiffer suspension for high-speed runs keep circling back to the stock springs—most aftermarket air shocks run too soft and short, so meaningful firmness gains require sourcing the stiffest factory-rate springs and tuning damping instead.[^5]

## Power & Thermal Guardrails

- Paolo now caps motor phase near 200–250 A unless you rewire with shorter, larger-gauge leads; the stock PTFE insulation looks thin but sheds heat better than silicone, so verify cross-section before tearing harnesses apart.[^6]
- Catalog hub winds before tuning: stock 60 H cans are usually 17/4 torque windings, while 22/3 and 33/2 variants trade torque for speed. Paolo reminded builders the notation is “turns × parallels,” so document wind counts or freewheel speed when spec sheets are missing.[^7]
- Favor dual-drive current splits: the same Tronic 250 hardware that bakes at ~60 °C as a single motor holds near 40 °C when the load is shared across both ends.[^1]
- Upgrade overheated harnesses with 10 AWG silicone phase leads—the swap let Rob Ver hold 116 A battery and 240 A phase without cooking the loom, provided pack and controller temps stayed logged.[^tronic_harness]
- Treat 200 A battery / 310 A phase experiments as short-lived: even purpose-built dual Spintend setups report hub and pack overheating at those levels.[^2]
- Respect the stock module’s ≈116 A continuous ceiling—AYÓ advises capping peaks near 135 A until the pack is rebuilt or paralleled.[^2]
- Data logging must sum both controllers; otherwise, power traces plateau near 19 kW even while riders believe they’re pushing 170 A/200 A per side.[^9]
- Track NAMI builds already touch triple digits on 65H motors without FW; spend effort on tire compound, suspension balance, and braking instead of chasing voltage for speed alone.[^4]
- Hotdog-class 100 H rears paired with 70 H fronts survive 500 A phase pulls when fed by 22 S 11 P P45 packs, but only with traction control engaged and front-motor FW at 100 % to match wheel speed—expect front-wheel lift at 120 km/h if TC is disabled.[^hotdog]
- 🇪🇸AYO#74 is testing whether stock 72 V controllers stay happy on a homemade 60 V pack by rewiring phase leads—down-voltage behaviour remains unproven, so log carefully before committing a commuter build.[^8]

## Battery Strategy & Pack Building

- Documented GT2 rebuilds pair 20 S 9 P LG 40P packs with Daly smart BMS hardware and thick copper busbars—use this as a template when refreshing commuter modules.[^6]
- A Chilean Blast Max mule now runs roughly 59 Ah by pairing the stock 35 Ah Panasonic deck with a 24 Ah SunPower bag; the crew only kept the add-on after securing it with foam and Velcro because earlier loose packs battered cells in the frame.[^9]
- Mixed-chemistry packs (LG 40T + LG M50LT) demand conservative discharge ceilings and a robust 150 A smart BMS to keep 4 Ah and 5 Ah sticks in balance; many veterans still discourage blending chemistries at all.[^3]
- OEM BMS retention is viable: Yoann’s customer conversion kept the NAMI BMS while adding dual Spintend Lite controllers for cleaner throttle response without altering the scooter’s appearance.[^8]
- When aiming beyond stock output, log pack temperatures alongside controller data—Omar’s 20 S 10 P 50S build overheated both hubs and cells at 200 A battery, 310 A phase, and 380 A ABS.[^2]
- Yamal’s 22 S 11 P 50PL concept highlights today’s BMS bottleneck—compact smart boards still cap around 500 A continuous, so dual-BMS or pyrofuse plans belong in the design once current heads toward 770 A nominal.[^bms_ceiling]

## Electronics & Accessory Integration

- Start with the proven harness baseline—6 mm bullets and XT90 battery plugs—and only upsize once current goals justify the extra packaging work.[^5]
- Budget separate DC/DC rails for heavy accessories: Tronic X12 logic supplies only ~150 mA at 5 V, so horns, fans, and dashboards still need dedicated bucks on high-current NAMI builds.[^tronic_logic]
- Avoid hanging full lighting loads directly off controller accessories: horn outputs only source a few amps, so trigger relays or separate DC/DC rails for halogens and other heavy draws.[^12]
- Document accessory power paths before splicing dashboards or smart displays; riders are still mapping which 5 V/12 V rails share regulators on Ubox and Makerbase logic stages.[^13]

## Reliability Watchlist

- Early production stems still ship with the softer front axle—🇪🇸AYO#74 recommends swapping to the stainless replacement (≈€60 installed) to avoid the stem failures that triggered factory recalls.[^10]
- First-generation frames have shown weld cracking; later 72/40 chassis add gussets, giving buyers a visual checklist when sourcing used NAMI decks.[^14]
- Handmade 22 S hybrids need machine work and inspection of fork clearances, and water sealing should be rechecked whenever machining exposes fresh metal.[^11]
- Race outfits have started enclosing the C350 controller in custom waterproof housings—Face de Pin’s crew was the only team still lapping Albaida once rain hit and now machines most of their replacement frame parts in-house—reinforcing that sealing electronics and reinforcing hinges is essential before endurance sessions.[^c350-case]
- High-voltage experiments above stock (26 S or more) demand validated controllers—confirm CAN, throttle, and hall health before blaming firmware for traction loss.[^7]
- Avoid 12" AliExpress rim swaps without suspension mods—the community expects spring interference and rubbing, so 65 mm front / 80 mm rear LY combinations remain the safe default for wide-hub conversions.[^rim_warning]
- Tubeless Ambrosini rims can burp air after potholes; reseat by pulling the valve core, blasting the bead with a compressor, and cleaning debris before reinflating.[^burp_fix]
- If the dash shows 84.5 V at startup with no throttle, inspect the ADC divider and recalibrate voltage sensing—the control board may misreport pack voltage even when the charger caps at 83.6 V.[^11]

## Tires & Wheel Fitment

- PMT’s rain tread in 90 mm and 100 mm widths costs about $80 per tire but remains the go-to upgrade when riders need wet grip over cheaper slicks.[^pmt_rain]

## Build Checklist for New NAMI Projects

1. **Audit the harness** – verify all 6 mm bullets are fully seated, confirm XT90 condition, and plan any XT150/QS8 upgrades before reassembly.[^5]
2. **Baseline the pack** – log temperature and sag on the stock LG M50LT module before chasing new current limits; schedule a rebuild if peaks exceed ~135 A.[^2]
3. **Spec the damper** – install a motorcycle-grade unit and check elastomer blocks before pushing wider tires or higher speed profiles.[^3][^10]
4. **Plan accessory power** – route horns, lights, and smart displays through relays or dedicated converters instead of relying on controller aux rails.[^12][^13]
5. **Aggregate telemetry** – configure logging on both controllers so power, temperature, and fault data capture the full system during tuning sessions.[^9]

## Source Notes

[^1]: Dual vs. single-drive thermal observations on Tronic 250-equipped NAMI builds.Source: knowledge/notes/input_part008_review.md, L24 to L31
[^2]: Omar’s 200 A/310 A Spintend build overheating hubs and AYÓ’s reminder about the stock LG M50LT pack’s ≈116 A continuous rating with ≤135 A peak guidance.Source: knowledge/notes/input_part013_review.md, L118 to L123
[^3]: Mixed-chemistry caution, chassis use-cases, and handling priorities for NAMI frames versus other race platforms.Source: knowledge/notes/input_part008_review.md, L188 to L190Source: knowledge/notes/input_part008_review.md, L227 to L236
[^4]: 65H track benchmarks near 100 km/h without field weakening and 26 S dual-motor success restoring traction on GT2 builds.Source: knowledge/notes/input_part012_review.md, L103 to L107Source: knowledge/notes/input_part011_review.md, L204 to L218
[^5]: OEM connector specifications and upgrade practices for NAMI scooters.Source: knowledge/notes/input_part002_review.md, L430 to L445
[^6]: GT2 pack rebuild using Daly 100Balance BMS, 20 S 9 P LG 40P cells, and copper busbars.Source: knowledge/notes/input_part011_review.md, L204 to L206
[^7]: NAMI GT2 running 26 S packs again with stock motors and Makerbase X12 controllers online.Source: knowledge/notes/input_part011_review.md, L204 to L218
[^8]: Yoann’s stealth dual Spintend Lite conversion retaining the NAMI BMS and stock exterior.Source: knowledge/notes/input_part009_review.md, L253 to L256
[^9]: Dual-controller power logging plateau around 19 kW without aggregated telemetry.Source: knowledge/notes/input_part013_review.md, L454 to L459
[^10]: Reports of cheap steering dampers failing and recommendations for motorcycle-grade replacements on NAMI chassis.Source: knowledge/notes/input_part008_review.md, L293 to L296
[^11]: Fabrication needs when merging NAMI Viper and Rion components for 22 S 10 P builds.Source: knowledge/notes/input_part008_review.md, L205 to L208
[^12]: Controller horn/aux channels sourcing only a few amps—relay heavy lighting loads instead of direct wiring.Source: knowledge/notes/input_part012_review.md, L96 to L99
[^13]: Accessory-rail documentation gaps and current-limit questions on Ubox 85240/85250 harnesses.Source: knowledge/notes/input_part013_review.md, L116 to L130
[^14]: Visual differences between cracked first-gen NAMI frames and reinforced 72/40 chassis.Source: knowledge/notes/input_part012_review.md, L129 to L132
[^kaabo-swap]: NAMI riders debating Kaabo fork swaps concluded the mod is mostly for looks—70 H motors fit, but 75 H clearance is uncertain without extra machining.Source: knowledge/notes/input_part009_review.md, L228 to L233
[^c350-case]: Face de Pin Sucé’s race team sealed their NAMI’s C350 in a custom waterproof enclosure, kept lapping Albaida in the rain, and now machines most replacement frame parts in-house to shore up Thunder-family hinges.Source: data/vesc_help_group/text_slices/input_part009.txt, L22034 to L22072
[^hotdog]: Latest NAMI hotdog builds with 100 H rears and 70 H fronts running 22 S 11 P P45 packs, 500 A phase / 550 A absolute limits, 100 % front FW, and ~61 °C stator temps while traction control prevents front-wheel lift beyond 120 km/h.Source: knowledge/notes/input_part014_review.md, L8930 to L8933Source: knowledge/notes/input_part014_review.md, L10001 to L10055
[^bms_ceiling]: 22 S 11 P 50PL pack planning noting today’s smart BMS hardware caps ≈500 A continuous, requiring dual-BMS or pyrofuse strategies when targeting ≈770 A nominal current.Source: knowledge/notes/input_part014_review.md, L2965 to L2974Source: knowledge/notes/input_part014_review.md, L3427 to L3434
[^rim_warning]: Community warning that 12" AliExpress rims interfere with NAMI suspension, so 65 mm front / 80 mm rear LY combos remain the preferred setup.Source: knowledge/notes/input_part014_review.md, L5103 to L5113
[^burp_fix]: Tubeless Ambrosini rims occasionally burp air after potholes; reseat by pulling the valve core and blasting the bead clean with a compressor.Source: knowledge/notes/input_part014_review.md, L4610 to L4619
[^pmt_rain]: PMT rain-specific tires in 90 mm and 100 mm widths cost roughly $80 each but deliver the wet grip racers need versus cheaper slicks.Source: knowledge/notes/input_part014_review.md, L5359 to L5399
[^tronic_harness]: Rob Ver’s harness refresh swapped the NAMI loom to 10 AWG phases so dual Tronic X12 controllers could sustain 116 A battery and 240 A phase without overheating.Source: knowledge/notes/input_part013_review.md, L33 to L33
[^tronic_logic]: Tronic X12 accessory rails only deliver about 5 V at 150 mA, so builders still power horns and lighting from dedicated buck converters.Source: knowledge/notes/input_part013_review.md, L32 to L33

## References

[^1]: Source: knowledge/notes/input_part010_review.md, L282 to L283
[^2]: Source: knowledge/notes/input_part006_review.md, L136 to L136
[^3]: Source: knowledge/notes/input_part006_review.md, L97 to L97
[^4]: Source: knowledge/notes/input_part009_review.md, L385 to L385
[^5]: Source: knowledge/notes/input_part010_review.md, L56 to L57
[^6]: Source: knowledge/notes/input_part009_review.md, L309 to L310
[^7]: Source: knowledge/notes/input_part010_review.md, L339 to L341
[^8]: Source: knowledge/notes/input_part010_review.md, L185 to L186
[^9]: Source: knowledge/notes/input_part006_review.md, L387 to L387
[^10]: Source: data/vesc_help_group/text_slices/input_part010.txt, L10386 to L10394
[^11]: Source: knowledge/notes/input_part011_review.md, L394 to L395
