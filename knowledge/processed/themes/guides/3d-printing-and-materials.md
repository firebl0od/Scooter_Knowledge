# 3D Printing & Materials Playbook

## Filament Selection & Tooling

- PETG and carbon-filled PETG handle deck spacers and mounts, but CF blends demand ≥0.6 mm hardened-steel nozzles, heated chambers, and filament dryers to fight brittleness; PLA survives storage yet warps in high-heat climates like Las Vegas.[^1]
- Tinmorry’s true chopped-fibre PETG-CF prints significantly tougher than powder-filled “carbon” blends.
  - builders even turn the parts on lathes, whereas filler-only filaments offer little benefit beyond marketing.[^2]
- Keep epoxy, cyanoacrylate, or specialty plastic adhesives on hand when reinforcing PETG/PLA accessories.
  - these glues bond without melting the print and keep commuter hardware intact.[^3]
- Smooth PEI sheets grip PETG aggressively—bump Z offset ~0.1 mm or switch to glass, textured PEI, FR4, or a glue-stick barrier before ripping the coating during enclosure runs.[^smooth_pei_offset]

## Production Discipline

- PETG battery holders crack when printed wet or too fast; veterans dry filament, slow to 80–120 mm/s with 0.6 mm nozzles, run 240–260 °C hotends, and tune retraction/fan settings before trusting cages to hold 21700 cells.[^4]
- Artem finally tamed PETG stringing by running 0.3 mm layers at 0.4 mm width around 140 mm/s (~14 mm³/s) and cycling rolls within two days so the filament never needs drying on current tooling.[^petg_fast]
- Printing transparent PETG carriers demands ~13 mm/s speeds, minimal cooling, and post-polish to avoid haze.
  - stock Bambu profiles run too hot and cloud the parts immediately.[^5]
- Shops chasing quick turnaround on fixtures keep praising the Bambu P1S because its enclosed chamber and turnkey slicer profil
es spit out ABS/ASA spacers, insulation trays, and lighting brackets without weeks of tuning—handy when you need fresh mounts b
etween test rides.[^bambu_p1s]
- Stuffing twin 12 AWG leads into QS8 shells is notoriously tight.
  - use plenty of flux, fully wet both conductors, and layer heat-shrink when the plastic lid refuses to latch cleanly.[^6]
- Working aluminium or PETG parts throws fine particulates; wear gloves, wash thoroughly, and avoid eating until you clean up to limit microplastic exposure.[^microplastic-ppe]
- Keep textured PEI sheets spotless (dish soap or IPA) and hold the bed near 95 °C so PETG grips without warping; too much adhesion still calls for careful part removal despite the texture.[^7]
- Skip exotic PEEK or metal prints for high-load gearboxes.
  - builders remind 130 kg riders pushing 150 A at 10 krpm that plastic reducers fail fast, while chain drives with QS90 hubs survive cramped frames far better.[^8]

## Battery Fixtures & Hardware

- Xiaomi-class PETG carriers still relax with heat; Finn sizes the cups for 21.4 mm P42A vs. tighter 21.15 mm 40P cans and runs high infill so the pack flexes before cracking when warm.[^petg-holders]
- Pandalgns’ modular battery cases add BMS service holes and screw-linked columns with mesh caps for triangular 10 S6 P bike packs, keeping nickel clamped while leaving room for a dedicated BMS plate.[^pandalgns-triangle]
- Builders are still hunting thin thrust washers to sit between hub shafts and end caps—call out the sourcing gap when assembling maintenance kits alongside spare controller boards.[^thrust-washers]
## Shared Print Assets

- Community brace kits for Ninebot G30 decks now circulate as `middle.stl` plus `front/left/right/rear.3mf` files so builders can reinforce ground decks after heavy grinding without redrawing the geometry from scratch.[^g30_brace]


## References

[^1]: Source: knowledge/notes/input_part006_review.md†L118-L118
[^2]: Source: knowledge/notes/input_part006_review.md†L223-L223
[^3]: Source: knowledge/notes/input_part006_review.md†L120-L120
[^4]: Source: knowledge/notes/input_part006_review.md†L192-L192
[^5]: Source: knowledge/notes/input_part006_review.md†L243-L243
[^6]: Source: knowledge/notes/input_part006_review.md†L194-L194
[^microplastic-ppe]: Source: knowledge/notes/input_part006_review.md†L90-L90
[^7]: Source: knowledge/notes/input_part006_review.md†L362-L362
[^8]: Source: knowledge/notes/input_part006_review.md†L363-L363
[^bambu_p1s]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24552-L24554
[^petg-holders]: Source: knowledge/notes/input_part010_review.md†L432-L433
[^pandalgns-triangle]: Source: knowledge/notes/input_part010_review.md†L438-L438
[^thrust-washers]: Source: knowledge/notes/input_part010_review.md†L411-L412
[^petg_fast]: Source: knowledge/notes/input_part002_review.md†L645-L646
[^g30_brace]: Source: knowledge/notes/input_part002_review.md†L526-L526
[^smooth_pei_offset]: Source: knowledge/notes/input_part002_review.md†L19661-L19664
