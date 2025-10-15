# Motor Cooling & Thermal Management Notes

## Why Fans Rarely Help Scooter Hubs
- Denis Yurev reminded the workshop that scooters already move fresh air past the hub at riding speed, so bolt-on fan kits add little cooling compared with ensuring good heat transfer from the windings to the shell.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L422-L441】
- Riders debating CPU-style blowers learned that evaporation-driven skin cooling does not apply to dry aluminum shells; without a wet surface the only lever is temperature delta, so focus on conductive paths instead of add-on spinners.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L424-L441】
- Veterans recommended ferrofluid or oil-fill experiments (with leak safeguards) if you need real winding-to-shell transfer—simply drilling covers or gluing “windmills” to the hub only cools the outer case.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L456-L520】

## Controller Interface Refresh Checklist
- When raising voltage, replace Kapton tape with 0.5 mm thermal pads so MOSFETs stay isolated yet shed heat; stacking pads on top of Kapton just adds resistance.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L202-L223】
- Sand controller bases, clean MOSFET tabs, and reinstall paste before clamping the box—loose wiring under the plate prevents full contact and spikes temperatures on the first ride.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60020-L60025】
- Keep silicone pads on hand when chasing 48 V/15 S tunes; the crew pairs IRFB4110 MOSFETs with 100 V 1,000 µF and 47 µF capacitors and swaps pads plus paste before closing the case.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60009-L60024】

## Temperature Guardrails
- Battery temps around 41 °C were deemed healthy for summer rides, but the group flagged ~60 °C as a ceiling—anything hotter accelerates degradation and calls for gentler tunes.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60004-L60008】
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
