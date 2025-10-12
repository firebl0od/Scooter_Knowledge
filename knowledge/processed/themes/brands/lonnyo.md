# Lonnyo Hub Motor Dossier

## TL;DR
- Lonnyo’s stator codes map cleanly to use cases: 17×4 torque, 22×3 “standard”, and 33×2 high-speed winds, with riders stepping up to 80H/100H cores when chasing 150 km/h builds or >300 A phase targets.【F:knowledge/notes/input_part011_review.md†L288-L293】【F:knowledge/notes/input_part011_review.md†L328-L329】
- Real-world current envelopes show 22×3 hubs settling near 110–150 A battery and ~300 A phase on Spintend 75/200-class controllers, while single Ubox 85150 installs bump into a ~150 A firmware ceiling regardless of higher software limits.【F:knowledge/notes/input_part011_review.md†L309-L311】【F:knowledge/notes/input_part011_review.md†L340-L353】
- Packaging is the gating factor above 70H: the 100H cans require ≈183 mm dropouts plus custom shock brackets, 80H swaps need 155 mm fork spacing and longer caliper studs, and even 70H hubs ship unsealed—expect a full bearing and weatherproofing job before first ride.【F:knowledge/notes/input_part011_review.md†L365-L417】【F:knowledge/notes/input_part011_review.md†L482-L483】【F:knowledge/notes/input_part011_review.md†L531-L536】【F:knowledge/notes/input_part011_review.md†L463-L465】

## Motor Lineup & Sourcing Signals
| Wind | Typical Stator | Community Use Case | Notes |
| --- | --- | --- | --- |
| 17×4 | 40H torque cores | Launch torque for hill-heavy or cargo builds | Keeps amperage modest but caps top speed; often paired with thicker packs instead of field weakening.【F:knowledge/notes/input_part011_review.md†L328-L329】【F:knowledge/notes/input_part011_review.md†L431-L434】 |
| 22×3 | 40H/65H standard | Balanced street setups targeting 120–150 km/h with traction control | Riders log 200 A-per-motor goals but admit traction is the bottleneck without TC or race tires.【F:knowledge/notes/input_part011_review.md†L288-L289】 |
| 33×2 | 80H/100H speed | Highway-speed touring and race builds | Requires flawless tuning and long, straight courses to exploit; many owners resell 22×3 sets to fund the jump.【F:knowledge/notes/input_part011_review.md†L288-L289】 |
| 70H | 22×3 torque refresh | Waterproofed commuter upgrade | Ships dry—budget bearings, seals, and coatings up front.【F:knowledge/notes/input_part011_review.md†L463-L465】 |
| 80H | 33×2 performance | Step between 22×3 and 100H | Arrive with halls/NTCs, cost ≈€736 without rims, and need 155 mm dropouts plus longer pivot hardware.【F:knowledge/notes/input_part011_review.md†L482-L483】【F:knowledge/notes/input_part011_review.md†L531-L536】【F:knowledge/notes/input_part011_review.md†L628-L628】 |
| 100H | 33×2 race | Extreme builds chasing 600 A phase stacks | Measure ~183 mm across the axle and force bespoke suspension mounts before pairing with 3Shul 400 A or dual Tronic stacks.【F:knowledge/notes/input_part011_review.md†L365-L417】 |

**Procurement watchpoints.** Genuine 65H 22×3 hubs hover near $205 (~€315 landed), but veterans warn that many “90H” listings hide cheaper 80–85H stators and customs fees can erase gray-market savings. Keep receipts, request stator photos, and budget for duties when importing to stricter regions.【F:knowledge/notes/input_part011_review.md†L292-L293】

## Electrical Envelopes & Controller Pairings
- **Spintend 75/200 & 75/240 (dual):** Treat 22×3 Lonnyos as ~150 A battery / 300 A phase hardware. Race setups trim battery current toward 110 A to keep thermal headroom for field weakening or regen bursts.【F:knowledge/notes/input_part011_review.md†L309-L311】
- **Single Ubox 85150 installs:** Multiple riders hit a hard ~150 A phase ceiling even with 210–280 A software targets; Statorade plus ≤20 % saturation compensation keeps temps manageable but doesn’t lift the cap. Suspect firmware or BMS enforcement before chasing hardware mods.【F:knowledge/notes/input_part011_review.md†L340-L353】
- **Dual-drive traction planning:** Without traction control, dual 22×3 builds spin tires around 200 A per motor; expect to log duty-cycle and slip data before pushing beyond that envelope. Pair fast-wind 33×2 motors with high-voltage packs (≥22 S) and stable suspension to actually translate current into road speed.【F:knowledge/notes/input_part011_review.md†L288-L289】
- **Controller synergy for 100H projects:** Pandalgns budgets 3Shul 400 A stages and 30 S packs once the chassis accepts the 100H cans, underscoring the need for Seven-class controllers or Tronic X12 pairs when stator surface area finally stops being the bottleneck.【F:knowledge/notes/input_part011_review.md†L365-L417】

## Chassis Fitment & Fabrication Checklist
1. **Measure dropouts before ordering.**
   - 100H hubs span ≈183 mm; Halo frames (150 mm stock) need +33 mm plus new shock brackets (~€200–300 to fabricate).【F:knowledge/notes/input_part011_review.md†L415-L417】
   - 80H motors require 155 mm fork openings and longer swingarm bolts so calipers clear the wider stator stack; expect to machine fresh studs and spacers.【F:knowledge/notes/input_part011_review.md†L482-L483】【F:knowledge/notes/input_part011_review.md†L531-L536】【F:knowledge/notes/input_part011_review.md†L628-L628】
2. **Preempt waterproofing.** Lonnyo 70H hubs ship unsealed with budget bearings—plan a full tear-down, bearing swap, and housing seal before installation. Plasti Dip offers reversible protection for motor leads and controller cavities if you avoid permanent potting.【F:knowledge/notes/input_part011_review.md†L463-L465】
3. **Controller mounting.** 100H swaps often coincide with dual-controller layouts; leave space for 3Shul/Tronic heat spreaders and consider external radiators or aluminum decks before you close the frame.【F:knowledge/notes/input_part011_review.md†L365-L417】
4. **Brake clearance.** Yamal’s 80H retrofit stalled until longer hardware arrived—the caliper physically cannot mount on stock-length swingarm bolts. Test-fit the rotor and caliper with the wheel torqued before final wiring.【F:knowledge/notes/input_part011_review.md†L531-L536】【F:knowledge/notes/input_part011_review.md†L736-L736】

## Commissioning & Maintenance Playbook
- **Bearing & seal upgrade (70H).** Replace both bearings, pack fresh grease, and add gaskets or sealant before first ride. Document torque values during reassembly to avoid preloading the new races.【F:knowledge/notes/input_part011_review.md†L463-L465】
- **Sensor verification (80H/100H).** Lonnyo 80H shipments include hall and temperature sensors; validate continuity before lacing into rims to avoid relacing later. Longer bolt kits also keep harnesses from pinching against brake mounts.【F:knowledge/notes/input_part011_review.md†L482-L483】【F:knowledge/notes/input_part011_review.md†L531-L536】
- **Thermal logging.** Single-controller builds should log CAN data for commanded vs. delivered amps—many “weak” Lonnyo setups trace back to firmware ceilings, not motor limits. Pair phase-current logs with tire temperature checks after field-weakening pulls.【F:knowledge/notes/input_part011_review.md†L340-L353】

## Build Budgeting & Upgrade Roadmap
- **Step-up strategy:** Riders frequently liquidate 22×3 sets to fund 80H or 100H upgrades once they outgrow traction-limited builds. Budget for new suspension components, custom machining, and controller upgrades—not just the hubs themselves.【F:knowledge/notes/input_part011_review.md†L288-L289】【F:knowledge/notes/input_part011_review.md†L365-L417】
- **Import math:** Between €736 80H kits and €315 65H hubs, shipping and customs can rival motor cost. Factor duties into ROI calculations and request detailed invoices to avoid seizure or reassessment at the border.【F:knowledge/notes/input_part011_review.md†L292-L293】【F:knowledge/notes/input_part011_review.md†L482-L483】

## Emerging Field Notes & Troubleshooting
- **Validate sensor harnesses before tuning.** A mispinned third-party loom left a Lonnyo 11" hub reporting 59 °C at ambient; repinning to Lonnyo’s wire order, confirming ≈10 kΩ-to-ground at 25 °C, and updating to current 6.xx firmware restored accurate telemetry.【F:data/vesc_help_group/text_slices/input_part014.txt†L7858-L7889】
- **Plan for shrinking retail channels.** US buyers report Lonnyo listings disappearing from AliExpress, prompting bulk purchases or alternate distributors to avoid long lead times on replacements.【F:knowledge/notes/input_part008_review.md†L563-L576】
- **Leverage high-temp cabling on rewinds.** Builders rewinding 65H 33×2 hubs are trialing thin glass-fiber 6 mm² leads (rated ≈800 °C) to squeeze larger conductors through the axle while warning the labor, not the wire, is the true bottleneck.【F:knowledge/notes/input_part009_review.md†L152-L155】
- **Map rebrand families when sourcing.** Longyu manufactures many 65H/70H cores sold as Lonnyo, Vsett, Huameng, or Kaabo; factor that overlap into spec sheets and verify axle hardware before assuming a “new” model differs materially.【F:knowledge/notes/input_part009_review.md†L294-L299】
- **Specify magnet length on custom orders.** When requesting bespoke winds from Ambrosini/Lonnyo, include the desired magnet stack (e.g., 70 mm on 22×3) and stator size, and temper expectations above ~300 A on 70H cans without corresponding controller and cooling upgrades.【F:data/vesc_help_group/text_slices/input_part014.txt†L4533-L4540】

## Source Notes
[^1]: Lonnyo wind shorthand, pricing, and traction-limited current goals for 22×3 vs. 33×2 builds.【F:knowledge/notes/input_part011_review.md†L288-L293】【F:knowledge/notes/input_part011_review.md†L328-L329】
[^2]: Community current envelopes for 22×3 hubs on Spintend hardware plus firmware caps on single Ubox 85150 setups.【F:knowledge/notes/input_part011_review.md†L309-L311】【F:knowledge/notes/input_part011_review.md†L340-L353】
[^3]: Dropout widths, swingarm hardware, and sealing requirements for 70H/80H/100H Lonnyo conversions.【F:knowledge/notes/input_part011_review.md†L365-L417】【F:knowledge/notes/input_part011_review.md†L463-L465】【F:knowledge/notes/input_part011_review.md†L482-L536】【F:knowledge/notes/input_part011_review.md†L628-L736】
[^4]: Controller pairing plans and budget ranges when escalating to 100H stators with 30 S packs and 400 A-class stages.【F:knowledge/notes/input_part011_review.md†L365-L417】
[^5]: Customs risk and landed cost expectations for 65H and 80H Lonnyo orders.【F:knowledge/notes/input_part011_review.md†L292-L293】【F:knowledge/notes/input_part011_review.md†L482-L483】
[^6]: Sensor harness diagnostics, supply-chain shifts, cabling experiments, Longyu rebrand overlaps, and custom magnet guidance noted in recent transcript reviews.【F:data/vesc_help_group/text_slices/input_part014.txt†L7858-L7889】【F:knowledge/notes/input_part008_review.md†L563-L576】【F:knowledge/notes/input_part009_review.md†L152-L155】【F:knowledge/notes/input_part009_review.md†L294-L299】【F:data/vesc_help_group/text_slices/input_part014.txt†L4533-L4540】
