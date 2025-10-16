# Chassis Fitment and Maintenance

## Bearing and Wheel Upgrades

- Monorim 500 W hub motors accept 6001 rear bearings and 16003 stainless fronts when refreshing the rolling hardware, supporting wider tire conversions.[^bearing_sizes]
- Xiaomi frames can host 2.5–3.0 inch tires, but builders watch for clearance limits to avoid rubbing after the wider fitment.[^tire_clearance]
- Scooter bearing techs warn against cracking open sealed hubs or stuffing them with 70 % grease fills; standard-clearance cartridges already tolerate thermal expansion, so riders stick with OEM-style fills instead of chasing C3 replacements that only add drag.[^sealed_bearing_fill]

## Frame Stiffness Checks

- Removing the deck from a Dualtron Spider leaves the frame too flexy to stand on; riders are adding reinforcement and planning higher-power motor swaps only after hall wiring and 10 AWG phase leads are sorted to keep the chassis stable.[^dualtron_spider]

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


## References

[^1]: Source: knowledge/notes/input_part000_review.md†L323-L323
[^2]: Source: knowledge/notes/input_part000_review.md†L376-L376
[^3]: Source: knowledge/notes/input_part000_review.md†L374-L374
[^4]: Source: knowledge/notes/input_part000_review.md†L515-L516
[^5]: Source: knowledge/notes/input_part000_review.md†L517-L517
[^6]: Source: knowledge/notes/input_part000_review.md†L706-L710
[^7]: Source: knowledge/notes/input_part000_review.md†L710-L714
[^sns_supply]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24537-L24551
