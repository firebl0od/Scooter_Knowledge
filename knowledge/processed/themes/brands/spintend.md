# Spintend Controllers Brand Dossier

## TL;DR

- Community veterans now default to Spintend when budget Makerbase/Flipsky boards melt down—the Ubox lineup shrugs off BMS trips and keeps scooters rolling where 75xxx-class ESCs lock wheels or self-destruct under the same abuse.[^1]
- Ubox V2 hardware now ships with resettable fuses on each auxiliary rail, isolated 3.3 V logic, dedicated 12 V lighting/horn/brake outputs, a fan header, CAN power jumpers for 4WD builds, and an external NRF/BLE slot—removing the need for firmware hacks to stay under the STM32’s logic ceiling.[^1]
- New ALU batches squeeze dual 10 AWG battery leads into a single 8 mm bullet and ship accessory pigtails on tiny keyed connectors, so installs now budget proper crimpers, heavy soldering, or larger bullets to avoid cooking the joint during assembly.[^2]
- NetworkDir even steers budget dual-motor Xiaomi builds toward paired Ubox controllers because Flipsky/Makerbase 75100s keep dying after pack cut-offs—dual Lites have become the reliable mid-tier choice when riders can’t stretch to premium controllers.[^3]
- The legacy dual Ubox remains a 75 V-class workhorse that comfortably feeds roughly 150 A phase per side, while the refreshed single 85 V/240 A shell ships with 8 AWG outputs, reversible exits, and pricing below the outgoing 250 A block—teams are already mixing the new singles with older duals on tight decks.[^dual-75v]
- Riders note that even when undersized hubs fail catastrophically, Spintend’s 100 V Lite shrugged off the shorts—GABE killed three commuter motors in two days without harming the controller, underscoring the brand’s resilience to motor-side faults.[^motor-survival]
- Yamal has already logged roughly 2,500 km hammering 200 A battery/phase on a Spintend build without failures, highlighting how meticulous wiring and conservative validation keep the hardware alive even for heavy daily use.[^4]
- Even with the shared “no limits” firmware, single Ubox installs treat ~80 A battery and 130 A phase as the sensible ceiling—the hardware clamp near 300 A still applies, so cooling and telemetry matter more than chasing the unlocked config file.[^40]
- Face de Pin Sucé’s benching confirms the public 300 A BIN lets stock V2 hardware flirt with ~250 A phase and 420 A ABS in open air, yet Artem still tells sealed-deck riders to cap tunes around 130 A phase unless they upgrade cooling and rubber first.[^5]
- Early 85250 V1 controllers used current-transformer sensing that saturates near 100 A and complicates auto-detection, so Smart Repair now nudges heavy builds toward shunt-based MK8/X12 footprints (or waits for the teased 18-FET refresh) unless the board has been reworked with proven Toll MOSFETs.[^ct_limit]
- Thermal success hinges on treating every Spintend as a passively cooled module: clamp the aluminum base to a 3–5 mm plate with paste or pads and reserve generous deck space for 25 × 15 cm heatsinks so dual stacks stay below ~70 °C.[^2]
- Stock pad stacks combine a 2 mm × 1.1 cm × 9.6 cm strip with a 0.5 mm × 2.4 cm × 9.6 cm shim; swapping to uniform 1 mm sheets with proper clamp pressure has dropped single-Ubox temperatures from 68 °C at 110 A to 49 °C at 142 A on icy rides, underscoring contact pressure over exotic materials.[^6][^7]
- Treat the ADC lighting bridge as an accessory tap, not a main switch—its ~12 V / 3 A rail and updated harnesses simplify pods and brake throttles, but real kill circuits still require relays, smart-BMS buttons, or loop keys.[^3]
- Single-channel Uboxes still omit the 12 V/3 A accessory rail, so plan fused buck converters for headlights and horns instead of hijacking fan headers or the ADC board.[^8]
- Built-in alarms scream if the remote fails to handshake at power-up while still letting the motors drive, so wire brake interlocks or auxiliary sirens if you rely on the feature for theft deterrence.[^9]
- The cost-reduced Ubox V2 quietly swapped 4 A Infineon gate drivers for 1.5 A generics and dropped the BLE board, so sustained high-duty tunes need extra cooling and independent telemetry.[^v2_downgrade]
- Single Ubox lids still mount MOSFETs on the removable cover—treat them as ~30 A continuous hardware unless you add external heatsinks or step up to dual-channel cases for 100 A peaks.[^single_lid_limit]
- Long-haul logs show the controllers outlasting peripherals—throttles and other accessories still fail first even after cleaning factory solder balls, so carry spares and plan quick swaps for track weekends.[^10]
- The compact V100 revision leans on higher-Rdson MOSFETs plus revised copper tracing to shed heat, yet riders still beg for smaller cases, front-facing connectors, integrated Bluetooth, and direct MOSFET-to-heatsink clamps with copper bars.[^11]
- Stock MOSFETs still fail when builders push >40 A of field weakening on 20 S packs; plan on HY- or HSBL-class swaps before chasing high-ERPM targets on 85150/85250 hardware.[^20]
- A fresh wave of 100/100 failures—four units within a year despite 20 S packs capped near 60 A battery and 130 A phase—has veterans advising swaps to alternative controllers instead of gambling on replacements.[^12]
- Random throttle surges continue to surface on 85 V/240 A, 100 V/100 A, and even v2 85 V/250 A units, so budget time for filtering, shielded cabling, and harness inspections when diagnosing jitter complaints.[^17]
- The latest single-board revision lands on an aluminium PCB with G015N10 MOSFETs—stick with the matching gate network instead of improvising swaps or you’ll destabilise the driver stage.[^13]
- Singles without the integrated BLE module reserve the NRF header for Bluetooth because the lone RX/TX pair is often claimed by dashboards or ADC adapters—plan harnesses accordingly.[^14]
- Spintend sunset the 85/250 and now routes the 85/240 through a New Jersey hub for U.S. buyers—stock spares if you rely on the higher-rated board because the replacement is easier to source but capped a touch lower.[^logistics_update]
- Product management is leaning heavily on group feedback—including Russian-language experimenters—to steer new scooter-specific screens and throttle accessories.[^community_feedback]
- The single-channel preview shares twin-Ubox DNA but still needs active cooling above ~30–50 A; expect ≈100 A with a fan, Bluetooth sold separately, and ~$150 pricing once anodised cases ship.[^single_preview]
- Twelve-FET Spintend stacks are still marketed at 400 A but field logs keep them around ~250 A battery / 450 A phase with real heatsinking—riders treat claims of 400 A per side as marketing bravado rather than a daily target.[^15]
- ExpressLine DDP orders are landing in Germany within about a week, but riders still see surprise import invoices even on “duty paid” shipments—budget customs padding despite the expedited route.[^16]
- EU buyers still shoulder VAT and customs surprises on accessories—expect €30 invoices on €20 parcels until Spintend rolls IOSS collection or a prepaid tax option into checkout.[^17]
- DHL eCommerce has stranded multiple RMAs for five weeks and returned singles with recurring capacitor failures, so veteran buyers now film unboxings and pay for FedEx or AliExpress Standard with prepaid VAT despite the surcharge.[^18]
- The V2 sales launch kept MSRP at $300 but deleted onboard Bluetooth to avoid metal-deck interference, making external dongles mandatory for sealed builds and signalling that future cases will stay radio-transparent.[^19]
- Riders are consolidating ADC-board orders after repeated failures and €37 replacement shipping plus on-delivery VAT; some now power throttles straight from the controller’s 3.3 V rail to skip the accessory board entirely.[^20]
- Upcoming aluminum-core singles are on the roadmap: expect fdbl MOSFET options, thicker copper, SH8/6 AWG support, and firmware-locked tiers up to 300 A phase / 150 A battery once production lands.[^21][^22]
- V2 thermal telemetry reads hotter than V1 under the same rides because of NTC placement and extra phase current; reverting to stock pads outperformed fancy Thermal Grizzly swaps, so fix clamp pressure before chasing exotic materials.[^v2_ntc]
- The public 5.3 firmware drop split testers—Spintend support is still telling riders to sit tight on 5.2 until its customised 5.3 binaries soak, while early adopters praise quieter motors; archive configs and logs before experimenting.[^fw53_release]
- V2 boards ship with self-reset fuses on every 5 V/12 V/3.3 V rail, but VESC Tool 3.01 still crashes during ADC calibration if 5 V throttles land on the STM32 input—stick to 3.00/5.2 firmware or add dividers before sealing decks.[^23]

## Inbound QC & Power-Up Protocol

1. **Full teardown and dry clean before first power.** Crack the enclosure, remove conformal covers, vacuum or IPA-wipe solder balls, and inspect gate-driver rails prior to energising the board.[^41]
   - Second-hand single-case uBox controllers have turned up with stray solder balls, uneven MOSFET pad contact, and phase leads chafing through silicone grommets—strip the shell, clean, and add insulation before trusting a resale unit.[^24]
   - Newer housings now fasten with four screws and side-facing ports, but riders still open fresh units to clear stray solder before the first ride.[^25]
- Latest single-channel batches even arrived without all case bolts or with loose solder balls rattling around the shell, so film inspections and demand replacements before installation.[^26]
- Early Ubox 85150 batches shipped with 100 V/100 A silkscreens on the powerstage despite the 85 V/150 A marketing copy; replacement boards reportedly need two new holes drilled because only two of six screws align with the legacy case.[^27]
2. **Torque and upgrade the high-current connectors.** Swap factory XT90 jumpers for QS8/AS150-class hardware or busbars with proper lugs, and route control wiring through shielded CAT6A pairs to avoid melted solder-only links.[^42]
   - Factory Ubox looms ship with XT90 battery tails but only female motor bullets; most builders trim lead length, swap to 5.5 mm connectors, and split power vs. signal looms down opposite deck rails to curb EMI.[^motor_connectors]
3. **Hunt for stray conductive debris.** Rental-fleet autopsies found solder beads bridging phase outputs on dual installs—confirm nothing rattles inside before closing the case.[^43]
4. **Respect symmetric power loops.** When disconnecting packs, pull both battery leads or open the main contactor before touching CAN; popping one lead while the bus is live has blown Ubox Lite ESD protection.[^44]
   - Rowan’s 4WD build cooked a CAN transceiver when controllers were energised separately—power every VESC before plugging in CAN or add isolation relays when singles live in different enclosures.[^28]
5. **Document baseline idle draw.** Expect roughly 20 mA standby current with the latching power button off—any illuminated switch LED signals a wiring fault.[^45]
6. **Capture fault codes before pulling power.** Ubox singles store the last fault until a reboot; pop the deck and read VESC Tool’s terminal over USB before cycling the controller so you do not erase the evidence.[^29]
6. **Plan upstream isolation for singles.** The single-board UBOX still relies on its MOSFET stack as the master switch; there’s no dedicated latch rail to intercept, so add a real contactor, loop key, or smart-BMS disconnect instead of cutting traces or bodging low-voltage relays onto the logic feed.[^30]
- Builders retrofitting keyed ignitions splice the switch in series with the red power-button lead and power dash voltmeters from the battery—expect the display to stay lit until the key cuts pack power.[^31]
7. **Only enable the phase filter during detection.** Spintend confirmed the toggle exists to stabilise the motor wizard; leaving it on while riding injects noise and can resurrect ABS overcurrent faults.[^54]
8. **Check for copper busbars and debris on arrival.** Early 75 V betas exposed copper bars while some 100 V runs hide higher-Rds(on) MOSFETs under resin and ship with loose solder balls—open every case and confirm the busbar stack before trusting marketing photos.[^u75_vs100]
9. **Bench-test current-sense offsets before installation.** Three of four UBOX Single 100/100 boards arrived with shorted op-amps reporting nonsensical offsets (30–4,000 counts), and a working unit blew input capacitors during a routine reconnect—validate sensor readings before trusting controllers in builds.[^qc_input004]
10. **Check Bluetooth harness polarity on fresh Ubox units.** A new 80 V single shipped with its BLE lead reversed, killing the module immediately—verify continuity before power-up.[^bt_polarity]
11. **Repin the single-channel JST harness thoughtfully.** The single Ubox shares its eight-pin header between the ADC throttle board and Bluetooth module—borrow ground from elsewhere and keep UART accessories off the CAN header when you shuffle plugs.[^32]
12. **Lock ADC daughterboard switches before sealing.** The single-channel JST shares the ADC throttle board with Bluetooth; epoxy or tape the 3.3 V/5 V selector so vibration cannot flip it mid-ride and brick the adapter.[^33]
13. **Disable traction control on single-motor installs.** The “anti-slip” flag is for dual builds—leaving it enabled on a lone controller cuts power with red/green blink codes at low speed.[^34]

## Product Line Cheat Sheet

| Model | Nominal Pack Window | Field Envelope & Use Case | Distinguishing Notes |
| --- | --- | --- | --- |
| Dual Ubox 75/100 | 16–20 S | ≈150 A phase per side when cooled properly; duals still popular for compact dual-motor decks | Legacy two-in-one chassis remains a 75 V-class unit that survives racing loads when given airflow.[^4] |
| Ubox Lite (single) | 16–20 S | ≈150 A battery/phase; dual Lite = two singles under one lid | Lite boards share hardware with the dual 100/100, letting riders mix singles or duals to balance heat against mounting simplicity.[^5] |
| Ubox 85/200 (12‑FET) | 18–22 S | 250 A battery / ~350 A phase with cooling; dual stacks log ~500 A combined bursts | Tuners report faults only past ~450 A phase when thermals are dialed in, making the 12‑FET the workhorse for 20–22 S superbikes.[^6] |
| Ubox 85/240 (rev.) | 18–22 S (marketing 24 S with care) | Targeting ~240 A battery in a smaller shell for tight decks | New single-chassis revision ships with 8 AWG leads, reversible exits, and a lower price than the outgoing 250 A model, prompting direct-import demand.[^7] |
| Dual 75/100 (early rev.) | 16–20 S | Needs external filtering for the noisiest installs | First batches omitted phase filters; retrofit boards or external filters tame switching noise on sensitive builds.[^8] |
| Single-board prototype | 16–22 S (target) | Paolo estimates ≈150 A battery on flat roads once firmware stabilises | Current revision is ~60 mm wide without the case, adds capacitance versus a Nucular 12F, and still needs external sealing before living in wet decks.[^single-proto] |
Spintend now colour-codes dual Ubox trims—red prioritises current for commuter tunes, purple adds TVS protection for safer 18 S work, and black pairs with 22 S builds so long as e-brake regen is capped under ~80 V—so log the shell colour before assuming voltage headroom.[^35]

## Spin-Y Control Ecosystem

- Builders continue to ask for clearer Spin-Y wiring and voltage diagrams; Spintend responded with linked manuals, promised improved graphics, and is iterating clamp geometry for 22.2 mm bars with shims and relief cuts.[^36][^37]
- Batch-2 firmware adds OEM controller dead-zone compensation, one-minute calibration, and steadier cruise behaviour, consolidated through a new Spin-Y Facebook group.[^38]
- The Gen2 throttle roadmap doubles useful throw (≈65° drive / 35° regen), adds internal cruise wiring, dead-zone compensation for legacy controllers, longer harness options, and forthcoming textured wheels sized for gloved riders.[^39][^40]
- Adding a 1 mm spacer between magnets and hall sensors removed saturation and shrank dead zones by roughly two-thirds, reinforcing the need for updated calibration guides and retrofit instructions.[^41]

## Operating Guardrails
### Battery & Phase Current Targets

- Stock firmware keeps 85‑250 hardware near 150 A battery / 200 A phase continuous, with seasoned tuners only flashing no-limit binaries once motors and cooling can stomach 400 A phase spikes.[^9]
- Smart Repair’s track-tested window keeps refreshed 85 250/240 stacks reliable around 380 A phase, 480 A absolute, and ~200 A battery once you strip paint, add thermal paste, and clamp the base to added aluminum mass.[^smartrepair_85250]
- The revised 85250 V2 may handle 22 S, but early adopters are still collecting long-term data before trusting race builds at ≈92 V—treat the voltage headroom as experimental until logs prove otherwise.[^42]
- Daily riders now treat 85150s as ~150 A battery / 250 A phase hardware even after flashing the no-limits BIN; pushing harder cooked stock-firmware units within days when regen stayed disabled.[^safe_envelope]
- Tokmas/JMSh1001ATLQ MOSFET swaps let modders pull roughly 160–180 A battery and ~240 A phase from Ubox 85/150 boards, but the higher RDS(on) parts run hotter and the six-FET stage still soft-caps practical phase current around 230–250 A.[^tokmas_swap]
- Front-wheel Thunder builds hold 85150s near 150 A battery / 230 A phase with heavy thermal prep—fresh paste, external heatsinks, optional fans, and temperature limits that taper output before the case nears 96 °C on 120–130 km/h pulls.[^thunder_front85150]
- Firmware on 85/250 hardware still clamps phase around 350 A with only momentary spikes to ~400 A; seasoned tuners keep practical use near 300 A phase to avoid the thermal and reliability penalties.[^43]
- Matthew’s latest logs confirm firmware clamps 85150 phase current around 150 A even when commands call for 180 A with 90 A battery, signalling that ABS limits still need manual tuning if you want more torque headroom.[^44]
- **Single Ubox 100/100 daily safe zone:** Lonnyo 65 H commuters are holding tunes near 130–135 A phase with 85–90 A battery and 150–180 A absolute, trimming duty to ~98 % and starting FW around 88 % to clear residual stutter without climbing past 40 °C case temps.[^u100_daily]
- With upgraded MOT1111T silicon and external cooling, riders have logged ~480 A phase bursts per controller on 85250 stacks—proof the hardware has headroom when thermals are engineered properly.[^hackintosh_burst]
- Field logs from daily 18 S commuters show 85150 hardware getting unhappy above ~240 A phase; trimming tunes to roughly 220 A phase, 90 A battery, and ≈60 A of field weakening kept case temps stable without neutering performance.[^45][^46]
- Real-world logs show dual Lite builds requesting 160/140 A phase yet barely topping 100 A peaks, underscoring the need to capture data from both controllers before chasing higher numbers.[^10]
- Dualtron GT riders running Ubox Lite hardware corroborate those peaks: 55–60 A battery per motor with 160/140 A phase commands only logged ~100 A, offering a realistic ceiling for keeping stock hubs alive at highway pace.[^47]
- Solo commuters copying the shared 300 A hardware-limit BIN still hold tunes near 80 A battery / 130 A phase until they validate heatsinking and airflow; the file only removes software clamps—it does not grant extra headroom.[^40]
- Veterans cap single-channel phase current around 115–125 A until more telemetry lands, noting that even dual Ubox stacks rarely stay clean above ~130 A without short phase leads and strong thermal coupling.[^48]
- Early field testing shows MOSFET temps climbing to ~50 °C within seconds at 50 A battery draw before pack protection intervenes, so validate heatsinking before raising thermal cutbacks above stock.[^rapid_heat]
- Firmware bundles ship in 100 A and 300 A flavours; Smart Repair urges riders to stay on the 100 A pack for warranty support because the higher bin both voids coverage and still bottlenecks battery input near 60 A even when phase currents spike around 147 A.[^firmware-bins]
- Even the new 85/240 single pushes 80 H hubs toward 95 km/h on 22 S, so the smaller shell still demands proper cooling and current discipline before chasing dual-motor-class speeds.[^u85240_speed]
- Heavy riders continue blowing 12‑FET stages even with modest throttle inputs; treat 20 S commuter builds as derated compared with lightweight race scooters and reserve “fat VESC” footprints when riders plus cargo exceed ~120 kg.[^18]
- Start with conservative dual-drive baselines: 17 S builds have settled near 2×120 A phase / 2×90 A battery / 2×180 A absolute, while 16 S commuters ride closer to 2×100 A phase / 2×60 A battery until thermal logs show headroom.[^30]
- Remember the Spintend bridge mirrors battery current to both controllers—profile toggles or 1WD/2WD switches must isolate CAN or power, otherwise the smaller front ESC still sees the rear controller’s amps.[^bridge_mirror]
- Revised single-channel harnesses now sneak 5 V down the CAN umbilical to wake the second controller; confirm accessory loads stay off that pin and inspect new looms for missing case bolts or stray solder before buttoning up.[^26]

### Voltage & Regen Discipline

- Riders stepping into 22 S still back off charge voltage or disable heavy regen to avoid 100 V spike failures that plague 75xxx competitors; Ubox-class controllers tolerate the packs but demand measured braking ramps.[^11]
- Ubox 100/100 revisions still cap regen safely below full pack voltage; Smart Repair warns the stage ships without ST-Link pads or beefy 12 V rails and arrives set around 135 A phase / 180 A absolute until you validate cooling.[^u100_baseline]
- Firmware caps near 300 A phase on early 85/200 units until owners compile the unofficial “no limits” branch—use sparingly because support teams treat it as a warranty break.[^12]
- Early “85/150” beta boards still rely on 100 V components; clamp them to ≥3 mm aluminum baseplates and add sheet-metal spreaders or active airflow if you want ~180 A phase without cooking the stage.[^49]
- Watch for BMS thermal trips even on Spintend hardware—dual Ubox owners running 2×135 A phase / 2×71 A battery still logged pack over-temp around 90 A spikes; monitor pack sag and internal resistance monthly.[^31]
- Size battery groups for the torque you plan: 65 H motors needed roughly 150–200 A battery per side, and undersized parallel packs tripped companion BMSes when regen slammed add-on modules.[^32]
- If battery leads stretch across the frame, bolt low-ESR 470 µF capacitors near the controller input to shield the MCU from back-EMF spikes before they trigger brownouts.[^input_caps]
- Treat BMS cutoffs as glide events, not anchors—Spintend hardware coasts when a pack trips, but trim regen near full charge (≈76.6 V on 20 S) to avoid repeated over-voltage faults.[^1][^33]
- Replacement HY power stages sourced through Raphaël Foujiwara are still capped at ≤20 S (~400 A phase) unless you add his HF filter and cooling mods; even experienced builders with the new boards are holding off on 22 S experiments until thermal issues are solved.[^50][^51]
- 17 S pushes on 75 V units demand extra input capacitance and lower charge cutoffs (~4.1 V per cell) to tame back-EMF spikes—seasoned tuners still recommend staying at 16 S because regen and launches can overvoltage the sparse 220 µF bank even after upgrades.[^52]

### Interfaces & Telemetry

- The single Ubox keeps CAN, Bluetooth, and USB online simultaneously, so you can run diagnostics and accessory modules without swapping cables—just mind idle draw when parking long-term.[^single-can]
- The onboard fan header feeds a thermostatic 12 V rail only; firmware cannot switch it, so tap a constant 12 V source or external buck for lighting mods instead of relying on that header.[^53]
- Beta accessory boards spotted in March bundle addressable LEDs (likely WS2812/WS2815) and a piezo buzzer alongside throttle inputs, signalling that future Spintend harnesses may ship with built-in lighting and alert control instead of relying on third-party strips.[^54]
- Spintend’s BLE hardware remains a boutique accessory—Paolo hand-builds modules for roughly €20 plus shipping while the official AliExpress listing sits near €29, and Flipsky’s mass-produced NRF clone has climbed to ~€40 despite using a €5 core—budget telemetry extras accordingly and expect to flash third-party boards yourself.[^55][^56][^ble_dongle][^ble_required][^missing_ble]
- Keep Bluetooth enabled even on headless builds—experienced 75100 converts lean on wireless tuning and fault pulls because Spintend hardware is impractical to service without logs in the field.[^ble_required]
- Ubox V2 shipments have turned up without the promised Bluetooth module; the UART header expects a 5 V module on RX/TX/GND, so builders either chase replacements or install third-party BLE boards while tracing any noisy ADC rails back to damaged STM32 inputs.[^missing_ble]
- Avoid USB-only tuning on unplugged decks—laptops feeding the USB-C port without pack power have created destructive ground loops, so either power the controller normally or fall back to Bluetooth/Wi-Fi for configuration.[^57]
- Swapping to 10 AWG phase leads now calls for 60–80 W irons and broad tips—portable TS80P pencils can desolder stock 12 AWG but rarely leave clean tin on heavier cable without external heat.[^phase_rework]
- SmartDisplay’s roadmap now includes a “panic button” that flashes legal 125 W/20 km/h limits into connected controllers and a May production target of ~20 simplified enclosures (including central-mount variants), so plan firmware hooks and mounting space if customers expect stealth compliance modes from future Spintend bundles.[^58]

### Field-Weakening & High-Load Limits

- Stock 85150 MOSFETs overheat quickly once you layer 45 A of field weakening on top of 105–120 A battery and 150–175 A phase requests; riders chasing higher ERPMs swap in HY/HSBL Toll packages with hotplate reflow or back FW down to ~50 A at 87 % duty.[^20]
- 85240 hardware is happiest at 20 S—one HY-revision board tolerated 21 S, but pushing to 22 S without auditing supporting components risks the same runaway failures seen on overloaded 12-FET stages.[^22]
- Heavy riders continue blowing 85/250 units even with gentle ramps, so dual-motor “fat VESC” upgrades or derated current ceilings remain the conservative path for >20 S commuters.[^18]

## Thermal & Packaging Playbook

- Mount each ESC against aluminum with thermal compound on both faces; copper spacers are discouraged because corrosion outweighs the modest conductivity gain once you already have aluminum-to-aluminum contact.[^2]
- Retain or improve OEM pad compression—Ubox V2 temperature deltas often trace back to NTC placement and clamp pressure more than exotic pad swaps.[^25]
- Bolt controllers directly to bare metal structure: sand paint, polish deck plates, and clamp the Ubox to aluminum or copper spreaders to hold MOSFETs near 55 °C at 50 A battery / 120 A phase.[^26]
- Maintain pad thickness discipline; thicker thermal replacements have pushed case temps toward 70 °C when compression was lost.[^27]
- Mount 6‑FET minis on 3–5 mm aluminum plates with paste on both faces—copper sandwiches corrode faster than they help once you already couple to aluminum.[^28]
- Share load across dual drives when possible: single-controller hill climbs hit ~60 °C while dual-drive equivalents stay below 40 °C, underscoring the headroom gained by splitting torque.[^29]
- A single 25 × 15 cm heatsink can host two 12‑FET bodies without fin trimming, giving dual builds a repeatable footprint for under-deck cooling plates.[^2]
- Plan airflow and strain relief so BMS cutoffs do not shock the controllers—Spintend hardware coasts through pack trips, but keeping harnesses tidy prevents the upstream faults that still kill rivals.[^1]
- Connector failures still dominate thermal complaints—melted XT90 jumpers on dual Ubox builds traced to soldered bus bars without copper pigtails, so riders now spec QS8/AS150U/QS8H hardware or machined lugs and route low-current controls through shielded CAT6A pairs.[^connector_upgrade]
- Riders logging 67 °C case temps at 50 A battery / 120 A phase cut that to ~55 °C after sanding deck paint, flattening copper spreaders, and re-seating stock pads before bolting the controller straight to bare aluminum.[^case_prep]
- Bonding the 85150 case to the scooter frame with thermal adhesive and watching per-motor temperature logs helps spot miswired phases or sensor faults before they torch a controller.[^21]
- Re-tap the tiny M2.5 bosses or print adapter plates when mounting 85/240 and Lite boards—the flat housings ship without hardware and benefit from thicker pads or thermal glue plus reinforced brackets.[^mounting_threads]
- Repurpose dead 75/200 baseplates as aux heat spreaders—JPPL’s stack adds aluminum spacers and CNC clamps while Shlomozero sketches radiator blocks tied into Dualtron side plates to keep HY power stages cool.[^baseplate_spreader]
- When compression is weak, riders are stacking 0.5 mm stock pads with 1 mm Thermal Grizzly sheets and paste-filling seams—MOSFET peaks fell from ~67 °C at 45 A/110 A to ~61 °C at 50 A/130 A, letting single Ubox builds launch at 150 A phase without faults.[^59]
- Flip the split case so the MOSFET half sits against metal; leaving the logic side down keeps transistors hot while the MCU stays cool, whereas inverted installs share heat with the chassis and stabilize temps.[^60]
- Extreme experiments bolt bare boards to 1 cm aluminum slabs or add copper heat pipes—insulate everything, but expect case temps dropping into the 25–44 °C range at ~110 A phase once the mounting is dialled.[^61][^62]
- Warranty tear-downs should end with fresh pads (up to 1 mm), solder-ball cleanup, and gluing the ADC adapter slide switch in the 5 V position so throttle rails stop flickering after reassembly.[^63]
- JPPL’s X12 installs highlight the packaging ceiling: the accessory rail only delivers 5 V / 150 mA, so plan on a dedicated buck converter if you need 12 V lighting or telemetry alongside the ADC bridge.[^53]
- Water-cooled loops can hold 85250 cores within ~4 °C of ambient at 90 A battery / 130 A phase, yet those builds still suffer tariff-driven price creep and encourage interest in the teased 18‑FET alternative positioned around €180.[^52]

## Wiring & Accessory Integration

- The latest v3 ADC adapter arrives with proper harness plugs; pair it with the documented throttle pinout (3.3 V red, ground black, ADC1 signal) and keep the NRF port free for Bluetooth modules.[^3][^13]
- Budget the ADC rail for light loads only: dual 18 W lamps already stress the ~12 V / 3 A output, so horns, halogens, or RGB kits belong on dedicated DC/DC converters triggered by the adapter or a relay.[^3]
- Budget the ADC rail for light loads only: dual 18 W lamps already stress the ~12 V / 3 A output, so horns, halogens, or RGB kits belong on dedicated DC/DC converters triggered by the adapter or a relay—and Dualtron riders now reserve the rail for brake lights after burning controllers by running both headlight and taillight sets directly.[^64][^3]
- **Hang heavy accessories on an external buck.** A dedicated 12 V/20 A converter powering horns, pumps, fans, and lights only sips ~4–6 A from a 60 V pack, and trimming controller battery amps preserves BMS headroom during horn spikes.[^accessory_buck]
- **Treat ADC2 as logic-only.** Builders are seeing barely an amp of safe headroom on the secondary ADC rail, so horns and 12 V headlights now run off battery-fed relays instead of that logic supply.[^adc2_limit]
- When reusing OEM dashes or switches, add pull-down resistors or relays instead of tying controller 5 V rails together—shared ignition lines without isolation have cooked boards in cramped conversions.[^3]
- The ADC adapter already handles turn-signal strips and Spin dial throttles; use the supplied JST harness for ADC3, calibrate legacy Spin Y pods manually, and keep phase leads equal length when trimming looms.[^23]
- Artem’s upcoming scroll throttle keeps dual-screw clamps, reversible hall direction, selectable 3.3 V/5 V outputs, and a €45–55 target price; beta CNC runs land before the injection-molded release so riders can stop replacing €160 pods every crash.[^65]
- Sequential LED turn signals still require extra logic; riders rewiring looms from scratch report the VESC signal wires cannot drive cascaded strips directly, so plan dedicated controllers if you expect chase effects.[^seq_led]
- If throttle noise persists, compress the ADC window so idle rests near 0.8–1.0 V, verify chassis grounding, and add filtering before blaming firmware for runaway acceleration reports.[^17][^24]
- Leverage the ADC adapter without killing CAN—run ADC1/2 through the splitter while leaving UART dashboards online, and diode-isolate lighting feeds so traction control and telemetry stay intact.[^34]
- Feed auxiliary rails from a clean supply: Ubox Lite lacks a native 12 V rail, so power the ADC adapter from an external DC-DC while keeping grounds common to prevent lighting glitches.[^35]
- Mind standby behaviour before adding smart switches—the latching Spintend button already isolates the logic rail with minimal drain; external anti-spark solutions are optional unless you need hard battery isolation.[^45]

## Common Issues & Troubleshooting

- Voyage dashes can mask low ABS limits—Arnau’s new Voyage-equipped 85 V/150 A controller threw ABS OCP faults immediately until Jason advised connecting with VESC Tool and raising the absolute current ceiling instead of relying on the dash alone.[^66]

### Auto-Off Failures on 100/100 Units

- Some Spintend 100/100 controllers refuse to shut down even when ADC auto-off timers are disabled in VESC Tool, indicating accessory power bleed or stuck logic rails preventing proper shutdown.[^autooff-issue]
- **Troubleshooting steps:**
1. Check for backfeed from auxiliary power sources (displays, lighting, BMS wake circuits) that may be energizing the logic rail.
2. Verify ADC adapter wiring and confirm no pull-up resistors or external circuits are holding the enable pin high.
3. Test with all accessories disconnected to isolate whether peripheral power is preventing shutdown.
4. Consider using smart-BMS discharge control or physical loop keys as backup shutdown methods until root cause is identified.[^autooff-issue]
- Document firmware version, accessory wiring, and ADC adapter configuration when reporting this issue to identify common patterns.[^autooff-issue]

### Spintend Lite Connector Sourcing

- Oreo Huzky's Apollo City Pro conversion highlighted that Spintend Alu Lite logic harnesses use keyed multi-pin plugs that builders must reuse or source when extending looms—part numbers remain undocumented in community threads as of late 2025.[^lite-connector]
- When building or repairing Lite harnesses, photograph factory connectors and measure pin pitch/count before attempting aftermarket substitutes to avoid compatibility issues.[^lite-connector]
- Consider ordering spare connectors directly from Spintend or trusted resellers when planning custom harness work on Lite platforms.[^lite-connector]

## Commissioning & Diagnostics Checklist

1. **Audit firmware limits before tuning.** Confirm the phase ceiling in VESC Tool; early 85/200 units stall at ~300 A until reflashed, and Lite boards mirror duals so mismatched limits skew traction control.[^12][^5]
2. **Flash vendor firmware and let auto-detection pick the hardware profile.** Spintend-supplied BINs and automatic R3 detection remain the safe path; forcing V6 targets or manual overrides has bricked controllers on the bench.[^46]
- The phone app hides alternative firmware once connected—enable “Show non-default firmware” on desktop builds or compile binaries locally before flashing bootloaders over USB.[^67][^68]
3. **Validate motor detection results.** Limited-edition hubs have returned ~270 A recommendations despite ~200 A safe limits, and some Ubox V2 units only auto-detect ~88 A versus ~135 A on V1—log outputs and set limits manually when they drift.[^47][^48]
4. **Disable regen during PSU testing.** Spinning up field-weakening on a bench supply can over-voltage the source; keep regen off until testing on a full battery stack.[^49]
5. **Capture fault codes before power-cycling.** If ABS overcurrent trips during early rides, dump VESC `faults` logs before rebooting so you can correlate spikes with wiring or observer changes.[^50]
6. **Log both controllers on every shakedown.** Aggregate CAN data to verify commanded vs. actual amps; many “weak” builds simply read one side and miss per-motor dropouts.[^10]
7. **Stage regen carefully on 22 S builds.** Drop charge voltage a few volts or cap braking current until you validate pack and controller headroom with logs.[^11]
8. **Inspect phase filters on older duals.** Populate missing components or add external LC filters if noise, thermal, or EMI issues surface on early 75/100 hardware.[^8]
9. **Verify accessory wiring.** Keep lighting loads within the ADC bridge limits and route any kill-switch expectations through smart-BMS logic or physical loop keys.[^3]
3. **Reflash the stock bootloader before jumping to VESC 6.0.** Stubborn 5.3 installs accept the official 6.0 binary only after VESC Tool restores the default bootloader—skip the step and you may end up chasing ST-Link fixes unnecessarily.[^69]
4. **Validate motor detection results.** Limited-edition hubs have returned ~270 A recommendations despite ~200 A safe limits, and some Ubox V2 units only auto-detect ~88 A versus ~135 A on V1—log outputs and set limits manually when they drift.[^47][^48]
5. **Disable regen during PSU testing.** Spinning up field-weakening on a bench supply can over-voltage the source; keep regen off until testing on a full battery stack.[^49]
6. **Capture fault codes before power-cycling.** If ABS overcurrent trips during early rides, dump VESC `faults` logs before rebooting so you can correlate spikes with wiring or observer changes.[^50]
7. **Log both controllers on every shakedown.** Aggregate CAN data to verify commanded vs. actual amps; many “weak” builds simply read one side and miss per-motor dropouts.[^10]
8. **Stage regen carefully on 22 S builds.** Drop charge voltage a few volts or cap braking current until you validate pack and controller headroom with logs.[^11]
9. **Inspect phase filters on older duals.** Populate missing components or add external LC filters if noise, thermal, or EMI issues surface on early 75/100 hardware.[^8]
10. **Verify accessory wiring.** Keep lighting loads within the ADC bridge limits and route any kill-switch expectations through smart-BMS logic or physical loop keys.[^3]
10. **Leverage the CAN wake line deliberately.** 85-series controllers share power-on logic over CAN, so a single latching button can wake master and slave; isolate supplies first if you plan to power-cycle one controller independently.[^can_power_sync]

## Procurement & Support Signals

- Warranty debates flared when a rider refused to return hardware; moderators reiterated that Spintend covers repairs with paid return shipping and contrasted the turnaround with slower Rion/Tronic replacements before issuing a ban.[^70][^71]
- Storefront reputation took a hit after community members spotted deleted negative Spin-Y reviews despite active Telegram support—set expectations around official response cadence before promising service levels.[^72]
- ExpressLine DDP shipments are clearing customs in about a week for EU buyers, yet import offices still assess duties despite the “duty paid” label.[^14]
- Regional mark-ups can double MSRP—Israeli riders now see ~$575 street pricing, pushing them toward direct factory orders or alternative brands when budgets are tight.[^14]
- Sellers occasionally under-declare controller value (e.g., listing €160 modules at €55); while it trims duties, buyers carry the audit risk if customs spot the mismatch.[^14]
- Treat the €140 “Spintend” AliExpress storefront as a likely scam—new account, no replies, and a bill of materials that already costs more than the asking price.[^73]
- Single-channel boards still ship without Bluetooth; riders bolt on external modules (shared over CAN) or email Spintend for a forgotten dongle, and the CAN harness ships with paired singles so accessories live on the master controller.[^74]
- Spintend’s 500 W water pump supplier stalled during lockdowns; 350 W replacements run hot and sparked bait-and-switch complaints, so builders now chase alternative pumps or budget for active cooling redesigns.[^75]
- Sellers occasionally under-declare controller value (e.g., listing €160 modules at €55); Paolo’s latest shipment sat in customs for weeks before full duties were applied anyway, so he stopped falsifying invoices despite vendor offers.[^14][^customs-warning]
- Expect warranty friction on unexplained failures—retailers are already pointing at firmware versions (e.g., 6.05) to deny coverage—so document software builds, logs, and install photos before submitting RMAs.[^19]
- Spintend’s capacitor bank remains thin for oversized QS hubs; heavy builders increasingly migrate to shunt-sensed platforms (Ennoid MK8, Tronic X12) when repeated gate-driver deaths surface.[^16]

## Displays & Telemetry

- Voyage’s “Megan” bundle (≈$400) piggybacks on the Metr app to expose full VESC parameters, trip logging, and multi-mode storage for Spintend builds, but riders still treat the enclosure as rain-only hardware until someone waterproofs the housing.[^voyage_megan]

## Failure Watchlist & Logging Habits

- Warranty replacements have already covered a Wolf Warrior 16 S build that ignited during motor detection; Spintend replicated the setup and suspected a failed MOSFET stage, so document pack and motor specs when filing incidents.[^wolf_fire]
- Track voltage ambitions on the 85/150 carefully—units have failed at 20 S when stacked with high-Kv hubs, MTPA, and aggressive field weakening, so treat 22 S as experimental until more telemetry lands.[^36]
- Vet MOSFET swaps before chasing 200 A+: bargain JJmicro devices underperform while Huayi parts have held 20 kW loads below 40 °C, so confirm datasheets before reflowing silicon.[^37]
- Log every ride by exporting VESC Tool CSVs or bridging Android sessions to desktop so you can correlate current spikes, duty limits, and temps before relaxing guardrails.[^38]
- Inspect for contamination after heavy service—moisture ingress and solder splatter have spoofed temperature telemetry and shorted controllers even after repairs, so schedule post-ride inspections after rain or workshop work.[^39]
- Stock firmware on single 80/85-series boards still caps phase near 150 A/ABS 210 A; flash the no-limit build and raise ABS toward 240 A with solid cooling before commanding 100 A battery / 180 A phase, and remember that smaller hubs saturate near 100 A regardless.[^76]
- Treat AI-generated traction-control scripts as experimental—recent CAN/UART toggler code needed debouncing, cached telemetry, voltage checks, and divide-by-zero fixes before it was safe to run on live hardware.[^77]
- Franchesco’s brand-new 85/250 flashed internally within a few metres on a 20 S 42 Ah build tuned for 150 A battery / 250 A phase (350 A absolute); peers are urging photo documentation and a warranty claim while warning others not to re-energise smoked hardware.[^78]
- Budget for QA misses: multiple 85/250s arrived DOA or died within weeks at 200 A battery / 170 A motor settings, pushing riders toward Seven or 3Shul spares while they wait on replacements.[^doa250]
- Diagnose ADC rail failures before reflashing—throttle noise can short the 3.3 V rail to ground and kill STM32 ADC inputs, so check resistance between 5 V/3.3 V and ground, then attempt MCU swaps only if you own hot-air gear and magnification.[^adc_short]

## Roadmap & Community Sentiment

- The upcoming single-channel unit is targeting ~85 mm × 54 mm (with mounts), sub-€180 pricing, an onboard IMU, and an external USB pigtail so tight decks can stay sealed during tuning.[^single_dims]
- Community support remains strong thanks to fast warranty service and spare logic/power boards—especially compared with ongoing frustration over Flipsky QC and marketing-first “reviews.”[^community_sentiment]
- Ubox Pro is in final testing with 100 V support (likely 22 S regen), but veterans plan to tear down every unit for solder balls or metal shavings before the first power-up.[^79]

## Roadmap Signals & Known Pain Points (Aug–Oct 2022)

- **Copper single production cadence.** Artem is finishing roughly 100 pre-order units (≈500 Spin-Y throttles) with seven-wire looms, copper spreaders, and onboarding media while planning a modular “integrator” accessory board that preserves the 3 A 12 V rail for riders who depend on onboard lighting.[^80][^81]
- **Packaging feedback loop.** Community teardown photos pushed for slimmer housings, vertical MOSFET stacks, deck-bolt mounting, and even aluminum alternatives under a $119 target price to keep harness runs short without sacrificing cooling.[^82][^83][^84]
- **Thermal rethink in progress.** Long pulls still drive copper singles past 80 °C, so testers are trialling graphite pads, potting gaps, and direct-mount heatsinks while waiting on the promised aluminum PCB revision to mitigate galvanic corrosion risk.[^85][^86][^87]
- **FET-sourcing strategy.** Spintend plans parallel 80 V “performance” and 100 V “headroom” trims for refreshed singles, keeping the removable integrator board optional so the accessory rail stays intact for early adopters.[^88]
- **Aluminum enclosure watch-outs.** Reports of metal shavings inside Flipsky aluminum housings have Spintend collecting QA incidents before copying the material change for future singles.[^89]
- **Spin-Y batch-two refresh.** Shipments paused to add logarithmic throttle curves, 0.05-step calibration cues, internal cruise control, and wheel-clearance tweaks before resuming sales at the €59 intro price.[^90][^91]
- **Production cadence:** Artem’s August 2022 status update confirmed 500 Spin-Y throttles were moving through hand-soldering while copper-backed singles entered onboarding—expect staggered deliveries and keep install guides handy for first-time buyers.[^2022_prod_update]
- **Spin-Y firmware refresh:** Batch-two plans locked in logarithmic throttle curves, 0.05-step calibration, internal cruise logic, wider wheel clearances, and tighter metal tolerances, with Artem reminding testers to verify NTC sensors in boiling water before deployment.[^92]
- **Traction-control heat spikes:** September test logs showed traction-control pulls heating Ubox singles faster than manual throttle launches; Artem said the next single would ship in 80 V and 100 V MOSFET flavours until the integrator board is ready, so plan cooling plates before flashing aggressive slip control.[^tc_heat]

## Late-2022 Iteration Highlights

- **Spin-Y Gen2 throttle polish.** Artem’s November updates locked in a 65° forward / 35° regen sweep, longer cabling, batch‑1 retrofit discounts, and a 1 mm magnet spacer that recovers two-thirds of the dead zone. Follow-on prototypes trialled wider diamond-cut wheels with glove-friendly textures, plus a single-magnet Spin-Y2 profile that flattens the output curve while Spintend recruits more QA coverage for the ramp-up.[^spin_y_gen2]
- **Control cluster & accessory planning.** The same push yielded a five-position thumb switch for blinkers, horn, and lighting along with reminders that Spintend’s light cluster *sources* 12 V—drive external relays instead of hanging accessories directly on the harness.[^spin_y_controls]
- **Aluminum-core Ubox roadmap.** Artem confirmed 6- and 12-FET aluminum singles are in flight with thicker copper, SH8/6 AWG support, and firmware-locked tiers that hold phase near 200–300 A and battery near 150 A until cooling is proven.[^aluminum_roadmap]
- **Single Ubox tuning guardrails.** Community clinics continue to steer 75 V singles toward ~130 A phase / 50–60 A battery, motor NTC retrofits, and bare-metal deck contact (scrape the paint) before chasing S/M/L tier upgrades or 200–350 A 6‑FET targets.[^single_tuning]
- **QC watchlist.** Fresh singles still arrive with missing screws or solder balls; pair the teardown with an ANT standby-draw check (a few tenths of a volt overnight is normal when the latching key is wired correctly) and document any power-board swaps before warranty claims.[^spintend_qc_nov]
- **Traction-control caution.** Rosheee’s rear Tronic fire after a traction-control slip renewed guidance to dial phase/battery limits and prefer front-only slip control when experimenting on Spintend duals.[^tc_failure]
- **ADC accessory budget.** Builders toasted the ADC adapter by adding 12 V fans to the board; treat it as a signal bridge and keep heavier loads on dedicated converters.[^adc_overload]
- **Diagnostics & rescue.** Mirono mapped the single’s unpopulated SWD pads to STM32 pins 46/49 and reminded rescuers to clean flux before micro-soldering, while SmartDisplay testers layered Waze alerts over Spintend CAN data for richer nav dashboards.[^stlink_waze]
- **Mind firmware tooling.** VESC Tool 6.0.11 mobile flags “limited mode” on 5.3 firmware until you USB-flash the 6.0 bootloader and reload vendor bins—keep desktop access handy when mobiles hide the packages.[^93]

## Source Notes

[^1]: Makerbase/Flipsky QC issues versus Spintend reliability, plus reports that Ubox controllers coast through BMS trips instead of locking wheels.Source: knowledge/notes/input_part005_review.md, L17 to L20Source: knowledge/notes/input_part008_review.md, L31 to L36
[^2]: Community thermal practices for Spintend hardware, including aluminum plate mounting guidance and dual-controller heatsink sizing.Source: knowledge/notes/input_part008_review.md, L25 to L30Source: knowledge/notes/input_part010_review.md, L531 to L531
[^3]: Limits and wiring expectations for Spintend’s ADC adapter, including delivered harness connectors and accessory-current ceilings.Source: knowledge/notes/input_part005_review.md, L57 to L58Source: knowledge/notes/input_part007_review.md, L221 to L223
[^4]: Dual Ubox 75/100 capabilities and continued 75 V-class usage in race builds.Source: knowledge/notes/input_part010_review.md, L189 to L190
[^5]: Packaging flexibility and current targets for Ubox Lite singles versus the dual 100/100 chassis.Source: knowledge/notes/input_part010_review.md, L92 to L98
[^6]: Field logs showing 12‑FET Ubox battery and phase limits when cooled.Source: knowledge/notes/input_part010_review.md, L190 to L190
[^7]: Details on the revised 85 V/240 A single Ubox with 8 AWG leads and reversible exits.Source: knowledge/notes/input_part010_review.md, L202 to L203
[^dual-75v]: Legacy dual Ubox safe envelope (~150 A phase per side) plus refreshed 85 V/240 A single with AWG 8 leads and reversible exits priced below the retired 250 A block.Source: knowledge/notes/input_part010_review.md, L201 to L203
[^8]: Early dual 75/100 revisions shipping without populated phase filters.Source: knowledge/notes/input_part005_review.md, L167 to L167
[^v2_downgrade]: Raphaël confirmed Spintend swapped 4 A Infineon gate drivers for 1.5 A generics and removed the BLE daughterboard on cost-reduced V2 hardware, explaining weaker high-duty performance.Source: knowledge/notes/input_part002_review.md, L129 to L132
[^single_lid_limit]: The single Ubox enclosure still bolts MOSFETs to the lid, leaving roughly half the thermal mass of the dual case—fans now remind riders it was designed for ~30 A continuous one-wheel builds, not 100 A dual-motor pulls.Source: data/vesc_help_group/text_slices/input_part002.txt, L9689 to L9697
[^9]: Recommended continuous versus peak targets for 85-250 hardware and firmware-imposed voltage/current caps.Source: knowledge/notes/input_part010_review.md, L567 to L567
[^10]: Dual-controller log evidence showing commanded versus actual current disparities on Lite builds.Source: knowledge/notes/input_part010_review.md, L564 to L564
[^11]: Regen strategies and voltage precautions for 21–22 S packs to avoid over-voltage failures.Source: knowledge/notes/input_part005_review.md, L152 to L153
[^12]: Firmware-imposed ~300 A phase ceiling on early 85/200 controllers and the risks of flashing unofficial builds.Source: knowledge/notes/input_part007_review.md, L236 to L236
[^13]: Documented throttle pinout and NRF/Bluetooth layout for Spintend controllers.Source: knowledge/notes/input_part010_review.md, L526 to L526
[^14]: Shipping timelines, regional price hikes, and customs under-valuation practices affecting Spintend buyers.Source: knowledge/notes/input_part010_review.md, L179 to L179Source: knowledge/notes/input_part010_review.md, L361 to L361Source: knowledge/notes/input_part005_review.md, L100 to L100
[^customs-warning]: Paolo’s reminder that under-declared packages still drew full duties after weeks in customs, so he no longer accepts falsified invoices.Source: knowledge/notes/input_part010_review.md, L372 to L373
[^motor-survival]: GABE killed three commuter-grade hubs in two days while his Spintend 100 V Lite kept running, highlighting the controller’s tolerance of motor-side faults.Source: data/vesc_help_group/text_slices/input_part011.txt, L19136 to L19173
[^16]: Heavy QS hub loads overheating undersized Spintend capacitor banks and the push toward heavier-duty controllers.Source: knowledge/notes/input_part014_review.md, L16 to L16
[^firmware-bins]: Official Spintend firmware offers 100 A and 300 A battery-limit variants; the hotter bin voids warranty and still shows ≈60 A battery ceilings with ~147 A phase bursts in field logs.Source: knowledge/notes/input_part000_review.md, L42 to L42
[^ct_limit]: Early 85250 V1 current-transformer sensing saturating near 100 A and Smart Repair’s recommendation to pivot to shunt-based MK8/X12 footprints (with IPTC017N12NM6 swaps for Ennoid builds) until the 18-FET revision ships.Source: knowledge/notes/input_part014_review.md, L12 to L13
[^17]: Persistent throttle jitter complaints across multiple Ubox hardware revisions that require wiring and filtering fixes.Source: knowledge/notes/input_part014_review.md, L17 to L17
[^18]: Heavy riders continuing to burn 12-FET 85/250 hardware despite conservative ramps, reinforcing derating guidance.Source: knowledge/notes/input_part014_review.md, L19 to L19
[^19]: Warranty denials tied to firmware blame, underscoring the need to document software builds before submitting RMAs.Source: knowledge/notes/input_part014_review.md, L12 to L22
[^community_feedback]: Spintend monitors rider chats—including Russian-language experiments—to prioritise scooter-focused screens and throttles.Source: knowledge/notes/input_part000_review.md, L56 to L56
[^single_preview]: Source: knowledge/notes/input_part000_review.md, lines 252 and 299.
[^20]: Field-weakening failure case on 85150 hardware and guidance to cap FW or swap MOSFETs before chasing more ERPM.Source: knowledge/notes/input_part014_review.md, L21 to L21Source: knowledge/notes/input_part014_review.md, L167 to L168
[^21]: Thermal adhesive mounting tips, per-motor temperature monitoring, and reminders that workmanship faults still kill controllers.Source: knowledge/notes/input_part014_review.md, L22 to L22Source: knowledge/notes/input_part014_review.md, L45 to L45
[^22]: Voltage headroom cautions for 85240 revisions and the need for full-component audits before 22 S experiments.Source: knowledge/notes/input_part014_review.md, L205 to L205
[^23]: Turn-signal strip support, Spin dial harness guidance, and equal-length phase lead reminders for tidy installs.Source: knowledge/notes/input_part014_review.md, L208 to L210
[^24]: ADC window compression, grounding checks, and filtering strategies that resolved runaway throttle noise on compact Spintend builds.Source: knowledge/notes/input_part014_review.md, L85 to L86Source: knowledge/notes/input_part014_review.md, L220 to L221
[^25]: Comparative thermal readings showing OEM pad compression impacts on Ubox V2 temperature deltas.Source: knowledge/notes/input_part001_review.md, L181 to L183
[^26]: Deck-sanding and clamp-mount techniques that held Ubox cases near 55 °C under 50 A/120 A loads.Source: knowledge/notes/input_part001_review.md, L249 to L250
[^27]: Thermal pad shootout results where thicker aftermarket pads raised MOSFET temperatures.Source: knowledge/notes/input_part001_review.md, L855 to L856
[^28]: Mounting guidance for Spintend aluminum 6-FET units using 3–5 mm plates and thermal paste.Source: knowledge/notes/input_part008_review.md, L29 to L29
[^29]: Thermal headroom gains observed when sharing load across dual controllers versus single-drive pulls.Source: knowledge/notes/input_part008_review.md, L28 to L28
[^rapid_heat]: Early Spintend Ubox shakedowns logged MOSFET temperatures hitting ~50 °C within seconds at 50 A battery draw before pack protection intervened.Source: knowledge/notes/input_part000_review.md, L94 to L94
[^30]: Current baselines logged on 17 S and 16 S dual-drive Spintend builds.Source: knowledge/notes/input_part001_review.md, L207 to L207
[^31]: Observed 2×135 A phase / 2×71 A battery setups and associated BMS thermal trip warnings.Source: knowledge/notes/input_part001_review.md, L657 to L662
[^32]: Battery group sizing lessons from high-Kv hubs requiring ≥150 A battery per side and companion pack BMS trips during regen.Source: knowledge/notes/input_part008_review.md, L291 to L291Source: knowledge/notes/input_part008_review.md, L275 to L276
[^33]: Regen adjustments needed to clear BMS over-voltage faults around 76.6 V on 20 S packs.Source: knowledge/notes/input_part008_review.md, L607 to L607
[^input_caps]: Adding 470 µF low-ESR capacitors close to the controller when pack leads are long prevents MCU brownouts from back-EMF spikes.Source: knowledge/notes/input_part000_review.md, L89 to L89
[^34]: ADC adapter wiring with diode isolation while keeping UART dashboards online.Source: knowledge/notes/input_part009_review.md, L84 to L86
[^tokmas_swap]: Hackintoshhhh’s Tokmas/JMSh1001ATLQ MOSFET swap logs showing 160–180 A battery and ~240 A phase capability alongside hotter case temps, plus Patrick’s reminder that the six-FET stage still caps practical output near 230–250 A.Source: knowledge/notes/input_part011_review.md, L411 to L413
[^thunder_front85150]: Thunder 2 front-motor plan targeting 150 A battery / 230 A phase with repaste, exposed heatsinks, optional fans, and temperature ceilings that taper output before ~96 °C during 120–130 km/h runs.Source: knowledge/notes/input_part011_review.md, L415 to L417
[^can_power_sync]: Dual Thunder builds confirmed the 85-series CAN power line wakes both controllers from a single button; isolate supplies if you need independent power-cycling.Source: knowledge/notes/input_part011_review.md, L468 to L470
[^voyage_megan]: Voyage “Megan” displays bundle Metr integration, trip logging, and mode storage for roughly $400, but riders still avoid rain because the housing is not sealed.Source: knowledge/notes/input_part011_review.md, L447 to L449
[^35]: Feeding Spintend’s ADC adapter from an external DC-DC on Ubox Lite builds.Source: knowledge/notes/input_part008_review.md, L606 to L606
[^hackintosh_burst]: Hackintoshhhh’s MOT1111T-equipped 85250 build tolerated ~480 A phase bursts per controller once the upgraded silicon and cooling were dialed in.Source: knowledge/notes/input_part013_review.md, L34 to L34
[^arnau_dropout]: Arnau Martinez Casals’ Ubox 250 stayed powered yet blocked Bluetooth pairing after a 60 V/120 A trip—evidence of failing regulators or CAN protection parts rather than a pure software fault.Source: knowledge/notes/input_part013_review.md, L61 to L62
[^direct_order]: Matthew’s reminder that direct-from-Spintend orders avoid AliExpress markups and keep warranty support responsive for 85150/85250 hardware.Source: knowledge/notes/input_part013_review.md, L227 to L234
[^soderstrom]: 🇪🇸AYO#74’s shout-out to James Soderstrom for repairing Spintend driver stages and fabricating replacement BLE modules during RMA backlogs.Source: knowledge/notes/input_part013_review.md, L236 to L244
[^u100_daily]: Matthew and ’lekrsu’ aligned on ~130–135 A phase, 85–90 A battery, and 150–180 A absolute as the dependable daily window for single Ubox 100/100 Lonnyo 65 H builds once duty and FW trims were set.Source: data/vesc_help_group/text_slices/input_part013.txt, L17015 to L17084
[^u100_cooling]: The same build’s custom water-cooled base plate shed ~14 °C within a minute at 130 A phase in 35 °C ambient tests, making back-to-back pulls viable.Source: data/vesc_help_group/text_slices/input_part013.txt, L17077 to L17084Source: data/vesc_help_group/text_slices/input_part013.txt, L17358 to L17363
[^accessory_buck]: Matthew’s accessory-rail math showed a 12 V/20 A converter only draws ~4–6 A from a 60 V pack while running horns, pumps, fans, and lights; he now trims controller battery amps to protect the BMS during horn spikes.Source: data/vesc_help_group/text_slices/input_part013.txt, L17300 to L17340Source: data/vesc_help_group/text_slices/input_part013.txt, L17449 to L17477
[^adc2_limit]: Spintend owners cap ADC2 loads around 1 A and reroute horns or high-draw lights through separate switches so the logic rail isn’t overloaded.Source: knowledge/notes/input_part006_review.md, L401 to L401
[^safe_envelope]: Rogerio’s stock-firmware 85250 failed within days at 180 A phase / 80 A battery with regen disabled, prompting the group to flash the no-limits firmware but cap daily tunes near 150 A battery / 250 A phase while keeping enclosures clean.Source: knowledge/notes/input_part013_review.md, L225 to L234
[^36]: Spintend 85/150 failures at 20 S under heavy field-weakening stress.Source: knowledge/notes/input_part009_review.md, L87 to L87
[^wolf_fire]: Spintend agreed to replace a Ubox that caught fire during Wolf Warrior motor detection and requested full build specs to replicate the failure.Source: knowledge/notes/input_part000_review.md, L62 to L62
[^37]: MOSFET reliability comparisons favouring Huayi devices over cheaper alternatives for 200 A-class loads.Source: knowledge/notes/input_part009_review.md, L88 to L88
[^38]: Recommended CSV logging workflows via VESC Tool and Android bridge methods.Source: knowledge/notes/input_part001_review.md, L149 to L150
[^39]: Moisture contamination spoofing temperature telemetry until enclosures were cleaned and resealed.Source: knowledge/notes/input_part008_review.md, L40 to L40
[^v2_ntc]: Ubox V2’s higher reported temperatures trace back to NTC placement and higher phase current, and riders found the stock Spintend pads cooled better than aftermarket Thermal Grizzly sheets once clamp pressure was restored.Source: data/vesc_help_group/text_slices/input_part001.txt, L24976 to L25009Source: data/vesc_help_group/text_slices/input_part001.txt, L25349 to L25359
[^ble_dongle]: Official Spintend Bluetooth modules arrive pre-flashed around €29 with taxes included, while generic NRF51822 boards demand manual flashing before they pair reliably, so most riders pay for the plug-and-play option.Source: data/vesc_help_group/text_slices/input_part001.txt, L24903 to L24930
[^ble_required]: Veteran 75100 users keep Bluetooth enabled on Spintend controllers because field tuning and fault collection are impractical without wireless access once the deck is sealed.Source: data/vesc_help_group/text_slices/input_part001.txt, L24915 to L24921
[^adc_short]: Diagnosing Ubox “B” side failures starts with checking resistance between the 5 V/3.3 V rails and ground—noise-induced shorts cook STM32 ADC inputs, and only experienced rework techs should attempt MCU swaps after confirming the short.Source: data/vesc_help_group/text_slices/input_part001.txt, L4386 to L4499
[^single_dims]: Source: knowledge/notes/input_part000_review.md, line 183.
[^community_sentiment]: Source: knowledge/notes/input_part000_review.md, line 184.
[^missing_ble]: Ubox V2 shipments missing the Bluetooth daughterboard forced riders to plug third-party 5 V UART modules into the header and troubleshoot noisy ADC rails or damaged STM32 pins themselves.Source: data/vesc_help_group/text_slices/input_part001.txt, L5811 to L5868
[^phase_rework]: Upgrading to 10 AWG phase leads demanded 60–80 W irons; compact TS80P pencils desolder stock leads but struggle to tin heavier cable cleanly.Source: data/vesc_help_group/text_slices/input_part001.txt, L5920 to L5938
[^fw53_release]: Spintend’s public 5.3 firmware drop earned mixed reviews—official support urged riders to remain on 5.2 until customised 5.3 binaries soak, even as early testers praised smoother acoustics.Source: data/vesc_help_group/text_slices/input_part001.txt, L4000 to L4052Source: data/vesc_help_group/text_slices/input_part001.txt, L5042 to L5059
[^u75_vs100]: Early 75 V betas shipped with exposed copper busbars while later 100 V runs hid higher-Rds(on) MOSFETs under resin and still arrived with loose solder balls, prompting riders to open every unit on delivery.Source: data/vesc_help_group/text_slices/input_part001.txt, L25795 to L25855
[^logistics_update]: Spintend discontinuing the 85/250 while routing 85/240 shipments through a New Jersey hub so U.S. buyers see faster delivery and minimal tariffs, leaving the higher-rated board scarce.[Source: knowledge/notes/input_part012_review.md, L111 to L135Source: knowledge/notes/input_part012_review.md, L379 to L405]
[^u100_baseline]: Smart Repair’s teardown of the Ubox 100/100 highlights its 22 S limit, ≈135 A phase / 180 A absolute defaults, lack of ST-Link pads, and the need to tame regen unless you’re ready for MOSFET swaps.Source: knowledge/notes/input_part012_review.md, L48 to L48
[^u85240_speed]: Single 85/240 builds have already pushed Lonnyo 80 H hubs to ~95 km/h on 22 S, underscoring that the compact case still needs race-grade cooling before chasing dual-drive numbers.Source: knowledge/notes/input_part012_review.md, L24 to L24
[^seq_led]: Sequential LED strips overrun the ADC turn-signal line without helper logic, so riders rewire lighting looms or add controllers when they want chase effects.Source: knowledge/notes/input_part012_review.md, L481 to L481
[^mounting_threads]: Riders printing adapter plates, adding 0.5 mm pads, or retapping the tiny M2.5 bosses because 85/240/Lite housings ship without sturdy mounting ears or hardware.[Source: knowledge/notes/input_part012_review.md, L419 to L420Source: knowledge/notes/input_part012_review.md, L465 to L466
[^doa250]: Reports of 85/250 controllers arriving DOA or failing quickly at 200 A battery / 170 A motor, prompting owners to migrate toward Seven or 3Shul alternatives.[Source: knowledge/notes/input_part012_review.md, L110 to L111Source: knowledge/notes/input_part012_review.md, L135 to L136
[^40]: Shared 300 A hardware-limit firmware for single Ubox installs and the reminder to keep real tunes near 80 A battery / 130 A phase with solid cooling.Source: knowledge/notes/input_part001_review.md, L12 to L12
[^41]: Solder-ball contamination on new Ubox V2 units prompting full disassembly and cleaning before use.Source: knowledge/notes/input_part001_review.md, L238 to L240
[^42]: Connector melt reports that led riders to upgrade to QS8/AS150 hardware with shielded control wiring.Source: knowledge/notes/input_part001_review.md, L242 to L244
[^motor_connectors]: Factory looms pairing XT90 battery tails with female motor bullets prompted builders to shorten leads, install 5.5 mm connectors, and split power versus signal runs down opposite deck rails.Source: knowledge/notes/input_part000_review.md, L85 to L85
[^connector_upgrade]: Melted XT90 jumpers on dual Ubox builds traced to soldered bus bars without copper leads, prompting QS8/AS150U/QS8H upgrades and shielded CAT6A control looms.Source: data/vesc_help_group/text_slices/input_part001.txt, L5231 to L5284
[^case_prep]: Sanding deck paint, flattening copper plates, and re-seating stock pads cut Ubox case temps from 67 °C to about 55 °C at 50 A battery / 120 A phase while preventing throttling.Source: data/vesc_help_group/text_slices/input_part001.txt, L5400 to L5438Source: data/vesc_help_group/text_slices/input_part001.txt, L5418 to L5437
[^43]: Fleet teardown showing stray solder balls bridging dual Spintend outputs and destroying both controllers.Source: knowledge/notes/input_part008_review.md, L268 to L268
[^44]: Ubox Lite ESD failures caused by unsymmetrical power disconnects while CAN remained energised.Source: knowledge/notes/input_part008_review.md, L269 to L269
[^45]: Standby draw measurements and LED behaviour on Spintend’s latching power switch.Source: knowledge/notes/input_part001_review.md, L214 to L216
[^46]: Community flashing workflow relying on Spintend-supplied BINs and auto-detection to avoid bricking controllers.Source: knowledge/notes/input_part001_review.md, L632 to L633
[^47]: Auto-detect anomalies recommending ~270 A on dual-phase hubs until limits are manually corrected.Source: knowledge/notes/input_part001_review.md, L824 to L825
[^single-proto]: Paolo’s single-board Spintend prototype measures ~60 mm wide without the case, adds capacitance over a Nucular 12F, should manage ≈150 A battery on flat roads, and still needs external sealing for wet decks.Source: knowledge/notes/input_part001_review.md, L80 to L82
[^single-can]: Koxx confirmed the single Ubox exposes CAN, Bluetooth, and USB simultaneously, letting accessories and diagnostics stay online without swapping cables.Source: knowledge/notes/input_part001_review.md, L99 to L99
[^48]: Ubox V1 vs. V2 motor detection variances demanding manual review of current limits.Source: knowledge/notes/input_part001_review.md, L889 to L889
[^49]: Bench-testing guidance to disable regen and field weakening on PSU-powered Spintend setups to avoid over-voltage damage.Source: knowledge/notes/input_part009_review.md, L84 to L84
[^50]: Fault logging workflow for ABS overcurrent and sensorless diagnostics before power-cycling, plus recommended CSV logging methods.Source: knowledge/notes/input_part001_review.md, L138 to L150
[^52]: Water-cooled 85250 performance data, tariff-driven price creep, and the teased €180 18-FET revision.Source: knowledge/notes/input_part014_review.md, L20 to L20
[^53]: Spintend X12 accessory rail limits and the need for external buck converters to power lighting or telemetry hardware.Source: knowledge/notes/input_part014_review.md, L140 to L143
[^54]: The phase-filter toggle should be used only during motor detection; leaving it active while riding reintroduces noise and ABS overcurrent errors.Source: knowledge/notes/input_part004_review.md, L31 to L31
[^bridge_mirror]: Spintend’s bridge keeps battery current mirrored across controllers—Smart Repair’s GT1 logs showed the front 150 A unit inheriting the rear controller’s battery amps until CAN or power was isolated.[Source: knowledge/notes/input_part011_review.md, L79 to L79Source: knowledge/notes/input_part011_review.md, L317 to L317
[^baseplate_spreader]: JPPL and Shlomozero are reusing dead 75/200 baseplates as auxiliary heatsinks with aluminum spacers and radiator blocks tied into Dualtron side plates to cool HY-equipped stages.Source: knowledge/notes/input_part011_review.md, L521 to L521
[^qc_input004]: Quality control failures on UBOX Single 100/100 batch showing shorted current-sense op-amps and blown input capacitors.Source: knowledge/notes/input_part004_review.md, L15 to L15Source: knowledge/notes/input_part004_review.md, L88 to L88
[^bt_polarity]: Ubox 80 V single shipped with reversed Bluetooth harness, killing the module on power-up.Source: knowledge/notes/input_part004_review.md, L287 to L287
[^autooff-issue]: Spintend 100/100 refusing to shut down despite disabled ADC auto-off timers, indicating accessory power bleed or stuck logic rails.Source: knowledge/notes/input_part013_review.md, L464 to L464
[^lite-connector]: Spintend Alu Lite logic harness using undocumented keyed multi-pin connectors that must be reused or sourced for custom wiring.Source: knowledge/notes/input_part013_review.md, L777 to L780

## References

[^1]: Source: knowledge/notes/input_part000_review.md, L502 to L504
[^2]: Source: knowledge/notes/input_part006_review.md, L107 to L107
[^3]: Source: knowledge/notes/input_part010_review.md, L32 to L33
[^4]: Source: knowledge/notes/input_part011_review.md, L759 to L765
[^5]: Source: knowledge/notes/input_part000_review.md, L504 to L504
[^6]: Source: knowledge/notes/input_part001_review.md, L549 to L550
[^7]: Source: knowledge/notes/input_part001_review.md, L565 to L566
[^8]: Source: knowledge/notes/input_part000_review.md, L496 to L498
[^9]: Source: knowledge/notes/input_part000_review.md, L308 to L308
[^10]: Source: knowledge/notes/input_part005_review.md, L242 to L242
[^11]: Source: knowledge/notes/input_part001_review.md, L592 to L593
[^12]: Source: data/vesc_help_group/text_slices/input_part014.txt, L10636 to L10663
[^13]: Source: data/vesc_help_group/text_slices/input_part004.txt, L4241 to L4268
[^14]: Source: data/vesc_help_group/text_slices/input_part004.txt, L8813 to L8818
[^15]: Source: knowledge/notes/input_part006_review.md, L188 to L188
[^16]: Source: data/vesc_help_group/text_slices/input_part010.txt, L17340 to L17348
[^17]: Source: data/vesc_help_group/text_slices/input_part001.txt, L20979 to L21033
[^18]: Source: knowledge/notes/input_part000_review.md, L505 to L509
[^19]: Source: knowledge/notes/input_part000_review.md, L562 to L563
[^20]: Source: knowledge/notes/input_part000_review.md, L563 to L563
[^21]: Source: data/vesc_help_group/text_slices/input_part003.txt, L12321 to L12355
[^22]: Source: data/vesc_help_group/text_slices/input_part003.txt, L12890 to L12957
[^23]: Source: data/vesc_help_group/text_slices/input_part001.txt, L8424 to L8453
[^24]: Source: data/vesc_help_group/text_slices/input_part001.txt, L20826 to L20905
[^25]: Source: knowledge/notes/input_part001_review.md, L509 to L510
[^26]: Source: knowledge/notes/input_part000_review.md, L585 to L585
[^27]: Source: knowledge/notes/input_part011_review.md, L321 to L327
[^28]: Source: knowledge/notes/input_part000_review.md, L235 to L235
[^29]: Source: knowledge/notes/input_part000_review.md, L592 to L594
[^30]: Source: knowledge/notes/input_part004_review.md, L24 to L24
[^31]: Source: knowledge/notes/input_part004_review.md, L203 to L203
[^32]: Source: knowledge/notes/input_part000_review.md, L588 to L588
[^33]: Source: knowledge/notes/input_part000_review.md, L588 to L589
[^34]: Source: knowledge/notes/input_part000_review.md, L592 to L593
[^35]: Source: knowledge/notes/input_part003_review.md, L223 to L223
[^36]: Source: data/vesc_help_group/text_slices/input_part003.txt, L3006 to L3084
[^37]: Source: data/vesc_help_group/text_slices/input_part003.txt, L3231 to L3249
[^38]: Source: data/vesc_help_group/text_slices/input_part003.txt, L9349 to L9352
[^39]: Source: data/vesc_help_group/text_slices/input_part003.txt, L11768 to L11824
[^40]: Source: data/vesc_help_group/text_slices/input_part003.txt, L11972 to L12033
[^41]: Source: data/vesc_help_group/text_slices/input_part003.txt, L12202 to L12209
[^42]: Source: knowledge/notes/input_part013_review.md, L709 to L710
[^43]: Source: knowledge/notes/input_part011_review.md, L468 to L469
[^44]: Source: knowledge/notes/input_part011_review.md, L436 to L441
[^45]: Source: data/vesc_help_group/text_slices/input_part013.txt, L3769 to L3770
[^46]: Source: data/vesc_help_group/text_slices/input_part013.txt, L4184 to L4184
[^47]: Source: knowledge/notes/input_part010_review.md, L66 to L67
[^48]: Source: knowledge/notes/input_part000_review.md, L380 to L380
[^49]: Source: knowledge/notes/input_part011_review.md, L397 to L398
[^50]: Source: knowledge/notes/input_part011_review.md, L31 to L31
[^51]: Source: knowledge/notes/input_part011_review.md, L169 to L169
[^52]: Source: data/vesc_help_group/text_slices/input_part001.txt, L9584 to L9623
[^53]: Source: knowledge/notes/input_part001_review.md, L508 to L509
[^54]: Source: knowledge/notes/input_part001_review.md, L629 to L630
[^55]: Source: knowledge/notes/input_part001_review.md, L92 to L92
[^56]: Source: knowledge/notes/input_part001_review.md, L548 to L549
[^57]: Source: data/vesc_help_group/text_slices/input_part001.txt, L20906 to L20947
[^58]: Source: knowledge/notes/input_part001_review.md, L668 to L670
[^59]: Source: data/vesc_help_group/text_slices/input_part001.txt, L10015 to L10202
[^60]: Source: data/vesc_help_group/text_slices/input_part001.txt, L10273 to L10314
[^61]: Source: data/vesc_help_group/text_slices/input_part001.txt, L9226 to L9351
[^62]: Source: data/vesc_help_group/text_slices/input_part001.txt, L9333 to L9348
[^63]: Source: data/vesc_help_group/text_slices/input_part001.txt, L10314 to L10343
[^64]: Source: knowledge/notes/input_part013_review.md, L430 to L431
[^65]: Source: data/vesc_help_group/text_slices/input_part001.txt, L25592 to L25626
[^66]: Source: knowledge/notes/input_part011_review.md, L471 to L479
[^67]: Source: data/vesc_help_group/text_slices/input_part003.txt, L18185 to L18336
[^68]: Source: data/vesc_help_group/text_slices/input_part003.txt, L18775 to L19035
[^69]: Source: knowledge/notes/input_part004_review.md, L32 to L32
[^70]: Source: data/vesc_help_group/text_slices/input_part003.txt, L2209 to L2223
[^71]: Source: data/vesc_help_group/text_slices/input_part003.txt, L231 to L297
[^72]: Source: data/vesc_help_group/text_slices/input_part003.txt, L5746 to L5754
[^73]: Source: knowledge/notes/input_part000_review.md, L348 to L348
[^74]: Source: knowledge/notes/input_part000_review.md, L333 to L334
[^75]: Source: data/vesc_help_group/text_slices/input_part002.txt, L2691 to L2716
[^76]: Source: knowledge/notes/input_part011_review.md, L487 to L489
[^77]: Source: knowledge/notes/input_part011_review.md, L472 to L473
[^78]: Source: knowledge/notes/input_part011_review.md, L463 to L471
[^79]: Source: knowledge/notes/input_part000_review.md, L509 to L512
[^80]: Source: data/vesc_help_group/text_slices/input_part003.txt, L2 to L55
[^81]: Source: data/vesc_help_group/text_slices/input_part003.txt, L372 to L391
[^82]: Source: data/vesc_help_group/text_slices/input_part003.txt, L348 to L392
[^83]: Source: data/vesc_help_group/text_slices/input_part003.txt, L2233 to L2364
[^84]: Source: data/vesc_help_group/text_slices/input_part003.txt, L2717 to L2746
[^85]: Source: data/vesc_help_group/text_slices/input_part003.txt, L4089 to L4128
[^86]: Source: data/vesc_help_group/text_slices/input_part003.txt, L4500 to L5176
[^87]: Source: data/vesc_help_group/text_slices/input_part003.txt, L5443 to L5468
[^88]: Source: data/vesc_help_group/text_slices/input_part003.txt, L6860 to L6867
[^89]: Source: data/vesc_help_group/text_slices/input_part003.txt, L6873 to L6878
[^90]: Source: data/vesc_help_group/text_slices/input_part003.txt, L7540 to L7567
[^91]: Source: data/vesc_help_group/text_slices/input_part003.txt, L8580 to L8664
[^92]: Source: knowledge/notes/input_part003_review.md, L84 to L84
[^93]: Source: knowledge/notes/input_part003_review.md, L143 to L143
