# Motor Configuration Insights

## Delta Winding Considerations

- Delta-configured hub motors on 36 V systems produced voltage spikes exceeding 100 V, and long-term reliability with VESC hardware remains unproven without alternative firmware or controller pairings.[^delta_spikes]
- Stock Xiaomi and Segway controllers tolerated aggressive delta settings with battery currents above 56 A, but multiple ESCs failed when chasing ~70 km/h on 10 S packs.
  - higher-voltage 48 V packs increased the stress.[^delta_failures]

## Real-World Power Benchmarks

- Xiaomi commuters chasing 50–70 km/h keep stressing that the small tires, modest brakes, and lightweight chassis leave no safety margin—treat protective gear and realistic targets as part of every high-speed plan.[^xiaomi_speed_risk]
- Dual Minimotors controllers fed by a 54 Ah pack delivered ~90 km at 38 km/h, but riders noted VESC tunes feel more conservative and emphasised monitoring energy use when comparing platforms.[^minimotors_range]
- Monorim is prototyping a dual-motor controller that drives two hubs from a single ECU, while proven AWD scooters such as François’ build still split roughly 65 A across twin controllers to stay cool.[^monorim_dual]
- 2 000 W hub motors begin to warm after ~3 km at 60 A battery / 100 A phase, pushing builders toward 3 000 W swaps to sustain 3–4 kW bursts without cooking stators.[^2000w_heat]
- Sustained 27 A hill climbs have already shaken magnets loose inside Pro 2 hubs, leaving the motor howling and efficiency permanently down—active cooling or beefier hubs are mandatory for that duty cycle.[^magnet_shake]
- Stock 300 W Pro hubs cook within minutes once power climbs past 1 kW, whereas Monorim’s 500 W motor tolerates ~2 kW bursts much better under wind loads, underscoring why higher-current tunes pair with hub upgrades.[^monorim_500w_margin]
- Motor Kv dictates trade-offs: the 250 W stator keeps torque with less heat but caps speed, the 300 W Pro motor balances torque and pace, and the 350 W hub overvolts well but demands far more current and cooling for hill climbs—reinforced 13 S/10″ builds have touched 60–70 km/h downhill when everything holds together.[^motor_kv_tradeoffs]
- Monorim’s 500 W solid tire collapses under hard launches; either drill the rim for pneumatic rubber or stay on genuine Xuancheng tires before chasing 48 V tunes.[^monorim_solid_collapse]
- Ninebot Max Gen 2 hubs have hit 5 kW and 125 km/h unloaded on 16 S VESC benches, but the casing does not bolt into Xiaomi frames without Monorim brackets or welding, and early Gen 1 wheels trade top speed for torque.[^g30_overvolt_benchmark]
- Rita-based AWD builds essentially double everything—two ESCs, BLEs, motors, and matched batteries—to avoid voltage sag, while single-motor riders smooth launches by rolling at ~3 km/h before hitting the throttle.[^rita_awd]
- Dualtron Spider conversions are running 135 A motor / 35 A battery per channel with 100 A regen per motor, highlighting how easily stock packs sag when asked for ~260 A combined bursts.[^spider_current]

## Voltage Strategy & Stress Tests

- Dual 13 S packs plateau around 40–42 km/h because Xiaomi controllers clamp speed internally even when voltage rises—plan controller swaps if higher top speed is the goal.[^dual13s_plateau]
- 12 S 350 W hubs record ~47 km/h at ≈28 A, while 14 S builds with 75 kg riders nudge 49–52 km/h; the extra pace demands cooling upgrades and stronger brakes.[^12s_14s_speed]
- VTA 14 S controllers keep drive current near 32 A but limit regen around 20 A to spare VBEC stages and MOSFETs; braking feels stronger than 12 S tunes even at lower negative amps.[^vta_regen_cap]
- Stepping from 16 S to 20 S trims current for the same wattage and adds roughly 2.5 km/h per extra series cell, but 100 V-rated MOSFETs run ~33 % higher Rds(on) than 75 V parts and longer packs demand better insulation and safety checks.
  - plan enclosure space before chasing headline voltage gains.[^1]
- Chasing extreme speed on low voltage pushes currents to impractical levels; balance motor geometry, series/parallel splits, and packaging rather than fixating on a single voltage target.[^2]
- Overvolting small hubs is unforgiving.
  - feeding an 800 W Citycoco motor with 26 S and 100 A cooked it on an uphill pull, underscoring how quickly winding heat saturates when voltage and current climb together.[^3]
- Nameplate wattage assumes nominal voltage: a “1 000 W 48 V” hub draws roughly 1.75 kW on 84 V (20 S), so size controllers and MOSFETs—think IRFB4110-class or VESC hardware—before chasing headline voltage.[^nameplate_scaling]

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
- Monorim’s 500 W hub is built for 48 V—on 10 S it behaves like a 375 W motor—so pair it with 13 S packs and reinforced controllers (caps, MOSFETs, traces) if you expect it to survive.[^monorim_48v]
- Trampa VESC upgrades can deliver ~78 km/h bursts on 12 S ebike builds but require extra cooling, torque arms, and motorcycle-grade protection before exploring 70–80 A targets.[^trampa_highspeed]
- Seat phase connectors firmly: solder the flat side of each lug to the controller pins so heat does not build and melt housings on high-current stems.[^phase_connector_solder]
- PaoloWu’s Blade 10 hub remains the go-to Xiaomi drop-in: riders report 55–60 km/h on 13 S, ~65 km/h with field weakening, and reliable ~150 A phase tolerance for roughly €150 plus shipping, while Zero 10X and Boyueda alternatives cost more for similar kv.[^10]
- Marketing wattage is meaningless on Vsett 10+ motors.
  - inspect winding fill and magnet stack height to judge headroom before pushing phase amps or buying donor wheels for AWD swaps.[^11]
- Happy Giraffe logged key Blade hub dimensions (130 mm inner axle, ≈160 mm fork span, M12 threads with 10 mm flats, 12 mm rotor offset, 4 mm hex hardware) and confirmed the shell is tubeless-ready, giving Xiaomi builders a reference checklist before ordering forks and spacers.[^12]
- Rage Mechanics’ 75 mm stator motors are sustaining 10 kW per wheel on Weped platforms but cost ≈€650 each and require wider axles.
  - plan chassis spacing before chasing 120 km/h builds with them.[^13]
- Fitting Ninebot G30 hubs into Xiaomi frames means mixing two Monorim kits, machining spacers, lengthening phase leads, and slightly enlarging controller plugs before the motor seats reliably.[^g30_swap_fitment]

## Hall Sensor Repair & Orientation

- Replace Ninebot G30 hall ICs with the matching part numbers (SS41F vs. R43) and keep the stamped face oriented the same direction; mismatched or reversed sensors output ~2 V constantly and will not sync until the firmware detects proper alignment.[^14]
- Superglue or RTV secures loose sensors, but rerun motor detection and temporarily cap limits around 40 A battery / 80 A phase after repairs until you source proper hall spares.[^15]

## Efficiency & Range Benchmarks

- Artem’s Xiaomi/Ninebot comparisons underline controller influence on consumption: the stock 52 V 13 Ah square-wave setup burned ~26 Wh/km wide open, his dual-motor VESC trimmed it to ~22.5 Wh/km at higher speeds, and the sine-modulated Vsett achieved ~17 Wh/km when limited to 676 Wh at 25–35 km/h.[^16]
- Range planning threads now scale PaoloWu Blade hub claims to real loads.
  - expect roughly 65 km/h on 13 S with field weakening but closer to 50 km/h once rider mass and sag are factored in, helping commuters size forks and gearing before ordering kits.[^17]

[^delta_spikes]: Source: knowledge/notes/input_part000_review.md, line 40.
[^delta_failures]: Source: knowledge/notes/input_part000_review.md, line 41.
[^minimotors_range]: Source: knowledge/notes/input_part000_review.md, line 165.
[^monorim_dual]: Source: knowledge/notes/all_part01_review.md†L618-L618
[^2000w_heat]: Source: knowledge/notes/input_part000_review.md, line 166.
[^magnet_shake]: Source: knowledge/notes/all_part01_review.md†L686-L686
[^rita_awd]: Source: knowledge/notes/all_part01_review.md†L688-L688
[^monorim_48v]: Source: knowledge/notes/all_part01_review.md†L689-L689
[^xiaomi_speed_risk]: Source: knowledge/notes/all_part01_review.md†L701-L701
[^monorim_500w_margin]: Source: knowledge/notes/all_part01_review.md†L728-L728
[^dual13s_plateau]: Source: knowledge/notes/all_part01_review.md†L729-L729
[^12s_14s_speed]: Source: knowledge/notes/all_part01_review.md†L730-L730
[^vta_regen_cap]: Source: knowledge/notes/all_part01_review.md†L731-L731
[^phase_connector_solder]: Source: knowledge/notes/all_part01_review.md†L737-L737
[^spider_current]: Source: knowledge/notes/input_part000_review.md, line 167.
[^motor_kv_tradeoffs]: Source: knowledge/notes/all_part01_review.md†L855-L855
[^monorim_solid_collapse]: Source: knowledge/notes/all_part01_review.md†L811-L811
[^g30_overvolt_benchmark]: Source: knowledge/notes/all_part01_review.md†L812-L812
[^nameplate_scaling]: Source: knowledge/notes/all_part01_review.md†L857-L857
[^trampa_highspeed]: Source: knowledge/notes/all_part01_review.md†L859-L859
[^g30_swap_fitment]: Source: knowledge/notes/all_part01_review.md†L891-L891


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
[^16]: Source: knowledge/notes/input_part000_review.md†L486-L489
[^17]: Source: knowledge/notes/input_part000_review.md†L489-L493
