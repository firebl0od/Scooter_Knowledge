# High-Power VESC Scooter Reliability Field Guide

A distilled playbook for keeping race-level VESC builds dependable when running 15S–22S packs, 200 A+ phase currents, and long-range commuting setups.

## 1. Build Planning & Component Selection

- **Controller tiers:** Treat Makerbase/Flipsky aluminum-PCB boxes as interim ≤15 S 50 A solutions; high-power riders standardize on 3Shul C350/CL350, Ubox duals, or BRIESC units for thermal headroom and QC maturity.[^1][^2][^3]
- **Spintend for Vsett 10+ swaps.** Crew consensus still leans on Spintend’s 12-fet controllers when Vsett 10+ owners want Bluetooth profile switching; the chassis’ larger deck, custom suspension, and improved stem/clamp make packaging bigger batteries easier than on Zero 10X frames.[^spintend-vsett]
- **Torque hardware before shakedowns.** Ebike conversions running VESCs have thrown axles within metres when relying on washers; file torque-arm slots for an interference fit, add pinch bolts so 10 mm steel clamps carry axle load, and tighten with short-handled sockets in small increments to avoid crushing thin dropouts.[^1][^2]
- **Plan closed-course validation for high-speed pulls.** 🇪🇸AYO#74’s 131 km/h rear-motor run ran out of runway, reinforcing that 30 kW scooters need long, obstacle-free straights or track time for testing.[^ayo-131]
- **Log every shakedown.** With dynos rare, riders lean on CAN traces, GPS runs, and disciplined cooling upgrades instead of optimistic app readouts when validating power claims.[^log-every-run]
- **Trust alloy handlebars over bargain carbon.** Track telemetry showed cheap carbon bars flexing heavily at speed and failing without warning; stick with quality alloy cockpits even if they add grams.[^3]
- **Skip bargain steering dampers.** Cheap motorcycle-style dampers have introduced dead zones and wobble; veterans revert to wide bars or invest roughly $400 in quality units, and still rate Nami and LongThunder chassis as the stiffest high-power frames.[^dampers-budget]
- **Match shunt mods to motor capability.** PuneDir’s shunt-heavy square-wave ESC already saturates a 1 kW motor.
  - traces and FETs have blown before
  - and the “fix” of staying above 50 km/h just hides the real problem, so current limits still need to match motor size instead of what the modded board can momentarily supply.[^4]
- **Upgrade undersized hubs before raising current limits.** Matthew’s Yume Y11 motor cooked itself at only 16 S and 180 A battery/phase while his Lonnyo hub shrugged off 300 A, underscoring that small OEM cans become the weak link once torque targets rise.[^y11-motor-limit]
- **Shitsky 75350 proves budget headroom.** A 20 S 13 P LG M58T pack pushed a Shitsky 75350 to ~32 kW (500 A phase / 235 A battery) while holding sag near 7 V and returning 57 Wh/km.
  - evidence that solid busbars and careful wiring let the controller survive real superbike duty.[^5]
- **Ignore the “V2” hype:** The rumored Makerbase 75100 V2 is just the aluminum-PCB refresh with the same stray solder, inaccurate shunts, missing key-switch support, and weak documentation, so plan upgrades instead of waiting on a non-existent redesign.[^makerbase_v2]
- **Plan for physical fit.** Makerbase 75200 V2 measures roughly 130 × 68 × 28 mm versus 103 × 58 × 19 mm for 75100 V2, letting all three units squeeze into Navee N65 decks once you trim fins and keep VESC undervoltage above the BMS trip point.[^6]
- **Treat 6-FET Ubox minis as 250 A-class hardware.** Shlomozero’s replacement 6-FET board exploded at roughly 280 A phase / 550 A absolute with 60 A of field weakening, so compact stages still demand conservative current and FW targets.[^ubox-6fet-failure]
- **Carry proven backups for commuters.** When that 6-FET died, Shlomozero dropped in a spare Vsett controller to keep his NIU rolling—daily riders should stage drop-in replacements before a controller failure strands their only transport.[^backup-controller]
- **Log packaging for heavyweight frames.** LiquorHole’s 21 kW Yisuntrek R8 plan now defaults to 6 AWG cabling, QS8 V2 connectors for 10–15 s bursts, actively cooled Spintend 85250 controllers in the stem, and Lonnyo 70 H 33×2 motors because the 150 mm dropouts will not swallow 75 H axles.[^yisuntrek-packaging]
- **Account for sustained fade on 75××× hardware.** Shlomozero’s MakerBase 75200 started tapering after extended 250 A phase / 150 A battery pulls even with MOSFET telemetry stuck near 100–110 °C, so treat those numbers as the practical ceiling for long climbs rather than chasing the firmware cutoff.[^makerbase-75200-fade]
- **Expect airflow mods on 84 V Makerbase boxes.** Sideways heatsink screws choke convection on the 84 V “84200HP/84100HP” line, so owners plan thermal pads, custom housings, or deck cut-outs before pushing current.[^7]
- **Spec connectors to match battery current.** Daily riders keep XT90s around 100–110 A battery and step to dual XT90s or QS8s once Spintend-class controllers pull harder.
  - document those breakpoints so parallel-pack builds stop melting undersized plugs.[^8]
- **Balance airflow with sealing on under-slung ESCs.** Ausias’ bottom-mounted Kelly controller clogged with dust even without sand exposure; he is switching to a ventilated yet splash-resistant 3D-printed shroud, underscoring that deck-bottom installs need filtered airflow rather than wide-open vents or fully sealed boxes.[^9]
- **Favor aluminum bases when you can.** Open-air 75100 aluminum plates stayed cool through 30 minute 45 km/h rides at 11 °C while boxed controllers thermal-throttled around 35 A.
  - tie airflow and heatsinking directly into the enclosure choice.[^10]
- **Keep phase extensions short and anchored.** Three-metre test leads on a Flipsky rig whipped violently once current ramped, reminding builders that long, unsupported phase runs experience Lorentz forces capable of ripping looms apart under load.[^11]
- PuneDir’s single-motor G30 test still logged ~4.2 kW while a Makerbase 75100 sat near 44 °C inside the stock controller can.
  - evidence that OEM housings can work as heatsinks when airflow is limited.[^12]
- Cross-check VESC telemetry against smart-BMS logs before celebrating current numbers; a MakerX build set to 70 A battery read ~10 A lower on the ANT BMS until owners reconciled pack-side data.[^telemetry_crosscheck]
- **Treat ad-hoc dual-motor add-ons skeptically.** Veterans found “bolt-on” second motors with their own controller and pack crowd the deck, delete the rear brake, overheat uncooled controllers, and deliver little efficiency.
  - serious AWD builds demand matched motors, dual controllers, and real cooling from the outset.[^13]
- **Source hubs with the frame in mind.** Lonnyo and NAMI hubs even share factory engravings; racers grab 70 H magnet stacks to stay within 150 mm dropouts and brace Laotie TI30 tubes with fresh welds and CAD references before chasing 11 kW+ launches.[^14]
  - 3Shul’s 70H hubs ship with fixed rims for standard 11″ tires while 75H hubs need separate rims; both accept ~350 A phase but the high-torque wind prefers shorter bursts.[^shul_variants]
- **Pick drivetrains that match copper fill.** Kaabo’s 60 H / 33×3 stators ship with thicker phase leads and shrug off >200 A, while stock Nami hubs overheat once you push past ~200 A unless you upsize cabling—budget swaps accordingly when planning 300 A builds.[^kaabo-vs-nami]
- **Kaabo/Weped hub genealogy matters.** Wolf Warrior hubs come from the same supplier as Rion/Weped units.
  - the 1 200 W trims carry 60 mm magnets while the GT’s 2 000 W set stretches to 65 mm with 33/43 Kv windings
  - so expect to shunt Minimotors controllers past 50 A or swap to higher-phase VESC hardware to unlock the extra copper.[^15]
- **“Six-phase” marketing is mostly doubled wiring.** The touted multi-phase hubs are typically standard three-phase motors with parallel windings; the real gain is reduced voltage drop and inductance, so set expectations accordingly.[^16]
- **Respect Laotie shock geometry.** The rear linkage only clears ≈130 mm eye-to-eye dampers.
  - dropping in 150 mm coils over-extends the swingarm and binds the suspension, so relocate mounts or stick with stock length when upgrading shocks.[^17]
- **Audit boutique chassis claims.** Face de Pin Sucé tore down legacy Rion frames and found cracked steering heads, flexing plates, under-specced Kelly controllers, and fan ducts blasting straight into walls—reinforce or replace the platform before leaning on 40 kW figures.[^rion-inspection]
- **Inspect new-production LY rims.** Off-centre drilling, missing bead seats, and inverted bolt patterns on current tubeless runs force brake-rotor removal just to pull wheels and introduce vibration at speed; plan rework or alternative rims for race duty.[^ly-rim-qc]
- **Victor vs. Vsett hub traits.** Dualtron Victor’s 45 H wind favours higher ERPM while Vsett 10 hubs deliver more torque.
  - pair the motor to your gearing and controller (e.g., MakerBase 75200 on 72 V packs) before chasing 100 km/h benchmarks.[^18]
- **Boutique ceilings:** Tronic X12 (24 S), Ubox 240, and Spintend 85250 builds all share MOSFET and shunt limits around 331 A; most racers cap hubs near 150–200 A battery and 310–360 A phase even after swapping to upgraded silicon.[^33]
- **Hall sensors are now stock on Dualtron Storm/X2 frames.** Current production runs ship with hall-equipped hubs, so VESC conversions can skip aftermarket sensor retrofits and jump straight to tuning once the harness is verified.[^19]
- **Pick Ubox over Flipsky for 14 S torque pulls.** Denis’ workshop rated Spintend’s Ubox ahead of Flipsky thanks to beefier MOSFETs and cooling; early Ubox units benefit from thicker thermal pads, and 14 S packs built on Samsung 30Q/40T cells can sustain ≈70 A battery draw as long as you respect the motor’s thermal limits.[^denis-ubox]
- **Mind 22 S on Makerbase 85/250s:** Multiple racers have already popped Ubox 85/250 controllers on 22 S packs even with regen disabled, whereas C350 hardware survives full race weekends so long as regen stays off; CL350s run hotter and now circulate official firmware links community members had to dig up themselves.[^makerbase_22s_fail][^cl350_drive_links]
- **Expect DOA CAN rails on Tronic 250 batches.** Several fresh units have arrived with dead CAN buses; the stopgap is to feed both controllers the same throttle signal while leaving the second ESC’s 3.3 V rail disconnected so you do not fry the accelerator while waiting for warranty replacements.[^tronic_can_doas]
- **Inspect Ubox V2 sensorless inputs.** Outdoor-mounted dual Ubox builds that suddenly lose sensorless detection have traced the failure to a cracked A6 diode feeding the EG3112 gate driver; replacing or bridging the diode restored detection and highlighted mediocre stock soldering on that rail.[^ubox_a6_diode]
- **FarDriver ND72450 field report.** A dual ND72450 Roadrunner running half of its battery capability still delivers 450 A phase, 32 kW peaks, working field-weakening, and cool motors—performance the builder preferred over comparable Tronic stacks.[^fardriver_nd72450]
- **Log field-weakening runaways.** A 75100 stayed spinning after throttle close when FW was active, underscoring the need to capture and report reproducible regressions to Vedder instead of assuming configuration error.[^fw_runaway]
- **Size Ninebot/GT2 packs for the current you want.** 26 S 8 P P42A builds feeding Tronic X12s already fight thermal issues until dual Uboxes are clamped to aluminum and wheel diameter/kv are tuned for the higher pack voltage.[^gt2_pack]
- **Validate MXlemming thermal gains.** Aluminum PCBs kept a 3.2 kW setup near 29 °C, and MXlemming tuning on 30 S gear cut controller temps from 80 °C to ~60 °C at ~150 A, though some racers bailed because the algorithm trimmed top speed on high-power hubs.[^mxlemming_thermal]
- **Keep Kaabo Thunder 2 controllers matched.** Mixing the 45 A front and 60 A rear boards leaves the scooter voltage-limited on top speed and saps launch thrust; either shunt the 45 A unit to match or source a twin 60 A module before raising current limits.[^21]
- **Burn E2 hub swaps need rotor spacers.** Fry the Guy’s conversion showed Kaabo 2 kW hubs clear the Burn E2 caliper only after adding rotor spacing, and ZAITUO 100/65-6.5 tires drop straight into the chassis.
  - add the note to fitment guides so builders order spacers and tires with the hubs.[^22]
- **Asymmetrical tunes need telemetry.** Smart Repair’s GT builds send ~420 A phase to the rear and 120 A to the front to balance launch traction.
  - replicate the setup only if you log per-wheel current so traction control and ABS ceilings stay predictable.[^23]
- **Log proven Spintend envelopes.** Matthew’s 18 S Spintend 85150 stopped cooking once he capped the tune near 220 A phase, 90 A battery, and ~60 A of field weakening.
  - use those numbers as a thermal sanity check before chasing 240 A+ experiments.[^24]
- **85240/85250 guardrails.** Matthew steers newcomers toward Spintend’s 85250/85150 controllers, while Yamal caps dual 85240 builds near 300 A phase per motor and the factory guidance stays around 240–250 A battery on 85240/85250 stacks.
  - treat those numbers as daily envelopes instead of spec-sheet fantasies.[^25]
- **Flash no-limit firmware before stress tests.** Rogerio’s friend cooked a stock-firmware 85250 at only 180 A phase / 80 A battery with regen disabled; the crew now flashes the hardware-unlocked build and keeps battery around 150 A with 250 A phase while cleaning debris from the enclosure.[^26][^27]
- **Treat 22/3 Lonnyo hubs as 250–300 A hardware.** Shlomozero’s 75 H 22/3 hit ~80 °C within minutes at 400 A phase, and Paolo reminded everyone the wind uses fewer parallel strands than 33/2, so hold hill climbs nearer 250–300 A unless you like burned stators.[^28][^29]
- **MakerX G300 saturation ceiling.** 🇪🇸AYO#74 and Face de Pin Sucé logged repeated heat soak and saturation above ~320 A phase on 22 S packs, forcing racers back to C350 hardware when they want the full 400 A envelope.
  - set expectations accordingly and budget C350 swaps for 22 S sprint builds.[^30]
- **Schedule post-impact tear-downs.** 🇪🇸AYO#74’s 22 S 70 H rear hub and Fry the Guy’s front Shul both logged current cuts and “voltage imbalance” faults after pothole strikes; inspect magnets, hall boards, and harness strain before the next sprint instead of blaming firmware quirks.[^pothole-teardown]
- **Overbuild stem hardware on heavy commuters.** LiquorHole’s 220 lb Yisuntrek stayed upright when the frame folded because he had already added a second stem bolt; replacing the chassis still cost about $1.3 k and 10 days, so reinforce steering assemblies before chasing 20 kW launches.[^yisuntrek-stem]
- **Single-motor Daly builds need accurate sensing.** Arnau’s 20 S 6 P P45B commuter pairs a Ubox 240 at 200 A phase / 100 A battery and keeps FET temps around 36 °C after swapping the thermistor pull-up to 100 kΩ.
  - proof Daly-managed singles survive when sensing is calibrated and currents stay sane.[^31]
- **Wolf King GT packaging reality.** Mattia’s sleeper build already runs dual 85240s, a 54 Ah Molicel P42A pack, and 6 AWG phase leads but still can’t fit a 75 H hub up front without machining the 140 mm dropout.
  - plan hub swaps around chassis clearance, not just controller headroom.[^32][^33]
- **RM-Light benchmark.** Face de Pin Suce’s 37 kg RM-Light pairs a C350 drivetrain, 22 S 4 P tabless pack, and RM-X 2024 rear motor to reach ≈25 kW and 130–140 km/h.
  - use it as a reality check for ultralight race targets.[^34]
- **Spanish Thunder current envelope.** Local race teams push 22 S 11 P P45B packs around 100/75 A battery and 250/220 A phase on G300 controllers for 140 km/h runs.
  - size wiring, cooling, and BMS hardware accordingly before copying the tune.[^35]
- **Dual-stack telemetry planning.** Yamal is targeting 150–175 A battery and 250–300 A phase per controller on a dual-drive G2 Max and flagged that VESC Tool aggregates CAN stats.
  - log per-controller telemetry before pushing 250 A per wheel.[^36][^37]
- **G300 toggles need firmware tweaks.** The controller ships with a momentary power input; change App → General shutdown settings so a quick button press truly latches the ESC instead of leaving it permanently live when the battery is connected, and treat six red LED blinks as a low-voltage warning until MakerX patches the auto-off fault.[^38][^39][^40]
- **Respect Spintend 85/150 voltage headroom:** The light 85/150 ships with 100 V-rated components and proven logs only on 20 S packs.
  - stacking high-kV hubs, MTPA, and FW near its ceiling has already popped stages, so plan drop-in HY/Huayi MOSFET swaps or step up to 3Shul/Tronic hardware for sustained spikes.[^spintend-85150]
- **Spintend 85/150 reliability watch.** One mislabeled “100 A” unit blew three input capacitors mid-ride and melted the CAN harness that backfeeds 12 V from the partner controller; pursue an RMA and audit CAN wiring before tying controllers together.[^spintend_85150_rma]
- **Overvolting 75 V hardware needs extra capacitance.** Paolo’s FlipSky clone failures and Ubox warnings show 17 S pushes demand more input capacitance plus lower charge targets (~4.1 V/cell) to keep regen spikes from nuking the sparse 220 µF bank.
  - most veterans stop at 16 S unless they retrofit the front end.[^41][^42]
- **Plan for BMS fault behaviour.** MKSESC 84/200 HP controllers have been blowing MOSFETs the moment a pack BMS opens under load, while Spintend Ubox and 3Shul hardware typically coast through the interruption; riders now favour Ubox 85/150 over Makerbase 84/200 HP despite the price gap, and CL350-class controllers ride out brief supply drops more gracefully when you add extra 12 V capacitance at the input.[^43]
- **Respect Spintend 85/150 voltage headroom:** The light 85/150 ships with 100 V-rated components and proven logs only on 20 S packs.
  - stacking high-kV hubs, MTPA, and FW near its ceiling has already popped stages, Paolo has already sacrificed a unit doing exactly that, and racers eye Huayi-sourced MOSFET swaps when they refuse to jump platforms.[^spintend-85150]
- **Treat miracle-spec MOSFET datasheets skeptically.** JJMicro-branded devices measured wildly off their published Rds(on) claims, so Paolo and other builders now trust Huayi-sourced silicon when assembling boutique controllers instead of gambling on unverified parts.[^44]
- **35 kW-on-10" dreams still need water cooling.** Riders concluded you only reach those peaks with water-cooled ~45 kV hubs, reduced PWM frequency, and premium cells such as Molicel P50B/EVE 40PL.
  - traction becomes the limiting factor long before spec sheets do.[^45]
- **Document catastrophic harness failures.** A dual-pack moped shorted a QS8 and vaporised the Ignite logic stack at first throttle despite balanced phases.
  - inspect every high-current lead after pack work and add redundant insulation/strain relief before sign-off.[^46][^47]
- **Map 20–22 S packaging before chasing 130 km/h.** Denis’ workshop shows 50–60 mm Blade/Vsett motors paired with 15–22 S packs and 300 A VESC installs; expect 22 S to boost acceleration more than top speed, while 20 S remains the practical daily setup once you account for mounting space and weatherproofing requirements.[^48]
- **Marketing vs. reality:** Expect Makerbase boxed 75100 units to deliver only one-half to one-third of the configured current, while Flipsky 75350 shunt math caps phase current near 500 A despite brochure claims.[^4][^5]
- **Kaabo pack sag is real:** Wolf-class 16 S5 P packs still droop ≈15 V when dual Uboxes surge to 150 A despite 60 A limits, underscoring the need for chemistry upgrades (P42A/P45B/50S) and thicker connectors when chasing sustained output.[^kaabo-sag]
- **Budget controller picks:** Seasoned builders steer dual-motor projects toward Spintend duals or Makerbase 75200s and warn that Flipsky 75100s overheat or blow 12 V rails when 75 V field weakening and BMS cutoffs collide.
  - invest in robust packs and extra capacitance if you insist on the cheaper hardware.[^49]
- **Budget packs still cap speed.** Dual 84100HP controllers on a 14 S 4 P Samsung 50E pack plateaued around 56 km/h even with 120 A phase limits, pointing to battery sag rather than controller ceilings when commuters chase higher top speed.[^50][^51]
- **12-FET ceilings:** Makerbase’s 12-FET controllers stay reliable around 180 A phase (200 A only in cold weather), while Spintend’s 12-FET Ubox units sustain 250–300 A when cooled.
  - ignore the 700 A MOSFET headline unless you’re paralleling phases.[^52]
- **Spintend minis top out near 135 A phase.** Community logs peg the Lite controllers around 135 A out of the box; stretching them to 180–200 A plus field weakening has already cracked hardware, so budget cable upgrades or larger controllers for sustained experiments.[^53]
- **Motor KV still sets the ceiling.** Low-Kv hubs have failed to reach the advertised 250 A phase on single Ubox 85/150 installs, underscoring that electrical limits hit before the controller does on torque-wound motors.[^54]
- **Cooling is the limiting factor on dual X12s.** Yamal’s X12 still feeds only 100 A battery while commanding 250 A per motor, highlighting how quickly dual setups overwhelm cooling if enclosures aren’t upgraded.[^55]
- **FarDriver still feels oversized on scooters.** Paolo keeps avoiding Fardriver controllers even when oversizing looks safe, preferring VESC-class hardware for compact chassis.[^56]
- **Watch for dead-short phase stacks.** MKS 84100HP failures have torched XT60s instantly; a blown MOSFET bank leaves one phase at roughly 0 Ω, and builders now source replacement MOSFETs from distributors like LCSC to dodge counterfeits.[^57]
- **Stock gate drivers are fragile:** Makerbase 75100 boards ship with EG Micro EG3112 drivers.
  - carry exact-pinout spares, budget MOSFET replacements such as NCEP023N10 or Infineon IPP023N10N05 from authorised distributors, and recalc gate resistors/snubbers before swapping silicon to avoid another failure.[^58]
- **Bring unknown boards up on bench supplies first.** Makerbase MKS 84 HP controllers that trip on 13 S packs still power on at 36 V; veterans now energise new hardware on 30–50 mA current-limited bench supplies to catch shorts or firmware faults before a full battery turns a mistake into blown MOSFETs.[^59]
- **Buffer the logic rails:** Flipsky driver stacks lack solid undervoltage lockout on the 12 V rail; add bulk capacitance or a small buffer pack so BMS hard cuts don’t leave MOSFETs biased and short the rail.[^60]
- **Audit workmanship before blaming silicon.** Smart Repair keeps finding “mystery” deaths tied to loose bullets, scuffed insulation, or unstable observers.
  - rebuild harnesses and confirm detection results before condemning the controller.[^61]
- **DIY alternatives:** Ennoid MK8 shares the Spintend footprint but still needs Infineon IPTC017N12NM6 or similar MOSFET upgrades before flirting with 26 S / 500 A goals.
  - plan the reflow work if you want to stretch beyond stock specs.[^39]
- **Budget standby draw:** Flipsky 75100 owners who skip antisparks still unplug XT90S leads between rides or accept the ~5 mA idle draw when storing high-voltage scooters for weeks; document storage procedures accordingly.[^62]
- **Ubox 100/100 Lite ceiling.** Finn proved the Lite can deliver roughly 170 A phase / 90 A battery after flashing Vedder’s no-hardware-limit 6.05 firmware, while most riders hover around 130 A without those changes.
  - Noname logged ~6–7 kW before deciding a larger controller would be safer.[^63]
- **Skip MK8 Pro for big scooters.** Undersized stock capacitors make MK8 Pro boards risky above commuter power unless you redesign wiring and packs to tame transients.
  - most racers look elsewhere for 200 A+ duty.[^64]
- **New open-source experiments:** The freshly published six-MOSFET “Baguette ESC” offers a lightweight starting point for contributors who want to prototype compact controllers, albeit without real-world validation yet.[^65]
- **Match controller to hub mass.** Heavy QS 12–13" hubs have cooked the sparse bulk-cap banks on Spintend 85× hardware; Smart Repair now nudges those builds toward “fat VESC” or FarDriver-class controllers unless the boards get capacitor and sensing upgrades first.[^66]
- **TOLT telemetry proves the headroom but not invincibility.** Rob Ver’s dual Ubox builds running Toll-package FETs are already logging ≈210 A battery and 310 A phase without drama, yet the crew is treating 250 A/400 A experiments as destructive testing that may overwhelm 12-FET hardware if cooling and wiring aren’t perfect.
  - document heat soak and connector temps before copying the trials.[^67]
- **Six-FET ceiling awareness:** Little FOCer and Tronic 250 controllers remain happiest around 100 A battery, 250 A phase (≈300 A absolute) with ≤45 A of field weakening.
  - earlier burnouts linked back to over-current hits, water ingress, and fresh reports of random boot failures on compact boards that pushed G30 builders toward MP2, Spintend, or the incoming CL350 refresh.[^lfocer_limits][^alu-75100-phase][^lfocer-random]
- **Voltage headroom pays off.** The same Little FOCer drivetrain dropped 0–50 km/h times from 3.7 s on 16 S (≈166 A battery peak) to 3.2 s on 20 S (≈258 A) simply by raising pack voltage, underscoring how extra series cells slash launch times without touching phase current.[^68]
- **Traction control still taxes launches.** Back-to-back logs on 16 S and 20 S builds showed traction control delaying full battery current until roughly 35 km/h, adding ~0.8 s to 0–50 km/h sprints and running controllers hotter; disabling TC and managing a touch of slip restored 2.8–3.2 s launches.[^69]
- **Watch 3Shul packaging revisions.** Rage Mechanics’ next CL350 run swaps to low-profile bus capacitors and dual power plugs to squeeze into 100 × 120 × 25 mm cavities that keep killing Little FOCer and Tronic boards.
  - plan mounting around the flatter layout if you are packaging dual drives in Xiaomi tubs.[^70]
- **Deck-mounted Little FOCers demand heat sinking.** Jan’s dual Little FOCer build only held 21.8 kW peaks once both controllers were bolted to deck plates; the same session highlighted delays in Tronic deliveries and ongoing efforts to pair open-source dashboards with VESC hardware.[^71]
- **Serviceable sensor boards.** 3Shul race scooters that lost their NTC powerboards have been revived by swapping in the latest replacement modules, and builders report the new production run looks cleaner.
  - proof the platform remains repairable even when auxiliary boards fail.[^72]
- **C350 V4 hardware shift.** Face de Pin Sucé reports the refreshed C350 moved to low-side shunts and 12 FET packs that tolerate roughly 500 A absolute / 400 A phase, explaining why labels still cite 200 A battery while seasoned tuners lean on the higher phase ceiling.[^73][^74]
- **Flipsky 75100 “Pro” changes.** The latest aluminum-case refresh arrives with AWG10 leads, onboard Bluetooth, and cleaned thermistor routing yet still omits a dedicated enable pin.
  - budget an external ignition even on the upgraded hardware.[^75]
- **When 75100s keep popping FETs, inspect the gate-drive stage.** Repeat transistor failures.
  - even at idle
  - have traced back to damaged gate drivers and op-amps; replace or probe the driver chain before installing another MOSFET set.[^76]
- **Stock Vsett 10+ controllers cap at 16 S.** The factory FETs and bulk caps are only rated to ~85 V; running 20 S or aggressive regen has already blown stages, so steer riders toward VESC swaps instead of parts-bin voltage mods.[^77]
- **Kelly torque limits:** Kelly 7212 stacks built around 12 × 5.5 mΩ FETs run out of punch above ~120 A battery, whereas 7230 drivetrains paired with Makerbase 75200 controllers have logged bursts near 592 A phase / 225 A battery.
  - numbers 75100 hardware cannot sustain.[^78][^79]
- **60/18 Zero 10X upgrade paths.** Dual Ubox stacks still spike near 250 A battery while the single 80 V aluminum board runs cooler; 3Shul C350/C350s remain the premium alternative when you need higher sustained current without water cooling.[^80][^81]
- **Source 3Shul motors with hall support.** Rage Mechanics and Face de Pin Sucé are bundling TTY hall repairs and EU distribution.
  - keep sensors bonded inside the stator slots and confirm who handles replacements before placing race orders.[^82][^83]
- **Makerbase 75100 high-voltage caution:** A 16 S-stable aluminum-PCB unit shorted instantly when first throttled on 22 S, leaving both motors resistive.
  - treat higher pack voltage as a hardware change, not just a tune tweak.[^84]
- **No-limit firmware is still experimental.** Jake’s custom binaries calm noise-induced stutter on Flipsky/Makerbase 75200 hardware at high duty, but testers are keeping launches below ≈80 % duty and logging temps until an official fix ships.[^85]
- **BMS limits surface before controller specs.** Dual Makerbase 75200 boards spiking to ~452 A phase / 150 A battery tripped the ANT BMS at 2.9 V per cell, locked both motors, and cracked a MOSFET.
  - proof that 7 P packs and small hubs cannot sustain 330 A+ launches without voltage headroom.[^86]
- **Ubox v2 still tops out around 150 A phase.** Rage Mechanics and community testers reiterate that 50–60 A battery / ≈150 A phase per motor is the practical ceiling; anyone chasing 150 A battery and 350 A phase per wheel needs C350-class or Kelly hardware instead of overdriving Uboxes.[^87]
- **Firmware 6.0/6.2 adds heavy-load stutter.** High-current hubs that run smoothly on FW 5.3 start chugging on 6.0/6.2 with identical parameters, pointing to observer changes.
  - either stay on 5.3 or be ready to reduce phase limits until VESC Tool stabilises.[^88]
- **Scrutinise refreshed 84100 HP samples.** The latest Makerbase 84100 HP batches arrive with isolated hardware, copper shunts, glued logic stacks, and 8 AWG pigtails, yet riders still flag the cramped front-end sampling layout as a thermal and packaging risk.
  - treat the upgrades as incremental rather than a licence to raise current ceilings blindly.[^89]
- **Cap Makerbase 84100 battery amps conservatively.** Veterans now hold them near 60–80 A battery and ≈135 A phase after watching one burn at 160 A; PuneDir was told to move to 85/250-class hardware for real 120 A battery service.[^90]
- **Audit 75100 shunts before trusting telemetry.** NetworkDir’s teardown proved the stock 75100 current sense network reads wildly low; he published 5 mΩ shunt firmware to regain accuracy and warned that the factory parts look tuned to clamp phase current rather than report honestly.[^91]
- **Protect fragile 3.3 V rails.** A Bluetooth daughterboard brushing the aluminum lid killed a 75100’s logic rail even though the power stage survived, and another commuter board died outright after ~2,000 km at only 10 A.
  - evidence that “gentle” duty cycles still brick Makerbase singles without insulation upgrades.[^92]
- **Keep Makerbase 84100 at ≤20 S.** Riders probing 23 S packs on the 84100 platform were told to stay at or below 20 S unless they accept elevated failure risk.
  - the hardware still isn’t rated for sustained 100 V service despite the marketing.[^93]
- **Budget dual-controller path:** When money is tight, run two Makerbase 75100 Alu boards on CAN instead of gambling on bargain dual ESCs.
  - one throttle feeds both controllers and the pair has survived daily 22 S commuting once current limits are kept realistic.[^dual-75100-can]
- **Leave throttles on the master when you mirror CAN.** Dual-motor builders keep only one throttle wired to the master (`ADC+UART`) and cap the front controller near the battery limit to tame slip; true independent throttles mean breaking CAN and duplicating accessories, so plan extra harnessing before ditching mirroring.[^94]
- **Spintend supply shift:** The 85/250 run is over—stock spares or pivot to 85/240/Seven-class hardware now that Spintend routes 240 A controllers through New Jersey with minimal tariffs.[^41]
- **Unlock warranty firmware on Ubox 85/150.** New units ship capped near 130 A phase / 180 A absolute until you flash the 100/250 profile, so budget the firmware swap before tuning high-power builds.[^95]
- **Traction control scope:** Enable traction control on the local/master controller in a CAN pair; 🇪🇸AYO#74’s 22 S build only needed TC on the front node to stop wheelspin, but he and Yamal disable it after runs because the algorithm shaves a few kilowatts off top-speed pulls.[^96]
- **Spintend supply shift:** The 85/250 run is over.
  - stock spares or pivot to 85/240/Seven-class hardware now that Spintend routes 240 A controllers through New Jersey with minimal tariffs; riders chasing more headroom are already moving to X12 or Seven stacks instead of hunting scarce inventory.[^97][^41]
- **Keep 85/250 current realistic.** Community consensus holds Spintend 85/250 builds near 200 A battery / 300 A phase unless you upgrade MOSFETs and cooling.
  - Yamal flatly calls 350 A “not safe,” and riders chasing bigger numbers are shopping Seven or X12 hardware.[^98]
- **Budget for DOA 85/250 units.** Multiple 85 V 250 A boards have arrived dead or died within weeks at 200 A motor / 170 A battery, pushing riders toward Seven or 3Shul replacements even before the line’s discontinuation; Smart Repair confirmed production has stopped, so treat surviving units as short-term hardware.[^99][^100]
- **Hack your own logic boards.** Community repair leads like Hackintosh are buying failed 85240/85250 brains to keep fleets alive, underscoring that regional service still hinges on DIY swaps rather than factory RMAs.[^101]
- **Document recovery workflows.** Builders still struggle to resurrect bricked 85150s even with spare hardware, signalling a need for well-documented laptop/ST-Link alternatives before field failures strand high-power scooters.[^102]
- **3Shull repair network is growing.** C350 stacks keep running 400 A phase / 200 A battery at 22 S when installed carefully, and Figiwara has already revived multiple failed boards.
  - record regional contacts before shipping hardware overseas.[^103]
- **Seven vs. Fardriver packaging.** Seven controllers continue to earn praise for robust signal connectors, whereas Fardrivers remain niche picks when you have room for their much larger enclosures.[^104]
- **Recent sprint benchmarks:** Dual Ubox 85250 riders chasing 0–100 km/h in 6–6.5 s lean on 20 S10 P Samsung 40T packs with 0.2 mm copper busbars, while Yamal’s day-to-day dual 12-FET tune holds roughly 28–30 kW.
  - use those logs to sanity-check acceleration promises and thermal budgets before marketing bigger numbers.[^105][^106]
- **Reality check on 40 kW boasts:** Tronic inrunner hype still hinges on marketing.
  - Dimos’ 70 mph near-cutout traced back to sloppy solder joints, and Ninebot G30 builds chasing 40 kW only log ~8.9 kW without bypassing safety hardware. Treat 10 kW/60 mph as the current bar and demand real logs before promising more.[^107]
- **Phase-current guardrails:** Daily riders still cap single Spintend 100/100 controllers around 130 A phase and stock 85150 hardware around 220 A phase unless silicon and cooling are upgraded; pushing harder without hardware changes keeps popping MOSFETs.[^108]
- **Skip over-volting Flipsky boards:** Veterans call 22 S experiments on Flipsky hardware “crazy” because the predictable result is controller carnage.
  - treat voltage jumps as a hardware swap requirement, not a firmware tweak.[^109]
- **100/100 attrition warning:** Four Spintend 100/100 controllers have failed within a year despite 20 S packs capped near 60 A battery and 130 A phase; veterans are swapping to other hardware instead of gambling on replacements.[^110]
- **Secondary market pulse:** Slack Core 920R dual 75 H Numo motors with factory 10 k NTC sensors and tubeless rims sold instantly for €500, signalling demand for logged, drop-in upgrades when vetted hardware appears.[^111]
- **Sizing heuristics:** Artem’s quick-start math keeps launches safe.
  - begin with phase amps around motor wattage ÷ 10, set battery amps to ≈67 % of phase, and trim battery current again whenever you raise phase limits for extra punch.[^artem-sizing]
- **Compact singles:** Spintend’s upcoming single-channel controller mirrors dual-Ubox silicon but needs active cooling above roughly 30–50 A; budget a fan for ≈100 A service in the XT90-sized case once production lands around $150.[^spintend-single]
- **G300 sprint controllers:** Waterproofed 18-FET G300 builds are logging ≈250 A battery / 500 A phase bursts on 22 S, but riders still report heat soak if they hammer regen.
  - treat them as sprint hardware rather than hill-climb replacements.[^40]
- **FarDriver mega-controllers:** Nanjiang units rated 160 kW advertise ~1 200 A battery and 2 400 A phase, but community consensus is that scooters rarely need more than ~200 A phase.
  - these controllers suit dirt bikes and conversions that can house the battery volume and cooling those numbers demand.[^112]
- Haku remains wary of bargain FarDriver 450 A controllers, warning their current ceiling can cook standard scooter hubs.
  - treat those boxes as experimental unless you’ve proven the motor’s thermal headroom.[^113]
- **BAC lock-in vs. VESC/Nuc flexibility:** ASI BAC 4000-class controllers deliver power but keep firmware and motor provisioning locked behind resellers, void warranties on unapproved hubs, and leave riders chasing paperwork-friendly “police modes”.
  - pains that continue to push scooter builders toward Spintend or Nucular ecosystems.[^114]
- **Open-source options:** MP2/CCC_ESC remains a 30 S-capable DIY path when you can populate through-hole MOSFETs, machine heatsinks, and flash ready firmware sourced from the community.[^6]
- **Carbon experiments have trade-offs.** Collaborations with Formula 1 composites engineers on carbon-fibre G30 fenders and aluminium heat-spreader spacers look promising, but veterans warn that brittle carbon mudguards can shatter and lock wheels under torsion.
  - plan validation before daily use.[^115]
- **“1000 A” wishlists remain theoretical.** Riders daydreaming about 3Shul “1000” stacks or FarDriver ND722600/842600 stages acknowledge that China-only availability, questionable software support, and steep pricing keep these mega-controllers aspirational compared with proven 1 800 A-phase Vesco builds.[^116]
- **Open-source options:** MP2/CCC_ESC remains a 30 S-capable DIY path when you can populate through-hole MOSFETs, machine heatsinks, and flash ready firmware sourced from the community.
  - Jason is now targeting a 30 S 4 P Molicel 50S pack to sustain 600 A phase bursts once his 18 FET TOLL-stage experiments behave.[^117][^6]
- **Plan MP2 stack height.** The controller core sits roughly 22–23 mm tall and you can drop the capacitor “pills” lower by removing pin headers (sacrificing USB access), leaving room for 30 S ambitions inside 10" decks when packaging is modelled early.[^118]
- **Import-constrained markets:** High-end track scooters entering Israel must ship as parts with local battery assembly unless a licensed importer handles the whole vehicle.
  - budget extra for customs and in-country pack work.[^119]
- **Singapore clampdown:** FalconPEV and Carbonrevo still sell parts, but licensing caps and even storefront photography bans highlight how hard it has become to buy or register high-power scooters locally compared with neighbouring markets that only check for plates.
  - plan offshore builds when necessary.[^120]
- **Spain’s certification window:** DGT-approved scooters such as the Mantis King GT and Dualtron Victor will retain street legality after January 2027, while Sur-Ron-style e-motos already require motorcycle registration and Fiido-style seated scooters still lack a registration path.
  - choose frames with compliance paperwork if you plan to ride there long-term.[^121]
- **Kukirin G4 build reality:** The roomy frame invites upgrades, but dual LY 70 H hubs plus a 20 S 8 P Samsung 50S pack still lean on a Ubox 85150 that caps output below the battery’s 360 A peak, and customers have already seen the stock motor hit 90 km/h at 8 kW while running “oven” temperatures.
  - plan hub upgrades alongside controller swaps.[^122][^123]
- **Kukirin G2 Master reality:** Treat the stock 52 V (14 S) battery as disposable if you want serious acceleration.
  - Max Rainlogix and others jump to 60 V (16 S) packs built on Samsung 50E/50S or EVE 40PL cells by trusted builders such as @jamessoderstrom or @Mirono_escooters, and even “budget” dual mini Ubox stacks still cost €100–120 per controller once shipping lands.[^124]
- **Chassis headroom check:** Pumping 15 kW through the G2 frame triggered wobble complaints even with dampers, so high-spend riders are nudged toward Ninebot G30 platforms with speed forks instead of over-investing in the Kukirin shell.[^125]
- **Highway lane discipline:** Above roughly 65 km/h the crew treats lane changes as a last resort and even removes helmet-mounted GoPros that tug in crosswinds, preferring smooth weight transfer over abrupt steering inputs to keep long-wheelbase scooters stable.[^126]
- **Teverun upgrade reality:** Riders squeezing LY 75 H hubs into Teverun frames widen swingarms, plan titanium steering columns, and run 20 S 84 V P45B packs clamped to ~350 A.
  - even on Daly hardware
  - while peers draft 22 S 11 P P45B layouts rated near 495 A for future controller swaps.[^127]
- **Wolf Warrior X pack reality:** The stock 1.2 kWh module uses respectable cells for its class but still sags under sustained 4.4 kW draws.
  - Purp and Cihan recommend budgeting a custom pack when buying used units so performance-per-dollar keeps pace with controller upgrades.[^128]
- **Single-motor torque ceiling:** Jan’s 12 kW rear-motor project still tried to loop out from a standstill and stalled near 62 km/h without field weakening; chasing 100 km/h on a 20 S single demands 16×4–22×3 hubs plus complex switching, so veterans steer high-power riders toward dual Vsett 10+ drivetrains instead.[^129]
- **Segway GT2 telemetry:** Jerome’s GT2 logs kept dual Spintend 85150s at 60 A battery / 150 A phase with 30 A FW on a 19 S 9 P EVE 50E pack.
  - cells were the bottleneck, and Patrick recommends setting BMS thermal cutoffs around 75 °C (80 °C max) while trusting quality ESCs to ride through the trip.[^130]
- **Geometry still caps real speed.** Zero 10X and Dualtron frames flirting with 100 km/h lack motorcycle-grade rake/trail; veterans now pair any triple-digit tune with aggressive braking upgrades and geometry inspections before chasing GPS records.[^131]
- **High-speed chassis reality:** Denis’ crew rates Vsett 10+ (with upgrades) and Segway GT2-class frames far sturdier than Dualtrons once speeds climb toward 70 km/h; Dualtrons kept failing in sealing, wobble, and suspension despite their price, so there’s no cheap path to a reliable 60–70 km/h scooter.[^132]
- **22 kW dual-drive baseline:** Yamal’s 22 S setup runs dual controllers at roughly 130 A battery / 200 A phase each (≈21–22 kW total), Thunder 3 projects target similar figures with 20 S9 P Samsung 50S packs and dual VESC 85150s, and Fardriver-powered 22 S9 P Samsung 50S builds have already logged ~140 km/h.
  - use these logs to sanity-check phase and battery goals before you chase bigger numbers.[^133][^134]
- **G30 race-proof:** Jan’s enclosed dual Spintend 85/250 G30 clears ~21 kW and 136 km/h on a 20 S 6 P P42A pack with a 550 A BMS while staying inside the frame; swapping to Samsung 40PL cells would raise theoretical pack ceiling toward 26–34 kW if the wiring and controllers can absorb 200–250 A battery draw.[^135][^136]
- **Race aero wall:** Face de Pin Sucé’s 20 S 8 P 40T race setups still stall near 147 km/h (~25 kW) because 11″ scooter frames hit aero and resonance limits.
  - pushing toward 200 km/h would need 40 kW+ plus heavy chassis work.[^137]
- **Extreme-range experiments:** Jan’s next commuter test pivots to a 19 S 6 P low-Kv 65 H single-motor G30 targeting roughly 200 km of range without deck spacers.
  - a reminder to consider energy density once top-speed goals are met.[^138]
- **Wind selection heuristics:** NetworkDir reminds builders that 22×3 winds trade top speed for easier torque and efficiency while 33×2 variants demand huge phase current for burnouts.
  - pick motors that match voltage goals instead of banking on field weakening to fix everything.[^139]
- **Match winding to current budget.** Victor swaps showed 16×4 torque hubs sip current where 22×3 speed stators demand far more amps and aggressive temperature monitoring to hold 2–3× nominal power; hall sensors smooth sine starts, but sensorless launches remain viable if you tolerate kick starts or brief BLDC phases.[^140][^141]
- **Use field weakening sparingly.** Community debate reaffirmed that FW trades away torque you could reclaim with higher-KV hubs; riders still lean on it for low-voltage (≈13 S) builds where buying new packs/controllers isn’t practical, so log temps and amps before banking on FW for top speed gains.[^142]
- **Respect short-wheelbase limits.** Compact 20 S 2 P commuters can still launch at ~75 A phase (~3 kW), but riders report needing to lean forward during 100 A spikes to avoid looping out; range hovers near 20 km from 41–81 V until larger 20 S 7 P packs and improved waterproofing fit the same deck.[^143]
- **Plan traction aids for 22×3 race hubs.** Yamal’s logs show dual 22×3 Lonnyo motors break traction around 200 A per wheel without traction control, while 33×2 stators soak highway speeds but require flawless tuning and budget-stretching phase current.
  - factor those behaviours into motor buys before selling proven hardware.[^144]
- **Mini-moto donor option:** Off-the-shelf 48 V/1.5 kW pit bikes now ship with small, parameter-editable Fardriver controllers, giving builders a ready-made 72 V-capable platform without replacing electronics on day one.[^145]
- **Flipsky 75xxx triage:** Bench tests continue to pop DC-link caps on 74 V Flipsky builds.
  - swap in Nichicon replacements, bump the ADC low end to ~0.2 V to calm throttle chatter, relocate capacitors with pigtails when the aluminum shell blocks clearance, and don’t hesitate to pivot to Spintend 85150/85250 controllers (often via @jamessoderstrom) when QC woes drag on; fresh 75200 V2 hardware still blew immediately on first plug-in despite improved detection routines.[^146][^147]
- **Flipsky 75xxx triage:** Bench tests continue to pop DC-link caps on 74 V Flipsky builds.
  - swap in Nichicon replacements, bump the ADC low end to ~0.2 V to calm throttle chatter, relocate capacitors with pigtails when the aluminum shell blocks clearance, and don’t hesitate to pivot to Spintend 85150/85250 controllers (often via @jamessoderstrom) when QC woes drag on.[^146]
- **Flipsky 84-series limits:** Max Rainlogix pegs 84100 controllers around 60 A battery continuous (≈100-series), while 84200 hardware survives near 150 A before FET reliability nosedives.
  - treat higher targets as a sign you need Spintend 85-series or better controllers.[^148]
- **60 V bargain boxes have hard ceilings.** Pandalgns warns Laotie/J&P square-wave controllers tap out around 19 S.
  - pushing to 20 S “go boom”
  - so budget Damao-branded 72 V units instead of gambling on stock electronics for cheap 20 S support.[^149]
- **Turnkey QS drivetrain:** Builders unwilling to rewind hubs can grab 72 V, 15 kW QS-motor scooters straight off AliExpress.
  - Pandalgns surfaced a listing that bundles the whole drivetrain for drop-in projects.[^150]
- **Motor/power pairing:** Samsung 29E commuter cells fall flat beyond ~80–90 A even in 11 P, so racers swap to P42A or VTC6A chemistry to keep 130 km/h pulls viable.[^7]
- **Nucular trade-offs:** A single controller cannot run two motors.
  - budget dual 6F/12F stacks plus the CAN display, expect months-long (sometimes year-long) backorders while the Russian team relocates, and factor in optional potting, uLight modules, and the promised CAN-integrated BMS if you want a cohesive ecosystem; the refreshed 24F case now measures roughly 196 × 86 × 35 mm with 12F/6F redesigns on deck and a SmartDisplay beta that bridges VESC, Kelly, Sabvoton, and Zero harnesses above €300 once production scales.[^151][^152][^153]
- **Kelly vs. Sabvoton reliability:** Kelly 7212/7218 hardware still draws random-death complaints despite waterproof housings, while Sabvoton kits rated 95 V include TVS protection that leaves regen headroom on 18 S commuters charged below 75 V; expect sparse app telemetry.
  - Sabvoton’s phone app still omits live current
  - and budget staged programming plus BLE adapters to keep high-KV hubs from tripping red-light faults.[^154][^155]
- **Treat Kelly 7212 specs realistically.** Riders log 220 A battery bursts on 20 S and praise the launch feel, yet the controller remains a ~50 A continuous unit without added airflow.
  - budget shunt mods or step up to the 7218 when you need sustained power.[^156]
- **Kelly 7230 copper sleds:** Custom TIG frames hiding 20 S10 P Samsung 40T packs (~40 Ah, ≈350 A discharge) feeding dual Kelly 7230s highlight how compact Sabvoton swaps free volume.
  - plan harness strain relief and compare controller volume before promising similar builds.[^157]
- **Retail support gaps persist.** Riders continue to report €300 Sabvotons arriving dead with no vendor help while VESC alternatives spun their motors within minutes.
  - document fault-finding and plan to self-support controllers purchased from distant resellers.[^158]
- **Premium motor envelope:** Rage Mechanics’ 75 mm stator hubs run well over 10 kW per wheel on Weped platforms but cost ~€650 each and demand wide dropouts.
  - budget axle-width checks before planning 120 km/h builds around them.[^159][^160]
- **Extreme-speed builds demand heavy hardware:** Face de Pin Sucé’s platform already touched 134 km/h on 15 S with dual Uboxes and is stepping to 20–21 S packs plus 75 mm hubs and 21 S 11 P Molicel bricks to chase 140 km/h goals.
  - plan for multi-kilogram motors (~6.5 kg bare) and oversized harnesses before emulating the setup.[^161][^162][^163]
- **Field-weakening ROI:** Expect diminishing returns—adding 25 A of FW only moved a 20×70 kV setup from 66 km/h to ~84 km/h freewheel, topping out around 96 km/h at the hardware cap.[^34]
- **Hub wind selection:** Community logs keep 60 H 22/3 stators as the default street wind, Nami’s 17/4 motors as the torque pick just under 100 km/h, and 33/2 rewinds for high-speed circuits; stretching to 65 H 33/2 hardware demands ≥12‑FET controllers, bespoke harnesses, and 8 mm² phase leads, while Rosheee’s dyno pulls showed a single 65 H hub on a 16 s 6 p pack beating paired 50 H hubs 0–30 km/h at the cost of top speed and fast energy drain.[^hub_winds]
- **Match windings per axle:** Mirono and Gabe cautioned that pairing dissimilar stators (22×3 rear with 33×2 front, 75 H with 50 H) invites detection issues and uneven torque.
  - stick with matched Kv sets when configuring dual-drive builds.[^mixed_windings]
- **Synchronise control loops on mixed hardware.** NetworkDir reminded riders blending Zero and Mantis drivetrains to match PWM frequency (≈30–35 kHz) and observer choice across controllers so traction control and thermal behaviour stay predictable when hubs come from different generations.[^164]
- **Controller derating reality:** Tronic 250 riders now target ≈200 A rear / 180 A front with moderate field-weakening after thermal cutouts at 230 A, Rochee’s retune proved that lowering phase amps cures grinding when heavy FW stacks on high duty, and Jesús’s 24 S Rion still skids the front wheel near 120 km/h.
  - traction and realistic phase ceilings matter more than brochure numbers.[^tronic_real]
- **Max Rainlogix baseline:** His Thunder build (dual Lonnyo 70/110 hubs, Ubox 85/240) hauled two riders up a bridge at 320 A battery while staying 23–28 °C thanks to 150/200 A rear and 120/140 A front phase limits plus traction control.
  - use it as proof that tuning beats brute force.[^165]
- **Race voltage consensus:** French race teams continue to cap builds at 22 S because today’s 30 S hardware cannot feed the same battery amps without losing punch.[^race_22s]
- **Scarce premium options:** Nucular’s 24F remains alluring yet heavy, four-figure expensive, and harder to source than a 3Shul C700, making the latter the pragmatic upgrade path in 2024.[^nucular_scarce]
- **Dual-case controllers:** “Dual ESC” housings genuinely contain two linked boards on one heatsink, making them viable for dual 500 W Monorim builds so long as each channel stays within spec.[^dual_case]
- **Non-VESC fallback:** Fardriver controllers now anchor budget high-current projects with 2,600 A-class offerings, and Weped’s Sonic.
  - freshly sighted in Portugal
  - is expected to ship with Fardriver FOC hardware while VESC remains the premium but fragile option at those current levels.[^166][^fardriver_alt]
- **Frame selection heuristics:** Ninebot G30 rental frames still take the abuse of 20 S builds, Vsett G2 decks fit fewer cells, and SNSC donors are the bargain tanks.
  - Mi 3/Mi 4 decks stay stock-friendly only and fight heavy mods.[^167]
- Builders now blacklist RX7/Onvo-style frames that crack after wheelies and abuse.
  - if you plan high-power tunes, start with sturdier bike frames instead of patching flimsy scooter welds.[^168]
- Rental-derived stems with IoT cutouts (SNSC, Marti, Xiaomi G30) keep failing at the opening; scrap welded repairs, collar the pole with external aluminum, and wear moto-grade gear because 60–75 km/h breakages are catastrophic.[^169]
- **Start from proven frames.** Ninebot G30 chassis offer better routing and sealing than Kugoo-class frames, which demand extensive reinforcement before surviving VESC conversions.[^170]
- **Welding and chassis reality checks:** PuneDir’s “PuneRon” hybrid (a Hyosung RX125 frame headed for QS138 power) still goes to a professional welder after practice passes.
  - heavy conversions demand proper jigs, upgraded brakes, and motor-mount fabrication before anyone should ride them on public roads.[^171]
- **Know when to outsource deck work.** Aluminum aftermarket decks need skilled TIG welders, intermittent cooling, and proper PPE; many builders drill new bolt patterns, verify alloys, or hand the job to fabrication shops rather than risking weak welds on load-bearing scooter frames.[^172]
- **Clean corroded hubs mechanically.** Riders salvaging motors prefer drill-mounted wire brushes over chemical baths so rust comes off without leaving residue inside the hub.[^173]
- **Machining for oversize hubs:** Even premium forks need lathe time.
  - Simone had to machine mixed Nami/Rion fork legs to clear 70 H hubs and 3 mm rotors, so budget machining and fit checks whenever you push beyond stock stator widths or rotor thicknesses.[^174]
- **Log halo swingarm spacing.** The crew is cataloging 155–200 mm swingarm and fork options that swallow Lonnyo 80 H hubs.
  - archive those dimensions with your build sheets so machining plans start from known clearances.[^175]
- **Reinforce Kaabo necks:** Her0DasH keeps finding flex and glued charge-port plates on Mantis necks.
  - add through-bolts, mind latch orientation, and secure charge ports before unleashing 20 S torque.[^176]
- **Race teams embrace bespoke drivetrains:** Face de Pin Sucé’s 2024 race scooter pairs 22 S 11 P packs, a C350 controller, Hope Tech 4 V4 brakes, and in-house rewound motors, underscoring how pro crews now lean on custom drivetrains rather than off-the-shelf hubs at the front of the grid.[^177]
- **Swedish “hyper” benchmark:** A 22×3 wind project with 700 mm bars, steering damper, and @jamessoderstrom coaching already clocked 117 km/h on a Rage Mechanics G30.
  - proof that stems and dampers must scale with triple-digit ambitions.[^178]
- **RM-Light sprint context:** Rage Mechanics’ RM-Light (Dualtron Compact frame, 22 S 4 P pack, C350 RM-X rear, Beringer brakes, titanium pole) hits ~140 km/h but only lasts 17 minutes on track.
  - treat it as a sprint build, not a street tune.[^179]
- **Hackintosh/Arnau benchmarks:** Expect ~127 km/h and 26.5 kW from Hackintosh’s latest scooter and 23 S 13 P (~60 Ah) LG M50/M58 packs on Arnau’s commuter builds.
  - use them as reference points when sizing 96 V-class projects.[^180]
- **Rob Ver’s Spintend data:** 22 S builds on 85/240 controllers are touching 35 kW and 132 km/h with ~80 A FW, but repeated MOSFET failures after BMS trips show how essential pack protection and tire discipline are during 320 A launches.[^181]
- **Nami daily ceiling.** Yamal still caps his dual Nami stack around 175 A battery / 300 A phase per controller after past failures.
  - treat those numbers as the reliable baseline before chasing higher logs.[^182]
- **Smart Repair traction notes:** One GT1 build now runs 420 A phase rear / 120 A front with 85 A battery caps because the front tire still spins at 80 km/h.
  - traction, not controller headroom, sets the ceiling.[^183]
- **Plan suspension for 70 H front hubs.** Smart Repair’s 26 S dual-drive still needs widened front suspension to accept a 70 H motor.
  - budget chassis work before committing to 12" front upgrades.[^184]
- **Document Victor-to-Thunder deck swaps.** Matching bolt patterns, swapping swingarms for Lonnyo 70 H hubs, and rerouting shortened phase leads are mandatory before the deck transplant feels OEM.
  - capture measurements before cutting loom length.[^185]
- **Document NIU dual-hub conversions.** One German build grafted a Soflow front motor, rewound the rear to delta, and ran 18 S 7 P packs with 95 A/40 A (front) and 140 A/70 A (rear) tunes for ~90 km/h.
  - but repeated 90→0 km/h stops overheat 120 mm rotors without regen support.[^186]
- **Mind EU legal ceilings.** Spain’s 2027 homologation list keeps Thunder 3 legal while Nami likely won’t be; anything above 4 kW still counts as a motorcycle across much of the EU, so plan registration and stealth profiles accordingly.[^187]

## 2. Harness & Wiring Hardening

- Upsize Laotie-derived harnesses.
  - the stock loom still overheats at race current while QS273 hubs ship with ≈7 AWG phase leads, so budget thicker cabling before raising phase amps.[^188]
- Replace stock loom jackets with TPU spiral wrap or PET braid once the harness is exposed—both stayed flexible after 18 months outdoors.[^8]
- **Respect wiring ampacity.** Even 8 AWG harnesses start to warm near 150 A continuous, and 2.5 mm² motor leads inside Blade/VSETT hubs melted after repeated 110–155 A pulls until they were upsized to 4–6 mm² conductors through the axle.[^ampacity_warning]
- **Mounting dictates continuous current.** Riders cap boxed 75100s around 40–50 A battery when they’re bolted to scooter frames; they only stretch toward ~70 A once the controller is clamped to a solid aluminum block and every capacitor is mechanically staked to survive vibration.[^189]
- **Stake capacitors and insulate legs.** Reglue every loose bus cap, keep bench tests within the documented 4–20 S window, and insulate MOSFET legs plus hot spots with fishpaper before reassembly.
  - aluminum-PCB repairs have died instantly when metal shavings bridged phases or when techs hot-plugged packs without precharge tools.[^190]
- **Flash ESP32 telemetry bridges with a scripted workflow.** rESCue proxies and a simple USB-to-UART map let builders flash bare ESP32s for BLE/CAN bridges without paying for Makerbase modules.
  - budget 5 V bench power and proper RX/TX crossover instead of gambling on Arduino IDE uploads.[^191]
- **Upsize phase leads with flat conductors, not bulk silicone.** Blade and VSETT hubs already squeeze 3×4 mm² through axles; veterans strip outer jackets, stagger splices, add spacers, or press axles a few millimetres instead of drilling housings or stuffing thick silicone that robs clearance.[^phase_routing]
- Re-terminate budget-controller switch leads with ring lugs, add strain relief on throttle grounds, and minimize inline connectors to prevent runaway events from broken returns.[^9]
- Keep a rounded-fastener rescue kit.
  - Dremel cutoff wheels for slotting, oversized flat-head/“Thor head” drivers, and a heat source
  - so Thunder/Victor hardware swaps don’t stall when phase-lead reroutes shorten your wrench reach.[^192]
- **Upgrade consumables.** Big-box GB zip ties are cracking in cold weather.
  - switch to industrial nylon or imported bundles when dressing harnesses for winter use.[^193]
- **Log halo swingarm spacing.** Lonnyo 80 H hubs need 155–200 mm between dropouts plus shim packs to center rotors.
  - measure before machining frames or ordering custom spacers.[^175]
- Schedule deliberate reassembly time.
  - one rushed teardown twisted a 12 V accessory lead, killed the VESC, and left the rider pushing an 8 km commute, so strain-relief checks go on the pre-ride list.[^194]
- Favor waterproof signal/phase connectors like Julet, L1019, or HiGo (≤100 A phase); budget extra for hall/thermistor additions that feed VESC telemetry directly.[^10]
- Treat XT90 as a temporary lead above 150 A phase.
  - dual Spintend logs show 500 A bursts cooking XT90 solder joints, so crews now standardise on XT150 or Amass AS150U anti-spark plugs with 8 AWG pigtails and silicone charge leads to keep smart-BMS shunts honest.[^195]
- Inspect anti-spark connectors periodically.
  - Noname’s XT90S precharge strip started heating and discolouring after repeated plugs, so replace fatigued housings before they melt under high-current launches.[^196]
- Sync controller power buttons or add isolation relays—waking one Ubox in a 4WD stack while the other stays off has already blown CAN transceivers via reverse-polarity paths.[^can-sync]
- Upgrade abrasion points: sleeving PTFE leads before pulling 6 mm² conductors through axles prevents insulation tears, and RX/Nami riders now jump to AWG 11 silicone (AWG 10 rarely fits) to keep hubs cool on summer climbs.[^35]
- Step up motor leads where heat persists.
  - silicone-insulated 6 mm² (≈10 AWG) phase wires survive hub temps better than PVC, and Higo L1019 harnesses bundle three ~11 AWG phases plus seven signals in a 7.7 mm jacket; stock VSETT 9 cabling measures only ~2.5 mm² (≈13 AWG), so monitor MT60/XT150 connectors for heat when pushing past ~90 A phase and retire the L1019 once you step up to 60–70 mm motors that no longer accept the jacket cleanly.[^197][^198]
- Avoid aggressive axle drilling unless you can deburr perfectly.
  - jumping from 8.5 mm to 10 mm bores for 6 mm² leads makes silicone jackets vulnerable, so taper the exit, reinforce externally, and stop if suppliers call the mod unsafe.[^199]
- Consolidate dual-phase spaghetti harnesses into single 8–10 AWG runs terminated near the motor.
  - each extra soldered split or XT150 adds resistive loss and becomes a failure point once currents crest 200 A.[^wiring-bundle]
- Retire solder-only XT90 jumpers on dual-controller decks.
  - burnt connectors traced to rigid bus bars, and riders incinerated XT90S plugs when feeding >2,000 µF banks at 16 S+; migrate to QS8/AS150U/QS8H hardware with shielded CAT6A control looms to survive 200 A+ pulls.[^200][^201]
- Reflow XT150s tight against the cup walls and trim excess lead length; sloppy soldering has shown 53 mΩ phase resistance where healthy HM/Blade/Rion hubs sit near 132 mΩ, 85 mΩ, and 50 mΩ respectively.
  - numbers that flag heat issues before motors cook.[^202]

## 3. Battery & BMS Strategy

- **Pack chemistry:** Document any stock packs using LG M50LT or Samsung 29E cells and plan rebuilds when aiming for >120 A discharge; monitor internal resistance deltas and pause parallelization above ~3 mΩ spread.[^11]
- **Treat BMS trips as emergencies:** MKSESC 84/200 HP units have blown MOSFETs whenever a BMS opened under load, whereas Spintend controllers coast through the same event.
  - oversize protection and design tunes so the BMS never has to intervene mid-ride.[^makervsUbox][^bms-trip]
- **Derate XT90 connectors on 100 A builds.** Stock XT90s plateau around 45 A continuous; riders chasing 100 A peaks now jump to QS8, dual XT90s, or AS150/6 mm bullets and upsize cabling so connectors stop being the bottleneck.[^203]
- **Match BMS to charging goals:** 20 S6 P Zero 10X builders default to ANT or JBD smart boards when they need 40 A charging with unrestricted discharge; cheaper Dollatek 20 S options hover near 40 A continuous and run marginal for 60 A pack targets.[^204]
- **Adjust regen ceilings at the BMS first:** Matthew’s 18 S Spintend 85/150 quit regen above ~76.6 V until he raised the BMS cutoff start/end, proving the controller was fine and the BMS voltage limit was the bottleneck.[^205]
- **Regen boundaries:** Cap regen between –5 A and –12 A on 60 V 38 Ah commuter packs until BMS specs are confirmed; firmware ERPM caps can still drop braking, so validate on firmware ≥6.05 beta (build 20).[^12][^13]
- **Log bus voltage during high-speed regen.** Crews chasing 80–100 km/h field-weakening runs record pack voltage during braking to prove Spintend hardware survives the back-EMF spikes instead of assuming it is safe.[^206]
- **Parallel pack discipline:** Match pack voltage before plugging in, skip ideal-diode fantasies, and use solid XT90/Y harnesses on common-port BMS designs.
  - mixed 17 S/16 S experiments triggered throttle cut-outs until riders paralleled only voltage-matched packs, trimmed regen to controller limits, left charge MOSFETs enabled, and even let multiple chargers share the load because each supply naturally tapers in CV mode as voltages equalise.[^207][^36]
- **Thermal guardrails:** Rental-grade SNSC hubs pushed to 20 S 40 A hit ~160 °C without ferrofluid—daily riders should cap voltage at 13–16 S or add cooling mods.[^14]
- **BMS vetting:** JK smart BMS units continue to outclass ANT variants for connectivity.
  - the new compact boards ship tidy copper bus rods, dual temp probes, 1 A or 2 A active-balancing variants, and optional OLEDs; wake them by applying 5–7 V above pack voltage (or plugging in the display) before configuring pack parameters, pop the lid to pluck stray solder beads, and source through official channels to ensure RS485/CAN and heater-pad support.[^208][^15]
- **Retire weak BMS hardware:** Daly smart boards that refuse to balance below 4.18 V/cell or advertise 35 A hardware still struggle at 50 A continuous.
  - builders replacing them with ANT or JK units report fewer shutdowns and healthier pack temps.[^209]
- **Avoid chemistry mixes inside parallels.** Pairing MJ1 and MH1 cells accelerated sag once discharge topped ~8 A per cell; keep parallels chemistry-matched when chasing 130 A pack output.[^210]
- **Respect charge limits.** Sony VTC6A 7P groups accept about 63 A before heat soars, Samsung 40T owners target ~0.5 C (~35 A per cell pair), and Molicel P45B claims still lack third-party curves.
  - stay near 30 A bulk charge unless you have lab-grade cooling and instrumentation.[^211]
- **Mega-pack reality:** Sustaining 800 A continuous output demands at least 32 P li-ion groups or high-current LiFePO₄ bricks (~60 Ah, 200 A each), plus serious cooling and volume planning.
  - far beyond typical scooter battery envelopes.[^212]
- **Samsung 48X field data:** Fresh 20 S9 P packs held cell delta to 0.002 V after 5-mile runs, sagged only 4–7 V at 110–135 A, and let VSETT motors sustain 10 kW/64 mph while keeping windings near 65 °C.
  - evidence that top-tier cells unlock reliable 10 kW commuting.[^213]
- **Connector selection matters.** QS8 anti-spark plugs now ship with 6 AWG-ready cups, making them a better fit for 60 A+/135 A dual-controller builds than AS150 connectors that choke at ~8 AWG.
  - retrofit both battery and controller leads before raising current limits despite the ~21.50 CHF per-pair cost in the EU.[^214][^215]
- **Upsize again for race builds.** High-current scooters are already stepping from QS8 to QS10 or QS12 hardware for 110–200 A+ battery pulls, stuffing dual 12 AWG or 6 AWG leads per shell while retiring XT30/XT90 plugs that overheat or melt on 10 kW setups.[^216][^217]
- **Audit Sur-Ron packs for real busbars.** Vendors are still shipping €2 500 “12 kW” batteries built on pure nickel, so experienced buyers crack cases or demand photos before purchase and budget copper or isolation upgrades if they spot thin strip work.[^218]
- **Respect thermal trips.** Daly-class BMS boards that spike past their limits raise cell resistance; veterans now log monthly IR checks and back off charge currents once a pack trips to avoid long-term damage.[^219]
- **One overcharge is too many.** A 13 S pack pushed to 60 V (~4.61 V/cell) lost most of its cycle life (~250 cycles) and flirted with venting.
  - set conservative charge cutoffs and audit charger calibration regularly.[^220]
- **Pack-based regen math:** Artem keeps battery regen at or below the pack’s amp-hour rating (10 Ah pack ⇒ ≤10 A regen) and programs controller regen ≈15 A higher so any overshoot dumps as heat instead of spiking cells or tripping BMS charge FETs.[^221]
- **Baseline braking:** Dual-motor builders start near −30 A battery/−80 A phase on the rear and −25 A/−55 A on the front for confident stopping without tripping controllers.
  - treat these as ceiling values before tuning higher.[^regen-baseline]
- **Parallel pack discipline:** Match voltages and skip ideal diodes.
  - mixed 17 S/16 S experiments induced throttle cut-outs until builders simply paralleled packs, budgeted regen against controller limits, and kept charge MOSFETs enabled for braking.[^36]
- **Don’t bypass BMS hardware:** Parallel Xiaomi packs without active BMS boards drifted into 0 V cells despite manual balancing.
  - leave supervisory boards in circuit or expect pack death within months.[^bms-bypass]
- **Thermal guardrails:** Rental-grade SNSC hubs pushed to 20 S 40 A hit ~160 °C without ferrofluid—daily riders should cap voltage at 13–16 S or add cooling mods.[^14]
- **BMS vetting:** JK smart BMS units continue to outclass ANT variants for connectivity; confirm RS485/CAN and heater-pad support with official distributors before ordering.[^15]
- **Daly behaviour:** Display models ignore remote shut-off commands, latch MOSFETs open after hard sag, and can flick charge FETs during strong regen.
  - keep antisparks as safety backups and budget time to reset via the Bluetooth app if they trip mid-ride.[^daly-behaviour]

## 4. Instrumentation & Thermal Management

- Single-motor 65 H Lonnyo builds that flutter past 35 mph benefited from deleting throttle smoothing, reviewing VESC logs, and swapping to Ortega’s foc observer when mxlemming struggled; plan to raise limits toward 150 A only after the BMS and wiring catch up, remembering 22×3 winds trade launch torque for top speed versus 16×4 options and that premium halls plus Statorade help the hub survive the extra amps.[^222][^223]
- Embed hall sensors and NTC thermistors into hubs for consistent launch torque and accurate thermal telemetry—Bluetooth probes in motor shells lag dangerously.[^16]
- **Fix halls instead of running sensorless.** Bypassing healthy hall sensors robs low-speed torque and smooth launches; repair the harness rather than forcing sensorless detection just to dodge soldering.[^224]
- **Log a baseline detection before first rides.** 🇪🇸AYO#74’s fresh 22 S 11 P P45B pack is still running sensorless until halls arrive; publishing the working detection template lets other builders bench-test commutation before rolling out new packs.[^225]
- **Charger audits matter.** The Celler-branded 20 S adjustable supply arrived accurate and sturdy (aside from an on/off fan), making it a vetted budget option once you confirm build quality and keep wall-plug-first sequencing to avoid XT arcing.[^226][^227]
- Wate/YZPower CC‑CV bricks remain the dependable budget pick; anonymous lab supplies can overvolt packs with a careless knob twist, so adjustable units demand disciplined trim checks plus BMS safeguards before field use.[^228]
- **Grease with caution.** Semi-fluid fills inside geared hubs slash cooldown time but double rolling resistance and can leak through rotor bolts.
  - log temperatures and trim fill levels after each ride.[^229]
- Remember stators can sit 100 °C hotter than hub shells for minutes; trust embedded sensors over external touch checks when chasing 20–33 kW race pulls.[^17]
- Treat SmartDisplay telemetry as complementary: it now ships with Kelly KLS profiles and OTA-updated police-mode shortcuts while Sabvoton/BAC support queues up; firmware flashes over HTTPS with encrypted images, but you still need VESC Tool logs for battery current and Voyage/Ambrosini dashboards when CAN aggregation hides which hub is fading.[^230][^18][^37]
- Front-mounted ducting keeps dual-motor 16 S7 P Samsung 50E packs alive around 140 A battery by holding phase current near 70 A per controller and dumping controller heat into the airstream instead of the sealed deck.[^vsett-airflow]
- Sealed Wolf Warrior decks trap heat.
  - dual Ubox installs hitting 120 A battery / 440 A phase saw MOSFET temps climb until riders logged runs and added ducted cooling or cut current.[^wolfwarrior-ducts]
- Export VESC Tool CSVs or bridge Android sessions to desktop after every tune change.
  - Android 11+ hides files under `Android/data/vedder.vesctool/files`, so plan a TCP bridge or capable file manager before sealing decks for weatherproofing.[^logging-workflow]
- Windows riders continue to flag VESC Tool 6.05 installers that refuse to launch while the same build runs on Ubuntu.
  - bundle dependency notes or workaround steps whenever you share the official binaries so troubleshooting doesn’t stall customer support.[^231][^232]
- When moving off the 6.05 beta, export your XML backups first, install the release build, flash matching firmware, and then restore the saved configs; Happy Giraffe’s workflow preserved throttle and limit settings without forcing a full retune.[^233]
- Compare GPS dashboards.
  - Relive routinely over-reports top speed by ~7 km/h when it loses lock, while Speed View GPS Pro offers floating overlays, exportable logs, and reliable range data once paired with Ubox telemetry.[^234][^235]
- Consider sealed-oil experiments cautiously.
  - roughly 40 ml of inert oil inside a hub dropped winding temps from ~120 °C to ~75 °C and sped cooldowns, but you still need intact seals and should set thermal rollback near 100 °C with a hard stop around 115 °C to protect magnets that hover near 80 °C.[^236]
- Respect insulation limits even with better cooling.
  - VSETT hubs rely on glass-fiber sleeves and PTFE inserts rated near 200 °C, yet commodity enamel softens around 120–155 °C and even premium windings short near 200 °C, so treat scorched coils as rewinds before they spike controllers.[^237]
- Dose ferrofluid conservatively: 6–6.5 ml of Statorade drops VSETT hub windings from ~145 °F to ~104 °F without drag, while larger 60 mm motors may need 7–8 ml.
  - overfill past ~8 ml and you add friction instead of cooling; bargain fluids can pass conductivity tests yet flash at low temperatures, so riders stick with €30 EU-sourced Statorade and cap magnet temps near 90 °C.[^238][^239]
- Embed epoxy-coated 100 k B3950 probes directly under the windings with silicone adhesive, route a single sensor lead through the axle alongside phase and hall conductors, and stick with Statorade-grade ferrofluid.
  - cheap educational mixes have lower flash points and unknown additives that compromise tests; VESCs accept either 10 k or 100 k NTC probes between TEMP and GND, with 100 k parts offering finer resolution.[^240][^241]
- Schedule ferrofluid top-offs during maintenance.
  - community consensus keeps fills between 4–8 ml per hub (≈6 ml on VSETT motors) and calls for resealing covers while tracking how much fluid remains before refilling.[^242]
- Inject ferrofluid through existing ventilation screws or dedicated ports so you avoid disturbing hall boards, then reseal the covers immediately.
  - open vents will sling fluid during high-speed runs.[^243]
- Bolt-on hubsinks with thermal paste and custom PVC/acrylic ducting redirect airflow past the motor while freeing deck space for taller packs.
  - key for sustaining 70–75 km/h cruises without cooking magnets.[^244]
- Bolt controllers flat to aluminium decks with fresh thermal paste.
  - remote radiator boxes or thick spacers added heat and resistance, while Weped-mounted dual Uboxes still brushed 80 °C at ~500 A phase until clamped directly to the chassis; riders favour paste over pads whenever the ESC clamps to metal to maximise contact.[^245][^246]
- Vsett riders swapping out stock square-wave ESCs for dual Uboxes reached the same conclusion.
  - scrape paint, repaste the heatsink blocks, and bolt the controllers straight to the deck even if it means pulling the battery to reach the mounts.[^247]
- Vent holes buy only a little time: 75 A battery / 190 A phase tunes crept toward thermal cutback until builders resurfaced the deck interface and reran tests with paste, proving direct deck contact beats airflow tweaks for sustained hill pulls.[^248]
- Regen torture tests on 10 S 2 P P42A packs have spiked to 2.55 kW and heated motors plus MOSFETs quickly—log stator temps anytime you raise negative current limits.[^regen-heat]
- Wepoor burnouts keep smoking front-end stages when ANT BMS charge thresholds are too aggressive; cap regen near 120 A, leave charge FETs enabled, separate discharge/short limits, and raise charge trip points so the controller never sees an “uncaptured” regen event that opens the circuit mid-slide.[^249]
- Haku’s latest failures still happened at conservative 200 A battery / 300 A phase settings after dead-stop launches; stretching positive ramp to 10 s just starved the controllers until the BMS tripped, so veterans now keep ramp times near zero and focus on supply integrity instead.[^250]
- A 750 W Boosted Rev hub on a single Ubox still hit 55 °C controller / 80 °C stator in eight minutes at 120 A phase / 80 A battery, and regen pulses add another ~5 °C.
  - treat thermal logs as mandatory when upsizing current on small motors.[^boosted-logs]
- Flipsky’s compact single overheated to ~60 °C MOSFET temps within 3 km at 50 A battery / 85 A phase, prompting veterans to increase heatsink pressure, reapply quality paste, and add 40 mm fans before chasing 100–120 A experiments.[^251]
- Treat SmartDisplay telemetry as complementary: it logs per-motor phase amps and traction events while VESC Tool mobile still requires manual battery-current logging, and Voyage/Ambrosini dashboards help separate per-controller data when CAN aggregation hides which hub is fading.[^18][^37]
- Export VESC Tool CSV or XLS logs after hill climbs to graph pack sag before retuning current limits; reviewing the traces beats guessing mid-ride.[^sag-logging]
- Enter the actual magnet count and compressed-on-tire diameter in VESC Tool; GPS traces lag too much for launch analysis compared with controller RPM telemetry.[^magnet-entry]

### New Fault Signatures & Repairs (2024 Telegram logs)

- **Fuse specs matter on Ubox repairs.** The ignite JST on Ubox V2 boards feeds through a slow-blow fuse near 125 V/≤1 A; matching that part after a connector repair restores normal boot behaviour.[^252]
- **Chasing phantom ABS trips?** Wiggle the hall loom.
  - several riders traced intermittent `ABS_OVER_CURRENT` faults to loose hall harness strands and cured the error by reseating or re-terminating the plug before touching firmware limits.[^253]
- **Moisture can spoof FET telemetry.** Ubox owners logging 190 °C “FET” temperatures under throttle found condensation on the PCB; warming and cleaning the board with isopropyl returned normal readings.[^254]
- **Verify NTC part numbers after swaps.** Mixed-controller builds misreported Lonnyo 70H stator temps until the owner confirmed the correct thermistor value.
  - double-check sensor specs before blaming firmware for nonsense data.[^255]
- **Hall failures still mimic ESC death.** Yoann’s dual Spintend setup only lost detection on one wheel; swapping controllers proved the hall sensors were the culprit, reinforcing the habit of bench-testing sensors before opening RMAs.[^256]

## 5. Firmware, Calibration & UX Safeguards

- Override desktop input wizard center-voltage prompts on one-direction throttles or finish calibration in the mobile app to prevent reversed brake/throttle mapping.[^19]
- Rehearse the seven golden commissioning rules.
  - wire everything before energising, pre-charge ≥20 S packs, discharge capacitors after unplugging, keep ADC inputs ≤3.3 V, avoid hot-plugging, eliminate ground loops, and re-check each step before troubleshooting
  - to stop repeatable VESC kill-shots.[^257]
- Re-run input + motor detection after changing traction control or ramp settings on CL350 hardware; writes occasionally drop, erasing throttle calibration.[^20]
- Slow ABS overcurrent can mask poor current tuning yet saves time when observers are unstable—disable only after fixing detection and ramp configuration.[^21]
- **Reflash stubborn reboot loops.** Patrick’s MakerBase rig kept tripping ABS at 225 A and rebooting mid-ride until the group raised the absolute limit and reflashed the same firmware over a clean template to clear suspected corrupted writes; treat unexplained resets as a cue to rewrite firmware before swapping hardware.[^258]
- Keep the absolute-current limit roughly 1.5× your phase ceiling once you raise battery amps; JPPL’s fix for Hugo’s throttle cutouts was simply lifting ABS to ~240 A so 100 A battery / 180 A phase tunes stop faulting.[^259]
- VESC Bridge V2 now promises plug-and-play harnesses for Segway GT1/GT2 and Ninebot G30/G2 plus OTA firmware, anti-theft modes, per-motor torque shifting, adjustable regen ceilings, and upcoming JK/JBD/ANT/Daly BMS support.
  - plan harness routing so the upgrade slots in once released.[^260]
- Treat PWM frequency as an efficiency knob: Smart Repair and ‘lekrsu’ run 30–33 kHz for smooth torque despite the loss in efficiency, while others drop frequency when they need peak range.
  - log heat and current draw before picking a value.[^261]
- Avoid triggering permanent BLE pairing (“pairing done”) unless you truly need it; clearing the lockout demands a VESC Tool update and manual flag reset.[^22]
- **Treat VESC Tool 6.05’s MP3 demo as a party trick.** Streaming audio through the motor with the bundled Lisp example shook frames and sounded terrible.
  - log it as novelty so riders don’t plan on it for daily use.[^262]
- **MakerBase X12 writes revert to 120 A.** Reading back a config forces VESC Tool to clamp phase/absolute limits to 120 A unless you follow the read→edit→write workflow, so treat every tune change as a two-step write and confirm the limits stick before closing the deck.[^263]
- **Document silent latch-offs.** Arnau’s Ubox 250 powered down at 60 V / 120 A while the status LED stayed green.
  - capture reset sequences for controllers that appear healthy yet stop driving motors so riders aren’t stranded mid-ride.[^264]
- **Watch traction-control heat soak.** Little FOCer traction control doubled controller temps during 10 kW pulls until riders disabled it, whereas C350 hardware survived the same loads.
  - proof the algorithm taxes smaller stages disproportionately.[^265]
- **Prefer front-only traction control.** Spintend duals survived slips better with front-wheel TC and lowered phase/battery limits; full dual traction combined with 250 A phase already torched one rear Tronic during a minor slide.[^266][^267]
- **Dualtron launches need halls or HFI.** Sensorless Dualtron fronts slammed the ABS ceiling at 100–120 A motor current and stuttered under 10 mph until riders added hall sensors or tuned HFI/VSS with proper pole counts and wheel diameters.[^268]
- **Document config persistence.** If regen or wattage caps reset to 500–700 W, suspect flash wear—back up configs, reflash, and validate limits on fresh hardware.[^param-reset]
- **Check scripts before blaming hardware.** Makerbase 75200 riders stuck at ~20 km/h ultimately traced the cap to missing Lisp dash scripts and overly aggressive 70 A field-weakening limits.
  - reinstall the script, tame FW, and confirm duty/ERPM caps before swapping controllers.[^269]
- **Calm Flipsky 75200 idle heating.** Disable the built-in phase filter, rerun detection with the `mxlemming` observer, and cap current near 120 A phase / 120 A motor / 50–60 A battery with about −5 A regen on 20 mΩ hubs; Jason also reminds testers to kill regen on bench supplies because FW-induced back-EMF has already destroyed lab PSUs.[^270]
- **Use the right detection templates.** Large outrunners often need the preset to match (e.g., Chen Simhony’s Inokim OX only passed detection after selecting “large outrunner”), and miswired CAN/hall/temperature looms keep throwing faults.
  - double-check wiring before blaming firmware.[^271]
- **Square-wave shunt mods still hit saturation.** PuneDir’s €25 ESC hit 260–280 A phase yet coughed through 25–50 km/h because the square-wave stage was saturating the hub; the crew advised detuning phase limits or moving to FOC hardware before the traces burn again.[^272]
- **Verify Rs/Ls externally when auto-detect lies.** Riders now measure resistance and inductance with standalone tools before typing values into VESC Tool after repeated Makerbase/Flipsky detection failures and random hard braking events.[^273]
- **Sensorless FOC still needs a shove.** Mirono confirmed VESCs will launch sensorless builds in FOC mode so long as you kick the wheel to seed detection; HFI experiments can remove the push, but most still prefer a rolling launch.[^274]
- **Remember “VESC amps” are optimistic.** Engineers keep warning that VESC Tool’s displayed “VESC amps” exceed instrumented phase current, so leave headroom instead of chasing the app’s highest number.[^275]
- **Makerbase 84100 needs real phase amps.** Paolo reminded riders chasing stock Mantis torque to raise the 84100 above its 90 A default.
  - target 150 A phase (with ~150 A absolute) or at least 120 A with the no-limits firmware so e-brake headroom and launch torque match OEM behaviour.[^276]
- When scripting 1WD/2WD toggles on Spintend bridges, isolate CAN or power between controllers.
  - otherwise the “sleeping” ESC keeps mirroring the active unit’s battery current and never actually idles.[^spintend_toggle]
- Disable traction control on ultra-high-power AWD tests unless you have confirmed hardware tolerance; Roscheeee snapped Tronic controllers when TC yanked rear-wheel power on slick concrete and dumped ~250 A back through the system.[^277]
- Run the `faults` command before power-cycling after an ABS trip and raise `ABS Max Current` above commanded phase current (200–250 A for 120–130 A tunes) so noise-induced spikes stop shutting hardware down mid-ride.[^fault-logging]
- Field-weakening remains gated to FW 5.3 binaries.
  - builders sideload the 300 A hardware-limit bin and experiment with duty triggers around 70 % to stretch past the 95–98 % ceiling without cooking hubs.[^278]
- **Match BMS hardware to the tune.** Even a 300 A ANT pack tripped short-circuit protection at 120 km/h when phase current hit ~690 A.
  - log peaks and extend delay timers or uprate protection before chasing higher slip thresholds.[^279][^280]
- Vedder Sensorless Start hides inside the sensorless encoder profile and expects temperature telemetry; without it, scooters fall back to noisy hall launches that stretch 0–30 km/h to ~5 s on hills.[^281]
- **Tame mid-speed rattles with LemmingMX templates.** TrentXWB stopped a commuter-speed vibration by flashing LemmingMX settings and capping a single-motor tune around 35 A battery / 90 A phase for ~44 km/h, avoiding field weakening entirely.
  - use it as the baseline before chasing exotic observers.[^282]
- **Avoid locked-wheel burnouts.** Haku’s one-second front burnout on a 33×2 high-kV setup stalled the motor, spiked current, and shorted two MOSFETs in the rear slave.
  - proof that locking a wheel can instantly kill aluminum-PCB VESCs even when the hub keeps spinning.[^283]
- **Triage blown stages methodically.** NetworkDir’s first checks after a failure are continuity across the QS8 battery plug and each phase-to-ground sweep.
  - any beep signals shorted FETs that must be replaced before reconnecting power.[^284]
- **Match silicon when repairing.** Veterans warned you cannot mix spare MOSFETs across boards; aluminum substrates demand proper reflow gear, and regen-only braking is reckless because hardware faults leave you without stopping power.[^285]
- Leave MTPA disabled on surface-mount hubs.
  - FW 5.3 keeps it off by default, preventing negative d-axis injection that can spike voltage if the current collapses during a fault.[^286]
- Keep logging PID tweaks: riders running the 1200 W wizard preset, 20 kHz switching, and aggressive PID gains clawed back launch torque while trimming ~100 A from full-throttle pulls.
  - proof that firmware discipline beats brute current.[^287][^288]
- Sensorless riders are leaning on HFI again: ensure ≥15 % Ld/Lq spread via `measure_ind`, then expect near-hall launch torque with only a faint startup whine once tuned.[^sensorless-hfi]
- Keep field-weakening on a throttle or speed trigger—firmware 5.3 beta adds ~8 km/h at ~20 A extra draw, but using it below cruise speeds cooks motors fast.[^fw-usage]

## 6. Fabrication & Assembly Discipline

- Budget soldering stations.
  - TS100/PTS200 pens, Ryobi 120 W cordless irons, or 80 W benches with digital readouts
  - cover most harness work without spending €600 on lab gear; reserve premium stations for production shops.[^289]
- When trimming frames, pick thin dedicated steel or aluminium discs and make multiple shallow passes; forcing thick multipurpose wheels stalls grinders and drains small batteries.[^290]
- Aluminium grinding throws neurotoxic dust—wear masks, clean up, and avoid eating until hands and faces are washed after fabrication sessions.[^291]
- Use molded cell holders or reinforced 3D-printed fixtures plus flexible adhesives (B7000/E8000) so parallel groups stay serviceable after cell failures.[^23]
- **Inspect boards for stray solder before closing the deck.** Dual Spintend units shorted phases instantly after loose solder balls bridged traces; Smart Repair now adds magnified inspections and alcohol rinses even on premium controllers before final assembly.[^292]
- 🇪🇸AYO#74 cautions against hot glue on hall elements.
  - it softens near 120 °C
  - so builders now favour high-temp silicone or epoxy, test each sensor before soldering, and keep spare 60° Wolf King GT hall boards on hand when converting sensorless hubs.[^293][^294]
- MP2 builders now solder copper busbars on the hotplate before mounting FETs and only terminate phase leads once the power stage is secured.
  - keep electrolytic capacitors off the plate so the ~200 °C soak doesn’t cook them.[^295]
- Proven MP2 conductor stack: 8 AWG battery leads with three 12 AWG runs per phase (~10 mm²); stuffing 6 AWG through the layout risks strand damage and shorted legs when the ~420 A protection trips, making rework miserable.[^296]
- **Laser-cut torque arms for bigger axles.** Swapping to 14 mm laser-cut torque arms ahead of QS hub upgrades shows how much fabrication margin dual-sport conversions need once axle diameters grow past stock hardware.[^297]
- **Purge solder-clogged vias with air.** Clearing Makerbase 75200 headers goes faster by heating the solder and blasting ~4 bar compressed air through the hole; flux and hand wicking alone can take hours.[^298]
- **Hand-tap new caliper mounts.** Builders drilling fresh brake mounts now insist on manual tapping with proper holders, frequent back-outs, and rigid clamping.
  - power tapping keeps snapping bits, and a machinist can rescue damaged holes when patience runs out.[^299]
- **Skip resin potting unless it’s disposable.** Makerbase’s factory silicone can be peeled for repairs, but epoxy potting kills rework and buries ADC pins.
  - stick with serviceable sealants plus dielectric isolation when repainting decks.[^300]
- **Capture crash puck STLs.** Pandalgns is printing 100 % infill ASA “anti-fall” sliders for deck protection.
  - archive the files once shared so riders can bolt sacrificial pucks to high-power builds instead of grinding the chassis.[^301]
- **Leverage shared CAD before cutting metal.** Builders posted a Fusion 360 SurRon frame model for scaling custom plates and 20 S packs.
  - use it to validate deck packaging before machining or welding chassis parts.[^302]
- **Leave MOSFET legs necked unless the design expects vertical mounting.** Surface-mount packages rely on those thin sections to sit flat against the spreader; trimming to the fat tab only works on vertical installs such as Nucular’s sealed boards that pair the mod with layered short- and hall-protection hardware.[^303]
- **Resolder burnt stator joints before trusting high-speed conversions.** A 13.5 kg E-TWOW on 15 S3 P Samsung 50G cells hit 60 km/h without mechanical brakes, and the crew agreed that scorched terminations warrant an RMA or complete rewire with heavier-gauge leads before the next test ride.[^304]
- **Lean on turnkey printers for fixtures.** The Bambu P1S keeps showing up in shop logs because its enclosed chamber and stock ABS/ASA profiles pump out spacers, insulation trays, and lighting brackets without weeks of slicer tuning.
  - handy when you’re iterating housings for high-power decks.[^305]
- **Purge metal shavings before reassembly.** Deck debris has tripped smart BMS hardware, scrambled VESC state-of-charge maths, and forced pack recalibrations even after the harness was cleaned.
  - vacuum, blow out, and retest telemetry before sealing the enclosure.[^306]
- Skip decorative deck fans and hobby water loops.
  - without controlled exhaust paths and real thermal interfaces they stall immediately, so bolting MOSFETs to structural aluminum still beats gadget airflow experiments.[^307]
- **Plan deck extenders for serviceability.** Halo T107 builders split carbon-fibre deck extenders into a lower battery drawer and upper electronics bay, relocating headlights into the extender and re-drilling misaligned mounts to keep service access reasonable despite tight packaging.[^308]
- **Mini BMX conversions stay modest on current.** Haku’s 20 S 3 P P42A build runs dual Spintend 100/100 controllers near 65 A battery / 100 A phase per side, underscoring how shorter wheelbases and small hubs demand restrained tunes even when the controllers can deliver more.[^309]
- **Stagger multi-controller upgrades.** Smart Repair’s Kaabo GT hybrid currently runs a 20 S 9 P (~40 Ah) pack with a front Ubox 150 and rear Ubox 250, topping out around 115 km/h until the new battery lands and the rear controller upgrades to a Tronic X12.
  - log sag and plan airflow before mixing disparate controllers in the same frame.[^310]
- **Post-crash inspections are mandatory.** A Halo rear controller that spat MOSFET silicon during a 20 km/h lock-up launched its rider; the recovery plan now includes stripping both motors, checking harnesses for damage, and replacing the destroyed display before returning the scooter to service.[^311]
- **Prep Dualtron frames without stripping anodizing.** Thunder builders now keep the stock heatsink plate, clean wiring, and resist grinding the frame bare.
  - bolting paired 75200s directly plus tidy harnessing beats chasing raw-aluminum contact and risking corrosion; intermittent faults often trace to loose wiring, not the 220 A BMS rating.[^312]
- Laser-cut 0.5 mm copper busbars sandwiched under nickel keep 20 S 10 P packs tidy; budget for KWeld/Malectrics rigs delivering ≥1 kA pulses when welding copper.[^24]
- Treat theories about extra-long leads wicking controller heat as unproven until data surfaces.
  - the group called the idea out immediately and stuck with compact looms.[^313]
- Jason shortened his 17×4 phase leads to drop roughly 3 mΩ of resistance, restoring reliable 140 A launches without ABS trips; after a 300 A experiment blew MOSFETs, he now treats 100 A battery / 250 A phase as the sustainable MP2 ceiling on 150 V packs.[^314]
- Sandwich 0.1 mm copper under nickel and keep weld energy near 50–60 J with KWeld/Malectrics probes while using the “infinite slot” (dual-strip) technique to push current into the can without cracking copper.[^315]
- Halo T107 rewires require widening the axle slot from 8 mm to 10 mm so 12 AWG phases and 28 AWG hall leads pass without pinching.
  - Pandalgns removed minimal material and now has room for temperature sensing on the 60 H hub once it moves to 72 V duty.[^316]
- NetworkDir’s teardown logs keep 4 mm phase leads around 50 A battery / 120 A phase on Mantis and Wolf-class motors; plan rewires or harness upgrades before commanding more current through stock looms.[^317]
- 0.1 mm copper at 10 mm width already carries roughly 15–20 A per parallel cell (≈200 A on 9 P groups), so oversizing plates is unnecessary unless you exceed those per-cell currents.[^318]
- Happy Giraffe’s drilling playbook.
  - pilot slightly above chisel width, add cutting fluid, and chase threads with tapping grease
  - helps land precise M6 bolt patterns even without a full machine shop; spring punches recentre wandering pilots.[^319]
- Cheap 180×300 mm hobby lathes only cut soft aluminium.
  - source heavier used machines for steel work and confirm household wiring can feed welders or lathe motors without tripping breakers.[^320]
- Align hubs and rotors with proper tooling—mag-base dial indicators and CNC edge finders beat eyeballing even if tyres mask some runout.[^321]
- DIY spot welders need quality LiPo/capacitor banks—cheap 20 € control boards still demand 100 € batteries or supercaps to avoid melted leads.[^25]
- Bring unvetted ESCs up on a current-limited bench supply and inspect insulation before connecting full pack voltage.
  - one rider torched a bare board immediately after assuming every controller shipped with a protective rear cover.[^322]
- Powder-coating hub shells is risky—the cure oven runs ≈204 °C and can demagnetize rotors—stick to high-temp paint or ceramic coatings for cosmetic refreshes.[^38]
- Tubeless tire swaps are harder than YouTube suggests.
  - 11″ Wolf rims and tight beads led the crew to curate tool lists and tutorials after wrestling them for hours; stock spares early as tyre prices jumped ~16 % with supply disruptions.[^323][^324]
- Depower packs before any rework: energized Makerbase 75200 soldering triggered an instant fire, so standard practice now includes disconnecting batteries, stripping old paste, and thread-locking covers after service.[^325]
- Keep phase leads short.
  - 2 m runs on Flipsky 75100 builds choked phase current to ~11 A and pushed other riders into oversaturation once phase cables stretched toward two metres; shorten or upsize leads before chasing controller faults.[^326][^327]
- Conformal coating remains cheap insurance even on sealed singles; spray boards and re-harden harnesses because water ingress elsewhere will still defeat unsealed wiring.[^328]
- Charge-port shorts still kill controllers—add double-check rituals and isolate packs before handling ports, even on “simple” service calls.[^329]
- **Break power symmetrically when unplugging CAN.** PuneDir blew the Ubox Lite’s onboard ESD protector by pulling a single battery lead while the CAN link stayed live, so always de-energise both rails before touching CAN looms.[^330]
- Pandalgns drafted a Halo T107 loom extender that isolates the battery bay from control wiring, relocates frame lights, and adds dedicated pass-throughs for phase, hall, brake, dash, and charger leads so the frame finally has Dualtron-style service access.[^331]
- Silicone battery bays and deck seams before returning customer scooters—shops saw standing water reach controller bays without full sealing.[^deck_seal]
- If water breaches the deck, depower immediately, open the enclosure, force-dry with air/isopropyl rinses, then reseal with silicone along seams and cable glands once hardware checks out.[^water_recovery]
- Heat pipes are replacing water loops on cramped decks: riders now bolt finned arrays between controllers and frames, pair them with 10 mm² leads for 80 A shared-pack builds, and leave pumps to marine projects.[^332]
- Her0DasH warns that clamping bare copper heatsinks directly to aluminum frames invites galvanic corrosion.
  - add silicone isolators or nickel plating before bolting mixed metals together.[^333]
- Treat live charge-port work as a checklist drill.
  - a single slip during a Vsett swap shorted the leads and filled the garage with smoke.[^334]
- DIY Type 2 adapters only handshake reliably once the pilot resistor drops to ~880 Ω and a manual status button is added.
  - confirm wiring before plugging into public EVSEs.[^335]
- Daly smart BMS boards reboot straight from the phone app, saving deck teardowns on sealed builds—log the workflow for field techs.[^336]
- Tronic controllers revived after water damage still need the DC-DC enable pad scraped clean and re-soldered before conformal recoating.
  - hot-air reflow seals the fix.[^337][^338]
- Purp’s hall-less Mantis 10 conversion planning shows single Ubox/Spintend modules (~58 mm wide) can be stood on edge along the frame or split between floor and lid; Noname suggests foam or 3D-printed dummies to test fit and warns screw mounting becomes the bottleneck inside cramped controller bays.[^339]
  - Log the final mounting and cooling layout once Purp finishes street testing so future hall-less swaps know which orientation holds temperature and vibration in check.[^mantis-controller-proof]

## 7. Chassis Benchmarks & Handling Notes

- Dualtron Thunder still leads >150 km/h stability thanks to adjustable arm angles and shortened stems, while GT2 and Inmotion RS platforms need CNC work yet reward riders with calmer steering above 90 km/h.[^340]
- Thunder wobble troubleshooting starts with hardware.
  - not dampers: riders blamed factory tires that dislike lean, single front-brake setups, loose wheel centering, and tall arm positions before collar clamps and steering geometry entered the conversation. Lower the chassis, balance brakes, and upgrade to PMT or quality Xuangxeng clones before chasing damper fixes.[^341]
- NAMI frames excel for long-range and off-road duty when paired with quality dampers instead of raw top-speed tuning.
  - a reminder to match geometry to mission.[^340]
- PMT Junior slicks feel glued on Segway G2 builds, but veterans refuse to ride 90 km/h without a steering damper.
  - budget damping hardware alongside premium rubber once speeds climb.[^342]
- Singapore’s clampdown on PEVs pushed locals to disguise VESC builds as e-bikes or commute across the Malaysian border, highlighting legal context as part of reliability planning when choosing frames and accessories.[^343]
- Miniwalker’s race win underscored how lighter packs can beat heavier “big battery” builds on technical circuits when sag is controlled and rider skill is comparable.[^mini-light-pack]
- Purpose-built tubeless rims from rfp-performance (via Sombre_enfant) and Amass 8 mm bullets have proven race-ready—source them before trusting split rims that pop beads under load.[^rfp-rims]
- Lonnyo 70 H and 75 H hubs share axles/shells with the 60 H, squeezing into G30 forks so long as the deck budget allows at least a 5 P pack; 90 H experiments remain deck-limited.[^344]
- Despite the occasional drag scooter experiment, race builds still rely on chain drives; belt-drive prototypes remain rare enough to treat as experimental hardware.[^race-chain]
- Kirill’s geometry diagrams highlight how inverted forks can slip into negative trail mid-travel.
  - target consistent positive trail like motorcycle telelever setups or risk self-flip tendencies at speed.[^345]
- Her0DasH warns Ninebot’s tubular-frame scooters (F-series, Mi 3/4, kid models) cram wiring and epoxy neck joints so tightly that bearings chew out and dust infiltrates hubs.
  - fine for errands, miserable mod platforms.[^346]
- Yoann’s Spintend 85/200 + 70 H builds benefited from pack cycling, 40 A of field weakening, side-cap phase exits for thicker sleeved leads, widened Burn-E dropouts, and tubeless-ready split rims.
  - older axle-exit hubs stay tube-bound.[^347]
- Tommy notes Xiaomi’s Mi 3 Lite/4 frames aren’t Ninebot-built.
  - they’re flimsier, software-locked, and even rear tire swaps require deck removal while the Pro 2/Pro 3 remain mod-friendly baselines.[^348]
- Sombre_enfant’s Beni Stern Thunder build.
  - dual 90 H hubs, titanium steering tube, 20 S10 P 40T battery
  - shows how custom frames push far beyond production packaging.[^349]
- Yamal pegs LY’s latest 70 H hubs around €800 and confirms they remain drop-in upgrades for most 11″ chassis while builders evaluate new 90 H customs.[^350]
- PuneDir is eyeing Makerbase 84100HP controllers as replacements for repeatedly failing Zero ESCs.
  - a reminder that mid-tier housings crave sturdier VESC swaps.[^351]
- **Mind Kaabo/Wolf hub swaps.** Slotting Wolf or Kaabo hubs into Dualtron arms needs alternative washer stacks and sometimes a fresh cable exit; flipping the stator rarely works because the laminations are asymmetrical, so plan machining before promising the fit.[^352]
- **Pair Thunder builds with metal-bodied VESCs.** Dualtron Thunder owners running 72 V/36 Ah packs and 60 H Wolf motors are shelving Flipsky 75200s in favour of Spintend or other aluminium-clad controllers that hold higher continuous current without cooking.[^353]
- **Street-legality workflow:** Noname confirmed NIU frames ship with VINs while custom builds require homemade-vehicle inspections; skip self-stamped numbers (a crime) and either prep DOT tyres for inspection or register a donor motorcycle frame when moped plates cap at ~30 mph.[^354]
- **Respect C-fork wobble limits:** Multiple riders have crashed Vsett 10+ and similar C-fork scooters above ~80 km/h; expect fatal wobble risk unless trail numbers improve and dampers plus tire selection are dialed.[^355]
- **Pick frames that match speed goals.** Lightweight 20 kg-class decks (G30, Kaboo Mantis 8, etc.) need major pack cuts or dual VESC swaps to sniff 60–100 km/h, while heavier 56 kg Segway GT2 builds already hold traction and stability for top-speed runs.
  - choose chassis based on the power envelope instead of forcing commuter frames past their comfort zone.[^356]
- **Match tire profiles to rim width.** Zero/Vsett owners are adopting PMT’s 80/70-6 casings on 6 in rims for a fuller contact patch while steering clear of 10×3.5 casings that “egg” on narrow wheels; stick to 10×3 slicks when the rim can’t support wider beads.[^357]
- **Front brakes are non-negotiable above highway speeds.** Riders flogging Zero 10X builds past 100 km/h with only a rear Nutt caliper plus regen keep getting called out.
  - reinstate the front brake hardware before more high-speed testing.[^358]
- **Face de Pin’s Thunder clamp is now the hinge insurance benchmark.** Their bracket ties the steering stem to both axle nuts and, paired with waterproofed C350 enclosures, has kept race Namis lapping in the rain.
  - use it as the template when chasing similar reinforcement.[^359][^360]
- **Traction control preserves tires:** Holding an ~80 000 ERPM differential kept CST 10×3 rubber alive on Zero/Vsett builds, while disabling TC shredded tires within days.
  - log TC settings as part of chassis maintenance.[^361]
- 🇪🇸AYO#74’s 33×2, 70 H build still lifts the front above 135 km/h even with ramp-time tweaks; he’s reviving the steering-cam sensor before re-enabling traction control, and Haku/Yamal benchmarked 400 A phase / 200 A battery as the power needed to chase 90 mph once cooling is sorted.
  - plan TC and steering feedback before chasing similar speeds.[^362]
- VESC’s IMU still chases “level” by default, so enabling wheelie control mid-stunt will yank the scooter upright unless you start at the target pitch.
  - Noname warns small-stator builds need custom logic if you expect controlled wheelies.[^363]
- Wrap Makerbase logic sections in Kapton or other dielectric barriers during installs; a single static discharge was enough to nearly scrap a 75100 before the insulation fix.[^maker-kapton]

## 8. Structural Integrity, Performance & Safety

- Treat 30 S ambitions as a full-system redesign.
  - teams upsized ESCs, fusing, and insulation after concluding that 20 S is the practical ceiling without more chassis room and safety tooling.[^364]
- Never leave lithium packs charging unattended.
  - mis-matched chargers have already set beds and floors alight when riders walked away from RC-style bricks.[^365]
- Retire helmets after any hard crash; the community bins shells immediately rather than gambling on hidden damage during the next fall.[^366]
- Replace bearings and add ferrofluid or seals whenever you fit fresh Chinese hubs (Lonnyo, Inokim, Dualtron); veterans treat the factory hardware as disposable and rework it before first rides.[^367]
- Face de Pin Sucé’s Slack Core 920R customer snapped the chassis before delivery, forcing a choice between custom reinforcement and migrating the build to a Rage frame.
  - treat Core frames as needing structural scrutiny before you pour power into them.[^368]
- 🇪🇸AYO#74 reminded early Nami owners to swap the original soft axle for the stainless retrofit (≈€60 installed) to head off the stem failures that sparked factory recalls.[^369]
- **E-moped packaging blueprint:** Noname’s Niu-based commuter (32 S 20 P Samsung 35E, QS260 45H, dual 85/250s) now hits 0–68 mph in 18 s, proving seated builds can reach highway pace without abandoning scooter-style packaging.[^370]
- **Keep a legal profile handy.** Yamal keeps his modified Nami out of city centers and rides a sleeper Ninebot under 25 km/h to avoid enforcement crackdowns in dense areas.[^371]
- **Watch regional utility trends.** Segway ZT3 delivery scooters are popping up across Spain, highlighting how regulated markets steer riders toward compliant utility frames over outlaw builds.[^372]
- **Bank on safety gear, not luck.** Community logs include fatal solo crashes even among veteran tuners.
  - keep full-face helmets and conservative margins part of every test plan.[^373]
- **Controller cut-outs can crash racers.** A front-motor dropout at Le Mans rag-dolled a rider mid-corner, matching other reminders to inspect traction hardware as closely as tires before track sessions.[^374]
- **Sideline wounded controllers.** Riders park 85 V 240 A Ubox units the moment a capacitor blows.
  - even if the board still boots
  - to avoid cascading failures while waiting on repairs or single-controller swaps.[^375]
- **Audit yourself after crashes.** A rider who slid out taking a turn too fast escaped with minor injuries but only after a post-crash self-check.
  - build personal assessments into ride protocols before resuming hard pulls.[^376]
- Replace cracked Zero/Nami stems with solid aluminum or 15 mm steel units when running wheelie-heavy, 8 kW+ builds; repeated failures cluster at cable cutouts.[^26]
- Heavy ~110 kg riders driving dual Spintend 85/240 stacks at 100 A battery / 200 A phase / 300 A ABS have logged rear-motor cut-outs.
  - treat drivetrain fatigue as a hard limit and capture logs before chasing higher torque numbers.[^377]
- Inspect VSETT 10 steering columns for thin-wall fractures and retrofit thicker Warrior stems or machined sleeves before chasing high-power builds.
  - the factory pole has split cleanly at the lower weld in real-world photos.[^43]
- **Audit new motors on arrival.** Supposedly “fresh” VSETT hubs have shown rust, loose magnets, and carbon dust.
  - strip, clean, and re-glue magnets with Loctite AA326 before trusting them.[^378]
- **Use proven frames for high-speed builds.** Fabricating motorcycle frames from raw tubing demands professional jigs; veterans salvage legal 50 cc chassis or buy production Surron/Bomber frames instead of trusting hobby welds at 70 km/h.[^379]
- Replace cracked Zero/Nami stems with solid aluminum or 15 mm steel units when running wheelie-heavy, 8 kW+ builds; repeated failures cluster at cable cutouts, and the older Zero 10X 60-series necks without the “X” rib keep snapping under aggressive wheelies.
  - inspect or upgrade before chasing 140 km/h claims.[^380][^381][^26]
- Nami owners grafting Kaabo forks say the mod is mostly cosmetic.
  - 70 H hubs fit, but 75 H clearance remains unproven without extra machining, so don’t assume the swap unlocks bigger stators out of the box.[^382]
- Face de Pin Sucé now races with a waterproof enclosure around the Nami C350 controller and machines replacement Thunder-family frame parts in-house so hinges survive rain events that sidelined rivals.[^360]
- NetworkDir still calls the Dualtron Thunder 3 and Storm LTD the weakest frames in the lineup because of folding-hinge flaws, preferring older T1 chassis unless you reinforce hinge hardware yourself.[^383]
- Burn‑E owners confirm the stock hub is a 17×4 in 60 H (~1.5 kW) motor, while Kaabo’s Wolf King GT ships 60 H 22×3 hubs.
  - jumping to 11″ motors usually means import workarounds and custom swingarms.[^384]
- **Respect thermal limits.** Fresh 60 mm hubs run happily around 50 A battery / 100 A phase with ferrofluid, while 11″ torque motors shed magnets under sustained 200 A+ phase and aggressive FW pushes.[^385]
- **Parking-brake experiments:** Without native locks, some riders wire breakers or briefly short motor phases as a parking brake.
  - effective but risky if applied while rolling, so treat it as a last-resort theft deterrent.[^386]
- **Respect thermal limits.** Fresh 60 mm hubs run happily around 50 A battery / 100 A phase with ferrofluid, while 11″ torque motors can unglue magnets when you stack 200 A+ phase, MTPA, and FW.
  - even a 10″ Blade motor only hit 117 km/h on 15 S after easing back to proven controllers instead of fragile early 75100s.[^387][^388]
- **Cool brakes before stopping.** Magura calipers that are smoked by high-speed stops need gentle rolling cooldowns.
  - parking immediately boils the fluid and forces a re-bleed.[^389]
- **Match motor Kv front to rear.** Mixing unequal windings turns the faster hub into a drag load once speed climbs; keep Kv aligned before chasing independent tuning.[^390]
- **Fix hall sensors instead of running blind.** Sensorless launches sacrifice low-speed torque and smooth take-offs.
  - repairing halls beats ditching them just to avoid soldering.[^224]
- **Add halls to sensorless front hubs when chatter appears.** Paolo’s 33×2 70 H motors stopped vibrating around 10–15 km/h once hall sensors were soldered in, reinforcing that torque-wound fronts need sensors for smooth low-speed launches.[^391][^392]
- Keep head bearings just snug enough to remove play—over-tightening preloads the races, induces wobble, and shortens bearing life even when premium dampers are installed.[^headset]
- **Audit fork geometry before adding dampers.** Poorly tuned C-type forks and weak Weped Fold stems have tossed riders during panic stops; reinforce dropouts with torque plates, swap in grade‑12.9 axles, and match suspension setup to local road quality before chasing 150 km/h bragging rights.[^393]
- **Validate tubeless rim dimensions.** 11 in PMT-style slicks tame chatter once mounted tubeless, but the handful of 12 in 4.5-wide options demand ≈66 mm rims.
  - confirm width before ordering so the bead seats cleanly.[^394][^395]
- **Pick stout 11″ chassis.** Zero-style clones (Kugoo G1, Falcon, Vsett 10+, Nanrobot, Mukuta, Varla) share weak stems that have snapped during 30 km/h braking; riders migrating to 11″ builds favour GT2 or Teverun/Blade frames with dampers and reinforcement welds.[^396]
- **Install sealed hub bearings.** Vsett/Zero owners replacing stock bearings with 2RS units from SKF-class brands report far better winter durability.
  - open bicycle bearings or no-name copies seize quickly in slush and can pitch the wheel sideways at speed.[^397]
- **Re-torque axle hardware with fresh arms.** New torque arms torqued around 60 Nm with threadlocker keep hub axles seated after power upgrades, preventing cable strain and dropout fretting on high-power builds.[^398]
- Prioritize mechanical brakes and axle hardware (blue Loctite + lock washers) because electronics can die mid-ride; round-profile tires boost corner grip but require careful bead seating, and even Pune’s regen-heavy build kept a rear drum as the safety net while flashing 6.05 for smoother braking.[^399][^27]
- **Keep carbon paste off bearings.** Carbon assembly paste that migrates into headset bearings will seize the steering once it mixes with grease; clean and re-grease or swap the bearing if contamination occurs.[^400]
- **Audit fork geometry before adding dampers.** Poorly tuned C-type forks and weak Weped Fold stems have tossed riders during panic stops; reinforce dropouts with torque plates and match suspension setup to local road quality before chasing 150 km/h bragging rights.[^401]
- Prioritize mechanical brakes and axle hardware (blue Loctite + lock washers) because electronics can die mid-ride; round-profile tires boost corner grip but require careful bead seating.[^27]
- Retire tiny XTech-style calipers on 60 km/h+ scooters.
  - their minimal oil volume, rattling auto-centering hardware, and heat-warped rotors demand thicker discs and frequent inspections after flats or emergency stops.[^402]
- High-speed stability starts with positive trail and stiff bearings—bolt-on dampers merely mask poor geometry and can fail under stiff aftermarket springs.[^28]
- PuneDir’s 90 km/h traffic runs sparked another reminder that dampers alone aren’t enough.
  - NetworkDir chased wobble fixes through frame geometry, suspension setup, and trail numbers before trusting 100 km/h tunes.[^403][^404]
- Heavy tires and helmet-mounted action cams can destabilize Zero 10X builds above ~65 km/h.
  - Shlomozero’s high-speed runs mixed 50 H motors with bulky tyres and still felt sketchy, so trim rotating mass and rethink camera mounts before pushing top speed.[^405][^406]
- Inspect Laotie-style steering tubes and similar hollow-neck chassis for cracks; wobble on ES19 builds often traces to the front swingarm and budget shocks, so riders retorque bolts, upgrade suspension, brace the stem, and still budget chromoly TIG reinforcement borrowed from roll-cage fabrication for 80 km/h duty.[^laotie][^laotie-es19]
- **Reinforce cockpits for triple-digit runs.** Crash reports above 110 km/h on Zero 10X-class frames pushed veterans toward titanium stems, reinforced handlebars, and wide slicks before reattempting high-speed pulls.
  - treat chassis stiffening as mandatory, not optional, when chasing those numbers.[^407]
- PuneDir’s Zero 12″ experiments showed upsized tyres exacerbate wobble on marginal trail—fix geometry before chasing larger rubber.[^408]
- Retire Wheelway hubs when magnet adhesive browns.
  - overheated units have cooked halls clean off and are safer replaced with high-KV Blade motors for 12 S speed builds targeting 35–40 A battery / ~120 A phase.[^409]
- **Log where rental frames are still available.** SNSC 2.3 chassis are drying up as EU fleets pivot to Okai hardware, so builders are hoarding spares, cataloguing which operators still auction frames, and standardising Bambu P1S print profiles for spacers, lighting pods, and harness saddles that drop straight onto the rental geometry.[^410][^411]
- Upgrade braking hardware for 100 km/h stops: thin 1.8 mm bicycle rotors deform under sustained heat, so move to 3 mm+ rotors, fresh pads, and even moped-grade calipers while logging GPS-backed deceleration data to validate gains.[^brake-data]
- On VSETT-class builds, jump from stock 140 mm discs to 160 mm SRAM Cleansweep or 180 mm Magura MDR-P rotors, align pads with purpose-made brackets, and swap washer stacks for machined mounts to avoid warping under heavy loads.[^412]
- Routing Magura hoses externally demands short banjos and matched kits.
  - the Elvedes Hydro kit covers dual M8 banjos, Jagwire quick-disconnects require their own hose sets (~$120–$125 per scooter), and Hope’s HFA701 bundle delivers M6 banjos/bleeders without custom machining.[^413]
- Expect 43 kV Rion-spec hubs to overwhelm compact FOC units—pair them with ≥250 A phase controllers (Kelly, Sabvoton) or risk repeated VESC 75/200 failures at low ERPM.[^high-kv]
- Keep both motors active unless legally required otherwise; two hubs share copper losses better and a “sleeping” front wheel drags more than a free-spinning rim.
  - PuneDir even logged 20 A into a single hub as slower than splitting the same 20 A across both motors (10 A/10 A). Use CAN profiles or power cuts only when staging compliance modes for inspections.[^414][^dual-motor]
- Theft prevention relies on ≥10 mm hardened chains, welded eyelets, and recessed fasteners; thin aluminum tabs remain easy targets for cordless grinders.[^29]
- Treat “six-phase” marketing claims skeptically.
  - most scooter hubs simply double conductor count on standard three-phase motors, lowering voltage drop and inductance rather than adding true electrical phases.[^16]
- Gear up accordingly: commuters pushing 50–60 km/h stick with full-face motorcycle lids meeting ECE 22.05/22.06 and treat DOT-only stickers as insufficient.
  - lighter downhill helmets such as the iXS Trigger FF with MIPS stay on hand for slower summer rides but sacrifice protection.[^415]

## Legal & Compliance Prep

- Noname confirmed NIU frames ship with VINs while custom builds do not; instead of stamping your own (a crime), pursue homemade-vehicle inspections with DOT tyres or register a donor motorcycle frame because moped plates cap you near 30 mph.[^416]
- Swiss enforcement campaigns are handing out CHF 20 reflector fines, €1 370 penalties, and even impounding scooters when police spot obvious mods; builders label hardware “250 W,” carry invoices, and keep stock-looking displays plus compliance paperwork ready for roadside tests that clock instantaneous peaks rather than nominal power.[^417]
- Do not rely on regen-only stopping at 20 S.
  - builders logging 50–65 km/h runs treat hydraulic brakes as mandatory backup and keep them freshly bled before trusting wheel-locking e-brakes.[^418]
- Rental Ninebot stems ship with red Loctite on the pole hardware.
  - if you reassemble without fresh threadlocker the pole wobbles, so heat the screws for removal and reapply medium threadlocker plus the factory washers on reassembly.[^419]
- High-speed stability starts with positive trail and stiff bearings—bolt-on dampers merely mask poor geometry and can fail under stiff aftermarket springs.[^28]
- Pick suspension for the job: hydraulic dampers maximise comfort, elastomer stacks keep scooters planted at speed, and crews are eyeing Bronco’s Xtreme 11 chassis as another mod-friendly platform.[^420]
- Ninebot’s Max G2 frame still uses thin sheet sections.
  - Jan and Mirono steer heavy riders back to aluminium G30 decks or surplus SNSC rental frames if they want true abuse tolerance.[^421]
- Inspect Laotie-style steering tubes and similar hollow-neck chassis for cracks; reinforcing with chromoly TIG work borrowed from roll-cage fabrication remains the durable fix when the factory welds give way.[^laotie]
- **Size main harnesses for the current goal.** 20 S 9 P packs chasing ~350 A peaks now ship with 6 AWG leads or paired 8 AWG runs on QS8s, and crews remind racers that true 500 A duty calls for ≈50 mm² copper despite short harnesses letting some builds skate by temporarily.[^422]
- Delta rewinds demand roughly double the phase current for the same torque—upgrade hub leads before flipping to delta to avoid roasting stock windings during high-speed pulls.[^delta-leads]
- Theft prevention relies on ≥10 mm hardened chains, welded eyelets, and recessed fasteners; thin aluminum tabs remain easy targets for cordless grinders.[^29]
- Protective gear still matters at commuter speeds.
  - stick with ECE 22.05/22.06 full-face helmets with MIPS-style liners and treat subdued lighting plus “police mode” buttons as tools for avoiding unwanted attention, not excuses to ride unarmoured.[^rider-safety]

## 9. Charging Infrastructure & Power Logistics

- Expect charger LEDs to cycle red/green near 100 % SoC on Daly/YXP units—this is normal balancing behavior, not a wiring fault.[^30]
- GTK 0–102 V adjustable supplies and 120 V lab PSUs offer cheaper wide-voltage charging versus Grin Satiator if you can live with bulkier hardware and lower (≈3 A) defaults.[^31]
- **Verify isolation before stacking chargers.** Check for earth-referenced outputs with an ohmmeter before wiring supplies in series.
  - bonded returns can trip breakers or energize frames, so long-term builds rely on purpose-built high-voltage chargers instead of improvised pairs.[^423]
- Stock Laotie packs can sag from 58 V to 50 V under load; log real-time voltage drop and adjust low-voltage cutoffs or plan pack upgrades before increasing current limits.[^32]
- Add radial shaft seals or swap to premium cartridges on Xiaomi-class front ends—stock caps let water in after rain and eat bearings quickly.[^424]
- Nucular controllers already accept PSU inputs below pack voltage and charge through phase leads (e.g., 3 kW Flatpack2 feeding ~13 A into 20 S); riders pair them with 2–4 kW adjustable lab supplies.
  - on 110 V grids that lands ~13 A at 72 V, while 220 V outlets can deliver the full 37 A output, though most cap real-world charging around 20 A for safety, and Vedder’s VESC firmware still omits converter mode because he considers user-programmed PSUs too risky.[^425][^426][^427][^428]
- Skip bargain FLJ/Janobike/Boyueda frames for 100 km/h builds.
  - the rebranded chassis ships with sloppy folding tolerances and cheap hardware, so serious riders either rework the frame or avoid the platform entirely.[^429]
- Properly potted controllers (à la Nucular) pass bucket-immersion tests, wick heat into the housing, and add vibration damping.
  - just discharge capacitors and use non-conductive, low-expansion compounds so the cure cycle doesn’t crack boards.[^430]

## Outstanding Compliance & Diagnostic Follow-Ups

- Watch EU regulatory changes for high-power scooters and confirm whether private insurance remains viable for Halo-class builds so compliance advice stays current.[^eu-halo]
- Capture Luis’ root-cause analysis of the MKS 84 HP 48 V shutdown—including any pre-charge, shunt, or firmware faults plus logs—before closing out the failure mode section.[^mks-shutdown]
- Revisit Nawfal’s MKS 84 HP speed cap to document whichever firmware, pole-count, or hardware tweaks restore the expected 80 km/h ceiling.[^mks-speedcap]

---

## Source Notes

[^1]: Experienced tuners steer buyers away from Makerbase/Flipsky boxes because of QC defects and instead recommend 3Shul, Spintend, Trampa, or Ubox-class controllers.[^431]
[^2]: Makerbase alu-PCB units overheat without heatsinking; racers migrate to dual Ubox or similar hardware after fuse and logic-rail failures.[^432]
[^mini-light-pack]: Miniwalker’s win highlighted how lighter packs outpace heavier builds on technical courses when sag stays controlled.[^433]
[^rfp-rims]: Sombre_enfant pointed the crew to rfp-performance tubeless rims and matching Amass 8 mm bullets after losing beads mid-race.[^434]
[^race-chain]: The group agreed most race scooters still use chain drives, treating belt-drive examples as rare experiments.[^435]
[^3]: BRIESC controllers target 200 A battery/400 A phase capability in a compact footprint, proven on 22 S builds chasing 154 km/h runs.[^436]
[^4]: Makerbase 75100 boxes deliver roughly half to one-third of programmed current, motivating upgrades to Ubox 80100-class controllers.[^437]
[^makerbase_v2]: The rumored Makerbase 75100 “V2” is merely the aluminum-PCB refresh and keeps the same QC faults (stray solder, inaccurate shunts, missing key switches, poor documentation).[^431]
[^5]: Flipsky 75350 shunt sizing realistically caps usable phase current near 500 A despite marketing claims.[^438]
[^hp-84100-guardrails]: Real-world logs cap Flipsky 84100s at roughly 60–80 A battery and ~135 A phase, while Makerbase 84100HP riders rarely exceed 85–100 A battery without upgrading the stock looms that struggle past 60 A.[^439]
[^hp-voltage-headroom]: Builders stepping to 20 S packs still recommend 100 V controllers.
  - running 21 S or strong regen on 85 V hardware remains risky even with braking boosts disabled.[^440]
[^hp-budget-path]: Spintend’s 12 FET remains the proven budget commuter choice, with Ubox Lite or 85/250 as reliable upgrades when Tronic-class controllers are unavailable.[^441]
[^6]: MP2/CCC_ESC is a 30 S-capable DIY design requiring through-hole assembly, heatsink machining, and firmware flashing, shared via community GitHub links.[^442]
[^7]: Samsung 29E packs sag heavily; racers rebuild with high-discharge P42A or VTC6A cells to maintain 130 km/h pulls.[^443]
[^8]: TPU spiral wrap and PET braided sleeving have survived 18 months outdoors, making them preferred harness upgrades.[^444]
[^loom_triage]: Riders temporarily stack shrink-wrap over exposed looms until proper sleeving arrives, then replace it with TPU or PET braid for lasting protection.[^444]
[^9]: Poor stock harness construction and throttle-ground failures drove the community to re-terminate connectors, add strain relief, and minimize inline joints.[^445][^446]
[^10]: Waterproof Julet/L1019/HiGo connectors work well but L1019 peaks around 100 A phase; hall/thermistor additions feed reliable telemetry.[^447]
[^hp-cabling]: Riders are doubling phase cross-section to tame voltage drop, keeping silicone 12 AWG on G30 phases, monitoring 4 mm² (~AWG 11) leads near 250 A, and extending “silver” looms with real copper because the shiny conductors are only tinned.[^448]
[^11]: Stock packs using LG M50LT/Samsung 29E cells are limited around 120 A discharge; builders monitor IR spread before parallelizing groups.[^449]
[^eu-halo]: Pending EU legal updates for high-power scooters and insurance viability for Halo-class builds. Source: knowledge/notes/input_part011_review.md†L905-L905
[^mks-shutdown]: Awaiting Luis’ diagnosis of the MKS 84 HP 48 V shutdown and associated fault logs. Source: knowledge/notes/input_part011_review.md†L906-L906
[^mks-speedcap]: Outstanding investigation into Nawfal’s capped MKS 84 HP top speed and whatever fixes restore 80 km/h. Source: knowledge/notes/input_part011_review.md†L910-L910
[^hp-32e-limit]: Samsung 32E cells plateau around 6.5 A each (~39 A for 6 P), so extra nickel over the joints adds little for mid-power scooters.[^450]
[^12]: Riders cap regen between –5 A and –12 A on 60 V 38 Ah packs until BMS specs are confirmed.[^451]
[^13]: ERPM speed limits caused intermittent regen dropouts that firmware 6.05 beta (build 20) resolves, preventing over-voltage incidents on high-S setups.[^452]
[^makerbase_regen]: Flipsky/Makerbase 75100 aluminum-PCB controllers keep failing on 22 S packs when regen pushes bus voltage past 100 V; veterans disable e-brake or upgrade to Ubox-class hardware for high-voltage builds.[^453]
[^hv_bleed]: 21–22 S owners drop charge voltage slightly (e.g., 86.5 V vs. 88 V) before hill descents to maintain regen headroom without overstressing controllers.[^454]
[^14]: SNSC/Ninebot rental hubs reach ~160 °C when pushed to 20 S 30–40 A without cooling; veterans recommend 13–16 S for daily use.[^455]
[^15]: JK active-balancing BMS lines advertise RS485/CAN while AliExpress listings vary on heater support, so riders source from official channels; JK apps remain more reliable than ANT.[^456][^457]
[^16]: Adding hall sensors and thermistors directly to VESC inputs improves launch smoothness and thermal telemetry; Bluetooth probes lag inside hub shells.[^458]
[^17]: Stators can be 100 °C hotter than hub shells for minutes, underscoring the need for embedded sensors during 20–33 kW pulls.[^459]
[^18]: SmartDisplay dashboards expose per-motor phase amps, traction-control response, and cloud-shared telemetry while VESC Tool mobile logs require manual battery-current capture.[^460]
[^19]: Desktop input wizard misreads center voltage on one-direction throttles; overriding prompts or using the mobile app preserves brake mapping.[^461]
[^20]: Traction-control or ramp changes can erase throttle calibration on CL350 hardware, forcing repeated setup runs.[^462]
[^21]: Slow ABS overcurrent sparks debate—it can hide poor current tuning yet saves time when observers are hard to dial on high-power builds.[^463]
[^22]: Hitting “pairing done” on mobile locks administrators out until they update VESC Tool and clear the flag manually.[^464]
[^hp-fw-failure]: FW-induced cutoffs have spiked components and “killed everything” when riders pushed 37 A of FW into Little Focer/Tronic 250 stacks.
  - treat FW as a last resort with ample battery headroom.[^465]
[^hp-detection]: Makerbase/Flipsky auto-detection still misreports inductance and resistance by triple-digit percentages, so veterans measure with trusted instruments before riding.[^466]
[^23]: Builders combine molded cell holders, 3D-printed guides, and flexible glues to keep parallel groups serviceable.[^467]
[^24]: Copper busbars under nickel require ≥1 kA welders; suppliers like Peng Chen ship 0.5 mm combs for neat 20 S 10 P layouts.[^468]
[^25]: DIY spot welders and KWeld kits need quality LiPo/capacitor packs to avoid overheated leads; Malectrics + LiPo setups succeed on copper builds.[^469]
[^26]: Aggressive braking/wheelies crack Zero/Nami stems at cable cutouts, prompting solid aluminum or 15 mm steel replacements.[^470]
[^dragy]: Dragy GPS timers remain the community benchmark for launch data.
  - stock Segway GT2 logs sit around 4.1 s to 30 mph while dual-ESC builds hit ≈3.2 s when traction is optimized.[^471]
[^27]: Mechanical brakes with lock washers + blue Loctite provide fail-safe stopping; round-profile tires aid cornering but demand careful bead seating to prevent vibration.[^472]
[^28]: High-speed stability relies on positive trail and stiff bearings; dampers alone mask geometry problems and can fail under stiff springs.[^473]
[^29]: Theft prevention advice centers on ≥10 mm hardened chains, welded steel eyelets, and recessed fasteners to defeat cordless tools.[^474]
[^30]: Daly/YXP charger LEDs alternating red/green near full charge indicate normal balancing—no rewiring needed.[^475]
[^31]: GTK 0–102 V adjustable supplies and 120 V bench PSUs offer cheaper wide-voltage charging alternatives at ≈3 A defaults.[^476]
[^32]: Laotie packs sag 8 V under load and can overheat even with 60 A Daly BMS units, so monitor voltage drop and plan upgrades before raising limits.[^477]
[^qs8_norm]: Dual-controller Kelly builds now standardise on QS8 antisparks because XT90S resistors overheat from the inrush current on high-power harnesses.[^478]
[^kelly_signal]: Shops re-pin Kelly throttle/key looms with sealed JST/HiGo connectors to stabilise dual-controller signal splits.[^479]
[^pack_validation]: High-discharge validation workflow covering 20 S11 P enclosure dimensions, preferred cell chemistries, and ANT 300 A BMS trip data near 690 A.[^480]
[^marketing_physics]: Continuous power and pack-mass calculations debunking 150 km/h and 150 km range marketing promises.
  - expect 26–27 kW cruise draw and ≥11 kg of cells.[^481]
[^fw_vsett]: Real-world 16 S VSETT 10 logs showing 30 A field-weakening per motor only added ~8 km/h while boosting draw from 4 kW to 7 kW.[^482]
[^custom_12fet]: Boutique 12‑FET controller project targeting 200 A battery / 300 A phase with NCEP85T14 MOSFETs and remote NTC probes; Wolf King GT validation planned once 250/250R hubs land.[^483]
[^pane_ntc]: Ametherm PANE253411 25 kΩ thermistor sourcing tip to replace inconsistent AliExpress sensors for reliable VESC temperature readings.[^484]
[^ble_diag]: BLE error diagnosis workflow.
  - verify RX/TX polarity, protection resistors, and MCU UART before replacing modules when the app reports "couldn't read firmware version."[^485]
[^multimeter]: Large-screen budget multimeters can work once converted to lithium packs, but Uni‑T handhelds remain the trusted standard for high-voltage and capacitance checks without brownouts.[^486]
[^voltage_parallel]: Debate over 10 S10 P vs. 20 S5 P packs showing ~20 % efficiency difference at 25 km/h while acknowledging aero drag dominates at higher speed.[^487]
[^chassis_damper]: Riders fighting Blade and Vsett wobble still rely on motorcycle-grade dual dampers and admit scooter suspension parts lag moto quality even on triple-digit builds.[^488]
[^bms_margin]: BMS cutoff failures when VESC voltage limits sat flush with pack voltage, prompting a ≥5 V safety margin.[^489]
[^fake_pack]: Counterfeit 52 V “Panasonic” packs testing at ~30 Ah despite 35 Ah labels, requiring weight and weld inspections before approval.[^490]
[^makerx_ntc]: MakerX thermistors misreported temperatures until crews reflashed VESC Tool 6.0 with corrected coefficients, avoiding false throttling/shutdowns.[^491]
[^gt_gusset]: Segway GT and SNSC frames cracking near controller pockets after impacts, leading to gusset welding and accessory weight reviews.[^492]
[^bench_supply]: Telecom-derived 100 V/45 A bench supplies ship without earth bonding or precharge, so techs now ground the chassis and energise AC before connecting packs.[^493]
[^xiaomi_trim]: Xiaomi/Ninebot chargers can be trimmed to ≈61.5 V with pot adjustments but require capacitor upgrades and manual disconnects at high voltage.[^494]
[^deck_seal]: Shops now silicone battery bays and deck seams after seeing water pool around controllers when the cavities weren’t sealed.[^495]
[^water_recovery]: Water-intrusion drill.
  - kill power, open the deck, dry with forced air and IPA, then reseal with silicone once electronics test good.[^496]
[^33]: Tronic X12, Ubox 240, and Spintend 85250 tuning envelopes, including 331 A MOSFET limits and typical 150–200 A battery / 310–360 A phase guardrails.[^497][^498]
[^34]: Field-weakening gains plateauing on 20×70 kV builds after adding 25 A of FW current.[^499]
[^laotie-es19]: Laotie ES19 wobble stems from front swingarm play and bargain shocks; riders retorque the hardware, upgrade suspension, and brace the stem before attempting 80 km/h runs.[^500]
[^35]: PTFE sleeving tips for 6 mm² leads plus AWG 11 silicone upgrades to keep hubs cool on Sevillian climbs.[^501][^502]
[^36]: Parallel-pack lessons covering voltage matching, regen budgeting, and the need to leave charge MOSFETs enabled for braking performance.[^503][^504]
[^37]: CAN telemetry aggregation behaviour and the value of Voyage/Ambrosini dashboards for per-controller diagnostics.[^505]
[^lfocer_limits]: Little FOCer and Tronic 250 guardrails.
  - 100 A battery, 250 A phase (≈300 A absolute), ≤45 A FW
  - and the role of water ingress in past failures.[^506]
[^lfocer-random]: Compact Little FOCer/Tronic boards still suffer random boot failures according to Jan and Face de Pin Sucé, pushing builders toward MP2, Spintend, or refreshed CL350 hardware for reliable 100 × 120 × 25 mm swaps.[^507]
[^alu-75100-phase]: Fresh Makerbase 75100 Alu boards have failed moments after increasing phase current from 175 A to 185 A, reinforcing the narrow headroom on six-FET hardware.[^508]
[^dual-75100-can]: Budget commuters run paired Makerbase 75100 Alu controllers on CAN with a single throttle to avoid unreliable dual ESCs while staying under 22 S.[^509]
[^ampacity_warning]: High-current wiring anecdotes noting 8 AWG harness heating at ~150 A and 2.5 mm² leads melting inside hubs until upgraded to 4–6 mm² silicone cable.[^510][^511]
[^bms-bypass]: Disconnected BMS boards let parallel Xiaomi packs drift into 0 V cells even with periodic manual balancing.
  - leave supervision hardware in-circuit for long-term health.[^512]
[^75100-jitter]: Makerbase 75100 Alu controllers can show severe duty ripple above ~80 % until flashed with Jake’s experimental `fsesc_75_200_alu_sample2` firmware that matches their hardware quirks.[^513]
[^shunt-mismatch]: High-speed ABS overcurrent faults on shunt-modded controllers disappeared only after undoing the mismatch or reverting firmware, proving the need for matched current sensing when targeting 350 A phase pulls.[^514]
[^mp2-abs]: MP2/Tronic builders reported ABS cut-outs past ≈95 % duty even on conservative tunes and now cap duty until firmware fixes land.[^515]
[^mihail_filter]: Mihail’s aluminium-PCB controller uses a GD32F405, dense 0402 filtering, and €2 NRF51 modules, but it demands hot-plate busbar soldering, cool housings (<50 °C), and microscope assembly.[^516]
[^phase_routing]: Upsizing 75/90 H motor leads means flattening 5–6 mm² conductors, stripping jackets, staggering splices, and adding spacers instead of drilling axles or stuffing bulky silicone jackets that pinch bends.[^517]
[^75x200_boot]: Makerbase 75×200 owners flash the Generic bootloader with a battery connected, load the 6.02 `FSESC_75_200_ALU` binary via “custom file,” then disable phase filters after detection to quiet idle chatter.[^518]
[^config_clone]: Veterans warn against cloning someone else’s configuration.
  - rerun detection and set unique ABS/current limits to avoid runaway amps or oscillations.[^519]
[^zvf_heat]: Raising zero-vector frequency toward 25–35 kHz cooled saturated motors slightly but also increased FET heat, so riders log controller temps during experiments.[^520]
[^75x200_repair]: Refurbishing Flipsky/Makerbase 75×200 boards means hot-plate heating of the aluminium base, diode-checking every MOSFET, replacing phases with matched parts, and reinstalling missing bulk capacitance before reassembly.[^521]
[^75100_epoxy]: Photos of newer 75100 batches revealed epoxy patch wires bridging a missed analog VCC trace, reinforcing the habit of inspecting every controller before installation.[^522]

## Late-2022 Field Updates (input_part003 lines 301–400)

### High-discharge pack validation workflow

1. Size the enclosure (≈485 × 210 × 86 mm for 20 S11 P) around high-discharge cells such as P42A, P45B, 40T, or 50S and reject 50G under heavy loads.[^523]
2. Validate marketing claims by calculating the power needed for targets like 150 km/h cruising (≈26–27 kW) and checking pack mass so spec sheets stay honest.[^524][^525]
3. Bench-test BMS cutoff delays and log phase-current spikes.
  - ANT 300 A boards tripped near 690 A, prompting hardware swaps or timer tweaks before top-speed pulls.[^526]
4. Stage thermal runs (street, hill, track) to document when ferrofluid, forced air, or extra copper mass is mandatory before lifting controller limits.[^527][^528]
5. Treat 30 S ambitions as an enclosure and insulation problem first—bigger ESCs, fast fuses, and reinforced sleeving are mandatory, and even Smart Express CAN peripherals struggled with noise above 20 S.[^thirty_s_pack]

### Controller handling & bench safety refreshers

- Disconnect packs before soldering or inspection.
  - a live Makerbase 75200 caught fire mid-rework and reset expectations for “quick” tweaks.[^529]
- Strip factory paste, inspect pads, and reapply thread-lock on enclosure screws so vibration doesn’t loosen service covers.[^529]
- When Y-splitting dual Kelly harnesses, leave horns and lights on dedicated battery/DC-DC feeds so controller rails don’t brown out during regen or horn hits.[^530][^531]
- Cap absolute current around 300 A on Flipsky 75100-class hardware until more long-term data clears higher thresholds.[^532]
- Heat pipes still beat deck-mounted water loops on scooters; Rosheee, Jan, and Paolo keep steering 15 kW builds toward passive conduction because plumbing vibrates loose and chews up deck space.[^heat_pipe_shift_hp]

### Telemetry & validation workflow reminders

1. Pair Dragy hardware with sprint sessions for third-party-verified acceleration data before sharing public claims.[^533]
2. Align logs on VESC Tool 6.0 (desktop or sideloaded Android APK) so configuration exports and diagnostics match across the team.[^534]
3. Layer SmartDisplay overlays only after confirming CAN message maps.
  - Segway GT dashboards deviate from M365 conventions and need bespoke mapping.[^535][^536]

### Failure watchlist additions

- Makerbase aluminum-board clones still shatter MOSFETs once absolute current clears ≈450–500 A; any log past the 300 A consensus deserves teardown.[^532]
- MakerBoard/MakerBase copies routinely ship with poor thermal-pad contact.
  - redo paste coverage and torque checks or expect overheating; recent arrivals showed patchy TIM that left MOSFETs semi-floating until the owners scraped and repasted the base plate.[^537][^maker_clone_tim]
- Spin-Y batch‑1 throttles need the 1 mm magnet spacer retrofit to remove the dead zone; flag early units still missing the fix.[^538]
- Traction-control surges have destroyed Tronic dual setups, including a front-ESC fire after DC/DC contamination.
  - treat post-cleaning inspections as mandatory.[^539][^540]
- Keep VESC input-voltage limits ~5 V above max pack voltage to avoid BMS-induced MOSFET failures during over-voltage faults.[^541]
- Counterfeit 52 V 35 Ah packs delivered only ~30 Ah.
  - audit weight, welds, and discharge logs before trusting “Panasonic”-branded bricks.[^542]
- French riders already forced replacements on “35 Ah Panasonic” packs that only delivered ~30 Ah at 2 A—validate supplier claims before committing them to 20 S racing builds.[^french_pack_recall]
- Segway GT and SNSC frames have fractured at controller mounts; add welded gussets and reconsider handlebar-mounted battery weight on those chassis.[^543]
- Wolf GT electronics bays still swallow only a single Flipsky without spacers—plan taller decks or staged mounting when chasing dual-controller conversions.[^wolf_packaging]
- Xiaomi conversions hanging Ubox singles inside the deck need drilled mounts, threaded inserts, and dedicated bucks for 5 V tail lights to keep harnesses tidy.[^xiaomi_mount]
- MakerX thermistors misreported temps until firmware coefficients were corrected in VESC Tool 6.0.
  - flash updates or risk unwarranted throttling and shutdowns.[^544]
- MakerX duals continue to show high attrition: waterlogged singles only returned after reflashing Jaykup firmware and powering BLE boards from the comm rail, fresh duals blew MOSFETs on the first launch, and shop owners report ~70 % DOA rates that pushed them toward Spintend singles.[^makerx_rescue][^makerx_attrition]

### High-current tuning highlights

- Abandon six-phase “dual cable” experiments—PWM harmonics destabilised controllers until riders reverted to single heavy-gauge phases.[^545]
- 135–200 A phase tests on 16 S packs exposed traction loss above 70 km/h and 100 °C stator spikes; add sensors and traction control before chasing 300 A bursts.[^546][^547]
- LLT/JBD, ANT, and JK smart BMS units remain the shortlist for 150–300 A builds.
  - JK’s short-circuit resilience stands out, but keep B‑ leads short with stout busbars on 20 S layouts.[^548][^549]
- Retune observers and PID after voltage jumps (48 V→60 V) to stop phase-current overshoot and ABS overcurrent faults.[^550]
- Vedder’s 45° V0 HFI profile on firmware 6.0 enabled full-torque launches without halls on hub motors.
  - plan UBOX trials and filter audits before deleting sensor harnesses.[^551]
- Ortega observers stabilised high-ERPM pulls once hall detection was rerun, sensorless ERPM limits raised toward 10 000, and PWM frequency balanced for heat versus smoothness.[^552][^553]
- Follow the Ortega stabilization playbook.
  - flash firmware, run 10 A hall detection, copy realtime rotor angles into PID offsets, and reset ERPM/interpolation defaults to eliminate Blade 1200 W shudder on UBOX singles.[^554]
- Xiaomi dash Lisp scripts chew 25–30 % MCU load and can drop throttle when PWM stays at 30 kHz.
  - cap switching frequency or move to native firmware for the single’s MCU.[^555][^556]
- Expect generic hall throttles to saturate around 4.2 V despite 5 V rails.
  - Spin-Y remaps to 0–3.3 V for MCUs that demand lower ceilings.[^557]
- Traction-control tests on G30 builds doubled MOSFET temps (30 °C→70 °C); keep slip budgets tight or drop TC on high-speed pulls without refined phase caps.[^558][^559]
- Flattening the 75/300 aluminum base, adding paste, and clamping to 10 mm plate let one sample hold 300 A phase/100 A battery with 454 A peaks at 42 °C.
  - remember the stats screen sums dual VESC currents unless you split logs.[^560]
- Open-loop duty-cycle tests dumped ~7.8 kW into a Rage Mechanics prototype coil and burned it.
  - limit current and duration during duty experiments.[^561]
- Dropping zero-vector frequency toward 16–25 kHz cools VESCs and restores low-end torque but can heat motors.
  - log temps before locking in low-PWM tunes.[^562]
- Duty ceilings of ~96–98 % with 35–50 A of field-weakening remain the late-September sweet spot; FW still carries efficiency and thermal penalties at top speed.[^563][^564]
- MP2 builders are hot-plate soldering busbars with CRST030N10N FETs, debating 8–10 AWG phases, 7 mm bullets, and AS150 battery plugs to survive 300 A pulls.[^565][^566]
- Thermal interface math shows 0.03 mm Kapton with paste only matches 0.5 mm pads near 4 W/mK when surfaces are perfectly flat.
  - most MP2 builders still order premium pads for headroom.[^567]
- 20 S riders eyeing 24 S upgrades debated scarce 125 V TO-220 parts versus higher-Rds(on) 150 V MOSFETs; consensus favours extra voltage margin when targeting 20–30 kW pulls.[^568]

### Mechanical integration cues

- Monorim/Flipsky retrofits need fresh RL/flux detection, healthy 20 S packs, correct dash firmware, and Lisp scripts via PC to avoid filter damage.[^569]
- Add inner cable-relief washers, safety spacers, and ~16 mm arm bends when fitting 10×3 in tires; source 23×8 mm (or sanded 25×8 mm) RockShox bushings and swap stamped caliper adapters for machined steel/M6 hardware.[^570][^571]
- Double-check pole-pair and wheel-diameter entries before free-spin tests.
  - bad telemetry can shred hubs; confirm speeds with GPS before trusting high-RPM numbers.[^572]
- Custom 6 mm stainless Monorim adapters triple stiffness versus aluminium plates and replace flimsy Dualtron-style brackets on G30 conversions.[^573]
- Seal decks proactively and, after immersion, dry with heat/rice plus IPA scrubs before corrosion lifts components.[^574][^575]
- Blade GT+ waterproofing tips: sparing RTV on cable glands, no extra grease on used bearings, avoid insulating sprays that trap heat, and use 704 silicone as a thin gasket to keep Blade/Ninebot hubs weather-ready.[^576]

[^75100_fragile]: Non-aluminium Makerbase 75100 enclosures continue to desolder FETs at ~450 A phase / 300 A battery despite firmware tweaks, pushing riders toward aluminium cases or higher-tier controllers.[^577]
[^75200_blow]: JPPL’s 75200 build logged 350–370 A phase spikes per wheel before every MOSFET failed after stacking high-current sampling, MTPA, and a 600 A absolute limit on 20 S packs; hard BMS cuts finished the stage within milliseconds.[^578]
[^param-reset]: Makerbase 75100 owners have seen regen and wattage limits reset to 500–700 W until reflashing firmware and verifying writes on fresh hardware, hinting at flash wear.[^579]
[^regen-only]: A 20 kW scooter run exclusively on regen overheated controllers quickly, reinforcing that at least one mechanical brake must remain in service.[^580]
[^charger-risk]: A refurbished Meanwell-based adjustable charger leaked ~60 VAC to its case because of cold solder joints, tripping RCDs and proving the value of new industrial supplies over refurb gambles.[^581]
[^phase-filter]: Spintend’s phase-filter checkbox should only be enabled during the detection wizard.
  - leaving it on in service reintroduces noise and ABS overcurrent faults.[^582]
[^abs-reset]: Flipsky 75100 ABS overcurrent recoveries required matched bootloader/firmware flashes, sensible detection limits, and the slow ABS limiter before faults cleared.[^583]
[^38]: Risks of powder-coating hub shells at ≈204 °C cure temperatures and the preference for high-temp paint or ceramic coatings.[^584]
[^39]: Ennoid MK8 reliability chatter, including the need for IPTC017N12NM6 MOSFET swaps to reach 26 S/500 A envelopes.[^585]
[^40]: Waterproofed 18-FET G300 controllers delivering ~250 A battery / 500 A phase bursts on 22 S while overheating under sustained regen, signalling sprint-oriented use cases.[^586]
[^g300_ceiling]: 🇪🇸AYO#74 and Face de Pin Suce logged G300 saturation above ~320 A phase on 22 S packs, prompting racers to revert to 3Shul C350 hardware for full torque headroom.[^587]
[^spintend-85150]: Spintend’s light 85/150 is built entirely on 100 V-rated components and has already failed at 20 S when Paolo stacked high-kV hubs with MTPA and FW.
  - treat Huayi-sourced MOSFET swaps or a controller upgrade as mandatory if you need more headroom.[^588]
[^41]: Spintend discontinued the 85/250 and now ships 85/240 controllers through a New Jersey hub, letting U.S. builders avoid tariffs while planning alternatives for higher-rated boards.[^589][^590]
[^vsett-airflow]: Dual 16 S7 P Samsung 50E builds capped phase current at ~70 A per controller and mounted ducted fans up front to stay inside the pack’s ≈140 A battery comfort zone.[^591]
[^wolfwarrior-ducts]: Wolf Warrior riders pushing 120 A battery / 440 A phase on sealed decks logged MOSFET heat rise until they added ducted cooling or backed off current.[^592]
[^headset]: Steering-stability guidance emphasising lightly snug head bearings to prevent wobble and premature failure even when using motorcycle-grade dampers.[^593]
[^wolfx_headset]: Wolf Warrior X owners found the center stem screw over-tightened with dry bearings, requiring disassembly, grease, and careful retorque before the front end freed up.[^594]
[^wolfx_bms]: Wolf Warrior X owners worried about the sealed stock BMS now crack the deck and manually probe parallel-group voltages until a telemetry upgrade is installed.[^595]
[^laotie]: Laotie-style steering tube failures and the recommendation to reinforce with chromoly TIG welding borrowed from motorsport roll-cage practices.[^596]
[^spintend_toggle]: Smart Repair’s Spintend bridge experiments showed that one-button 1WD/2WD toggles require CAN or power isolation; otherwise the secondary controller stays awake and mirrors the primary’s current draw.[^597][^598]
[^fault-logging]: ABS overcurrent recoveries now start with the `faults` command and a higher absolute-current ceiling so observers stop tripping during high-phase pulls.[^599][^600]
[^wiring-bundle]: Harness-simplification lessons from riders replacing dual-phase spaghetti looms with single 8–10 AWG leads terminated near the motor to cut resistive joints and random cut-outs.[^601]
[^logging-workflow]: Android 11+ hides VESC Tool logs under `Android/data/vedder.vesctool/files`; builders now export via TCP bridge or file managers like XFolder before sealing decks for wet-weather riding.[^602]
[^brake-data]: High-speed brake testing shows 3 mm Magura MDR-P rotors with MT7 calipers sustain 2 g stops, whereas 1.8 mm bicycle discs warp.
  - log braking runs with Dragy/GPS before claiming upgrades beat the benchmark.[^603]
[^high-kv]: Paolo’s 43 kV Rion hubs cooked a VESC 75/200; he now favours Kelly or Sabvoton controllers capable of ≥250 A phase for high-KV launches.[^604]
[^dual-motor]: Dual-motor efficiency discussions warn that disabling the front hub drags more than it saves; riders stage compliance modes by zeroing front phase current via CAN when police check scooters.[^605]
[^spintend-single]: Spintend’s single-channel preview needs active cooling above ~30–50 A and targets ≈100 A with a fan in an XT90-sized case priced near $150 once anodized enclosures arrive.[^606]
[^regen-baseline]: Baseline regen setup notes pegging rear wheels around −30 A battery/−80 A phase and fronts near −25 A/−55 A to avoid controller faults during hard braking.[^607]
[^regen-heat]: Regen tests on a 10 S 2 P P42A pack logging 2.55 kW bursts and rapid motor/MOSFET heating, reinforcing stator temperature logging when upping negative current.[^regen-baseline][^sag-logging]
[^sag-logging]: Riders export VESC Tool CSV/XLS files after hill climbs to graph pack sag before retuning current limits.[^608]
[^can-sync]: Rowan’s 4WD build blew a Ubox CAN transceiver when the controllers were powered at different times, pointing to reverse-polarity paths without synchronized wake-ups.[^spintend-single][^can-cite]
[^delta-leads]: Delta rewinds require double the phase amps for equal torque, so uprated hub leads are mandatory before flipping the termination.[^delta-cite]
[^can-cite]: Separate power-ups on linked Uboxes can back-feed CAN and kill transceivers—keep switch timing aligned or add isolation relays.[^609]
[^delta-cite]: Delta-wound hub experiments hitting 70 km/h+ highlighted the need for heavier leads before swapping from star to delta to avoid cooked windings.[^610]
[^artem-sizing]: Artem’s launch heuristic ties phase current to motor wattage ÷ 10 and caps battery current near two-thirds of that value, trimming battery amps whenever phase is raised for harder launches.[^611]
[^daly-behaviour]: Daly smart BMS units ignore remote-off commands, latch MOSFETs after deep sag, and can flip charge FETs during regen, forcing resets via the Bluetooth app and reliance on external antisparks.[^612][^613]
[^boosted-logs]: Small hubs run hot quickly.
  - a 750 W Boosted Rev on a single Ubox climbed to 55 °C controller / 80 °C stator within eight minutes at 120 A phase / 80 A battery, and regen bursts add ~5 °C more to the windings.[^614]
[^magnet-entry]: Accurate telemetry depends on entering actual magnet counts and compressed wheel diameter in VESC Tool; GPS traces lag too much for launch analysis.[^615]
[^sensorless-hfi]: Sensorless Spintend riders confirm near-hall launches once HFI is tuned with ≥15 % Ld/Lq separation via `measure_ind`, leaving only a faint start-up whine.[^616]
[^fw-usage]: Firmware 5.3 beta adds roughly 8 km/h using field weakening at ~20 A extra draw, but crews only enable it above cruising speed to avoid extra heat when packs are sagging.[^617]
[^kaabo-sag]: Rosheee’s Wolf logs showed twin Uboxes pulling ~150 A and dropping the stock 16 S5 P pack about 15 V despite 60 A limits, motivating connector and chemistry upgrades toward P42A/P45B/50S options.[^618][^619]
[^rider-safety]: Helmets with ECE 22.05/22.06 certification and MIPS-style liners remain the minimum; riders keep lighting subtle and reserve “police mode” or field-weakening bursts for brief compliance, not daily cruising.[^620]
[^denis-ubox]: Riders comparing Spintend Ubox and Flipsky controllers highlighted Ubox’s stronger MOSFETs and cooling headroom; early units benefit from thicker thermal pads, and 14 S Samsung 30Q/40T packs hold ≈70 A battery draw if motor limits are respected.[^621]
[^makerbase-75200-fade]: Source: knowledge/notes/input_part013_review.md†L706-L706
[^y11-motor-limit]: Source: knowledge/notes/input_part013_review.md†L803-L803
[^ubox-6fet-failure]: Source: knowledge/notes/input_part013_review.md†L804-L804
[^backup-controller]: Source: knowledge/notes/input_part013_review.md†L806-L806
[^yisuntrek-packaging]: Source: knowledge/notes/input_part013_review.md†L812-L812
[^dampers-budget]: Source: knowledge/notes/input_part013_review.md†L809-L809
[^yisuntrek-stem]: Source: knowledge/notes/input_part013_review.md†L829-L829
[^kaabo-vs-nami]: Source: knowledge/notes/input_part013_review.md†L713-L713
[^rion-inspection]: Source: knowledge/notes/input_part013_review.md†L716-L716
[^ly-rim-qc]: Source: knowledge/notes/input_part013_review.md†L717-L717
[^pothole-teardown]: Source: knowledge/notes/input_part013_review.md†L741-L744


## References

[^1]: Source: knowledge/notes/input_part002_review.md†L140-L141
[^2]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11337-L11435
[^3]: Source: data/vesc_help_group/text_slices/input_part003.txt†L7212-L7235
[^4]: Source: knowledge/notes/input_part009_review.md†L353-L354
[^5]: Source: knowledge/notes/input_part012_review.md†L115-L115
[^6]: Source: knowledge/notes/input_part005_review.md†L399-L400
[^7]: Source: knowledge/notes/input_part007_review.md†L340-L344
[^8]: Source: data/vesc_help_group/text_slices/input_part013.txt†L17329-L17333
[^9]: Source: knowledge/notes/input_part013_review.md†L301-L303
[^10]: Source: knowledge/notes/input_part005_review.md†L413-L417
[^11]: Source: data/vesc_help_group/text_slices/input_part002.txt†L22890-L22924
[^12]: Source: knowledge/notes/input_part005_review.md†L248-L248
[^13]: Source: knowledge/notes/denis_all_part02_review.md†L479-L480
[^14]: Source: knowledge/notes/input_part005_review.md†L419-L424
[^15]: Source: knowledge/notes/input_part001_review.md†L44-L44
[^16]: Source: data/vesc_help_group/text_slices/input_part001.txt†L9423-L9452
[^17]: Source: knowledge/notes/input_part011_review.md†L291-L295
[^18]: Source: data/vesc_help_group/text_slices/input_part013.txt†L5254-L5271
[^19]: Source: knowledge/notes/input_part013_review.md†L31-L31
[^20]: Source: knowledge/notes/input_part008_review.md†L305-L305
[^tronic_can_doas]: Source: knowledge/notes/input_part008_review.md†L419-L420
[^ubox_a6_diode]: Source: knowledge/notes/input_part008_review.md†L428-L429
[^fw_runaway]: Source: knowledge/notes/input_part008_review.md†L311-L311
[^gt2_pack]: Source: knowledge/notes/input_part008_review.md†L312-L312
[^mxlemming_thermal]: Source: knowledge/notes/input_part008_review.md†L313-L313
[^21]: Source: knowledge/notes/input_part013_review.md†L47-L47
[^22]: Source: knowledge/notes/input_part013_review.md†L101-L101
[^23]: Source: knowledge/notes/input_part013_review.md†L66-L66
[^24]: Source: knowledge/notes/input_part013_review.md†L114-L114
[^25]: Source: knowledge/notes/input_part013_review.md†L217-L218
[^26]: Source: knowledge/notes/input_part013_review.md†L255-L257
[^27]: Source: knowledge/notes/input_part013_review.md†L292-L292
[^28]: Source: data/vesc_help_group/text_slices/input_part013.txt†L9779-L9788
[^29]: Source: data/vesc_help_group/text_slices/input_part013.txt†L10402-L10404
[^30]: Source: data/vesc_help_group/text_slices/input_part013.txt†L15507-L15540
[^31]: Source: data/vesc_help_group/text_slices/input_part013.txt†L10221-L10233
[^32]: Source: knowledge/notes/input_part013_review.md†L183-L184
[^33]: Source: data/vesc_help_group/text_slices/input_part013.txt†L6163-L6176
[^34]: Source: data/vesc_help_group/text_slices/input_part013.txt†L6333-L6334
[^35]: Source: data/vesc_help_group/text_slices/input_part013.txt†L6654-L6684
[^36]: Source: data/vesc_help_group/text_slices/input_part013.txt†L5655-L5658
[^37]: Source: data/vesc_help_group/text_slices/input_part013.txt†L6488-L6493
[^38]: Source: knowledge/notes/input_part013_review.md†L219-L219
[^39]: Source: knowledge/notes/input_part013_review.md†L247-L247
[^40]: Source: knowledge/notes/input_part013_review.md†L362-L367
[^41]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8824-L8828
[^42]: Source: data/vesc_help_group/text_slices/input_part001.txt†L9584-L9623
[^43]: Source: knowledge/notes/input_part008_review.md†L32-L35
[^44]: Source: knowledge/notes/input_part008_review.md†L115-L115
[^45]: Source: knowledge/notes/input_part008_review.md†L116-L116
[^46]: Source: data/vesc_help_group/text_slices/input_part013.txt†L18312-L18333
[^47]: Source: data/vesc_help_group/text_slices/input_part013.txt†L18402-L18418
[^48]: Source: knowledge/notes/denis_all_part02_review.md†L354-L355
[^49]: Source: knowledge/notes/input_part005_review.md†L373-L381
[^50]: Source: data/vesc_help_group/text_slices/input_part009.txt†L9746-L9760
[^51]: Source: data/vesc_help_group/text_slices/input_part009.txt†L9765-L9775
[^52]: Source: data/vesc_help_group/text_slices/input_part009.txt†L15383-L15455
[^53]: Source: data/vesc_help_group/text_slices/input_part009.txt†L6008-L6036
[^54]: Source: data/vesc_help_group/text_slices/input_part009.txt†L12555-L12557
[^55]: Source: data/vesc_help_group/text_slices/input_part009.txt†L135-L138
[^56]: Source: knowledge/notes/input_part012_review.md†L343-L343
[^57]: Source: knowledge/notes/input_part012_review.md†L116-L116
[^58]: Source: knowledge/notes/input_part005_review.md†L210-L214
[^59]: Source: knowledge/notes/input_part011_review.md†L365-L370
[^60]: Source: knowledge/notes/input_part005_review.md†L214-L214
[^61]: Source: knowledge/notes/input_part014_review.md†L18-L22
[^62]: Source: data/vesc_help_group/text_slices/input_part002.txt†L9327-L9334
[^63]: Source: knowledge/notes/input_part012_review.md†L268-L272
[^64]: Source: knowledge/notes/input_part012_review.md†L119-L119
[^65]: Source: knowledge/notes/input_part012_review.md†L120-L120
[^66]: Source: knowledge/notes/input_part014_review.md†L11-L18
[^67]: Source: knowledge/notes/input_part014_review.md†L53-L55
[^68]: Source: data/vesc_help_group/text_slices/input_part004.txt†L2294-L2294
[^69]: Source: knowledge/notes/input_part004_review.md†L29-L29
[^70]: Source: knowledge/notes/input_part004_review.md†L301-L305
[^71]: Source: knowledge/notes/input_part003_review.md†L85-L85
[^72]: Source: knowledge/notes/input_part008_review.md†L42-L42
[^73]: Source: data/vesc_help_group/text_slices/input_part010.txt†L17364-L17397
[^74]: Source: data/vesc_help_group/text_slices/input_part010.txt†L17405-L17406
[^75]: Source: data/vesc_help_group/text_slices/input_part004.txt†L20282-L20349
[^76]: Source: data/vesc_help_group/text_slices/input_part009.txt†L11818-L11920
[^77]: Source: data/vesc_help_group/text_slices/input_part004.txt†L8396-L8410
[^78]: Source: data/vesc_help_group/text_slices/input_part004.txt†L2467-L2509
[^79]: Source: data/vesc_help_group/text_slices/input_part004.txt†L4133-L4139
[^80]: Source: data/vesc_help_group/text_slices/input_part004.txt†L10970-L10979
[^81]: Source: data/vesc_help_group/text_slices/input_part004.txt†L11298-L11338
[^82]: Source: data/vesc_help_group/text_slices/input_part004.txt†L11040-L11077
[^83]: Source: data/vesc_help_group/text_slices/input_part004.txt†L11160-L11197
[^84]: Source: knowledge/notes/input_part004_review.md†L117-L117
[^85]: Source: data/vesc_help_group/text_slices/input_part004.txt†L8942-L8968
[^86]: Source: data/vesc_help_group/text_slices/input_part004.txt†L7577-L7678
[^87]: Source: data/vesc_help_group/text_slices/input_part004.txt†L7771-L7787
[^88]: Source: data/vesc_help_group/text_slices/input_part004.txt†L7797-L7810
[^89]: Source: knowledge/notes/input_part008_review.md†L46-L46
[^90]: Source: knowledge/notes/input_part008_review.md†L125-L125
[^91]: Source: knowledge/notes/input_part008_review.md†L265-L265
[^92]: Source: knowledge/notes/input_part008_review.md†L266-L267
[^93]: Source: data/vesc_help_group/text_slices/input_part009.txt†L12011-L12033
[^94]: Source: knowledge/notes/input_part004_review.md†L209-L209
[^95]: Source: knowledge/notes/input_part008_review.md†L47-L47
[^96]: Source: knowledge/notes/input_part010_review.md†L211-L213
[^97]: Source: knowledge/notes/input_part012_review.md†L118-L118
[^98]: Source: knowledge/notes/input_part012_review.md†L263-L268
[^99]: Source: knowledge/notes/input_part012_review.md†L117-L118
[^100]: Source: knowledge/notes/input_part012_review.md†L141-L141
[^101]: Source: knowledge/notes/input_part012_review.md†L143-L143
[^102]: Source: knowledge/notes/input_part012_review.md†L146-L146
[^103]: Source: knowledge/notes/input_part012_review.md†L269-L277
[^104]: Source: knowledge/notes/input_part012_review.md†L277-L279
[^105]: Source: knowledge/notes/input_part014_review.md†L55-L55
[^106]: Source: knowledge/notes/input_part014_review.md†L56-L56
[^107]: Source: data/vesc_help_group/text_slices/input_part014.txt†L10507-L10586
[^108]: Source: data/vesc_help_group/text_slices/input_part014.txt†L10587-L10605
[^109]: Source: data/vesc_help_group/text_slices/input_part014.txt†L10603-L10606
[^110]: Source: data/vesc_help_group/text_slices/input_part014.txt†L10636-L10663
[^111]: Source: data/vesc_help_group/text_slices/input_part014.txt†L10618-L10630
[^112]: Source: data/vesc_help_group/text_slices/input_part001.txt†L20423-L20465
[^113]: Source: data/vesc_help_group/text_slices/input_part010.txt†L11561-L11602
[^114]: Source: knowledge/notes/input_part001_review.md†L650-L651
[^115]: Source: data/vesc_help_group/text_slices/input_part002.txt†L9360-L9395
[^116]: Source: knowledge/notes/input_part011_review.md†L141-L148
[^117]: Source: knowledge/notes/input_part011_review.md†L463-L471
[^118]: Source: knowledge/notes/input_part011_review.md†L439-L440
[^119]: Source: knowledge/notes/input_part010_review.md†L45-L45
[^120]: Source: knowledge/notes/input_part009_review.md†L315-L318
[^121]: Source: knowledge/notes/input_part009_review.md†L318-L318
[^122]: Source: data/vesc_help_group/text_slices/input_part009.txt†L16520-L16560
[^123]: Source: data/vesc_help_group/text_slices/input_part009.txt†L16291-L16308
[^124]: Source: knowledge/notes/input_part010_review.md†L220-L222
[^125]: Source: knowledge/notes/input_part010_review.md†L222-L222
[^126]: Source: knowledge/notes/input_part009_review.md†L391-L391
[^127]: Source: knowledge/notes/input_part009_review.md†L371-L371
[^128]: Source: knowledge/notes/input_part010_review.md†L231-L232
[^129]: Source: knowledge/notes/input_part010_review.md†L234-L236
[^130]: Source: knowledge/notes/input_part010_review.md†L305-L307
[^131]: Source: knowledge/notes/input_part011_review.md†L199-L206
[^132]: Source: knowledge/notes/denis_all_part02_review.md†L341-L342
[^133]: Source: knowledge/notes/input_part010_review.md†L225-L226
[^134]: Source: knowledge/notes/input_part010_review.md†L250-L251
[^135]: Source: data/vesc_help_group/text_slices/input_part009.txt†L14260-L14272
[^136]: Source: data/vesc_help_group/text_slices/input_part009.txt†L17045-L17053
[^137]: Source: data/vesc_help_group/text_slices/input_part009.txt†L14905-L14949
[^138]: Source: data/vesc_help_group/text_slices/input_part009.txt†L15183-L15190
[^139]: Source: knowledge/notes/input_part010_review.md†L228-L229
[^140]: Source: knowledge/notes/input_part011_review.md†L420-L421
[^141]: Source: knowledge/notes/input_part011_review.md†L421-L421
[^142]: Source: knowledge/notes/input_part011_review.md†L444-L445
[^143]: Source: knowledge/notes/input_part011_review.md†L456-L457
[^144]: Source: knowledge/notes/input_part011_review.md†L508-L513
[^145]: Source: knowledge/notes/input_part010_review.md†L272-L273
[^146]: Source: knowledge/notes/input_part010_review.md†L317-L319
[^147]: Source: data/vesc_help_group/text_slices/input_part009.txt†L15391-L15405
[^148]: Source: data/vesc_help_group/text_slices/input_part010.txt†L17460-L17471
[^149]: Source: data/vesc_help_group/text_slices/input_part010.txt†L17410-L17422
[^150]: Source: knowledge/notes/input_part010_review.md†L275-L277
[^151]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8720-L8768
[^152]: Source: data/vesc_help_group/text_slices/input_part001.txt†L12400-L12615
[^153]: Source: data/vesc_help_group/text_slices/input_part001.txt†L20401-L20464
[^154]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8290-L8418
[^155]: Source: knowledge/notes/input_part001_review.md†L589-L590
[^156]: Source: data/vesc_help_group/text_slices/input_part001.txt†L2735-L2806
[^157]: Source: knowledge/notes/input_part001_review.md†L88-L88
[^158]: Source: knowledge/notes/input_part002_review.md†L154-L157
[^159]: Source: data/vesc_help_group/text_slices/input_part000.txt†L18931-L18955
[^160]: Source: data/vesc_help_group/text_slices/input_part000.txt†L19204-L19233
[^161]: Source: knowledge/notes/input_part000_review.md†L720-L737
[^162]: Source: knowledge/notes/input_part000_review.md†L738-L744
[^163]: Source: knowledge/notes/input_part000_review.md†L747-L754
[^164]: Source: data/vesc_help_group/text_slices/input_part009.txt†L20432-L20475
[^165]: Source: knowledge/notes/input_part012_review.md†L372-L372
[^166]: Source: knowledge/notes/input_part007_review.md†L420-L420
[^167]: Source: knowledge/notes/input_part007_review.md†L524-L524
[^168]: Source: knowledge/notes/input_part005_review.md†L121-L121
[^169]: Source: knowledge/notes/input_part005_review.md†L122-L122
[^170]: Source: knowledge/notes/input_part005_review.md†L66-L67
[^171]: Source: knowledge/notes/input_part007_review.md†L490-L491
[^172]: Source: knowledge/notes/input_part006_review.md†L113-L113
[^173]: Source: knowledge/notes/input_part006_review.md†L116-L116
[^174]: Source: knowledge/notes/input_part007_review.md†L491-L491
[^175]: Source: knowledge/notes/input_part012_review.md†L321-L321
[^176]: Source: knowledge/notes/input_part007_review.md†L531-L531
[^177]: Source: knowledge/notes/input_part007_review.md†L492-L492
[^178]: Source: knowledge/notes/input_part012_review.md†L392-L392
[^179]: Source: knowledge/notes/input_part012_review.md†L393-L394
[^180]: Source: knowledge/notes/input_part012_review.md†L394-L394
[^181]: Source: knowledge/notes/input_part012_review.md†L445-L447
[^182]: Source: knowledge/notes/input_part012_review.md†L373-L373
[^183]: Source: knowledge/notes/input_part012_review.md†L448-L448
[^184]: Source: knowledge/notes/input_part012_review.md†L411-L413
[^185]: Source: knowledge/notes/input_part012_review.md†L316-L316
[^186]: Source: knowledge/notes/input_part012_review.md†L413-L414
[^187]: Source: knowledge/notes/input_part012_review.md†L451-L455
[^188]: Source: knowledge/notes/input_part007_review.md†L429-L429
[^189]: Source: knowledge/notes/input_part004_review.md†L312-L315
[^190]: Source: knowledge/notes/input_part004_review.md†L312-L313
[^191]: Source: data/vesc_help_group/text_slices/input_part004.txt†L11438-L11445
[^192]: Source: knowledge/notes/input_part012_review.md†L315-L315
[^193]: Source: knowledge/notes/input_part012_review.md†L435-L435
[^194]: Source: knowledge/notes/input_part006_review.md†L36-L38
[^195]: Source: knowledge/notes/input_part000_review.md†L610-L612
[^196]: Source: data/vesc_help_group/text_slices/input_part009.txt†L20442-L20448
[^197]: Source: data/vesc_help_group/text_slices/input_part001.txt†L11220-L21516
[^198]: Source: knowledge/notes/input_part001_review.md†L653-L655
[^199]: Source: knowledge/notes/input_part001_review.md†L555-L556
[^200]: Source: data/vesc_help_group/text_slices/input_part001.txt†L5231-L5284
[^201]: Source: knowledge/notes/input_part001_review.md†L595-L596
[^202]: Source: data/vesc_help_group/text_slices/input_part001.txt†L7532-L7600
[^203]: Source: knowledge/notes/input_part005_review.md†L311-L320
[^204]: Source: knowledge/notes/input_part008_review.md†L15872-L15884
[^205]: Source: knowledge/notes/input_part008_review.md†L611-L614
[^206]: Source: knowledge/notes/input_part005_review.md†L259-L259
[^207]: Source: data/vesc_help_group/text_slices/input_part001.txt†L20518-L20539
[^208]: Source: data/vesc_help_group/text_slices/input_part001.txt†L10630-L11043
[^209]: Source: data/vesc_help_group/text_slices/input_part001.txt†L21222-L21238
[^210]: Source: data/vesc_help_group/text_slices/input_part001.txt†L7100-L7125
[^211]: Source: data/vesc_help_group/text_slices/input_part001.txt†L9063-L9299
[^212]: Source: data/vesc_help_group/text_slices/input_part001.txt†L20441-L20488
[^213]: Source: data/vesc_help_group/text_slices/input_part001.txt†L21612-L21658
[^214]: Source: data/vesc_help_group/text_slices/input_part001.txt†L10421-L10520
[^215]: Source: data/vesc_help_group/text_slices/input_part001.txt†L9140-L9158
[^216]: Source: knowledge/notes/input_part006_review.md†L329-L329
[^217]: Source: knowledge/notes/input_part006_review.md†L332-L338
[^218]: Source: knowledge/notes/input_part006_review.md†L434-L434
[^219]: Source: knowledge/notes/input_part001_review.md†L661-L662
[^220]: Source: knowledge/notes/input_part001_review.md†L663-L663
[^221]: Source: data/vesc_help_group/text_slices/input_part000.txt†L17390-L17416
[^222]: Source: knowledge/notes/input_part010_review.md†L120-L122
[^223]: Source: knowledge/notes/input_part010_review.md†L122-L122
[^224]: Source: knowledge/notes/input_part004_review.md†L212-L212
[^225]: Source: data/vesc_help_group/text_slices/input_part009.txt†L22070-L22074
[^226]: Source: knowledge/notes/input_part004_review.md†L301-L302
[^227]: Source: knowledge/notes/input_part004_review.md†L323-L324
[^228]: Source: knowledge/notes/input_part005_review.md†L250-L250
[^229]: Source: knowledge/notes/input_part004_review.md†L320-L320
[^230]: Source: data/vesc_help_group/text_slices/input_part001.txt†L10887-L11025
[^231]: Source: data/vesc_help_group/text_slices/input_part009.txt†L6354-L6356
[^232]: Source: data/vesc_help_group/text_slices/input_part009.txt†L6483-L6490
[^233]: Source: data/vesc_help_group/text_slices/input_part009.txt†L10709-L10723
[^234]: Source: data/vesc_help_group/text_slices/input_part001.txt†L6003-L6013
[^235]: Source: data/vesc_help_group/text_slices/input_part001.txt†L6414-L6436
[^236]: Source: knowledge/notes/input_part001_review.md†L516-L518
[^237]: Source: knowledge/notes/input_part001_review.md†L520-L522
[^238]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8463-L8518
[^239]: Source: knowledge/notes/input_part001_review.md†L531-L533
[^240]: Source: data/vesc_help_group/text_slices/input_part001.txt†L10364-L11252
[^241]: Source: knowledge/notes/input_part001_review.md†L586-L587
[^242]: Source: knowledge/notes/input_part001_review.md†L574-L575
[^243]: Source: data/vesc_help_group/text_slices/input_part001.txt†L11140-L11216
[^244]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8601-L8786
[^245]: Source: knowledge/notes/input_part000_review.md†L614-L617
[^246]: Source: knowledge/notes/input_part006_review.md†L343-L343
[^247]: Source: knowledge/notes/input_part000_review.md†L701-L704
[^248]: Source: knowledge/notes/input_part000_review.md†L617-L678
[^249]: Source: knowledge/notes/input_part011_review.md†L339-L357
[^250]: Source: knowledge/notes/input_part011_review.md†L322-L333
[^251]: Source: data/vesc_help_group/text_slices/input_part000.txt†L17166-L17186
[^252]: Source: knowledge/notes/input_part008_review.md†L38-L38
[^253]: Source: knowledge/notes/input_part008_review.md†L39-L39
[^254]: Source: knowledge/notes/input_part008_review.md†L40-L40
[^255]: Source: knowledge/notes/input_part008_review.md†L43-L43
[^256]: Source: knowledge/notes/input_part008_review.md†L44-L44
[^257]: Source: data/vesc_help_group/text_slices/input_part001.txt†L20946-L20947
[^258]: Source: knowledge/notes/input_part013_review.md†L305-L309
[^259]: Source: knowledge/notes/input_part011_review.md†L538-L538
[^260]: Source: knowledge/notes/input_part011_review.md†L280-L287
[^261]: Source: knowledge/notes/input_part011_review.md†L360-L366
[^262]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21480-L21499
[^263]: Source: knowledge/notes/input_part013_review.md†L112-L112
[^264]: Source: knowledge/notes/input_part013_review.md†L115-L115
[^265]: Source: knowledge/notes/input_part004_review.md†L158-L158
[^266]: Source: knowledge/notes/input_part003_review.md†L116-L116
[^267]: Source: knowledge/notes/input_part003_review.md†L124-L124
[^268]: Source: knowledge/notes/input_part004_review.md†L395-L397
[^269]: Source: knowledge/notes/input_part008_review.md†L41-L41
[^270]: Source: knowledge/notes/input_part008_review.md†L103-L105
[^271]: Source: knowledge/notes/input_part008_review.md†L126-L126
[^272]: Source: knowledge/notes/input_part008_review.md†L127-L127
[^273]: Source: knowledge/notes/input_part008_review.md†L129-L129
[^274]: Source: knowledge/notes/input_part008_review.md†L120-L120
[^275]: Source: knowledge/notes/input_part008_review.md†L200-L200
[^276]: Source: knowledge/notes/input_part013_review.md†L185-L185
[^277]: Source: knowledge/notes/denis_all_part02_review.md†L489-L490
[^278]: Source: data/vesc_help_group/text_slices/input_part001.txt†L7166-L7194
[^279]: Source: knowledge/notes/input_part003_review.md†L150-L150
[^280]: Source: knowledge/notes/input_part003_review.md†L190-L190
[^281]: Source: data/vesc_help_group/text_slices/input_part001.txt†L7351-L7415
[^282]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21762-L21770
[^283]: Source: data/vesc_help_group/text_slices/input_part010.txt†L11403-L11448
[^284]: Source: data/vesc_help_group/text_slices/input_part010.txt†L11412-L11419
[^285]: Source: data/vesc_help_group/text_slices/input_part010.txt†L11438-L11459
[^286]: Source: data/vesc_help_group/text_slices/input_part001.txt†L9973-L10014
[^287]: Source: data/vesc_help_group/text_slices/input_part001.txt†L6990-L7058
[^288]: Source: data/vesc_help_group/text_slices/input_part001.txt†L7003-L7028
[^289]: Source: knowledge/notes/input_part006_review.md†L417-L417
[^290]: Source: knowledge/notes/input_part006_review.md†L418-L418
[^291]: Source: knowledge/notes/input_part006_review.md†L412-L412
[^292]: Source: knowledge/notes/input_part008_review.md†L268-L268
[^293]: Source: data/vesc_help_group/text_slices/input_part010.txt†L10117-L10119
[^294]: Source: data/vesc_help_group/text_slices/input_part010.txt†L11185-L11229
[^295]: Source: knowledge/notes/input_part012_review.md†L45-L45
[^296]: Source: knowledge/notes/input_part012_review.md†L46-L46
[^297]: Source: knowledge/notes/input_part012_review.md†L156-L156
[^298]: Source: knowledge/notes/input_part005_review.md†L228-L229
[^299]: Source: knowledge/notes/input_part005_review.md†L305-L312
[^300]: Source: knowledge/notes/input_part005_review.md†L422-L425
[^301]: Source: knowledge/notes/input_part013_review.md†L128-L128
[^302]: Source: knowledge/notes/input_part005_review.md†L418-L419
[^303]: Source: knowledge/notes/input_part003_review.md†L30-L31
[^304]: Source: knowledge/notes/input_part003_review.md†L31-L32
[^305]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24552-L24554
[^306]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24123-L24169
[^307]: Source: knowledge/notes/input_part005_review.md†L249-L249
[^308]: Source: knowledge/notes/input_part011_review.md†L309-L317
[^309]: Source: knowledge/notes/input_part011_review.md†L391-L393
[^310]: Source: knowledge/notes/input_part011_review.md†L367-L368
[^311]: Source: knowledge/notes/input_part011_review.md†L334-L335
[^312]: Source: knowledge/notes/input_part011_review.md†L429-L437
[^313]: Source: knowledge/notes/input_part012_review.md†L47-L47
[^314]: Source: knowledge/notes/input_part012_review.md†L228-L231
[^315]: Source: data/vesc_help_group/text_slices/input_part001.txt†L25425-L25518
[^316]: Source: knowledge/notes/input_part010_review.md†L215-L217
[^317]: Source: knowledge/notes/input_part010_review.md†L293-L294
[^318]: Source: data/vesc_help_group/text_slices/input_part001.txt†L25469-L25490
[^319]: Source: knowledge/notes/input_part007_review.md†L323-L325
[^320]: Source: knowledge/notes/input_part007_review.md†L325-L327
[^321]: Source: knowledge/notes/input_part007_review.md†L332-L335
[^322]: Source: knowledge/notes/input_part006_review.md†L64-L64
[^323]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11187-L11187
[^324]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11745-L11759
[^325]: Source: knowledge/notes/input_part003_review.md†L734-L736
[^326]: Source: data/vesc_help_group/text_slices/input_part009.txt†L10494-L10515
[^327]: Source: data/vesc_help_group/text_slices/input_part009.txt†L12968-L12970
[^328]: Source: knowledge/notes/input_part003_review.md†L238-L239
[^329]: Source: knowledge/notes/input_part003_review.md†L240-L241
[^330]: Source: knowledge/notes/input_part008_review.md†L269-L269
[^331]: Source: knowledge/notes/input_part010_review.md†L296-L297
[^332]: Source: data/vesc_help_group/text_slices/input_part003.txt†L16419-L16455
[^333]: Source: knowledge/notes/input_part007_review.md†L344-L348
[^334]: Source: data/vesc_help_group/text_slices/input_part003.txt†L16593-L16605
[^335]: Source: data/vesc_help_group/text_slices/input_part003.txt†L17403-L17413
[^336]: Source: data/vesc_help_group/text_slices/input_part003.txt†L17498-L17503
[^337]: Source: data/vesc_help_group/text_slices/input_part003.txt†L21805-L21824
[^338]: Source: data/vesc_help_group/text_slices/input_part003.txt†L23563-L23653
[^339]: Source: data/vesc_help_group/text_slices/input_part010.txt†L20034-L20062
[^mantis-controller-proof]: Source: knowledge/notes/input_part010_review.md†L702-L703
[^340]: Source: knowledge/notes/input_part008_review.md†L228-L228
[^341]: Source: knowledge/notes/input_part012_review.md†L22-L22
[^342]: Source: knowledge/notes/input_part012_review.md†L26-L26
[^343]: Source: knowledge/notes/input_part008_review.md†L229-L229
[^344]: Source: knowledge/notes/input_part007_review.md†L340-L343
[^345]: Source: knowledge/notes/input_part007_review.md†L343-L347
[^346]: Source: knowledge/notes/input_part007_review.md†L347-L352
[^347]: Source: knowledge/notes/input_part007_review.md†L352-L356
[^348]: Source: knowledge/notes/input_part007_review.md†L356-L358
[^349]: Source: knowledge/notes/input_part007_review.md†L358-L360
[^350]: Source: knowledge/notes/input_part007_review.md†L360-L362
[^351]: Source: knowledge/notes/input_part007_review.md†L362-L364
[^352]: Source: knowledge/notes/input_part010_review.md†L362-L363
[^353]: Source: knowledge/notes/input_part010_review.md†L362-L364
[^354]: Source: data/vesc_help_group/text_slices/input_part010.txt†L10739-L10759
[^355]: Source: knowledge/notes/input_part008_review.md†L365-L368
[^356]: Source: knowledge/notes/input_part005_review.md†L301-L304
[^357]: Source: data/vesc_help_group/text_slices/input_part005.txt†L21883-L21905
[^358]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21194-L21218
[^359]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21749-L21756
[^360]: Source: data/vesc_help_group/text_slices/input_part009.txt†L22034-L22072
[^361]: Source: knowledge/notes/input_part008_review.md†L368-L368
[^362]: Source: data/vesc_help_group/text_slices/input_part010.txt†L10528-L10551
[^363]: Source: knowledge/notes/input_part010_review.md†L302-L303
[^364]: Source: data/vesc_help_group/text_slices/input_part003.txt†L20945-L21000
[^365]: Source: knowledge/notes/input_part006_review.md†L413-L413
[^366]: Source: knowledge/notes/input_part006_review.md†L414-L414
[^367]: Source: knowledge/notes/input_part006_review.md†L411-L411
[^368]: Source: data/vesc_help_group/text_slices/input_part010.txt†L10370-L10376
[^369]: Source: data/vesc_help_group/text_slices/input_part010.txt†L10386-L10394
[^370]: Source: knowledge/notes/input_part012_review.md†L192-L192
[^371]: Source: knowledge/notes/input_part012_review.md†L295-L299
[^372]: Source: knowledge/notes/input_part012_review.md†L299-L300
[^373]: Source: knowledge/notes/input_part012_review.md†L127-L127
[^374]: Source: knowledge/notes/input_part012_review.md†L132-L132
[^375]: Source: knowledge/notes/input_part012_review.md†L134-L134
[^376]: Source: knowledge/notes/input_part012_review.md†L133-L133
[^377]: Source: knowledge/notes/input_part012_review.md†L30-L30
[^378]: Source: knowledge/notes/input_part004_review.md†L138-L138
[^379]: Source: knowledge/notes/input_part005_review.md†L349-L355
[^380]: Source: data/vesc_help_group/text_slices/input_part009.txt†L20036-L20043
[^381]: Source: data/vesc_help_group/text_slices/input_part009.txt†L20505-L20518
[^382]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21996-L22002
[^383]: Source: data/vesc_help_group/text_slices/input_part009.txt†L22058-L22072
[^384]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21268-L21279
[^385]: Source: knowledge/notes/input_part004_review.md†L139-L140
[^386]: Source: data/vesc_help_group/text_slices/input_part002.txt†L11269-L11298
[^387]: Source: knowledge/notes/input_part004_review.md†L33-L33
[^388]: Source: knowledge/notes/input_part004_review.md†L36-L36
[^389]: Source: knowledge/notes/input_part004_review.md†L141-L141
[^390]: Source: knowledge/notes/input_part004_review.md†L271-L271
[^391]: Source: data/vesc_help_group/text_slices/input_part009.txt†L13508-L13516
[^392]: Source: data/vesc_help_group/text_slices/input_part009.txt†L13527-L13534
[^393]: Source: knowledge/notes/input_part005_review.md†L320-L330
[^394]: Source: data/vesc_help_group/text_slices/input_part005.txt†L22861-L22880
[^395]: Source: data/vesc_help_group/text_slices/input_part005.txt†L23881-L23888
[^396]: Source: knowledge/notes/input_part005_review.md†L365-L373
[^397]: Source: knowledge/notes/input_part005_review.md†L333-L337
[^398]: Source: knowledge/notes/input_part005_review.md†L337-L339
[^399]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24715-L24725
[^400]: Source: data/vesc_help_group/text_slices/input_part013.txt†L6526-L6533
[^401]: Source: knowledge/notes/input_part005_review.md†L328-L330
[^402]: Source: data/vesc_help_group/text_slices/input_part001.txt†L20680-L20760
[^403]: Source: data/vesc_help_group/text_slices/input_part009.txt†L20406-L20423
[^404]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21250-L21257
[^405]: Source: data/vesc_help_group/text_slices/input_part009.txt†L20578-L20599
[^406]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21252-L21257
[^407]: Source: knowledge/notes/input_part001_review.md†L52-L52
[^408]: Source: knowledge/notes/input_part007_review.md†L364-L366
[^409]: Source: knowledge/notes/input_part001_review.md†L76-L78
[^410]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24537-L24568
[^411]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24552-L24565
[^412]: Source: data/vesc_help_group/text_slices/input_part001.txt†L8211-L8253
[^413]: Source: data/vesc_help_group/text_slices/input_part001.txt†L9208-L10216
[^414]: Source: data/vesc_help_group/text_slices/input_part009.txt†L18575-L18576
[^415]: Source: data/vesc_help_group/text_slices/input_part001.txt†L21540-L21580
[^416]: Source: knowledge/notes/input_part010_review.md†L117-L118
[^417]: Source: knowledge/notes/input_part001_review.md†L601-L611
[^418]: Source: knowledge/notes/input_part000_review.md†L634-L634
[^419]: Source: data/vesc_help_group/text_slices/input_part000.txt†L17960-L17982
[^420]: Source: knowledge/notes/input_part007_review.md†L452-L452
[^421]: Source: knowledge/notes/input_part007_review.md†L244-L244
[^makerbase_22s_fail]: Source: knowledge/notes/input_part008_review.md†L416-L416
[^cl350_drive_links]: Source: knowledge/notes/input_part008_review.md†L417-L417
[^fardriver_nd72450]: Source: knowledge/notes/input_part008_review.md†L453-L454
[^spintend_85150_rma]: Source: knowledge/notes/input_part008_review.md†L492-L493
[^422]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24287-L24336
[^423]: Source: knowledge/notes/input_part004_review.md†L225-L225
[^424]: Source: knowledge/notes/input_part007_review.md†L242-L242
[^425]: Source: data/vesc_help_group/text_slices/input_part001.txt†L6208-L6233
[^426]: Source: data/vesc_help_group/text_slices/input_part001.txt†L6329-L6336
[^427]: Source: data/vesc_help_group/text_slices/input_part001.txt†L10197-L10268
[^428]: Source: data/vesc_help_group/text_slices/input_part001.txt†L14432-L14456
[^429]: Source: data/vesc_help_group/text_slices/input_part001.txt†L14410-L14423
[^430]: Source: data/vesc_help_group/text_slices/input_part001.txt†L20808-L20858
[^431]: Source: knowledge/notes/input_part005_review.md†L16-L20
[^432]: Source: knowledge/notes/input_part005_review.md†L18-L19
[^433]: Source: knowledge/notes/input_part007_review.md†L161-L161
[^434]: Source: knowledge/notes/input_part007_review.md†L166-L166
[^435]: Source: knowledge/notes/input_part007_review.md†L168-L168
[^436]: Source: knowledge/notes/input_part005_review.md†L164-L169
[^437]: Source: knowledge/notes/input_part005_review.md†L166-L167
[^438]: Source: knowledge/notes/input_part005_review.md†L164-L165
[^439]: Source: knowledge/notes/input_part009_review.md†L345-L347
[^440]: Source: knowledge/notes/input_part009_review.md†L348-L348
[^441]: Source: knowledge/notes/input_part009_review.md†L357-L358
[^442]: Source: knowledge/notes/input_part005_review.md†L155-L157
[^443]: Source: knowledge/notes/input_part005_review.md†L23-L24
[^444]: Source: knowledge/notes/input_part005_review.md†L11-L14
[^445]: Source: knowledge/notes/input_part005_review.md†L12-L13
[^446]: Source: knowledge/notes/input_part005_review.md†L37-L37
[^447]: Source: knowledge/notes/input_part005_review.md†L35-L36
[^448]: Source: knowledge/notes/input_part009_review.md†L350-L376
[^449]: Source: knowledge/notes/input_part005_review.md†L29-L33
[^450]: Source: knowledge/notes/input_part009_review.md†L368-L368
[^451]: Source: knowledge/notes/input_part005_review.md†L25-L25
[^452]: Source: knowledge/notes/input_part005_review.md†L150-L153
[^453]: Source: knowledge/notes/input_part005_review.md†L151-L156
[^454]: Source: knowledge/notes/input_part005_review.md†L156-L158
[^455]: Source: knowledge/notes/input_part005_review.md†L31-L31
[^456]: Source: knowledge/notes/input_part005_review.md†L29-L30
[^457]: Source: knowledge/notes/input_part005_review.md†L55-L55
[^458]: Source: knowledge/notes/input_part005_review.md†L35-L35
[^459]: Source: knowledge/notes/input_part005_review.md†L172-L178
[^460]: Source: knowledge/notes/input_part005_review.md†L179-L183
[^461]: Source: knowledge/notes/input_part005_review.md†L45-L45
[^462]: Source: knowledge/notes/input_part005_review.md†L47-L47
[^463]: Source: knowledge/notes/input_part005_review.md†L50-L50
[^464]: Source: knowledge/notes/input_part005_review.md†L48-L48
[^465]: Source: knowledge/notes/input_part009_review.md†L353-L355
[^466]: Source: knowledge/notes/input_part009_review.md†L358-L360
[^467]: Source: knowledge/notes/input_part005_review.md†L13-L14
[^468]: Source: knowledge/notes/input_part005_review.md†L145-L147
[^469]: Source: knowledge/notes/input_part005_review.md†L189-L191
[^470]: Source: knowledge/notes/input_part005_review.md†L43-L43
[^471]: Source: knowledge/notes/input_part005_review.md†L41-L42
[^472]: Source: knowledge/notes/input_part005_review.md†L123-L134
[^473]: Source: knowledge/notes/input_part005_review.md†L175-L177
[^474]: Source: knowledge/notes/input_part005_review.md†L199-L200
[^475]: Source: knowledge/notes/input_part005_review.md†L26-L26
[^476]: Source: knowledge/notes/input_part005_review.md†L143-L143
[^477]: Source: knowledge/notes/input_part005_review.md†L185-L187
[^478]: Source: knowledge/notes/input_part003_review.md†L311-L312
[^479]: Source: knowledge/notes/input_part003_review.md†L311-L313
[^480]: Source: data/vesc_help_group/text_slices/input_part003.txt†L25501-L25996
[^481]: Source: data/vesc_help_group/text_slices/input_part003.txt†L25568-L26111
[^482]: Source: data/vesc_help_group/text_slices/input_part003.txt†L24684-L24692
[^483]: Source: data/vesc_help_group/text_slices/input_part003.txt†L24837-L24872
[^484]: Source: data/vesc_help_group/text_slices/input_part003.txt†L24381-L24399
[^485]: Source: data/vesc_help_group/text_slices/input_part003.txt†L25051-L25070
[^486]: Source: data/vesc_help_group/text_slices/input_part003.txt†L25059-L25112
[^487]: Source: data/vesc_help_group/text_slices/input_part003.txt†L25001-L25048
[^488]: Source: data/vesc_help_group/text_slices/input_part003.txt†L24873-L24955
[^489]: Source: knowledge/notes/input_part003_review.md†L350-L350
[^490]: Source: knowledge/notes/input_part003_review.md†L351-L351
[^491]: Source: knowledge/notes/input_part003_review.md†L353-L353
[^492]: Source: knowledge/notes/input_part003_review.md†L352-L352
[^493]: Source: knowledge/notes/input_part003_review.md†L301-L301
[^494]: Source: knowledge/notes/input_part003_review.md†L302-L302
[^495]: Source: knowledge/notes/input_part003_review.md†L313-L313
[^496]: Source: knowledge/notes/input_part003_review.md†L335-L338
[^497]: Source: knowledge/notes/input_part013_review.md†L364-L369
[^498]: Source: knowledge/notes/input_part013_review.md†L799-L804
[^499]: Source: knowledge/notes/input_part013_review.md†L29-L31
[^500]: Source: knowledge/notes/input_part001_review.md†L676-L678
[^501]: Source: knowledge/notes/input_part013_review.md†L48-L48
[^502]: Source: knowledge/notes/input_part013_review.md†L190-L191
[^503]: Source: knowledge/notes/input_part013_review.md†L154-L157
[^504]: Source: knowledge/notes/input_part009_review.md†L377-L377
[^505]: Source: knowledge/notes/input_part013_review.md†L186-L186
[^506]: Source: knowledge/notes/input_part004_review.md†L106-L108
[^507]: Source: knowledge/notes/input_part004_review.md†L307-L308
[^508]: Source: knowledge/notes/input_part004_review.md†L219-L220
[^509]: Source: knowledge/notes/input_part004_review.md†L201-L204
[^510]: Source: knowledge/notes/input_part004_review.md†L121-L122
[^511]: Source: knowledge/notes/input_part004_review.md†L177-L178
[^512]: Source: knowledge/notes/input_part004_review.md†L211-L211
[^513]: Source: knowledge/notes/input_part004_review.md†L204-L204
[^514]: Source: knowledge/notes/input_part004_review.md†L232-L232
[^515]: Source: knowledge/notes/input_part004_review.md†L240-L240
[^516]: Source: data/vesc_help_group/text_slices/input_part004.txt†L13601-L13746
[^517]: Source: data/vesc_help_group/text_slices/input_part004.txt†L14873-L14919
[^518]: Source: data/vesc_help_group/text_slices/input_part004.txt†L14938-L14999
[^519]: Source: data/vesc_help_group/text_slices/input_part004.txt†L15164-L15171
[^520]: Source: data/vesc_help_group/text_slices/input_part004.txt†L15642-L15646
[^521]: Source: data/vesc_help_group/text_slices/input_part004.txt†L13664-L14193
[^522]: Source: data/vesc_help_group/text_slices/input_part004.txt†L15303-L15310
[^523]: Source: data/vesc_help_group/text_slices/input_part003.txt†L25501-L25522
[^524]: Source: data/vesc_help_group/text_slices/input_part003.txt†L25567-L25606
[^525]: Source: data/vesc_help_group/text_slices/input_part003.txt†L26039-L26048
[^526]: Source: data/vesc_help_group/text_slices/input_part003.txt†L25905-L26024
[^527]: Source: data/vesc_help_group/text_slices/input_part003.txt†L25766-L25811
[^528]: Source: data/vesc_help_group/text_slices/input_part003.txt†L17013-L17049
[^529]: Source: data/vesc_help_group/text_slices/input_part003.txt†L25812-L25846
[^530]: Source: data/vesc_help_group/text_slices/input_part003.txt†L8427-L8476
[^531]: Source: data/vesc_help_group/text_slices/input_part003.txt†L26056-L26243
[^532]: Source: data/vesc_help_group/text_slices/input_part003.txt†L11641-L11710
[^533]: Source: data/vesc_help_group/text_slices/input_part003.txt†L26407-L26482
[^534]: Source: data/vesc_help_group/text_slices/input_part003.txt†L26572-L26598
[^535]: Source: data/vesc_help_group/text_slices/input_part003.txt†L26364-L26496
[^536]: Source: data/vesc_help_group/text_slices/input_part003.txt†L26600-L26606
[^537]: Source: data/vesc_help_group/text_slices/input_part003.txt†L16244-L16267
[^538]: Source: data/vesc_help_group/text_slices/input_part003.txt†L12202-L12209
[^539]: Source: data/vesc_help_group/text_slices/input_part003.txt†L12565-L12640
[^540]: Source: data/vesc_help_group/text_slices/input_part003.txt†L23300-L23538
[^541]: Source: data/vesc_help_group/text_slices/input_part003.txt†L21224-L21247
[^542]: Source: data/vesc_help_group/text_slices/input_part003.txt†L21032-L21044
[^543]: Source: data/vesc_help_group/text_slices/input_part003.txt†L26560-L26622
[^544]: Source: data/vesc_help_group/text_slices/input_part003.txt†L17564-L17610
[^545]: Source: data/vesc_help_group/text_slices/input_part003.txt†L200-L221
[^546]: Source: data/vesc_help_group/text_slices/input_part003.txt†L685-L748
[^547]: Source: data/vesc_help_group/text_slices/input_part003.txt†L742-L766
[^548]: Source: data/vesc_help_group/text_slices/input_part003.txt†L469-L520
[^549]: Source: data/vesc_help_group/text_slices/input_part003.txt†L1219-L1223
[^550]: Source: data/vesc_help_group/text_slices/input_part003.txt†L853-L906
[^551]: Source: data/vesc_help_group/text_slices/input_part003.txt†L22577-L22606
[^552]: Source: data/vesc_help_group/text_slices/input_part003.txt†L4135-L4190
[^553]: Source: data/vesc_help_group/text_slices/input_part003.txt†L5720-L5736
[^554]: Source: data/vesc_help_group/text_slices/input_part003.txt†L4545-L4620
[^555]: Source: data/vesc_help_group/text_slices/input_part003.txt†L4536-L4549
[^556]: Source: data/vesc_help_group/text_slices/input_part003.txt†L5686-L5689
[^557]: Source: data/vesc_help_group/text_slices/input_part003.txt†L3491-L3516
[^558]: Source: data/vesc_help_group/text_slices/input_part003.txt†L6800-L6829
[^559]: Source: data/vesc_help_group/text_slices/input_part003.txt†L6870-L6871
[^560]: Source: data/vesc_help_group/text_slices/input_part003.txt†L7853-L7884
[^561]: Source: data/vesc_help_group/text_slices/input_part003.txt†L7102-L7141
[^562]: Source: data/vesc_help_group/text_slices/input_part003.txt†L7145-L7164
[^563]: Source: data/vesc_help_group/text_slices/input_part003.txt†L7443-L7457
[^564]: Source: data/vesc_help_group/text_slices/input_part003.txt†L7476-L7500
[^telemetry_crosscheck]: Source: knowledge/notes/input_part003_review.md†L502-L502
[^maker_clone_tim]: Source: knowledge/notes/input_part003_review.md†L520-L520
[^makerx_rescue]: Source: knowledge/notes/input_part003_review.md†L546-L546
[^makerx_attrition]: Source: knowledge/notes/input_part003_review.md†L547-L548
[^heat_pipe_shift_hp]: Source: knowledge/notes/input_part003_review.md†L556-L557
[^thirty_s_pack]: Source: knowledge/notes/input_part003_review.md†L558-L559
[^wolf_packaging]: Source: knowledge/notes/input_part003_review.md†L562-L563
[^xiaomi_mount]: Source: knowledge/notes/input_part003_review.md†L563-L564
[^shul_variants]: Source: knowledge/notes/input_part003_review.md†L567-L567
[^french_pack_recall]: Source: knowledge/notes/input_part003_review.md†L569-L569
[^565]: Source: data/vesc_help_group/text_slices/input_part003.txt†L18051-L18138
[^566]: Source: data/vesc_help_group/text_slices/input_part003.txt†L19431-L19437
[^567]: Source: data/vesc_help_group/text_slices/input_part003.txt†L18841-L18874
[^568]: Source: data/vesc_help_group/text_slices/input_part003.txt†L19332-L19365
[^569]: Source: data/vesc_help_group/text_slices/input_part003.txt†L3600-L3651
[^570]: Source: data/vesc_help_group/text_slices/input_part003.txt†L4248-L4314
[^571]: Source: data/vesc_help_group/text_slices/input_part003.txt†L4256-L4301
[^572]: Source: data/vesc_help_group/text_slices/input_part003.txt†L3678-L3699
[^573]: Source: data/vesc_help_group/text_slices/input_part003.txt†L5766-L5781
[^574]: Source: data/vesc_help_group/text_slices/input_part003.txt†L337-L346
[^575]: Source: data/vesc_help_group/text_slices/input_part003.txt†L446-L449
[^576]: Source: data/vesc_help_group/text_slices/input_part003.txt†L22936-L22975
[^577]: Source: data/vesc_help_group/text_slices/input_part004.txt†L15628-L15699
[^578]: Source: data/vesc_help_group/text_slices/input_part004.txt†L15623-L15690
[^579]: Source: knowledge/notes/input_part004_review.md†L283-L283
[^580]: Source: knowledge/notes/input_part004_review.md†L222-L222
[^581]: Source: knowledge/notes/input_part004_review.md†L207-L207
[^582]: Source: knowledge/notes/input_part004_review.md†L110-L111
[^583]: Source: knowledge/notes/input_part004_review.md†L111-L111
[^584]: Source: knowledge/notes/input_part013_review.md†L147-L147
[^585]: Source: knowledge/notes/input_part014_review.md†L19-L37
[^586]: Source: knowledge/notes/input_part012_review.md†L398-L399
[^587]: Source: knowledge/notes/input_part013_review.md†L415-L416
[^588]: Source: knowledge/notes/input_part008_review.md†L113-L115
[^589]: Source: knowledge/notes/input_part012_review.md†L110-L111
[^590]: Source: knowledge/notes/input_part012_review.md†L379-L405
[^591]: Source: knowledge/notes/input_part001_review.md†L20-L21
[^592]: Source: knowledge/notes/input_part001_review.md†L21-L21
[^593]: Source: knowledge/notes/input_part014_review.md†L42-L42
[^594]: Source: knowledge/notes/input_part014_review.md†L256-L257
[^595]: Source: data/vesc_help_group/text_slices/input_part014.txt†L10583-L10591
[^596]: Source: knowledge/notes/input_part014_review.md†L184-L184
[^597]: Source: knowledge/notes/input_part011_review.md†L317-L317
[^598]: Source: knowledge/notes/input_part011_review.md†L79-L79
[^599]: Source: data/vesc_help_group/text_slices/input_part001.txt†L2840-L2872
[^600]: Source: data/vesc_help_group/text_slices/input_part001.txt†L3796-L3808
[^601]: Source: data/vesc_help_group/text_slices/input_part001.txt†L3260-L3305
[^602]: Source: data/vesc_help_group/text_slices/input_part001.txt†L3440-L4018
[^603]: Source: data/vesc_help_group/text_slices/input_part001.txt†L2891-L3010
[^604]: Source: data/vesc_help_group/text_slices/input_part001.txt†L3820-L3856
[^605]: Source: data/vesc_help_group/text_slices/input_part001.txt†L25184-L25233
[^606]: Source: knowledge/notes/input_part000_review.md†L251-L252
[^spintend-vsett]: Source: knowledge/notes/input_part007_review.md†L404-L404
[^607]: Source: knowledge/notes/input_part000_review.md†L256-L256
[^608]: Source: knowledge/notes/input_part000_review.md†L300-L300
[^609]: Source: knowledge/notes/input_part000_review.md†L234-L234
[^610]: Source: knowledge/notes/input_part000_review.md†L253-L253
[^611]: Source: knowledge/notes/input_part000_review.md†L302-L304
[^612]: Source: knowledge/notes/input_part000_review.md†L315-L316
[^613]: Source: knowledge/notes/input_part000_review.md†L366-L369
[^614]: Source: knowledge/notes/input_part000_review.md†L304-L305
[^615]: Source: knowledge/notes/input_part000_review.md†L326-L328
[^616]: Source: knowledge/notes/input_part000_review.md†L379-L380
[^617]: Source: knowledge/notes/input_part000_review.md†L349-L350
[^618]: Source: knowledge/notes/input_part002_review.md†L180-L181
[^619]: Source: knowledge/notes/input_part002_review.md†L214-L215
[^620]: Source: knowledge/notes/input_part000_review.md†L362-L364
[^621]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L102569-L102598

[^ayo-131]: Source: knowledge/notes/input_part010_review.md†L643-L643
[^log-every-run]: knowledge/notes/input_part010_review.md†L644-L644
