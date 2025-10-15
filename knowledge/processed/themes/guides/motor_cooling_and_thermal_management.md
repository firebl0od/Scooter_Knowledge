# Motor Cooling & Thermal Management Notes

## Why Fans Rarely Help Scooter Hubs
- Denis Yurev reminded the workshop that scooters already move fresh air past the hub at riding speed, so bolt-on fan kits add little cooling compared with ensuring good heat transfer from the windings to the shell.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L422-L441】
- Riders debating CPU-style blowers learned that evaporation-driven skin cooling does not apply to dry aluminum shells; without a wet surface the only lever is temperature delta, so focus on conductive paths instead of add-on spinners.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L424-L441】
- Veterans recommended ferrofluid or oil-fill experiments (with leak safeguards) if you need real winding-to-shell transfer—simply drilling covers or gluing “windmills” to the hub only cools the outer case.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L456-L520】

## Controller Interface Refresh Checklist
- When raising voltage, replace Kapton tape with 0.5 mm thermal pads so MOSFETs stay isolated yet shed heat; stacking pads on top of Kapton just adds resistance.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L202-L223】
- Sand controller bases, clean MOSFET tabs, and reinstall paste before clamping the box—loose wiring under the plate prevents full contact and spikes temperatures on the first ride.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60020-L60025】
- Keep silicone pads on hand when chasing 48 V/15 S tunes; the crew pairs IRFB4110 MOSFETs with 100 V 1,000 µF and 47 µF capacitors and swaps pads plus paste before closing the case.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60009-L60024】

## Temperature Guardrails
- Battery temps around 41 °C were deemed healthy for summer rides, but the group flagged ~60 °C as a ceiling—anything hotter accelerates degradation and calls for gentler tunes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60004-L60008】
- Larger packs and long shocks trap heat around the deck; riders re-bend frames, add inner/outer steel plates, and swap to lower-rate springs instead of trimming coils so the chassis and cells stop cooking each other.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L90030-L90136】

## Overload Warning Signs
- Pushing a stock 350 W Ninebot MAX hub to ~5 kW on 72 V/35 A tunes cooks magnets and windings—the rotor feels “full of honey” when spun by hand, signalling demagnetisation or shorts that no amount of firmware tweaking will fix.【F:knowledge/notes/input_part006_review.md†L42-L42】

## Sealed Bearing Service Cheatsheet
- Pack sealed bearings to roughly 30 % of the cavity with high-temperature grease (Mobil XHP 222 or similar); overfilling to 100 % just churns heat and purges grease past the seals on the first ride.【F:knowledge/notes/input_part006_review.md†L509-L509】
- Choose C3 clearance bearings when hubs see high heat or prolonged highway runs—the extra internal play prevents bind-up once the races expand.【F:knowledge/notes/input_part006_review.md†L509-L509】
- Document every bearing change with mileage and grease type so follow-up inspections can flag premature wear before shells overheat or magnets rub.【F:knowledge/notes/input_part006_review.md†L509-L509】

## Weatherproofing Hub Cavities
- Tear down Ninebot F2 Pro hubs after rain commutes—the factory 6001RS bearings arrive nearly dry, so riders repack them with marine or polyurea grease and upgrade to premium SKF RSH 2RS units rather than smearing silicone over the caps.【F:knowledge/notes/input_part006_review.md†L409-L410】
- When resealing Zero or Vsett hubs, apply silicone at seam joints, refresh lithium grease on the bearings, and avoid overfilling so heat can still escape; the goal is to stop rust and hall failures without trapping moisture against the windings.【F:knowledge/notes/input_part006_review.md†L368-L368】【F:knowledge/notes/input_part006_review.md†L488-L488】

## Coil Retention & Harness Dressing
- Inside hub motors, standard nylon cable ties survive stator temperatures when cinched correctly; some builders still wrap phases with cotton rope for redundancy, so combining both methods keeps windings tight without melting ties.【F:knowledge/notes/input_part014_review.md†L185-L185】

## Adhesives & Sensor Retention
- Hall sensors that walk out of their slots should be glued with heat-tolerant RTV 704 or slow-drying high-temp silicone; super glue works after scuffing the pocket but runs hotter under load.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131261-L131275】
- Keep 704 RTV on the bench for accessory wiring too—the same adhesive secures buck-converter leads so vibration cannot snap them before the scooter ever rolls out.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L31-L32】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131265-L131275】
