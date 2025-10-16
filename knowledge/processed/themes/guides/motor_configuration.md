# Motor Configuration Insights

## Delta Winding Considerations

- Delta-configured hub motors on 36 V systems produced voltage spikes exceeding 100 V, and long-term reliability with VESC hardware remains unproven without alternative firmware or controller pairings.[^delta_spikes]
- Stock Xiaomi and Segway controllers tolerated aggressive delta settings with battery currents above 56 A, but multiple ESCs failed when chasing ~70 km/h on 10 S packs.
  - higher-voltage 48 V packs increased the stress.[^delta_failures]

## Real-World Power Benchmarks

- Dual Minimotors controllers fed by a 54 Ah pack delivered ~90 km at 38 km/h, but riders noted VESC tunes feel more conservative and emphasised monitoring energy use when comparing platforms.[^minimotors_range]
- 2 000 W hub motors begin to warm after ~3 km at 60 A battery / 100 A phase, pushing builders toward 3 000 W swaps to sustain 3–4 kW bursts without cooking stators.[^2000w_heat]
- Dualtron Spider conversions are running 135 A motor / 35 A battery per channel with 100 A regen per motor, highlighting how easily stock packs sag when asked for ~260 A combined bursts.[^spider_current]
- Real-world logs peg dual Monorim or Blade AWD builds around 65 km/h on 10 S and 70–72 km/h on series 10 S packs drawing ~100 A, while single Blade hubs on 13 S FOC hover near 55 km/h—controller headroom, gearing, and aerodynamics gate top speed more than voltage alone.[^denis-awd-speed]
- Budget 500 W hub swaps run scorching at 75–95 A phase, whereas Blade hubs stay hand-warm near 120 A, so 60 km/h ambitions demand premium motors, wider forks, and serious brake packages.[^denis-hub-heat]
- KD pegs dual Xiaomi Pro or Monorim hubs on 17 S VESC builds around 60–70 km/h and reminds crews that VESC phase current slams hardware harder than Xiaomi ESC ratings, so plan upgraded hubs and extra cooling if you chase those speeds.[^denis-17s-vesc]

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
- Marketing wattage is meaningless on Vsett 10+ motors.
  - inspect winding fill and magnet stack height to judge headroom before pushing phase amps or buying donor wheels for AWD swaps.[^11]
- Happy Giraffe logged key Blade hub dimensions (130 mm inner axle, ≈160 mm fork span, M12 threads with 10 mm flats, 12 mm rotor offset, 4 mm hex hardware) and confirmed the shell is tubeless-ready, giving Xiaomi builders a reference checklist before ordering forks and spacers.[^12]
- Rage Mechanics’ 75 mm stator motors are sustaining 10 kW per wheel on Weped platforms but cost ≈€650 each and require wider axles.
  - plan chassis spacing before chasing 120 km/h builds with them.[^13]

- AWD projects gravitate toward VESCs, Spintend Ubox, or Kelly controllers to unlock higher phase currents; Rion’s dual 250 A stacks impressed riders, but Ninebot conversions still debate enclosure cooling and stem strength for 16 S–22 S builds.[^denis-awd-controller]
- Two stock Xiaomi packs in series lack current for real 72 V AWD attempts—serious 20 S builds commission purpose-built batteries instead.[^denis-72v-warning]

## Xiaomi Drop-In Realities (Denis Part 02)

- Rita builders still chase ~40 km/h with reputable 350 W hubs plus 12 S–13 S packs or 10″ tires; “Monorim 350 W” storefront motors are high-kV clones that trade torque for speed.[^denis-40kph]
- Field logs show genuine Monorim 500 W hubs cooled with ferrofluid and pneumatic tires cruising 48–50 km/h at roughly 2.2 kW while running cooler than 350 W cans; bargain “1 kW” clones still suffer weak halls, low kV, and captive rims despite the marketing.[^denis-monorim-500w-field]
- Mixing a 12 S rear with a 10 S front on AWD hybrids drags the lower-voltage wheel through regen; keep pack voltages matched before wiring dual hubs.[^denis-regen-drag]
- Rental-sourced 350 W hubs remain the preferred drop-in upgrade, while 500 W Monorim fronts still need conservative current and 48 V support before they beat a well-tuned dual-350 W setup.[^denis-rental-hubs]
- Keep Xiaomi tires near 50–60 psi on 12 S tunes; dropping pressure for comfort robs the 40 km/h targets riders chase and adds braking drama.[^denis-tire-psi]
- Johnny Player standardises on 6001-2RS rear and 6002-2RS front bearings from SKF/Koyo/ZVL; bargain bearings fail early under commuter loads and often slow Rita builds once the grease cooks off around the 2 000 km mark.[^denis-bearings][^denis-bearing-interval]
- Monorim’s 500 W hub ships with fragile sensors, bolts, and solid tires; veterans favour dual stock motors or matched 350 W high-kV hubs for AWD because they service easily and avoid low-kV torque slumps that overheat lone 500 W swaps.[^denis-monorim-500w]
- Real-world speed logs put 300–350 W swaps around 34 km/h on 36 V, ~45 km/h on 48 V, and roughly 40–41 km/h for Kenso 350 W hubs fed by dual 10 S packs—marketing claims rarely beat motor kV.[^denis-real-speeds]
- High current XiaoGen maps can mimic regen drag or buzzing motors; backing battery current down from 28 A to 26 A cleared the issue and aligns better with Rita’s ~25 A ceiling.[^denis-current-trim]
- Ferrofluid builds pair best with bearing upgrades (6002 ZVL2RS or branded SKF/Koyo) and throttle maps capped near a 25 000 “motor power constant” for endurance instead of maxing XiaoGen at 32 000.[^denis-bearing-upgrade]
- Motor rewinds directly alter kV, and any hub run beyond ~100 °C risks permanent damage—stick to purpose-made Statorade when adding ferrofluid cooling.[^denis-rewind]
- Dual-motor Xiaomi builds require two controllers/dashboards; Rita cannot manage AWD, pushing serious projects toward dual VESC stacks (e.g., Spintend Ubox) or acceptance of single-motor limits.[^denis-dual]
- “1 000 W” Monorim hubs arrive with undersized connectors, weak tubeless tires, and no brake-disc mount; they have already high-sided riders at ~2 kW unless you overhaul the wheel and braking package.[^denis-monorim-1kw]
- Dropping a 1 000 W hub into a Xiaomi deck requires the Monorim suspension with the fork flipped so the rim and six-bolt rotor clear the frame—stock geometry simply won’t fit.[^denis-1000w-fitment]
- G30 Max frames are wider than Xiaomi Pro decks, so cross-platform motor swaps need custom spacers even when the wheels look interchangeable.[^denis-g30-width]

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
[^2000w_heat]: Source: knowledge/notes/input_part000_review.md, line 166.
[^spider_current]: Source: knowledge/notes/input_part000_review.md, line 167.
[^denis-17s-vesc]: Source: knowledge/notes/denis_all_part02_review.md†L817-L817
[^denis-awd-speed]: Source: knowledge/notes/denis_all_part02_review.md†L1019-L1020
[^denis-hub-heat]: Source: knowledge/notes/denis_all_part02_review.md†L1020-L1020
[^denis-awd-controller]: Source: knowledge/notes/denis_all_part02_review.md†L1074-L1074
[^denis-72v-warning]: Source: knowledge/notes/denis_all_part02_review.md†L1092-L1092


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
[^denis-40kph]: Source: knowledge/notes/denis_all_part02_review.md†L610-L612
[^denis-regen-drag]: Source: knowledge/notes/denis_all_part02_review.md†L610-L610
[^denis-rental-hubs]: Source: knowledge/notes/denis_all_part02_review.md†L642-L646
[^denis-bearings]: Source: knowledge/notes/denis_all_part02_review.md†L648-L648
[^denis-bearing-interval]: Source: knowledge/notes/denis_all_part02_review.md†L807-L807
[^denis-monorim-500w]: Source: knowledge/notes/denis_all_part02_review.md†L648-L648
[^denis-real-speeds]: Source: knowledge/notes/denis_all_part02_review.md†L685-L685
[^denis-rewind]: Source: knowledge/notes/denis_all_part02_review.md†L643-L644
[^denis-dual]: Source: knowledge/notes/denis_all_part02_review.md†L644-L645
[^denis-monorim-1kw]: Source: knowledge/notes/denis_all_part02_review.md†L818-L818
[^denis-1000w-fitment]: Source: knowledge/notes/denis_all_part02_review.md†L819-L819
[^denis-g30-width]: Source: knowledge/notes/denis_all_part02_review.md†L820-L820
[^denis-monorim-500w-field]: Source: knowledge/notes/denis_all_part02_review.md†L706-L706
[^denis-tire-psi]: Source: knowledge/notes/denis_all_part02_review.md†L918-L918
[^denis-current-trim]: Source: knowledge/notes/denis_all_part02_review.md†L978-L978
[^denis-bearing-upgrade]: Source: knowledge/notes/denis_all_part02_review.md†L979-L979
