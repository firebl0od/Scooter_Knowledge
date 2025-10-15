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
8. **Refinish soldered connectors, don’t patch corroded XT60s.** R3VOLT’s refresh reminded the crew to swap oxidised housings entirely, heat the bullet—not the wire—so solder flows, and slide the molded cover back over the last few millimetres before heat-shrinking insulation to prevent shorts.【F:knowledge/notes/input_part007_review.md†L84-L84】
9. **Use drilling jigs when precision holes matter.** Off-the-shelf square-hole guides keep controller and bracket installs tidy for builders who struggle to drill straight freehand.【F:knowledge/notes/input_part007_review.md†L97-L97】

## Controller & Motor Tests
- **Continuity sweep before power-up:** With the battery unplugged, probe between B+ / B− and each motor phase. Any reading below ~50 Ω signals a shorted MOSFET that must be replaced before reconnecting cells.【F:knowledge/notes/denis_all_part02_review.md†L37-L38】
- **Hall sensor alignment:** Preserve the original spacing when replacing hall ICs—swapping long packages for short ones costs roughly 10 km/h, and forgetting isolation pads risks shorting MOSFETs to the case.【F:knowledge/notes/denis_all_part02_review.md†L40-L41】
- **Rebuild Xiaomi hall boards with insulation intact.** Keep the factory fishpaper backing and bed the PCB in neutral-cure RTV 704 before closing the motor so refurbished sensors stay isolated from the stator laminations.【F:knowledge/notes/input_part007_review.md†L487-L487】
- **Data-line triage after regen faults:** Error 21 that appears immediately after an emergency stop usually points to a cooked controller data line. Bench-test the pack on a known-good scooter or send it in rather than reflashing firmware blindly.【F:knowledge/notes/denis_all_part02_review.md†L368-L369】
- **Backfeed with care:** A depleted 44 V pack can be nudged awake with a 36 V charger only when its open-circuit voltage sits under ~41 V. Anything higher risks over-voltage damage once the charger’s CV phase kicks in.【F:knowledge/notes/denis_all_part02_review.md†L37-L38】
- **Log Rita/Happy current spikes:** Error 39 beeps and thermal cutbacks appear when firmware demands exceed Rita’s ~30 A ceiling; capture live amps with m365Tools before dialing tuning back.【F:knowledge/notes/denis_all_part02_review.md†L55-L57】
- **Post-failure VESC triage:** After meltdown events, test each MOSFET drain-to-source, inspect both sides of the board, confirm the Bluetooth module and 5 V rail still light up, then beep between pack leads and every phase before repowering; if the 5 V rail is dead, isolate hall supplies with 1N4148 diodes and inspect the resettable fuses that guard the 12 V/5 V/3.3 V rails and ignite port.【F:knowledge/notes/input_part007_review.md†L31-L32】【F:knowledge/notes/input_part007_review.md†L515-L515】
- **Cure Monorim launch chatter:** If a Monorim build shakes off the line, rerun hall detection, bump the sensored→sensorless handoff to about 3,000 ERPM, and swap to the Ortega observer so the controller transitions cleanly instead of cogging.【F:knowledge/notes/input_part007_review.md†L19-L19】
- **Keep G30/75100 swaps on halls.** Deadword’s Ninebot build only cleared “limited mode” once the motor wizard ran on Ortega with BEMF decoupling, halls stayed enabled for dash speed, and firmware versions matched between VESC Tool and the controller before a power-cycle.【F:knowledge/notes/input_part007_review.md†L405-L405】

## Field Recovery Tricks
- **Wake sleeping packs:** Happy BMS batteries ship dormant—tap them with a charger to enable the discharge MOSFETs before chasing wiring faults.【F:knowledge/notes/denis_all_part02_review.md†L376-L376】
- **Reconnect stubborn externals:** If Rita “ghosts” an auxiliary pack, blip the throttle for a second to force rediscovery before tearing down wiring.【F:knowledge/notes/all_part01_review.md†L209-L210】
- **Time full charges when vetting replacements:** Stock Xiaomi bricks add ≈1.7 Ah per hour; a legitimate 12 Ah Pro 2 pack should need nearly seven hours from empty, so a “full” light in 90 minutes signals a counterfeit pack.【F:knowledge/notes/denis_all_part02_review.md†L230-L231】
- **Probe every series group on dead packs:** When a fresh build refuses to wake, crack the wrap and meter each group—bypassing the BMS is for testing only because running without it is a fire risk.【F:knowledge/notes/denis_all_part02_review.md†L121801-L121804】
- **Go sensorless when halls fail.** If a Zero or similar scooter loses hall sensors mid-ride, drop open-loop ERPM to 0, switch to the Mxlemming observer with BEMF decoupling, and limp home on sensorless starts.【F:knowledge/notes/input_part007_review.md†L403-L404】
- **Recover CAN chains through the survivor.** Change the remaining controller’s VESC ID and reflash the bootloader over the intact CAN link to revive dead peers before opening sealed housings.【F:knowledge/notes/input_part007_review.md†L404-L404】

## Security Layers & Theft Response
- Hide GPS trackers along the main harness, combine Rita builds with motion alarms inside the battery bag, and budget a hardened chain for long stops; layered defenses buy recovery time even though determined thieves can still lift a 20 kg scooter.【F:knowledge/notes/all_part01_review.md†L896-L896】

## Documentation & Support Habits
- Keep a photo log of connector routing, ST-Link pinouts, and fuse replacements so future technicians can retrace your steps. Denis’ English manual is updated as new edge cases surface—reference it before opening support tickets.【F:knowledge/notes/all_part01_review.md†L209-L210】
- **Windows VESC Tool onboarding:** On dual-ESC repairs, plug each controller into USB separately, flash firmware in Read→Write order, and expect the desktop app to expose editable fields that the free iOS build hides—Lyss’ troubleshooting logs show most confusion stems from skipped per-controller sessions.【F:knowledge/notes/input_part007_review.md†L523-L523】

## Mechanical Checks & Ride Diagnostics
- **Balance hubs after impacts.** PuneDir’s post-crash wobble only calmed once the wheel was rebalanced like a motorcycle rim and inspected for bent castings—expect permanent deformation if a car clips the shell.【F:knowledge/notes/input_part007_review.md†L409-L409】
- **Refresh chain-drive consumables.** Even flawless sprockets stay noisy; replace chain, sprockets, and upgrade to sealed 6002 2RS bearings because lightweight 6000-series clones or belt conversions wear out fast on 140 kg loads.【F:knowledge/notes/input_part007_review.md†L411-L411】

## Motor Cleaning & Overhaul
- **Degrease hubs methodically.** Blow dust clear first, then spot-clean contaminants with brake cleaner or alcohol on cotton rags—Happy Giraffe’s Bafang service avoided microfiber because it drags lint into windings.【F:knowledge/notes/input_part007_review.md†L449-L449】

