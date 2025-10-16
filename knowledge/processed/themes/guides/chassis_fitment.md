# Chassis Fitment and Maintenance

## Bearing and Wheel Upgrades

- Monorim 500 W hub motors accept 6001 rear bearings and 16003 stainless fronts when refreshing the rolling hardware, supporting wider tire conversions.[^bearing_sizes]
- Xiaomi frames can host 2.5–3.0 inch tires, but builders watch for clearance limits to avoid rubbing after the wider fitment.[^tire_clearance]

## Frame Stiffness Checks

- Removing the deck from a Dualtron Spider leaves the frame too flexy to stand on; riders are adding reinforcement and planning higher-power motor swaps only after hall wiring and 10 AWG phase leads are sorted to keep the chassis stable.[^dualtron_spider]

## Deck Fabrication & Accessories

- Builders experimenting with transparent deck plates pair 6 mm acrylic lids with foam bedding or CNC 12 mm plexiglass spacers to hide LED strips; plan for eventual cracking and reinforce mounts before sealing the deck.[^1]
- Rental G30 frames accept printed battery extenders, but high BMS harnesses can foul vertical cells.
  - rewire harness exits or add 2 mm spacers so deck lids close without pinching leads.[^2]
- Vsett headlight retrofits need stiffer stem brackets to keep elevated lamps from shaking and to shorten the dark “dead zone”; CAD the mount before drilling to preserve the OEM look.[^3]
- Ninebot rental chassis hide factory silicone seams, lockable battery latches, and swappable pack harnesses.
  - making them attractive donors for high-power conversions once you add disc-compatible brake mounts.[^4]
- Riders comparing Ninebot Max G2 and G30 frames noted the G2’s suspension improves vibration longevity, while SNSC rental frames shrugged off ~80 km/h guardrail hits with only peripheral damage; the same thread shared DNM shock fitment tips, 13"×7" tire swaps, and a lever-free hub tire removal method to avoid scratching rims.[^sns_c_service]
- Boosted Rev decks only swallow roughly 60×21700 cells (≈12 S5 P) plus an underslung controller, so builders often pair charge-only BMS + fuse strategies when ANT smart boards exceed the 100 mm × 40 mm envelope.[^5]
- Ninebot G30 rental frames remain coveted donor chassis thanks to non-folding stems, dual brakes, oil suspension, thicker tubing, and ~10 kg of extra steel that swallows 13 S 5 P 21700 packs and 1.2 kW hubs without flexing like stock Xiaomi frames.[^6]
- Community salvage runs keep surfacing Dualtron, Etwow, and Xiaomi donor parts.
  - complete with 60 V packs and heavy-duty motors
  - illustrating how friendships and group buys keep premium frames affordable.[^7]
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

[^bearing_sizes]: Source: knowledge/notes/input_part000_review.md, line 74.
[^tire_clearance]: Source: knowledge/notes/input_part000_review.md, line 74.
[^dualtron_spider]: Source: knowledge/notes/input_part000_review.md, line 187.


## References

[^1]: Source: knowledge/notes/input_part000_review.md†L323-L323
[^2]: Source: knowledge/notes/input_part000_review.md†L376-L376
[^3]: Source: knowledge/notes/input_part000_review.md†L374-L374
[^4]: Source: knowledge/notes/input_part000_review.md†L515-L516
[^5]: Source: knowledge/notes/input_part000_review.md†L517-L517
[^6]: Source: knowledge/notes/input_part000_review.md†L706-L710
[^7]: Source: knowledge/notes/input_part000_review.md†L710-L714
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
