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
- Caps sustained output near 25–30 A, now beeping and throwing error 39 on newer boards if regen or drivetrain demand pushes past the limit; stay within the published ceiling even when firmware sliders allow higher numbers.[^rita-current-limit]
- Maintains pack isolation instead of voltage-equalizing, so riders must align state-of-charge manually—especially when mixing internal 12S builds or dual externals.[^rita-soh]
- Gen 4 hardware adds charger/KERS surge protection and a shunt resistor that spoofs −10 °C during over-voltage events, but first-generation boards still lean entirely on the pack BMS—treat higher-voltage charging as a reduced-SOC tactic and keep Rita inline with the scooter charge splitter.[^rita-overvoltage]
- Telemetry prioritizes whichever pack sits a few tenths of a volt higher; disconnect or top-charge the auxiliary pack to view its stats.[^rita-telemetry]
- AWD conversions must nominate a single Rita “master” controller, forward only the white data lead to the slave dash, and keep dashboard grounds common to avoid error 14/21 loops.[^rita-awd]

### Repair BMS Program
- Current production supports 10S4P batteries with ongoing development toward 12S models; units are configurable over simple USB-UART adapters for clone scooters.[^bms-roadmap]
- Default charge ceiling is 4.15 V per cell (≈4.14 V after diode drop) but can be tuned higher or lower for longevity or range.[^bms-ceiling]
- Field tests logged 37 A discharge headroom when paralleled with another 10S pack, while the 3 A charge limit pushes owners toward patience or dual chargers.[^bms-headroom]

### External Battery Kits
- Wildman 2 L hard cases remain the standard enclosure, cleanly fitting 8 Ah-class 10S or 12S packs; 3 L variants are reserved for future 5P customs once supply stabilizes.[^battery-enclosures]
- Builds lean on Samsung 35E or equivalent 21700 cells, quality 12 AWG wiring, and Daly 25 A common-port BMS boards; XT30 connectors are intended for semi-permanent joints rather than frequent hot-swaps.[^battery-bom]
- Range Boost bundles double an M365 Pro’s capacity by matching OEM pack size, while Range+Speed kits demand firmware tweaks whenever the auxiliary pack is removed.[^range-kits]
- AliExpress packs with separate charge ports require BMS swaps before pairing with Rita to avoid uncontrolled overcharge through the discharge leads.[^separate-charge]
- Reject “13.8 Ah” 10S2P listings and other bargain packs that sag early—veterans favor Samsung 22PM-based builds, insist on common-port BMS boards, and test suspect batteries alone before entrusting Rita with them.[^battery-fraud]
- Mount the bag right-side-up, tuck wiring under the flap, and cinch it with pipe clamps or a cage so opportunistic thieves cannot unzip and walk off with the pack.[^security-clamps]

## Pricing & Bundles
- Complete Rita + bag + battery kits price in the €250–€280 band plus roughly €20 shipping depending on charger inclusion, reflecting low-volume assembly with branded components.[^pricing]
- Late-summer 2020 quotes landed near £290 delivered for 12S kits to the UK and about €325 to Finland, with no additional VAT within the EU customs zone.[^regional-pricing]
- The Range + Speed bundle ships with a 50.4 V brick that tops both batteries sequentially; splitting the packs across chargers finishes faster while keeping BMS thermals comfortable.[^range-speed-charging]

## Fulfillment & Lead Times
- Adapters ship worldwide, but lithium packs stay EU-only because Denis relies on ground carriers; he experiments with UPS options for markets like Kuwait while offering electronics-only deliveries to regions such as Norway or Turkey.[^shipping-scope]
- Production runs ship in weekly batches (e.g., 30 adapters, 15 bags, nine batteries), with typical EU door-to-door timelines around 10 days and three-day deliveries from Poland once regional stock depots are replenished.[^batching]
- Battery assembly lead times fluctuate around two to three weeks when charger inventory tightens; 12S chargers resumed after supplier holidays, and by mid-August he quoted three business days to build a pack.[^lead-times]
- Charging telemetry continues after the scooter powers down—expect the dash to hover near 99 % until the external pack balances, so rely on charger LEDs or the Rita app for confirmation.[^charging-telemetry]

## Support & Documentation
- Denis maintains installation guides for Rita, external batteries, and repair BMS builds on his storefront to avoid marketplace fees and centralize support.[^docs]
- Customers are urged to include order IDs in support tickets while Denis manually reconciles payments during banking or payment-processor outages.[^support-ops]
- Rita MAX remains on the roadmap as the variant that natively understands Ninebot Max voltage reporting; legacy hardware will need adapters if riders migrate to that platform.[^rita-max]

## Risks & Watchlist
- Jumping to 13S requires cutting Rita’s sense jumper, reinforcing controllers, and following the manual via the M365 BMS Tool; reverting without restoring the jumper is unsafe.[^thirteen-steps]
- High-power firmware tunes above ~1 kW or aggressive regen profiles can overheat motors and burn MOSFETs unless paired with controller trace reinforcement and mechanical brake upgrades.[^power-risks]
- Older Rita revisions lack modern surge clamping—treat charger relocations carefully, keep the three-way splitter inline, and respect the adapter’s 25 A ceiling to avoid repeated error beeps or melted harnesses.[^legacy-boards]

---
[^rita-capabilities]: Source: `knowledge/notes/all_part01_review.md`, lines 16-18, 23.
[^rita-emulator]: Source: `knowledge/notes/all_part01_review.md`, lines 19, 114.
[^rita-current-limit]: Sources: `knowledge/notes/all_part01_review.md`, lines 20-24; `knowledge/notes/denis_all_part02_review.md`, lines 22, 31-33, 153.
[^rita-soh]: Source: `knowledge/notes/all_part01_review.md`, lines 21, 133.
[^rita-overvoltage]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 29-33.
[^rita-telemetry]: Sources: `knowledge/notes/all_part01_review.md`, lines 25, 139, 219; `knowledge/notes/denis_all_part02_review.md`, lines 33, 100.
[^rita-awd]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 26-28, 197.
[^bms-roadmap]: Source: `knowledge/notes/all_part01_review.md`, lines 13, 117.
[^bms-ceiling]: Source: `knowledge/notes/all_part01_review.md`, line 182.
[^bms-headroom]: Source: `knowledge/notes/all_part01_review.md`, line 184.
[^battery-enclosures]: Source: `knowledge/notes/all_part01_review.md`, lines 45, 48.
[^battery-bom]: Source: `knowledge/notes/all_part01_review.md`, lines 46, 61, 66, 102, 145, 238.
[^battery-fraud]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 20-23, 126-127.
[^security-clamps]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 44-45.
[^range-kits]: Source: `knowledge/notes/all_part01_review.md`, lines 18, 260.
[^separate-charge]: Source: `knowledge/notes/all_part01_review.md`, line 180.
[^pricing]: Source: `knowledge/notes/all_part01_review.md`, lines 30, 61.
[^regional-pricing]: Source: `knowledge/notes/all_part01_review.md`, lines 176, 274.
[^range-speed-charging]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 33, 46.
[^shipping-scope]: Source: `knowledge/notes/all_part01_review.md`, lines 27, 177, 275.
[^batching]: Source: `knowledge/notes/all_part01_review.md`, lines 29, 33, 174.
[^lead-times]: Source: `knowledge/notes/all_part01_review.md`, lines 32, 34, 35, 212.
[^charging-telemetry]: Sources: `knowledge/notes/all_part01_review.md`, lines 172-173; `knowledge/notes/denis_all_part02_review.md`, lines 33, 46.
[^docs]: Source: `knowledge/notes/all_part01_review.md`, line 17.
[^support-ops]: Source: `knowledge/notes/all_part01_review.md`, line 150.
[^rita-max]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 195-196.
[^thirteen-steps]: Source: `knowledge/notes/all_part01_review.md`, lines 162-166, 217.
[^power-risks]: Source: `knowledge/notes/all_part01_review.md`, lines 22, 155, 170-171.
[^legacy-boards]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 29-33, 153.
