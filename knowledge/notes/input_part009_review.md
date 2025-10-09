# input_part009.txt Review

## Scope
- Source: `data/vesc_help_group/text_slices/input_part009.txt`
- Coverage: 2024-07-29 07:15:06 through 2024-08-26 07:04:10 (lines 1-8000)
- Next starting point: line 8001 (2024-08-26 07:04:10 and later)

## Key Findings

### Lighting & Control Wiring
- Tronic 250 aux 5 V rail keeps a 0.6 W taillight permanently on; moving the light to the connector beside the CAN bus only powers it while the controller is awake, otherwise add a self-latching switch for manual control.【F:data/vesc_help_group/text_slices/input_part009.txt†L41-L78】
- The VESC ADC lighting harness uses high-side switching: brake output sources battery positive while ground is shared with the headlight, so combine functions with diodes or resistors and wire anodes to the function pins, cathodes to ground as noted in the updated diagram.【F:data/vesc_help_group/text_slices/input_part009.txt†L46-L96】
- Xiaomi/Ninebot builders confirmed that an ADC expander can coexist with the stock dashboard by wiring the ADC module to ADC1/ADC2 and the dash to RX/TX, keeping cruise-control experiments possible without extra buttons.【F:data/vesc_help_group/text_slices/input_part009.txt†L1253-L1255】

### Battery Building Insights
- Mixing grey and purple LG M26 cells is acceptable here because every parallel group was binned to the same internal resistance; consistency matters more than colorways.【F:data/vesc_help_group/text_slices/input_part009.txt†L32-L37】
- Molicel P42A packs show little benefit for scooters limited to ~120 A battery draw; 50H motors on 20 S without ferrofluid saturate around 60 A battery current, so cheaper cells may suffice.【F:data/vesc_help_group/text_slices/input_part009.txt†L48-L49】
- Custom ASA‑CF cell holders require a heated build chamber to avoid warping, but the result is extremely rigid; expect filament costs near €50 per 750 g—roughly double standard ASA.【F:data/vesc_help_group/text_slices/input_part009.txt†L607-L615】
- Builders caution that XT90S anti-spark connectors fail quickly under scooter duty; QS8s are the preferred drop-in upgrade for higher reliability.【F:data/vesc_help_group/text_slices/input_part009.txt†L627-L628】
- Running range-extender packs with their own BMS in parallel works if the packs share voltage, but a tripped BMS can dump the full load on the others and instantly overstress them—plan for coordinated limits and protection.【F:data/vesc_help_group/text_slices/input_part009.txt†L470-L476】
- Heavy 17 S builds reported that VESC electrical braking respects the 71.4 V full-charge voltage, so regen at 72 V setpoints stays within controller limits.【F:data/vesc_help_group/text_slices/input_part009.txt†L1015-L1020】
- Rebuilt honeycomb packs benefitted from silicone spacers plus fishpaper or Kapton between series rows to preserve insulation while hot-gluing parallel groups, especially when wraps need replacing.【F:data/vesc_help_group/text_slices/input_part009.txt†L1354-L1383】【F:data/vesc_help_group/text_slices/input_part009.txt†L1946-L1953】
- Using twin steel strips over nickel is acceptable for ~8 A per cell in LG M26 builds, but ensure reinforcement and plan for ~10–11 kW limits on 17P layouts.【F:data/vesc_help_group/text_slices/input_part009.txt†L1044-L1062】
- Active balancing boards can equalize large packs in about an hour, whereas relying on the JBD BMS’s onboard balancing would take days—handy when finishing high-capacity assemblies.【F:data/vesc_help_group/text_slices/input_part009.txt†L1904-L1905】

### Quality Control Watch-outs
- Multiple members documented a €270 store-built pack with unsecured nickel, dented cells, and “repairs” that relied on electrical tape; the vendor refused refunds and suggested the buyer fund new cells despite the safety hazards.【F:data/vesc_help_group/text_slices/input_part009.txt†L315-L370】

### Controller Setup & Troubleshooting
- ABS over-current trips can be mitigated by raising the Max ABS Current in VESC Tool when the hardware and wiring allow it.【F:data/vesc_help_group/text_slices/input_part009.txt†L193-L198】
- Keyboard control in VESC Tool must be explicitly enabled in the UI (right-side toggle) even after a successful motor wizard run—useful when pairing Ubox controllers with M365 dashboards.【F:data/vesc_help_group/text_slices/input_part009.txt†L257-L294】
- For Flipsky 75200 V2 installs that heat motors during free-spin, disable the phase filter, rerun detection, switch to the `mxlemming` observer, and cap currents at ~120 A motor / 50–60 A battery with -5 A regen until the tune is stable.【F:data/vesc_help_group/text_slices/input_part009.txt†L768-L783】
- When bench-testing a Spintend VESC on a DC PSU, disable regen and avoid free-spinning field-weakening, otherwise back-EMF can over-voltage the supply and pop it.【F:data/vesc_help_group/text_slices/input_part009.txt†L1120-L1125】
- Small hub motors driven by Flipsky 75200s showed that aggressive field-weakening observers (`mxm` variants) deliver speed but have killed controllers; increasing system voltage or easing FW demand is safer than pushing tiny motors past their limits.【F:data/vesc_help_group/text_slices/input_part009.txt†L1290-L1331】
- Sensorless VESC operation in FOC is viable but expect to push-start the wheel or invest time in HFI tuning to avoid squealing stalls.【F:data/vesc_help_group/text_slices/input_part009.txt†L1713-L1721】
- Spintend 85150 controllers rely on 100 V-class components, yet reports show units failing at 20 S when high-kV motors, MTPA, and heavy field-weakening stack stress on the hardware—stay conservative on voltage boost strategies.【F:data/vesc_help_group/text_slices/input_part009.txt†L1522-L1536】
- Paolo highlighted reliability gaps in unvetted MOSFETs (e.g., fake datasheets from JJmicro) and favors Huayi parts that hold 20 kW loads below 40 °C—verify switching parameters before adopting bargain FETs.【F:data/vesc_help_group/text_slices/input_part009.txt†L1541-L1555】

### Spot Welders & Power Delivery
- Glitter 801D users saw LiPo-fed capacitor banks sag toward 5.7 V, with weld quality falling off unless they rotate packs or switch to low-ESR capacitor supplies.【F:data/vesc_help_group/text_slices/input_part009.txt†L2001-L2013】
- Paolo cautioned that KWelds will still trip on over-current if the input bank is oversized or the cabling is wrong, so Glitter owners shouldn’t expect immunity just because they run capacitors.【F:data/vesc_help_group/text_slices/input_part009.txt†L2015-L2018】
- Builders weighing upgrades highlighted why the 801H is the “buy once” choice: twenty transistors instead of five, stronger shunts/protection, and better welding pens for regions where returns are costly.【F:data/vesc_help_group/text_slices/input_part009.txt†L2054-L2056】
- Follow-up chatter clarified limits—GABE flatly noted that a stock 801D cannot reliably weld 0.15 mm copper, so heavier sandwiches belong on the 801H plan.【F:data/vesc_help_group/text_slices/input_part009.txt†L2959-L2960】

### Spot Welder Power Debates & Alternatives
- Paolo reiterated that 60 Ah car batteries only deliver ~750 A pulses and still trip KWeld overcurrent faults, urging builders to avoid lead-acid sources and instead size their cabling/connectors (QS8/EC8 with 25 mm² leads) for KWeld’s ~2000 A ceiling.【F:data/vesc_help_group/text_slices/input_part009.txt†L5004-L5076】
- The same thread recommends TIG with a low-cost timer board as a clean alternative that sidesteps cable heating losses when spot welders keep faulting, particularly for builders chasing thick copper sandwiches.【F:data/vesc_help_group/text_slices/input_part009.txt†L5057-L5068】
- Later updates confirm Glitter 801D success only when pairing 0.1 mm copper with steel or iron caps; pure nickel sandwiches tear free even at full power, underscoring the need for higher-grade machines before attempting thicker copper stacks.【F:data/vesc_help_group/text_slices/input_part009.txt†L6203-L6239】

### Suspension, Tires & Mounting
- Riders comparing EXA shocks report that KKE dampers outperform EXA 388/291 units, with 60 kg riders advised to start around 650–850 lb springs (1000 lb if running twin shocks) and adjust upward only for firmer feel.【F:data/vesc_help_group/text_slices/input_part009.txt†L5168-L5228】
- Tubeless tire swaps on 11–12 inch rims are easiest with ratchet straps or belts plus pry bars; small pumps can seat beads once the strap preloads the carcass, offering a portable alternative to shop compressors.【F:data/vesc_help_group/text_slices/input_part009.txt†L6281-L6333】
- PuneDir’s 12-inch conversion on a Zero 10X highlights clearance challenges, while Paolo notes that true 11-inch motors often foul suspension springs unless spacers are reworked—keep motor diameter in mind before chasing larger rims.【F:data/vesc_help_group/text_slices/input_part009.txt†L6281-L6299】【F:data/vesc_help_group/text_slices/input_part009.txt†L6369-L6371】

### Controller & Firmware Notes
- Xiaomi XESC controllers can run field-weakening up to ~20 S if hardware mods raise voltage sensing, but veterans warn that FW cutoffs can still brick Xiaomi and G30 ESCs—treat FW as optional speed boost, not daily tuning baseline.【F:data/vesc_help_group/text_slices/input_part009.txt†L5231-L5274】
- Community feedback pegs Spintend minis at ~135 A phase from the factory; pushing 180–200 A plus FW has cracked hardware, so plan cable mods or bigger controllers for sustained power experiments.【F:data/vesc_help_group/text_slices/input_part009.txt†L6008-L6036】
- Windows users continue to report VESC Tool 6.05 launch failures even though the build runs on Ubuntu, suggesting a lingering installer or dependency issue worth documenting alongside the newly posted 6.05 binaries.【F:data/vesc_help_group/text_slices/input_part009.txt†L6354-L6356】【F:data/vesc_help_group/text_slices/input_part009.txt†L6483-L6490】

### Sensor & Display Updates
- Patrick fixed a -23 °C thermistor reading on his VESC by swapping in a 100 kΩ NTC and 1 kΩ PTC pair, confirming the stock scaling expects that combo.【F:data/vesc_help_group/text_slices/input_part009.txt†L6505-L6507】
- The factory Vsett display works with VESC builds when flashed with the open-source firmware that’s circulating on GitHub, giving commuters a plug-in dash option.【F:data/vesc_help_group/text_slices/input_part009.txt†L6920-L6920】

### Vsett 10+ Dual-VESC Conversion Lessons
- Yoann’s customer build expanded the stock pack to 20 S 8 P while retaining the NAMI BMS, then dropped in dual Spintend VESC Lite 100 V/100 A controllers to deliver smoother power without changing the scooter’s stock appearance.【F:data/vesc_help_group/text_slices/input_part009.txt†L6553-L6560】
- Lacking a native 12 V rail, he now uses VESC 5 V to trigger an Arduino relay that energizes a battery-fed 12 V converter, keeping lights and accessories off the delicate Ignite port fuse that has already blown twice in testing.【F:data/vesc_help_group/text_slices/input_part009.txt†L6603-L6608】
- Dual-hall throttle setups demanded manual tweaks to the throttle’s start voltage after calibration to keep brake and throttle inputs stable, so expect iterative tuning if you split controls across master/slave VESCs.【F:data/vesc_help_group/text_slices/input_part009.txt†L6561-L6563】

### Wiring & Harness Tips
- Doubling up 12 AWG leads proved sufficient for ~80 A battery runs on GABE’s 8 P pack, suggesting parallel silicone leads are a workable compromise when routing space is tight.【F:data/vesc_help_group/text_slices/input_part009.txt†L6581-L6584】
- Two-meter throttle extensions haven’t shown noise problems for Ion when using quality silicone cable, so shielded loom is optional for most scooters.【F:data/vesc_help_group/text_slices/input_part009.txt†L7164-L7185】
- Rewiring a JBD harness without shorting the identical white sense leads caused false zero readings until the missing parallels were re-tied to the same terminal—double-check the diagram before moving balance wires around mid-pack repair.【F:data/vesc_help_group/text_slices/input_part009.txt†L6669-L6686】
- Pandalgns discovered that older Android VESC Tool builds lock users into “limited” mode; reinstalling the free 6.05 release from vesc-project.com restored full configuration access and firmware updates.【F:data/vesc_help_group/text_slices/input_part009.txt†L6825-L6890】

### Regen Brake Lighting Reality Check
- Riders relying on regen throttles confirmed that most VESCs—including Makerbase 75/200 variants—lack a native brake-light trigger, so you either dedicate an ADC board output or program a spare GPIO with external resistors/relays to drive 12 V lighting.【F:data/vesc_help_group/text_slices/input_part009.txt†L7134-L7141】【F:data/vesc_help_group/text_slices/input_part009.txt†L7741-L7754】

### Copper Welding & Materials Debates
- The group keeps steering newcomers toward KWeld kits (or Glitter 801H-class rigs) when they need reliable copper welds; Glitter 801D struggles beyond 0.1 mm copper while KWeld’s joule-controlled pulses manage 0.1–0.2 mm with good prep.【F:data/vesc_help_group/text_slices/input_part009.txt†L7559-L7583】【F:data/vesc_help_group/text_slices/input_part009.txt†L7631-L7645】
- Builders warned that 0.5 mm copper strip is overkill for spot welding, recommending wider 0.1–0.2 mm sheets or stacked layers instead of fighting thick stock that overheats pens and is difficult to cut cleanly.【F:data/vesc_help_group/text_slices/input_part009.txt†L7589-L7643】

### Adhesive & Insulation Lessons
- Hot-melt glue softens around 80–90 °C and doesn’t adhere well to cold cans, so Noname prefers it only for temporary tacking before switching to cell holders, fishpaper, or silicone that resists vibration in finished packs.【F:data/vesc_help_group/text_slices/input_part009.txt†L7754-L7760】

### Mechanical & Repair Tips
- Xiaomi frame owners debating oversize fasteners were advised to avoid 3.2 mm pilot holes for M4 taps—Arsenus reports that diameter risks thinning the frame bosses, so step up cautiously if you already stripped M3 hardware.【F:data/vesc_help_group/text_slices/input_part009.txt†L7964-L7978】

### Controller Maintenance & Recovery
- Jeferson’s Flipsky 75100 remains stuck on a blue LED despite ST-Link attempts, underscoring the need for a documented unbrick workflow when SWD flashing fails on these boards.【F:data/vesc_help_group/text_slices/input_part009.txt†L7995-L7995】

### Long-Range Emoto Tuning Notes
- Noname’s single-Ubox commuter is clocking 100-mile rides by capping motor phase around 80 A and battery draw near 155 A to keep the QS hub under 45 °C, while he plans larger heatsinks (or even water cooling) before exploring higher power.【F:data/vesc_help_group/text_slices/input_part009.txt†L7715-L7729】

### Motor & Wiring Sourcing
- Paolo advises capping Nami motor phase current near 200–250 A unless you rewire with shorter, larger-gauge leads; stock PTFE-insulated conductors look thin but carry heat better than silicone, so confirm cross-section before replacement.【F:data/vesc_help_group/text_slices/input_part009.txt†L6030-L6077】
- Longyu (LY) manufactures many “65H” performance hubs; Vsett, Lonnyo, Huameng, and Kaabo-labeled motors are often rebrands, and Paolo cautions that some AliExpress “factory” sellers are just resellers despite marketing claims.【F:data/vesc_help_group/text_slices/input_part009.txt†L6381-L6416】
- Eleven-inch hub swaps can collide with suspension springs on stock swingarms, making zero/Kaabo-style 65H hubs the safer upgrade path for 10-inch frames than chasing oversized Vsett housings.【F:data/vesc_help_group/text_slices/input_part009.txt†L6369-L6389】

### Battery Packaging & Maintenance
- PuneDir’s attempt to hang a 20S10P stem pack drew safety pushback—veterans prefer internal mounting or backpacks to avoid exposed mass on the mast, especially once existing decks are already full.【F:data/vesc_help_group/text_slices/input_part009.txt†L5113-L5121】
- Water-soaked Niu motors came back to life after drying and regreasing bearings, but the group still recommends sealed bearings and added seals before riding through floods again.【F:data/vesc_help_group/text_slices/input_part009.txt†L6271-L6278】

### BMS & Voltage References
- Quick math for 22 S packs: divide total voltage by 22 and compare to a single-cell curve; memorizing the linear 3.1–4.2 V window per cell helps translate pack percentage readings on the fly.【F:data/vesc_help_group/text_slices/input_part009.txt†L6358-L6363】

### Battery Pack Assembly & Insulation
- Builders layered plexiglass and fishpaper as rigid sidewalls, then doubled nickel over thin copper leads to stiffen current paths on tight decks.【F:data/vesc_help_group/text_slices/input_part009.txt†L2025-L2035】
- Oversized JBD “100 A” enclosures actually measure ~27 mm once screws and heat sinks are counted, forcing silicone shims and spacer reprints for safe isolation in crowded bays.【F:data/vesc_help_group/text_slices/input_part009.txt†L2041-L2087】
- Copper/nickel sandwich debates underscored oxidation trade-offs: nickel-plated steel caps stay popular, but anyone chasing 0.2 mm copper thickness was advised to pair it with 801H-grade power and watch tip pressure carefully.【F:data/vesc_help_group/text_slices/input_part009.txt†L2146-L2200】
- When customs delays blocked metal boxes, riders wedged packs with foam blocks or even taped shells just to ride—stopgaps that need better thermal padding guidance before they become permanent fixes.【F:data/vesc_help_group/text_slices/input_part009.txt†L3051-L3056】【F:data/vesc_help_group/text_slices/input_part009.txt†L3302-L3327】

### BMS Tools & App Quirks
- JBD’s smartphone app blindly mirrors the handset language, so the “Softlock” toggle and balance thresholds only show up once you flip Android/iOS to English, load the admin APK, and reopen the menus.【F:data/vesc_help_group/text_slices/input_part009.txt†L2098-L2135】
- ANT Smart BMS harness pinouts change between 10 S and higher packs; the actual diagrams sit inside AliExpress listings, and miswiring has already killed hardware, so the shared screenshot archive is now the group’s go-to reference.【F:data/vesc_help_group/text_slices/input_part009.txt†L3350-L3415】

### Controller & Powertrain Lessons
- Flipsky 84100 owners kept reiterating that 60–80 A battery and ~135 A phase is the realistic ceiling; reports of 120 A battery draw usually end in thermal or hardware failure (including the Chile burnout).【F:data/vesc_help_group/text_slices/input_part009.txt†L3011-L3024】
- European builders reminded newcomers that typical three-phase residential feeds are ~16 A per leg (~11 kW total), so fantasies about 40 C home charging only work with industrial-grade service upgrades.【F:data/vesc_help_group/text_slices/input_part009.txt†L3288-L3296】
- Paolo keeps upgrading phase leads to roughly 2.5× stock cross-section to curb voltage drop, while PuneDir’s over-shunted square-wave controller started “coughing” between 25–50 km/h after his latest tune—both data points argue for thicker cabling and sane verification before chasing peak numbers.【F:data/vesc_help_group/text_slices/input_part009.txt†L3441-L3448】【F:data/vesc_help_group/text_slices/input_part009.txt†L3491-L3497】

### Late-Stage Controller Failures & Guardrails
- PuneDir’s shunt-heavy square-wave ESC is saturating a 1 kW motor and even previously blew traces and FETs; he can only mask the issue above ~50 km/h, so current limits need to match motor capability rather than what the modded board can momentarily supply.【F:data/vesc_help_group/text_slices/input_part009.txt†L3503-L3525】【F:data/vesc_help_group/text_slices/input_part009.txt†L3526-L3532】
- Yamal’s dual Little Focer/Tronic 250 build finally failed after repeated 37 A field-weakening pulls at ~20 kW; the group reiterated those controllers are happiest near 150 A phase (~5–8 kW) and surviving higher power requires stepping up to 12 FET Spintend or Tronic 250R-class hardware.【F:data/vesc_help_group/text_slices/input_part009.txt†L3730-L3732】【F:data/vesc_help_group/text_slices/input_part009.txt†L3702-L3710】
- Field-weakening cutoffs can cascade into catastrophic failures: both GABE and Yamal called out that an FW-induced shutdown can spike components and “kill everything,” so conservative FW settings plus proper battery headroom are mandatory for highway-speed testing.【F:data/vesc_help_group/text_slices/input_part009.txt†L3730-L3732】

### Budget Controller Shopping & Detection Pitfalls
- Spintend’s 12 FET controller remains the community’s go-to “budget but proven” choice for 20 S commuters, while Ubox Lite and full Ubox 85/250 units are the practical upgrade paths when customs or budget block Tronic replacements.【F:data/vesc_help_group/text_slices/input_part009.txt†L3562-L3568】【F:data/vesc_help_group/text_slices/input_part009.txt†L3738-L3753】
- Makerbase/Flipsky detection routines continue to misreport inductance and resistance by triple-digit percentages, and veterans now insist on measuring motor parameters with trusted tools (or a known-good VESC) before riding—automatic detection has already caused on-road accidents.【F:data/vesc_help_group/text_slices/input_part009.txt†L3854-L3875】
- Budget dual-motor dreams on G30 platforms still require two independent controllers; trying to save money with unknown AliExpress boards only shifts risk because capacitor banks, thermal mass, and layout quality vary wildly between look-alike units.【F:data/vesc_help_group/text_slices/input_part009.txt†L3754-L3788】

### Balance Leads, Harnessing & Spot-Welding Alternatives
- Jason’s balance-lead workflow keeps the JST harness plugged in while routing; if you misplace a wire the BMS simply refuses to boot until the lead is corrected, sparing the board as long as you fix the mistake quickly.【F:data/vesc_help_group/text_slices/input_part009.txt†L3834-L3848】
- Builders struggling with customs delays are experimenting with €25 purple PCB welders driven by 72 Ah car batteries; they weld 0.2 mm nickel reliably but likely lack the transistor count for 0.15 mm copper, reinforcing earlier advice to reserve thicker copper sandwiches for Glitter 801H rigs.【F:data/vesc_help_group/text_slices/input_part009.txt†L4259-L4273】
- PuneDir’s clamp-meter tests on a single phase showed how easy it is to overestimate delivered phase current when shunt mods and square-wave controllers are in play; he still targets 200 A phase / 150 A battery but the hardware happily overshoots into the 260 A phase range, so instrumentation and sane cabling remain vital.【F:data/vesc_help_group/text_slices/input_part009.txt†L3809-L3826】【F:data/vesc_help_group/text_slices/input_part009.txt†L4049-L4069】

### Cells, Cabling & Supply Limits
- Samsung 32E cells are only good for ~6.5 A per can (≈39 A shared across six parallels), so stacking extra nickel over series joints adds little benefit on mid-power builds.【F:data/vesc_help_group/text_slices/input_part009.txt†L2360-L2370】
- Stock G30 phase wires are undersized “chinesium”; upgrading to silicone 12 AWG keeps short runs cool even if tables rate them for only 20 A continuous, as scooter duty cycles and AC drive let them survive bursts.【F:data/vesc_help_group/text_slices/input_part009.txt†L3381-L3403】
- Range-focused packs like 22 S 11 P LG M50LT builds still peak near 120 A with legacy controllers, and owners plan P45B upgrades once the current pack ages out.【F:data/vesc_help_group/text_slices/input_part009.txt†L3351-L3355】

### Tools & Build Process Tips
- Paolo walked PuneDir through reshaping that €25 square-wave ESC: use a bench supply, read millivolt drop across the shunt, and back into resistance with Ohm’s law instead of guessing with hobby meters.【F:data/vesc_help_group/text_slices/input_part009.txt†L2964-L2987】
- When customs halted battery boxes, temporary solutions ranged from foam blocks to literal tape cocoons—fine for testing, but everyone acknowledged the need for sturdier printable cradles once imports resume.【F:data/vesc_help_group/text_slices/input_part009.txt†L3302-L3327】

- Capture a clean wiring diagram showing how to share brake and reverse lighting on the VESC ADC harness without overloading a single output.【F:data/vesc_help_group/text_slices/input_part009.txt†L46-L96】
- Summarize safe current-sharing strategies for hybrid packs so newcomers understand the BMS trip failure mode before paralleling dissimilar batteries.【F:data/vesc_help_group/text_slices/input_part009.txt†L470-L476】
- Track down trusted suppliers for QS8 anti-spark connectors and document retrofit steps for scooters currently wired with XT90S.【F:data/vesc_help_group/text_slices/input_part009.txt†L627-L628】
- Draft a bench-testing checklist for VESCs that explains PSU voltage limits, regen disablement, and safe spin tests before riders hook fragile lab supplies to controllers.【F:data/vesc_help_group/text_slices/input_part009.txt†L1120-L1125】
- Collect vetted sources for Glitter/KWeld accessories (replacement tips, capacitor packs, steel strip) so builders can replicate the reliable welding setups discussed here.【F:data/vesc_help_group/text_slices/input_part009.txt†L2001-L2056】【F:data/vesc_help_group/text_slices/input_part009.txt†L2146-L2200】
- Produce a quick-reference guide for the JBD/Jiyuan mobile apps that covers Softlock toggles, admin mode installation, and balance-threshold edits so builders stop bricking translations.【F:data/vesc_help_group/text_slices/input_part009.txt†L2098-L2135】
- Summarize safe working limits for Flipsky 84100 and similar six-FET VESCs so newcomers respect the 60–80 A battery guidance and avoid cooked hardware.【F:data/vesc_help_group/text_slices/input_part009.txt†L3011-L3024】
- Capture wiring diagrams/pinouts for ANT Smart BMS harness variants before more builders miswire balance leads when converting between 10 S and higher cell counts.【F:data/vesc_help_group/text_slices/input_part009.txt†L3350-L3415】
- Document proven spacer/foam recipes (or printable cradles) for riders stuck without metal battery boxes so temporary tape jobs don’t become long-term hazards.【F:data/vesc_help_group/text_slices/input_part009.txt†L3051-L3056】【F:data/vesc_help_group/text_slices/input_part009.txt†L3302-L3327】
- Create a failure-analysis brief on Tronic 250/Little Focer field-weakening limits so riders stop pushing 20 kW through controllers rated for ~8 kW and burning PCBs mid-ride.【F:data/vesc_help_group/text_slices/input_part009.txt†L3730-L3732】
- Summarize safe testing steps for shunt-modded square-wave controllers, including phase-current verification and motor saturation checks, to keep future PuneDir-style builds from cooking traces or FETs.【F:data/vesc_help_group/text_slices/input_part009.txt†L3503-L3532】【F:data/vesc_help_group/text_slices/input_part009.txt†L3809-L3826】
- Evaluate the €25 purple PCB spot welder against Glitter/KWeld options and note realistic thickness limits so builders know when they must upgrade to capacitor-driven machines.【F:data/vesc_help_group/text_slices/input_part009.txt†L4259-L4273】
- Build a KWeld setup guide that covers acceptable power sources, cable gauges, and connector choices so newcomers stop pairing car batteries or oversized capacitor banks that trigger faults.【F:data/vesc_help_group/text_slices/input_part009.txt†L5004-L5076】
- Draft a spring-rate cheat sheet for EXA/KKE shocks on lightweight scooters, including baseline suggestions for riders under 70 kg and notes on dual-shock tuning.【F:data/vesc_help_group/text_slices/input_part009.txt†L5168-L5228】
- Create a tubeless tire mounting checklist (belts, straps, portable pumps) tailored to 10–12 inch scooter rims to reduce failed bead attempts in the field.【F:data/vesc_help_group/text_slices/input_part009.txt†L6281-L6333】
- Publish a 22 S voltage-to-percentage reference so riders can cross-check SOC without digging up single-cell charts mid-ride.【F:data/vesc_help_group/text_slices/input_part009.txt†L6358-L6363】
- Map Longyu/Lonnyo/Huameng motor families, including expected stator sizes and required cable mods, to guide upgrades beyond stock 50H hubs.【F:data/vesc_help_group/text_slices/input_part009.txt†L6030-L6077】【F:data/vesc_help_group/text_slices/input_part009.txt†L6381-L6416】
- Document the 100 kΩ NTC/1 kΩ PTC sensor pairing and other common thermistor swaps so mis-scaled temperature readings are easier to diagnose.【F:data/vesc_help_group/text_slices/input_part009.txt†L6505-L6507】
- Turn Yoann’s Vsett 10+ conversion into a wiring/cable-management case study covering ADC board roles, relay-powered lighting, and throttle tuning on dual VESC installs.【F:data/vesc_help_group/text_slices/input_part009.txt†L6553-L6563】【F:data/vesc_help_group/text_slices/input_part009.txt†L6603-L6608】
- Capture a JBD harness troubleshooting guide that explains which white sense leads share terminals and how to recover from miswired balance looms mid-pack repair.【F:data/vesc_help_group/text_slices/input_part009.txt†L6669-L6686】
- Add a regen-brake lighting how-to that compares ADC boards, GPIO triggers, and 12 V relay options for builders who want brake lights without sacrificing throttle inputs.【F:data/vesc_help_group/text_slices/input_part009.txt†L7134-L7141】【F:data/vesc_help_group/text_slices/input_part009.txt†L7741-L7754】
- Expand the copper-welding primer with KWeld joule targets, Glitter 801-series limits, and practical strip thickness choices for 0.1–0.2 mm builds.【F:data/vesc_help_group/text_slices/input_part009.txt†L7559-L7583】【F:data/vesc_help_group/text_slices/input_part009.txt†L7631-L7645】
- Outline hot-glue alternatives (cell holders, silicone, TPU spacers) for pack assembly so newcomers avoid adhesives that creep at 80 °C.【F:data/vesc_help_group/text_slices/input_part009.txt†L7754-L7760】
- Build an ST-Link recovery checklist specific to Flipsky/Makerbase 75100 blue-LED faults to reduce guesswork when SWD flashing fails.【F:data/vesc_help_group/text_slices/input_part009.txt†L7995-L7995】
