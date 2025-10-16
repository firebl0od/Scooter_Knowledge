# Xiaomi High-Voltage Upgrade Checklist

A step-by-step reference for converting Xiaomi M365/Pro-class scooters from 36 V (10S) systems to 12S or 13S configurations without sacrificing reliability.

## 1. Decide Whether More Voltage Is Worth It

- External 36 V packs only extend range; meaningful speed gains begin with 12S/13S packs paired with matching chargers and firmware.[^1]
- Doubling pack voltage roughly doubles no-load speed, but veterans report stock Xiaomi/Ninebot hubs overheat or fail quickly if you jump straight from 10 S to 20 S without major cooling or motor upgrades.
  - treat 18 S as the practical ceiling unless you swap in a beefier hub.[^20s-burn]
- Recent deck mockups confirm you can cram 20 S 1–2 P (or even tight 30 S 1 P) layouts once the ESC and BMS move under the footplate, but the crew still calls 18 S the “sweet spot” for reliability and packaging sanity.[^deck-relocate]
- Stem-mounted boosters and skinny OEM forks won’t survive 20 S abuse—budget larger ESx/G30-class hubs and stronger front ends before chasing sleeper builds at those voltages.[^sleeper-hardware]
- Swapping from 36 V to 48 V at the same amp-hour rating still increases watt-hours and torque, helping heavier riders keep pace even when scooters start from identical hardware.[^1]
- A 13S6P pack built from 2,500 mAh cells roughly doubles the energy of a stock Pro battery while remaining within Rita’s 5 A shared charging envelope when chargers are split.[^2]
- Riders chasing 40 km/h+ targets often graduate to 14S or dual-motor builds—confirm you have the braking, tires, and frame reinforcement to match the higher kinetic energy.[^1][^3]
- Expect 70–80 km/h goals to demand at least 17 S packs, upgraded controllers, full suspension, and 6–10 P batteries that can cost €500–700 in cells alone—far beyond what the stock frame houses without external bags.[^17s_speed]
- A 16S5P Samsung 35E pack safely feeds about 50 A; chasing 100 km/h on a single-motor Xiaomi with that chemistry is unrealistic without higher-voltage packs, better brakes, and wider forks to house VSETT-class hubs.[^2]
- Tool and lawnmower packs bring little to the table—Rita waits for ≈36 V before blending, so five-cell modules barely contribute and run dangerously hot under scooter loads.[^tool-pack]
- Skip 2S/3S “speed booster” bricks strapped in series with the stock pack; the add-ons backfeed once voltage sags and riders have blown OEM ESCs around 54.6 V without heavy reinforcement.[^3][^4]
- Even dual 13 S packs plateau near 40–42 km/h because stock controllers enforce their own speed ceiling; real top-speed gains require controller swaps or field weakening.[^dual13s_cap]
- 12 S 350 W hubs log roughly 47 km/h at ≈28 A, while 14 S builds with 75 kg riders reach 49–52 km/h—plan braking and cooling upgrades before chasing those voltages.[^12s14s_speed_benchmark]
- Ignore bargain “48 V 62 Ah” bundles—builders calculated that the advertised capacity requires non-existent 21 Ah cells and the included controllers rarely survive 48 V operation.[^ali48]
- Delta-wound 10 S builds already touch ~55 km/h and pull 50–100 A spikes; one rider logged 91 km/h on 16 S before the stock controller died, so plan VESC swaps or limit OEM boards to ≈15 S when chasing top speed.[^5]
- Xiaomi-class ESCs get flaky above 12 S.
  - GABE’s 13 S conversion tripped repeatedly until he rebuilt it as a 12 S 6 P pack, trading headline voltage for reliable commuting.[^6]

## 2. Hardware Pre-Flight Inspection

| Checkpoint | Requirement | Notes |
| --- | --- | --- |
| Controller revision | Xiaomi V3 controllers accept 13S natively; earlier boards need resistor and capacitor changes at 20S.[^4] | Inspect PCB silkscreen before proceeding.
| MOSFET interface | Replace Kapton tape with 0.5 mm thermal pads or fresh paste to avoid isolation failures and thermal runaway.[^5] | Clean MOSFETs and heatsinks before installing pads.
| Component kit | Stage IRFB4110 MOSFETs plus 100 V/1,000 µF and 100 V/47 µF low-ESR capacitors before pushing 48 V builds, but confirm whether the stock ST15810 devices already meet your targets before desoldering. Swap in silicone pads and sand the controller base so new paste bonds evenly.[^parts-kit]
| Power routing | Direct-solder motor phase leads to controller stubs to cut resistive heating when current climbs; treat 60–65 A experiments as short bursts because stock connector caps have melted above ~55 A even with reinforcement.[^6][^connector-ceiling] | Avoid stacked XT60→XT30 adapters.
| Rita harness | Leave the gray surge jumper intact for 10–12 S; cut it and the pink sense wire only when pairing 13–15 S externals, then recalibrate firmware.[^7]
| Motor selection | Stock 300 W hubs survive ~800 W surges briefly; counterfeit “350 W” hubs fail quickly at 62 V.
  - use vetted suppliers for 13S-20S plans and budget ≥€200 for reputable Blade-class replacements; Monorim motors sit below stock quality.[^7][^3][^8] | Source from reputable vendors, note that 10" Kugoo 500 W hubs (≈23–25 Kv) run on stock ESCs or VESCs with 120° halls (or 60° once XiaoDash remaps), and keep OEM hall placement for stable detection.[^8] |
  - Stock Pro 300 W hubs overheat within minutes past 1 kW, whereas Monorim’s 500 W motor tolerates ~2 kW bursts under wind load—pair voltage jumps with hub upgrades.[^monorim_500w_heat]
| Motor upgrade budget | Rage Mechanics’ Blade kits, VSETT drop-ins, and Monorim options span roughly €300–€500 per motor before hall-board swaps; confirm quality and lead time before promising Pro 2 customers higher torque builds.[^9] | Set expectations around cost and QC when pitching full Pro 2 conversions. |
| Controller mounting | Bolt controllers flat with fresh thermal paste and clear wiring; lifted plates overheat on the first long ride and can pinch the brake line.[^mounting]
| Deck packaging | Splitting a 20 S pack 11 S internal/9 S external kept Gabe’s Pro 2 sleeper build within the deck.
  - twin 6 AWG feeds, a 50 mm controller spacer, and relocating the BMS into the stem free the cavity for cells.[^10]
  - Alternative layouts squeeze 20 S 1–2 P or even 30 S 1 P into the tray once the controller lives under the deck (Ubox 100/100 Lite or similar) and the harness is reworked.[^deck-relocate] | Keep electronics outside the main battery bay when chasing 20 S layouts. |
| Controller mounting | Bolt controllers flat with fresh thermal paste, lap the ESC baseplate and deck for full contact, and clear wiring; lifted plates overheat on the first long ride and can pinch the brake line.[^mounting][^lap-base]
| Aftermarket ESC installs | Grind standoffs or add thick plates so VESC-class controllers clamp like heat sinks; thin adapter plates let 75100 boards spike within seconds.[^vesc-plate]
| STM32 ADC protection debate | Denis trusts the factory 10 MΩ divider on 13–16 S builds, but other techs still swap ≈160 kΩ resistors to avoid error 24 or protect STM inputs when emulating a Xiaomi BMS.
  - document whichever approach you choose for future servicing.[^11] |

## 3. Build Recipes

### 3.1 12S Range+Speed Combo (10S internal + 12S external)

1. Flash higher-voltage firmware (XiaoFlasher/XiaoGen) and reinforce controller power traces before plugging in the 12S pack.[^9]
2. Source or modify a 50.4 V charger so both packs finish together; Denis’ range kit originally bundled this supply.[^10]
3. Keep sustained battery current near 27 A (~800 W) to protect MOSFETs and hubs; higher values drain packs and spike heat.[^11]
4. Raise Rita’s recuperation-off voltage to ~4.15 V if throttle kicks appear after the upgrade.[^12]

### 3.2 Full 13S Conversions

1. Confirm the controller is a Xiaomi V3 (or reinforce older boards) and swap Kapton for 0.5 mm pads across MOSFETs.[^4][^5]
2. Cut Rita’s pink sense lead, open the surge jumper, and reinforce controller traces plus wiring before applying 48–54 V externals; once that jumper is cut you cannot safely drop back to 10 S without restoring it.[^7][^13][^return-jumper]
3. Maintain common-port BMS wiring and avoid charging 13S packs through Rita’s onboard jack—use dedicated XT30 harnesses or split chargers.[^14]
4. Pre-configure XiaoDash/XiaoGen for 13 cells and ~20 Ah before plugging Denis’ 48 V internal pack in; leaving defaults set to 36 V locks performance.[^xiaodash]
5. Limit charging to ~7.5 A (≈2 h) to balance pack longevity with turnaround; one-hour fast charges accelerate degradation.[^2][^15]
6. Smooth throttle maps (quadratic/smart) tame twitchiness on delivery routes once extra voltage is online.[^16]
2. Order Denis’ 44 V Pro battery kit and note you need the 48 V variant.
  - his store swaps the pack and harness at fulfillment; generic 48 V bricks fit but waste deck volume and require custom padding.[^12]
3. Cut Rita’s pink sense lead, open the surge jumper, and reinforce controller traces plus wiring before applying 48–54 V externals.[^7][^13]
4. Set controller limits realistically.
  - Denis caps Xiaomi ESCs around 55 A phase and 30 A battery current once 48 V packs are installed to stay inside hardware limits.[^13]
5. Maintain common-port BMS wiring and avoid charging 13S packs through Rita’s onboard jack—use dedicated XT30 harnesses or split chargers.[^14]
6. Pre-configure XiaoDash/XiaoGen for 13 cells and ~20 Ah before plugging Denis’ 48 V internal pack in; leaving defaults set to 36 V locks performance.[^14][^xiaodash]
7. Limit charging to ~7.5 A (≈2 h) to balance pack longevity with turnaround; one-hour fast charges accelerate degradation.[^2][^15]
8. Smooth throttle maps (quadratic/smart) tame twitchiness on delivery routes once extra voltage is online.[^16]

### 3.3 17S Samsung 40T Trials

1. Plan for dual XT150 phase connectors, thicker insulation, and brake upgrades before jumping to 17 S6 P.
  - budget Daly replacements if the existing BMS forces 4.18 V/cell to balance and accept ~20 V sag until wiring is upsized.[^15][^16]
2. Until a programmable charger arrives, set 16 S supplies around 67 V for partial charges and monitor balance delta closely; Daly hardware often refuses to wake balancing without near-full voltage.[^16]

### 3.4 22S Pro 2 Packaging Experiment

1. GABE proved a 22 S pack fits once PETG carriers slide between the rails (~660 Wh), but he plans to disable or heavily limit regen so the Mini Ubox survives and may short-charge to ≈21.5 S to keep braking headroom.[^gabe-22s]
2. Expect sanding or external enclosures if deck tolerances clamp the PETG carriers; the build only clears once spacer thickness and rail clearance are tuned.[^gabe-22s]

## 4. Charger & BMS Planning

- Modify OEM chargers by replacing the 10 kΩ feedback resistor with a 30 kΩ+27 kΩ stack (~14.3 kΩ) and fine-tuning the trim pot to 50.4 V for 12S packs.[^10]
- When sourcing standalone supplies, Denis recommends Mean Well ELG-240-48A-class chargers and notes that finding Xiaomi’s coaxial plug is often the hardest step of the conversion.[^hv-supply]
- Stretching the stock Xiaomi charger to 15 S requires adjusting internal trim pots to ~61.5 V and uprating output capacitors.
  - the unit remains a constant-current supply with no overcharge shutoff beyond the new voltage target.[^17]
- Validate charge completion with a meter—Xiaomi chargers have stayed green while still delivering 42 V, so confirm pack voltage rather than trusting indicator LEDs.[^charger-led]
- Rita keeps topping the external pack after the scooter powers down; rely on the charger LED or a voltmeter instead of the dash to confirm charging is complete.[^18]
- Avoid 5 A firmware hacks on legacy M365 BMS boards; they reach ~150 °C under sustained charge. Pro-era boards and Samsung 35E cells handle higher current better, but quality Daly-class BMS hardware is still recommended.[^17][^18]
- Double-check balance-lead order and wire negatives first—miswired Daly smart boards have popped instantly, forcing full harness rebuilds before the first ride.[^balance-leads-xiaomi]
- Daly “Smart” and Xiaoxiang “Smart Ant” BMS modules are popular for 12S–13S builds thanks to reliable balancing and Bluetooth telemetry.[^18][^19]
- External packs should remain common-port so Rita (or any Y-cable) can police charge flow; charging 13S packs through Rita’s charge lead is explicitly discouraged.[^14]
- Treat 13S chargers as emergencies only on 12S packs—veterans rely on the BMS cutoff for a one-off recovery but warn against using 13S bricks as routine CC/CV replacements.[^13s-brick]

## 5. Commissioning Checklist

| Step | What to do | Why |
| --- | --- | --- |
| Static inspection | Verify XT30/XT60 joints, enclosure clearances, and bag strain relief before power-up. | Prevents shorts from vibrating connectors.[^6]
| Firmware validation | Confirm XiaoGen reports correct series count and nominal voltage; rerun m365_DownG “intermediate” package if DRV200 blocks flashing, and lean on the Scooter Companion iOS beta when Android tools are unavailable.[^9][^20][^ios-companion] | Keep ST-Link pogo pins clamped to the ESC pads.
  - floating leads cause most failed reflashes before the board ever sees new firmware.[^19] |
| Firmware validation | Confirm XiaoGen reports correct series count and nominal voltage; rerun m365_DownG “intermediate” package if DRV200 blocks flashing, lean on the Scooter Companion iOS beta when Android tools are unavailable, and remember new Pro 2 dashboards still need an ST-Link flash or temporary old-dash swap before custom firmware sticks.[^20][^9][^20][^ios-companion]
| Thermal shakedown | Perform a short hill climb and log controller temps; repeated cutbacks indicate dried paste or inadequate cooling.[^5][^21]
| Current logging | Use Rita or XiaoDash logs to confirm battery current stays below 30 A continuous. | Exceeding 30 A fries controllers despite firmware settings.[^11][^22]
| Regen sanity check | Set recuperation thresholds so regen stays off above 4.15 V per cell; monitor for error 39 spikes after aggressive braking.[^12][^23]

## 6. Operating Guardrails

- Skip serial “booster” bricks on 12 S builds—each extra 1 S segment needs matching parallel count and its own charging path, making a dedicated 15–17 S pack safer than stacking mismatched add-ons.[^series_booster_guardrail]
- Tudor’s reinforced controllers still top out near 13 S; earlier 17–19 S experiments overheated MOSFETs around 27 A, so future high-voltage hardware is being purpose-built instead of reusing those boards.[^tudor_headroom]
- Exotic 13 S star/delta experiments have logged 74 km/h freewheel speeds but sit well outside Xiaomi’s safe design envelope—treat them as proof-of-concept rather than commuter targets.[^star_delta_warning]
- Keep firmware speed limits near 34 km/h despite extra voltage; hardware limit unlocks raise crash risk even if 38.5 km/h is possible.[^24]
- Expect significant packaging work above 18 S.
  - the crew squeezed 20 S 1–2 P and even 30 S 1 P bricks into M365 decks only by relocating controllers (e.g., Ubox Lite under the floor) and reworking harness routing, effectively turning the scooter into a mini G30LP.[^deck-layout]
- Align regen voltage ceilings with the actual pack.
  - set limits near real 48 V/51 V values so controllers do not throw over-voltage faults when regen kicks in after a high-voltage conversion.[^21]
- Avoid mixing configuration generators or chasing 33 k+ phase amps; veterans have already destroyed MOSFETs with mismatched presets and weak cooling.[^22]
- Match Drive-mode current to real pack voltage—32 A on 12 S pulls roughly 1.3 kW, so dial back if you need a ~900 W ceiling.[^22]
- Keep intensity-of-current-change sliders near 300–350 mA—raising them toward 800 mA spikes controller heat even on reinforced boards.[^current-step]
- Delta rewinds demand roughly double the phase current for the same torque.
  - upgrade hub leads and consider star reconnections if you want >70 km/h without melting stock windings.[^23]
- Monitor pack temperature after charging—freshly topped 12S4P bricks have hit 50 °C on hard climbs. Let packs rest or dial back firmware before commuting.[^21]
- Park packs around 3.7 V for storage and expect Rita telemetry to favour whichever battery sits roughly 0.5 V higher.
  - those swings are normal once externals stay plugged in.[^24]
- Aggressive regen on 48 V packs can still blow “reinforced” Xiaomi controllers.
  - the back-EMF spike after panic stops has shorted 85 V MOSFETs and 60 V capacitors, so budget controller upgrades or soften e-brake settings on high-voltage builds.[^25]
- Treat ≈60 °C as a practical ceiling for battery cores; the workshop logged 41 °C packs as healthy but warned that sustained climbs past 60 °C shorten cell life quickly.[^pack-temps]
- High-voltage builds magnify braking and tire demands; run quality CST/Xuancheng casings at 36–50 psi and inspect bearings regularly to keep speed stable.[^25][^26]
- Treat Xiaomi/Monorim hubs as ~25–30 A battery / 50–70 A phase devices even with ferrofluid.
  - higher currents overheat hall sensors and thin leads, so plan motor swaps or new datasheets before exceeding those guardrails.[^26]
- Evaluate external-pack health with a constant-current load while the internal battery stays connected; reconnect only when voltages sit within ~1 V to avoid slamming the weaker BMS.[^27]
- Treat Rita error 14 as a hard stop when dual dashboards share a pack; re-check polarity and harness routing before riding again so the isolation hardware can still block cross-pack faults.[^27]
- Pro 2 dashboards on firmware newer than DRV2.2.3 clamp custom builds; stay on DRV2.2.3 or temporarily downgrade to DRV155 to configure Rita before returning to the latest release.[^28]
- Stock Xiaomi dashboards speak half-duplex UART and still cannot talk directly to Flipsky 75100 controllers.
  - flash VESC firmware onto the OEM ESC if you want the factory dash to stay on the bus during VESC swaps.[^29]
- Custom dashboards (dual displays, Wi-Fi logging) remain experimental.
  - plan on Android-first tooling because Apple’s developer program keeps iOS support lagging behind.[^30]
- After 10" swaps, adjust Xiaogen’s wheel constant by ≈8.1 % and confirm against GPS; “Russian” throttle mode keeps the lever mapped directly to torque for aggressive high-voltage builds.[^31]
- 60 V experiments remain strictly provisional—monitor Rita’s alarms, confirm firmware, and stage launches before trusting the higher voltage for daily riding.[^rita60v_xiaomi]
- Skip 3S “powercube” add-ons on Xiaomi 1S boards.
  - lifting pack voltage past 56 V invites regen spikes that kill the stock controller unless KERS is disabled and braking stays mechanical; veterans reinforce traces or jump directly to 15 S packs instead.[^32]
- 84 V/25 A tunes belong on reinforced frames: the crew found 30 S tests really demand an 11-inch chassis, avoid regen entirely, and accept that Xiaomi controllers eventually fail if you chase triple-digit speed on stock hardware.[^33][^34]
- When pairing Rita with external packs, connect the internal (boat) battery first so the adapter “sees” the right baseline, cap output near 25 A continuous/30 A peak, and disable or soften e-brake regen on 84 V builds to keep trace-cut controllers alive.[^35][^34][^36]
- XiaoDash’s Speed Boost adds 6–7 km/h only when battery current climbs toward 27 A; ScooterHacking firmware lacks the feature, so migrate to XiaoDash for field weakening while respecting Rita’s ~30 A ceiling.[^37]
- Field weakening retimes PWM to counter back-EMF rather than raising pack voltage; plan for extra current headroom and proper cooling if you chase the added speed on higher-turn motors.[^38]
- First-generation Xiaomi hubs plateau around 32 km/h even with field weakening; later Pro 2 motors deliver higher top speed without sacrificing torque when you push voltage.[^39]
- Export VESC Tool CSV/XLS logs after climbs to quantify sag before raising limits; riders now retune current using data instead of guessing mid-ride.[^40]
- Give the motor a running start on steep hills—keeping it near 80 % of top speed prevents 48 V builds from cooking hall sensors during full-throttle climbs.[^hill-technique]
- Park RC LiPo bricks back on the shelf for commuting—they puff when stored full and gain resistance within days, making them poor daily scooter batteries.[^lipo]
- Expect winter range to fall sharply (~30 Wh/km vs 18–20 Wh/km in summer); keep packs warm indoors or add gentle heaters before charging below freezing.[^winter]
- Pro 2 dashboards shipped after DRV2.2.3 clamp custom firmware; stay on DRV2.2.3 or temporarily downgrade to DRV155 to configure Rita before returning to the latest release.[^pro2-fw]
- Never power a 16 S conversion by tapping a 10 S segment for the controller—the idle draw unbalances the pack faster than the BMS can correct, even if the adapter only sips ≈12 mA.[^tap-imbalance]
- Secret-mode unlocks still require holding full brake and throttle while double-tapping the dash button; forgetting to exit walk mode caps speed near 20 km/h, and removing the dash Lisp while it’s locked freezes the limit until you reinstall it.[^41]
- Firmware 6.05’s Ninebot branch adds fixed `secret-sport-fw`/`secret-sport-watts` parameters and a ~470 Ω throttle resistor recommendation, and riders add RC filters across the hall supply so headlights stop dragging brake voltage low.[^42]
- Keep throttle and brake harnesses hard-wired once configuration is done; field reports show random power cuts when the dash proxies those signals, so treat the display as instrumentation rather than a control path.[^43]

---

## Source Notes

[^1]: [^44]
[^2]: [^45][^46]
[^3]: [^47][^44]
[^4]: [^48]
[^5]: [^49][^50]
[^6]: [^51][^52]
[^7]: [^53][^54]
[^8]: [^55][^56]
[^mounting]: [^57]
[^lap-base]: [^58]
[^vesc-plate]: [^59]
[^9]: [^60][^61][^62]
[^10]: [^63]
[^hv-supply]: [^64]
[^11]: [^65]
[^12]: [^66]
[^13]: [^67]
[^xiaodash]: [^14]
[^14]: [^68][^69]
[^return-jumper]: [^70]
[^15]: [^45]
[^16]: [^71]
[^17]: [^72][^73]
[^18]: [^69][^74]
[^19]: [^74]
[^13s-brick]: [^75]
[^balance-leads-xiaomi]: [^76]
[^20]: [^77][^78]
[^21]: [^50][^79]
[^22]: [^80][^81][^82]
[^23]: [^66][^83]
[^24]: [^84]
[^25]: [^85][^86]
[^26]: [^86][^87]
[^lipo]: [^88]
[^winter]: [^89]
[^27]: [^90]
[^charger-led]: [^91]
[^tool-pack]: [^92]
[^ali48]: [^93]
[^rita60v_xiaomi]: [^94]
[^connector-ceiling]: [^95]
[^ios-companion]: [^96]
[^current-step]: [^97][^98]
[^pro2-fw]: [^28]
[^hill-technique]: [^99]
[^parts-kit]: [^100][^101]
[^pack-temps]: [^102]
[^20s-burn]: Doubling a 10 S Xiaomi/Ninebot build to 20 S roughly doubles unloaded speed but repeatedly burned stock hubs in community testing, so veterans treat 18 S as the upper limit without major motor swaps.[^103]
[^fiido-l3]: Riders suggested the Fiido L3 rear hub for 20 S conversions because its wider stator and unobstructed casing dump heat better than Xiaomi-class motors, surviving abuse that killed smaller hubs within days.[^104]
[^deck-layout]: Packing 20 S 1–2 P or even 30 S 1 P bricks into M365 decks demanded relocating controllers (e.g., mounting a Ubox Lite underneath) and aggressive harness rerouting, effectively recreating a compact G30LP layout.[^105]
[^tap-imbalance]: [^101]


## References

[^1]: Source: knowledge/notes/denis_all_part02_review.md†L118600-L118609
[^2]: Source: data/vesc_help_group/text_slices/input_part001.txt†L6015-L6114
[^3]: Source: knowledge/notes/denis_all_part02_review.md†L302-L302
[^4]: Source: knowledge/notes/denis_all_part02_review.md†L393-L394
[^5]: Source: knowledge/notes/input_part000_review.md†L229-L230
[^6]: Source: data/vesc_help_group/text_slices/input_part009.txt†L14989-L14998
[^7]: Source: knowledge/notes/input_part004_review.md†L264-L264
[^8]: Source: knowledge/notes/input_part004_review.md†L267-L267
[^9]: Source: data/vesc_help_group/text_slices/input_part004.txt†L12982-L12995
[^10]: Source: knowledge/notes/input_part007_review.md†L309-L314
[^11]: Source: knowledge/notes/denis_all_part02_review.md†L492-L493
[^12]: Source: knowledge/notes/denis_all_part02_review.md†L99777-L99795
[^13]: Source: knowledge/notes/denis_all_part02_review.md†L329-L330
[^14]: Source: knowledge/notes/denis_all_part02_review.md†L114513-L114519
[^15]: Source: data/vesc_help_group/text_slices/input_part001.txt†L21680-L21840
[^16]: Source: data/vesc_help_group/text_slices/input_part001.txt†L21780-L21868
[^17]: Source: knowledge/notes/input_part003_review.md†L142-L142
[^18]: Source: knowledge/notes/all_part01_review.md†L350-L350
[^19]: Source: knowledge/notes/all_part01_review.md†L331-L331
[^20]: Source: knowledge/notes/denis_all_part02_review.md†L409-L411
[^21]: Source: knowledge/notes/all_part01_review.md†L317-L317
[^22]: Source: knowledge/notes/all_part01_review.md†L179-L179
[^23]: Source: knowledge/notes/input_part000_review.md†L253-L253
[^24]: Source: knowledge/notes/all_part01_review.md†L312-L312
[^25]: Source: knowledge/notes/denis_all_part02_review.md†L99966-L99999
[^26]: Source: knowledge/notes/input_part003_review.md†L170-L170
[^27]: Source: knowledge/notes/denis_all_part02_review.md†L335-L336
[^28]: Source: knowledge/notes/all_part01_review.md†L176-L176
[^29]: Source: knowledge/notes/input_part001_review.md†L528-L529
[^30]: Source: knowledge/notes/all_part01_review.md†L313-L313
[^31]: Source: knowledge/notes/all_part01_review.md†L181-L181
[^32]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L97446-L97459
[^33]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89361-L89420
[^34]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89576-L89578
[^35]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89652-L89661
[^36]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L90181-L90183
[^37]: Source: knowledge/notes/denis_all_part02_review.md†L389-L390
[^38]: Source: knowledge/notes/denis_all_part02_review.md†L390-L391
[^39]: Source: knowledge/notes/denis_all_part02_review.md†L430-L430
[^40]: Source: knowledge/notes/input_part000_review.md†L300-L300
[^41]: Source: knowledge/notes/input_part008_review.md†L215-L216
[^42]: Source: knowledge/notes/input_part008_review.md†L216-L216
[^43]: Source: knowledge/notes/input_part008_review.md†L217-L217
[^44]: Source: knowledge/notes/denis_all_part02_review.md†L114-L116
[^45]: Source: knowledge/notes/denis_all_part02_review.md†L101-L102
[^46]: Source: knowledge/notes/denis_all_part02_review.md†L157-L158
[^47]: Source: knowledge/notes/denis_all_part02_review.md†L35-L39
[^48]: Source: knowledge/notes/denis_all_part02_review.md†L11-L12
[^49]: Source: knowledge/notes/denis_all_part02_review.md†L12-L13
[^50]: Source: knowledge/notes/denis_all_part02_review.md†L32
[^51]: Source: knowledge/notes/denis_all_part02_review.md†L13
[^52]: Source: knowledge/notes/denis_all_part02_review.md†L37
[^53]: Source: knowledge/notes/denis_all_part02_review.md†L22
[^54]: Source: knowledge/notes/denis_all_part02_review.md†L218
[^55]: Source: knowledge/notes/denis_all_part02_review.md†L38-L39
[^56]: Source: knowledge/notes/denis_all_part02_review.md†L147
[^57]: Source: knowledge/notes/denis_all_part02_review.md†L140-L143
[^58]: Source: knowledge/notes/all_part01_review.md†L180-L180
[^59]: Source: knowledge/notes/denis_all_part02_review.md†L155-L156
[^60]: Source: knowledge/notes/all_part01_review.md†L121-L123
[^61]: Source: knowledge/notes/denis_all_part02_review.md†L11
[^62]: Source: knowledge/notes/denis_all_part02_review.md†L155-L167
[^63]: Source: knowledge/notes/all_part01_review.md†L94-L96
[^64]: Source: knowledge/notes/all_part01_review.md†L107-L107
[^65]: Source: knowledge/notes/all_part01_review.md†L73-L74
[^66]: Source: knowledge/notes/all_part01_review.md†L169-L170
[^67]: Source: knowledge/notes/denis_all_part02_review.md†L110-L111
[^68]: Source: knowledge/notes/denis_all_part02_review.md†L23
[^69]: Source: knowledge/notes/denis_all_part02_review.md†L124
[^70]: Source: knowledge/notes/all_part01_review.md†L343-L343
[^71]: Source: knowledge/notes/denis_all_part02_review.md†L136-L137
[^72]: Source: knowledge/notes/all_part01_review.md†L102-L103
[^73]: Source: knowledge/notes/all_part01_review.md†L151-L151
[^74]: Source: knowledge/notes/denis_all_part02_review.md†L158-L159
[^75]: Source: knowledge/notes/denis_all_part02_review.md†L194-L195
[^76]: Source: knowledge/notes/denis_all_part02_review.md†L7028-L7068
[^77]: Source: knowledge/notes/denis_all_part02_review.md†L50-L51
[^78]: Source: knowledge/notes/denis_all_part02_review.md†L161-L168
[^79]: Source: knowledge/notes/denis_all_part02_review.md†L213
[^80]: Source: knowledge/notes/denis_all_part02_review.md†L153-L154
[^81]: Source: knowledge/notes/denis_all_part02_review.md†L165-L168
[^82]: Source: knowledge/notes/all_part01_review.md†L333-L333
[^83]: Source: knowledge/notes/denis_all_part02_review.md†L29-L33
[^84]: Source: knowledge/notes/all_part01_review.md†L122-L123
[^85]: Source: knowledge/notes/denis_all_part02_review.md†L15-L17
[^86]: Source: knowledge/notes/denis_all_part02_review.md†L56-L57
[^87]: Source: knowledge/notes/denis_all_part02_review.md†L171-L175
[^88]: Source: knowledge/notes/denis_all_part02_review.md†L115837-L115845
[^89]: Source: knowledge/notes/denis_all_part02_review.md†L160-L162
[^90]: Source: knowledge/notes/denis_all_part02_review.md†L10541-L10598
[^91]: Source: knowledge/notes/input_part011_review.md†L18-L18
[^92]: Source: knowledge/notes/denis_all_part02_review.md†L8873-L8893
[^93]: Source: knowledge/notes/denis_all_part02_review.md†L114472-L114485
[^94]: Source: knowledge/notes/denis_all_part02_review.md†L9495-L9520
[^95]: Source: knowledge/notes/all_part01_review.md†L206-L207
[^96]: Source: knowledge/notes/all_part01_review.md†L213-L213
[^97]: Source: knowledge/notes/all_part01_review.md†L205-L206
[^98]: Source: knowledge/notes/all_part01_review.md†L348-L348
[^99]: Source: knowledge/notes/denis_all_part02_review.md†L102538-L102548
[^100]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60004-L60024
[^101]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60151-L60159
[^102]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60004-L60008
[^103]: Source: data/vesc_help_group/text_slices/input_part011.txt†L19101-L19145
[^104]: Source: data/vesc_help_group/text_slices/input_part011.txt†L19136-L19173
[^105]: Source: data/vesc_help_group/text_slices/input_part011.txt†L19145-L19185
[^gabe-22s]: Source: knowledge/notes/input_part010_review.md†L499-L500
[^deck-relocate]: Source: knowledge/notes/input_part011_review.md†L509-L511 and L610-L611
[^sleeper-hardware]: Source: knowledge/notes/input_part011_review.md†L510-L510
[^17s_speed]: Source: knowledge/notes/all_part01_review.md†L676-L676
[^series_booster_guardrail]: Source: knowledge/notes/all_part01_review.md†L675-L675
[^tudor_headroom]: Source: knowledge/notes/all_part01_review.md†L684-L684
[^star_delta_warning]: Source: knowledge/notes/all_part01_review.md†L687-L687
[^dual13s_cap]: Source: knowledge/notes/all_part01_review.md†L729-L729
[^12s14s_speed_benchmark]: Source: knowledge/notes/all_part01_review.md†L730-L730
[^monorim_500w_heat]: Source: knowledge/notes/all_part01_review.md†L728-L728
