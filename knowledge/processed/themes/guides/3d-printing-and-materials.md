# 3D Printing & Materials Playbook

## Filament Selection & Tooling

- PETG and carbon-filled PETG handle deck spacers and mounts, but CF blends demand ≥0.6 mm hardened-steel nozzles, heated chambers, and filament dryers to fight brittleness; PLA survives storage yet warps in high-heat climates like Las Vegas.[^1]
- Tinmorry’s true chopped-fibre PETG-CF prints significantly tougher than powder-filled “carbon” blends.
  - builders even turn the parts on lathes, whereas filler-only filaments offer little benefit beyond marketing.[^2]
- Keep epoxy, cyanoacrylate, or specialty plastic adhesives on hand when reinforcing PETG/PLA accessories.
  - these glues bond without melting the print and keep commuter hardware intact.[^3]

## Production Discipline

- PETG battery holders crack when printed wet or too fast; veterans dry filament, slow to 80–120 mm/s with 0.6 mm nozzles, run 240–260 °C hotends, and tune retraction/fan settings before trusting cages to hold 21700 cells.[^4]
- Printing transparent PETG carriers demands ~13 mm/s speeds, minimal cooling, and post-polish to avoid haze.
  - stock Bambu profiles run too hot and cloud the parts immediately.[^5]
- Shops chasing quick turnaround on fixtures keep praising the Bambu P1S because its enclosed chamber and turnkey slicer profil
es spit out ABS/ASA spacers, insulation trays, and lighting brackets without weeks of tuning—handy when you need fresh mounts b
etween test rides.[^bambu_p1s]
- Stuffing twin 12 AWG leads into QS8 shells is notoriously tight.
  - use plenty of flux, fully wet both conductors, and layer heat-shrink when the plastic lid refuses to latch cleanly.[^6]
- Keep textured PEI sheets spotless (dish soap or IPA) and hold the bed near 95 °C so PETG grips without warping; too much adhesion still calls for careful part removal despite the texture.[^7]
- Skip exotic PEEK or metal prints for high-load gearboxes.
  - builders remind 130 kg riders pushing 150 A at 10 krpm that plastic reducers fail fast, while chain drives with QS90 hubs survive cramped frames far better.[^8]


## References

[^1]: Source: knowledge/notes/input_part006_review.md†L118-L118
[^2]: Source: knowledge/notes/input_part006_review.md†L223-L223
[^3]: Source: knowledge/notes/input_part006_review.md†L120-L120
[^4]: Source: knowledge/notes/input_part006_review.md†L192-L192
[^5]: Source: knowledge/notes/input_part006_review.md†L243-L243
[^6]: Source: knowledge/notes/input_part006_review.md†L194-L194
[^7]: Source: knowledge/notes/input_part006_review.md†L362-L362
[^8]: Source: knowledge/notes/input_part006_review.md†L363-L363
[^bambu_p1s]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24552-L24554
