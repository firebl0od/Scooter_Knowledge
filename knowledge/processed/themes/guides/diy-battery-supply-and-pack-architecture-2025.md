# DIY Battery Supply & Pack Architecture Playbook (2025)

## TL;DR

- Europe’s salvage stream of EVE 50PL cells pushes landed costs near 1 € per cell while U.S. buyers still face ~$9 retail, so teams are forming cross-border partnerships and stockpiling QS8 hardware ahead of tariff hikes.[^1]
- High-power scooters are converging on 22–30 S frames with 8–11 P parallels: Dualtron Achilleus decks accept 22 S9 P packs once controllers move outboard, Nami race builds run 22 S11 P Molicel layouts toward 40 kW, and G30 conversions rely on upgraded skid plates, spacers, and cardboard pack mockups before committing to 20 S12 P experiments.[^2][^3][^4][^5]
- Production scooters rarely ship high-discharge cells outside of premium brands like Nami, so builders keep planning sleeper 20 S 3 P Molicel packs or full 20 S 9 P 21700 conversions even when the OEM battery is new.[^6]
- Copper strip markets are volatile again.
  - mid-2024 quotes doubled while riders debated 0.37 C “fast” charging, forcing TIG busbar budgets and group buys before multi-day endurance rides.[^7][^8]
- Smart BMS headroom still lags pack ambition: ANT discharge FETs can latch on failures and balance slowly, so builders pair structural pack supports (no hot glue) with redundant protection, UV inspections, and JBD/JK alternatives sized around 500 A continuous until 700 A units mature.[^9][^10][^11]
- Voltage raises demand more than it saves: stepping commuter builds from 16 S to 20 S trims battery current and nets roughly 2.5 km/h per added series cell, but 100 V MOSFETs run ~33 % higher Rds(on) and the longer pack demands tighter insulation, busbar clearance, and rider safety protocols before chasing the headline speed.[^12]
- NKON buyers chasing ≈100 A battery peaks still favour Molicel 40T cells despite cost, treating LG M50LT as a budget fallback until high-current tests confirm it avoids the 15 V sag seen on older 50G packs; budget ebike builds meanwhile stick with LG MH1 at about €1.70 per cell until 21700 options are affordable again.[^nkon-40t]
- Kaabo’s stock 16 S5 P pack still surges to 150–155 A despite 60 A controller limits, dropping ~15 V under dual-Ubox launches.
  - most riders plan chemistry upgrades (P42A/P45B or Samsung 50S) and connector changes before trusting the platform at sustained 120 A battery draw.[^13][^14][^15]
- Real sag logs put chemistry choices in context: a 20 S9 P Samsung 48X pack only dropped 6–7 V at 130–150 A with cell temps under 27 °C, while Paolo’s 21 S7 P Sony pack lost about 9 V at ~193 A.
  - evidence that 14 A-class cells stay cool but 25 A-class sticks need active monitoring when pushed harder.[^16]
- Size parallels by expected watt-hours and load.
  - not nominal Ah
  - with 6 P 21700 stacks roughly matching 7 P 18650 volume and VTC6 12 S strings rivaling 35E 13 S sag when currents stay under 7 A per cell.[^17]
- Regional packaging philosophies diverge: U.S. commuters keep bolting on seats and external battery crates for comfort, while European race crews carve weight out of standing decks.
  - log both approaches so new builders balance ergonomics, legality, and style goals before welding a pack around one camp.[^18]
- AWD newcomers should stage upgrades: 12 S 3 P commuter packs brown out on VESC duals, so run a single motor until a 16 S 5–7 P pack (or paired internal/external strings) is ready, and treat 13 S 5 P builds as 50–75 A battery systems despite the 15 A-rated cells.[^19][^20]

## Cell & Component Sourcing Reference

- **Keep the high-power roster current.** Community testers just flagged EVE 40PL/50PL, Molicel P50B, and BAK 45D as the modern reference set for 300 A+ packs.
  - refresh comparison sheets with Mooch’s latest lab data before committing to older chemistries.[^21]
- **Log per-cell sag realities.** LG MJ1 parallels started drooping once draws topped ~7–10 A per cell, whereas Samsung 35E banks held voltage better at the same load.
  - document chemistry limits before promising 16 S commuters big torque numbers.[^22]
- **Budget Xiaomi rebuilds still bottleneck at ~40 A per half-pack.** Dual 20 S stacks built from repacked Xiaomi cells only yield ~17.5 Ah and 40 A per section, so Zero 10X upgrades need parallel 8 AWG-equivalent harnesses at 100 A draws to avoid voltage sag.[^23]
- **Expect regional sourcing hurdles.** Turkish builders blocked from NKON lean on LG 29E/50E substitutes despite their sag, while racers still crown Molicel P45B for holding voltage under high current.
  - plan budgets and timelines around customs bottlenecks.[^24]
- **Budget regional price swings.** Israeli builders are now paying roughly €47 for a pair of Samsung P42A cells and struggling to import Samsung 50S stock, so mentors steer them toward EVE 40P parallels that give up 1 Ah yet deliver nearly double the discharge headroom at similar landed cost.[^25]
- **Keep the high-power roster current.** Community testers just flagged EVE 40PL/50PL, Molicel P50B, and BAK 45D as the modern reference set for 300 A+ packs.
  - refresh comparison sheets with Mooch’s latest lab data before committing to older chemistries.[^21][^26]
- **Budget trustworthy refurb lots.** Denis steers budget builds toward refurbished Samsung 35E/50E batches from NKON’s late-2021 stock as a reliable midlife option when premium chemistries are unobtainable.
  - document provenance and avoid mixing them with tired originals.[^27]
- **Match AWD chemistries to the target current.** Denis steers 15 S all-wheel-drive packs toward LG M29 or EVE 33V cells, while Arsenus adds proven high-draw staples.
  - Molicel P42A/P40T, Samsung 25R/30Q, and Sony VTC5/VTC6
  - keeping 21700 formats as the preferred baseline for sustained torque.[^28]
- **Monitor Denis’ in-house Pro/Pro 2 pack program.** His custom internal battery just entered production with hand-braided heavy-gauge charge/discharge looms that mirror the earlier 36 V kits.
  - expect vetted harness lengths and drop-in Xiaomi fitment once inventory lands.[^29]
- Even premium scooters rarely ship high-discharge cells beyond names like Nami, so builders plan sleeper 20 S 3 P Molicel packs or full 20 S 9 P 21700 conversions whenever packaging allows.[^premium-cells]
| Component | EU Pricing & Availability | North America Reality | Immediate Actions |
| --- | --- | --- | --- |
| **EVE 50PL 21700** | Salvaged Stark Varg modules deliver grade-A cells for ~1 € each after labor; retail bulk hovers 1.5 € with logos shaved yet still grade A.[^30] | ~$9 per cell retail with looming import duties.[^31] | Form cooperative buys, pre-clear customs brokers, and reserve storage for incoming pallets. |
| **Samsung/EVE 50E variants** | €1.5–2 each keep commuter packs affordable when 50PL supply tightens.[^10] | Similar pricing once landed but subject to tariff swings; easier sourcing than 50PL yet lower discharge ratings.[^10] | Stage these as fallback chemistries for ≤200 A builds; adjust wiring gauge accordingly. |
| **Samsung 48X 21700** | €3.35 per cell in 130-piece lots with excellent voltage matching (≤1 mV spread after 7 kW pulls).[^32] | Limited availability; prized for low impedance and cycle life projections (~2 000 cycles at 30–95 % SoC).[^33] | Reserve for high-power commuters needing long life; compare against Samsung 50G when prioritising low-amp cruising efficiency. |
| **Samsung 50G / 50S (direct import)** | Group buys land around €4.9–5.1 per cell (100 pc MOQ) with fresh offers dipping to €4.71 when teams coordinate outside marketplace fees; 50S handles 20 A fanless or 35 A with active cooling while 48X trails on heat.[^34][^35] | Expect €10 retail via EU resellers; still cheaper than piecemeal U.S. buys but budget shipping lead time.[^34] | Organise pallet orders, pre-pay VAT, and log discharge tests before promising 35 A service. |
| **LiitoKala LF105 / LF280 LiFePO₄** | Budget prismatic cells arrive unbalanced and sag above 12 A; sea freight stretches timelines but chemistry remains attractive for stationary packs.[^36] | Heavy freight and low C-rate limits make them poor scooter candidates without huge enclosures.[^36] | Reserve for off-board storage or energy carts; budget active balancing before parallel use. |
| **Molicel P45B / Samsung 40T** | Used in 22 S10/11 P race packs with 0.2 mm copper busbars and 350–500 A targets.[^37][^4] | Importable but pricier; marketing touts 45 A discharge and 6 A charge, yet builders still favour Samsung 30T/40T or P42A until independent 20–40 A curves prove the gains.[^38][^39][^40] | Schedule welding capacity, busbar stock, and thermal monitoring for >300 A continuous expectations. |
| **Molicel P45B / Samsung 40T** | Used in 22 S10/11 P race packs with 0.2 mm copper busbars and 350–500 A targets.[^37][^4] | Importable but pricier; rely on trusted builders when tooling costs outweigh one-off packs.[^38][^39] | Schedule welding capacity, busbar stock, and thermal monitoring for >300 A continuous expectations. |
| **LG M50LT (21700)** | Considered a budget alternative to 40T for ≈100 A packs, pending confirmation it avoids the voltage sag seen on older LG 50G builds.[^41] | Limited test data; treat as provisional until high-current characterization is logged.[^41] | Stage lab discharges before deploying in high-demand packs; weigh P42A/P45B thermal headroom against Samsung 50S cost before locking chemistry.[^14] |
| **LG MH1 (18650)** | Still popular in lightweight commuter packs at ≈€1.70 per cell despite limited current capability.[^42] | Similar pricing in other regions; best suited for modest current demands until 21700 budgets recover.[^42] | Use for low-amp builds and plan future upgrades to higher-discharge chemistries. |
| **Samsung 48X** | Veterans still praise 48X for moderate 12 A-per-cell builds, reporting ≤30 °C pack temps and excellent balancing with active shuttling.[^43] | Scarcer in North America; import when you prioritise longevity over sheer discharge capability.[^43] | Pair with active balancers to exploit the chemistry’s tight cell spread. |
| **EVE 40P (21700)** | Authentic samples show 5–7 mΩ IR and cooler operation than P42A pulls | Pricing still volatile; confirm provenance before bulk buys | Favor for high-current builds when 40PL packaging is impractical.[^44] |
| **BAK 2600 mAh (18650)** | ~€0.50 per cell for Xiaomi conversions but ~40 mΩ IR keeps them commuter-only | Limited U.S. sourcing and marginal headroom for heavy riders | Cap around 20 A per cell or reserve for lightweight builds to avoid sag complaints.[^45] |
| **Aspilsan 18650 (2.9 Ah)** | Entering Zero 10X upgrades across Turkey; treated as 5 C parts despite 25 A pulse claims | Import friction keeps pricing uncertain outside TR | Hold continuous draw near 15–20 A per cell until broader validation lands.[^46] |
| **EVE 40PL prisms** | ≈€6–7 each in small batches or ~$4.35 direct (50 pc MOQ + ~$100 freight) | Held 3.0 V for 62 s at 100 A while P45B sagged to 2.78 V after 44 s | Reserve wider housings and reinforce busbars before switching to pouch cells.[^21][^eve-pricing] |
| **Molicel P50B / XA3 previews** | P50B sampled at 5 Ah/65 A; XA3 teased at ≈50 A discharge with unknown cycle life | Potential step beyond P45B pending validation | Budget pilot batches and expect premium pricing until datasheets land.[^p50b][^xa3] |
| **LG M26 / MH1 budget stock** | €1 M26 cells remain common in high-tariff regions but show ≈14 mΩ IR when fresh versus >30 mΩ on older MH1 pulls | Adequate for commuter packs but sag versus premium cells; plan future upgrades | Builders debate tolerating sag temporarily or pausing builds until pricier cells are affordable, noting Aspilsan A28 samples breach 90 °C at 10–15 A while LG M26 stays near 40 °C on the same draw.[^47][^48] |
| **Tenpower 40TG** | Early four-parallel pulls held ≈65 A per cell with datasheet claims of 40 A continuous, hinting at promising race chemistry once thermal data is logged.[^49] | Limited field testing; expect pilot batches and temperature logging before deploying in commuter fleets. | Instrument packs heavily and validate heat rise before adopting for sustained 150 A scooters. |
| **QS8 connectors** | Stock through EU vendors today, but panel-mount options remain custom-fabricated.[^50] | Tariffs threaten to push unit cost toward $35; panel mounts rare.[^51][^50] | Bulk-order straight housings, print or machine mounts, and document safe connection sequences. |

- **SK 54 Ah pouch modules** | Advertised around 2 mΩ with 300 A continuous / 500 A peak output, but the tall bricks demand external battery bags or enlarged scooter housings to clear typical decks.
  - treat packaging as the limiting factor, not the cell chemistry.[^52] |
| **Smart BMS (JBD/JK/ANT)** | JBD units land around €50 for 20 S packs; JK units offer higher balancing throughput but larger footprints.[^53][^54] | ANT advertises 470 A–1 050 A but has logged discharge latch failures; redundancy required.[^9] | Combine smart BMS with external fusing/contactors and publish reset workflows for stuck FETs. |
| **Spot welders (K-Weld, Glitter 811A)** | Proven 0.1 mm copper welds at ≈300 € including PSU; Glitter 811A needs periodic pin cleaning to restore 4.4 kA output.[^55][^56] | Cheaper 90 € claims lack field proof on copper; shipping heavy welders across the Atlantic adds cost.[^55] | Allocate budget for pro-grade welders, shorten KWeld 8 AWG leads, stack CNHL LiPos or car batteries for 1 600 A hits, and refresh lugs so cable losses don’t steal kilowatts from copper “sandwich” busbars.[^57] |

Alibaba-listed A123 20 Ah LiFePO₄ prismatics still tout 200 A charge capability, but builders treat the spec skeptically and warn that the bulky format complicates scooter packaging compared with cylindrical cells.[^58]

- NetworkDir is already eyeing Molicel’s XA-series race cells (~2.6 Ah, ≈1.5–2 mΩ, 125 A charge/250 A discharge) while noting EVE 40PL still leads around 3 mΩ.
  - use those benchmarks when planning 30 S drag packs.[^59]
- 🇪🇸AYO#74’s 22 S11 P LG M50LT pack now serves as a placeholder until a P45B rebuild unlocks ≈495 A, underscoring how race teams schedule chemistry upgrades around discharge goals.[^60]
- Turkey’s new €30 import ceiling effectively blocks direct orders of scooters, motors, and welders; expect to pay 2–3× via licensed importers or coordinate in-country sourcing.[^61]
- Even shipping bare frames faces scrutiny.
  - airlines flag scooter parts over 100 Wh, so plan on slow, expensive ground freight for cross-border chassis trades.[^62]

## Motor & Controller Procurement Signals

- **Cheap 60 H “20×3” hubs trade torque for price.** AliExpress listings confirmed to use only 20 parallel strands instead of the usual 22, noticeably cutting copper fill and off-the-line thrust.
  - plan on rewinds or pay for higher-grade cores when you need real race torque.[^63]
- **Document axle swaps step-by-step.** Arnau’s workflow removes the lock washer, drives the old axle out with a protected mallet, and re-centres LY hubs with thin washers because many rims ship offset toward the brake side.
  - capture photos before pressing in new shafts.[^64]
- **Shortlist 85 V-class controllers with accessories in mind.** Spintend’s 85150 remains the go-to replacement when riders outgrow Flipsky 75100 duals; Matthew’s lineup reminder covers the ADC3 accessory bridge and the 18 S dual variant so builds preserve brake lights, horns, and external switches without homebrew boards.[^65]
- **Budget time for magnet topology differences.** Paolo notes Lonnyo’s budget 80 H cores stitch two 40 H magnets together, complicating smooth FOC versus single-piece 70/75/90 H stacks.
  - log detection tweaks or spend more on monolithic magnet rings.[^66]

## Pack Architecture Patterns

- **32 S3 P vs. 16 S6 P geometry** – Jan reminded builders that a 32 S 3 P stack fits the same 17×4 cell footprint as a 16 S 6 P module, so high-voltage prototypes can reuse proven deck layouts as long as insulation and enclosure clearances scale with the extra series count.[^67]
- **18 S 9 P P45B commuter packs** – Pulling 350 A from nine parallels lands near 40 A per cell; mentors advised logging sag and delivered phase amps before redesigning the layout, then focusing on cooling and packaging rather than jumping to 20 S because higher voltage won’t ease per-cell stress and mainly raises top speed.[^68]
- **20 S 5 P 65H race packs** – Custom 20 S 5 P layouts around 65H 17×4 motors land near 31.5 Ah (≈90 A battery) and force teams to decide between dual 16 S packs for 63 Ah range, a 20 S jump for speed, or a full 32 S leap depending on controller health (85150 vs. 85250).[^69]
- **Dualtron Achilleus conversions** – Deck cavity (~485 mm × 181 mm) supports 22 S9 P if controllers move to an external mount; stock decks hold 20 S7–8 P and ~100 A battery before needing relocation or compact ESCs.[^70]
- **Kaabo Wolf deck plans** – Owners sketch 20 S7 P footprints around 160 × 470 × 75 mm and weigh charge-only BMS wiring plus detachable JK balancers against flat ANT/JK smart boards that can actively balance ≈150 A builds inside the deck.[^kaabo-20s7p]
- **Deck spacer cautionary tales** – Oversized 3D-printed spacers claiming to fit four Xiaomi Pro packs rely on sparse M3 hardware and plastic trays to restrain ~30 kg of cells; veterans flag braking/suspension limits and insist on metal reinforcements before chasing that capacity.[^71]
- **Layout planning tools** – RePackr and e4bike.ru configurators help visualise series/parallel counts but miss vertical stacking tricks; CAD mockups remain mandatory for triangle packs and tight decks.[^72]
- **Hyosung “Puneron” gearing reference** – A 72 T/9 T sprocket set delivered the dirt-bike torque PuneDir was chasing on large-wheel conversions, giving builders a baseline ratio for similar hybrids.[^73]
- **Jiabada 17 S BMS fit checks** – Copper-backed 17 S/50 A Jiabada smart boards ship in under a week and fit alongside 17 S6 P LG stacks inside Xiaomi Pro 2 decks (~119 mm internal width) once you grind the rails or extend the tray for 21700 cells plus clearance.[^74]
- **SNSC rental-frame builds** – Crash-tested Segway SNSC tubes are handling 84 V packs at ~300 A continuous when paired with dual Spintend 85/250 controllers, cementing the platform as a premium donor once fleet frames surface.[^75]
- **Deck booster modules** – External 20 S 4 P bricks riding in 5 L Newboler or Wildman bags must match the deck pack’s chemistry, IR, and capacity before paralleling.
  - mismatched cells fight each other and cook balance leads on 20 S 8 P Ninebot builds.[^76]
- **Teverun Supreme 20 S 7 P reality** – The stock 35 Ah pack can burst past datasheet limits but still sags around 100 A; commuters planning sustained power swaps are moving to P45B-class cells or custom packs sized for higher continuous output.[^77]
- **High-voltage vs. high-current layouts** – Riders moving from 10 S 6 P to 20 S 3 P P45B packs log lower I²R losses and steadier torque because the controller can deliver 60–80 A phase while sipping ~40 A battery; the extra voltage headroom beats brute-force current for efficiency.[^78]
- **Ninebot G30 rectangular packs first.** The stock frame hides 20S6P packs cleanly, but veterans warn that stretching to 20S9P by machining rails and relocating the ESC complicates busbar routing and weakens structure.
  - keep first builds rectangular before chasing every spare millimetre.[^79]
- **20 S7 P Xiaomi-class builds need risers.** Packing 140 cells into a stock deck requires roughly 40 mm extender plates, proving that large parallels demand structural add-ons rather than simply rearranging the OEM bay.[^80]
- **Hybrid internal/external layouts demand precise planning.** A 3 L Wildman bag barely swallows 56 × 21700 cells, so stretch builds mock up nickel runs, split parallels (e.g., 12 P internal, 8 P external), and treat pack harnessing as the gating factor before punching slots in the deck.[^81]
- **Samsung 40T rebuilds revitalise tired fleets.** Replacing saggy 29E packs with 20 S 10 P 40T arrays drops voltage sag by roughly 7 V.
  - nearly a 10 % top-speed bump on voltage-limited scooters
  - while demanding controllers that can stomach the heavier current draw.[^82]
- **Commuter e-bikes benefit from 20 S upgrades.** Swapping 13 S 6 P 35E bricks for 20 S 5 P high-discharge packs nets about 60 % more capacity with less sag, especially when riders stage spare modules to keep handling sharp.[^83]
- **Navee N65/S65 headroom.** Expect room for dual VESCs and roughly 100 21700 cells with modest spacers, but cramming 120×18650 cells plus a 150 A JK BMS takes aggressive packaging and careful harness routing.[^84]
- **40PL GT2 envelopes** – Rosheee’s 20 S 6 P Samsung 40PL core from @jamessoderstrom stays inside James’ conservative current caps yet has riders eyeing 26 S upgrades; he’s already ordering 0.3 mm copper busbars so the pack can stretch safely once the chassis is ready.[^85]
- **Stealth 20 S9 P sleepers** – Jerome’s 20 S9 P EVE 40P commuter pack prioritises low internal resistance and cold-weather output even after peers praised Bak 45D; he shelved 40PL cells as overkill for the target scooter.[^86]
- **30 S single-motor experiments** – Patrick’s 30 S ambitions lean on Samsung 40T because customs complicate EVE imports, and his Lonnyo 16×4 hub plan includes dual-end wiring so he can swap between star and delta when chasing 120 km/h goals.[^87]
- **20 S12 P high-current commuters** – Haku’s 20 S12 P Molicel P42A pack regularly handles ~250 A battery and 300 A phase with a 520 A BMS cutoff, reinforcing that highway pulls demand large parallels to limit sag and overheating.[^88]
- **Dualtron Achilleus conversions** – Deck cavity (~485 mm × 181 mm) supports 22 S9 P if controllers move to an external mount, and builders are now stretching Achilleus/DT3 shells for 21 S 11 P Molicel packs or 22 S 9 P P45B layouts paired with Spintend 85250 controllers.
  - budget spacer stacks and dropout machining before chasing legal-looking, high-voltage drivetrains.[^70][^89]
- **Halo T107 Pro drawer pack** – Pandalgns’ 22 S 10 P P45B rebuild barely clears the drawer extender; offset rows, compression wrap, and abrasion barriers are mandatory to stop cells rubbing as the sled flexes.[^90]
- **Samsung 48G commuter baseline** – A Samsung 48G 20 S 8 P pack tops out around 150 A continuous before the BMS becomes the bottleneck; plan controller upgrades (e.g., dual Spintend 85/150) only after confirming the discharge spec and thermal headroom.[^91]
- **Halo Knight T107 Pro blueprint** – Pandalgns is packaging dual MKS 84200HPs, HM 3000 W 60 H hubs, and a planned 22 S 10 P P45B pack with 12 AWG phases, offering a ready-made layout for similarly sized decks once cooling and capacitor headroom are logged.[^92]
- **RM-Light race scooter baseline** – The RM-Light crew’s 22 S 4 P tabless packs, RM-X 2024 rear motors, and Beringer Br4ve brakes come in around 37 kg, giving builders a lightweight benchmark for 130–140 km/h race scooters built from premium components.[^93]
- **Cooling above 300 A phase** – Omar’s dual Spintend NAMI build overheated hubs and the 20 S 10 P 50S pack at 200 A battery / 310 A phase, while AYÓ reminded riders the stock 40 Ah module’s LG M50LT cells are only good for ~116 A continuous (≤135 A peaks) until rebuilt.
  - treat airflow, pack upgrades, or current caps as mandatory before chasing similar numbers.[^94]
- **Stem-pack practicality** – Noname’s Vsett 11 runs a 16 S 6 P stem pack without upsetting chassis balance, but he cautions the same mass overwhelms Ninebot G30 frames.
  - log stem-pack weight limits per chassis before copying the recipe.[^95]
- **Reinforced Ninebot G2 conversions** – Face de Pin Sucé is machining adapters and a 1 cm steel skid plate to house a 20 S 5 P Samsung 40T pack plus Rage FH60 motor, highlighting the fabrication burden when chasing street-legal torque in lightweight frames.[^96]
- **Hybrid Minimotors/VESC stacks** – Murcia’s “Pump” scooter ties two 16 S 200 A Molicel modules into a Minimotors controller and a VESC 75100 V1 for ≈20 kW mixed drivetrains.
  - proof hybrids can work when charge paths and grounding are planned carefully.[^97]
- **Turnkey single-motor benchmark** – Baartu is selling a €1.5 k package (20 S 5 P EVE 40P pack, LY 17×4 65 H hub, Ubox 85150, PMT tires, Monorim suspension) that claims 10.5 kW, 0–50 km/h in 2.2 s, and 85 km/h with field weakening.
  - handy price/performance reference when quoting custom builds.[^98]
- **22 S 10 P roadmaps** – Race builders still default to Molicel P45B for 22 S 10 P layouts but are already scouting 40–50 PL chemistries and Ampace JP40 cells for future 30–40 S experiments where higher voltage trims amp draw instead of chasing thicker busbars.[^99]
- **Rob Ver’s JP40 proof point** – His 22 S 9 P Ampace JP40 pack holds roughly 45 A continuous and 140 A peak per cell with only ~6 V sag, staying under 30 °C at 500 A thanks to 0.2 mm copper laminations; a prior 21 S 9 P LG M58T pack with 0.1 mm copper plus 0.1 mm nickel still feeds dual 100 A around 40 °C.[^jp40_pack]
- **Vsett/G30 packaging guardrail** – Forol squeezed 20 S 6 P (and maybe 7 P with printed spacers) into a dual-motor frame but warns newcomers not to tuck cell groups below the chassis ledge because the cover and BMS still need that volume.[^g30_ceiling]
- **Forol’s dual-motor deck walkthrough** – Sliding a 20 S pack beneath one ledge frees the opposite ledge for the BMS, slim chargers, or even VESCs when every millimetre is planned.[^forol_walkthrough]
- **Ninebot GT2 / Max G2 race builds** – Teams now pursue 26 S8 P P42A layouts feeding Tronic X12s; success hinges on clamping dual Ubox controllers to aluminum and retuning wheel diameter/kv for the higher voltage.[^100]
- **Nami “hotdog” racers** – 22 S11 P P45 builds pair 100 H rear / 70 H front motors, 500 A phase, 550 A absolute, and 100 % front FW to sync wheel speed, netting 146 km/h GPS with manageable 61 °C stator temps.[^4]
- **VSETT 10+ deck with external controllers** – Relocating controllers outside the deck makes room for a 20 S9 P Samsung 48X pack with ~2 mm side clearance in a 169 mm jig; builders pair it with JK active-balancing BMS boards, waterproof Higo/Julet harnesses, pre-welded copper-clad bus tabs (~$170 shipped), and QS8 anti-spark mains that tuck into copper-reinforced “W” busbars before the lid rises on PVC/acrylic spacers.[^101][^102][^103]
- **Long-term upgrade debates** – Riders weighing 30 S6 P Max conversions and 65H hubs in 11″ frames found that minor swingarm milling plus shims make oversized stators feasible if battery and controller volume are planned early.[^104]
- **Segway C80 retrofits** – Noname’s walkthrough fits a 32 P Samsung 35E pack by cutting the plastic trunk into four 6×10 cell layers, massaging corners, trimming the battery box, and notching the upper shock bracket just enough to keep the exterior plastics intact while using the ≈165 mm dropout that accepts threaded 10" hubs with drum brakes and sprocket mounts.[^105]
- **Seated tourers need packaging discipline.** The same Segway-based moped now weighs ~350 lb before the rider; Noname would redo it as a lighter 32 S 20 P stack with a Seven controller to regain torque, illustrating how dense 32 P packs trade away maneuverability despite delivering ≈9.4 kWh and 70 mi of range.[^106][^107]
- **Thunder 22 S builds** – Dualtron Thunder conversions fit 22 S 11 P packs by crossing cell columns; veterans still recommend stopping at 10 P unless you’re ready for precision machining, and the latest teardown calls for documenting crossed-cell layouts, AWG10 axle limits, fork widening for 70H fronts, and BMS placement before publishing a turnkey 26 S recipe.[^108][^109]
- **Dual X12 packaging lessons** – Smart Repair’s mixed 70H rear/GT1 front project already needed AWG10 phase leads through the axle and creative BMS placement to clear a 26 S upgrade.
  - plan harness routing before committing to multi-controller layouts, and capture the crossed-cell diagrams so others don’t pinch leads in the fork.[^110][^109]
- **Noname’s 20 S 32 P moped pack** – The seated build balances ≈9.4 kWh (112 Ah) against a 350 lb curb weight; future iterations will target a lighter 32 S 20 P layout with Seven controllers for better torque, so log enclosure volume, dropout spacing (~165 mm), and weight-handling expectations before copying the stack.[^107][^111]
- **Segway moped range lessons** – The same platform’s 32 S 20 P refresh plans to redistribute weight and revisit controller selection after the current pack forces awkward lifting; keep these ergonomic notes with your packaging drawings so seated conversions remain serviceable.[^111]
- **Begode Q3 constraints** – The frame leaves minimal battery space, forcing glass-filled PETG housings and even key relocations to clear the bars when upsizing packs.[^begode_q3_pack]
- **Turnkey superbike benchmark** – Russia’s billet RTV Ultra scooter ships with dual 3Shul controllers, 26 S 64 Ah packs, 115 mm stators, and 11×PMT130 tires while quoting six-month lead times, offering a reference for premium turnkey builds.[^112]
- **Sleeper Vsett 11 packaging** – Rob Ver squeezed a 22 S 9 P (~37 Ah) pack and both controllers inside the deck by machining spacers down to the last millimetre, trading exposed hardware for stealth that dodges EU police scrutiny.[^vsett11_pack]
- **Used Max G2 baseline** – A lightly cycled Segway Max G2 battery that lived indoors provides a sanity check when buying second-hand packs for donor builds.[^maxg2_baseline]
- **VSETT 10+ deck with external controllers** – Relocating controllers outside the deck makes room for a 20 S9 P Samsung 48X pack with ~2 mm side clearance in a 169 mm jig; builders pair it with JK active-balancing BMS boards and waterproof Higo/Julet harnesses for serviceable installs.[^101][^102]
- **Cell chemistry trade-offs** – Sony VTC6A cells sag less and run cooler than Molicel P42A but cost roughly twice as much unless ordering ~10 k pieces monthly, while Samsung 30T remains the punchiest option albeit with limited capacity.[^113]
- **8–9 P performance packs** – Brief riders on how P42A and P45B deliver the best blend of discharge headroom and cycle life for 20 S builds, when Samsung 50S makes sense for fast-charging commuters, and why long-range chemistries like LG M50LT/Samsung 50E still need larger parallels if you expect sustained 300 A duty.[^p42a_brief]
- **Ninebot G30 MAX** – Builders drill and trim 3 mm ePowerFun skid plates for €25 stopgap protection, map roughly 112–120 horizontal 21700 slots (~17 S8 P) with careful copper folding, swap in custom spacers, and plan 20 S4 P-to-22 S layouts once rails are clear and pack supports printed.
  - just avoid mixing aged grey and purple LG M26 variants that upset balance.[^114][^115][^116]
- **Xiaomi Pro 2 packaging example** – Relocating the ESC lets a 13 S8 P (104-cell) pack fit with side-mounted BMS modules, highlighting the gains from asymmetrical stacking inside cramped decks.[^117]
- **Ninebot G30 MAX** – Builders drill and trim 3 mm ePowerFun skid plates for €25 stopgap protection, swap in custom spacers, plan 20 S4 P-to-22 S layouts once rails are clear, and now spec 21700 3 S booster bricks with 100 A BMS units after 18650 versions browned out at 60 A.[^114][^115][^118]
- **Xiaomi Pro 2 decks swallow 12 S 8 P.** Removing the honeycomb inserts opens space for roughly 96 cells and even dual QS8 battery leads, but tight 6 AWG bends demand careful routing to avoid abrasion.[^119]
- **Mirono’s 13 S 5 P NCR21700A core** – Rated around 15 A per cell, it launches at 50 A battery and caps near 75 A to preserve longevity while awaiting external packs for AWD expansions.[^120]
- **Stageable AWD upgrades** – Run the dual controller in single-motor mode until a 16 S 5–7 P deck pack or hybrid internal/external pairing is finished; smaller 12 S 3 P strings sag or overheat on VESC launches.[^121]
- **Split touring packs** – 15 S 10 P VTC6 arrays now span deck plus side bags under 150 A/60 A BMS limits with 8 AWG trunks, enabling heavy regen without saturating MOSFETs on long-range builds.[^122]
- **30 S prototypes (Segway/Nami/G3)** – Ausias is CNC-ing supports for 22 S10 P Nami decks, while Finn’s G3 conversion fits 30 S3 P (15 S6 P) modules after bracket cuts; 30 S4 P remains too wide without welding and enclosure surgery.[^123]
- **Fiido compact e-bikes** – Target 16 S packs with 0.2 mm copper strip reinforcement, 3D-printed spacers for 21700 cells, and upgraded motor leads; copper stiffens the busbars but needs high-power soldering gear, and riders planning 14 S8 P/5 kW hub swaps must confirm 135 mm dropouts and ≥45 mm magnet height before abandoning QS205-class hubs.[^124][^125]
- **Mega-controller projects** – Sustaining FarDriver-class 800 A continuous targets requires at least 32 P li-ion groups or high-current LiFePO₄ bricks (~60 Ah, 200 A each), so budget the volume, cooling, and weight trade-offs before chasing 160 kW marketing claims.[^126]

## Tooling, Fabrication & Thermal Management

- Budget welders rated for 0.15 mm copper rarely meet spec; proven setups rely on K-Weld or Glitter 811A plus rip-tests, nickel sandwiching, and calibrated power for 0.1 mm sheet.[^55][^56]
- Turkey-based builders validated the €25 “purple PCB” 12 V welder board when fed by a 72 Ah car battery.
  - it handles 0.2 mm nickel but still lacks the current to weld 0.15 mm copper, so plan on capacitor rigs if customs block pro welders.[^127]
- TIG-welded copper busbars remain the standard for high-current packs.
  - Paolo’s 20 S6 P P45B build is another reminder that nickel alone adds too much resistance at 300 A targets.[^8]
- 0.3 mm copper laminates waste weight and money because the weldable layer is still nickel.
  - stick with thinner copper or sandwich welding to keep resistance low without overpaying.[^128][^129]
- Keep skid plates functional: thermal paste is required before 3 mm aluminum plates materially sink heat, and fan kits need ducting rather than flush mounts to avoid recirculating hot air.[^130]
- QS8/MT60 panel mounts are mostly custom; teams CAD their own plates to keep phase and battery leads from dangling while preserving access for service loops.[^50]
- Patrick found 10 mm² mains too stiff and dropped to dual 6 mm² conductors while PuneDir mirrored his 10 P nickel so 80 A targets stay symmetric instead of reinforcing only the “red” side.[^131]
- PETG honeycomb carriers and kraftplex skeletons let packs dry-fit without glue, while 25 mm nickel “accordion” strips shorten sense leads and copper/nickel sandwich busbars keep 150 A paths compact in cramped decks.[^132][^133][^134]
- Layer plexiglass and fish paper between every series plane before heat-shrink, then route twin packs (20 S10 P + 20 S7 P) through triple XT60 harnesses when you need 150 A bursts without sacrificing insulation.[^135]
- Seal copper sandwiches after assembly or they oxidize quickly; 8 mm nickel remains the sweet spot on 18650 positive rings, and 0.2 mm copper only makes sense once 6 P strings truly see >50 A.[^136]
- Haku’s 3D-printed holders paired with wide fishpaper tape keep copper sheets off can walls and fully insulate every cell face before the final wrap.
  - use the template when building mixed-nickel/copper decks.[^137]
- Vertical 12 S 4 P–5 P 21700 stacks now stand cells on end inside Xiaomi frames with deck spacers, fish-paper wraps, and insulated trays so the aluminium chassis can’t abrade nickel tabs.
  - even 0.8 mm magnet clearances failed without the extra padding.[^138]
- EU builders are hoarding 220 mm shrink and 0.25–0.30 mm copper straps because the “thick” 13 S 5 P 21700 rental packs choke on single 8 mm nickel links; budget the wider shrink wrap and multi-strip bussing before scaling above commuter-sized modules.[^139]
- Solid 4 mm or dual 3 mm BMS leads shed less heat than long silicone runs, and connector amp tables are being revalidated after conflicting vendor claims.
  - log actual limits before committing harness designs.[^140]
- Nickel cross-section math matters: a 30.4 mm × 0.15 mm strip only nets ~4.56 mm², capping safe series current near 20 A unless you add copper busbars or thicker nickel to curb sag on 12 S commuter packs.[^141]
- Glass-fibre interlayers and glued parallels keep RePackr-balanced groups uniform in cramped decks, and kraftplex sleeves are replacing scarce fish paper without sacrificing series isolation.[^142]
- Document thermistor retrofits when adding internal sensors: heat-shrink channels and sleeved joints stop axle chafe and preserve insulation on Vsett hubs.[^143]

## Range & Touring Concepts

- Mirono’s 3D-printed deck extender packs 260 cells (≈15 S 17 P) for 120 km coastal rides and hints at 600 A peak capability.
  - treat structural reinforcement and cooling as mandatory when chasing similar capacity boosts.[^144]
- Long-haul teams are prototyping cargo trailers and 80 W folding solar panels, logging ~2 A at 36 V during daylight charging while scouting 500 km Bonn-to-coast routes; staged charging plus swappable packs keep journeys practical.[^145]
- Range logs from 12 S 4 P P42A commuter packs show 15–20 km of spirited riding burns ~40 % capacity at 40 A battery / 80 A phase, and the same low-voltage Wheelway hubs overheat quickly without embedded thermistors.
  - plan airflow or cooling before pushing current on similar builds.[^146]
- Long-distance riders still face hours-long stops: a 274 km (170.4 mi) day on the fast-charged NIU took just under 12 hours despite the 2.2 kW charger, highlighting real touring cadence.[^147]

## BMS & Protection Strategy

- ANT 470 A/1 050 A packs have latched discharge FETs after overnight charges; the community now treats ANT as requiring redundant contactors or manual disconnects and documents UV-inspection resets before declaring hardware dead.[^9]
- **Charge-only workflows** – Some Kaabo builders wire charge-only BMS leads and rely on external JK active balancers or VESC undervoltage cutoffs when deck space is scarce, pairing the setup with main-line fuses and periodic balancer sessions instead of permanent discharge FETs.[^kaabo-20s7p]
- ANT’s published 420 A ceiling leaves Halo-style 22 S 10 P race packs with limited headroom.
  - either parallel two units or accept accelerated wear when chasing 300–350 A discharge goals.[^148]
- ANT’s published 420 A ceiling leaves Halo-style 22 S 10 P race packs with limited headroom.
  - either parallel two units or accept accelerated wear when chasing 300–350 A discharge goals, because each P45B cell is still spec’d at 45 A continuous despite community attempts to pull 300 A+ through a single BMS.[^149]
- Riding big packs on charge-only protection is risky.
  - Yamal’s 20 S 10 P commuter runs an ANT board only on the charge side, and peers warned a short could torch the ESC, so document inspection intervals, discharge-side fusing, and escalation plans until a full BMS lands.[^150][^151]
- Balance behavior differs: ANT bleeds every cell simultaneously but with limited current, whereas JK hardware addresses two series groups at once, making JK preferable for large parallels needing faster equalization.[^54]
- Smart BMS trip faster than fuses: riders remind newcomers that integrated protections catch shorts far quicker than external fuses, so keep charge balancers and discharge FETs in the loop even when packs feel cramped.[^152]
- Daly 400 A frames can be revived with LLT logic boards, but the hybrids need shunt recalibration and hardened auxiliary supplies before they belong on 80‑FET, 400 A continuous experiments.
  - treat them as advanced builds rather than off-the-shelf upgrades.[^153]
- Regen spikes punish aged packs: a tired 14 S 5 P stack with 100 mΩ cells hit 8.4 V per group during 30 A front-wheel braking, threatening 56 V controllers rated only 60 V.
  - either limit regen near 15 A, add parallels, or retire high-impedance cells.[^154]
- Denis still caps Happy BMS builds around 53 V/40 A and leans on refurbished OEM Xiaomi packs when AliExpress “fire emoji” bricks show laptop-pull cells.
  - plan range with externals instead of forcing Rita or Happy beyond spec.[^155][^156]
- High-speed racers now log ANT 300 A BMS trips near 690 A phase / 160 A battery peaks above 130 km/h, so extend delay timers or upgrade hardware before chasing similar pulls.[^157]
- Keep cost spreadsheets realistic: even DIY 20 S packs need €50 BMS units, €50–200 welders, insulation, and shipping cushions.
  - budget builders increasingly hire trusted pack shops when customs make single builds uneconomical.[^10]
- JK hardware has already saved builds from abuse.
  - Noname tripped a 60 A JK BMS by pulling 70 A battery on a C80 conversion and now plans a 20 S 3 P pack instead of bypassing protection.[^158]
- JKBMS’s compact 17 S active-balancing board (≈10 × 8 × 1.7 cm) handles 60 A continuous/100 A burst while redistributing 600 mA per channel, offering smarter balancing than passive Daly units in tight decks.[^159]
- Tape balance looms in place while routing and keep the JST plugged in; Jason notes a mispinned lead usually just keeps the BMS off until corrected, making the workflow forgiving when documented properly.[^160]
- Always land B− before the balance taps on ANT/JBD harnesses.
  - builders fried boards by skipping the ground reference while stepping up cell voltages.[^161]
- Artem’s active-balancing platform shuttles up to 600 mA once any group drifts beyond 0.01 V, clamps charge above 4.22 V, and keeps deviations near 3–7 mV.
  - document those thresholds alongside charger guidance so field techs can validate behaviour during service calls.[^162]
- Daly smart BMS displays still win on UI but ignore remote power-off requests; keep an external antispark inline and be ready to reset latched MOSFETs via the Bluetooth app after deep sags or regen spikes.[^163][^164]
- Artem’s latest 14 S pack hides dual 3 mm copper busbars under layered insulation and demands a 5 V pre-charge before plugging in the SIM-enabled BMS harness.
  - write that activation order into build docs so installers don’t arc balance leads or latch MOSFETs during bring-up.[^165]
- Oversized JBD smart BMS units may force silicone isolation around outputs and custom deck spacers.
  - budget thickness for screw heads and heatsinks, not just PCB height.[^166]
- Patrick’s main JBD app respects the phone’s language and enforces a 15 mV minimum balance delta unless you disable “softlock” via the admin app or switch to English.
  - document that quirk for field techs.[^167]
- Calibrate clone ESC shunts with a bench supply and Ohm’s law; PuneDir’s €25 board measured 280 A stock and needed a ~25 A target to match realistic pack limits, and standard multimeters won’t resolve the milliohm resistor without load.[^168]
- Stock GX16-3 charge inlets only stay cool around 3 A because the internal JST pigtail overheats; either parallel pins on a GX16-4 for 6–8 A service or swap to XT30 leads with 16–18 AWG silicone wire before raising charge current.[^169]
- Builders weighing upgrades now swap fragile GX16 charge ports for IP67 Cnlinko LP16 connectors, while others keep XT60s for ~20 A duty when weather sealing is less critical.[^170]
- Heavy fast-chargers who push 15–25 A into dual GX16 ports accept accelerated wear and check connector temps mid-charge, whereas commuters favour 0.2–0.3 C overnight balancing for pack longevity.[^171]
- Budget “smart” BMS boards remain a packaging trade-off.
  - the latest no-name unit was twice the size of an ANT despite lower amp ratings, while a 21 S 100 A JBD still fit between 18650 rows for €45 during an AliExpress sale.[^172]
- Budget 5 A “travel” chargers that never leave constant-current mode have held 4.3–4.4 A into full packs with no CV taper.
  - treat them as emergency bricks only and invest in adjustable YZPower-style supplies for daily use.[^173][^174]

## Refurbishment & Secondhand Pack QA

- Rebuilt packs that swing wildly on a 2 A charger point to poor grouping.
  - tear them down, capacity/IR-test each cell, regroup by mileage rather than labeled amp-hours, and expect marginal cells to keep worsening even after balancing.[^175]

## Charging & Maintenance Heuristics

- Per-cell fast-charge math matters: Sony VTC6A groups tolerate roughly 9 A per cell (~63 A on 7 P), Samsung 40T owners eye 0.5 C ceilings around 6×35 A for 6 P packs, and builders cap bulk charging near 30 A even when datasheets hint higher rates.[^176]
- Oversized copper busbar packs have comfortably accepted 1.5 kW lunch-break charges, taking a 20 S Sur-Ron battery from ~40 % to 90 % while keeping 260-cell layouts near 18–19 A per group.[^177]
- Keep periodic balance cycles on the calendar.
  - packs left idle for two months drifted out of balance, and moisture ingress soaked a parallel group on a 30 S build, demanding inspections after rain before hammering high-power tunes again.[^178]
- Document J1772 adapter harness wiring when planning road-trip charging: one field build used 12 AWG silicone plus 2.5 mm² leads feeding XT60 + AC outlets and required 2.74 kΩ/1.3 kΩ pilot resistors for public-station handshakes.[^179]
- Budget adjustable 22 S/18 A supplies or multi-voltage 16–24 S/20 A chargers when premium 21 S bricks are sold out, and pair them with ANT BMS sleep timers so dormant packs don’t drift after a month offline.[^180]
- Cap fast-charging on 10 P Samsung 40T commuter packs around 20 A (~1.6 kW); experienced builders call 50 A sessions abusive for both the cells and typical household circuits despite the 60 A discharge rating.[^181]
- PuneDir’s crew is now stockpiling 200 A JK smart BMS units for upcoming high-power packs, leaning into oversized protection hardware as current goals climb.[^182]
- A VESC-swapped NIU NQi is already taking ~33 A/67 V (≈2.2 kW) through its 28 P pack—about 1.17 A per cell—before the owner adds a second charger.[^183]
- A 90 Ah touring pack drawing 33 A (~0.37 C) sparked debate; veterans still cap 12 P packs near 0.1 C despite higher datasheet ratings to preserve cycle life.[^184]
- 95 A EV charger demos look impressive, but a 20 S6 P pack already draws ~6.3 kW at that rate.
  - treat 1 C as the ceiling and watch cell temps if you experiment beyond it.[^185]
- Talk of “40 C” fast charging translates to ~11 kW on a 20 S6 P pack.
  - well beyond typical 10 A household circuits
  - so XA3-class cells still need industrial infrastructure for minute-long fills.[^186]
- Telecom-derived chargers (Huawei 60 A bricks around US$340 or touchscreen 50 A models near US$260) remain repackaged rectifiers.
  - verify cooling, isolation, and safety claims instead of trusting the marketing gloss.[^187]
- Beware AliExpress “chargers” that are actually constant-current supplies with no CV taper or cutoff.
  - leaving them unattended risks overcharging overnight.[^188]
- Treat telecom 100 V bench supplies as bare rectifiers until you add earth bonding and precharge.
  - the community now grounds the chassis and energises AC before connecting packs to avoid arcs and tingling housings.[^189]
- Nudging Xiaomi/Ninebot chargers toward 61.5 V via trim pots demands upgraded output capacitors and manual cut-off monitoring; these CC bricks never stop automatically at the higher voltage.[^190]
- Skip generic DC bench supplies as primary chargers—they lack CV taper and balancing finesse, so packs leave unbalanced and age faster.[^191]

## Structural & Safety Fundamentals

- Moisture checks matter: Jason traced a persistent imbalance in his 30 S pack to water ingress, reinforcing that waterproofing reviews follow every wet ride before the next high-power outing.[^192]
- Validate copper cross-sections before final assembly: Jason’s copper “sandwich” links focus roughly 150 A through a narrow junction, so he’s running PCB-trace math before signing off on the design.
  - do the same whenever you compress high-current buses into compact plates.[^193]
- Never rely on hot glue alone; use 3D-printed spacers or structural adhesives so weld strips don’t carry mechanical load during transport or crashes.[^194]
- Wrap each 21700 in shrink plus Kapton, slip wax/fish-paper between parallels, sheath the finished block in epoxy board and heavy heat-shrink, and add a cradle strap so 20 S9 P assemblies slide in and out without chafing the deck.[^195]
- Shield mixed-metal busbars from air: copper-nickel “sandwich” tabs crack when exposed, so either seal joints with tin interfaces or revert to pure nickel when Sunko-grade welders can’t penetrate copper reliably.[^196]
- Keep communal CAD libraries handy.
  - drops like the Fusion 360 SurRon frame model let teams validate 20 S pack packaging and bolt-on brackets digitally before committing to metalwork.[^197]
- **ANT BMS app access.** iPhone users can grab the ANT companion directly from Apple’s App Store, so friends can configure packs without sideloading tools.[^198]
- PETG holders printed at 100 % infill have proven resilient for compact Xiaomi frames.
  - builders size cavities to 21.4 mm for P42A versus 21.15 mm for 40P cells and rely on PETG’s flex to survive heat cycles without cracking.[^199]
- Treat pouch experiments cautiously.
  - unlike cylindrical cells that usually fail open, pouches need constant compression and can vent violently if overcharged, so reserve them for builders with proper fixtures and monitoring.[^27]
- AliExpress “bargain” packs keep arriving with laptop pulls and fake ratings; the workshop bins them immediately and redirects budgets toward refurbished OEM cores or fresh externals instead of risking thermal events inside the deck.[^155]
- Preheat winter packs intentionally.
  - charging 20 S systems at 35–40 A up to 84 V soaks cells to ~45 °C and keeps voltage sag predictable when the ride starts in freezing conditions.[^200]
- Honeycomb cell holders add roughly 3 cm to a 20 S stick because of their 1.5 mm walls; inspect for shipping damage (crushed shrink, stray shavings) before sealing packs that rely on the extra spacing.[^201]
- Builders debating hot-glue compression versus honeycomb cages keep the modular holders for serviceability even when 75200 installs crave every millimetre.
  - plan deck layouts around the added height rather than sacrificing repair access.[^202]
- Plan per-cell discharge ceilings around chemistry limits: LG M50LT packs sag badly above ≈15 A, 35E commuters stay near 7 A per cell, P42A’s 45 A claim is really a five-second burst spec, and Samsung MH1 cells with 30–36 mΩ IR should be reserved for low-amp duty unless you can source 12 mΩ-class Aspilsan alternatives.
  - set controller limits accordingly to preserve longevity.[^203][^204]
- Disconnect chargers before any welding or pack rework.
  - one builder instantly killed an 80 ¢ charger by working on energized leads, reinforcing the “depower first” rule even on low-cost supplies.[^204]
- Screen “Panasonic” or similar branded packs by weight and weld quality; the group traced range loss and voltage sag to counterfeit cells bundled with 3Shul C700 motors and now treats suspect modules as unsafe for high-speed builds.[^205]
- Match chemistries inside parallels: mixing pouch and cylindrical cells accelerates swelling even when copper busbars handle 350 A/450 A bursts, so spec unified cells or larger BMS hardware (≈230 A) before blending formats.[^38]
- When soldering balance leads onto copper-clad packs, touch the joint for ~0.5 s at 400 °C.
  - the copper acts as a heatsink and avoids warming cells compared with nickel-only tabs.[^206]
- Resist blending similar-looking 18650 lines: pairing LG MJ1 with MH1 cells in the same parallel string drags voltage once currents exceed ~8 A per cell and undermines 130 A pack targets, so keep parallel groups chemistry-matched.[^207]
- Scrap any pierced cell immediately—builders warned that compromised cans trigger cascading failures if reused in high-current packs.[^208]
- Honeycomb fish paper layouts let Xiaomi Pro 2 riders squeeze 20 S5 P internally without spacers, but the group still demands meticulous insulation and limits bag batteries to about 20 S6 P unless you accept risky 7 P stacks.[^209]
- Salvaged vape cells arrived wildly imbalanced with unknown provenance; even hobbyists labeled them “pocket-size cancer,” reinforcing the advice to avoid disposable cells in serious builds.[^210]
- Verify “pure nickel” claims.
  - many AliExpress listings hide nickel-plated steel
  - leave vent paths open with 8 mm strip on 18650 positives, and avoid potted packs without gas gaps.[^211]
- Mixing LG 40T and LG M50LT strings in parallel demands conservative current draw and a smart 150 A BMS so the weaker chemistry doesn’t overheat or drift out of balance.[^212]
- Treat glossy spec sheets skeptically: Dualtron 7260R “60 Ah” packs tear down to SK-made 57 Ah pouches rated ≈300 A continuous per cell, and owners warn the labeling gymnastics complicate warranty claims.
  - log actual capacity before mirroring the architecture or promising the marketing numbers.[^213]
- Don’t trust “20 kg, 150 km range” marketing.
  - community math shows 150 km alone demands ~11 kg of cells plus structure, so vet vendor specs before redesigning decks around unrealistic claims.[^214]
- Vet “used but tested” Samsung 35E/40T lots for weld scars and elevated IR.
  - community buyers now skip the €2.5–€3 pulls unless sellers document low cycle counts and clean tabs.[^215]
- Treat Nordbot “premium” packs with suspicion.
  - community photos showed rewrapped Sanyo cells, exposed bus bars, and flimsy insulation that suggest recycled or stolen modules.[^216]
- Schedule periodic UV/visual inspections for burned traces on smart BMS boards, especially after preload-failure alarms or unexplained current draw.[^217]
- Use small insulating pads instead of full foam blocks when cradling deck packs so heat can escape; the crew told Cihan to damp rattles without blanketing the battery in thermal insulation.[^218]
- Wrap 8 P sticks with clear 160 mm shrink plus kraft paper so inspection windows stay visible, and rely on XTAR VC8 analyzers over budget LittoKala testers when validating reclaimed 21700 lots.[^219]
- Keep 120 mm shrink on hand for stock Xiaomi packs and 170 mm sleeves for Wildman-bag externals; Denis caps Xiaomi ESCs around 55 A phase/30 A battery even with thicker wrap to stay inside hardware limits.[^220]
- Treat Kapton as a moisture barrier, not primary insulation.
  - high-discharge packs still need fish paper or other thermal shields, and Dualtron Ultra teardowns exposed nickel touching bare cans where insulation was missing entirely.[^221]
- Budget pack shops that lean on silicone blobs and Kapton once threaded inserts strip leave balance leads exposed; veterans insist on rigid spacers, fish paper under every BMS, and thicker mains to avoid the “fire starter” XT30 failures seen in teardown photos.[^222][^223]
- Printable trays are evolving beyond scooters.
  - Pandalgns’ 10 S6 P triangular bike pack clamps nickel between bolted columns, adds removable covers for balance taps, and integrates a dedicated BMS base with mesh protection for tight commuter frames.[^224]
- Sleeper commuters are iterating thicker 20 S cell-holder prints to hide ~600 Wh in “250 W” frames.
  - Haku’s downloaded Xiaomi fixtures proved too thin, so he and GABE are reinforcing walls while Pandalgns models a beefier 20 S8 P cage for daily abuse.[^224]
- GABE’s attempt to solder nickel straight to cells triggered another reminder to avoid the hack.
  - light sanding is a last resort
  - and Jerome now outsources welding to a 24 kW capacitor rig after trashing two overheated packs, underscoring the risk of DIY copper work without serious gear.[^225]
- Welding debates from the same thread stressed that ≈1 kA pulse capability and enough voltage to overcome joint resistance matter more than headline kW ratings when joining steel or copper buswork.[^226]
- Noname proved a shared 9 × 12 in heatsink can host dual VESCs with minimal thermal-paste loss provided you budget deck space; later he kept a single controller near 40 °C at 6 kW with pads, paste, and planned ram-air ducting while Haku’s setup still peaked around 70 °C.
  - use their logs as controller cooling benchmarks during pack planning.[^227][^228]
- Mirono now refuses to build small packs without honeycomb cages or holders; sanding Xiaomi frame rails and adding rubber liners keeps 12 S 4 P 21700 packs plus VESC looms from chafing against the aluminium tray.[^229]
- A mishandled Mirono pack shows why retention hardware matters.
  - deck rails wore through fish paper, Kapton, and shrink when the battery slid loosely, so add foam blocks or brackets and photograph deliveries to document condition.[^mirono-chafe]
- Courier builds that rip through antisparks now bed connectors in silicone and jump to 8 mm bullets once M3 threads strip.
  - plan mechanical reinforcement alongside electrical upgrades so high-current harnesses survive daily swaps.[^230][^231]
- QS8 anti-spark plugs are replacing AS150 on 100 A+ scooters thanks to their 110 A continuous rating and the new 6 AWG solder cups, which pair cleanly with 6 mm² phase looms when dual controllers climb past 60 A battery per side.
  - even if EU pricing still hovers around CHF 21.50 per pair.[^232]
- When paralleling extender packs, match voltages before connecting, use XT90/Y harnesses on common-port BMS designs, and let multiple chargers share the constant-voltage stage so each supply tapers naturally as the packs equalise.[^233]
- QS8 connectors handle roughly 70 A continuous but take valuable deck space; many riders now substitute 8 mm bullets for compact high-current runs while keeping XT90S on sub-45 A projects.[^234]

## Build Checklist

1. **Lock in cell supply** – confirm volume, customs path, and aging tests for each batch of 50PL/50E/P45B cells before welding.[^235][^10]
2. **Spec welding & busbars** – validate welder output on scrap strips, target 0.1–0.2 mm copper, and document Glitter/K-Weld maintenance steps for the build log.[^55][^56]
3. **Mock the enclosure** – dry-fit spacers, skid plates, and controller mounts to prove 22 S9 P–30 S3 P geometries before live welding.
  - PuneDir’s steel box missed the Hyosung frame opening by 1 cm, stranding the build until a new shell was cut.[^2][^3][^236]
4. **Layer protection** – choose BMS hardware with known reset workflows, add external fuses/contactors, and rehearse ANT fault recovery with UV inspection gear.[^9][^54]
5. **Secure the pack** – replace hot glue with interlocking supports, torque QS8/MT60 mounts, and apply thermal paste before final enclosure torque-down.[^130][^194][^50]
6. **Stage controller, pack, then motor upgrades** – High-voltage conversions show the biggest ride gains after upgrading the VESC, then the battery, and only then the hub; even modest motors tolerate 3–4× nameplate power once cooling is sorted.[^237]
6. **Prep service harnesses** – pre-soldered AS150 leads now ship with 8 AWG mains and four 24 AWG signal wires, making 70 A quick-disconnects trivial.
  - stock spares and document polarity before field installs.[^238]

## Source Notes

[^1]: Battery cost, cell sourcing, and spot-welder economics from late-2025 VESC Help Group logs.[^239][^10]
[^2]: Pack layout, chassis fitment, and race-build current benchmarks documented in the same log slice.[^2][^240]
[^3]: Smart BMS fault reports, balance behavior comparisons, and safety guidance against hot-glue-only assemblies.[^9][^11]
[^4]: Additional Ninebot/N65 packaging lessons, nickel sourcing, copper fabrication requirements, and stock-pack limitations gathered from the input_part006 review.[^241][^242][^243]
[^nkon-40t]: NKON shoppers favour Molicel 40T for ≈100 A builds, keep LG M50LT as a tentative backup pending high-current tests, and lean on LG MH1 for budget ebike packs around €1.70 per cell.[^244]
[^kaabo-20s7p]: Kaabo Wolf owners mapped 160 × 470 × 75 mm decks for 20 S7 P packs, weighed charge-only harnesses plus detachable JK balancers against flat ANT/JK boards, and highlighted the ≈150 A balancing capability of the slim smart units.[^245]
[^mirono-chafe]: Mirono’s inspection showed loose packs sliding against deck rails can chew through fish paper, Kapton, and shrink, reinforcing the need for foam blocks, brackets, and delivery photos when shipping builds.[^246]


## References

[^1]: Source: knowledge/notes/input_part014_review.md†L34-L38
[^2]: Source: knowledge/notes/input_part014_review.md†L37-L45
[^3]: Source: knowledge/notes/input_part014_review.md†L151-L160
[^4]: Source: knowledge/notes/input_part014_review.md†L168-L169
[^5]: Source: knowledge/notes/input_part008_review.md†L402-L408
[^6]: Source: knowledge/notes/input_part006_review.md†L102-L102
[^7]: Source: knowledge/notes/input_part008_review.md†L16198-L16266
[^8]: Source: knowledge/notes/input_part008_review.md†L20698-L20700
[^9]: Source: knowledge/notes/input_part014_review.md†L99-L101
[^10]: Source: knowledge/notes/input_part014_review.md†L155-L156
[^11]: Source: knowledge/notes/input_part014_review.md†L172-L174
[^12]: Source: knowledge/notes/input_part000_review.md†L601-L602
[^13]: Source: data/vesc_help_group/text_slices/input_part002.txt†L8972-L8985
[^14]: Source: data/vesc_help_group/text_slices/input_part002.txt†L8992-L9016
[^15]: Source: data/vesc_help_group/text_slices/input_part002.txt†L8830-L8854
[^16]: Source: knowledge/notes/input_part002_review.md†L446-L465
[^17]: Source: knowledge/notes/input_part000_review.md†L224-L225
[^18]: Source: knowledge/notes/input_part013_review.md†L201-L201
[^19]: Source: knowledge/notes/input_part000_review.md†L309-L311
[^20]: Source: knowledge/notes/input_part000_review.md†L310-L311
[^21]: Source: knowledge/notes/input_part013_review.md†L523-L524
[^22]: Source: knowledge/notes/input_part003_review.md†L121-L121
[^23]: Source: knowledge/notes/input_part004_review.md†L236-L236
[^24]: Source: knowledge/notes/input_part005_review.md†L344-L345
[^25]: Source: data/vesc_help_group/text_slices/input_part010.txt†L9039-L9093
[^26]: Source: data/vesc_help_group/text_slices/input_part013.txt†L5661-L5666
[^27]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L97241-L97259
[^28]: Source: knowledge/notes/denis_all_part02_review.md†L76-L77
[^29]: Source: knowledge/notes/denis_all_part02_review.md†L407-L407
[^30]: Source: knowledge/notes/input_part014_review.md†L35-L36
[^31]: Source: knowledge/notes/input_part014_review.md†L36-L38
[^32]: Source: data/vesc_help_group/text_slices/input_part001.txt†L25083-L25095
[^33]: Source: data/vesc_help_group/text_slices/input_part001.txt†L25101-L25145
[^34]: Source: knowledge/notes/input_part000_review.md†L274-L274
[^35]: Source: knowledge/notes/input_part000_review.md†L151-L151
[^36]: Source: knowledge/notes/input_part000_review.md†L317-L317
[^37]: Source: knowledge/notes/input_part014_review.md†L37-L39
[^38]: Source: knowledge/notes/input_part014_review.md†L39-L39
[^39]: Source: knowledge/notes/input_part014_review.md†L156-L156
[^40]: Source: data/vesc_help_group/text_slices/input_part001.txt†L9085-L9299
[^41]: Source: knowledge/notes/input_part002_review.md†L145-L146
[^42]: Source: knowledge/notes/input_part002_review.md†L146-L147
[^43]: Source: knowledge/notes/input_part002_review.md†L170-L172
[^44]: Source: knowledge/notes/input_part008_review.md†L499-L500
[^45]: Source: knowledge/notes/input_part006_review.md†L275-L275
[^46]: Source: knowledge/notes/input_part006_review.md†L278-L278
[^47]: Source: knowledge/notes/input_part008_review.md†L357-L363
[^48]: Source: knowledge/notes/input_part008_review.md†L15885-L15938
[^49]: Source: knowledge/notes/input_part008_review.md†L19028-L19052
[^50]: Source: knowledge/notes/input_part014_review.md†L188-L188
[^51]: Source: knowledge/notes/input_part014_review.md†L38-L38
[^52]: Source: knowledge/notes/input_part006_review.md†L435-L435
[^53]: Source: knowledge/notes/input_part014_review.md†L155-L155
[^54]: Source: knowledge/notes/input_part014_review.md†L174-L174
[^55]: Source: knowledge/notes/input_part014_review.md†L34-L34
[^56]: Source: knowledge/notes/input_part014_review.md†L152-L152
[^57]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11188-L11209
[^58]: Source: knowledge/notes/input_part006_review.md†L437-L437
[^59]: Source: knowledge/notes/input_part008_review.md†L132-L132
[^60]: Source: knowledge/notes/input_part008_review.md†L133-L133
[^61]: Source: knowledge/notes/input_part008_review.md†L147-L147
[^62]: Source: knowledge/notes/input_part008_review.md†L148-L148
[^63]: Source: knowledge/notes/input_part013_review.md†L339-L344
[^64]: Source: knowledge/notes/input_part013_review.md†L344-L350
[^65]: Source: knowledge/notes/input_part013_review.md†L348-L357
[^66]: Source: knowledge/notes/input_part013_review.md†L357-L362
[^67]: Source: data/vesc_help_group/text_slices/input_part011.txt†L19303-L19306
[^68]: Source: knowledge/notes/input_part011_review.md†L521-L522
[^69]: Source: knowledge/notes/input_part012_review.md†L122-L123
[^70]: Source: knowledge/notes/input_part014_review.md†L37-L44
[^71]: Source: data/vesc_help_group/text_slices/input_part002.txt†L4757-L4799
[^72]: Source: data/vesc_help_group/text_slices/input_part002.txt†L4813-L4857
[^73]: Source: knowledge/notes/input_part008_review.md†L108-L108
[^74]: Source: knowledge/notes/input_part008_review.md†L231-L233
[^75]: Source: knowledge/notes/input_part008_review.md†L14765-L14807
[^76]: Source: knowledge/notes/input_part005_review.md†L231-L232
[^77]: Source: knowledge/notes/input_part005_review.md†L320-L324
[^78]: Source: knowledge/notes/input_part005_review.md†L296-L297
[^79]: Source: knowledge/notes/input_part006_review.md†L27-L27
[^80]: Source: knowledge/notes/input_part006_review.md†L436-L436
[^81]: Source: knowledge/notes/input_part006_review.md†L103-L103
[^82]: Source: knowledge/notes/input_part006_review.md†L141-L141
[^83]: Source: knowledge/notes/input_part006_review.md†L309-L309
[^84]: Source: knowledge/notes/input_part006_review.md†L85-L85
[^85]: Source: knowledge/notes/input_part010_review.md†L324-L325
[^86]: Source: data/vesc_help_group/text_slices/input_part010.txt†L18727-L18741
[^87]: Source: data/vesc_help_group/text_slices/input_part010.txt†L19893-L20028
[^88]: Source: data/vesc_help_group/text_slices/input_part010.txt†L19921-L19942
[^89]: Source: knowledge/notes/input_part013_review.md†L223-L223
[^90]: Source: data/vesc_help_group/text_slices/input_part013.txt†L17621-L17635
[^91]: Source: data/vesc_help_group/text_slices/input_part013.txt†L6065-L6200
[^92]: Source: knowledge/notes/input_part013_review.md†L119-L119
[^93]: Source: knowledge/notes/input_part013_review.md†L204-L204
[^94]: Source: knowledge/notes/input_part013_review.md†L120-L121
[^95]: Source: knowledge/notes/input_part013_review.md†L122-L122
[^96]: Source: knowledge/notes/input_part013_review.md†L123-L123
[^97]: Source: knowledge/notes/input_part013_review.md†L124-L124
[^98]: Source: knowledge/notes/input_part013_review.md†L145-L145
[^99]: Source: knowledge/notes/input_part013_review.md†L269-L269
[^100]: Source: knowledge/notes/input_part008_review.md†L312-L315
[^101]: Source: data/vesc_help_group/text_slices/input_part001.txt†L6371-L6486
[^102]: Source: data/vesc_help_group/text_slices/input_part001.txt†L6501-L6504
[^103]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8851-L8913
[^104]: Source: knowledge/notes/input_part012_review.md†L161-L161
[^105]: Source: knowledge/notes/input_part012_review.md†L288-L295
[^106]: Source: knowledge/notes/input_part012_review.md†L333-L336
[^107]: Source: knowledge/notes/input_part012_review.md†L312-L316
[^108]: Source: knowledge/notes/input_part012_review.md†L189-L189
[^109]: Source: knowledge/notes/input_part012_review.md†L304-L304
[^110]: Source: knowledge/notes/input_part012_review.md†L190-L190
[^111]: Source: knowledge/notes/input_part012_review.md†L322-L323
[^112]: Source: knowledge/notes/input_part012_review.md†L191-L191
[^113]: Source: data/vesc_help_group/text_slices/input_part001.txt†L1603-L1655
[^p42a_brief]: Cell-selection TODO capturing P42A/P45B vs. Samsung 50S and LG/Samsung long-range chemistries for 8–9 P scooter packs, including when premium cells justify cost versus leaning on faster charging. Source: data/vesc_help_group/text_slices/input_part005.txt†L24420-L24451.
[^114]: Source: knowledge/notes/input_part014_review.md†L151-L151
[^115]: Source: knowledge/notes/input_part014_review.md†L118-L118
[^116]: Source: knowledge/notes/input_part008_review.md†L184-L184
[^117]: Source: knowledge/notes/input_part008_review.md†L109-L109
[^118]: Source: knowledge/notes/input_part000_review.md†L221-L221
[^119]: Source: knowledge/notes/input_part006_review.md†L310-L310
[^120]: Source: knowledge/notes/input_part000_review.md†L309-L310
[^121]: Source: knowledge/notes/input_part000_review.md†L309-L312
[^122]: Source: knowledge/notes/input_part000_review.md†L219-L219
[^123]: Source: knowledge/notes/input_part014_review.md†L159-L160
[^124]: Source: knowledge/notes/input_part001_review.md†L46-L48
[^125]: Source: data/vesc_help_group/text_slices/input_part001.txt†L21239-L21247
[^126]: Source: data/vesc_help_group/text_slices/input_part001.txt†L20423-L20488
[^127]: Source: knowledge/notes/input_part008_review.md†L140-L140
[^128]: Source: knowledge/notes/input_part008_review.md†L20898-L20916
[^129]: Source: knowledge/notes/input_part008_review.md†L20943-L20951
[^130]: Source: knowledge/notes/input_part014_review.md†L119-L120
[^131]: Source: knowledge/notes/input_part008_review.md†L163-L163
[^132]: Source: knowledge/notes/input_part000_review.md†L214-L216
[^133]: Source: knowledge/notes/input_part000_review.md†L220-L220
[^134]: Source: knowledge/notes/input_part000_review.md†L239-L239
[^135]: Source: knowledge/notes/input_part008_review.md†L164-L164
[^136]: Source: knowledge/notes/input_part008_review.md†L166-L166
[^137]: Source: knowledge/notes/input_part008_review.md†L167-L167
[^138]: Source: data/vesc_help_group/text_slices/input_part000.txt†L16998-L17021
[^139]: Source: knowledge/notes/input_part000_review.md†L681-L682
[^140]: Source: knowledge/notes/input_part000_review.md†L237-L237
[^141]: Source: data/vesc_help_group/text_slices/input_part000.txt†L21855-L21875
[^142]: Source: knowledge/notes/input_part000_review.md†L313-L315
[^143]: Source: knowledge/notes/input_part000_review.md†L320-L321
[^144]: Source: knowledge/notes/input_part000_review.md†L158-L158
[^145]: Source: knowledge/notes/input_part000_review.md†L159-L159
[^146]: Source: data/vesc_help_group/text_slices/input_part000.txt†L19037-L19122
[^147]: Source: knowledge/notes/input_part008_review.md†L194-L194
[^148]: Source: knowledge/notes/input_part013_review.md†L403-L405
[^149]: Source: data/vesc_help_group/text_slices/input_part013.txt†L17525-L17545
[^150]: Source: knowledge/notes/input_part013_review.md†L224-L224
[^151]: Source: knowledge/notes/input_part013_review.md†L250-L250
[^152]: Source: data/vesc_help_group/text_slices/input_part002.txt†L4868-L4888
[^153]: Source: data/vesc_help_group/text_slices/input_part003.txt†L24344-L24355
[^154]: Source: knowledge/notes/input_part005_review.md†L292-L293
[^155]: Source: knowledge/notes/denis_all_part02_review.md†L458-L459
[^156]: Source: knowledge/notes/denis_all_part02_review.md†L466-L466
[^157]: Source: data/vesc_help_group/text_slices/input_part003.txt†L25927-L26063
[^158]: Source: knowledge/notes/input_part012_review.md†L280-L285
[^159]: Source: knowledge/notes/input_part000_review.md†L270-L270
[^160]: Source: knowledge/notes/input_part008_review.md†L134-L134
[^161]: Source: knowledge/notes/input_part008_review.md†L135-L135
[^162]: Source: knowledge/notes/input_part000_review.md†L716-L723
[^163]: Source: knowledge/notes/input_part000_review.md†L315-L316
[^164]: Source: knowledge/notes/input_part000_review.md†L366-L368
[^165]: Source: data/vesc_help_group/text_slices/input_part000.txt†L18837-L18854
[^166]: Source: knowledge/notes/input_part008_review.md†L165-L165
[^167]: Source: knowledge/notes/input_part008_review.md†L170-L170
[^168]: Source: knowledge/notes/input_part008_review.md†L171-L171
[^169]: Source: data/vesc_help_group/text_slices/input_part000.txt†L21739-L21808
[^170]: Source: knowledge/notes/input_part008_review.md†L144-L144
[^171]: Source: data/vesc_help_group/text_slices/input_part000.txt†L21810-L21849
[^172]: Source: knowledge/notes/input_part008_review.md†L189-L189
[^173]: Source: knowledge/notes/input_part000_review.md†L716-L724
[^174]: Source: knowledge/notes/input_part000_review.md†L724-L731
[^175]: Source: knowledge/notes/denis_all_part02_review.md†L332-L333
[^176]: Source: data/vesc_help_group/text_slices/input_part001.txt†L9063-L9076
[^177]: Source: knowledge/notes/input_part012_review.md†L124-L124
[^178]: Source: knowledge/notes/input_part012_review.md†L160-L160
[^179]: Source: knowledge/notes/input_part012_review.md†L155-L155
[^180]: Source: knowledge/notes/input_part012_review.md†L166-L167
[^181]: Source: knowledge/notes/input_part010_review.md†L50-L52
[^182]: Source: knowledge/notes/input_part008_review.md†L273-L273
[^183]: Source: knowledge/notes/input_part008_review.md†L192-L192
[^184]: Source: knowledge/notes/input_part008_review.md†L193-L193
[^185]: Source: knowledge/notes/input_part010_review.md†L245-L246
[^186]: Source: knowledge/notes/input_part008_review.md†L142-L142
[^187]: Source: knowledge/notes/input_part010_review.md†L247-L247
[^188]: Source: data/vesc_help_group/text_slices/input_part002.txt†L2721-L2724
[^189]: Source: data/vesc_help_group/text_slices/input_part003.txt†L18612-L18636
[^190]: Source: data/vesc_help_group/text_slices/input_part003.txt†L18653-L18671
[^191]: Source: knowledge/notes/input_part008_review.md†L195-L195
[^192]: Source: knowledge/notes/input_part012_review.md†L139-L139
[^193]: Source: knowledge/notes/input_part012_review.md†L286-L288
[^194]: Source: knowledge/notes/input_part014_review.md†L172-L172
[^195]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8927-L8933
[^196]: Source: data/vesc_help_group/text_slices/input_part002.txt†L1640-L1645
[^197]: Source: data/vesc_help_group/text_slices/input_part005.txt†L22392-L22397
[^198]: Source: data/vesc_help_group/text_slices/input_part010.txt†L19869-L19873
[^199]: Source: knowledge/notes/input_part010_review.md†L23-L24
[^200]: Source: knowledge/notes/input_part003_review.md†L209-L210
[^201]: Source: knowledge/notes/input_part005_review.md†L290-L291
[^202]: Source: knowledge/notes/input_part005_review.md†L502-L503
[^203]: Source: knowledge/notes/input_part005_review.md†L340-L345
[^204]: Source: knowledge/notes/input_part005_review.md†L367-L368
[^205]: Source: knowledge/notes/input_part003_review.md†L206-L207
[^206]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8874-L8897
[^207]: Source: data/vesc_help_group/text_slices/input_part001.txt†L7100-L7125
[^208]: Source: knowledge/notes/input_part008_review.md†L180-L180
[^209]: Source: knowledge/notes/input_part008_review.md†L183-L183
[^210]: Source: knowledge/notes/input_part008_review.md†L185-L185
[^211]: Source: knowledge/notes/input_part008_review.md†L187-L187
[^212]: Source: knowledge/notes/input_part008_review.md†L188-L188
[^213]: Source: knowledge/notes/input_part014_review.md†L59-L59
[^214]: Source: data/vesc_help_group/text_slices/input_part003.txt†L25568-L25606
[^215]: Source: data/vesc_help_group/text_slices/input_part003.txt†L16250-L16267
[^216]: Source: data/vesc_help_group/text_slices/input_part001.txt†L9376-L9399
[^217]: Source: knowledge/notes/input_part014_review.md†L100-L100
[^218]: Source: knowledge/notes/input_part008_review.md†L138-L138
[^219]: Source: knowledge/notes/input_part000_review.md†L271-L273
[^220]: Source: knowledge/notes/denis_all_part02_review.md†L329-L330
[^221]: Source: knowledge/notes/denis_all_part02_review.md†L357-L359
[^222]: Source: data/vesc_help_group/text_slices/input_part000.txt†L19126-L19172
[^223]: Source: data/vesc_help_group/text_slices/input_part000.txt†L19787-L19899
[^224]: Source: data/vesc_help_group/text_slices/input_part010.txt†L10127-L10621
[^225]: Source: data/vesc_help_group/text_slices/input_part010.txt†L18743-L18766
[^226]: Source: data/vesc_help_group/text_slices/input_part010.txt†L18982-L19024
[^227]: Source: data/vesc_help_group/text_slices/input_part010.txt†L19035-L19044
[^228]: Source: data/vesc_help_group/text_slices/input_part010.txt†L20140-L20158
[^229]: Source: data/vesc_help_group/text_slices/input_part000.txt†L19913-L19947
[^230]: Source: data/vesc_help_group/text_slices/input_part000.txt†L18939-L18955
[^231]: Source: data/vesc_help_group/text_slices/input_part000.txt†L19126-L19129
[^232]: Source: data/vesc_help_group/text_slices/input_part001.txt†L10421-L10520
[^233]: Source: data/vesc_help_group/text_slices/input_part001.txt†L20518-L20539
[^234]: Source: knowledge/notes/input_part002_review.md†L208-L208
[^235]: Source: knowledge/notes/input_part014_review.md†L35-L37
[^236]: Source: knowledge/notes/input_part008_review.md†L139-L139
[^237]: Source: knowledge/notes/input_part005_review.md†L303-L304
[^238]: Source: knowledge/notes/input_part000_review.md†L272-L272
[^239]: Source: knowledge/notes/input_part014_review.md†L34-L39
[^240]: Source: knowledge/notes/input_part014_review.md†L151-L169
[^241]: Source: knowledge/notes/input_part006_review.md†L24-L26
[^242]: Source: knowledge/notes/input_part006_review.md†L48-L48
[^243]: Source: knowledge/notes/input_part006_review.md†L62-L63
[^premium-cells]: Source: knowledge/notes/input_part006_review.md†L102-L102
[^244]: Source: knowledge/notes/input_part002_review.md†L145-L147
[^245]: Source: knowledge/notes/input_part002_review.md†L148-L149
[^246]: Source: knowledge/notes/input_part002_review.md†L205-L207
[^jp40_pack]: Source: knowledge/notes/input_part012_review.md, lines 440-441.
[^vsett11_pack]: Source: knowledge/notes/input_part012_review.md, line 442.
[^g30_ceiling]: Source: knowledge/notes/input_part012_review.md, line 438.
[^maxg2_baseline]: Source: knowledge/notes/input_part012_review.md, line 443.
[^begode_q3_pack]: Source: knowledge/notes/input_part012_review.md, line 466.
[^forol_walkthrough]: Source: knowledge/notes/input_part012_review.md, line 476.
