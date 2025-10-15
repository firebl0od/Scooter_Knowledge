# Motor Cooling & Thermal Management Notes

## Why Fans Rarely Help Scooter Hubs
- Denis Yurev reminded the workshop that scooters already move fresh air past the hub at riding speed, so bolt-on fan kits add little cooling compared with ensuring good heat transfer from the windings to the shell.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L422-L441】
- Riders debating CPU-style blowers learned that evaporation-driven skin cooling does not apply to dry aluminum shells; without a wet surface the only lever is temperature delta, so focus on conductive paths instead of add-on spinners.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L424-L441】
- Veterans recommended ferrofluid or oil-fill experiments (with leak safeguards) if you need real winding-to-shell transfer—simply drilling covers or gluing “windmills” to the hub only cools the outer case.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L456-L520】

## Ferrofluid Selection & Handling
- The VESC Help crew continues to vouch for ferrofluid/Statorade when the goal is winding-to-shell transfer, but they emphasise reading datasheets—some mixes flash at low temperature and budget hubs can demagnetise above ~80 °C—before flooding a motor.【F:knowledge/notes/input_part007_review.md†L48-L48】
- Ferrotec APG1110 remains the benchmark for hub fillings, while Supermagnete’s 10 mL bottles offer reliable sourcing for EU riders upgrading Xiaomi and G30 hubs without importing large lots.【F:knowledge/notes/input_part007_review.md†L60-L60】

## Hub Current Guardrails
- Single Monorim 500 W hubs stay happy around 80 A phase—ideally with ferrofluid—while the crew’s Xiaomi-class builds overheat quickly once they push 65–73 A without battery temperature sensing or keep more than roughly 30–35 A combined draw from paired 12 S packs.【F:knowledge/notes/input_part007_review.md†L18-L19】

## Controller Interface Refresh Checklist
- When raising voltage, replace Kapton tape with 0.5 mm thermal pads so MOSFETs stay isolated yet shed heat; stacking pads on top of Kapton just adds resistance.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L202-L223】
- Sand controller bases, clean MOSFET tabs, and reinstall paste before clamping the box—loose wiring under the plate prevents full contact and spikes temperatures on the first ride.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60020-L60025】
- Keep silicone pads on hand when chasing 48 V/15 S tunes; the crew pairs IRFB4110 MOSFETs with 100 V 1,000 µF and 47 µF capacitors and swaps pads plus paste before closing the case.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60009-L60024】

## Controller Mounting & Airflow Discipline
- Track-focused builders now strip paint, drill fresh bolt holes, clamp controllers with washers and threadlocker, add thermal paste, and route heat into the chassis or external sinks; relying on foam or internal fans in sealed bays just cooks the controllers.【F:knowledge/notes/input_part007_review.md†L26-L26】【F:knowledge/notes/input_part007_review.md†L28-L28】
- External fins need real airflow—drop the heatsink through the deck, drill and tap anchors, and bolt the controller straight to the frame with paste; leaving fins flush inside the deck traps hot air.【F:knowledge/notes/input_part007_review.md†L83-L83】
- Skip brazing aluminum frames for heatsink bonding unless you have specialty tooling; even experienced metalworkers called it a last resort compared with mechanical fasteners.【F:knowledge/notes/input_part007_review.md†L78-L78】
- When clamping copper blocks to aluminum frames, isolate them with silicone sheets or plating; bare copper-on-aluminum mounts trigger galvanic corrosion that quietly eats the chassis.【F:knowledge/notes/input_part007_review.md†L321-L322】
- Dial in airflow paths after rework—builders now notch decks, tap fins, and bridge controllers to fresh-cut ducts so heat actually leaves the bay instead of recirculating behind sealed covers.【F:knowledge/notes/input_part007_review.md†L537-L537】

## Temperature Guardrails
- Battery temps around 41 °C were deemed healthy for summer rides, but the group flagged ~60 °C as a ceiling—anything hotter accelerates degradation and calls for gentler tunes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60004-L60008】
- Makerbase 100/100-class controllers start current limiting once MOSFETs touch ~70 °C if the base plate lacks fresh thermal paste; the crew now treats 70 °C as the everyday limit and 100 °C as the hard ceiling for VESC MOSFETs to preserve lifespan.【F:data/vesc_help_group/text_slices/input_part007.txt†L123-L146】
- Larger packs and long shocks trap heat around the deck; riders re-bend frames, add inner/outer steel plates, and swap to lower-rate springs instead of trimming coils so the chassis and cells stop cooking each other.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L90030-L90136】

## Coil Retention & Harness Dressing
- Inside hub motors, standard nylon cable ties survive stator temperatures when cinched correctly; some builders still wrap phases with cotton rope for redundancy, so combining both methods keeps windings tight without melting ties.【F:knowledge/notes/input_part014_review.md†L185-L185】

## Adhesives & Sensor Retention
- Hall sensors that walk out of their slots should be glued with heat-tolerant RTV 704 or slow-drying high-temp silicone; super glue works after scuffing the pocket but runs hotter under load.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131261-L131275】
- Keep 704 RTV on the bench for accessory wiring too—the same adhesive secures buck-converter leads so vibration cannot snap them before the scooter ever rolls out.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L31-L32】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131265-L131275】
- After water ingress, reseal hubs immediately with neutral-cure RTV (Ali 704/705); acidic silicones corrode laminations and a single wet commute can kill rear controllers once the factory bead is disturbed.【F:knowledge/notes/input_part007_review.md†L330-L332】
- When reopening controller bays, clean out the factory bead, repaste, and reseal with breathable neutral-cure silicone or fresh gaskets—Izuna’s team warns that over-sealing traps condensation while loose lids invite corrosion inside the logic bay.【F:knowledge/notes/input_part007_review.md†L508-L508】
