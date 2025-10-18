# Scooter Waterproofing & Security

## Overview

Protecting electric scooters from water ingress and theft requires systematic sealing, proper component selection, and security measures. This guide covers field-tested waterproofing techniques, sealant recommendations, bearing upgrades, and anti-theft strategies. Whether commuting in rain or storing outdoors, these practices will help prevent corrosion, electrical failures, and theft while maintaining serviceability.

## What You'll Learn

- How to seal decks, charge ports, and cable penetrations
- Recommended sealants and when to use each type
- Bearing selection for wet conditions
- Post-ride inspection and maintenance procedures
- Controller and pack waterproofing strategies
- Anti-theft hardware and security best practices
- Emergency recovery procedures for water-damaged components

## 💧 Why Waterproofing Matters

🔴 **Water kills electronics**: Most controller and BMS failures trace to moisture ingress.

## 📋 Quick Reference: Waterproofing Priority

| Component | Priority | Method | Cost | Difficulty |
|-----------|----------|--------|------|------------|
| Controller | ⭐⭐⭐⭐⭐ Critical | Conformal coat + silicone | $20 | ⭐⭐ Easy |
| BMS | ⭐⭐⭐⭐⭐ Critical | Conformal coat + heat shrink | $15 | ⭐⭐ Easy |
| Connectors | ⭐⭐⭐⭐ High | Dielectric grease + heat shrink | $10 | ⭐ Very Easy |
| Display | ⭐⭐⭐ Medium | Silicone gasket + seal | $5 | ⭐⭐ Easy |
| Deck seams | ⭐⭐⭐ Medium | Silicone sealant | $10 | ⭐⭐ Easy |

## 📋 Recommended Products

| Product | Use Case | Application | Cost |
|---------|----------|-------------|------|
| MG Chemicals 422B | Conformal coat for PCBs | Spray or brush | ~$15 |
| Dielectric grease | Connector weatherproofing | Thin layer | ~$5 |
| Silicone sealant | Deck and cable entry sealing | Bead application | ~$8 |
| Heat shrink tubing | Connector and wire protection | Heat gun | ~$10 |

💡 **Pro Tip**: Apply conformal coat BEFORE your first wet ride. Fixing water damage is 10x harder than preventing it.

## ⚠️ Common Mistakes

🔴 **Over-coating**: Too much conformal coat can trap heat and cause failures
🔴 **Sealing before testing**: Seal after confirming everything works
🔴 **Forgetting cable entries**: Where cables enter the deck is the #1 water entry point
🔴 **Cheap conformal coat**: Bargain coatings crack or peel quickly

## 🔒 Security Best Practices

💡 **Layered security**: No single method stops all theft - use multiple layers

📋 **Security Hierarchy**:
1. **Insurance** - Most cost-effective for expensive builds
2. **GPS tracker** - Recovery if stolen (hidden mount essential)
3. **U-lock + cable** - Deters casual thieves
4. **Alarm** - Audible deterrent
5. **Hidden kill switch** - Prevents joy-riding

## 🔧 Related Guides

- [Daly BMS Waterproofing](daly-bms-waterproofing.md) - Specific BMS moisture recovery
- [VESC ADC Accessory Integration](vesc-adc-accessory-integration.md) - Connector weatherproofing

## Weatherproof the Chassis Before the Storm

- **Seal every seam.** Run silicone along deck joints, cable pass-throughs, and the charge door, then coat hub interfaces with lithium grease so sustained rain rides don\'t wick water into the pack or motor bay.[^1]
- **Add cheap dash protection.** A hydrogel phone film keeps Xiaomi dash buttons responsive in the rain, and engine gasket sealant around deck seams and grommets finishes a £1–2 waterproofing job.[^hydrogel_dash_seal]
- **Choose durable sealants.** Veterans skip Sikaflex in favour of PU50-class marine urethanes (Illbruck/Enfy) because they cure even underwater, stay elastic for years, can be sanded smooth, and pair with neutral silicones where joints must reopen later.[^pu50]
- **Deploy Tec7 on harness entries.** The crew runs Tec7 sealant around loom penetrations and external pack cases, lets it cure fully, and accepts they’ll need to cut and reapply it each time the chassis reopens to avoid trapped moisture.[^tec7]
- **Keep PCB-safe 704 on hand.** The workshop leans on 704 (Liveall/Heinkel) sealant for tubeless builds and electronics because it cures rubbery, with Loctite variants reserved when budgets allow.[^sealant-704]
- **Repack leaky Kaabo hubs.** RTV the shell seam and stuff fresh lithium grease into the bearings.
  - rusted motors often recover once water ingress is halted.[^2]
- **Weatherproof external packs thoroughly.** Riders strapping batteries to rear suspensions silicone every seam to keep exposed packs dry on long commutes.
  - expect to lose folding ability but gain reliable sealing.[^3]
- **Add moisture sentries.** Builders embed hydrometers on DC–DC converters that feed Arduinos driving buzzers; when the sensor trips, the alarm screams before corrosion sets in.[^1]
- **Prep for snow and spray.** Ninebot Max riders trade winter fender STLs and revisit NAMI trailing-arm suspension tuning to balance curb compliance against braking dive when roads turn sloppy.[^snow_hardware]
- **Pack silica gel inside decks.** Rental-frame conversions stay dry longest when silica packets live beside the battery and automotive engine sealant closes the lid.
  - silicone peels by hand for service yet seals better than chasing custom gaskets.[^4]
- **Audit Kaabo decks for pooling.** Wolf inspections uncovered water trapped under 20 S packs that soaked LG M50LT modules despite shrink wrap.
  - add drain checks, dielectric grease, and redundant silicone/Kapton layers around series bridges and BMS leads before chasing 20 S8 P upgrades.[^5]
- **Relocate or seal storm-vulnerable modules.** Recent rain rides soaked CAN adapters and accessory bucks until builders moved them above the deck line, potted JST backshells, and added drain paths before the next storm season.[^6]
- **Inspect charge-port wiring before sealing the deck.** Misrouted leads and hasty silicone blobs have already shorted chargers or started fires; verify polarity and clearance before you close the lid.[^charge-port-audit]
- **Choose the right bearings.** Swap stock 2Z hubs for sealed 2RS units and refresh grease after wet weeks to keep Monorim and Xiaomi front ends from grinding themselves apart.[^7]
- **Choose the right bearings.** Swap stock 2Z hubs for sealed 2RS units rated for 80–100 °C, then refresh grease after wet weeks so rain rides don’t cook Xiaomi or Monorim front ends.[^7][^8]
- **Revive soaked motors methodically.** Niu hubs that sat underwater came back after thorough drying and fresh grease, but the crew now treats sealed bearings and upgraded seals as mandatory before splashing through floods again.[^9]
- **Waterproof race controllers deliberately.** Face de Pin’s Thunder and Nami builds machine custom C350 enclosures, add drain paths, and fabricate frame parts so the electronics stay sealed without sacrificing serviceability during rainy track days.[^10][^11]
- **Copy proven controller shells.** Haku told Noname to mimic Peak G30-style cases and seal ports with silicone instead of plastic wrap when mounting exposed controllers in wet climates.[^peak-case]
  - Nami chassis still need purpose-built watertight boxes beneath the heatsink if they will ever see heavy rain; don’t trust shrink-wrap stopgaps on exposed controller stacks.[^nami-box]
- **Inspect after every soak.** Error 28 beeps and erratic state-of-charge readings usually mean the controller or white battery plug corroded.
  - scrub with contact cleaner, dry thoroughly, and don\'t trust factory IP54 stickers.[^12][^13]
- **Reseal deck mods.** Grinding Xiaomi/Ninebot ribs to fit BMS hardware opens new leak paths; reseal the deck lid and servo-lock cavity with silicone rather than leaving raw metal to rust.[^14]
- **Copy proven enclosure designs.** Koxx’s latest SmartController case uses taller internal walls and TPU cable glands that survived a five-minute hose test.
  - treat it as a template when weather-sealing other electronics.[^15]
- **Waterproof methodically.** Scrape factory paste with care before recoating controllers in silicone.
- **Protect battery leads from abrasion.** Apply secondary heat-resistant sleeving over silicone battery leads, add strain relief at connection points, and perform post-service inspections before reinstalling decks to catch wear before insulation failures cause shorts or fires.[^battery-lead-protection]
  - overdoing sealant complicates future repairs and traps moisture if the enclosure still leaks.[^16]
- **Pressure-test new gaskets.** After resealing enclosures with custom gaskets, riders blast the deck with a pressure washer to confirm no leaks before going back to road duty.[^17]
- **Keep custom builds out of storms.** High-power scooters with relocated electronics still struggle in heavy rain; veterans wait for weather breaks and save storm commutes for stock Ninebots to avoid water-logged controllers.[^18]
- **Route rear lights from the controller.** Tapping battery negative and ESC-positive at fuse F1 replaces the fragile deck lead, but insulate the new run and add strain relief before sealing the lid.[^rear-light]
- **Map relocation priorities before storm season.** The latest review calls for a rainproofing guide that spells out which controllers, converters, and connectors need sealing or relocation on custom builds.
  - capture those lists with your wiring diagrams so water mitigation isn’t improvised after the first downpour.[^19]
- **Cut water-diversion grooves.** Jason now machines shallow channels into axle exits so runoff can’t wick straight into 65 H hubs after wet rides.
  - a simple mod that protects hall bundles on repeated rain routes.[^20]
- **Inspect after every soak.** Error 28 beeps and erratic state-of-charge readings usually mean the controller or white battery plug corroded.
  - look for pink moisture stickers, scrub with contact cleaner, dry thoroughly, and don\'t trust factory IP54 stickers after floods.[^21][^12][^13]
- **Skip deck fan cutouts.** PC fans mounted under the deck barely move heat yet open a direct water path.
  - keep the aluminum plate intact and rely on thermal pads instead of venting that shorts controllers or LiPo-powered fan mods strapped nearby.[^22][^23]

## Layered Theft & Compliance Tactics

- **Build loud, cheap alarms.** Pair gyroscopes with 120 dB buzzers tied to ignition keys or BLE presence so tampering keeps the siren blaring until the scooter rests motionless.[^24]
- **Wire BLE-powered relays correctly.** Feed the relay from the dashboard’s 5 V red/black leads, return the out pair to the dash, and avoid switching the high-current battery line directly.[^ble_relay]
- **Mount motion sensors in the battery bag.** Couriers hide Arduino-driven buzzers inside Wildman cases so cutting the strap or unzipping the bag triggers instant noise without alerting thieves to the electronics location.[^1]
- **Carry layered locks.** Quick errands get a compact Master Lock cable that stays smooth with graphite; long stops call for hardened chains plus GPS trackers taped into the loom.[^25][^26]
- **Layer active deterrents.** Hide GPS trackers along the main harness, tuck motion alarms in the battery bag, keep hardened chains ready, and consider immobilisers that lock the front wheel until a fob reactivates the scooter.[^layered_deterrence]
- **Treat Abus Granit-style chains as the baseline.** Even “unpickable” locks fall to cutters, so riders double up heavy chains or keep the scooter within sight despite the weight penalty.[^abus_granit_benchmark]
- **Treat thin cables as token deterrents.** City riders report compact cable locks stop nothing.
  - start with ≥8 mm hardened chains for real security.[^27]
- **Pad battery-bag cages.** Stainless cable ties or cages still help, but wrap them in heat-shrink or foam so they don’t saw into the pack while slowing opportunists.[^bag-padding]
- **Gig riders budget time for serious locks.** European couriers report food-delivery pay dipping from ≈€20/h toward “slavery” wages post-acquisitions, so they now stage 2–3 heavy chains and padlocks at regular stops to keep scooters secured between orders.[^28]
- **Pick proven trackers.** Invoxia GPS units remain the €100 gold standard because Bluetooth tags lose coverage away from crowds, while Jason’s DIY LTE tracker stores data in Grafana, runs from the scooter pack, and falls back to a roaming SIM battery when unplugged.[^29][^invoxia-2025]
- **Expect opportunists.** Dense-city riders report scooters disappearing within minutes if left unlatched, so treat even short drop-offs like high-risk events and keep the alarm armed.[^26]
- **Double up locks in theft hot spots.** Paris commuters now pair U-locks with Kryptonite chains and keep scooters within sight while obeying 25 km/h limits, lighting, and bike-lane rules to avoid roadside seizures.[^30]
- **Upgrade hardpoints.** Builds pushing 8 kW+ torque now weld steel eyelets, use ≥10 mm hardened chains, and recess security bolts because factory aluminum tabs vanish under cordless grinders.[^31]
- **Keep a mechanical kill switch.** Without native VESC shutdown, riders lean on keyed mains, throttle-disable switches, or Safe Start current limits.
  - and Spintend’s ADC adapter v2 still needs loop keys or smart-BMS latches because it only ferries 5 V/12 V accessory power. Treat Bluetooth/relay locks as secondary deterrents that thieves can bypass quickly.[^32][^33]
  - veterans now layer loop keys, smart-BMS latching buttons, and even VESC Tool’s software power-off so a thief has to defeat multiple systems before the pack energises again.[^adc_layers]
- **Layer trackers by medium.** Mix AirTags or SmartTags for crowd-sourced pings with SIM trackers (TK806, SIM800) where IMEI registration allows ongoing data plans so a stolen scooter keeps reporting in real time.[^34]
- **Prototype smarter telemetry.** Builders are testing ESP32-based 4G+GPS trackers that ride the scooter pack, broadcast IMEI-backed telemetry, and integrate alongside SmartDisplay so theft alerts keep flowing even when BLE trackers fail.[^35]
- Denis’ shop is iterating plug-and-play immobilisers with onboard 5 V regulators, fingerprint readers, and alarm speakers so scooters can sound off or cut power if moved without authorisation.[^denis-tracker-proto]
- **Hide trackers inside the pack.** New SIM7600/BMW tracker builds live under the battery shrink with UART links to MOSFET cutoffs, letting riders remote-kill packs while thieves fumble for the enclosure.[^36]

## Protective Gear & Stealth Riding

- **Dress for the crash, not the ride.** The crew leans on ECE 22.05/22.06 full-face helmets with MIPS-style protection and full moto gear because even 30 km/h lowsides can shatter chins; DOT stickers alone aren’t trusted.[^37]
- **Read traffic early.** Riders trading road stories focus on scanning for blind bike-lane entries, staging full gear, and respecting how quickly tuned scooters hit 60 km/h—seven-second launches demand motorcycle-grade awareness.[^denis-road-awareness]
- **Audit hardware while you suit up.** Replace any missing suspension bolts immediately, add a pea-sized dab of blue threadlocker, and run weekly clamp checks; veterans pair that routine with motorcycle armor, gloves, and Kevlar-lined pants so 50 km/h confiscations or marketing-tempted speed runs don’t end in hospital visits.[^denis-hardware-gear]
- **Stay discreet around police.** Choose understated frames, keep lighting subdued, and reserve police-mode or field-weakening bursts for brief escapes while cruising near rental speeds the rest of the time.[^38]
- **Plan for battery fires.** Lithium packs burn independently of water, so shops consider safer chemistries like LiFePO₄ where packaging allows and keep fire-response drills focused on evacuation, not hose lines.[^denis-lifepo4]
- **Lock down digital attack surfaces.** Builders disguise scooters as stock with low-power brake profiles, MAC-filter Bluetooth modules behind PIN prompts, and add keyed or NFC power switches so pranksters can’t rewrite CAN settings while the scooter is parked.[^39][^40]
- **Budget layered tracking at ~€50 per scooter.** Riders pair Samsung SmartTags with Apple AirTags and plan a GPS IoT beacon for higher-value builds; the combo already recovered a stolen e-bike, but veterans still warn against confronting thieves in person.
  - share location intel with authorities instead.[^41]

## Regional Compliance Pressure

- Ireland and UK riders report €1,500 fines and confiscations for overpowered scooters, so stealth builds and restrained riding remain the safest path in strict EU jurisdictions.[^42]
- Germany still caps e-scooters at 20 km/h with insurance requirements, and French enforcement is catching up; riders keep builds discreet and ride cautiously to avoid roadside trouble.[^de_fr_rules]
- **Plan for roadside inspections.** Finnish police are confiscating scooters that exceed 25 km/h without registration and even checking bulb part numbers, while southern EU riders dodge €8–9 k fines by programming low-power “police modes” and swapping to halogen BA9S lamps to satisfy moped rules.[^43]
- **Swiss crackdowns escalate.** Authorities recently seized a 133 km/h Wolf Warrior outright, reinforcing the need to keep legal commuter profiles alongside race setups.[^44]
- **Pre-stage a legal profile.** Belgian riders have seen 50 km/h scooters confiscated and cases escalated to lawyers; their workaround is to flash a 25–30 km/h VESC profile for roadside checks while keeping a high-speed mode for private property, paired with calm riding to avoid attracting attention.[^45]
- **Match frame choice to insurance rules.** Converting 50 cc mopeds to QS hubs can void payouts because paperwork still lists ICE drivetrains, and Israeli riders report dual-motor scooters are outright illegal.
  - keep Zero 10X builds single-motor despite upgrades.[^46]
- **Expect highway patrol scrutiny.** A U.S. park ranger fined a rider $130 and classed his 65 mph Wepoor as a motorcycle, highlighting how mislabeling high-speed builds as “scooters” risks confiscation.
  - know local registration and plate rules before using highways.[^47]
- **Track looming EU certification changes.** Spanish riders expect new power limits and registration requirements by January 2027; some are purchasing private insurance now to stay legal while enjoying a two-year grace window.[^48]

## Post-Ride Water Diagnostics

- **Run the emergency dry-out drill immediately.** Kill power, open the deck, and disconnect the battery as soon as water reaches board level; forced air, alcohol rinses, and fresh desiccant beat passive “rice bag” drying before you reseal seams with silicone.[^49][^50]
- **Track regen-related faults.** Error 21 after a panic stop usually points to a cooked data line, not a dead BMS.
  - bench-test packs on a known-good scooter before blaming Happy BMS or Rita.[^51]
- **Recognize Rita\'s behavior.** External packs lose regen while full by design; bleed a few percent off the top and confirm series-count settings before chasing wiring ghosts.[^52]
- **Keep electronics dry when folding.** Monorim and Mi 3 dashboards that auto-boot after rain usually revive after 99 % isopropyl baths and patient drying.
  - never fold a wet stem onto the deck where water can pool around the button PCB.[^53]

## Travel & Storage Tips

- **Drain packs safely for flights.** Commuters running 24 Ah externals discharge with incandescent lamps for hours to hit airline targets, proving how long large packs need to reach “safe” storage levels.[^54]
- **Recharge before hibernation.** Rita draws a small standby current even when the scooter is off, so top packs to storage voltage if the build will sit for weeks rather than leaving it connected indefinitely.[^55]
- **Know the local rules.** Dutch riders remind visitors that stand-up scooters remain illegal without seats; expect enforcement even if locals still spot Xiaomi commuters around Venlo.[^56]
- **Avoid backyard storage.** Dew-point swings push condensation into bearings and electronics.
  - keep scooters under a roof and move packs indoors or into insulated boxes instead of leaving them outside overnight.[^57]
- **Plan spacer height when stuffing the deck.** 46 mm 3D-printed shims support some external cases, internal 13S6P builds cleared with roughly 27 mm, and VESC conversions needed about 30 mm—measure before printing or machining.[^spacer-height]
- **Weatherproof XT30 charge-port swaps.** When replacing the coax jack, add a weatherproof cap, sealant, and ideally an inline fuse so exposed male pins can’t short in rain or debris.[^xt30-port]
- **Check accessory ergonomics.** Bolt-on saddles push weight rearward and complicate unloading speed bumps, and 2.5 L frame bags are shorter but wider than 3 L options.
  - mock up foot room before committing.[^58]

## Field Checklist

1. Seal the deck and hub seams before rainy season commutes.[^1]
2. Test alarms weekly—confirm gyros, hydrometers, and buzzers still trigger in seconds.[^59]
3. Inspect connectors and controller boards after any water-triggered fault code, cleaning and drying before the next ride.[^12]
4. Log where each tracker and alarm sits so technicians can service the scooter without cutting hidden hardware.[^60][^13]


## References

[^1]: Source: knowledge/notes/all_part01_review.md†L86-L87
[^2]: Source: knowledge/notes/input_part006_review.md†L217-L217
[^3]: Source: knowledge/notes/denis_all_part02_review.md†L99839-L99856
[^4]: Source: knowledge/notes/input_part000_review.md†L685-L685
[^5]: Source: knowledge/notes/input_part002_review.md†L159-L161
[^6]: Source: knowledge/notes/input_part012_review.md†L308-L309
[^7]: Source: knowledge/notes/all_part01_review.md†L27274-L27275
[^8]: Source: data/vesc_help_group/text_slices/input_part009.txt†L13324-L13332
[^9]: Source: knowledge/notes/input_part009_review.md†L322-L322
[^10]: Source: data/vesc_help_group/text_slices/input_part009.txt†L22050-L22053
[^11]: Source: data/vesc_help_group/text_slices/input_part009.txt†L22066-L22072
[^peak-case]: Source: knowledge/notes/input_part010_review.md†L503-L503
[^nami-box]: Source: knowledge/notes/input_part010_review.md†L503-L503
[^12]: Source: knowledge/notes/denis_all_part02_review.md†L419-L421
[^13]: Source: knowledge/notes/denis_all_part02_review.md†L454-L455
[^14]: Source: knowledge/notes/input_part000_review.md†L292-L293
[^15]: Source: knowledge/notes/input_part000_review.md†L513-L513
[^16]: Source: knowledge/notes/input_part006_review.md†L225-L225
[^17]: Source: knowledge/notes/input_part006_review.md†L330-L330
[^18]: Source: knowledge/notes/input_part012_review.md†L214-L217
[^19]: Source: knowledge/notes/input_part012_review.md†L308-L308
[^20]: Source: knowledge/notes/input_part012_review.md†L233-L235
[^21]: Source: knowledge/notes/denis_all_part02_review.md†L307-L309
[^22]: Source: knowledge/notes/denis_all_part02_review.md†L433-L436
[^23]: Source: knowledge/notes/denis_all_part02_review.md†L440-L441
[^^snow_hardware]: Source: knowledge/notes/input_part003_review.md†L507-L507
[^24]: Source: knowledge/notes/all_part01_review.md†L88-L88
[^ble_relay]: Source: knowledge/notes/all_part01_review.md†L642-L642
[^25]: Source: knowledge/notes/all_part01_review.md†L167-L167
[^26]: Source: knowledge/notes/all_part01_review.md†L27392-L27407
[^layered_deterrence]: Source: knowledge/notes/all_part01_review.md†L895-L895
[^abus_granit_benchmark]: Source: knowledge/notes/all_part01_review.md†L741-L741
[^27]: Source: knowledge/notes/input_part006_review.md†L252-L252
[^28]: Source: knowledge/notes/input_part011_review.md†L330-L337
[^29]: Source: knowledge/notes/input_part013_review.md†L794-L796
[^30]: Source: knowledge/notes/input_part006_review.md†L170-L171
[^31]: Source: knowledge/notes/input_part005_review.md†L195-L200
[^32]: Source: knowledge/notes/input_part005_review.md†L348-L350
[^33]: Source: knowledge/notes/input_part005_review.md†L504-L506
[^adc_layers]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24596-L24612
[^34]: Source: knowledge/notes/input_part005_review.md†L350-L351
[^35]: Source: knowledge/notes/input_part000_review.md†L239-L239
[^36]: Source: knowledge/notes/input_part000_review.md†L506-L508
[^37]: Source: knowledge/notes/input_part000_review.md†L364-L364
[^38]: Source: knowledge/notes/input_part000_review.md†L365-L365
[^denis-hardware-gear]: Source: knowledge/notes/denis_all_part02_review.md†L710-L711
[^denis-road-awareness]: Source: knowledge/notes/denis_all_part02_review.md†L1097-L1097
[^denis-lifepo4]: Source: knowledge/notes/denis_all_part02_review.md†L713-L713
[^pu50]: Source: knowledge/notes/denis_all_part02_review.md†L528-L528
[^tec7]: Source: knowledge/notes/denis_all_part02_review.md†L658-L658
[^charge-port-audit]: Source: knowledge/notes/denis_all_part02_review.md†L632-L632
[^rear-light]: Source: knowledge/notes/denis_all_part02_review.md†L659-L659
[^bag-padding]: Source: knowledge/notes/denis_all_part02_review.md†L660-L660
[^spacer-height]: Source: knowledge/notes/denis_all_part02_review.md†L661-L661
[^xt30-port]: Source: knowledge/notes/denis_all_part02_review.md†L662-L662
[^sealant-704]: Source: knowledge/notes/denis_all_part02_review.md†L681-L681
[^39]: Source: knowledge/notes/input_part006_review.md†L79-L79
[^40]: Source: knowledge/notes/input_part006_review.md†L428-L429
[^41]: Source: knowledge/notes/input_part012_review.md†L201-L203
[^42]: Source: knowledge/notes/input_part005_review.md†L124-L124
[^de_fr_rules]: Source: knowledge/notes/all_part01_review.md†L632-L632
[^hydrogel_dash_seal]: Source: knowledge/notes/all_part01_review.md†L876-L876
[^43]: Source: knowledge/notes/input_part005_review.md†L225-L227
[^44]: Source: data/vesc_help_group/text_slices/input_part002.txt†L9471-L9489
[^45]: Source: data/vesc_help_group/text_slices/input_part002.txt†L9502-L9510
[^46]: Source: knowledge/notes/input_part005_review.md†L358-L365
[^47]: Source: knowledge/notes/input_part011_review.md†L149-L154
[^48]: Source: knowledge/notes/input_part011_review.md†L386-L393
[^49]: Source: data/vesc_help_group/text_slices/input_part003.txt†L337-L345
[^50]: Source: data/vesc_help_group/text_slices/input_part003.txt†L345-L346
[^51]: Source: knowledge/notes/denis_all_part02_review.md†L368-L369
[^52]: Source: knowledge/notes/denis_all_part02_review.md†L374-L375
[^53]: Source: knowledge/notes/denis_all_part02_review.md†L455-L455
[^54]: Source: knowledge/notes/denis_all_part02_review.md†L414-L415
[^55]: Source: knowledge/notes/denis_all_part02_review.md†L483-L484
[^56]: Source: knowledge/notes/input_part006_review.md†L59-L59
[^57]: Source: knowledge/notes/input_part006_review.md†L384-L384
[^58]: Source: knowledge/notes/input_part006_review.md†L94-L94
[^59]: Source: knowledge/notes/all_part01_review.md†L86-L88
[^60]: Source: knowledge/notes/all_part01_review.md†L896-L896
[^denis-tracker-proto]: Source: knowledge/notes/denis_all_part02_review.md†L932-L932
[^battery-lead-protection]: Source: knowledge/notes/input_part006_review.md†L501-L501
