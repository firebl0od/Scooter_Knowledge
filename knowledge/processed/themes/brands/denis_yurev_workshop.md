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
- Refurbished Samsung 35E/50E lots from NKON’s late-2021 inventory remain Denis’ go-to when new stock dries up—he logs batch codes so midlife rebuilds stay traceable.【F:knowledge/notes/denis_all_part02_review.md†L97241-L97259】
- Secure the Wildman case upright with clamps or cages instead of glue fills so thieves cannot unzip the pack in seconds and technicians can still service the battery.[^bag-security]
- New mounting hardware bolts packs to Wildman bags with eight screw/wide-washer mounts, fiberglass sleeving, and foam padding so cells cannot rattle or chafe during pothole hits.【F:knowledge/notes/denis_all_part02_review.md†L361-L362】
- Repurposing tool batteries like Makita BL1850B modules rarely works—the 5 S packs sit too low for Rita to blend in, so Denis advises selling them and investing in 10–12 S scooter packs with Daly common-port BMS boards instead; bargain 4 Ah lawnmower bricks built for ~180 W peaks can overheat or ignite when pushed toward Rita’s 25 A ceiling.[^tool-packs][^lawn-pack]
- Cheap “13 Ah” externals often sag early enough that Rita falls back to the OEM battery—test suspect packs alone at low load and expect legitimate Daly-based builds to cost far more than €160 listings.[^cheap-packs]

## Pricing & Bundles
- Complete Rita + bag + battery kits price in the €250–€280 band plus roughly €20 shipping depending on charger inclusion, reflecting low-volume assembly with branded components.[^pricing]
- Late-summer 2020 quotes landed near £290 delivered for 12S kits to the UK and about €325 to Finland, with no additional VAT within the EU customs zone.[^regional-pricing]
- The Range + Speed bundle ships with a 50.4 V brick that tops both batteries sequentially; splitting the packs across chargers finishes faster while keeping BMS thermals comfortable.[^range-speed-charging]

## Fulfillment & Lead Times
- Adapters ship worldwide, but lithium packs stay EU-only because Denis relies on ground carriers; he experiments with UPS options for markets like Kuwait while offering electronics-only deliveries to regions such as Norway or Turkey.[^shipping-scope]
- Production runs ship in weekly batches (e.g., 30 adapters, 15 bags, nine batteries), with typical EU door-to-door timelines around 10 days and three-day deliveries from Poland once regional stock depots are replenished.[^batching]
- Battery assembly lead times fluctuate around two to three weeks when charger inventory tightens; 12S chargers resumed after supplier holidays, and by mid-August he quoted three business days to build a pack.[^lead-times]
- Charging telemetry continues after the scooter powers down—expect the dash to hover near 99 % until the external pack balances, so rely on charger LEDs or the Rita app for confirmation.[^charging-telemetry]
- Shipping hazardous goods remains a compliance exercise: Denis’ crew warns that every lithium shipment must be declared and certified under EU ADR/IATA rules with proper paperwork and, in many jurisdictions, a contracted safety advisor—undeclared packs leave senders on the hook for six-figure liabilities if a parcel ignites.[^hazmat]
- Polish Post now carries electronics and packs to Serbia again, and London buyers can source Rita hardware locally via reseller @Kvarkas while UK 12S kits land around €207 after his early-August backlog clears.[^serbia]
- The main workshop recently moved to a space with limited mains power, so Denis is evaluating DC welders and backup generators to keep pack production online without tripping breakers.[^workshop-power]

## Support & Documentation
- Denis maintains installation guides for Rita, external batteries, and repair BMS builds on his storefront to avoid marketplace fees and centralize support.[^docs]
- Customers are urged to include order IDs in support tickets while Denis manually reconciles payments during banking or payment-processor outages.[^support-ops]
- Rita MAX remains on the roadmap as the variant that natively understands Ninebot Max voltage reporting; legacy hardware will need adapters if riders migrate to that platform.[^rita-max]
- BMS coverage is deliberately strict: Rita units stay warrantied because they are harder to miswire, but standalone BMS buyers must prove faults aren’t installer-induced, and Denis keeps sales off PayPal/eBay to avoid anti-seller chargebacks.[^bms-warranty]

## Integration & Maintenance Highlights
- Xiaomi V3 controllers tolerate 13S packs without hardware swaps, but Denis’ crew replaces Kapton strips with 0.5 mm thermal pads and direct-solders phase leads to keep MOSFETs cool on higher-current tunes.[^controller-thermals]
- Rita’s 25 A ceiling limits the torque boost from tiny external packs; for long hill climbs riders step up to dual motors or uprated controllers rather than forcing more current through the adapter.[^rita-hill]
- Dual-dash AWD builds treat Rita as the master: tie controller grounds together, forward a single data lead to the slave dash, and investigate any Error 14 immediately because it signals cross-pack leakage the adapter should block.[^awd]
- Treat a sudden Error 14 or 21 on a secondary dash as a wiring or polarity fault—Denis warns it means packs are backfeeding and the scooter should stay parked until the harness and BMS are rechecked.[^error14]
- XiaoFlasher’s 13 S BMS emulator can add throttle lag, whereas Rita’s emulation keeps instant response when blending large internal packs with the stock dashboard.[^xiaoflasher]
- Recurrent thermal shutdowns after a Rita upgrade usually trace to dried controller paste; replace compound (not pads) and monitor logs before pushing harder firmware.[^thermal-paste]
- Tally charge time when evaluating third-party packs: the stock 1.7 A Xiaomi brick adds roughly 1.7 Ah per hour, so a genuine 12 Ah module should take close to seven hours from empty.【F:knowledge/notes/denis_all_part02_review.md†L98595-L98598】
- Expect the scooter to rest a few tenths below full charge because Rita deliberately undercharges the internal pack to preserve regen margin; treat buzzing motors or error 39 beeps as signs to dial battery current back under the adapter’s 25 A ceiling.[^rita-undercharge]
- Rita’s Schottky charge diode drops roughly 0.6 V, so stock packs plateau around 97 % unless you bypass the adapter during off-scooter charging; Denis prefers the mild undercharge for longevity and regen headroom.[^rita-schottky]
- High-voltage experiments around 60 V still demand staged launches, BLE firmware checks, and careful thermal monitoring since Rita enforces its own limits even when the drivetrain can pull harder.[^rita-60v]
- Expect Rita to draw a small standby current—packs left connected for months drift toward empty, so recharge to storage voltage every few weeks instead of leaving the adapter plugged in indefinitely.【F:knowledge/notes/denis_all_part02_review.md†L221-L222】
- A small Gen 4 batch under-reported output above ~20 A; cross-check logs against stock wiring and lean on Rita’s redundant current sensing if you suspect phantom throttling.[^rita-underreport]
- Dashboard state-of-charge becomes unreliable once Rita blends packs—Denis tells riders to treat ~50 % on the display as the cue to head home and verify voltage inside the app instead.[^rita-soc]
- Gen 4 harness staging matters: route Rita’s potted balance leads along the controller side, keep the three-way charge splitter inline even if the port relocates, and only cut the gray surge jumper when stepping beyond 12 S packs.[^harness_staging]

## Risks & Watchlist
- Jumping to 13S requires cutting Rita’s sense jumper, reinforcing controllers, and following the manual via the M365 BMS Tool; reverting without restoring the jumper is unsafe.[^thirteen-steps]
- High-power firmware tunes above ~1 kW or aggressive regen profiles can overheat motors and burn MOSFETs unless paired with controller trace reinforcement and mechanical brake upgrades.[^power-risks]
- Older Rita revisions lack modern surge clamping—treat charger relocations carefully, keep the three-way splitter inline, and respect the adapter’s 25 A ceiling to avoid repeated error beeps or melted harnesses.[^legacy-boards]
- New Rita over-voltage guards still depend on healthy BMS hardware; relocating charge ports without the required splitter blinds the adapter to charger events and removes those protections.[^rita-v4]
- Using Xiaomi packs as ad hoc chargers without proper current limiting remains a fire risk—Denis instead repurposes them as externals with their own BMS and keeps charge circuits separated.[^pack-charger]
- Miswired balance leads have popped Daly smart boards instantly—wire negatives first, confirm each cell step with a meter, and avoid doubling sense wires on the same pad.[^balance-leads]
- LiFePO₄ BMS boards cannot safeguard li-ion packs; return the part or build a dedicated chemistry match instead of forcing it into 12 S scooter builds.[^lifepo4]
- Pairing 12 S externals still demands keeping firmware nominal voltage around 51 V so Rita’s limits align—forgetting the setting after a pack swap risks overcharging or limp modes.[^twelve-s-config]
- “Powercube” 3S boosters push Xiaomi 1S packs beyond 56 V; without reinforced controllers and disabled KERS, regen spikes cook the MOSFETs—Denis steers riders toward proper 13 S upgrades instead.【F:knowledge/notes/denis_all_part02_review.md†L97446-L97459】
- Skip fan-and-hole cooling mods on Xiaomi decks; cutting vents adds water ingress without meaningful heat reduction unless thick thermal pads tie MOSFETs to the chassis.【F:knowledge/notes/denis_all_part02_review.md†L86203-L86239】

---

## Source Notes

[^rita-capabilities]: 【F:knowledge/notes/all_part01_review.md†L16-L18】【F:knowledge/notes/all_part01_review.md†L23】
[^rita-emulator]: 【F:knowledge/notes/all_part01_review.md†L19】【F:knowledge/notes/all_part01_review.md†L114】
[^rita-current-limit]: 【F:knowledge/notes/all_part01_review.md†L20-L24】【F:knowledge/notes/denis_all_part02_review.md†L22】【F:knowledge/notes/denis_all_part02_review.md†L31-L33】【F:knowledge/notes/denis_all_part02_review.md†L153】
[^rita-soh]: 【F:knowledge/notes/all_part01_review.md†L21】【F:knowledge/notes/all_part01_review.md†L133】
[^rita-overvoltage]: 【F:knowledge/notes/denis_all_part02_review.md†L29-L33】
[^rita-telemetry]: 【F:knowledge/notes/all_part01_review.md†L25】【F:knowledge/notes/all_part01_review.md†L139】【F:knowledge/notes/all_part01_review.md†L219】【F:knowledge/notes/denis_all_part02_review.md†L33】【F:knowledge/notes/denis_all_part02_review.md†L100】
[^rita-awd]: 【F:knowledge/notes/denis_all_part02_review.md†L26-L28】【F:knowledge/notes/denis_all_part02_review.md†L197】
[^bms-roadmap]: 【F:knowledge/notes/all_part01_review.md†L13】【F:knowledge/notes/all_part01_review.md†L117】
[^bms-ceiling]: 【F:knowledge/notes/all_part01_review.md†L182】
[^bms-headroom]: 【F:knowledge/notes/all_part01_review.md†L184】
[^battery-enclosures]: 【F:knowledge/notes/all_part01_review.md†L45】【F:knowledge/notes/all_part01_review.md†L48】
[^battery-bom]: 【F:knowledge/notes/all_part01_review.md†L46】【F:knowledge/notes/all_part01_review.md†L61】【F:knowledge/notes/all_part01_review.md†L66】【F:knowledge/notes/all_part01_review.md†L102】【F:knowledge/notes/all_part01_review.md†L145】【F:knowledge/notes/all_part01_review.md†L238】
[^range-kits]: 【F:knowledge/notes/all_part01_review.md†L18】【F:knowledge/notes/all_part01_review.md†L260】
[^separate-charge]: 【F:knowledge/notes/all_part01_review.md†L180】
[^pricing]: 【F:knowledge/notes/all_part01_review.md†L30】【F:knowledge/notes/all_part01_review.md†L61】
[^regional-pricing]: 【F:knowledge/notes/all_part01_review.md†L176】【F:knowledge/notes/all_part01_review.md†L274】
[^range-speed-charging]: 【F:knowledge/notes/denis_all_part02_review.md†L33】【F:knowledge/notes/denis_all_part02_review.md†L46】
[^shipping-scope]: 【F:knowledge/notes/all_part01_review.md†L27】【F:knowledge/notes/all_part01_review.md†L177】【F:knowledge/notes/all_part01_review.md†L275】
[^batching]: 【F:knowledge/notes/all_part01_review.md†L29】【F:knowledge/notes/all_part01_review.md†L33】【F:knowledge/notes/all_part01_review.md†L174】
[^lead-times]: 【F:knowledge/notes/all_part01_review.md†L32】【F:knowledge/notes/all_part01_review.md†L34】【F:knowledge/notes/all_part01_review.md†L35】【F:knowledge/notes/all_part01_review.md†L212】
[^charging-telemetry]: 【F:knowledge/notes/all_part01_review.md†L172-L173】【F:knowledge/notes/denis_all_part02_review.md†L33】【F:knowledge/notes/denis_all_part02_review.md†L46】
[^docs]: 【F:knowledge/notes/all_part01_review.md†L17】
[^support-ops]: 【F:knowledge/notes/all_part01_review.md†L150】
[^rita-max]: 【F:knowledge/notes/denis_all_part02_review.md†L195-L196】
[^serbia]: 【F:knowledge/notes/all_part01_review.md†L300-L300】
[^workshop-power]: 【F:knowledge/notes/all_part01_review.md†L298-L298】
[^bms-warranty]: 【F:knowledge/notes/all_part01_review.md†L299-L301】
[^thirteen-steps]: 【F:knowledge/notes/all_part01_review.md†L162-L166】【F:knowledge/notes/all_part01_review.md†L217】
[^power-risks]: 【F:knowledge/notes/all_part01_review.md†L22】【F:knowledge/notes/all_part01_review.md†L155】【F:knowledge/notes/all_part01_review.md†L170-L171】
[^legacy-boards]: 【F:knowledge/notes/denis_all_part02_review.md†L29-L33】【F:knowledge/notes/denis_all_part02_review.md†L153】
[^rita-v4]: 【F:knowledge/notes/denis_all_part02_review.md†L22-L33】
[^controller-thermals]: 【F:knowledge/notes/denis_all_part02_review.md†L10-L13】
[^rita-hill]: 【F:knowledge/notes/denis_all_part02_review.md†L31-L33】
[^awd]: 【F:knowledge/notes/denis_all_part02_review.md†L25-L28】
[^error14]: 【F:knowledge/notes/denis_all_part02_review.md†L26-L31】【F:knowledge/notes/denis_all_part02_review.md†L6433-L6456】
[^thermal-paste]: 【F:knowledge/notes/denis_all_part02_review.md†L32-L33】
[^counterfeit]: 【F:knowledge/notes/denis_all_part02_review.md†L19-L23】
[^bag-security]: 【F:knowledge/notes/denis_all_part02_review.md†L42-L45】
[^pack-charger]: 【F:knowledge/notes/denis_all_part02_review.md†L45-L46】
[^tool-packs]: 【F:knowledge/notes/denis_all_part02_review.md†L235-L235】
[^lawn-pack]: 【F:knowledge/notes/denis_all_part02_review.md†L6610-L6635】
[^balance-leads]: 【F:knowledge/notes/denis_all_part02_review.md†L7028-L7068】
[^lifepo4]: 【F:knowledge/notes/denis_all_part02_review.md†L7080-L7089】
[^rita-schottky]: Rita’s Schottky drop leaving internal packs near 97 % unless bypassed during off-scooter charging, which Denis still recommends for pack longevity.【F:knowledge/notes/denis_all_part02_review.md†L103-L103】【F:knowledge/notes/denis_all_part02_review.md†L108-L108】
[^rita-underreport]: Small Rita Gen 4 batch that under-reported current above ~20 A while redundant sensing still tripped overcurrent protection on Ninebot Max validation builds.【F:knowledge/notes/denis_all_part02_review.md†L198-L198】
[^rita-soc]: Dashboard state of charge drifting after Rita installs, prompting Denis to treat 50 % on the display as the return threshold while using the app for actual voltage.【F:knowledge/notes/denis_all_part02_review.md†L127-L127】
[^rita-undercharge]: 【F:knowledge/notes/denis_all_part02_review.md†L220-L229】
[^rita-60v]: 【F:knowledge/notes/denis_all_part02_review.md†L256-L257】
[^harness_staging]: 【F:knowledge/notes/denis_all_part02_review.md†L7534-L7589】【F:knowledge/notes/denis_all_part02_review.md†L7567-L7589】【F:knowledge/notes/denis_all_part02_review.md†L11671-L11676】
[^cheap-packs]: 【F:knowledge/notes/denis_all_part02_review.md†L5499-L5526】
[^xiaoflasher]: 【F:knowledge/notes/denis_all_part02_review.md†L2467-L2470】
[^twelve-s-config]: 【F:knowledge/notes/denis_all_part02_review.md†L10541-L10552】
[^hazmat]: 【F:knowledge/notes/denis_all_part02_review.md†L188-L193】
