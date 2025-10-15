# Scooter Diagnostic Toolkit & Field Practices

## Core Instruments
- **Handheld multimeter:** Expect budget meters to ship with 12 V A23 cells and fragile F200 mA fuses—stock replacements and keep a sturdier backup such as the Mustool MT111 on hand for daily troubleshooting.【F:knowledge/notes/all_part01_review.md†L164-L164】
- **Cell testing bench:** Pair LiitoKala or Opus bays with a 3.3 Ω / 25 W Ohmite resistor block so you can discharge or capacity-test loose 18650s before grouping them into packs, especially when customer batteries arrive full.【F:knowledge/notes/all_part01_review.md†L165-L165】
- **Firmware lifeline:** ST-Link V2 programmers remain the fastest recovery path for bricked dashboards, ESCs, and Rita-linked BMS boards—clip onto the pads, flash stock firmware, then resume Bluetooth updates once communications return. Modern Ninebot Max dashboards also demand ST-Link access because recent BLE revisions block OTA downgrades.【F:knowledge/notes/all_part01_review.md†L47-L49】【F:knowledge/notes/all_part01_review.md†L166-L166】【F:knowledge/notes/all_part01_review.md†L331-L331】【F:knowledge/notes/denis_all_part02_review.md†L103-L104】
- **Low-voltage logging:** Keep Bluetooth thermometers or CR2032-powered loggers in the spares bin when validating experimental packs so you can capture temperature spikes before they cook cells.【F:knowledge/notes/all_part01_review.md†L372-L372】
- **Insulation & adhesive supplies:** Stock RTV silicone, Kapton, and zip ties to strain-relieve DC/DC converters and harnesses; vibration snaps converter leads unless they are glued or tied back to the PCB before the scooter ever rolls.【F:knowledge/notes/denis_all_part02_review.md†L31-L32】
- **Reliable FDM printers:** Skip wobble-prone Ender 3 V3 SE units—teams are grabbing discounted Bambu Lab A1/A1 Mini machines for fixtures because they print accurately out of the box.【F:knowledge/notes/input_part008_review.md†L55-L55】

## Wiring & Harness Checks
1. **Start at the XT30:** After any crash or curb strike, verify the adapter output voltage before chasing other faults; browned phase pins or half-seated BMS harnesses are the most common culprits when scooters power-cycle on bumps.【F:knowledge/notes/all_part01_review.md†L195-L195】
2. **Inspect pack protection:** Cheap “25 A” eBay BMS boards routinely trip around 18 A despite balanced cell groups—swap in reputable 20–30 A hardware before blaming Rita or the controller for brownouts.【F:knowledge/notes/all_part01_review.md†L172-L172】
3. **Match radio gear:** Immobiliser and alarm kits ship in multiple frequencies; confirm your remote (315 MHz vs. 415 MHz) before hard-wiring to the scooter’s 5 V accessory tap so the system actually arms.【F:knowledge/notes/all_part01_review.md†L167-L167】
4. **Treat locks as consumables:** Light cable locks such as compact Master Lock loops work for coffee stops only if they stay lubricated with graphite—dry mechanisms jam quickly after rain or grit exposure.【F:knowledge/notes/all_part01_review.md†L191-L191】
5. **Identify controller silicon before flashing.** New Xiaomi ESCs use GD32 MCUs; flashing STM firmware bricks them, so zoom in on chip markings and grab the GD image set before running ST-Link recoveries.【F:knowledge/notes/denis_all_part02_review.md†L95680-L95780】
6. **Secure accessory power taps.** Dashboards only expose 5 V logic—drive headlights and horns from a dedicated DC/DC converter, tie the output wires to the board with RTV, and route the harness away from moving stems so the leads do not fatigue.【F:knowledge/notes/denis_all_part02_review.md†L28-L32】【F:knowledge/notes/denis_all_part02_review.md†L31-L32】
7. **Trace weak 5 V accessory ports back to the buck converter.** A Max G30 plug that still shows 5 V but no current usually means a failed converter stage—follow the trace with a multimeter until you reach the DC/DC module and verify components between it and the port before ordering a replacement board.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L110038-L110041】
8. **Inspect Zero/Vsett harnesses after motor swaps.** One Zero 10X 50H build ripped the combined phase/hall loom entirely—strain-relieve new looms and document pinouts before closing the deck.【F:knowledge/notes/input_part008_review.md†L322-L322】
9. **Chase 5 V shorts by elimination.** Disconnect each accessory and recheck the regulator rail; once the shorted branch is found, recalibrate throttle min/max to confirm the sensor survived the fault.【F:knowledge/notes/input_part008_review.md†L511-L516】

## Controller & Motor Tests
- **Continuity sweep before power-up:** With the battery unplugged, probe between B+ / B− and each motor phase. Any reading below ~50 Ω signals a shorted MOSFET that must be replaced before reconnecting cells.【F:knowledge/notes/denis_all_part02_review.md†L37-L38】
- **Hall sensor alignment:** Preserve the original spacing when replacing hall ICs—swapping long packages for short ones costs roughly 10 km/h, and forgetting isolation pads risks shorting MOSFETs to the case.【F:knowledge/notes/denis_all_part02_review.md†L40-L41】
- **Data-line triage after regen faults:** Error 21 that appears immediately after an emergency stop usually points to a cooked controller data line. Bench-test the pack on a known-good scooter or send it in rather than reflashing firmware blindly.【F:knowledge/notes/denis_all_part02_review.md†L368-L369】
- **Backfeed with care:** A depleted 44 V pack can be nudged awake with a 36 V charger only when its open-circuit voltage sits under ~41 V. Anything higher risks over-voltage damage once the charger’s CV phase kicks in.【F:knowledge/notes/denis_all_part02_review.md†L37-L38】
- **Log Rita/Happy current spikes:** Error 39 beeps and thermal cutbacks appear when firmware demands exceed Rita’s ~30 A ceiling; capture live amps with m365Tools before dialing tuning back.【F:knowledge/notes/denis_all_part02_review.md†L55-L57】
- **Validate Makerbase adapter baselines:** The Adapter V2 throttle bridge should idle near 0.8 V—anything higher signals wiring faults or a failed board before you flash firmware or re-pin connectors.【F:knowledge/notes/input_part008_review.md†L516-L517】
- **Chase Spin-Y2 reboot loops methodically:** When a Spin-Y2 throttle repeatedly kills power on a Spintend build, reflash firmware, confirm the BMS isn’t tripping, rerun motor detection, and only then tear into wiring—the step-by-step approach cleared Alex’s looping fault without replacing hardware.【F:knowledge/notes/input_part008_review.md†L617-L623】
- **Check Makerbase Bluetooth daughterboards for shorts:** Overheated antenna tabs have killed the 3.3 V rail—inspect every supply, swap TX/RX, and escalate to the vendor once the blue LED stays dark even after rewiring.【F:knowledge/notes/input_part008_review.md†L18981-L19011】

## Telemetry & Data Capture
- **Background logging works.** VESC Tool keeps recording logs while the Android app runs in the background, so you can foreground GPS overlays or dashboards during speed tests without losing current traces.【F:knowledge/notes/input_part008_review.md†L257-L257】
- **Prefer controller logs for speed math.** High-speed GPS overlays have drifted by ~7 km over a run; riders now rely on VESC logs for trustworthy speed traces before publishing results.【F:knowledge/notes/input_part008_review.md†L258-L258】
- **Plan for sensorless coasting.** VESC firmware estimates speed from back-EMF even with halls unplugged, but freewheeling geared hubs can drop to zero when coasting—pair the logs with GPS or auxiliary sensors if you rip the hall board out entirely.【F:knowledge/notes/input_part008_review.md†L617-L623】
- **Mirror telemetry to CarPlay.** Jailbroken iOS or custom Android bridges can mirror VESC dashboards onto a helmet HUD or phone, giving riders higher-visibility data during testing.【F:knowledge/notes/input_part008_review.md†L507-L509】
- **Archive EY dash firmware.** Dualtron EY1/EY2/EY4 clusters run WCH CH582M MCUs and flash over WCHISPStudio; keep the published EY2 hex handy for recovery before experimenting with BLE scripts.【F:knowledge/notes/input_part008_review.md†L509-L512】

## Field Recovery Tricks
- **Wake sleeping packs:** Happy BMS batteries ship dormant—tap them with a charger to enable the discharge MOSFETs before chasing wiring faults.【F:knowledge/notes/denis_all_part02_review.md†L376-L376】
- **Reconnect stubborn externals:** If Rita “ghosts” an auxiliary pack, blip the throttle for a second to force rediscovery before tearing down wiring.【F:knowledge/notes/all_part01_review.md†L209-L210】
- **Time full charges when vetting replacements:** Stock Xiaomi bricks add ≈1.7 Ah per hour; a legitimate 12 Ah Pro 2 pack should need nearly seven hours from empty, so a “full” light in 90 minutes signals a counterfeit pack.【F:knowledge/notes/denis_all_part02_review.md†L230-L231】
- **Probe every series group on dead packs:** When a fresh build refuses to wake, crack the wrap and meter each group—bypassing the BMS is for testing only because running without it is a fire risk.【F:knowledge/notes/denis_all_part02_review.md†L121801-L121804】

## Chassis & Suspension Quick Fixes
- **Rebuild sloppy folding clamps:** Shim ovalized bushings with thin metal or heat-shrink and lock every fastener with threadlocker so the top plate stops wallowing out mid-ride.【F:knowledge/notes/input_part008_review.md†L54-L54】
- **Tune cheap steering dampers:** Swap generic damper fluid for 10W/60 shock oil or Citroën LHM+ to regain adjustability without chewing seals, especially on freebie take-offs.[^damper-oil]
- **Favor suspended frames for high-power conversions:** Ninebot Max G2 chassis with suspension outlast rigid G30 decks under vibration, SNSC rental frames survive high-speed crashes with minimal damage, and DNM shock/13"×7" tire combos plus lever-free hub tire removals keep service visits efficient.【F:knowledge/notes/input_part008_review.md†L316-L316】

## Tire & Traction Observations
- **Balance electronics with mechanics:** Traction control helps rein front-wheel slip up to ~55 mph, but riders still cut front phase amps to keep dual-drive scooters manageable in launches.【F:knowledge/notes/input_part008_review.md†L74-L74】
- **Match tires to power levels:** Xuancheng 12" slicks stay budget-friendly but spin under hard launches, so high-power builds migrate to CST or PMT rubber; on 6" rims, Tuovt 90/55-6 casings grip better than CST 90/65-6 while oversized 6.5" skins pinch split rims and look sloppy.【F:knowledge/notes/input_part008_review.md†L75-L78】
- **Pick tires for the surface, not hype:** Riders are steering 10" Zero/Vsett owners toward CST 10×3 or PMT 10×3.5 rubber, calling Xuancheng slicks short-lived above 4 kW without traction control, and leaning on Tuovt 90/55-6 for broken pavement longevity.【F:knowledge/notes/input_part008_review.md†L348-L350】
- **Address pinch flats proactively:** Vsett 9 owners fighting split-rim pinch flats now double heavy-duty Ulip tubes, dust them with baby powder during install, and experiment with 3D-printed bead covers to protect the tube crease.【F:knowledge/notes/input_part008_review.md†L79-L79】

## Security Layers & Theft Response
- Hide GPS trackers along the main harness, combine Rita builds with motion alarms inside the battery bag, and budget a hardened chain for long stops; layered defenses buy recovery time even though determined thieves can still lift a 20 kg scooter.【F:knowledge/notes/all_part01_review.md†L896-L896】

## Documentation & Support Habits
- Keep a photo log of connector routing, ST-Link pinouts, and fuse replacements so future technicians can retrace your steps. Denis’ English manual is updated as new edge cases surface—reference it before opening support tickets.【F:knowledge/notes/all_part01_review.md†L209-L210】

## Mini-Bike & Fiido L3 Conversions
- **Respect the stock controller limits:** Fiido L3 controllers float loose without heatsinks and only deliver ~25 A; jumping straight to 20 S test packs without pre-charging popped factory BMS units. Match pack voltages before connecting higher-voltage VESC hardware.【F:knowledge/notes/input_part008_review.md†L381-L381】
- **Dial conservative currents:** After cutting battery current to ~20 A, setting traction control to 20/20 A, and capping phase around 60 A with FW, builders hit 45 km/h and repeatable wheelies without overheating the compact hub.【F:knowledge/notes/input_part008_review.md†L382-L382】
- **Plan full teardowns:** Packs are heavily sealed—glued busbars, soldered fasteners, and tripped protection boards left entire parallel groups at 0 V—so refurb projects require full BMS removal rather than capacitor swaps.【F:knowledge/notes/input_part008_review.md†L383-L383】

[^damper-oil]: PuneDir’s free steering damper only behaved after switching to lighter fluids; veterans now recommend 10W/60 shock oil or Citroën LHM+ to preserve seals while restoring adjustability.【F:knowledge/notes/input_part008_review.md†L56-L56】

