# Xiaomi Tire, Brake & Handling Upgrade Notes

## Tire Selection & Pressures
- **10" pneumatic upgrades:** CST 10×2.25, Wanda 10×2, and Xuancheng casings deliver the best grip once inflated toward 3.5–4.2 bar; running them near 36 psi dulls the expected 12 S speed gains and risks fender rub until clearances are checked.【F:knowledge/notes/all_part01_review.md†L226-L228】【F:knowledge/notes/all_part01_review.md†L369-L370】【F:knowledge/notes/all_part01_review.md†L696-L696】
- **Solid vs. pneumatic:** Riders report roughly 20 % higher energy use, harsher ride quality, and accelerated fatigue on battery tabs when solid tires replace pneumatics—reserve solids for short-range emergency duty.【F:knowledge/notes/all_part01_review.md†L336-L337】
- **Valve and rim prep:** Monorim 500 W hubs ship without valve holes; drill carefully and add angled stems before installing tubes. Sand thick CST beads or rim casting bumps so 10" conversions seat evenly and avoid wobble. Blade owners even notch the split rim so a beefier Schrader clears the casting—valve extensions help you inflate but still expect to relieve metal around the stem on compact rims.【F:knowledge/notes/all_part01_review.md†L337-L338】【F:knowledge/notes/all_part01_review.md†L696-L696】【F:data/vesc_help_group/text_slices/input_part007.txt†L512-L521】
- **Match tire to rim width:** Stretching 6"-wide casings over 6.1" rims left beads off-center, valves fouled, and fenders rubbing; source true 155 mm tires or machine rims instead of forcing a mismatch. Stick with 10×2 tubes inside 10×2.125 casings—10×2.5 tubes balloon, wrinkle, and feel sketchy even if you manage to bolt the rim halves together.【F:knowledge/notes/denis_all_part02_review.md†L99284-L99353】【F:data/vesc_help_group/text_slices/input_part007.txt†L494-L515】【F:data/vesc_help_group/text_slices/input_part007.txt†L543-L547】
- **Pressure by load:** Heavy riders stabilize handling by targeting ≈4 bar rear / 3.5 bar front once mudguard brackets and wiring are rerouted for the taller rubber.【F:knowledge/notes/all_part01_review.md†L369-L370】
- **Read the sidewall markings.** Her0DasH confirmed the yellow stripe denotes a tubeless carcass—tube-only casings still need an inner tube even if they look identical on the shelf.【F:data/vesc_help_group/text_slices/input_part007.txt†L142-L143】
- **Know when tubeless fails.** Sealant tricks only go so far—if the split hub was never machined for a tubeless bead, plan on dedicated rims instead of wasting time trying to seat incompatible casings.【F:knowledge/notes/input_part007_review.md†L512-L512】

## Mounting & Sealant Tips
- **Warm and center stubborn casings.** Dust rims and tubes with talc, pre-warm Xuancheng/PMT shells with a heat gun, and cinch the tread with zip ties so beads drop into the rim center before levering the tire home.【F:knowledge/notes/denis_all_part02_review.md†L90621-L90637】【F:knowledge/notes/denis_all_part02_review.md†L90909-L90921】
- **Use air volume, not pressure spikes.** Hand pumps stall near 105 psi—seat tubeless tires with high-flow foot pumps, station compressors, or ratchet straps that momentarily seal the beads.【F:knowledge/notes/denis_all_part02_review.md†L81739-L81819】
- **Pick aluminum-safe sealants.** Yellow tubeless Slime avoids rim corrosion and plays nicely with PMT/Xuancheng setups; mixing CRC Fix foam with standard Slime violently reacts and coats the wheel in expanding goo.【F:knowledge/notes/denis_all_part02_review.md†L85974-L85997】【F:knowledge/notes/denis_all_part02_review.md†L81862-L81882】
- **Use the valves provided with modern tubeless casings.** PMT/Xuancheng tires now ship with tubeless valves that seal without slime—reserve sealant for aluminum-safe formulas if you still want puncture insurance.【F:knowledge/notes/denis_all_part02_review.md†L101765-L101775】

## Conversion & Fitment Steps
- **Machine rims for true 10×2.5″ tires.** Shave ≈1.5 mm from Xiaomi rims (lathe preferred), deburr carefully, and swap to curved valves so Monorim forks clear the stem—run 60–65 psi for 90 kg riders and treat wet pavement with caution. Builders chasing 10×3 conversions on the Pro 2 received the same advice along with reminders to upgrade controller MOSFETs/caps before pairing wider rubber with 48 V tunes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60009-L60033】[^lathe]
- **Protect Monorim hub screws.** When swapping to pneumatics, support the wheel and ease out the five perimeter screws—stripping one ruins the hub. Drill for 90° valves, shield magnets from filings, and rotate the stem ~45° if it still touches the fork.[^monorim-valve]
- **Keep water out after valve tweaks.** After rotating or bending stems for clearance, reinforce the grommet area so spray can’t wick into the motor cavity during rain rides.[^water-guard]
- **Pair 500 W Monorim hubs with quality air tires.** The workshop cautioned that the 500 W kit feels unsafe on stock rubber—install a modded air tire before feeding it 12 S power so traction matches the torque jump.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L20004-L20007】
- **Source race-proven tubeless hardware.** Rage Mechanics and RFP rims lock beads under race abuse—document part numbers plus the matching Amass 8 mm connectors so others can replicate the setup without guessing at components.【F:knowledge/notes/input_part007_review.md†L539-L539】

## Brake Packages
- **Semi-metallic pads:** Gold-toned semi-metallic pads last longer and maintain bite in rain compared with organic pads bundled with XTech calipers; ceramics run hotter and demand rotor monitoring.【F:knowledge/notes/all_part01_review.md†L226-L227】
- **Rotor sizing:** Community swaps standardize on 135–140 mm rotors for Pro decks and 120 mm for base models when installing X-Tech HB100s or higher-end hydraulics.【F:knowledge/notes/all_part01_review.md†L338-L338】
- **Budget alternatives:** Properly adjusted MTB-style mechanical calipers (“Bike Attitude”) can outperform misaligned semi-hydraulics when combined with 135 mm rotors—center the fixed pad before tightening mounts.【F:knowledge/notes/all_part01_review.md†L226-L227】
- **Support brake housing runs.** Tie the cable housing to the frame and trim excess length—loose housing eats lever travel and ruins braking force no matter the caliper upgrade.【F:knowledge/notes/denis_all_part02_review.md†L89091-L89096】
- **Integrate Nutt Y5 hydraulics carefully.** Ninebot F2 Pro conversions need a resistor ladder on the hall-brake line plus 5-bolt rotor adapters—thicker 120 mm discs or Monorim’s 140 mm rotor only fit once the adapter is installed.【F:knowledge/notes/input_part007_review.md†L408-L410】

## Suspension, Wheelbase & Handling Tweaks
- **Rear suspension stretch:** Bolt-on rear suspension kits extend wheelbase roughly 10 cm, noticeably calming Xiaomi chassis at 35–40 km/h once brake adapters are spaced correctly.【F:knowledge/notes/all_part01_review.md†L226-L227】
- **Stem stability:** Pair plastic shims with Foldster X-Lock or Phoenix clamps to eliminate wobble; trim or relocate latch hardware so Wildman battery bags clear the hook without scuffing packs.【F:knowledge/notes/all_part01_review.md†L272-L276】【F:knowledge/notes/all_part01_review.md†L399-L401】
- **Lighting integration:** 3D-printed fender supports and extender housings can host sealed LED strips or ESP32-controlled animations, but route wiring inside the bag to protect it from tire splash.【F:knowledge/notes/all_part01_review.md†L276-L276】
- **Mind suspension travel on 11" conversions.** Gabe’s 11" PMT swap only cleared by limiting fork travel, making the mod viable for light riders willing to trade comfort for tire width.【F:knowledge/notes/input_part007_review.md†L414-L414】
- **Brace the F2 Pro steering column.** Cihan traced jerky braking to ~2.5 mm of play above the front wheel, signalling the column—not the rotor—needs reinforcement for smooth lever feel.【F:knowledge/notes/input_part007_review.md†L416-L416】

## Setup Checklist
1. **Mock clearances:** Dry-fit the chosen tire and suspension combo, confirming mudguard, brake, and harness spacing before inflating to full pressure.【F:knowledge/notes/all_part01_review.md†L337-L338】【F:knowledge/notes/all_part01_review.md†L369-L370】
2. **Bed brakes:** After any pad or rotor swap, bed the system in with controlled stops to prevent glazing and squeal—especially important for semi-metallic upgrades.【F:knowledge/notes/all_part01_review.md†L226-L227】
3. **Retorque hardware:** Recheck axle nuts, adapter bolts, and suspension pivots after the first rides; stretched wheelbases and taller tires settle hardware quickly.【F:knowledge/notes/all_part01_review.md†L226-L227】【F:knowledge/notes/all_part01_review.md†L336-L337】

[^lathe]: 【F:knowledge/notes/all_part01_review.md†L93600-L93647】【F:knowledge/notes/all_part01_review.md†L93636-L93646】【F:knowledge/notes/all_part01_review.md†L93717-L93725】
[^monorim-valve]: 【F:knowledge/notes/all_part01_review.md†L107469-L107478】
[^water-guard]: 【F:knowledge/notes/all_part01_review.md†L111977-L111999】

