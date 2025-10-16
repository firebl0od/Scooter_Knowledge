# Scooter Waterproofing & Security Field Manual

## Weatherproof the Chassis Before the Storm
- **Seal every seam.** Run silicone along deck joints, cable pass-throughs, and the charge door, then coat hub interfaces with lithium grease so sustained rain rides don\'t wick water into the pack or motor bay.【F:knowledge/notes/all_part01_review.md†L86-L87】
- **Repack leaky Kaabo hubs.** RTV the shell seam and stuff fresh lithium grease into the bearings—rusted motors often recover once water ingress is halted.【F:knowledge/notes/input_part006_review.md†L217-L217】
- **Add moisture sentries.** Builders embed hydrometers on DC–DC converters that feed Arduinos driving buzzers; when the sensor trips, the alarm screams before corrosion sets in.【F:knowledge/notes/all_part01_review.md†L86-L87】
- **Pack silica gel inside decks.** Rental-frame conversions stay dry longest when silica packets live beside the battery and automotive engine sealant closes the lid—silicone peels by hand for service yet seals better than chasing custom gaskets.【F:knowledge/notes/input_part000_review.md†L685-L685】
- **Waterproof methodically.** Scrape factory paste with care before recoating controllers in silicone—overdoing sealant complicates future repairs and traps moisture if the enclosure still leaks.【F:knowledge/notes/input_part006_review.md†L225-L225】
- **Choose the right bearings.** Swap stock 2Z hubs for sealed 2RS units and refresh grease after wet weeks to keep Monorim and Xiaomi front ends from grinding themselves apart.【F:knowledge/notes/all_part01_review.md†L27274-L27275】
- **Inspect after every soak.** Error 28 beeps and erratic state-of-charge readings usually mean the controller or white battery plug corroded—scrub with contact cleaner, dry thoroughly, and don\'t trust factory IP54 stickers.【F:knowledge/notes/denis_all_part02_review.md†L419-L421】【F:knowledge/notes/denis_all_part02_review.md†L454-L455】
- **Pressure-test new gaskets.** After resealing enclosures with custom gaskets, riders blast the deck with a pressure washer to confirm no leaks before going back to road duty.【F:knowledge/notes/input_part006_review.md†L330-L330】

## Layered Theft & Compliance Tactics
- **Build loud, cheap alarms.** Pair gyroscopes with 120 dB buzzers tied to ignition keys or BLE presence so tampering keeps the siren blaring until the scooter rests motionless.【F:knowledge/notes/all_part01_review.md†L88-L88】
- **Mount motion sensors in the battery bag.** Couriers hide Arduino-driven buzzers inside Wildman cases so cutting the strap or unzipping the bag triggers instant noise without alerting thieves to the electronics location.【F:knowledge/notes/all_part01_review.md†L86-L87】
- **Carry layered locks.** Quick errands get a compact Master Lock cable that stays smooth with graphite; long stops call for hardened chains plus GPS trackers taped into the loom.【F:knowledge/notes/all_part01_review.md†L167-L167】【F:knowledge/notes/all_part01_review.md†L27392-L27407】
- **Treat thin cables as token deterrents.** City riders report compact cable locks stop nothing—start with ≥8 mm hardened chains for real security.【F:knowledge/notes/input_part006_review.md†L252-L252】
- **Pick proven trackers.** Invoxia GPS units remain the €100 gold standard because Bluetooth tags lose coverage away from crowds, while DIY LTE trackers powered off the scooter pack can log to self-hosted dashboards and fall back to roaming SIM batteries when unplugged.【F:knowledge/notes/input_part013_review.md†L794-L796】
- **Expect opportunists.** Dense-city riders report scooters disappearing within minutes if left unlatched, so treat even short drop-offs like high-risk events and keep the alarm armed.【F:knowledge/notes/all_part01_review.md†L27392-L27407】
- **Double up locks in theft hot spots.** Paris commuters now pair U-locks with Kryptonite chains and keep scooters within sight while obeying 25 km/h limits, lighting, and bike-lane rules to avoid roadside seizures.【F:knowledge/notes/input_part006_review.md†L170-L171】
- **Upgrade hardpoints.** Builds pushing 8 kW+ torque now weld steel eyelets, use ≥10 mm hardened chains, and recess security bolts because factory aluminum tabs vanish under cordless grinders.【F:knowledge/notes/input_part005_review.md†L195-L200】
- **Keep a mechanical kill switch.** Without native VESC shutdown, riders lean on keyed mains, throttle-disable switches, or Safe Start current limits—and Spintend’s ADC adapter v2 still needs loop keys or smart-BMS latches because it only ferries 5 V/12 V accessory power. Treat Bluetooth/relay locks as secondary deterrents that thieves can bypass quickly.【F:knowledge/notes/input_part005_review.md†L348-L350】【F:knowledge/notes/input_part005_review.md†L504-L506】
- **Layer trackers by medium.** Mix AirTags or SmartTags for crowd-sourced pings with SIM trackers (TK806, SIM800) where IMEI registration allows ongoing data plans so a stolen scooter keeps reporting in real time.【F:knowledge/notes/input_part005_review.md†L350-L351】
- **Lock down digital attack surfaces.** Builders disguise scooters as stock with low-power brake profiles, MAC-filter Bluetooth modules behind PIN prompts, and add keyed or NFC power switches so pranksters can’t rewrite CAN settings while the scooter is parked.【F:knowledge/notes/input_part006_review.md†L79-L79】【F:knowledge/notes/input_part006_review.md†L428-L429】

## Regional Compliance Pressure
- **Plan for roadside inspections.** Finnish police are confiscating scooters that exceed 25 km/h without registration and even checking bulb part numbers, while southern EU riders dodge €8–9 k fines by programming low-power “police modes” and swapping to halogen BA9S lamps to satisfy moped rules.【F:knowledge/notes/input_part005_review.md†L225-L227】

## Post-Ride Water Diagnostics
- **Track regen-related faults.** Error 21 after a panic stop usually points to a cooked data line, not a dead BMS—bench-test packs on a known-good scooter before blaming Happy BMS or Rita.【F:knowledge/notes/denis_all_part02_review.md†L368-L369】
- **Recognize Rita\'s behavior.** External packs lose regen while full by design; bleed a few percent off the top and confirm series-count settings before chasing wiring ghosts.【F:knowledge/notes/denis_all_part02_review.md†L374-L375】
- **Keep electronics dry when folding.** Monorim and Mi 3 dashboards that auto-boot after rain usually revive after 99 % isopropyl baths and patient drying—never fold a wet stem onto the deck where water can pool around the button PCB.【F:knowledge/notes/denis_all_part02_review.md†L455-L455】

## Travel & Storage Tips
- **Drain packs safely for flights.** Commuters running 24 Ah externals discharge with incandescent lamps for hours to hit airline targets, proving how long large packs need to reach “safe” storage levels.【F:knowledge/notes/denis_all_part02_review.md†L414-L415】
- **Recharge before hibernation.** Rita draws a small standby current even when the scooter is off, so top packs to storage voltage if the build will sit for weeks rather than leaving it connected indefinitely.【F:knowledge/notes/denis_all_part02_review.md†L97264-L97268】
- **Know the local rules.** Dutch riders remind visitors that stand-up scooters remain illegal without seats; expect enforcement even if locals still spot Xiaomi commuters around Venlo.【F:knowledge/notes/input_part006_review.md†L59-L59】
- **Avoid backyard storage.** Dew-point swings push condensation into bearings and electronics—keep scooters under a roof and move packs indoors or into insulated boxes instead of leaving them outside overnight.【F:knowledge/notes/input_part006_review.md†L384-L384】
- **Check accessory ergonomics.** Bolt-on saddles push weight rearward and complicate unloading speed bumps, and 2.5 L frame bags are shorter but wider than 3 L options—mock up foot room before committing.【F:knowledge/notes/input_part006_review.md†L94-L94】

## Field Checklist
1. Seal the deck and hub seams before rainy season commutes.【F:knowledge/notes/all_part01_review.md†L86-L87】
2. Test alarms weekly—confirm gyros, hydrometers, and buzzers still trigger in seconds.【F:knowledge/notes/all_part01_review.md†L86-L88】
3. Inspect connectors and controller boards after any water-triggered fault code, cleaning and drying before the next ride.【F:knowledge/notes/denis_all_part02_review.md†L419-L421】
4. Log where each tracker and alarm sits so technicians can service the scooter without cutting hidden hardware.【F:knowledge/notes/all_part01_review.md†L896-L896】【F:knowledge/notes/denis_all_part02_review.md†L454-L455】
