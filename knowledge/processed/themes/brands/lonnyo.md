# Lonnyo Hub Motor Dossier

## TL;DR

- Lonnyo’s stator codes map cleanly to use cases: 17×4 torque, 22×3 “standard”, and 33×2 high-speed winds, with riders stepping up to 80H/100H cores when chasing 150 km/h builds or >300 A phase targets.[^1][^2]
- Real-world current envelopes show 22×3 hubs settling near 110–150 A battery and ~300 A phase on Spintend 75/200-class controllers, while single Ubox 85150 installs bump into a ~150 A firmware ceiling regardless of higher software limits.[^3][^4]
- Packaging is the gating factor above 70H: the 100H cans require ≈183 mm dropouts plus custom shock brackets, 80H swaps need 155 mm fork spacing and longer caliper studs, and even 70H hubs ship unsealed—expect a full bearing and weatherproofing job before first ride.[^5][^6][^7][^8]
- Traction, not thermal headroom, still limits many builds—70 H motors hold roughly 12 kW without overheating, yet even 350 A battery pushes spin the front tire first on 33×2 windings.[^9]
- 80H 22×3 winds measure roughly 34.8 kV—good for ~141 km/h free spin at 80 V—but meaningful acceleration still demands dual motors or lighter rims once you move beyond 11" commuter tires.[^80h_kv]
- Lonnyo remains the go-to 11" 84 V upgrade for stronger launches; riders are pairing the hubs with Hope Tech V4 brake bundles around €457 delivered to keep stopping power in step.[^10]
- New-gen 70H/75H hubs share axles with the 60H family, squeeze into G30 forks with minimal shimming, and route phases through the side cover—plus the 70H split rims now ship tubeless-ready while axle-exit variants remain tube-only.[^11]

## Motor Lineup & Sourcing Signals

| Wind | Typical Stator | Community Use Case | Notes |
| --- | --- | --- | --- |
| 17×4 | 40H torque cores | Launch torque for hill-heavy or cargo builds | Keeps amperage modest but caps top speed; often paired with thicker packs instead of field weakening.[^2][^12] |
| 22×3 | 40H/65H standard | Balanced street setups targeting 120–150 km/h with traction control | Riders log 200 A-per-motor goals but admit traction is the bottleneck without TC or race tires.[^13] |
| 33×2 | 80H/100H speed | Highway-speed touring and race builds | Requires flawless tuning and long, straight courses to exploit; many owners resell 22×3 sets to fund the jump.[^13] |
| 65H 22×3 | Torque refresh | Single-motor commuters chasing harder launches | Rosheee’s dyno pulls showed a lone 65 H hub on a 16 S 6 P pack beating dual 50 H motors 0–30 km/h, albeit with lower top speed and faster energy drain.[^14][^15] |
| 70H | 22×3 torque refresh | Waterproofed commuter upgrade | Ships dry—budget bearings, seals, and coatings up front.[^8] |
| 80H | 33×2 performance | Step between 22×3 and 100H | Arrive with halls/NTCs, cost ≈€736 without rims, and need 155 mm dropouts plus longer pivot hardware.[^6][^7][^16] |
| 100H | 33×2 race | Extreme builds chasing 600 A phase stacks | Measure ~183 mm across the axle and force bespoke suspension mounts before pairing with 3Shul 400 A or dual Tronic stacks.[^5] |

- **Procurement watchpoints.** Genuine 65H 22×3 hubs hover near $205 (~€315 landed), but veterans warn that many “90H” listings hide cheaper 80–85H stators and customs fees can erase gray-market savings. Israeli buyers have even seen bargain orders confiscated outright, turning “too good to be true” deals into total losses. Keep receipts, request stator photos, and budget for duties when importing to stricter regions.[^17][^18] Mixing magnet stacks is viable when the wind count matches—Noname okayed pairing an 80 H rear with a 70 H front so long as both share the same turns—and even the older tubed-rim 70 H motors use the current split-rim stator, making discounted “non-removable” wheels attractive if you are prepared for manual tire changes.[^19] Remember that Longyu manufactures the same cores for Vsett, Huameng, Kaabo, and Lonnyo-badged scooters—plenty of “factory” AliExpress shops are simply resellers—so verify axle widths and wind codes before wiring funds.[^6]
- **Price signals.** Recent Tao listings floated new 80 H hubs around US$200 while direct-from-Lonnyo orders sat near US$317 before shipping, and bare 75 H stators without rims dipped to about US$245 on Alibaba—factor rim sourcing and freight before assuming stripped stators save money.[^20]
- Noname surfaced an LY/Lonnyo 11" catalog spanning 60–120 V / up to 6 kW, and Patrick’s swap logs show stock Vsett motors overheating where Lonnyo 16×4 hubs stay cool on climbs (albeit with lower top speed until he experiments with 22×3 tires or delta wiring).[^21]
- Recent 65H 16×4 purchases landed at US$399 shipped with 180 °C potting and 12 AWG, 200 °C phase leads, underscoring both the price creep and the importance of upgrading chassis wiring to match the hotter-rated stators.[^22]
- **7" LY 90 H torque case study.** Dualtron Achilleus owners twisted Lonnyo 90 H axles because the shafts are narrower than Thunder arms; plan Victor arms or torque hardware and verify the 176 mm opening before hammering 7" rubber at race currents.[^23][^24]
- Field chat confirms Vsett OEM hubs ship with 40 H stators, reinforcing that salvaged Vsett motors mirror Lonnyo 22×3 cores and share the same thermal headroom when reused in custom frames.[^25]
**Map Lonnyo vs. NAMI engravings.** Builders comparing hubs note shared factory stamps, thicker Lonnyo phase leads, and a preference for 70 H magnet stacks because they just squeeze into 150 mm dropouts once frames (e.g., Laotie TI30) receive gussets or reinforcement welds.[^nami_overlap]

## Electrical Envelopes & Controller Pairings

- **Spintend 75/200 & 75/240 (dual):** Treat 22×3 Lonnyos as ~150 A battery / 300 A phase hardware. Race setups trim battery current toward 110 A to keep thermal headroom for field weakening or regen bursts.[^3]
- **Field-weakening experiments stay measured.** Shlomozero’s 20 S 9 P Lishen build spins 22×3 hubs toward 200 km/h with ~200 A battery, 200 A phase, and 60–80 A of field weakening—proof that aggressive FW requires serious cooling and regen planning on 75200-class controllers.[^26]
- **70H/Laotie pairings:** Even the refreshed 70 H Lonnyo and Laotie hubs still prefer 12‑FET Spintend 85/200 controllers; 80100 hardware saturates near 150 A phase and leaves speed-wind 33×2 stators underfed.[^27]
- **Single Ubox 85150 installs:** Multiple riders hit a hard ~150 A phase ceiling even with 210–280 A software targets; Statorade plus ≤20 % saturation compensation keeps temps manageable but doesn’t lift the cap. Suspect firmware or BMS enforcement before chasing hardware mods.[^4]
- **Dual-drive traction planning:** Without traction control, dual 22×3 builds spin tires around 200 A per motor; expect to log duty-cycle and slip data before pushing beyond that envelope. Pair fast-wind 33×2 motors with high-voltage packs (≥22 S) and stable suspension to actually translate current into road speed.[^13]
- **Single 65 H tuning heuristics:** Matthew’s 22×3 Lonnyo on 18 S surged past 35 mph then “fluttered” until he deleted throttle smoothing, graphed logs, and trialled Ortega’s FOC observer; the crew pinned his 90 A BMS as the torque bottleneck and only plans to raise battery/phase toward ~150 A once hardware upgrades land, reiterating that 22×3 winds sacrifice launch torque versus 16×4 hubs and need premium halls plus Statorade to survive extra amps.[^28][^29][^30]
- **High-speed 33×2 demands:** Yamal reminded the crew that 65 H 33/2 hubs need ≥12‑FET controllers, dedicated harnesses, and thicker 8 mm² cabling warmed with a heat gun before bending so the upgraded leads seat cleanly inside widened dropouts.[^31][^32][^33]
- **Controller synergy for 100H projects:** Pandalgns budgets 3Shul 400 A stages and 30 S packs once the chassis accepts the 100H cans, underscoring the need for Seven-class controllers or Tronic X12 pairs when stator surface area finally stops being the bottleneck.[^5]
- **Road-speed benchmarks:** Rob Ver’s 80H 22×3 build (132 km/h logged on 22 × 3 tires, dual controllers, and 22 S packs) shows the platform’s ceiling when aero, pack voltage, and cooling align.[^robver132]

## Chassis Fitment & Fabrication Checklist

1. **Measure dropouts before ordering.**
   - 100H hubs span ≈183 mm; Halo frames (150 mm stock) need +33 mm plus new shock brackets (~€200–300 to fabricate).[^34]
   - 80H motors require 155 mm fork openings and longer swingarm bolts so calipers clear the wider stator stack; expect to machine fresh studs and spacers.[^6][^7][^16]
   - LY 11″ rims accept 155 mm axles, easing wider slick conversions on legacy chassis once spacers are machined.[^35]
   - Even GT1 front ends need modification—Smart Repair’s dual-drive build is widening the suspension to swallow a 70H hub up front.[^36]
   - Halo swingarms are already being opened to ~200 mm for 80 H conversions, while stock forks hover around 170–175 mm and 155 mm special orders cover 60 H commuters—measure before ordering rims or custom spacers.[^37]
   - Dualtron Achilleus riders already twisted 90 H axles by forcing them into stock arms; plan Victor arms or torque plates and expect 176 mm openings with custom washer stacks before hammering high-torque launches.[^achilleus_axle]
   - Thunder decks buy a little breathing room—the stock arms measure roughly 4 mm wider than the Achilleus, so 22 S11 P boxes and large parallels fit easier even though the Achilleus still needs machining to house equivalent packs.[^24]
   - Face de Pin and others measured Lonnyo/Ly axles varying by up to 5 mm between batches—mock up washer stacks on both sides and re-check rotor centering before locking in spacer lengths.[^38]
2. **Preempt waterproofing.** Lonnyo 70H hubs ship unsealed with budget bearings—plan a full tear-down, bearing swap, and housing seal before installation. Plasti Dip offers reversible protection for motor leads and controller cavities if you avoid permanent potting.[^8]
3. **Source tubeless O-rings from bearing suppliers.** Tubeless split rims rely on model-specific seals seated in machined rails; keep spares because generic O-rings rarely fit.[^39][^40]
4. **Controller mounting.** 100H swaps often coincide with dual-controller layouts; leave space for 3Shul/Tronic heat spreaders and consider external radiators or aluminum decks before you close the frame.[^5]
5. **Brake clearance.** Yamal’s 80H retrofit stalled until longer hardware arrived—the caliper physically cannot mount on stock-length swingarm bolts. Test-fit the rotor and caliper with the wheel torqued before final wiring.[^7][^41]
6. **Harness routing on new batches.** Recent Lonnyo 70H/75H shipments reroute phase leads through the side cover instead of the axle, leaving room for 6 mm²+ upgrades once you heat the silicone jackets and widen tight dropouts.[^side_exit]

## Commissioning & Maintenance Playbook

- **Bearing & seal upgrade (70H).** Replace both bearings, pack fresh grease, and add gaskets or sealant before first ride. Document torque values during reassembly to avoid preloading the new races.[^8]
- **Confirm bearing part numbers.** Lonnyo 70 H hubs run 6003 rotor-side and 6008 stator-side bearings, making spares easy to source before you tear down imports.[^42]
- **Sensor verification (80H/100H).** Lonnyo 80H shipments include hall and temperature sensors; validate continuity before lacing into rims to avoid relacing later. Longer bolt kits also keep harnesses from pinching against brake mounts.[^6][^7]
- **Stick with 10 kΩ motor probes.** Jason confirmed Lonnyo 75 H hubs ship with 10 kΩ NTCs that align with Ubox thermistor scaling—100 kΩ sensors technically read but lose accuracy at low temperatures, so spec 10 k replacements.[^43]
- **Thermal logging.** Single-controller builds should log CAN data for commanded vs. delivered amps—many “weak” Lonnyo setups trace back to firmware ceilings, not motor limits. Pair phase-current logs with tire temperature checks after field-weakening pulls.[^4]

## Build Budgeting & Upgrade Roadmap

- **Step-up strategy:** Riders frequently liquidate 22×3 sets to fund 80H or 100H upgrades once they outgrow traction-limited builds. Budget for new suspension components, custom machining, and controller upgrades—not just the hubs themselves.[^13][^5]
- **Import math:** Between €736 80H kits and €315 65H hubs, shipping and customs can rival motor cost. Factor duties into ROI calculations and request detailed invoices to avoid seizure or reassessment at the border.[^17][^6]

## Emerging Field Notes & Troubleshooting

- **Validate sensor harnesses before tuning.** A mispinned third-party loom left a Lonnyo 11" hub reporting 59 °C at ambient; repinning to Lonnyo’s wire order, confirming ≈10 kΩ-to-ground at 25 °C, and updating to current 6.xx firmware restored accurate telemetry.[^44]
- **Log thermal behaviour on 22×3 commuters.** Matthew’s rear Lonnyo with Statorade held long runs near 85 °C and highlighted that prior Ubox cutouts were controller-side faults, not the motor—evidence that healthy hubs stay cool when paired with reliable ESCs.[^45]
- **Confirm current ceilings with live logs.** A Dualtron Achilleus running Lonnyo 75H 22×3 hubs and 16 S 7 P pack only delivered ~135 A despite 220 A targets; the crew recommended rerunning mxlemming detection, graphing battery voltage/current, and watching for regen spikes at top speed to decide whether saturation or configuration is the limiting factor.[^46]
- **Plan for shrinking retail channels.** US buyers report Lonnyo listings disappearing from AliExpress, prompting bulk purchases or alternate distributors to avoid long lead times on replacements.[^47]
- **Yume Y11+ can swallow 80H 33/2 rears.** Matthew’s conversion notes show the frame handles higher-output Lonnyo hubs if you budget thermal headroom and current for the wider stator.[^48]
- **Skip 70H stopgaps when chasing torque.** Smart Repair keeps a spare 70H hub on the shelf but advises jumping straight to an 80H fed by multiple ESCs when you want serious rear-wheel thrust.[^49]
- **Custom rotor manufacturing needs tight tolerances.** Patrick’s three-piece LY rotor concept keeps a 0.5 mm airgap and drops hall sensors to fit 75–80 H stators, yet machinists warned the cooling fins demand multi-axis work, tiny tooling, and extra setups that erase cost savings.[^50]
- **Add locating features before going CNC.** Veterans recommend machining concentric locating beads or grooves in custom endcaps so both sides align without relying on screws—a must before committing to production batches.[^51]
- **Validate magnetic circuits, not just magnet thickness.** Riders cautioned that thicker magnets and tighter airgaps can still underperform proven 110/65 designs if the magnetic path is poor; benchmark against known-good motors before investing hundreds in bespoke rotors.[^52][^53]
- **Budget CNC rims and thick harnesses.** Ambrosini/LY CNC rims still land near €100–€120, expect 155 mm axles for 6.5″ setups, and arrive with AWG 7–8 sleeved phase leads.[^54]
- **Confirm stator widths on new batches.** Scrtt’s hunt for 75 H hubs confirmed multiple widths exist, reinforcing the need to verify axle spacing and stator thickness before wiring funds to boutique vendors.[^55]
- **Mock up washer stacks on every delivery.** Shlomozero’s 75 H test fit only needed a thin washer on the wire side, but Face de Pin Sucé has measured more than 5 mm of axle-length variance between Lonnyo batches—check each hub before committing to spacers or torque-arm machining.[^56]
- **Choose tubeless cores deliberately.** Split Lonnyo rims can’t convert to tubeless after purchase—builders pay more up front for tubeless-ready batches to survive racing heat, while tube versions stay viable for budget commuters who accept more maintenance.[^57]
- **Leverage drop-in G30 swaps.** 60H hubs remain a bolt-on upgrade for G30 frames (mount from the inside and shim with steel if needed), whereas M365 decks lack clearance and 65H fits only at the rear.[^58]
- **Leverage high-temp cabling on rewinds.** Builders rewinding 65H 33×2 hubs are trialing thin glass-fiber 6 mm² leads (rated ≈800 °C) to squeeze larger conductors through the axle while warning the labor, not the wire, is the true bottleneck.[^59]
- **Map rebrand families when sourcing.** Longyu manufactures many 65H/70H cores sold as Lonnyo, Vsett, Huameng, or Kaabo; factor that overlap into spec sheets and verify axle hardware before assuming a “new” model differs materially.[^60]
- **Specify magnet length on custom orders.** When requesting bespoke winds from Ambrosini/Lonnyo, include the desired magnet stack (e.g., 70 mm on 22×3) and stator size, and temper expectations above ~300 A on 70H cans without corresponding controller and cooling upgrades.[^61]
- **Verify 90H authenticity before teardown.** Genuine 90H hubs ship with visibly longer magnets; riders measure the stack through the vent holes before committing to full disassembly.[^magnet_auth]
- **Confirm lead gauge before pushing current.** Recent Dualtron Achilleus tear-downs measured Lonnyo phase leads near 7 AWG with ~8 mm sleeving, supporting high-current goals but reinforcing the need to inspect for shipping damage before final assembly.[^62]
- **Rob Ver’s street setup favors wide rims.** His Vsett runs an LY 80H on a 110/100 rim with 80 mm tyres stretched onto the bead, lowered suspension, and controller temps around 40 °C thanks to under-deck mounting.[^63][^64]
- **Plan loom replacements on dual 65H builds.** Factory phase and hall leads choke inside the axle; riders targeting 300–400 A per controller report internal nicks and now budget fresh, thicker looms before raising current limits.[^axle_looms]
- **Track traction-control headroom.** Max Rainlogix’s Thunder (dual Lonnyo 70/110 hubs, Ubox 85/240) hauled two riders uphill at 320 A battery without overheating by capping phase to 150/200 A rear and 120/140 A front and leaving TC enabled—earlier 200/300 A tests proved viable but wheelie-prone.[^thunder_tc]
- **Log insulation upgrades.** Latest 65H 16×4 hubs ship potted for ≈180 °C operation, making them attractive commuter swaps so long as torque arms and wider swingarms handle the added stator mass.[^180c_insulation]

## Lonnyo Axle Spacing & Offset Cautions (Batch 13 Additions)

- Lonnyo spacer and offset specifications are critical for proper fitment—incorrect spacing has caused axle binding, premature bearing failure, and frame alignment issues on Dualtron and custom chassis builds.[^spacing-critical]
- **Spacer/offset guidance:**
  - 90H Lonnyo hubs demand torque-arm and deck-clearance planning before installation on Dualtron frames
  - Arm choices, spacer stacks, and dropout prep must be verified before riders twist axles under load
  - 145 mm dropout requirement for 11" hubs means many frames need machining or replacement swingarms[^dropout-req]
  - Expect up to 5 mm of axle-length variance between batches—mock up washer stacks on both sides and verify rotor centring before locking torque arms.[^65][^66]
- Document proper spacer stack configurations for common chassis (Dualtron, Nami, custom builds) to prevent field failures from improper fitment.[^spacing-guide]

## Source Notes

[^1]: Lonnyo wind shorthand, pricing, and traction-limited current goals for 22×3 vs. 33×2 builds.Source: knowledge/notes/input_part011_review.md, L288 to L293Source: knowledge/notes/input_part011_review.md, L328 to L329
[^2]: Community current envelopes for 22×3 hubs on Spintend hardware plus firmware caps on single Ubox 85150 setups.Source: knowledge/notes/input_part011_review.md, L309 to L311Source: knowledge/notes/input_part011_review.md, L340 to L353
[^3]: Dropout widths, swingarm hardware, and sealing requirements for 70H/80H/100H Lonnyo conversions.Source: knowledge/notes/input_part011_review.md, L365 to L417Source: knowledge/notes/input_part011_review.md, L463 to L465Source: knowledge/notes/input_part011_review.md, L482 to L536Source: knowledge/notes/input_part011_review.md, L628 to L736
[^4]: Controller pairing plans and budget ranges when escalating to 100H stators with 30 S packs and 400 A-class stages.Source: knowledge/notes/input_part011_review.md, L365 to L417
[^5]: Customs risk and landed cost expectations for 65H and 80H Lonnyo orders.Source: knowledge/notes/input_part011_review.md, L292 to L293Source: knowledge/notes/input_part011_review.md, L482 to L483
[^6]: Sensor harness diagnostics, supply-chain shifts, cabling experiments, and Longyu’s OEM role underpinning rebranded 65H hubs alongside custom magnet guidance from recent transcripts.Source: knowledge/notes/input_part014_review.md, L69 to L128Source: knowledge/notes/input_part008_review.md, L563 to L569Source: knowledge/notes/input_part009_review.md, L152 to L155Source: knowledge/notes/input_part009_review.md, L294 to L299
[^nami_overlap]: Lonnyo and NAMI hubs share factory engravings; Laotie TI30 builders reinforce frames and pick 70 H magnet stacks to keep 150 mm dropouts intact while gaining thicker phase leads.Source: data/vesc_help_group/text_slices/input_part005.txt, L22549 to L22556Source: data/vesc_help_group/text_slices/input_part005.txt, L23133 to L23193
[^80h_kv]: Lonnyo 80 H 22×3 stators logging ~34.8 kV free spin at 80 V and the reminder that 11" builds still need dual motors or lighter rims to accelerate well at that voltage.Source: knowledge/notes/input_part012_review.md, L234 to L236
[^achilleus_axle]: Dualtron Achilleus crews twisting Lonnyo 90 H axles until switching to Victor arms or custom torque hardware and widening clearances to ~176 mm with washer stacks.Source: knowledge/notes/input_part013_review.md, L421 to L421
[^tubeless_choice]: Community debates over tubed versus tubeless Lonnyo rims—split motors cannot be converted later, so racers pay for tubeless batches while commuters accept tubes and the maintenance trade-off.Source: knowledge/notes/input_part013_review.md, L335 to L338
[^side_exit]: New-gen Lonnyo 70H/75H hubs route phases through the side cover, freeing room for larger sleeved leads once the silicone jackets are warmed and dropouts are relieved.Source: knowledge/notes/input_part007_review.md, L306 to L306
[^thunder_tc]: Max Rainlogix’s dual-Lonnyo Thunder log covering 320 A battery climbs with traction control and staged phase limits plus earlier 200/300 A experiments that proved wheelie-prone.Source: knowledge/notes/input_part012_review.md, L362 to L363
[^180c_insulation]: Latest Lonnyo 65H 16×4 hubs shipping with 180 °C potting for commuter builds, highlighting the insulation upgrade over earlier 120 °C stators.Source: knowledge/notes/input_part010_review.md, L87 to L87
[^spacing-critical]: Lonnyo spacer and offset specifications being critical for proper fitment to avoid axle binding and bearing failures.Source: knowledge/notes/input_part013_review.md, L267 to L267
[^dropout-req]: 145 mm dropout requirement for 11" Lonnyo hubs and Paolo's spacing guidance.Source: knowledge/notes/input_part009_review.md, L355 to L355
[^spacing-guide]: Follow-up action to document Lonnyo axle-spacing guide for common chassis builds.Source: knowledge/notes/input_part013_review.md, L278 to L278

## References

[^1]: Source: knowledge/notes/input_part011_review.md, L288 to L293
[^2]: Source: knowledge/notes/input_part011_review.md, L328 to L329
[^3]: Source: knowledge/notes/input_part011_review.md, L309 to L311
[^4]: Source: knowledge/notes/input_part011_review.md, L340 to L353
[^5]: Source: knowledge/notes/input_part011_review.md, L365 to L417
[^6]: Source: knowledge/notes/input_part011_review.md, L482 to L483
[^7]: Source: knowledge/notes/input_part011_review.md, L531 to L536
[^8]: Source: knowledge/notes/input_part011_review.md, L463 to L465
[^9]: Source: knowledge/notes/input_part006_review.md, L315 to L315
[^10]: Source: data/vesc_help_group/text_slices/input_part014.txt, L10599 to L10612
[^11]: Source: knowledge/notes/input_part007_review.md, L328 to L333
[^12]: Source: knowledge/notes/input_part011_review.md, L431 to L434
[^13]: Source: knowledge/notes/input_part011_review.md, L288 to L289
[^14]: Source: knowledge/notes/input_part007_review.md, L49 to L49
[^15]: Source: knowledge/notes/input_part007_review.md, L59 to L59
[^16]: Source: knowledge/notes/input_part011_review.md, L628 to L628
[^17]: Source: knowledge/notes/input_part011_review.md, L292 to L293
[^18]: Source: knowledge/notes/input_part011_review.md, L306 to L308
[^19]: Source: knowledge/notes/input_part010_review.md, L205 to L208
[^20]: Source: knowledge/notes/input_part010_review.md, L205 to L209
[^21]: Source: knowledge/notes/input_part010_review.md, L172 to L174
[^22]: Source: knowledge/notes/input_part010_review.md, L87 to L88
[^23]: Source: data/vesc_help_group/text_slices/input_part013.txt, L15577 to L15603
[^24]: Source: data/vesc_help_group/text_slices/input_part013.txt, L16218 to L16240
[^25]: Source: data/vesc_help_group/text_slices/input_part010.txt, L11518 to L11518
[^26]: Source: knowledge/notes/input_part011_review.md, L370 to L371
[^27]: Source: knowledge/notes/input_part007_review.md, L430 to L430
[^28]: Source: data/vesc_help_group/text_slices/input_part010.txt, L10911 to L10988
[^29]: Source: data/vesc_help_group/text_slices/input_part010.txt, L10937 to L10948
[^30]: Source: data/vesc_help_group/text_slices/input_part010.txt, L10969 to L10972
[^31]: Source: knowledge/notes/input_part007_review.md, L24 to L24
[^32]: Source: knowledge/notes/input_part007_review.md, L38 to L38
[^33]: Source: knowledge/notes/input_part007_review.md, L22 to L22
[^34]: Source: knowledge/notes/input_part011_review.md, L415 to L417
[^35]: Source: knowledge/notes/input_part012_review.md, L465 to L465
[^36]: Source: knowledge/notes/input_part012_review.md, L412 to L412
[^37]: Source: knowledge/notes/input_part012_review.md, L245 to L245
[^38]: Source: knowledge/notes/input_part013_review.md, L312 to L323
[^39]: Source: knowledge/notes/input_part012_review.md, L425 to L425
[^40]: Source: knowledge/notes/input_part012_review.md, L483 to L483
[^41]: Source: knowledge/notes/input_part011_review.md, L736 to L736
[^42]: Source: knowledge/notes/input_part006_review.md, L153 to L153
[^43]: Source: data/vesc_help_group/text_slices/input_part013.txt, L18489 to L18495
[^44]: Source: knowledge/notes/input_part014_review.md, L128 to L128
[^45]: Source: knowledge/notes/input_part010_review.md, L378 to L378
[^46]: Source: data/vesc_help_group/text_slices/input_part011.txt, L19419 to L19459
[^47]: Source: knowledge/notes/input_part008_review.md, L563 to L576
[^48]: Source: knowledge/notes/input_part012_review.md, L464 to L464
[^49]: Source: knowledge/notes/input_part012_review.md, L462 to L462
[^50]: Source: knowledge/notes/input_part014_review.md, L5801 to L5840
[^51]: Source: knowledge/notes/input_part014_review.md, L5962 to L5968
[^52]: Source: knowledge/notes/input_part014_review.md, L5954 to L5959
[^53]: Source: knowledge/notes/input_part014_review.md, L6101 to L6109
[^54]: Source: knowledge/notes/input_part012_review.md, L426 to L426
[^55]: Source: knowledge/notes/input_part012_review.md, L273 to L273
[^56]: Source: knowledge/notes/input_part013_review.md, L325 to L334
[^57]: Source: knowledge/notes/input_part013_review.md, L335 to L338
[^58]: Source: knowledge/notes/input_part007_review.md, L333 to L339
[^59]: Source: knowledge/notes/input_part009_review.md, L152 to L155
[^60]: Source: knowledge/notes/input_part009_review.md, L294 to L299
[^61]: Source: knowledge/notes/input_part014_review.md, L69 to L69
[^62]: Source: knowledge/notes/input_part012_review.md, L472 to L473
[^63]: Source: knowledge/notes/input_part012_review.md, L424 to L424
[^64]: Source: knowledge/notes/input_part012_review.md, L480 to L481
[^65]: Source: data/vesc_help_group/text_slices/input_part013.txt, L9331 to L9349
[^66]: Source: data/vesc_help_group/text_slices/input_part013.txt, L10155 to L10159
