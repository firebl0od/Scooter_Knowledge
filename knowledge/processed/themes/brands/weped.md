# Weped Performance Scooter Brand Dossier

## TL;DR
- Factory GTS units arrive with 16S6P Samsung 50E packs but demand comprehensive QC—fork alignment, fastener swaps, and harness inspections—before they are safe at the triple-digit speeds owners expect from 21S-class rebuilds.【F:knowledge/notes/input_part001_review.md†L24-L25】【F:knowledge/notes/input_part000_review.md†L717-L717】
- The community still argues over the stock 50E chemistry: veteran Weped FS riders log 240 A peaks with minimal sag after >10 000 km, yet tuners warn the cells only behave when deployed in large parallel groups and prefer 40T/P42A for high-discharge projects.【F:knowledge/notes/input_part007_review.md†L286-L286】
- Thermal headroom is razor thin—sealed decks see Spintend twins crest 80 °C at ~500 A phase unless builders hard-mount controllers and feed Weped’s side-fan tunnels with serious airflow.【F:knowledge/notes/input_part000_review.md†L610-L614】【F:knowledge/notes/input_part007_review.md†L26-L26】
- Sonic-era bikes ship with QS hubs and Fardriver FOC controllers, but buyers still face inconsistent after-sales support; even fans rank the Fold 3 as the only near-factory-finished chassis among Korea’s boutique frames.【F:knowledge/notes/input_part006_review.md†L195-L195】【F:knowledge/notes/input_part007_review.md†L395-L395】【F:knowledge/notes/input_part009_review.md†L75-L76】

## Platform Snapshot
| Focus | Stock Insight | Upgrade & Watchouts |
| --- | --- | --- |
| Powertrain | Recent Sonic deliveries arrive with QS hub motors paired to Fardriver controllers, keeping costs lower than dual-VESC race builds while preserving strong launch torque.【F:knowledge/notes/input_part006_review.md†L195-L195】 | VESC conversions promise finer tuning but require custom cooling ducts and deck machining before pitching the idea to Weped’s OEM contacts.【F:knowledge/notes/input_part010_review.md†L354-L354】 |
| Battery module | Production GTS/Fold packs are 16S6P 50E assemblies that survive high mileage when left largely stock.【F:knowledge/notes/input_part001_review.md†L24-L25】【F:knowledge/notes/input_part007_review.md†L286-L286】 | Race builds chase 21S11P Molicel layouts for 140 km/h targets; plan pack height, BMS placement, and wiring for the added cells before cutting decks.【F:knowledge/notes/input_part000_review.md†L717-L717】 |
| Cooling & packaging | OEM housings rely on forced-air side tunnels to keep electronics alive at speed.【F:knowledge/notes/input_part007_review.md†L26-L26】 | Dual Spintend or similar installs need bare-metal mounting, fresh thermal paste, and potentially external heatsinks to stay below thermal shutdown.【F:knowledge/notes/input_part000_review.md†L610-L615】 |
| Quality & support | Premium price tags hide budget cockpit parts and inconsistent service; even loyalists treat new deliveries as kits that require teardown.【F:knowledge/notes/input_part001_review.md†L787-L787】【F:knowledge/notes/input_part009_review.md†L75-L76】 | Maintain detailed punch lists for fork, stem, and wiring work so customers understand the scope before the scooter ever hits pavement.【F:knowledge/notes/input_part001_review.md†L24-L25】 |

## Battery Strategy & Electrical Guardrails
### OEM Pack Baseline
Weped’s factory 16S6P Samsung 50E battery ships on the GTS and Fold series, but seasoned builders open the deck immediately to realign forks, lengthen hardware, and reseat harnesses before trusting the scooter at its advertised speed envelope.【F:knowledge/notes/input_part001_review.md†L24-L25】 The same chassis readily accepts 21S11P Molicel upgrades for 140 km/h projects, yet those packs consume precious deck height and require advance planning for BMS placement and strain relief.【F:knowledge/notes/input_part000_review.md†L717-L717】

### Chemistry Debates & Parallel Scaling
Despite the criticism, Yoann’s four-year-old Weped FS still peaks 240 A on the original 50E module with an ANT smart BMS, demonstrating that the cells can deliver when backed by large parallel strings and conservative thermal management.【F:knowledge/notes/input_part007_review.md†L286-L286】 Builders chasing harder acceleration prefer Samsung 40T or Molicel P42A/P45B packs once current demands exceed what 50E chemistry tolerates per cell, treating the OEM block as a long-range option rather than a high-discharge foundation.【F:knowledge/notes/input_part007_review.md†L286-L286】

### BMS, Regen & Controller Survivability
Front-end controller failures on the Weped Wepoor show how sensitive the platform is to BMS behavior: repeated deaths occurred at only 200 A battery / 300 A phase, with the owner suspecting ANT BMS cutoffs or regen spikes after dead-stop launches despite cool temps.【F:knowledge/notes/input_part011_review.md†L227-L229】 Keep regen well inside the charge FET’s comfort zone, verify ANT or JK boards leave both charge and discharge channels enabled, and log BMS data during launch tests so you can correlate faults with pack events.

## Drivetrain, Controllers & Upgrades
### Stock & Semi-Stock Options
The latest Sonic runs with QS-manufactured hubs and Fardriver controllers, a combination that racers view as the budget alternative to fragile high-power VESC stacks while still offering serious output headroom.【F:knowledge/notes/input_part006_review.md†L195-L195】【F:knowledge/notes/input_part007_review.md†L40-L40】【F:knowledge/notes/input_part007_review.md†L395-L395】 Owners considering VESC conversions should arrive at Weped’s door with cooling plans, because the stock enclosure needs rework to house larger heatsinks or external mounts without cooking the electronics.【F:knowledge/notes/input_part010_review.md†L354-L354】

### High-Power Motor Paths
Rage Mechanics’ 75 mm stator hubs remain the go-to race upgrade, pushing well past 10 kW per wheel on Weped frames but costing about €650 each and demanding careful axle-width planning.【F:knowledge/notes/input_part000_review.md†L449-L449】 Builders on tighter budgets can still source Rion/Weped FF-spec motors around €340 in France, though freight costs quickly erode the savings for overseas buyers.【F:knowledge/notes/input_part000_review.md†L698-L698】 Pair these motors with the aforementioned 21S packs to unlock the 140 km/h envelope already mapped out for upcoming Weped SS projects.【F:knowledge/notes/input_part000_review.md†L717-L717】

## Thermal Management & Mechanical Prep
Sealed decks leave almost no thermal margin: dual Spintend installs logged ~500 A phase and 80 °C controller temps until owners sanded paint from the deck, applied quality thermal paste, and bolted the housings directly to the frame.【F:knowledge/notes/input_part000_review.md†L610-L615】 Even the OEM layout assumes aggressive airflow—paired 30 Ah 40T packs feed opposing side fans at roughly 145 km/h to keep electronics alive, so any stealth conversion must preserve or improve that ducting.【F:knowledge/notes/input_part007_review.md†L26-L26】 Plan for external heatsinks, repaste jobs, and fan redundancy before lifting current limits.

## Handling & Rider Feedback
- Paolo still praises the Rion RX2000 for running stable near 100 km/h without a damper, whereas Face de Pin Sucé finds the chassis twitchy compared with Weped builds and argues the oversized Weped columns pay off once paired with PMT tires for corner grip—factor rider preference into cockpit upgrades rather than chasing a single “best” setup.【F:knowledge/notes/input_part001_review.md†L51-L52】

## Quality, Support & Delivery Reality
Community audits describe new Wepeds as expensive kits: owners routinely replace bargain switches, Zoom brakes, and flimsy stems despite €3–4 k invoices, treating the chassis as the only real value-add.【F:knowledge/notes/input_part001_review.md†L787-L787】 Customer service isn’t much better—Paolo notes Weped’s support remains inconsistent even as prices climb, while racers consider the Fold 3 the lone chassis that arrives close to track-ready without reinforcement.【F:knowledge/notes/input_part009_review.md†L75-L76】 Expect to document every correction for clients, including fork bearing work, steering column alignment, and fastener swaps.

## Procurement & Planning Notes
- **Motor sourcing:** Rage Mechanics and other boutique suppliers can still deliver Weped-spec hubs, but lead times and freight swing wildly—budget extra for customs and verify axle widths before ordering.【F:knowledge/notes/input_part000_review.md†L449-L449】【F:knowledge/notes/input_part000_review.md†L698-L698】
- **Partnership outreach:** When pitching VESC-based drivetrains to Weped, arrive with enclosure redesigns and cooling analysis; the factory expects partners to shoulder housing rework in exchange for adopting open hardware.【F:knowledge/notes/input_part010_review.md†L354-L354】
- **Future builds:** Planned SS upgrades targeting 140 km/h already have 21S11P pack dimensions and controller selections scoped—use these benchmarks to sanity-check customer requests before committing to fabrication timelines.【F:knowledge/notes/input_part000_review.md†L717-L717】

## Build Checklist
1. **Strip & inspect the chassis** – realign forks, torque the stem, and document any hardware replacements before the first ride so clients understand the baseline.【F:knowledge/notes/input_part001_review.md†L24-L25】【F:knowledge/notes/input_part001_review.md†L787-L787】
2. **Model the energy system** – decide whether the OEM 50E block meets the use case or if a parallel-heavy 40T/P42A pack is required; budget deck spacers and harness routing accordingly.【F:knowledge/notes/input_part007_review.md†L286-L286】【F:knowledge/notes/input_part000_review.md†L717-L717】
3. **Engineer cooling paths** – hard-mount controllers with quality TIM, preserve side-fan airflow, and log temps during shakedowns before raising current limits.【F:knowledge/notes/input_part000_review.md†L610-L615】【F:knowledge/notes/input_part007_review.md†L26-L26】
4. **Validate BMS behavior** – confirm charge/discharge FET states, regen thresholds, and fault logs to prevent the ANT-induced controller deaths observed on recent Wepoor builds.【F:knowledge/notes/input_part011_review.md†L227-L229】
5. **Plan sourcing & support** – lock in motor suppliers, document lead times, and set expectations about Weped’s limited after-sales help ahead of any customer-facing commitments.【F:knowledge/notes/input_part000_review.md†L449-L449】【F:knowledge/notes/input_part009_review.md†L75-L76】

## Source Notes
[^1]: Factory GTS/Fold pack configuration and required pre-delivery rework.【F:knowledge/notes/input_part001_review.md†L24-L25】
[^2]: Planned 21S11P upgrades for Weped SS high-speed builds.【F:knowledge/notes/input_part000_review.md†L717-L717】
[^3]: Long-term 50E performance data and chemistry debates on Weped FS builds.【F:knowledge/notes/input_part007_review.md†L286-L286】
[^4]: Dual Spintend thermal logs inside Weped decks at ~500 A phase.【F:knowledge/notes/input_part000_review.md†L610-L614】
[^5]: OEM fan-assisted cooling layout on high-speed Wepeds.【F:knowledge/notes/input_part007_review.md†L26-L26】
[^6]: Sonic deliveries with QS hubs and Fardriver controllers plus European sightings.【F:knowledge/notes/input_part006_review.md†L195-L195】【F:knowledge/notes/input_part007_review.md†L395-L395】
[^7]: Weped service reputation and Fold 3 chassis quality assessments.【F:knowledge/notes/input_part009_review.md†L75-L76】
[^8]: Premium pricing contrasted with bargain-spec cockpit hardware on shipped units.【F:knowledge/notes/input_part001_review.md†L787-L787】
[^9]: Guidance to approach Weped about VESC integration with revised cooling plans.【F:knowledge/notes/input_part010_review.md†L354-L354】
[^10]: Repeated controller failures on a Weped Wepoor linked to suspected ANT BMS/regen events.【F:knowledge/notes/input_part011_review.md†L227-L229】
[^11]: Rage Mechanics and FF-spec motor sourcing costs for Weped platforms.【F:knowledge/notes/input_part000_review.md†L449-L449】【F:knowledge/notes/input_part000_review.md†L698-L698】
