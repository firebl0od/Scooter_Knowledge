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

## Coil Retention & Harness Dressing
- Inside hub motors, standard nylon cable ties survive stator temperatures when cinched correctly; some builders still wrap phases with cotton rope for redundancy, so combining both methods keeps windings tight without melting ties.【F:knowledge/notes/input_part014_review.md†L185-L185】

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

## Source Notes
[^vsett_rebuild]: VSETT hub overheating and methodical repair procedure.【F:knowledge/notes/input_part004_review.md†L19-L19】【F:knowledge/notes/input_part004_review.md†L94-L94】
[^sensorless_handoff]: Sensorless handoff tuning to cure heat-related stutter.【F:knowledge/notes/input_part004_review.md†L20-L20】【F:knowledge/notes/input_part004_review.md†L96-L97】
[^ntc_install]: Motor temperature sensor installation using EPCOS B57861S0502F040 NTCs.【F:knowledge/notes/input_part004_review.md†L44-L44】【F:knowledge/notes/input_part004_review.md†L69-L69】
[^temp_routing]: Temperature sensor wiring away from phase bundles to avoid ground loops.【F:knowledge/notes/input_part004_review.md†L49-L49】
[^60h_baseline]: 60H hub baseline tuning with ferrofluid and field-weakening.【F:knowledge/notes/input_part004_review.md†L36-L36】
