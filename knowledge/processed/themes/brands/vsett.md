# VSETT Performance Scooter Dossier

## TL;DR

- VSETT 10+ frames remain one of the stiffest production stems—only two rear shock mount failures were logged before the factory revision—and relocating controllers to the neck frees the deck for 20 S 9 P 21700 packs without compromising rigidity.[^1]
- The 92 mm stator VSETT 9 motor (15 pole pairs, 0.5 mm air gap) hits the sweet spot for 10-inch comfort and is still sourced around €120 inside the EU, making it a go-to upgrade hub.[^2]
- Artem’s field logs keep PMT 10×3 at the top of the tire list (≈48 psi target) with CST 10×3 as the budget runner-up; expect egg-shaped carcasses on narrow rims but manageable ride quality.[^3]
- Split rims simplify roadside service—each half separates once the axle nuts are off—so keep spare halves, bearings, and stators handy for pothole-induced wobble hunts.[^4]
- Matris dampers paired with PMT tires and EXA shocks deliver rock-solid steering, but beware clones from FalconPEV/AliExpress/Amazon; genuine units run ~€250 and require inspection before trust.[^5]
- Launch torque hinges on tuned current ramps and PID gains—community recipes (FOC redetection, 20 kHz switching, hall interpolation, unchecked current limits) recovered punch while trimming ~100 A from full-throttle pulls once logs validated the new curves.[^6][^7]
- Stock 140 mm rotors fade quickly on high-power builds; 160 mm SRAM Cleansweep or Magura MDR-P discs plus proper banjo hardware transform braking torque and heat rejection for dual-motor commuters.[^8][^9]
- Factory 9+/10+ and Kugoo G4 packs are paired right at their controller ceilings; riders log severe sag, speed loss, and wobble complaints until higher-discharge packs replace the stock modules.[^10]

## Platform Notes
### Frame & Packaging

- Neck-mounted controller relocations open enough deck volume for 20 S 9 P 21700 packs while maintaining stem stiffness, giving commuters long-range options without external battery boxes.[^1]
- A documented VSETT 10+ build squeezes a 20 S 9 P Samsung 48X pack (≈43.2 Ah, ~150 A max discharge) alongside dual Nucular 12F controllers once the deck is reorganised, cementing the relocation playbook.[^20a]
- Rental-grade Xiaomi conversions borrowing VSETT hardware add roughly 10 kg with thick stems and oversized fork hardware; expect a sturdier but less portable chassis once dual brakes and battery bays are reinforced.[^11]
- Artem is confident the Vsett 9 chassis swallows 52 V 30 Ah packs—and even vertical 20 S 8 P trays with spacers—for ~160 km range while keeping everything internal, so plan wiring harnesses with the extra volume in mind.[^12]
- Packaging experiments now map an 18 S 7 P layout (395 × 151 × 49 mm, 66.6 V/24.5 Ah) that drops straight into VSETT 9 decks without spacers, giving compliance-focused riders stealth high-voltage options.[^pack_18s7p]
- Fresh bay surveys put the VSETT 9 cavity around 154 × 455 × 49.5 mm with rounded ends; a 25 mm spacer fits 19 S 7 P stacks while 50 mm risers squeeze 20 S 6 P Xiaomi builds at the cost of ground clearance.[^ip001-deck-map]
- Yoann’s Vsett 10 dual Lite conversion keeps the stock lighting loom by using the ADC 5 V rail to drive a relay that wakes a separate 12 V converter; their 72 V battery mod reuses a Nami 80 A BMS that trips near 120 A, so total pack current stays around 100–120 A while Lisp code blends phase amps versus ERPM to manage wheelspin.[^13]

### Motor & Wheel Options

- Stock VSETT 9 hubs feature 92 mm stators, 15 pole pairs, and a tight 0.5 mm air gap—pair them with the taller 10-inch carcass to smooth harsh pavement while keeping torque respectable.[^2]
- Artem now pegs the Vsett 9 hub around 48 km/h on 52 V (≈58 km/h dual) and says the 10+ wheel needs 60 V to shine; expect muted top speed on 48 V despite its ~130 A/50 A thermal headroom and 1 400 W nominal rating.[^14]
- Build a reference card for Vsett 9/10 hubs—52 V vs. 60 V speed, split-rim service order, and shipping options—so 48 V riders know the upgrade path before committing to 60 V hardware.[^vsett_map]
- Ignore marketing wattage on Vsett 10+ motors—inspect winding fill and magnet stack height before pushing phase amps or buying donor wheels for AWD conversions.[^15]
- Paolo is distributing 6 mm (≈9 AWG) motor leads rated around 3 kW continuous per hub, giving retrofitters a vetted harness option when Vsett 10+ spares pop up.[^paolo_leads]
- Recent teardowns logged 9×7 slot/pole counts, 0.5 mm laminations, and RUWH 6003RS bearings; blank front covers from Vsett 9 rentals can disguise dual-motor conversions by hiding the second hub’s wattage rating during inspections.[^16]
- Vsett 9+/10+ hubs comfortably burst near 5 kW when temperature sensors track sustained loads, so treat the “600 W” label as commuter-only marketing and log temps before upping duty cycles.[^17]
- Stock hub hardware has already endured serious power—the community logged 10–12 kW pushes on OEM motors before Nucular 12F limits intervened—so thermal headroom comes from cooling and harness upgrades rather than immediate motor swaps.[^18]
- Split rims allow tire swaps without disconnecting harnesses, but install 6 mm bullets on phases plus 6-pin Higo/Julet blocks for halls and thermistors to simplify maintenance.[^19][^20]
- Split rims allow tire swaps without disconnecting harnesses, but install 6 mm bullets on phases plus 6-pin Higo/Julet blocks for halls and thermistors to simplify maintenance.[^21][^20]
- Owners chasing temperature telemetry on Vsett 10 hubs still have to source six-pin motor looms (often from AliExpress) because the stock harness omits the thermistor pair—budget bespoke cabling alongside controller upgrades.[^22]
- Kaabo-sourced hubs vary: square-wave throttle kits often ship hall-less while sine-wave GT packages include sensors—verify before planning regen-heavy controller swaps.[^23]
- Bench jigs that see ≈28 mΩ across two phases (≈14 mΩ per phase) flag healthy Blade/VSETT hubs—use the fixture for repeatable QC before buttoning up builds and still rerun VESC detection to capture in-ride inductance shifts.[^24]
- VSETT 10 motors share the 50 mm stator Laotie uses; they bolt straight into G30 swingarms but still lack a tubeless 10″ option, pushing commuters toward heavier 11″ conversions when they want fatter rubber.[^25]
- Swapping Zero 10X hubs into Vsett frames changes the ride entirely—the Zero windings run lower kV for torque while Vsett sticks with higher-kV speed winds, so budget gearing and controller tweaks if you trade between the platforms despite the shared axle width.[^26]
- Salvaged OEM hubs still ship with 40 H stators, so expect Lonnyo-class thermal limits when transplanting them into custom frames or dual-drive conversions.[^27]
- When doubling 10 AWG phase leads, Haku defaults to 10 mm bullet connectors; forcing the bundle into 8 mm shells demands soldering and shaving the joint, so size connectors before committing to doubled conductors.[^28]
- “SHDC” castings show up across Kaabo/Nanrobot supply chains and will add hall sensors on request; Wolf GT owners confirm newer sine-wave motors arrive with halls while Kelly conversions retrofit them for reliable starts.[^29]
- Xiaomi and VSETT hall boards aren’t interchangeable—the Vsett 10+ rotor spacing keeps Xiaomi controllers from running the hub smoothly even after sensor swaps, so plan controller changes instead of chasing hall geometry fixes.[^30]
- HM and Blade “limited edition” hubs share the ~135 mm axle spacing, so they drop straight into VSETT 10/G30 swingarms once spacers are trimmed; SibClimb and Paolo’s EU storefronts are the go-to sources when you need the higher-torque windings.[^31][^32]
- Limited-edition VSETT 10+/Zero 10X hubs even ship with dual phase leads and higher-Kv winds; riders meter them with YR1035s and budget roughly €180 per replacement motor plus shipping.[^ip001-limited-leads][^ip001-limited-price]
- Dual-phase “limited edition” hubs are also throwing ~270 A recommendations during auto-detect instead of the usual 120–130 A; cap manual limits near 200 A until Spintend updates the estimator.[^ip001-dual-phase-detect]
- HM-branded hubs demand ≥50 A battery to feel lively yet run noticeably hotter than comparable LY winds, so high-power conversions with identical fork spacing keep favouring the lower-KV LY motors for better thermal margin.[^33]
- Budget dual-motor swaps are back on the menu: Paolo is selling Blade hubs for about €200 each (≈€520 with PMT slicks) and even offering shipping tricks—declare warranty parts and skip UPS, which has lost multiple high-value parcels.[^34]
- Paolo’s 60 mm magnet Blade hubs are already holding 85 A battery on 16 S and targeting 20 S tests; expect to lean on ferrofluid and active cooling before chasing higher voltage because the same motor survived 130 A battery/350 A phase only after aggressive thermal prep.[^35]
- Factory star-point solder still needs QA—torch off lacquer, brush clean, and reflow the joints before re-running motor detection to cut resistance and heat on refurbished VSETT stators.[^36]
- Inspect “new” OEM hubs before installation—one VSETT motor shipped rusty with loose magnets, and the community now strips corrosion and bonds magnets back with Loctite AA326 before reuse.[^37]
- Fresh 60 mm VSETT hubs respond well to ferrofluid fills and careful clamping; riders are comfortable around ~50 A battery and 100 A phase once the stator is rewrapped and torqued correctly.[^38]
- High-torque 11-inch hubs start shedding magnets when hammered with sustained 200 A+ phase current—dial back current or expect heat-driven failures on VSETT conversions pushing that envelope.[^39]

### Harness, Display & Control Integration

- The factory “DS” conductor backfeeds display power into the controller once the RFID tag authenticates; keep the line intact when repinning harnesses so the throttle stays analog while CAN-style messages update ride modes every 200–500 ms.[^vsett_ds_harness]
- Dual-motor enable traces share continuity between the handlebar button, display, and controller, so VESC swaps must preserve that signal path or the dash will light up without actually waking the slave controller.[^vsett_dual_enable]

### Tire, Pressure & Maintenance Guidance

- Run PMT 10×3 near 48 psi for grip; CST 10×3 tubeless remains the cost-effective choice but bulges into an egg on narrow rims. Stock CST beads run small—seat them carefully to avoid wobble.[^3]
- Rougher US streets are pushing riders to 43–45 psi on PMT 10×3 tires to stop bending rims, even though smoother European pavement still lets commuters run closer to 30 psi for grip.[^ip001-pmt-psi]
- PMT casings are tubeless-ready yet tolerate inner tubes (CST 10×2.5 pairing works); the stiff carcass can even limp home deflated for short distances, which is handy for roadside repairs.[^40]
- Keep spare split-rim halves and bearings—pothole hits can ovalize the shells, so swap components methodically until vibration disappears, documenting tire experiments to isolate causes.[^4]
- Track pressures by rider weight: PMT slicks stay happy near 2.4 bar, Vsett racers run ~3.5 bar, and dropping to 1.8 bar shreds cords while 4.2 bar CST setups lose grip—log PSI alongside rider mass when comparing setups.[^41]
- CST 10×2.5 inner tubes have proven durable across months of mixed on/off-road use and are thick enough for 10×3 tires, but 20 S setups still shred them quickly if pressures stay low—log PSI after hard rides.[^42]
- Persistent flat-prone builds respond well to Vsett 10 inner tubes—Haku already stretches the larger tube onto Ninebot G30 conversions to avoid thin-tube blowouts.[^43]

### Compliance & Insurance Notes

- Scandinavian insurance rules still push stealth builds: Denmark offers no theft coverage above ~20 km/h, Sweden limits legal scooters to 250 W/20 km/h with pedal assist, and Finland sells €50–€70/year policies that lift limits to roughly 1 kW when throttles stay discreet.[^scand_rules]

### Steering & Stability Hardware

- **Inspect 10-series steering columns for thin-wall cracks.** Photos show the lower weld splitting along the slender extrusion, so retrofit thicker Warrior stems or add machined sleeves before cranking up power levels.[^44]
- Triangulated neck brackets tying Matris dampers into PMT tires and EXA shocks eliminate wobble on VSETT 10 builds; ensure at least three anchor points instead of relying on the flex-prone stock tab.[^45]
- Genuine Matris dampers ship around €250 and need inspection—budget clones from FalconPEV, AliExpress, or Amazon masquerade as Matris/Öhlins but lack consistent internals.[^46]
- A 20-mile shakedown on a bar-mounted damper eliminated wobble at 45–50 mph but highlighted how overly stiff settings slow emergency swerves and tight manoeuvres—tune damping for stability without killing agility.[^ip001-damper]
- Reports of VSETT 10 motors holding 63 mph on 20 S while Blade frames wobble without real dampers sparked renewed warnings to verify genuine Matris hardware or fabricate three-point mounts; counterfeit kits from Falcon-branded sellers keep surfacing.[^ip001-highspeed]
- Reserve dampers for robust frames—Monorim-equipped Xiaomi forks remain only ~4 mm thick, making 90 km/h runs suicidal without serious reinforcement.[^47]
- **Chasing a post-service “clunk.”** Loud knocks that appear between braking and throttle after wheel bearing work usually trace to loose axles or missing torque washers; snug hardware and fit proper torque arms before assuming controller faults.[^axle-clunk]
- Sharkset’s adjustable cockpit kit (~$100 in Germany) pairs cleanly with Magura MT8 SL brakes (~€200 per wheel) and Kool Stop sintered pads on 17 S builds—budget grinding the stock clamp and planning for higher braking loads when you make the swap.[^ip001-sharkset]

### Performance & Telemetry Benchmarks

- Fresh Dragy runs clocked a VSETT 10 at 0–60 km/h in roughly 4.75 s and 0–80 km/h in 7.5 s using 78 A/200 A rear and 70 A/130 A front profiles (~148 A battery combined, 196 A rear phase); even with motors staying near 130 °F, riders flagged chassis control as the new limiting factor at those tune levels.[^48]
- Stock VSETT 8+ controllers have tolerated jumps from 13 S to 17 S (≈63.6 V) without hardware mods, netting roughly 30 % more power, though riders now compare those results against Ubox dual builds and caution that 20 S/field-weakening pushes require aggressive cooling.[^ip001-stock-17s]
- Correct VSETT 9 speed readings on Ubox builds require entering 15 pole pairs (not 30 poles) and shrinking the wheel diameter to ~210 mm to account for tire compression, otherwise the dash reports barely 28 km/h instead of the real ~55 km/h on 60 V packs.[^speed_cal]
- Shlomozero keeps Vsett 1400 W hubs above ~55 A phase and caps battery current near 25 A around the stock BMS; Christophe settled on 130 A motor and 45 A battery limits to keep his Spintend 85 V swap reliable around 50 km/h cruise speeds, plus real regen braking.[^49][^50]
- Ubox speed readings stay honest only after setting 15 pole pairs (instead of 30 poles) and shrinking wheel diameter to ~210 mm for tire squish; skipping the tweak leaves the dash stuck near 28 km/h on 60 V packs even when the scooter is really doing ~55 km/h.[^51]
- Treat aerodynamic tweaks as meaningful range levers—commuters logged 63–65 Wh/km in calm weather that jumped to ~72 Wh/km when battling headwinds in bulky winter jackets, illustrating how rider silhouette nearly doubles energy draw even when electrical settings hold steady.[^52]
- Field-weakening is staged carefully on dual builds: crews activate 87.5–89.5 % duty and +25 % throttle curve on the rear before bringing the front online around 93 % to avoid simultaneous current spikes while still gaining a modest 8 km/h at the cost of doubled power draw.[^53][^54]
- The community’s new LT-01/QS-S4 Lisp driver mirrors UART telemetry and expects throttles to stay under 3.3 V; add resistor dividers or the dash’s safe-start logic trips and ADC rails risk over-voltage when swapping controllers.[^55][^56]
- Ferrofluid (≈6 ml Statorade) keeps dual 1.4 kW hubs under ~40 °C on 16 S routes that previously hit ~63 °C, but heat shifts into the magnets—long climbs still need logging to avoid saturation.[^57][^58]
- Unsealed Vsett 9 decks remain risky in sustained rain; riders either pot electronics or tear them down immediately for ingress checks if they have to commute through storms.[^59]
- Haku stays wary of bargain FarDriver 450 A controllers on VSETT-class hubs—he expects their current ceiling to cook standard scooter motors unless you’ve validated thermal headroom, so treat them as experimental hardware.[^60]
- If a 17 S build free-spins slower than the old 16 S tune, revisit pole-pair counts and duty caps—identical VSETT motors should spin faster with more voltage, so firmware misconfiguration is the prime suspect.[^61]
- Artem’s refreshed Vsett 9 now runs dual 650 W hubs on a 16 S 8 P Samsung 35E pack with dual Ubox controllers, SmartController integration, LED spacers, and a GPS/4G tracker—logging 0–50 km/h in 5.5 s with only 3.6 V sag at 27 A battery and 80–85 A phase per motor while highlighting rear-motor sync hiccups above ~85 A phase for diagnostics.[^62]
- Tuned PID ramps paired with the community’s 1200 W wizard preset and 20 kHz switching held 90 kg riders at full throttle above 30 km/h while drawing roughly 100 A less than stock tunes, underscoring how much launch maths lives in firmware rather than brute current.[^6][^7]
- Samsung 48X 20 S9 P packs are backing 10 kW bursts with only 4–7 V sag at 110–135 A and keeping 64 mph runs under ~65 °C winding temperature, so long as cell delta stays near 0.002 V after spirited rides.[^63]
- EU pack builders are quoting roughly €540–€990 for 60 V 15–40 Ah Samsung 50G packs with optional smart BMS and XT90 upgrades, providing a benchmark for internal 10-series refreshes.[^ip001-pack-pricing]

### High-Discharge Build Guardrails

- 20 S 11 P ambitions require ≥300 A of pack capability plus P42A/P45B/40T-class cells; the crew budgets roughly 250 A battery and 350–550 A phase per motor alongside 485 × 210 × 86 mm trays to unlock 20 kW-class launches without cooking the pack.[^64]
- Treat “20 kg, 157 km/h, 150 km range” marketing with skepticism—just the claimed range would need ~11 kg of cells, and even NAMI motors struggle to hold 100 km/h on 20 S without rewinds and aggressive cooling toward 27–30 kW continuous output.[^65]

### Launch & Field-Weakening Experiments

- Genuine field-weakening toggles remain locked to FW 5.3 firmware; owners are sideloading 300 A bins and testing duty-cycle triggers near 70 % to break through the 95–98 % plateau without roasting hubs.[^66]
- Vedder Sensorless Start hides under the sensorless encoder profile and expects motor-temperature telemetry—without it, launches fall back to noisy hall-only starts that stretch 0–30 km/h runs toward five seconds on hills.[^67]
- Keep the OEM dash by flashing the community script or repurposing 10 kΩ NTCs between hall ground and an extra conductor so dual builds log motor temps without ditching the stock display.[^68]

### Battery & Enclosure Upgrades

- Relocating controllers outside the deck opens room for a 20 S9 P Samsung 48X pack inside the 10+; builders report ~2 mm side clearance in a 169 mm jig and pair the pack with JK active-balancing BMS boards and waterproof Higo/Julet harnesses for serviceability.[^69][^70]
- Community packaging logs now include 13 S 10 P Samsung 40T packs inside the 9+ deck plus parallel 20 S 6 P and 20 S 5 P MH1 add-ons (≈72 V, 32 Ah, ~100 A continuous) when space is tight—mixed chemistries demand careful harnessing and coordinated BMS balancing but keep sleeper builds rolling.[^71]
- Stock Vsett 9 commuters appreciate the removable battery and hydraulic brakes yet still flag the dated 8.5″ tubes as a reliability risk in 2024—plan tire upgrades alongside pack work.[^72]
- The flagship 20 S9 P build highlighted in late-2021 chats delivered 43.2 Ah and a 150 A discharge ceiling when matched with dual Nucular 12F controllers—the “most beast” deck-mounted configuration to date.[^73]
- A newer 20 S9 P revision barely clears the deck once controllers move outside: builders convert the controller tails to AS150, wrap the pack in Kapton/fish paper instead of full shrink for serviceability, and set a 2.5 mm thermal pad beneath so the lid clamps the pack without chafing while wicking heat into the deck.[^74]
- Harness planning matters at these pack sizes—Happy Giraffe and Koxx now run shared-ground 24–26 AWG looms or slim AliExpress harnesses for throttle/brake/start lines so the wiring clears the tight passthroughs without resorting to stiff Ethernet cables.[^75]
- Artem’s copper-clad 20 S 9 P build uses pre-welded laser-cut tabs, QS8 anti-spark connectors, and copper bus reinforcements (~$170 shipped) to fit a 168 mm-wide “W” pack inside the 171 mm deck once controllers move outside; 19 mm PVC plus 5 mm acrylic risers lift the lid for a top-mounted BMS.[^76]
- Protect every cell: wrap 21700s in heat-shrink and Kapton, slide wax/fish-paper between parallels, sheath the finished pack in epoxy board plus giant heat-shrink, and add a cradle strap so the assembly slides out for service without scuffing the deck.[^77]
- Swap the stock loom for a Higo L1019 harness when you relocate controllers—three ~11 AWG phases plus seven signal leads share a sealed 7.7 mm jacket, making 6 mm bullet terminations and temperature telemetry tidy even in tight VSETT 9 axle cavities, but retire the plug on 60–70 mm motors where the jacket no longer fits cleanly without trimming the casting.[^78][^79][^80]
- Owners measuring factory cabling are finding only ~2.5 mm² (≈13 AWG) phase copper, which stays cool around 90 A phase/30 A battery but needs 3 mm²+ upgrades; the latest QS8 anti-spark connectors arrive with 6 AWG cups, making them a better fit than AS150 hardware once dual controllers push 60 A+/135 A combined.[^81][^82]
- Spintend Ubox V1 auto-detects around 135 A while some V2 units only return ~88 A; sanity-check detection results and be ready to set manual limits before trusting new hardware.[^ip001-ubox-detect]
- Silicone-insulated 6 mm² (≈10 AWG) phase leads shrug off hub heat better than PVC jackets when rerouting harnesses, and the Higo L1019 bundle fits VSETT 9 axles once you swap to 6 mm bullets—just monitor MT60/XT150 connectors for heat on long pulls.[^78][^83]
- VSETT 9 commuters can still package 18 S7 P (395 × 151 × 49 mm, 66.6 V/24.5 Ah) without deck spacers, but Italian riders report shops relabelling motors to 500 W and carrying invoices to appease police that assume stock 650 W ratings.[^84]
- Expect roughly 5 V of sag at 70 % SOC on healthy 10+ packs; larger drops usually trace to resistive wiring or undervoltage cutoffs long before the controllers hit their phase limits.[^85]
- Community CAD work pegs the factory deck spacer at 194–195 mm outer width (170–171 mm inner), 520 mm overall length (≈458 mm inner), and 470 mm to the front bevel, with cable notches up top—dimensions that let builders CNC or print replacements when relocating controllers outside the deck.[^86]

### Logistics & Pricing Signals

- VSETT 10+ limited-edition hubs slot into Ninebot forks with minimal spreading; EU importers quote ~CHF 400 for dual motors with tires and warranty while AliExpress sellers hover around €150–€200 per motor plus €50–€170 shipping, encouraging group buys or forwarders to tame freight.[^32][^87][^88]
- French riders even mask 500 W labels by explaining the second hub as an “electric brake,” underscoring how inspectors still look for engraved wattage even when firmware limits top speed.[^89]
- AliExpress now lists OEM VSETT 10+ hubs near €159 before ~€52 freight, and French resellers are quoting €140 delivered for Blade-spec motors—regional pricing is falling but duties still dominate the landed cost.[^90]
- Tudor’s latest order of 1 200 W/50 H hubs for 17 S P42A packs highlighted how AliExpress freight can balloon without prior negotiation—forwarders or pre-arranged shipping quotes keep costs sane.[^91]
- Rion/Weped FF-spec motors are landing around €340 each through Face de Pin Sucé in France, but rising freight costs can erase the bargain for international buyers—budget shipping buffers before committing to group buys.[^92]
- Nordic compliance rules push stealth builds—Denmark offers no theft coverage above ~20 km/h, Sweden limits legal scooters to 250 W/20 km/h with pedal assist, and Finland sells €50–€70/year policies that raise legal caps to ~1 kW when throttles stay discreet.[^93]

### Brake & Hose Upgrades

- Bed sintered Kool-Stop pads with 30–60 full-power stops so they outlast the ~800 km organic cycle; keep spare 160 mm rotors on hand because the harder compound can chew ~1 mm off the disc within 1,000 km and squeals more at low speed.[^94]
- Swap the stock 140 mm rotors for 160 mm SRAM Cleansweep or even 180 mm Magura MDR-P discs to gain braking torque and thermal mass; align pads carefully and retire washer stacks for proper brackets to avoid warping the new hardware under heavy loads.[^8]
- External Magura routing needs the right banjos: the Elvedes Hydro Parts Kit provides dual M8 banjos for fork exits, while Jagwire quick-disconnects demand matching Jagwire hose runs and roughly $120–$125 in hardware for dual-motor layouts—and you still have to source the missing M6 banjo bolts separately or machine your own before 10×3 tires clear.[^95][^96][^97]
- Jagwire-style external hose reroutes have already crushed Magura MT7 lines and robbed braking until the hose was replaced; once sealed they still risk banjo rub on 10×3 tires after a flat, so revert to inline routing if clearance drops below ~5 mm and pack spare hardware for roadside swaps.[^98]
- Hope’s HFA701 kit ships the correct M6 banjos and bleed screws in one bundle; for odd fasteners, Venhill, Trickstuff, and AliExpress stock standalone M6 banjos and M5 bleeders, but most riders still buy the complete Jagwire kit to keep barb dimensions consistent.[^99]
- Premium Braking Incas 2 kits deliver 3 mm 180/203 mm rotors and CNC spacers for €675–€850, but the oversized hardware can strike the ground during flats unless you flip banjos and re-check clearance on Monorim arms or other low-slung frames.[^100]
- Magura’s support team still refuses to endorse third-party fittings and voids warranties when non-Magura pads or banjos are used, so document any custom M6 hardware or EU-sourced replacements before needing service.[^101]
- Tighten Magura lever bleed screws with the supplied 0.5 Nm tool instead of guessing by feel—over-torqueing strips the lever threads and dumps pressure mid-ride.[^102]

### Battery Planning

- New Vsett 11+ builders are targeting 60 V 50 Ah packs and documenting LG cell SKUs plus motor wind counts before swapping hardware—the stock 2 000 W hubs already reach ≈10 kW when paired with quality cells, so capture provenance before promising upgrades.[^103]
- Expect LG M50LT cells in 10 P strings to sustain roughly 9 kW safely; once internal clearances are confirmed you can stage controller upgrades without replacing the battery a second time.[^103]
- Stock VSETT 8 packs blend DynoVolt 2 600 mAh cells in 5 P (~13 Ah) or LG MH1/MJ1 parallels; keep discharge near 40 A (~3 C) to curb heat, and note how Flipsky 75100 swaps still feel stronger with just ~30 A battery and 90 A phase limits thanks to FOC efficiency.[^ip001-v8-pack][^ip001-foc-swap]
- First 20 S 9 P Samsung 48X logs hit ~10 kW with only 5–6 V sag at 133 A battery draw, keeping cells below 29 °C and motors near 66 °C after 15 spirited miles—proof that copper busbars and ferrofluid prep unlock higher sustained power.[^ip001-20s9p]

### Thermal Management & Instrumentation

- Dual Ubox retrofits still need fresh paste and a clean deck interface even if the outgoing Minimotors square-wave ESCs ran hotter; expect to pull the battery to reach the mounting blocks during the swap.[^vsett_ubox_paste]
- Dose 6–6.5 ml of Statorade per VSETT 10+ hub to drop winding peaks from ~145 °F to ~104 °F without noticeable drag; fill after the stator is seated, avoid metal syringe tips, and seal covers with silicone so the ferrofluid stays put. Larger 60 mm magnet motors may need 7–8 ml, while overfilling beyond ~8 ml adds friction—cheap AliExpress ferrofluids pass conductivity tests yet flash early, so riders stick with €30 EU-sourced Statorade and cap magnet temps around 90 °C when fluid is present.[^104][^105][^106]
- Community consensus keeps Statorade fills between roughly 4–8 ml per hub (≈6 ml in VSETT motors), resealing covers after inspections and weighing vent holes (≈5–10 °C gains) against the risk of fluid loss and water ingress.[^fill_guidance]
- 50 mm VSETT hubs running 17 S packs rarely need more than 60–70 A battery; most riders hold 125–180 A phase and rely on ferrofluid instead of pushing 90 A battery, because that simply cooks the motors faster.[^ip001-17s-limit]
- Poorly mounted Spintend duals are still spiking toward 90 °C until they’re clamped hard against the deck with thicker pads or steel plates; the 100 V revision spreads heat better but still needs solid mechanical contact.[^ip001-spintend-mount]
- Embed epoxy-coated 100 k B3950 probes under the windings with silicone adhesive, route a single sensor lead through the axle with the phases and halls, and stick with Statorade-grade ferrofluid—even “educational” blends have low flash points and unknown additives.[^107]
- Use existing cover screws or purpose-drilled ports to inject ferrofluid without disturbing hall boards, then reseal both side covers to stop leaks once the hubs are topped off; drilled vent holes can drop temps another 5–10 °C on smaller motors but risk weeping fluid and water ingress, so weigh airflow against weather sealing.[^108][^109]
- Check hubs seasonally and top off if fills dip below 4–8 ml—the community treats ≈6 ml as the sweet spot for VSETT motors and reseals covers after every inspection to prevent evaporation and leaks.[^110]
- Bolt-on hubsinks with thermal paste plus deck spacers or ducted lighting housings cut from PVC/acrylic push heat into the airstream and make room for taller packs, helping sustained 70–75 km/h runs without cooking the stator.[^111]
- Clamp controllers directly to aluminum structure with thin thermal pads and run lighting through relays; standalone fans on the harness keep running after shutdown because Spintend’s enable lead sources 12 V instead of sinking it.[^112]
- External 12 V shrouds with mesh filters held 6.2 kW pulls near 50 °C in wet 8 °C weather; plan motor NTC installs before removing firmware current limits so logs capture the new cooling headroom.[^113]
- One pothole strike left a front hub wobbling until the owner rewound the stator with an embedded temp sensor, swapped rims, and installed fresh bearings—proof that telemetry upgrades can ride along with mechanical repairs.[^ip001-tempwobble]
- Stock stator joints still need inspection—builders are ordering 10 k 3950 sensors for axle installs and reworking factory solder that left Huameng cores at 30–31 mΩ with stray splatter in the slots.[^114][^115]

### Bearings & Rolling Hardware

- Swap factory bearings for Timken 2RS units when chasing tight steering—riders report they remove inner-race play without the drag penalty of SKF 2RSH seals, and ZZ/2Z shields remain a low-resistance option if paired with external simmering seals; VSETT 9/10 housings accept roughly 7.5 mm shafts when shields are deleted, so spec C3/C4 tolerance replacements accordingly.[^116]

## Source Notes

- VSETT platform stiffness, controller relocation space, and PMT/CST tire guidance are drawn from the part001 review slice summarising winter 2021–spring 2022 field reports.[^117]
- Split-rim serviceability, tubeless behaviour, and Matris damper cautions originate from the same slice’s maintenance and handling notes.[^118]

## References

[^1]: Source: knowledge/notes/input_part001_review.md, L25 to L25
[^2]: Source: knowledge/notes/input_part001_review.md, L42 to L42
[^3]: Source: knowledge/notes/input_part001_review.md, L55 to L57
[^4]: Source: knowledge/notes/input_part001_review.md, L60 to L62
[^5]: Source: knowledge/notes/input_part001_review.md, L68 to L70
[^6]: Source: data/vesc_help_group/text_slices/input_part001.txt, L6990 to L7058
[^7]: Source: data/vesc_help_group/text_slices/input_part001.txt, L7003 to L7028
[^8]: Source: data/vesc_help_group/text_slices/input_part001.txt, L8211 to L8253
[^9]: Source: data/vesc_help_group/text_slices/input_part001.txt, L9522 to L9538
[^10]: Source: knowledge/notes/input_part006_review.md, L101 to L101
[^11]: Source: knowledge/notes/input_part001_review.md, L64 to L64
[^12]: Source: data/vesc_help_group/text_slices/input_part003.txt, L10118 to L10132
[^13]: Source: data/vesc_help_group/text_slices/input_part010.txt, L20034 to L20062
[^14]: Source: knowledge/notes/input_part000_review.md, L352 to L352
[^vsett_map]: Source: knowledge/notes/input_part000_review.md†L807-L807
[^vsett_ubox_paste]: Source: knowledge/notes/input_part000_review.md†L702-L703
[^paolo_leads]: Source: knowledge/notes/input_part000_review.md†L723-L723
[^vsett_ds_harness]: Source: knowledge/notes/input_part000_review.md†L731-L731
[^vsett_dual_enable]: Source: knowledge/notes/input_part000_review.md†L732-L732
[^15]: Source: knowledge/notes/input_part000_review.md, L440 to L443
[^16]: Source: knowledge/notes/input_part000_review.md, L387 to L388
[^17]: Source: knowledge/notes/input_part005_review.md, L69 to L69
[^18]: Source: knowledge/notes/input_part006_review.md, L314 to L314
[^19]: Source: knowledge/notes/input_part001_review.md, L59 to L63
[^20]: Source: knowledge/notes/input_part001_review.md, L73 to L74
[^21]: Source: knowledge/notes/input_part001_review.md, L59 to L62
[^22]: Source: knowledge/notes/input_part014_review.md, L4568 to L4569
[^23]: Source: knowledge/notes/input_part001_review.md, L74 to L74
[^24]: Source: data/vesc_help_group/text_slices/input_part003.txt, L24566 to L24578
[^25]: Source: knowledge/notes/input_part006_review.md, L316 to L316
[^26]: Source: knowledge/notes/input_part006_review.md, L317 to L317
[^27]: Source: data/vesc_help_group/text_slices/input_part010.txt, L11518 to L11518
[^28]: Source: data/vesc_help_group/text_slices/input_part010.txt, L11527 to L11529
[^29]: Source: knowledge/notes/input_part001_review.md, L583 to L584
[^30]: Source: data/vesc_help_group/text_slices/input_part004.txt, L7238 to L7258
[^31]: Source: data/vesc_help_group/text_slices/input_part001.txt, L25331 to L25337
[^32]: Source: data/vesc_help_group/text_slices/input_part001.txt, L5520 to L5631
[^33]: Source: knowledge/notes/input_part001_review.md, L43 to L43
[^34]: Source: data/vesc_help_group/text_slices/input_part001.txt, L26005 to L26103
[^35]: Source: data/vesc_help_group/text_slices/input_part001.txt, L11407 to L11433
[^ip001-deck-map]: Source: data/vesc_help_group/text_slices/input_part001.txt†L23033-L23392
[^ip001-limited-leads]: Source: data/vesc_help_group/text_slices/input_part001.txt†L22030-L22118
[^ip001-limited-price]: Source: data/vesc_help_group/text_slices/input_part001.txt†L22188-L22221
[^ip001-dual-phase-detect]: Source: data/vesc_help_group/text_slices/input_part001.txt†L24642-L24683
[^ip001-pmt-psi]: Source: data/vesc_help_group/text_slices/input_part001.txt†L22120-L22166
[^ip001-v8-pack]: Source: data/vesc_help_group/text_slices/input_part001.txt†L19007-L19066
[^ip001-foc-swap]: Source: data/vesc_help_group/text_slices/input_part001.txt†L19038-L19048
[^ip001-20s9p]: Source: data/vesc_help_group/text_slices/input_part001.txt†L19918-L19960
[^ip001-17s-limit]: Source: data/vesc_help_group/text_slices/input_part001.txt†L21900-L22033
[^ip001-spintend-mount]: Source: data/vesc_help_group/text_slices/input_part001.txt†L21960-L22363
[^ip001-damper]: Source: data/vesc_help_group/text_slices/input_part001.txt†L20060-L20076
[^36]: Source: data/vesc_help_group/text_slices/input_part003.txt, L23963 to L24010
[^37]: Source: data/vesc_help_group/text_slices/input_part004.txt, L2133 to L2152
[^38]: Source: data/vesc_help_group/text_slices/input_part004.txt, L3001 to L3015
[^39]: Source: data/vesc_help_group/text_slices/input_part004.txt, L2695 to L2706
[^40]: Source: knowledge/notes/input_part001_review.md, L59 to L61
[^41]: Source: knowledge/notes/input_part003_review.md, L111 to L111
[^42]: Source: data/vesc_help_group/text_slices/input_part004.txt, L2640 to L2656
[^43]: Source: data/vesc_help_group/text_slices/input_part010.txt, L11580 to L11582
[^44]: Source: knowledge/notes/input_part004_review.md, L16 to L16
[^45]: Source: knowledge/notes/input_part001_review.md, L68 to L68
[^46]: Source: knowledge/notes/input_part001_review.md, L69 to L69
[^47]: Source: knowledge/notes/input_part001_review.md, L70 to L70
[^ip001-highspeed]: Source: data/vesc_help_group/text_slices/input_part001.txt†L26428-L26488; data/vesc_help_group/text_slices/input_part001.txt†L26827-L26841
[^ip001-sharkset]: Source: data/vesc_help_group/text_slices/input_part001.txt†L24574-L24597
[^ip001-stock-17s]: Source: data/vesc_help_group/text_slices/input_part001.txt†L17870-L17940; data/vesc_help_group/text_slices/input_part001.txt†L18089-L18155
[^ip001-pack-pricing]: Source: data/vesc_help_group/text_slices/input_part001.txt†L26910-L26910
[^ip001-ubox-detect]: Source: data/vesc_help_group/text_slices/input_part001.txt†L26956-L26999
[^48]: Source: data/vesc_help_group/text_slices/input_part001.txt, L27655 to L27667
[^49]: Source: data/vesc_help_group/text_slices/input_part010.txt, L19045 to L19067
[^50]: Source: data/vesc_help_group/text_slices/input_part010.txt, L19864 to L19864
[^51]: Source: knowledge/notes/input_part001_review.md, L524 to L525
[^52]: Source: data/vesc_help_group/text_slices/input_part001.txt, L25022 to L25045
[^53]: Source: data/vesc_help_group/text_slices/input_part003.txt, L24013 to L24167
[^54]: Source: data/vesc_help_group/text_slices/input_part003.txt, L24676 to L24694
[^55]: Source: knowledge/notes/input_part004_review.md, L231 to L231
[^56]: Source: knowledge/notes/input_part004_review.md, L239 to L239
[^57]: Source: data/vesc_help_group/text_slices/input_part001.txt, L6340 to L6362
[^58]: Source: data/vesc_help_group/text_slices/input_part001.txt, L6800 to L6821
[^59]: Source: knowledge/notes/input_part006_review.md, L397 to L397
[^60]: Source: data/vesc_help_group/text_slices/input_part010.txt, L11561 to L11602
[^61]: Source: data/vesc_help_group/text_slices/input_part001.txt, L26300 to L26380
[^62]: Source: knowledge/notes/input_part000_review.md, L714 to L727
[^63]: Source: data/vesc_help_group/text_slices/input_part001.txt, L21612 to L21658
[^64]: Source: knowledge/notes/input_part003_review.md, L26 to L27
[^65]: Source: knowledge/notes/input_part003_review.md, L26 to L28
[^66]: Source: data/vesc_help_group/text_slices/input_part001.txt, L7166 to L7194
[^67]: Source: data/vesc_help_group/text_slices/input_part001.txt, L7351 to L7415
[^68]: Source: knowledge/notes/input_part006_review.md, L271 to L271
[^69]: Source: data/vesc_help_group/text_slices/input_part001.txt, L6371 to L6486
[^70]: Source: data/vesc_help_group/text_slices/input_part001.txt, L6501 to L6504
[^71]: Source: knowledge/notes/input_part006_review.md, L184 to L184
[^72]: Source: knowledge/notes/input_part006_review.md, L176 to L176
[^73]: Source: knowledge/notes/input_part001_review.md, L538 to L539
[^74]: Source: knowledge/notes/input_part001_review.md, L623 to L624
[^75]: Source: data/vesc_help_group/text_slices/input_part001.txt, L6481 to L6504
[^76]: Source: data/vesc_help_group/text_slices/input_part001.txt, L8851 to L8913
[^77]: Source: data/vesc_help_group/text_slices/input_part001.txt, L8927 to L8933
[^78]: Source: data/vesc_help_group/text_slices/input_part001.txt, L11220 to L11286
[^79]: Source: data/vesc_help_group/text_slices/input_part001.txt, L21320 to L21404
[^80]: Source: knowledge/notes/input_part001_review.md, L653 to L655
[^81]: Source: data/vesc_help_group/text_slices/input_part001.txt, L10421 to L10520
[^82]: Source: data/vesc_help_group/text_slices/input_part001.txt, L21404 to L21516
[^83]: Source: data/vesc_help_group/text_slices/input_part001.txt, L21320 to L21516
[^84]: Source: knowledge/notes/input_part001_review.md, L577 to L578
[^85]: Source: knowledge/notes/input_part006_review.md, L149 to L149
[^86]: Source: knowledge/notes/input_part001_review.md, L635 to L636
[^87]: Source: data/vesc_help_group/text_slices/input_part001.txt, L5695 to L5718
[^88]: Source: data/vesc_help_group/text_slices/input_part001.txt, L6190 to L6198
[^89]: Source: knowledge/notes/input_part000_review.md, L213 to L213
[^90]: Source: data/vesc_help_group/text_slices/input_part001.txt, L24060 to L24088
[^91]: Source: knowledge/notes/input_part000_review.md, L518 to L518
[^92]: Source: knowledge/notes/input_part000_review.md, L746 to L749
[^93]: Source: knowledge/notes/input_part001_review.md, L535 to L536
[^94]: Source: knowledge/notes/input_part001_review.md, L620 to L621
[^95]: Source: data/vesc_help_group/text_slices/input_part001.txt, L9208 to L9538
[^96]: Source: data/vesc_help_group/text_slices/input_part001.txt, L9901 to L10054
[^97]: Source: knowledge/notes/input_part001_review.md, L544 to L546
[^98]: Source: knowledge/notes/input_part001_review.md, L642 to L644
[^99]: Source: data/vesc_help_group/text_slices/input_part001.txt, L9947 to L10216
[^100]: Source: knowledge/notes/input_part001_review.md, L562 to L563
[^101]: Source: knowledge/notes/input_part001_review.md, L546 to L546
[^102]: Source: knowledge/notes/input_part001_review.md, L683 to L684
[^103]: Source: knowledge/notes/input_part010_review.md, L380 to L382
[^104]: Source: data/vesc_help_group/text_slices/input_part001.txt, L8463 to L8518
[^105]: Source: knowledge/notes/input_part001_review.md, L531 to L533
[^106]: Source: knowledge/notes/input_part001_review.md, L613 to L615
[^107]: Source: data/vesc_help_group/text_slices/input_part001.txt, L10364 to L11187
[^108]: Source: data/vesc_help_group/text_slices/input_part001.txt, L11140 to L11216
[^109]: Source: knowledge/notes/input_part001_review.md, L615 to L615
[^110]: Source: knowledge/notes/input_part001_review.md, L574 to L575
[^111]: Source: data/vesc_help_group/text_slices/input_part001.txt, L8601 to L8786
[^112]: Source: knowledge/notes/input_part003_review.md, L128 to L128
[^113]: Source: knowledge/notes/input_part003_review.md, L133 to L133
[^114]: Source: knowledge/notes/input_part003_review.md, L135 to L135
[^115]: Source: knowledge/notes/input_part003_review.md, L181 to L181
[^ip001-tempwobble]: Source: knowledge/notes/input_part001_review.md†L665-L666
[^116]: Source: knowledge/notes/input_part001_review.md, L638 to L640
[^117]: Source: knowledge/notes/input_part001_review.md, L25 to L74
[^118]: Source: knowledge/notes/input_part001_review.md, L59 to L70
[^axle-clunk]: Source: knowledge/notes/input_part006_review.md†L16-L16
[^20a]: Source: knowledge/notes/input_part001_review.md, L538 to L539
[^pack_18s7p]: Source: knowledge/notes/input_part001_review.md, L577 to L578
[^speed_cal]: Source: knowledge/notes/input_part001_review.md, L524 to L526
[^fill_guidance]: Source: knowledge/notes/input_part001_review.md, L574 to L575
[^scand_rules]: Source: knowledge/notes/input_part001_review.md, L535 to L537
