# 3D Printing & Materials for E-Scooter Builds

## Overview

This guide covers 3D printing best practices for creating custom e-scooter parts, including material selection, print settings, and quality control. Whether you're making battery spacers, mounting brackets, or enclosure parts, these field-tested techniques will help you produce durable components.

## What You'll Learn

- Which filaments work best for different applications
- Print settings that prevent failures
- How to achieve strong, durable parts
- Safety considerations when working with materials

## Recommended Materials

### PETG (Polyethylene Terephthalate Glycol)

**Best For**: Deck spacers, mounting brackets, battery holders, general structural parts

**Properties**:
- Good strength and flexibility balance
- Resistant to impacts and vibration
- Works in most climates (but can warp in extreme heat like Las Vegas)[^1]
- Bonds with mechanical fasteners or specialized adhesives[^3]

**Print Settings**:
- **Temperature**: 240-260°C hotend
- **Speed**: 80-120 mm/s with 0.6mm nozzle
- **Layer Height**: 0.3mm at 0.4mm width for strength
- **Bed**: 95°C on textured PEI[^7]
- **Critical**: Dry your filament first! Wet PETG cracks easily[^4]

> **💡 Pro Tip**: Artem's fast PETG profile runs 0.3mm layers at 140 mm/s (~14 mm³/s) and uses filament within 2 days to avoid needing a dryer.[^petg_fast]

### Carbon Fiber PETG

**Best For**: High-strength brackets, motor mounts, load-bearing structural parts

**Two Types**:
1. **True Chopped Fiber** (e.g., Tinmorry): Significantly stronger, can even be turned on a lathe[^2]
2. **Powder-Filled**: Minimal strength benefit, mostly cosmetic

**Requirements**:
- ≥0.6mm hardened steel nozzle (CF is abrasive)
- Heated chamber for best results
- Filament dryer to maintain quality

> **⚠️ Material Note**: Don't waste money on "carbon-filled" filaments that only contain powder. True chopped-fiber versions provide real strength improvements.

### PLA (Polylactic Acid)

**Best For**: Prototypes, jigs, temporary parts, storage fixtures

**Limitations**:
- Warps in high heat environments
- Not suitable for parts exposed to sun or motor heat
- Use for testing designs before printing in PETG

### Specialty Materials

**PEEK & Metal Prints**: Skip these for high-load applications. Even at 150A and 10krpm with heavy riders (130kg), plastic gearboxes fail quickly. Chain drives with QS90 hubs work better in tight spaces.[^8]

**ABS/ASA**: Good for enclosed chamber printing (Bambu P1S) when you need quick turnaround on fixtures and brackets.[^bambu_p1s]

## Critical Print Quality Settings

### For Battery Holders

Battery holders are safety-critical—they must not crack during riding vibration.

**Requirements**:[^4]
1. **Dry filament** - Store in sealed containers with desiccant
2. **Slow down** - 80-120 mm/s prevents layer adhesion issues
3. **Optimize temperature** - 240-260°C for PETG
4. **Tune retraction** - Reduce stringing without causing gaps
5. **Control cooling** - Balance layer adhesion with dimensional accuracy

**Sizing Considerations**:
- Size cups for actual cell diameter (e.g., 21.4mm for P42A vs. 21.15mm for 40P)
- Use high infill so parts flex slightly rather than crack when warm[^petg-holders]

### For Transparent Parts

**Special Requirements**:[^5]
- Print at ~13 mm/s (very slow)
- Minimal cooling fan
- Post-process with polishing for clarity
- Stock Bambu profiles run too hot and cause clouding

### Bed Adhesion

**PEI Sheet Tips**:
- **Smooth PEI**: Grips PETG very aggressively
  - Increase Z-offset by ~0.1mm
  - Or use glass, textured PEI, or glue stick barrier to prevent damage[^smooth_pei_offset]
- **Textured PEI**: Keep clean with dish soap or IPA
  - Heat bed to 95°C for PETG
  - Good grip without excessive adhesion[^7]

## Practical Applications

### Battery Pack Fixtures

**Modular Cases**: Pandalgns' designs include BMS service holes, screw-linked columns, and mesh caps for triangular 10S6P e-bike packs. These keep nickel strips clamped while providing access for maintenance.[^pandalgns-triangle]

**Cell Retention**: PETG relaxes with heat, so design holders with appropriate clearance and high infill for flex without cracking.

### Deck Reinforcement

**Community Files Available**: Ninebot G30 deck brace kits circulate as `middle.stl` plus `front/left/right/rear.3mf` files. These let you reinforce ground decks after heavy use without redrawing geometry.[^g30_brace]

### Sourcing Gap

**Thrust Washers**: Builders are still hunting thin thrust washers to sit between hub shafts and end caps. Stock these in maintenance kits alongside spare controller boards.[^thrust-washers]

## Assembly & Finishing

### Adhesives

When parts need bonding:[^3]
- **Epoxy**: Best for structural joints
- **Cyanoacrylate (Super Glue)**: Quick fixes
- **Specialty plastic adhesives**: For flexible connections
- These bond without melting prints like solvent-based methods

### Connector Assembly

**QS8 Connectors**: Stuffing twin 12 AWG leads is notoriously tight:[^6]
1. Use plenty of flux
2. Fully wet both conductors with solder
3. Layer heat-shrink tubing
4. Be patient when the plastic lid resists latching

## Safety & Health

### Material Handling

**Microplastic Exposure**:[^microplastic-ppe]
- Wear gloves when sanding aluminum or PETG parts
- Wash hands thoroughly before eating
- Fine particulates from working these materials can accumulate
- Consider respiratory protection for heavy sanding

### Print Environment

**Enclosed Printers**: Help contain fumes and maintain temperature
- Especially important for ABS/ASA printing
- Improves part quality and consistency

## Recommended Equipment

### Why Bambu P1S?

The community praises this printer for scooter work:[^bambu_p1s]
- Enclosed chamber for ABS/ASA
- Turnkey slicer profiles
- Fast production of spacers, trays, and brackets
- Minimal tuning needed between prints
- Quick turnaround for test iterations

## Troubleshooting

### PETG Stringing

Artem's solution: Use filament within 2 days of opening so it never needs drying. Alternatively, invest in a good filament dryer and sealed storage.[^petg_fast]

### Cracked Battery Holders

If your holders crack:
1. Verify filament is completely dry
2. Slow print speed to 80-100 mm/s
3. Increase hotend temperature slightly
4. Check that cooling isn't too aggressive
5. Ensure bed adhesion is good (no warping stress)

### Part Warping

- Increase bed temperature
- Ensure drafts aren't cooling parts unevenly  
- Use an enclosure for temperature-sensitive materials
- Add brims or rafts for better first-layer adhesion

## Related Guides

- [Battery Pack Design](battery_pack_design.md) - For battery holder dimensions
- [Chassis Fitment](chassis_fitment.md) - Mounting considerations
- [Power Distribution](power_distribution.md) - Cable routing and brackets

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
