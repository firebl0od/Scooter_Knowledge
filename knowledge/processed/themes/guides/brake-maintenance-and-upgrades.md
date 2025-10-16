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

### Rotor Sizing Considerations
- Brake discussions suggest upsizing rotors from 180 mm to 203 mm mainly boosts thermal mass and leverage but may be excessive for scooters; larger rotors require frame clearance checks and stronger mounting tabs to handle increased braking forces.[^rotor-sizing]
- Segway GT2 rotors measure 2.42 mm thick (versus typical 1.8–2.0 mm commuter discs), providing superior warp resistance for repeated high-speed stops once Hope V4 or equivalent calipers are installed.[^gt2-rotors]
- Custom rotor projects now target 203 mm discs cut from 2.3–2.5 mm acid-proof steel, but Magura calipers only clear ≈2.1 mm—budget runout checks and pad clearance before ordering thicker hardware.【F:knowledge/notes/input_part006_review.md†L375-L375】
- Magura and TRP four-piston setups expect 2.0–2.3 mm rotors, and AliExpress Brembo clones often ship in left/right-specific pairs—verify orientation when ordering for right-hand-drive scooters to avoid fitment surprises.【F:knowledge/notes/input_part006_review.md†L123-L123】

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
- PMT 110/55 R6.5 slicks feel vague at the 2.2 bar sidewall spec; experienced tuners run ~3.5 bar for crisp handling without reported failures.【F:knowledge/notes/input_part006_review.md†L162-L162】
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
[^bionol-flash]: Trickstuff Bionol flashed in a Magura MT7 stack, venting fluid through the banjo because the reservoir was overfilled before the descent.【F:knowledge/notes/input_part006_review.md†L12-L13】
[^front-priority]: Riders reiterating that strong front hydraulics plus dual electronic braking provide real stopping power; rear-only braking just slides.【F:knowledge/notes/input_part006_review.md†L14-L14】
[^resin-rotor]: Shimano “resin only” 160 mm rotors failing on 72 V scooters and the recommendation to run 2 mm metallic-ready discs with hydraulic calipers instead.【F:knowledge/notes/input_part006_review.md†L15-L15】
[^post-heat-service]: Premium MT7/MT8 builds scheduling pad and rotor inspections after every downhill session once high-temp fluid flashes exposed weak hardware.【F:knowledge/notes/input_part006_review.md†L12-L13】
