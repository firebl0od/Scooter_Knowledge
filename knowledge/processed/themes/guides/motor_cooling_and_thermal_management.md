# Motor Cooling & Thermal Management Notes

## Why Fans Rarely Help Scooter Hubs
- Denis Yurev reminded the workshop that scooters already move fresh air past the hub at riding speed, so bolt-on fan kits add little cooling compared with ensuring good heat transfer from the windings to the shell.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L422-L441】
- Riders debating CPU-style blowers learned that evaporation-driven skin cooling does not apply to dry aluminum shells; without a wet surface the only lever is temperature delta, so focus on conductive paths instead of add-on spinners.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L424-L441】
- Veterans recommended ferrofluid or oil-fill experiments (with leak safeguards) if you need real winding-to-shell transfer—simply drilling covers or gluing “windmills” to the hub only cools the outer case.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part01.txt†L456-L520】
- 2024 Weeped experiments reiterated the fundamentals: relocate VESCs off thin steel plates, add thermal pads/paste, and prioritise airflow before adopting mini water loops that add leak points and weight.【F:knowledge/notes/input_part010_review.md†L24-L26】
- Lieven reminded high-speed builders that airflow alone cannot match a radiator’s surface area; once relocation and paste upgrades stall out, a compact water loop becomes the next lever for keeping 90 mph controllers inside their thermal envelope.【F:data/vesc_help_group/text_slices/input_part010.txt†L11248-L11250】
- Noname kept dual controllers under control by bolting them to a shared 9 × 12 inch heatsink with thermal pads and paste, noting paste losses are minor compared with the added fin area; later tests kept a single controller under ~40 °C at 6 kW while planning ram-air ducting to push temps lower.【F:knowledge/notes/input_part010_review.md†L162-L164】
- Jan cautioned that drilling water jackets into hubs still leaves them mostly passive unless you engineer full closed-loop plates, pumps, and radiators; budget CPU coolers or open cavities just add drag in the magnetic path without removing meaningful heat.【F:data/vesc_help_group/text_slices/input_part010.txt†L11334-L11367】
- Recent hub debates echoed the same lesson: bolt-on fins or cover plates barely move the needle because the stator still floats inside an air gap—builders only saw meaningful improvements with sealed quick-connect water loops or by switching to mid-drives entirely.【F:knowledge/notes/input_part010_review.md†L238-L240】
- Side-cover fins only help when paired with ferrofluid; otherwise the air gap insulates the stator and vent drilling invites debris without measurably lowering temperatures.【F:knowledge/notes/input_part010_review.md†L26-L27】
- Ferrofluid moves heat into the side plates, allowing “hand-test” cooldowns by spinning wheels unloaded rather than riding on overheated copper—use VESC Tool’s input hand test to validate throttle and brake signals before each session.【F:knowledge/notes/input_part010_review.md†L27-L27】

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
- Swap out low-temp hot glue for high-temp silicone or epoxy when reseating hall PCBs; standard sticks slump around 120 °C whereas RTV keeps sensors planted even on smaller hubs that still crest triple-digit winding temps.【F:data/vesc_help_group/text_slices/input_part010.txt†L11203-L11215】
- Bench-test replacement hall boards before soldering—the Slack crew keeps finding occasional DOA sensors, so meter outputs first and only commit once each channel toggles correctly.【F:data/vesc_help_group/text_slices/input_part010.txt†L11224-L11229】
- Keep spare 60° 41F hall boards on hand for Wolf King GT and other 60 H Kaabo hubs; AYO#74 validated the common AliExpress kit as a direct drop-in for 2 kW-class motors.【F:data/vesc_help_group/text_slices/input_part010.txt†L11226-L11239】
