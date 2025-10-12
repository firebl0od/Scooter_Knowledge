# Xiaomi High-Voltage Upgrade Checklist

A step-by-step reference for converting Xiaomi M365/Pro-class scooters from 36 V (10S) systems to 12S or 13S configurations without sacrificing reliability.

## 1. Decide Whether More Voltage Is Worth It
- External 36 V packs only extend range; meaningful speed gains begin with 12S/13S packs paired with matching chargers and firmware.[^1]
- A 13S6P pack built from 2,500 mAh cells roughly doubles the energy of a stock Pro battery while remaining within Rita’s 5 A shared charging envelope when chargers are split.[^2]
- Riders chasing 40 km/h+ targets often graduate to 14S or dual-motor builds—confirm you have the braking, tires, and frame reinforcement to match the higher kinetic energy.[^1][^3]
- Tool and lawnmower packs bring little to the table—Rita waits for ≈36 V before blending, so five-cell modules barely contribute and run dangerously hot under scooter loads.[^tool-pack]

## 2. Hardware Pre-Flight Inspection
| Checkpoint | Requirement | Notes |
| --- | --- | --- |
| Controller revision | Xiaomi V3 controllers accept 13S natively; earlier boards need resistor and capacitor changes at 20S.[^4] | Inspect PCB silkscreen before proceeding.
| MOSFET interface | Replace Kapton tape with 0.5 mm thermal pads or fresh paste to avoid isolation failures and thermal runaway.[^5] | Clean MOSFETs and heatsinks before installing pads.
| Power routing | Direct-solder motor phase leads to controller stubs to cut resistive heating when current climbs.[^6] | Avoid stacked XT60→XT30 adapters.
| Rita harness | Leave the gray surge jumper intact for 10–12 S; cut it and the pink sense wire only when pairing 13–15 S externals, then recalibrate firmware.[^7]
| Motor selection | Stock 300 W hubs survive ~800 W surges briefly; counterfeit “350 W” hubs fail quickly at 62 V—use vetted suppliers for 13S-20S plans.[^3][^8]

## 3. Build Recipes
### 3.1 12S Range+Speed Combo (10S internal + 12S external)
1. Flash higher-voltage firmware (XiaoFlasher/XiaoGen) and reinforce controller power traces before plugging in the 12S pack.[^9]
2. Source or modify a 50.4 V charger so both packs finish together; Denis’ range kit originally bundled this supply.[^10]
3. Keep sustained battery current near 27 A (~800 W) to protect MOSFETs and hubs; higher values drain packs and spike heat.[^11]
4. Raise Rita’s recuperation-off voltage to ~4.15 V if throttle kicks appear after the upgrade.[^12]

### 3.2 Full 13S Conversions
1. Confirm the controller is a Xiaomi V3 (or reinforce older boards) and swap Kapton for 0.5 mm pads across MOSFETs.[^4][^5]
2. Cut Rita’s pink sense lead, open the surge jumper, and reinforce controller traces plus wiring before applying 48–54 V externals.[^7][^13]
3. Maintain common-port BMS wiring and avoid charging 13S packs through Rita’s onboard jack—use dedicated XT30 harnesses or split chargers.[^14]
4. Limit charging to ~7.5 A (≈2 h) to balance pack longevity with turnaround; one-hour fast charges accelerate degradation.[^2][^15]
5. Smooth throttle maps (quadratic/smart) tame twitchiness on delivery routes once extra voltage is online.[^16]

## 4. Charger & BMS Planning
- Modify OEM chargers by replacing the 10 kΩ feedback resistor with a 30 kΩ+27 kΩ stack (~14.3 kΩ) and fine-tuning the trim pot to 50.4 V for 12S packs.[^10]
- Validate charge completion with a meter—Xiaomi chargers have stayed green while still delivering 42 V, so confirm pack voltage rather than trusting indicator LEDs.[^charger-led]
- Avoid 5 A firmware hacks on legacy M365 BMS boards; they reach ~150 °C under sustained charge. Pro-era boards and Samsung 35E cells handle higher current better, but quality Daly-class BMS hardware is still recommended.[^17][^18]
- Double-check balance-lead order and wire negatives first—miswired Daly smart boards have popped instantly, forcing full harness rebuilds before the first ride.[^balance-leads-xiaomi]
- Daly “Smart” and Xiaoxiang “Smart Ant” BMS modules are popular for 12S–13S builds thanks to reliable balancing and Bluetooth telemetry.[^18][^19]
- External packs should remain common-port so Rita (or any Y-cable) can police charge flow; charging 13S packs through Rita’s charge lead is explicitly discouraged.[^14]

## 5. Commissioning Checklist
| Step | What to do | Why |
| --- | --- | --- |
| Static inspection | Verify XT30/XT60 joints, enclosure clearances, and bag strain relief before power-up. | Prevents shorts from vibrating connectors.[^6]
| Firmware validation | Confirm XiaoGen reports correct series count and nominal voltage; rerun m365_DownG “intermediate” package if DRV200 blocks flashing.[^9][^20]
| Thermal shakedown | Perform a short hill climb and log controller temps; repeated cutbacks indicate dried paste or inadequate cooling.[^5][^21]
| Current logging | Use Rita or XiaoDash logs to confirm battery current stays below 30 A continuous. | Exceeding 30 A fries controllers despite firmware settings.[^11][^22]
| Regen sanity check | Set recuperation thresholds so regen stays off above 4.15 V per cell; monitor for error 39 spikes after aggressive braking.[^12][^23]

## 6. Operating Guardrails
- Keep firmware speed limits near 34 km/h despite extra voltage; hardware limit unlocks raise crash risk even if 38.5 km/h is possible.[^24]
- Avoid mixing configuration generators or chasing 33 k+ phase amps; veterans have already destroyed MOSFETs with mismatched presets and weak cooling.[^22]
- Monitor pack temperature after charging—freshly topped 12S4P bricks have hit 50 °C on hard climbs. Let packs rest or dial back firmware before commuting.[^21]
- High-voltage builds magnify braking and tire demands; run quality CST/Xuancheng casings at 36–50 psi and inspect bearings regularly to keep speed stable.[^25][^26]
- Treat Rita error 14 as a hard stop when dual dashboards share a pack; re-check polarity and harness routing before riding again so the isolation hardware can still block cross-pack faults.[^27]
- 60 V experiments remain strictly provisional—monitor Rita’s alarms, confirm firmware, and stage launches before trusting the higher voltage for daily riding.[^rita60v_xiaomi]

---

## Source Notes

[^1]: 【F:knowledge/notes/denis_all_part02_review.md†L114-L116】
[^2]: 【F:knowledge/notes/denis_all_part02_review.md†L101-L102】【F:knowledge/notes/denis_all_part02_review.md†L157-L158】
[^3]: 【F:knowledge/notes/denis_all_part02_review.md†L35-L39】【F:knowledge/notes/denis_all_part02_review.md†L114-L116】
[^4]: 【F:knowledge/notes/denis_all_part02_review.md†L11-L12】
[^5]: 【F:knowledge/notes/denis_all_part02_review.md†L12-L13】【F:knowledge/notes/denis_all_part02_review.md†L32】
[^6]: 【F:knowledge/notes/denis_all_part02_review.md†L13】【F:knowledge/notes/denis_all_part02_review.md†L37】
[^7]: 【F:knowledge/notes/denis_all_part02_review.md†L22】【F:knowledge/notes/denis_all_part02_review.md†L218】
[^8]: 【F:knowledge/notes/denis_all_part02_review.md†L38-L39】【F:knowledge/notes/denis_all_part02_review.md†L147】
[^9]: 【F:knowledge/notes/all_part01_review.md†L121-L123】【F:knowledge/notes/denis_all_part02_review.md†L11】【F:knowledge/notes/denis_all_part02_review.md†L155-L167】
[^10]: 【F:knowledge/notes/all_part01_review.md†L94-L96】
[^11]: 【F:knowledge/notes/all_part01_review.md†L73-L74】
[^12]: 【F:knowledge/notes/all_part01_review.md†L169-L170】
[^13]: 【F:knowledge/notes/denis_all_part02_review.md†L110-L111】
[^14]: 【F:knowledge/notes/denis_all_part02_review.md†L23】【F:knowledge/notes/denis_all_part02_review.md†L124】
[^15]: 【F:knowledge/notes/denis_all_part02_review.md†L101-L102】
[^16]: 【F:knowledge/notes/denis_all_part02_review.md†L136-L137】
[^17]: 【F:knowledge/notes/all_part01_review.md†L102-L103】
[^18]: 【F:knowledge/notes/denis_all_part02_review.md†L124】【F:knowledge/notes/denis_all_part02_review.md†L158-L159】
[^19]: 【F:knowledge/notes/denis_all_part02_review.md†L158-L159】
[^balance-leads-xiaomi]: 【F:knowledge/notes/denis_all_part02_review.md†L7028-L7068】
[^20]: 【F:knowledge/notes/denis_all_part02_review.md†L50-L51】【F:knowledge/notes/denis_all_part02_review.md†L161-L168】
[^21]: 【F:knowledge/notes/denis_all_part02_review.md†L32】【F:knowledge/notes/denis_all_part02_review.md†L213】
[^22]: 【F:knowledge/notes/denis_all_part02_review.md†L153-L154】【F:knowledge/notes/denis_all_part02_review.md†L165-L168】
[^23]: 【F:knowledge/notes/all_part01_review.md†L169-L170】【F:knowledge/notes/denis_all_part02_review.md†L29-L33】
[^24]: 【F:knowledge/notes/all_part01_review.md†L122-L123】
[^25]: 【F:knowledge/notes/denis_all_part02_review.md†L15-L17】【F:knowledge/notes/denis_all_part02_review.md†L56-L57】
[^26]: 【F:knowledge/notes/denis_all_part02_review.md†L56-L57】【F:knowledge/notes/denis_all_part02_review.md†L171-L175】
[^27]: 【F:knowledge/notes/denis_all_part02_review.md†L10541-L10598】
[^charger-led]: 【F:knowledge/notes/input_part011_review.md†L18-L18】
[^tool-pack]: 【F:knowledge/notes/denis_all_part02_review.md†L8873-L8893】
[^rita60v_xiaomi]: 【F:knowledge/notes/denis_all_part02_review.md†L9495-L9520】
