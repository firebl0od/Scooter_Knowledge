# Motor Cooling & Thermal Management Notes

## Why Fans Rarely Help Scooter Hubs
- Denis Yurev reminded the workshop that scooters already move fresh air past the hub at riding speed, so bolt-on fan kits add little cooling compared with ensuring good heat transfer from the windings to the shell.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L422-L441】
- Riders debating CPU-style blowers learned that evaporation-driven skin cooling does not apply to dry aluminum shells; without a wet surface the only lever is temperature delta, so focus on conductive paths instead of add-on spinners.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L424-L441】
- Veterans recommended ferrofluid or oil-fill experiments (with leak safeguards) if you need real winding-to-shell transfer—simply drilling covers or gluing “windmills” to the hub only cools the outer case.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L456-L520】
- Community case studies still favour passive conduction upgrades over active plumbing: Mirko’s 15 mm aluminum deck plate plus open vents held dual 190 A phase / 70 A battery runs near 52 °C, while heat-pipe experiments outperformed vibration-prone water loops on cramped decks.【F:knowledge/notes/input_part003_review.md†L115-L115】【F:knowledge/notes/input_part003_review.md†L240-L240】

## Motor Architecture Context
- Axial-flux scooter prototypes mount magnets on facing disks for high power density, while hybrid “raxial” concepts add more phases for torque; production hubs still favour radial flux because the hollow stator leaves little room for liquid cooling hardware and costs stay lower.【F:knowledge/notes/input_part012_review.md†L41-L41】
- Treat flashy “liquid-cooled radial hub” marketing videos skeptically—veterans spotted builds with only phase leads and no coolant plumbing, confirming many are passive designs dressed up for promotion.【F:knowledge/notes/input_part012_review.md†L42-L42】

## Ferrofluid Selection & Handling
- The VESC Help crew continues to vouch for ferrofluid/Statorade when the goal is winding-to-shell transfer, but they emphasise reading datasheets—some mixes flash at low temperature and budget hubs can demagnetise above ~80 °C—before flooding a motor.【F:knowledge/notes/input_part007_review.md†L48-L48】
- Ferrotec APG1110 remains the benchmark for hub fillings, while Supermagnete’s 10 mL bottles offer reliable sourcing for EU riders upgrading Xiaomi and G30 hubs without importing large lots.【F:knowledge/notes/input_part007_review.md†L60-L60】
- Ferrofluid refreshes should be sparing—apply a thin bead between magnets and add a dedicated temperature probe so rising wattage doesn’t go unnoticed after the fill.【F:knowledge/notes/input_part012_review.md†L198-L198】
- Segway-class hub service days now pair ferrofluid top-ups with temperature-probe checks; bake those steps into maintenance lists before long tours so commuter fleets don’t head into rain weeks with dry stators.【F:knowledge/notes/input_part012_review.md†L306-L306】
- Before drilling breather ports, builders mark bit depth, stop once the cover breaks through, and reseal with clear RTV after filling; adding a temp sensor during the same service keeps long-term monitoring simple.【F:knowledge/notes/input_part012_review.md†L217-L219】

## Hub Current Guardrails
- Single Monorim 500 W hubs stay happy around 80 A phase—ideally with ferrofluid—while the crew’s Xiaomi-class builds overheat quickly once they push 65–73 A without battery temperature sensing or keep more than roughly 30–35 A combined draw from paired 12 S packs.【F:knowledge/notes/input_part007_review.md†L18-L19】

## Micro-Hub Voltage Stress Signals
- Doubling a Xiaomi/Ninebot commuter from 10 S to 20 S roughly doubles the free-spin speed but repeatedly burns the stock hub from heat saturation, so builders now treat 18 S as the limit unless they add serious cooling or swap motors.【F:data/vesc_help_group/text_slices/input_part011.txt†L19101-L19145】
- Fiido L3 rear hubs emerged as the go-to drop-in upgrade for 20 S experiments because their wider stator and exposed shell shed heat far better than Xiaomi-class cans—veterans report killing three narrow hubs in two days while the Fiido survived on a Spintend 100 V Lite.【F:data/vesc_help_group/text_slices/input_part011.txt†L19136-L19173】
- GABE is also sandwiching aluminium plates with thermal paste around a 10 mm 3D-printed spacer to keep his 250 W commuter hub cool after widening the dropout, showing how thin filler plates can restore conduction when packaging changes add air gaps.【F:knowledge/notes/input_part011_review.md†L768-L769】

## Controller Interface Refresh Checklist
- When raising voltage, replace Kapton tape with 0.5 mm thermal pads so MOSFETs stay isolated yet shed heat; stacking pads on top of Kapton just adds resistance.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L202-L223】
- Sand controller bases, clean MOSFET tabs, and reinstall paste before clamping the box—loose wiring under the plate prevents full contact and spikes temperatures on the first ride.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60020-L60025】
- Keep silicone pads on hand when chasing 48 V/15 S tunes; the crew pairs IRFB4110 MOSFETs with 100 V 1,000 µF and 47 µF capacitors and swaps pads plus paste before closing the case.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60009-L60024】
- Deck-mounted controller plates should be sanded to bare metal and paired with thin thermal pads; open-vent decks plus 15 mm aluminum plates have proven the most repeatable way to keep single- and dual-motor builds near 50 °C under 190 A phase loads.【F:knowledge/notes/input_part003_review.md†L115-L115】
- Hard-mount controllers whenever possible: bolting a MakerX HI100 to an aluminum cradle dropped case temps to ~23 °C on 60 A battery / 200 A phase pulls at 7 °C ambient versus 60–80 °C when the unit was bag-mounted.【F:data/vesc_help_group/text_slices/input_part003.txt†L13806-L13840】
- Mirko’s machined radiator plate hangs roughly 3 cm below the frame (7.5 cm ground clearance unloaded) and needs insulated FET interfaces plus potential heat pipes to spread hotspot load—log spacer stacks and insulation plans before copying the design.【F:data/vesc_help_group/text_slices/input_part003.txt†L6630-L6678】【F:data/vesc_help_group/text_slices/input_part003.txt†L7291-L7303】

### Deck Radiator & Thermal Interface Experiments
- Community photos comparing thick paste bridges against bare ergal vs. 6061 plates showed paste still outperforms air gaps, but PCB-mounted probes can lag case temperature by several degrees—treat onboard telemetry as relative trends, not absolute hotspots.【F:data/vesc_help_group/text_slices/input_part003.txt†L7540-L7582】
- VSETT stator rewinds revealed lacquer-shelled star points barely wetted from the factory; torch the enamel, brush clean, and fully re-solder before running fresh motor detection to cut resistance and heat soak.【F:data/vesc_help_group/text_slices/input_part003.txt†L23963-L24010】
- Heat-pipe arrays are supplanting water loops on compact decks; builders now pair finned pipes with QS8-class harnesses and 10 mm² (≈8 AWG) leads when paralleling external packs so 80 A continuous transfers without cooking insulation.【F:data/vesc_help_group/text_slices/input_part003.txt†L16419-L16455】

## Heat Transfer Upgrades from VESC Field Logs
- Spintend dual-Ubox owners report the factory ships thermal pads (not paste) on MOSFET plates; lapping the deck and adding fresh paste keeps Laotie builds under ≈80 °C even on hard pulls.【F:knowledge/notes/input_part005_review.md†L113-L121】
- Epoxy putty doubles as a heat spreader around controller cases while builders embed thermistors through the existing hall harness and pot them with epoxy or silicone for direct winding contact.【F:knowledge/notes/input_part005_review.md†L115-L124】
- Resin-potted water-cooled Flipsky builds now ship with INA181 phase sensors and denser heatsinks, but veterans still expect MOSFET-to-heatsink contact to be the bottleneck until independent testing confirms the claimed improvements.【F:knowledge/notes/input_part005_review.md†L486-L488】

## Controller Mounting & Airflow Discipline
- Track-focused builders now strip paint, drill fresh bolt holes, clamp controllers with washers and threadlocker, add thermal paste, and route heat into the chassis or external sinks; relying on foam or internal fans in sealed bays just cooks the controllers.【F:knowledge/notes/input_part007_review.md†L26-L26】【F:knowledge/notes/input_part007_review.md†L28-L28】
- External fins need real airflow—drop the heatsink through the deck, drill and tap anchors, and bolt the controller straight to the frame with paste; leaving fins flush inside the deck traps hot air.【F:knowledge/notes/input_part007_review.md†L83-L83】
- Skip brazing aluminum frames for heatsink bonding unless you have specialty tooling; even experienced metalworkers called it a last resort compared with mechanical fasteners.【F:knowledge/notes/input_part007_review.md†L78-L78】
- When clamping copper blocks to aluminum frames, isolate them with silicone sheets or plating; bare copper-on-aluminum mounts trigger galvanic corrosion that quietly eats the chassis.【F:knowledge/notes/input_part007_review.md†L321-L322】
- Dial in airflow paths after rework—builders now notch decks, tap fins, and bridge controllers to fresh-cut ducts so heat actually leaves the bay instead of recirculating behind sealed covers.【F:knowledge/notes/input_part007_review.md†L537-L537】

## Controller Cooling Case Studies
- Jason resurrected an MP2 after a MOSFET failure and now caps the platform around 100 A battery / 250 A phase, acknowledging a 300 A launch cooked the board while chasing sensor cogging.【F:knowledge/notes/input_part012_review.md†L234-L235】
- Finn keeps an Ubox Lite below 50 °C while pulling 160 A phase / 90 A battery by swapping in Arctic MX4 paste and bolting through the controller’s M2 bosses into a 3 mm aluminum belly pan.【F:knowledge/notes/input_part012_review.md†L235-L235】【F:knowledge/notes/input_part012_review.md†L251-L251】
- Matthew’s DIY water loop dropped his VESC enclosure from ~90 °C cutbacks to ~26–28 °C during 45 mph pulls; Noname is planning a moped-sized radiator, pump, and expansion tank to scale the concept.【F:knowledge/notes/input_part012_review.md†L236-L236】
- Swapping to higher-grade thermal paste still nets ~5 °C improvements, but veterans stress optimizing airflow before escalating to liquid cooling complexity.【F:knowledge/notes/input_part012_review.md†L237-L237】
- Fold these Lite and MP2 mitigation case studies into controller SOP binders—document Arctic MX4 swaps, belly-plate mounting, and air-vs.-liquid trade-offs so future tear-downs start with proven recipes instead of trial-and-error.【F:knowledge/notes/input_part012_review.md†L320-L320】

## Temperature Guardrails
- Misconfigured thermistors triggered limp mode within 15 minutes on a modest 48 V 800 W hub; confirm the sensor type (NTC 100 k vs. alternatives) with a meter or disable the probe until the value matches reality.【F:knowledge/notes/input_part012_review.md†L195-L195】
- Dual 90 H builds logged ~58 °C rear / 48 °C front after a 24 km, 10 % grade climb in 25 °C ambient—use those numbers as a sanity check for 75 200/85 150 setups before raising current further.【F:knowledge/notes/input_part012_review.md†L197-L197】
- Battery temps around 41 °C were deemed healthy for summer rides, but the group flagged ~60 °C as a ceiling—anything hotter accelerates degradation and calls for gentler tunes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60004-L60008】
- Makerbase 100/100-class controllers start current limiting once MOSFETs touch ~70 °C if the base plate lacks fresh thermal paste; the crew now treats 70 °C as the everyday limit and 100 °C as the hard ceiling for VESC MOSFETs to preserve lifespan.【F:data/vesc_help_group/text_slices/input_part007.txt†L123-L146】
- Larger packs and long shocks trap heat around the deck; riders re-bend frames, add inner/outer steel plates, and swap to lower-rate springs instead of trimming coils so the chassis and cells stop cooking each other.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L90030-L90136】
- Abuse tests that pumped 84 V/2 000 W into stock 250 W hubs demagnetised rotors once magnets crossed ~80 °C, permanently reducing speed—log stator temps on recycled hardware before chasing high-voltage experiments.【F:knowledge/notes/input_part000_review.md†L117-L117】
- Weped-mounted dual Uboxes still brushed ~80 °C delivering ~500 A phase until riders resurfaced the deck and clamped the controller directly with fresh thermal paste—remote radiator boxes and thick spacers only added heat soak.【F:knowledge/notes/input_part000_review.md†L614-L617】
- Even robust controllers cannot save undersized hubs: a 750 W Boosted Rev on a Spintend single hit 55 °C controller / 80 °C stator in eight minutes at 120 A phase / 80 A battery, proving you must tune current to motor mass, not ESC ceiling.【F:knowledge/notes/input_part000_review.md†L304-L305】
- Regen spikes add heat too—phase clipping kicked in around 25–30 km/h and each hard brake pulse lifted the stator roughly 5 °C, so log braking currents whenever you raise negative amps.【F:knowledge/notes/input_part000_review.md†L305-L305】
- Field-weakening remains a high-speed tool only; riders toggle it above cruise speed after seeing 20–40 km/h gains at the cost of huge current draw and extra heat when left on below the duty sweet spot.【F:knowledge/notes/input_part000_review.md†L306-L306】【F:knowledge/notes/input_part000_review.md†L349-L350】
- Embed 100 kΩ NTC probes inside the windings on Vsett-class builds—the shell can feel cool while the coils touch 90 °C, and pairing the sensors with FOC controllers keeps launches smooth while logging real stator temps.【F:knowledge/notes/input_part000_review.md†L658-L660】
- Overvolting an 800 W Citycoco hub to 26 S/100 A cooked the windings mid-hill, underscoring how quickly small motors die when voltage climbs faster than thermal paths—treat voltage bumps as motor swaps, not just controller tweaks.【F:knowledge/notes/input_part000_review.md†L641-L642】

## Ferrofluid Handling & Hub Maintenance
- Dose scooter hubs with roughly 3–6 ml of Statorade (60 mm motors stretch to 7–8 ml) only after the stator is seated; plastic syringes keep filings out while the magnets self-level the fluid.【F:knowledge/notes/input_part001_review.md†L613-L615】
- Reseal side covers with silicone and revisit fills seasonally—vent holes can shave another 5–10 °C on smaller motors but risk weeping ferrofluid and inviting water, so log temps before committing to drilled covers.【F:knowledge/notes/input_part001_review.md†L613-L615】
- Wolf Warrior hubs that survived ~10,000 km came back with cracked phase insulation and missing hall boards; use refreshes to rewire phases, embed new hall sensors, and add Statorade while the shell is open.【F:knowledge/notes/input_part001_review.md†L626-L627】

## Cooling Accessory Reality Checks
- 3D-printed “hub fin” shells draw criticism because blocked airflow paths limit their effectiveness—testers prefer spacing the fins with washers or pivoting to ferrofluid/oil cooling when they need real thermal headroom.【F:knowledge/notes/input_part001_review.md†L672-L674】
- Judge cooling tweaks only with controlled A/B runs on fully cooled motors; hub-shell surface temperature alone says little about magnet health, so embed sensors or log winding temps before declaring success.【F:knowledge/notes/input_part001_review.md†L674-L674】

## Overload Warning Signs
- Pushing a stock 350 W Ninebot MAX hub to ~5 kW on 72 V/35 A tunes cooks magnets and windings—the rotor feels “full of honey” when spun by hand, signalling demagnetisation or shorts that no amount of firmware tweaking will fix.【F:knowledge/notes/input_part006_review.md†L42-L42】

## Sealed Bearing Service Cheatsheet
- Pack sealed bearings to roughly 30 % of the cavity with high-temperature grease (Mobil XHP 222 or similar); overfilling to 100 % just churns heat and purges grease past the seals on the first ride.【F:knowledge/notes/input_part006_review.md†L509-L509】
- Choose C3 clearance bearings when hubs see high heat or prolonged highway runs—the extra internal play prevents bind-up once the races expand.【F:knowledge/notes/input_part006_review.md†L509-L509】
- Document every bearing change with mileage and grease type so follow-up inspections can flag premature wear before shells overheat or magnets rub.【F:knowledge/notes/input_part006_review.md†L509-L509】

## Weatherproofing Hub Cavities
- Tear down Ninebot F2 Pro hubs after rain commutes—the factory 6001RS bearings arrive nearly dry, so riders repack them with marine or polyurea grease and upgrade to premium SKF RSH 2RS units rather than smearing silicone over the caps.【F:knowledge/notes/input_part006_review.md†L409-L410】
- When resealing Zero or Vsett hubs, apply silicone at seam joints, refresh lithium grease on the bearings, and avoid overfilling so heat can still escape; the goal is to stop rust and hall failures without trapping moisture against the windings.【F:knowledge/notes/input_part006_review.md†L368-L368】【F:knowledge/notes/input_part006_review.md†L488-L488】

## Field Gauges & Coolant Debates
- Eduuuuuuuuu’s “ten-second touch test” remains a simple thermal sanity check—if you cannot keep a hand on the motor shell for ten seconds, drop phase amps before heat soaks the windings.【F:knowledge/notes/input_part013_review.md†L232-L233】
- Shlomozero’s 75 H 22/3 test hit ~80 °C within minutes at 400 A because undersized phase leads bottlenecked cooling; peers now hold the same hardware nearer 200–250 A motor current and treat 300 A uphill bursts as a winding death sentence.【F:data/vesc_help_group/text_slices/input_part013.txt†L9778-L9819】【F:data/vesc_help_group/text_slices/input_part013.txt†L10160-L10169】【F:data/vesc_help_group/text_slices/input_part013.txt†L10549-L10555】
- Arnau’s single-motor 75 H 22/3 setup stayed below 90 °C at 200 A phase once he swapped the thermistor pull-up to 100 kΩ, pairing a Ubox 240 with a 20 S 6 P P45B pack and ANT 450 A BMS—evidence that accurate sensing plus sane currents keep Daly-equipped commuters alive.【F:data/vesc_help_group/text_slices/input_part013.txt†L10221-L10248】
- Matthew continues to see ~30 °C drops within minutes when hubs get ≈4 ml of Statorade, but Haku cautions that sealing the air gap can overheat magnets—log magnet temps and weigh long-term wear before filling every race hub.【F:data/vesc_help_group/text_slices/input_part013.txt†L10299-L10309】
- Yamal’s dual 33/2 windings hold roughly 49–63 °C during hard pulls, proving so-called “speed” winds can still deliver torque when the pack and cooling strategy are dialed.【F:knowledge/notes/input_part013_review.md†L715-L715】

## Rotor & Magnet Integrity
- 7" LY 90 H hubs run a 127 mm stator with 40-magnet rotors, hitting noticeably harder than 110 mm-class cans but forcing builders onto matching 7" tire inventory and careful chassis clearance checks.【F:knowledge/notes/input_part013_review.md†L445-L445】
- Double-magnet 80 H stacks have twisted stators after 350–500 A assaults and 133–144 °C cores; Paolo warns lamination glue softens and magnets can demagnetise past ≈120 °C, so log temps and back current down before the damage becomes permanent.【F:knowledge/notes/input_part013_review.md†L446-L447】
- After pothole strikes at speed, Lonnyo/Shul race hubs that trip current or throw “voltage imbalance” faults should be torn down to inspect magnets, hall boards, and harness strain before the next run.【F:knowledge/notes/input_part013_review.md†L744-L767】

## Coil Retention & Harness Dressing
- Inside hub motors, standard nylon cable ties survive stator temperatures when cinched correctly; some builders still wrap phases with cotton rope for redundancy, so combining both methods keeps windings tight without melting ties.【F:knowledge/notes/input_part014_review.md†L185-L185】

## Axle Retainers & Circlips
- Reinstall the axle circlip before sealing a hub—omitting it lets the stator drift along the shaft under load despite magnetic drag, risking rotor contact or bearing wear. Builders now reopen freshly sealed motors to refit the ring rather than gambling on friction alone.【F:data/vesc_help_group/text_slices/input_part000.txt†L22955-L22991】

## Adhesives & Sensor Retention
- Hall sensors that walk out of their slots should be glued with heat-tolerant RTV 704 or slow-drying high-temp silicone; super glue works after scuffing the pocket but runs hotter under load.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131261-L131275】
- Keep 704 RTV on the bench for accessory wiring too—the same adhesive secures buck-converter leads so vibration cannot snap them before the scooter ever rolls out.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L31-L32】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131265-L131275】

## VSETT Hub Thermal Rebuild Procedure
- **Overheated VSETT hubs need methodical repair.** Single-motor riders pushing 190 A phase / 90 A battery overheated new VSETT hubs within kilometres; the fix is to cap phase current near 140–160 A, strip and resolder discoloured phase joints with a high-watt iron after burning off enamel, clean stray solder, and add temperature sensing before retrying.[^vsett_rebuild]
- **Raise sensorless handoff when heat-related stutter appears.** The same hub quit stuttering once sensorless transition was raised from 500 to ~3,000 eRPM, then ran smoothly with 20 A of field weakening, duty capped around 85–89%, and an 800 ms FW ramp to soften current spikes above 55 km/h.[^sensorless_handoff]

## Motor Temperature Instrumentation
- **Install proper NTC sensors for accurate readings.** Installing EPCOS/TDK B57861S0502F040 2×4 mm NTCs against the hall/phase bundle, secured with thermal epoxy rated to 150 °C, delivered accurate phase readings in minutes and enables reliable over-temp cutbacks.[^ntc_install]
- **Route temp leads away from phase bundles.** Gordan's Ubox V2 logs showed thermistor signals collapsing above 80 A until he chased the ground loop, underscoring the need to reroute sensor wiring or add shielding when phase currents spike.[^temp_routing]

## 60H Hub Specific Notes
- **60H builds prefer 50 A battery / 100 A phase with ferrofluid.** Riders reported smooth launches after sealing leads, adding ferrofluid, and pairing the tune with ~10 A field-weakening that engages around 91.5% duty while holding full duty near 95%; still install temperature sensors before chasing 16 S, 60 km/h targets on long hill routes.[^60h_baseline]

## High-Torque Motor Stress & Thermal Limits
- **80H 22×3 motors twisted stators after sustained high-current abuse.** Multiple builds failed after 350–500 A phase assaults at 133–144 °C core temps; prolonged heat softens lamination glue, and rotors demagnetize above ≈120 °C, especially on LY's double-magnet stack designs.[^80h-stress]
- **Magnet demagnetization occurs above 100–120 °C stator temps.** Paolo warned that magnets lose strength once core temps breach this threshold, and LY 70/75/80 H units have twisted under 400 A, prompting race teams to wind custom stators and mandate traction control even on 0–100 km/h builds that complete sprints in ~3.7 s.[^demagnetization]
- **Single 60H hubs survive 500 A launches at 107 km/h without field-weakening.** Leon's data demonstrates both torque potential and heat-management challenges when running smaller rotors at extreme phase current, underscoring the need for active cooling or conservative duty cycles on high-stress builds.[^60h-extreme]
- **7" LY 90H hub delivers harder launches than 110mm-class cans.** The 127 mm stator and 40-magnet rotor configuration hits harder than 75/80/90 H alternatives but demands matching 7" tire availability, limiting platform adoption compared to standard 6.5" wheel ecosystems.[^90h-torque]

## Magnet Inspection & Shipping Logistics
- **Inspect magnets for cracks or chips before installation.** High-torque builds should visually check rotor magnets for damage after shipping or pothole strikes, as cracked segments can fly apart under load and destroy windings.[^magnet-inspect]
- **European teams export race hardware to Israel by shipping rims and stators separately.** Face de Pin Sucé reports this approach avoids customs classification issues but requires labor-intensive assembly at destination, highlighting international sourcing challenges for high-performance components.[^magnet-shipping]

## Source Notes
[^vsett_rebuild]: VSETT hub overheating and methodical repair procedure.【F:knowledge/notes/input_part004_review.md†L19-L19】【F:knowledge/notes/input_part004_review.md†L94-L94】
[^sensorless_handoff]: Sensorless handoff tuning to cure heat-related stutter.【F:knowledge/notes/input_part004_review.md†L20-L20】【F:knowledge/notes/input_part004_review.md†L96-L97】
[^ntc_install]: Motor temperature sensor installation using EPCOS B57861S0502F040 NTCs.【F:knowledge/notes/input_part004_review.md†L44-L44】【F:knowledge/notes/input_part004_review.md†L69-L69】
[^temp_routing]: Temperature sensor wiring away from phase bundles to avoid ground loops.【F:knowledge/notes/input_part004_review.md†L49-L49】
[^60h_baseline]: 60H hub baseline tuning with ferrofluid and field-weakening.【F:knowledge/notes/input_part004_review.md†L36-L36】
[^80h-stress]: 80H 22×3 motors twisted stators after 350–500 A phase at 133–144 °C, with lamination glue softening under prolonged heat.【F:knowledge/notes/input_part013_review.md†L151-L153】
[^demagnetization]: Magnet demagnetization above 100–120 °C stator temps and LY double-magnet stack vulnerability at 400 A.【F:knowledge/notes/input_part013_review.md†L151-L154】
[^60h-extreme]: Single 60H hub surviving 500 A launches and 107 km/h without field-weakening, demonstrating torque potential and thermal challenges.【F:knowledge/notes/input_part013_review.md†L155-L155】
[^90h-torque]: 7" LY 90H hub with 127 mm stator and 40-magnet rotor delivering superior torque compared to 110mm-class alternatives.【F:knowledge/notes/input_part013_review.md†L150-L150】
[^magnet-inspect]: Magnet inspection recommendations for cracks or chips before installation on high-torque builds.【F:knowledge/notes/input_part013_review.md†L513-L513】
[^magnet-shipping]: European race hardware shipping to Israel via separate rim/stator shipments to avoid customs classification.【F:knowledge/notes/input_part013_review.md†L156-L156】
