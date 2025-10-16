# Chassis Fitment and Maintenance

## Bearing and Wheel Upgrades

- Monorim 500 W hub motors accept 6001 rear bearings and 16003 stainless fronts when refreshing the rolling hardware, supporting wider tire conversions.[^bearing_sizes]
- Xiaomi frames can host 2.5–3.0 inch tires, but builders watch for clearance limits to avoid rubbing after the wider fitment.[^tire_clearance]
- Blade split rims that refuse to separate often need the cover holes chased or the 110–112 mm axle stack reset with fresh 12 mm washers/nuts before committing to a full motor tear-down.[^blade_split]
- Stuck hub bearings warrant a proper puller; cutting shoulders risks permanent axle damage when rusted races won’t slide off by hand.[^bearing_puller]
- High-speed hub refreshes now favor 2RS seals as the balance between drag and protection, keep ZZ for minimal resistance, and skip RSH unless you accept extra drag—Vsett bearings cooked after ~17 000 km without timely swaps.[^bearing_seals]
- Updated Vsett 10+ service lists now call for SKF 6202/6004 2RSH wheel bearings, 20 × 28 × 6 and 15 × 25 × 5 simmering seals, 16287 2RS swingarm bearings, and 30 × 41 × 6.5 36°×45° headset bearings to replace the rust-prone stock hardware.[^vsett10_bearings]
- SKF clarified that C3-clearance 2Z bearings leave extra race spacing for thermal growth, making them suitable for racing hubs despite the limited sealing compared with 2RS options.[^c3_clearance]

## Frame Stiffness Checks

- Removing the deck from a Dualtron Spider leaves the frame too flexy to stand on; riders are adding reinforcement and planning higher-power motor swaps only after hall wiring and 10 AWG phase leads are sorted to keep the chassis stable.[^dualtron_spider]
- Slack Core prototypes may need reinforcement: the forged-aluminium neck geometry wins praise, but builders plan to beef up the thin lower joint before putting 100 kg riders on production frames.[^slack_core]

## Hardware Compatibility & Troubleshooting

- Blade 10/11 axles show up in both M12×1.25 and M14×1.5 threads depending on the batch; lock the hinge solid on donor frames and inventory hardware before chasing replacements.[^blade_threads]
- Retail techs note that Achilleus frames sit larger than Thunder chassis yet still wobble unless the hinge is overtightened, and Speedtrott’s smaller 40 mm motors remain the weak link even when the hinge survives.[^achilleus_feedback]
- A 203 mm rotor adapter that sits high usually means the axle isn’t fully seated; custom torque arms that sit flush on the dropout solved repeat pop-outs once the frame was tilted.[^torque_arm_flush]
- Monorim AWD conversions require flipping the suspension sides or spacing/bending the arms to clear Blade 10" hubs, plus at least 6 P of 50E/50G-class cells (or stronger) per wheel so 40 A battery feeds don’t cook marginal packs.[^monorim_swap]

## Deck Fabrication & Accessories

- Builders experimenting with transparent deck plates pair 6 mm acrylic lids with foam bedding or CNC 12 mm plexiglass spacers to hide LED strips; plan for eventual cracking and reinforce mounts before sealing the deck.[^1]
- Rental G30 frames accept printed battery extenders, but high BMS harnesses can foul vertical cells.
  - rewire harness exits or add 2 mm spacers so deck lids close without pinching leads.[^2]
- Vsett headlight retrofits need stiffer stem brackets to keep elevated lamps from shaking and to shorten the dark “dead zone”; CAD the mount before drilling to preserve the OEM look.[^3]
- Ninebot rental chassis hide factory silicone seams, lockable battery latches, and swappable pack harnesses.
  - making them attractive donors for high-power conversions once you add disc-compatible brake mounts.[^4]
- Boosted Rev decks only swallow roughly 60×21700 cells (≈12 S5 P) plus an underslung controller, so builders often pair charge-only BMS + fuse strategies when ANT smart boards exceed the 100 mm × 40 mm envelope.[^5]
- Ninebot G30 rental frames remain coveted donor chassis thanks to non-folding stems, dual brakes, oil suspension, thicker tubing, and ~10 kg of extra steel that swallows 13 S 5 P 21700 packs and 1.2 kW hubs without flexing like stock Xiaomi frames.[^6]
- Community salvage runs keep surfacing Dualtron, Etwow, and Xiaomi donor parts.
  - complete with 60 V packs and heavy-duty motors
  - illustrating how friendships and group buys keep premium frames affordable.[^7]

## Tyre Selection & Pricing

- PMT shoppers report €53–58 Stradale pricing in Italy versus €48 plus €19 shipping from Fastride, and Paolo nudges commuters toward the slightly softer Junior compound for grip without major range penalties.[^pmt_pricing]

[^bearing_sizes]: Source: knowledge/notes/input_part000_review.md, line 74.
[^tire_clearance]: Source: knowledge/notes/input_part000_review.md, line 74.
[^dualtron_spider]: Source: knowledge/notes/input_part000_review.md, line 187.
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


## References

[^1]: Source: knowledge/notes/input_part000_review.md†L323-L323
[^2]: Source: knowledge/notes/input_part000_review.md†L376-L376
[^3]: Source: knowledge/notes/input_part000_review.md†L374-L374
[^4]: Source: knowledge/notes/input_part000_review.md†L515-L516
[^5]: Source: knowledge/notes/input_part000_review.md†L517-L517
[^6]: Source: knowledge/notes/input_part000_review.md†L706-L710
[^7]: Source: knowledge/notes/input_part000_review.md†L710-L714
[^pmt_pricing]: Source: knowledge/notes/input_part002_review.md†L19775-L19804
