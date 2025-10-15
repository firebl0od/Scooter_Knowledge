# Lonnyo Hub Motor Dossier

## TL;DR
- Lonnyo’s stator codes map cleanly to use cases: 17×4 torque, 22×3 “standard”, and 33×2 high-speed winds, with riders stepping up to 80H/100H cores when chasing 150 km/h builds or >300 A phase targets.【F:knowledge/notes/input_part011_review.md†L288-L293】【F:knowledge/notes/input_part011_review.md†L328-L329】
- Real-world current envelopes show 22×3 hubs settling near 110–150 A battery and ~300 A phase on Spintend 75/200-class controllers, while single Ubox 85150 installs bump into a ~150 A firmware ceiling regardless of higher software limits.【F:knowledge/notes/input_part011_review.md†L309-L311】【F:knowledge/notes/input_part011_review.md†L340-L353】
- Packaging is the gating factor above 70H: the 100H cans require ≈183 mm dropouts plus custom shock brackets, 80H swaps need 155 mm fork spacing and longer caliper studs, and even 70H hubs ship unsealed—expect a full bearing and weatherproofing job before first ride.【F:knowledge/notes/input_part011_review.md†L365-L417】【F:knowledge/notes/input_part011_review.md†L482-L483】【F:knowledge/notes/input_part011_review.md†L531-L536】【F:knowledge/notes/input_part011_review.md†L463-L465】
- 80H 22×3 winds measure roughly 34.8 kV—good for ~141 km/h free spin at 80 V—but meaningful acceleration still demands dual motors or lighter rims once you move beyond 11" commuter tires.[^80h_kv]

## Motor Lineup & Sourcing Signals
| Wind | Typical Stator | Community Use Case | Notes |
| --- | --- | --- | --- |
| 17×4 | 40H torque cores | Launch torque for hill-heavy or cargo builds | Keeps amperage modest but caps top speed; often paired with thicker packs instead of field weakening.【F:knowledge/notes/input_part011_review.md†L328-L329】【F:knowledge/notes/input_part011_review.md†L431-L434】 |
| 22×3 | 40H/65H standard | Balanced street setups targeting 120–150 km/h with traction control | Riders log 200 A-per-motor goals but admit traction is the bottleneck without TC or race tires.【F:knowledge/notes/input_part011_review.md†L288-L289】 |
| 33×2 | 80H/100H speed | Highway-speed touring and race builds | Requires flawless tuning and long, straight courses to exploit; many owners resell 22×3 sets to fund the jump.【F:knowledge/notes/input_part011_review.md†L288-L289】 |
| 70H | 22×3 torque refresh | Waterproofed commuter upgrade | Ships dry—budget bearings, seals, and coatings up front.【F:knowledge/notes/input_part011_review.md†L463-L465】 |
| 80H | 33×2 performance | Step between 22×3 and 100H | Arrive with halls/NTCs, cost ≈€736 without rims, and need 155 mm dropouts plus longer pivot hardware.【F:knowledge/notes/input_part011_review.md†L482-L483】【F:knowledge/notes/input_part011_review.md†L531-L536】【F:knowledge/notes/input_part011_review.md†L628-L628】 |
| 100H | 33×2 race | Extreme builds chasing 600 A phase stacks | Measure ~183 mm across the axle and force bespoke suspension mounts before pairing with 3Shul 400 A or dual Tronic stacks.【F:knowledge/notes/input_part011_review.md†L365-L417】 |

**Procurement watchpoints.** Genuine 65H 22×3 hubs hover near $205 (~€315 landed), but veterans warn that many “90H” listings hide cheaper 80–85H stators and customs fees can erase gray-market savings. Keep receipts, request stator photos, and budget for duties when importing to stricter regions.【F:knowledge/notes/input_part011_review.md†L292-L293】 Remember that Longyu manufactures the same cores for Vsett, Huameng, Kaabo, and Lonnyo-badged scooters—plenty of “factory” AliExpress shops are simply resellers—so verify axle widths and wind codes before wiring funds.[^6]
**Map Lonnyo vs. NAMI engravings.** Builders comparing hubs note shared factory stamps, thicker Lonnyo phase leads, and a preference for 70 H magnet stacks because they just squeeze into 150 mm dropouts once frames (e.g., Laotie TI30) receive gussets or reinforcement welds.[^nami_overlap]

## Electrical Envelopes & Controller Pairings
- **Spintend 75/200 & 75/240 (dual):** Treat 22×3 Lonnyos as ~150 A battery / 300 A phase hardware. Race setups trim battery current toward 110 A to keep thermal headroom for field weakening or regen bursts.【F:knowledge/notes/input_part011_review.md†L309-L311】
- **Single Ubox 85150 installs:** Multiple riders hit a hard ~150 A phase ceiling even with 210–280 A software targets; Statorade plus ≤20 % saturation compensation keeps temps manageable but doesn’t lift the cap. Suspect firmware or BMS enforcement before chasing hardware mods.【F:knowledge/notes/input_part011_review.md†L340-L353】
- **Dual-drive traction planning:** Without traction control, dual 22×3 builds spin tires around 200 A per motor; expect to log duty-cycle and slip data before pushing beyond that envelope. Pair fast-wind 33×2 motors with high-voltage packs (≥22 S) and stable suspension to actually translate current into road speed.【F:knowledge/notes/input_part011_review.md†L288-L289】
- **Controller synergy for 100H projects:** Pandalgns budgets 3Shul 400 A stages and 30 S packs once the chassis accepts the 100H cans, underscoring the need for Seven-class controllers or Tronic X12 pairs when stator surface area finally stops being the bottleneck.【F:knowledge/notes/input_part011_review.md†L365-L417】

## Chassis Fitment & Fabrication Checklist
1. **Measure dropouts before ordering.**
   - 100H hubs span ≈183 mm; Halo frames (150 mm stock) need +33 mm plus new shock brackets (~€200–300 to fabricate).【F:knowledge/notes/input_part011_review.md†L415-L417】
   - 80H motors require 155 mm fork openings and longer swingarm bolts so calipers clear the wider stator stack; expect to machine fresh studs and spacers.【F:knowledge/notes/input_part011_review.md†L482-L483】【F:knowledge/notes/input_part011_review.md†L531-L536】【F:knowledge/notes/input_part011_review.md†L628-L628】
   - Dualtron Achilleus riders already twisted 90 H axles by forcing them into stock arms; plan Victor arms or torque plates and expect 176 mm openings with custom washer stacks before hammering high-torque launches.[^achilleus_axle]
2. **Preempt waterproofing.** Lonnyo 70H hubs ship unsealed with budget bearings—plan a full tear-down, bearing swap, and housing seal before installation. Plasti Dip offers reversible protection for motor leads and controller cavities if you avoid permanent potting.【F:knowledge/notes/input_part011_review.md†L463-L465】
3. **Controller mounting.** 100H swaps often coincide with dual-controller layouts; leave space for 3Shul/Tronic heat spreaders and consider external radiators or aluminum decks before you close the frame.【F:knowledge/notes/input_part011_review.md†L365-L417】
4. **Brake clearance.** Yamal’s 80H retrofit stalled until longer hardware arrived—the caliper physically cannot mount on stock-length swingarm bolts. Test-fit the rotor and caliper with the wheel torqued before final wiring.【F:knowledge/notes/input_part011_review.md†L531-L536】【F:knowledge/notes/input_part011_review.md†L736-L736】
5. **Harness routing on new batches.** Recent Lonnyo 70H/75H shipments reroute phase leads through the side cover instead of the axle, leaving room for 6 mm²+ upgrades once you heat the silicone jackets and widen tight dropouts.[^side_exit]

## Commissioning & Maintenance Playbook
- **Bearing & seal upgrade (70H).** Replace both bearings, pack fresh grease, and add gaskets or sealant before first ride. Document torque values during reassembly to avoid preloading the new races.【F:knowledge/notes/input_part011_review.md†L463-L465】
- **Confirm bearing part numbers.** Lonnyo 70 H hubs run 6003 rotor-side and 6008 stator-side bearings, making spares easy to source before you tear down imports.【F:knowledge/notes/input_part006_review.md†L114-L114】
- **Sensor verification (80H/100H).** Lonnyo 80H shipments include hall and temperature sensors; validate continuity before lacing into rims to avoid relacing later. Longer bolt kits also keep harnesses from pinching against brake mounts.【F:knowledge/notes/input_part011_review.md†L482-L483】【F:knowledge/notes/input_part011_review.md†L531-L536】
- **Thermal logging.** Single-controller builds should log CAN data for commanded vs. delivered amps—many “weak” Lonnyo setups trace back to firmware ceilings, not motor limits. Pair phase-current logs with tire temperature checks after field-weakening pulls.【F:knowledge/notes/input_part011_review.md†L340-L353】

## Build Budgeting & Upgrade Roadmap
- **Step-up strategy:** Riders frequently liquidate 22×3 sets to fund 80H or 100H upgrades once they outgrow traction-limited builds. Budget for new suspension components, custom machining, and controller upgrades—not just the hubs themselves.【F:knowledge/notes/input_part011_review.md†L288-L289】【F:knowledge/notes/input_part011_review.md†L365-L417】
- **Import math:** Between €736 80H kits and €315 65H hubs, shipping and customs can rival motor cost. Factor duties into ROI calculations and request detailed invoices to avoid seizure or reassessment at the border.【F:knowledge/notes/input_part011_review.md†L292-L293】【F:knowledge/notes/input_part011_review.md†L482-L483】

## Emerging Field Notes & Troubleshooting
- **Validate sensor harnesses before tuning.** A mispinned third-party loom left a Lonnyo 11" hub reporting 59 °C at ambient; repinning to Lonnyo’s wire order, confirming ≈10 kΩ-to-ground at 25 °C, and updating to current 6.xx firmware restored accurate telemetry.【F:knowledge/notes/input_part014_review.md†L128-L128】
- **Plan for shrinking retail channels.** US buyers report Lonnyo listings disappearing from AliExpress, prompting bulk purchases or alternate distributors to avoid long lead times on replacements.【F:knowledge/notes/input_part008_review.md†L563-L576】
- **Choose tubeless cores deliberately.** Split Lonnyo rims can’t convert to tubeless after purchase—builders pay more up front for tubeless-ready batches to survive racing heat, while tube versions stay viable for budget commuters who accept more maintenance.[^tubeless_choice]
- **Leverage high-temp cabling on rewinds.** Builders rewinding 65H 33×2 hubs are trialing thin glass-fiber 6 mm² leads (rated ≈800 °C) to squeeze larger conductors through the axle while warning the labor, not the wire, is the true bottleneck.【F:knowledge/notes/input_part009_review.md†L152-L155】
- **Map rebrand families when sourcing.** Longyu manufactures many 65H/70H cores sold as Lonnyo, Vsett, Huameng, or Kaabo; factor that overlap into spec sheets and verify axle hardware before assuming a “new” model differs materially.【F:knowledge/notes/input_part009_review.md†L294-L299】
- **Specify magnet length on custom orders.** When requesting bespoke winds from Ambrosini/Lonnyo, include the desired magnet stack (e.g., 70 mm on 22×3) and stator size, and temper expectations above ~300 A on 70H cans without corresponding controller and cooling upgrades.【F:knowledge/notes/input_part014_review.md†L69-L69】
- **Confirm lead gauge before pushing current.** Recent Dualtron Achilleus tear-downs measured Lonnyo phase leads near 7 AWG with ~8 mm sleeving, supporting high-current goals but reinforcing the need to inspect for shipping damage before final assembly.【F:knowledge/notes/input_part012_review.md†L472-L473】
- **Track traction-control headroom.** Max Rainlogix’s Thunder (dual Lonnyo 70/110 hubs, Ubox 85/240) hauled two riders uphill at 320 A battery without overheating by capping phase to 150/200 A rear and 120/140 A front and leaving TC enabled—earlier 200/300 A tests proved viable but wheelie-prone.[^thunder_tc]
- **Log insulation upgrades.** Latest 65H 16×4 hubs ship potted for ≈180 °C operation, making them attractive commuter swaps so long as torque arms and wider swingarms handle the added stator mass.[^180c_insulation]

## Lonnyo Axle Spacing & Offset Cautions (Batch 13 Additions)
- Lonnyo spacer and offset specifications are critical for proper fitment—incorrect spacing has caused axle binding, premature bearing failure, and frame alignment issues on Dualtron and custom chassis builds.[^spacing-critical]
- **Spacer/offset guidance:**
  - 90H Lonnyo hubs demand torque-arm and deck-clearance planning before installation on Dualtron frames
  - Arm choices, spacer stacks, and dropout prep must be verified before riders twist axles under load
  - 145 mm dropout requirement for 11" hubs means many frames need machining or replacement swingarms[^dropout-req]
- Document proper spacer stack configurations for common chassis (Dualtron, Nami, custom builds) to prevent field failures from improper fitment.[^spacing-guide]

## Source Notes
[^1]: Lonnyo wind shorthand, pricing, and traction-limited current goals for 22×3 vs. 33×2 builds.【F:knowledge/notes/input_part011_review.md†L288-L293】【F:knowledge/notes/input_part011_review.md†L328-L329】
[^2]: Community current envelopes for 22×3 hubs on Spintend hardware plus firmware caps on single Ubox 85150 setups.【F:knowledge/notes/input_part011_review.md†L309-L311】【F:knowledge/notes/input_part011_review.md†L340-L353】
[^3]: Dropout widths, swingarm hardware, and sealing requirements for 70H/80H/100H Lonnyo conversions.【F:knowledge/notes/input_part011_review.md†L365-L417】【F:knowledge/notes/input_part011_review.md†L463-L465】【F:knowledge/notes/input_part011_review.md†L482-L536】【F:knowledge/notes/input_part011_review.md†L628-L736】
[^4]: Controller pairing plans and budget ranges when escalating to 100H stators with 30 S packs and 400 A-class stages.【F:knowledge/notes/input_part011_review.md†L365-L417】
[^5]: Customs risk and landed cost expectations for 65H and 80H Lonnyo orders.【F:knowledge/notes/input_part011_review.md†L292-L293】【F:knowledge/notes/input_part011_review.md†L482-L483】
[^6]: Sensor harness diagnostics, supply-chain shifts, cabling experiments, and Longyu’s OEM role underpinning rebranded 65H hubs alongside custom magnet guidance from recent transcripts.【F:knowledge/notes/input_part014_review.md†L69-L128】【F:knowledge/notes/input_part008_review.md†L563-L569】【F:knowledge/notes/input_part009_review.md†L152-L155】【F:knowledge/notes/input_part009_review.md†L294-L299】
[^nami_overlap]: Lonnyo and NAMI hubs share factory engravings; Laotie TI30 builders reinforce frames and pick 70 H magnet stacks to keep 150 mm dropouts intact while gaining thicker phase leads.【F:knowledge/notes/input_part005_review.md†L422-L422】【F:knowledge/notes/input_part005_review.md†L575-L575】
[^80h_kv]: Lonnyo 80 H 22×3 stators logging ~34.8 kV free spin at 80 V and the reminder that 11" builds still need dual motors or lighter rims to accelerate well at that voltage.【F:knowledge/notes/input_part012_review.md†L234-L236】
[^achilleus_axle]: Dualtron Achilleus crews twisting Lonnyo 90 H axles until switching to Victor arms or custom torque hardware and widening clearances to ~176 mm with washer stacks.【F:knowledge/notes/input_part013_review.md†L421-L421】
[^tubeless_choice]: Community debates over tubed versus tubeless Lonnyo rims—split motors cannot be converted later, so racers pay for tubeless batches while commuters accept tubes and the maintenance trade-off.【F:knowledge/notes/input_part013_review.md†L310-L310】
[^side_exit]: New-gen Lonnyo 70H/75H hubs route phases through the side cover, freeing room for larger sleeved leads once the silicone jackets are warmed and dropouts are relieved.【F:knowledge/notes/input_part007_review.md†L306-L306】
[^thunder_tc]: Max Rainlogix’s dual-Lonnyo Thunder log covering 320 A battery climbs with traction control and staged phase limits plus earlier 200/300 A experiments that proved wheelie-prone.【F:knowledge/notes/input_part012_review.md†L362-L363】
[^180c_insulation]: Latest Lonnyo 65H 16×4 hubs shipping with 180 °C potting for commuter builds, highlighting the insulation upgrade over earlier 120 °C stators.【F:knowledge/notes/input_part010_review.md†L87-L87】
[^spacing-critical]: Lonnyo spacer and offset specifications being critical for proper fitment to avoid axle binding and bearing failures.【F:knowledge/notes/input_part013_review.md†L267-L267】
[^dropout-req]: 145 mm dropout requirement for 11" Lonnyo hubs and Paolo's spacing guidance.【F:knowledge/notes/input_part009_review.md†L355-L355】
[^spacing-guide]: Follow-up action to document Lonnyo axle-spacing guide for common chassis builds.【F:knowledge/notes/input_part013_review.md†L278-L278】
