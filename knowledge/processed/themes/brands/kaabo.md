# Kaabo & Wolf King Platform Notes
## TL;DR

- Wolf King GT conversions quickly overrun stock welding and Daly protection once 22 S builds push past ~160 A battery; plan busbar upgrades, higher-spec BMS hardware, and thermal monitoring before chasing 20 kW launches.[^1]
- Deck packaging limits still constrain dual-controller 22 S installs—expect to add spacers or mount controllers externally to route 10 mm² phase leads and heavier harnessing without pinching cables.[^2][^3]
- Blade GT+ waterproofing demands selective sealant and bearing service; avoid heavy coatings that trap heat around the stator during high-load runs.[^4]
- Recurrent Mantis fires—including parked scooters—are being blamed on underspec batteries and poor crimps; Kaabo’s 40 A fuse response (versus 55 A draw) deepened distrust and even spurred reports of a regional blacklist.[^5][^6]
- Long-term Mantis riders are modeling CNC collar replacements because grade 12.9 bolts still stretch or rust through by ~10 k km—plan improved coatings and grease alongside the hardware swap.[^7]
- Simone’s 21 S 6 P Samsung 35E Mantis and Face de Pin Sucé’s 24.8 kg daily rider prove Kaabo frames can hide 30 kW-class packs when you budget spacers, SmartDisplay telemetry, and serious cooling—set expectations around deck height and airflow before promising stealth builds.[^mantis_high_density][^mantis_daily_spec]

## Wolf King GT Build Guidance

- Stock Daly packs sag and trip near 160 A combined battery draw once 22 S controllers are installed, so rebuild the busbars and upgrade to BMS hardware that tolerates higher burst currents before raising limits.[^1]
- Wolf decks only fit one large controller without risers; dual-controller conversions rely on 3D-printed spacers, staggered mounting, and careful cable routing to keep 22 S harnesses from chafing or overheating.[^2]
- Stock pack options span 16 S10 P 18650 (Warrior), 16 S7 P 21700 (Warrior GT), 20 S8 P 18650 (Wolf King), and 20 S7 P 21700 (Wolf King GT), but the cramped deck (≈172 × 70 × 430 mm internal volume, ~68 mm usable height once wiring is routed) still forces controllers outside and leaves little upgrade room—budget wiring changes before promising higher-current packs.[^ip001-wolf-pack]
- Remanufacturers now order custom 3 mm rotors and 10 mm² phase looms for Wolf/VSETT builds targeting >300 A launches—have CAD ready for rotor suppliers and budget thicker cabling to stop voltage drop on high-current pulls.[^3]

## Blade & GT-Series Chassis Care

- Apply sealant only where water intrusion has been observed, service bearings, and skip thick insulating sprays; over-coating traps heat inside the motors during repeated hard pulls.[^4]
- Segway GT tear-downs show Hope V4 brake swaps and wider rotor packaging translating to Kaabo GT projects—log rotor thickness and caliper clearance before committing to DOT-fluid conversions on Wolf or Blade frames.[^8]
- German riders chasing road legality are experimenting with VSETT 48 V controllers to retain Kaabo dashboards while unlocking 16 S support—expect wiring adapters but a friendlier compliance path than full VESC swaps.[^9]

## Mantis High-Power Builds

- High-density Mantis conversions now squeeze 21 S 6 P Samsung 35E or even 24 S 7 P packs under the deck with spacers and external cooling; expect ~32 kW peaks around 82 V and plan SmartDisplay telemetry plus airflow before replicating the setup.[^mantis_high_density]
- Daily commuter trims still hit 75 km/h on 8.5″ tyres by pairing a narrowed FHT60 motor, SmartDisplay logging, and a 21 S 6 P pack while keeping weight under 25 kg.[^mantis_daily_spec]

## Cockpit & Display Roadmap

- Kaabo is prototyping a sealed TFT throttle/display that could slot into VESC builds if the protocol matches—track compatibility tests as a compact alternative to Android dash experiments.[^10]

# Kaabo Brand Snapshot

- Wolf Warrior X frames keep their reputation as durable, all-weather commuters—buyers report €500 rollers and even $750 riders logging 7,500 km as fair purchases so long as pack health and lighting budgets are accounted for.[^11]
- Stock BMS units hide under sealed decks; experienced owners crack the lid and probe parallel groups manually until a telemetry-capable replacement or smart-BMS tap is installed.[^12]
- Fresh teardowns reveal over-tightened steering columns with dry bearings and threadlocked centre screws—freeing the headset requires full disassembly, re-greasing, and careful re-torque to restore smooth steering.[^13]
- Chassis upgrades lean on laser-cut 10 mm torque plates and automotive rotor alloys to tame 20 S launches; forged solutions remain rare, so builders plan around heavy steel plates when chasing Lonnyo-class hubs.[^14]
- Even boutique Dualtron/Kaabo fabricators still machine axles and spacers on manual lathes despite CNC debates, highlighting the hybrid of hand craftsmanship and outsourced production that supports high-power builds.[^15]

## Secondary Market & Ownership Notes

- Confirm battery state-of-health before committing to used Wolf Warrior purchases; even well-priced rollers may need pack refurbishments and replacement headlights to meet commuter expectations.[^16]
- Budget immediate headset service—dry bearings and threadlocked centre screws bind the front end from the factory. Removing the stem, cleaning threads, adding grease, and re-torquing brings the steering back to normal.[^13]

## Electrical & Safety Reminders

- Treat the sealed OEM BMS as a temporary solution. Until a smart BMS or telemetry tap goes in, riders manually monitor cell groups to catch imbalances early.[^12]
- High-power upgrades call for custom torque plates and thicker rotor materials—laser-cut 1 cm steel remains the baseline for reining 20 S launches without deforming the stock dropouts.[^14]
- Confirm hall sensor coverage before controller swaps—older square-wave Kaabo hubs often omit halls while Wolf King GT sine packages include them, saving retrofit time.[^ip001-hall-coverage]

## Sourcing & Upgrade Watchlist

- Factor lighting upgrades into purchase budgets; OEM headlights fail cheaply and often, so commuters planning weatherproof builds add replacements alongside battery inspections.[^17]
- Keep an eye on aftermarket torque-arm kits and brake upgrades that ship with thicker plates—most Wolf Warrior X builds still rely on community-fabricated steel to manage Lonnyo or QS hub swaps.[^14]

## Source Notes

- Wolf Warrior resale values, BMS monitoring habits, steering column service requirements, and torque-plate fabrication expectations derive from the 2025 VESC Help Group recap covering lines 6925–7075 and 10663–10700 of `input_part014` slices.[^18]

## References

[^1]: Source: data/vesc_help_group/text_slices/input_part003.txt, L22671 to L22774
[^2]: Source: data/vesc_help_group/text_slices/input_part003.txt, L20149 to L20210
[^3]: Source: data/vesc_help_group/text_slices/input_part003.txt, L25807 to L25888
[^4]: Source: data/vesc_help_group/text_slices/input_part003.txt, L22936 to L22975
[^5]: Source: data/vesc_help_group/text_slices/input_part003.txt, L103 to L120
[^6]: Source: data/vesc_help_group/text_slices/input_part003.txt, L227 to L228
[^7]: Source: data/vesc_help_group/text_slices/input_part003.txt, L18358 to L18376
[^8]: Source: data/vesc_help_group/text_slices/input_part003.txt, L24802 to L25463
[^9]: Source: data/vesc_help_group/text_slices/input_part003.txt, L2201 to L2206
[^10]: Source: data/vesc_help_group/text_slices/input_part003.txt, L9804 to L9808
[^11]: Source: knowledge/notes/input_part014_review.md, L218 to L222
[^12]: Source: knowledge/notes/input_part014_review.md, L230 to L231
[^13]: Source: knowledge/notes/input_part014_review.md, L268 to L271
[^14]: Source: knowledge/notes/input_part014_review.md, L272 to L276
[^15]: Source: knowledge/notes/input_part014_review.md, L117 to L117
[^16]: Source: knowledge/notes/input_part014_review.md, L218 to L226
[^17]: Source: knowledge/notes/input_part014_review.md, L220 to L222
[^18]: Source: knowledge/notes/input_part014_review.md, L218 to L276
[^mantis_high_density]: Source: data/vesc_help_group/text_slices/input_part004.txt†L25331-L25384
[^mantis_daily_spec]: Source: data/vesc_help_group/text_slices/input_part004.txt†L25380-L25391
[^ip001-wolf-pack]: Source: data/vesc_help_group/text_slices/input_part001.txt†L26535-L26855
[^ip001-hall-coverage]: Source: data/vesc_help_group/text_slices/input_part001.txt†L27111-L27168
