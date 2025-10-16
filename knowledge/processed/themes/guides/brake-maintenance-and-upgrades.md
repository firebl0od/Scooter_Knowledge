# Brake Maintenance & Upgrade Guide

## TL;DR
- Hydraulic brake systems demand proper bleeding technique (level levers, flick hoses to vent micro-bubbles, patient lever cycling) and proactive seal maintenance to avoid spongy feel or sudden failures during high-speed stops.[^bleed-technique]
- Four-piston calipers provide superior thermal mass and stopping power for high-performance builds but require careful rotor sizing (180–203 mm) and clearance checks to avoid frame interference.[^four-piston]
- Wheel-centering kits and dual-caliper setups eliminate rotor wobble and improve braking consistency on racing builds, but add complexity and weight that commuter riders may not need.[^centering-kits]
- Keep at least one mechanical brake active even on regen-heavy builds—logs show regen-only riding overheats controllers quickly, and dual-motor setups still rely on mechanical rotors to stop safely when electronics fault.【F:knowledge/notes/input_part004_review.md†L222-L222】【F:knowledge/notes/input_part004_review.md†L230-L230】

## Bleeding Techniques

### Magura MT5/MT7 Bleeding Procedure
- Successful Magura bleeds require leveling the brake lever, repeatedly flicking the hose to vent micro-bubbles, and patiently cycling the lever until the feel firms up—this mirrors bicycle-service best practices the community plans to document more thoroughly.[^magura-bleed]
- **Step-by-step bleeding:**
  1. Remove pads and install bleed block to protect pistons during bleeding
  2. Level the brake lever horizontally to ensure air naturally rises toward reservoir
  3. Attach syringe to caliper bleed port, fill with mineral oil (DOT fluid damages Magura seals)
  4. Open lever reservoir and insert second syringe or funnel
  5. Gently push fluid from caliper toward lever while flicking hose to dislodge bubbles
  6. Cycle brake lever slowly (5–10 times) to work out remaining air
  7. Top off reservoir, close ports, reinstall pads and test lever firmness[^magura-bleed]
- 🇪🇸AYO#74 also swapped to a higher-flow bleed needle to tighten Shimano/Magura lever feel, noting the larger bore purged dead-zone bubbles faster than stock fittings.【F:knowledge/notes/input_part013_review.md†L228-L228】

### Preventing Seal Damage During Pad Changes
- skrtt burst an MT5 lever seal by pushing pistons back without cracking the bleed screw, so pad-swap guides need to stress releasing system pressure (or upgrading to metal levers) before compressing calipers to avoid hydraulic overload.[^seal-damage]
- **Safe pad replacement procedure:**
  1. Open caliper bleed screw slightly to relieve pressure
  2. Slowly push pistons back with flat tool (plastic tire lever or dedicated brake piston tool)
  3. Close bleed screw and verify no leaks
  4. Install new pads and bed them properly on first rides[^seal-damage]

### Pad Conditioning & Bedding
- Riders formed a “sanded pad club,” resurfacing pads before bedding to tame squeal and keep braking consistent after swapping to thicker rotors.【F:knowledge/notes/input_part012_review.md†L35-L35】

### Lever Durability Notes
- Magura composite lever hardware can snap with hand force—many owners preemptively swap to Shimano Saint or other metal bodies before trusting 3 mm rotors and high-torque braking setups.【F:knowledge/notes/input_part012_review.md†L34-L34】

## Brake Upgrades & Sizing

### Four-Piston Caliper Benefits
- Artem's freshly delivered Shimano M7120 four-piston set (≈€155 for the pair without rotors) brings stiffer one-finger levers and extra thermal mass that he plans to migrate from his trial bike to the scooter if he decides four pistons are overkill off-road.[^four-piston-cost]
- Four-piston systems improve heat dissipation during repeated high-speed stops but may be excessive for commuter builds under 60 km/h where two-piston Magura MT5 or similar calipers provide adequate stopping power.[^four-piston-vs-two]
- Zoom-branded hydraulics continue to underperform at speed—riders are standardising on Nutt, Magura MT5e, Shimano Saint, or Hope calipers paired with 3 mm reinforced 160 mm rotors to survive repeated 120→0 km/h stops, noting that Magura reservoirs can crack under extreme loads.【F:knowledge/notes/input_part000_review.md†L511-L511】
### Motorcycle-Caliper Imports (Kotto Example)
- Kotto’s 3 mm motorcycle kits deliver fierce bite out of the box but ship dry and oversized—expect to bleed them immediately and clearance thick rotors or caliper mounts so the hardware sits square on scooter forks.【F:knowledge/notes/input_part004_review.md†L221-L221】
### Regen Modulation Lessons
- Riders experimenting with high-force regen reported −80 A electronic braking nearly pitching them over the bars; most now tune Spinny/ADC profiles so regen complements (rather than replaces) hydraulic stoppers.【F:knowledge/notes/input_part008_review.md†L249-L249】
- Heavy scooters devour cheap pads even with regen assist—switching to metallic compounds such as Galfer keeps feel consistent when regen is dialed back for wet roads.【F:knowledge/notes/input_part008_review.md†L250-L251】
- Denis’ workshop now treats Magura-class hydraulics as mandatory once Pro 2 builds creep toward 80 km/h—Xtech hybrids can’t arrest the extra energy, so riders add lever sensors if they still want regen without sacrificing lever feel and plan a careful bleed after rerouting hoses.【F:knowledge/notes/denis_all_part02_review.md†L433-L433】

### Rotor Sizing Considerations
- Brake discussions suggest upsizing rotors from 180 mm to 203 mm mainly boosts thermal mass and leverage but may be excessive for scooters; larger rotors require frame clearance checks and stronger mounting tabs to handle increased braking forces.[^rotor-sizing]
- Magura MT7/MT5 calipers barely clear 2.9 mm Kaabo rotors—fresh pads or 3 mm aftermarket discs often rub unless you machine custom spacers—so many riders stick with stock Zoom calipers or thinner discs when chasing upgrades.【F:knowledge/notes/input_part002_review.md†L141-L142】
- Repeated 80–90 km/h stops roasted 120 mm rotors and overheated Magura MT8s; the crew now defaults to dual front brakes or 203 mm discs on heavy scooters to regain thermal margin.【F:data/vesc_help_group/text_slices/input_part002.txt†L11088-L11137】
- When rotors need a millimetre of offset, riders cut thin shim plates (nickel strip or torque-arm washers) instead of stacking round washers that flex loose under repeated braking loads.【F:data/vesc_help_group/text_slices/input_part002.txt†L11406-L11455】
- Premium rotors from Shimano, Magura, or Galfer stay on the shopping list while AliExpress specials are avoided for 70 km/h builds despite the price gap.【F:data/vesc_help_group/text_slices/input_part002.txt†L12102-L12151】
- Kaabo Wolf owners now swap to 3 mm Kaabo discs after stock rotors warped—confirm caliper spacing and expect longer life once the thicker rotors are paired with Wolf motors.【F:knowledge/notes/input_part011_review.md†L346-L351】
- Segway GT2 rotors measure 2.42 mm thick (versus typical 1.8–2.0 mm commuter discs), providing superior warp resistance for repeated high-speed stops once Hope V4 or equivalent calipers are installed.[^gt2-rotors]
- Tall brake adapters should use a single ring spacer instead of stacked washers so axial loads do not rock the disc bolts—5 mm steel rings have proven stable on custom Blade hubs, while 1.7 mm washer stacks remain a stopgap only.【F:knowledge/notes/input_part000_review.md†L520-L522】
- Expect to budget CNC time for bespoke rotor shims because six-hole aftermarket rims rarely align with Xiaomi five-hole spacers when mixing OEM and custom hubs.【F:knowledge/notes/input_part000_review.md†L521-L522】
### Fork & Adapter Fitment
- Monorim fork swaps need custom torque arms, thin-head bolts, and stacked stainless shims so 140–160 mm discs clear the square legs without grinding away the casting—document CAD references before committing to the conversion.【F:knowledge/notes/input_part000_review.md†L512-L512】
- Sombre_enfant warned that custom brackets held on with M5 bolts will ovalise mounts under MT7 loads—upgrade to snug M6/M8 hardware and machined adapters before trusting 100 km/h stops.[^m6-brackets]
- VSETT riders swapping the stock 140 mm rotors for 160 mm SRAM Cleansweep or 180 mm Magura MDR-P discs report dramatically better torque and heat rejection, but the upgrade only works if you retire washer stacks for purpose-built brackets and re-align pads to prevent warped rotors.【F:data/vesc_help_group/text_slices/input_part001.txt†L8211-L8253】
### External Hose Routing & Quick-Disconnect Hardware
- Rerouting Magura hoses outside the fork demands the correct short banjo bolts and bleed screws; mixing long/short clamp screws has already shorted controller phases, so standardise hardware before final assembly.【F:data/vesc_help_group/text_slices/input_part001.txt†L9208-L9211】
- The Elvedes Hydro Parts Kit supplies dual M8 banjos for clean fork exits, while Jagwire’s quick-disconnect system costs roughly $120–$125 for enough hose and couplers to outfit dual-motor scooters and requires committing to Jagwire hose diameters.【F:data/vesc_help_group/text_slices/input_part001.txt†L9522-L9538】【F:data/vesc_help_group/text_slices/input_part001.txt†L9901-L10054】
- Hope’s HFA701 kit bundles the correct M6 banjos and bleed screws; if you piece together individual fittings from Venhill, Trickstuff, or AliExpress, match barb dimensions to hose ID or you will fight leaks during the first bleed.【F:data/vesc_help_group/text_slices/input_part001.txt†L9947-L10216】
- Even with premium hardware, external routing can crush Magura MT7 lines after flats or tire swaps—inspect clearance after every wheel service and carry spare banjos plus hoses for roadside replacements.【F:knowledge/notes/input_part001_review.md†L642-L644】
### Semi-Hydraulic Caliper Limitations
- XTech-style semi-hydraulic calipers carry minimal oil volume, rely on rattly auto-centering hardware, and have warped rotors on scooters above 60 km/h—upgrade to sturdier discs, avoid flimsy quad calipers, and inspect the whole brake stack after flats or heavy emergency stops.【F:data/vesc_help_group/text_slices/input_part001.txt†L20680-L20760】
- Track abuse already pushed Magura calipers past the Curie point (>700 °C), wiping magnetism and underscoring the need for engine braking or larger rotors on race builds before mechanical fade sets in.【F:data/vesc_help_group/text_slices/input_part003.txt†L8386-L8400】
- 100 km/h track logs keep comparing Trickstuff, Kool-Stop, Shimano, and XLC rotors—prep extra thermal mass, ventilation, and pad choices before sprint sessions so glowing hardware doesn’t demagnetise calipers or chew pads mid-run.【F:knowledge/notes/input_part003_review.md†L103-L103】
- Dual-rotor experiments now include Trickstuff, Kool-Stop, Shimano Saint, Ashima, and XLC floating discs; the budget XLC hardware bites hard but its floating hardware feels suspect on dual G30 conversions, so budget inspections between sessions.【F:data/vesc_help_group/text_slices/input_part003.txt†L11517-L11570】【F:data/vesc_help_group/text_slices/input_part003.txt†L11935-L11970】
- Bosch’s e-bike ABS pairs cleanly with Magura CMe5 levers, giving scooters a path to anti-lock hydraulics while still functioning as premium standalone brakes if you skip the controller module.【F:knowledge/notes/input_part003_review.md†L166-L166】
- Brakestuff 3 mm rotors reward precise setup—Magura Saints squeal if runout isn’t near perfect, but Hope Tech 4 V4 calipers on the same discs delivered the strongest stops the testers have measured so far.【F:data/vesc_help_group/text_slices/input_part004.txt†L7401-L7405】【F:data/vesc_help_group/text_slices/input_part004.txt†L7469-L7472】
- Custom rotor projects now target 203 mm discs cut from 2.3–2.5 mm acid-proof steel, but Magura calipers only clear ≈2.1 mm—budget runout checks and pad clearance before ordering thicker hardware.【F:knowledge/notes/input_part006_review.md†L375-L375】
- Magura and TRP four-piston setups expect 2.0–2.3 mm rotors, and AliExpress Brembo clones often ship in left/right-specific pairs—verify orientation when ordering for right-hand-drive scooters to avoid fitment surprises.【F:knowledge/notes/input_part006_review.md†L123-L123】
### Magura MT5e Kits & Setup
- Community carts keep landing full MT5e front/rear kits around $200, and Jenson USA ships globally via DHL—several riders noted the pricing is better than expected for four-piston hydraulics.[^mt5e-pricing]
- Burnout-focused builders sometimes leave the MT5e e-brake sensors unplugged or repurpose a single caliper while waiting on replacements; strip non-essential electrical loads when testing to confirm the new hydraulics clear the fork and wiring bundles.[^mt5e-sensors]
- Inspect bundled levers before trusting them—Jan flagged one aftermarket lever as “the worst” thanks to plastic threads and screws despite pairing with Magura calipers, so budget for higher-quality levers if the kit feels flimsy.[^bad-lever]
- Rotor slot orientation matters—aim the cooling slots forward on the front wheel, but flip a rear rotor if the slots face the wrong direction after a wheel swap so debris clears properly.【F:data/vesc_help_group/text_slices/input_part009.txt†L12472-L12477】
- Rim brakes gouged paint and underperformed on Haku’s 20 mph minibike conversion—plan disc-ready wheels or fabricate caliper mounts if you need real stopping power beyond low-speed duty.【F:data/vesc_help_group/text_slices/input_part009.txt†L21004-L21007】
### Compact Lever & Sensor Options
- For builds that cannot fit full-size brake levers, the crew recommends child-sized handles with built-in e-brake switches or even spare thumb throttles rewired as brake inputs to keep regen triggers within reach on narrow cockpits.【F:data/vesc_help_group/text_slices/input_part009.txt†L20306-L20327】
- Wuxing’s budget 115PDD lever closes a simple loop when pulled, making it a drop-in cut-off option for commuters that need electrical braking without hunting premium hardware.【F:data/vesc_help_group/text_slices/input_part009.txt†L20306-L20327】
- Whenever possible, choose hall-based brake levers over binary switches—especially for small hands—and pair hydraulic setups with magnetic two-pin sensors like the modules 🇪🇸AYO#74 installs on high-power scooters to guarantee consistent regen cues.【F:data/vesc_help_group/text_slices/input_part009.txt†L20536-L20556】【F:data/vesc_help_group/text_slices/input_part009.txt†L20928-L20934】【F:data/vesc_help_group/text_slices/input_part009.txt†L21186-L21187】
- Riders pushing highway pulls on a single rear brake, such as Shlomozero’s Zero running a lone Nutt caliper plus regen, were urged to upgrade to Magura or Shimano Saint-class dual setups before continuing 100 km/h testing.【F:data/vesc_help_group/text_slices/input_part009.txt†L21214-L21232】
- Apo cautioned that motorcycle Brembo calipers demand thicker rotors and extra fork clearance than most scooter chassis provide, so premium bicycle systems remain the realistic upgrade path until frames adopt moto-style mounts.【F:knowledge/notes/input_part010_review.md†L261-L262】
- Yamal warned that floating bicycle rotors look flashy but perform worse on high-power scooters—stick with proven solid discs for consistent bite.【F:knowledge/notes/input_part010_review.md†L262-L263】
- Yamal and 🇪🇸AYO#74 still favour the solid 3 mm “Wolf” discs from AliExpress—non-floating despite the two-piece look—because they survive where riveted rotors sheared; at ≈€30 online (vs. €80–100 retail) riders buy them in sets of four.【F:data/vesc_help_group/text_slices/input_part010.txt†L18701-L18712】
- Brake-Stuff’s Shimano-pattern 6-bolt rotors are proving durable replacements for worn discs on VESC conversions—Yamal’s installs slot straight onto common hubs when builders want mid-tier pricing without sacrificing material quality.【F:knowledge/notes/input_part010_review.md†L391-L392】
### Superbikes & Heat Management
- Racers weighing €1.2 k Trickstuff Maxima kits against Magura MT5/MT7 setups note that motorcycle Brembos rarely clear scooter forks; 150 km/h stopping demands bigger rotors and higher-volume masters no matter which premium caliper you choose.【F:knowledge/notes/input_part011_review.md†L368-L374】
- 3 mm × 170 mm rotors dramatically stiffen braking response but require retracting pistons fully for clearance and a quick true after the first bedding stops.【F:knowledge/notes/input_part012_review.md†L33-L33】
- A commuter who bent a Vsett rotor mid-ride now keeps spares on hand and leans on e-brakes when mechanical hardware warps unexpectedly—plan redundancy for traffic incidents.【F:knowledge/notes/input_part012_review.md†L186-L186】
- Skrtt’s 2.3 mm rotor experiments required shaving calipers while 🇪🇸AYO#74 stressed using “elevator” spacers to clear thicker discs—document allowable rotor thickness per caliper so riders stop guessing on machining limits.【F:knowledge/notes/input_part013_review.md†L161-L161】
- Ausias is milling Magura MT5 calipers “radially” to clear 3.6 mm rotors; peers warned most bicycle brakes expect ≤2.8 mm discs, so publish machining tolerances, lever upgrades, and testing steps before anyone copies the mod.【F:knowledge/notes/input_part013_review.md†L376-L378】
- Hope Tech Evo calipers routinely sell for €260–€300 (≈$300) per end; racers have found 3 mm rotors clear the four-piston bodies when regen remains primary braking, reinforcing that premium stopping power demands both budget planning and rotor-thickness checks.[^hope-pricing]
- Paolo’s rotor group buy keeps blanks at 2 mm so stock calipers bolt up; builders confirm Magura MT5 Pro units can swallow 2.7 mm rotors and trimmed Nutt four-piston calipers clear 3 mm, but thicker discs raise costs and require caliper mods many riders skip.[^rotor-thickness]
- Jan’s hardened 420C 160 mm rotors landed at 45 € plus shipping; prototypes survived light bicycle testing but still need scooter-load validation—log bedding, braking torque, and temperature before committing to fleet orders.【F:data/vesc_help_group/text_slices/input_part014.txt†L10221-L10228】
- Spintend detachable rims still favour 160 mm, ≈2.7 mm rotors so riders can stock one spare width; jumping to 180 mm adds leverage but risks front-wheel skids unless chassis geometry and modulation keep up.【F:data/vesc_help_group/text_slices/input_part014.txt†L10613-L10622】【F:data/vesc_help_group/text_slices/input_part014.txt†L10616-L10619】
- 160 mm rotor upgrades on Xiaomi frames need careful spacing—builders raised calipers or machined thicker adapters so disc bolts stop striking tire adapters after aggressive braking tests on AWD/RWD conversions.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89952-L90018】

### Hope Tech/Tesch 3 Caliper Service
- 🇪🇸AYO#74's first successful Hope Tech/Tesch 3 rebuild covered piston re-greasing, compatible pad sizes, and bedding procedures that other riders can replicate for improved braking on high-power builds.[^hope-service]
- Kaabo Wolf riders source rear Magura adapters from Javamba after discovering flipped front hubs could not accommodate left-side calipers—keep vendor links handy before tearing down the rear motor.【F:knowledge/notes/input_part011_review.md†L406-L408】
- AliExpress shim kits (2–5 mm rotors spacers plus washers) keep oversized calipers from fouling hub flanges, giving Dualtron and Kaabo owners a cheap path to widen rotor stance without machining custom spacers.【F:knowledge/notes/input_part011_review.md†L304-L308】
- **Hope caliper maintenance tips:**
  - Disassemble calipers and clean pistons with isopropyl alcohol
  - Apply fresh brake-specific grease to piston seals (avoid petroleum-based products)
  - Verify pad backing plates are flat and not warped from heat
  - Bed new pads gradually with 10–15 moderate stops from 30 km/h before attempting hard braking[^hope-service]

## Ninebot F2 Pro Brake Upgrades

## Ninebot G30 Brake Retrofits
- 3D-printed rear brake adapters with thin aluminium reinforcement rings drew skepticism about PLA strength at 60 km/h; riders recommend CNC or full-metal conversions before trusting repeated hard stops.【F:data/vesc_help_group/text_slices/input_part002.txt†L3214-L3249】
- Fitting 10×3 in tyres demands trimming the rear fender and routing the brake hose internally instead of relying on inverted Magura mods to keep wobble away.【F:data/vesc_help_group/text_slices/input_part002.txt†L3536-L3551】
- cihan's wobble fix involved swapping to sintered pads and sourcing compatible rotors for the F2 Pro platform, demonstrating that budget commuter platforms benefit from modest brake improvements without requiring full hydraulic conversions.[^f2-upgrade]
- Expect odd hardware: the F2 Pro uses a 51 mm post mount and five-bolt rotor pattern, so riders stack sturdier post-to-post adapters (avoiding soft Monorim brackets) and often jump to 140 mm rotors to keep pad contact when stacking spacers.【F:knowledge/notes/input_part007_review.md†L348-L352】
- **F2 Pro brake upgrade recipe:**
  - Install sintered pads for better bite and longevity compared to organic pads
  - Source inexpensive soft rotors compatible with the F2 Pro mounting pattern—cihan is happy to burn through €2 discs in exchange for the stability boost once they warm up
  - Expect accelerated rotor wear compared to higher-grade steel on premium builds
  - Budget for rotor replacement every 1,000–2,000 km depending on riding style[^f2-upgrade]
- **Hydraulic retrofit fitment.** 1200 W Blade and Monorim front ends accept full hydraulic kits with 2 m hoses, but expect adapter sourcing drama on Xiaomi frames—pre-fit brackets and hose routing before committing to the swap.【F:data/vesc_help_group/text_slices/input_part003.txt†L11882-L11884】

- **Regen-only braking has limits.** Francois is temporarily riding a front drum plus −90 A motor brake while waiting on display parts—a reminder that regen alone can’t cover emergency stops and should stay supplemental to mechanical brakes.【F:knowledge/notes/input_part013_review.md†L163-L163】【F:knowledge/notes/input_part013_review.md†L5639-L5653】

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
- Don’t run highway speeds on a single rear brake—Shlomozero’s Zero 10X is still on a lone Nutt four-piston with regen, and the crew keeps pushing riders toward Magura or Saint-class dual setups before continuing 100 km/h pulls.【F:data/vesc_help_group/text_slices/input_part009.txt†L21214-L21232】

## Tire Inflation & Bead Seating
- Haku's Xiaomi inflator couldn't seat 21×3 tires even with a ratchet strap, reinforcing that serious tubed slick installs demand higher-flow compressors (≥150 PSI, 2+ CFM) or shop assistance to pop beads properly.[^tire-inflation]
- Roadside swaps go smoother when you break the bead with dish soap, dust tubes in talc or baby powder, and reassemble carefully—the combo stops inner-tube chafing after emergency tire pulls.【F:knowledge/notes/input_part000_review.md†L669-L670】
- PMT 110/55 R6.5 slicks feel vague at the 2.2 bar sidewall spec; experienced tuners run ~3.5 bar for crisp handling without reported failures.【F:knowledge/notes/input_part006_review.md†L162-L162】
- Ratchet straps or belts cinched around 11–12″ tubeless tires let portable pumps pop beads once the carcass is preloaded—ideal when you need a trail-side seating trick without a shop compressor.【F:data/vesc_help_group/text_slices/input_part009.txt†L6281-L6333】
- Installing solid tires goes faster if you heat the tire (boiling water or a microwave for ~10–15 minutes), brace the hub on the floor, lever with two irons, then finish with soapy water so the bead seats evenly.【F:data/vesc_help_group/text_slices/input_part009.txt†L8387-L8398】
- **Compressor requirements for large tires:**
  - Minimum 150 PSI working pressure for 21×3 and larger tires
  - 2+ CFM flow rate to seat beads quickly before air leaks past unseated tire
  - Use bead seater tools or ratchet straps around tire circumference to help initial seating
  - Remove valve core temporarily during seating to maximize airflow, reinstall once beads are set[^tire-inflation]
- Stock extra casings and tubes—one PMT puncture forced a 4 km walk, highlighting how quickly high-speed tires destroy rims when no spare is available.【F:knowledge/notes/input_part012_review.md†L37-L37】
## Hose & Banjo Hardware
- Dualtron owners flipping banjo orientation often choose Fastride’s stainless dual-M8 kit (~€40) because it includes crush washers and O-rings, avoiding piecemeal sourcing for hose reroutes.【F:knowledge/notes/input_part012_review.md†L38-L38】
## Brake Fluid & Compatibility
- Xtech hydraulic conversions rely on mineral oil (not DOT fluid) for Magura-compatible systems; Mirono bled his calipers with dual syringes and quickly abandoned the idea of using water after seeing trapped bubbles compromise lever feel.[^mineral-oil]
- DOT 5/5.1 silicone formulas eat the seals in Magura and Shimano systems—stick with mineral oil and consider Trickstuff Bionol for downhill scooters because its 300–420 °C boiling range survives the heat that cooks stock fluids.[^dot5-warning]
- Split tubeless rims still respond best to ratchet straps plus high-flow compressors; skrtt’s bead only sealed after cinching the carcass, and the crew explicitly discouraged flammable “quick seat” tricks—document the safe workflow before recommending tubeless conversions.【F:knowledge/notes/input_part013_review.md†L196-L197】
## Wheel & Rim References
- Rage’s CNC rim for Fastgirl measures 65 mm internal width for 11″ 90/65 tires, closely matching skrtt’s new 33×2 profile—log those dimensions so tire-fit calculators stop relying on guesses.【F:knowledge/notes/input_part013_review.md†L131-L131】
- Mixing Shimano and Magura mineral oils proved safe during field tests, but the crew still monitors lever seals after the swap to confirm no swelling or leaks creep in post-service.【F:knowledge/notes/input_part013_review.md†L228-L229】
- **Fluid compatibility chart:**
  - **Magura, Shimano, Tektro:** Mineral oil only (DOT fluid damages seals)
  - **Hope, Hayes, Avid:** DOT 4 or DOT 5.1 (never DOT 5 silicone-based)
  - **Never mix fluids:** Contamination causes seal swelling and brake failure
  - Store mineral oil in sealed containers away from light to prevent oxidation[^fluid-compat]
- Shimano MT-series kits ship pre-bled but still need hoses re-threaded through stems, a follow-up bleed, and either the €15 EZ-MTB service kit or clever improvisation; riders have finished jobs with Total LHM Plus or even baby oil when OEM fluid ran out.[^shimano-mt]

## Hydraulic Sensor Retrofits
- Builders add hall sensors or reed switches to existing hydraulic levers when they need proportional regen or kill-switch behaviour, freeing them from the limited OEM sensored lever catalog.[^hall-retrofit]
- When extending short Magura bicycle hoses, reuse the correct olives and barbs at each end—aftermarket lines such as Jagwire Pro handle higher pressure but still leak if the hardware mismatch leaves gaps at the caliper or lever.[^jagwire-hardware]
## Post-Flood Brake Recovery
- Flood-soaked calipers should be stripped, scrubbed with dedicated brake cleaner, and dried before touching WD-40 or silicone sprays—those products swell seals and leave corrosion that will seize pistons again.[^flood-recovery]
### High-Heat Hydraulic Practices
- **Leave reservoir headroom.** Mountain-pass riders boiling 360 °C Trickstuff Bionol in Magura MT7 stacks watched the banjo burp once expansion had nowhere to go—bleed with a visible air gap so thermal growth doesn’t pop seals mid-descent.[^bionol-flash]
- **Prioritise front stopping power.** Community logs keep stressing that rear-only braking just locks and skids; pair a strong front hydraulic with regen on both controllers whenever possible so emergency stops stay controllable.[^front-priority]
- **Upgrade rotors for high voltage.** Shimano “resin only” 160 mm discs fade instantly on 72 V scooters—step up to 2 mm-thick metallic-ready rotors and full-hydraulic calipers before raising pack voltage.[^resin-rotor]
- **Inspect hardware after heat events.** That same MT7/MT8 build now budgets pad checks and rotor swaps after every downhill session because fluid flash cooked fittings despite premium components.[^post-heat-service]

## Follow-Up Actions Needed
- Write up an 80/100 H wheel-centering and dual-caliper setup guide (kit sourcing, torque, clearance checks) so track-focused Nami/Dualtron builds can copy the wobble fix.[^follow-centering]
- Turn the dual-disc vs. dual-caliper debate—and Matthew's regen save—into a braking guide that spells out when dual rotors help, how to size levers/calipers, and why regen can't replace hydraulics on high-speed builds.[^follow-dual-disc]

## Source Notes
[^bleed-technique]: Magura bleeding technique emphasizing level levers, hose flicking, and patient lever cycling.【F:knowledge/notes/input_part013_review.md†L388-L388】
[^magura-bleed]: Successful Magura MT5/MT7 bleed procedure following bicycle-service best practices.【F:knowledge/notes/input_part013_review.md†L388-L388】
[^seal-damage]: MT5 lever seal burst from pushing pistons without relieving pressure via bleed screw.【F:knowledge/notes/input_part013_review.md†L758-L760】
[^four-piston-cost]: Shimano M7120 four-piston caliper pricing and thermal mass benefits.【F:knowledge/notes/input_part000_review.md†L567-L567】
[^four-piston-vs-two]: Four-piston caliper benefits for high-performance builds vs. two-piston sufficiency for commuters.
[^rotor-sizing]: Rotor sizing from 180 mm to 203 mm for thermal mass and leverage, with frame clearance warnings.【F:knowledge/notes/input_part014_review.md†L43-L43】
[^gt2-rotors]: Segway GT2 2.42 mm rotors providing warp resistance for repeated high-speed stops.【F:knowledge/notes/input_part006_review.md†L357-L357】
[^m6-brackets]: Oversized hydraulic setups demand M6/M8 hardware and tight-tolerance adapters; M5 bolts quickly elongate mounts under MT7 braking loads.【F:data/vesc_help_group/text_slices/input_part001.txt†L4671-L4707】
[^mt5e-pricing]: Magura MT5e front/rear kits hovering around $200 shipped via Jenson USA/DHL impressed riders expecting higher prices.【F:knowledge/notes/input_part007_review.md†L109-L130】
[^mt5e-sensors]: Riders testing MT5e swaps left e-brake sensors unplugged, stripped non-essential loads, and double-checked caliper clearance while waiting on any missing hardware.【F:knowledge/notes/input_part007_review.md†L130-L130】
[^bad-lever]: Jan called out a Magura-compatible lever with plastic threads/screws as the worst he has used—treat cheap bundles as suspect.【F:knowledge/notes/input_part007_review.md†L147-L147】
[^hope-pricing]: Hope Tech Evo pricing and 3 mm rotor clearance observations from group buys.【F:knowledge/notes/input_part014_review.md†L3124-L3163】
[^hope-service]: Hope Tech/Tesch 3 caliper service covering piston re-greasing and pad compatibility.【F:knowledge/notes/input_part013_review.md†L677-L678】
[^f2-upgrade]: Ninebot F2 Pro brake upgrade using sintered pads and compatible rotors.【F:data/vesc_help_group/text_slices/input_part013.txt†L8828-L8831】
[^centering-kits]: Wheel-centering kits and dual-caliper setups for wobble elimination on 80/100H racing builds.【F:knowledge/notes/input_part013_review.md†L645-L647】
[^dual-caliper-when]: When to consider dual-caliper systems based on speed and use case.
[^regen-braking]: Matthew's regen-assisted braking demonstration showing mechanical brakes as backup.【F:knowledge/notes/input_part013_review.md†L635-L637】
[^tire-inflation]: Compressor requirements for seating 21×3 and larger tires with ratchet strap assistance.【F:knowledge/notes/input_part013_review.md†L761-L762】
[^mineral-oil]: Mineral oil requirement for Magura hydraulic systems and water bleeding failure.【F:knowledge/notes/input_part000_review.md†L567-L567】
[^dot5-warning]: DOT 5/5.1 destroys Magura/Shimano seals; Trickstuff Bionol offers a mineral-oil alternative rated to ~420 °C for heat-soaked scooters.【F:knowledge/notes/input_part002_review.md†L24-L26】
[^fluid-compat]: Brake fluid compatibility chart for common hydraulic brake systems.
[^hall-retrofit]: Adding hall or reed sensors to any hydraulic lever unlocks proportional regen or kill-switch control without hunting rare OEM sensored levers.【F:knowledge/notes/input_part002_review.md†L26-L27】
[^jagwire-hardware]: Jagwire Pro hoses outperform stock Magura lines, but the correct olives/barbs are mandatory at each end to prevent leaks after re-termination.【F:knowledge/notes/input_part002_review.md†L26-L27】
[^flood-recovery]: Post-flood brakes revive when stripped, cleaned with brake cleaner, and finished with PTFE lube once dry—WD-40 or silicone swell seals and leave rust behind.【F:knowledge/notes/input_part002_review.md†L29-L30】
[^follow-centering]: Follow-up action to create wheel-centering and dual-caliper setup guide.【F:knowledge/notes/input_part013_review.md†L645-L647】
[^follow-dual-disc]: Follow-up action to document dual-disc vs. dual-caliper decision matrix.【F:knowledge/notes/input_part013_review.md†L635-L637】
- **Cool overheated brakes while rolling.** Riders who stop immediately after smoking a Magura caliper trap heat, boil fluid, and face a full re-bleed—keep the scooter moving to shed heat before coming to rest after heavy stops.【F:data/vesc_help_group/text_slices/input_part004.txt†L4146-L4156】
[^bionol-flash]: Trickstuff Bionol flashed in a Magura MT7 stack, venting fluid through the banjo because the reservoir was overfilled before the descent.【F:knowledge/notes/input_part006_review.md†L12-L13】
[^front-priority]: Riders reiterating that strong front hydraulics plus dual electronic braking provide real stopping power; rear-only braking just slides.【F:knowledge/notes/input_part006_review.md†L14-L14】
[^resin-rotor]: Shimano “resin only” 160 mm rotors failing on 72 V scooters and the recommendation to run 2 mm metallic-ready discs with hydraulic calipers instead.【F:knowledge/notes/input_part006_review.md†L15-L15】
[^post-heat-service]: Premium MT7/MT8 builds scheduling pad and rotor inspections after every downhill session once high-temp fluid flashes exposed weak hardware.【F:knowledge/notes/input_part006_review.md†L12-L13】
[^shimano-mt]: Shimano MT-series kits still need hoses re-threaded through stems, a fresh bleed, and either the €15 EZ-MTB kit or improvised tools; Total LHM Plus or baby oil has stood in for mineral fluid in a pinch.【F:knowledge/notes/input_part007_review.md†L238-L238】
[^rotor-thickness]: Paolo’s rotor group buy sticking with 2 mm blanks and caliper clearance notes for 2.7–3 mm discs.【F:knowledge/notes/input_part014_review.md†L10356-L10365】
- **Support cable housing runs.** Zip-tie the housing to the frame and trim excess slack before chasing pad or caliper issues—every bit of housing flex steals lever travel and torpedoes braking force.【F:knowledge/notes/denis_all_part02_review.md†L348-L349】
