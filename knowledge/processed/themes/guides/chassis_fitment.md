# Chassis Fitment and Maintenance

## Overview

Proper chassis fitment and maintenance are critical for scooter safety, performance, and longevity. This guide covers bearing selection and replacement, wheel/tire fitment, frame stiffness considerations, and front-end stability upgrades. Understanding these mechanical fundamentals helps prevent failures and ensures reliable operation, especially on high-power builds where stress on components increases significantly.

## What You'll Learn

- Bearing selection criteria (seal types, clearances, sizing)
- Wheel and tire fitment considerations and clearances
- Frame stiffness evaluation and when reinforcement is needed
- Front-end geometry and stability at different speed ranges
- Proper bearing installation and maintenance procedures
- When to upgrade from stock to aftermarket components
- Quality markers for replacement parts

## 🔧 Critical Fitment Principles

⚠️ **Measure twice, order once**: Wrong bearing sizes or axle diameters mean expensive returns.

## 📋 Quick Reference: Common Bearing Sizes

| Application | Bearing Size | Inner Diameter | Outer Diameter | Width |
|-------------|-------------|----------------|----------------|-------|
| Front wheel hub | 6001 | 12mm | 28mm | 8mm |
| Rear wheel hub | 6202 | 15mm | 35mm | 11mm |
| Steering column | 6900 series | Varies | Varies | Varies |
| Suspension pivot | 608 | 8mm | 22mm | 7mm |

💡 **Pro Tip**: Buy sealed (2RS) bearings, not open or shielded. They last 3-5x longer in outdoor conditions.

## 📋 Wheel Compatibility Chart

| Rim Size | Compatible Motors | Tire Options | Best For |
|----------|------------------|--------------|----------|
| 8-inch | 40-50H motors | Limited selection | Compact commuters |
| 10-inch | 60-70H motors | Good selection (PMT, CST) | Most builds |
| 11-inch | 70-80H motors | Excellent selection | Performance builds |
| 12-inch | 90H+ motors | Limited, heavy-duty | Race/extreme builds |

## ⚠️ Common Fitment Mistakes

🔴 **Axle too short** - Motor won't seat properly, caliper won't align
🔴 **Dropout width mismatch** - Motor won't fit without frame mods
🔴 **Brake rotor size** - Caliper may not reach larger rotors
🔴 **Tire width** - Wide tires may rub fenders or deck

## 🔧 Related Guides

- [Brake Maintenance & Upgrades](brake-maintenance-and-upgrades.md) - Caliper and rotor fitment
- [Motor Configuration](motor_configuration.md) - Selecting motor size
- [Xiaomi Tire & Brake Upgrades](xiaomi_tire_brake_upgrade_notes.md) - Platform-specific fitment

## Bearing and Wheel Upgrades

- Monorim 500 W hub motors accept 6001 rear bearings and 16003 stainless fronts when refreshing the rolling hardware, supporting wider tire conversions.[^bearing_sizes]
- EU suppliers now list 33×2 60 H hubs with 125 mm dropouts and 4 mm banana phases for roughly €300 shipped, giving builders a compact dual-drive option without custom axles.[^eu_33x2_hub]
- Xiaomi frames can host 2.5–3.0 inch tires, but builders watch for clearance limits to avoid rubbing after the wider fitment.[^tire_clearance]
- Scooter bearing techs warn against cracking open sealed hubs or stuffing them with 70 % grease fills; standard-clearance cartridges already tolerate thermal expansion, so riders stick with OEM-style fills instead of chasing C3 replacements that only add drag.[^sealed_bearing_fill]
- LY will ship 11‑inch wheels on 130 mm axles, yet riders still stack spacers and washers carefully when slotting 70–75 H Lonnyo stators into minibike frames to preserve dropout alignment and keep brake rotors centred.[^ly-11in-fit]
- Blade split rims that refuse to separate often need the cover holes chased or the 110–112 mm axle stack reset with fresh 12 mm washers/nuts before committing to a full motor tear-down.[^blade_split]
- Stuck hub bearings warrant a proper puller; cutting shoulders risks permanent axle damage when rusted races won’t slide off by hand.[^bearing_puller]
- High-speed hub refreshes now favor 2RS seals as the balance between drag and protection, keep ZZ for minimal resistance, and skip RSH unless you accept extra drag—Vsett bearings cooked after ~17 000 km without timely swaps.[^bearing_seals]
- Updated Vsett 10+ service lists now call for SKF 6202/6004 2RSH wheel bearings, 20 × 28 × 6 and 15 × 25 × 5 simmering seals, 16287 2RS swingarm bearings, and 30 × 41 × 6.5 36°×45° headset bearings to replace the rust-prone stock hardware.[^vsett10_bearings]
- SKF clarified that C3-clearance 2Z bearings leave extra race spacing for thermal growth, making them suitable for racing hubs despite the limited sealing compared with 2RS options.[^c3_clearance]
- Oversize 10×2.5 in CST casings on 155 mm rims usually need 2–2.5 mm of machining for a safe bead seat—take material from the rim, not the tire, to avoid hidden cuts that explode at speed.[^denis-cst-machining]

## Frame Stiffness Checks

- Removing the deck from a Dualtron Spider leaves the frame too flexy to stand on; riders are adding reinforcement and planning higher-power motor swaps only after hall wiring and 10 AWG phase leads are sorted to keep the chassis stable.[^dualtron_spider]
- Zero 10X stems, frames, and OEM suspension pieces have cracked when riders push past ~60 km/h; NetworkDir nudges builders toward Vsett 10+ chassis with dual stems when planning high-power conversions.[^zero10x_fail]
- Zero 10X conversions that jump to 11-inch wheels also need upgraded brake kits for rotor clearance before the new wheelset is rideable.[^zero10x_11in]
- Slack Core 920R frames have snapped before upgrade work even began; inspect boutique chassis for hidden damage before pouring money into power mods.[^slack_core_fail]
- Dualtron race builds still require heavy frame, fork, and motor rework despite the platform’s popularity, because Minimotors outsources much of the hardware.[^dualtron_outsource]
- Raising the rear ride height without a quality damper has triggered wobble on Dualtrons; balanced geometry can still reach 150 km/h damper-free, but the Spanish crew noted stricter policing as another reason to keep setups stable and discreet.[^dualtron-geometry]

## Front-End Stability Upgrades

- JREV Speedfork assemblies have earned rider trust up to ~70 km/h, while the crew flatly rejects pushing Xiaomi/Ninebot stock steering to those speeds—budget commuters need fork and headset upgrades before high-speed tuning.[^speedfork]
- Slack Core prototypes may need reinforcement: the forged-aluminium neck geometry wins praise, but builders plan to beef up the thin lower joint before putting 100 kg riders on production frames.[^slack_core]

## Hardware Compatibility & Troubleshooting

- Blade 10/11 axles show up in both M12×1.25 and M14×1.5 threads depending on the batch; lock the hinge solid on donor frames and inventory hardware before chasing replacements.[^blade_threads]
- Retail techs note that Achilleus frames sit larger than Thunder chassis yet still wobble unless the hinge is overtightened, and Speedtrott’s smaller 40 mm motors remain the weak link even when the hinge survives.[^achilleus_feedback]
- A 203 mm rotor adapter that sits high usually means the axle isn’t fully seated; custom torque arms that sit flush on the dropout solved repeat pop-outs once the frame was tilted.[^torque_arm_flush]
- Monorim AWD conversions require flipping the suspension sides or spacing/bending the arms to clear Blade 10" hubs, plus at least 6 P of 50E/50G-class cells (or stronger) per wheel so 40 A battery feeds don’t cook marginal packs.[^monorim_swap]

## High-Power Motor Fitment

- Builders stepping up to 72 V 1,000–1,500 W swaps lean on PaoloWu’s 1.2 kW hub motors with larger magnet stacks to cut copper loss and boost torque versus stock cans.[^paolo72v]
- Mirono reminds newcomers those wide motors usually need inverted Monorim forks or a rear-drive conversion to clear 10" rubber, so plan fork and chassis work alongside the motor purchase.[^mirono-fork]
- Dropping a 1 000 W hub into a Xiaomi deck means flipping the Monorim fork so the larger rim and six-bolt rotor clear the chassis; the stock fork orientation simply lacks space.[^denis-1000w-fit]
- Ninebot Max frames swallow 1 000 W hubs (with or without suspension) thanks to wider dropouts, while Xiaomi rears still lack clearance even with Monorim shocks—front installs remain the practical Xiaomi option.[^denis-1000w-max]

## Deck Fabrication & Accessories

- Builders experimenting with transparent deck plates pair 6 mm acrylic lids with foam bedding or CNC 12 mm plexiglass spacers to hide LED strips; plan for eventual cracking and reinforce mounts before sealing the deck.[^1]
- Face de Pin Sucé’s carbon extension for Dualtron Victor/Luxury/Compact adds ~605 mm of mounting length (≈434 mm usable with a Ubox) and fits a 21 S 6–7 P pack plus an 85 V 240 A controller, giving Spanish builders a bolt-on path to longer batteries without welding.[^dualtron-extension]
- Rental G30 frames accept printed battery extenders, but high BMS harnesses can foul vertical cells.
  - rewire harness exits or add 2 mm spacers so deck lids close without pinching leads.[^2]
- Vsett headlight retrofits need stiffer stem brackets to keep elevated lamps from shaking and to shorten the dark “dead zone”; CAD the mount before drilling to preserve the OEM look.[^3]
- Francois splits his 13 S8 P pack between the deck and an external half because the Xiaomi frame can’t swallow the whole module; he bolts dual VESCs to the deck as a heatsink and warns that bag-mounted controllers sacrifice cooling and theft resistance.[^denis-francois]
- Ninebot rental chassis hide factory silicone seams, lockable battery latches, and swappable pack harnesses.
  - making them attractive donors for high-power conversions once you add disc-compatible brake mounts.[^4]
- Riders comparing Ninebot Max G2 and G30 frames noted the G2’s suspension improves vibration longevity, while SNSC rental frames shrugged off ~80 km/h guardrail hits with only peripheral damage; the same thread shared DNM shock fitment tips, 13"×7" tire swaps, and a lever-free hub tire removal method to avoid scratching rims.[^sns_c_service]
- Boosted Rev decks only swallow roughly 60×21700 cells (≈12 S5 P) plus an underslung controller, so builders often pair charge-only BMS + fuse strategies when ANT smart boards exceed the 100 mm × 40 mm envelope.[^5]
- Ninebot G30 rental frames remain coveted donor chassis thanks to non-folding stems, dual brakes, oil suspension, thicker tubing, and ~10 kg of extra steel that swallows 13 S 5 P 21700 packs and 1.2 kW hubs without flexing like stock Xiaomi frames—but budget time for drilling, longer hardware, and pricey OEM parts when you swap motors or poles.[^6][^denis-rental-weight]
- Portable AWD Xiaomi builds creep toward 29 kg once dual batteries, locks, and beefy motors are installed—many riders settle on stout rear-wheel-drive G30 conversions instead of lugging dual-motor frames upstairs.[^denis-awd-weight]
- G30 Max decks are still wider than Xiaomi Pro trays, so cross-platform motor or deck swaps need custom spacer stacks even when the housings look identical.[^denis-g30-width-fit]
- Community salvage runs keep surfacing Dualtron, Etwow, and Xiaomi donor parts.
  - complete with 60 V packs and heavy-duty motors
  - illustrating how friendships and group buys keep premium frames affordable.[^7]
- SNSC 2.3 rental frames are drying up as fleets pivot to Okai hardware, so builders now scout Brussels, Düsseldorf, and other
operator auctions to stockpile Ninebot donor chassis before the supply disappears.[^sns_supply]

## Zero 10X and Thunder Fitment Updates

- Some regions still deliver the Zero 10X with a dummy front hub; upgrading to dual drive means importing a live motor (often from FalconPEV), rewiring Zero/Mantis harness mixes, and watching frame integrity once speeds climb past ~100 km/h.[^zero_dummy_hub]
- Paolo’s measurements show 11-inch hubs need ≈145 mm fork spacing and a longer axle on the Zero 10X, while the stock 125 mm dropouts cap builds around 65 H 10-inch motors unless you extend the swingarm or buy a conversion kit.[^zero_11inch]
- Face de Pin’s clamp that ties both steering-nut lockrings to the stem has become the go-to insurance mod against Thunder hinge failures, and the same crew is packaging 22 S 8 P C350 controllers inside proprietary cases to keep rain out during race duty.[^thunder_clamp]
- High-power Zero builds in France are stuffing ~22 S 11 P packs inside bespoke frames (“French style”) while relocating controllers externally; the tradeoff is custom fabrication cost for every donor chassis.[^zero_custom_packaging]
- Lengthened frames can still squeeze 24 S stacks without deck spacers, but Andrei notes the stretched wheelbase complicates transport through elevators and tight hallways.[^extended_frames]
- The current fork project clears 70 H motors yet likely refuses thicker 75 H stators, so confirm measurements before ordering oversized hubs.[^fork_clearance]
## Tire Clearance & Suspension Packaging

- Jumbo tires can clear swingarms with about 4″ per side, but slicks get unforgiving on wet pavement—rain wheels need conservative throttle maps or treaded rubber to stay upright.[^jumbo-clearance]
- Rob Ver’s Vsett 11 stretches 80 mm rubber over 100 mm rims, drops the suspension, and favours 130/40 PMTs to keep tyre and controller temps near 40 °C during hard street riding.[^rob-vsett-packaging]
- High-travel (≈150 mm) suspensions pushed Ausias to move controllers up into the chassis and rely on model-specific O-rings to seal tubeless split rims; under-deck mounts were scraping at full compression.[^ausias-travel]
- Ambrosini/LY CNC rims still hover around €100–€120 each, expect 155 mm axles for 6.5″ fitments, and ship with hefty AWG 7–8 phase sleeves in the harness.[^ly-rims]

## Legal Compliance & Model Selection

- Spain’s 2027 homologation wave keeps Thunder 3 scooters road-legal while sidelining many Nami models; enforcement remains spotty, but the 25 km/h cap still applies on public roads.[^spain-homologation]
- Achilleus Limited editions hover around €3,200 versus roughly €4,300 for a homologated Thunder 3, making Achilleus a roomy, VESC-ready base with Thunder arms and 11″ tyre support.[^achilleus-pricing]
- Victor Luxury + owners log about 20 S 8 P capacity once controllers move outside the deck, whereas Achilleus builders can machine an aluminium neck box to hide VESC hardware for stealth and legality.[^victor-capacity][^achilleus-neck]
- Anything above ~4 kW still falls under motorcycle registration rules in many EU locales even if day-to-day enforcement is lax, so keep paperwork in mind before chasing headline power figures.[^eu-motorcycle]
- Yamal notes how quickly dual VESC builds, premium cells, brakes, and backup scooters inflate project budgets—plan for a spare vehicle while the main chassis is torn down.[^project-costs]
- Mock up any 20 S 12 P Ninebot G30 pack in cardboard first; fitting more than ~120 cells demands stacked modules, tall spacers, remote ESCs, and acceptance of 65–70 kg curb weights plus suspension geometry shifts.[^g30_20s12p_mockup]

## Platform-Specific Fitment Notes

- NetworkDir’s Zero 10X 50H hub shares the 16×4 shell used on some Vsett swaps, and his failure traced back to a ripped phase/hall harness—add strain relief before pushing higher current motors in those decks.[^networkdir_harness]
- Vsett 10+ owners chasing Spintend swaps cite Bluetooth telemetry, speed-limit removal, and auxiliary 3 S packs as key wins but still want documentation for reusing stock lighting and accessory ports before committing.[^vsett_spintend]
- Apo’s hunt for Vsett 10+ harness pinouts and alternative Ubox sellers underscores the need for accurate diagrams and sourcing references when converting rental frames.[^vsett_pinout]
- Segway Ninebot SNSC 2.0 frames handle 200 kg loads and add only ~1.3 kg over a G30, but U.S. builders still rely on auctions or fleet sell-offs to source them.[^snsc_availability]
- Zero 10X belly measurements land around 123 × 32 × 50 cm once stock gear is removed, giving builders a sanity check before speccing 38 cm packs and dual-controller layouts.[^zero10x_belly_volume]

## Tire & Wheel Fitment Debates

- Zero/Vsett owners keep steering riders toward CST 10×3 or PMT 10×3.5 rubber, warning that Xuancheng slicks feel soft and short-lived above 4 kW without traction control, and that 10" rims look undersized paired with 165 mm rotors.[^zero_vsett_tires]
- Fork swaps to 145 mm travel assemblies only slightly improve Zero 10X trail figures, so builders still rely on dampers and ~60 % rear phase bias to calm wobble during launches.[^zero_fork_trail]
- Recent feedback praises Tuovt 90/55-6 tires for surviving broken pavement far longer than PMT slicks, which grip harder but shred quickly on rough commutes.[^tuovt_feedback]
- Track riders rate Xuancheng slicks for circuit grip yet call them too fragile for street abuse, preferring CST-patterned 11" tires day-to-day and warning that 3.5" rubber looks tractor-wide on Zero/Vsett rims unless pressure and rim width are tuned carefully.[^xuancheng_race][^zero_vsett_3p5_width]

## Geometry & Stability Notes

- Vsett 10+ and other C-fork scooters remain unstable above roughly 80 km/h; riders linked fatal wobbles to poor trail and still recommend better geometry or dampers before chasing triple-digit speeds.[^c_fork_instability]
- PuneDir and others shared tank-slapper incidents (e.g., 78 km/h on a Zero) to emphasize how quickly oscillations escalate, especially with lighter riders or mediocre tires.[^tank_slapper_logs]
- Traction control set around an 80 000 ERPM differential preserves CST 10×3 tires, whereas disabling TC shredded them within days.[^tc_tire_preservation]
- Kirill countered the doom posts by listing inherently stable production scooters (Segway GT1/GT2, ST1/ST2, Inmotion RS, large Wepeds, Monorim-modded G30s, NAMI Blast), underscoring that C-fork wobble is model-dependent.[^stable_platforms]
- Zero 10X racers logging 10 kW tunes even ran traction control off for tire noise yet capped real-world speed near 60 km/h to preserve stability on twin-stem frames.[^zero10x_tc_off]
- Zero 10X suspension tuning now centres on 165 mm/1,500 lb rear springs and 135–150 mm/1,500 lb fronts, with ~70 kg riders still favouring stiff rates for asphalt while heavier racers rotate 1,250–1,800 lb coils by terrain.[^zero10x_spring_rates]
- Tighten wobbly Zero/Vsett folding clamps with a rag and channel locks; once torqued properly the joint rarely folds tool-free, but it stops stem play before rotors groove the pads.[^folding_clamp_fix]

## High-Power Suspension & Frame Upgrades

- The Weepor’s rear suspension bottoms out under heavier riders; budget an EXA 150 mm shock or similar-quality damper before unlocking more power.[^weepor_shock]
- Thunder-frame builders are mapping 22 S11 P battery bays (with BMS) or 22 S10 P layouts using next-gen 40PL cells to balance weight and capacity.[^thunder_pack]
- Scarcity and steep local pricing are pushing some builders away from Thunder frames entirely, opting for heavier Nami or Teverun Blade platforms despite the weight hit.[^thunder_scarcity]
- Raphael Foujiguara Performance now offers reinforced decks, welded battery boxes, and mudguards tailored to 20 S-class scooters with Thunder-style necks—handy when OEM frames skip critical accessories.[^rfp_accessories]

## Suspension & Fork Notes

- Kaabo storm-style frames diverge: the GTR carries a 135 mm shock while cheaper variants rely on twin 40 mm springs stacked with bushings, echoing “pogo” complaints about block-sprung forks and guiding upgrade planning.[^kaabo-suspension]

## Custom Dropouts & Frame Surgery

- Deep sleeper builds can demand literal chassis surgery: GABE’s stretched frame now pulls the hub forward ~15 cm, machines legacy fork dropouts for disc clearance, adds steel reinforcement beams, and repackages the battery as a 22 S 6 P stack to maintain geometry.[^dropout_mods]

## Tyre Selection & Pricing

- PMT shoppers report €53–58 Stradale pricing in Italy versus €48 plus €19 shipping from Fastride, and Paolo nudges commuters toward the slightly softer Junior compound for grip without major range penalties.[^pmt_pricing]

## Xiaomi / Pro Tire & Cockpit Mods

- Removing a Xiaomi rear side plate lets the hub and stock tire slide off together; match inner diameter and width carefully before trimming metal for 10 inch solid conversions.[^xiaomi_sideplate]
- Fitting Deli 10×2 inch rubber on 1S/Pro 2 frames means relocating or trimming the rear-light connector, extending wiring, and resealing the exit with glue or grommets so the carcass clears the housing.[^deli_install]
- Mountain-bike cockpit swaps need an oval-to-round stem adapter, and relocating the BLE/dashboard harness is part of the job when upgrading to stiffer bars.[^mtb_stem]
- Later-production Xiaomi frames arrive packed with foam that must be excavated before routing new cabling or swapping motors—budget time for the cleanup.[^foam_cleanup]
- CST 10×2.25 tires cut for 152 mm rims refuse to seat on the Xiaomi 155 mm wheel and can foul the frame, so resell them or swap to scooter-specific casings instead of forcing the fit.[^cst_mismatch]
- Riders have squeezed CST 10×2.5 inch tires onto Pro/1S frames without deck spacers, but centering the carcass is tedious and benefits from suspension travel to clear the added width.[^cst_10x25]
- Ninebot G30 hub swaps into Xiaomi frames mean mixing two Monorim kits, machining spacers, lengthening motor leads, and slightly opening the controller plug before the axle seats reliably.[^g30_swap_fitment_chassis]
- Converting Xiaomi rear dropouts to driven hubs means drilling the axle slot, fitting adapter plates, and committing with threadlocked hardware—the change is effectively irreversible once the opening is enlarged.[^denis-rear-drive]

[^bearing_sizes]: Source: knowledge/notes/input_part000_review.md, line 74.
[^tire_clearance]: Source: knowledge/notes/input_part000_review.md, line 74.
[^sealed_bearing_fill]: Source: knowledge/notes/input_part006_review.md†L450-L451
[^dualtron_spider]: Source: knowledge/notes/input_part000_review.md, line 187.
[^zero_dummy_hub]: Source: knowledge/notes/input_part009_review.md†L406-L406.
[^zero_11inch]: Source: knowledge/notes/input_part009_review.md†L407-L407.
[^thunder_clamp]: Source: knowledge/notes/input_part009_review.md†L408-L409.
[^zero_custom_packaging]: Source: knowledge/notes/input_part009_review.md†L427-L427.
[^extended_frames]: Source: knowledge/notes/input_part009_review.md†L429-L429.
[^fork_clearance]: Source: knowledge/notes/input_part009_review.md†L432-L432.
[^jumbo-clearance]: Source: knowledge/notes/input_part012_review.md, line 423.
[^rob-vsett-packaging]: Source: knowledge/notes/input_part012_review.md, lines 424 and 481.
[^ausias-travel]: Source: knowledge/notes/input_part012_review.md, lines 425 and 477.
[^ly-rims]: Source: knowledge/notes/input_part012_review.md, line 426.
[^spain-homologation]: Source: knowledge/notes/input_part012_review.md, line 452.
[^achilleus-pricing]: Source: knowledge/notes/input_part012_review.md, line 453.
[^victor-capacity]: Source: knowledge/notes/input_part012_review.md, line 454.
[^achilleus-neck]: Source: knowledge/notes/input_part012_review.md, line 478.
[^eu-motorcycle]: Source: knowledge/notes/input_part012_review.md, line 455.
[^project-costs]: Source: knowledge/notes/input_part012_review.md, line 456.
[^zero10x_fail]: Source: knowledge/notes/input_part010_review.md†L407-L408
[^zero10x_11in]: Source: knowledge/notes/input_part010_review.md†L618-L618
[^slack_core_fail]: Source: knowledge/notes/input_part010_review.md†L618-L619
[^dualtron_outsource]: Source: knowledge/notes/input_part010_review.md†L621-L621
[^weepor_shock]: Source: knowledge/notes/input_part010_review.md†L458-L459
[^thunder_pack]: Source: knowledge/notes/input_part010_review.md†L505-L506
[^thunder_scarcity]: Source: knowledge/notes/input_part010_review.md†L687-L687
[^rfp_accessories]: Source: knowledge/notes/input_part010_review.md†L514-L515
[^ly-11in-fit]: Source: knowledge/notes/input_part013_review.md†L729-L729
[^dualtron-extension]: Source: knowledge/notes/input_part013_review.md†L730-L730
[^dualtron-geometry]: Source: knowledge/notes/input_part013_review.md†L857-L857
[^kaabo-suspension]: Source: knowledge/notes/input_part013_review.md†L826-L826
[^eu_33x2_hub]: Source: data/vesc_help_group/text_slices/input_part011.txt, L21207 to L21208
[^dualtron_spider]: Source: knowledge/notes/input_part000_review.md, line 187.
[^speedfork]: Source: knowledge/notes/input_part011_review.md†L616-L617.
[^blade_split]: Source: knowledge/notes/input_part002_review.md†L623-L624
[^bearing_puller]: Source: knowledge/notes/input_part002_review.md†L664-L665
[^bearing_seals]: Source: knowledge/notes/input_part002_review.md†L18111-L18234
[^slack_core]: Source: knowledge/notes/input_part002_review.md†L685-L686
[^blade_threads]: Source: knowledge/notes/input_part002_review.md†L651-L652
[^achilleus_feedback]: Source: knowledge/notes/input_part002_review.md†L652-L653
[^torque_arm_flush]: Source: knowledge/notes/input_part002_review.md†L678-L679
[^monorim_swap]: Source: knowledge/notes/input_part002_review.md†L688-L690
[^c3_clearance]: Source: knowledge/notes/input_part002_review.md†L19835-L19839
[^vsett10_bearings]: Source: data/vesc_help_group/text_slices/input_part002.txt†L20580-L20591
[^paolo72v]: Source: knowledge/notes/denis_all_part02_review.md†L524-L524
[^mirono-fork]: Source: knowledge/notes/denis_all_part02_review.md†L525-L525
[^denis-1000w-fit]: Source: knowledge/notes/denis_all_part02_review.md†L819-L819
[^denis-1000w-max]: Source: knowledge/notes/denis_all_part02_review.md†L927-L927
[^denis-cst-machining]: Source: knowledge/notes/denis_all_part02_review.md†L963-L963
[^denis-francois]: Source: knowledge/notes/denis_all_part02_review.md†L656-L657


## References

[^1]: Source: knowledge/notes/input_part000_review.md†L323-L323
[^2]: Source: knowledge/notes/input_part000_review.md†L376-L376
[^3]: Source: knowledge/notes/input_part000_review.md†L374-L374
[^4]: Source: knowledge/notes/input_part000_review.md†L515-L516
[^5]: Source: knowledge/notes/input_part000_review.md†L517-L517
[^6]: Source: knowledge/notes/input_part000_review.md†L706-L710
[^7]: Source: knowledge/notes/input_part000_review.md†L710-L714
[^sns_supply]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24537-L24551
[^sns_c_service]: Source: knowledge/notes/input_part008_review.md†L316-L316
[^networkdir_harness]: Source: knowledge/notes/input_part008_review.md†L343-L343
[^vsett_spintend]: Source: knowledge/notes/input_part008_review.md†L344-L344
[^vsett_pinout]: Source: knowledge/notes/input_part008_review.md†L345-L345
[^zero_vsett_tires]: Source: knowledge/notes/input_part008_review.md†L348-L348
[^zero_fork_trail]: Source: knowledge/notes/input_part008_review.md†L349-L349
[^tuovt_feedback]: Source: knowledge/notes/input_part008_review.md†L350-L350
[^g30_20s12p_mockup]: Source: knowledge/notes/input_part008_review.md†L402-L403
[^xuancheng_race]: Source: knowledge/notes/input_part008_review.md†L405-L406
[^zero_vsett_3p5_width]: Source: knowledge/notes/input_part008_review.md†L407-L407
[^c_fork_instability]: Source: knowledge/notes/input_part008_review.md†L366-L366
[^tank_slapper_logs]: Source: knowledge/notes/input_part008_review.md†L367-L367
[^tc_tire_preservation]: Source: knowledge/notes/input_part008_review.md†L368-L368
[^stable_platforms]: Source: knowledge/notes/input_part008_review.md†L369-L369
[^zero10x_tc_off]: Source: knowledge/notes/input_part008_review.md†L315-L315
[^snsc_availability]: Source: knowledge/notes/input_part008_review.md†L437-L438
[^zero10x_belly_volume]: Source: knowledge/notes/input_part008_review.md†L468-L468
[^zero10x_spring_rates]: Source: knowledge/notes/input_part008_review.md†L443-L444
[^folding_clamp_fix]: Source: knowledge/notes/input_part008_review.md†L457-L458
[^dropout_mods]: Source: data/vesc_help_group/text_slices/input_part011.txt, L20800 to L20825; L21193 to L21206; L21355 to L21367
[^pmt_pricing]: Source: knowledge/notes/input_part002_review.md†L19775-L19804
[^xiaomi_sideplate]: Source: knowledge/notes/all_part01_review.md†L504-L504
[^deli_install]: Source: knowledge/notes/all_part01_review.md†L505-L505
[^mtb_stem]: Source: knowledge/notes/all_part01_review.md†L506-L506
[^foam_cleanup]: Source: knowledge/notes/all_part01_review.md†L507-L507
[^cst_mismatch]: Source: knowledge/notes/all_part01_review.md†L554-L554
[^cst_10x25]: Source: knowledge/notes/all_part01_review.md†L556-L556
[^g30_swap_fitment_chassis]: Source: knowledge/notes/all_part01_review.md†L891-L891
[^denis-rental-weight]: Source: knowledge/notes/denis_all_part02_review.md†L750-L750
[^denis-awd-weight]: Source: knowledge/notes/denis_all_part02_review.md†L1034-L1034
[^denis-g30-width-fit]: Source: knowledge/notes/denis_all_part02_review.md†L820-L820
[^denis-rear-drive]: Source: knowledge/notes/denis_all_part02_review.md†L751-L751
