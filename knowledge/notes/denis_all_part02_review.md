# all.part02.txt Review

## Scope
- Source: `data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt`
- Coverage: 2021-08-15T19:35 through 2025-10-09T09:03 (lines 1-131,313)
- Next starting point: Completed through line 131,313 (file end)

## Key Findings

### 13S Single-Motor Builds Outperform Dual Swaps on the G30 (Lines 119,361-119,473 & 119,648-119,656)
- Denis and James steered riders toward a 13S pack on the stock G30 motor instead of chasing dual hubs: the factory wheel already hustles at 40–45 km/h on 30–40 A, the Happy/Denis BMS tops out at 44 A, and Rita’s 30 A ceiling cannot feed a second motor, so budget goes furthest on cells, thermistors, and controller settings while monitoring regen on full packs to avoid cooked ESCs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L119361-L119473】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L119648-L119656】

### Solid Tires and Suspension Choices for High-Speed G30 Builds (Lines 119,502-119,560)
- Veterans warned that the foam-filled “solid” tires vibrate enough to loosen magnets and shake packs apart, and recommended pairing quality 10-inch pneumatics with a Monorim front/DNM rear combo for 50+ km/h stability—Sharkset forks stay comfy but wobble over ~45 km/h while Monorim rears struggle to clear large motors.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L119502-L119560】

### Happy BMS Capacity Limit is Only an SoC Estimate (Lines 120,201-120,206)
- Denis confirmed Happy BMS happily manages packs larger than its 32 Ah rating: the display just hits 0 % with ~3 Ah remaining before it keeps discharging, so owners can oversize capacity without tripping protection.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L120201-L120206】

### BMS Emulation Doesn’t Cure Cell Imbalance (Lines 120,220-120,240)
- Ignoring the Xiaomi BMS signal via SHFW only hides error 21—the charger still cycles red/green when the pack’s cell delta is high, so troubleshoot the battery instead of blaming firmware bypasses.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L120220-L120240】

### Fix Monorim Stem Wobble with the Correct Hardware Stack (Lines 120,269-120,296)
- Stem play after a Monorim install usually traces to missing parts: reuse the short upper screw, seat the small top ring, and swap tired bearings before reassembly to restore steering stiffness.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L120269-L120296】

### Monorim’s “304 Stainless” Axle Upgrade is Marketing (Lines 120,375-120,399)
- The touted V5 “304 stainless” axle still behaves like cheap mild steel—Magnets stick and hardware yields—so builders stick with grade 12.9 or titanium fasteners if they need real strength.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L120375-L120399】

### Use Dedicated DC‑DC Converters for 12 V Accessories (Lines 120,316-120,325)
- G30 dashboards only expose 5 V data power, so lighting mods need an external DC‑DC converter sized to fit above the charger; verify the enclosure before ordering and skip unnecessary enable pins when the light has its own switch.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L120316-L120325】

### Stress-Relieve Buck Converter Leads to Stop Wire Fatigue (Lines 121,001-121,023)
- Frequently flexed converter leads snap cleanly unless they’re pre-tinned, glued, or tied to the PCB—RTV silicone, zipties, and letting the cable rest against the board prevent breakoffs before the scooter even rolls.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L121001-L121023】

### Match Wire Gauge and Reinforce Clone Controllers Before Pushing 12S (Lines 121,041-121,058)
- Builders spec AWG14 for ~16 A 12S packs and treat AliExpress controller clones as bare boards: replace junk MOSFETs, add copper to traces, and only reuse donor MOSFETs if they test good before soldering them in.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L121041-L121058】

### Continuity Tests Reveal MOSFET Failures and Low-Voltage Chargers Only Revive Depleted 44 V Packs (Lines 121,058-121,069)
- Probe between battery rails and phase leads with the pack disconnected—beeping under 50 Ω signals a shorted MOSFET—and only backfeed a 44 V pack with a 36 V charger if the pack rests under ~41 V to avoid overvoltage.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L121058-L121069】

### Keep Hall Sensors in Their Original Geometry and Maintain MOSFET Isolation (Lines 121,130-121,145)
- Swapping long-form hall ICs for short ones costs ~10 km/h because sensor spacing matters; glue replacements exactly where the originals sat and retain insulating pads or isolation tape when bolting MOSFETs back down.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L121130-L121145】

### Diagnose Dead Packs by Probing Every Cell (Lines 121,801-121,804)
- When a fresh pack refuses to wake, crack the wrap and measure every series group—bypassing the BMS is strictly for testing because running without it is a fire risk.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L121801-L121804】

### Charging at 29 °C is Fine—Just Avoid Subzero Sessions (Lines 121,820-121,829)
- Group consensus put safe charging under ~55 °C and warned against charging below freezing; brief 28–29 °C sessions pose no issue, but cold-soaked packs should warm before plugging in.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L121820-L121829】

### Print Cell Holders in Heat-Resistant Filament (Lines 122,809-122,815)
- PLA battery cradles deform once cells warm; PETG or ASA withstand scooter temps and let 21700 honeycomb layouts survive in tight decks.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L122809-L122815】

### Modern Rita Harnesses Don’t Need Jumpers Cut at 13S—Configure Before Connecting Packs (Lines 122,300-122,315)
- Denis clarified that current Rita revisions keep both jumpers intact on 13S setups; only cut the green lead when using a 10S+ internal pack and always set the external series count in the app before plugging it in to dodge error 39.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L122300-L122315】

### Log Real-World Current to Clear Rita Error 39 (Lines 122,563-122,575)
- Rita throws error 39 when firmware pulls past 30 A or the adapter overheats—record live amps with m365Tools and turn the tune down before the new adapter protects itself again.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L122563-L122575】

### Reconfigure Rita Whenever You Swap External Pack Voltage (Lines 122,580-122,588)
- Running 36 V and 48 V externals on the same scooter is fine, but only after updating Rita’s series and capacity settings each time; the manual lives at Embedden’s Rita docs for quick reference.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L122580-L122588】

### Round Nickel Edges and Mind Load When Building Low-Current Packs (Lines 122,364-122,385)
- For 1S12P power-bank builds, Denis okayed light welds under 5 A, while James reminded newcomers to deburr nickel around positive caps because the can is negative and sharp tabs pierce fishpaper rings.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L122364-L122385】

### Stock Xiaomi BMSs Can’t Be Paralleled Safely Without a Common-Port Design (Lines 122,761-122,787)
- Denis stressed that OEM Xiaomi packs lack common ports, so they shouldn’t be paralleled through Rita or Y-cables; equalize voltage first and leave parallel wiring to builders who truly understand the risks.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L122761-L122787】

### Replace Every Cell in Worn Packs Instead of Mixing Fresh Ones (Lines 122,788-122,795)
- Sergey called partial replacements a waste—aging Xiaomi packs need complete re-cell jobs because the remaining groups are already degraded and won’t match new inserts for long.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L122788-L122795】

### Never Pull Lighting Power from the Charge Port (Lines 122,796-122,799)
- Even on Vsett-class scooters, veterans refuse to draw accessory power from the charge socket; build a Y-connector off the discharge rails to keep charging protections intact.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L122796-L122799】

### Happy BMS 44 A Ceiling Is Fixed—Use a Larger BMS for 3 kW Goals (Lines 123,270-123,276)
- Denis told AWD planners that Happy BMS isn’t the right tool for 3 kW builds; stick to its 44 A limit and choose Daly/ANT-class boards if you need 50–60 A continuous headroom.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L123270-L123276】

### Recommended Cell Chemistries for High-Draw Builds (Lines 123,275-123,279)
- For 15S AWD packs, Denis pointed to LG M29 or EVE 33V cells, while Arsenus added Molicel P42A/40T, Samsung 25R/30Q, and Sony VTC5/VTC6 for higher discharge setups—21700 cells remain the preferred AWD baseline.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L123275-L123279】

### Drop Xiaomi’s Data Line by Flashing BMS Emulation (Lines 123,431-123,437)
- Replacing an M365 BMS with a generic board requires flashing SHFW or XiaoDash with BMS emulation—the ESC will throw error 21 without it, and ScooterHacking’s guide walks through the process.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L123431-L123437】

### Monorim AWD Kits Disappoint—DIY with OEM Motors Instead (Lines 123,525-123,533)
- The off-the-shelf Monorim 48 V AWD kit ships with weak controllers, poor motors, and an undersized battery; veterans advise building AWD with dual OEM controllers and hubs instead.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L123525-L123533】

### Mi3 BLE Downgrades Need Older DRV Files and NGFW Mods (Lines 123,536-123,561)
- When BMS Tool refuses to connect to a Mi3, Denis and HeroDash advised downgrading BLE/DRV via Scooter Hacking Utility: flash DRV016 with NGFW’s model-lock removal and expect to hunt compatible firmware on mp365.es until SHU adds broader support.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L123536-L123561】

### Swap the Monorim 500 W Dust Cover for the Disc Adapter (Lines 123,575-123,577)
- The Monorim 500 W disc adapter replaces the stock cover—it does not stack on top—so remove the original plate before installing the brake mount.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L123575-L123577】

### Dual-Motor GT100 Controllers Depend on Accurate Hall Settings (Lines 123,588-123,610)
- Erratic speeds on GT100 dual setups typically stem from misconfigured magnet counts or hall order; restore factory P-menu values (e.g., 30 magnets) and remember these controllers switch to sensorless operation above low speeds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L123588-L123610】

### Diagnosing Dead Xiaomi Dashboards and ESC Power Rails (Lines 99,377-99,445)
- When a scooter won’t power up and the ESC status LED stays dark, veterans direct owners to inspect the controller first: the power button just bridges ground to signal on the dashboard cable, so focus on the ESC power-supply stages, trace any intermittent faults over time, and probe voltage regulators and coil drop across both sides instead of blaming the dash itself.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L99377-L99445】

### Rita Charge Ceilings and Dual 10S Behavior (Lines 99,469-99,516)
- Rita v4 settles around 41.2 V when charging because of its inline diodes, mirroring stock chargers; running two 10S packs in parallel doesn’t require Rita, but keeping it inline is harmless aside from its 25 A continuous ceiling, so conservative builds leave it in place for monitoring even when both packs are stock-voltage.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L99469-L99516】

### Happy/Ninebot BMS Cutoff Expectations (Lines 99,579-99,592)
- When Happy- or Ninebot-managed packs refuse to charge near empty, the group pegs their shutdown window around 3.0–3.3 V per cell, so seeing 3.14 V on a stalled pack is normal protection—not a dead BMS—before recovery or reawakening steps.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L99579-L99592】

### New G30 Speed Mods Demand ST-Link Access (Lines 99,608-99,636)
- Unlocking late-production Ninebot Max G30s past ~32 km/h now requires an ST-Link flash because recent dashboards block OTA downgrades; owners without a Windows PC still need to source the programmer or borrow one to push XiaoDash firmware manually.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L99608-L99636】

### Kickstand Extensions on 10-Inch Rear Conversions (Lines 99,684-99,689)
- The extra alloy block supplied with 10-inch rear swingarm kits simply relocates the kickstand so the longer wheelbase can park level; clones without the bracket end up leaning dangerously until the spacer is bolted on.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L99684-L99689】

### Sourcing True 10-Inch Tires and Clearing Fender Rub (Lines 99,361-99,733 & 102,555-102,563)
- Cheap 10-inch casings often arrive out-of-round and unrideable—builders junk visibly lopsided tires rather than grinding rubber, opting for proven ULIP or PMT sets that seat correctly on 6.1-inch rims even if they cost more.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L99361-L99375】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L99715-L99733】
- Fitting quality 10-inch rubber on Xiaomi frames still needs clearance mods: swap the front mudguard bolt for a countersunk fastener, shim the guard upward a few millimeters, and brace the rear fender to stop it from striking the tire on rough roads.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L102555-L102563】

### Vetting Suspension Swaps on Clone Frames (Lines 99,733-99,776 & 102,550-102,563)
- Clone scooters that already pack budget shocks can’t simply stack a Konyk or other rear kit on top—measure eye-to-eye lengths, expect geometry changes, and reinforce mounts because cheap dual-shock combos ride harsh, add leverage, and can fail at speed without proper hardware.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L99733-L99776】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L102550-L102563】

### Ordering Denis’ 48 V Internal Kits for the Pro 2 (Lines 99,777-99,809)
- Pro 2 owners chasing 48 V speed gains (about 1.5× stock) must order Denis’ 44 V Pro set and note at checkout that they need the 48 V version; the smaller generic 48 V pack fits but wastes space and needs custom padding, so it’s rarely worth replacing a healthy OEM battery.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L99777-L99795】

### Monorim External Packs Arrive Half-Baked (Lines 99,800-99,811)
- Mirono and Denis warn that Monorim’s 48 V pack ships without brake or BMS harnesses, forcing owners to fabricate missing leads; Denis attributes it to poor engineering rather than an intentional upsell and suggests avoiding the pack entirely.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L99799-L99811】

### External Pack Racks and Weatherproofing (Lines 99,839-99,856)
- Riders strapping external batteries to rear suspensions use the swingarm as a cargo rack, but the trade-off is losing folding ability; sealing every seam with silicone is the go-to method to keep the exposed pack weatherproof on long commutes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L99839-L99856】

### Regen Spikes Can Kill Reinforced Controllers (Lines 99,966-99,999)
- Even “reinforced” Xiaomi controllers with 85 V MOSFETs and 60 V capacitors can short after panic e-braking with high-voltage packs—the back-EMF spike blows the MOSFETs, so riders planning hard regen on 48 V builds should budget for upgraded controllers or disable aggressive electronic braking.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L99966-L99999】

### Hall Sensor Failures and Cooling Strategies (Lines 100,305-100,375 & 102,534-102,548)
- Repeated hard launches and braking on 48 V conversions cook hall sensors and high-kV aftermarket hubs within days; veterans recommend sourcing quality hall ICs (e.g., SS41F), adding ferrofluid/Statorade, lowering phase amps, or stepping up to physically larger or lower-kV motors to keep temps manageable.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L100305-L100375】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L102534-L102548】

### Parallel Pack Basics When Reusing Stock Batteries (Lines 101,708-101,717)
- Adding a spare Xiaomi pack externally is electrically simple—match voltages and tie them in parallel—but the real obstacle is packaging; without proper mounting room, builders usually shift to purpose-built external packs sold by Denis instead.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L101708-L101717】

### Rita Draws from the Higher-Voltage Pack First (Lines 101,707-101,728)
- Rita automatically favors whichever pack sits at the higher voltage before blending both, so there’s no way to force external-first discharge; equal 10S+10S combos still share load once voltages converge, and Denis discourages manual overrides to avoid cycling one pack unevenly.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L101707-L101728】

### Finding High-Current Bullet Connectors (Lines 101,695-101,722)
- Replacement Rita and battery bullets are standard “banana” connectors from AliExpress; opt for 5–5.5 mm sets when you need higher current capacity, and keep in mind the platform offers countless variants so double-check sizing before ordering.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L101695-L101722】

### Controller Mounting and Thermal Interface Must Stay Intact (Lines 101,755-101,764)
- Stock Xiaomi controllers rely on bolting flat against the chassis with thermal paste for heat dissipation; loose mounting screws or cable clutter that lifts the plate off the frame leads to rapid overheating on the first long ride and can pinch the brake line.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L101755-L101764】

### Tubeless Sealant Guidance for PMT-Style Tires (Lines 101,765-101,775)
- The latest PMT/Xuancheng-style tires ship with tubeless valves and seal fine without slime, but if riders insist on sealant they must choose formulas rated for aluminum rims—standard slime corrodes bare aluminum when run tubeless.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L101765-L101775】

### Beware AliExpress 48 V Bargains With Impossible Specs (Lines 114,472-114,485)
- Veterans told Tito to cancel a €60 AliExpress “48 V 62 Ah” pack and companion controller because the advertised capacity requires non-existent 21.3 Ah cells and bargain controllers rarely survive 48 V, turning those bundles into fire hazards rather than budget upgrades.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L114472-L114485】

### Configure XiaoDash Before Installing Denis’ 48 V Internal Pack (Lines 114,513-114,519)
- Denis’ 48 V Pro/Pro 2 battery expects XiaoDash’s BMS emulation slider set to 13 cells and the capacity slider at 20 Ah while leaving the remaining sliders untouched, otherwise the scooter stays locked to 36 V limits.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L114513-L114519】

### Hacking Ninebot G2s Without Controller Swaps (Lines 114,520-114,535)
- Swapping a G30 controller into a G2 is no longer mandatory—flash XiaoDash onto the stock G2 ESC, add the dashboard harness plus SHFW Gen 4 patch, and you keep blinkers and buzzer while raising the speed ceiling.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L114520-L114535】

### Treat Aftermarket ESCs Like Heat Sinks, Not Drop-In Bricks (Lines 114,560-114,577 & 115,432-115,503)
- Builders recommend grinding Xiaomi’s cast standoffs or bolting VESCs to a solid metal bottom plate with thermal paste so the case can wick heat; thin plates or sloppy thermal glue let 75100-style boards spike in seconds, so sealing the housing and maintaining proper contact is critical for reliability.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L114560-L114577】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L115432-L115503】

### Handle LiPo Packs Conservatively (Lines 115,837-115,845)
- Gabe and Mirono reminded commuters that RC LiPo bricks dislike sitting at full charge, develop high resistance, and can puff after only a few days if stored topped-off, making them poor everyday scooter batteries.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L115837-L115845】

### Winter Range Planning Needs Warm Batteries (Lines 115,861-115,870)
- Expect winter Wh/km to nearly double—Happy Giraffe now sees ~30 Wh/km in snow versus 18–20 Wh/km in summer and keeps packs warm indoors or adds gentle heaters to preserve performance on freezing commutes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L115861-L115872】

### Fitting 13S Packs Into Frame Bags Takes Real Estate (Lines 115,874-115,898)
- A 13S4P build barely fits a 3 L Wildman bag; riders reported better success with 2–2.5 L phone bags, self-tapping screws or aluminum strips for mounting, and cardboard liners to shield cells from fasteners.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L115874-L115898】

### Don’t Parallel Mixed Packs Through Rita (Lines 116,206-116,215)
- Denis cautioned that Rita only supports paralleling identical external packs without their own charge ports; tying a factory battery and a Litokala pack together through a Y-harness risks damaging Rita and both batteries.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L116206-L116215】

### Dial In PETG Print Temps for Scooter Hardware (Lines 116,230-116,236)
- Denis and Happy shared reliable PETG print settings—nozzle ≈230 °C with 100 °C first-layer bed (≈80 °C afterward), or 231 °C/101 °C/81 °C when printing on PEI—to produce durable mounts and enclosures.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L116230-L116236】

### 48 V Swaps Add Range and Pull on Identical Ah Packs (Lines 118,600-118,609)
- Upgrading from 36 V to 48 V at the same amp-hour rating increases total watt-hours and improves torque, so heavier riders can keep pace even when scooters are otherwise identical.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L118600-L118609】

### Budget Monorim Brake Adapters Likely Need Custom Fabrication (Lines 118,611-118,621)
- Monorim will not sell the rear caliper bracket separately for G30 suspensions; owners should expect to commission or machine their own spacer to clear the wider swingarm.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L118611-L118621】

### Diagnose Error 21 After Regen Events by Checking Data Lines (Lines 118,622-118,635)
- When a Mi 3 threw error 21 after an emergency stop, Denis suspected the regen spike cooked the controller’s data line; his fix path is to bench-test the pack with a known-good scooter or send it in for service rather than assume the Happy BMS failed.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L118622-L118635】

### Rita Disables Regen Until Both Packs Drop Below Full (Lines 118,642-118,646)
- Rita intentionally kills e-brake regen when an external pack is full—re-enable braking by discharging slightly and ensure Rita’s cell-count setting matches the battery (e.g., 12S) so it doesn’t stay disabled forever.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L118642-L118646】

### Charging Through Happy BMS XT30 Bypasses Overvoltage Protections (Lines 118,684-118,688)
- Happy BMS-equipped packs can be topped up via the XT30 controller lead in a pinch, but Denis warns that route lacks any overvoltage cutoff, so monitor voltage manually to avoid overcharging cells.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L118684-L118688】

### Declare and Certify Lithium Shipments or Risk Liability (Lines 119,042-119,143)
- Group consensus was to always ship batteries as declared hazmat—UPS will accept them when labeled, but James explained EU ADR/IATA rules still require proper certification, documentation, and often an external safety advisor, so undeclared packs can leave senders liable for six-figure damages if something burns.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L119042-L119143】

### Used Dual-Motor Bargains Still Need Controller Work—Consider Modding a G30 (Lines 119,205-119,360)
- Mechanics warned Jacob that midrange Dualtron, Vsett, and Zero scooters command high resale despite jerky, failure-prone stock controllers, while a modded Ninebot G30 or newer G2 with 13S/35 A firmware delivers 40–45 km/h sleeper performance that stays under police radar and retains robust frames.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L119205-L119360】

### Charging 12S Packs with a 13S Brick Is a Stopgap Only (Lines 101,776-101,787)
- Builders occasionally top up paired 12S packs using a 13S charger, relying on the BMS to cut off, yet veterans stress it lacks proper CC/CV control and should only be a one-off emergency tactic, not a routine charging method.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L101776-L101787】

### Matching Shock Lengths on Monorim and Dereza Front Ends (Lines 101,733-101,749)
- For balanced ride height, stick to 150 mm shocks on front SNSC/Monorim setups and move 150 mm units to the rear if you upgrade the front to 165 mm or Dereza hardware; shorter air shocks complicate pump access and leave the scooter nose-down.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L101732-L101749】

### Riding Technique to Manage Motor Heat (Lines 102,538-102,548)
- High-kV hubs heat fastest when they’re forced to climb slowly at full throttle; to protect them, take run-ups so the motor operates near 80 % of top speed on hills, avoid repeated throttle-brake bursts, add ferrofluid, and consider AWD to split the load.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L102538-L102548】

### VESC Upgrade Considerations for High-Power Builds (Lines 102,569-102,598)
- Riders eyeing VESC swaps rate Spintend’s Ubox higher than Flipsky thanks to its MOSFETs and cooling; early Ubox units benefit from upgraded thermal pads, and planners pairing 14S packs discussed pulling ~70 A with Samsung 30Q/40T cells while watching motor limits.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L102569-L102598】

### External Pack Swapping on Clone Scooters (Lines 94,820-94,873)
- Boris’ clone build can’t run Rita, so he routed 50 cm XT60 extensions from the deck to a Wildman 3 L stem bag and hot-swaps whole 10S packs rather than paralleling them; the setup keeps wiring outside for quick changes but demands per-pack charging and voltage checks before reconnecting.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L94820-L94873】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L94841-L94873】

### Series vs. Parallel Energy Planning (Lines 95,313-95,356)
- Jan reminded builders that range hinges on watt-hours (V×Ah), so two 10S3P packs wired as 20S3P or 10S6P yield similar capacity; higher series counts lower current draw and cable heating at speed, explaining why Sannio’s 20S conversion roughly doubled range over 10S with the same cells.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L95313-L95357】

### GD32 Xiaomi Controller Recovery Precautions (Lines 95,680-95,780)
- Newer Xiaomi ESCs ship with GD32 MCUs, requiring full-flash images meant for GD silicon; flashing STM firmware bricks them, so owners should secure ST-Link access, dump the board markings with magnification, and source GD-compatible images before attempting recovery.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L95680-L95780】

### Cheap Charge-Line Diodes in Monorim Packs (Lines 96,880-96,892)
- Monorim’s external pack uses a series diode on the charge lead—a low-cost safeguard against reversed polarity on common-port BMS units—even though it wastes voltage headroom, so builders often bypass it once they confirm correct wiring.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L96880-L96892】

### Diagnosing Burned Motors and Upgrade Paths (Lines 96,894-96,912)
- A screeching hub that had climbed steep hills at 33 A showed melted slot insulation, prompting recommendations to replace it outright with hall-sensored Blade 10 or Vsett 10+ hubs; sensorless options like Vsett 11+ won’t run on stock Xiaomi controllers without additional hall feedback.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L96894-L96912】

### Rita Standby Drain and Storage (Lines 97,264-97,268)
- Denis confirmed Rita draws a trickle even when the scooter is off, so parking for months can leave both packs near empty—BMS protection prevents damage, but owners should recharge to storage levels instead of leaving Rita connected indefinitely.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L97264-L97268】

### Cylindrical Cell Safety and Refurb Sources (Lines 97,241-97,259)
- Cylindrical cells can open-circuit internally when abused, whereas pouch cells need constant compression and are more likely to vent fire when overcharged; Denis pointed builders toward refurbished Samsung 35E/50E stock from NKON dated late 2021 as a reliable midlife option.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L97241-L97259】

### Risks of 3S Powercube Mods on Xiaomi 1S (Lines 97,446-97,458)
- Adding a 3S “powercube” to the 1S lifts pack voltage beyond 56 V, so regen spikes can kill the stock controller unless KERS is disabled and braking done mechanically; veterans instead advise modding the controller traces or stepping up to 15S packs with reinforced hardware.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L97446-L97459】

### Verifying Pack Capacity with the Stock Charger (Lines 98,595-98,598)
- To validate questionable replacement batteries, Denis suggested timing a full charge with the OEM brick—each hour on the 1.7 A charger adds roughly 1.7 Ah—so a genuine 12 Ah Pro 2 pack should need close to seven hours from empty.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L98595-L98598】

### Deck-Mounted Multi-Pack Setups Need Reinforcement (Lines 98,855-98,874)
- Boris strapped two 10S packs inside metal conduit along the deck to free backpack space, but others warned the exposed bundle is a “self-propelled bomb” unless the housing is mechanically protected and wired for permanent duty rather than quick swaps.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L98855-L98874】

### Suspension Trade-offs on Xiaomi Frames (Lines 99,000-99,017)
- Riders split on aftermarket suspension: some consider Monorim or Sharkset essential for comfort, while Denis refuses to run cheap forks after seeing failures that shear wheels at speed, underscoring the need for proven hardware and frequent inspections.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L99000-L99017】

### Undersized “1000 W” Hub Motors (Lines 99,055-99,074)
- Paolo dissected a so-called 1,600 W hub and found a narrow stator smaller than Ninebot’s, highlighting that many “1 kW” AliExpress motors rely on high resistance and marketing rather than true copper volume—making them poor candidates for high-power VESC builds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L99055-L99074】

### Citylion Range Kit Wiring Guidance (Lines 99,259-99,266)
- Denis advised new Citylion Rita users to skip the extra Y-junction harness and simply follow the manual; the stock charger should read ~42 V when both 10S packs are full, so a fast green light just means the fresh pack shipped charged.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L99259-L99266】

### Fitting 10-Inch Tires on 6.1-Inch Rims (Lines 99,284-99,353)
- Attempting to stretch 6″-wide tires over 6.1″ rims left Boris with off-center beads, valve interference, and fender rub; veterans recommended sourcing true 155 mm casings, grinding the fender lip down to ~2 mm, and avoiding mismatched tire sizes that demand rim machining.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L99284-L99353】

### High-Voltage Pack Planning and Frame Requirements (Lines 89,361-89,440)
- Builders targeting 20S daily setups and 30S testing noted that stacking 30-series packs really calls for an 11-inch frame to keep geometry safe, while 84 V/25 A tunes deliver ~70 km/h but should avoid regen altogether because Xiaomi controllers eventually fail under that voltage spike.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89361-L89420】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89576-L89578】
- The same chat reinforced that power demand climbs fast with speed from aero drag, so investing in aerodynamic tweaks or a windshield gives better returns than pushing fragile stock frames past triple-digit goals.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89361-L89420】

### External Battery Builds and Sourcing Notes (Lines 89,472-89,520)
- Mirono shared a 13S3P 48 V/15 Ah pack (LG M50T or Samsung 50E) that fits inside a Xiaomi deck with Denis’ extender, runs fine on BMS emulation to dodge Happy BMS costs, and relies on NKON for bulk cells; Denis countered that his Happy-equipped equivalent sells for €290, underscoring the labor margins DIY builders trade on.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89473-L89522】
- Spot-welding gear remains the gating tool: Mirono recommended Sunkko welders (~€300) for consistent nickel welding, while Denis highlighted presentation and sealing as the differentiators customers pay for.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89501-L89531】

### Controller and Rita Configuration Updates (Lines 89,603-90,183)
- Denis reminded owners to connect the boat battery before Rita so the adapter just “sees” an internal pack, and Mirono reiterated that Ninebot Max 14S conversions need the ADC resistor mod plus caution because 63 V caps leave no margin for regen spikes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89652-L89661】
- Rita’s recommended output is still 25 A continuous/30 A peak, and Mirono warned that 84 V builds should limit or disable e-brake because stock trace-cut controllers will eventually blow at those voltages even though the stock brake channel is rated around 35 A.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89576-L89578】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L90181-L90183】
- For 15S Xiaomi 1S boards, Mirono confirmed the classic “baguette” resistor-capacitor swap (or BMS emulation) is mandatory to keep ADC readings in range.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89493-L89500】

### Battery Housing Materials and Cooling Considerations (Lines 89,665-89,760)
- Community feedback on deck-mounted battery housings stressed using PETG (or better) instead of PLA because PLA softens when cells warm, and that bolting heavy packs through only four small screws overloads the plastic unless the base plate shares the load.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89665-L89693】
- Builders found fans ineffective without proper ducts; using solid heat spreaders tied into exterior airflow and sealing against moisture ingress delivers better thermal control for enclosed packs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89665-L89696】

### Suspension Reinforcement Lessons (Lines 89,842-90,140)
- Ulip/Konyk-style long rear shocks change leverage enough to crush Xiaomi decks; HeroDash advised sandwiching the frame with inner and outer steel plates, re-bending the deck without the battery, and replacing springs with lower-rate options sourced from suspension shops instead of trimming coils.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89952-L90077】
- Reinforcement should avoid ad-hoc weld blobs: bolting matched plates on both sides, checking that disc hardware clears adapters, and keeping thread-lock on upgraded fasteners prevents cracked housings and lost bolts after hard braking.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89987-L90118】

### Brake Upgrades and Hardware Fitment (Lines 89,887-90,112)
- Builders running 160 mm rotors noted that DOT4 hydraulic systems transformed lever feel—HeroDash’s dual XiaoDash at 25/25 A produced “abnormally strong” braking yet still required regular bolt checks because aggressive testing backed bolts out mid-ride.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89987-L90018】
- Custom rear-disc adapters must account for caliper clearance to avoid disc bolts striking the tire adapter; raising calipers with 160 mm rotors or machining thicker aluminum plates kept braking hardware clear on AWD and RWD conversions.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89952-L90012】

### Tire, Wheel, and Mounting Care (Lines 89,462-90,637)
- Riders replacing solid Monorim casings were encouraged to drill valve holes and jump to true 10×3 pneumatic or tubeless tires, because 9.5-inch solids ride harshly and even rust nearby fasteners after a few thousand salty kilometers.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89735-L89755】
- HeroDash’s tire-mounting playbook—dust rims and tubes with talc, pre-warm outer casings with a heat gun or hair dryer, and cinch them into the rim center with zip ties—helped owners seat stiff Xuancheng/PMT tires without levers; he also warned that vacuum-packed shipments deform casings, so stand them upright to avoid “egg” tires.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L90621-L90637】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L90909-L90921】
- Switching to low-profile M6 countersunk screws or trimming fork plastics clears 10-inch fronts on Xiaomi 1S/Pro decks, preventing fender rub after conversions.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L90615-L90634】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L93429-L93434】

### Charger Interfaces and New Tools (Lines 90,140-90,183 & 91,512-91,538)
- Mirono clarified wiring on Xiaomi controllers: “C-” is charger negative, “P-” handles discharge negative, and “B-” lands on pack negative—use the right pads when repurposing connectors for custom lighting or battery swaps.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L90142-L90150】
- Denis prototyped a splitter that lets the stock charger top up both the original 10S pack and an additional 3S speed module simultaneously through the scooter charge port, opening cleaner dual-pack charging without external brick swaps.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L91512-L91538】

### Air Travel and Pack Discharge Guidance (Lines 90,960-91,040)
- Pilots moving 24 Ah external packs by air drained them with incandescent lamps to satisfy airline “discharged” requirements, yet still needed to budget 70 km of riding to hit 30 %—highlighting how long big packs take to empty safely.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L90969-L91024】
- Group consensus warned that DIY-looking external packs invite scrutiny at security, so plan for proof of compliance or repack cells separately before flights.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L90969-L91040】

### Range Planning and Pack Capacity Benchmarks (Lines 91,124-91,240 & 93,440-93,478)
- Riders considering Denis’ 48 V/14 Ah kit sought real-world deltas; Denis pointed them to existing footage and reminded them that pack health drives perceived acceleration more than motor swaps when the stock 250 W hub is voltage-limited.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L91124-L91132】
- Denis also quantified that a Pro 2 paired with his 36 V 10 Ah external “boat” pack reliably returns ~50 km of usable range, while Sergey’s 10S3P/10S4P combos manage ~30 km before tapering, reinforcing that published OEM ranges rarely match reality.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L93450-L93458】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L93462-L93478】

### Parallel Pack Charging and Common-Port Debates (Lines 92,999-93,636)
- Diagnostics on a 42 V pack showing only 20 V at the BMS output pointed to protection mode—halved voltage simply means the BMS has cut through-paths until errors (often rail contacts) are fixed.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L92999-L93011】
- Extensive Q&A around common versus separate charge ports concluded that common-port externals can charge through the scooter safely (BMS handles cutoffs), while separate-port packs need their own charger or a rewired XT30 harness; either way, match voltages with a multimeter before re-paralleling and avoid constantly disconnecting packs to minimize equalization surges.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L93548-L93558】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L93604-L93636】

### Clone Dashboard Flashing Tips (Lines 93,680-93,705)
- Purple-case clone dashboards can be flashed safely at 3.3 V with an ST-Link—just wire SWDIO/SWCLK/GND/3V3 on the rear pads and use Camilo’s “purple” firmware branch, knowing the boards revert if the wrong BLE image is loaded.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L93680-L93705】

### Clone Scooter Battery Expansion Caveats (Lines 93,104-93,520)
- Owners of iScooter 1S clones learned Rita cannot be configured without Xiaomi firmware support, so parallel Y-cables remain the only realistic expansion path; equalize voltages before connecting, keep packs attached to avoid constant balancing surges, and recognize that cheap clones lack protective charge modes, making high-quality packs and wiring discipline critical.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L93104-L93308】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L93340-L93386】

### Field-Weakening Limits and Stock ESC Voltage Ceilings (Lines 86,739-86,784)
- Riders confirmed Gen 1 Xiaomi controllers only manage ~32 km/h even with field weakening, underscoring that the platform favors torque over high top speed.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86739-L86747】
- Builders stacking 2S packs in series with stock 10S batteries reported ~50 V peaks but warned 13S (54.6 V) easily blows Xiaomi ESCs unless heavily reinforced, so casual users should avoid “shitty cell” add-ons and stick to Rita-assisted builds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86751-L86785】

### Firmware Access for Locked Dashboards (Lines 86,786-86,799)
- Owners of DE-market Pro 2 scooters on BLE 1.55+ must downgrade with an ST-Link; clone controllers often spoof serials yet still refuse OTA flashes, and flashing new Xiaomi BMS firmware can permanently brick the board even if ST-Link is available.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86786-L86829】

### Water Intrusion Diagnostics and Controller Recovery (Lines 86,979-87,038)
- MOSFET error beeps (error 28) typically indicate a shorted high-side bridge; repeated wet/dry cycles leave pink moisture stickers and white corrosion, so technicians advise swapping the controller rather than chasing intermittent faults.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86979-L87007】
- Power resets and erratic battery readings almost always stem from oxidation under the white battery plug—clean with contact spray, dry thoroughly, and avoid relying on factory IP54 sealing if you ride in rain or floods.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L87008-L87031】

### Suspension Spacers and Frame Protection (Lines 87,046-87,066 & 87,606-87,647)
- Extreme Monorim spacer stacks (40–55 mm, 190/165 mm shocks) change the fork angle and can punch holes in the deck; veterans add 5 mm stainless plates or repurpose upper arms to keep long shocks off the frame and maintain safe geometry.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L87046-L87066】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L87640-L87647】

### Rita Configuration and Thermal Cutoffs (Lines 87,167-87,182 & 87,629-87,635)
- Rita throws error 39/100 °C when external packs aren’t configured—set series count and capacity in the app before paralleling 10S and 15S batteries, and observe the adapter’s 30 A discharge ceiling.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L87167-L87182】
- Default Rita/Happy BMS charge protection halts at 40 °C pack temperature and resumes near 35 °C, so let hot packs cool before expecting charge current to return.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L87629-L87635】

### Hardware Sourcing and Fastener Notes (Lines 87,201-87,203 & 87,318-87,333)
- Damaged Monorim star nuts can be replaced with paired standard bike star nuts driven in on a sacrificial bolt, and longer stem bolts help retain alignment after repeated rebuilds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L87201-L87203】
- DIY NeatDash-style auxiliary displays struggle with clone BLE boards; follow the published schematics (120–150 Ω resistors, correctly oriented diodes) and expect to upgrade to an ESP32/OLED solution once Mirono and nvram release their open-source design.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L88003-L88055】

### Happy BMS Current and Fuse Behavior (Lines 87,309-87,315)
- Denis reiterated Happy BMS sustains 44 A; it trips a second after exceeding that and its internal fuses pop around 60 A, so there’s no headroom for 50–60 A experiments without redundancy.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L87309-L87315】

### Solid Tire Trade-offs and Tubeless Preferences (Lines 87,317-87,533 & 87,499-87,575)
- Veterans cautioned that 9.5-inch solid tires are harsh and dangerous—swap to thicker pneumatic casings or tubeless conversions; Xuancheng slicks are acceptable for budget use, but PMT or Wanda P1069 casings grip better albeit at higher cost.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L87317-L87333】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L87502-L87533】
- Tubeless off-road tires stay flat-free when paired with sealant, but avoid single-component slime that corrodes rims; keep Xuancheng fronts until worn, then upgrade to true tubeless sets for better stability.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L87545-L87576】

### Battery Wrapping and Current Targets (Lines 87,806-87,820)
- Stock Xiaomi packs fit 120 mm heat-shrink tubing; Denis prefers 170 mm sleeves for Wildman bag builds, and he sets Xiaomi ESCs at 55 A phase/30 A battery current to stay within hardware limits.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L87806-L87820】

### Refurb Pack Risk Management (Lines 87,827-87,866)
- Secondhand cell builds that swing voltage wildly on a 2 A charger signal poor grouping—dismantle packs, capacity/IR-test each cell, regroup by mileage rather than measured Ah, and expect degraded cells to keep worsening even after balancing.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L87827-L87868】

### Parallel Pack Testing and Voltage Matching (Lines 87,925-87,970)
- When checking external-pack capacity, leave the internal battery connected and use a constant-current load; paralleling packs more than ~1 V apart slams the low pack with high current and risks BMS damage despite Xiaomi’s 30 A discharge limit.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L87925-L87970】

### Motor Overheat Repairs and RTV Reinsulation (Lines 88,714-88,777)
- Waterlogged Pro 2 hubs showed melted yellow slot liners and missing insulation; technicians recommended stripping the stator, resoldering phase joints, and recoating with neutral-cure RTV to prevent shorts that will otherwise kill MOSFETs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L88714-L88777】

### High-Speed Scooter Comparisons (Lines 88,839-88,947)
- Community consensus pegged Vsett 10+ (with mods) and GT2-class machines as sturdier high-speed options than Dualtrons, citing sealing, wobble, and suspension failures on expensive Dualtron builds; there’s effectively no “cheap” path to a reliable 60–70 km/h scooter.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L88839-L88947】

### Partial Charging and Mounting Accessories (Lines 88,507-88,515 & 88,909-88,915)
- Happy BMS accepts a 13S (54.6 V) charger on 14S packs—it simply finishes early until the proper charger arrives, so range is reduced but charging is safe.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L88507-L88508】
- Denis released updated Wildman 2 L/3 L battery mount STLs, enabling securely bolted bag packs instead of improvised foam blocks.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L88509-L88515】

### Brake Cable Housing Support (Lines 89,091-89,096)
- Secure the brake-housing run to the frame and trim excess length—every bit of housing flex eats lever travel and reduces braking force, so tie it down before chasing caliper adjustments.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89091-L89096】

### 3D-Printed Pack Mount Fatigue (Lines 89,197-89,202)
- Heavy 13S packs mounted on 3D-printed rear supports can crack near the rear bolt, immediately skewing group voltages; inspect printed brackets regularly or replace them with stronger materials before high-speed runs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89197-L89202】

### High-Voltage VESC Planning (Lines 89,284-89,335)
- Builders chasing 70–130 km/h targets swap in 50–60 mm Blade/VSETT-class motors with VESCs and 15–22S packs—22S adds acceleration more than top speed, while 20S remains a practical daily setup and 300 A VESC installs demand creative mounting and weatherproofing.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89284-L89335】

### Battery Insulation Debates and Pack Quality (Lines 76,791-76,998)
- Builders argued over relying on Kapton tape versus fish paper for pack insulation: Kapton’s water resistance and clean removal help in damp climates, but it offers little thermal shielding, so high-discharge packs still need sound thermal design and conservative current limits.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L76791-L76833】
- A 2020 Dualtron Ultra teardown revealed loose cell holders and nickel strips touching bare cans with no insulating barriers—spot welds and LG MH1 cells looked tidy, yet the missing isolation was flagged as a fire risk that should be corrected during service.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L76982-L76998】

### External Battery Mounting and Capacity Planning (Lines 77,134-77,156 & 78,354-78,370)
- Riders who lost externals at speed now bolt packs to Wildman bags with eight screw/wide-washer mounts, fiberglass cable sleeving, chair-foot padding, and internal foam so the battery can’t rattle, chafe on screw heads, or shift mid-ride.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L77134-L77155】
- Capacity experiments show a Wildman 3 L bag can swallow 13S5P or even 16S3P 21700 assemblies (with BMS) when holders are omitted, but adding spacers makes fitment difficult, so builders accept tight tolerances and custom supports.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L78354-L78370】

### Rita Current Limits, Charging, and Configuration (Lines 77,367-77,478 & 78,276-78,309 & 80,299-80,331)
- Denis reminded users that Rita silently trips around 30 A; if externals drop out, check the “battery serial number” field in m365tools for Rita fault codes rather than blaming speed, and keep current peaks below the adapter’s limit.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L77367-L77379】
- Mixing OEM packs through Rita still demands separate wall charging—charging through the discharge leads bypasses Xiaomi protection, so Denis suggests leaving Rita’s charge wires floating and charging external packs directly when voltages or max cell counts differ.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L77474-L77478】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L78276-L78293】
- Gen 1 adapters lack overcurrent protection and require cutting the red jumper for ≥13S use; Denis and Happy Giraffe caution to cap controller battery current at 30 A and ensure Rita’s series-count configuration matches the pack so state-of-charge and shutdown logic stay accurate.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L80299-L80309】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L80312-L80331】

### High-Voltage Controller Planning and Resistor Mods (Lines 78,738-78,754 & 80,299-80,331 & 80,944-81,004)
- Denis and Mirono reiterated that Xiaomi v1.4 controllers rarely survive 13S–14S operation without reinforcement; reputable workshops avoid Monorim-branded 48 V packs that omit data leads and instead supply balanced 36 V upgrades for reliable range gains.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L78738-L78754】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L78795-L78822】
- When chasing 14S/15S builds, V3.1 boards only need one resistor change in the voltage divider; replacing both skews ADC readings and can trigger brownouts near 25 % state of charge, so builders verify measurements with Xiaodash/BMS emulation before riding.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L80299-L80309】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L80944-L81005】

### Happy BMS Wiring and Commissioning (Lines 79,003-79,034 & 78,626-78,632 & 81,560-81,568)
- Sergey walked a 48 V builder through regrouping 39 cells into thirteen 3P blocks before tying them in series, pointing to the official Happy BMS documentation to avoid dangerous parallel/series mix-ups and to wire the balance leads correctly.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L79003-L79034】
- Happy BMS outputs stay off until a charger is first connected, so new installs that read pack voltage but no XT60 output simply need a quick wake-up charge before testing discharge paths.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L81560-L81568】

### Tubeless Tire Seating and Repair Lessons (Lines 81,739-81,835)
- Seating Xiaomi tubeless casings demands a high-airflow burst rather than extreme pressure—hand pumps stall at 105 psi, so riders lean on foot pumps or fuel-station compressors and even cinch ratchet straps around the tread to seal beads long enough to pop them into place.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L81739-L81819】
- Slime is still a stop-gap; veterans swap to easier-mounting Huancheng or thicker CST 2.5 tires (often with tubes) for long-term durability on rutted, icy roads.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L81823-L81846】

### CRC Fix and Slime Reaction Warning (Lines 81,862-81,882)
- Mixing CRC Fix foam with Slime sealant triggers a violent reaction that spews green foam, self-inflates the tire, and leaves residue—avoid combining the two inside tubeless builds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L81862-L81882】

### Rita-Limited Dual-Motor Planning (Lines 81,898-82,024)
- AWD Xiaomi builds need matching OEM hubs, dual controllers, and dual Ritas; each adapter still trips near 30 A, so splitting current between two motors effectively caps each at ~15 A, making a stronger single rear motor the more sensible upgrade.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L81898-L81992】
- Rather than buying pricey kits, builders grab authentic hubs on AliExpress, budget ~€100 for reinforced controllers, and accept that Rita’s battery-current limit—not pack voltage—is the bottleneck until the pack, firmware, and ESC all scale together.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L81933-L82030】

### XiaoDash Field Weakening Guidance (Lines 82,006-82,030 & 83,438-83,443)
- XiaoDash’s Speed Boost adds 6–7 km/h when paired with higher battery current (~27 A) but ScooterHacking Firmware lacks that feature, so serious tuners migrate to XiaoDash while keeping Rita below its 30 A ceiling.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L82006-L82031】
- Denis likens field weakening to adding a second propeller that counters back-EMF: the controller retimes PWM rather than raising voltage, clarifying why extra current is mandatory for faster motor winds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L83438-L83443】

### External Pack Balancing and Serial Conversions (Lines 83,730-83,766)
- Serial “speed” boosters must be charged separately—if the small pack dips below the internal battery it backfeeds through the negative pole and cooks cells, so most riders commission a proper 13 S internal upgrade plus modified stock controllers instead of juggling mismatched packs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L83730-L83766】

### Happy BMS Charging Troubleshooting (Lines 83,342-83,368)
- Happy BMS packs that refuse to charge usually see only 42 V from Xiaomi bricks; step up to ≥47 V CC/CV (or a true 48 V charger) because feeding less than pack voltage leaves the BMS idle even though discharge works.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L83342-L83370】

### Charger Port Wear, Wiring Upgrades, and Happy BMS Capacity Limits (Lines 85,591-85,630)
- A 3 A charger that scorched a Xiaomi charge jack turned out to have tired wiring rather than a faulty port—veteran techs suggest refreshing the short leads with heavier gauge (≈24 AWG for 3 A runs) and inspecting the socket for looseness once plastic melts.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L85591-L85607】
- Builders can pair a 35 A pack with Happy BMS hardware despite the adapter’s 32 A spec; the controller still limits output safely, but the coulomb counter saturates and will show 0 % while ~10 % energy remains near the bottom of the pack.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L85618-L85630】
- Rita-compatible BMS emulators continue to report “empty” around 3.4 V per cell even when cutoff is set near 2.7 V, so riders keep a manual voltage check or conservative range buffer when relying on emulation instead of a Xiaomi board.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86152-L86158】

### Pro/Pro2 Custom Internal Battery Release and Cabling (Lines 85,640-85,647)
- Denis announced the production-ready custom internal pack for Xiaomi Pro/Pro 2 models and noted that the heavy-gauge charge/discharge harness is hand-braided in-house, mirroring his earlier 36 V kits.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L85640-L85647】

### XiaoDash Recovery and Rita Charging Readouts (Lines 86,060-86,082)
- A Mi 3 running Denis’ 48 V pack locked itself in a perpetual “on” state with flashing dash LEDs until the owner flashed stock firmware in XiaoDash, reactivated the scooter, and then re-applied the performance profile—suggesting recent XiaoDash updates can corrupt activation data and require a stock reset before upgrades stick.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86060-L86063】
- Rita adapters (Gen 1–Gen 5) hide the external battery indicator whenever a charger is attached, so lack of voltage telemetry while charging is expected and not a wiring fault.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86065-L86068】
- Unlocking the newest Pro 2 dashboards still demands either an ST-Link flash or temporarily swapping in an older dash to apply custom firmware; warranty seals aren’t a concern because the head unit simply unscrews for the swap.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86076-L86082】

### Motor, Tire, and Thermal Notes (Lines 77,156-77,156 & 77,058-77,087 & 81,226-81,259 & 83,387-83,395 & 86,220-86,245)
- A 10″ tubeless rider finally linked spontaneous pressure swings to thermal expansion: moving scooters from ~25 °C indoors to −3 °C streets self-deflates the casing, so cold-weather riders top up pressures before leaving warm garages.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L77156-L77159】
- High-phase builds lean on 11″ Boyueda 2800 W/60 H hubs driven by Kelly controllers at 200 + A for torque rather than peak speed (≈50 km/h without extra voltage), highlighting the need for temperature monitoring when overdriving big magnets.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L77058-L77087】
- A new Ninebot motor with integrated solid tire topped out near 39 km/h even on 15 S packs and delivered poor grip; riders immediately swapped to pneumatic tires or looked for higher-kV hubs when targeting 40 km/h builds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L81237-L81260】
- Monorim-branded motors drew criticism for steep pricing and mediocre output—builders instead favor PMT, Vsett, or Blade-spec hubs paired with reputable controllers rather than paying a premium for Monorim’s badge.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L83387-L83395】
- Fan-and-hole controller “cooling” mods add water-ingress risk and do little without proper thermal pads; the deck already acts as a heatsink, so the safer path is insulating pads or a VESC swap rather than cutting vents.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86220-L86245】

### Controller Cooling Experiments and Waterproofing Risks (Lines 86,203-86,239)
- Enthusiasts who bolted PC fans under the deck reported little benefit and heavy pushback: without thermal pads to couple MOSFETs to the chassis, airflow just recirculates warm air while the cutouts invite water intrusion, shorting the controller or any LiPo-powered fan mods strapped nearby.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86203-L86239】
- Veterans instead rely on thick thermal pads, proper sealant, or full VESC swaps bolted to the frame for sustained 80 km/h builds, noting that the aluminum deck is already a substantial heatsink when left intact.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86219-L86239】

### PMT 10×3 Fitment and Alternatives (Lines 86,176-86,195 & 86,649-86,656)
- PMT 10×3 tires do not drop onto stock Pro 2 rims without machining roughly 2 mm from the rim sidewalls; riders either trim the green-highlighted bead seat or source wider Dualtron-style wheels to clear the carcass.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86176-L86195】
- Standard PMT 10×2.125 casings fit 6.1″ Xiaomi rims without modification, making them the easier upgrade when grip is the priority.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86649-L86656】

### Brake and Sensor Upgrades for High-Power Builds (Lines 86,670-86,676)
- Xtech hybrids struggle to slow 80 km/h Pro 2 conversions; builders step up to full hydraulic systems (Magura-class) and add dedicated brake sensors if they want regenerative braking without removing lever feel, accepting that bleeding and hose routing are part of the conversion.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86670-L86676】

### Firmware Serial Resets and Recovery (Lines 86,682-86,688)
- Recent ScooterHacking/XiaoDash flashes sometimes zero the serial number and odometer; technicians restore the serial via the DownG app and only resort to ST-Link reflashes if they need the lifetime mileage counter reinstated.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86682-L86688】

### Suspension Extensions and Ride Height Tricks (Lines 86,697-86,701)
- To level flipped-fork or aftermarket front suspensions, riders fabricate bolt extenders that lengthen the rear shock shaft and sometimes stack an auxiliary spring in series, raising the tail without over-compressing the stock spring.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86697-L86701】

### Field-Weakening Expectations for Legacy Motors (Lines 86,737-86,744)
- Even with field weakening enabled, first-generation Xiaomi motors plateau near 32 km/h on flat ground; later Pro 2 hubs remain the better choice when chasing higher top speed rather than sacrificing torque on the older windings.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86737-L86744】

### Kickstand Spacers, Printing, and Hardware (Lines 71,739-71,836 & 71,756-71,825)
- Riders sizing Essential kickstand spacers landed on ~6.5 cm height by stacking books under the stand first; taller 8–10 cm blocks make the scooter unstable and overload the bolts.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L71795-L71826】
- Happy Giraffe reminds builders that taller prints weaken the part and stresses the hardware, so they source longer M6/M8 fasteners (80 mm) or tap fresh threads instead of stacking washers—buying proper length screws beats risky drilling hacks.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L71810-L71825】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L72361-L72386】

### Rita External-Pack Handling, Connectors, and Fuse Service (Lines 71,832-71,856 & 72,495-72,505 & 72,388-72,392)
- Rita always charges the pack with the lower voltage first; with non-common-port externals you must either charge both packs separately or rewire for a common port because charging through the discharge leads bypasses the external BMS protection.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L71832-L71853】
- Latest Rita harnesses ship with XT60 discharge connectors, so builders planning new externals can match that plug without adapters.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L72388-L72392】
- Replacing Rita’s 30 A fuse requires a stout (≈65 W) iron and sticking with the original rating—overfusing to 40 A risks destroying the adapter’s internal circuitry during a fault.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L72495-L72505】

### Tubeless Tire Options and Sealants (Lines 85,961-85,997)
- When Xiaomi V3 tires are unavailable, riders reuse stock casings with tubeless valves plus automotive sealant, but they warn the rim isn’t meant to be airtight and may seep unless the sealant is refreshed frequently.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L85961-L85980】
- Tubeless-specific (yellow) Slime avoids aluminum corrosion, and some switch back to tubes after AliExpress tubeless skins leaked within months despite sealant treatments.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L85974-L85997】

### Firmware Recovery and Activation Fixes (Lines 85,960-86,068 & 86,392-86,431)
- Mi3 dashboards that wake themselves with flashing red bars recovered after flashing back to stock via XiaoDash, reactivating the scooter, and then reapplying the custom profile—activation is a must whenever the board behaves like an uninitialized unit.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86060-L86063】
- If XiaoDash suddenly hides external voltages, unplug the mains brick: Rita gen1–gen5 suppress external readings whenever a charger is attached, which can mimic a wiring fault.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86066-L86068】
- Persistent auto-boot loops after a 48 V swap often trace to water-corroded dashboards; scrub them with 99 % isopropanol, dry the power button thoroughly, and avoid folding a wet scooter to keep moisture away from the electronics.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86392-L86431】

### Battery Sourcing and Charging Limits (Lines 86,511-86,538)
- AliExpress “bargain” packs earn fire emojis because many are built from laptop pulls—riders would rather buy refurbished OEM batteries, cap Happy BMS builds around 53 V/40 A, and rely on external packs for range instead of forcing Rita beyond spec.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86511-L86546】
- Controller cooling is safer with insulating pads or quality thermal paste under the MOSFETs; cutting fan holes in the deck invites shorts and water damage without meaningful heat relief.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86545-L86558】

### Brake and Hydraulic Upgrade Advice (Lines 86,661-86,676)
- Riders outgrowing Xtech hybrids graduate to full hydraulic systems and, if they still want regenerative braking, add lever sensors or dedicated wiring; finish the swap with a proper bleed once hose lengths are finalized to avoid spongy levers.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86670-L86676】

### Serial Number Reset Workarounds (Lines 86,682-86,687)
- Firmware flashes that zero mileage and serials are reversible—restore the serial via the DownG app and, if odometer accuracy matters, refresh the motherboard over ST-Link; otherwise treat the reset as a cosmetic bug.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86682-L86687】

### Suspension Extension Trick (Lines 86,690-86,699)
- To clear larger motors on AliExpress fork kits, builders thread in a bolt extender and add a second spring in series so the rear shock rests mid-axle rather than at the eyelet, gaining ride height without replacing the whole assembly.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86690-L86699】

### PMT Fitment Notes (Lines 86,161-86,193 & 86,661-86,663)
- PMT 10×3 tires require machining ~2 mm from Xiaomi rim sidewalls (or adopting Dualtron rear rims) to seat properly, whereas PMT 10×2.125 rubber slips onto stock 6.1 rims with no grinding for riders chasing premium grip.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86176-L86193】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L86661-L86663】

### Rita Configuration Over USB-UART (Lines 85,951-85,954)
- While Android fixes roll out, Rita owners can wire a USB-UART converter to configure the adapter from a PC—Denis even sells the cable separately for builders who want guaranteed compatibility.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L85951-L85954】

### Happy BMS Charging Configuration and Cable Limits (Lines 71,879-71,905)
- Happy BMS units block chargers above 3 A by default; owners moving to 5 A bricks must raise the limit to 5.5 A in the Embedden BMS Tool app, and Denis notes the restriction exists to prevent overheated Xiaomi charge leads.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L71879-L71905】

### Daly and Happy BMS Balancing Behaviour (Lines 71,869-71,871 & 73,328-73,339)
- Daly boards only bleed cells above ~4.18 V, so slow chargers are needed to reach the balance window; otherwise a pack can stay imbalanced indefinitely.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L71869-L71870】
- Happy BMS uses MCU-controlled passive balancing that can trim cells at any state of charge, while cheap analog boards need a full charge, and even Happy BMS will slowly self-discharge stored packs (≈0.6 %/day) unless woken with a charger after long storage.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L73330-L73345】

### Rita Storage Draw and Winter Parking (Lines 73,343-73,355)
- Rita sleeps at roughly 2 mA, equating to ~0.6 % per day; Denis advises riders parking for months to leave packs near 60 % and simply spot-check monthly rather than disconnecting wiring.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L73343-L73355】

### Accessory Power and Lighting Quirks (Lines 72,487-72,494 & 72,490-72,494)
- KERS-fed regen current won’t harm a 36–40 V headlight tied directly to the external pack, but a faulty “purple” dashboard can sag throttle voltage when lights are on, effectively limiting speed until the dash is replaced.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L72487-L72494】

### Traction-Control Hazards on High-Power AWD Builds (Lines 71,980-72,046)
- Roscheeee’s VESC-based dual-motor G30 snapped expensive Tronic controllers when traction control cut rear-wheel power at full throttle on slick concrete, allegedly dumping 250 A back through the system; testers now disable TCS on high-power setups or risk catastrophic back-EMF spikes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L71980-L72013】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L72041-L72046】

### Dual-Motor Add-On Plans and Thermal Management (Lines 72,088-72,142)
- Veterans caution that running a second motor with its own battery/controller “on demand” crowds the deck, roasts controllers that lack cooling, removes the rear brake, and offers little efficiency—serious AWD builds demand matched motors, dedicated mounts, and dual controllers with proper heat sinking.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L72088-L72137】
- Monorim rear kits need longer axle nuts to avoid slicing motor leads; builders should confirm the hardware before riding.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L72140-L72144】

### Battery Case Service and CF Capacitor Failures (Lines 72,071-72,155 & 72,248-72,255)
- Opening Xiaomi packs means slicing sealant along both bottom lids, warming the glue, and hammering the module out of the aluminum shell; Denis notes imbalanced packs often trace back to degraded CF-series capacitors that need replacement after checking each for infinite resistance.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L72071-L72080】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L72248-L72255】

### Firmware, BMS Emulation, and High-S Voltage Debates (Lines 72,063-72,069 & 72,880-73,060)
- Without Rita, external packs need either a Xiaomi BMS transplant or Xiaodash-based BMS emulation; simple smart-BMS boards lack the data line Xiaomi controllers expect and will throw error 21.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L72063-L72069】
- Converting controllers for 13S–16S still sparks debate: Denis argues the STM32 ADC survives higher voltage via the stock 10 MΩ divider, while others insist swapping ~160 kΩ resistors prevents error 24 and protects inputs during BMS emulation; Xiaodash handles the firmware side without legacy RX/TX jumpers.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L72880-L72960】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L72430-L72441】

### Rita Charging Strategy and Temperature Sensors (Lines 72,989-73,005 & 73,775-73,797)
- Rita intentionally tops 12S externals around 49.2 V (~4.1 V/cell) to preserve regen headroom—raising the limit gains only ~1 km of range/speed while risking e-brake loss on descents.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L72989-L72993】
- Chronic split charging between internal and external packs often traces back to failed OEM temperature sensors that lock out the internal BMS; disconnect Rita and verify both sensors before blaming the adapter.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L73776-L73797】

### Battery Mixing, Chargers, and Connector Upgrades (Lines 73,038-73,095 & 74,369-74,396)
- Never parallel 48 V and 36 V packs directly—Rita is the only safe method—and equalize voltages before combining even matching packs to avoid huge inrush currents.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L73038-L73054】
- Using a 13S charger on a 12S pack only works if the BMS survives; Denis allows it for emergencies but stresses the fire risk if protection fails and suggests timers or unplugging early instead.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L73546-L73552】
- Builders swapping Xiaomi’s skinny JST charge plug for XT30/XT60 or XT90S anti-spark connectors verify they comfortably handle 5 A and provide easier phase wiring upgrades (4 mm bullets for motor phases).【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L72393-L72404】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L73760-L73773】

### Tire, Suspension, and Winter Riding Lessons (Lines 73,358-73,407 & 73,553-73,559)
- For snow, members favour 10×2 tubeless off-road tires (AliExpress SKU linked) or Amalibay 9.2″ treaded casings; studded DIY conversions need caution because protruding screws quickly damage thin scooter rubber on bare pavement.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L73358-L73390】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L73553-L73557】
- Cold-weather range loss comes from slowed cell chemistry, so expect lower top speeds and range once temperatures drop below freezing.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L73400-L73407】
- Monorim suspension hardware continues to loosen or chew through bearings; upgrading to 12.9-grade bolts, trimming overly long hardware, and watching for play prevents cable damage.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L72577-L72600】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L74217-L74222】

### Brake Maintenance and Component Quality (Lines 74,250-74,260)
- Shop owners report repeated piston corrosion and leaks on Xtech hybrid brakes—many now prefer full hydraulic setups (Magura) or quality mechanical calipers rather than relying on budget hybrids for high-speed builds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L74250-L74260】

### Battery Vendor Vetting and Pack Construction (Lines 73,461-73,505 & 73,463-73,472)
- Community members caution that inexpensive AliExpress packs vary wildly: Aerdu’s 10S units can offer honest capacity if well-potted, but lack of fish paper between series groups is a fire risk—serious builders still favour reputable cell suppliers like NKON and add insulation themselves.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L73461-L73501】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L73748-L73758】

### High-Power Motor Sourcing and Fork Requirements (Lines 66,754-66,820)
- Builders aiming for 72 V 1,000–1,500 W swaps lean on Paolo’s 1.2 kW+ hub motors and remind newcomers that the casing’s larger magnets reduce copper loss and raise torque/efficiency versus smaller stock hubs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L66754-L66777】
- Mirono cautions that these wide motors demand either inverted Monorim forks or moving the drive to the rear to clear 10″ rubber, so plan chassis work alongside the motor purchase.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L66757-L66760】

### Sealants, Deck Hardware, and Waterproofing Practices (Lines 66,922-66,945)
- Veteran modifiers dismiss Sikaflex for deck sealing and instead rely on PU50 marine-grade urethanes (Illbruck/Enfy) that cure even underwater, can be sanded, stay elastic, and survive years of exposure; neutral silicones remain the go-to for joints that must reopen later.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L66922-L66945】

### Custom Packs, Rita Safety, and Battery Quality (Lines 66,951-67,099)
- A Shenzhen-built 36 V 25 Ah front-pack used Samsung 50E2 21700 cells, but the crew warns to evaluate steering balance before committing heavy head-tube batteries.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L66951-L66957】
- Denis reiterates Rita cannot stand in for a BMS: external packs still need their own protection, fuses, and sound wiring or the adapter’s fuse will blow and Happy BMS will block output after detecting shorts.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L66967-L67021】
- Cheap “30 Ah” externals that collapse to 6 % under load are condemned as unsafe; a legitimate 10 Ah 36 V pack needs ~40 quality cells (~€70 in cells alone), and users are told not to repurpose OEM Xiaomi packs as externals unless they disconnect them for every charge.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L67071-L67099】

### Charging Diagnostics and Step-Up Setup (Lines 67,013-67,125)
- When Happy BMS blinks red after a hard brake, the crew isolates the controller, safely discharges the main capacitors on a non-conductive surface, and measures the power stage before reconnecting to avoid further shorts.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L67015-L67038】
- Denis’ recipe for taming DC step-up “chargers” is to set output voltage below pack voltage, connect, then slowly raise voltage until charge current hits ~1 A before dialing the current-limit pot—staying within CC/CV behavior avoids sparks and overheated LEDs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L67113-L67120】

### Parallel Charging, Connector Limits, and Happy BMS Current Handling (Lines 68,334-68,380 & 68,039-68,040)
- Xiaomi owners running dual packs should parallel the JST charge leads (two males into one female) so both BMS boards stay in balance control; leave the data ribbon on the internal pack only and expect the internal BMS to blink red until cells finish balancing before reconnection.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L68334-L68390】
- JST charge leads are comfortable around 3 A and the Happy BMS enforces a ~5 A ceiling anyway, so high-current charging requires beefier plugs, while discharge leads handling ≥40 A should be upgraded to XT60 or better because two-minute pulls are not “short bursts.”【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L68370-L68376】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L68038-L68040】

### Happy BMS and Firmware Tips (Lines 67,987-68,022)
- Scootermode 14 S conversions can throw error 24 on Happy BMS; flashing with a 10 S pack connected clears the fault, and riders must remember Xiaomi throttles ignore input until the wheel spins slightly after boot.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L67987-L68007】
- Mi Electric 3 dashboards locked by Mi Home need their BLE/UUID checked via Downg or Xiaodash firmware; without that handshaking, STLink work is wasted because stock firmware simply reboots.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L68012-L68022】

### High-Speed Tire and Brake Considerations (Lines 67,903-68,059)
- Roscheeee’s custom metal brake adapter supports 160–180 mm rotors with 10×2.5–10×3.0 or 110/65 tires, but he warns conventional brake fluid boils long before a glowing 700 °C rotor, so premium systems must be specced with realistic fade expectations.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L67894-L67919】
- High-speed testers swap CST/PMT tires frequently—hitting 80 km/h-plus quickly overheats stock rubber—while peers stress aramid riding gear because even durable PMTs have no official speed rating under rider load.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L68045-L68059】

### Motor Cooling, Waterproofing, and Range Planning (Lines 61,739-62,200)
- Winter headwinds and hills can double load, so the crew caps long rides around 600 W, keeps throttle near 80%, and uses ferrofluid (about 4-6 ml such as Statorade) plus cool ambient temps to manage heat on Xiaomi hubs during 30 km/h cruises.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L61746-L61793】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L61821-L61833】
- Happy Giraffe reiterates full waterproofing: silicone every cable pass-through, seal the deck screen, grease bearings, and sandwich 3D-printed spacers between silicone layers while keeping threads clean so the deck can be reopened later.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L61797-L61819】

### Battery Builds, BMS Limits, and Wiring Upgrades (Lines 62,040-62,576 & 63,329-63,332)
- Planning 48 V packs, the team suggests Samsung 40T 13S5P builds with 60 A BMS hardware (or 44 A smart BMS) and reminds riders to swap Xiaomi's XT30 for XT60 plus higher-gauge leads so the drivetrain can tolerate the extra current headroom.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L62040-L62076】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L62513-L62524】
- Denis confirms his BMS firmware stores capacity in a 16-bit signed field, limiting configuration to 32 Ah; balance current is ~30 mA and each battery can supply 32 A, so oversize packs simply read 0% while ~3 Ah remain.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L62057-L62078】
- Happy Giraffe warns that long AWG16 extensions add resistance—upgrade custom harnesses to AWG12 and avoid thin replacement motor cables that undercut the stock gauge.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L62519-L62524】
- Pro 2 owners chasing accuracy keep BMS firmware 126: newer stock firmware caps charge near 40.5 V instead of 42 V, so flashing 126 keeps full voltage and harmonizes capacity labels (12,400 vs. 12,800 mAh).【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L66329-L66333】

### Rita Configuration, Charging, and Safety (Lines 62,532-63,585 & 63,553-63,570 & 64,413-66,620)
- Denis reiterates how Rita shares load: it draws from the higher-voltage pack first, raises top speed proportional to voltage, extends range proportional to capacity, and should keep combined battery current under 30 A with firmware still checking errors—otherwise expect app readings to flatline or hardware to fail.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L62532-L62538】
- The manual-style warnings stress fundamentals: only use common-port externals, match charger voltage to the external pack, configure Rita's series counts for every battery you swap in, cut the red jumper and reinforce the ESC for 14S-15S builds, and expect e-brake limits for the first kilometre on freshly charged packs—especially with cheaper batteries.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L63553-L63570】
- Regen on a full battery still burns MOSFETs, so riders descending from hills limit charge to about 95-97%, disable aggressive KERS if needed, and keep Rita disconnected while diagnosing shorted controllers.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L64160-L64191】
- Charging quirks trace back to setup: Rita needs its series parameter set (e.g., 12S externals) to clear temperature icons and to charge higher-voltage packs, and faulty chargers show normal voltage with no load yet sag to ~40 V under charge, starving the external battery.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L66413-L66420】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L66558-L66560】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L66582-L66588】
- When reviving storage-drained packs, Denis still advises measuring every cell group before kick-starting through the discharge port so low groups don't get over-driven during recovery.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L2622-L2624】

### High-Power Motors, Firmware Tweaks, and Regen Limits (Lines 62,454-62,708 & 64,160-64,199 & 63,352-63,399)
- Izuna outlines high-kV swaps: a 1200 W (50 mm magnet) hub on a Flipsky 75100 VESC with 72 V pack already tops 75 km/h, while an 800 W (40 mm) variant on a 12-mosfet Xiaomi ESC and 60 V pack should reach ~65 km/h—field weakening and ample phase amps are mandatory to sustain those speeds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L62454-L62472】
- Mirono cautions VESC users not to yank 105 A from mid-grade cells; set proper voltage limits so sag doesn't trigger 2.5 V undervoltage faults, and tune firmware if mixing BMS hardware so regen cut-offs behave.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L62500-L62507】
- Dexter's Xiaogen experiments show that dropping the brake lever parameter to 32 can brick the ESC (flashing tail light, no drive); restoring higher values and keeping KERS currents reasonable fixes the issue and avoids stressing the stock battery.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L66335-L66399】

### Tires, Brakes, and Hardware Fitment (Lines 62,083-62,226 & 64,216-64,233 & 66,442-66,720)
- Johnny Player shredded a tubeless slick after five months of overpower abuse—far longer than Xuancheng tires—and notes 135 mm rotors devour cheap pads, so semi-metallic compounds are preferred.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L62083-L62088】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L62524-L62526】
- PMT/Hero 10″ tires transform handling with glue-like grip and more stability over bumps; Dkey sources them from Voltride and highlights their wider, rubber carcasses versus nylon clones, though they tilt riders harder in corners.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L64216-L64233】
- Beware off-brand 10″ tires: mislabelled casings that measure 152-155 mm won't seat on Xiaomi rims and produce miserable, bumpy rides, so the group reorders Xuancheng or other known-good tubes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L66442-L66475】
- Converting to Vsett-style 10″ tires requires shaving roughly 2 mm from the rim lip, and poorly trained technicians who splice motor leads outside the frame invite failures—proper installs route cables through the stem instead of heat-shrinking cut wires.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L66684-L66720】
- Half a 237 ml bottle of slime seals 10″ tires effectively; Hero reminds riders the small bottles are about 8 oz.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L62289-L62296】

### Maintenance, Troubleshooting, and Vendors (Lines 62,740-63,004 & 64,213-64,270)
- When a BMS shuts down after impacts, Denis insists the module stay inside the pack, group voltages be checked at the board, and the cut-off MOSFETs temporarily bypassed only for diagnostics via the Android tool—dangling the BMS outside invites shorts.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L62564-L62608】
- Riders praise Voltride for quick PMT deliveries, while Mirono keeps steering buyers toward Scootermode and Paolo's upgraded controllers or 50 mm motors instead of overpriced MaxMods offerings.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L64226-L64233】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L66589-L66597】

### Charger Mods, TL431 Tuning, and Heat Limits (Lines 41,739-42,100)
- Mihail pushed the stock Xiaomi brick to 14 S (57.5 V) by restacking the TL431 feedback resistors (two 33 kΩ plus 100 kΩ while sourcing a single 16 kΩ 0805) and immediately swapped the 63 V output capacitors for 100 V parts because the higher voltage leaves no margin; he plans to watch shunt value, thermal rise, and mains differences (220 V vs. 120 V) before trusting it overnight.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L41890-L41999】
- Sergey reminded modifiers that understanding the TL431 reference loop and mapping the regulator before swapping parts is essential, while others flagged the charger’s ~1.7–2 A transformer ceiling as another heat constraint for extended high-voltage sessions.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L41900-L41937】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L42055-L42063】

### Rita Jumpers, Fuse Repairs, and Charging Behavior (Lines 42,101-43,250)
- Denis confirmed Gen 1–2 Rita boards cannot self-limit catastrophic shorts: blown XT30 contacts or fuses must be replaced, and Gen 5 users can solder new surface-mount fuses onto the exposed pads after checking which link failed.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L42460-L42479】
- For 13 S packs on pre-Gen 5 hardware, riders must cut the pink jumper: leaving it intact caps the adapter at 12 S and risks an over-voltage detonation, whereas cutting it raises the clamp to ~71 V but requires a reinforced controller and <30 A battery current to stay reliable.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L42868-L42909】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L42881-L42897】
- Charging through Rita fills the internal pack before topping the external; expect external volts to lag until the 10 S pack hits ≈42 V, and note that Gen 1 voltage readouts wander a little even with the charger unplugged.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L43141-L43180】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L43225-L43237】
- Denis’ crew still coaches riders to store builds near 60 % state of charge for long breaks and to rely on the app’s automation once jumper and series counts are correct.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L43246-L43248】

### BMS Apps, Android 12 Workarounds, and Instrumentation (Lines 42,101-44,300)
- Android 12 blocks recent Rita/BMS packages, but sideloading v0.0.12 from APKPure restores connectivity; older tablets or Bluestacks are fallbacks if newer builds refuse to pair.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L42028-L42049】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L42863-L42873】
- Riders adding dash voltage monitors should parallel-solder into the XT60 leads rather than interrupt them—running full traction current through a tiny gauge display lead or switch causes sparks and destroys the accessory.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L44419-L44444】

### Charger Quality, Connectors, and External-Pack Logistics (Lines 42,101-44,100)
- Cheap “48 V” bricks from eBay lack documented CC/CV stages; the group steers buyers toward YZPOWER 13 S chargers (3 A max on stock ports) and insists on soldered, heat-shrunk connector swaps instead of taped splices or 4 A pushes through Xiaomi’s red JST.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L42790-L42825】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L42801-L42839】
- Using multiple 2 A chargers in parallel is viable if each lead is properly soldered, and riders chasing faster fills upgrade internal charge leads to XT30/GX12 hardware before exceeding 3 A through the scooter port.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L42869-L42879】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L42828-L42839】
- Rita happily parallels mismatched-capacity 10 S packs, but the adapter only links an external once its voltage matches the internal; plan on separate wall chargers or patience when mixing 36 V and 48 V packs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L43141-L43175】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L44065-L44069】

### Battery Sourcing, BMS Quality, and Pack Maintenance (Lines 42,101-44,300)
- Veterans continue to pan Monorim-branded batteries: listings hide cell types, some ship with reversed polarity, and Denis’ team directs EU riders toward Scootermode, VTA, or EtorroS packs instead.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L42944-L42950】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L44007-L44024】
- Daly-branded Bluetooth BMS boards now arrive as lower-quality SouthROL clones; builders either source verified originals, switch to ANT/JK units, or expect poor balancing and misreported cells.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L43578-L43607】
- EtorroS dissected a Kaabo Wolf 20 S pack and found undersized nickel, failing MJ1 groups, and collapsed parallel strings when owners crank controller P-settings—he now rebuilds three groups per pack and warns riders to leave P7 ≥ 5 and stop around 20 % state of charge to avoid repeat failures.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L44369-L44407】
- Keeping spent packs from sitting empty prevents BMS sleep issues: even “dead” Xiaomi batteries usually wake when a charger is connected normally, so avoid bypass-charging unless diagnostics prove the BMS is offline.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L42510-L42526】

### Motors, Tires, Brakes, and Suspension (Lines 42,101-44,300)
- Chasing 40 km/h on Rita builds still favors reputable 350 W hubs plus 12 S–13 S packs or 10″ tires; “Monorim 350 W” storefront motors are just high-kV AliExpress clones that sacrifice torque, and mixing 12 S rear with 10 S front drives causes drag regen on AWD setups.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L42105-L42137】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L43700-L43702】
- Front disc conversions on 500 W aftermarket hubs need the Monorim adapter plus XTech calipers, while Monorim’s own brake and suspension hardware regularly arrives mis-machined—expect to replace fasteners, add self-locking nuts, or skip the kit entirely after repeated bending failures.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L42529-L42537】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L43343-L43349】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L43661-L43683】
- Stock brake cables fit within 2 m if you lack rear suspension, and 10×3 tire upgrades still demand higher pressures plus solid braking before exploring faster firmware maps.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L44000-L44005】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L42105-L42135】


### External Batteries, Rita Limits, and Safety (Lines 15,001-16,500)
- Rita only links in an external pack when its voltage matches or exceeds the internal battery, so builders need to top externals before plugging them in.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L15001-L15002】
- The crew warns that the stock charge JST warms even at 2.5 A; pushing 4 A through it requires upgraded connectors or alternate charge leads despite aftermarket chargers advertising 4 A compatibility.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L15033-L15045】
- Denis reiterates that braking current above 30 A trips error 39 and can literally explode Rita because the higher-voltage pack takes the full load; he and Happy cap battery current around 28–30 A for reliability.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L15064-L15071】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L19229-L19235】
- BMS emulation demands a separate-port smart BMS on the external pack—common-port packs can spike the controller during regen and destroy it once Rita is removed.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L15075-L15086】
- When charging or powering the internal pack through the XT30, double-check charger health and polarity because the BMS will not stop a reversed connection.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L15110-L15119】
- Rita purposely delays external-pack engagement until after boot to dodge Xiaomi’s error 24 voltage check; that safeguard disappears if riders rely on a single external battery without the internal pack attached.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L16354-L16356】
- Florian’s disappearing external pack traced back to wiring issues—the solution was to re-seat connectors, keep leads separated, and inspect the external fuse when Rita drops a pack mid-ride.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L16353-L16374】
- Rita does not interfere with Xiaomi’s weak internal balancing routine, so equalizing a tired pack can still take weeks even with the adapter installed.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L16448-L16455】

### Battery Building, Cells, and Charging Practices (Lines 15,001-16,500)
- Denis confirms you can extend an internal pack by adding a 2S2P booster, but it must carry its own BMS and dedicated charge plug because it cannot be charged through the stock harness.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L15300-L15304】
- Soldering extra cells directly to the stock battery is only “safe” if you rebuild every parallel group; slapping an unprotected sub-pack across the terminals is not acceptable and still leaves you with awkward charging.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L15305-L15311】
- Recycled laptop cells are rejected for traction packs—use fresh high-discharge cells such as EVE INR18650-26V sourced from NKON or similar reputable vendors instead.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L15319-L15329】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L15824-L15838】
- The Rita BMS tool’s capacity fields are cosmetic; only the series configuration settings affect scooter behavior, so mis-entered amp-hours will not fix range anomalies.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L15330-L15335】
- Cheap handheld spot welders lack punch for EV packs—the crew suggests investing in a K-weld-class tool or expect weak welds—and notes that 21700 groups shed heat better than 18650 at similar capacity counts.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L15721-L15729】
- Serial booster packs stress their tiny BMS units: red-blinking dashboards and power cutouts at 25–30 A usually mean the booster’s BMS or cells are sagging, so the fix is higher-current hardware (60–100 A BMS, 25 A-rated cells) rather than firmware tweaks; never parallel packs of different voltages.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L15442-L15553】
- Inspect charge-port wiring before closing the deck: reversed leads or hasty silicone blobs can short the charger, set the port on fire, or falsely suggest water damage.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L16041-L16074】

### Troubleshooting, Repairs, and Fitment Notes (Lines 15,001-16,500)
- When external packs drop out under load, Denis walks riders through checking parallel voltages, redoing suspect welds, and temporarily bypassing the BMS to confirm it is the source—only then should you plan a replacement, because the BMS is trying to save a bad cell group (and your house).【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L15895-L15947】
- Error 21 after a rock strike usually means the controller’s tiny BMS resistor burnt: swap in an 0805 part around 100–150 Ω instead of leaving it shorted, because the part protects the data line.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L16009-L16019】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L16122-L16148】
- Pro 2 decks built after 2021 squeeze Rita—mount it lower to avoid crushing cables, expect the folding hinge to bind with a battery bag, and remember the display only reports 12 S pack voltage accurately while the 10 S internal will read high.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L16023-L16033】
- Random power cycling and stuck lights typically trace back to water in the controller or power button; tear the board down, dry it thoroughly (hair dryer, re-seating cables), and seal the deck before the next rain ride.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L15683-L15718】
- Cruise control glitches that appear after a Rita install are usually wiring-related—re-seat the display-to-controller harness and verify Rita’s tight packaging in the Essential before blaming firmware.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L16490-L16510】

### Motors, Accessories, and Security Upgrades (Lines 15,001-20,000)
- Rental-sourced 350 W hubs are prized drop-in upgrades, but the crew tempers expectations: 500 W Monorim fronts still need sane current limits and at least 48 V support before they deliver more torque than a well-tuned dual-350 W setup.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L15358-L15370】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L15987-L15990】
- Motor rewinds directly affect kV; pushing a 350 W shell with 250 W stator windings changes speed/torque, and any motor run past ~100 °C risks permanent damage—ferrofluid cooling only helps if you use purpose-made statorade rather than generic ferrofluid that can evaporate or ignite.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L16049-L16058】
- Dual-motor Xiaomi builds need two controllers/dashboards; Rita cannot manage AWD, so serious projects jump to dual VESCs (e.g., Spintend Ubox) or accept the stock single-motor limits.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L16530-L16583】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L19208-L19232】
- 12 V accessories such as horns draw meaningful current—budget 1–1.5 A and fuse the supply—and many riders pair a loud electronic horn with a polite bell for pedestrians.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L16530-L16550】
- Layered security beats single locks: combine quality U-locks with GPS trackers (preferably 9–90 V units fused below 1 A) and even Airtags, and expect to route tracker power from the controller’s 12 V rail if the device supports it.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L19914-L19955】

### Bearings, Motors, and Tire Upgrades (Lines 12,001-13,500)
- Johnny Player standardizes on 6001-2RS rear and 6002-2RS front bearings, noting mid-grade seals from SKF, Koyo, and ZVL run cleanly while bargain no-name bearings fail early.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12024-L12031】
- The crew warns that Monorim’s 500 W hub ships with fragile sensors, bolts, and solid tires; they prefer dual stock motors or well-matched 350 W high-kV hubs for AWD builds because those service easily and avoid the low-kV torque slump that overheats single-wheel 500 W swaps.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12060-L12083】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12904-L12935】
- Solid tires remain a failure point—Happy Giraffe calls them dangerous for motors, batteries, and riders—so the group continues to recommend pneumatic conversions for performance scooters.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12086-L12091】
- For 10″ upgrades, Xuancheng tires still balance ride comfort, ease of mounting, and price, but their tread wears quickly and unlabeled clones should be avoided despite lower cost.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12563-L12571】
- Riders chasing 50 km/h claims on “350 W” hubs often rely on dashboard miscalibration; even Xiaomi dashboards can be set to oversized wheel diameters, so GPS checks are essential when evaluating top speed.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12926-L12945】

### Battery, Controller Packaging, and Waterproofing
- Francois splits his 13S8P pack into equal internal/external halves because the Xiaomi frame cannot swallow the whole pack, and he keeps a dual VESC controller bolted to the deck as a heatsink—moving controllers into bags sacrifices cooling and theft resistance.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12164-L12199】
- Johnny and others advise leaving high-power controllers in the deck cavity: the enclosure already runs near the ground, provides the largest heat-spreading surface, and protects wiring better than stem- or bag-mounted experiments.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12204-L12225】
- Tec7 sealant can waterproof harness entries and external pack cases by curing into rubber, but installers must allow drying time, avoid trapping moisture, and be ready to cut and reapply sealant whenever they reopen the chassis.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12260-L12271】
- Rear light power can be rerouted from the controller by tapping battery negative and ESC-positive at fuse F1, eliminating the fragile stock lead that snakes through the internal pack while keeping wiring tidy.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12271-L12292】
- Battery-bag theft deterrents such as stainless cable ties or cages help but must be padded or heat-shrunk to avoid cutting the pack, and determined thieves with metal cutters can still defeat them—pipe clamps or custom cages add better delay.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12322-L12352】
- 3D-printed spacers need generous height: 46 mm shims suit some external cases, while internal 13S6P builds worked with ~27 mm and VESC conversions reported 30 mm to clear a 10S3P P42A pack with minimal sag.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12462-L12476】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12854-L12858】
- Converting Xiaomi charge ports to XT30 connectors demands weatherproof caps, sealant, and preferably an inline fuse, because exposed male XT30 pins can short if struck by debris or rain.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12760-L12795】

### Firmware, Electronics, and Monitoring
- The Pro dashboard will show both internal and external Rita-managed packs; Denis documents the behavior in the manual’s page 9 reference.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12200-L12203】
- When flashing an M365 for 12S packs, the crew sets the battery-voltage limit to 52 V and, when using BotoX smart BMS hardware, raises the ESC↔BMS baud rate to 76,800 for stable comms.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12441-L12445】
- Rita Gen 4 still requires cutting the pink jumper for 13S operation, and the adapter’s stock current-ramp setting offers little benefit above ~100 mA while Rita itself caps battery draw at ~25 A.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12451-L12458】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12509-L12512】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12613-L12615】
- Builders who want more than 25 A either switch to upgraded controllers or disable BMS comms in firmware; Denis stresses Rita cannot simply be left inline on the data cable while the pack feeds the ESC directly for higher current.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12627-L12633】
- Xiaomi ESCs without BMS emulation show 0 V when Rita is removed; alternatives include custom smart BMS units, firmware with ADC-resistor tweaks, or standalone handlebar voltmeters for pack monitoring.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12532-L12540】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12555-L12562】
- The rear light circuit only provides ~3 V at low current; tapping it for accessories will overheat regulator U3. Instead, riders grab pack voltage and feed accessories through a dedicated buck converter that powers up with the scooter.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12869-L12885】
- German-market dual brake levers simply parallel their sensors, but mixing analog outputs can backfeed current; adding diodes or factory harnesses prevents burning the ESC’s inputs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12871-L12879】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12926-L12950】

### BMS, Charging, and Component Quality
- Daly’s newer 30 A BMS revisions use MOSFETs that fail in series connections; builders stick to the 40 A models for dual-pack scooters until Daly resolves the downgrade.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12827-L12829】
- Lost battery bars on the M365 Pro usually mean the controller’s R43 data-line resistor (≈120 Ω) has burned; swapping it restores BMS communication.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12573-L12603】
- 52 V external packs nearly double stock voltage, so riders warn that reinforcing the controller and motor is mandatory before pairing them with Xiaomi drivetrains.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12604-L12612】
- The stock Xiaomi battery still delivers power and can be charged through its XT30 even with the data ribbon disconnected, making it a handy 36 V source for lighting mods.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13440-L13443】
- When repairing packs, replace weak cell groups entirely, spot-weld fresh nickel, and reseal with a non-conductive silicone—apps should be used to confirm balance after a few cycles.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13452-L13489】

### Suspension, Tires, and Ride Prep (Lines 13,501-15,000)
- For tubeless builds, the crew recommends PCB-safe 704 sealant (also sold as Liveall/Heinkel) from bike shops, AliExpress, or Kaufer, noting Loctite variants are pricier but effective when electronics need splash protection.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13506-L13514】
- Installing a 165 mm Monorim spring can bind steering unless riders remove the headlight prism and adapter; the stock 150 mm spring clears without interference.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13769-L13800】
- M365 owners squeeze 13S6P packs inside the deck by adding ~20 mm spacers, but the taller build reduces ground clearance and works best with 10″ tires; slime helps patch punctures, yet 2.5″ CST pneumatics remain the group’s durable, grippy choice even in rain compared with 8.5″ stock or honeycomb tires.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13627-L13646】
- Tubeless slicks worry veterans at 50 km/h because rim dents or poor sealing dump air instantly; they steer speed seekers toward 10×2.5″ CST or PMT V-pattern tires, and reserve tubeless setups for carefully sealed rims with slime that can survive jumps.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13911-L13990】
- Riders swapping to 300 W and 350 W motors report realistic top speeds around 34 km/h on 36 V, 45 km/h on 48 V, and roughly 40–41 km/h from Kenso 350 W hubs paired with dual 10 S packs—underscoring that motor kV, not marketing, determines gains.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13546-L13560】

### Batteries, BMS, and External Packs
- The Rita BMS tool remains Android-only; the Telegram crew circulates a debug APK because the Play Store build lags new Rita hardware.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13548-L13554】
- Rita does not “switch” packs—it drains the higher-voltage battery first, then shares load once both packs equalize, so aging 7 Ah externals that sag to internal voltage will hand control back to the stock pack; riders diagnose this with the BMS tool under load.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13583-L13588】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13605-L13608】
- Pro 12 Ah batteries plug into Xiaomi electronics once their aluminum shell is removed, but M365 frames require trimming and spacers; builders increasingly spec custom 10S3P or 21700 packs in the stock BMS housing or outsource the work when prices and fitment justify it.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13616-L13634】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13784-L13798】
- External mounting stays popular: Dejan straps a Pro 2 pack into a handlebar bag (even pairing two packs in parallel/series) while others caution about added mass and make sure clamps and axles can cope.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13699-L13731】
- Aerdu packs divide opinion—some owners praise their 12 Ah externals while others cite imbalance and safety concerns—so veterans recommend EU builders like Scootermode or Denis’s own packs despite higher prices and shipping.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13589-L13604】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13742-L13798】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14713-L14718】
- Rita error 39 flags battery current spikes above ~25 A; Denis advises limiting battery current to 28–30 A while leaving phase/braking currents stock to avoid frying the module or controller, especially when only a 36 V system is present.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14720-L14742】
- Hard braking on a full pack without the internal battery attached can dump regen into Rita and destroy it; the group stresses keeping the stock pack connected (or wiring packs in parallel) so the controller has a safe sink for recovery current.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14755-L14806】
- Scooters see steep shipping/price trade-offs—e.g., €150 for a fresh Pro 2 battery plus ~€25 shipping within the EU—so some riders simply buy a discounted Pro 2 scooter for the 12 Ah pack and updated frame.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13594-L13631】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14743-L14768】
- Balancing repaired packs is slow because Xiaomi BMS boards bleed at ~30 mA; techs either leave packs on charge overnight or top the low group directly with a bench supply while disconnecting the BMS for safety.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14889-L14922】
- M365/Pro BMS boards default to ~20 A discharge whenever data lines are unplugged or voltage checks are disabled; keeping BMS telemetry alive (or using a different pack) is essential for >20 A builds and for range-boost kit configuration via the M365 BMS Tool.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14891-L14999】

### Controllers, Firmware, and Electronics
- Paolo’s 15 S-ready ESC mod cuts the feed trace to U4 and strings diodes in series, so peers double-check dissipation (~3 W across 21 diodes) and plan to log NTC temps before declaring it production-ready.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13524-L13533】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13725-L13726】
- When STLink access locks up, Sergey walks builders through “connect under reset” by shorting capacitor C35 (MCU pin 7) to ground with tweezers or a temporary pushbutton before reconnecting and reflashing the ESC.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13880-L13910】
- Upgrading Xiaomi controllers still means swapping to beefier MOSFETs (IRFB4110 or NCEP85T14), adding thermal pads/paste, and reinforcing copper with solder and extra wire; Mirono logged 55 °C continuous on bolted MOSFETs while noting motors overheat before fortified controllers.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13812-L13820】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14090-L14110】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14300-L14335】
- JST PAP-0xV-S plugs match Xiaomi’s BMS, BLE, and hall connectors (3-, 4-, and 5-pin respectively), letting repairers source exact replacements instead of reusing brittle stock housings.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14074-L14078】
- The rear light rail only supplies ~3–5 V with tight current limiting, so aftermarket LED strips often glow dim; techs either align the lens properly or drive accessories from 5/12 V controller pins via a relay or buck converter.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14123-L14172】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14567-L14582】
- Denis’s public Ninebot MAX firmware (cfw.sh) advertises 95 km/h capability, but veterans mock the marketing and remind riders that protective gear is mandatory when pushing such extremes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14590-L14601】
- Field reports confirm that 500 W Monorim hubs with ferrofluid and pneumatic tires stay dramatically cooler than 350 W units on hilly commutes while hitting 48–50 km/h when fed ~2.2 kW, whereas cheap “1 kW” motors still suffer weak halls, low kV, and captive rims.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14335-L14338】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14223-L14233】
- Xiaomi KERS recovers little day-to-day energy—perhaps one extra kilometer over 50 km—but it saves brake pads; riders disable throttle-off regen in sport mode while keeping gentle recovery through the brake lever.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14364-L14421】

### Maintenance, Safety, and Shop Talk
- Lost suspension bolts should be replaced immediately and secured with a pea-sized dab of blue threadlocker; veterans inspect clamp hardware weekly and suit up with motorcycle armor, gloves, and Kevlar-lined pants to walk away from crashes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13652-L13680】
- Riders note local laws (e.g., a 50 km/h Pro 2 confiscated by police) and treat protective gear as insurance against fines and injuries.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13649-L13667】
- Thread repair options range from tapping up to M6 with self-cutting inserts/time-serts to installing rivet nuts—just avoid drilling into the deck battery and mind screw length.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14324-L14338】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14360-L14381】
- Lithium fires are self-sustaining; after watching pack videos, the group recommends safer chemistries like LiFePO₄ where possible and warns that water won’t extinguish a runaway pack.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14605-L14618】
- Soldering high-current leads demands ≥60 W irons, quality (rosin-core) solder, proper flux discipline, and practice on scrap to avoid melting insulation or leaving cold joints; builders share part numbers for heavy bullet/banana connectors when upgrading phase wires.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14819-L14864】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14807-L14833】

### Suspension, Gear, and Maintenance
- Riders rate Monorim suspension about 7/10 once an EXA air shock replaces the noisy stock spring; they advise skipping the “Super” kit until its weak aluminum fork issues are solved.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13387-L13399】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13413-L13438】
- Regular maintenance keeps Monorim hardware quiet: grease the pivots every ~30 hours, cycle the shock after long storage, and mist lithium spray on the small bearings to stop squeaks.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L13491-L13499】
- Happy Giraffe flagged a €100 IXON Murray moto jacket that blends into streetwear yet uses 600D Cordura with CE Level 2 armor, surviving an estimated 60–80 km/h slide—an accessible gear upgrade for higher-speed commuters.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L12477-L12507】

### Controller Voltage Upgrades & Thermal Management
- Riders confirmed Xiaomi V3 controllers run 13S packs without hardware swaps, noting SMD resistor and dual-capacitor mods are only needed when stretching toward 20S builds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L14-L209】
- For 13S builds, the group keeps stock capacitors but insists on replacing Kapton tape with 0.5 mm thermal pads so MOSFETs stay isolated while shedding heat efficiently.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L211-L223】
- Direct-soldering motor phase leads to the controller stubs (instead of chaining adapters) minimizes resistive losses and connector overheating on higher-current tunes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L283-L291】

### Rita Configuration, External Packs, and BMS Practices (Lines 20,001-22,000)
- Denis’ app remains mandatory whenever riders swap Rita between 10S and 12S externals; leaving the configuration at the wrong nominal voltage confuses the controller even if the scooter boots.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L20045-L20058】
- Legacy “reinforced” Rita batches could pass 40 A battery / 100 A phase, but Denis no longer sells them—current production still limits most users to ~25 A, so high-power builds need other hardware.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L20064-L20084】
- The new Rita MAX for Ninebot G30 enters early access with a 30 A ceiling and model-specific connectors, expanding official support beyond Xiaomi frames.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L20725-L20748】
- Troubleshooting a dead external pack starts with isolating Rita: Denis tells riders to connect one battery at a time and check for the module’s red LED before chasing blown fuses or wiring faults.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L20820-L20829】
- Rita only emulates Xiaomi’s data lines; it does not balance cells or replace a BMS, so builders still need healthy pack-side protection and should treat any Daly/Aerdu faults as battery issues first.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L21281-L21303】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L21378-L21419】

### Charging, Logistics, and Wiring Notes (Lines 20,001-22,500)
- Denis caps his smart BMS charge port at 3 A because firmware and the Schottky path overheat above that, making upgraded connectors pointless without matching software limits.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L20830-L20835】
- Shipping lithium packs across borders remains fraught: customs X-ray parcels, shippers reject undeclared batteries, and Denis estimates Brexit wiped a quarter of his UK sales despite builders running informal ground couriers.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L20848-L20859】
- When paralleling two external packs, Francois stresses “marrying” them at identical voltages and leaving the XT-splitter in place; once paired, common-port BMS units are preferred so Rita can manage charge sensing cleanly.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L21452-L21458】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L21491-L21498】

### Battery Behavior, Diagnostics, and Cell Construction (Lines 20,001-22,500)
- Community veterans remind newcomers that current draw is constrained by cell voltage sag and internal resistance, so partially charged packs can still hit their amp limits until V-drop forces power sharing or thermal cutbacks.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L21342-L21377】
- Daly 10S BMS units may fail to balance after a week; the fix is replacement rather than expecting Rita to guard the pack, and builders should verify balance-lead pinouts when swapping hardware.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L21378-L21399】
- Paolo’s 20S10P high-power builds rely on copper-sandwiched bus bars and premium Murata cells, yet even he concedes that without robust fusing and monitoring an ESC fault can short the pack and ignite the scooter.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L21125-L21145】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L21188-L21205】

### Motors, Controllers, and High-Voltage Ambitions (Lines 20,001-23,000)
- Monorim’s 500 W hub still needs reinforced controllers and pneumatic tires; simply bumping wattage doesn’t buy speed, and riders chasing 60 km/h are urged toward purpose-built Vsett/Yume/Dualtron platforms.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L20004-L20058】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L20564-L20599】
- Spintend VESCs satisfy most Xiaomi conversions around 50 A battery / 120 A phase, but Paolo notes they cannot sustain the 100 A continuous outputs needed for Rion-class 20S builds without heavier-duty controllers such as Flipsky 75200 or Nucular units.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L21087-L21145】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L21178-L21205】
- Rita-equipped scooters should stay at ≤15S even when pairing with 100 V-capable ESCs; Denis’ crew rejects 16S plans as excessive for the adapter’s safeguards.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L21441-L21446】
- Blade 10 and other aftermarket motors are available via AliExpress, but buyers must confirm axle width, order proper spacers, and expect long lead times amid MOSFET shortages.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L20085-L20087】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L21338-L21340】

### Frames, Fitment, and Brake Upgrades (Lines 20,001-23,500)
- Rental G30 frames weigh ~10 kg more and use thicker stems; swapping motors or poles often means drilling, sourcing longer nuts, and accepting high OEM part prices that rival complete scooters.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L20600-L20638】
- Converting Xiaomi rears to driven hubs requires drilling the dropout, fitting adapter plates, longer reach nuts, and thread-locking everything—the process is effectively irreversible once the axle slot is enlarged.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L20669-L20713】
- Riders pushing past 50 km/h deem a second hydraulic brake mandatory; cheap Monorim adapters flex, aluminium 135 mm rotors warp, and many are upgrading to 140 mm five-bolt discs or quality dual-caliper setups.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L21462-L21511】

### Tires, Lighting, and Accessory Power (Lines 20,001-23,500)
- The group runs 10×3 tires above labeled 45 psi for 100 kg riders without issue, but they caution that better braking and suspension are needed once speeds climb.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L21449-L21503】
- Many rewire lighting directly to the traction battery or replace USB lights with 18650-powered units, warning that “10 Ah” marketing claims and 3,000 lm ratings are usually inflated; beam pattern photos matter more than box specs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L21305-L21337】

### Firmware, Connectors, and Late-2021 Tips (Lines 22,500-25,000)
- Flashing the wrong CFW (e.g., Classic firmware on an Essential) kills speed display and sport mode after a 12S upgrade; reinstalling the correct XiaoGen build restores operation.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L20839-L20844】
- XiaoGen’s “police mode” simply toggles alternate speed limits via the power button once the new throttle algorithm is enabled, giving commuters a quick-compliance profile.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L24990-L24995】
- Stock MT60/MR60 motor plugs already handle Monorim current levels, so thick phase-wire swaps rarely fit through the axle; instead, builders focus on upgrading the ESC junction to 4 mm bullets and cleaning capacitor glue that can fracture legs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L24983-L25009】
- Pro 2 clone controllers from AliExpress can sap range with poor MOSFETs, and riders should be ready to reglue capacitors or step back to OEM boards when replacements run hotter than stock.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L24965-L24982】

### Tire, Wheel, and Pressure Practices
- Frequent rear flats traced back to running ~28 psi on soft Wanda tires; veterans recommend 36–50 psi, swapping to Xuancheng/CST casings, and bathing tubes/tires/rims in talc instead of oils during installation to prevent chafing.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L56-L104】
- When rotating 10 inch tires, riders orient the valve away from the footpath and rely on 9.37" wheel-size calibration in Xiaogen firmware to restore accurate speed readings.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L500-L512】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L809-L810】

### External Battery Safety & Rita Limits
- Proper Y-cables use two female battery inputs and a male controller lead, with both packs matched in voltage before connection; poorly crimped or unsoldered joints in moving bags have already shorted packs and scarred decks.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L531-L605】
- The crew warns against AliExpress “13.8 Ah” packs whose 10S2P layouts make the rating impossible, urging disputes and pointing to Samsung 22PM-based builds as a safer baseline.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L594-L607】
- Rita v4 supports up to 15S packs but still bottlenecks battery current around 25 A; higher-voltage combos need controller reinforcement, and mixing 15S externals with stock 10S internals offers little benefit.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L811-L848】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1063-L1111】
- Non-common-port externals may require bypassing Rita’s charge jack; otherwise the Xiaomi charger shows no animation even though pack voltage rises slowly.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L611-L629】

### Rita Charging, Regen, and AWD Diagnostics (Lines 10,501-12,000)
- Denis flagged Error 14 on a second dashboard that shares one battery between two controllers as a critical Rita failure—the module should block any inter-pack current flow—so builders should re-check polarity incidents or wiring before riding again.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L10541-L10598】
- When pairing a 12 S external pack with Rita, Denis reiterated that the custom firmware’s nominal voltage must stay at 51 V to keep charge limits aligned.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L10541-L10552】
- Dual-dash AWD harnesses need their battery grounds tied together while leaving the dashboards isolated; otherwise control signals misbehave once both throttles and brakes share a pack.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L10650-L10652】
- New Rita hardware adds wall-charger and KERS over-voltage protection, but Denis warned that gen 1–2 boards still rely solely on the internal BMS, and even on newer units a simultaneous BMS/Rita fault could dump full charger voltage into the pack—use higher-voltage charging only if 95 % state-of-charge is acceptable.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L11620-L11670】
- Relocating the Xiaomi charge port outside Rita is fine, yet installers must keep a three-way parallel splitter so Rita still senses charge mode; otherwise its protections won’t trigger.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L11671-L11676】
- Rita’s 25 A ceiling limits how much hill-climb torque a tiny boost pack can add—Mirono recommends either a dual-motor conversion or uprated controller before chasing sustained climbs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L11124-L11136】
- Controller thermal shutdowns that repeat every few minutes after a Rita upgrade typically trace to dried thermal compound; Denis told riders to replace paste (not pads) and monitor temperatures before the next outing.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L11695-L11704】
- During charging, Rita isolates the external pack, so riders should watch the charger LED or Rita app voltages—the scooter’s dash will stay around 99 % until the auxiliary battery finishes balancing.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L11958-L11975】

### Motor, Controller, and Hill-Climb Planning (Lines 10,501-12,000)
- Riders pushing Xiaomi 1S scooters with 3 S booster packs found the controllers overheat and shut down on steep grades; veterans advise upgrading the entire battery/ESC/motor stack—or stepping up to a purpose-built climber—rather than chasing 350 W motor swaps that add little torque.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L10655-L10691】
- If you do move to a Monorim 500 W hub, plan on air-filled tires and refreshed phase connectors so the higher currents seat firmly; otherwise the hot leads will arc under load.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L10665-L10670】
- Fake “350 W” hubs from AliExpress routinely burn when fed 62 V packs, whereas reputable 350 W motors paired with 13S–20S controllers have survived years of use—reinforcing the value of vetted suppliers such as @paolo_vlc.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L11148-L11159】
- Mirono reminded AWD builders that kV matching matters more than watt labels: Xiaomi Pro 300 W and Monorim 500 W hubs spin at similar speeds, but the widely sold “Monorim 350 W” units in Moscow are just high-kV Ali clones unsuitable for balanced dual-motor builds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L11236-L11280】

### Battery Packaging, Security, and Charging Logistics (Lines 10,501-12,000)
- Handlebar battery pods don’t fit Xiaomi tubes (only nine cells max) and would be crushed in a crash; builders instead 3D-print deck drops, add rear racks, or keep packs at their feet—and they strongly discourage gambling on generic AliExpress batteries.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L10750-L10775】
- Ongoing complaints about Monorim-branded packs (snapped bolts, overstated capacities, messy wiring) underscore the need to source from safety-focused builders when mounting high-energy packs near the stem.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L10780-L10797】
- To deter theft, mount the Rita bag right-side-up with wiring tucked under the flap, then cinch the pack with two or three heavy pipe clamps or a custom cage so thieves can’t simply unzip it—goo-filling the bag only creates a mess when you need to remove the battery.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L11560-L11595】
- Using a stock Xiaomi pack as a charger for other batteries is a fire risk without a proper current limiter; instead, repurpose old packs as externals with their own BMS and charge them separately.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L11181-L11195】
- Denis’ Range + Speed kit lets both batteries charge from the bundled 50.4 V brick, but splitting them between chargers is faster, and the Rita app provides more accurate voltage readings than the scooter dash while charging.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L11958-L11975】

### Firmware, Tooling, and Flashing Tips (Lines 10,501-12,000)
- Riders still debate XiaoDash versus XiaoGen: XiaoDash sells inexpensive field-weakening presets and even advertises 20 S support, but XiaoGen’s cruise-control logic and migration tools remain more reliable for everyday commuting.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L11596-L11615】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L11600-L11610】
- Controllers already on DRV200 firmware need the m365_DownG XG Mod “intermediate” package before XiaoGen will flash again; once the clean base is installed you can reload premium configs and restore serial numbers via ScooterHacking Utility if they change.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L11734-L11855】
- Dot-style clone dashboards sometimes require removing both C16 and R1 jumpers for ST-Link to recognize the MCU—a wrinkle veterans hadn’t seen on earlier batches—after which the BLE rec flash succeeds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L11655-L11657】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L11926-L11933】

### Battery Construction and Spot-Welding Lessons (Lines 10,501-12,000)
- Builders critiqued cheap portable welders: running 52 J pulses with a soft 80 C LiPo scorched nickel and overheated leads, whereas shortening leads, solder-reinforcing traces, and pairing the welder with a high-discharge (≈180 C) pack at ≤30 J produced clean welds on 0.1–0.15 mm nickel without cooking MOSFETs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L11770-L11828】

### Maintenance, Tires, and Bearings (Lines 10,501-12,000)
- Heavy riders chasing stability don’t need water-filled tires—stick to ~5 bar on CST V3 casings or jump to 10″ Xuancheng/9×2 off-road tires for better winter grip, keeping in mind that higher pressures sap energy but protect rims.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L11437-L11475】
- Chronic speed loss on Rita builds often means the hub bearings have run dry; Johnny swaps Chinese bearings roughly every 2,000 km (sooner on solid tires) before heat and rattling balls destroy the motor.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L11975-L11989】

### Suspension, Brake, and Hardware Fitment
- Monorim V4 kits often arrive without the shim stack shown in Kroxne’s tutorial, forcing riders to add their own washers and highlighting ongoing tolerance issues between batches.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L800-L808】
- Thin M3 bolts in the Monorim V4 fender bracket shear easily; owners plan to swap in higher-grade hardware before the adapter loosens or brakes rub the rotor.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1198-L1203】

### Firmware & Speed Claims
- Xiaogen is praised as the “best” custom firmware, but veterans caution that borrowed configs can fake 42–44 km/h readings by abusing wheel multipliers; genuine >35 km/h pulls on stock 300 W motors still require higher voltage, FOC-capable ESCs, or rewound hubs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L809-L867】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1135-L1187】

### VESC Builds & Motor Selection
- KD estimates 17S VESC setups with dual Xiaomi Pro or Monorim motors top out near 60–70 km/h and stresses that VESC phase current hits harder than Xiaomi ESC figures, warranting aggressive motor cooling and, ideally, dual upgraded hubs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1283-L1296】
- Builders warn that “1000 W” Monorim hubs ship with undersized, non-gold connectors, flimsy tubeless tires, and no brake-disc support; Happy Giraffe recounts a 2 kW-induced wipeout and recommends avoiding the combo without major tire/brake changes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1290-L1303】
- Swapping a 1000 W hub into a Xiaomi requires Monorim suspension with a reversed fork to clear the larger rim and integrated 6-bolt rotor, reinforcing that the stock chassis lacks the space.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1321-L1325】
- G30 Max frames are noticeably wider than Xiaomi Pro decks, so cross-platform motor or deck swaps need custom spacers despite superficial similarities.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1445-L1450】

### ESC Thermal Management & Installation Checks
- Reapply quality thermal paste (about 4 g) between the M365 ESC and deck casting, replacing the stock yellow tape with a ≤1 mm non-conductive thermal pad and shimming the rubber puck so the controller sits flush without brake-cable interference.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1353-L1391】
- Clean old compound from both surfaces before installing the pad, verify the ESC cannot wiggle by hand, and reroute or slightly relieve the brake cable instead of grinding the chassis whenever possible.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1359-L1369】
- Happy Giraffe reports the thermal-pad swap let him sustain ~40 A battery current at comparable temps, though performance dropped after rework—underscoring careful reassembly.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1387-L1391】

### Soldering Prep & Capacitor Safety
- Before reinforcing traces, scrape conformal coatings, clean with solvent, and add solder only after discharging the controller capacitor by shorting the XT30 leads; leaving it charged causes sparks that can kill the ESC.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1464-L1487】
- Mirono and KD note discharged energy simply becomes heat and that even brief shorts are generally safe, but they caution against repeated sparks while working.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1474-L1488】

### Tire Choices for Monorim Builds
- Riders confirm air-filled tires fit the Monorim 500 W hub, recommending CST 10 × 2.5 or 10 × 3 casings to replace the stock hazardous tire before chasing higher power.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1303-L1305】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1441-L1443】

### Suspension & Wheel Fitment Updates (Lines 3,001-4,500)
- The Max-style Monorim V4 fork uses thinner mudguard brackets than the Xiaomi-specific V3, giving 10" tire builds more fender clearance when paired with the CNC “Max” hanger.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L3003-L3016】
- Xtech brakes sit higher than the stock clamp and can clear fat rotors on Monorim swingarms, but installers often have to file the caliper ears and still risk the housing touching the motor shell; oversized discs may leave pads working on <50 % of the surface.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L3331-L3351】
- Kroxne recommends keeping spare suspension hardware—folding pins, spacers, brake cables, pads, and even a V3 controller clone—on hand so breakdowns don’t strand riders while parts ship from AliExpress.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L3832-L3834】
- Monorim air-spring servicing is easier with two people: keep the fork suspended while holding the valve high, add pressure through the positive valve only, and bleed from the negative side after each adjustment, with light lithium spray on moving parts.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L4395-L4428】

### Brake, Suspension, and Cooling Updates (Lines 1,501-3,000)
- TRP Spyke mechanical brakes foul the Wheelway 500 W rim on Xiaomi Pro builds, so riders downsize the rear caliper and add metallic pads for dependable stopping without tire rub.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1501-L1504】
- Andreas outlined a liquid-cooling concept using twin MOSFET cold plates, a small radiator under the stem, and a temperature-triggered pump that only runs past ~30 °C to limit electrical load while riding.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1602-L1609】
- Owners traced burned Rita v4 photos to abusive firmware settings; veterans stress that even the charge leads can melt when current is pushed beyond design limits.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1618-L1627】
- Happy Giraffe still rates Xuancheng 10 inch tires best for stock rims but notes that 10×3 conversions demand spacer kits plus washers between the fork and hub to keep 500 W motors from rubbing.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1632-L1638】
- Kroxne reminds installers that Monorim fork brackets are secured by the axle and the spacer’s set screw; overtightening the outer bolts only strips threads without stopping the bracket from shifting.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L2986-L2996】

### Rita Operations, Charging, and BMS Emulation
- Newer Rita controllers still cap pack draw near 25 A; exceeding that limit throws an error 39 beeping sequence, so riders keep Xiaomi firmware battery limits at or below ~27–29 A peaks.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1683-L1692】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1767-L1770】
- Rita prioritizes the higher-voltage pack and only blends current once both batteries sag to the same level, so 12S externals can power the scooter even when the 10S stock pack is nearly empty.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1698-L1704】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1904-L1908】
- Denis cautions that fast-charging a 13S6P pack in one hour slashes lifespan; a 7.5 A charger strikes a healthier two-hour charge window while still doubling range versus stock 10 S energy.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1968-L1973】
- Stock Xiaomi charge ports and JST leads are only rated around 3 A, so higher-current charging requires upgraded connectors or direct-pack charging to avoid overheating.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1981-L1986】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L2697-L2700】
- Rita’s Schottky diodes drop roughly 0.6 V during charging, leaving packs slightly under 42 V; Denis recommends leaving the wiring as-is because that mild undercharge benefits battery longevity.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L2929-L2939】
- Riders report that XiaoFlasher’s built-in 13 S BMS emulator introduces throttle lag, whereas Rita’s emulation restores instant response when pairing large internal packs with the stock dashboard.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L2467-L2470】

### Charging, Rita Behavior, and Battery Planning (Lines 3,001-4,500)
- Denis confirms his “44.4 V” and “50.4 V” chargers are the same YZPower units, advising riders to resolder worn barrel plugs or reuse connectors from their stock chargers when the cords fail.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L3028-L3042】
- Rita’s series Schottky diode shaves a few tenths of a volt, so internal packs plateau near 97 %; riders either bypass Rita when charging the stock battery alone or accept the gentle undercharge for longevity.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L3045-L3063】
- The adapter’s status LED “heartbeat” blinks even with the scooter off, which Sergey notes is normal behavior documented in the manual.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L3703-L3710】
- Denis tells 48 V customers to cut Rita’s pink jumper and reinforce the controller before plugging higher-voltage externals; classic M365 owners still need trace, MOSFET, and wiring upgrades to tolerate 13S-plus packs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L3845-L3853】
- External-only riding without Rita triggers BMS communication errors and limp mode unless firmware voltage limits are raised and battery warnings suppressed—another reason the group prefers Rita’s dual-pack management.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L3966-L3998】
- Rita has two battery leads so both packs feed through its balancing and protection; stacking adapters is unnecessary and risks mismatched voltages.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L4000-L4006】
- New-generation Rita boards add current sensing that beeps and throttles output above ~25 A continuous (~30 A peaks), protecting users who previously “Miked” older units; Denis suggests 28 A battery limits when experimenting beyond spec.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L4251-L4274】
- Riders reiterate that extra voltage—not parallel 36 V packs—delivers speed gains: 36 V externals simply extend range, 12S setups need dedicated chargers, 14S suits 40 km/h goals, and 13S6P internals (~35–40 km/h) double range while staying within Rita’s charge split.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L3890-L3926】
- High-voltage ambitions require capacity: 15S packs under 4P sag excessively, cost €600–800 in quality cells, and should be paired with upgraded internals rather than stock 10S batteries.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L3896-L3904】

### Maintenance & Safety Notes (Lines 4,501-6,000)
- Flush Xiaomi discs with brake cleaner after wet rides—it is safe on pads and calipers—and periodically retorque or replace folding pins and other fasteners to avoid fatigue cracks or catastrophic rotor failures at speed.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L4509-L4575】
- Riders who swapped to full motorcycle armor and ditched solid tires report fewer crashes; the group brands solid rubber as a “death wish” once speeds climb past ~40 km/h because the carcass can unseat mid-ride.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L5530-L5539】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L5791-L5800】

### External Batteries & Charging (Lines 4,501-6,000)
- Configure Rita’s external-battery mode for 12S packs, cap firmware voltage near 51 V, and remember externals are hot-swappable only when stopped—yanking a 50 V pack mid-ride backfeeds the 42 V internal battery through the motor.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L4667-L4676】
- A 12S “speed” pack will not fit inside a Pro/Pro2 deck without lowering the floor; builders either mount 3S boosters or pursue custom 2S projects for stealth installs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L4677-L4699】
- Daly BMS units earn praise for reliability, but the crew still recommends common-port wiring on external packs and forbids charging 13S batteries through Rita’s onboard charge lead.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L5112-L5142】
- Stock charge ports and Rita’s intermediate connector stay happy below ~3 A; riders upgrade to 2.5 A YZPower chargers for quicker top-ups and splice in fresh barrel plugs when cords fatigue.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L5151-L5156】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L5495-L5498】
- Rita blends packs only when their voltages align, so a cheap €160 “10S4P” external that sags early leaves the internal battery doing all the work—test suspect packs alone at low load and expect legitimate packs with quality cells to cost more.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L5499-L5526】
- Dashboard state of charge becomes unreliable once Rita is installed; Denis advises treating 50 % on the display as the cue to head home.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L5653-L5658】
- Without Rita you must equalize voltages before paralleling an M365 spare battery with a Pro 2, whereas Rita lets you plug and play between scooters.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L5157-L5159】

### Controller & Firmware Guidance (Lines 4,501-6,000)
- Happy Giraffe’s XiaoGen flashing checklist keeps BLE stock, uses the XG Mod 21 flasher, and applies the migration file before loading custom firmware—ST-Link is the safety fallback if anything misbehaves.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L4604-L4610】
- XiaoDash’s experimental field-weakening toggles are labeled “dangerous”; veterans note they add idle speed but little road performance while risking controller damage.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L4718-L4726】
- M365 V2.1 controllers upgraded for 48 V still need the small C3A/B/C and C11 capacitors (plus the trio on the board’s back) changed; skipping them keeps temperatures high enough to threaten MOSFETs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L4888-L4912】
- Replacing the Kapton strip with a 0.5–1.0 mm thermal pad across the MOSFETs, adding paste, and ensuring the brake cable sits in its groove helps the ESC clamp flat against the deck casting.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L4918-L4918】
- Denis confirms regen can exceed acceleration current; set both drive and braking limits to ~27 A on Rita builds to avoid downhill thermal trips.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L5698-L5709】
- Smooth-throttle or quadratic power maps in custom firmware tame twitchy throttles after 12S/13S upgrades, minimizing jerk during deliveries.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L4972-L4974】

### Motors, Suspension & Fitment (Lines 4,501-6,000)
- 500 W Monorim hubs need suspension or adapters to clear a rear brake rotor, and they only deliver their rated output on 48 V; a well-cooled 350 W hub on 48 V still hits ~40 km/h while staying within comfort limits.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L4753-L4821】
- Generic front suspensions often bind; riders restore travel by polishing the inner cylinders, inserting a spacer between motor and fork to preserve alignment, and lubricating the sliders before reassembly.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L5665-L5669】
- G30 motors can be shoehorned into Monorim forks by flipping the arms, using longer bolts, and carving a cable channel, but the crew warns the stock hardware (axles, boots, fender brackets) snaps easily without higher-grade replacements.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L5873-L5995】
- Keep hall-sensor spares on hand—three-sensor rails for Xiaomi hubs are available via AliExpress and simplify future repairs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L4837-L4842】

### Battery Quality & Construction (Lines 4,501-6,000)
- Avoid bargain “brandless” 18650s and AliExpress packs; experienced builders buy from reputable suppliers, expect >€100 in cells even for tiny speed packs, and caution that cheap externals may be filled with sand or used cells.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L4738-L4746】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L5317-L5319】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L5499-L5526】
- Battery refurbishers stress testing every reclaimed cell individually and favor rigid cages or high-strength adhesives (e.g., Gorilla, Sikaflex) over bare Kapton for packs that must survive vibration.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L5190-L5207】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L5261-L5278】
- Bargain “Wish” scooters often hide their only value in the battery; the group repurposes those 13S packs but warns about the lack of spare parts and noisy drivetrains.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L5287-L5299】

### Troubleshooting Highlights (Lines 4,501-6,000)
- Persistent error 21 on Xiaomi scooters usually traces back to the XT30 battery connector or a BMS LED that has stopped blinking.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L4585-L4593】
- Error 18 after reassembly often means a damaged hall-sensor harness; swapping in a fresh cable cured the issue when two separate controllers threw the same fault.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L5827-L5832】
- Error 24 denotes supply voltage out of range—power-cycle the scooter for 10 seconds after checking battery wiring before digging deeper.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L5691-L5694】
- Denis reminds owners to keep Rita-fed externals within the manual’s 25 A continuous rating even if XiaoDash allows 32 A battery values; brief spikes are fine, but abuse still fries motors and controllers.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L3488-L3500】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L4267-L4295】

### Battery Planning and Purchasing Guidance
- Scootermode’s 13 S range-and-speed kit needs Xiaomi firmware voltage limits raised to ~55 V plus BMS emulation enabled; skipping the jumper wire on the harness or Rita causes error 21 until emulation is active.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L2395-L2401】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L2411-L2422】
- Denis equates a 13S6P pack of 2,500 mAh cells to roughly 20 Ah at 10S, letting riders roughly double Xiaomi Pro range while still charging within Rita’s 5 A shared limit by splitting across dedicated charge ports.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1968-L1990】
- Mirono flags Xiaoxiang “Smart Ant” BMS units as a reliable EU-source option when Daly doesn’t stock 12S Li-ion boards.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L2601-L2602】

### Firmware Flashing, Field Weakening, and Recovery
- XiaoGen flashing on Pro2/1S/Essential scooters requires keeping the original BLE, running the m365Downgrade XG Mod migrator once, then loading custom configs; future updates skip the migration package entirely to avoid bricks.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L1918-L1937】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L2095-L2115】
- ST-Link “target not found” errors usually trace back to wrong pin order or an unpowered controller, and flashing generic rec.bin images wipes odometer data until the serial number is restored manually.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L2563-L2571】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L2625-L2634】
- XiaoDash introduces paid “SpeedBoost” field weakening that mimics Ninebot’s magic serial trick; developers warn it boosts speed 35–40 % at the expense of range, heat, and demands for uprated batteries, MOSFETs, and cabling.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L2324-L2356】

### Firmware & Tooling Lessons (Lines 3,001-4,500)
- Multiple riders report XiaoDash beta builds quietly rewriting parameters and gutting torque, forcing half-hour recoveries; Denis advises sticking to XiaoFlasher presets until the new tool stabilizes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L3073-L3086】
- Sergey’s workflow for replacing controllers that ship with DRV200 locks is to enter the new serial, press “make FW,” flash with standard m365_DownG, power-cycle, and—if stuck—use Downg’s “repair SN” before regenerating XiaoGen firmware.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L3265-L3327】
- XiaoDash’s 20S BMS emulation is still “coming soon”; Denis is waiting on fresh PCBs before trusting it, while veterans warn that extreme 6S booster packs and 20S trace-cut builds routinely kill hardware despite the app’s promises.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L4064-L4088】
- Tire slip and braking issues often tie back to firmware choices—keeping tires at 50–60 psi restores the 40 km/h top speed targets riders chase with 12S tunes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L3211-L3236】

### Diagnostics and Component Repairs
- Lighting-triggered surging often stems from the dashboard’s F2 resettable fuse; techs either replace it with a 0 Ω link or confirm 5 V is stable under load before sourcing a new BLE board.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L2533-L2580】
- Persistent BMS error 21 on Ninebot Max-to-M365 conversions cleared once installers enabled battery-data emulation and correctly seated the control-harness jumper after waterproofing checks.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L2395-L2406】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L2427-L2436】
- Low output despite balanced cell groups often traces to failed sensing capacitors on Xiaomi BMS boards; Denis advises probing each RC network and replacing any capacitor that doesn’t mirror its cell voltage.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L2941-L2953】
- Water intrusion through the rear fender grommet can temporarily disable the pack; drying the battery for a week and jump-starting with the charger revived a soaked scooter without replacing the BMS.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L2989-L2994】

### Platform Compatibility Notes
- Tudor confirms 1,000 W hubs slot into Ninebot Max frames (with or without suspension) thanks to wider dropouts, whereas Xiaomi rears still lack clearance even when running Monorim shocks—front-only installs remain the practical Xiaomi option.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L2520-L2532】

### Maintenance, Tools, and Safety Extras (Lines 3,001-4,500)
- Sergey recommends pairing a 20–30 W temperature-controlled iron for PCB work with a ≥65 W unit for XT150-class connectors so joints flow quickly without cooking pads.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L3257-L3258】
- Riders source Statorade ferrofluid locally from Nexun in Poland and note that ferrofluid or oil only helps after addressing the stator-to-shell bottleneck with proper thermal pathways.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L3835-L3889】
- Denis is prototyping plug-and-play tracker/immobilizer modules with 5 V power supplies, fingerprint readers, and alarm speakers so scooters can sound off or cut power when moved without authorization.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L3665-L3670】
- Aftermarket Xtech brakes bite hard in the dry but rely on cheap seals that rust quickly in rain, so commuters should keep rebuild kits or spares ready for wet-weather riding.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L4233-L4243】
- Hidden trackers need their own low-dropout regulator: Sergey points riders to AMS1117-3.3 modules, fed directly from the main battery because Xiaomi controllers lack standby 5 V rails.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L4153-L4184】

### Suspension & Hardware Quality Control (Lines 6,001-7,500)
- Chao confirms Monorim’s MXR1 V2 rear revision adds brake-mount holes and a washer pocket after riders stripped the earlier axle clamp; until the new run arrives he advises hand-cutting the recess or sourcing spare parts from dual-suspension owners.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L6001-L6059】
- Installers flag the rear motor kit’s long nut and spacer as still too short for high-power hubs, recommending higher-grade hardware (12.9 bolts, longer shafts) to keep 500 W motors from tearing threads out of the aluminum swing arm.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L6037-L6047】

### Controller Cooling Experiments
- Abs’ dual-controller build clamps MOSFETs to a 3–4 mm aluminum bar with mica insulators and filtered 12 V push-pull fans, dropping case temps from 67 °C to ~40 °C during 60 A, 20 S runs; he suggests skipping the effort for mild 12–13 S tunes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L6167-L6188】
- Builders debating liquid loops conclude scooter vibration and cramped decks make sealed PC water kits risky; bolting MOSFETs directly to the frame or adding copper heat spreaders is the safer path.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L6175-L6192】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L6073-L6088】

### Rita Integration & Diagnostics Updates
- Denis notes Rita MAX (still unreleased) is the version that natively supports Ninebot Max voltage reporting; legacy Rita hardware lacks compatible plugs and data protocol without adapters.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L6232-L6251】
- AWD builders must run all three Rita data leads to a single “master” controller and forward only the white wire to the slave; tying both dashboards’ full harnesses together shorts the outputs and triggers BMS error 21.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L6433-L6456】
- Denis acknowledges a small Rita batch that under-reports current above 20 A—owners should cross-check against stock wiring, but overcurrent protection still trips in time thanks to redundant sensing tested on Ninebot Max builds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L6748-L6778】
- Modern Rita firmware drops the configurable regen cutoff but instead monitors output voltage continuously, shunting surges into a 25 W resistor and spoofing −10 °C on the temp sensor to raise error 39 until the issue clears.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L7450-L7463】

### Battery Vetting, BMS Wiring, and Charger Safety
- The group warns that bargain 4 Ah lawnmower packs are built for ~180 W draws and can overheat or ignite when asked for 25 A scooter peaks; riders should verify wattage before strapping tool batteries to Rita setups.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L6610-L6635】
- Adding a 3 S booster to Xiaomi packs is viable only with a reinforced controller; otherwise the combined 13 S voltage overstresses stock ESCs and still leaves the booster under-utilized because it never fully discharges.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L6928-L6940】
- DIY pack builders share a cautionary tale of mis-wired balance leads that instantly popped a Daly BMS, stressing the need to follow the printed diagram, wire negative first, confirm each cell step with a meter, and avoid doubling wires on one pad.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L7028-L7068】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L7132-L7135】
- LiFePO₄ BMS boards cannot safeguard li-ion cells because of different voltage windows; either return the part or build a dedicated 12 S LiFePO₄ pack instead.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L7080-L7089】
- When diagnosing jerky hubs, isolate the issue by spinning the wheel with motor leads disconnected (blown MOSFETs drag) and inspect hall wiring—error 18 often traces to damaged cables or sensors rather than the controller itself.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L6633-L6665】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L7437-L7443】

### Firmware & Controller Service Notes
- Cloned controllers shipped with spoofed DRV/BLE builds often need their serial re-entered in DownG before XiaoGen will flash; on Pro1 hardware you simply load the migrate package twice, while Pro2 units require the dedicated migrator first.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L6945-L7033】
- Never reconnect a trace-cut harness while the wheel is spinning—Mike’s test lit the U4 regulator on fire, underscoring the need to power down before rewiring high-voltage mods.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L6979-L6986】

### Brake & Tire Notes (Lines 6,001-7,500)
- X-Tech calipers paired with cheap 135 mm AliExpress rotors feel weak, but swapping to a quality 140 mm disc on Tudor’s custom rear hub transformed braking performance, showing hardware choice matters more than the caliper brand alone.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L6924-L6927】
- Larger 10×2.5 in tires typically require machining the hub or frame spacers—custom-suspension owners report needing a lathe to widen the rear assembly before off-road or CST casings will clear.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L6422-L6428】

### Rita Fitment & Voltage Expansion (Lines 7,501-9,000)
- Tight decks still swallow Rita Gen 4 if you stage the harnesses: route stem leads along the controller’s side, tuck power runs under the charge port, and use the Monorim stem slack before clamping the cover so the potted balance leads are not pinched.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L7534-L7566】
- The gray loop beside Rita’s LED is the surge jumper—leave it intact for 10‑12 S builds and cut it when pairing 13‑15 S packs; Denis’ crew confirms 13S4P packs just fit Wildman’s 2 L bag if you commit to the tight squeeze or a printed cage.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L7567-L7589】
- New Rita revisions add XT60 leads, 25 A current monitoring, and over-voltage charge protection, while 48 V users must snip the pink jumper by the status LED and reconfigure the app to stay within the adapter’s 25 A continuous ceiling.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L8226-L8339】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L8249-L8252】
- Rita intentionally undercharges internals by a few tenths to preserve regen headroom—expect the stock pack to hover near 41 V at rest, pulsating as the BMS cycles, and reduce controller current if the adapter raises error 39 during sustained >25 A pulls.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L7744-L7751】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L8327-L8338】

### Lighting, Dash, and Accessory Wiring
- Xiaomi tail-light leads supply ~5 V PWM with limited current; teeing in extra lamps with Dupont jumpers is fine for testing, but riders should upgrade to permanent connectors or 12 V buck converters when powering brighter accessories.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L8129-L8158】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L8283-L8289】
- Custom internal batteries simply pass the taillight’s positive pin to the ESC—tie the lamp’s red wire to the dash lead and the negative to pack ground, and expect XiaoDash to read the board as a Pro unless you flash Pro 2 firmware.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L8708-L8714】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L8211-L8213】

### Tire, Tube, and Cooling Takeaways
- Oversize 10 in CST casings on 155 mm rims demand 2–2.5 mm of machining for a safe bead seat—grind the rim, not the tire carcass, to avoid micro-cuts that later explode at speed.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L7528-L7533】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L7680-L7686】
- 10 × 2.5 in tubes need 45° or 90° stems plus talcum-powder dusting to prevent valve tearing, and expect front Xuancheng casings to wear faster than rears—many commuters budget replacements around 1,500 km.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L8179-L8205】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L8165-L8186】
- High current maps can mimic regenerative drag or buzzing motors; one rider cured the issue by backing XiaoGen battery current down from 28 A to 26 A, reinforcing that Rita’s 25 A ceiling and motor heating go hand in hand.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L8206-L8206】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L8327-L8338】
- Ferrofluid (Statorade) remains the go-to hub coolant, but veterans pair it with bearing upgrades (6002 ZVL2RS or branded SKF/Koyo) and throttle maps capped near 25,000 “motor power constant” for endurance instead of maxing XiaoGen at 32,000.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L8993-L9055】

### Firmware & Troubleshooting Notes (Lines 7,501-9,000)
- XiaoGen migration hiccups almost always trace to bad serials—Sergey’s prebuilt DRV zip restored flashing, after which riders could generate proper configs and keep the genuine controller ID in DownG.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L8111-L8123】
- Bricked Pro 2 batteries often revive after a 10-second BMS button press; if red LEDs persist, Denis asks for per-cell voltages before suggesting repairs, highlighting the need for a multimeter even when Rita is installed.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L8730-L8755】
- Tool batteries such as Makita BL1850B packs are poor externals: Rita waits for ~36 V before blending, so the scooter barely uses their small 5 S modules—sell them and invest in 10‑12 S scooter packs with Daly common-port BMS units instead.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L8873-L8893】
- When Monorim brakes wobble or hardware snaps, swap the soft OE screws for 12.9-grade fasteners, reface the caliper mounts, and expect to sand swingarm tabs so the disc sits square; failing to rebolt the short main pin bends stems within a few jumps.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L9250-L9290】

### Motor Thermal Management & Ferrofluid (Lines 9,001-10,500)
- Riders dial Xiaogen’s “motor power constant” down to ~25,000 instead of 32,000 when they need the same 45 km/h cruise without cooking 350 W hubs, pairing the milder tune with eco-mode use on long rides.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L9030-L9056】
- Denis’ crew only adds about a quarter bottle of ferrofluid per motor; they report it fills air gaps by the magnets, allowing identical speeds with less heat, but still caution that repeated full-power climbs can melt valve stems once you stop abruptly.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L9036-L9048】
- Veterans dismiss clip-on plastic “motor coolers” as gimmicks, stressing that steady airflow plus ferrofluid are the proven ways to move heat and that better testing shows the case can run warmer because it is finally pulling energy from the stator.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L9065-L9116】

### Battery Sourcing, DIY Builds & Warranty (Lines 9,001-10,500)
- Community members call quality AliExpress packs a lottery win—if you cannot vet cells, they suggest building your own pack with verified cells rather than trusting rewrapped claims, even if Aerdu’s customs can be “fine” for some riders.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L9158-L9179】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L9163-L9174】
- Spot-welding pros note that tools are only half the equation: you need a reliable cell supply, and if you do buy a welder, kWeld is the gold standard while cheap Sunkko-style rigs are barely adequate past 0.12 mm nickel without external power upgrades.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L9184-L9184】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L9981-L9999】
- Daly BMS owners confirmed the yellow lead is the protected charge negative and that the board must sit between the pack and both load/charger leads; wiring it incorrectly or ignoring the diagram is what fried earlier boards.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L9453-L9467】
- A poorly built Mirono external pack overheated its BMS and deformed the enclosure; the vendor blamed field-weakening amperage and now doubles the heatsinks, but the thread reinforced that hobby-level packs need proper wiring, MOSFET cooling, and warranty support when things melt.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L9645-L9651】
- Builders weighing new internals confirmed 21700 cells fit 15S4P inside Xiaomi Pro frames (16S4P is the realistic ceiling) and recommended high-discharge parts like Samsung 50E, 40T, Molicel P42A, or Sony VTC6A to limit sag on powerful tunes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L9655-L9676】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L9710-L9716】

### Hardware, Suspension & Fasteners (Lines 9,001-10,500)
- Stem wobble cases boiled down to loose latch nuts and bent hinge pins; tightening the adjuster or swapping the damaged pin restored rigidity after crashes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L9224-L9235】
- Monorim installers keep replacing the kit’s soft bolts with grade 12.9 hardware, sanding caliper brackets square, and trimming adapter bolts so Xtech calipers clear—echoing the consensus that the €130 kits ship with under-specced fasteners.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L9243-L9258】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L9482-L9488】
- Owners swapping in aftermarket forks or CNC bodies still expect machining tolerances to be off; even “upgraded” Monorim rear arms may arrive without the promised accessories, so community photos and hardware swaps remain essential.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L9473-L9493】

### Rita Usage & High-Voltage Experiments (Lines 9,001-10,500)
- Testers flirting with 60 V Rita builds were urged to monitor the adapter’s temperature alarms, verify BLE firmware, and stage soft launches before full-throttle pulls because Rita still enforces its own limits and noisy motors hint at bearing wear.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L9495-L9520】
- Rita’s fuel gauge stays trustworthy when both batteries share the same voltage; swapping to a bare Y-cable only sacrifices the adapter’s hot-swapping safety, so most riders keep Rita installed even if the dashboard sits at five bars for longer trips.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L10041-L10056】

### Travel, Shipping & Logistics (Lines 9,001-10,500)
- Air travel remains impractical for full-size packs—airlines cap carry-ons at 100 Wh, so veterans either ship scooters by land couriers that accept lithium (e.g., DPD, UPS) or simply buy/rent a local scooter instead of sneaking packs onto planes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L9717-L9758】
- Even road shipping carries fire risk if handlers toss boxes, reinforcing the need for protective cases and honest declarations when mailing high-voltage packs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L9752-L9757】

### Tire, Comfort & Tubeless Lessons (Lines 9,001-10,500)
- Commuters chasing comfort confirmed that 10" pneumatic tires paired with quality suspensions (Konyk, dual-air setups) tame harsh pavement far better than stock solids, while Monorim-branded solid tires stay a crash hazard even at moderate speeds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L10019-L10100】
- Tubeless conversions on powerful hubs remain finicky: riders reported persistent leaks, rim dents, and bead-seat woes, prompting many to return to talc-dusted tubes unless they can machine the rim for a proper fit.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L10283-L10309】
- When fitting oversized tires, measure rim diameters, warm the rubber, and use talc/soap plus longer tire irons to avoid tearing beads—stock Xiaomi/Ninebot rims rarely accept thick tubeless casings without machining.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L10283-L10295】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L10294-L10305】

### High-Voltage Builds, Wiring, and Motor Limits (Lines 25,001-26,300)
- Denis’s crew treats connector upgrades as mandatory once current rises: swap the stock motor plug for 4 mm bullets and replace long XT30 harnesses with AWG12 leads and XT60s to stop voltage sag on dual-motor or external-pack builds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L25001-L25046】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L25134-L25146】
- Real-world AWD data pegs dual Monorim or Blade motors at ~65 km/h on 10S and 70–72 km/h on series 10S packs drawing ~100 A, while single Blade hubs on 13S FOC hold ~55 km/h—underscoring that gearing, aerodynamics, and controller headroom gate speed more than raw voltage boosts.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L25013-L25040】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L26080-L26093】
- Builders warn that budget 500 W swaps run scorching at 75–95 A phase, whereas Blade hubs stay near hand-warm even at 120 A—so high-power projects need premium motors, wider forks, and serious brakes before chasing 60 km/h+ targets.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L26218-L26267】

### External Battery Packaging, Materials, and Cases (Lines 25,098-26,700)
- Denis confirms square 10S3P packs slip into 2 L Wildman bags while 10S4P requires honeycomb spacing; he specifies ≥8 mm, multi-path nickel links so each cell has its own series bridge when builders reuse OEM spacers.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L25098-L25127】
- Custom pack makers route balance leads along the pack underside, keep balancer harness lengths within ~50 % of each other, and solder power leads across the full nickel bus to equalize loading—tips Denis praises while urging rivals to trim excess wire.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L25462-L25488】
- Metal battery “bag” concepts remain in progress: Denis, Hero, and Rumi are prototyping rigid external cases while users explore riveted aluminum shells as theft-resistant alternatives to Wildman pouches.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L25213-L25227】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L25707-L25739】

### Firmware, Controls, and Diagnostics (Lines 25,955-26,200)
- XiaoGen flashing trips riders when battery telemetry is absent; the fix is to read the UID from DownG with a stock pack, rebuild the firmware, and reflash—after which single-tap mode changes can be restored by assigning the same action to every press profile in the generator.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L25841-L25932】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L26044-L26064】
- ST-Link recovery remains the fallback for stubborn dashboards, and riders lean on paid XiaoFlasher or XiaoGen builds when ScooterHacking’s generator throws “no binary detected” errors on newer Pro dashboards.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L25820-L25870】

### Suspension, Handling, and Portability Updates (Lines 25,508-26,320)
- Bearing pullers remain optional: penetrating oil, snap-ring removal, and hammering from the opposite side will free seized hub bearings when replacement is already planned.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L25508-L25559】
- Monorim’s front kit still divides the group—light springs or EXA/DNM air shocks help, yet its single-pivot geometry limits plushness and 165 mm units can fail early; Dereza/Konyk linkages promise better travel if they can clear wide axles and brake mounts.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L26224-L26241】
- Riders chasing portable AWD note Xiaomi frames creep toward 29 kg once dual batteries, locks, and beefy motors are installed, making stair carries arduous compared with stock Pros; many settle on stout RWD G30 conversions instead.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L26243-L26280】

### BMS Troubleshooting, Charging, and Safety (Lines 25,232-26,520)
- When Aerdu packs show zero volts on a series group, the crew pries apart the glued cells, diagnoses the dead parallel, and treats the unit as a 12S pack until rebuilt—reminding riders that bargain packs often hide weak welds and glued cases.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L25232-L25239】
- Custom BMS boards from AliExpress may “fall asleep” overnight; Mikko revived his by reflashing firmware, swapping failed 1001 Ω balance resistors, and verifying per-cell voltages before trusting the pack again.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L26345-L26380】
- Solid tires remain a last resort—veterans warn they are unsafe above 20 km/h and can trigger BMS faults or rim damage, so pneumatic upgrades stay the preferred fix for commuters.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L26358-L26383】
- Separate-port BMS units stay Rita-safe during regen but offer no protection while charging through discharge leads; riders either use the dedicated charge plug or accept the risk only when packs sit below full.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L25896-L25915】

### Electronics, Accessories, and Miscellaneous Notes (Lines 26,301-27,000)
- Arduino-driven VESC dashboards are becoming reality: Koxx demoed a Xiaomi running custom VESC firmware with an auxiliary microcontroller, reinforcing that open hardware can backfill missing Rita telemetry.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L26408-L26433】
- High-output LED strips can draw 10 A at 5 V (100 LED/m), so builders plan dedicated DC/DC converters with enable pins or switch to electroluminescent tapes to keep auxiliary lighting from overtaxing scooter rails.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L26130-L26149】
- Charger mods stay conservative: pairing 10S packs in parallel still uses a 42 V charger, while series 20S experiments demand hardware upgrades far beyond what Rita or stock ESCs can handle.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L26834-L26860】

### Winter Riding Comfort and Heated Controls (Lines 30,001-30,120)
- Riders weighing heated grips versus gloves noted that grip heaters are convenient for long rides because they pull from the scooter pack—there’s no separate battery to forget—while gloves stay useful off-scooter but add charging chores and wiring bulk.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L30028-L30075】

### Rita Diagnostics, External Packs, and Firmware Safeguards (Lines 30,427-30,520)
- Persistent 24 V readings on the external-pack telemetry pointed to adapter faults: the crew advised reseating harnesses, checking fuses, cross-connecting packs, and measuring with a voltmeter before concluding that a Rita board failed.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L30427-L30448】
- A 10S2P range pack could not absorb regen spikes and blew a Rita; Denis responded by reiterating that only larger packs (e.g., 10S4P) keep voltage in check and that the new Rita generation now disables both recuperation and electric braking when batteries are full to stop further explosions—although that also briefly softens braking feel at the start of downhill rides.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L30450-L30488】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L31438-L31440】
- Fifth-generation Rita hardware can tolerate 2P externals because of those safeguards, but Denis still encourages users to message him with failure details so he can audit orders and support cases.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L30469-L30499】

### Front Brake Fitment, Suspension, and Hardware (Lines 30,501-31,260)
- When adding a front disc to the Pro 2, the group emphasized learning modulation to avoid washing the steering wheel while still upgrading calipers, spacers, and suspension brackets so the hardware clears wider tires and heavier motors.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L30501-L30520】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L31234-L31288】
- Builders reinforce monorim and custom forks with thicker torque plates or stacked steel “sandwiches,” relocate shocks, and experiment with Nutt calipers and sintered pads to carve clearance for 10×3.0 tires on AWD builds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L31240-L31289】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L31450-L31459】

### Firmware Recovery, BLE Boards, and Tooling (Lines 31,308-31,440)
- Riders stuck on error 24 after swapping batteries found that Chinese BLE boards flashing “9.0.2” often refuse authentication; Sergey recommends swapping the board or reprogramming it with ST-Link, while others recovered by reconnecting the stock pack and pushing stock firmware through XiaoFlasher before reinstalling Rita.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L31396-L31429】

### Charging Hardware, Telemetry, and Connectors (Lines 32,016-32,118 & 33,933-34,038)
- For 13S builds fed through Xiaomi’s stock charge port, veterans cap current at ~3 A because RCA Type X leads and OEM wiring overheat above that; heavier builds either request custom plugs from charger vendors or switch to GX12 connectors.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L32016-L32043】
- Rita currently hides external-pack voltage while charging, so owners either unplug to read levels or add standalone displays until Denis’ planned firmware update restores telemetry.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L32118-L32118】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L33930-L33936】

### Battery Building, Cells, and BMS Guidance (Lines 33,019-33,604 & 33,471-33,499)
- Denis steers Ninebot owners toward 13S3P packs unless they run high-discharge cells like VTC6, reminds them to flash custom firmware for >10S packs, and cautions that charging both packs from a 13S charger through Rita is generally safe but still carries a slim multi-fault fire risk.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L33019-L33046】
- The crew validates NKON-sourced EVE and BAK cells for budget packs and warns that random AliExpress batteries or mystery LG 21700 bundles often underperform or arrive damaged, so reputable builders (Denis, Scootermode, Tudor) remain safer despite higher prices.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L30806-L30821】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L33371-L33398】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L34482-L34505】
- Sergey logged Xiaomi BMS MOSFET part numbers (MDE1932, HY4008) to guide repairs after overheats, highlighting that genuine boards use 120–200 A-rated devices rather than the 4 A components seen on cheap clones.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L33471-L33478】
- EtorroS revived a 16S pack with a week of 0.5 A manual top-balancing, tracking 35 Ah returned to confirm cell health, and noted that many scooter BMS units barely balance—making periodic manual balancing or cell replacements essential for longevity.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L33587-L33604】

### High-Power Wiring, Controllers, and AWD Experiments (Lines 32,960-33,060 & 33,560-34,040)
- When splitting 60–70 A batteries between dual controllers, builders stick with AWG10 feeders, XT90 mains, and MR60 phase connectors, tinning or heat-gunning joints from both sides to get solid solder wicks; Daly BMS ratings are treated as optimistic despite their apparent tolerance for brief 50 A loads.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L32960-L33016】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L33395-L33434】
- AWD projects lean on VESCs, Spintend Ubox, or Kelly controllers rather than Xiaomi ESCs—Rion’s dual 250 A controllers drew praise for sheer output, while builders debated enclosure cooling and stem strength on 16S–22S Ninebot conversions.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L33895-L33920】
- Stock Xiaomi controllers overheat quickly when pushed to ~99 °C with 16S packs and 500 W motors under heavy riders, so the consensus was to migrate to beefier hardware rather than bank on case mods alone.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L34027-L34038】

### Brake Upgrades, Wear, and Maintenance (Lines 33,965-34,205)
- Xtech calipers offer a cheap upgrade path but need seasonal flushes, struggle in wet or salty climates, and often leak or rust; veterans now jump straight to Shimano or Magura hydraulics, pairing them with separate e-brake levers or throttle-based regen triggers.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L33965-L34015】
- Riders combining hydraulic fronts with Xiaomi e-brake levers in the rear report stable 50 km/h commuting, while others bolt on Nutt calipers and brake-disc spacers to clear 80/65-6 tires without relying on loose stacks of washers.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L31450-L31459】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L33970-L34012】

### Tires, Tubes, and Ride Quality (Lines 33,054-33,133 & 34,520-34,560)
- CST 10×2.5 tires wear quickly under aggressive use, pushing commuters toward Tuovt or PMT casings with thicker nylon plies and better tread depth, though those stiffer tires demand more effort to mount.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L33054-L33078】
- For lumpy inner tubes that make wheels “egg-shaped,” experienced mechanics deflate, dust with talc, and repeatedly reseat the tube—usually restoring roundness without replacing hardware.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L34324-L34333】

### Rita Current Limits and Fuse Sizing (Lines 35,007-35,055)
- Riders clarified that Rita’s 30 A fuse does not cap battery output at 30 A; they still spec 40 A BMS boards for better thermal headroom and future power increases, while 29 A current maps keep 500 W swaps reliable.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L35007-L35022】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L35013-L35017】
- Happy Giraffe reiterated that Rita enforces ~25 A continuous and 30 A peak battery current regardless of the CFW generator, so riders should treat inflated “battery current” sliders as UI noise.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L35045-L35055】

### Connector Handling and High-Voltage Planning (Lines 35,097-35,182)
- Denis reminded builders to desolder pack nickel before pulling welded brackets to avoid tearing cell tabs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L35097-L35100】
- Veterans flagged that phase connectors often “weld” themselves after high-current use; always depower the pack, discharge the controller, and expect sparks from the controller capacitors when reconnecting to prevent BLE/ESC damage.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L35102-L35146】
- For AWD aspirations, the crew steered riders toward VESC/Mobipus-class controllers and warned that two stock Xiaomi packs in series lack the current for 72 V builds—20 S dual-motor conversions need purpose-built batteries instead.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L35164-L35182】

### Suspension, Tire Fitment, and Road Awareness (Lines 35,147-35,347 & 35,683-35,773)
- Adding a few drops of silicone oil through the Schrader valve transformed EXA air shocks for small-bump compliance; riders settled near 40 psi (≈2.8 bar) on the EXA 291 and swap between 150 lb and 650 lb springs to balance wobble control and comfort.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L35240-L35300】
- 10 in conversions on Xiaomi frames require fender spacers and the low-profile screw bundled with most kits; skipping the swap leaves the tire rubbing and mimics bearing failure until the countersunk fastener goes in.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L35683-L35776】
- Commuters trading road stories stressed reading traffic early, avoiding blind bike-lane entries, and wearing full protective gear once scooters sprint past 60 km/h in under seven seconds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L35327-L35355】

### Battery Builds, Recycled Packs, and Speed Targets (Lines 35,517-35,590)
- EtorroS rebuilt a budget Boyueda 16 S pack with Daly 60 A BMS hardware and noted the recycled “Tesla” 21700 cells sag sharply below 40 % state-of-charge and warm to ~30 °C at 80 A—good enough for 20 mi (32 km) but inferior to fresh Molicels.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L35531-L35557】
- His finished Ninebot Max conversion—Monorim suspension, 16 S 15 Ah pack, Daly 60 A BMS, and 500 W hub—holds 45 km/h under heavier riders and touches 50 km/h with lighter pilots, showing the practical ceiling for that setup.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L35570-L35578】
- Fabricators squeezing 13 S4 P packs into Xiaomi decks rely on 27 mm spacers and remote VESCs; the mod keeps room for controllers while unlocking 42–46 km/h on PMT 10 in tires.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L35517-L35522】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L35598-L35600】
- Mirono cataloged Kugoo 500 W rotor details (11 mm-wide, 35 mm-tall magnets, 2.5 mm thick) and confirmed hall sensors are easy, low-cost replacements—useful intel for builders swapping alternative hubs into Monorim forks.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L36374-L36395】

### Rita State-of-Charge Limits and Internal Battery Roadmap (Lines 36,180-36,236)
- Denis confirmed Rita’s charge gauge is voltage-based and cannot be user-calibrated; long WOT pulls will always force the percentage display low despite firmware filtering attempts.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L36180-L36191】
- He teased an open-source 20 Ah 10 S4 P 21700 internal pack with integrated Rita BMS, 3D-printable spacers, and tilted deck risers that preserve the stock cover—positioned as a “default” community design to share on Thingiverse.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L36198-L36210】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L36226-L36229】
- Gen 5 Rita adapters now tolerate 10 S2 P externals without tripping, and Denis is targeting 40 A continuous for upcoming Ninebot 13 S BMS boards, with higher-current versions staged for later revisions.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L36231-L36240】

### External Battery Charging and BMS Requirements (Lines 36,607-36,615)
- Denis excerpted the Rita manual to stress that simultaneous charging through the scooter port only works safely with common-port BMS packs; separate-port batteries risk overcharge unless you isolate the charger or wire around Rita for the second pack.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L36607-L36615】

### Diagnostics, Apps, and Cooling Consumables (Lines 36,590-36,738)
- When Xiaomi BMS LEDs flash red despite even cell voltages, probe the CF test pads—failed sensing capacitors skew readings despite healthy groups, and NTC thermistors should measure near 100 kΩ when unplugged.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L36590-L36599】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L36552-L36569】
- Android 12 phones currently struggle with the Play Store Rita app; Denis recommends installing the refreshed debug build via APK or borrowing an older handset/downg app combo to reflash firmware.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L36650-L36684】
- Riders source Statorade from Nexun or Grin, use roughly 2 ml per hub, and avoid overfilling because excess ferrofluid increases drag instead of cooling efficiency.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L36720-L36724】
- For 140 mm rotor upgrades, square the adapter base, stack the supplied tall washers, extend cable housing to cut flex, and replace frayed brake cables before chasing caliper rub.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L36718-L36734】

### Tire Pressures and Wear Feedback (Lines 35,825-35,829 & 36,707-36,717)
- Heavier riders running 3 in tires on 300 W builds reported 40 psi as a sweet spot; dropping below ~20 psi slows the scooter and feels unsafe, while PMT tubeless casings continue to earn praise for durability once mounted.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L35825-L35829】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L36707-L36717】

### Rita Availability, Shipping, and App Support (Lines 36,739-37,410 & 40,820-41,220)
- Riders pointed newcomers to Denis’ official store (m365.embedden.com) and confirmed Rita hardware itself still sells for about €70, while external packs and bags add substantially to the final price; third-party resellers rarely ship to Turkey, so ordering direct remains the reliable path.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L36746-L36788】
- Samsung phones on recent Android builds struggle with the Rita BMSTool—owners sideload Denis’ debug APK or borrow older devices to configure pack settings, and they reminded each other that capacity entries are mostly cosmetic once voltages are correct.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L36828-L36840】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L37395-L37420】
- Denis will still mail single Rita units worldwide (e.g., Malaysia or Croatia) for roughly $7 with 10–30 day delivery, but shipping complete battery kits is off the table; he suggests sourcing Wild Man bags and chargers separately and specifying the RCA type‑X plug for Xiaomi compatibility.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L40820-L40838】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L41190-L41195】
- Rita flagging “KERS failure” or showing –10 °C while packs finish charging is expected behaviour—regen is disabled on full batteries to protect them, not a sign the emergency resistor tripped.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L40931-L40940】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L41197-L41221】

### External Batteries, Charging Strategy, and Safety (Lines 37,324-37,520 & 40,883-41,025)
- Rita misreports state of charge when a weak 2 P pack sags—the firmware temporarily reuses the last stable voltage if current exceeds ~2 A, a bug Denis already patched for future releases; until then, pair Rita with stout packs to avoid massive droop that drags the internal battery down.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L37324-L37352】
- Charging a 12 S external through Rita skips the internal pack’s CV top-off, intentionally leaving it slightly undercharged—which Denis considers healthier than sitting at 4.2 V per cell—but builders needing precise limits should add a dedicated plug and charge the external pack separately.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L40883-L40926】
- Long-term storage tips stayed consistent: stop around 80–90 % when possible, keep scooters at ~60 % for downtime, and remember Rita can’t impose charge ceilings without a Bluetooth BMS or smarter charger.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L40907-L40921】

### Controller Reinforcement, Capacitors, and Rita Jumper Policy (Lines 37,085-37,138 & 41,060-41,176)
- Veterans still swap Xiaomi controller caps for 100 V 1000 µF + 33–47 µF parts (or larger banks) when running 13 S—stock 63 V cans survive briefly but offer little headroom for regen spikes; stepping down to 470 µF has already cooked boards during bench braking tests.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L37085-L37115】
- Denis restated the Rita jumper rules: generations 1–4 only tolerate 10–12 S with the jumper intact (13 S risks exploding Rita but shields controllers at ~61 V), while cutting the jumper unlocks 10–15 S yet demands reinforced caps/MOSFETs because over-voltage protection shifts to ~71 V. Gen 5 removed that trade-off—13 S works jumper-intact without extra ESC prep.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L41144-L41176】
- Cutting the jumper can still be the “100 % safe” option for legacy units if riders are willing to fortify controllers; leaving it intact becomes a 95 % solution that gambles on Rita rather than ESC hardware.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L41144-L41175】

### Battery Maintenance, Fuses, and Cell Recovery (Lines 37,860-38,580 & 38,563-38,620)
- When reviving over-discharged packs, the group disconnects the BMS harness and uses hobby LiPo chargers to “prime” each series group—emphasising the fire risk and the need to stop if any cell sits below safe voltage after manual charging.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L37860-L37899】
- Daly-style 13 S packs often ship near storage voltage (~38 V), so builders shouldn’t panic over initial low readings; expect ~48 V nominal and 54.6 V full, then double-check Rita’s internal/external configuration before riding.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L38552-L38560】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L38581-L38599】
- Replacement Xiaomi BMS fuses rated 125 VAC/32 VDC work fine on 10 S scooters—solder both F1 and F2 pads so the parallel 30 A links share load like newer boards; expect the pair to trip near 60 A combined.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L38502-L38518】
- LiPo bricks remain a last resort for Rita builds: their high C-rates and lack of robust BMS protection make them prone to swelling or fire, so most riders sell RC packs and reinvest in quality Li-ion assemblies instead.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L38412-L38433】

### Tire, Suspension, and Structural Lessons (Lines 38,521-38,560; 39,750-40,007; 40,961-41,108; 41680-41708)
- Simply topping up underinflated tires cured major speed loss—one Essential owner jumped from 25 km/h to 30 km/h after repairing a hidden flat and now checks pressures weekly to avoid dragging the drivetrain.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L38519-L38535】
- Builders continue to distrust early Monorim hardware: undersized axle bolts, bending forks, and even snapped non-folding poles led them to retrofit stronger fasteners or abandon the platform for Kaabo/G30 components.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L37910-L37920】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L39940-L39959】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L40404-L40418】
- Ten-inch conversions still need careful spacing: front forks around 138 mm clear Blade motors without bending, but installers favour long steel tire levers, heat, and soapy water over dubious YouTube tricks or brittle Monorim bolts.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L39978-L40007】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L41680-L41708】
- Stock Xiaomi/Ninebot decks aren’t waterproof—seal stems with silicone and keep dashboards upright when wet to prevent random power cycling from moisture-damaged buttons.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L37361-L37394】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L41735-L41736】

### Firmware, Compliance, and Power Planning (Lines 39,981-40,033 & 41,660-41,706)
- MeanWell bench supplies struggle as scooter chargers—the crew swapped to dedicated 12 S Li-ion chargers (ideally 54.6 V CV units with RCA type‑X connectors) rather than fight unstable CC/CV behaviour on improvised setups.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L39981-L40009】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L40883-L40926】
- Denis urged Rita owners eyeing 48 V (13 S) packs to monitor current instead of chasing wattage—Rita taps out around 30 A battery current, so scooters needing >2.8 kW acceleration should graduate to VESC or dual-controller AWD builds rather than stacking stock ESCs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L39977-L40024】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L40550-L40558】
- For roadside compliance, firmware chefs recommended custom ScooterHacking/XiaoDash profiles or police modes that default to 20 km/h, letting riders unlock higher speeds only via button combos or companion apps when law enforcement isn’t watching.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L41559-L41605】

### Firmware, App Support, and Speed Calibration (Lines 46,739-47,420)
- Denis reminded Ninebot Max owners running 13 S Rita kits to lift their custom firmware max speed ceiling to 50 km/h, noting that top speed scales directly with battery voltage (10 S ≈ 33 km/h, 13 S ≈ 43 km/h).【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L46751-L46758】
- DownG builds routinely misreport speed because of inflated wheel-size settings, so the crew pointed riders toward GPS checks and modern CFWs while also warning that Rita Gen 5 needs the newest app (older 0.12 APKs crash under Android 12). Joining XiaoDash’s v10 beta via app update 1.38 unlocks per-mode cruise timing, higher PWM frequencies, and custom button mappings once the right phone is in hand.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L46778-L46804】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L46780-L46783】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L46829-L46838】
- After adding a 12 S external, riders must open the Rita app and set “External battery configuration” to 12 or the scooter stays capped and flashes warnings until the parameter is corrected.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L46804-L46813】
- Error 24 on high-voltage builds disappears once ScooterHacking’s “battery voltage limit” is raised to 60 V in the Advanced tab; leave charging mode enabled so regen and top-off routines continue to work.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L47141-L47155】
- Denis’ BMSTool dropped dangerous current-limit sliders in recent releases—the simplified menu is intentional even if older tutorials still show them.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L48204-L48212】

### External Packs, Cells, and Charging Strategy (Lines 47,421-48,600)
- “Speed batteries” that add 3 S 2 P of Samsung 40T cells deliver roughly 20 % more range on M365/1S scooters; Denis steers Polish riders toward Scootermode.eu for turnkey installs and controller swaps when theirs have burned out.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L47061-L47070】
- Battery builders favoured 21700 cells for range: Samsung 48X or LG M50LT maximise capacity, Samsung 40T handles the highest current, and 50E remains the budget pick—expect about €3.35 per 48X cell in bulk and plan packs around 13 S 6 P when space allows.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L47020-L47058】
- A Wild Man 3 L stem bag comfortably fits a 13 S 4 P (52-cell) 21700 pack; the team suggested charging only to 4.1 V and discharging to ~3.2 V for longevity, with Samsung 48X called out for solid cycle life.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L47269-L47288】
- Rita owners chasing AWD performance learned that the stock Pro 2 battery trips near 20 A, Rita itself tops out around 29–30 A, and Monorim’s 48 V packs are too weak—use high-discharge cells (e.g., 48X/40T) and plan on ~25 A per motor for hill work.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L47638-L47660】
- Denis cautioned that Rita expects a common-port BMS; Ninebot ES2 add-on packs with separate charge leads are questionable fits, so the crew advised selling them and buying purpose-built externals instead.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L47938-L47949】
- Never parallel chargers across series-linked batteries—doing so shorts the packs. Disconnect the series jumper or charge each sub-pack separately rather than tying two 3 S chargers together.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L48389-L48416】

### Suspension, Hardware, and Fitment Lessons (Lines 47,780-48,900)
- Monorim shocks often knock because of flimsy springs; the fix is lithium grease, spring swaps matched to rider weight, and higher-grade (12.9) hardware with proper washers/Loctite because the pivot design lacks bearings and likes to loosen.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L47295-L47305】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L47756-L47779】
- Custom fenders for Konyk rear suspension showed that 2.5″ tires remain the practical limit without cutting the swingarms; wider 3″ setups require trimming or alternate mounts even with 3D-printed brackets.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L47888-L47905】
- Ninebot G30 hub motors do not bolt into Xiaomi frames without machining—plan on adapters or different swingarms if you want the swap.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L47858-L47859】

### Diagnostics, Safety, and Waterproofing (Lines 48,600-49,600)
- After water ingress, riders disconnect the battery, rinse electronics with isopropyl, and inspect the power button first; Xiaomi’s newer dashboards still aren’t weather-sealed, so silicone covers and proper tools are needed because rain damage voids warranty claims.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L47378-L47397】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L48179-L48192】
- Rita-equipped scooters that stall at 99 % charge or flash the brake icon aren’t broken—the display is showing the regen-ready e-brake state, and unresolved charging almost always traces back to the internal overcharge jumper or mismatched cell voltages visible in Denis’ app.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L47416-L47460】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L47443-L47455】
- Android 12 support for Rita’s BMSTool is in progress; until Denis ships the update, owners stick with Android 11 devices or sideloaded builds because legacy APKs crash on Gen 5 hardware.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L46829-L46838】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L47871-L47887】
- Sudden cell imbalances on Xiaomi packs usually mean a broken spot-welded balance tab—check the harness before blaming the BMS and repair the tab if it has lifted.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L47909-L47933】
- Ninebot F40 chargers stop at 41 V to extend life, and accidentally topping up with a Xiaomi 42 V brick is harmless even if the gauge briefly reads over 100 %.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L48301-L48312】

### Motor, Controller, and Thermal Management (Lines 49,600-51,738)
- Motor survivability hinges on current and cooling: riders reported 40–65 A bursts on 350 W hubs but saw phase connectors desolder, so they preach installing temperature sensors instead of trusting watt labels and note that Xiaomi dashboards show battery vs. controller temps rather than motor values.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L47563-L47631】
- Rita can run 15 S packs only after cutting the red jumper, as spelled out in Denis’ manual—leave it intact and the adapter will fail catastrophically when a 63+ V battery is plugged in.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L48339-L48356】
- Jumping to 48 V on a stock Xiaomi ESC still demands reinforced controllers; the group panned Monorim’s MOSFET “upgrades” and recommended sourcing quality parts or rebuilding the factory board instead of trusting AliExpress clones.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L48369-L48385】
- AWD riders balance regen with hydraulics: use a strong hydraulic front brake (plus optional second throttle for variable regen), keep 160 mm rotors to maintain ground clearance, and stick with quality discs/pads because 180 mm setups hit the chassis on Xiaomi frames.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L47502-L47520】
- For long downhill runs, they either disable freewheel KERS entirely or raise `kers_min_speed` to ~50 km/h so regen only kicks in above that threshold, pairing the strategy with robust mechanical brakes to handle the load safely.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L47809-L47818】

### Battery Builders, Pricing, and Kaabo Reliability Checks (Lines 51,739-51,859)
- Mirono owned up to outsourcing a faulty pack, refunded the buyer, and Denis warned that once quality control slips most customers cannot spot problems—so outsourcing remains a reputational risk even if refunds are issued later.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L51741-L51799】
- Regional builders quoted Vsett 10+ battery options ranging from €540 for 60 V 15 Ah externals to €990 for 40 Ah internals, built with Samsung 50G cells, pure nickel or nickel-copper, and optional Bluetooth BMS/XT90 upgrades for lower voltage drop.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L51805-L51824】
- IO Hawk/Kaabo Mantis owners cataloged weak plastics, sloppy folding tolerances, and the cost of mandatory upgrades (geared motor swap, hydraulic brakes) before the chassis matches a tuned Xiaomi, suggesting buyers budget another €450+ if they pursue the platform.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L51831-L51857】

### 21S Builds and Kelly Controller Configuration (Lines 52,018-52,060)
- EtorroS is assembling a 21 S 10 P (≈42 Ah, 250 A) pack and lined up Kelly controller supply for the group, noting the Bluetooth module unlocks per-mode speed and power limits so riders can keep a 25 km/h compliance mode while retaining full output on demand.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L52018-L52055】
- He shared Kelly setup resources so builders can program eco toggles and travel-safe profiles without guesswork.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L52041-L52060】

### External Pack Paralleling and Charging Hygiene (Lines 52,174-52,280)
- To reuse a stock pack externally, the crew recommended a Y-harness on the main leads only, matching voltages before plugging in, charging both batteries to the same level first, and leaving them connected if the scooter stays unlocked for charger-in-ride operation.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L52174-L52213】
- Separate-port Xiaomi batteries complicate things—avoid paralleling chargers on tied packs, upgrade the charge port beyond 3 A, and consider unplugging the external for standalone charging if the BMS is not common-port or you need faster top-ups.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L52217-L52271】
- Riders power accessories such as phone chargers through dedicated step-down converters instead of tapping the pack directly.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L52276-L52280】

### Connector Sourcing and Tail-Light Options (Lines 52,368-52,418)
- Denis identified the Xiaomi tail-light connector as JST PAP-05V-S and proposed a community buy at $0.45 per bare plug (3,000 unit minimum), prompting debate between keeping the stock connector for plug-and-play battery swaps versus drilling for XT30s to improve sealing and durability.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L52368-L52418】

### Tire and Rim Fitment Tips (Lines 52,444-52,446)
- For stubborn CST 10-inch tires that refuse to seat evenly, veterans sometimes machine 1.2–1.5 mm from the rim interior to relieve the bead—a pricey but reliable fix when lubrication fails.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L52444-L52446】

### Auxiliary Lighting Performance and Cooling (Lines 52,531-52,667)
- Off-road riders mount 6-inch “18 W” LED pods for rural trails but report real output far below the sticker, pairing them with reference videos and 15 W single-LED beams to judge spread before wiring turn-signal selectors.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L52531-L52555】
- Others pointed to Busch & Müller e-bike headlights for efficient, non-blinding beams, while custom builders plan 50–100 W LED assemblies with serious heat sinking, avoiding generic AliExpress housings that can’t dissipate the load.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L52632-L52670】

### Controller Failures, Motor Heat, and Torque Debates (Lines 52,800-53,320)
- A 350 W high-kV swap cooked another Xiaomi controller under a 110 kg rider; the group stressed limiting duty-cycle cruise control, upgrading to reinforced or VESC-based ESCs for hills, and checking for phase shorts by unplugging the motor if the hub drags after a run.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L52800-L52860】
- Riders agreed high-kV clone motors pull harder at speed but deliver less torque per amp, heat faster, and demand temperature sensors plus higher voltage (13–15 S) if long hill climbs are planned.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L52915-L52949】
- Denis reminded newcomers that Rita can top-charge 10 S and 12 S packs in series with a single 12 S CC/CV charger, yet dual chargers remain the 99.99 % safe option because they bypass any BMS edge cases.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L52895-L52904】
- On the performance end, a 12 S VESC build with a 350 W high-kV hub still touched 48 km/h at ~30 A, but the owner capped current at 100 °C using a motor-mounted thermistor to keep phase leads alive.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L54894-L54906】

### Suspension Fasteners and Bearing Care (Lines 53,198-53,250)
- Builders blamed Monorim play on the lack of proper bearing housings and undersized hardware; upgrading to precise 12.9 bolts with self-locking nuts keeps the swingarm moving freely without needing aftermarket bearings.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L53198-L53247】

### Clone Battery Cleanup and Waterproofing (Lines 53,255-53,302)
- What looked like corroded nickel on a clone 7.8 Ah pack turned out to be softened glue, yet the teardown reinforced the need to inspect deck grommets for leaks, avoid soldering cells, and rebuild suspect packs with a spot welder, Kapton insulation, shrink wrap, and silicone-sealed ends.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L53255-L53302】

### Monorim Axle Hardware and ESC Diagnostics (Lines 54,163-54,238)
- Monorim owners measured the fork pivot at roughly 7.86 mm (effectively M8), warning that Chinese tolerances complicate bolt sourcing and that controllers can burn brake traces after long descents, especially if trackers or other loads share the harness.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L54163-L54238】

### Rita Gen1 Configuration and Charging Limits (Lines 53,948-53,975 & 55,931-55,972)
- Denis recapped that Gen 1–2 Rita adapters need no jumper change for 10 S externals, require software configuration for 11–12 S, and demand a jumper cut plus configuration for 13–15 S; charging separate-port packs through Rita is still discouraged because regen already backfeeds through the XT30.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L53948-L53975】
- Later chats reiterated Rita’s 30 A battery-current ceiling: exceeding it on Gen 1 hardware risks catastrophic failure, so power sliders in custom firmware should stay near 25–30 A despite temptingly high estimates.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L55931-L55972】

### Happy BMS Launch and Compatibility (Lines 54,916-54,963)
- Denis unveiled the “Happy BMS” smart board covering 9–15 S packs at up to 44 A, priced around €69, flashing a red status LED, and compatible with Xiaomi protocols while remaining usable in ebikes or other DIY projects that need a compact, trustworthy alternative to Daly clones.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L54916-L54963】

### Tire Sealant Expectations (Lines 54,964-54,999)
- Slime-type sealants still need pressure to set—tiny punctures may weep slowly, larger holes demand rubber plugs—and riders clarified the green formula suits tubeless casings, with about half a bottle per tire delivering the best odds of a lasting seal.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L54964-L54999】

### 15S Controller Mod Paths and Firmware Notes (Lines 55,883-55,905)
- For 15–20 S conversions, EtorroS and Abs coordinate resistor-mod or trace-cut controllers, with shipping support if local pickup is impossible; remember that ScooterHacking firmware voltage toggles mainly affect display reporting rather than true input limits.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L55883-L55899】

### VESC Dash Support and Firmware Paths (Lines 55,959-55,966)
- VESC adopters confirmed that full rewiring is required, but a new Lisp-based compatibility layer lets Xiaomi dashboards run on VESC 6 hardware, keeping stock displays while the community refines throttle-step behavior.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L55959-L55966】

### Monorim Battery Warnings and Rita Error Handling (Lines 56,642-56,679)
- Denis and Happy Giraffe advised against Monorim’s 48 V batteries—quality issues and limited controller compatibility make them poor Rita companions—and reminded riders that Rita hands power back to the internal pack near 41–42 V, triggering error 39 on Gen 1 boards once the stock battery overheats.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L56642-L56679】

### Repair BMS Calibration Workflow (Lines 56,680-56,694)
- Repair-BMS owners should fully charge until current tapers for two minutes to set 100 %, then ride to empty so the coulomb counter aligns with reality; if readings stay off, suspect a mis-set capacity value or a faulty board rather than the voltage table.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L56680-L56694】

### Cell Selection and Range Planning (Lines 56,712-56,716)
- Denis reiterated that 10 A-class cells suit most 10 S4 P commuter packs, while Happy Giraffe pointed budget builders toward Samsung 35E (18650) or LG M50LT/Samsung 48X (21700) for range, reserving 40T/Molicel cells for high-discharge builds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L56712-L56716】

### Top-Speed Targets and Motor KV Planning (Lines 56,718-56,738)
- Chasing 50 km/h on an M365 means more voltage and the right motor constant: swap to a low-KV hub, increase pack S-count with stout P-groups to cut sag, and plan on quality controllers (Mobipus, uBox, Kelly) because motor wattage ratings alone don’t dictate speed.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L56718-L56738】


### Low-KV Motor Strategy and Wheel-Size Trade-offs (Lines 56,730-56,770)
- KD and Happy Giraffe reiterated that Xiaomi platforms thrive on low-KV hubs fed by higher-voltage packs, since the stock electronics can’t push the current a high-KV “speed” motor demands without losing torque or overheating; reinforcing pack P-groups keeps voltage sag in check at higher speeds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L56730-L56745】
- The team debated taller 12-inch wheels, noting they allow larger stators but hurt launch torque, whereas 10-inch rims still balance grip and acceleration for 60 km/h builds when paired with long wheelbases and tuned suspension like Segway’s GT2.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L56757-L56770】

### External Battery Paralleling Habits (Lines 56,784-56,822)
- When paralleling a Ninebot ES2 pack with a Xiaomi Pro 2 battery, riders stressed matching voltages before connecting, periodically checking both packs with a multimeter after rides, and accepting that the dashboard only reports the internal battery unless a Rita interface is installed.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L56804-L56819】
- Xiaomi BMS firmware quirks can leave newer Pro 2 packs capping around 40.8 V, so external packs may finish charging higher—another reason to monitor voltages manually or switch to Rita for smarter balancing.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L56821-L56826】

### Mi3 Brake Compatibility Lessons (Lines 56,872-56,905)
- Mi3 owners confirmed the updated double-piston caliper outperforms Xtech clones but uses unique mounting holes and larger rotors, so adapters must be custom-made and pads sourced directly from Xiaomi—ideally in sintered or semi-metallic compounds for wet braking.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L56872-L56897】
- Community sellers only warranty Xtechs for three months because quality varies wildly; even good units demand frequent cleaning when used as the primary front brake on Monorim setups.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L56939-L56999】

### Monorim Kit and Fork Durability Warnings (Lines 56,899-56,932)
- Riders panned the Monorim U5 “Super” kit for using soft aluminum fork arms that bend from hard landings; even bearing housings can loosen, so aggressive riders should inspect pins regularly and plan upgrades instead of relying on bundled controllers that barely reach 40 km/h.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L56900-L56932】

### 48 V Upgrade Boundaries for Stock Controllers (Lines 56,914-56,940)
- Denis said 48 V can run on the newest V3 Xiaomi controllers, but Her0DasH cautioned that high current settings still overheat traces and trigger random error 28/29 events—reinforcement and careful firmware tuning remain mandatory beyond 12 S.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L56914-L56933】
- Ricardo Rapture limits controller noise by raising switching frequency to 16 kHz via XiaoDash, accepting extra MOSFET heat in exchange for quieter dual-motor builds with upgraded cap packs and parallel batteries.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L56932-L56946】

### Suspension and Brake Noise Mitigation (Lines 56,939-57,020)
- Konyk/Dereza suspension combos deliver buttery travel when paired with dual hydraulic brakes, yet riders still glue 3D-printed fenders and aftermarket throttles with Suxun T-7000 to silence creaks at 50 km/h speeds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L56950-L56970】
- E-brake reliance is fine for light riders, but heavier builds keep dual mechanical backups because electronic braking disengages once wheels lock, extending stopping distances.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57006-L57020】

### High-Speed Wobble Case Studies (Lines 57,041-57,210)
- EtorroS’ 100 km/h wobble footage prompted a breakdown on C-type fork geometry: letting off the throttle or running soft springs induces oscillations that even steering dampers can’t cure without stiffer shocks, longer Monorim spacers, and proper bar width.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57032-L57080】
- Riders tackling 60–110 km/h insisted on PMT tires, wide handlebars, and practiced body positioning to keep weight rearward while hardening dampers and rebound controls to tame high-speed shimmy.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57081-L57138】

### Rental Chassis Expectations (Lines 57,300-57,360)
- Heavy-duty Tier/Bird/Lime scooters (Okai ES400) can be bought as retired rentals, but veterans warn they ride poorly compared to tuned Xiaomi builds despite the rugged frames.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57189-L57210】

### Charger Current, Connectors, and Cell Stress (Lines 57,413-57,470)
- Moving to 42 V/3 A chargers halves charge time but noticeably heats stock JST charge leads, so owners either upgrade connectors or accept faster cell aging from aggressive charge rates.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57254-L57278】

### 48 V Monorim Battery Critiques (Lines 57,445-57,520)
- Denis and resellers dismissed Monorim-branded 48 V packs as “pure China,” citing fake Panasonic claims, downgraded cells (~4,200 mAh vs. 5,000 mAh advertised), and weak controllers—builders should wait for Denis’ native-data battery or commission customs instead.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57245-L57303】

### Monorim Maintenance Notes (Lines 57,520-57,590)
- Long-term Monorim users found pivot pins bending and bearing cups separating after jumps; replacing the pin proactively and re-torquing bolts prevents catastrophic fork failures.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57344-L57360】

### BLE Glitches and Cable Diagnostics (Lines 57,601-57,720)
- Random throttle loss without error codes often traces to failing BLE cables—if the dashboard stays lit yet throttle, lights, and brake lamps die, swapping the BLE harness restores normal modes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57380-L57420】
- For Rita users juggling external packs, the adapter was built to leave the internal battery at 100 % without harm, though Pro 2 owners stuck on BMS 126 still charge only to ~40.5 V until reflashed.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57453-L57518】

### Firmware Tweaks and Charging Etiquette (Lines 57,618-57,700)
- Denis reminded Rita installers to patch the “battery voltage limit/ADC divider” when running 10 S+ packs to avoid error 24, and Her0DasH reiterated the safest charge sequence: plug the scooter first, then connect mains power to reduce connector sparking.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57519-L57540】
- Riders relying on mechanical brakes still disable KERS in firmware for freewheeling, keeping engine braking mapped to lever pulls only.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57541-L57548】

### External Battery Weatherproofing (Lines 57,708-57,770)
- Rita’s bundled Wildman bags aren’t waterproof—the community covers them with separate seat covers or custom rain shells and warns that standard zippers leak without extra shielding.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57589-L57610】

### Paralleled Pack Balancing Behavior (Lines 57,780-57,826)
- External packs naturally backfeed into the internal battery when idle, so minor SOC rises (e.g., 70 %→71 %) are normal; if packs drift badly, check for motor faults or hall sensor failures before blaming Rita.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57620-L57660】

### Hall Sensor Troubleshooting Workflow (Lines 57,826-57,940)
- Her0DasH laid out a hall-diagnosis checklist: probe sensor wires with a multimeter while a helper slowly spins the wheel, verify each hall toggles between 0 and ~5 V, and inject 5 V from a spare USB lead to bench-test sensors outside the controller—any hall that stays flat must be replaced before chasing controller faults.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57660-L57720】

### Range vs. Speed Batteries (Lines 57,940-57,980)
- Add-on “range” packs keep speed the same but hold voltage longer, whereas true “speed” batteries raise series count and demand Rita plus controller mods; without Rita, higher-voltage packs require firmware emulation that’s risky on Xiaomi BMS boards.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57720-L57760】
- Builders cautioned against tiny “speed” modules without BMS protection—the high currents cook cells and wiring, making custom Li-ion packs or Denis’ planned 13 S internals a safer path to 50–60 km/h goals.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L58064-L58079】

### Suspension Supply Constraints and Cooling Projects (Lines 57,980-58,040)
- Dereza/Konyk suspension kits remain scarce due to Ukraine’s war-time production pauses, so builders hoard parts and design full cooling housings for 20–21 S packs with Tronic controllers before releasing them as kits.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57760-L57820】

### Phase Current Tuning and “Russian” Throttle (Lines 58,040-58,110)
- Denis shared optimal XiaoDash sliders—29/20/7 A for eco/drive/sport battery current with 55/32/20 A phase settings—and recommended the “Russian” throttle (flat power curve) so riders modulate torque directly, especially on 44.4 V 350 W hubs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57820-L57860】
- Without BMS communication cables, controllers throw brake-light errors; XiaoDash or ScooterHacking firmware can emulate the BMS if builders insist on deleting the data line.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57861-L57880】

### BLE 1.5.7 Downgrade Requirements (Lines 58,110-58,220)
- BLE 1.5.7 blocks Bluetooth flashing—owners must either swap in an older dashboard or use an ST-Link programmer with soldering access to downgrade the BLE before custom firmware or speed hacks will stick.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57880-L57940】

### Rita Fuse Protection (Lines 58,260-58,360)
- Gen 5 Rita boards use a single 30 A fuse on the external battery input; unlike older dual-20 A versions, exceeding 30 A simply blows the fuse instead of sacrificial traces, so diagnose with a multimeter or temporarily short the fuse pads before swapping in a replacement instead of reverting to a less-protected Gen 1.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57970-L58040】

### Wheel-Size Calibration and Tire Selection (Lines 58,360-59,040)
- Firmware “wheel size” is just a multiplier—GPS checks showed 10-inch PMT slicks still read fast unless the multiplier drops to ~9.5–9.8, while many clone 10×2.5 tires actually measure closer to 9.5 inches once mounted.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L58040-L58110】
- Mixing 10-inch front and 8.5-inch rear wheels induces wobble, and fitting true 10-inch CST/Tuovt casings may require shaving the rim bead or swapping mudguard screws for low-profile hardware to avoid rub.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L59013-L59039】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L59033-L59040】

### Voltage Limits and Heat Management (Lines 58,470-58,640)
- Builders chasing 50–60 km/h cited 15–17 S packs plus stout controllers, but veterans caution stock DRV 1.4 electronics top out around 12 S unless heavily reinforced (trace mods, lower PWM frequency) to avoid MOSFET burnout.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L58110-L58260】
- Real-world reports put 48 V (12 S) Pro 2 builds around 44 km/h on 8.5-inch tires, reinforcing that 12 S is already pushing Xiaomi hardware; attempts at 13 S need extensive controller mods and lowered PWM frequency to survive.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L57846-L57879】
- Summer heat shortens the safe duty cycle at high amperage; expect to roll back power once ambient temps climb past 25 °C or risk cooking motors and controllers that survived winter pushes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L58276-L58334】

### MOSFET and Component Sourcing (Lines 58,640-58,720)
- For controller upgrades, SirGeoff recommended NCEP01T18 MOSFETs as a superior drop-in to IRFB4110s, while others shared AliExpress sources for original Dot BLE boards and warned purple clones need ST-Link reflash before Bluetooth speed hacks work.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L58360-L58460】

### Torque Arms and Clamp Hardware (Lines 58,720-58,838)
- DIY torque arms for high-amp hub motors benefit from 5–10 mm steel plates with tight axle cuts bolted through the frame; hose clamps alone are considered “China shit” unless paired with correct-side mounting and minimal e-brake use.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L58480-L58570】
- Wildman bag hose clamps can deform if overtightened—replace damaged clamps cheaply rather than trusting fatigued hardware to restrain external packs at speed.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L58520-L58560】


## Follow-up Ideas
- Document a step-by-step 13S Xiaomi V3 reinforcement guide (soldering hotspots, thermal pad part numbers, resistor math for >13S).
- Capture a vetted wiring checklist for Rita installs covering Y-cable strain relief, fuse positions if desired, and charging-port routing for dedicated external packs.
- Compare Monorim V4 spacer/bolt revisions versus Kroxne’s best practices to propose a standardized shim kit.
- Draft a Rita generation comparison (old vs. current sensing boards) with safe amp limits, jumper guidance, and example XiaoDash settings.
- Produce a XiaoDash recovery checklist covering SN repair, DRV migrations, and warning signs before flashing custom profiles.
### Series Conversions Without Rita (Lines 104,385-105,174)
- Builders confirmed that bumping a Xiaomi 1S to 48 V by adding a 3S stack in series with the stock 10S pack does not require Rita—simple series wiring works, but the packs should be charged separately unless they are identical and kept well balanced.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L104385-L104391】
- Rita can still simplify single-port charging when the internal battery stays 10S and the external pack is 12S, yet Denis warned that the adapter cannot charge a 12S internal plus 10S external combo; confirm the architecture before tying chargers together.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L105164-L105174】

### Interpreting Rita Status and Error Logging (Lines 104,409-106,859)
- A red LED on Rita with a blue external-pack light simply means the adapter is powered; when the scooter stays dark after a shutdown, assume the controller blew MOSFETs instead of blaming Rita or the battery.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L104409-L104427】
- When Rita throws error 21, inspect its adapter board for visible damage and, on the next fault, connect with Peretti’s m365tools to read the human-readable message Denis embeds in the battery serial field to pinpoint the failure cause.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L104769-L104775】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L106854-L106859】

### Matching Motors and Controllers for High-Voltage Builds (Lines 104,466-104,558)
- Veterans cautioned that reinforced Xiaomi ESCs plateau around 35 A battery current—far below what high-kV Vsett 10+ hubs demand—so expect sluggish acceleration unless you step up to a VESC-class unit capable of 140 A+ phase output.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L104466-L104505】
- For 15S conversions that still rely on stock decks, the consensus is to choose an 800 W “mini blade” motor for torque at modest currents; 1.2 kW hubs can reach 80 km/h but only when fed far more amperage than Xiaomi electronics tolerate, and field-weakening heat makes ferrofluid or hubsinks mandatory.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L104545-L104558】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L104622-L104633】

### Suspension Kits, Tires, and Clone Hardware Caveats (Lines 104,659-109,207)
- Ultra-cheap “Monorim” forks advertised around €15 are just thin sheet metal that crack quickly; spend for the real assembly or expect catastrophic failure.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L104659-L104688】
- Proper 10×3 conversions often need custom spacers or washers to center the disc and caliper—off-the-shelf kits rarely line up—so builders fabricate steel adapters or source dedicated shims to avoid rubbing.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L106820-L106827】
- Mirono flagged Monorim’s branded 500 W motor as overpriced, unable to handle more than ~25 A, and sold with a harsh solid tire, making it a poor match for custom 48 V projects despite the marketing hype.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L109192-L109207】

### Repairing Burnt Phases and MOSFET Stages (Lines 105,023-105,637)
- After melted stock phase plugs cooked a controller, the group recommended replacing the Xiaomi blade terminals with properly crimped or soldered bullet connectors, ensuring each phase lead is fully seated and insulated with heat-shrink to stop repeat failures.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L105023-L105071】
- When swapping shorted MOSFET pairs, clean the conformal coating with 99 % isopropyl and a toothbrush, reuse matching 15810 devices in pairs, and verify each transistor sits flush on the thermal pad; warped packages or residual UV coating lead to hotspots and fresh blowouts.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L105561-L105637】

### Handling Overcurrent Trips and Controller Diagnostics (Lines 105,745-109,360)
- Error 28 and wheel vibration after reassembly point to lingering MOSFET faults; confirm diode-test readings on each leg before trusting the repair.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L105745-L105747】
- Rita v6 will cut power on overcurrent if firmware tries to pull above ~30 A battery; dialing back battery current in the custom firmware cleared repeated shutdowns.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L106854-L106864】
- A Xiaomi will still spin freely with two phase leads disconnected and throws no dashboard code—only hall sensors are monitored—so inspect the three phases manually whenever the throttle is dead without beeps.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L109352-L109360】

### Packing More Cells Into Xiaomi Decks (Lines 107,643-107,709)
- Experienced builders fit a maximum of thirty 21700 cells (13S2P) or forty 18650 cells inside a stock 1S deck without a spacer; squeezing 16 cells per row requires relocating the controller, and any 2P layout demands high-discharge cells plus meticulous welding to avoid overstressing the pack.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L107643-L107709】
- Denis recommends LG M50LT-grade cells and a 28 A battery limit when running 13S2P in the stock bay, stressing that 2P packs are brutal on the cells unless welds and cooling are perfect.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L107701-L107709】

### Cell Choices, Amp Math, and Pack Limits (Lines 109,173-109,293)
- Mentors reminded newcomers that Amps come from parallel groups: typical 5 A 18650s need at least 4 P to supply 25 A without brutal voltage sag, while premium Molicel P42A/45B 21700s can comfortably deliver 40+ A per cell, letting smaller packs hold torque.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L109173-L109293】
- Modified Xiaomi ESCs rarely survive beyond ~60 A battery draw even after trace reinforcements, so plan motor power around that ceiling or budget for a VESC-class controller.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L109257-L109266】

### Balancing and Diagnosing Dead Packs (Lines 105,378-105,387)
- Seeing ~14 V at the discharge leads of a 10S pack usually means the BMS latched off; probe each series group to find the dead cell block, and expect a faulty BMS if half the groups sit at 4.15 V while the others sag to ~3.5 V.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L105378-L105387】

### Motor Cooling and Ferrofluid Dosing (Lines 104,622-109,315)
- Field-weakening experiments showed Xiaomi-class hubs overheat quickly, so riders add ferrofluid between the magnets to shrink the air gap and wick heat into the shell, pairing the treatment with hubsinks for sustained high-speed runs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L104622-L104633】
- Keep ferrofluid volumes modest—about 4–6 mL is enough even for larger MXUS or Xiaomi hubs—because overfilling creates drag and mess without extra cooling benefit.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L109305-L109315】

### Battery Shipping and Storage Safety (Lines 106,838-106,910)
- When mailing packs, cushion them with foam or bubble wrap so they cannot move, insulate main connectors, and ship around 50–60 % state of charge to stay within carrier limits and prevent damage in transit or storage.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L106838-L106844】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L106910-L106911】

### Accessory Power and Charger Care (Lines 104,722-105,452 & 106,936-106,944)
- Xiaomi’s 5 V rail can barely run the stock dash—power hungrier accessories need their own DC-DC converter fed from battery voltage via an upgraded 5-wire harness to avoid brownouts and parasitic draw while parked.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L104722-L104725】
- Ninebot’s 3 A internal charger is held together with compound and three screws; remove the potting carefully and expect to replace the thermal fuse when refurbishing salvaged units for Xiaomi service bays.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L105439-L105452】
- Global Xiaomi chargers accept 100–240 V input, so swapping to a local plug or using a travel adapter is sufficient—just avoid twisting bare wires together.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L106936-L106947】

### Maintaining EXA Air Shocks Without Disassembly (Lines 106,931-106,955)
- To refresh EXA-style air shocks, drop the pressure, remove the standard Schrader valve core, drip silicone oil inside, and pump it back up; this lube approach keeps seals happy without a full teardown, though fork-specific grease lasts longer than generic chain oil.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L106931-L106955】

### Designing 15S Packs for Xiaomi Frames (Lines 109,381-109,441)
- A 15S2P build with Molicel P42A cells supplies up to ~84 A, but Denis stresses that pushing 25 A per cell demands reinforced welds and wide copper traces; otherwise the Xiaomi ESC’s ~50 A ceiling will trip before the pack delivers its potential, making a VESC upgrade the long-term plan.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L109381-L109418】
- Builders warn against mixing wildly different series counts—running 15S beside a stock 10S battery is only viable if the lower-voltage pack is removed, because Rita can’t safely balance such a large mismatch.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L109438-L109441】

### Flashing 48 V Conversions and Managing Hill Performance (Lines 109,502-109,549)
- Error 24 on 48 V Xiaomi conversions clears after flashing pro-model firmware—even if DownG warns about mismatched hardware—and riders keep an ST-Link handy as a safety net should the flash fail.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L109502-L109523】
- Switch ScooterHacking’s throttle curve to linear for predictable response: quadratic mapping hides power until full twist and makes hill launches sluggish.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L109525-L109532】
- When testing new power limits on climbs, start with a full charge, build speed before the slope, and watch ESC/motor temperatures before raising current to avoid overheating the drivetrain.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L109542-L109549】

### Switching Auxiliary Lighting from the Tail-Lamp Signal (Lines 109,555-109,583)
- Rather than loading the stock buck regulator, tap the tail light’s control wire to drive a relay and feed 12 V accessories from a dedicated DC-DC converter tied to the battery pack.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L109555-L109568】
- Owners report the Xiaomi rear light rail as 3.3 V while Sergey has measured a 5 V PWM output, so confirm the actual voltage on your scooter before wiring solid-state triggers.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L109563-L109585】

### Ferrofluid Dosing and Tire Prep Lessons (Lines 109,588-109,679)
- Only a few milliliters of ferrofluid are needed—overfilling causes drag without extra cooling—so add it gradually and test after each dose.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L109588-L109596】
- Riders battling recurring flats switched to quality 10×3 CST or PMT tires, filing rim burrs and upgrading camera mounts to aluminium because printed accessories tend to crack under real-road abuse.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L109676-L109679】

### Charging Gear for 15S Builds (Lines 109,691-109,735)
- A 42 V Xiaomi charger tops a 15S pack at only ~2/3 charge; order a ~63 V supply (even from AliExpress) with the Xiaomi plug fitted, keep current modest unless you rewire the deck harness, and expect slow charge times at ≤1 A.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L109691-L109735】

### Diagnosing Xiaomi BMS Half-Voltage Output (Lines 110,711-110,860)
- If a pack shows ~39.6 V at the cells but only ~19.6 V at the discharge leads, the BMS has latched off—reflow the top balancing rails, inspect the ribbon cable, and avoid mixing new 18650s with tired cells because the measurement harness only samples the welded rails.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L110711-L110860】

### Selecting and Mounting VESC-Class Controllers (Lines 111,127-111,185)
- For dual 12S builds, veterans favour the Spintend single Ubox (80 V/100 A) when bolted to aluminium for cooling; it can move ~10 kW but arrives with fragile M2.5 hardware and occasional solder defects that need rework or QC by a trusted reseller.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L111127-L111185】
- Expect to fabricate brackets—some repurpose the deck battery holes and upgrade to M6 threads—and use an ADC adapter if you want to retain stock Xiaomi throttle, brake sensors, and lighting.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L111176-L111185】

### Rita Regen Safeguards and External Pack Checks (Lines 111,808-111,850)
- A flashing temperature icon with dead e-brake isn’t overheating—it’s Rita disabling KERS per the manual (page 12) when braking pushes too much current back into the packs, so review external battery health and wiring before blaming sensors.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L111808-L111850】

### Rita Regen Failures and Controller Capacitors (Lines 112,621-112,667)
- Braking a 13S setup at high state of charge can spike voltage, blowing Rita and the controller’s 100 V capacitors; replace them with low-ESR parts (e.g., Nichicons), clean any electrolyte, and consider upgrading ADC dividers when stretching stock ESCs past 12S.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L112621-L112667】

### Internal Charger Limits on the Ninebot Max (Lines 112,683-112,717)
- The Max G30’s internal charger is only ~3 A (2.9 A nominal) and runs hot—over 60 °C even when idle—so builders either add thermal pads to the frame, accept early failures, or remove it when moving to higher-voltage battery systems.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L112683-L112717】

### Suspension Upgrades and Axle Hardware (Lines 113,905-114,209)
- Sharkset’s dual-shock kits offer more travel than Monorim but can add steering wobble if you only fit the front; pairing the rear suspension and optional Grip Kit restores trail and stability for 50 km/h builds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L113905-L113949】
- Converting to 10×3 rims demands purpose-made shoulder axles or 12.9-grade bolts with proper spacers—random hardware-store fasteners or 7075 aluminium rods will bend under load—so many riders order custom through-axles or lathe parts to match the wider hub.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L113900-L114209】

### New DRV Boards Still Need Matching Firmware (Lines 124,520-124,579)
- Replacing a dead Xiaomi DRV with an AliExpress board is not plug-and-play—the donor must share the target BLE firmware, otherwise you’ll need to ST-Link flash the proper image before the throttle responds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L124520-L124579】

### Diagnosing Xiaomi BMS Half-Voltage Output (Lines 124,564-124,575)
- If a rebuilt 10S4P pack only exposes ~20 V and blinks red, probe every group: uneven cells or a defective Xiaomi BMS can latch output low, and veteran builders suggest switching to a smart JBD BMS once group voltages drift beyond a few tenths.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L124564-L124575】

### Prefer G30 Gen 1 Motors Over Monorim 500 W Swaps for Torque (Lines 124,520-124,603)
- The workshop recommends G30 Gen 1 hubs for 48 V Xiaomi builds with Monorim forks—the clone 500 W motors arrive with solid tires, short leads, and QC issues, while the G30 mule tolerates rewired hall/phase combos and supplies reliable torque once the fork is reversed and wiring extended.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L124520-L124603】

### Trace 13S Parallel Cutouts to Weak Groups or Welds (Lines 124,603-124,626)
- Dual 13S packs that reboot under load usually point to one pack sagging—disconnect each battery, log JBD telemetry during a cut, and inspect for low groups or cracked welds rather than chasing dashboard corrosion.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L124603-L124626】

### Max G2 Deck Fits 13S6P at 122.5 mm; 16S Builds Need Relocated Hardware (Lines 124,634-124,711)
- Builders confirmed the Max G2 bay accepts a 122.5 mm-wide 13S6P pack without moving electronics, but 16S6P and 20S holders demand controller/charger relocation, tight 0.15 mm cell spacing, and patient 0.2 mm-nozzle prints to clear the screws and wiring.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L124634-L124711】

### Set Rita’s External Pack Serial Count Before Riding (Lines 124,706-124,707)
- Rita defaults to 10 S external packs—update the serial-count setting in the BMS tool so charge bars and protections follow your actual series configuration.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L124706-L124707】

### Water-Damaged Dashboards Beep Until the BLE Harness Dries (Lines 124,716-124,725)
- A Pro 2 that beeps once per minute while off usually has water across the BLE board: disconnect the harness, dry the LED rail, and clean corrosion before the 5 V rail fries the dash.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L124716-L124725】

### Copper Bus Bars and 600 A Spot Welds Support High-Power Packs (Lines 124,744-124,815)
- For 20 S builds, riders stack 0.3 mm copper with 0.12 mm nickel and hit welds with ~600 A for ~19 ms, preferring overkill contact to punctured cells and leveraging 4 mm copper plates plus dual 75100 VESCs on 60 V packs for AWD Xiaomi conversions.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L124744-L124815】

### Seal Charge Ports with Automotive RTV Instead of Generic Silicone (Lines 124,822-124,842 & 126,200-126,252)
- Workshop techs swap leaking RCA jacks for black housings and automotive sealants—Mannol motor RTV, PU50 polyurethane, Dirko HT, or Kafuter 704—because consumer silicone and Sikaflex leave gaps, crack on wires, or take too long to cure for daily use.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L124822-L124842】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L126200-L126252】

### Rewiring Hall Sensors Requires Matching Color Maps and Checking for Flying Boards (Lines 124,800-124,828)
- Error 18 returns after hall replacements when sensor boards shift or phases are mis-matched—verify each hall with a meter, follow the known Xiaomi color swaps (e.g., brown↔green), and secure the PCB so the sensors stay aligned.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L124800-L124828】

### Series Battery Builds Need Dedicated Charge Ports for Safe Regen (Lines 125,030-125,041 & 126,214-126,238)
- When stacking a 12.6 V pack in series with the stock battery, Denis insists on a BMS with its own charge port—regen dumps current through the same harness that powers the scooter, and common-port packs must stay slightly undercharged to absorb braking surges without popping the ESC.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L125030-L125041】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L126214-L126238】

### Replace Kapton Tape with High-W/mK Pads on Xiaomi Controllers (Lines 125,522-125,577)
- Kapton only moves ~0.45 W/m·K, so admins cut it off the MOSFETs, bolt the tabs down through thin silicone pads (≈6–15 W/m·K), and add fresh thermal paste before chasing higher voltage or PWM-frequency tweaks.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L125522-L125577】

### Balancing Guidance for Aging Packs (Lines 125,782-125,804)
- Cell deltas around 0.05 V after a ride are acceptable—leave the pack on the charger for three to four hours past green once or twice a week so Xiaomi’s smart BMS can bleed the high groups back in line.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L125782-L125804】

### Dry Out Rain-Soaked Dashboards Before Corrosion Sets In (Lines 125,845-125,868)
- A Pro 2 that cuts out after rain likely has moisture at the power button—disconnect the pack, open the dash and controller, blot everything dry, then flush the switch with isopropyl and mild heat so the 5 V rail doesn’t corrode traces.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L125845-L125868】

### 36 V 16 Ah Upgrades Work on 1S Without Controller Mods if Data Lines Disabled (Lines 125,868-125,875)
- Dropping a 16 Ah pack into a Xiaomi 1S is fine for the 350 W motor and stock ESC—just flash SHFW (or similar) to emulate the BMS data lines so the scooter ignores missing telemetry.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L125868-L125875】

### External Stem Batteries Shift Steering Feel (Lines 126,143-126,156)
- Stem-mounted packs stay put with silicone, Velcro, and duct tape, but they raise the center of mass—expect heavier steering and plan to remove the bag on short trips if you want the scooter to feel balanced.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L126143-L126156】

### Opening G30 Battery Cases Requires Patience but Only Thin Sealant (Lines 126,154-126,166)
- G30 battery lids are held by six screws and a thin bead—start at a corner with a slim screwdriver (or gentle heat) and pry evenly to avoid cracking the housing.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L126154-L126166】

### Xiaomi Pro 2 Controllers Tolerate About 25 A at 48 V Before MOSFET Reinforcement Limits (Lines 126,142-126,150)
- Even with trace reinforcement and Monorim motors, Denis caps Pro 2 V3 controllers around 25 A battery current—push higher and you risk cooking MOSFETs despite better cooling.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L126142-L126150】

### Common vs Separate Port Batteries Demand Different Parallel Wiring (Lines 126,214-126,238)
- When paralleling packs, tie common-port batteries together and split to dedicated charge/discharge plugs, but if one pack has a separate charge lead you must charge through that port—forcing 15 A through a 5 A-rated charge jack or a full common-port pack can blow fuses or the ESC during regen.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L126214-L126238】

### Use Neutral RTVs like Kafuter 704 or Mannol 9915 for Cable Glands (Lines 126,231-126,248)
- For sealing harness exits, techs prefer neutral-cure RTVs such as Kafuter 704 or Mannol 9915; generic hardware-store sealants dry too rigid, fail to grip insulation, or become impossible to service.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L126231-L126248】

### Stock BMS Sleeps Without Controller Handshake; Wake It via OEM Harness and 3.3 V Logic (Lines 126,300-126,318)
- Bench-testing Xiaomi packs requires the original controller harness: the BMS waits for ESC UART polling (3.3 V open-drain) and may indicate a weak cell group when it “sleeps,” so read group voltages through the plastic before assuming the pack is dead.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L126300-L126318】

### Air Shock Tuning Requires Correct Leverage and Dual-Chamber Pressures; Consider Softer Coils (Lines 129,205-129,330)
- Dual-chamber air shocks that feel rigid often suffer from wrong leverage or trapped pressure—bleed both chambers, experiment with 4/3 bar settings, ensure alignment, or even flip the shock to change leverage; if sag still stays at ~3 mm, swap to ~200 lb 165 mm coils for 0.5 inch sag and usable travel instead of fighting 700 lb springs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129205-L129330】

### Pouch E-Bike Modules Are Less Crash-Safe Than Cylindrical Cells (Lines 129,363-129,365)
- Denis okayed reusing ribbed e-bike pouch packs but warned they are less impact-resistant than round cells, so enclose them carefully and never puncture energized pouches during repackaging.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129363-L129365】

### A 2 m Brake Hose Reaches Pro 2 Suspension Conversions (Lines 129,366-129,367)
- A 2 m hydraulic line is long enough to route cleanly on a Pro 2 fitted with suspension, simplifying replacement planning.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129366-L129367】

### Source Ferrofluid from Specialist Vendors (Lines 129,374-129,381)
- Builders recommended buying motor ferrofluid from Grin Technologies or Nexun instead of AliExpress when European stock is needed.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129374-L129381】

### Use Rita or a Unified Controller When Mixing 36 V and 48 V Packs (Lines 129,384-129,401)
- Denis’ crew insisted that combining 36 V and 48 V packs demands Rita or an aftermarket controller—without it you must run a single battery chemistry, or move to VESC hardware sized for the combined voltage.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129384-L129401】

### Two-Piece Crash Sliders Protect Exposed Motor Leads (Lines 129,404-129,405)
- To shield externally routed motor cables, install split crash bungs that clamp around drilled axles or swingarms; single-piece sliders cannot be retrofitted without cable removal.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129404-L129405】

### Seat Offset Tires with Pressure Cycling, Massaging, and Talc (Lines 129,416-129,449)
- Stubborn tires straighten by inflating to 4–5 bar, riding or massaging the carcass, then repeating with talc-dusted tubes to let the bead glide into place; expect to deflate and reposition multiple times.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129416-L129449】

### High-Drain 21700 Builds Need ≥3 Ah Cells (Lines 129,422-129,429)
- Denis rejected Samsung 33J cells for performance packs—high-current 21700s cluster near 3 Ah, with builders preferring 4 Ah-class options like 40PL, 50PL, JP40, or Bak45D for both capacity and discharge headroom.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129422-L129429】

### “JST” Covers Multiple Families—Search by Brand (Lines 129,430-129,432)
- Scooter harness “JST” plugs are generic—searching the brand name is usually enough to locate matching housings and pins despite the catch-all label.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129430-L129432】

### Replace Chipped Hub Magnets and Epoxy Them in Place (Lines 129,434-129,453)
- Damaged Monorim magnets should be swapped, then re-bonded with dedicated magnet epoxy; running with missing chunks skews the magnetic field and risks further failure.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129434-L129453】

### External 12 V Packs Can Trip Stock Controllers (Lines 129,454-129,465)
- Riders adding 12 V serial boosters to Xiaomi controllers reported shutdowns under hard throttle—admins blamed undersized add-on BMS hardware and urged full controller capacitor/SMD upgrades before exceeding 12 s.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129454-L129465】

### Serial Booster Packs Must Exceed Stock Capacity (Lines 129,468-129,473 & 129,653-129,675)
- Supplemental 3 s packs need more usable capacity than the factory battery to prevent reverse charging; even then, serial mods remain range-limited, stress ESCs, and demand meticulous charging discipline—most techs still recommend a purpose-built pack instead.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129468-L129473】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129653-L129675】

### Fit Boyueda S3s with Shimano Calipers and E-Brake Levers (Lines 129,474-129,488 & 129,739-129,741)
- For Boyueda brake swaps, techs favor Shimano calipers plus compatible “Goodtaste” e-brake levers so the controller cuts power; Zoom kits were discouraged and banjo compatibility must be verified when reusing existing hoses.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129474-L129488】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129739-L129741】

### Bleed and Match Fluids When Changing Levers (Lines 129,512-129,527)
- Expect to top off mineral oil and bleed lines after lever swaps, and never mix DOT and mineral systems—identify the fluid before ordering parts.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129512-L129527】

### Do Not Series 36 V and 48 V Packs on a G30 (Lines 129,532-129,537)
- Denis flatly rejected stacking 36 V and 48 V packs to chase 72–84 V on Ninebot controllers; those experiments belong on high-voltage VESC builds instead.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129532-L129537】

### Source Replacement Hydraulic Hose by Brand (Lines 129,539-129,544)
- Shimano-compatible hoses are sold by the meter at bicycle shops, but Tektro hardware needs proprietary tubing—plan sourcing before ordering budget brake kits.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129539-L129544】

### Packs that Only Run with a Charger Point to BMS Faults (Lines 129,549-129,550)
- A scooter that powers up only while plugged into its charger indicates a failing BMS or power-stage issue that needs diagnosis before reuse.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129549-L129550】

### Upgrade Xiaomi Controllers with Cooler NCE MOSFETs (Lines 129,553-129,563)
- For 17 s/60 A ambitions, builders cited NCE8295A (≈82 V, 95 A) and similar NCE devices as better heat performers than IRFB4110s, provided the rest of the power stage is reinforced.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129553-L129563】

### Denis Ships 48 V Packs Half-Charged; 2 A Charging Takes ~14 h (Lines 129,575-129,589)
- New 48 V batteries leave Denis’ shop at roughly 50 % state of charge for safety; his 2 A charger needs about 14 hours for the 28 Ah pack, so riders often source a 5 A unit for faster turns.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129575-L129589】

### Keep the ESC Ground on the Stock Battery in Serial Mods (Lines 129,591-129,608)
- Error 21 and controller damage stemmed from routing the controller ground through add-on packs—always feed the ESC ground from the original BMS that handles comms, and only bring the booster’s positive into the series harness.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129591-L129608】

### Default XiaoDash Profiles Work for 48 V G2 Conversions (Lines 129,869-129,871 & 130327-130328)
- Denis confirmed the stock XiaoDash configuration runs fine after installing his 48 V G2 pack—no special tuning is required unless you chase custom performance modes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129869-L129871】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130327-L130328】

### Revive Sleeping Packs by Jump-Starting and Resetting the BMS (Lines 129,678-129,688)
- Bargain batteries that sat outside can often be resurrected: measure cell groups, ensure they exceed ~2.5 V, trickle the pack via the discharge port for 10 minutes, then press the BMS reset to wake it.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129678-L129688】

### Monitor Motor Heat When Pushing 1.6–1.9 kW (Lines 129,645-L129652 & 129,670-L129671)
- Xiaomi stators can swallow 1.6–1.9 kW bursts on stock phase wires, but techs cautioned to watch for overheating—extended abuse has melted components for careless riders.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129645-L129652】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129670-L129671】

### Ensure Controllers Have Proper Thermal Paste and Clamping (Lines 129,691-L129726)
- When one Xiaomi controller thermal-cut at 50 °C, admins pointed to poor heat transfer—scrape, paste, and firmly screw the case so temperatures stay in the high-20s even at 50 A draws.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129691-L129726】

### Tame Charger Sparks with Current-Limited Supplies or Anti-Spark Plugs (Lines 129,786-L129834)
- Lab supplies should be set to current-limit before connecting, and cheap chargers lacking inrush protection benefit from anti-spark XT60s or plugging into mains before the battery to avoid burnt connectors.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129786-L129834】

### Use AliExpress Image Search to Source Copper-Nickel Strip (Lines 129,836-L129849)
- Builders hunt for premade copper-nickel “sandwich” strip by reverse image-searching on AliExpress Choice listings, which often unlock region-specific stock and free shipping.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129836-L129849】

### Arrange Forwarders or Use JBD When Happy BMS Won’t Ship (Lines 129,850-L129854)
- Denis cannot send Happy BMS hardware to Indonesia or Vietnam; locals either recruit a reshipper or pair ScooterHacking Utility with JBD smart BMS units as a substitute.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129850-L129854】

### Check Cell Voltages When G30 Packs Stall at 40 V (Lines 129,872-L129878)
- If a G30LP charger stops at ~40 V, verify cell groups with a phone app—fast-charge-only habits usually cause imbalance, so ride gently then rebalance with the 2 A stock charger.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L129872-L129878】

### Burned 120 Ω Data Resistors Kill BMS Telemetry (Lines 130,114-L130,118)
- Missing battery bars and cut-outs on Xiaomi dashboards often trace to the pair of 120 Ω resistors near the ESC data plug; replace them before blaming the pack.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130114-L130118】

### Denis’ XT60+UART Harness Lets You Tune Happy BMS Packs (Lines 130,119-L130,121)
- The accessory harness with XT60 and 4-pin connector is meant for PC monitoring—plug it into the battery to adjust settings or log pack data via software.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130119-L130121】

### Set CC/CV Step-Up Modules Before Charging Other Packs (Lines 130,122-L130,145)
- Charging a 12 s pack from 10 s needs a CC/CV boost converter; adjust the trimmers for output voltage, current limit, and input cutoff so you do not blast stock scooters with uncontrolled amperage.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130122-L130145】

### G2 Controllers Are Limited by 63 V Capacitors (Lines 130,304-L130,307)
- Builders pegged the G2’s safe ceiling at 48 V packs because the controller uses 63 V capacitors; any higher voltage or regen spikes require upgrading those caps.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130304-L130307】

### Denis’ 48 V Pack Does Not Fit the G3 Without Custom BMS Work (Lines 130,168-L130,175 & 130,493-L130,495)
- Denis confirmed G2 and G3 scooters differ too much for a drop-in swap—G3 upgrades will need bespoke BMS solutions, with Denis targeting a release later in the year.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130168-L130175】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130493-L130495】

### Pop G2 Displays with Suction Cups to Avoid Damage (Lines 130,180-L130,190)
- Removing a glued G2 dashboard requires a suction cup or careful screw-anchor prying—the cluster is stuck with adhesive and cracks if forced from the edges.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130180-L130190】

### External G2 Packs Need SHFW with Charging Mode Disabled (Lines 130,338-L130,360)
- Denis advises paralleling reputable 10 s packs via Y-cables for G2 range boosts, but only after flashing SHFW with charging mode disabled; avoid low-quality Ali/CityaLion packs and keep voltage chemistries matched.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130338-L130360】

### Align Two Chargers Before Parallel Charging a Pack (Lines 130,507-L130,510)
- You can charge a single battery with multiple chargers if their combined current stays under the BMS limit—bring the higher-voltage unit online first, equalize pack voltage, then parallel both chargers.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130507-L130510】

### Use the PAP03/PAP05 Harness to Run Xiaomi Tail Lights Without the BMS (Lines 130,513-L130,520)
- When the stock BMS is absent, tap the controller’s PAP03-V (BMS/rear light) connector and verify voltage with a multimeter to power the taillight directly.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130513-L130520】

### Estimate Charge Time with Amp-Hour Math (Lines 130,529-L130,532)
- Charging duration is simply battery Ah divided by charger current—e.g., a 20 Ah pack on a 5 A brick takes about four hours.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130529-L130532】

### Pick Loctite Strengths Carefully and Consider Nord-Lock Washers (Lines 130,534-L130,539)
- Loctite only needs a drop—drenching hardware or using the strongest grades fuses threads—while Nord-Lock washers add 20–30 N·m of anti-loosening force for high-vibration assemblies.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130534-L130539】

### Happy BMS Is Verified on 10s7p G2 Packs (Lines 130,543-L130,545)
- Denis confirmed Happy BMS runs reliably in 10 s 7 p Max G2 builds and shared a supporting walkthrough video for installers.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130543-L130545】

### Reinforced Xiaomi Controllers Remain the Go-To Compact 36 V Upgrade (Lines 130,546-L130,554)
- When riders want the smallest 36 V high-current controller, experts still recommend reinforced Xiaomi boards paired with SHFW—they’re cheaper and more adaptable than generic alternatives or VESCs for modest builds.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130546-L130554】

### Motor Temp Sensors and XiaoDash Modes Need Monitoring After 48 V Swaps (Lines 130,429-L130,490)
- G2 hubs include NTC sensors viewable on the dashboard; Denis warned 48 V packs can trigger error 51 if you hold full throttle uphill, and SHFW sport mode currently applies extra multipliers—use drive mode for predictable current until firmware updates land.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130429-L130490】

### Xiaomi Motors Use 30 Poles for VESC Configuration (Lines 130,496-L130,498)
- When configuring a Xiaomi hub on VESC, set pole pairs for a 30-pole stator to keep telemetry accurate.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130496-L130498】

### Rita Alternates Packs per Its Manual (Lines 130,503-L130,506)
- Newcomers wondering about Rita pack behavior were directed to Denis’ manual, which details how the adapter balances and schedules internal versus external batteries.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130503-L130506】

### Wake Dormant Smart BMS Boards by Plugging in a Charger (Lines 130,583-L130,592)
- If a freshly built pack shows 0 V on charge leads yet cells sit around 3.6 V, Denis recommends connecting a charger to kick the smart BMS awake before deeper debugging.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130583-L130592】

### Verify Caliper Clearance Before Adding Hydraulic Brakes to the M365 (Lines 130,593-L130,598)
- The community cautioned that M365 hydraulic conversions hinge on hardware fit: dashboard glitches blamed on EMI usually trace to water ingress, while brake swaps demand careful disc and caliper sizing before ordering parts sight unseen.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130593-L130600】

### Preheat MP2 VESC Boards and Strain-Relieve Heavy Leads (Lines 130,602-L130,646)
- Builders struggled to wet MP2 power pads until they preheated the PCB to ~170–190 °C with a hot plate or hot air, switched to higher-mass tips with leaded solder, and anchored thick 8 AWG leads so vibration would not rip fragile traces from the board.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130602-L130646】

### Cure Kukirin G4 Stem Rocking by Overhauling the Folding Assembly (Lines 130,616-L130,635)
- Chronic stem play on Kukirin G4 scooters comes from loosening bolts throughout the folding stack; veterans advise inspecting every fastener, replacing the entire hinge module if wear persists, and documenting movement with video before riding again.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130616-L130635】

### Match Brake Caliper Orientation on Boyueda S3 Installs (Lines 130,626-L130,635)
- When Nutt hydraulic calipers would not bolt up to a Boyueda S3, admins explained the scooter uses right-side mounts—rotate the wheel or source a mirrored caliper, and expect to shorten over-long hoses during the retrofit.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130626-L130635】

### Respect Constant-Current Headlight Drivers and 6 V BLE Rails (Lines 130,648-L130,662)
- Xiaomi Pro 2 headlights rely on controller current limiting rather than a fixed 3.3 V rail, so modders should measure load current, avoid back-feeding 5 V from the throttle, and remember the BLE board itself is powered by 6 V when planning accessories or step-downs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130648-L130662】

### Reflash Xiaomi BLEs with SHU Reflasher or ST-Link—Skip DownG (Lines 130,664-L130,693)
- Owners correcting misidentified dashboards were urged to edit SHU Reflasher packages or hard-flash with an ST-Link; using the legacy DownG app often bricks GD32 boards, so stick with ScooterHacking Utility’s downgrade workflows for safe firmware swaps.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130664-L130693】

### Configure Rita via Older BLE Firmware or CP2102 UART When Apps Fail (Lines 130,781-L130792)
- Rita adapters refuse to pair with Xiaomi dashboards on the newest BLE firmware; Denis now recommends downgrading via SHU or programming the unit over USB-UART (prefer CP2102 adapters with white-to-RX, yellow-to-TX, black-to-GND wiring) using his Windows tools.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130781-L130792】

### Replace Fried 100 Ω Data Resistors Before Relying on Rita (Lines 130,793-L130,824)
- Error 21 and Rita lockouts after high-speed runs were traced to burnt 100 Ω resistors on the controller’s white/yellow UART lines; Denis warned that bypassing them with a BMS emulator leaves regen uncontrolled and can literally explode the Rita, so fix communication before riding.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130793-L130824】

### Validate Controllers with Known-Good Parts After Rita Faults (Lines 130,830-L130,849)
- When a Rita-equipped Pro 2 began spamming random codes and killing a BLE, Denis advised swapping in trusted dashboards and ESCs one at a time and keeping Rita draw under ~30 A with modest field weakening until the hardware proves stable.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130830-L130849】

### Happy BMS Misreads LiFePO₄ Packs Until Recalibrated Above 3.5 V (Lines 130,894-L130,907)
- The Happy BMS coulomb counter assumes 4.1 V lithium-ion cells; LiFePO₄ packs show 5 % state-of-charge until charged beyond 3.5 V/cell, after which the firmware relearns capacity—use Denis’ included USB dongle or web app to monitor settings on modern Android devices.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130894-L130907】

### XiaoDash Defaults Suffice for 48 V G2 Upgrades, with 30 A Continuous Limits (Lines 130,909-L130,949 & 130932-L130,935)
- Riders chasing 48 V performance on the Ninebot G2 were told to leave SHFW settings stock: Denis’ packs ship preconfigured, cap current near 30 A continuous/39 A peak, and include a USB dongle for optional tweaks—sport mode or CFW questions belong in ScooterHacking groups.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130909-L130949】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130932-L130935】

### Stock G2 Motors Handle 48 V Better Than Monorim Swaps (Lines 130,994-L131,001)
- Denis and other techs reiterated that the factory G2 hub survives 48 V without drama, whereas Monorim-branded replacements have poor dropout alignment, mismatched hall layouts, and underperform versus genuine Ninebot motors.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L130994-L131001】

### VESC Brake Harnesses Need Seven Conductors and Shielding (Lines 131,003-L131,013)
- Converting Xiaomi controls to VESC requires more than the stock four wires—builders add ADC leads plus 3.3 V power and shielded cabling to keep digital brake signals clean when layering extra accessories.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131003-L131013】

### Ninebot Rental Packs Stay Locked Without Vendor Keys—Use JBD2G30 Bridges (Lines 131,019-L131,068)
- Attempts to reuse VOI nee1009-W batteries fail because Ninebot embeds vendor passwords; Finn’s JBD2G30 bridge lets hobbyists mate JBD BMS hardware with classic G30 controllers, but it still cannot unlock newer CAN-based Ninebots or SNSC rentals without matching IDs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131019-L131068】

### Generate 13S7P Cell Holders with Lekrsu’s Python Tool (Lines 131,073-L131,089)
- Lekrsu shared a GitHub script for printing customizable cell holders—run `python3 test.py 385 125 0.43 21.4 0.4 true true 2 true true` (dimensions, wall width, cover thickness, etc.) to adapt 13S7P packs for Xiaomi chassis, then split prints as needed.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131073-L131089】

### Diagnose Sudden Motor Drag by Inspecting Phases, Halls, and Thermal Damage (Lines 131,092-L131,136)
- When BLDC hubs topped out at 10 km/h, troubleshooters checked controller settings, phase continuity, hall sensor phasing, and heat damage—burned phase wires, demagnetized rotors, or mismatched 60° sensors all cause the symptoms observed after overheated rides.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131092-L131136】

### Replace the Pro 2 Tail-Light Inductor When Brightness Fades (Lines 131,104-L131,135)
- A dim Mi Pro 2 brake light was cured by jumping or replacing the L3 inductor on the lighting PCB; technicians noted multiple coil variants exist, so inspect the board and be ready to scavenge donor controllers if the part is unavailable.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131104-L131135】

### ESC 3.0 Reinforcement Still Caps Voltage at 13S Without Divider Mods (Lines 131,144-L131,178)
- Even heavily reinforced ESC 3.0 builds remain limited to 13S unless you swap the voltage-divider resistors (R41/R44) and upgrade supporting components; tin overlays add little conductivity, so monitor motor temperatures and consult the community mod guide before chasing 14S packs.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131144-L131178】

### Parallel Batteries Within ~1 V to Protect G2 Controllers (Lines 131,179-L131,185)
- Owners paralleling internal and external Max G2 batteries were told that a 1 V mismatch is acceptable—G2 packs sometimes rest below 42 V—so connect chargers in parallel only after equalizing voltages to spare the BMS from inrush spikes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131179-L131185】

### Glue Hall Sensors with RTV or Epoxy During 13S Rita Builds (Lines 131,261-L131,276)
- Escaping hall sensors in high-voltage projects were secured with silicone or heat-resistant epoxy; 704 RTV from AliExpress is the go-to, though it cures slowly, and builders scuff the stator slots before bonding for better adhesion.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131261-L131276】

### Estimate 38 Ah Charge Times via Amp-Hour Math and 5 A Limitations (Lines 131,276-L131,307)
- Newcomers planning 38 Ah Max G2 packs learned to divide capacity by charger current—about 13 h on the 3 A stock brick or 7.5 h on a 5 A “speed cable”—and Denis confirmed he currently ships batteries without chargers until new stock arrives.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131276-L131307】

### Buy Complete Sensor Boards for Pro 2 Motors and Plan Brake Hardware for Dual Drives (Lines 131,308-L131,313)
- Rather than swapping single hall elements, Denis’ crew recommends buying full sensor boards matched to your motor style; dual-motor Xiaomi builds also need Monorim disc adapters up front because the classic frame leaves little space for rear calipers.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131308-L131313】
