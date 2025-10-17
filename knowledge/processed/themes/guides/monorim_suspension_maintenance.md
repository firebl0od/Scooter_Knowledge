# Monorim Suspension & Hardware Guide

## Overview

Monorim produces popular aftermarket suspension kits and performance upgrades for Xiaomi, Ninebot, and other compact scooters. This guide covers installation, maintenance, and common issues with Monorim front forks, rear shocks, and related hardware. Understanding these upgrades' limitations and proper setup procedures is essential for safe operation, especially on high-power builds. Quality suspension dramatically improves ride comfort and handling, but requires careful assembly and regular maintenance.

## What You'll Learn

- Recommended suspension combinations (forks, shocks, tires)
- When to upgrade from budget to premium suspension arms
- Proper installation procedures and common assembly mistakes
- Hardware quality issues and necessary upgrades
- Spring and shock tuning for different rider weights
- Compatibility considerations for motor and brake upgrades
- Maintenance requirements and spare parts to stock

## 🔧 Suspension Basics

💡 **Key principle**: Suspension setup is personal - what works for one rider won't work for another.

## 📋 Quick Reference: Spring Setup by Rider Weight

| Rider Weight | Front Spring Rate | Rear Spring Rate | Sag Target |
|--------------|------------------|------------------|------------|
| <60 kg | Softer (stock or -10%) | Softer (stock or -10%) | 25-30% |
| 60-80 kg | Stock | Stock | 20-25% |
| 80-100 kg | Stiffer (+10-20%) | Stiffer (+10-20%) | 20-25% |
| >100 kg | Stiffer (+20-30%) | Stiffer (+20-30%) | 15-20% |

💡 **Pro Tip**: Measure sag with rider gear on. Full gear adds 5-10 kg.

## 📋 Maintenance Schedule

| Task | Frequency | Difficulty | Time | Critical? |
|------|-----------|------------|------|-----------|
| Visual inspection | Weekly | ⭐ Easy | 2 min | ✅ Yes |
| Clean stanchions | Monthly | ⭐ Easy | 10 min | ✅ Yes |
| Check preload | Monthly | ⭐⭐ Medium | 15 min | ✅ Yes |
| Oil change | 6 months / 1000km | ⭐⭐⭐ Hard | 1 hour | ✅ Yes |
| Seal replacement | Annually / 2000km | ⭐⭐⭐⭐ Expert | 2 hours | ✅ Yes |

## ⚠️ Common Mistakes

🔴 **Too much preload** - Makes ride harsh, damages seals
🔴 **Wrong oil viscosity** - Causes either harsh or mushy feel
🔴 **Dirty stanchions** - Scratches seals, causes leaks
🔴 **Skipping seal lubrication** - Premature seal wear

## 🔧 Related Guides

- [Chassis Fitment](chassis_fitment.md) - Suspension mounting and compatibility
- [Scooter Diagnostic Toolkit](scooter_diagnostic_toolkit.md) - Tools for suspension work

## Core Principles

- **Build around quality pneumatics and matched shocks.** Pair Monorim front forks with DNM or EXA dampers and a proper rear shock; foam “solid” tires and mismatched hardware shake magnets loose above ~45 km/h.[^1][^2]
- **Know when to upgrade arms.** Budget Monorim castings keep costs low but flex under 3 kW loads; European-made Konyk or Dereza arms cost about €100 per end yet deliver better travel and durability for <60 km/h builds that need reliable torque-arm integration.[^3]
- **Expect machining mismatches.** Aftermarket forks or CNC bodies still arrive out of tolerance, and even “upgraded” Monorim rear arms have shipped without the advertised accessories—lean on community teardown photos and shared hardware swaps during assembly.[^denis-machining]
- **Tighten bushings for high-power swaps.** Upgraded bushings, washers, or custom-machined spacers tame slop when Monorim forks carry 3 kW-class motors.
  - and some builders consider Konyk arms purely to simplify torque-arm integration.[^4]
- **KKE shocks beat EXA 388/291 for light riders.** 60 kg owners are starting around 650–850 lb springs (1,000 lb on twin-shock setups) and only stepping up if they want a firmer feel, noting better damping than EXA units in the same weight class.[^5]
- **Recreate the factory hardware stack.** Reinstall the short upper screw, small top ring, and fresh bearings during stem assemblies.
  - missing parts are the leading cause of Monorim wobble.[^6]
- **Watch for Monorim’s grey mast revision.** The double-welded tube fixes early cracking but still needs a notch in the controller box to route wiring cleanly.[^grey_mast_revision]
- **Upgrade fasteners immediately.** Swap the kit’s soft bolts for grade 12.9 hardware, trim overly long screws, and add washers/Loctite so pivots stop loosening and knocking after a few rides.[^7][^8]
- **Spec proper shoulder hardware for fork swaps.** Grade 12.9 shoulder bolts or custom stainless axles hold alignment far better than the inconsistent AliExpress kits, and missing inner washers or soft brackets twist calipers until custom steel plates replace the stock hardware.[^monorim_axle][^monorim_bracket]
- **Kill stem play without over-torquing.** Loosen the side bolts, snug the centre hinge screw just enough to remove wobble, then re-lock the pinch bolts—over-clamping snaps the bolt and causes crashes.[^stem_play_fix]
- **Track the MXR1 V2 rear revision.** The updated swingarm adds brake-mount holes and a washer pocket; until the new run lands, hand-cut the recess or salvage parts from dual-suspension owners to stop axle clamp stripping.[^denis-mxr1-v2]
- **Bring spare shims for V4 kits.** Recent batches ship without the washer stack Kroxne documents, so expect to fabricate or source your own spacers to remove fork play.[^denis-v4-shims]
- **Upgrade fasteners immediately.** Swap the kit’s soft bolts for grade 12.9 hardware, trim overly long screws, add washers/Loctite, and recheck play so loosened pivots stop chewing bearings or slicing nearby harnesses after a few rides.[^7][^8]
- **Replace the thin M3 fender bolts.** The stock fasteners shear quickly on Monorim’s V4 fender bracket, so swap them before the adapter loosens or the rotor rubs.[^denis-v4-m3]
- **Stock spare suspension hardware.** Keep folding pins, spacers, brake cables, pads, and even a V3 controller clone on hand so a failure doesn’t sideline the scooter while AliExpress parts ship.[^denis-spares]
- **Match spring hardware to rider weight.** EXA 291 coils (150–350 lb springs) stay supple for ~90 kg riders, while RockShox or Fox air shocks add adjustability.
  - just confirm leverage ratios and clearance before swapping hardware.[^9]
- **Lightweight rider coils:** ≈55 kg riders report the best compliance with 150–250 lb EXA/DNM coils around 90–95 mm length sourced from AliExpress for ~€20; stock 650 lb Monorim springs prove too harsh once speeds climb.[^10]
- **Treat Monorim-branded packs and AWD kits as projects, not plug-and-play.** External batteries ship without brake/BMS harnesses, cheap charge-line diodes waste voltage, and the 48 V AWD bundle under-delivers.
  - build your own pack/controller stack instead.[^11][^12][^13]
- **Treat Monorim-branded packs and AWD kits as projects, not plug-and-play.** External batteries ship without brake/BMS harnesses, cheap charge-line diodes waste voltage, and the 48 V AWD bundle under-delivers.
  - build your own pack/controller stack instead.[^11][^12][^14]
- **Mind brake adapters and clearance.** The 500 W disc adapter replaces the dust cover (don’t stack it), expect to machine or source custom rear spacers because Monorim won’t sell the bracket separately, budget a second hydraulic brake for 50 km/h builds, and remember that premium Braking Incas 2 kits can strike the ground unless banjos are flipped and clearances double-checked on extended Monorim arms.[^15][^16][^17][^18][^19]
- **Reinforce Monorim’s bolt-on front caliper bracket.** The two small screws struggle with 120 mm rotors; add adhesive or aftermarket hardware and keep the hub bearings packed with grease—stock units run nearly dry and fail around 1 000 km without service.[^front_bracket_warning]
- **Redesign clamp spacers when stems interfere.** Builders are revising the front clamp block and adding extenders so Sokil/Konyk stem hardware clears the fork arms without killing the folding lock.[^20]
- **Reinforce long-shock installs with full “sandwich” plates and softer springs.** Welding gussets on one side just drives the rear arm into the deck; add inner/outer steel plates, re-bend the chassis with the battery removed, and source lower-rate springs instead of cutting coils.[^21]
- **Size coils for rider weight.** ~55 kg riders are swapping stock 650 lb coils for 150–250 lb EXA/DNM options (~90–95 mm length) sourced for ~€20 on AliExpress to improve small-bump response.[^10]
- **Mind fork bending projects.** Custom VSETT conversions that cold-set Monorim forks need ~16 mm wider dropouts, 160 mm-from-axle bends, longer hardware, and carefully machined spacers.
  - stacked washers or thin arms crack once 160 mm rotors and 150 mm axles enter the mix.[^22][^23]
- **Respect axle width ceilings.** Rion-spec 150–160 mm axles from 70 mm magnet hubs simply don’t fit the Monorim fork cavity; builders either machine new side plates or reserve those motors for larger Zero 11X-class frames rather than overstressing the arms.[^24]

## Hardware Checklist

| Area | Baseline Actions | Notes |
| --- | --- | --- |
| **Stem & crown** | Reuse the OEM short screw and ring, press new bearings, torque gradually while cycling the fork to settle spacers.[^6] | Missing pieces cause wobble within the first ride. |
| **Upper brace** | Install the shared 6061 brace or machine equivalents from the released STEP files; pair with grade 12.9 axles, quality M8 hardware, and new bearings to tighten the cockpit before VESC upgrades.[^25] | CNC services (PCBWay/JLCPCB) can turn the files quickly; expect riders to fabricate matching torque plates next. |
| **Axles & spacers** | Ignore the “304 stainless” marketing.
  - magnets still stick; replace with grade 12.9 or titanium fasteners and confirm spacer stacks before tightening.[^26][^27]
  - the rear motor kit’s long nut and spacer stay too short for high-power hubs, so source longer shafts and hardened bolts before 500 W swaps.[^denis-monorim-hardware] | Prevents bent pivots and maintains steering geometry. |
| **Pivot bolts** | Swap soft hardware for grade 12.9 bolts, trim excess length, add washers/self-locking nuts, and reapply grease every ~30 hours.[^7][^28] | Stops squeaks and protects harnesses routed near the swingarm. |
| **Shocks** | Favor 150 mm units for balanced geometry; 165 mm springs require trimming headlight mounts and spacer plates to avoid binding.[^29] | Longer shocks need headlight relocation and extra hardware; match spring rates to rider weight when choosing between coil and air upgrades.[^9] |
| **Crossbar reinforcement** | Add Mirko’s avional-2024 tie bar and avoid spacer stacks/long threaded bolts to tame arm flex and wobble on tuned Monorim arms.[^30][^31] | Reinforcement plates plus higher-grade fasteners keep high-speed wobble in check. |
| **Brakes** | Use the 500 W adapter as a replacement cover, not an add-on; plan custom rear spacers and a second hydraulic brake for >50 km/h builds.[^15][^16][^17][^18] | Cheap adapters flex and warp thin rotors at speed. |
| **Steerer retention** | Replace damaged Monorim star nuts with paired bike star nuts driven in on a sacrificial bolt and fit longer stem bolts when the stack grows.[^32] | Prevents bar play after repeated rebuilds. |

## Electrical & Power Considerations

- **Avoid Monorim-branded batteries.** Listings omit cell types, arrive without brake/BMS leads, rely on lossy series diodes, and frequently ship with reversed polarity.
  - community techs recommend sourcing packs from Scootermode/VTA/EtorroS or building customs with Rita/Happy BMS instead.[^12][^13][^33][^34]
- **Treat AWD kits as incomplete.** The bundled controllers and motors underperform; veterans build dual OEM-controller setups or pair reputable Blade/Vsett hubs with reinforced wiring for real gains.[^11][^35]
- **Cable management matters.** Stress-relieve converter leads with RTV or zip ties, upgrade undersized motor connectors, and monitor hall sensors.
  - cheap 500 W hubs ship with fragile sensors that fail quickly at 48 V.[^36][^37][^38]
- **Blade/Vsett hub swaps need swingarm work.** Reverse the Monorim swingarm, cut fresh axle slots, and trim dropout edges so the security washers seat properly.
  - bent retainers or thin sliders can’t hold the 135 mm hubs at 60 V.[^39]
- **Xiaomi rear conversions need wider rotors.** Pinkflozd logged 120 mm dropout spacing and 180 mm rotors to clear Magura MT4 calipers when fitting 40 mm PaoloWu motors under Konyk or Monorim suspension kits.[^xiaomi_spacing]
- **Kuugo M4 hub conversions demand extra hardware.** Plan on 180 mm shafts, longer fasteners, and even trimming frame pockets to clear wider tires; community shared AliExpress sourcing for 500 W assemblies to simplify the swap.[^40]
- **Bulk-buy caveats:** Alibaba runs on enticing €80 offers for Monorim 500 W hubs, but 11.11 sales slow fulfillment and factory harnesses often omit the connectors bundled with retail kits.
  - budget extra parts and time when importing direct.[^41]
- **Print in PETG or ASA.** Denis and Happy’s go-to recipe.
  - ≈230 °C nozzle with 100 °C first-layer bed (≈80 °C afterward, or 231 °C/101 °C/81 °C on PEI)
  - keeps brackets from warping in hot decks.[^42]

## Ride & Maintenance Notes

- Keep pneumatic 10×3 tires at proper pressure and drill valve holes when converting from solids; true ULIP/PMT casings seat cleanly and avoid rubbing once mudguard bolts are countersunk and fenders braced.[^43][^44]
- Monorim’s front kit remains divisive—light springs or EXA/DNM air shocks help the single-pivot geometry, yet 165 mm shocks can fail early; Dereza/Konyk linkages promise better travel if they clear wide axles and brake mounts.[^denis-front-kit]
- **Use the Max hanger for 10" clearance.** The Monorim V4 fork with the CNC “Max” hanger ships with thinner mudguard brackets that buy extra room for big tires.[^denis-max-hanger]
- Add a few drops of silicone oil through EXA Schrader valves to soften small-bump response; riders settle near 40 psi (≈2.8 bar) on EXA 291s and swap between 150 lb and 650 lb springs to balance wobble control and comfort.[^denis-exa-oil]
- 10" conversions on Xiaomi frames need the bundled low-profile fender screw and spacer stack; skipping the swap leaves the tire rubbing and mimics bearing failure until the countersunk hardware is installed.[^denis-10in-spacer]
- Run tubeless PMT/Xuancheng tires without slime; if riders insist on sealant, stick to aluminum-safe formulas so bare rims don’t corrode.[^45]
- Grease pivots, cycle air shocks after storage, and mist lithium spray on small bearings to silence knocks; replace pivot pins proactively before they bend from jumps.[^28][^46]
- **Bleed the air spring with two people.** Suspend the fork, hold the valve high, add pressure through the positive valve only, and bleed the negative side after each change while misting moving parts with light lithium spray.[^denis-air-bleed]
- Expect roughly a “7/10” ride once an EXA air shock replaces the noisy stock spring, but keep up the 30-hour grease interval, cycle the shock after storage, and mist bearings with lithium spray to stop squeaks; the crew still warns against the Super kit until its weak aluminium fork issues are solved.[^denis-exa-maintenance]
- Expect iglidur bushings to flatten quickly under heavy scooters.
  - police training laps deformed them within weeks, so treat the plastic sleeves as consumables and keep bronze or nylon replacements ready for long-term durability.[^47][^48]
- Expect maintenance on brake adapters: sand mounts square, shorten bolts so XTech calipers clear, and check torque frequently because soft kit hardware loosens quickly.[^49][^50]
- Handlebar adapters can lift the folded deck slightly—rotate or shim the bell hook so the rear fender still latches after the conversion.[^handlebar_adapter]
- **Let the axle seat the fender bracket.** The Monorim fork bracket is clamped by the axle and the spacer’s set screw; overtightening the outer bolts only strips threads without stopping movement.[^denis-spacer-set]
- Remove the headlight prism and adapter when fitting 165 mm Monorim springs; the stock 150 mm coil clears without binding.[^denis-165mm]
- When rotor spacing grows beyond a few millimetres, machine a single-piece steel ring (≈5–10 mm thick) instead of stacking loose washers.
  - builders still experimenting with 1.7 mm washer stacks under Blade rotors quickly see alignment drift; confirm whether your hub uses Xiaomi’s 5-bolt or aftermarket 6-bolt pattern before cutting the spacer.[^51][^52]
- Add foam over the shallow Wildman bag screws and orient power leads upward so clamps and levers cannot puncture packs once the suspension stretches the cockpit.[^53]
- Keep electronics isolated from vibration by routing Rita/Happy harnesses along the controller side and using Monorim stem slack before clamping covers shut.[^54]
- Expect updated clamp spacers soon.
  - builders are extending the stem block so Sokil/Konyk clamps clear the fork arms while keeping the folding lock functional.[^55]
- Sandwich the deck with inner/outer steel plates when running Ulip/Konyk-length rear shocks, re-bend the frame without the battery installed, and commission softer springs rather than trimming coils so the arm stops chewing into the chassis.[^56]
- Seal every cable pass-through with silicone, grease bearings, and capture 3D-printed spacers between silicone layers while keeping threads clean so the deck stays serviceable yet waterproof.[^57]
- Set kickstand spacer height around 6.5 cm by stacking books under the stand before printing or machining the block, then swap in proper-length M6/M8 hardware (≈80 mm) instead of washer stacks so the bolts survive daily parking; factory 10-inch swingarm kits include a spacer block.
  - install it or the scooter leans dangerously.[^58][^59][^60]
- Bolt extenders plus auxiliary springs raise ride height without replacing the whole rear shock.
  - thread couplers onto the shaft so flipped forks or AliExpress swingarms sit level while the main spring stays in its working range.[^61][^62]

## Red Flags & When to Walk Away

- Skip ultra-cheap “Monorim” forks—thin sheet-metal clones crack almost immediately and jeopardize the entire front end.[^63]
- Avoid 48 V Monorim batteries until the vendor ships proper harnesses and cells; Denis labels them “pure China” with fake Panasonic specs and weak controllers.[^64]
- If hardware keeps loosening despite upgrades, inspect for missing shim stacks or bent spacer plates.
  - the fork geometry changes with 40–55 mm spacers and can punch through the deck without reinforcement plates on both sides. Add 5 mm stainless liners or repurposed upper arms as standoffs so 165–190 mm shocks never chew the deck.[^27][^65]

## Commissioning Workflow

1. **Dry-fit suspension and brake adapters** before wiring.
  - confirm clearance for pneumatics, rotor spacing, and headlight mounts so you know which spacers to fabricate.[^16][^44]
2. **Replace hardware & grease pivots** with grade 12.9 bolts, Loctite, and lithium grease; retorque after the first 20 km to catch settling play.[^7][^8]
3. **Wire power responsibly:** run Rita/Happy harnesses along the controller side, add DC/DC converters for accessories, and log early rides to verify current stays within Rita/Happy limits.[^54][^36][^66]
4. **Inspect after shakedowns**.
  - look for spacer creep, cracked adapters, loose calipers, or pack harness chafing before committing to long commutes.[^7][^49]


## References

[^1]: Source: knowledge/notes/denis_all_part02_review.md†L13-L14
[^2]: Source: knowledge/notes/denis_all_part02_review.md†L717-L717
[^3]: Source: knowledge/notes/input_part006_review.md†L17-L17
[^4]: Source: knowledge/notes/input_part006_review.md†L115-L115
[^5]: Source: data/vesc_help_group/text_slices/input_part009.txt†L5168-L5228
[^6]: Source: knowledge/notes/denis_all_part02_review.md†L22-L23
[^7]: Source: knowledge/notes/denis_all_part02_review.md†L515-L515
[^8]: Source: knowledge/notes/denis_all_part02_review.md†L1171-L1171
[^stem_play_fix]: Source: knowledge/notes/all_part01_review.md†L694-L694
[^denis-v4-shims]: Source: knowledge/notes/denis_all_part02_review.md†L810-L810
[^denis-v4-m3]: Source: knowledge/notes/denis_all_part02_review.md†L811-L811
[^denis-spares]: Source: knowledge/notes/denis_all_part02_review.md†L837-L837
[^9]: Source: data/vesc_help_group/text_slices/input_part003.txt†L23160-L23216
[^10]: Source: data/vesc_help_group/text_slices/input_part001.txt†L25245-L25272
[^11]: Source: knowledge/notes/denis_all_part02_review.md†L82-L83
[^12]: Source: knowledge/notes/denis_all_part02_review.md†L119-L120
[^13]: Source: knowledge/notes/denis_all_part02_review.md†L215-L216
[^14]: Source: knowledge/notes/denis_all_part02_review.md†L99799-L99811
[^15]: Source: knowledge/notes/denis_all_part02_review.md†L88-L89
[^16]: Source: knowledge/notes/denis_all_part02_review.md†L176-L177
[^17]: Source: knowledge/notes/denis_all_part02_review.md†L752-L752
[^18]: Source: knowledge/notes/denis_all_part02_review.md†L118611-L118621
[^19]: Source: knowledge/notes/input_part001_review.md†L562-L563
[^20]: Source: knowledge/notes/input_part006_review.md†L137-L137
[^21]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L90030-L90134
[^22]: Source: data/vesc_help_group/text_slices/input_part001.txt†L10470-L10603
[^23]: Source: data/vesc_help_group/text_slices/input_part001.txt†L11300-L11400
[^24]: Source: data/vesc_help_group/text_slices/input_part001.txt†L11338-L11395
[^grey_mast_revision]: Source: knowledge/notes/all_part01_review.md†L892-L892
[^25]: Source: knowledge/notes/input_part005_review.md†L318-L320
[^26]: Source: knowledge/notes/denis_all_part02_review.md†L25-L26
[^27]: Source: knowledge/notes/denis_all_part02_review.md†L312-L312
[^28]: Source: knowledge/notes/denis_all_part02_review.md†L718-L718
[^denis-air-bleed]: Source: knowledge/notes/denis_all_part02_review.md†L838-L838
[^29]: Source: knowledge/notes/denis_all_part02_review.md†L101732-L101749
[^30]: Source: data/vesc_help_group/text_slices/input_part003.txt†L18508-L18521
[^31]: Source: data/vesc_help_group/text_slices/input_part003.txt†L18731-L18775
[^32]: Source: knowledge/notes/denis_all_part02_review.md†L87201-L87203
[^33]: Source: knowledge/notes/denis_all_part02_review.md†L604-L604
[^34]: Source: knowledge/notes/denis_all_part02_review.md†L1245-L1245
[^35]: Source: knowledge/notes/denis_all_part02_review.md†L610-L611
[^36]: Source: knowledge/notes/denis_all_part02_review.md†L31-L32
[^37]: Source: knowledge/notes/denis_all_part02_review.md†L761-L761
[^38]: Source: knowledge/notes/denis_all_part02_review.md†L650-L650
[^front_bracket_warning]: Source: knowledge/notes/all_part01_review.md†L861-L861
[^39]: Source: data/vesc_help_group/text_slices/input_part001.txt†L7093-L7147
[^40]: Source: data/vesc_help_group/text_slices/input_part003.txt†L19446-L19510
[^41]: Source: knowledge/notes/all_part01_review.md†L171-L171
[^42]: Source: knowledge/notes/denis_all_part02_review.md†L116230-L116236
[^43]: Source: knowledge/notes/denis_all_part02_review.md†L109-L111
[^44]: Source: knowledge/notes/denis_all_part02_review.md†L274-L274
[^denis-max-hanger]: Source: knowledge/notes/denis_all_part02_review.md†L835-L835
[^denis-machining]: Source: knowledge/notes/denis_all_part02_review.md†L1002-L1002
[^denis-front-kit]: Source: knowledge/notes/denis_all_part02_review.md†L1033-L1033
[^denis-exa-oil]: Source: knowledge/notes/denis_all_part02_review.md†L1095-L1095
[^denis-10in-spacer]: Source: knowledge/notes/denis_all_part02_review.md†L1096-L1096
[^45]: Source: knowledge/notes/denis_all_part02_review.md†L140-L143
[^46]: Source: knowledge/notes/denis_all_part02_review.md†L1293-L1294
[^47]: Source: knowledge/notes/input_part004_review.md†L186-L187
[^48]: Source: data/vesc_help_group/text_slices/input_part004.txt†L7513-L7527
[^49]: Source: knowledge/notes/denis_all_part02_review.md†L611-L611
[^denis-spacer-set]: Source: knowledge/notes/denis_all_part02_review.md†L845-L845
[^denis-mxr1-v2]: Source: knowledge/notes/denis_all_part02_review.md†L937-L937
[^denis-monorim-hardware]: Source: knowledge/notes/denis_all_part02_review.md†L938-L938
[^50]: Source: knowledge/notes/denis_all_part02_review.md†L1001-L1001
[^51]: Source: data/vesc_help_group/text_slices/input_part000.txt†L22903-L22942
[^52]: Source: data/vesc_help_group/text_slices/input_part000.txt†L23098-L23100
[^53]: Source: knowledge/notes/all_part01_review.md†L274-L276
[^54]: Source: knowledge/notes/denis_all_part02_review.md†L966-L966
[^55]: Source: knowledge/notes/input_part006_review.md†L98-L98
[^handlebar_adapter]: Source: knowledge/notes/all_part01_review.md†L695-L695
[^56]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L90030-L90136
[^57]: Source: knowledge/notes/denis_all_part02_review.md†L553-L553
[^58]: Source: knowledge/notes/denis_all_part02_review.md†L440-L441
[^59]: Source: knowledge/notes/denis_all_part02_review.md†L441-L441
[^60]: Source: knowledge/notes/denis_all_part02_review.md†L99684-L99689
[^61]: Source: knowledge/notes/denis_all_part02_review.md†L434-L434
[^62]: Source: knowledge/notes/denis_all_part02_review.md†L468-L468
[^denis-exa-maintenance]: Source: knowledge/notes/denis_all_part02_review.md†L717-L718
[^63]: Source: knowledge/notes/denis_all_part02_review.md†L1366-L1366
[^denis-165mm]: Source: knowledge/notes/denis_all_part02_review.md†L682-L682
[^64]: Source: knowledge/notes/denis_all_part02_review.md†L1290-L1291
[^65]: Source: knowledge/notes/denis_all_part02_review.md†L87046-L87066
[^66]: Source: knowledge/notes/denis_all_part02_review.md†L618-L618
[^monorim_axle]: Source: knowledge/notes/input_part003_review.md†L536-L537
[^monorim_bracket]: Source: knowledge/notes/input_part003_review.md†L537-L538
[^xiaomi_spacing]: Source: knowledge/notes/input_part003_review.md†L563-L563
