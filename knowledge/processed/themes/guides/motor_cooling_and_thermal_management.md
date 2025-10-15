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

## Ferrofluid Handling & Hub Maintenance
- Dose scooter hubs with roughly 3–6 ml of Statorade (60 mm motors stretch to 7–8 ml) only after the stator is seated; plastic syringes keep filings out while the magnets self-level the fluid.【F:knowledge/notes/input_part001_review.md†L613-L615】
- Reseal side covers with silicone and revisit fills seasonally—vent holes can shave another 5–10 °C on smaller motors but risk weeping ferrofluid and inviting water, so log temps before committing to drilled covers.【F:knowledge/notes/input_part001_review.md†L613-L615】
- Wolf Warrior hubs that survived ~10,000 km came back with cracked phase insulation and missing hall boards; use refreshes to rewire phases, embed new hall sensors, and add Statorade while the shell is open.【F:knowledge/notes/input_part001_review.md†L626-L627】

## Cooling Accessory Reality Checks
- 3D-printed “hub fin” shells draw criticism because blocked airflow paths limit their effectiveness—testers prefer spacing the fins with washers or pivoting to ferrofluid/oil cooling when they need real thermal headroom.【F:knowledge/notes/input_part001_review.md†L672-L674】
- Judge cooling tweaks only with controlled A/B runs on fully cooled motors; hub-shell surface temperature alone says little about magnet health, so embed sensors or log winding temps before declaring success.【F:knowledge/notes/input_part001_review.md†L674-L674】

## Coil Retention & Harness Dressing
- Inside hub motors, standard nylon cable ties survive stator temperatures when cinched correctly; some builders still wrap phases with cotton rope for redundancy, so combining both methods keeps windings tight without melting ties.【F:knowledge/notes/input_part014_review.md†L185-L185】

## Adhesives & Sensor Retention
- Hall sensors that walk out of their slots should be glued with heat-tolerant RTV 704 or slow-drying high-temp silicone; super glue works after scuffing the pocket but runs hotter under load.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131261-L131275】
- Keep 704 RTV on the bench for accessory wiring too—the same adhesive secures buck-converter leads so vibration cannot snap them before the scooter ever rolls out.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L31-L32】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131265-L131275】
