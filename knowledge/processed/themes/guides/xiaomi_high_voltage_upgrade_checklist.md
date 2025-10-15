# Xiaomi High-Voltage Upgrade Checklist

A step-by-step reference for converting Xiaomi M365/Pro-class scooters from 36 V (10S) systems to 12S or 13S configurations without sacrificing reliability.

## 1. Decide Whether More Voltage Is Worth It
- External 36 V packs only extend range; meaningful speed gains begin with 12S/13S packs paired with matching chargers and firmware.[^1]
- Doubling pack voltage roughly doubles no-load speed, but veterans report stock Xiaomi/Ninebot hubs overheat or fail quickly if you jump straight from 10 S to 20 S without major cooling or motor upgrades—treat 18 S as the practical ceiling unless you swap in a beefier hub.[^20s-burn]
- A 13S6P pack built from 2,500 mAh cells roughly doubles the energy of a stock Pro battery while remaining within Rita’s 5 A shared charging envelope when chargers are split.[^2]
- Riders chasing 40 km/h+ targets often graduate to 14S or dual-motor builds—confirm you have the braking, tires, and frame reinforcement to match the higher kinetic energy.[^1][^3]
- Tool and lawnmower packs bring little to the table—Rita waits for ≈36 V before blending, so five-cell modules barely contribute and run dangerously hot under scooter loads.[^tool-pack]
- Ignore bargain “48 V 62 Ah” bundles—builders calculated that the advertised capacity requires non-existent 21 Ah cells and the included controllers rarely survive 48 V operation.[^ali48]

## 2. Hardware Pre-Flight Inspection
| Checkpoint | Requirement | Notes |
| --- | --- | --- |
| Controller revision | Xiaomi V3 controllers accept 13S natively; earlier boards need resistor and capacitor changes at 20S.[^4] | Inspect PCB silkscreen before proceeding.
| MOSFET interface | Replace Kapton tape with 0.5 mm thermal pads or fresh paste to avoid isolation failures and thermal runaway.[^5] | Clean MOSFETs and heatsinks before installing pads.
| Component kit | Stage IRFB4110 MOSFETs plus 100 V/1,000 µF and 100 V/47 µF low-ESR capacitors before pushing 48 V builds, but confirm whether the stock ST15810 devices already meet your targets before desoldering. Swap in silicone pads and sand the controller base so new paste bonds evenly.[^parts-kit]
| Power routing | Direct-solder motor phase leads to controller stubs to cut resistive heating when current climbs; treat 60–65 A experiments as short bursts because stock connector caps have melted above ~55 A even with reinforcement.[^6][^connector-ceiling] | Avoid stacked XT60→XT30 adapters.
| Rita harness | Leave the gray surge jumper intact for 10–12 S; cut it and the pink sense wire only when pairing 13–15 S externals, then recalibrate firmware.[^7]
| Motor selection | Stock 300 W hubs survive ~800 W surges briefly; counterfeit “350 W” hubs fail quickly at 62 V—use vetted suppliers for 13S-20S plans, or adopt a wider Fiido L3 rear hub if you insist on 20 S because its broader stator and open sides shed heat better than Xiaomi-class cans.[^3][^8][^fiido-l3]
| Controller mounting | Bolt controllers flat with fresh thermal paste and clear wiring; lifted plates overheat on the first long ride and can pinch the brake line.[^mounting]
| Aftermarket ESC installs | Grind standoffs or add thick plates so VESC-class controllers clamp like heat sinks; thin adapter plates let 75100 boards spike within seconds.[^vesc-plate]

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
4. Pre-configure XiaoDash/XiaoGen for 13 cells and ~20 Ah before plugging Denis’ 48 V internal pack in; leaving defaults set to 36 V locks performance.[^xiaodash]
5. Limit charging to ~7.5 A (≈2 h) to balance pack longevity with turnaround; one-hour fast charges accelerate degradation.[^2][^15]
6. Smooth throttle maps (quadratic/smart) tame twitchiness on delivery routes once extra voltage is online.[^16]

## 4. Charger & BMS Planning
- Modify OEM chargers by replacing the 10 kΩ feedback resistor with a 30 kΩ+27 kΩ stack (~14.3 kΩ) and fine-tuning the trim pot to 50.4 V for 12S packs.[^10]
- Validate charge completion with a meter—Xiaomi chargers have stayed green while still delivering 42 V, so confirm pack voltage rather than trusting indicator LEDs.[^charger-led]
- Avoid 5 A firmware hacks on legacy M365 BMS boards; they reach ~150 °C under sustained charge. Pro-era boards and Samsung 35E cells handle higher current better, but quality Daly-class BMS hardware is still recommended.[^17][^18]
- Double-check balance-lead order and wire negatives first—miswired Daly smart boards have popped instantly, forcing full harness rebuilds before the first ride.[^balance-leads-xiaomi]
- Daly “Smart” and Xiaoxiang “Smart Ant” BMS modules are popular for 12S–13S builds thanks to reliable balancing and Bluetooth telemetry.[^18][^19]
- External packs should remain common-port so Rita (or any Y-cable) can police charge flow; charging 13S packs through Rita’s charge lead is explicitly discouraged.[^14]
- Treat 13S chargers as emergencies only on 12S packs—veterans rely on the BMS cutoff for a one-off recovery but warn against using 13S bricks as routine CC/CV replacements.[^13s-brick]

## 5. Commissioning Checklist
| Step | What to do | Why |
| --- | --- | --- |
| Static inspection | Verify XT30/XT60 joints, enclosure clearances, and bag strain relief before power-up. | Prevents shorts from vibrating connectors.[^6]
| Firmware validation | Confirm XiaoGen reports correct series count and nominal voltage; rerun m365_DownG “intermediate” package if DRV200 blocks flashing, and lean on the Scooter Companion iOS beta when Android tools are unavailable.[^9][^20][^ios-companion]
| Thermal shakedown | Perform a short hill climb and log controller temps; repeated cutbacks indicate dried paste or inadequate cooling.[^5][^21]
| Current logging | Use Rita or XiaoDash logs to confirm battery current stays below 30 A continuous. | Exceeding 30 A fries controllers despite firmware settings.[^11][^22]
| Regen sanity check | Set recuperation thresholds so regen stays off above 4.15 V per cell; monitor for error 39 spikes after aggressive braking.[^12][^23]

## 6. Operating Guardrails
- Keep firmware speed limits near 34 km/h despite extra voltage; hardware limit unlocks raise crash risk even if 38.5 km/h is possible.[^24]
- Expect significant packaging work above 18 S—the crew squeezed 20 S 1–2 P and even 30 S 1 P bricks into M365 decks only by relocating controllers (e.g., Ubox Lite under the floor) and reworking harness routing, effectively turning the scooter into a mini G30LP.[^deck-layout]
- Avoid mixing configuration generators or chasing 33 k+ phase amps; veterans have already destroyed MOSFETs with mismatched presets and weak cooling.[^22]
- Keep intensity-of-current-change sliders near 300–350 mA—raising them toward 800 mA spikes controller heat even on reinforced boards.[^current-step]
- Monitor pack temperature after charging—freshly topped 12S4P bricks have hit 50 °C on hard climbs. Let packs rest or dial back firmware before commuting.[^21]
- Treat ≈60 °C as a practical ceiling for battery cores; the workshop logged 41 °C packs as healthy but warned that sustained climbs past 60 °C shorten cell life quickly.[^pack-temps]
- High-voltage builds magnify braking and tire demands; run quality CST/Xuancheng casings at 36–50 psi and inspect bearings regularly to keep speed stable.[^25][^26]
- Treat Rita error 14 as a hard stop when dual dashboards share a pack; re-check polarity and harness routing before riding again so the isolation hardware can still block cross-pack faults.[^27]
- 60 V experiments remain strictly provisional—monitor Rita’s alarms, confirm firmware, and stage launches before trusting the higher voltage for daily riding.[^rita60v_xiaomi]
- Give the motor a running start on steep hills—keeping it near 80 % of top speed prevents 48 V builds from cooking hall sensors during full-throttle climbs.[^hill-technique]
- Park RC LiPo bricks back on the shelf for commuting—they puff when stored full and gain resistance within days, making them poor daily scooter batteries.[^lipo]
- Expect winter range to fall sharply (~30 Wh/km vs 18–20 Wh/km in summer); keep packs warm indoors or add gentle heaters before charging below freezing.[^winter]
- Pro 2 dashboards shipped after DRV2.2.3 clamp custom firmware; stay on DRV2.2.3 or temporarily downgrade to DRV155 to configure Rita before returning to the latest release.[^pro2-fw]
- Never power a 16 S conversion by tapping a 10 S segment for the controller—the idle draw unbalances the pack faster than the BMS can correct, even if the adapter only sips ≈12 mA.[^tap-imbalance]

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
[^mounting]: 【F:knowledge/notes/denis_all_part02_review.md†L140-L143】
[^vesc-plate]: 【F:knowledge/notes/denis_all_part02_review.md†L155-L156】
[^9]: 【F:knowledge/notes/all_part01_review.md†L121-L123】【F:knowledge/notes/denis_all_part02_review.md†L11】【F:knowledge/notes/denis_all_part02_review.md†L155-L167】
[^10]: 【F:knowledge/notes/all_part01_review.md†L94-L96】
[^11]: 【F:knowledge/notes/all_part01_review.md†L73-L74】
[^12]: 【F:knowledge/notes/all_part01_review.md†L169-L170】
[^13]: 【F:knowledge/notes/denis_all_part02_review.md†L110-L111】
[^xiaodash]: 【F:knowledge/notes/denis_all_part02_review.md†L149-L151】
[^14]: 【F:knowledge/notes/denis_all_part02_review.md†L23】【F:knowledge/notes/denis_all_part02_review.md†L124】
[^15]: 【F:knowledge/notes/denis_all_part02_review.md†L101-L102】
[^16]: 【F:knowledge/notes/denis_all_part02_review.md†L136-L137】
[^17]: 【F:knowledge/notes/all_part01_review.md†L102-L103】
[^18]: 【F:knowledge/notes/denis_all_part02_review.md†L124】【F:knowledge/notes/denis_all_part02_review.md†L158-L159】
[^19]: 【F:knowledge/notes/denis_all_part02_review.md†L158-L159】
[^13s-brick]: 【F:knowledge/notes/denis_all_part02_review.md†L194-L195】
[^balance-leads-xiaomi]: 【F:knowledge/notes/denis_all_part02_review.md†L7028-L7068】
[^20]: 【F:knowledge/notes/denis_all_part02_review.md†L50-L51】【F:knowledge/notes/denis_all_part02_review.md†L161-L168】
[^21]: 【F:knowledge/notes/denis_all_part02_review.md†L32】【F:knowledge/notes/denis_all_part02_review.md†L213】
[^22]: 【F:knowledge/notes/denis_all_part02_review.md†L153-L154】【F:knowledge/notes/denis_all_part02_review.md†L165-L168】
[^23]: 【F:knowledge/notes/all_part01_review.md†L169-L170】【F:knowledge/notes/denis_all_part02_review.md†L29-L33】
[^24]: 【F:knowledge/notes/all_part01_review.md†L122-L123】
[^25]: 【F:knowledge/notes/denis_all_part02_review.md†L15-L17】【F:knowledge/notes/denis_all_part02_review.md†L56-L57】
[^26]: 【F:knowledge/notes/denis_all_part02_review.md†L56-L57】【F:knowledge/notes/denis_all_part02_review.md†L171-L175】
[^lipo]: 【F:knowledge/notes/denis_all_part02_review.md†L158-L160】
[^winter]: 【F:knowledge/notes/denis_all_part02_review.md†L160-L162】
[^27]: 【F:knowledge/notes/denis_all_part02_review.md†L10541-L10598】
[^charger-led]: 【F:knowledge/notes/input_part011_review.md†L18-L18】
[^tool-pack]: 【F:knowledge/notes/denis_all_part02_review.md†L8873-L8893】
[^ali48]: 【F:knowledge/notes/denis_all_part02_review.md†L146-L148】
[^rita60v_xiaomi]: 【F:knowledge/notes/denis_all_part02_review.md†L9495-L9520】
[^connector-ceiling]: 【F:knowledge/notes/all_part01_review.md†L206-L207】
[^ios-companion]: 【F:knowledge/notes/all_part01_review.md†L213-L213】
[^current-step]: 【F:knowledge/notes/all_part01_review.md†L205-L206】【F:knowledge/notes/all_part01_review.md†L348-L348】
[^pro2-fw]: 【F:knowledge/notes/all_part01_review.md†L176-L176】
[^hill-technique]: 【F:knowledge/notes/denis_all_part02_review.md†L102538-L102548】
[^parts-kit]: 【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60004-L60024】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60151-L60159】
[^pack-temps]: 【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60004-L60008】
[^20s-burn]: Doubling a 10 S Xiaomi/Ninebot build to 20 S roughly doubles unloaded speed but repeatedly burned stock hubs in community testing, so veterans treat 18 S as the upper limit without major motor swaps.【F:data/vesc_help_group/text_slices/input_part011.txt†L19101-L19145】
[^fiido-l3]: Riders suggested the Fiido L3 rear hub for 20 S conversions because its wider stator and unobstructed casing dump heat better than Xiaomi-class motors, surviving abuse that killed smaller hubs within days.【F:data/vesc_help_group/text_slices/input_part011.txt†L19136-L19173】
[^deck-layout]: Packing 20 S 1–2 P or even 30 S 1 P bricks into M365 decks demanded relocating controllers (e.g., mounting a Ubox Lite underneath) and aggressive harness rerouting, effectively recreating a compact G30LP layout.【F:data/vesc_help_group/text_slices/input_part011.txt†L19145-L19185】
[^tap-imbalance]: 【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60151-L60159】
