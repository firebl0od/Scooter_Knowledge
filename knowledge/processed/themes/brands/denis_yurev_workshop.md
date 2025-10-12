# Denis Yurev Workshop (Rita Ecosystem)

## Quick Facts
| Topic | Details |
| --- | --- |
| Flagship products | Rita smart battery adapter, common-port external packs, repair BMS line |
| Target platforms | Xiaomi M365/Pro families and compatible clones |
| Sales channel | Direct via m365.embedden.com with self-published guides and tooling docs |
| Typical customers | Riders extending range or voltage while retaining Xiaomi dashboards |

## Product Portfolio

### Rita Smart Adapter
- Designed for Xiaomi-style data-line traffic and parallel battery expansions; supports Bluetooth configuration or serial tooling when the stock dashboard is absent.[^rita-capabilities]
- Offers a “permanent BMS emulator” mode for scooters that lack data lines yet still orchestrates current like paired smart diodes, routing charger input automatically between packs.[^rita-emulator]
- Sustains roughly 30 A output, tolerates anti-spark switches between adapter and controller, and ships with XT30 harnesses sized to the enclosure’s thermal and spatial limits.[^rita-hardware]
- Maintains pack isolation instead of voltage-equalizing, so riders must align state-of-charge manually—especially when mixing internal 12S builds or dual externals.[^rita-soh]
- Telemetry prioritizes whichever pack sits a few tenths of a volt higher; disconnect or top-charge the auxiliary pack to view its stats.[^rita-telemetry]
- V4 hardware extends sensing up to 15S while still bottlenecking battery current near 25 A; newer boards add charger and regen over-voltage protection that only works when Rita stays inline with the scooter’s charge path.[^rita-v4]
- Relocating the Xiaomi charge port outside the bag is acceptable if a three-way splitter remains so Rita can detect chargers and enforce safeguards.[^rita-v4]

### Repair BMS Program
- Current production supports 10S4P batteries with ongoing development toward 12S models; units are configurable over simple USB-UART adapters for clone scooters.[^bms-roadmap]
- Default charge ceiling is 4.15 V per cell (≈4.14 V after diode drop) but can be tuned higher or lower for longevity or range.[^bms-ceiling]
- Field tests logged 37 A discharge headroom when paralleled with another 10S pack, while the 3 A charge limit pushes owners toward patience or dual chargers.[^bms-headroom]

### External Battery Kits
- Wildman 2 L hard cases remain the standard enclosure, cleanly fitting 8 Ah-class 10S or 12S packs; 3 L variants are reserved for future 5P customs once supply stabilizes.[^battery-enclosures]
- Builds lean on Samsung 35E or equivalent 21700 cells, quality 12 AWG wiring, and Daly 25 A common-port BMS boards; XT30 connectors are intended for semi-permanent joints rather than frequent hot-swaps.[^battery-bom]
- Range Boost bundles double an M365 Pro’s capacity by matching OEM pack size, while Range+Speed kits demand firmware tweaks whenever the auxiliary pack is removed.[^range-kits]
- AliExpress packs with separate charge ports require BMS swaps before pairing with Rita to avoid uncontrolled overcharge through the discharge leads.[^separate-charge]
- Community buyers now dispute “13.8 Ah” 10S2P listings and inspect harnesses closely after shorts traced back to unsoldered Y-cable joints inside Wildman bags—treat unbelievable capacity claims as fire risks.[^counterfeit]
- Secure the Wildman case upright with clamps or cages instead of glue fills so thieves cannot unzip the pack in seconds and technicians can still service the battery.[^bag-security]

## Pricing & Bundles
- Complete Rita + bag + battery kits price in the €250–€280 band plus roughly €20 shipping depending on charger inclusion, reflecting low-volume assembly with branded components.[^pricing]
- Late-summer 2020 quotes landed near £290 delivered for 12S kits to the UK and about €325 to Finland, with no additional VAT within the EU customs zone.[^regional-pricing]

## Fulfillment & Lead Times
- Adapters ship worldwide, but lithium packs stay EU-only because Denis relies on ground carriers; he experiments with UPS options for markets like Kuwait while offering electronics-only deliveries to regions such as Norway or Turkey.[^shipping-scope]
- Production runs ship in weekly batches (e.g., 30 adapters, 15 bags, nine batteries), with typical EU door-to-door timelines around 10 days and three-day deliveries from Poland once regional stock depots are replenished.[^batching]
- Battery assembly lead times fluctuate around two to three weeks when charger inventory tightens; 12S chargers resumed after supplier holidays, and by mid-August he quoted three business days to build a pack.[^lead-times]

## Support & Documentation
- Denis maintains installation guides for Rita, external batteries, and repair BMS builds on his storefront to avoid marketplace fees and centralize support.[^docs]
- Customers are urged to include order IDs in support tickets while Denis manually reconciles payments during banking or payment-processor outages.[^support-ops]

## Integration & Maintenance Highlights
- Xiaomi V3 controllers tolerate 13S packs without hardware swaps, but Denis’ crew replaces Kapton strips with 0.5 mm thermal pads and direct-solders phase leads to keep MOSFETs cool on higher-current tunes.[^controller-thermals]
- Rita’s 25 A ceiling limits the torque boost from tiny external packs; for long hill climbs riders step up to dual motors or uprated controllers rather than forcing more current through the adapter.[^rita-hill]
- Dual-dash AWD builds treat Rita as the master: tie controller grounds together, forward a single data lead to the slave dash, and investigate any Error 14 immediately because it signals cross-pack leakage the adapter should block.[^awd]
- Recurrent thermal shutdowns after a Rita upgrade usually trace to dried controller paste; replace compound (not pads) and monitor logs before pushing harder firmware.[^thermal-paste]

## Risks & Watchlist
- Jumping to 13S requires cutting Rita’s sense jumper, reinforcing controllers, and following the manual via the M365 BMS Tool; reverting without restoring the jumper is unsafe.[^thirteen-steps]
- High-power firmware tunes above ~1 kW or aggressive regen profiles can overheat motors and burn MOSFETs unless paired with controller trace reinforcement and mechanical brake upgrades.[^power-risks]
- New Rita over-voltage guards still depend on healthy BMS hardware; relocating charge ports without the required splitter blinds the adapter to charger events and removes those protections.[^rita-v4]
- Using Xiaomi packs as ad hoc chargers without proper current limiting remains a fire risk—Denis instead repurposes them as externals with their own BMS and keeps charge circuits separated.[^pack-charger]

---
[^rita-capabilities]: Source: `knowledge/notes/all_part01_review.md`, lines 16-18, 23.
[^rita-emulator]: Source: `knowledge/notes/all_part01_review.md`, lines 19, 114.
[^rita-hardware]: Source: `knowledge/notes/all_part01_review.md`, lines 20, 24, 61.
[^rita-soh]: Source: `knowledge/notes/all_part01_review.md`, lines 21, 133.
[^rita-telemetry]: Source: `knowledge/notes/all_part01_review.md`, lines 25, 139, 219.
[^bms-roadmap]: Source: `knowledge/notes/all_part01_review.md`, lines 13, 117.
[^bms-ceiling]: Source: `knowledge/notes/all_part01_review.md`, line 182.
[^bms-headroom]: Source: `knowledge/notes/all_part01_review.md`, line 184.
[^battery-enclosures]: Source: `knowledge/notes/all_part01_review.md`, lines 45, 48.
[^battery-bom]: Source: `knowledge/notes/all_part01_review.md`, lines 46, 61, 66, 102, 145, 238.
[^range-kits]: Source: `knowledge/notes/all_part01_review.md`, lines 18, 260.
[^separate-charge]: Source: `knowledge/notes/all_part01_review.md`, line 180.
[^pricing]: Source: `knowledge/notes/all_part01_review.md`, lines 30, 61.
[^regional-pricing]: Source: `knowledge/notes/all_part01_review.md`, lines 176, 274.
[^shipping-scope]: Source: `knowledge/notes/all_part01_review.md`, lines 27, 177, 275.
[^batching]: Source: `knowledge/notes/all_part01_review.md`, lines 29, 33, 174.
[^lead-times]: Source: `knowledge/notes/all_part01_review.md`, lines 32, 34, 35, 212.
[^docs]: Source: `knowledge/notes/all_part01_review.md`, line 17.
[^support-ops]: Source: `knowledge/notes/all_part01_review.md`, line 150.
[^thirteen-steps]: Source: `knowledge/notes/all_part01_review.md`, lines 162-166, 217.
[^power-risks]: Source: `knowledge/notes/all_part01_review.md`, lines 22, 155, 170-171.
[^rita-v4]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 22-33.
[^controller-thermals]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 10-13.
[^rita-hill]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 31-33.
[^awd]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 25-28.
[^thermal-paste]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 32-33.
[^counterfeit]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 19-23.
[^bag-security]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 42-45.
[^pack-charger]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 45-46.
