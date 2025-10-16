# Motor Cooling & Thermal Management Notes

## Why Fans Rarely Help Scooter Hubs

- Denis Yurev reminded the workshop that scooters already move fresh air past the hub at riding speed, so bolt-on fan kits add little cooling compared with ensuring good heat transfer from the windings to the shell.[^1]
- Riders debating CPU-style blowers learned that evaporation-driven skin cooling does not apply to dry aluminum shells; without a wet surface the only lever is temperature delta, so focus on conductive paths instead of add-on spinners.[^2]
- Veterans recommended ferrofluid or oil-fill experiments (with leak safeguards) if you need real winding-to-shell transfer.
  - simply drilling covers or gluing “windmills” to the hub only cools the outer case.[^3]
- Polish builders are sourcing Statorade directly from Nexun and stress that ferrofluid or oil only helps after you’ve addressed the stator-to-shell bottleneck with solid thermal interfaces.[^denis-nexun-ferro]
- Community case studies still favour passive conduction upgrades over active plumbing: Mirko’s 15 mm aluminum deck plate plus open vents held dual 190 A phase / 70 A battery runs near 52 °C, while heat-pipe experiments outperformed vibration-prone water loops on cramped decks.[^4][^5]
- Skip deck-mounted water loops unless you have room for pumps and vibration isolation.
  - recent builders concluded sealed PC-style kits rattle apart under scooter vibration; bolting MOSFETs to the frame or adding copper spreaders remains the safer path.[^6][^denis-waterloop-risk]
- Fresh water-cooled, resin-potted controller builds with INA181 current sensors promise better cut-off behaviour, yet veterans still warn that MOSFET-to-heatsink transfer is the real bottleneck until someone logs sustained high-power runs on the new hardware.[^7]
- When water cooling is unavoidable, Smart Repair’s X12 loop blueprint calls for a 40 × 80 mm block on the MOSFET bank, a PWM-controlled ~800 L/h pump, small radiator, and roughly 1 kg total system mass (≈300 g coolant, 300 g pump, 500 g hardware) with conformal coating and Kapton to harden the controller after prior water damage.[^8]

## Motor Architecture Context

- Axial-flux scooter prototypes mount magnets on facing disks for high power density, while hybrid “raxial” concepts add more phases for torque; production hubs still favour radial flux because the hollow stator leaves little room for liquid cooling hardware and costs stay lower.[^9]
- Treat flashy “liquid-cooled radial hub” marketing videos skeptically.
  - veterans spotted builds with only phase leads and no coolant plumbing, confirming many are passive designs dressed up for promotion.[^10]
- Deck-cut fan experiments proved counter-productive.
  - the airflow just recirculates hot air while the holes invite water ingress that shorts controllers or LiPo-powered fan mods; riders now double down on thick thermal pads and intact decks instead.[^11][^12]

## Ferrofluid Selection & Handling

- The VESC Help crew continues to vouch for ferrofluid/Statorade when the goal is winding-to-shell transfer, but they emphasise reading datasheets.
  - some mixes flash at low temperature and budget hubs can demagnetise above ~80 °C
  - before flooding a motor.[^13]
- Ferrotec APG1110 remains the benchmark for hub fillings, while Supermagnete’s 10 mL bottles offer reliable sourcing for EU riders upgrading Xiaomi and G30 hubs without importing large lots.[^14]
- HeroDasH demonstrated clean application with magnetic bottles that pull fluid straight into magnet gaps and warned against overfilling because excess drag hurts efficiency; peers now lean on ebikes.ca’s simulator to visualize how kv and resistance tweaks shift the efficiency curve before sealing hubs.[^15]
- Grin’s Statorade has logged roughly 30 % winding-temperature drops with 6 ml doses and no noticeable drag, whereas bargain ferrofluids risk conductivity, residue, and magnet damage once they bake inside the hub.[^16][^17]
- Denis’ crew only adds about a quarter bottle of ferrofluid per motor; they report identical top speed with less heat but still caution that repeated full-power climbs can melt valve stems once you stop abruptly.[^denis-quarter-bottle]
- Budget “educational” ferrofluids coming from lab suppliers carry lower flash points and unknown additives.
  - stick with Statorade/Grin blends even on 60 mm hubs, which still respond well to roughly 5–6 ml fills when you need winding-to-shell transfer.[^18][^19]
- Dosing dual 1.4 kW VSETT hubs with roughly 6 ml of Statorade dropped peak winding temperature from ~145 °F (63 °C) to ~104 °F (40 °C) on identical 16 S rides; veterans still log magnet temps because the heat migrates into the rotor during long climbs.[^20][^21]
- Follow-up tests note magnets running slightly warmer but transferring heat to the case faster, and sealing the covers with automotive silicone keeps the fluid contained even on off-road builds.[^22]

## Hub Heatsinks & External Cooling

- Builders chasing sustained 70–75 km/h add bolt-on hubsinks with thermal paste to move heat into airflow, noting that balanced e-bike rings avoid vibration if machined precisely.[^23]
- Custom deck spacers and ducted lighting housings are being hand-cut from PVC/acrylic to route airflow past motors while freeing deck space for taller battery packs.[^24]
- Riders toying with automatic transmission fluid (ATF) were warned it will leak through cable glands and bearings.
  - stick with ferrofluid for controllable rotor-gap transfer unless you have data proving a hybrid fill can stay sealed.[^atf-leak]
- Mirono’s wrap-and-fluid test showed thermal tape fins plus ferrofluid kept a bag-mounted VESC near ambient (≈42 °C heatsink in 34 °C weather) while the hub shell matched coil temps, confirming the stator finally dumps heat into the case efficiently.[^25][^26]
- Builders reseating ferrofluid-treated stators set the rim between their feet, slide the stator straight in, and tape XT150 terminations with Kapton to avoid slicing insulation while keeping service access.[^27]
- Community debate over branded Statorade vs. generic ferrofluids continues: premium mixes claim tuned viscosity, yet budget blends still deliver major gains unless you’re chasing Rosheee-level power, provided there’s a solid path from stator to ambient air.[^28]
- Expect roughly a 10 % premium on ferrofluid and hubsinks to net 15–30 % more continuous output; riders paying CHF 21 per 10 mL import fee for genuine Statorade still call the trade worthwhile for €200 hubs when paired with machined “windmill” fans.[^29][^30]
- Late-2022 teardown logs converged on dosing sealed 10″ hubs with roughly 2.5–5 ml of ferrofluid (3–4 ml for 11″ cans), applied between magnets after pulling the stator so the air gap fills without spraying grit into open-frame motors.[^31]
- **Service & reseal workflow (2022 refresher).** Photograph stator joints on arrival, resolder undersized leads, inject 2.5–5 ml of ferrofluid between the magnets on sealed hubs, refresh bearings and thermal paste, then pressure-wash or silicone-seal swingarms and cable exits before reinstalling the wheel.[^32][^33][^34][^35][^36]
- Fresh logs show ferrofluid’s benefit is immediate: once heat soaks into the side plates you can cool an overheated hub by spinning it unloaded instead of riding it harder.
  - hand-test inputs first, then let the wheel freewheel until case temps fall.[^37]
- Ferrofluid refreshes should be sparing.
  - apply a thin bead between magnets and add a dedicated temperature probe so rising wattage doesn’t go unnoticed after the fill.[^38]
- Segway-class hub service days now pair ferrofluid top-ups with temperature-probe checks; bake those steps into maintenance lists before long tours so commuter fleets don’t head into rain weeks with dry stators.[^39]
- Before drilling breather ports, builders mark bit depth, stop once the cover breaks through, and reseal with clear RTV after filling; adding a temp sensor during the same service keeps long-term monitoring simple.[^40]
- **Apply ferrofluid sparingly.** Builders found that overfilling with ferrofluid traps heat; a hair-thin film between magnets is enough and torque gains should come from raising phase current, not bathing the rotor.[^41]

## Hub Current Guardrails

- Single Monorim 500 W hubs stay happy around 80 A phase.
  - ideally with ferrofluid
  - while the crew’s Xiaomi-class builds overheat quickly once they push 65–73 A without battery temperature sensing or keep more than roughly 30–35 A combined draw from paired 12 S packs.[^42]
- Gen 4 Ninebot G30 hubs have already squealed and overheated after 30 km of 35 A battery riding in 35 °C ambient without temp sensors on the motor or ESC.
  - treat instrumentation as mandatory before chasing high-phase tunes on commuter hubs.[^43]

## Micro-Hub Voltage Stress Signals

- Doubling a Xiaomi/Ninebot commuter from 10 S to 20 S roughly doubles the free-spin speed but repeatedly burns the stock hub from heat saturation, so builders now treat 18 S as the limit unless they add serious cooling or swap motors.[^44]
- Fiido L3 rear hubs emerged as the go-to drop-in upgrade for 20 S experiments because their wider stator and exposed shell shed heat far better than Xiaomi-class cans.
  - veterans report killing three narrow hubs in two days while the Fiido survived on a Spintend 100 V Lite.[^45]
- Kugoo M4 hubs stall near 50 km/h even with 25 A of field weakening on 14 S builds, hinting that the motor design.
  - not just voltage
  - caps speed; missing thermistor wiring leaves VESC logs stuck at −66 °C, so add sensors before chasing more current.[^46]
- GABE is also sandwiching aluminium plates with thermal paste around a 10 mm 3D-printed spacer to keep his 250 W commuter hub cool after widening the dropout, showing how thin filler plates can restore conduction when packaging changes add air gaps.[^47]
- Stock Ninebot G30 hubs top out around 80 km/h solo and ~98 km/h in dual-motor builds, but a single motor hauling two riders at 40 A cooked its insulation.
  - treat heavy two-up duty as a thermal red line without upgraded cooling.[^48]

## Controller Interface Refresh Checklist

- When raising voltage, replace Kapton tape with 0.5 mm thermal pads so MOSFETs stay isolated yet shed heat; stacking pads on top of Kapton just adds resistance.[^49]
- Sand controller bases, clean MOSFET tabs, and reinstall paste before clamping the box.
  - loose wiring under the plate prevents full contact and spikes temperatures on the first ride.[^50]
- Keep silicone pads on hand when chasing 48 V/15 S tunes; the crew pairs IRFB4110 MOSFETs with 100 V 1,000 µF and 47 µF capacitors and swaps pads plus paste before closing the case.[^51]
- Deck-mounted controller plates should be sanded to bare metal and paired with thin thermal pads; open-vent decks plus 15 mm aluminum plates have proven the most repeatable way to keep single- and dual-motor builds near 50 °C under 190 A phase loads.[^4]
- Paolo swaps thick thermal pads for thin Kapton plus paste on CNC-machined housings to maximise contact, reserving pads for rough castings where gap filling matters more.[^52]
- Riders add thin washers under CNC motor coolers so air can pass beneath the plate; Laotie ES19 hubs share the Vsett 10 bolt pattern, making dual-sided heatsinks easier to print.[^53]
- Race telemetry backs the approach: Benur Lgl’s 20s12p C350 scooter used a finned aluminum radiator with copper-backed Arctic Gel to hold ~38.5 kW pulls around 55 °C even at 850 A phase, illustrating how rigid clamping and real heatsinks outperform clip-on fans at race power.[^54]
- Hard-mount controllers whenever possible: bolting a MakerX HI100 to an aluminum cradle dropped case temps to ~23 °C on 60 A battery / 200 A phase pulls at 7 °C ambient versus 60–80 °C when the unit was bag-mounted.[^55]
- Treat magnet grades as the limiting factor: budget neodymium begins fading around 80 °C, premium specs survive closer to 120 °C, and enamel windings only last near 150 °C.
  - monitor stator temps and dose ferrofluid carefully so repeated 3 kW pulls don’t demagnetise the rotor and raise Kv.[^56]
- Mirko’s machined radiator plate hangs roughly 3 cm below the frame (7.5 cm ground clearance unloaded) and needs insulated FET interfaces plus potential heat pipes to spread hotspot load.
  - log spacer stacks and insulation plans before copying the design.[^57][^58]
- Gigolo Joe’s CPU-style heatsinks still let a single 75100 V1 hit 96 °C on 10 km speed runs at 180 A phase / 100 A battery, proving airflow and heat sinking remain the limit even on 9–12 kW single-motor builds.[^59]

### Deck Radiator & Thermal Interface Experiments

- Community photos comparing thick paste bridges against bare ergal vs. 6061 plates showed paste still outperforms air gaps, but PCB-mounted probes can lag case temperature by several degrees.
  - treat onboard telemetry as relative trends, not absolute hotspots.[^60]
- Longitudinal skid plates without thermal paste plateaued around 54 °C even with solid airflow; crews now spread paste across the plate and step up to 25 mm fins or thicker stock before expecting meaningful heat transfer gains.[^61]
- VSETT stator rewinds revealed lacquer-shelled star points barely wetted from the factory; torch the enamel, brush clean, and fully re-solder before running fresh motor detection to cut resistance and heat soak.[^62]
- Paolo reminded riders that handheld IR thermometers aimed at heatsinks under-read MOSFET junction temperatures.
  - reliable checks need bare-die access or pro-grade IR cameras, reinforcing the value of direct FET-to-baseplate contact on Little FOCer or Tronic designs.[^63]
- Heat-pipe arrays are supplanting water loops on compact decks; builders now pair finned pipes with QS8-class harnesses and 10 mm² (≈8 AWG) leads when paralleling external packs so 80 A continuous transfers without cooking insulation.[^64]

## Heat Transfer Upgrades from VESC Field Logs

- Spintend dual-Ubox owners report the factory ships thermal pads (not paste) on MOSFET plates; lapping the deck and adding fresh paste keeps Laotie builds under ≈80 °C even on hard pulls.[^65]
- Dual Ubox owners pour potting compound, deck-mount clamps with fresh paste, and even heat pipes into thick aluminium plates to shave ~20 °C.
  - yet 220–250 A surges still blow traces, so airflow and external mounting remain mandatory on extreme builds.[^66][^67][^68]
- Even potted Nucular 12F controllers run cooler than bare front-mounted units, reinforcing the value of potting compounds or aluminium baseplates when decks have the space.[^69]
- Ubox Lite testers also learned that 5 mm replacement pads choke heat flow.
  - switching to thin pads or quality paste stopped 70 °C surges and reminded crews that even heatpipes saturate when the interface layer gets too thick.[^70]
- Epoxy putty doubles as a heat spreader around controller cases while builders embed thermistors through the existing hall harness and pot them with epoxy or silicone for direct winding contact.[^71]
- Marketing tags like “5,600 W” on Laotie hubs hide commuter-class limits.
  - tuners see roughly 1.2 kW continuous and ≈3 kW peaks unless you step up to true 60 H/70 H race cans, dual controllers, ferrofluid, and fat phase leads to move 20–33 kW safely.[^72]
- Longer magnets and thicker stators are what lift continuous power; removable-rim Huameng hubs trade iron volume for convenience while 90 H LY motors justify the machining effort when you actually need ~30 kW dual setups.[^72]
- Resin-potted water-cooled Flipsky builds now ship with INA181 phase sensors and denser heatsinks, but veterans still expect MOSFET-to-heatsink contact to be the bottleneck until independent testing confirms the claimed improvements.[^73]
- Passive mods still need conduction.
  - welded side-cover fins only shed heat when ferrofluid is present; otherwise the stator stays insulated by the air gap and drilled vent holes just invite debris without improving transfer.[^74]
- Jan and others confirmed that adding internal fins or covers barely changes temperatures because the stator still floats across an air gap; meaningful cooling jumps require water quick-connects or abandoning hubs for mid-drives, despite the packaging headache of chains and belts on scooter frames.[^75]

## Controller Mounting & Airflow Discipline

- Spintend dual and Makerbase/Tronic-class controllers still dump serious heat.
  - riders logging ~180 A phase on 84100-class ESCs report case temperatures climbing fast unless the units are bolted to large external heatsinks with fresh paste, reinforcing that even “cooler” Spintend hardware only halves the dissipation of Tronic boxes when airflow and interface pressure are maximised.[^76]
- Nucular 12-FET controllers happily sustain roughly 210 A battery current while holding ~48 °C when they are clamped firmly to deck aluminium, underscoring the payoff from rigid mounting pressure on MOSFET plates.[^77]
- Refresh thermal interfaces on a schedule: the community now treats ESC paste like desktop-PC maintenance.
  - strip the controller every couple of years, clean the heatsink, and reapply high-quality compound before summer pushes start.[^78]
- Load sharing matters. A lone Tronic 250 on steep climbs still touches ~60 °C, while an equivalent dual-drive setup running the same hills stays under 40 °C because the thermal load splits between controllers and each unit has better deck contact.[^79]
- Spintend’s compact 6-FET aluminium controllers want a sandwich mount: spread thermal paste on both sides of a 3–5 mm aluminium plate, clamp the ESC between the plate and the deck, and avoid copper interface plates that encourage galvanic corrosion once they are bolted to aluminium chassis members.[^80]
- Lieven reminded builders that even perfect airflow can’t match the surface area of a proper radiator.
  - if relocation alone fails, step up to water plates or larger sinks to keep high-power VESCs in check during 90 mph pulls.[^81]
- Noname’s latest plan for 30–40 kW scooters leans on inexpensive AliExpress radiators to liquid-cool QS hubs; expect roughly 52 mph from 20 S and 42 mph from 16 S today, with 32 S packs reserved for future 30 kW attempts once cooling is validated.[^82]
- Track-focused builders now strip paint, drill fresh bolt holes, clamp controllers with washers and threadlocker, add thermal paste, and route heat into the chassis or external sinks; relying on foam or internal fans in sealed bays just cooks the controllers.[^83][^84]
- External fins need real airflow.
  - drop the heatsink through the deck, drill and tap anchors, and bolt the controller straight to the frame with paste; leaving fins flush inside the deck traps hot air.[^85]
- Flush-mounted fan kits inside sealed decks simply recirculate warm air; racers relocate fans externally or add ducts so airflow actually sweeps across the heatsink before trusting the upgrade.[^86]
- Bond compact Spintend cases to the frame with thermal adhesive and log front/rear motor temps; mismatched readings often trace to wiring or observer faults before the controller itself overheats.[^87]
- Skip brazing aluminum frames for heatsink bonding unless you have specialty tooling; even experienced metalworkers called it a last resort compared with mechanical fasteners.[^88]
- When clamping copper blocks to aluminum frames, isolate them with silicone sheets or plating; bare copper-on-aluminum mounts trigger galvanic corrosion that quietly eats the chassis.[^89]
- Dial in airflow paths after rework.
  - builders now notch decks, tap fins, and bridge controllers to fresh-cut ducts so heat actually leaves the bay instead of recirculating behind sealed covers.[^90]
- Dual Spintend installs on sealed Weped decks hit ~80 °C while delivering ~500 A phase, underlining how little thermal margin exists without direct deck contact and fresh paste.[^91]
- Consensus from recent debates: bolt controllers flat to aluminium chassis plates with quality thermal paste.
  - remote radiator boxes, thick spacers, and long external runs add heat, resistance, and failure points compared with a well-clamped deck or footrest mount.[^92]
- Cracking deck vents alone only delays thermal cutback; re-bedding Ubox cases with paste against the deck proved to be the repeatable fix for 75 A battery / 190 A phase tunes that otherwise crept toward shutdown.[^93]
- Deck vents alone only buy moments of relief: one Wolf owner carved large side openings yet still saw limited airflow, and others simply ride with deck covers ajar because closing the bay drives controller temps past 80 °C until better cooling arrives.[^94]
- Xiaomi conversions demonstrate why enclosure shape matters: dual ESCs mounted in printed side pods that funnel oncoming air stay cool even when riders rely on regen-only braking from 70–80 km/h, though builders already plan aluminium skins to survive crashes.[^95]
- Weeped-class builds proved that sandwiching a VESC on a thin steel plate between the controller and battery just traps heat.
  - add thermal pads or paste and relocate the stage into cleaner airflow before escalating to liquid loops because front fairings often choke ventilation.[^96]

## Controller Cooling Case Studies

- Jason resurrected an MP2 after a MOSFET failure and now caps the platform around 100 A battery / 250 A phase, acknowledging a 300 A launch cooked the board while chasing sensor cogging.[^97]
- Finn keeps an Ubox Lite below 50 °C while pulling 160 A phase / 90 A battery by swapping in Arctic MX4 paste and bolting through the controller’s M2 bosses into a 3 mm aluminum belly pan.[^98][^99]
- Abs’ dual-controller build clamps MOSFETs to a 3–4 mm aluminum bar with mica insulators and filtered 12 V push-pull fans, dropping case temps from ~67 °C to ~40 °C during 60 A, 20 S runs; he recommends skipping the complexity on mild 12–13 S tunes.[^denis-abs-cooling]
- Matthew’s DIY water loop dropped his VESC enclosure from ~90 °C cutbacks to ~26–28 °C during 45 mph pulls; Noname is planning a moped-sized radiator, pump, and expansion tank to scale the concept.[^100]
- Swapping to higher-grade thermal paste still nets ~5 °C improvements, but veterans stress optimizing airflow before escalating to liquid cooling complexity.[^101]
- SNSC rental frames that arrived with warped mounting faces now get controllers preloaded against thick pads (or graphene sheets) and may even receive thermal glue to flatten hot spots before endurance sessions, showing how enclosure alignment affects long-pull temps.[^102]
- Fold these Lite and MP2 mitigation case studies into controller SOP binders.
  - document Arctic MX4 swaps, belly-plate mounting, and air-vs.-liquid trade-offs so future tear-downs start with proven recipes instead of trial-and-error.[^103]

## Temperature Guardrails

- Misconfigured thermistors triggered limp mode within 15 minutes on a modest 48 V 800 W hub; confirm the sensor type (NTC 100 k vs. alternatives) with a meter or disable the probe until the value matches reality.[^104]
- Dual 90 H builds logged ~58 °C rear / 48 °C front after a 24 km, 10 % grade climb in 25 °C ambient.
  - use those numbers as a sanity check for 75 200/85 150 setups before raising current further.[^105]
- Battery temps around 41 °C were deemed healthy for summer rides, but the group flagged ~60 °C as a ceiling.
  - anything hotter accelerates degradation and calls for gentler tunes.[^106]
- Dry hub motors start complaining above ~90–105 °C; riders treat that range as the safe ceiling without ferrofluid and switch pads/rotors before chasing 100 km/h pulls.[^107]
- Makerbase 100/100-class controllers start current limiting once MOSFETs touch ~70 °C if the base plate lacks fresh thermal paste; the crew now treats 70 °C as the everyday limit and 100 °C as the hard ceiling for VESC MOSFETs to preserve lifespan.[^108]
- Stock Xiaomi controllers paired with 16 S packs and 500 W hubs have already logged ~99 °C under heavier riders—plan controller upgrades instead of trusting case mods alone for 60 km/h builds.[^xiaomi-99c]
- Larger packs and long shocks trap heat around the deck; riders re-bend frames, add inner/outer steel plates, and swap to lower-rate springs instead of trimming coils so the chassis and cells stop cooking each other.[^109]
- Abuse tests that pumped 84 V/2 000 W into stock 250 W hubs demagnetised rotors once magnets crossed ~80 °C, permanently reducing speed.
  - log stator temps on recycled hardware before chasing high-voltage experiments.[^110]
- Treat 80–100 °C as the practical magnet ceiling even when windings temporarily tolerate 120 °C; ferrofluid’s real job is moving magnet heat into the shell, not lowering copper temperature.[^111]
- Delta-wound Xiaomi hubs start to lose launch torque above ~80 °C even if they recover later, so add live temperature telemetry before pushing high phase current on compact stators.[^112]
- Repeated hard launches and panic stops on 48 V conversions have been cooking hall sensors and high-kV hubs within days; builders now source quality SS41F-class sensors, add ferrofluid, cut phase amps, or step up to larger/lower-kV motors to keep temperatures manageable.[^113][^114]
- Keep high-kV hubs near ~80 % of top speed on steep hills.
  - charging into climbs from a run-up avoids the full-throttle slog that overheats windings and hall sensors on 48 V builds.[^115]
- Weped-mounted dual Uboxes still brushed ~80 °C delivering ~500 A phase until riders resurfaced the deck and clamped the controller directly with fresh thermal paste.
  - remote radiator boxes and thick spacers only added heat soak.[^116]
- Race telemetry has already captured 171 °C stator cores when airflow stalls; treat 160 °C as an emergency ceiling and back power off before magnets soften or lamination glue fails.[^117]
- Even robust controllers cannot save undersized hubs: a 750 W Boosted Rev on a Spintend single hit 55 °C controller / 80 °C stator in eight minutes at 120 A phase / 80 A battery, proving you must tune current to motor mass, not ESC ceiling.[^118]
- Regen spikes add heat too.
  - phase clipping kicked in around 25–30 km/h and each hard brake pulse lifted the stator roughly 5 °C, so log braking currents whenever you raise negative amps.[^119]
- Field-weakening remains a high-speed tool only; riders toggle it above cruise speed after seeing 20–40 km/h gains at the cost of huge current draw and extra heat when left on below the duty sweet spot.[^120][^121]
- Embed 100 kΩ NTC probes inside the windings on Vsett-class builds.
  - the shell can feel cool while the coils touch 90 °C, and pairing the sensors with FOC controllers keeps launches smooth while logging real stator temps.[^122]
- Overvolting an 800 W Citycoco hub to 26 S/100 A cooked the windings mid-hill, underscoring how quickly small motors die when voltage climbs faster than thermal paths.
  - treat voltage bumps as motor swaps, not just controller tweaks.[^123]

## Ferrofluid Handling & Hub Maintenance

- Dose scooter hubs with roughly 3–6 ml of Statorade (60 mm motors stretch to 7–8 ml) only after the stator is seated; plastic syringes keep filings out while the magnets self-level the fluid.[^124]
- Reseal side covers with silicone and revisit fills seasonally.
  - vent holes can shave another 5–10 °C on smaller motors but risk weeping ferrofluid and inviting water, so log temps before committing to drilled covers.[^124]
- Wolf Warrior hubs that survived ~10,000 km came back with cracked phase insulation and missing hall boards; use refreshes to rewire phases, embed new hall sensors, and add Statorade while the shell is open.[^125]

## Cooling Accessory Reality Checks

- 3D-printed “hub fin” shells draw criticism because blocked airflow paths limit their effectiveness.
  - testers prefer spacing the fins with washers or pivoting to ferrofluid/oil cooling when they need real thermal headroom.[^126]
- Judge cooling tweaks only with controlled A/B runs on fully cooled motors; hub-shell surface temperature alone says little about magnet health, so embed sensors or log winding temps before declaring success.[^127]
- Longitudinal skid plates need real thermal interfaces: a 3 mm aluminum plate ran 54 °C without paste even with decent airflow, so builders now add high-quality compound, consider 25 mm fins or thicker stock, and clamp controllers hard against the plate before trusting it for sustained pulls.[^128]
- Deck-mounted fan kits struggle when they blow straight into enclosure walls; tuners wedge spacers or relocate fans externally so airflow actually crosses heat sinks instead of recirculating warm air inside sealed decks.[^129]

## Overload Warning Signs

- Pushing a stock 350 W Ninebot MAX hub to ~5 kW on 72 V/35 A tunes cooks magnets and windings.
  - the rotor feels “full of honey” when spun by hand, signalling demagnetisation or shorts that no amount of firmware tweaking will fix.[^130]

## Sealed Bearing Service Cheatsheet

- Pack sealed bearings to roughly 30 % of the cavity with high-temperature grease (Mobil XHP 222 or similar); overfilling to 100 % just churns heat and purges grease past the seals on the first ride.[^131]
- Choose C3 clearance bearings when hubs see high heat or prolonged highway runs—the extra internal play prevents bind-up once the races expand.[^131]
- Document every bearing change with mileage and grease type so follow-up inspections can flag premature wear before shells overheat or magnets rub.[^131]

## Weatherproofing Hub Cavities

- Tear down Ninebot F2 Pro hubs after rain commutes.
  - the factory 6001RS bearings arrive nearly dry, so riders repack them with marine or polyurea grease and upgrade to premium SKF RSH 2RS units rather than smearing silicone over the caps.[^132]
- When resealing Zero or Vsett hubs, apply silicone at seam joints, refresh lithium grease on the bearings, and avoid overfilling so heat can still escape; the goal is to stop rust and hall failures without trapping moisture against the windings.[^133][^134]
- Waterlogged Pro 2 hubs with melted slot liners need full strip-downs.
  - resolder phase joints, dry the stator, and recoat with neutral-cure RTV so the next ride doesn’t short MOSFETs instantly.[^135]

## Field Gauges & Coolant Debates

- Eduuuuuuuuu’s “ten-second touch test” remains a simple thermal sanity check.
  - if you cannot keep a hand on the motor shell for ten seconds, drop phase amps before heat soaks the windings.[^136]
- Shlomozero’s 75 H 22/3 test hit ~80 °C within minutes at 400 A because undersized phase leads bottlenecked cooling; peers now hold the same hardware nearer 200–250 A motor current and treat 300 A uphill bursts as a winding death sentence.[^137][^138][^139]
- Arnau’s single-motor 75 H 22/3 setup stayed below 90 °C at 200 A phase once he swapped the thermistor pull-up to 100 kΩ, pairing a Ubox 240 with a 20 S 6 P P45B pack and ANT 450 A BMS.
  - evidence that accurate sensing plus sane currents keep Daly-equipped commuters alive.[^140]
- Matthew continues to see ~30 °C drops within minutes when hubs get ≈4 ml of Statorade, but Haku cautions that sealing the air gap can overheat magnets.
  - log magnet temps and weigh long-term wear before filling every race hub.[^141]
- Noname’s KTY-83 probe spikes instantly with throttle even when the stock NTC track looks calm, hinting at electrical noise and renewing interest in ferrofluid for both thermal damping and acoustic quieting on high-speed Lonnyo hubs.[^142]
- Yamal’s dual 33/2 windings hold roughly 49–63 °C during hard pulls, proving so-called “speed” winds can still deliver torque when the pack and cooling strategy are dialed.[^143]
- Heavy scooter harnesses show their limits quickly: even 8 AWG looms start heating around 150 A, and Paolo logged sub-50 % efficiency once bursts climbed toward 330 A without forced-air cooling and vented covers to keep the stator in check.[^144]

## Rotor & Magnet Integrity

- 7" LY 90 H hubs run a 127 mm stator with 40-magnet rotors, hitting noticeably harder than 110 mm-class cans but forcing builders onto matching 7" tire inventory and careful chassis clearance checks.[^145]
- Strip corrosion and reglue loose magnets on “new” hubs before riding.
  - VSETT assemblies have arrived rusty with magnets shifting, and veterans clean the rotor then bond magnets back with Loctite AA326 before reassembly.[^146]
- Double-magnet 80 H stacks have twisted stators after 350–500 A assaults and 133–144 °C cores; Paolo warns lamination glue softens and magnets can demagnetise past ≈120 °C, so log temps and back current down before the damage becomes permanent.[^147]
- After pothole strikes at speed, Lonnyo/Shul race hubs that trip current or throw “voltage imbalance” faults should be torn down to inspect magnets, hall boards, and harness strain before the next run.[^148]

## Coil Retention & Harness Dressing

- Inside hub motors, standard nylon cable ties survive stator temperatures when cinched correctly; some builders still wrap phases with cotton rope for redundancy, so combining both methods keeps windings tight without melting ties.[^149]
- Rewind workflows fold 0.2 mm copper into 0.8 mm busbars, crimp then solder the phases, and bury thermistors deep in the windings so thermal feedback reacts quickly during high-load pulls.[^150]

## Axle Retainers & Circlips

- Reinstall the axle circlip before sealing a hub.
  - omitting it lets the stator drift along the shaft under load despite magnetic drag, risking rotor contact or bearing wear. Builders now reopen freshly sealed motors to refit the ring rather than gambling on friction alone.[^151]

## Adhesives & Sensor Retention

- Hall sensors that walk out of their slots should be glued with heat-tolerant RTV 704 or slow-drying high-temp silicone; super glue works after scuffing the pocket but runs hotter under load.[^152]
- Keep 704 RTV on the bench for accessory wiring too.
  - the same adhesive secures buck-converter leads so vibration cannot snap them before the scooter ever rolls out.[^153][^154]

## VSETT Hub Thermal Rebuild Procedure

- **Overheated VSETT hubs need methodical repair.** Single-motor riders pushing 190 A phase / 90 A battery overheated new VSETT hubs within kilometres; the fix is to cap phase current near 140–160 A, strip and resolder discoloured phase joints with a high-watt iron after burning off enamel, clean stray solder, and add temperature sensing before retrying.[^vsett_rebuild]
- **Raise sensorless handoff when heat-related stutter appears.** The same hub quit stuttering once sensorless transition was raised from 500 to ~3,000 eRPM, then ran smoothly with 20 A of field weakening, duty capped around 85–89%, and an 800 ms FW ramp to soften current spikes above 55 km/h.[^sensorless_handoff]

## Motor Temperature Instrumentation

- **Install proper NTC sensors for accurate readings.** Installing EPCOS/TDK B57861S0502F040 2×4 mm NTCs against the hall/phase bundle, secured with thermal epoxy rated to 150 °C, delivered accurate phase readings in minutes and enables reliable over-temp cutbacks.[^ntc_install]
- **Embed 100 k probes under the windings.** Builders settled on epoxy-coated 100 k B3950 NTC sensors with one-metre leads, gluing them beneath the windings with silicone before routing a single temp wire through the axle alongside phase and hall conductors to keep telemetry stable at high current.[^155]
- **Route temp leads away from phase bundles.** Gordan's Ubox V2 logs showed thermistor signals collapsing above 80 A until he chased the ground loop, underscoring the need to reroute sensor wiring or add shielding when phase currents spike.[^temp_routing]
- **Relocate sensors toward the magnet gap when possible.** Artem is experimenting with moving hub thermistors into the air gap so readings reflect magnet temperature instead of coil hotspots.
  - a better proxy for demag risk on ventilated rims.[^156]
- **Trust embedded sensors over hand checks.** Artem’s Vsett logs showed hub shells barely warm while windings hit ~90 °C, proving that hand tests lag true winding temperature and that 100 kΩ NTC probes inside the hub are essential on high-power conversions.[^157]

## Efficiency Planning

- Artem pegs real-world BLDC outrunners around 86 % efficient in block commutation and higher under FOC; holding the motor near its rpm sweet spot pays off more than brute-force phase amps on small scooter hubs.[^158]
- **Inject ferrofluid without disturbing sensors.** Dose hubs through existing cover screws or dedicated ports, then reseal both side covers so fluid stays put during high-speed runs.
  - no need to pull hall boards if you plan ahead.[^159]
- **Verify sensor curves before trusting logs.** Builders embedding 10 k B3950 or 100 k probes inside VSETT hubs warn that generic PC temperature sensors rarely match VESC lookup tables, so capture beta values and confirm readings before relying on them for cutoffs.[^160]

## Phase Resistance Diagnostics

- Sloppy XT150 soldering and long leads have returned 53 mΩ readings that masquerade as “bad motors”; reflow strands tight to the connector walls and shorten runs before blaming the hub.[^161]
- Reference healthy baselines: HM 1600 W hubs sit near 132 mΩ, Blade motors around 85 mΩ, and Rion-spec hubs roughly 50 mΩ.
  - use these numbers when chasing unexplained heat.[^162]
- **Inject ferrofluid from the open cover.** Rather than drilling hubs, veterans crack the side cover and syringe Statorade along the stator slots to avoid misaligned holes and keep debris out of the rotor.[^163]

## 60H Hub Specific Notes

- **60H builds prefer 50 A battery / 100 A phase with ferrofluid.** Riders reported smooth launches after sealing leads, adding ferrofluid, and pairing the tune with ~10 A field-weakening that engages around 91.5% duty while holding full duty near 95%; still install temperature sensors before chasing 16 S, 60 km/h targets on long hill routes.[^60h_baseline]
- **Inject ferrofluid through the cable grommet, not with spray grease.** Veterans loosen RTV-sealed glands, push ≈4.5 ml of Statorade in with a syringe, and avoid aerosol greases that contaminate bearings.
  - airflow mods still matter once the stator saturates.[^164][^165]
- **Expect efficiency to crash past 330 A battery unless you add airflow.** Track logs showed <50 % motor efficiency, 133–162 Wh/km consumption, and low tire pressures to maintain grip when sealed hubs were over-driven.
  - proof that cooling upgrades are mandatory before chasing higher phase current.[^166]

## High-Torque Motor Stress & Thermal Limits

- Rental SNSC/350 W hubs saturate and shudder past roughly 25 A continuous per motor.
  - dual setups handle short 40 A bursts, but expect heat and torque ripple instead of miracles at 2.5 kW each.[^167]
- **80H 22×3 motors twisted stators after sustained high-current abuse.** Multiple builds failed after 350–500 A phase assaults at 133–144 °C core temps; prolonged heat softens lamination glue, and rotors demagnetize above ≈120 °C, especially on LY's double-magnet stack designs.[^80h-stress]
- **Magnet demagnetization occurs above 100–120 °C stator temps.** Paolo warned that magnets lose strength once core temps breach this threshold, and LY 70/75/80 H units have twisted under 400 A, prompting race teams to wind custom stators and mandate traction control even on 0–100 km/h builds that complete sprints in ~3.7 s.[^demagnetization]
- **Single 60H hubs survive 500 A launches at 107 km/h without field-weakening.** Leon's data demonstrates both torque potential and heat-management challenges when running smaller rotors at extreme phase current, underscoring the need for active cooling or conservative duty cycles on high-stress builds.[^60h-extreme]
- **Tiny 250–300 W hubs vaporise quickly at 72 V.** Feeding budget commuter motors 55–70 A phase on 20 S packs cooked two units back-to-back; without a temp probe the crew capped the last spare at ~35 A until a 350 W replacement arrives, reinforcing how little thermal headroom small cans have at high voltage.[^168]
- **7" LY 90H hub delivers harder launches than 110mm-class cans.** The 127 mm stator and 40-magnet rotor configuration hits harder than 75/80/90 H alternatives but demands matching 7" tire availability, limiting platform adoption compared to standard 6.5" wheel ecosystems.[^90h-torque]

## Magnet Inspection & Shipping Logistics

- **Inspect magnets for cracks or chips before installation.** High-torque builds should visually check rotor magnets for damage after shipping or pothole strikes, as cracked segments can fly apart under load and destroy windings.[^magnet-inspect]
- **European teams export race hardware to Israel by shipping rims and stators separately.** Face de Pin Sucé reports this approach avoids customs classification issues but requires labor-intensive assembly at destination, highlighting international sourcing challenges for high-performance components.[^magnet-shipping]

## Source Notes

[^vsett_rebuild]: VSETT hub overheating and methodical repair procedure.[^169][^170]
[^sensorless_handoff]: Sensorless handoff tuning to cure heat-related stutter.[^171][^172]
[^ntc_install]: Motor temperature sensor installation using EPCOS B57861S0502F040 NTCs.[^173][^174]
[^temp_routing]: Temperature sensor wiring away from phase bundles to avoid ground loops.[^175]
[^60h_baseline]: 60H hub baseline tuning with ferrofluid and field-weakening.[^176]
[^80h-stress]: 80H 22×3 motors twisted stators after 350–500 A phase at 133–144 °C, with lamination glue softening under prolonged heat.[^177]
[^demagnetization]: Magnet demagnetization above 100–120 °C stator temps and LY double-magnet stack vulnerability at 400 A.[^178]
[^60h-extreme]: Single 60H hub surviving 500 A launches and 107 km/h without field-weakening, demonstrating torque potential and thermal challenges.[^179]
[^90h-torque]: 7" LY 90H hub with 127 mm stator and 40-magnet rotor delivering superior torque compared to 110mm-class alternatives.[^180]
[^magnet-inspect]: Magnet inspection recommendations for cracks or chips before installation on high-torque builds.[^181]
[^magnet-shipping]: European race hardware shipping to Israel via separate rim/stator shipments to avoid customs classification.[^182]
[^atf-leak]: Community members reported ATF seeping out of hubs and prefer ferrofluid-only fills while they wait for real hybrid-temperature data.[^183]
[^denis-nexun-ferro]: Source: knowledge/notes/denis_all_part02_review.md†L931-L931
[^denis-quarter-bottle]: Source: knowledge/notes/denis_all_part02_review.md†L989-L989
[^denis-abs-cooling]: Source: knowledge/notes/denis_all_part02_review.md†L941-L941
[^denis-waterloop-risk]: Source: knowledge/notes/denis_all_part02_review.md†L942-L942
[^xiaomi-99c]: Source: knowledge/notes/denis_all_part02_review.md†L1075-L1075


## References

[^1]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L422-L441
[^2]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L424-L441
[^3]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L456-L520
[^4]: Source: knowledge/notes/input_part003_review.md†L115-L115
[^5]: Source: knowledge/notes/input_part003_review.md†L240-L240
[^6]: Source: data/vesc_help_group/text_slices/input_part003.txt†L20860-L20920
[^7]: Source: data/vesc_help_group/text_slices/input_part005.txt†L23967-L23995
[^8]: Source: knowledge/notes/input_part011_review.md†L431-L433
[^9]: Source: knowledge/notes/input_part012_review.md†L41-L41
[^10]: Source: knowledge/notes/input_part012_review.md†L42-L42
[^11]: Source: knowledge/notes/denis_all_part02_review.md†L433-L436
[^12]: Source: knowledge/notes/denis_all_part02_review.md†L440-L441
[^13]: Source: knowledge/notes/input_part007_review.md†L48-L48
[^14]: Source: knowledge/notes/input_part007_review.md†L60-L60
[^15]: Source: knowledge/notes/input_part000_review.md†L597-L599
[^16]: Source: data/vesc_help_group/text_slices/input_part001.txt†L7901-L8089
[^17]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8079-L8109
[^18]: Source: data/vesc_help_group/text_slices/input_part001.txt†L10364-L10463
[^19]: Source: data/vesc_help_group/text_slices/input_part001.txt†L11119-L11187
[^20]: Source: data/vesc_help_group/text_slices/input_part001.txt†L6340-L6362
[^21]: Source: data/vesc_help_group/text_slices/input_part001.txt†L6800-L6821
[^22]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8038-L8098
[^23]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8601-L8607
[^24]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8772-L8786
[^25]: Source: data/vesc_help_group/text_slices/input_part002.txt†L27288-L27324
[^26]: Source: data/vesc_help_group/text_slices/input_part002.txt†L27471-L27523
[^27]: Source: knowledge/notes/input_part002_review.md†L435-L435
[^28]: Source: data/vesc_help_group/text_slices/input_part002.txt†L27496-L27523
[^29]: Source: data/vesc_help_group/text_slices/input_part002.txt†L22651-L22660
[^30]: Source: data/vesc_help_group/text_slices/input_part002.txt†L22679-L22735
[^31]: Source: knowledge/notes/input_part003_review.md†L33-L33
[^32]: Source: data/vesc_help_group/text_slices/input_part003.txt†L25740-L25827
[^33]: Source: data/vesc_help_group/text_slices/input_part003.txt†L25766-L25811
[^34]: Source: data/vesc_help_group/text_slices/input_part003.txt†L25888-L25910
[^35]: Source: data/vesc_help_group/text_slices/input_part003.txt†L25795-L25811
[^36]: Source: data/vesc_help_group/text_slices/input_part003.txt†L337-L345
[^37]: Source: knowledge/notes/input_part010_review.md†L28-L29
[^38]: Source: knowledge/notes/input_part012_review.md†L198-L198
[^39]: Source: knowledge/notes/input_part012_review.md†L306-L306
[^40]: Source: knowledge/notes/input_part012_review.md†L217-L219
[^41]: Source: data/vesc_help_group/text_slices/input_part013.txt†L6230-L6247
[^42]: Source: knowledge/notes/input_part007_review.md†L18-L19
[^43]: Source: data/vesc_help_group/text_slices/input_part009.txt†L15009-L15026
[^44]: Source: data/vesc_help_group/text_slices/input_part011.txt†L19101-L19145
[^45]: Source: data/vesc_help_group/text_slices/input_part011.txt†L19136-L19173
[^46]: Source: knowledge/notes/input_part011_review.md†L377-L383
[^47]: Source: knowledge/notes/input_part011_review.md†L768-L769
[^48]: Source: knowledge/notes/input_part006_review.md†L152-L152
[^49]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L202-L223
[^50]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60020-L60025
[^51]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60009-L60024
[^52]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11037-L11042
[^53]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11045-L11076
[^54]: Source: knowledge/notes/input_part008_review.md†L224-L224
[^55]: Source: data/vesc_help_group/text_slices/input_part003.txt†L13806-L13840
[^56]: Source: knowledge/notes/input_part005_review.md†L236-L237
[^57]: Source: data/vesc_help_group/text_slices/input_part003.txt†L6630-L6678
[^58]: Source: data/vesc_help_group/text_slices/input_part003.txt†L7291-L7303
[^59]: Source: knowledge/notes/input_part002_review.md†L427-L428
[^60]: Source: data/vesc_help_group/text_slices/input_part003.txt†L7540-L7582
[^61]: Source: knowledge/notes/input_part014_review.md†L119-L119
[^62]: Source: data/vesc_help_group/text_slices/input_part003.txt†L23963-L24010
[^63]: Source: knowledge/notes/input_part002_review.md†L180-L181
[^64]: Source: data/vesc_help_group/text_slices/input_part003.txt†L16419-L16455
[^65]: Source: knowledge/notes/input_part005_review.md†L113-L121
[^66]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11480-L11520
[^67]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11588-L11670
[^68]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11686-L11699
[^69]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11491-L11507
[^70]: Source: knowledge/notes/input_part008_review.md†L225-L225
[^71]: Source: knowledge/notes/input_part005_review.md†L115-L124
[^72]: Source: knowledge/notes/input_part005_review.md†L111-L112
[^73]: Source: knowledge/notes/input_part005_review.md†L486-L488
[^74]: Source: knowledge/notes/input_part010_review.md†L27-L28
[^75]: Source: knowledge/notes/input_part010_review.md†L238-L240
[^76]: Source: knowledge/notes/input_part008_review.md†L25-L25
[^77]: Source: knowledge/notes/input_part008_review.md†L26-L26
[^78]: Source: knowledge/notes/input_part008_review.md†L27-L27
[^79]: Source: knowledge/notes/input_part008_review.md†L28-L28
[^80]: Source: knowledge/notes/input_part008_review.md†L29-L29
[^81]: Source: data/vesc_help_group/text_slices/input_part010.txt†L11244-L11250
[^82]: Source: knowledge/notes/input_part010_review.md†L398-L400
[^83]: Source: knowledge/notes/input_part007_review.md†L26-L26
[^84]: Source: knowledge/notes/input_part007_review.md†L28-L28
[^85]: Source: knowledge/notes/input_part007_review.md†L83-L83
[^86]: Source: knowledge/notes/input_part014_review.md†L120-L120
[^87]: Source: knowledge/notes/input_part014_review.md†L45-L45
[^88]: Source: knowledge/notes/input_part007_review.md†L78-L78
[^89]: Source: knowledge/notes/input_part007_review.md†L321-L322
[^90]: Source: knowledge/notes/input_part007_review.md†L537-L537
[^91]: Source: knowledge/notes/input_part000_review.md†L623-L626
[^92]: Source: knowledge/notes/input_part000_review.md†L626-L635
[^93]: Source: knowledge/notes/input_part000_review.md†L635-L639
[^94]: Source: knowledge/notes/input_part002_review.md†L484-L486
[^95]: Source: data/vesc_help_group/text_slices/input_part003.txt†L18986-L19004
[^96]: Source: knowledge/notes/input_part010_review.md†L26-L27
[^97]: Source: knowledge/notes/input_part012_review.md†L234-L235
[^98]: Source: knowledge/notes/input_part012_review.md†L235-L235
[^99]: Source: knowledge/notes/input_part012_review.md†L251-L251
[^100]: Source: knowledge/notes/input_part012_review.md†L236-L236
[^101]: Source: knowledge/notes/input_part012_review.md†L237-L237
[^102]: Source: knowledge/notes/input_part008_review.md†L284-L284
[^103]: Source: knowledge/notes/input_part012_review.md†L320-L320
[^104]: Source: knowledge/notes/input_part012_review.md†L195-L195
[^105]: Source: knowledge/notes/input_part012_review.md†L197-L197
[^106]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60004-L60008
[^107]: Source: knowledge/notes/input_part003_review.md†L103-L103
[^108]: Source: data/vesc_help_group/text_slices/input_part007.txt†L123-L146
[^109]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L90030-L90136
[^110]: Source: knowledge/notes/input_part000_review.md†L117-L117
[^111]: Source: knowledge/notes/input_part000_review.md†L531-L533
[^112]: Source: knowledge/notes/input_part000_review.md†L534-L534
[^113]: Source: knowledge/notes/denis_all_part02_review.md†L100305-L100375
[^114]: Source: knowledge/notes/denis_all_part02_review.md†L102534-L102548
[^115]: Source: knowledge/notes/denis_all_part02_review.md†L102538-L102548
[^116]: Source: knowledge/notes/input_part000_review.md†L614-L617
[^117]: Source: knowledge/notes/input_part008_review.md†L285-L285
[^118]: Source: knowledge/notes/input_part000_review.md†L304-L305
[^119]: Source: knowledge/notes/input_part000_review.md†L305-L305
[^120]: Source: knowledge/notes/input_part000_review.md†L306-L306
[^121]: Source: knowledge/notes/input_part000_review.md†L349-L350
[^122]: Source: knowledge/notes/input_part000_review.md†L658-L660
[^123]: Source: knowledge/notes/input_part000_review.md†L641-L642
[^124]: Source: knowledge/notes/input_part001_review.md†L613-L615
[^125]: Source: knowledge/notes/input_part001_review.md†L626-L627
[^126]: Source: knowledge/notes/input_part001_review.md†L672-L674
[^127]: Source: knowledge/notes/input_part001_review.md†L674-L674
[^128]: Source: knowledge/notes/input_part014_review.md†L3792-L3858
[^129]: Source: knowledge/notes/input_part014_review.md†L3588-L3636
[^130]: Source: knowledge/notes/input_part006_review.md†L42-L42
[^131]: Source: knowledge/notes/input_part006_review.md†L509-L509
[^132]: Source: knowledge/notes/input_part006_review.md†L409-L410
[^133]: Source: knowledge/notes/input_part006_review.md†L368-L368
[^134]: Source: knowledge/notes/input_part006_review.md†L488-L488
[^135]: Source: knowledge/notes/denis_all_part02_review.md†L338-L339
[^136]: Source: knowledge/notes/input_part013_review.md†L232-L233
[^137]: Source: data/vesc_help_group/text_slices/input_part013.txt†L9778-L9819
[^138]: Source: data/vesc_help_group/text_slices/input_part013.txt†L10160-L10169
[^139]: Source: data/vesc_help_group/text_slices/input_part013.txt†L10549-L10555
[^140]: Source: data/vesc_help_group/text_slices/input_part013.txt†L10221-L10248
[^141]: Source: data/vesc_help_group/text_slices/input_part013.txt†L10299-L10309
[^142]: Source: data/vesc_help_group/text_slices/input_part013.txt†L10245-L10253
[^143]: Source: knowledge/notes/input_part013_review.md†L715-L715
[^144]: Source: data/vesc_help_group/text_slices/input_part004.txt†L9418-L9434
[^145]: Source: knowledge/notes/input_part013_review.md†L445-L445
[^146]: Source: data/vesc_help_group/text_slices/input_part004.txt†L2133-L2152
[^147]: Source: knowledge/notes/input_part013_review.md†L446-L447
[^148]: Source: knowledge/notes/input_part013_review.md†L744-L767
[^149]: Source: knowledge/notes/input_part014_review.md†L185-L185
[^150]: Source: knowledge/notes/input_part014_review.md†L123-L123
[^151]: Source: data/vesc_help_group/text_slices/input_part000.txt†L22955-L22991
[^152]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131261-L131275
[^153]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L31-L32
[^154]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131265-L131275
[^155]: Source: data/vesc_help_group/text_slices/input_part001.txt†L11104-L11181
[^156]: Source: knowledge/notes/input_part000_review.md†L533-L533
[^157]: Source: knowledge/notes/input_part000_review.md†L676-L678
[^158]: Source: knowledge/notes/input_part000_review.md†L598-L598
[^159]: Source: data/vesc_help_group/text_slices/input_part001.txt†L11140-L11216
[^160]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8521-L8546
[^161]: Source: data/vesc_help_group/text_slices/input_part001.txt†L7532-L7599
[^162]: Source: data/vesc_help_group/text_slices/input_part001.txt†L7595-L7600
[^163]: Source: data/vesc_help_group/text_slices/input_part004.txt†L8825-L8851
[^164]: Source: knowledge/notes/input_part004_review.md†L205-L205
[^165]: Source: knowledge/notes/input_part004_review.md†L217-L217
[^166]: Source: knowledge/notes/input_part004_review.md†L208-L208
[^167]: Source: knowledge/notes/input_part005_review.md†L160-L160
[^168]: Source: knowledge/notes/input_part011_review.md†L373-L374
[^169]: Source: knowledge/notes/input_part004_review.md†L19-L19
[^170]: Source: knowledge/notes/input_part004_review.md†L94-L94
[^171]: Source: knowledge/notes/input_part004_review.md†L20-L20
[^172]: Source: knowledge/notes/input_part004_review.md†L96-L97
[^173]: Source: knowledge/notes/input_part004_review.md†L44-L44
[^174]: Source: knowledge/notes/input_part004_review.md†L69-L69
[^175]: Source: knowledge/notes/input_part004_review.md†L49-L49
[^176]: Source: knowledge/notes/input_part004_review.md†L36-L36
[^177]: Source: knowledge/notes/input_part013_review.md†L151-L153
[^178]: Source: knowledge/notes/input_part013_review.md†L151-L154
[^179]: Source: knowledge/notes/input_part013_review.md†L155-L155
[^180]: Source: knowledge/notes/input_part013_review.md†L150-L150
[^181]: Source: knowledge/notes/input_part013_review.md†L513-L513
[^182]: Source: knowledge/notes/input_part013_review.md†L156-L156
[^183]: Source: knowledge/notes/input_part002_review.md†L46-L48
