# Xiaomi Tire, Brake & Handling Upgrade Notes

## Tire Selection & Pressures
- **10" pneumatic upgrades:** CST 10×2.25, Wanda 10×2, and Xuancheng casings deliver the best grip once inflated toward 3.5–4.2 bar; running them near 36 psi dulls the expected 12 S speed gains and risks fender rub until clearances are checked.【F:knowledge/notes/all_part01_review.md†L226-L228】【F:knowledge/notes/all_part01_review.md†L369-L370】【F:knowledge/notes/all_part01_review.md†L696-L696】
- **Solid vs. pneumatic:** Riders report roughly 20 % higher energy use, harsher ride quality, and accelerated fatigue on battery tabs when solid tires replace pneumatics—reserve solids for short-range emergency duty.【F:knowledge/notes/all_part01_review.md†L336-L337】
- **Valve and rim prep:** Monorim 500 W hubs ship without valve holes; drill carefully and add angled stems before installing tubes. Sand thick CST beads or rim casting bumps so 10" conversions seat evenly and avoid wobble.【F:knowledge/notes/all_part01_review.md†L337-L338】【F:knowledge/notes/all_part01_review.md†L696-L696】
- **Match tire to rim width:** Stretching 6"-wide casings over 6.1" rims left beads off-center, valves fouled, and fenders rubbing; source true 155 mm tires or machine rims instead of forcing a mismatch.【F:knowledge/notes/denis_all_part02_review.md†L99284-L99353】
- **Pressure by load:** Heavy riders stabilize handling by targeting ≈4 bar rear / 3.5 bar front once mudguard brackets and wiring are rerouted for the taller rubber.【F:knowledge/notes/all_part01_review.md†L369-L370】
- **Track pressures:** PMT 10×3 slicks settle around 2.4 bar for general track duty, Vsett racers push 3.5 bar, and dropping to 1.8 bar shreds cords—log rider weight alongside PSI when tuning Xiaomi race builds.【F:data/vesc_help_group/text_slices/input_part003.txt†L12150-L12156】【F:data/vesc_help_group/text_slices/input_part003.txt†L12214-L12226】

## Mounting & Sealant Tips
- **Warm and center stubborn casings.** Dust rims and tubes with talc, pre-warm Xuancheng/PMT shells with a heat gun, and cinch the tread with zip ties so beads drop into the rim center before levering the tire home.【F:knowledge/notes/denis_all_part02_review.md†L90621-L90637】【F:knowledge/notes/denis_all_part02_review.md†L90909-L90921】
- **Use air volume, not pressure spikes.** Hand pumps stall near 105 psi—seat tubeless tires with high-flow foot pumps, station compressors, or ratchet straps that momentarily seal the beads.【F:knowledge/notes/denis_all_part02_review.md†L81739-L81819】
- **Blast stubborn tubeless beads.** For 11 in conversions, remove the valve core, flood the bead with soapy water, cinch the tread, and dump ~150 psi from a bead bazooka or large compressor—portable inflators lack the airflow. Immediately bleed pressure back toward 50 psi for riding once the bead pops.【F:knowledge/notes/input_part005_review.md†L202-L204】
- **Skip improvised “air cannons.”** Ratchet straps and steady 5.5 bar airflow work; pulsed compressors and homemade blasts have flung hoses, damaged hearing, and convinced riders to buy shop-grade 8 bar compressors instead.【F:knowledge/notes/input_part005_review.md†L357-L358】
- **Pick aluminum-safe sealants.** Yellow tubeless Slime avoids rim corrosion and plays nicely with PMT/Xuancheng setups; mixing CRC Fix foam with standard Slime violently reacts and coats the wheel in expanding goo.【F:knowledge/notes/denis_all_part02_review.md†L85974-L85997】【F:knowledge/notes/denis_all_part02_review.md†L81862-L81882】
- **Rinse tube sealant after seating.** Tube-specific Slime must be flushed from tubeless G30 rims once the bead seals to prevent long-term corrosion and mess inside the wheel.【F:knowledge/notes/input_part005_review.md†L356-L357】
- **Use the valves provided with modern tubeless casings.** PMT/Xuancheng tires now ship with tubeless valves that seal without slime—reserve sealant for aluminum-safe formulas if you still want puncture insurance.【F:knowledge/notes/denis_all_part02_review.md†L101765-L101775】
- **Heat and reshape dented rims cautiously.** Small tubeless rim dents can be warmed and hammered flat, but expect to reseal with silicone or swap the tire if the bead still leaks after repairs—suspended G30 builds still need correct tire pressure and post-curb inspections.【F:data/vesc_help_group/text_slices/input_part000.txt†L17940-L18007】

## Conversion & Fitment Steps
- **Machine rims for true 10×2.5″ tires.** Shave ≈1.5 mm from Xiaomi rims (lathe preferred), deburr carefully, and swap to curved valves so Monorim forks clear the stem—run 60–65 psi for 90 kg riders and treat wet pavement with caution. Builders chasing 10×3 conversions on the Pro 2 received the same advice along with reminders to upgrade controller MOSFETs/caps before pairing wider rubber with 48 V tunes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60009-L60033】[^lathe]
- **Protect Monorim hub screws.** When swapping to pneumatics, support the wheel and ease out the five perimeter screws—stripping one ruins the hub. Drill for 90° valves, shield magnets from filings, and rotate the stem ~45° if it still touches the fork.[^monorim-valve]
- **Keep water out after valve tweaks.** After rotating or bending stems for clearance, reinforce the grommet area so spray can’t wick into the motor cavity during rain rides.[^water-guard]
- **Pair 500 W Monorim hubs with quality air tires.** The workshop cautioned that the 500 W kit feels unsafe on stock rubber—install a modded air tire before feeding it 12 S power so traction matches the torque jump.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L20004-L20007】

## Brake Packages
- **Semi-metallic pads:** Gold-toned semi-metallic pads last longer and maintain bite in rain compared with organic pads bundled with XTech calipers; ceramics run hotter and demand rotor monitoring.【F:knowledge/notes/all_part01_review.md†L226-L227】
- **Rotor sizing:** Community swaps standardize on 135–140 mm rotors for Pro decks and 120 mm for base models when installing X-Tech HB100s or higher-end hydraulics.【F:knowledge/notes/all_part01_review.md†L338-L338】
- **Rear-disc conversions:** Konyk 40 mm magnet hubs clear Xiaomi dropouts with 120 mm spacing and accept 180 mm rotors once spacers are machined—capture final washer stacks and torque specs when documenting conversions.【F:data/vesc_help_group/text_slices/input_part003.txt†L20636-L20643】
- **Controller mounting templates:** Community drills for hanging a Ubox 75 V 100 A under the deck rely on threaded inserts plus separate buck converters for 5 V tail lights—document hole spacing and enclosure choices before copying the layout.【F:data/vesc_help_group/text_slices/input_part003.txt†L20935-L20956】
- **Budget alternatives:** Properly adjusted MTB-style mechanical calipers (“Bike Attitude”) can outperform misaligned semi-hydraulics when combined with 135 mm rotors—center the fixed pad before tightening mounts.【F:knowledge/notes/all_part01_review.md†L226-L227】
- **SNSC drum adapters:** Inverted SNSC setups need a spacer and both mounting points engaged before the drum aligns—plan fabrication time instead of relying on a single bracket.【F:knowledge/notes/input_part004_review.md†L241-L241】
- **Kotto 3 mm motorcycle calipers:** Expect to machine spacers and bleed them immediately—the bite is excellent but the calipers ship thick and dry compared with scooter hydraulics.【F:knowledge/notes/input_part004_review.md†L221-L221】
- **Support brake housing runs.** Tie the cable housing to the frame and trim excess length—loose housing eats lever travel and ruins braking force no matter the caliper upgrade.【F:knowledge/notes/denis_all_part02_review.md†L89091-L89096】
- **Watch Magura clearance.** MT7/MT8 calipers squeezed onto Xiaomi G30 and VSETT frames can lose their <5 mm tire gap as the casing flexes—check clearance regularly, keep spare banjos/hardware, and reconsider external hose reroutes that rub 10×3 tires after flats.【F:knowledge/notes/input_part001_review.md†L642-L644】
- **Torque lever bleeds properly.** Magura lever bleed screws only want 0.5 Nm; overtightening strips the threads and dumps pressure mid-ride.【F:knowledge/notes/input_part001_review.md†L683-L684】

## Suspension, Wheelbase & Handling Tweaks
- **Rear suspension stretch:** Bolt-on rear suspension kits extend wheelbase roughly 10 cm, noticeably calming Xiaomi chassis at 35–40 km/h once brake adapters are spaced correctly.【F:knowledge/notes/all_part01_review.md†L226-L227】
- **Stem stability:** Pair plastic shims with Foldster X-Lock or Phoenix clamps to eliminate wobble; trim or relocate latch hardware so Wildman battery bags clear the hook without scuffing packs.【F:knowledge/notes/all_part01_review.md†L272-L276】【F:knowledge/notes/all_part01_review.md†L399-L401】
- **Lighting integration:** 3D-printed fender supports and extender housings can host sealed LED strips or ESP32-controlled animations, but route wiring inside the bag to protect it from tire splash.【F:knowledge/notes/all_part01_review.md†L276-L276】
- **Beam pattern validation:** Budget Towwoo “8000 lm” lights produced narrow hotspots compared with Olight/OSRAM lamps—photograph beam patterns after upgrades so Xiaomi riders can trust claimed lumen figures.【F:data/vesc_help_group/text_slices/input_part003.txt†L23928-L23969】

## Setup Checklist
1. **Mock clearances:** Dry-fit the chosen tire and suspension combo, confirming mudguard, brake, and harness spacing before inflating to full pressure.【F:knowledge/notes/all_part01_review.md†L337-L338】【F:knowledge/notes/all_part01_review.md†L369-L370】
2. **Bed brakes:** After any pad or rotor swap, bed the system in with controlled stops to prevent glazing and squeal—especially important for semi-metallic upgrades.【F:knowledge/notes/all_part01_review.md†L226-L227】
3. **Retorque hardware:** Recheck axle nuts, adapter bolts, and suspension pivots after the first rides; stretched wheelbases and taller tires settle hardware quickly.【F:knowledge/notes/all_part01_review.md†L226-L227】【F:knowledge/notes/all_part01_review.md†L336-L337】

[^lathe]: 【F:knowledge/notes/all_part01_review.md†L93600-L93647】【F:knowledge/notes/all_part01_review.md†L93636-L93646】【F:knowledge/notes/all_part01_review.md†L93717-L93725】
[^monorim-valve]: 【F:knowledge/notes/all_part01_review.md†L107469-L107478】
[^water-guard]: 【F:knowledge/notes/all_part01_review.md†L111977-L111999】

