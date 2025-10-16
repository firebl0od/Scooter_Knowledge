# Brake Maintenance & Upgrade Guide

## TL;DR
- Hydraulic brake systems demand proper bleeding technique (level levers, flick hoses to vent micro-bubbles, patient lever cycling) and proactive seal maintenance to avoid spongy feel or sudden failures during high-speed stops.[^bleed-technique]
- Four-piston calipers provide superior thermal mass and stopping power for high-performance builds but require careful rotor sizing (180–203 mm) and clearance checks to avoid frame interference.[^four-piston]
- Wheel-centering kits and dual-caliper setups eliminate rotor wobble and improve braking consistency on racing builds, but add complexity and weight that commuter riders may not need.[^centering-kits]

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

### Preventing Seal Damage During Pad Changes
- skrtt burst an MT5 lever seal by pushing pistons back without cracking the bleed screw, so pad-swap guides need to stress releasing system pressure (or upgrading to metal levers) before compressing calipers to avoid hydraulic overload.[^seal-damage]
- **Safe pad replacement procedure:**
  1. Open caliper bleed screw slightly to relieve pressure
  2. Slowly push pistons back with flat tool (plastic tire lever or dedicated brake piston tool)
  3. Close bleed screw and verify no leaks
  4. Install new pads and bed them properly on first rides[^seal-damage]

## Brake Upgrades & Sizing

### Four-Piston Caliper Benefits
- Artem's freshly delivered Shimano M7120 four-piston set (≈€155 for the pair without rotors) brings stiffer one-finger levers and extra thermal mass that he plans to migrate from his trial bike to the scooter if he decides four pistons are overkill off-road.[^four-piston-cost]
- Four-piston systems improve heat dissipation during repeated high-speed stops but may be excessive for commuter builds under 60 km/h where two-piston Magura MT5 or similar calipers provide adequate stopping power.[^four-piston-vs-two]

### Regen Modulation Lessons
- Riders experimenting with high-force regen reported −80 A electronic braking nearly pitching them over the bars; most now tune Spinny/ADC profiles so regen complements (rather than replaces) hydraulic stoppers.【F:knowledge/notes/input_part008_review.md†L249-L249】
- Heavy scooters devour cheap pads even with regen assist—switching to metallic compounds such as Galfer keeps feel consistent when regen is dialed back for wet roads.【F:knowledge/notes/input_part008_review.md†L250-L251】

### Rotor Sizing Considerations
- Brake discussions suggest upsizing rotors from 180 mm to 203 mm mainly boosts thermal mass and leverage but may be excessive for scooters; larger rotors require frame clearance checks and stronger mounting tabs to handle increased braking forces.[^rotor-sizing]
- Segway GT2 rotors measure 2.42 mm thick (versus typical 1.8–2.0 mm commuter discs), providing superior warp resistance for repeated high-speed stops once Hope V4 or equivalent calipers are installed.[^gt2-rotors]

### Hope Tech/Tesch 3 Caliper Service
- 🇪🇸AYO#74's first successful Hope Tech/Tesch 3 rebuild covered piston re-greasing, compatible pad sizes, and bedding procedures that other riders can replicate for improved braking on high-power builds.[^hope-service]
- **Hope caliper maintenance tips:**
  - Disassemble calipers and clean pistons with isopropyl alcohol
  - Apply fresh brake-specific grease to piston seals (avoid petroleum-based products)
  - Verify pad backing plates are flat and not warped from heat
  - Bed new pads gradually with 10–15 moderate stops from 30 km/h before attempting hard braking[^hope-service]

## Ninebot F2 Pro Brake Upgrades
- cihan's wobble fix involved swapping to sintered pads and sourcing compatible rotors for the F2 Pro platform, demonstrating that budget commuter platforms benefit from modest brake improvements without requiring full hydraulic conversions.[^f2-upgrade]
- **F2 Pro brake upgrade recipe:**
  - Install sintered pads for better bite and longevity compared to organic pads
  - Source 120 mm rotors compatible with F2 Pro mounting pattern
  - Expect accelerated rotor wear compared to higher-grade steel on premium builds
  - Budget for rotor replacement every 1,000–2,000 km depending on riding style[^f2-upgrade]

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

## Tire Inflation & Bead Seating
- Haku's Xiaomi inflator couldn't seat 21×3 tires even with a ratchet strap, reinforcing that serious tubed slick installs demand higher-flow compressors (≥150 PSI, 2+ CFM) or shop assistance to pop beads properly.[^tire-inflation]
- **Compressor requirements for large tires:**
  - Minimum 150 PSI working pressure for 21×3 and larger tires
  - 2+ CFM flow rate to seat beads quickly before air leaks past unseated tire
  - Use bead seater tools or ratchet straps around tire circumference to help initial seating
  - Remove valve core temporarily during seating to maximize airflow, reinstall once beads are set[^tire-inflation]

## Brake Fluid & Compatibility
- Xtech hydraulic conversions rely on mineral oil (not DOT fluid) for Magura-compatible systems; Mirono bled his calipers with dual syringes and quickly abandoned the idea of using water after seeing trapped bubbles compromise lever feel.[^mineral-oil]
- **Fluid compatibility chart:**
  - **Magura, Shimano, Tektro:** Mineral oil only (DOT fluid damages seals)
  - **Hope, Hayes, Avid:** DOT 4 or DOT 5.1 (never DOT 5 silicone-based)
  - **Never mix fluids:** Contamination causes seal swelling and brake failure
  - Store mineral oil in sealed containers away from light to prevent oxidation[^fluid-compat]

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
[^hope-service]: Hope Tech/Tesch 3 caliper service covering piston re-greasing and pad compatibility.【F:knowledge/notes/input_part013_review.md†L677-L678】
[^f2-upgrade]: Ninebot F2 Pro brake upgrade using sintered pads and compatible rotors.【F:knowledge/notes/input_part013_review.md†L653-L653】
[^centering-kits]: Wheel-centering kits and dual-caliper setups for wobble elimination on 80/100H racing builds.【F:knowledge/notes/input_part013_review.md†L645-L647】
[^dual-caliper-when]: When to consider dual-caliper systems based on speed and use case.
[^regen-braking]: Matthew's regen-assisted braking demonstration showing mechanical brakes as backup.【F:knowledge/notes/input_part013_review.md†L635-L637】
[^tire-inflation]: Compressor requirements for seating 21×3 and larger tires with ratchet strap assistance.【F:knowledge/notes/input_part013_review.md†L761-L762】
[^mineral-oil]: Mineral oil requirement for Magura hydraulic systems and water bleeding failure.【F:knowledge/notes/input_part000_review.md†L567-L567】
[^fluid-compat]: Brake fluid compatibility chart for common hydraulic brake systems.
[^follow-centering]: Follow-up action to create wheel-centering and dual-caliper setup guide.【F:knowledge/notes/input_part013_review.md†L645-L647】
[^follow-dual-disc]: Follow-up action to document dual-disc vs. dual-caliper decision matrix.【F:knowledge/notes/input_part013_review.md†L635-L637】
