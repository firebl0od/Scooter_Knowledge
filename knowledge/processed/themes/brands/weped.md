# Weped Performance Scooters

## Overview

Weped produces high-performance scooters targeting 100+ km/h speeds, but they require extensive quality control and upgrades to achieve their potential safely. This brand dossier covers common issues with factory builds, battery chemistry considerations, thermal management requirements, and upgrade paths for Weped GTS, Fold, and Sonic models. Understanding these platforms' strengths and weaknesses is essential before investing in premium-priced Weped hardware.

## What You'll Learn

- Required QC checks before riding (fork alignment, fasteners, wiring)
- Samsung 50E vs. high-discharge cell chemistry trade-offs
- Thermal management for dual-controller setups
- 21S pack upgrade procedures and packaging
- QS hub and Fardriver controller characteristics
- Common failure modes and prevention
- When Weped platforms make sense vs. alternatives

## Key Platform Characteristics

- Factory GTS units arrive with 16S6P Samsung 50E packs but demand comprehensive QC—fork alignment, fastener swaps, and harness inspections—before they are safe at the triple-digit speeds owners expect from 21S-class rebuilds.[^1][^2]
- The community still argues over the stock 50E chemistry: veteran Weped FS riders log 240 A peaks with minimal sag after >10 000 km, yet tuners warn the cells only behave when deployed in large parallel groups and prefer 40T/P42A for high-discharge projects.[^3]
- Thermal headroom is razor thin—sealed decks see Spintend twins crest 80 °C at ~500 A phase unless builders hard-mount controllers and feed Weped’s side-fan tunnels with serious airflow.[^4][^5]
- Sonic-era bikes ship with QS hubs and Fardriver FOC controllers, but buyers still face inconsistent after-sales support; even fans rank the Fold 3 as the only near-factory-finished chassis among Korea’s boutique frames.[^6][^7][^8]

## Platform Snapshot

| Focus | Stock Insight | Upgrade & Watchouts |
| --- | --- | --- |
| Powertrain | Recent Sonic deliveries arrive with QS hub motors paired to Fardriver controllers, keeping costs lower than dual-VESC race builds while preserving strong launch torque.[^6] | VESC conversions promise finer tuning but require custom cooling ducts and deck machining before pitching the idea to Weped’s OEM contacts.[^9] |
| Battery module | Production GTS/Fold packs are 16S6P 50E assemblies that survive high mileage when left largely stock.[^1][^3] | Race builds chase 21S11P Molicel layouts for 140 km/h targets; plan pack height, BMS placement, and wiring for the added cells before cutting decks.[^2] |
| Cooling & packaging | OEM housings rely on forced-air side tunnels to keep electronics alive at speed.[^5] | Dual Spintend or similar installs need bare-metal mounting, fresh thermal paste, and potentially external heatsinks to stay below thermal shutdown.[^10] |
| Quality & support | Premium price tags hide budget cockpit parts and inconsistent service; even loyalists treat new deliveries as kits that require teardown.[^11][^8] | Maintain detailed punch lists for fork, stem, and wiring work so customers understand the scope before the scooter ever hits pavement.[^1] |

## Battery Strategy & Electrical Guardrails
### OEM Pack Baseline

Weped’s factory 16S6P Samsung 50E battery ships on the GTS and Fold series, but seasoned builders open the deck immediately to realign forks, lengthen hardware, and reseat harnesses before trusting the scooter at its advertised speed envelope.[^1] The same chassis readily accepts 21S11P Molicel upgrades for 140 km/h projects, yet those packs consume precious deck height and require advance planning for BMS placement and strain relief.[^2]

### Chemistry Debates & Parallel Scaling

Despite the criticism, Yoann’s four-year-old Weped FS still peaks 240 A on the original 50E module with an ANT smart BMS, demonstrating that the cells can deliver when backed by large parallel strings and conservative thermal management.[^3] Builders chasing harder acceleration prefer Samsung 40T or Molicel P42A/P45B packs once current demands exceed what 50E chemistry tolerates per cell, treating the OEM block as a long-range option rather than a high-discharge foundation.[^3]
- Treat Samsung 50E cells as ~10 A parts—pushing 15 A per cell drives them toward 70 °C within minutes, mirroring the stock 16 S6 P Weped pack’s limits unless you add aggressive cooling.[^ip001-50e-limit]

### BMS, Regen & Controller Survivability

Front-end controller failures on the Weped Wepoor show how sensitive the platform is to BMS behavior: repeated deaths occurred at only 200 A battery / 300 A phase, with the owner suspecting ANT BMS cutoffs or regen spikes after dead-stop launches despite cool temps.[^12] Keep regen well inside the charge FET’s comfort zone, verify ANT or JK boards leave both charge and discharge channels enabled, and log BMS data during launch tests so you can correlate faults with pack events.

## Drivetrain, Controllers & Upgrades
### Stock & Semi-Stock Options

The latest Sonic runs with QS-manufactured hubs and Fardriver controllers, a combination that racers view as the budget alternative to fragile high-power VESC stacks while still offering serious output headroom.[^6][^13][^7] Owners considering VESC conversions should arrive at Weped’s door with cooling plans, because the stock enclosure needs rework to house larger heatsinks or external mounts without cooking the electronics.[^9]

### High-Power Motor Paths

Rage Mechanics’ 75 mm stator hubs remain the go-to race upgrade, pushing well past 10 kW per wheel on Weped frames but costing about €650 each and demanding careful axle-width planning.[^14] Builders on tighter budgets can still source Rion/Weped FF-spec motors around €340 in France, though freight costs quickly erode the savings for overseas buyers.[^15] Pair these motors with the aforementioned 21S packs to unlock the 140 km/h envelope already mapped out for upcoming Weped SS projects.[^2]

## Thermal Management & Mechanical Prep

Sealed decks leave almost no thermal margin: dual Spintend installs logged ~500 A phase and 80 °C controller temps until owners sanded paint from the deck, applied quality thermal paste, and bolted the housings directly to the frame.[^10] Even the OEM layout assumes aggressive airflow—paired 30 Ah 40T packs feed opposing side fans at roughly 145 km/h to keep electronics alive, so any stealth conversion must preserve or improve that ducting.[^5] Plan for external heatsinks, repaste jobs, and fan redundancy before lifting current limits.
- Wepoor owners are now hunting machinists to shave aftermarket fin stacks so Spintend stages can mount flush; removing a fin creates a bolt strip, and direct-to-heatsink installs cool better than remote brackets once insulation checks pass.[^wepoor_fins_trim]

## Handling & Rider Feedback

- Paolo still praises the Rion RX2000 for running stable near 100 km/h without a damper, whereas Face de Pin Sucé finds the chassis twitchy compared with Weped builds and argues the oversized Weped columns pay off once paired with PMT tires for corner grip—factor rider preference into cockpit upgrades rather than chasing a single “best” setup.[^16]

## Quality, Support & Delivery Reality

Community audits describe new Wepeds as expensive kits: owners routinely replace bargain switches, Zoom brakes, and flimsy stems despite €3–4 k invoices, treating the chassis as the only real value-add.[^11] Customer service isn’t much better—Paolo notes Weped’s support remains inconsistent even as prices climb, while racers consider the Fold 3 the lone chassis that arrives close to track-ready without reinforcement.[^8] Expect to document every correction for clients, including fork bearing work, steering column alignment, and fastener swaps.

## Procurement & Planning Notes

- **Motor sourcing:** Rage Mechanics and other boutique suppliers can still deliver Weped-spec hubs, but lead times and freight swing wildly—budget extra for customs and verify axle widths before ordering.[^14][^15]
- **Partnership outreach:** When pitching VESC-based drivetrains to Weped, arrive with enclosure redesigns and cooling analysis; the factory expects partners to shoulder housing rework in exchange for adopting open hardware.[^9]
- **Future builds:** Planned SS upgrades targeting 140 km/h already have 21S11P pack dimensions and controller selections scoped—use these benchmarks to sanity-check customer requests before committing to fabrication timelines.[^2]

## Build Checklist

1. **Strip & inspect the chassis** – realign forks, torque the stem, and document any hardware replacements before the first ride so clients understand the baseline.[^1][^11]
2. **Model the energy system** – decide whether the OEM 50E block meets the use case or if a parallel-heavy 40T/P42A pack is required; budget deck spacers and harness routing accordingly.[^3][^2]
3. **Engineer cooling paths** – hard-mount controllers with quality TIM, preserve side-fan airflow, and log temps during shakedowns before raising current limits.[^10][^5]
4. **Validate BMS behavior** – confirm charge/discharge FET states, regen thresholds, and fault logs to prevent the ANT-induced controller deaths observed on recent Wepoor builds.[^12]
5. **Plan sourcing & support** – lock in motor suppliers, document lead times, and set expectations about Weped’s limited after-sales help ahead of any customer-facing commitments.[^14][^8]

## Source Notes

[^1]: Factory GTS/Fold pack configuration and required pre-delivery rework. Source: knowledge/notes/input_part001_review.md, L24 to L25
[^2]: Planned 21S11P upgrades for Weped SS high-speed builds. Source: knowledge/notes/input_part000_review.md, L717 to L717
[^3]: Long-term 50E performance data and chemistry debates on Weped FS builds. Source: knowledge/notes/input_part007_review.md, L286 to L286
[^4]: Dual Spintend thermal logs inside Weped decks at ~500 A phase. Source: knowledge/notes/input_part000_review.md, L610 to L614
[^5]: OEM fan-assisted cooling layout on high-speed Wepeds. Source: knowledge/notes/input_part007_review.md, L26 to L26
[^6]: Sonic deliveries with QS hubs and Fardriver controllers plus European sightings. Source: knowledge/notes/input_part006_review.md, L195 to L195. Source: knowledge/notes/input_part007_review.md, L395 to L395
[^7]: Weped service reputation and Fold 3 chassis quality assessments. Source: knowledge/notes/input_part009_review.md, L75 to L76
[^8]: Premium pricing contrasted with bargain-spec cockpit hardware on shipped units. Source: knowledge/notes/input_part001_review.md, L787 to L787
[^9]: Guidance to approach Weped about VESC integration with revised cooling plans. Source: knowledge/notes/input_part010_review.md, L354 to L354
[^10]: Repeated controller failures on a Weped Wepoor linked to suspected ANT BMS/regen events. Source: knowledge/notes/input_part011_review.md, L227 to L229
[^wepoor_fins_trim]: Source: data/vesc_help_group/text_slices/input_part011.txt, L20866 to L20903; L21313 to L21319; L21504 to L21518
[^11]: Rage Mechanics and FF-spec motor sourcing costs for Weped platforms. Source: knowledge/notes/input_part000_review.md, L449 to L449. Source: knowledge/notes/input_part000_review.md, L698 to L698

## References

[^1]: Source: knowledge/notes/input_part001_review.md, L24 to L25
[^2]: Source: knowledge/notes/input_part000_review.md, L717 to L717
[^3]: Source: knowledge/notes/input_part007_review.md, L286 to L286
[^4]: Source: knowledge/notes/input_part000_review.md, L610 to L614
[^5]: Source: knowledge/notes/input_part007_review.md, L26 to L26
[^6]: Source: knowledge/notes/input_part006_review.md, L195 to L195
[^7]: Source: knowledge/notes/input_part007_review.md, L395 to L395
[^8]: Source: knowledge/notes/input_part009_review.md, L75 to L76
[^9]: Source: knowledge/notes/input_part010_review.md, L354 to L354
[^10]: Source: knowledge/notes/input_part000_review.md, L610 to L615
[^11]: Source: knowledge/notes/input_part001_review.md, L787 to L787
[^12]: Source: knowledge/notes/input_part011_review.md, L227 to L229
[^13]: Source: knowledge/notes/input_part007_review.md, L40 to L40
[^14]: Source: knowledge/notes/input_part000_review.md, L449 to L449
[^15]: Source: knowledge/notes/input_part000_review.md, L698 to L698
[^16]: Source: knowledge/notes/input_part001_review.md, L51 to L52
[^ip001-50e-limit]: Source: data/vesc_help_group/text_slices/input_part001.txt†L26670-L26700
