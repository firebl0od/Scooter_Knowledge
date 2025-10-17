# Brake Maintenance & Upgrade Guide

## Overview

Proper brake maintenance and strategic upgrades are critical for safe high-speed scooter operation. This guide covers hydraulic brake bleeding, pad maintenance, caliper upgrades, rotor sizing, and the integration of mechanical brakes with regenerative braking systems. Understanding brake system limitations and maintenance requirements prevents failures during emergency stops.

## What You'll Learn

- Hydraulic brake bleeding procedures (Magura, Shimano, Hope)
- Four-piston caliper benefits and installation
- Rotor sizing and clearance considerations
- Pad selection and wear monitoring
- Mechanical brake backup requirements
- Regen braking integration best practices
- Thermal management for high-power stops
- Common brake failures and prevention

## ⚠️ Safety First

🔴 **Critical**: Always test brakes in a safe environment before riding at speed. Brake failure at high speed can be fatal.

## 📋 Quick Reference: Brake Upgrades by Performance Level

| Build Type | Front Brake | Rear Brake | Rotor Size | Priority |
|------------|-------------|------------|------------|----------|
| Stock commuter | Mechanical drum | Mechanical drum | Stock | Keep one mechanical active |
| Mid-power (5-10kW) | Hydraulic 2-piston | Drum or hydraulic | 160mm | Upgrade front first |
| High-power (10-20kW) | Hydraulic 4-piston | Hydraulic 2-piston | 180-203mm | Dual hydraulic required |
| Race (20kW+) | Hydraulic 4-piston | Hydraulic 4-piston | 203mm+ | Full race setup |

💡 **Pro Tip**: The front brake handles 70-80% of stopping force. Upgrade it before the rear.

## 🔧 Related Guides

- [Xiaomi Tire & Brake Upgrades](xiaomi_tire_brake_upgrade_notes.md) - Platform-specific brake options
- [High-Power VESC Reliability](high-power-vesc-scooter-reliability-guide.md) - Matching brakes to power
- [Motor Controller Tuning](motor_controller_tuning.md) - Regen braking configuration

## Key Safety Principles

- Hydraulic brake systems demand proper bleeding technique (level levers, flick hoses to vent micro-bubbles, patient lever cycling) and proactive seal maintenance to avoid spongy feel or sudden failures during high-speed stops.[^bleed-technique]
- Four-piston calipers provide superior thermal mass and stopping power for high-performance builds but require careful rotor sizing (180–203 mm) and clearance checks to avoid frame interference.[^four-piston]
- Wheel-centering kits and dual-caliper setups eliminate rotor wobble and improve braking consistency on racing builds, but add complexity and weight that commuter riders may not need.[^centering-kits]
- Keep at least one mechanical brake active even on regen-heavy builds.
  - logs show regen-only riding overheats controllers quickly, and dual-motor setups still rely on mechanical rotors to stop safely when electronics fault.[^1][^2]
- Leave expansion room in master cylinders. Overfilled reservoirs build pressure as fluid heats, forcing fittings to burp fluid or leak once systems see triple-digit Celsius rotor temps.[^heat-expansion]
- Expect the front brake to carry the bulk of stopping duty; riders relying on rear-only braking continue to report easy slides, so dual-hydraulic setups or regen+front hydraulic pairings remain the safe baseline for high-power scooters.[^front-bias]
- After wet rides, flush rotors and calipers with brake cleaner—it is safe on pads—and retorque folding pins or other fasteners so grit and fatigue cracks do not sneak in after rain sessions.[^denis-brake-clean]
- Riders pushing 40 km/h+ speed builds pair full motorcycle armor with pneumatic tires; the crew now labels solid tires a “death wish” at those speeds because the carcass can unseat mid-ride.[^denis-armor]

## Bleeding Techniques

### Magura MT5/MT7 Bleeding Procedure

- Successful Magura bleeds require leveling the brake lever, repeatedly flicking the hose to vent micro-bubbles, and patiently cycling the lever until the feel firms up.
  - this mirrors bicycle-service best practices the community plans to document more thoroughly.[^magura-bleed]
- **Step-by-step bleeding:**
  1. Remove pads and install bleed block to protect pistons during bleeding
  2. Level the brake lever horizontally to ensure air naturally rises toward reservoir
  3. Attach syringe to caliper bleed port, fill with mineral oil (DOT fluid damages Magura seals)
  4. Open lever reservoir and insert second syringe or funnel
  5. Gently push fluid from caliper toward lever while flicking hose to dislodge bubbles
  6. Cycle brake lever slowly (5–10 times) to work out remaining air
  7. Top off reservoir, close ports, reinstall pads and test lever firmness[^magura-bleed]

- 🇪🇸AYO#74 also swapped to a higher-flow bleed needle to tighten Shimano/Magura lever feel, noting the larger bore purged dead-zone bubbles faster than stock fittings.[^3]
- When calipers keep rubbing after a textbook bleed, remove the block, push each piston out halfway with a syringe full of clean mineral oil, lubricate the seals, and centre the caliper before the first lever pull—spreading the pistons evenly stops the asymmetric bite that causes rotor rub.[^magura_pistons]

### Preventing Seal Damage During Pad Changes

- skrtt burst an MT5 lever seal by pushing pistons back without cracking the bleed screw, so pad-swap guides need to stress releasing system pressure (or upgrading to metal levers) before compressing calipers to avoid hydraulic overload.[^seal-damage]
- **Safe pad replacement procedure:**
  1. Open caliper bleed screw slightly to relieve pressure
  2. Slowly push pistons back with flat tool (plastic tire lever or dedicated brake piston tool)
  3. Close bleed screw and verify no leaks
  4. Install new pads and bed them properly on first rides[^seal-damage]

### Pad Conditioning & Bedding

- Riders formed a “sanded pad club,” resurfacing pads before bedding to tame squeal and keep braking consistent after swapping to thicker rotors.[^4]
- Kool-Stop sintered pads stretch VSETT pad life beyond 800 km provided riders bed them with 30–60 hard 50→0 km/h stops, but they run louder and chew roughly 1 mm off rotors every ~1000 km—plan spare discs for long trips.[^ip001-sintered]

### Pad Selection & Wet-Weather Behavior

- Heavy scooters routinely chew through stock Magura pads in under 500 km; the crew now defaults to full-metallic Kool Stop D170S sets to keep MT5/MT7 systems consistent in gritty, high-power service.[^kool_stop]
- MT5/MT7 riders pairing Kool Stop sintered pads with Magura MDR-C 2 mm rotors and MT7 HC3 bite-point knobs report fierce bite and on-trail adjustability without reaching for hex tools.[^magura_field]
- Hope/Jagwire banjo kits cover every washer except the required M6 × 20 mm banjo bolt; after boiling Shimano rotors toward an estimated 350–450 °C, track riders now reinforce hoses with steel-braided “fuckeria” lines before the next session.[^magura_banjo]
- Magura’s stock Royal Blood boils around 120 °C, so aggressive downhill crews keep Shimano or Brembo mineral oil on hand for repeated 100 → 0 km/h stops and log rotor temps that push past 110 °C even on flat routes.[^royal_blood]
- Xiaomi Xtech calipers grab harder once the rotor is wet, so riders plan fresh bleeds and bedding cycles after rain to restore predictable modulation.[^xtech_wet]
- Logan four-piston calipers on NAMI scooters already deliver Magura-level stopping, so owners only switch brands if they prefer MT-series lever feel or pad options.[^logan_caliper]

### Xiaomi / Pro Brake Fitment Updates

- Stock organic pads on Xiaomi/Pro platforms fade quickly once speeds climb, so fast riders are shifting to sintered or ceramic compounds and, when chasing dual-disc conversions, splitting a single lever’s cable into matched housings so both calipers pull evenly.[^m365_pad_compounds]
- Classic cable-disc setups dial fine tension with the barrel adjuster and reserve the caliper’s hex bolt for coarse tweaks; if levers start bottoming out, veterans inspect pad wear before blaming cables.[^barrel_adjust]
- Confirm rotor bolt patterns before importing mountain-bike discs for a Pro 2: that hub uses six bolts while classic M365 rims only offer five, so mismatched hardware will not seat correctly.[^pro2_rotor_pattern]
- Tudor is gauging interest in a CNC’d Monorim 500 W brake adapter and plans to machine the first batch once roughly 20 riders commit, so builders eyeing dual-disc Monorim setups should register early or organize a group buy.[^monorim_adapter_batch]

### Lever Durability Notes

- Magura composite lever hardware can snap with hand force.
  - many owners preemptively swap to Shimano Saint or other metal bodies before trusting 3 mm rotors and high-torque braking setups.[^5]

## Brake Upgrades & Sizing

### Four-Piston Caliper Benefits

- Artem's freshly delivered Shimano M7120 four-piston set (≈€155 for the pair without rotors) brings stiffer one-finger levers and extra thermal mass that he plans to migrate from his trial bike to the scooter if he decides four pistons are overkill off-road.[^four-piston-cost]
- Four-piston systems improve heat dissipation during repeated high-speed stops but may be excessive for commuter builds under 60 km/h where two-piston Magura MT5 or similar calipers provide adequate stopping power.[^four-piston-vs-two]
- Zoom-branded hydraulics continue to underperform at speed.
  - riders are standardising on Nutt, Magura MT5e, Shimano Saint, or Hope calipers paired with 3 mm reinforced 160 mm rotors to survive repeated 120→0 km/h stops, noting that Magura reservoirs can crack under extreme loads.[^6]
- Inokim OXO owners hunting for a four-piston front upgrade either flip a rear swingarm to mount the caliper underneath or machine a dedicated adapter for the stock arm—there’s no bolt-on solution yet.[^oxo-front]
- Xiaomi riders chasing >50 km/h treat a second hydraulic brake as mandatory; flimsy Monorim adapters flex and 135 mm rotors warp, so upgrade to stiff adapters and 140 mm five-bolt discs or quality dual-caliper setups.[^denis-dual-brake]

### Motorcycle-Caliper Imports (Kotto Example)

- Kotto’s 3 mm motorcycle kits deliver fierce bite out of the box but ship dry and oversized.
  - expect to bleed them immediately and clearance thick rotors or caliper mounts so the hardware sits square on scooter forks.[^7]

### Regen Modulation Lessons

- Riders experimenting with high-force regen reported −80 A electronic braking nearly pitching them over the bars; most now tune Spinny/ADC profiles so regen complements (rather than replaces) hydraulic stoppers.[^8]
- Heavy scooters devour cheap pads even with regen assist.
  - switching to metallic compounds such as Galfer keeps feel consistent when regen is dialed back for wet roads.[^9]
- Denis’ workshop now treats Magura-class hydraulics as mandatory once Pro 2 builds creep toward 80 km/h.
  - Xtech hybrids can’t arrest the extra energy, so riders add lever sensors if they still want regen without sacrificing lever feel and plan a careful bleed after rerouting hoses.[^10]
- Riders retiring Xiaomi e-brake sensors after repeated controller pops at ~45 km/h now switch to full-hydraulic Shimano or Magura systems and upgrade mechanical cables to tougher bicycle housings when hydraulics are not yet installed.[^sensor_pop]

### Rotor Sizing Considerations

- Brake discussions suggest upsizing rotors from 180 mm to 203 mm mainly boosts thermal mass and leverage but may be excessive for scooters; larger rotors require frame clearance checks and stronger mounting tabs to handle increased braking forces.[^rotor-sizing]
- Magura MT7/MT5 calipers barely clear 2.9 mm Kaabo rotors.
  - fresh pads or 3 mm aftermarket discs often rub unless you machine custom spacers
  - so many riders stick with stock Zoom calipers or thinner discs when chasing upgrades.[^11]
- A Brakestuff rotor cracked after just a few races, sparking debate over its twin-ring design and whether added venting is needed to stop flipping/warping under race heat.[^brakestuff_rotor_debate]
- Magura Storm HC rotors measure about 1.9 mm new and get replaced near 1.8 mm; setting reach adjusters fully out, bleeding with piston blocks, and holding the caliper above the lever while closing ports prevents rubbing when fitting thicker MDR-C or MDR-P rotors with Kool Stop pads.[^storm_hc]
- X-Tech calipers quickly expose flimsy bargain rotors—if the disc warps after a ride, replace it with bike-shop-grade hardware rather than blaming the caliper.[^xtech_rotor_upgrade]
- Repeated 80–90 km/h stops roasted 120 mm rotors and overheated Magura MT8s; the crew now defaults to dual front brakes or 203 mm discs on heavy scooters to regain thermal margin.[^12]
- When rotors need a millimetre of offset, riders cut thin shim plates (nickel strip or torque-arm washers) instead of stacking round washers that flex loose under repeated braking loads.[^13]
- Premium rotors from Shimano, Magura, or Galfer stay on the shopping list while AliExpress specials are avoided for 70 km/h builds despite the price gap.[^14]
- Community tests agree that braking style dominates rotor temperature, yet aggressive metallic compounds can still dump rotor heat into motor shells during repeated panic stops—log hub temps if you lean on sintered pads.[^ip001-rotorheat]
- Kaabo Wolf owners now swap to 3 mm Kaabo discs after stock rotors warped.
  - confirm caliper spacing and expect longer life once the thicker rotors are paired with Wolf motors.[^15]
- Skip Shimano “resin only” 160 mm rotors on 72 V-class scooters; the thin rotors fade quickly and risk glazing metallic pads. Veterans instead budget 2 mm rotors rated for metallic compounds and pair them with full-hydraulic calipers before raising pack voltage.[^shimano-metal]
- Builders hunting thicker 160 mm options are sourcing 3 mm AliExpress rotors that clear Hope calipers without machining, smoothing upgrades on Zero and Dualtron conversions.[^ali-3mm]
- Segway GT2 rotors measure 2.42 mm thick (versus typical 1.8–2.0 mm commuter discs), providing superior warp resistance for repeated high-speed stops once Hope V4 or equivalent calipers are installed.[^gt2-rotors]
- Tall brake adapters should use a single ring spacer instead of stacked washers so axial loads do not rock the disc bolts.
  - 5 mm steel rings have proven stable on custom Blade hubs, while 1.7 mm washer stacks remain a stopgap only.[^16]
- Expect to budget CNC time for bespoke rotor shims because six-hole aftermarket rims rarely align with Xiaomi five-hole spacers when mixing OEM and custom hubs.[^17]

### Fork & Adapter Fitment

- Monorim fork swaps need custom torque arms, thin-head bolts, and stacked stainless shims so 140–160 mm discs clear the square legs without grinding away the casting.
  - document CAD references before committing to the conversion.[^18]
- Sombre_enfant warned that custom brackets held on with M5 bolts will ovalise mounts under MT7 loads—upgrade to snug M6/M8 hardware and machined adapters before trusting 100 km/h stops.[^m6-brackets]
- VSETT riders swapping the stock 140 mm rotors for 160 mm SRAM Cleansweep or 180 mm Magura MDR-P discs report dramatically better torque and heat rejection, but the upgrade only works if you retire washer stacks for purpose-built brackets and re-align pads to prevent warped rotors.[^19]

### External Hose Routing & Quick-Disconnect Hardware

- Magura MT5 single-pad kits ship without pad screws, so riders trim M4×25 mm bolts to fit, and the Jagwire Hyflow + Hope quick-connect set relocates the banjo outward with sealed M6/M5 washers—essential for tight decks like the Ninebot G30.[^magura_hardware]
- Track builds follow that kit with steel-braided “fuckeria” hoses after boiling Shimano rotors and seeing fade around 350–450 °C.[^magura_track]
- Rerouting Magura hoses outside the fork demands the correct short banjo bolts and bleed screws; mixing long/short clamp screws has already shorted controller phases, so standardise hardware before final assembly.[^20]
- The Elvedes Hydro Parts Kit supplies dual M8 banjos for clean fork exits, while Jagwire’s quick-disconnect system costs roughly $120–$125 for enough hose and couplers to outfit dual-motor scooters and requires committing to Jagwire hose diameters.[^21][^22]
- Hope’s HFA701 kit bundles the correct M6 banjos and bleed screws; if you piece together individual fittings from Venhill, Trickstuff, or AliExpress, match barb dimensions to hose ID or you will fight leaks during the first bleed.[^23]
- Even with premium hardware, external routing can crush Magura MT7 lines after flats or tire swaps.
  - inspect clearance after every wheel service and carry spare banjos plus hoses for roadside replacements.[^24]
- Jagwire-style external reroutes can kink MT7 hoses and kill braking until the line is replaced; inspect for damage after any flat and confirm at least 5 mm clearance to 10×3 rubber even when deflated.[^ip001-jagwire]
- Xiaomi and VSETT frames that run MT7/MT8 calipers close to the tire should stock spare banjos/bolts—sidewall flex can close sub-5 mm gaps mid-ride, so schedule clearance checks alongside pad inspections.[^ip001-clearance]
- Magura MT5e and MT7 calipers share castings, but the MT7 lever adds bite-point adjustment and four individual pads; most commuters still chase the aluminium one-finger HC lever upgrade for harder stops without the flex of plastic blades.[^mt7_lever]
- Rosheee’s €90 “Stahlflex” steel-braided hoses keep lever feel consistent under heat, yet fittings must match each brand’s banjo outlets to avoid leaks when mixing Magura, Shimano, or Hope hardware.[^stahlflex]
- When stock compounds glaze during track sessions, the group swaps to EBC sintered pads as the reliable fallback.[^ebc_pads]

### Semi-Hydraulic Caliper Limitations

- Aftermarket Xtech calipers bite hard in the dry but rely on cheap seals that rust quickly in rain—daily commuters keep rebuild kits or spares ready for wet-weather riding, flush them seasonally, and still report leaks once road salt enters the mix.[^denis-xtech-seals]
- Pair X-Tech calipers with quality 140 mm rotors; cheap 135 mm AliExpress discs feel weak until you upgrade the hardware.[^denis-xtech-rotor]
- **Budget hybrids keep failing.** Shop owners keep seeing piston corrosion and fluid leaks on Xtech-style hybrids, so high-speed builds increasingly jump straight to full hydraulics (Magura) or quality mechanical calipers instead of trusting the semi-hydraulic compromise.[^xtech-corrosion]
- XTech-style semi-hydraulic calipers carry minimal oil volume, rely on rattly auto-centering hardware, and have warped rotors on scooters above 60 km/h.
  - upgrade to sturdier discs, avoid flimsy quad calipers, and inspect the whole brake stack after flats or heavy emergency stops.[^25]
- For mechanical builds, the TRP Spyke dual-piston caliper remains the dependable upgrade and even pairs with Xiaomi-style brake levers that include e-brake switches for simple commuter maintenance.[^trp_spyke]
- Track abuse already pushed Magura calipers past the Curie point (>700 °C), wiping magnetism and underscoring the need for engine braking or larger rotors on race builds before mechanical fade sets in.[^26]
- 100 km/h track logs keep comparing Trickstuff, Kool-Stop, Shimano, and XLC rotors.
  - prep extra thermal mass, ventilation, and pad choices before sprint sessions so glowing hardware doesn’t demagnetise calipers or chew pads mid-run.[^27]
- Dual-rotor experiments now include Trickstuff, Kool-Stop, Shimano Saint, Ashima, and XLC floating discs; the budget XLC hardware bites hard but its floating hardware feels suspect on dual G30 conversions, so budget inspections between sessions.[^28][^29]
- Bosch’s e-bike ABS pairs cleanly with Magura CMe5 levers, giving scooters a path to anti-lock hydraulics while still functioning as premium standalone brakes if you skip the controller module.[^30]
- Brakestuff 3 mm rotors reward precise setup.
  - Magura Saints squeal if runout isn’t near perfect, but Hope Tech 4 V4 calipers on the same discs delivered the strongest stops the testers have measured so far.[^31][^32]
- Custom rotor projects now target 203 mm discs cut from 2.3–2.5 mm acid-proof steel, but Magura calipers only clear ≈2.1 mm.
  - budget runout checks and pad clearance before ordering thicker hardware.[^33]
- Magura and TRP four-piston setups expect 2.0–2.3 mm rotors, and AliExpress Brembo clones often ship in left/right-specific pairs.
  - verify orientation when ordering for right-hand-drive scooters to avoid fitment surprises.[^34]

### Magura MT5e Kits & Setup

- Community carts keep landing full MT5e front/rear kits around $200, and Jenson USA ships globally via DHL.
  - several riders noted the pricing is better than expected for four-piston hydraulics.[^mt5e-pricing]
- Burnout-focused builders sometimes leave the MT5e e-brake sensors unplugged or repurpose a single caliper while waiting on replacements; strip non-essential electrical loads when testing to confirm the new hydraulics clear the fork and wiring bundles.[^mt5e-sensors]
- Inspect bundled levers before trusting them.
  - Jan flagged one aftermarket lever as “the worst” thanks to plastic threads and screws despite pairing with Magura calipers, so budget for higher-quality levers if the kit feels flimsy.[^bad-lever]
- Treat the supplied 0.5 Nm bleed wrench as mandatory; over-tightening the lever screw by feel strips threads and dumps pressure mid-ride.[^ip001-bleedtorque]
- Rotor slot orientation matters.
  - aim the cooling slots forward on the front wheel, but flip a rear rotor if the slots face the wrong direction after a wheel swap so debris clears properly.[^35]
- Rim brakes gouged paint and underperformed on Haku’s 20 mph minibike conversion.
  - plan disc-ready wheels or fabricate caliper mounts if you need real stopping power beyond low-speed duty.[^36]

### Compact Lever & Sensor Options

- For builds that cannot fit full-size brake levers, the crew recommends child-sized handles with built-in e-brake switches or even spare thumb throttles rewired as brake inputs to keep regen triggers within reach on narrow cockpits.[^37]
- Wuxing’s budget 115PDD lever closes a simple loop when pulled, making it a drop-in cut-off option for commuters that need electrical braking without hunting premium hardware.[^37]
- Whenever possible, choose hall-based brake levers over binary switches.
  - especially for small hands
  - and pair hydraulic setups with magnetic two-pin sensors like the modules 🇪🇸AYO#74 installs on high-power scooters to guarantee consistent regen cues.[^38][^39][^40]
- Riders pushing highway pulls on a single rear brake, such as Shlomozero’s Zero running a lone Nutt caliper plus regen, were urged to upgrade to Magura or Shimano Saint-class dual setups before continuing 100 km/h testing.[^41]
- Apo cautioned that motorcycle Brembo calipers demand thicker rotors and extra fork clearance than most scooter chassis provide, so premium bicycle systems remain the realistic upgrade path until frames adopt moto-style mounts.[^42]
- Yamal warned that floating bicycle rotors look flashy but perform worse on high-power scooters—stick with proven solid discs for consistent bite.[^43]
- Yamal and 🇪🇸AYO#74 still favour the solid 3 mm “Wolf” discs from AliExpress.
  - non-floating despite the two-piece look
  - because they survive where riveted rotors sheared; at ≈€30 online (vs. €80–100 retail) riders buy them in sets of four.[^44]
- Sonken-branded 160 mm rotors mirror the weak inner-ring geometry that doomed earlier Brakestuff copies; without better tempering and precise Hope caliper shimming they bend within months on RM-X race scooters.[^sonken-warning]
- Brake-Stuff’s Shimano-pattern 6-bolt rotors are proving durable replacements for worn discs on VESC conversions.
  - Yamal’s installs slot straight onto common hubs when builders want mid-tier pricing without sacrificing material quality.[^45]

### Superbikes & Heat Management

- Racers weighing €1.2 k Trickstuff Maxima kits against Magura MT5/MT7 setups note that motorcycle Brembos rarely clear scooter forks; 150 km/h stopping demands bigger rotors and higher-volume masters no matter which premium caliper you choose.[^46]
- 3 mm × 170 mm rotors dramatically stiffen braking response but require retracting pistons fully for clearance and a quick true after the first bedding stops.[^47]
- A commuter who bent a Vsett rotor mid-ride now keeps spares on hand and leans on e-brakes when mechanical hardware warps unexpectedly.
  - plan redundancy for traffic incidents.[^48]
- Even premium hardware stacks can boil fluid. One MT7/MT8 build with copper sintered pads, Bionol fluid, Steelflex hoses, and prototype levers still flashed 360 °C fluid and leaked at the banjo, forcing pad and rotor inspections after every downhill session; treat aggressive descents as consumable events even on boutique components.[^mt7-boil]
- Skrtt’s 2.3 mm rotor experiments required shaving calipers while 🇪🇸AYO#74 stressed using “elevator” spacers to clear thicker discs.
  - document allowable rotor thickness per caliper so riders stop guessing on machining limits.[^49]
- Ausias is milling Magura MT5 calipers “radially” to clear 3.6 mm rotors; peers warned most bicycle brakes expect ≤2.8 mm discs, so publish machining tolerances, lever upgrades, and testing steps before anyone copies the mod.[^50]
- Hope Tech Evo calipers routinely sell for €260–€300 (≈$300) per end; racers have found 3 mm rotors clear the four-piston bodies when regen remains primary braking, reinforcing that premium stopping power demands both budget planning and rotor-thickness checks.[^hope-pricing]
- Paolo’s rotor group buy keeps blanks at 2 mm so stock calipers bolt up; builders confirm Magura MT5 Pro units can swallow 2.7 mm rotors and trimmed Nutt four-piston calipers clear 3 mm, but thicker discs raise costs and require caliper mods many riders skip.[^rotor-thickness]
- Jan’s hardened 420C 160 mm rotors landed at 45 € plus shipping; prototypes survived light bicycle testing but still need scooter-load validation.
  - log bedding, braking torque, and temperature before committing to fleet orders.[^51]
- Spintend detachable rims still favour 160 mm, ≈2.7 mm rotors so riders can stock one spare width; jumping to 180 mm adds leverage but risks front-wheel skids unless chassis geometry and modulation keep up.[^52][^53]
- 160 mm rotor upgrades on Xiaomi frames need careful spacing.
  - builders raised calipers or machined thicker adapters so disc bolts stop striking tire adapters after aggressive braking tests on AWD/RWD conversions.[^54]

### Hope Tech/Tesch 3 Caliper Service

- 🇪🇸AYO#74's first successful Hope Tech/Tesch 3 rebuild covered piston re-greasing, compatible pad sizes, and bedding procedures that other riders can replicate for improved braking on high-power builds.[^hope-service]
- 🇪🇸AYO#74 finally cleared a four-year sticky-piston saga by stripping and re-greasing his Hope caliper; he also flagged the latest Tesch 3 V4 pads as ~2 mm taller than earlier tablets, so update spares lists before ordering replacements.[^hope-regrease]
- Kaabo Wolf riders source rear Magura adapters from Javamba after discovering flipped front hubs could not accommodate left-side calipers.
  - keep vendor links handy before tearing down the rear motor.[^55]
- AliExpress shim kits (2–5 mm rotors spacers plus washers) keep oversized calipers from fouling hub flanges, giving Dualtron and Kaabo owners a cheap path to widen rotor stance without machining custom spacers.[^56]
- **Hope caliper maintenance tips:**
  - Disassemble calipers and clean pistons with isopropyl alcohol
  - Apply fresh brake-specific grease to piston seals (avoid petroleum-based products)
  - Verify pad backing plates are flat and not warped from heat
  - Bed new pads gradually with 10–15 moderate stops from 30 km/h before attempting hard braking[^hope-service]

## Ninebot F2 Pro Brake Upgrades

## Ninebot G30 Brake Retrofits

- 3D-printed rear brake adapters with thin aluminium reinforcement rings drew skepticism about PLA strength at 60 km/h; riders recommend CNC or full-metal conversions before trusting repeated hard stops.[^57]
- Fitting 10×3 in tyres demands trimming the rear fender and routing the brake hose internally instead of relying on inverted Magura mods to keep wobble away.[^58]
- cihan's wobble fix involved swapping to sintered pads and sourcing compatible rotors for the F2 Pro platform, demonstrating that budget commuter platforms benefit from modest brake improvements without requiring full hydraulic conversions.[^f2-upgrade]
- Expect odd hardware: the F2 Pro uses a 51 mm post mount and five-bolt rotor pattern, so riders stack sturdier post-to-post adapters (avoiding soft Monorim brackets) and often jump to 140 mm rotors to keep pad contact when stacking spacers.[^59]
- **F2 Pro brake upgrade recipe:**
  - Install sintered pads for better bite and longevity compared to organic pads
  - Source inexpensive soft rotors compatible with the F2 Pro mounting pattern—cihan is happy to burn through €2 discs in exchange for the stability boost once they warm up
  - Expect accelerated rotor wear compared to higher-grade steel on premium builds
  - Budget for rotor replacement every 1,000–2,000 km depending on riding style[^f2-upgrade]
- **Hydraulic retrofit fitment.** 1200 W Blade and Monorim front ends accept full hydraulic kits with 2 m hoses, but expect adapter sourcing drama on Xiaomi frames.
  - pre-fit brackets and hose routing before committing to the swap.[^60]

- **Regen-only braking has limits.** Francois is temporarily riding a front drum plus −90 A motor brake while waiting on display parts.
  - a reminder that regen alone can’t cover emergency stops and should stay supplemental to mechanical brakes.[^61][^62]

## Wheel Centering & Dual-Caliper Setups

### Wheel-Centering Kits for 80/100H Hubs

- Track-focused Nami/Dualtron builds copy the wobble fix Arnau and Yamal are lining up by using wheel-centering kits and dual-caliper setups (dual rotors or dual calipers per wheel) to ensure consistent pad contact during high-speed braking.[^centering-kits]
- **Centering kit installation:**
  1. Verify hub spacers and axle alignment before installing centering hardware
  2. Mount dual calipers with proper clearance from frame and swingarm
  3. Use centering gauge or dial indicator to verify rotor runs true (≤0.1 mm runout)
  4. Torque caliper mounts to manufacturer specification (typically 8–10 Nm)
  5. Test brake feel and rotor clearance before first ride[^centering-kits]

### When to Consider Dual-Caliper Systems

- Dual-caliper or dual-rotor configurations make sense for racing builds where consistent braking at 100+ km/h justifies the added weight and complexity, but commuter riders below 70 km/h see diminishing returns from the upgrade.[^dual-caliper-when]
- Matthew's regen-assisted braking setup suggests that well-tuned regenerative braking can supplement or even replace hydraulic brakes for routine speed control, reserving mechanical brakes for emergencies and final stops.[^regen-braking]
- Don’t run highway speeds on a single rear brake.
  - Shlomozero’s Zero 10X is still on a lone Nutt four-piston with regen, and the crew keeps pushing riders toward Magura or Saint-class dual setups before continuing 100 km/h pulls.[^41]

## Tire Inflation & Bead Seating

- Haku's Xiaomi inflator couldn't seat 21×3 tires even with a ratchet strap, reinforcing that serious tubed slick installs demand higher-flow compressors (≥150 PSI, 2+ CFM) or shop assistance to pop beads properly.[^tire-inflation]
- Roadside swaps go smoother when you break the bead with dish soap, dust tubes in talc or baby powder, and reassemble carefully.
  - the combo stops inner-tube chafing after emergency tire pulls.[^63]
- PMT 110/55 R6.5 slicks feel vague at the 2.2 bar sidewall spec; experienced tuners run ~3.5 bar for crisp handling without reported failures.[^64]
- Ratchet straps or belts cinched around 11–12″ tubeless tires let portable pumps pop beads once the carcass is preloaded.
  - ideal when you need a trail-side seating trick without a shop compressor.[^65]
- Installing solid tires goes faster if you heat the tire (boiling water or a microwave for ~10–15 minutes), brace the hub on the floor, lever with two irons, then finish with soapy water so the bead seats evenly.[^66]
- **Compressor requirements for large tires:**
  - Minimum 150 PSI working pressure for 21×3 and larger tires
  - 2+ CFM flow rate to seat beads quickly before air leaks past unseated tire
  - Use bead seater tools or ratchet straps around tire circumference to help initial seating
  - Remove valve core temporarily during seating to maximize airflow, reinstall once beads are set[^tire-inflation]
- Stock extra casings and tubes.
  - one PMT puncture forced a 4 km walk, highlighting how quickly high-speed tires destroy rims when no spare is available.[^67]

## Hose & Banjo Hardware

- Dualtron owners flipping banjo orientation often choose Fastride’s stainless dual-M8 kit (~€40) because it includes crush washers and O-rings, avoiding piecemeal sourcing for hose reroutes.[^68]

## Brake Fluid & Compatibility

- Xtech hydraulic conversions rely on mineral oil (not DOT fluid) for Magura-compatible systems; Mirono bled his calipers with dual syringes and quickly abandoned the idea of using water after seeing trapped bubbles compromise lever feel.[^mineral-oil]
- DOT 5/5.1 silicone formulas eat the seals in Magura and Shimano systems.
  - stick with mineral oil and consider Trickstuff Bionol for downhill scooters because its 300–420 °C boiling range survives the heat that cooks stock fluids.[^dot5-warning]
- Split tubeless rims still respond best to ratchet straps plus high-flow compressors; skrtt’s bead only sealed after cinching the carcass, and the crew explicitly discouraged flammable “quick seat” tricks.
  - document the safe workflow before recommending tubeless conversions.[^69]

## Wheel & Rim References

- Rage’s CNC rim for Fastgirl measures 65 mm internal width for 11″ 90/65 tires, closely matching skrtt’s new 33×2 profile.
  - log those dimensions so tire-fit calculators stop relying on guesses.[^70]
- Mixing Shimano and Magura mineral oils proved safe during field tests, but the crew still monitors lever seals after the swap to confirm no swelling or leaks creep in post-service.[^71]
- **Fluid compatibility chart:**
  - **Magura, Shimano, Tektro:** Mineral oil only (DOT fluid damages seals)
  - **Hope, Hayes, Avid:** DOT 4 or DOT 5.1 (never DOT 5 silicone-based)
  - **Never mix fluids:** Contamination causes seal swelling and brake failure
  - Store mineral oil in sealed containers away from light to prevent oxidation[^fluid-compat]
- Shimano MT-series kits ship pre-bled but still need hoses re-threaded through stems, a follow-up bleed, and either the €15 EZ-MTB service kit or clever improvisation; riders have finished jobs with Total LHM Plus or even baby oil when OEM fluid ran out.[^shimano-mt]

## Hydraulic Sensor Retrofits

- Builders add hall sensors or reed switches to existing hydraulic levers when they need proportional regen or kill-switch behaviour, freeing them from the limited OEM sensored lever catalog.[^hall-retrofit]
- When extending short Magura bicycle hoses, reuse the correct olives and barbs at each end.
  - aftermarket lines such as Jagwire Pro handle higher pressure but still leak if the hardware mismatch leaves gaps at the caliper or lever.[^jagwire-hardware]

## Post-Flood Brake Recovery

- Flood-soaked calipers should be stripped, scrubbed with dedicated brake cleaner, and dried before touching WD-40 or silicone sprays.
  - those products swell seals and leave corrosion that will seize pistons again.[^flood-recovery]

### High-Heat Hydraulic Practices

- **Leave reservoir headroom.** Mountain-pass riders boiling 360 °C Trickstuff Bionol in Magura MT7 stacks watched the banjo burp once expansion had nowhere to go.
  - bleed with a visible air gap so thermal growth doesn’t pop seals mid-descent.[^bionol-flash]
- **Prioritise front stopping power.** Community logs keep stressing that rear-only braking just locks and skids; pair a strong front hydraulic with regen on both controllers whenever possible so emergency stops stay controllable.[^front-priority]
- **Upgrade rotors for high voltage.** Shimano “resin only” 160 mm discs fade instantly on 72 V scooters.
  - step up to 2 mm-thick metallic-ready rotors and full-hydraulic calipers before raising pack voltage.[^resin-rotor]
- **Inspect hardware after heat events.** That same MT7/MT8 build now budgets pad checks and rotor swaps after every downhill session because fluid flash cooked fittings despite premium components.[^post-heat-service]

## Follow-Up Actions Needed

- Write up an 80/100 H wheel-centering and dual-caliper setup guide (kit sourcing, torque, clearance checks) so track-focused Nami/Dualtron builds can copy the wobble fix.[^follow-centering]
- Turn the dual-disc vs. dual-caliper debate.
  - and Matthew's regen save
  - into a braking guide that spells out when dual rotors help, how to size levers/calipers, and why regen can't replace hydraulics on high-speed builds.[^follow-dual-disc]

## Source Notes

[^bleed-technique]: Magura bleeding technique emphasizing level levers, hose flicking, and patient lever cycling.[^72]
[^magura-bleed]: Successful Magura MT5/MT7 bleed procedure following bicycle-service best practices.[^72]
[^seal-damage]: MT5 lever seal burst from pushing pistons without relieving pressure via bleed screw.[^73][^seal-damage-2025]
[^seal-damage-2025]: Source: knowledge/notes/input_part013_review.md†L747-L747
[^four-piston-cost]: Shimano M7120 four-piston caliper pricing and thermal mass benefits.[^74]
[^four-piston-vs-two]: Four-piston caliper benefits for high-performance builds vs. two-piston sufficiency for commuters.
[^rotor-sizing]: Rotor sizing from 180 mm to 203 mm for thermal mass and leverage, with frame clearance warnings.[^75]
[^brakestuff_rotor_debate]: Source: knowledge/notes/input_part008_review.md†L456-L457
[^gt2-rotors]: Segway GT2 2.42 mm rotors providing warp resistance for repeated high-speed stops.[^76]
[^m6-brackets]: Oversized hydraulic setups demand M6/M8 hardware and tight-tolerance adapters; M5 bolts quickly elongate mounts under MT7 braking loads.[^77]
[^mt5e-pricing]: Magura MT5e front/rear kits hovering around $200 shipped via Jenson USA/DHL impressed riders expecting higher prices.[^78]
[^mt5e-sensors]: Riders testing MT5e swaps left e-brake sensors unplugged, stripped non-essential loads, and double-checked caliper clearance while waiting on any missing hardware.[^79]
[^bad-lever]: Jan called out a Magura-compatible lever with plastic threads/screws as the worst he has used—treat cheap bundles as suspect.[^80]
[^hope-pricing]: Hope Tech Evo pricing and 3 mm rotor clearance observations from group buys.[^81]
[^hope-service]: Hope Tech/Tesch 3 caliper service covering piston re-greasing and pad compatibility.[^82]
[^hope-regrease]: Source: knowledge/notes/input_part013_review.md†L714-L714
[^f2-upgrade]: Ninebot F2 Pro brake upgrade using sintered pads and compatible rotors.[^83]
[^centering-kits]: Wheel-centering kits and dual-caliper setups for wobble elimination on 80/100H racing builds.[^84]
[^dual-caliper-when]: When to consider dual-caliper systems based on speed and use case.
[^regen-braking]: Matthew's regen-assisted braking demonstration showing mechanical brakes as backup.[^85]
[^tire-inflation]: Compressor requirements for seating 21×3 and larger tires with ratchet strap assistance.[^86]
[^mineral-oil]: Mineral oil requirement for Magura hydraulic systems and water bleeding failure.[^74]
[^dot5-warning]: DOT 5/5.1 destroys Magura/Shimano seals; Trickstuff Bionol offers a mineral-oil alternative rated to ~420 °C for heat-soaked scooters.[^87]
[^fluid-compat]: Brake fluid compatibility chart for common hydraulic brake systems.
[^hall-retrofit]: Adding hall or reed sensors to any hydraulic lever unlocks proportional regen or kill-switch control without hunting rare OEM sensored levers.[^88]
[^jagwire-hardware]: Jagwire Pro hoses outperform stock Magura lines, but the correct olives/barbs are mandatory at each end to prevent leaks after re-termination.[^88]
[^ip001-sintered]: Source: knowledge/notes/input_part001_review.md†L620-L621
[^ip001-jagwire]: Source: knowledge/notes/input_part001_review.md†L642-L643
[^ip001-clearance]: Source: knowledge/notes/input_part001_review.md†L642-L644
[^ip001-rotorheat]: Source: knowledge/notes/input_part001_review.md†L680-L681
[^ip001-bleedtorque]: Source: knowledge/notes/input_part001_review.md†L683-L684
[^flood-recovery]: Post-flood brakes revive when stripped, cleaned with brake cleaner, and finished with PTFE lube once dry.
  - WD-40 or silicone swell seals and leave rust behind.[^89]
[^follow-centering]: Follow-up action to create wheel-centering and dual-caliper setup guide.[^84]
[^follow-dual-disc]: Follow-up action to document dual-disc vs. dual-caliper decision matrix.[^85]

- **Cool overheated brakes while rolling.** Riders who stop immediately after smoking a Magura caliper trap heat, boil fluid, and face a full re-bleed.
  - keep the scooter moving to shed heat before coming to rest after heavy stops.[^90]
[^bionol-flash]: Trickstuff Bionol flashed in a Magura MT7 stack, venting fluid through the banjo because the reservoir was overfilled before the descent.[^91]
[^front-priority]: Riders reiterating that strong front hydraulics plus dual electronic braking provide real stopping power; rear-only braking just slides.[^92]
[^resin-rotor]: Shimano “resin only” 160 mm rotors failing on 72 V scooters and the recommendation to run 2 mm metallic-ready discs with hydraulic calipers instead.[^93]
[^post-heat-service]: Premium MT7/MT8 builds scheduling pad and rotor inspections after every downhill session once high-temp fluid flashes exposed weak hardware.[^91]
[^shimano-mt]: Shimano MT-series kits still need hoses re-threaded through stems, a fresh bleed, and either the €15 EZ-MTB kit or improvised tools; Total LHM Plus or baby oil has stood in for mineral fluid in a pinch.[^94]
[^rotor-thickness]: Paolo’s rotor group buy sticking with 2 mm blanks and caliper clearance notes for 2.7–3 mm discs.[^95]

- **Support cable housing runs.** Zip-tie the housing to the frame and trim excess slack before chasing pad or caliper issues.
  - every bit of housing flex steals lever travel and torpedoes braking force.[^96]


## References

[^1]: Source: knowledge/notes/input_part004_review.md†L222-L222
[^2]: Source: knowledge/notes/input_part004_review.md†L230-L230
[^3]: Source: knowledge/notes/input_part013_review.md†L228-L228
[^4]: Source: knowledge/notes/input_part012_review.md†L35-L35
[^5]: Source: knowledge/notes/input_part012_review.md†L34-L34
[^6]: Source: knowledge/notes/input_part000_review.md†L511-L511
[^7]: Source: knowledge/notes/input_part004_review.md†L221-L221
[^8]: Source: knowledge/notes/input_part008_review.md†L249-L249
[^9]: Source: knowledge/notes/input_part008_review.md†L250-L251
[^10]: Source: knowledge/notes/denis_all_part02_review.md†L433-L433
[^denis-dual-brake]: Source: knowledge/notes/denis_all_part02_review.md†L752-L752
[^denis-xtech-seals]: Source: knowledge/notes/denis_all_part02_review.md†L933-L933
[^denis-xtech-rotor]: Source: knowledge/notes/denis_all_part02_review.md†L962-L962
[^denis-front-disc]: Source: knowledge/notes/denis_all_part02_review.md†L1056-L1056
[^denis-fork-reinforce]: Source: knowledge/notes/denis_all_part02_review.md†L1057-L1057
[^denis-mixed-brake]: Source: knowledge/notes/denis_all_part02_review.md†L1079-L1079
[^11]: Source: knowledge/notes/input_part002_review.md†L141-L142
[^12]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11088-L11137
[^13]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11406-L11455
[^14]: Source: data/vesc_help_group/text_slices/input_part002.txt†L12102-L12151
[^15]: Source: knowledge/notes/input_part011_review.md†L346-L351
[^16]: Source: knowledge/notes/input_part000_review.md†L520-L522
[^17]: Source: knowledge/notes/input_part000_review.md†L521-L522
[^18]: Source: knowledge/notes/input_part000_review.md†L512-L512
[^19]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8211-L8253
[^20]: Source: data/vesc_help_group/text_slices/input_part001.txt†L9208-L9211
[^21]: Source: data/vesc_help_group/text_slices/input_part001.txt†L9522-L9538
[^22]: Source: data/vesc_help_group/text_slices/input_part001.txt†L9901-L10054
[^23]: Source: data/vesc_help_group/text_slices/input_part001.txt†L9947-L10216
[^24]: Source: knowledge/notes/input_part001_review.md†L642-L644
[^25]: Source: data/vesc_help_group/text_slices/input_part001.txt†L20680-L20760
[^26]: Source: data/vesc_help_group/text_slices/input_part003.txt†L8386-L8400
[^27]: Source: knowledge/notes/input_part003_review.md†L103-L103
[^28]: Source: data/vesc_help_group/text_slices/input_part003.txt†L11517-L11570
[^29]: Source: data/vesc_help_group/text_slices/input_part003.txt†L11935-L11970
[^30]: Source: knowledge/notes/input_part003_review.md†L166-L166
[^31]: Source: data/vesc_help_group/text_slices/input_part004.txt†L7401-L7405
[^32]: Source: data/vesc_help_group/text_slices/input_part004.txt†L7469-L7472
[^33]: Source: knowledge/notes/input_part006_review.md†L375-L375
[^34]: Source: knowledge/notes/input_part006_review.md†L123-L123
[^35]: Source: data/vesc_help_group/text_slices/input_part009.txt†L12472-L12477
[^36]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21004-L21007
[^37]: Source: data/vesc_help_group/text_slices/input_part009.txt†L20306-L20327
[^38]: Source: data/vesc_help_group/text_slices/input_part009.txt†L20536-L20556
[^39]: Source: data/vesc_help_group/text_slices/input_part009.txt†L20928-L20934
[^40]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21186-L21187
[^41]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21214-L21232
[^42]: Source: knowledge/notes/input_part010_review.md†L261-L262
[^43]: Source: knowledge/notes/input_part010_review.md†L262-L263
[^44]: Source: data/vesc_help_group/text_slices/input_part010.txt†L18701-L18712
[^ali-3mm]: Source: knowledge/notes/input_part010_review.md†L620-L620
[^sonken-warning]: Source: knowledge/notes/input_part010_review.md†L665-L665
[^45]: Source: knowledge/notes/input_part010_review.md†L391-L392
[^46]: Source: knowledge/notes/input_part011_review.md†L368-L374
[^47]: Source: knowledge/notes/input_part012_review.md†L33-L33
[^48]: Source: knowledge/notes/input_part012_review.md†L186-L186
[^49]: Source: knowledge/notes/input_part013_review.md†L161-L161
[^50]: Source: knowledge/notes/input_part013_review.md†L376-L378
[^51]: Source: data/vesc_help_group/text_slices/input_part014.txt†L10221-L10228
[^52]: Source: data/vesc_help_group/text_slices/input_part014.txt†L10613-L10622
[^53]: Source: data/vesc_help_group/text_slices/input_part014.txt†L10616-L10619
[^54]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89952-L90018
[^55]: Source: knowledge/notes/input_part011_review.md†L406-L408
[^56]: Source: knowledge/notes/input_part011_review.md†L304-L308
[^57]: Source: data/vesc_help_group/text_slices/input_part002.txt†L3214-L3249
[^58]: Source: data/vesc_help_group/text_slices/input_part002.txt†L3536-L3551
[^59]: Source: knowledge/notes/input_part007_review.md†L348-L352
[^60]: Source: data/vesc_help_group/text_slices/input_part003.txt†L11882-L11884
[^61]: Source: knowledge/notes/input_part013_review.md†L163-L163
[^62]: Source: knowledge/notes/input_part013_review.md†L5639-L5653
[^63]: Source: knowledge/notes/input_part000_review.md†L669-L670
[^64]: Source: knowledge/notes/input_part006_review.md†L162-L162
[^65]: Source: data/vesc_help_group/text_slices/input_part009.txt†L6281-L6333
[^66]: Source: data/vesc_help_group/text_slices/input_part009.txt†L8387-L8398
[^67]: Source: knowledge/notes/input_part012_review.md†L37-L37
[^68]: Source: knowledge/notes/input_part012_review.md†L38-L38
[^69]: Source: knowledge/notes/input_part013_review.md†L196-L197
[^70]: Source: knowledge/notes/input_part013_review.md†L131-L131
[^71]: Source: knowledge/notes/input_part013_review.md†L228-L229
[^72]: Source: knowledge/notes/input_part013_review.md†L388-L388
[^73]: Source: knowledge/notes/input_part013_review.md†L758-L760
[^74]: Source: knowledge/notes/input_part000_review.md†L567-L567
[^75]: Source: knowledge/notes/input_part014_review.md†L43-L43
[^76]: Source: knowledge/notes/input_part006_review.md†L357-L357
[^77]: Source: data/vesc_help_group/text_slices/input_part001.txt†L4671-L4707
[^78]: Source: knowledge/notes/input_part007_review.md†L109-L130
[^79]: Source: knowledge/notes/input_part007_review.md†L130-L130
[^80]: Source: knowledge/notes/input_part007_review.md†L147-L147
[^81]: Source: knowledge/notes/input_part014_review.md†L3124-L3163
[^82]: Source: knowledge/notes/input_part013_review.md†L677-L678
[^83]: Source: data/vesc_help_group/text_slices/input_part013.txt†L8828-L8831
[^84]: Source: knowledge/notes/input_part013_review.md†L645-L647
[^85]: Source: knowledge/notes/input_part013_review.md†L635-L637
[^86]: Source: knowledge/notes/input_part013_review.md†L761-L762
[^87]: Source: knowledge/notes/input_part002_review.md†L24-L26
[^88]: Source: knowledge/notes/input_part002_review.md†L26-L27
[^89]: Source: knowledge/notes/input_part002_review.md†L29-L30
[^90]: Source: data/vesc_help_group/text_slices/input_part004.txt†L4146-L4156
[^91]: Source: knowledge/notes/input_part006_review.md†L12-L13
[^92]: Source: knowledge/notes/input_part006_review.md†L14-L14
[^93]: Source: knowledge/notes/input_part006_review.md†L15-L15
[^94]: Source: knowledge/notes/input_part007_review.md†L238-L238
[^95]: Source: knowledge/notes/input_part014_review.md†L10356-L10365
[^96]: Source: knowledge/notes/denis_all_part02_review.md†L348-L349
[^heat-expansion]: Source: knowledge/notes/input_part006_review.md†L13-L13
[^front-bias]: Source: knowledge/notes/input_part006_review.md†L14-L14
[^shimano-metal]: Source: knowledge/notes/input_part006_review.md†L15-L15
[^mt7-boil]: Source: knowledge/notes/input_part006_review.md†L12-L12
[^oxo-front]: Source: knowledge/notes/input_part011_review.md†L513-L513
[^magura_field]: Source: knowledge/notes/input_part002_review.md†L17154-L17243
[^magura_banjo]: Source: knowledge/notes/input_part002_review.md†L17178-L17275
[^magura_pistons]: Source: data/vesc_help_group/text_slices/input_part002.txt†L20741-L20809
[^royal_blood]: Source: data/vesc_help_group/text_slices/input_part002.txt†L20728-L20753
[^storm_hc]: Source: knowledge/notes/input_part002_review.md†L19214-L19505
[^logan_caliper]: Source: knowledge/notes/input_part002_review.md†L19882-L19887
[^magura_hardware]: Source: knowledge/notes/input_part002_review.md†L638-L639
[^magura_track]: Source: knowledge/notes/input_part002_review.md†L657-L657
[^kool_stop]: Source: knowledge/notes/input_part002_review.md†L547-L548
[^xtech_wet]: Source: knowledge/notes/input_part002_review.md†L549-L549
[^mt7_lever]: Source: knowledge/notes/input_part002_review.md†L569-L570
[^stahlflex]: Source: knowledge/notes/input_part002_review.md†L571-L571
[^ebc_pads]: Source: knowledge/notes/input_part002_review.md†L572-L572
[^trp_spyke]: Source: knowledge/notes/input_part002_review.md†L600-L600
[^m365_pad_compounds]: Source: knowledge/notes/all_part01_review.md†L501-L503
[^barrel_adjust]: Source: knowledge/notes/all_part01_review.md†L602-L602
[^pro2_rotor_pattern]: Source: knowledge/notes/all_part01_review.md†L502-L502
[^monorim_adapter_batch]: Source: knowledge/notes/all_part01_review.md†L503-L503
[^xtech_rotor_upgrade]: Source: knowledge/notes/all_part01_review.md†L736-L736
[^sensor_pop]: Source: knowledge/notes/all_part01_review.md†L628-L628
[^xtech-corrosion]: Source: knowledge/notes/denis_all_part02_review.md†L518-L518
[^denis-brake-clean]: Source: knowledge/notes/denis_all_part02_review.md†L867-L867
[^denis-armor]: Source: knowledge/notes/denis_all_part02_review.md†L868-L868
- **Front disc conversions demand discipline.** Learn modulation before hammering the lever, then upgrade calipers, spacers, and suspension brackets so heavier motors and wider tires clear without washing the front wheel.[^denis-front-disc]
- Reinforce Monorim and custom forks with thicker torque plates or “sandwich” steel stacks, relocate shocks, and consider Nutt calipers with sintered pads to carve clearance for 10×3.0 tires on AWD builds.[^denis-fork-reinforce]
- Mixed braking setups still work: some riders pair hydraulic fronts with Xiaomi e-brake levers in the rear for stable 50 km/h commutes, while others add Nutt calipers and brake-disc spacers to clear 80/65-6 tires without loose washer stacks.[^denis-mixed-brake]
