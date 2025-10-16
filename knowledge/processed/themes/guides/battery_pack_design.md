# Battery Pack Design Notes

## Cell Selection Strategies

- Builders are migrating from Samsung 40T 15 S 6 P packs to denser 15 S 10 P VTC6 or pending Samsung 50S cells to curb voltage sag, accepting higher per-cell costs for improved current handling.[^pack_cells]
- Abuse testing on recycled 250 W hub motors with 84 V/2 000 W inputs demagnetised rotors past ~80 °C, so builders now favour fresh Samsung 35E/50S/48X cells or 21700 formats when repacking Xiaomi decks to keep thermal headroom and energy density balanced.[^cell_refresh]
- Mirono’s teardown of Vsett-sourced packs shows DynaVolt-built 14 S 6 P modules with BAK 2 600 mAh cells staying near ambient at ~30 A (≈2.3 C); they are viable donor bricks so long as the original BMS current limits remain in place.[^1]
- NKON-sourced EVE and BAK cells continue to meet spec for budget packs, whereas random AliExpress batteries or mystery LG bundles often arrive damaged or underperform—stick with reputable builders even if prices climb.[^denis-cell-vetting]
- High-current discharge tests demand Kelvin (four-wire) probing.
  - thin alligator clips dropped a healthy P42A to a false 1.9 V at 20 A until the team clamped directly to the tabs
  - so upgrade leads and meters before condemning cells.[^2]
- EU comparison logs now peg P42A as the 20–30 A workhorse, LG/Samsung 50G as the 7–10 A efficiency pick, and Samsung 50S/Vapcell T50 matching P42A output only if you can justify roughly double the price; community bulk buys land 30T/35E/50G cells near €2.5–€4 each.[^3]

## Capacity Planning & Chemistry Guardrails

- Mirono’s 13 S 5 P NCR21700A pack starts at 50 A battery current and caps around 75 A so the ≈15 A-per-cell string stays inside spec.
  - use the same discipline whenever you squeeze high-capacity cells into 5 P commuters.[^4]
- AWD conversions should run a single motor until a 16 S 5–7 P (or internal/external hybrid) battery is ready; 12 S 3 P packs sag or overheat on VESC hardware even when the controller can deliver the amps.[^5]
- Mixed MJ1/MH1 parallels sag 10–12 V at ≈9 A per cell; veterans cap both chemistries near 7 A and pivot to Samsung 50G, Molicel P42A, or Murata VTC6 for higher-current builds instead of chasing firmware fixes.[^6]
- Denis equates a 13 S 6 P stack of 2 500 mAh cells to roughly 20 Ah at 10 S, giving Pro-class decks about double the stock range so long as you respect Rita’s 5 A shared charging limit.[^denis-13s6p-pack]
- Budget Liitokala LiFePO₄ cells arrive unbalanced, sag heavily above ≈12 A, and often ship slowly by boat.
  - reserve them for stationary projects unless you can package much larger scooter enclosures.[^7]
- Lithium fires are effectively self-sustaining, so crews only trust water for cooling nearby equipment; where packaging allows, they spec LiFePO₄ blocks to tame thermal runaway risk despite the weight penalty.[^denis-fire]

## Booster & Repair Safeguards (Denis Part 02, Lines 15 001–16 500)

- Extending Xiaomi internals with 2S2P “booster” bricks only works when the add-on carries its own BMS and dedicated charge plug—never backfeed the stock harness.[^booster-bms]
- Don’t tack spare cells across finished packs: Denis only tolerates soldering after you rebuild each parallel group properly, otherwise the sub-pack stays unprotected and charges awkwardly.[^solder-parallel]
- Retire recycled laptop cells from traction duty; stick with fresh high-discharge parts such as EVE INR18650-26V sourced from NKON or similar vetted vendors.[^fresh-cells]
- The Rita BMS Tool’s amp-hour fields are cosmetic; only the series configuration changes scooter behavior, so mis-entered capacity values won’t fix range math.[^rita-capacity]
- Cheap handheld spot welders still struggle with EV-grade interconnects—budget for K-weld-class tools if you expect durable joints, especially when stepping up to 21700 builds.[^welder-upgrade]
- Portable capacitor welders behave far better when you shorten the leads, reinforce high-current traces, and feed them with ≥180 C LiPo packs while keeping pulses at or below ~30 J; overshooting toward 50 J on soft 80 C bricks scorches 0.1–0.15 mm nickel and overheats MOSFETs.[^portable-welder-tuning]

## Layout and Interconnects

- Proposed geometries include 16 S 7 P and 12 S 9 P assemblies that rely on wider nickel strips and copper busbar "sandwich" welds to sustain 70–80 A continuous discharge without overheating.[^pack_layout]
- Community connector tables drive upgrades from stock 10–12 AWG leads to heavier wiring and lower-resistance plugs (XT60/90/150, EC5) on Ubox builds.[^pack_connectors]
- Square 10S3P bricks slip into 2 L cases while 10S4P packs demand honeycomb spacing; reuse OEM spacers only when you add ≥8 mm multi-path nickel links so every cell has its own series bridge.[^denis-10s-spacing]
- Route balance leads along the pack underside, keep harness lengths within ~50 % of each other, and solder power leads across the full nickel bus so load spreads evenly instead of concentrating on a single strip.[^denis-balance-routing]
- Ninebot Max and Xiaomi Pro deck extensions can accommodate up to 16 S 5 P 21700 modules with ~27 mm spacers, though installers often trim or rotate controller housings to keep packaging tidy.[^deck_extension]
- Tudor’s PETG honeycomb holders and interlocking connectors let Xiaomi and G30 packs dry-fit without glue, while other builders laser-cut 3–6 mm kraftplex skeletons, wrap them in thin PETG jackets, and still tape the stack with fish paper because sealed decks trap heat regardless of insulation choices.[^petg_honeycomb]
- Recycling pledges are nudging EU pack shops toward kraftplex or other recyclable wraps, yet fish-paper rolls are scarce enough that crews are prototyping 0.8 mm kraftplex jackets while still insisting on series separators to prevent can-to-can shorts.[^8]
- Koxx’s 14 S 6 P build uses RePackr-balanced groups, glued cells, and glass-fibre spacers between layers to equalise resistance across parallels inside cramped decks.
  - mirror the approach when you need uniform discharge in tight enclosures.[^9]
- Xiaomi and Ninebot decks swallow 12 S 4 P–5 P 21700 packs if you stand the cells vertically, add deck spacers, wrap every edge in fish paper, and insulate the tray so the aluminium shell cannot abrade nickel; even sub-millimetre gaps around magnets become failure points without that prep.[^10]
- Xiaomi Pro frames will even accept 15 S 4 P 21700 bricks (16 S 4 P is the realistic ceiling) when you chase high-voltage internals; favour high-discharge cells such as Samsung 50E/40T, Molicel P42A, or Sony VTC6A to keep sag in check on aggressive tunes.[^denis-21700-fit]
- EU builders are struggling to source sub-kilogram lots of 21700 honeycomb nickel, so crews now pool half-kilo group buys or pay ~€40 to EU suppliers rather than wait for AliExpress consolidation when deadlines loom.[^11]
- Mirono refuses to assemble small packs without rigid holders or honeycomb cages, pairing the structure with rubber liners whenever Xiaomi frame rails are sanded so 12 S 4 P packs and controller looms can share the tray without chafing.[^12]
- Copper “sandwich” busbars (0.1 mm copper capped with nickel) paired with 0.1 mm pure copper links now anchor 120 A BMS builds, proving the laminate holds up when riders document weld energy and clamp pressure.[^copper_sandwich]
- Honeycomb layouts that funnel a whole 5 P group through a single 8 mm nickel strip have already bottlenecked current.
  - rebuild with sheet bussing or at least five 7–8 mm straps in parallel (0.25–0.30 mm thick) so each bridge carries ≥35–40 A without hot spots before scaling voltage or series count.[^13]
- Denis, Hero, and Rumi are prototyping rigid external cases while others test riveted aluminium shells as theft-resistant alternatives to Wildman pouches—treat metal bag concepts as in-progress until durability testing lands.[^denis-metal-bag]
- Even copper-sandwiched 20S10P builds demand robust fusing and monitoring—Paolo’s Murata packs can still light off if an ESC faults and shorts the bus, so treat protection hardware as mandatory, not optional.[^denis-paolo-fuse]
- Rental G30 conversions swallow "thick" 13 S 5 P 21700 packs once the spacer grows the cavity to ≈155 mm × 400 mm, but EU builders struggle to source 220 mm shrink locally.
  - plan packaging and consumables early for long-range decks.[^14]
- Battery refurbishers now glue reclaimed cells into rigid cages with Gorilla or Sikaflex-class adhesives instead of relying on bare Kapton, pairing the structure with individual cell testing so vibration does not tear packs apart mid-ride.[^adhesive-cages]

## Testing & Service Notes

- Serious pack testing now leans on iCharger 4010 Duos or DIY 400 W–1 kW resistor banks built into miner chassis so builders can log charge/discharge curves before the pack hits the road.[^15]
- Acetone remains the go-to solvent for peeling stubborn double-sided tape between LiPo bricks before repurposing them as spot-welder supplies.
  - ventilate the workspace and stage absorbent pads before bathing the cells.[^16]
- Xiaomi’s stock GX16-3 inlet is happiest around 3 A because the internal JST pigtail overheats; parallel pins on a GX16-4 for 6–8 A service or swap to XT30 leads with 16–18 AWG silicone wire to keep resistance and heat under control.[^17]
- Inmotion LF8 rental packs expose B+/B− pads under silicone-potted BMS boards.
  - bypassers now solder straight to the nickel busbars but stress that unsupervised discharge or secondary-BMS deletes are a fire risk.[^18]
- Face de Pin Sucé’s 16 S 10 P P42A pack tolerated 47 A fast charging once paired with an external power stage and active cooling, setting a benchmark for pit-charge workflows on high-capacity builds.[^19]
- Artem’s latest 14 S pack stacks dual 3 mm copper busbars, layered insulation, and remote BMS wiring that demands a 5 V pre-charge before plugging in the balance loom.
  - document that activation sequence before shipping SIM-enabled boards to customers.[^20]
- Range logs from 12 S 4 P P42A packs show 15–20 km of aggressive riding consuming ~40 % capacity with 40 A battery / 80 A phase peaks, underscoring how lower-voltage Wheelway hubs heat quickly without thermistors or active cooling.[^21]

[^pack_cells]: Source: knowledge/notes/input_part000_review.md, line 63.
[^cell_refresh]: Source: knowledge/notes/input_part000_review.md, line 117.
[^pack_layout]: Source: knowledge/notes/input_part000_review.md, line 64.
[^pack_connectors]: Source: knowledge/notes/input_part000_review.md, line 65.
[^deck_extension]: Source: knowledge/notes/input_part000_review.md, line 75.
[^petg_honeycomb]: Source: knowledge/notes/input_part000_review.md, line 216.
[^copper_sandwich]: Source: knowledge/notes/input_part000_review.md, lines 240 and 314.
[^denis-cell-vetting]: Source: knowledge/notes/denis_all_part02_review.md†L1068-L1069
[^denis-10s-spacing]: Source: knowledge/notes/denis_all_part02_review.md†L1023-L1023
[^denis-balance-routing]: Source: knowledge/notes/denis_all_part02_review.md†L1024-L1024
[^denis-metal-bag]: Source: knowledge/notes/denis_all_part02_review.md†L1025-L1025


## References

[^1]: Source: knowledge/notes/input_part000_review.md†L548-L548
[^2]: Source: knowledge/notes/input_part000_review.md†L605-L607
[^3]: Source: knowledge/notes/input_part000_review.md†L609-L617
[^4]: Source: knowledge/notes/input_part000_review.md†L311-L311
[^5]: Source: knowledge/notes/input_part000_review.md†L312-L312
[^6]: Source: knowledge/notes/input_part000_review.md†L313-L313
[^7]: Source: knowledge/notes/input_part000_review.md†L318-L318
[^8]: Source: knowledge/notes/input_part000_review.md†L315-L315
[^9]: Source: knowledge/notes/input_part000_review.md†L314-L314
[^10]: Source: knowledge/notes/input_part000_review.md†L446-L450
[^11]: Source: knowledge/notes/input_part000_review.md†L450-L452
[^12]: Source: knowledge/notes/input_part000_review.md†L482-L485
[^13]: Source: knowledge/notes/input_part000_review.md†L660-L664
[^14]: Source: knowledge/notes/input_part000_review.md†L680-L683
[^15]: Source: knowledge/notes/input_part000_review.md†L324-L324
[^16]: Source: knowledge/notes/input_part000_review.md†L397-L397
[^17]: Source: knowledge/notes/input_part000_review.md†L547-L552
[^18]: Source: knowledge/notes/input_part000_review.md†L551-L552
[^19]: Source: knowledge/notes/input_part000_review.md†L553-L554
[^20]: Source: knowledge/notes/input_part000_review.md†L512-L516
[^21]: Source: knowledge/notes/input_part000_review.md†L520-L524
[^booster-bms]: Source: knowledge/notes/denis_all_part02_review.md†L626-L626
[^solder-parallel]: Source: knowledge/notes/denis_all_part02_review.md†L627-L627
[^fresh-cells]: Source: knowledge/notes/denis_all_part02_review.md†L628-L628
[^rita-capacity]: Source: knowledge/notes/denis_all_part02_review.md†L629-L629
[^welder-upgrade]: Source: knowledge/notes/denis_all_part02_review.md†L630-L630
[^denis-fire]: Source: knowledge/notes/denis_all_part02_review.md†L713-L713
[^denis-paolo-fuse]: Source: knowledge/notes/denis_all_part02_review.md†L741-L741
[^portable-welder-tuning]: Source: knowledge/notes/denis_all_part02_review.md†L803-L803
[^adhesive-cages]: Source: knowledge/notes/denis_all_part02_review.md†L895-L895
[^denis-13s6p-pack]: Source: knowledge/notes/denis_all_part02_review.md†L906-L906
[^denis-21700-fit]: Source: knowledge/notes/denis_all_part02_review.md†L997-L997
