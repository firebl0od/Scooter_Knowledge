# Kaabo & Wolf King Platform Notes

## TL;DR
- Wolf King GT conversions quickly overrun stock welding and Daly protection once 22 S builds push past ~160 A battery; plan busbar upgrades, higher-spec BMS hardware, and thermal monitoring before chasing 20 kW launches.【F:data/vesc_help_group/text_slices/input_part003.txt†L22671-L22774】
- Deck packaging limits still constrain dual-controller 22 S installs—expect to add spacers or mount controllers externally to route 10 mm² phase leads and heavier harnessing without pinching cables.【F:data/vesc_help_group/text_slices/input_part003.txt†L20149-L20210】【F:data/vesc_help_group/text_slices/input_part003.txt†L25807-L25888】
- Blade GT+ waterproofing demands selective sealant and bearing service; avoid heavy coatings that trap heat around the stator during high-load runs.【F:data/vesc_help_group/text_slices/input_part003.txt†L22936-L22975】
- Recurrent Mantis fires—including parked scooters—are being blamed on underspec batteries and poor crimps; Kaabo’s 40 A fuse response (versus 55 A draw) deepened distrust and even spurred reports of a regional blacklist.【F:data/vesc_help_group/text_slices/input_part003.txt†L103-L120】【F:data/vesc_help_group/text_slices/input_part003.txt†L227-L228】
- Long-term Mantis riders are modeling CNC collar replacements because grade 12.9 bolts still stretch or rust through by ~10 k km—plan improved coatings and grease alongside the hardware swap.【F:data/vesc_help_group/text_slices/input_part003.txt†L18358-L18376】

## Wolf King GT Build Guidance
- Stock Daly packs sag and trip near 160 A combined battery draw once 22 S controllers are installed, so rebuild the busbars and upgrade to BMS hardware that tolerates higher burst currents before raising limits.【F:data/vesc_help_group/text_slices/input_part003.txt†L22671-L22774】
- Wolf decks only fit one large controller without risers; dual-controller conversions rely on 3D-printed spacers, staggered mounting, and careful cable routing to keep 22 S harnesses from chafing or overheating.【F:data/vesc_help_group/text_slices/input_part003.txt†L20149-L20210】
- Remanufacturers now order custom 3 mm rotors and 10 mm² phase looms for Wolf/VSETT builds targeting >300 A launches—have CAD ready for rotor suppliers and budget thicker cabling to stop voltage drop on high-current pulls.【F:data/vesc_help_group/text_slices/input_part003.txt†L25807-L25888】

## Blade & GT-Series Chassis Care
- Apply sealant only where water intrusion has been observed, service bearings, and skip thick insulating sprays; over-coating traps heat inside the motors during repeated hard pulls.【F:data/vesc_help_group/text_slices/input_part003.txt†L22936-L22975】
- Segway GT tear-downs show Hope V4 brake swaps and wider rotor packaging translating to Kaabo GT projects—log rotor thickness and caliper clearance before committing to DOT-fluid conversions on Wolf or Blade frames.【F:data/vesc_help_group/text_slices/input_part003.txt†L24802-L25463】
- German riders chasing road legality are experimenting with VSETT 48 V controllers to retain Kaabo dashboards while unlocking 16 S support—expect wiring adapters but a friendlier compliance path than full VESC swaps.【F:data/vesc_help_group/text_slices/input_part003.txt†L2201-L2206】

## Cockpit & Display Roadmap
- Kaabo is prototyping a sealed TFT throttle/display that could slot into VESC builds if the protocol matches—track compatibility tests as a compact alternative to Android dash experiments.【F:data/vesc_help_group/text_slices/input_part003.txt†L9804-L9808】
