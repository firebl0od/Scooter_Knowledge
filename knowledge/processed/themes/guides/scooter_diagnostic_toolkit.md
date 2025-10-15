# Scooter Diagnostic Toolkit & Field Practices

## Core Instruments
- **Handheld multimeter:** Expect budget meters to ship with 12 V A23 cells and fragile F200 mA fuses—stock replacements and keep a sturdier backup such as the Mustool MT111 on hand for daily troubleshooting.【F:knowledge/notes/all_part01_review.md†L164-L164】
- **Cell testing bench:** Pair LiitoKala or Opus bays with a 3.3 Ω / 25 W Ohmite resistor block so you can discharge or capacity-test loose 18650s before grouping them into packs, especially when customer batteries arrive full.【F:knowledge/notes/all_part01_review.md†L165-L165】
- **Firmware lifeline:** ST-Link V2 programmers remain the fastest recovery path for bricked dashboards, ESCs, and Rita-linked BMS boards—clip onto the pads, flash stock firmware, then resume Bluetooth updates once communications return. Modern Ninebot Max dashboards also demand ST-Link access because recent BLE revisions block OTA downgrades.【F:knowledge/notes/all_part01_review.md†L47-L49】【F:knowledge/notes/all_part01_review.md†L166-L166】【F:knowledge/notes/all_part01_review.md†L331-L331】【F:knowledge/notes/denis_all_part02_review.md†L103-L104】
- **Low-voltage logging:** Keep Bluetooth thermometers or CR2032-powered loggers in the spares bin when validating experimental packs so you can capture temperature spikes before they cook cells.【F:knowledge/notes/all_part01_review.md†L372-L372】
- **Insulation & adhesive supplies:** Stock RTV silicone, Kapton, and zip ties to strain-relieve DC/DC converters and harnesses; vibration snaps converter leads unless they are glued or tied back to the PCB before the scooter ever rolls.【F:knowledge/notes/denis_all_part02_review.md†L31-L32】

## Wiring & Harness Checks
1. **Start at the XT30:** After any crash or curb strike, verify the adapter output voltage before chasing other faults; browned phase pins or half-seated BMS harnesses are the most common culprits when scooters power-cycle on bumps.【F:knowledge/notes/all_part01_review.md†L195-L195】
2. **Inspect pack protection:** Cheap “25 A” eBay BMS boards routinely trip around 18 A despite balanced cell groups—swap in reputable 20–30 A hardware before blaming Rita or the controller for brownouts.【F:knowledge/notes/all_part01_review.md†L172-L172】
3. **Match radio gear:** Immobiliser and alarm kits ship in multiple frequencies; confirm your remote (315 MHz vs. 415 MHz) before hard-wiring to the scooter’s 5 V accessory tap so the system actually arms.【F:knowledge/notes/all_part01_review.md†L167-L167】
4. **Treat locks as consumables:** Light cable locks such as compact Master Lock loops work for coffee stops only if they stay lubricated with graphite—dry mechanisms jam quickly after rain or grit exposure.【F:knowledge/notes/all_part01_review.md†L191-L191】
5. **Identify controller silicon before flashing.** New Xiaomi ESCs use GD32 MCUs; flashing STM firmware bricks them, so zoom in on chip markings and grab the GD image set before running ST-Link recoveries.【F:knowledge/notes/denis_all_part02_review.md†L95680-L95780】
6. **Secure accessory power taps.** Dashboards only expose 5 V logic—drive headlights and horns from a dedicated DC/DC converter, tie the output wires to the board with RTV, and route the harness away from moving stems so the leads do not fatigue.【F:knowledge/notes/denis_all_part02_review.md†L28-L32】【F:knowledge/notes/denis_all_part02_review.md†L31-L32】
7. **Trace weak 5 V accessory ports back to the buck converter.** A Max G30 plug that still shows 5 V but no current usually means a failed converter stage—follow the trace with a multimeter until you reach the DC/DC module and verify components between it and the port before ordering a replacement board.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L110038-L110041】
8. **Respect sense shunts.** Paralleling extra R001 resistors onto a BMS without redesigning the circuit leaves components overheating even when balance leads look normal—walk the mod back and plan a higher-rated board instead.【F:knowledge/notes/input_part002_review.md†L246-L247】
9. **Secure long phase extensions.** Three‑metre leads whip violently once controllers push real amps; clamp and shorten runs to avoid Lorentz-force fatigue on solder joints or stator exits.【F:knowledge/notes/input_part002_review.md†L248-L248】

## Wheel & Brake Fitment Checks
- **Install torque arms before testing.** Ebike-to-scooter conversions powered by VESCs have levered axles out within metres when riders relied on washers; delay shakedowns until machined rear clamps arrive.【F:knowledge/notes/input_part002_review.md†L140-L141】
- **Clamp-on controller mounts demand matching torque arms.** MakerX downtube installs look tidy, but thin dropouts and extra washers let hubs slip without tight interference-fit torque arms.【F:knowledge/notes/input_part002_review.md†L305-L306】
- **Audit rotor clearance on Kaabo/Magura combos.** Magura MT7/MT5 calipers barely clear 2.9 mm Kaabo rotors—new pads or 3 mm discs overwhelm the pocket unless you machine spacers, so many stick with 2.0 mm hardware or stock Zoom calipers.【F:knowledge/notes/input_part002_review.md†L142-L142】
- **Escalate rotor size for highway stops.** Back-to-back 80–90 km/h stops cook 120 mm rotors and Magura MT8 calipers—default to dual front brakes or 203 mm discs on heavy builds.【F:knowledge/notes/input_part002_review.md†L344-L344】
- **Shim calipers with plates, not stacked washers.** Thin nickel-strip shims keep mounts rigid; tall washer stacks flex and work loose under repeated braking loads.【F:knowledge/notes/input_part002_review.md†L345-L345】
- **Source quality rotors.** Shimano RT66/RT86, Magura Storm HC, and Galfer discs survive 70 km/h abuse—AliExpress specials keep warping despite tempting prices.【F:knowledge/notes/input_part002_review.md†L346-L346】
- **Seat axles fully before blaming adapters.** A 203 mm rotor sat high on Mirono’s ebike because the axle wasn’t home in the dropout—even dual torque arms couldn’t stop the wheel from walking out until custom arms sat flush and locked the rotor plane.【F:knowledge/notes/input_part002_review.md†L678-L679】
- **Plan tyre service tools.** Tubeless slicks seal punctures but roadside swaps take longer than split-rim tubes; keep plugs plus split-rim tools when you expect field repairs.【F:knowledge/notes/input_part002_review.md†L143-L143】
- **Budget extra labour for non-split Wolf rims.** 11″ tubeless changes fought mechanics despite tutorials—document the required irons, bead clamps, and patience before attempting the job on the road.【F:knowledge/notes/input_part002_review.md†L367-L367】
- **Note factory loom limits.** Kaabo hubs ship with dual 6003 bearings and roughly 5 mm² (≈10 AWG) phase leads; 3×6 mm² conductors plus halls will squeeze through the axle on 2 000 W-class stators once you trim insulation.【F:knowledge/notes/input_part002_review.md†L191-L191】
- **Reposition forks for larger rotors.** Flipping Wolf fork legs left/right opens room for 180 mm Magura rotors up front, but the rear still lacks bosses and typically needs fabrication before Maguras fit cleanly.【F:knowledge/notes/input_part002_review.md†L192-L192】
- **Expect heavy solder on Kaabo terminations.** Factory joints resemble spot-welded “Kryptonian” blobs—plan to cut and splice upgrades rather than desoldering the OEM leads.【F:knowledge/notes/input_part002_review.md†L193-L193】
- **Evaluate aftermarket hub upgrades.** Paolo highlighted 65 mm-wide 10" motors with 10 mm² leads and 155 mm dropouts as Vsett upgrades, but the price may rival stepping to 11" platforms—budget accordingly.【F:knowledge/notes/input_part002_review.md†L194-L194】

## Hub Bearing & Cooling Service
- **Use a proper puller on stuck hubs.** Cutting at the axle shoulder ruins the shaft—grab an appropriate puller and expect rusted races to fight all the way off before reassembly.【F:knowledge/notes/input_part002_review.md†L665-L665】

## Brake Service & Fluid Recovery
- **Stick with mineral oil systems.** DOT 5/5.1 swell the silicone seals inside Magura and Shimano calipers; the group now defaults to mineral oil and favours Trickstuff Bionol for its 300–420 °C boiling range on scooters that regularly cook stock fluid.【F:knowledge/notes/input_part002_review.md†L24-L26】
- **Budget proper hose hardware.** Upgrading to Jagwire Pro or similar hoses still demands the correct olives and barbs on each end or the lever will leak once re-terminated.【F:knowledge/notes/input_part002_review.md†L26-L26】
- **Add sensors while you’re inside.** Flood-recovery work now includes bonding hall or reed sensors to hydraulic levers so riders gain proportional regen or kill-switch signalling without hunting rare OEM parts.【F:knowledge/notes/input_part002_review.md†L27-L27】
- **Clean flooded brakes correctly.** Strip pads and attack rust with dedicated brake cleaner—WD-40 or silicone spray swells seals and leaves corrosion; save PTFE lubes for finishing touches once everything is dry.【F:knowledge/notes/input_part002_review.md†L29-L30】

## Controller & Motor Tests
- **Continuity sweep before power-up:** With the battery unplugged, probe between B+ / B− and each motor phase. Any reading below ~50 Ω signals a shorted MOSFET that must be replaced before reconnecting cells.【F:knowledge/notes/denis_all_part02_review.md†L37-L38】
- **Hall sensor alignment:** Preserve the original spacing when replacing hall ICs—swapping long packages for short ones costs roughly 10 km/h, and forgetting isolation pads risks shorting MOSFETs to the case.【F:knowledge/notes/denis_all_part02_review.md†L40-L41】
- **Seat hub thermistors correctly.** Nest the probe between stator windings, secure only the lead with silicone, and leave the tip free so it survives heat cycles without insulating itself.【F:data/vesc_help_group/text_slices/input_part002.txt†L14118-L14124】
- **Route 100 kΩ NTCs through proper harnesses.** Tie one lead to hall ground, the other to the VESC temp input, and consider swapping to a Higo L1019 harness with 3×11 AWG phase cores plus eight signal pins if you need the extra conductor through the axle.【F:knowledge/notes/input_part002_review.md†L663-L664】
- **Reorder halls before blaming firmware.** Mirono’s surging vanished after rewiring a 2-1-3 harness back to 1-2-3 and lowering sensorless handover from 2 000 ERPM to 1 200 ERPM—VESC auto-detect can pass with mis-sequenced halls yet still misfire under load.【F:data/vesc_help_group/text_slices/input_part002.txt†L14506-L14532】【F:data/vesc_help_group/text_slices/input_part002.txt†L14820-L14824】
- **Data-line triage after regen faults:** Error 21 that appears immediately after an emergency stop usually points to a cooked controller data line. Bench-test the pack on a known-good scooter or send it in rather than reflashing firmware blindly.【F:knowledge/notes/denis_all_part02_review.md†L368-L369】
- **Backfeed with care:** A depleted 44 V pack can be nudged awake with a 36 V charger only when its open-circuit voltage sits under ~41 V. Anything higher risks over-voltage damage once the charger’s CV phase kicks in.【F:knowledge/notes/denis_all_part02_review.md†L37-L38】
- **Log Rita/Happy current spikes:** Error 39 beeps and thermal cutbacks appear when firmware demands exceed Rita’s ~30 A ceiling; capture live amps with m365Tools before dialing tuning back.【F:knowledge/notes/denis_all_part02_review.md†L55-L57】

## Communications & Firmware Recovery
- **Swap UART pins before panicking.** Spintend adapters that lose Bluetooth after firmware updates usually revive once you swap TX/RX or toggle the BLE module back on in VESC Tool; double-check throttle inputs because some vendors land them on VAL2 instead of the expected channel.【F:knowledge/notes/input_part002_review.md†L222-L223】
- **Configure MKSESC boards from a PC.** The Android Makerbase app hides throttle/brake mapping, so finish setup in desktop VESC Tool, write both configs, and only then flash Izuna’s calibration firmware if the board reports as 75_300_R2.【F:knowledge/notes/input_part002_review.md†L224-L224】
- **Reuse the CAN lead as an SWD cable.** Lost the Spintend SWD pigtail? The four-pin CAN harness matches the pinout (reset line unused), letting you bridge into SWD mode—install STM32 drivers on Windows and verify 3.3 V on the header before escalating to an RMA.【F:knowledge/notes/input_part002_review.md†L235-L236】

## Field Recovery Tricks
- **Wake sleeping packs:** Happy BMS batteries ship dormant—tap them with a charger to enable the discharge MOSFETs before chasing wiring faults.【F:knowledge/notes/denis_all_part02_review.md†L376-L376】
- **Reconnect stubborn externals:** If Rita “ghosts” an auxiliary pack, blip the throttle for a second to force rediscovery before tearing down wiring.【F:knowledge/notes/all_part01_review.md†L209-L210】
- **Time full charges when vetting replacements:** Stock Xiaomi bricks add ≈1.7 Ah per hour; a legitimate 12 Ah Pro 2 pack should need nearly seven hours from empty, so a “full” light in 90 minutes signals a counterfeit pack.【F:knowledge/notes/denis_all_part02_review.md†L230-L231】
- **Probe every series group on dead packs:** When a fresh build refuses to wake, crack the wrap and meter each group—bypassing the BMS is for testing only because running without it is a fire risk.【F:knowledge/notes/denis_all_part02_review.md†L121801-L121804】

## Compliance & Legal Mode Prep
- Pre-configure a 25–30 km/h profile in VESC Tool for roadside checks; Belgian riders have seen scooters confiscated around 50 km/h unless they can demonstrate a compliant mode, and calm street manners help avoid stops altogether.【F:knowledge/notes/input_part002_review.md†L118-L120】

## Security Layers & Theft Response
- Hide GPS trackers along the main harness, combine Rita builds with motion alarms inside the battery bag, and budget a hardened chain for long stops; layered defenses buy recovery time even though determined thieves can still lift a 20 kg scooter.【F:knowledge/notes/all_part01_review.md†L896-L896】

## Deck Waterproofing Lessons
- Kaabo Wolf inspections found water pooling under 20 S packs despite shrink wrap—add silicone layers, Kapton, drain checks, and dielectric grease around series bridges and BMS leads before chasing larger packs.【F:knowledge/notes/input_part002_review.md†L159-L161】
- Foam blocks or printed brackets still matter even with fish paper and shrink: loose packs have rubbed through insulation when slid into decks, so document retention hardware and shipping photos before handoff.【F:knowledge/notes/input_part002_review.md†L264-L264】
- Keep an eye on consumables pricing. A 16 % jump in tyre costs tied to Russian/Ukrainian supply shocks has riders stocking spares before shortages bite.【F:knowledge/notes/input_part002_review.md†L366-L366】

## Charging Gear & Connector Choices
- Budget 0–90 V/5 A AliExpress supplies land around €76 shipped, but owners plan PayPal disputes when deliveries slip; Grin’s Satiator costs more yet saves repeated charger fights and supports higher-quality CC/CV profiles.【F:knowledge/notes/input_part002_review.md†L241-L242】
- Ferrofluid and hubsink upgrades run ~10 % more than generic parts yet buy 15–30 % more continuous performance on €200 hubs—log before/after temps so the spend is justified.【F:knowledge/notes/input_part002_review.md†L243-L244】
- Daly Bluetooth BMS boards let you toggle outputs in-app without sparks, giving antispark-free builds a safe parking routine while still leaning on VESC voltage cutoffs for discharge.【F:knowledge/notes/input_part002_review.md†L262-L263】
- QS8 connectors realistically hold ~70 A continuous; riders chasing slimmer decks swap to 8 mm bullets while leaving XT90S for lower-amp projects because they plateau near 45 A continuous.【F:knowledge/notes/input_part002_review.md†L265-L265】
- Flipsky 75100s sip roughly 5 mA at idle—unplug XT90S loop keys during long storage if you skip antispark switches to avoid slow pack drain.【F:knowledge/notes/input_part002_review.md†L266-L266】

## Documentation & Support Habits
- Keep a photo log of connector routing, ST-Link pinouts, and fuse replacements so future technicians can retrace your steps. Denis’ English manual is updated as new edge cases surface—reference it before opening support tickets.【F:knowledge/notes/all_part01_review.md†L209-L210】

- **Retrofit hall sensors for regen.** Gluing magnets to levers and pairing them with A1324LUA sensors delivers proportional regen on any brake, while Bafang reed kits stay in the toolbox as simple on/off backups.【F:knowledge/notes/input_part002_review.md†L352-L352】
- **Map regen controls deliberately.** Left-hand throttles are taking over regen duty while the right hand stays on drive; VESC mapping even lets an auxiliary on/off lever cap panic stops around 10 A.【F:knowledge/notes/input_part002_review.md†L353-L353】
- **Treat parking-brake shortcuts with caution.** Shorting motor phases can lock a wheel instantly but hammers drivetrains if misused—reserve the trick for supervised maintenance, not street parking.【F:knowledge/notes/input_part002_review.md†L354-L354】
