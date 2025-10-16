# DIY Battery Sourcing & Welding Playbook (2025)

## TL;DR

- Grade-A 50PL and P45B cells now define the performance ceiling, but prices swing from €1–1.5 in the EU to ~$9 in the US, so teams must align sourcing tactics with customs realities before scoping pack power levels.[^1][^2]
- Copper spot welding remains the gating competency: bargain 90 € welders rarely prove 0.15 mm claims, while K-Weld or Glitter rigs with proper maintenance reliably join 0.1 mm copper for 22 S packs.[^3][^10]
- Mirono steers newcomers toward Docreate’s ~€100 capacitor welder and copper-under-nickel sandwiches (≈40 J for nickel, 60–70 J for copper) because LSUC-branded caps underdeliver and bare copper strips fail pull tests without a nickel cap.[^1]
- Before committing to copper busbars, Pandalgns is test-firing a €100–€120 welder at ≈0.1 s pulses to confirm it can join copper reliably—proof that bench tests should precede full 20 S10 P builds.[^welder-trials]
- Pack shops now expect reinforced printed holders and pro-grade tooling; Pandalgns is redesigning 20S8P cages after flimsy STLs failed, and Noname is pricing a $17 k laser welder to keep precision builds moving.[^stiff-holders]
- Community veterans call quality AliExpress packs a lottery—without cell provenance, they prefer building from verified cells even if Aerdu customs occasionally arrive “fine.”[^denis-ali-lottery]
- Size busbars with real cross-sectional math instead of stacking nickel.
  - triple 0.30 mm stacks still run resistive at 70 A, so teams now flip to copper once welders are dialled.[^2][^3]
- Nickel-plated steel strips remain serviceable when the welds are sealed under Kapton, fish paper, and shrink; leave plating exposed to humid decks and the steel rusts, while pure nickel keeps resistance lower if you can justify the cost.[^ip001-nickel-steel][^ip001-pure-nickel]
- When copper busbars are mandatory, plate them or hit them with zinc-rich coatings; bare copper sags less than nickel but corrodes quickly without a barrier.[^copper_plating_guard]
- Xiaomi Pro 2 and Navee conversions prove 20 S packs fit only when BMS and controllers move.
  - Gabe’s sleeper pack splits 11 S in-deck/9 S external with twin 6 AWG leads while controllers live in a 50 mm spacer and the BMS rides the stem; a 10 mm JBD board keeps Navee bays viable.[^4]
- Budget worksheets should factor in consumables, BMS headroom, and future tariff shocks (e.g., QS8 connectors drifting toward $35) to avoid mid-build redesigns when scaling beyond 300 A continuous.[^4][^5]
- One builder left boards on the hotplate briefly without visible damage, but the scare reinforced double-checking preheat routines before solder prep.
  - treat hotplate stages as live-fire operations every time.[^5]
- Samsung 50E vs. 35E debates continue: the 50E sags less but caps around 30 A on a 3 P string, global shortages hit both cells, and some branded Liitokala packs arrived with mystery “BICO” cells unfit for high-current builds.[^50e_supply]
- Seasoned welders still crown kWeld as the reliable benchmark and warn that Sunkko-style rigs barely clear 0.12 mm nickel unless you upgrade the power stage.[^denis-kweld-standard]

## Workshop Pricing & BMS Baselines

- Denis’ catalog still quotes ~€170 for a 10S4P Samsung 35E pack, €30 for the Wildman bag, and roughly €20 for EU shipping via DPD/UPS; he insists on genuine XT30 hardware and 20 A common-port BMS boards rather than AliExpress knock-offs.[^denis-pricing]
- Builders are binning cells by internal resistance with RePackr and double-checking charger calibration whenever meter readings disagree, keeping parallel groups balanced before welding.[^repackr_ir_match]
- Match BMS boards to the intended series count.
  - 12S packs need true 12S PCM/PCB hardware rated around 30 A so Rita installs do not outrun protection stages.[^6]
- Riders sourcing 15 S externals stick with common-port packs (AliExpress/Alibaba) that ship with integrated BMS hardware and budget for higher voltage alongside extra current headroom as parallels scale up.[^15s_common_port]
- Community teardown of a so-called “36 V 20 Ah” AliExpress pack revealed just 12 cells and sand filler.
  - treat round-number claims or >42 V open-circuit readings as immediate scams unless the seller proves a 10S6P layout.[^aliexpress-sand]
- Swap separate-port AliExpress BMS boards before paralleling with Rita; otherwise the discharge lead backfeeds chargers and overfills cells through the wrong path.[^7]
- Wary of flaky AliExpress “smart” boards, veterans are swapping to Daly hardware and only editing per-group internal-resistance tables after confirming wiring and cycling the pack.[^daly_swap]
- Expect honest 10S materials to cost roughly €100 before labor and tax—anything cheaper usually hides weak cells or flimsy protection hardware.[^8]
- Veterans now skip “brandless” AliExpress 18650s altogether, noting that even small external packs should budget well over €100 in quality cells and that suspiciously cheap bricks may be stuffed with sand or exhausted pulls.[^denis-brandless]
- Tudor/VTA external packs arrive with same-port BMS wiring; tie Rita’s XT30 into C-/B- and leave P- empty so charge and discharge share the protected port without bypassing the board.[^tudor-common]
- The workshop flags “fire emoji” AliExpress packs built from laptop pulls.
  - builders cap Happy BMS builds near 53 V/40 A and lean on refurbished OEM modules plus externals for range instead of forcing Rita past spec.[^ali-pack-warning-diy]
- If a smart BMS reports one parallel group drifting, verify cell authenticity and log voltages with a multimeter—bad cells are rare but easier to catch before they torch usable range.[^bms_drift_check]
- Vet cheap-pack marketing claims with lab-grade tools.
  - François leaned on a Hyperion 1420 charger, 800 W PSU, and a load bank to expose fraudulent capacity numbers, underscoring how expensive proper validation is.[^lab-gear]
- Aerdu’s inexpensive 10S packs can deliver honest capacity when properly potted, but missing fish paper between series groups remains a fire risk.
  - veterans still favour reputable cell sellers (e.g., NKON) and add insulation themselves before shipping customs builds.[^9]
- LiitoKala’s advertised 21 Ah packs recently tore down to uncertified ≈2200 mAh cells, dubious stickers, and weak QC; disappointed buyers opted back to Denis’ Samsung builds despite shipping headaches.[^liitokala_warning]
- EU paperwork and cell shortages have paused Denis’ kit shipments to the UK; NKON and other warehouses are dry, so Tudor is quoting bespoke 48 V/25 Ah builds while customers wait.[^uk_cell_shortage]
- External packs stay on common-port BMSes so Rita can police charge flow.
  - Denis refuses to ship his smart separate-port boards in range kits because they can’t stop overcharge through the discharge lead.[^common-port-chat]
- Retrofit third-party externals with 40 A UART485 common-port boards (often AliExpress kits bundled with Bluetooth dongles) so adapters can monitor and tune pack behaviour safely.[^uart485-diy]
- Among AliExpress vendors, Laudation remains one of the few delivering rated capacity—treat flashy “60 000 mAh” marketing as a red flag even when the listing looks professional.[^laudation-diy]
- Production packs come from the m365Krakow workshop; Denis handles support and logistics while the partner assembles cells, so large orders should plan around their combined lead times.[^m365krakow]
- Denis’ repair BMS defaults to ≈4.15 V/cell (≈4.14 V after its diode drop) yet lets riders raise or lower the ceiling to trade longevity for range; bench tests logged ≈37 A discharge headroom when paralleled with another 10S pack despite the older board’s 3 A charge limit.[^10]
- Import math still favours regional resellers: EU buyers report ~$40 shipping plus ≈€20 customs per motor with multi-week waits from China, so Kroxne/VTA stock often wins despite higher sticker prices.[^import_math]
- LLT’s 100 A smart boards remain the viable option for 4 S boosters.
  - cheaper BMSes brown out, and pushing Flipsky 75100 boxes to 20 S simply moves failure to the wiring long before the ESC runs out of headroom.[^11]
- JK active-balancing boards keep outrunning Daly units on telemetry and balancing strength; builders now reserve Daly for budget builds and spec JK or LLT when 20 S packs need reliable comms and cell maintenance.[^12]
- Daly’s 100Balance smart board can still support serious builds.
  - Jerome’s 20 S 9 P EVE 40P pack pairs it with 0.2 mm copper busbars and keeps GT2 motors around 7–10 kW continuous before heat becomes the limit.[^13]
- ANT smart BMS packs ship with a “starting current” precharge MOSFET; run it around 5 A for spark-free bring-up and keep it below 20 A or the firmware times out if bus caps never charge.[^14]
- **Match gauge charts carefully.** Builders keep confusing conductor diameter with cross-sectional area.
  - Smart Repair reminds shops that dual 14 AWG runs roughly equal an 11 AWG cross-section, so convert using area tables before sizing harness upgrades.[^15]
- **Pick the right welding process.** Halo deck and Nami frame repairs favour TIG work or professional shops; budget MIG rigs spatter excessively and stick welders simply cannot penetrate scooter aluminium without compromising strength.[^16][^17]
- **Size soldering irons for busbar work.** High-current harnesses solder cleanly with 200–300 W handheld irons or 350 W “3 kg” stations proven on QS8 connectors.
  - tiny 65 W wands only cope if you overdrive them, which risks cold joints and melted insulation.[^18]
- Practice high-current soldering on scrap first: Denis’ crew leans on ≥60 W irons, rosin-core solder, disciplined flux cleanup, and heavy bullet/banana connectors to avoid melting insulation or leaving cold joints when upgrading phase leads.[^denis-highcurrent-solder]
- Desolder nickel before prying welded brackets off recycled packs so you don’t tear cell tabs during teardown.[^denis-desolder]

## Cell Market Benchmarks

- Artem still steers 25 A-per-cell builds toward P42A-class chemistries, treats Samsung 48X as only a mild upgrade over 50G, highlights Samsung M50LT Gen 2 for 0–15 A commuters, and notes 20 S9 P Samsung 48X packs landing around $5.75 per cell delivered from Canada with 40–80 mile range potential.[^artem_cells][^pack_48x_cost]

| Source | Typical Price & Availability | Verified Performance | Procurement Notes |
| --- | --- | --- | --- |
| **Stark Varg salvage modules (50PL)** | ≈€1–1.2 per cell after labor in Europe | Bench-tested at 60 A discharge / 15 A charge with tight variance | Requires teardown expertise, cycle-life verification, and logistics for pallet shipments before trusting the pulls in customer packs.[^1][^varg-salvage] |
| **NKON / EU wholesalers (50PL)** | €1.5 per cell retail; logos often milled off | Verified as grade A despite shaved markings | Maintain purchase records to satisfy customs queries about rebranded stock.[^2] |
| **US resellers (50PL)** | ~$9 per cell | Same performance as EU stock | Factor in tariffs and shipping; consider freight-forwarding via EU partners.[^2] |
| **Custom P45B/P50B packs** | €3000–€4500 for 22 S 10 P/11 P assemblies | Continuous ≈495 A, BMS peaks ≈1040 A | Group buys enable supply; document BMS limits (≤500 A continuous today).[^6][^7] |
| **Samsung 6A & Lishen LR21700 12A** | Community-grade pulls, availability fluctuates | Regarded as “plenty” for Blade motors; LR2170LA variants have survived repeated >3 C draws in field use | Line up supply before retiring MH1/MG1 spares, budget for thicker harness routing, and expect to replace saggy LG M26 20 S 20 P concepts with higher-discharge 21700s to keep QS-class motors fed.[^19][^20] |
| **EVE 40PL factory-direct** | ≈$4.35 per cell (≥50 unit MOQ) plus freight/taxes | High-power cells shipping direct from the factory | Savings disappear without true bulk orders.
  - budget duties and shipping before chasing the discount.[^21] |
| **Commissioned builds (UK/US)** | Varies; premium vs DIY delta covers tooling | Output tied to builder’s QC logs | Trusted builders like jamessoderstrom eliminate tooling spend for one-off packs.[^11] |
| **BAK 2.5 Ah 20 A cells** | Budget-friendly yet capacity-limited options for dual 20 S packs (~17.5 Ah per half) | Continuous output around 40 A per pack; expect steep voltage sag at 100 A draws | Plan parallel 8 AWG-equivalent leads and set range expectations realistically.[^22] |

### Chemistry Trade-Off Snapshots

- Denis still leans on LG MJ1, Samsung 35E, and Sanyo energy cells for commuter packs, validating claims with lygte-info comparator data before publishing specs.[^23]
- Cell hunters just spotted Molicel’s 5 Ah/65 A P50B alongside rumors of XA3 21700 cells rated around 50 A, but both need long-term cycle tests before they can displace proven P45B/P42A packs.[^p50b_watch]
- **Sony VTC6A vs. Molicel P42A vs. Samsung 30T:** VTC6A delivers the lowest sag and coolest temps but runs roughly double the cost of P42A unless you buy ~10 k cells per month; 30T still hits hardest but sacrifices capacity, so reserve it for burst-focused builds.[^24]

### Compact Bag Builds & Blade Layouts

- Stuffing 72 cells into a 3 L Wildman bag technically works only if you fold copper interconnects and skip cell holders.
  - veterans still call holderless bricks unacceptable for long-term reliability.[^wildman-72]
- External 20 S 10 P packs hung from scooter frames now rely on tailor-added straps, rigid panels, or cavity fillers; letting a soft battery bag sag mid-ride already stressed frame mounts on Haku’s twin-pack minibike, so reinforce externals before commuting.[^external_bag_reinforcement]
- Blade conversions juggle multiple pack shapes: one builder is parking a 20 s 8 p module for a “clean” Pro 2, a 20 s 4 p MH1 pack for a beater, and scouting 16 s 5 p or 13 s 6 p layouts to tame MH1 sag when 21700s will not fit.[^blade-layouts]
- A single 10 s Blade motor already lifts the front wheel—dual-motor plans demand staged controller and pack upgrades toward 72 V before doubling hardware.[^blade-voltage]
- Happy Giraffe’s reminder still stands: 48 A at 72 V is ~3.5 kW, so raise voltage and lean on 100 A phase rather than piling more battery amps into MH1 cells.[^72v-3p5kw]
- Xiaomi-class decks need every millimetre: Gabe is printing a 5.4 cm extender to stack a 20 s pack under dual ESCs, and his “fastest Pro 2” split the 20 s7 p pack across twin 5 L shoulder bags because the 10.5–11 cm deck leaves only 0.3–0.5 cm spare width.[^25]
[^wildman-72]: Packing 72 cells into a 3 L Wildman bag requires folded copper and no holders.
  - veterans still reject holderless bricks as unreliable.[^26]
[^blade-layouts]: Blade conversions are juggling 20 s 8 p “clean” packs, 20 s 4 p MH1 beaters, and alternative 16 s 5 p / 13 s 6 p layouts to manage sag when 21700s won’t fit the frame.[^27]
[^blade-voltage]: A single 10 s Blade motor already wheelies.
  - plan 72 V controllers and packs before going dual motor so torque stays controllable.[^28]
[^72v-3p5kw]: Happy Giraffe reminded the group that 48 A at 72 V is ~3.5 kW.
  - raise voltage and lean on ~100 A phase instead of stuffing more battery amps into MH1 cells.[^29]

### Shrink Wrap & Pack Retention

- Packing crews now double-layer shrink—light “Albert” sleeves under thicker “Denis” stock—with foam padding over balance leads so shipping vibration doesn’t abrade insulation; a heat gun leaves cleaner seams than a hair dryer when closing the pack.[^shrink_layers]
- If shrink wrap scuffs once installed, treat it as a clamping failure rather than bad material and tighten the enclosure so the battery cannot slide.[^pack_clamp]

### Logistics Snapshots & Supplier QA

- **Store fresh stock cold and at 30 % SoC.** Recent P42A lots landed around $1.80 per cell delivered, and veterans park them in refrigeration at partial charge until welding to preserve shelf life.[^p42a_storage_tip]
- **Account for shipping cadence.** NKON’s EU warehouse can take up to a month to deliver popular 40PL lots, while Vapcell pushes the same cells in 3–5 days via DHL/UPS for roughly €150–€229 in freight with €2.2 per-cell pricing to Germany (≈€229 landed in Switzerland).
  - but Vapcell pallets have arrived with mixed voltages that need individual top-offs before welding.[^30][^31]
- **Vet “Shenzhen Vapcell Technology” listings.** Verified resellers share the same name as counterfeit storefronts.
  - check contact info and demand lot photos before paying so you don’t receive clone cells with shaved wraps.[^32]
- **Verify Lonnyo storefronts before wiring funds.** Builders swap WhatsApp contact +86 151 6855 5189 and compare Lonnyo.com against Lonnyomotor.com because Paolo keeps spotting reseller clones.
  - treat every listing as suspect until a factory rep answers directly.[^33]
- **Measure hub hardware on arrival.** Face de Pin Sucé logged Lonnyo axle variance beyond 5 mm across supposedly identical hubs; add thickness shims only after you mic both sides so brake-side offsets don’t trap rotors or misalign arms.[^34]
- **Boutique drop-in packs set price anchors.** D’s nearly new EVE 50E 20 S 3 P module (≈1,080 Wh) with a JBD smart BMS shipped from Germany for about €400 and fits Xiaomi Pro 2, G30, and G2 decks with a spacer.
  - use it as a benchmark when pricing custom range extenders.[^35]
- **Scrap compromised cells.** PuneDir binned water-soaked LG M26 pulls rather than gamble on hidden corrosion before restarting the build with fresh stock.[^pune_scrap_m26]

### Market Shifts & Pricing Signals

- Nickel’s 2022 price surge (+250 %) pushed pack builders toward 0.1–0.15 mm copper strip.
  - it bends easier over cell tops, carries more current, and costs less than the remaining nickel stockpile.[^36]
- ElectricPowa is quoting Samsung 50E at ~€3.20 and P42A at ~€2.90 per cell out of Spain, though overseas shipping often erases the bargain.[^electricpowa_prices]
- Authentic EVE 40P lots keep testing at 5–7 mΩ IR and cooler temps than P42A pulls, while welded-but-unused Samsung 50E batches are clearing for ≈$0.80 per cell in 2 k-unit deals.[^eve40p_ir_fresh][^welded_50e_lots]
- Telegram teardown threads just caught “nickel” strip that was actually plated steel.
   - plated stock measures roughly six times the resistance of pure nickel, so veterans now scratch-test every batch, source from trusted vendors such as Nkon, and favour pre-cut busbars or stacked pure nickel when targeting 5 kW outputs so counterfeit stock does not bottleneck current.[^37][^nkon-pure]
- Sony VTC5D prototypes are landing alongside Samsung 35E/50G/50S, Molicel P28A/P42A, and Samsung 48X cells; Artem is sourcing fresh 40T/48X/50G stock at €4–5 per cell while group buys quote P42A around €4 and 50S near €12.95, setting the 2025 price floor for high-discharge packs.[^38]
- **Samsung 50S group buys:** Community orders are landing grade-A 50S cells at €4.71 each with the potential for ~15 % savings when payments avoid eBay/PayPal fees.
  - coordinate escrow and inspection to lock in the deal before public pricing rebounds above €6.50.[^39]
- **Price/performance quick look:** Expect Samsung 30T around €2.50, 35E near €3.40, and 50G/50S roughly €4–4.5 when bought in quantity, with discharge logs confirming P42A outpaces 40T at 20–30 A, 50G shines at 7–15 A, and 50S matches P42A only if you can justify the premium.[^40][^41]
- **21700 energy density vs. recycled 18650s:** Recycled EVE 26V 18650 cells struggle beyond ~5 A per cell, whereas fresh Samsung 35E/48X/50S 21700 options pack more watt-hours into Xiaomi/Ninebot decks and sustain 15–20 A draws.
  - reserve reclaimed cells for low-power builds and spec new 21700s for high-range projects.[^42]
- **Honeycomb nickel shortages:** EU builders now pool orders for half-kilo lots because suppliers refuse to ship sub-1 kg batches; expect ~40 € quotes locally or wait on AliExpress consolidation when stocking cell cages.[^43]
- **Tabless cells keep packs cool.** Rob Ver’s testing shows tabless modules maintain pack temperatures within ≈3 °C of ambient even under heavy load, making them attractive for high-discharge scooters when paired with proven salvage sources.[^44]
- **Budget math for newcomers:** Tempting £3 50PL listings still double total cost once you factor a €50 JBD BMS, insulation, and a €50–€200 welder; many first-time builders pivot to €1.5–2 EVE/Samsung 50E cells instead or outsource packs entirely.[^45]
- **Commissioning remains attractive:** Even when shipping premiums bite, UK riders still hire trusted builders like @jamessoderstrom to dodge tooling purchases and customs headaches for one-off packs.[^46]

Regional sourcing realities still shape chemistry choices: Turkish builders blocked from NKON settle for Samsung 29E/50E lots despite higher sag, while racers keep paying for Molicel P45B as the only 21700 that resists brutal voltage droop at high current.[^47] Casual riders still default to cheaper Samsung or LG long-range cells unless their builds genuinely need 35–40 A per cell or fast-charging workflows, proving that cost and mission dictate chemistry more than spec-sheet hype.[^48] AliExpress flash sales still advertise fantasy pricing.
  - message sellers for real quotes, expect shipping to erase the $6-per-cell clickbait, and stick with the one vetted vendor the community trusts when you cannot buy direct.[^49]
- Reclaimed packs remain tempting.
  - builders strip P42A cells from Dyson vacuums and similar gear
  - but U.S. riders still lament how few lithium recycling drop-offs exist compared with EU mall programs, so plan shipping or hazmat-friendly disposal before hoarding scrap cells.[^50]

### 8–9 P Chemistry Trade-offs

- **P45B for brute force.** Flash-sale quotes hover around $6 per cell with ~7 mΩ IR, making P45B the go-to when a pack must hold 400 A+ without sagging.
  - but budget the premium upfront instead of rebuilding mid-grade packs after they cook under race duty.[^51]
- **P42A as the value pick.** P42A arrays still deliver stout 300–350 A performance for commuters and canyon riders; their ≈9 mΩ IR and lower pricing keep them attractive when the build lacks the charging infrastructure or current demand to justify P45B.[^51]
- **P45B for brute force.** Choose Molicel P45B when the build needs 400 A+ bursts and minimal voltage sag; Happy Giraffe’s cell curves show it beating Samsung 50S at 30 A while running cooler than P42A/40T, justifying the premium when range and punch matter.[^52][^53]
Regional sourcing realities still shape chemistry choices: Turkish builders blocked from NKON settle for Samsung 29E/50E lots despite higher sag, while racers keep paying for Molicel P45B as the only 21700 that resists brutal voltage droop at high current.[^54] South Korean riders face customs and licensing barriers on Samsung 40T/50S imports, so they lean on reclaimed MH1 packs or coordinate cross-border friend shipments unless they can travel with empty hardware.[^55] AliExpress flash sales still advertise fantasy pricing.
  - message sellers for real quotes, expect shipping to erase the $6-per-cell clickbait, and stick with the one vetted vendor the community trusts when you cannot buy direct.[^56]
- **P45B for brute force.** Choose Molicel P45B when the build needs 400 A+ bursts and minimal voltage sag; the premium pricing beats rebuilding packs that rely on mid-grade cells and cook under race duty.[^52]
- **Reclaimed Stark modules need careful prep.** Builders are restacking Stark’s mis-welded P45B stock into 20 S 5 P bricks without adhesives, logging 85 km/h before field weakening and planning higher current once the rebuilt pack is validated.[^57]
- **P42A as the value pick.** P42A arrays still deliver stout 300–350 A performance for commuters and canyon riders, especially when paired with faster charging rather than upsizing parallel count.[^52]
- **Samsung 50S for range.** 50S and LG 50LT cells stretch 8–9 P packs for touring but expect more sag.
  - pair them with conservative current limits or dual-pack fast-charging plans instead of chasing peak amps.[^52]
- **Budget chemistries need charge discipline.** Builders chasing LG M58 or Samsung 50E endurance budgets lean on higher-current chargers instead of premium cells; model turnaround times so clients understand the compromise.[^52]

> **Aspilsan A28 watchlist:** Telegram anecdotes praise ~16 mΩ internal resistance and cool 15 A continuous runs, but we still need controlled lab testing (capacity, sag, cycle life) before recommending the chemistry broadly.[^58]

- Denis’ crew still treats LG M29 or EVE 33V cells as the baseline for 15 S AWD commuters, with Molicel P42A/40T, Samsung 25R/30Q, and Sony VTC5/VTC6 reserved for higher-discharge layouts.
  - 21700 formats remain the preferred starting point for dual-motor projects.[^59]

## Welding Equipment Decision Guide

High-current harness work still rewards oversized irons.
  - shops rely on 200–300 W handheld irons or 3 kg stations for QS8 leads, while 65 W tools only keep up when dangerously overdriven.[^60]
| Scenario | Recommended Tooling | Why It Wins | Follow-Up Checks |
| --- | --- | --- | --- |
| First copper pack, limited budget | Rent/borrow K-Weld or Glitter kit | Proven to fuse 0.1 mm copper reliably versus unproven 90 € units | Inspect weld nuggets under magnification; rip-test samples before scaling.[^3] |
| Mobile copper welding on customer sites | Mirror 🇪🇸عمر’s build: a compact controller fed by a 5 S 1 P, 20 Ah, 200 A-rated industrial Li-ion pack powers copper-capable probes without needing mains. | Check pack health and cooling between jobs; portable rigs still need proper lugs and insulation before leaving the shop.[^61] |
| Daily fabrication shop | Own Glitter 811A or K-Weld with high-current PSU | Handles repeated 4 kA+ hits when contacts are clean | Schedule bus pin cleaning to prevent E01 faults and maintain 4.4 kA output.[^10] |
| Mixed chemistries (pouch + cylindrical) | Use adjustable pulse welders with copper/nickel sandwiches | Controls heat on dissimilar tabs, minimizes swelling risk | Pair with upgraded ≥230 A BMS and temperature probes on parallel groups.[^6] |
| Tight copper layouts | Stack 0.1 mm copper under 0.15 mm overlays and cap each strike near 50–60 J | Dual-strip “infinite slot” technique pushes current into the can without cracking copper; the same stack is fuelling 320–800 A pack targets even when smart BMS hardware only tolerates 30–60 s at 800 A.[^62] | Validate that 10 mm-wide copper already supports ~15–20 A per cell (≈200 A on 9 P) before oversizing plates.[^63][^64] |

- Copper strip thicker than ≈0.1 mm overwhelms hobby shears and improvised car-battery welders; shops either outsource laser/water-jet cutting or invest in Glitter-class welders instead of risking weak joints and blown cells.[^thick-copper-tooling]
- Cheap 20 € control boards still demand ~€100 worth of 3 S high-rate packs or supercapacitors.
  - plan those hidden costs before assuming a bargain welder will fuse copper reliably.[^65]
- Cihan priced the Docreate DO-02 capacitor welder around $108 shipped to Turkey (less with coupons) and confirmed ~0.36 mΩ capacitor ESR; crews recommend the foot-pedal bundle or Glitter 801D if you only ever weld 0.1–0.15 mm nickel.[^docreate]
- Builders get by with inexpensive 230 V stick irons and €6 pencil irons for quick controller jobs, but aluminum-PCB MOSFET arrays still demand 200 W stations or hot air so the large pads heat evenly.[^66]
- **Power the welder properly.** Car batteries sag after only a handful of welds; builders now favour CNHL 4S 9.5 Ah hardcase LiPos or similar high-C packs to keep K-weld pulses near 2 kA without undervoltage alarms, while aging RC packs and USB power banks overheat even with extra heatsinks.[^67]
Builders comparing Glitter rigs noted 801D capacitor banks sag toward 5.7 V under load, so weld quality falls off unless you rotate packs or move to low-ESR capacitor supplies; the 801H’s twenty-transistor stack and stronger shunts justify the higher price when thick copper sandwiches are on the menu. Follow-up tests also confirm stock 801D hardware cannot reliably weld 0.15 mm copper.
  - reserve heavier laminates for 801H/KWeld-class tools
  - and later experiments only succeeded when pairing 0.1 mm copper with steel or iron caps, while pure nickel stacks tore free even at full power.[^68][^69][^70][^71]
- Malectrics V4 welders now ship with parallel MOSFET daughterboards and run happily from triple 3 S LiPos; some builders still drop to 2 S packs to tame FET heating because the welder regulates to ~5–6 V at the electrodes.[^72]
- Artem’s 0.1 mm copper-under-nickel stacks respond best to heavy compression and careful hot-glue alignment.
  - done right they only sag ~3.5 V at 60 A on 60 V Samsung 35E packs versus the 7–20 V drop seen on looser busbars.[^73]

### Booster & Launch Packs

- **High-C LiPo reservoirs.** CNHL and GNB 140 C–180 C packs keep kWeld/Glitter rigs and launch boosters punching above 2 kA, but they empty within a sprint.
  - parallel two or more bricks if you need repeat hits instead of single holeshots.[^cnhl-booster]
- **Graphene LiPos feed copper welds.** KWeld users lean on high-discharge bricks like Turnigy’s Graphene 6000 mAh 3 S 75 C pack, run 60–70 J for 0.1 mm copper-on-nickel joints, and stack nickel/copper layers with ample flux so the welder wets up to ~0.4 mm of copper without brownouts.[^74]

- Grab scrap tubing from university bins to practice MIG/MAG beads.
  - veterans stress that clean, even passes matter more than picking the “perfect” process for scooter frame reinforcement.[^75]
- **Shield brazed copper joints.** When builders skip spot welding and braze copper busbars, they flood the joint with argon while feeding tin so oxidation doesn’t spike resistance; humidity alone can corrode unsealed copper/nickel “sandwich” welds within a few years.[^argon-braze]

Glitter 811A/811H rigs promise 6 kA bursts with 35 mm² cables for 0.2 mm copper sandwiches, but early adopters still tear them down to resolder loose capacitors and confirm the shop has 110 V/220 V service before committing.[^76]

- Glitter 801/811 welders only behave with copper when you cap the strip in nickel or plated steel.
  - running bare copper either blows holes or produces weak nuggets, so most crews still finish with nickel top plates for strength.[^77]

### Copper Busbars & Sandwich Welding Notes

- Springy copper sheet can be pre-tensioned by gently drawing it over a table edge before welding; the reverse bend helps 0.25 mm strip stay flat until the first welds lock it down.[^copper_pretension]
- Copper bus TIG welds work when you keep pulses around 20–30 A with argon shielding; most still prefer capacitor welders, but the field notes prove TIG can salvage thick bus work if you mind heat input.[^65]
- Laser-cut 0.5 mm copper combs (e.g., from Peng Chen) spot-weld cleanly when clamped under nickel-plated steel overlays, delivering neat 20 S 10 P layouts without bulky braided jumpers.[^78]
- Plan on ≥1 kA pulse capacity.
  - KWeld or 1,600 A Malectrics rigs
  - to bond 0.2 mm copper reliably; hobby welders under the 1 kA mark struggle and drive builders back to nickel overlays.[^79]
- Treat 0.15 mm pure-nickel bridges as single-digit-amp paths; pushing 9 kW through narrow welds has already cooked localized spots, so reinforce before raising battery current limits.[^80]
- Practice on dead cells before committing copper-nickel sandwiches to live packs; slotted nickel forces current through the can and punishes misaligned welds.[^81]
- Copper/nickel sandwiches still demand the right tongs.
  - builders stuck with only the control PCB on car-battery rigs could not weld until matching probes arrived, so budget electrode sourcing alongside the welder.[^82]

- Vet builders for steel enclosures and disciplined BMS work.
  - NYC shops have already rebranded after fires, reminding riders to choose quality over marketing gloss.[^83]
- **Material cost note:** Wellgo nickel-copper laminates run about $150 shipped for a 20 S 10 P pack and solder cleanly to nickel after welding.
  - budget the upgrade when planning copper-clad busbars.[^84]

- Budget builders are experimenting with €25 purple PCB welders powered by 72 Ah car batteries.
  - they handle 0.2 mm nickel but lack the transistor count for 0.15 mm copper, so reserve thick copper stacks for Glitter/KWeld-class rigs.[^85]
- Car-battery welding rigs only behave when the electrodes are solid copper.
  - shops hammer house wire or copper nails into the clamps and sleeve the joint before heat-shrinking, because steel hardware overheats and burns out quickly.[^86]

### Consumable Sourcing Alerts

- Leaded solder is getting scarce inside the EU; builders are already scrambling for compliant suppliers before pack repairs stall under regional restrictions.[^87]
- Jerome (St0fzuiger) pointed the crew to EleShop’s 60/40 premium solder, which ships across Europe and carries enough flux to wet thick busbars.
  - GABE is restocking there for his MP2 repairs until a broader supply chain emerges.[^88]
  - Pending: Monitor EleShop stock levels and log GABE’s long-term feedback on the solder once those MP2 repairs wrap so the sourcing guide reflects real durability.[^eleshop-follow]
- Peer-to-peer trades now fill the gap.
  - PaoloWu is literally mailing GABE leaded solder so his pack repairs resume, highlighting how community swaps keep benches running when stores dry up.[^89]
- GABE’s spot welder just lost a MOSFET (E02 fault); Haku’s replacement board only charges to 5.4 V and he pointed to the heavier Glitter 811H as the backup plan if repairs stall, so shops should budget downtime or a spare welder for 22 S builds.[^90]

## Pack Architecture Case Studies

| Platform | Layout & Cells | Controller Pairing | Lessons |
| --- | --- | --- | --- |
| Dual 70H race scooter | 22 S10/11 P P45B modules | MakerX G300 duals | Logs justify nearly 500 A continuous; plan dual-BMS or fuse strategy until 700 A-class boards exist.[^4][^7] |
| Dualtron Achilleus | 20 S8 P Molicel / 22 S9 P custom | Spintend 85250 relocated outside deck | Deck measures ≈48.5 cm × 18.1 cm.
  - external controller mounting frees volume for ≥100 A batteries.[^4][^8] |
| VSETT 10+ 20 S9 P | Copper-clad “W” pack with pre-welded tabs, QS8 connectors, copper bus reinforcements (~$170 shipped) | Controllers relocated outside deck | 168 mm-wide pack slides into the 171 mm cavity once controllers move; 19 mm PVC + 5 mm acrylic risers raise the lid for a top-mounted BMS.[^91] |
| Blade-compatible prototype | 20 S8 P Sony/Murata VTC5D (35 A cells) | In validation; targeting Blade hub swaps | Builder is logging 30 A sag data, comparing against Samsung 35E/50G/P42A alternatives, and pricing VTC5D vs. group-buy chemistries before committing to production.[^92] |
| Nami commuter upgrade | 22 S10 P layout in development | Awaiting high-current controllers | CNC + 3D-printed supports required; treat as modular sled to service 50PL packs.[^12] |
| G3 30 S conversion | 30 S3 P modules (15 S6 P split) | High-voltage VESC | Requires grinding factory brackets; 30 S4 P too wide without chassis surgery and new BMS routing.[^13] |
| 20 S10 P Samsung 40T | Dual Ubox 85250 | 0.2 mm copper busbars deliver ~350 A continuous / 450 A burst; avoid mixing pouch cells in parallel due to swelling | Reserve space for ≥230 A BMS and monitor temps during 40 kW pulls.[^6] |
| MH1 commuter rebuild | 20 S4 P aging pack → planned 20 S6 P 21700 swap | Makerbase 75100 single | Stock MH1 cells sagged from 80 % to 35 % under load; rebuilders are upsizing parallel count and logging rest voltage before landing the replacement BMS.[^93] |

### 2024 Telegram Updates (input_part009)

#### Cell & Materials Decisions

| Finding | Implementation Guidance | Implication |
| --- | --- | --- |
| 30 S ANT boards misreport when wired to 22 S harnesses without pin swaps.[^ip009-ant-down] | Document the harness repin and configure the app for the shorter stack before trimming leads. | Preserves telemetry accuracy when down-populating high-series boards. |
| Mixed-color LG M26 stock is safe once parallel groups are binned to matching IR values.[^ip009-m26] | Grade and bin cells before welding rather than chasing cosmetic uniformity. | Focus QC time on electrical variance, not sleeve colour. |
| P42A packs bring minimal benefit on scooters capped near 120 A battery when 50H motors saturate around 60 A.[^ip009-p42a] | Choose lower-cost cells if the drivetrain cannot exploit higher current headroom. | Budget savings can fund thermal instrumentation or spare packs. |
| ASA‑CF holders demand heated chambers but deliver exceptionally rigid frames at ~€50 per 750 g of filament.[^ip009-asacf] | Reserve these prints for high-stress packs and price builds accordingly. | Factor double-the-standard-ASA material cost into client quotes. |
| XT90S anti-spark connectors fatigue quickly under scooter loads; QS8 is the preferred drop-in upgrade.[^ip009-xt90] | Upsize to QS8 (or similar) on any build expecting repeated high-current plugs. | Reduces arcing failures and warranty returns on performance scooters. |
| EVE 40PL cells hold roughly 45–70 A continuous with ~60 % capacity left after 300 cycles at 30 A.[^ip009-40pl] | Treat manufacturer 100 A claims as marketing and size packs for realistic current and lifespan. | Helps frame warranty terms around accelerated ageing on torque builds. |

#### Protection & BMS Practice

| Finding | Implementation Guidance | Implication |
| --- | --- | --- |
| Parallel range-extender packs only stay safe if each BMS shares voltage; a tripped BMS dumps full load onto the remaining packs.[^ip009-parallel] | Align pack voltages and current limits, and add coordinated cutoff logic or fusing. | Prevents cascading overload when one BMS trips mid-ride. |
| Stacking off-the-shelf 14 S packs in series risks BMS mismatch; Paolo steers Apollo Phantom builders toward purpose-built dual 28 S 5 P packs with dedicated ANT BMS hardware instead of daisy-chaining random modules.[^ip010-28s] | Build true 28 S packs (each with its own BMS) or expect shutdowns and uneven state-of-charge when one half lags. | Keeps high-voltage experiments from faulting mid-ride and preserves pack balance. |
| VESC regen respected 71.4 V on 17 S builds, so 72 V setpoints remained within controller limits.[^ip009-regen] | You can leave regen enabled near full charge on 17 S scooters without overstressing the controller, provided wiring supports it. | Simplifies regen tuning for riders who top off frequently. |
| Deep-discharging a JK-managed pack to 57 V killed cells and the BMS interface.[^ip009-deepdis] | Enforce conservative low-voltage alarms on extender packs and recharge well before hard cutoff. | Avoids irreversible cell damage and lost telemetry. |
| Active balancing boards restored pack parity in roughly an hour versus days on stock JBD balancing.[^ip009-active] | Deploy active balancers during commissioning or service to accelerate equalisation. | Shortens delivery timelines for large-capacity builds. |
| Cloud-connected smart BMS portals can be tampered with, and some apps break if you change default passwords.[^ip009-bms-app] | Keep smart BMS units offline or maintain default credentials with physical security layers. | Reduces remote sabotage risk while preserving diagnostics. |

#### Build Process & Instrumentation Notes

| Finding | Implementation Guidance | Implication |
| --- | --- | --- |
| Jason keeps JST balance harnesses plugged in while routing, letting the BMS refuse to boot if a lead is misplaced so you can correct the order without damaging the board.[^94] | Leave the harness connected during reassembly and fix mistakes immediately if the BMS stays latched off. | Reduces risk of cooking balance resistors during pack service. |
| Clamp-meter spot checks on shunt-modded square-wave controllers exaggerated delivered phase current; PuneDir still logs targets around 200 A phase / 150 A battery but sees ~260 A spikes without careful instrumentation.[^95] | Validate current draws with trusted meters and telemetry before upping limits on modified controllers. | Prevents cable overheating and controller failures from misread current data. |
| Extending “silver” hub harnesses is safe because the conductors are just tinned copper.
  - matching-gauge copper splices maintain conductivity when lengthening motor looms.[^96] | Use quality copper leads and solder/heat-shrink to extend factory looms without chasing exotic wire. | Simplifies routing when controllers move outside tight decks. |
| 4 mm² (~AWG 11) silicone wire can overheat around 250 A even on short runs; monitor temps after upsizing controllers before committing to higher current limits.[^97] | Log wire temperatures on shakedown rides and upsize conductors if insulation softens. | Avoids hidden loom failures when chasing 250 A+ bursts. |

#### Packaging & Logistics Notes

| Finding | Implementation Guidance | Implication |
| --- | --- | --- |
| Hanging a 20 S 10 P stem pack drew safety pushback.
  - veterans prefer internal mounts or backpacks once decks are full to avoid slinging heavy mass on the mast.[^98] | Keep high-capacity packs inside the chassis or in purpose-built backpacks instead of stem mounts. | Prevents steering-column overloads and reduces crash risk. |
| Builders resorted to foam blocks or even taped shells when customs delayed metal boxes, but everyone agreed those stopgaps need better thermal padding before becoming permanent fixes.[^99][^100] | Treat foam/tape solutions as temporary and publish thermal padding guidance once proper enclosures arrive. | Keeps emergency packaging from becoming a long-term liability. |
| JK’s mobile app can disable the discharge MOSFET for storage or anti-theft once the pack is full.[^ip009-jk-mosfet] | Add the MOSFET-disable workflow to delivery checklists so riders can lock packs without rewiring. | Provides a simple parking lock without extra hardware. |
| Compact 10 S builds pulling 30–45 A per cell still favour JK/JBD 100 A boards (with ANT as backup) for protection and telemetry.[^ip009-compact-bms] | Budget space for smart BMS hardware even in tight enclosures to retain diagnostics. | Confirms that reliable protection trumps marginal space savings. |

#### Assembly & Mechanics

| Finding | Implementation Guidance | Implication |
| --- | --- | --- |
| Thin epoxy sheets between balance leads and copper busbars maintain insulation where plastic holders will not fit.[^ip009-epoxy] | Stock epoxy board alongside fishpaper for slim packs, especially Zero 10X builds. | Improves durability without increasing pack thickness. |
| Silicone spacers backed with fishpaper/Kapton keep honeycomb rows insulated when hot-gluing rebuilt packs.[^ip009-silicone] | Stage silicone/Kapton strips during rebuilds instead of relying on shrink alone. | Reduces rewrap labour after service. |
| Hot-melt glue softens around 80–90 °C and struggles to grip cold cans.[^ip009-hotmelt] | Use it only for temporary tacking before switching to holders, fishpaper, or silicone that tolerates vibration. | Prevents packs from walking apart once the scooter heat-soaks. |
| Silicone 12 AWG realistically handles ~100 A bursts while “8 AWG 400 A continuous” marketing ignores insulation and routing heat.
  - log real temps before trusting spec-sheet claims.[^ip010-amp-gauge] | Validate conductor temperature under load and route leads with airflow or shielding. | Prevents cooked looms when scaling 3 kW-class scooters. |
| Twin steel strip overlays support ~8 A per cell in LG M26 packs when reinforced, keeping 17 P builds near 10–11 kW.[^ip009-steel] | Pair steel overlays with structural bracing for high-parallel-count packs. | Offers a path to higher power without full copper busbars. |
| 0.1 mm copper sheet is the minimum for busbars; thinner 0.01 mm craft foil tears under welding current.[^ip009-copperthick] | Audit material deliveries before welding and reject ultra-thin foil. | Prevents catastrophic busbar failure mid-build. |
| Chamfer copper/nickel edges near positive terminals to stop them slicing insulation under heavy compression.[^ip009-chamfer] | Add deburring passes before final shrink and compression. | Cuts down on latent shorts in high-mass packs. |
| Tight-tolerance 3D-printed holders (PETG/ASA/ABS) outperform hot glue for spacing and heat paths, especially on long packs.[^ip009-holders] | Prioritise high-temp filaments for holders exposed to parked-car heat. | Raises mechanical reliability for summer storage. |
| Double-layer “makaron” shrink can substitute for fishpaper between rows, but scuffs faster and still benefits from fishpaper on series barriers.[^ip009-makaron] | Use makaron only for supplemental abrasion resistance, not as the sole barrier. | Avoids premature insulation wear. |
| **Manage heat on wraparound copper bridges.** GABE nearly overheated the copper span on his 20/22 S 2 P wraparound pack while welding inside a PETG carrier.
  - pause between hits or anneal strips so thin plastics do not deform.[^101] | Add cooling cycles or pre-anneal busbars before welding inside printed shells. | Protects printed carriers and keeps copper from softening mid-build. |
| Salvaged LG modules often arrive epoxied together; soak joints with acetone, pry gently, and plan to rewrap cells once the adhesive releases so you do not leave bare cans with pinhole insulation.[^102] | Stage replacement wraps and solvent-safe trays before teardown work. | Prevents latent shorts when refurbishing second-hand modules. |
| Fiberboard between copper folds keeps 0.20–0.25 mm busbars separated until spacers land.[^ip009-fiberboard] | Slide thin fiberboard into the fold before clamping and remove it once epoxy spacers are seated. | Prevents shorting while the copper stack is aligned. |
| Barley paper at strip ends stops heavy copper sandwiches from chafing insulation when packs flex.[^ip009-barley] | Wrap each series strip in barley paper before final compression or shrink. | Boosts abrasion resistance on high-mass builds. |
| Pre-tension springy copper before welding to tame rebound.[^ip009-pretension] | Drag the strip gently over a table edge so it lies flat once the first welds land. | Makes folding safer and keeps busbars seated. |
| Fine-strand silicone leads beat PVC in folding decks.[^103] | Route silicone-jacket wire through hinges and controller bays to resist heat and flex fatigue. | Prevents stiff jackets from chafing through insulation. |
| Glitter 811H can weld 0.2 mm copper-to-nickel once power is reduced and probes are dressed sharp.[^104][^105] | Regrind electrodes and back off joules before production welds; inspect nuggets often. | Avoids blowing holes in nickel while copper remains secure. |
| Rehearse on scrap nickel/dead cells before real packs; add a BMS and verify nickel purity rather than trusting “plated steel works fine” claims.[^106] | Treat practice welds and materials testing as part of build time so live packs launch with vetted strip. | Reduces rework and hidden resistance in high-current builds. |
| Limit KWELD supercap banks to four modules; larger arrays trip faults.
  - builders now slow charge/discharge with resistor banks and are prototyping water-cooled pens after shrink-stacked cables overheated.[^107] | Configure capacitor packs with managed charge circuits and consider active cooling on long copper sessions. | Keeps welders online through extended builds without overheating. |
| LiFePO₄ insulation needs reinforcement: sleeves cost more, run bulkier than PVC, and tear easily without abrasion guards.[^108] | Budget extra wrap and protective liners when packaging LiFePO₄ bricks inside scooter decks. | Prevents sharp deck edges from slicing pouch insulation. |
| PETG remains the go-to filament for outdoor battery carriers but needs supports/brims and good ventilation.
  - keep printers out of sleeping areas.[^109] | Print battery mounts in PETG (or CF-PETG) with ample bed adhesion and separate workspaces to manage fumes. | Balances toughness with safe fabrication practices. |
| Shop cleanup matters: working aluminum or PETG parts throws particulates.
  - wear gloves, wash up, and avoid eating until clean.[^110] | Treat fabrication spaces like light industrial zones; stage PPE and hygiene breaks during long print or machining sessions. | Limits microplastic exposure for builders. |
| Heat MP2 busbars evenly from both sides; uneven torch work warps the copper/aluminum stack before solder wets properly.[^111] | Use dual-torch or wraparound heating on MP2 assemblies before adding solder. | Keeps laminated busbars aligned and electrically sound. |
| Reinforce hanging extender bags with rigid bases or tailored straps.[^ip009-bag] | Add structural panels or relocate the pack to stop sag that stresses frames mid-ride. | Keeps twin-pack builds stable and protects enclosures. |
| G30 conversions fitting 20 S 6 P 21700 stacks needed a 36 mm deck extender plus ~1 mm grinding around the rail opening.[^ip009-g30] | Budget machining time and extender hardware when packaging large packs with dual controllers. | Prevents rework when packs will not seat flush. |
| Twin-MP2 G30 builds stack the 20 S brick to ~14.5 cm, park the smart BMS vertically at the nose, and split current across parallel QS8 leads with multiple 8 AWG runs while a welded rear controller box preserves the deck arches.[^ip009-g30blueprint] | Mock up the vertical BMS bay and welded enclosure before final welding to confirm harness slack and controller cooling. | Keeps tall packs serviceable without weakening the frame. |
| Guard welder power buttons.
  - GABE nuked an 801D by stomping the AC adapter while the foot pedal was pressed, so shield the switch and keep a car battery ready as a fallback welding supply.[^112] | Add switch covers or relocate adapters to avoid accidental power cycles mid-weld. | Prevents catastrophic welder failures and keeps production moving. |
| Modular 20 S 3 P P42A travel pack | Bag accepts 6 S + 2 S subpacks; keep harnessing modular so the pack can bounce between an ebike and Ninebot while the welder is down, and add a 10 mm deck spacer as a temporary heatsink until replacement CAD files are recovered.[^113] | Maintain swappable harnesses and interim cooling so projects continue even when tooling fails. | Keeps shared packs serviceable across multiple scooters during repair downtime. |
| Flush cutters lift welded nickel without grinding off plating; remaining specks can stay once flattened.[^ip009-flush] | Equip teardown stations with sharp flush cutters and burnishers. | Speeds rebuilds while preserving cell cans. |
| Adhesive-lined “marine” shrink grips bullet connectors more securely than thin sleeves.[^ip009-marine] | Standardise on glue-lined shrink for high-current leads. | Reduces connector loosening under vibration. |
| 🇪🇸AYO#74 secures rebuilt modules with hot silicone plus glass filament tape to stop vibration fret.[^ip009-ayo] | Add silicone tacks and filament wrap when custom holders are unavailable. | Lightweight reinforcement alternative for tight enclosures. |
| Switching Laotie builds to seated frames freed enough deck volume for a 240-cell main pack once the extender battery was repurposed.[^ip009-laotie240] | Scope bracing and BMS routing for the larger brick before committing to the chassis swap. | Avoids mid-build packaging surprises on cramped commuter frames. |
| Refurbishing Glitter 811H consumables restored reliable 0.25–0.30 mm copper weld strength on budget rigs.[^ip009-811h-refresh] | Keep spare electrodes and cables on the shelf and requalify weld nuggets after each refresh. | Extends the service life of 811H setups when KWeld imports are blocked. |
| Layer epoxy sheet, plexiglass, fishpaper, and polycarbonate around frame-mounted packs so vibration and water cannot chafe nickel or balance leads once the battery doubles as a chassis member.[^114] | Stage multi-layer insulation wherever packs bolt to frames or sit near sharp edges. | Prevents fretting failures on high-voltage deck builds. |
| Copper under nickel survives pull tests; pure copper strips still pop free.
  - tune weld energy to ≈40 J on nickel, 60–70 J on copper, and sandwich layers so joints tear metal instead of lifting.[^3] | Weld copper-nickel sandwiches in one pass and proof the nugget with pull tests. | Produces durable high-current busbars without bulky nickel stacks. |
| Tape between nickel layers, triple shrink with silicone-sealed exits, and route balance leads through plexiglass channels to protect 20 S harnesses from wet-deck chafing.[^115] | Overbuild insulation wherever 20 S looms exit tight decks. | Keeps high-series harnesses from abrading through on commuters. |
| Active-balancing hardware only shuttles ~600 mA between groups.
  - confirm the gain before reordering hardware or count on passive boards that simply dump excess energy as heat.[^116] | Pick balancers based on real current instead of marketing numbers. | Prevents disappointment with pricey “active” hardware. |
| JK’s 150 A/300 A smart BMS with a 1 A active balancer held groups within 0.001 V after 100+ days, but the enclosure is larger than ANT units despite better harnesses and app support.[^jk_balancer] | Budget space for the bigger board or keep ANT for tight decks. | Confirms the balancing upgrade works if you can accommodate the physical size. |
| Stop routine charges around 90 % if the BMS still balances there.
  - commuters quadruple pack life by avoiding full charges.[^117] | Set chargers and rider habits for partial charges when longevity outranks maximum range. | Extends cycle life on daily-use packs. |
| Salvaged Dyson V8 modules hide 6 S 1 P Molicels; release the enclosure’s hidden pins, refresh welds, and be ready to reflash the smart BMS with a Pickit 3 to clear soft-locks.[^118][^119] | Treat vacuum modules as quality donor cells once electronics are reset. | Adds an affordable path to high-discharge cells for scooter packs. |
| Samsung 50E chemistries polarise builders.
  - four-year Weped FS packs still hit 240 A with low sag, yet many reserve the cells for huge parallel counts while relying on 40T/P42A for high-amp builds.[^120] | Size 50E packs for high parallel count or pick punchier chemistry when current demand is high. | Matches chemistry to the mission to avoid premature sag. |
- Rosheee’s Kaabo testing pulled 130 A from a Samsung 50E 5 P block, melted a 3D-printed battery frame, and tripped the BMS at 180 A—treat 50E as an ~8 A real-world cell and plan 20 S6 P/20 S7 P upgrades for sustained high power.[^50e_abuse]

#### Consumables & Logistics

| Finding | Implementation Guidance | Implication |
| --- | --- | --- |
| Leaded solder continues to slip through AliExpress when shipped with Chinese labelling, letting builders finish 13S8P packs even where customs screenings are strict.[^ip009-solder] | Order spare reels ahead of schedule and document the supplier details in build logs in case a batch is seized. | Keeps bench work on track when domestic suppliers restrict leaded alloys. |

## Cost Planning Worksheet

1. **Cell procurement** – price the primary chemistry plus 10 % spares for grading losses and future replacements.[^2][^11]
2. **Interconnects & welding** – include copper/nickel, insulation, weld probe maintenance, and PPE alongside the welder cost or rental fees.[^3][^10]
3. **BMS & protection** – today’s compact boards cap around 500 A continuous; large packs may need dual-BMS or fuse-plus-charge solutions until 700 A hardware lands.[^7]
4. **Connectors & harnessing** – QS8 connectors, 8–10 AWG silicone wire, and panel mounts are trending upward in price due to tariffs—stockpile early.[^5][^9]
   - Reference the QS8 harness sizing cheatsheet below before committing to new layouts.[^qs8_chart]
5. **Copper inventory** – Nickel-copper laminate pricing swung from ~€15 to €45 per roll within weeks and is climbing again alongside copper-strip inflation debates; secure stock ahead of builds or budget fallbacks that rely on pure nickel when costs spike.[^23】[^121]
6. **Enclosure & structural supports** – CNC plates, 3D spacers, and adhesives trump hot glue for 22 S builds; treat mechanical retention as part of the electrical budget.[^8][^14]
7. **Labor or outsourcing** – weigh the tooling investment against commissioning vetted builders when customs, shipping, or learning curves threaten schedules.[^11]

#### QS8 Harness Sizing Cheatsheet

| Target Battery Current | Recommended Harness | Installation Notes |
| --- | --- | --- |
| ≤300 A burst / 200 A continuous | Dual 8 AWG (≈8 mm² each) into one QS8 | Split load across both cups and keep lead lengths under 300 mm to curb voltage drop.[^qs8_chart] |
| 350–400 A burst / 250 A continuous | Single 6 AWG (≈13 mm²) or parallel 2×8 AWG per QS8 | Stagger heatshrink and anchor the cable with clamps so the silicone jacket doesn’t lever the solder joint inside shallow decks.[^qs8_chart] |
| 450–500 A burst / 300 A continuous | Dual QS8s with 4 AWG (≈21 mm²) shared across packs | Route paired leads through opposite deck walls and secure them with printed saddles so short harnesses stay cool and vibration-free.[^qs8_chart] |

### Supplier Dispute Playbook

- **Document substitutions before filing claims.** Accepting a downgraded charger (e.g., 350 W XT90 delivered instead of a 500 W/100 V unit) still leaves room for partial refunds.
  - log the shortfall with photos and voltage checks before escalating with the seller.[^122]
- **Vet “premium” rebuilders.** Nordbot packs have arrived with rewrapped cells, exposed busbars, and flimsy insulation.
  - treat the vendor as suspect and demand teardown photos before wiring them into high-power scooters.[^123]

## QA & Maintenance Protocols

- **Thermal interface audits:** Log controller and stator temperatures on first shakedown runs; resurface heatsink plates and refresh thermal paste before chasing 400 A+ per motor.[^9]
- **Match weld energy to chemistry.** Nickel that grips LG MH1 cells can pop off Molicel P42A cans.
  - step up energy or use copper-clad busbars so high-drain cells stay bonded.[^124]
- **Weld verification:** Rip-test sample strips each session, especially after cleaning Glitter bus pins, to confirm energy settings haven’t drifted.[^10]
- **Copper strip finishing:** Keep scissors pivoted near their hinge for leverage on 0.15 mm sheet, cut curves gradually, and flatten tabs with a rubber or soft-blow mallet before stacking so laminates sit flat without specialty shears; builders also radius every corner and pre-tin copper inserts before welding so sharp edges and dry joints can’t chew through insulation once the pack is strapped together.[^125][^126]
- **Respect kWeld lead lengths:** A 1.2 kA overcurrent alarm traced back to using the wrong cable length.
  - swapping to the recommended leads cleared the fault
  - so keep probe wiring within spec before blaming the control board.[^127]
- **Harness strain relief:** Use deck plates or external mounts to keep relocated controllers from stressing phase leads and QS8 connectors during pack swaps.[^8][^9]
- **Clamp modules before welding:** Builders lean on threaded rods or dots of superglue between PETG holders and even plain duct tape when Kapton runs out; clear packing tape is the last resort before final wraps.[^holder-clamp]
- **Adhesive-lined shrink grips bullet connectors best.** Marine-grade heat-shrink that oozes glue under heat keeps bullet connectors from sliding off under vibration far better than thin sleeves.[^128]
- **High-temp harness upgrades:** Builders are trialling thin glass-fibre–insulated wire rated ~800 °C to squeeze 6 mm² conductors into Lonnyo 65 H hubs.
  - expect the rewinding labour to dwarf sourcing cables
  - and Tristan’s math pegs 6 mm² copper leads at ~0.000285 Ω so the wire dumps ~6.3 W at 150 A while XT90 connectors still run hotter.[^129][^130]
- **Refresh aging welders.** Replacing consumables on a Glitter 811H restored consistent 0.25–0.30 mm copper welds, proving the platform can rival KWeld output when tips and cables are renewed.[^131]
- **Pack stacking for minibikes:** Haku is combining 20 S 12 P P42A and 20 S 10 P 40T packs to chase ~90 Ah on a minibike while watching weight.
  - a reminder to balance chemistry choices against target discharge (~35 A per cell) when packaging multi-pack builds.[^132]
- **Prep salvage cells gently:** When stripping old solder from reclaimed P42A cans, use carbide burrs, copper braid, or metal cutoff wheels sparingly.
  - overheating the top insulator ruins the cell, so plan for fresh Bak 45D stock if cleanup goes sideways and stage TVS repairs for welders before diving in.[^133]
- **Wrap and isolate cells:** Heat-shrink each 21700, add Kapton plus wax/fish-paper between parallels, sheath the finished pack in epoxy board and giant heat-shrink, and add a cradle strap so it slides in/out without scuffing the deck.[^134]
- **Document insulation stacks before sign-off:** Matte’s latest teardown shows Kapton backed with vulcanized fiber between parallels; reviewers now insist on photographing balance-lead routing (“the money shot”) before approving high-current packs.[^135]
- **Stop short of 100 % and insulate glued packs.** Leaving the final few percent uncharged extends life, and dense bricks need fish paper or tape added during gluing so abrasion and heat do not chew through wraps.[^136]
- **Balance lead soldering:** Flow ~0.5 s of 400 °C heat with solder paste so the copper strip soaks the thermal load.
  - short pulses keep cells cool while locking balance wires into the copper bus.[^137]
- **Telemetry cross-checks:** Pair CAN smart BMS data with VESC logs to validate current draw and spot calibration drift in shunt-based readings.[^7]
- **Stay in the longevity window:** Artem keeps commuter packs between roughly 20 % and 85 % (≈3.6–4.1 V/cell) and under 40–45 °C; sag beyond ~3 V or repeated 70 °C peaks can cut lifespan to ~400 cycles.[^138]
- **Probe cells with Kelvin leads.** Alligator clips and single-sense multimeters can show false 1.9 V dips at 20 A; clamp meters across the battery and use four-wire probes directly at the tabs before condemning P42A-class cells.[^139]
- **Finish work around positives:** Deburr nickel edges near cell tops and re-seat fishpaper before closing the pack.
  - sharp tabs have already pierced insulation on low-current power-bank builds.[^140]
- **Pair Kapton with structural insulation:** Builders lean on Kapton for moisture resistance, but it lacks thermal shielding.
  - add fish paper or other barriers on high-discharge packs to stop nickel from rubbing bare cans as seen in recent Dualtron teardowns.[^141]
- **Respect connector gender standards:** Keep female shells on live battery leads and reserve male housings for chargers or controller-side harnesses; QS10’s 10 mm bullets support ≈400 A but only if polarity is consistent across every build.[^142]
- **Print holders for heat, not looks.** PLA cradles slump once cells warm; switch to PETG or ASA around 230 °C/100 °C bed temps so 21700 honeycombs and Wildman bag sleds stay rigid in summer decks.[^143][^144]
- **Bond prints with non-melting adhesives.** Epoxy, cyanoacrylate, or specialty plastics glue PETG/PLA parts without warping them.
- 3M marine adhesive cures rock-solid; plan on mechanical removal or fresh holders during rework, and machine sub-millimetre pack notches before gluing because there is no “peel back” once it sets.[^3m_marine_glue]
- Salvaged military packs hide soldered busbars and even fasteners—budget time for full desoldering or dremel work instead of assuming bolts will back out cleanly.[^soldered_busbars]
  - ideal for reinforcing phone mounts and pack accessories.[^145]
- **Dress electrodes & stage practice stock.** Glitter 811H rigs reliably join 0.2 mm copper to nickel once the power is dialled back and probe tips are sharpened; builders rehearse on loose strip and dead cells, add a BMS before fielding real packs, and ignore myths that nickel-plated steel is acceptable for high-current copper sandwiches.[^146]
- **Manage KWELD super-cap banks.** Keep parallel capacitor stacks to four modules to avoid over-current faults, use switched resistor banks on dual Meanwell LRS-350-4.2 supplies for charging and bleeding, and plan active cooling because seven heat-shrink layers still leave weld pens too hot for long sessions.[^147]
- **Document capacity checks.** Time OEM chargers (≈1.7 Ah per hour on Xiaomi bricks) when vetting customer packs; a genuine 12 Ah module needs nearly seven hours from empty.[^148]
- **Log cell provenance.** Refurb lots from NKON (late-2021 Samsung 35E/50E) arrive graded and safe when treated like fresh stock; track batch codes and keep compression on pouch experiments so swelling doesn’t lift tabs.[^149]
- **Layer real insulation.
  - not packing tape.** High-current packs rely on Kapton, dual heat-shrink, fishpaper, and fiberglass tape; SUNKKO clamps keep Sicaflex-potted arrays aligned while the glue cures.[^150]
- **Skip household splice tricks.** WAGO-style blocks and soldering bullets while clamped in heatsinks left brittle joints and scorched insulation; tin leads with ≥40 W irons, keep strip lengths short (~10 mm), and size lighting looms with 16–18 AWG copper instead.[^151][^152]
- **Translate C-ratings into real amps.** Treat a single 10 AWG lead as a ~100 A conductor and paired 12 AWG wires as roughly 140 A; cross-check cell C-ratings with these limits before promising 20 S Xiaomi builds more current than the harness can carry.[^153]
- **Retire WAGO phase adapters.** House-wiring clamps have already melted under 150 A hub loads.
  - swap to soldered joints backed by AS150/EC8 connectors and proper heatshrink before buttoning up the deck.[^154]
- **Calibrate adjustable chargers.** Trim VR1 for output voltage, VR2 for charge current, and VR3 for cutoff while the pack sits partially discharged so you stop guessing and over-driving AliExpress supplies.[^155]
- **Know when BMSs sleep.** Happy BMS packs can latch their discharge MOSFETs off after reconnection; wake them with a brief charger tap before blaming wiring or the controller.[^156]
- **Protect LiPo experiments.** A Daly-protected 4 Ah LiPo sank to 0.5 V per cell when left unattended, killing €120 worth of cells.
  - treat LiPo scooters as supervised builds or upgrade the BMS hardware.[^157]
- **Quarantine failing budget packs immediately:** Bargain eBay modules that vent or reignite during recharge attempts should be submerged in water and scrapped.
  - continued charging risks burning down the entire scooter even in freezing weather.[^158]
- **Store lithium packs at mid-SOC in fire-resistant containers.** Water-damaged groups left at 100 % stayed depressed; Denis now parks large assemblies near 50 %, replaces suspect cells, and keeps them in LiPo-safe bags with extinguishers nearby to mitigate runaway risk.[^storage-bags]
- **Respect scooter charge-port limits.** Keep on-board charging near 2 A so the internal BMS handles the load, and top external packs off-scooter with dedicated 3 A+ chargers through their own leads when you need faster turnaround.[^charge-port-limit]

### 21700 Dimension Cheat Sheet

- **Samsung 50E:** ≈21.12 mm with wrap.
- **Molicel P42A:** ≈21.34 mm with wrap.
- **Lishen LR21700:** ≈21.4 mm with wrap.
- **LG M58T:** ≈21.6 mm bare / 21.43 mm unwrapped.
- **Takeaway:** Oversize 3D-printed honeycombs and test-fit sacrificial cells; Mirono still ends up sanding fixtures because “21 mm” holders crush real-world cans.[^159][^160]

### Busbar Fabrication Workflow

- **Skip diode “engraver” shortcuts.** Desktop diode lasers only mark copper.
  - they cannot slice 0.2 mm sheet cleanly
  - so plan on industrial CO₂ hardware or go manual by drilling relief holes, following the outline with a coping/“leaf” saw, and cleaning edges with heavy-duty shears and files. Budget time rather than gambling on hobby engravers that leave ragged busbars.[^161]
- **Treat high-power lasers like industrial tools.** Multi-kilowatt beams blind observers instantly even off-reflections; any CO₂ upgrade needs full enclosures, interlocks, filtered camera monitoring, and PPE before you power it up next to pack builds.[^162]
- **Log copper-on-steel overlay settings.** PuneDir’s trials stacked 0.10 mm copper under 0.15 mm nickel at roughly 60–70 J; recording weld energy, probe spacing, and peel tests helps others repeat the plated-steel recipe without scorching cells.[^163]
- **Respect nickel’s 8 A ceiling.** Single-layer 0.2 mm nickel strips start cooking around 8 A per cell on performance packs.
  - step up to doubled nickel or copper busbars before chasing higher discharge targets.[^164]
- **Budget capable welders for copper.** Veterans keep Sunko 801D, Glitter 811-class rigs, or kWeld benches handy because budget 801A welders struggle with thick copper; buy or borrow proper gear instead of fighting underpowered tools.[^165]

### Enclosure Materials & Insulation

- **Treat carbon-fibre PETG as conductive until proven otherwise.** Builders still need proper resistivity tests.
  - keep prints away from live busbars until a megohmmeter confirms the carbon fill won’t leak current at pack voltage.[^166]

### Charging Connectors & Fast-Charge Planning

- **Match connectors to charge current.** XT90 anti-spark plugs stay reliable on 72 V packs when the charger’s current remains modest, but crews jump to XLR or QS8 hardware once charge rates exceed ~40–50 A to keep temperature rise in check.[^167]
- **Fuse the charge lead, not the plug.** Inline fusing lets low-current faults clear quickly; connector-mounted fuses react too slowly for scooter charge loops.[^168]
- **Reality-check community fast-charging.** Builders span everything from 12 A on 25 Ah commuter packs to 50 A on 44 Ah race batteries, so size wiring, connectors, and cooling for the highest rate you intend to run.[^169]

### Mounting & Housing Patterns

- **Prototype harness guides cheaply.** Builders mock up deck layouts with cardboard brackets before printing TPU/PETG fixtures, weighing Bambu P1P versus Ender 3 SE ownership while outsourcing large ASA/PEEK parts to avoid €1,500 machines.[^170]
- **Design footrests for moving hardware.** Monorim spring clamps printed in PETG at 100 % infill.
  - or even 70 % PLA when geometry distributes load
  - survived curb jumps, underscoring that clever design beats brute-force material swaps.[^171]
- **Print in-place frames for strength, not speed.** Print-in-place battery sleds need 100 % infill PETG (or stronger) plus fiberglass skins.
  - low-infill PLA softens in the sun and won’t protect the pack in a crash.[^172]
- **Armor deck-mounted conduits.** Twin 10S packs strapped along the deck need metal shielding and permanent wiring.
  - open conduit runs are “self-propelled bombs” unless the housing resists impacts and stays wired for continuous duty.[^173]
- **Overbuild bag brackets.** Wildman bag packs now use eight screw/wide-washer mounts, fiberglass sleeving, and interior foam so cells can’t chafe on hardware or eject during pothole hits.[^174]
- **Expect tight tolerances.** A 13S5P/16S3P 21700 stack just fits a 3 L Wildman when you skip holders, while 13S4P assemblies barely squeeze into 2–3 L shells.
  - plan for custom spacers, cardboard liners, and printed cages before drilling the pack.[^175][^176]
- **Upsize connectors for 300 A math.** Once current calculators spit out 300 A-plus targets, abandon twin XT90 leads for QS8 anti-sparks, 4 AWG cabling, and ring terminals.
  - reserve XT90s for charge ports and sub-100 A cruise loads.[^177]
- **Account for honeycomb growth.** Printed honeycomb holders add roughly 3 cm to a 20 S stick thanks to 1.5 mm walls.
  - verify deck clearance and inspect any shipped pack with crushed heat-shrink or stray metal before trusting it on a ride.[^178]
- **Retire fatigued brackets.** Heavy 13S packs crack 3D-printed rear supports near the rear bolt; inspect and replace printed mounts routinely or swap to metal before pushing high-speed builds.[^179]
- **Budget deck spacers for Zero 10X builds.** 20 S 7 P packs plus dual ESCs fit once you add ≈45 mm of deck spacing; G30 owners manage 18 S 5 P internally, but foam thicker than ~0.5 mm lets cells walk in holderless layouts.[^180]
- Zero 10X owners logged 360 × 133 × 62 mm beneath the carbon deck—ample for bespoke 20 S6 P/20 S7 P packs once controllers relocate or rails are removed.[^zero10x_dims]
- **Map Xiaomi sleeper layouts.** Gabe’s 20 S 8 P Pro 2 build splits cells between deck and bag, prints 35–36 mm spacers, reroutes phases, and trims foam so dual controllers and the pack coexist without killing ground clearance.[^181]

### Salvage & Pack Handling Lessons

- **Dyson V8 module recovery.** Vacuum packs mix 20700/21700/18650 cans; Gabe’s teardown shows V8 bricks house 6 s 1 p Molicels that often revive after reflashing the PIC with a Pickit 3 before rewelding the case.[^182]
- **Toss the hobby ESR pens.** Cheap handheld IR testers mis-rank salvaged cells—spend ~€20 on a dedicated meter before sorting reclaimed stock.[^183]
- **Plan for encapsulated fleet packs.** Ninebot rental batteries bury their BMS inside silicone potting; expect to chisel sealant or swap a fresh board because resets are impossible while encapsulated.[^15]
- **Retire leaky Navee packs.** Salvaged Navee N65 modules have shown leaking cells around 900 km; builders now plan full Aspilsan replacements or scrap the platform rather than risk venting packs.[^184]
- **Treat bargain “Ultrafire” packs as a structural hazard.** A fatal elevator blaze traced to an e-bike stuffed with dubious Ultrafire cells reminded the community to isolate DIY packs from living spaces, add vent paths, and respect condo/building bans before charging indoors.[^185]
- **Plan indoor storage like a fire event.** Stash commuter packs inside vented steel cases, reserve LiFePO₄ bricks for stationary 12 V supplies, and treat reclaimed BAK cells with 30–40 mΩ internal resistance as ≈30 A-per-7 P limits rather than high-discharge heroes.[^186]
- **Audit copper sandwiches carefully.** When you stack 0.1–0.2 mm copper with 0.15 mm nickel, test on dead cells first, skip nickel-plated strip on top, and only add flux if the pack will stay open.
  - early Glitter 811 batches even latched MOSFETs “on,” so document tuning before sealing the pack.[^187]
- **Segregate scooters in storage.** A premium-branded Blade/Teverun pack still ignited during charging.
  - never top packs unattended and park builds apart to limit collateral fire damage.[^188]
- **Log Aspilsan thermal limits.** Early A28 tests hit >90 °C at 10–15 A while LG M26 cells on the same rig stayed near 40 °C.
  - don’t parallel chemistries without temperature data.[^189]
- **Budget extra time for soldered salvage packs.** Military surplus modules arrived with soldered busbars and even fasteners, forcing full desoldering or dremel work instead of quick bolt removal.[^190]
- **Scrap waterlogged LG M26 stock.** Builders binned cells that took on water rather than risk corrosion-induced failures in new high-capacity packs.[^191]
- **Leverage welded 50E clear-outs.** Surplus Samsung 50E modules pre-welded for robots have dropped near $0.80 per cell when you buy 2,000+, making them worthwhile commuters after full inspection and re-termination.[^192]
- A dropped Nordbot 13 S pack lost an entire parallel pair and had to be rebuilt as 12 S—keep dense wraps, cell insulators, and cautious transport habits even after packs survive high-current testing.[^nordbot_drop]
- **Avoid grinders on aluminum shells.** Score the silicone bead with a utility knife, brace the enclosure in a vise, and drive the cell brick out with a wooden drift from the non-BMS end to preserve wiring.[^16]
- **Treat 0.1 mm nickel stacks like structural parts.** Double layers safely carry ≈20 A BMS currents, but only when bonded with multiple high-energy weld strikes.
  - thin hot glue fails once packs warm.[^17]
- **Triage refurb packs methodically.** Voltage swings on a 2 A charger signal mismatched cell groups.
  - dismantle, capacity/IR-test each cell, regroup by mileage, and expect degraded cells to keep worsening even after balancing.[^193]
- **Invest in training before welding.** Veterans keep Micah Toll’s handbook on the bench so new builders understand failure modes before touching live cells.[^18]
- **Model builds around stock chemistries.** Xiaomi packs routinely ship with LG M26 or blue EVE 18650 cells; use those discharge curves when calculating performance instead of optimistic MJ1 assumptions.[^19]
- **Distribute shoulder-bag loads.** Add thin aluminum plates outside fiberglass fire sleeves to spread weight and shield packs from direct flame when slinging externals over a shoulder.[^20]
- **Store loose cells smartly.** Keep unused cells near 3.3 V in a cool spot and rotate bargain batches quickly.
  - capacity drifts even in storage boxes.[^194]
- **Mount external bags off the swingarm.** Hanging heavy packs from the folding joint beats the steering head to death; bolt shelves to the swingarm so the folding mechanism isn’t bearing the load.[^195]

## Action Checklist

1. **Lock sourcing** – secure cell batches (with customs paperwork) before welding to avoid chemistry mismatches mid-build.[^1][^2]
2. **Stage tooling** – confirm welder calibration with sacrificial strips and schedule maintenance (cleaning, electrode dressing) ahead of production days.[^3][^10]
3. **Model pack fitment** – dry-fit modules in CAD or cardboard using deck measurements (e.g., 48.5 cm × 18.1 cm for Dualtron Achilleus) to plan controller relocation.[^8]
4. **Budget protection gear** – purchase BMS units, fuses, QS8 connectors, and spare harness parts before tariffs or stockouts force redesigns.[^5][^7][^9]
5. **Document performance** – archive discharge/charge test data, weld logs, and thermal profiles so future revisions start from validated baselines.[^1][^6][^10]

## Source Notes

[^ip009-m26]: Mixing grey and purple LG M26 cells proved acceptable once each parallel group was matched on internal resistance.[^196]
[^ip009-p42a]: Builders saw little advantage in P42A packs on scooters limited to ~120 A battery draw because 50H motors saturated around 60 A battery current on 20 S builds.[^197]
[^ip009-asacf]: Custom ASA‑CF holders demand heated chambers but deliver very rigid packs at roughly €50 per 750 g of filament.
  - about twice the cost of standard ASA.[^198]
[^ip009-xt90]: XT90S anti-spark plugs failed quickly under scooter duty, pushing builders toward QS8 connectors for reliability.[^199]
[^ip009-40pl]: Community testing pegs EVE 40PL cells at 45–70 A continuous with ~60 % capacity remaining after 300 cycles at 30 A, far below marketing claims.[^200]
[^ip009-parallel]: Running range-extender packs with independent BMS boards works only when voltages align; a tripped board can dump the entire load on the others and overstress them instantly.[^201]
[^ip010-28s]: Apollo Phantom builders were told to skip daisy-chaining 14 S packs in series and instead commission purpose-built 28 S 5 P packs with dedicated ANT BMS hardware to avoid mismatch faults.[^202]
[^ip010-amp-gauge]: Cable debates pegged silicone 12 AWG at roughly 100 A for short bursts and dismissed 8 AWG “300–400 A continuous” marketing claims without real thermal data.
  - route leads intelligently instead of trusting spec-sheet hype.[^203]
[^ip009-regen]: Heavy 17 S builds reported VESC regen respecting the 71.4 V full-charge voltage, keeping 72 V setpoints within limits.[^204]
[^ip009-deepdis]: A JK-managed pack left at 57 V lost BMS communications and damaged cells, underscoring the risk of deep discharge on extender packs.[^205]
[^ip009-active]: Active balancing boards equalised large packs in about an hour compared with days on passive JBD balancing.[^206]
[^ip009-bms-app]: Builders warned that keeping smart-BMS apps online invites tampering and even password changes can break connectivity, so many keep packs offline.[^207]
[^ip009-jk-mosfet]: JK’s app lets riders disable the discharge MOSFET to keep scooters from waking while parked.[^208]
[^ip009-compact-bms]: Even cramped 10 S builds drawing 30–45 A per cell rely on JK/JBD 100 A smart boards (with ANT backups) for protection and telemetry.[^209]
[^ip009-ant-down]: Down-populating a 30 S ANT board onto a 22 S harness produced bogus voltages until the pinout and app settings were updated for the shorter stack.[^210]
[^ip009-epoxy]: Zero 10X pack builders slid thin epoxy sheets between balance harnesses and copper busbars when plastic holders would not fit, preserving insulation without added thickness.[^211]
[^ip009-silicone]: Rebuilt honeycomb packs benefited from silicone spacers plus fishpaper or Kapton between series rows when hot gluing groups.[^212]
[^ip009-hotmelt]: Hot-melt glue softens around 80–90 °C and barely adheres to cold cans.
  - treat it as a temporary locator before adding holders or silicone reinforcement.[^213]
[^ip009-steel]: Using twin steel strips over nickel supported roughly 8 A per cell in LG M26 packs while keeping 17 P layouts near 10–11 kW.[^214]
[^ip009-copperthick]: Builders reminded AYO that 0.1 mm copper sheet is required for busbars; 0.01 mm foil tears under welding current.[^215]
[^ip009-chamfer]: Copper strip edges near positive terminals can slice insulation under heavy load, so chamfering is now standard before shrink-wrapping.[^216]
[^ip009-holders]: Multiple builders reiterated that tight-tolerance 3D-printed holders (PETG/ASA/ABS) improve spacing and thermal paths over hot glue, especially for long packs.[^217]
[^ip009-makaron]: Double-layer “makaron” shrink can replace fishpaper between rows but still scuffs faster, so veterans still prefer fishpaper for series barriers.[^218]
[^ip009-g30]: Squeezing a 20 S 6 P 21700 pack plus twin MP2 controllers into a G30 required a 36 mm deck extender and ~1 mm of grinding around the rail opening.[^219]
[^denis-ali-lottery]: Source: knowledge/notes/denis_all_part02_review.md†L993-L993
[^denis-kweld-standard]: Source: knowledge/notes/denis_all_part02_review.md†L994-L994
[^ip009-fiberboard]: Sliding thin fiberboard into 0.20–0.25 mm copper folds keeps the busbars separated until epoxy spacers land.[^220]
[^ip009-barley]: Builders finish each series strip with barley paper so heavy copper stacks don’t chafe insulation when the pack flexes.[^221]
[^ip009-pretension]: Pre-tensioning copper by bending it over a table edge keeps springy sheets seated once the first welds land.[^222]
[^ip009-bag]: Twin-pack minibike builds now reinforce external battery bags with tailored straps or rigid bases after sagging stressed the frame mid-ride.[^223]
[^ip009-g30blueprint]: The 20 S 12 P twin-MP2 concept stacks cells to roughly 14.5 cm, stands the smart BMS vertically ahead of the brick, and feeds dual QS8 harnesses with parallel 8 AWG leads while a welded rear controller box keeps the deck arches intact.[^224]
[^ip009-flush]: Veterans prefer flush cutters for tearing down welded packs, leaving flattened remnants that accept new strip without grinding plating away.[^225]
[^ip009-marine]: Adhesive-lined “marine” heat-shrink grips bullet connectors far better than thin sleeves that slide off under load.[^226]
[^ip009-ayo]: 🇪🇸AYO#74 secures rebuilt modules with hot silicone and glass filament tape so vibration cannot fret the wraps.[^227]
[^ip009-laotie240]: Switching from a stand-up to a seated Laotie frame let Haku fold a 240-cell pack into the main chassis instead of a bolt-on extender, albeit with heavy labor and safety cautions.[^228]
[^ip009-811h-refresh]: Fresh electrodes and cables brought a Glitter 811H back to consistent 0.25–0.30 mm copper welds, keeping it competitive with KWeld rigs despite customs limits.[^229]
[^ip009-solder]: Leaded solder reels are still arriving via AliExpress despite customs checks, letting builders complete 13S8P packs once shipments clear.[^230]
[^1]: Salvaged Stark Varg 50PL modules pricing and 60 A/15 A validation results.[^231]
[^varg-salvage]: Jose is stripping lightly used P45B cells from Stark Varg packs for roughly €1.2 each and only green-lights them after confirming cycle health, while Rob Ver praises the tabless layout for keeping pack temps within ≈3 °C of ambient under load.[^44]
[^2]: EU vs. US 50PL pricing, customs considerations, and grade-A assurances on rebranded cells.[^232]
[^3]: Spot welder cost comparison between 90 € generics and reliable K-Weld/Glitter setups for 0.1 mm copper joints.[^233]
[^argon-braze]: Tin-brazed copper busbars stayed low resistance only when shielded with argon; exposed copper/nickel sandwiches have corroded in humid storage within a few years.[^234]
[^4]: High-output pack examples (22 S10/11 P P45B, 20 S8 P Molicel) and their controller pairings.[^235]
[^5]: Tariff-driven QS8 and cell stockpiling strategies for US builders.[^236]
[^6]: Haku’s 20 S10 P Samsung 40T build, busbar thickness, and BMS upgrade warning against mixed chemistries.[^237]
[^7]: Continuous and peak current expectations plus current BMS limitations for 22 S packs.[^238][^239]
[^8]: Dualtron Achilleus deck dimensions and mounting implications for high-current batteries.[^240]
[^9]: Thermal envelope reminders (≤45 °C controller, ≤100 °C stator) and conductor upgrades for 400 A pursuits.[^241][^242]
[^10]: Glitter 811A maintenance steps to recover 4.4 kA output and recommended rip-testing routine.[^243]
[^11]: Guidance on commissioning trusted builders to bypass tooling purchases for single packs.[^244]
[^12]: Nami 22 S 10 P layout planning with CNC/3D-printed supports.[^245]
[^13]: G3 30 S conversion constraints and required chassis modifications.[^246]
[^14]: Rejection of hot glue for 22 S 10 P packs and emphasis on structural spacers/adhesives.[^247]
[^15]: Fleet Ninebot G30 rental packs arrive fully potted, hiding the BMS and forcing either destructive teardown or outright replacement during refurb work.[^248]
[^16]: Recommended aluminum-pack teardown workflow.
  - score silicone, secure the case, and drive cells out with a wooden dowel from the non-BMS side to keep harnesses intact.[^249]
[^17]: Double-stacked 0.1 mm × 8 mm nickel supports 20 A BMS loads only when welded with multiple high-power strikes; low-temp hot glue fails once packs heat during use.[^250]
[^18]: Community reminder to read Micah Toll’s battery handbook before building packs to avoid costly mistakes.[^251]
[^19]: Stock Xiaomi batteries typically use LG M26 or blue EVE 18650 cells.
  - model upgrades around those chemistries for realistic performance estimates.[^252]
[^20]: Shoulder-bag pack carriers add thin aluminum plates outside fiberglass sleeves to diffuse heat and prevent straps from pinching cells during transport.[^253]
[^21]: Patrick’s 100 A discharge logs showed EVE 40PL prismatic cells holding 3.0 V for 62 s while Molicel P45B packs sagged to 2.78 V after 44 s.[^254]
[^22]: Zero 10X builders fitting 20 S7 P packs plus dual controllers documented the need for a 45 mm deck extender, added insulation, and tightly managed wiring to avoid shorts.[^255]
[^23]: Community price tracking logged 0.1 × 200 × 5,000 mm nickel-copper laminate jumping from roughly €15 to €45 per roll in a matter of weeks.[^256]
[^24]: High-current motorcycle builds now run three BMS boards in parallel so massive 20 S24 P packs can share hundreds of amps without single-board cutoffs.[^257]
[^25]: NetworkDir previewed Molicel’s XA-series race cells at ≈2.6 Ah, ~1.5–2 mΩ, and 125 A charge / 250 A discharge capability as the next step beyond P45B once they reach production.[^258]
[^26]: GABE’s Xiaomi Pro 2 build squeezed a 13 S8 P pack (≈1.15 kWh) plus side-mounted BMS after relocating the ESC and carefully stacking cells without holders.[^259]
[^27]: Cihan’s hunt for thermally conductive foam ended with veterans recommending tiny insulating pads and open air gaps instead of dense foam blocks to avoid trapping heat around deck packs.[^260]
[^28]: PuneDir’s steel battery box missed his Hyosung frame opening by 1 cm, stranding the build and underscoring the need to template enclosures before welding or ordering heavy shells.[^261]
[^29]: Community fast-charge debates noted that 40 C fills on 20 S6 P packs would need roughly 11 kW from three-phase mains.
  - far beyond household 10 A circuits
  - so “minutes-long” charges demand industrial power.[^262]
[^30]: Builders weighing charge ports recommended IP67-rated Cnlinko LP16 connectors for weatherproof installs, while others stick with XT60 for 20 A charging when water ingress is not a concern.[^263]
[^31]: Turkish riders confirmed a new €30 personal-import ceiling that blocks direct purchases of scooters, motors, and welders, forcing reliance on licensed importers or accepting 2–3× local markups.[^264]
[^32]: Yamal reminded builders to configure VESC Tool for the combined series count (e.g., 20 S) even when chaining two 10 S packs so telemetry and cutoffs remain accurate.[^265]
[^33]: Glitter 811H spot welders have arrived with dead MOSFETs and half-charged banks; after repairs they still weld 0.2 mm copper-on-nickel, while kWeld handles 0.15 mm copper around 75 J but overheats during continuous runs.[^266]
[^34]: Paolo shifted heavy pack fabrication to TIG welding with pulse controllers, arguing it avoids thermal sag and unlocks thicker bus work faster than resistance welders.[^267]
[^35]: Grinding nickel off reclaimed cells has already ignited cells.
  - builders now avoid abrasive removal and document arc flashes from unstable Glitter welders to reinforce the fire risk.[^268]
[^36]: A Spanish NAMI rider paralleled LG 40T sticks with M50LT groups to extend range but now caps draw and leans on a 150 A smart BMS so the lower-capacity chemistry doesn’t overheat or drift out of balance.[^269]
[^37]: Budget “smart” BMS boards shipped twice the size of ANT units while the 21 S 100 A JBD still fits between 18650 rows and cost ~€45 during recent sales, making it the better fit for tight decks.[^270]
[^docreate]: Cihan priced the Docreate DO-02 capacitor welder around $108 delivered to Turkey (less with coupons) and confirmed ~0.36 mΩ capacitor ESR via teardown notes; peers recommend the foot-pedal bundle or Glitter 801D when welding only thin nickel.[^271]
[^kweld-lipo]: kWeld owners retired car batteries after a few welds sagged voltage; CNHL 4S 9.5 Ah hardcase packs and other high-C LiPos sustained 2 kA pulses while old RC packs and power banks overheated despite extra heatsinks.[^67]
[^denis-pricing]: [^272]
[^denis-pricing]: [^272]
[^aliexpress-sand]: [^273]
[^tudor-common]: [^274]
[^ali-pack-warning-diy]: [^275]
[^bms_drift_check]: Source: knowledge/notes/all_part01_review.md†L546-L546
[^lab-gear]: [^276]
[^common-port-chat]: [^274][^277]
[^uart485-diy]: [^278]
[^laudation-diy]: [^279]
[^m365krakow]: [^280]
[^cnhl-booster]: CNHL and GNB 140 C–180 C LiPo bricks power kWeld launches and scooter booster packs but drain after a single sprint.
  - parallel packs for repeated hits.[^281]
[^holder-clamp]: Threaded rods, dots of superglue, and even duct tape keep PETG holders aligned until final wraps; clear packing tape is the last resort when Kapton runs out.[^282]
[^storage-bags]: [^283]
[^charge-port-limit]: [^284]
[^bms-v3]: [^285]

## Copper Busbar Best Practices

- **Braze copper busbars with shielding gas.** Builders warned that nickel–copper "sandwich" welds oxidize and fail after a few years; brazing with tin while flooding the joint with argon (as micro-TIG stations do) keeps resistance low, whereas humidity alone can trigger corrosion if the pack isn't sealed.[^busbar_braze]
- **Use proper insulation layers, not packing tape.** Battery builders reiterated that Kapton, double heat-shrink, fishpaper, and fiberglass tape are the minimum for high-current packs.
  - clear packing tape alone cannot stop rail wear-through, and purpose-made clamps such as the SUNKKO fixture keep parallel groups aligned while you reglue Sicaflex-potted arrays.[^insulation_layers]
- **20 S 5 P decks demand machining.** Even experienced pack builders said a 20 S 5 P 21700 layout only fits a G30 deck after CNC work; newcomers are steered toward 16–18 S designs or professional builds to avoid compromised clearances and shipping headaches.[^20s5p_fit]
- **0.15 mm pure nickel still works.
  - within limits.** Mirono signs off on 0.15 mm strip in a W-bridge layout for ~40 A scooter packs provided per-cell current stays under the strip’s rating, sparing builders from copper busbars on moderate loads.[^286]
- **Laminate copper when welders lack punch.** Hackintoshhhh now stacks two 0.1 mm copper–nickel sheets instead of a single 0.2 mm strip because his Glitter 801D welder cannot penetrate thicker busbars reliably.
  - an approachable workaround until higher-output welders arrive.[^287]
- **Bridge big packs with multiple jumpers.** 16 S8 P layouts fed by just two series jumpers overheat interior rows; add extra links or second-layer plates so every parallel group shares load evenly.[^busbar_bridge]
- **Fold copper after soldering main leads.** Builders now solder main outputs to the copper strip before welding, fold the metal over as a double-thickness busbar, cover as many cell tops as possible, and insulate with fish paper or Kapton before sealing the pack.[^busbar_layout]

## Cell Internal Resistance Calibration

- **Calibrate 1 kHz AC internal-resistance meters with ~20 mΩ references.** The crew uses wire shunts or resistor networks to zero handheld testers, then expects fresh P42A cells around 8 mΩ, Samsung 50S ≈10 mΩ, first-generation 50E nearer 22–28 mΩ, and abused cells well above that, reminding each other that absolute values drift between instruments even when the relative spread remains useful.[^ir_calibration]

## Source Notes

[^busbar_braze]: Copper busbar brazing with shielding gas to prevent oxidation failures.[^234]
[^insulation_layers]: Proper battery insulation materials and parallel-group alignment techniques.[^150]
[^20s5p_fit]: Source: data/vesc_help_group/text_slices/input_part004.txt†L21277-L21290
[^20s5p_fit]: 20 S 5 P pack fitment challenges in G30 decks.[^288]
[^busbar_bridge]: Source: knowledge/notes/input_part002_review.md†L606-L607
[^busbar_layout]: Source: knowledge/notes/input_part002_review.md†L607-L608
[^ir_calibration]: Cell internal resistance measurement and calibration procedures.[^289]


## References

[^1]: Source: knowledge/notes/input_part007_review.md†L301-L303
[^2]: Source: knowledge/notes/input_part007_review.md†L301-L307
[^3]: Source: knowledge/notes/input_part007_review.md†L321-L325
[^4]: Source: knowledge/notes/input_part007_review.md†L309-L317
[^5]: Source: knowledge/notes/input_part012_review.md†L80-L80
[^6]: Source: knowledge/notes/all_part01_review.md†L316-L316
[^7]: Source: knowledge/notes/all_part01_review.md†L358-L358
[^8]: Source: knowledge/notes/all_part01_review.md†L359-L359
[^9]: Source: knowledge/notes/denis_all_part02_review.md†L521-L522
[^10]: Source: knowledge/notes/all_part01_review.md†L360-L363
[^11]: Source: knowledge/notes/input_part004_review.md†L216-L216
[^12]: Source: knowledge/notes/input_part004_review.md†L369-L369
[^13]: Source: knowledge/notes/input_part011_review.md†L221-L227
[^14]: Source: knowledge/notes/input_part004_review.md†L383-L383
[^15]: Source: knowledge/notes/input_part011_review.md†L352-L356
[^16]: Source: knowledge/notes/input_part011_review.md†L217-L224
[^17]: Source: knowledge/notes/input_part011_review.md†L225-L231
[^18]: Source: knowledge/notes/input_part011_review.md†L231-L238
[^19]: Source: data/vesc_help_group/text_slices/input_part007.txt†L271-L277
[^20]: Source: knowledge/notes/input_part007_review.md†L477-L477
[^21]: Source: knowledge/notes/input_part007_review.md†L478-L478
[^22]: Source: knowledge/notes/input_part004_review.md†L236-L236
[^23]: Source: knowledge/notes/all_part01_review.md†L319-L319
[^24]: Source: data/vesc_help_group/text_slices/input_part001.txt†L1603-L1655
[^25]: Source: knowledge/notes/input_part007_review.md†L218-L219
[^26]: Source: data/vesc_help_group/text_slices/input_part007.txt†L236-L239
[^27]: Source: data/vesc_help_group/text_slices/input_part007.txt†L252-L263
[^28]: Source: data/vesc_help_group/text_slices/input_part007.txt†L241-L247
[^29]: Source: data/vesc_help_group/text_slices/input_part007.txt†L273-L277
[^30]: Source: knowledge/notes/input_part013_review.md†L55-L55
[^31]: Source: knowledge/notes/input_part013_review.md†L400-L407
[^32]: Source: knowledge/notes/input_part013_review.md†L56-L56
[^33]: Source: knowledge/notes/input_part013_review.md†L205-L205
[^34]: Source: knowledge/notes/input_part013_review.md†L329-L334
[^35]: Source: knowledge/notes/input_part013_review.md†L96-L96
[^36]: Source: knowledge/notes/input_part001_review.md†L686-L687
[^37]: Source: knowledge/notes/input_part006_review.md†L104-L104
[^nkon-pure]: Source: knowledge/notes/input_part006_review.md†L28-L28
[^38]: Source: knowledge/notes/input_part001_review.md†L695-L696
[^39]: Source: knowledge/notes/input_part000_review.md†L148-L150
[^40]: Source: knowledge/notes/input_part000_review.md†L606-L607
[^41]: Source: knowledge/notes/input_part000_review.md†L694-L695
[^42]: Source: knowledge/notes/input_part000_review.md†L118-L118
[^43]: Source: data/vesc_help_group/text_slices/input_part000.txt†L17309-L17312
[^44]: Source: knowledge/notes/input_part013_review.md†L57-L57
[^thick-copper-tooling]: Source: knowledge/notes/input_part006_review.md†L29-L29
[^45]: Source: knowledge/notes/input_part014_review.md†L6601-L6633
[^46]: Source: knowledge/notes/input_part014_review.md†L6637-L6642
[^47]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24420-L24451
[^48]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24380-L24405
[^49]: Source: data/vesc_help_group/text_slices/input_part005.txt†L22670-L22699
[^50]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24420-L24441
[^51]: Source: data/vesc_help_group/text_slices/input_part005.txt†L22423-L22458
[^52]: Source: knowledge/notes/input_part005_review.md†L605-L605
[^53]: Source: knowledge/notes/input_part007_review.md†L229-L229
[^54]: Source: knowledge/notes/input_part005_review.md†L513-L513
[^55]: Source: knowledge/notes/input_part011_review.md†L47-L47
[^56]: Source: knowledge/notes/input_part005_review.md†L579-L579
[^57]: Source: knowledge/notes/input_part011_review.md†L424-L425
[^58]: Source: knowledge/notes/input_part007_review.md†L529-L529
[^59]: Source: knowledge/notes/denis_all_part02_review.md†L76-L77
[^60]: Source: knowledge/notes/input_part011_review.md†L369-L374
[^denis-highcurrent-solder]: Source: knowledge/notes/denis_all_part02_review.md†L714-L714
[^denis-desolder]: Source: knowledge/notes/denis_all_part02_review.md†L1090-L1090
[^61]: Source: knowledge/notes/input_part010_review.md†L257-L258
[^62]: Source: knowledge/notes/input_part006_review.md†L306-L306
[^63]: Source: data/vesc_help_group/text_slices/input_part001.txt†L25425-L25518
[^64]: Source: data/vesc_help_group/text_slices/input_part001.txt†L25469-L25490
[^65]: Source: knowledge/notes/input_part005_review.md†L115-L116
[^66]: Source: knowledge/notes/input_part005_review.md†L117-L117
[^67]: Source: knowledge/notes/input_part008_review.md†L237-L238
[^68]: Source: data/vesc_help_group/text_slices/input_part009.txt†L2001-L2056
[^69]: Source: data/vesc_help_group/text_slices/input_part009.txt†L2959-L2960
[^70]: Source: data/vesc_help_group/text_slices/input_part009.txt†L5057-L5068
[^71]: Source: data/vesc_help_group/text_slices/input_part009.txt†L6203-L6239
[^72]: Source: knowledge/notes/input_part001_review.md†L604-L605
[^73]: Source: knowledge/notes/input_part001_review.md†L607-L608
[^74]: Source: knowledge/notes/input_part009_review.md†L374-L374
[^75]: Source: knowledge/notes/input_part005_review.md†L118-L118
[^76]: Source: knowledge/notes/input_part005_review.md†L352-L354
[^77]: Source: knowledge/notes/input_part006_review.md†L307-L307
[^78]: Source: knowledge/notes/input_part005_review.md†L145-L147
[^79]: Source: knowledge/notes/input_part005_review.md†L147-L151
[^80]: Source: knowledge/notes/input_part005_review.md†L160-L161
[^81]: Source: knowledge/notes/input_part005_review.md†L488-L490
[^82]: Source: knowledge/notes/input_part006_review.md†L358-L358
[^83]: Source: knowledge/notes/input_part005_review.md†L148-L148
[^84]: Source: knowledge/notes/input_part007_review.md†L445-L445
[^85]: Source: knowledge/notes/input_part009_review.md†L364-L365
[^86]: Source: knowledge/notes/input_part006_review.md†L382-L382
[^87]: Source: data/vesc_help_group/text_slices/input_part011.txt†L19293-L19294
[^88]: Source: data/vesc_help_group/text_slices/input_part011.txt†L19382-L19393
[^eleshop-follow]: Pending EleShop availability checks and post-repair feedback from GABE once the MP2 work wraps. Source: knowledge/notes/input_part011_review.md†L913-L913
[^89]: Source: knowledge/notes/input_part011_review.md†L801-L805
[^90]: Source: knowledge/notes/input_part011_review.md†L783-L787
[^91]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8851-L8913
[^92]: Source: knowledge/notes/input_part001_review.md†L689-L696
[^93]: Source: knowledge/notes/input_part005_review.md†L420-L422
[^94]: Source: knowledge/notes/input_part009_review.md†L362-L362
[^95]: Source: knowledge/notes/input_part009_review.md†L365-L365
[^96]: Source: knowledge/notes/input_part009_review.md†L375-L375
[^97]: Source: knowledge/notes/input_part009_review.md†L376-L376
[^98]: Source: knowledge/notes/input_part009_review.md†L321-L321
[^99]: Source: knowledge/notes/input_part009_review.md†L334-L334
[^100]: Source: knowledge/notes/input_part009_review.md†L382-L382
[^101]: Source: knowledge/notes/input_part010_review.md†L309-L310
[^102]: Source: knowledge/notes/input_part010_review.md†L388-L389
[^103]: Source: knowledge/notes/input_part006_review.md†L55-L55
[^104]: Source: knowledge/notes/input_part006_review.md†L56-L56
[^105]: Source: knowledge/notes/input_part006_review.md†L60-L60
[^106]: Source: knowledge/notes/input_part006_review.md†L57-L57
[^107]: Source: knowledge/notes/input_part006_review.md†L58-L58
[^108]: Source: knowledge/notes/input_part006_review.md†L59-L59
[^109]: Source: knowledge/notes/input_part006_review.md†L89-L89
[^110]: Source: knowledge/notes/input_part006_review.md†L90-L90
[^111]: Source: knowledge/notes/input_part006_review.md†L92-L92
[^112]: Source: knowledge/notes/input_part010_review.md†L394-L396
[^113]: Source: knowledge/notes/input_part011_review.md†L17-L20
[^114]: Source: knowledge/notes/input_part007_review.md†L315-L321
[^115]: Source: knowledge/notes/input_part007_review.md†L325-L329
[^116]: Source: knowledge/notes/input_part007_review.md†L329-L334
[^jk_balancer]: Source: knowledge/notes/input_part002_review.md†L610-L611
[^117]: Source: knowledge/notes/input_part007_review.md†L334-L336
[^118]: Source: knowledge/notes/input_part007_review.md†L336-L349
[^119]: Source: knowledge/notes/input_part007_review.md†L349-L353
[^120]: Source: knowledge/notes/input_part007_review.md†L353-L356
[^50e_abuse]: Source: knowledge/notes/input_part002_review.md†L535-L537
[^121]: Source: knowledge/notes/input_part008_review.md†L16198-L16266
[^122]: Source: knowledge/notes/input_part001_review.md†L94-L95
[^123]: Source: data/vesc_help_group/text_slices/input_part001.txt†L9376-L9399
[^124]: Source: knowledge/notes/input_part007_review.md†L443-L443
[^125]: Source: data/vesc_help_group/text_slices/input_part009.txt†L1343-L1352
[^126]: Source: data/vesc_help_group/text_slices/input_part009.txt†L1492-L1493
[^127]: Source: data/vesc_help_group/text_slices/input_part009.txt†L1489-L1495
[^128]: Source: data/vesc_help_group/text_slices/input_part009.txt†L18894-L18900
[^129]: Source: data/vesc_help_group/text_slices/input_part009.txt†L15852-L15879
[^130]: Source: data/vesc_help_group/text_slices/input_part009.txt†L16423-L16441
[^131]: Source: data/vesc_help_group/text_slices/input_part009.txt†L22014-L22016
[^132]: Source: data/vesc_help_group/text_slices/input_part009.txt†L20199-L20220
[^133]: Source: knowledge/notes/input_part011_review.md†L311-L319
[^134]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8927-L8933
[^135]: Source: knowledge/notes/input_part011_review.md†L352-L359
[^136]: Source: knowledge/notes/all_part01_review.md†L363-L363
[^qs8_chart]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24287-L24336
[^137]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8874-L8897
[^138]: Source: knowledge/notes/input_part001_review.md†L698-L699
[^139]: Source: knowledge/notes/input_part000_review.md†L605-L605
[^140]: Source: knowledge/notes/denis_all_part02_review.md†L122364-L122385
[^141]: Source: knowledge/notes/denis_all_part02_review.md†L357-L359
[^142]: Source: knowledge/notes/input_part011_review.md†L333-L338
[^143]: Source: knowledge/notes/denis_all_part02_review.md†L116230-L116236
[^144]: Source: knowledge/notes/denis_all_part02_review.md†L89665-L89696
[^145]: Source: knowledge/notes/input_part006_review.md†L81-L81
[^146]: Source: knowledge/notes/input_part006_review.md†L52-L54
[^147]: Source: knowledge/notes/input_part006_review.md†L55-L57
[^148]: Source: knowledge/notes/denis_all_part02_review.md†L98595-L98598
[^149]: Source: knowledge/notes/denis_all_part02_review.md†L97241-L97259
[^150]: Source: data/vesc_help_group/text_slices/input_part004.txt†L21252-L21324 and L21888-L21899
[^151]: Source: data/vesc_help_group/text_slices/input_part004.txt†L22724-L22760
[^152]: Source: data/vesc_help_group/text_slices/input_part004.txt†L22762-L22798
[^153]: Source: data/vesc_help_group/text_slices/input_part004.txt†L11470-L11499
[^154]: Source: data/vesc_help_group/text_slices/input_part004.txt†L17752-L17764 and L18123-L18139
[^155]: Source: data/vesc_help_group/text_slices/input_part004.txt†L17519-L17544
[^156]: Source: data/vesc_help_group/text_slices/input_part004.txt†L19788-L19840
[^157]: Source: data/vesc_help_group/text_slices/input_part004.txt†L15089-L15110
[^158]: Source: knowledge/notes/input_part011_review.md†L325-L329
[^159]: Source: data/vesc_help_group/text_slices/input_part007.txt†L283-L296
[^160]: Source: data/vesc_help_group/text_slices/input_part007.txt†L290-L290
[^161]: Source: data/vesc_help_group/text_slices/input_part007.txt†L542-L590
[^162]: Source: data/vesc_help_group/text_slices/input_part007.txt†L561-L584
[^163]: Source: knowledge/notes/input_part007_review.md†L517-L517
[^164]: Source: knowledge/notes/input_part006_review.md†L211-L211
[^165]: Source: knowledge/notes/input_part006_review.md†L212-L212
[^166]: Source: knowledge/notes/input_part007_review.md†L506-L506
[^167]: Source: knowledge/notes/input_part005_review.md†L61-L64
[^168]: Source: knowledge/notes/input_part005_review.md†L62-L64
[^169]: Source: knowledge/notes/input_part005_review.md†L63-L64
[^170]: Source: knowledge/notes/input_part005_review.md†L11-L14
[^171]: Source: knowledge/notes/input_part005_review.md†L72-L73
[^172]: Source: knowledge/notes/input_part005_review.md†L221-L222
[^173]: Source: knowledge/notes/denis_all_part02_review.md†L230-L234
[^174]: Source: knowledge/notes/denis_all_part02_review.md†L361-L362
[^175]: Source: knowledge/notes/denis_all_part02_review.md†L362-L363
[^176]: Source: knowledge/notes/denis_all_part02_review.md†L165-L165
[^177]: Source: knowledge/notes/input_part006_review.md†L276-L276
[^178]: Source: knowledge/notes/input_part005_review.md†L501-L501
[^179]: Source: knowledge/notes/denis_all_part02_review.md†L352-L352
[^180]: Source: knowledge/notes/input_part007_review.md†L442-L442
[^zero10x_dims]: Source: knowledge/notes/input_part002_review.md†L539-L540
[^181]: Source: knowledge/notes/input_part007_review.md†L476-L476
[^182]: Source: knowledge/notes/input_part007_review.md†L309-L311
[^183]: Source: knowledge/notes/input_part006_review.md†L245-L245
[^184]: Source: knowledge/notes/input_part008_review.md†L359-L359
[^185]: Source: knowledge/notes/input_part008_review.md†L601-L604
[^186]: Source: knowledge/notes/input_part005_review.md†L52-L55
[^187]: Source: knowledge/notes/input_part006_review.md†L246-L246
[^188]: Source: knowledge/notes/input_part006_review.md†L247-L247
[^189]: Source: knowledge/notes/input_part008_review.md†L15885-L15938
[^3m_marine_glue]: Source: knowledge/notes/input_part008_review.md†L395-L395
[^soldered_busbars]: Source: knowledge/notes/input_part008_review.md†L396-L396
[^190]: Source: knowledge/notes/input_part008_review.md†L395-L396
[^191]: Source: knowledge/notes/input_part008_review.md†L518-L522
[^192]: Source: knowledge/notes/input_part008_review.md†L500-L503
[^copper_plating_guard]: Source: knowledge/notes/input_part008_review.md†L409-L410
[^p42a_storage_tip]: Source: knowledge/notes/input_part008_review.md†L412-L413
[^electricpowa_prices]: Source: knowledge/notes/input_part008_review.md†L434-L435
[^eve40p_ir_fresh]: Source: knowledge/notes/input_part008_review.md†L460-L461
[^welded_50e_lots]: Source: knowledge/notes/input_part008_review.md†L462-L462
[^pune_scrap_m26]: Source: knowledge/notes/input_part008_review.md†L498-L499
[^nordbot_drop]: Source: knowledge/notes/input_part002_review.md†L602-L603
[^193]: Source: knowledge/notes/denis_all_part02_review.md†L333-L333
[^194]: Source: knowledge/notes/input_part007_review.md†L369-L369
[^195]: Source: knowledge/notes/input_part007_review.md†L368-L368
[^196]: Source: knowledge/notes/input_part009_review.md†L19-L19
[^197]: Source: knowledge/notes/input_part009_review.md†L20-L20
[^198]: Source: knowledge/notes/input_part009_review.md†L21-L21
[^199]: Source: knowledge/notes/input_part009_review.md†L22-L22
[^200]: Source: knowledge/notes/input_part009_review.md†L39-L39
[^201]: Source: knowledge/notes/input_part009_review.md†L23-L23
[^202]: Source: knowledge/notes/input_part010_review.md†L242-L243
[^203]: Source: knowledge/notes/input_part010_review.md†L257-L259
[^204]: Source: knowledge/notes/input_part009_review.md†L24-L24
[^205]: Source: knowledge/notes/input_part009_review.md†L29-L29
[^206]: Source: knowledge/notes/input_part009_review.md†L27-L27
[^207]: Source: knowledge/notes/input_part009_review.md†L33-L33
[^208]: Source: knowledge/notes/input_part009_review.md†L35-L35
[^209]: Source: knowledge/notes/input_part009_review.md†L36-L36
[^shrink_layers]: Source: knowledge/notes/input_part002_review.md†L671-L672
[^pack_clamp]: Source: knowledge/notes/input_part002_review.md†L673-L673
[^210]: Source: knowledge/notes/input_part009_review.md†L403-L403
[^211]: Source: knowledge/notes/input_part009_review.md†L18-L18
[^212]: Source: knowledge/notes/input_part009_review.md†L25-L25
[^213]: Source: data/vesc_help_group/text_slices/input_part009.txt†L7754-L7760
[^214]: Source: knowledge/notes/input_part009_review.md†L26-L26
[^215]: Source: knowledge/notes/input_part009_review.md†L28-L28
[^216]: Source: knowledge/notes/input_part009_review.md†L30-L30
[^217]: Source: knowledge/notes/input_part009_review.md†L31-L31
[^218]: Source: knowledge/notes/input_part009_review.md†L32-L32
[^219]: Source: knowledge/notes/input_part009_review.md†L34-L34
[^220]: Source: knowledge/notes/input_part009_review.md†L398-L399
[^221]: Source: knowledge/notes/input_part009_review.md†L400-L400
[^222]: Source: knowledge/notes/input_part009_review.md†L401-L401
[^223]: Source: knowledge/notes/input_part009_review.md†L402-L402
[^224]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21845-L21939
[^225]: Source: knowledge/notes/input_part009_review.md†L37-L37
[^226]: Source: knowledge/notes/input_part009_review.md†L38-L38
[^227]: Source: knowledge/notes/input_part009_review.md†L40-L40
[^228]: Source: knowledge/notes/input_part009_review.md†L206-L214
[^229]: Source: knowledge/notes/input_part009_review.md†L214-L214
[^230]: Source: data/vesc_help_group/text_slices/input_part009.txt†L110-L111
[^231]: Source: knowledge/notes/input_part014_review.md†L35-L35
[^232]: Source: knowledge/notes/input_part014_review.md†L36-L36
[^233]: Source: knowledge/notes/input_part014_review.md†L34-L34
[^234]: Source: knowledge/notes/input_part004_review.md†L17-L17
[^235]: Source: knowledge/notes/input_part014_review.md†L37-L37
[^236]: Source: knowledge/notes/input_part014_review.md†L38-L38
[^237]: Source: knowledge/notes/input_part014_review.md†L39-L39
[^238]: Source: knowledge/notes/input_part014_review.md†L60-L61
[^239]: Source: knowledge/notes/input_part014_review.md†L101-L101
[^240]: Source: knowledge/notes/input_part014_review.md†L44-L44
[^241]: Source: knowledge/notes/input_part014_review.md†L61-L61
[^242]: Source: knowledge/notes/input_part014_review.md†L75-L75
[^243]: Source: knowledge/notes/input_part014_review.md†L152-L152
[^244]: Source: knowledge/notes/input_part014_review.md†L156-L156
[^245]: Source: knowledge/notes/input_part014_review.md†L159-L159
[^246]: Source: knowledge/notes/input_part014_review.md†L160-L160
[^247]: Source: knowledge/notes/input_part014_review.md†L172-L172
[^248]: Source: knowledge/notes/all_part01_review.md†L87214-L87233
[^249]: Source: knowledge/notes/all_part01_review.md†L88057-L88085
[^250]: Source: knowledge/notes/all_part01_review.md†L88155-L88333
[^251]: Source: knowledge/notes/all_part01_review.md†L88244-L88245
[^252]: Source: knowledge/notes/all_part01_review.md†L88335-L88345
[^253]: Source: knowledge/notes/all_part01_review.md†L88051-L88055
[^254]: Source: knowledge/notes/input_part008_review.md†L16-L16
[^255]: Source: knowledge/notes/input_part008_review.md†L13-L14
[^256]: Source: knowledge/notes/input_part008_review.md†L17-L17
[^257]: Source: knowledge/notes/input_part008_review.md†L15-L15
[^258]: Source: knowledge/notes/input_part008_review.md†L132-L133
[^259]: Source: knowledge/notes/input_part008_review.md†L108-L109
[^260]: Source: knowledge/notes/input_part008_review.md†L138-L138
[^261]: Source: knowledge/notes/input_part008_review.md†L139-L139
[^262]: Source: knowledge/notes/input_part008_review.md†L143-L143
[^263]: Source: knowledge/notes/input_part008_review.md†L144-L144
[^264]: Source: knowledge/notes/input_part008_review.md†L147-L148
[^265]: Source: knowledge/notes/input_part008_review.md†L153-L153
[^266]: Source: knowledge/notes/input_part008_review.md†L156-L158
[^p50b_watch]: Source: knowledge/notes/input_part008_review.md†L314-L314
[^267]: Source: knowledge/notes/input_part008_review.md†L158-L158
[^268]: Source: knowledge/notes/input_part008_review.md†L159-L159
[^269]: Source: knowledge/notes/input_part008_review.md†L188-L189
[^270]: Source: knowledge/notes/input_part008_review.md†L189-L189
[^271]: Source: knowledge/notes/input_part008_review.md†L398-L399
[^272]: Source: knowledge/notes/all_part01_review.md†L115-L116
[^273]: Source: knowledge/notes/all_part01_review.md†L216-L216
[^274]: Source: knowledge/notes/all_part01_review.md†L217-L217
[^275]: Source: knowledge/notes/all_part01_review.md†L118-L118
[^276]: Source: knowledge/notes/all_part01_review.md†L281-L281
[^277]: Source: knowledge/notes/all_part01_review.md†L258-L259
[^278]: Source: knowledge/notes/all_part01_review.md†L419-L419
[^279]: Source: knowledge/notes/all_part01_review.md†L420-L420
[^280]: Source: knowledge/notes/all_part01_review.md†L260-L260
[^281]: Source: knowledge/notes/input_part001_review.md†L19-L21
[^282]: Source: knowledge/notes/input_part007_review.md†L217-L224
[^283]: Source: knowledge/notes/all_part01_review.md†L218-L219
[^284]: Source: knowledge/notes/all_part01_review.md†L285-L285
[^285]: Source: knowledge/notes/all_part01_review.md†L284-L284
[^286]: Source: knowledge/notes/input_part007_review.md†L223-L223
[^287]: Source: knowledge/notes/input_part013_review.md†L322-L324
[^288]: Source: knowledge/notes/input_part004_review.md†L318-L318
[^289]: Source: knowledge/notes/input_part004_review.md†L37-L37
[^external_bag_reinforcement]: Source: knowledge/notes/input_part009_review.md†L420-L420
[^copper_pretension]: Source: knowledge/notes/input_part009_review.md†L401-L401
[^ip001-nickel-steel]: Source: data/vesc_help_group/text_slices/input_part001.txt†L18901-L18945
[^ip001-pure-nickel]: Source: data/vesc_help_group/text_slices/input_part001.txt†L18920-L18933
[^welder-trials]: Source: knowledge/notes/input_part010_review.md†L492-L493
[^stiff-holders]: Source: knowledge/notes/input_part010_review.md†L611-L612
[^artem_cells]: Source: knowledge/notes/input_part002_review.md†L18123-L18224
[^pack_48x_cost]: Source: knowledge/notes/input_part002_review.md†L17924-L17948
[^import_math]: Source: knowledge/notes/all_part01_review.md†L661-L661
[^50e_supply]: Source: knowledge/notes/all_part01_review.md†L677-L677
[^uk_cell_shortage]: Source: knowledge/notes/all_part01_review.md†L698-L698
[^repackr_ir_match]: Source: knowledge/notes/all_part01_review.md†L706-L706
[^daly_swap]: Source: knowledge/notes/all_part01_review.md†L722-L722
[^15s_common_port]: Source: knowledge/notes/all_part01_review.md†L609-L609
[^liitokala_warning]: Source: knowledge/notes/all_part01_review.md†L610-L610
[^denis-brandless]: Source: knowledge/notes/denis_all_part02_review.md†L894-L894
