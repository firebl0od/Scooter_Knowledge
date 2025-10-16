# Motor Configuration Insights

## Delta Winding Considerations

- Delta-configured hub motors on 36 V systems produced voltage spikes exceeding 100 V, and long-term reliability with VESC hardware remains unproven without alternative firmware or controller pairings.[^delta_spikes]
- Stock Xiaomi and Segway controllers tolerated aggressive delta settings with battery currents above 56 A, but multiple ESCs failed when chasing ~70 km/h on 10 S packs.
  - higher-voltage 48 V packs increased the stress.[^delta_failures]

## Real-World Power Benchmarks

- Dual Minimotors controllers fed by a 54 Ah pack delivered ~90 km at 38 km/h, but riders noted VESC tunes feel more conservative and emphasised monitoring energy use when comparing platforms.[^minimotors_range]
- 2 000 W hub motors begin to warm after ~3 km at 60 A battery / 100 A phase, pushing builders toward 3 000 W swaps to sustain 3–4 kW bursts without cooking stators.[^2000w_heat]
- Dualtron Spider conversions are running 135 A motor / 35 A battery per channel with 100 A regen per motor, highlighting how easily stock packs sag when asked for ~260 A combined bursts.[^spider_current]

## Voltage Strategy & Stress Tests

- Stepping from 16 S to 20 S trims current for the same wattage and adds roughly 2.5 km/h per extra series cell, but 100 V-rated MOSFETs run ~33 % higher Rds(on) than 75 V parts and longer packs demand better insulation and safety checks.
  - plan enclosure space before chasing headline voltage gains.[^1]
- Chasing extreme speed on low voltage pushes currents to impractical levels; balance motor geometry, series/parallel splits, and packaging rather than fixating on a single voltage target.[^2]
- Overvolting small hubs is unforgiving.
  - feeding an 800 W Citycoco motor with 26 S and 100 A cooked it on an uphill pull, underscoring how quickly winding heat saturates when voltage and current climb together.[^3]

## Sensorless & Hall Workflow

- Sensorless HFI tuning only behaves when the motor shows at least a ≈15 % Ld/Lq delta from `measure_ind`; once dialled, riders report near-hall launch torque with only faint startup whine, making it a viable fallback when hall harnesses fail.[^4]
- Keep VESC clients tethered during shakedowns; controllers only log faults while a phone or PC is connected, so xmatic or VESC Tool must stay open if you want post-run diagnostics on dead VESCs.[^5]

## Motor Specification Notes

- Wheelway “1 000 W” hubs hide modest 36 mm magnet stacks versus 60 mm on the 1 200 W variant; treat nameplate wattage as marketing and compare stator width, magnet depth, and real amp tolerance instead.[^6]
- G30 rental motors include a brown lead for the embedded 10 k/100 k NTC.
  - tie it into VESC temp rollback because hub covers stay cool even while windings approach 80 °C.[^7]
- Artem catalogued the Vsett 9/9+ hub (92 mm stator, 30 magnets, 9/7 wind with 0.5 mm strands, RUWH 6003RS bearings) and logged the 10+ wheel around 62 km/h on 48 V at 35 A despite 60 V marketing claims, so plan gearing or voltage upgrades if you need more top speed.[^8]
- HM’s 60 V 1.6–3.5 kW hubs ship for ≈€160 from Spain but arrive with conservative 25/37 A current recommendations.
  - builders intend to validate phase-amp headroom before trusting the spec sheet.[^9]
- PaoloWu’s Blade 10 hub remains the go-to Xiaomi drop-in: riders report 55–60 km/h on 13 S, ~65 km/h with field weakening, and reliable ~150 A phase tolerance for roughly €150 plus shipping, while Zero 10X and Boyueda alternatives cost more for similar kv.[^10]
- Pandalgns opened a 3 kW hub’s axle from 8 mm to 10 mm to feed 12 AWG phase leads and 28 AWG hall wiring, reporting only light material removal was needed to preserve shaft strength for 72 V conversions chasing higher phase current.[^axle-drill]
- Marketing wattage is meaningless on Vsett 10+ motors.
  - inspect winding fill and magnet stack height to judge headroom before pushing phase amps or buying donor wheels for AWD swaps.[^11]
- Happy Giraffe logged key Blade hub dimensions (130 mm inner axle, ≈160 mm fork span, M12 threads with 10 mm flats, 12 mm rotor offset, 4 mm hex hardware) and confirmed the shell is tubeless-ready, giving Xiaomi builders a reference checklist before ordering forks and spacers.[^12]
- PuneDir’s sluggish 27 H rear hub shows why some regions need to source QS or YM motors locally when customs block AliExpress imports.[^pundir-27h]
- Jetson minibike 72 V Sabvoton swaps pull about 30 A but still demand vigilant motor temperature monitoring until a cleaner all-internal VESC solution lands.[^jetson-minibike]
- Rage Mechanics’ 75 mm stator motors are sustaining 10 kW per wheel on Weped platforms but cost ≈€650 each and require wider axles.
  - plan chassis spacing before chasing 120 km/h builds with them.[^13]

## Hall Sensor Repair & Orientation

- Replace Ninebot G30 hall ICs with the matching part numbers (SS41F vs. R43) and keep the stamped face oriented the same direction; mismatched or reversed sensors output ~2 V constantly and will not sync until the firmware detects proper alignment.[^14]
- Superglue or RTV secures loose sensors, but rerun motor detection and temporarily cap limits around 40 A battery / 80 A phase after repairs until you source proper hall spares.[^15]
- Skip hot glue on hall boards—🇪🇸AYO#74 and `lekrsu` now rely on high-temp silicone or epoxy because hot glue softens near 120 °C and lets sensors drift during hub heat cycles.[^hall-adhesive]
- Kaabo Wolf King GT 60 H motors accept a 60° AliExpress hall board that 🇪🇸AYO#74 vetted; stock a spare before refurbishing large hubs.[^wolf-hall]

## Efficiency & Range Benchmarks

- Artem’s Xiaomi/Ninebot comparisons underline controller influence on consumption: the stock 52 V 13 Ah square-wave setup burned ~26 Wh/km wide open, his dual-motor VESC trimmed it to ~22.5 Wh/km at higher speeds, and the sine-modulated Vsett achieved ~17 Wh/km when limited to 676 Wh at 25–35 km/h.[^16]
- Range planning threads now scale PaoloWu Blade hub claims to real loads.
  - expect roughly 65 km/h on 13 S with field weakening but closer to 50 km/h once rider mass and sag are factored in, helping commuters size forks and gearing before ordering kits.[^17]

[^delta_spikes]: Source: knowledge/notes/input_part000_review.md, line 40.
[^delta_failures]: Source: knowledge/notes/input_part000_review.md, line 41.
[^minimotors_range]: Source: knowledge/notes/input_part000_review.md, line 165.
[^2000w_heat]: Source: knowledge/notes/input_part000_review.md, line 166.
[^spider_current]: Source: knowledge/notes/input_part000_review.md, line 167.


## References

[^1]: Source: knowledge/notes/input_part000_review.md†L601-L604
[^2]: Source: knowledge/notes/input_part000_review.md†L604-L604
[^3]: Source: knowledge/notes/input_part000_review.md†L728-L731
[^4]: Source: knowledge/notes/input_part000_review.md†L381-L381
[^5]: Source: knowledge/notes/input_part000_review.md†L382-L382
[^6]: Source: knowledge/notes/input_part000_review.md†L385-L385
[^7]: Source: knowledge/notes/input_part000_review.md†L386-L386
[^8]: Source: knowledge/notes/input_part000_review.md†L387-L387
[^9]: Source: knowledge/notes/input_part000_review.md†L388-L388
[^10]: Source: knowledge/notes/input_part000_review.md†L434-L440
[^11]: Source: knowledge/notes/input_part000_review.md†L440-L443
[^12]: Source: knowledge/notes/input_part000_review.md†L502-L505
[^13]: Source: knowledge/notes/input_part000_review.md†L494-L498
[^14]: Source: knowledge/notes/input_part000_review.md†L391-L391
[^15]: Source: knowledge/notes/input_part000_review.md†L392-L392
[^hall-adhesive]: Source: knowledge/notes/input_part010_review.md†L517-L518
[^wolf-hall]: Source: knowledge/notes/input_part010_review.md†L518-L519
[^axle-drill]: Source: knowledge/notes/input_part010_review.md†L549-L550
[^pundir-27h]: Source: knowledge/notes/input_part010_review.md†L636-L636
[^16]: Source: knowledge/notes/input_part000_review.md†L486-L489
[^17]: Source: knowledge/notes/input_part000_review.md†L489-L493

[^jetson-minibike]: knowledge/notes/input_part010_review.md†L683-L683
