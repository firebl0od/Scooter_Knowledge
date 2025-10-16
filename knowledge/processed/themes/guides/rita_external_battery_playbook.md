# Rita External Battery Deployment Playbook

## Pre-Build Checklist

| Check | Why it Matters | Notes |
| --- | --- | --- |
| Use a common-port BMS on every auxiliary pack | Separate charge ports let the charger overrun cells through the discharge lead. Rita only emulates Xiaomi data lines; it will not balance cells for you. | Swap third-party boards before pairing AliExpress packs with Rita; Daly boards stay reliable in common-port mode but still forbid charging 13 S packs through Rita’s lead.[^common-port][^denis-emulation-ext][^denis-daly-common]
| Pre-charge external packs before connection | Rita only engages externals once their voltage meets or exceeds the internal battery. | Top-charge auxiliaries before plugging them in so Rita latches cleanly.[^precharge]
| Inspect harness length and XT30 condition | Rita ships with XT30 pigtails sized for the enclosure; hot-swapping wears them quickly. | Reinforce joints and avoid repeated plugs/unplugs.[^xt30]
| Upgrade the stock charge JST before pushing >2.5 A | Xiaomi’s OEM JST warms even at 2.5 A; 4 A bricks overheat it without new connectors or bypass leads. | Rewire higher-current chargers to XT30 or dedicated ports before fast-charging Rita builds; stock ports and JST tails stay happy around 3 A.[^jst-heat][^denis-3a-port-ext]
| Enable Rita’s external-battery mode for 12 S packs and avoid hot-swapping while rolling | External-mode tuning keeps voltage limits aligned, and yanking a 50 V pack mid-ride backfeeds the 42 V internal through the motor. | Configure the profile before plugging in externals and only swap packs when stopped.[^denis-external-mode]
| Plan anti-spark placement between Rita and the controller | Cutting power upstream of the adapter keeps Rita’s charge logic live. | Mount switches between Rita and the scooter controller instead of between the battery and Rita.[^antispark]
| Vet pack specs and Y-cable build quality | Counterfeit “13.8 Ah” 10S2P packs and unsoldered Y-cables have already shorted bags. | Demand cell-level photos, dispute impossible ratings, and rework joints before mounting.[^ali-audit] |
| Confirm donor packs are scooter-grade | Lawn mower/tool batteries overheat near 25 A and barely contribute unless voltage matches scooter packs. | Skip five-cell tool packs and verify wattage before strapping externals to Rita.[^tool-warning] |
| Match external chemistry and wiring | Rita only tolerates identical external packs with common charge/discharge ports.
  - mixing a factory pack and Litokala brick through one harness can pop the adapter. | Keep externals the same series count and BMS topology before paralleling.[^1] |
| Never parallel 48 V and 36 V packs directly | Voltage deltas dump current violently without Rita handling the blend. | Equalise matching packs before connection and rely on Rita when mixing series counts; direct pairing invites huge inrush and pack damage.[^2] |
| Skip serial “speed booster” bricks | Small 2S/3S add-ons backfeed the main pack if they fall behind in voltage and regularly blow stock ESCs around 54.6 V. | Commission a full 13 S internal upgrade or Rita-managed external instead of strapping mismatched boosters in series.[^3][^4] |
| Scootermode 13 S Range+Speed kit prerequisites | The harness relies on Rita’s emulator and a jumper to silence error 21 once voltage climbs toward 55 V. | Raise Xiaomi nominal voltage in firmware, enable BMS emulation, and reseat the harness jumper after waterproofing before first ride.[^denis-13s-kit] |
| Leave modern jumpers intact | Current Rita harnesses ship ready for 13 S use.
  - set cell count in the app before connecting packs instead of cutting jumpers on newer boards.[^5] | Prevents self-inflicted wiring faults on updated hardware. |
| Stock up on 5–5.5 mm bullet connectors | Rita and Happy harnesses use common “banana” bullets.
  - larger plugs reduce heating on 30 A builds. | Verify diameter before ordering; AliExpress listings vary wildly.[^bullet] |
| Pre-fit the Wildman 2 L case or equivalent mount | Denis’ 8 Ah/12 S3P modules are sized to the 2 L shell; larger customs need 3 L brackets. | Square 10S3P packs slide into 2 L bags while 10S4P bricks need honeycomb spacing; pad the internal screws, route the lead upward, and note that the Wildman E2 (≈180 × 105 × 83 mm) fits 8 Ah bricks while the 1 L shell only swallows compact 36 V hoverboard packs; 3 L shells demand printed brackets plus bolt sleeves so externals stay fixed instead of floating on foam.[^cases][^wildman-stl][^square-10s3p]
| Model bag volume for 13S customs | A 13S4P barely fits 3 L shells; Denis’ own 13S4P bricks just squeeze into the Wildman 2 L, and stacking two builds a 13S8P tower that tames voltage sag for dual 500 W hubs. Expect LG MJ1 cores to droop more than Samsung 35E under the same loads. | Mock up layouts before drilling hardware into the pack; 12 S “speed” bricks do not fit a stock Pro/Pro 2 deck without lowering the floor.[^bag-volume][^bag-stack][^denis-12s-fit]
| Match XT60 discharge hardware | Current harnesses ship with XT60 leads (plus an XT30 adapter), so wire externals with native XT60 and anti-spark hardware instead of stacking adapters. | Prevents connector heating and keeps polarity consistent across packs.[^6] |
| Pre-fit the Wildman 2 L case or equivalent mount | Denis’ 8 Ah/12 S3P modules are sized to the 2 L shell; larger customs need 3 L brackets. | Square 10S3P packs slide into 2 L bags while 10S4P bricks need honeycomb spacing; pad the internal screws, route the lead upward, and print Denis’ updated 2 L/3 L STL mounts with bolt sleeves so externals stay fixed instead of floating on foam.[^cases][^wildman-stl][^square-10s3p]
| Model bag volume for 13S customs | A 13S4P barely fits 3 L shells; Denis’ own 13S4P bricks just squeeze into the Wildman 2 L, and stacking two builds a 13S8P tower that tames voltage sag for dual 500 W hubs. Builders have also wedged 16S3P 21700 assemblies into 3 L cases by deleting cell holders, then bracing them with custom mounts. Expect LG MJ1 cores to droop more than Samsung 35E under the same loads. | Mock up layouts before drilling hardware into the pack.[^bag-volume][^bag-stack]
| Stage firmware tools (M365 BMS Tool or XiaFlasher) and plan BLE downgrades | Configuration toggles (e.g., permanent emulator, cell count) require legacy BLE versions. | BLE 073/090 restore connectivity when the latest dashboard blocks access.[^ble]
| Set Rita’s nominal voltage before swapping packs | Leaving the adapter configured for a 10 S pack while plugging in 12 S externals (or vice versa) confuses the controller even if it boots. | Open the Rita app before each pack change and confirm the nominal voltage matches the external you’re about to connect.[^denis-app-voltage-ext]
| Reinforce controllers for ≥12 S or >27 A tunes | Stock traces and MOSFETs overheat above ~1 kW. | Pair firmware changes with soldered copper, thermal paste refresh, and conservative current ramps.[^thermal-prep]
| Keep Rita’s charge splitter inline | Removing the splitter when relocating charge ports hides charger presence and bypasses surge protections. | Leave the three-way harness installed even when the jack is moved outside the deck.[^splitter]
| Confirm balance-lead order before first charge | Daly smart boards have popped when sense wires were doubled or mis-ordered. | Wire the negative first, meter each cell step, and avoid stacking two leads on one pad.[^balance-wiring]
| Cap battery and regen limits near 27 A | Newer Rita boards beep error 39 above ~25 A continuous, even if firmware sliders allow more. | Match firmware battery/regen limits and monitor for warning beeps during shakedown rides.[^current-cap]

## Installation Workflow

1. **Top-balance packs**: Bring the external battery slightly above the internal pack (≈0.3–0.5 V) so Rita preferentially latches onto it during setup.[^balance]
2. **Mount the enclosure**: Seat the pack inside the Wildman case, add foam over the shallow screws, and secure the bag without pinching the deck latch or wiring; in tight decks, stage the harness along the controller side, tuck power runs under the charge port, and use Monorim stem slack before clamping the cover.[^mount][^tight-deck]
   - Builders now bolt Wildman bags through eight screw points with wide washers, fiberglass sleeving, and internal foam blocks so the pack can’t rattle, chafe on hardware, or eject during pothole hits.[^7]
3. **Route and secure leads**: Keep XT30 connectors strain-relieved, ensure the Y-cable uses two female battery legs feeding a single male controller lead, add anti-spark switches between Rita and the controller if desired, and avoid repeated hot-swaps.[^lead-care][^ali-audit]
   - When pairing Rita with a Xiaomi boat battery, connect the internal pack first so the adapter recognises the baseline voltage before you plug externals back in.[^8]
4. **Wire telemetry (if present)**: Retain the Xiaomi dashboard for Bluetooth control; clone scooters need dashboard swaps or serial adapters (CP2102 + pull-up) to access configuration.[^telemetry-setup]
5. **Flash and configure**: Downgrade BLE, connect the M365 BMS Tool, enable the permanent-emulator mode for analog scooters, and set the correct series count before first ride.[^configure]

- Reopen the app every time you swap external pack voltage.
  - builders toggling between 36 V and 48 V externals update Rita’s series/capacity fields before reconnecting to keep braking protections alive.[^9]
6. **Perform voltage and regen checks**: Verify recuperation-off voltage (≈4.15 V for 12 S), confirm throttle response using conservative intensity-of-current-change values (~300–350 mA), and watch for error 39 beeps that indicate regen or battery current above Rita’s ceiling.[^regen-check][^current-cap]

- Let new installs rest on the charger until they hit roughly 51 V before the first ride so the 12 S boost is evident and regen patches are validated under full voltage.[^first-ride]
- Skip XiaoFlasher’s 13 S emulator for regular use—it adds throttle lag, whereas Rita’s own emulation keeps large internal packs responsive on the stock dash.[^xiaoflasher_lag]

## Configuration Scenarios

### Baseline M365 / Pro (10S Parallel)

- Range Boost kits double usable capacity without firmware edits because the auxiliary pack mirrors stock voltage and the OEM charger feeds both packs through Rita.[^range-boost]
- Range+Speed owners must retune firmware or disable the 12 S profile before riding without the auxiliary pack; the range-only kit can unplug the extra battery with no firmware changes.[^range-speed-firmware]
- Keep regenerative braking within moderate settings—aggressive presets such as CWF W can scorch unreinforced traces in a few emergency stops.[^regen-risk]
- Expect telemetry to hop between packs during charge/discharge; disconnect or top-charge the external pack when you need to read its stats.[^telemetry-hop]

### 12 S Upgrade Path

- Complete three prerequisites: flash 50.4 V-ready firmware, reinforce controller power rails, and secure a 12 S-capable charger.
  - the stock 42 V Xiaomi brick stops at 10 S, so either add a 14.3 kΩ feedback stack to the OEM supply or adopt a Mean Well ELG-240-48A-class unit once you source the coaxial plug.[^12s-steps][^hv-charger]
- Cut Rita’s pink jumper only when stepping beyond 10 S, retain XT30 hardware, and continue matching pack voltages before parallel connection.[^jumper]
- Limit sustained draws near 27 A (~800 W) unless you have robust cooling (ferrofluid, thermal paste refresh) and MOSFET upgrades.[^current-limit]
- Keep nominal voltage at 51 V in XiaoFlasher/XiaoGen profiles so Rita’s charge thresholds and protections remain aligned after the upgrade.[^fiftyone]
- Reprogram Rita every time you swap between 10 S and 12 S externals; the workshop explicitly warned that leaving the adapter on 10 S while plugging a 12 S pack will disable braking protections until you correct the setting.[^swap-settings]
- Pro 2 dashboards still need DRV2.2.3 (or a temporary downgrade to DRV155) to configure Rita, and the Android app lacks native Pro 2 BLE support.
  - toggle permanent-emulator mode via desktop tools before returning to newer firmware.[^pro2-config]

### Clone Scooters without Data Lines

- Rita can operate as paired smart diodes, sharing current between packs while blocking reverse flow; regenerative braking must remain disabled in this analog mode.[^analog-mode]
- Serial configuration requires grounding FTDI to Rita, TX→yellow, RX→white, and a 1–10 kΩ pull-up because Rita’s TX pin is open-drain.[^serial]
- For full telemetry and firmware control, migrate to Xiaomi dashboards/controllers or adopt Denis’ repair BMS with USB-UART configuration.[^clone-upgrade]

### 13 S Experiments (Advanced Only)

- Cut the sense jumper, reconfigure cell count in the M365 BMS Tool, and raise firmware limits cautiously; reverting to 10 S after cutting the jumper is unsafe.[^13s-setup]
- Plan for aftermarket controllers or extensive reinforcement—the community still treats 13 S as experimental with limited support.[^13s-risk]
- Expect additional SMD resistor/capacitor work on Xiaomi controllers and remember that once those parts are moved the board is effectively locked to high-voltage duty.[^smd-lock]
- Remember that Rita still enforces ~25 A; even 15 S externals only shine when paired with uprated controllers and properly matched internals.[^15s-limit]

## Operational Practices

### Charging & Energy Management

- Rita charges whichever pack sits lower and will sequence mixed 10S/12S stacks.
  - expect the internal pack to plateau around 42 V before higher-voltage externals continue climbing. The adapter keeps topping packs after shutdown, the dash often sits at ~99 % until externals finish balancing, so watch the charger LED or Rita app for real completion and unplug externals when you need standalone charging because both packs share the scooter inlet.[^charge-flow][^mixed-charge][^denis-charge-led]
- A 13S6P pack built from 2 500 mAh cells lands near 20 Ah in 10S terms and roughly doubles Pro-range, but keep Rita’s shared 5 A limit in mind by splitting charge current across dedicated ports rather than hammering one lead.[^denis-13s6p]
- Denis caps his smart-BMS charge port around 3 A; firmware and the Schottky path overheat above that, so bigger connectors alone won’t raise charge current safely.[^denis-charge-cap-ext]
- When paralleling two externals, “marry” them at identical voltages, leave the XT splitter installed afterward, and favour common-port BMS boards so Rita can sense charge flow cleanly.[^denis-marry-packs-ext]
- Partially charged packs still hit their amp ceilings until voltage sag forces power sharing or thermal cutbacks—log live amps even when auxiliaries aren’t full so you catch overheating early.[^denis-sag-amps-ext]
- Range + Speed kits let both batteries charge from the bundled 50.4 V brick, but splitting them across chargers shortens downtime and keeps BMS temperatures in check.[^denis-range-charge]
- Treat 13 S chargers on 12 S packs as emergency-only top-ups—unplug early or use a timer, because survival depends on the BMS tripping before the pack overcharges.[^13s-emergency]
- Non-common-port externals still need standalone charging.
  - Rita prioritises the lower-voltage pack first, but feeding a charger through the discharge lead bypasses the external BMS entirely.[^lower-pack-first][^common-port-split]
- External-only charge sessions demand manual harness swaps once the auxiliary pack leaves the scooter; use a dedicated XT30 adapter rather than expecting Rita to backfeed a loose pack.[^harness-swap]
- Capacity tests happen with a constant-current load while the internal pack stays connected.
  - only reconnect externals once voltages sit within about 1 V to avoid hammering the weaker BMS.[^10]
- Happy BMS packs tolerate 54.6 V (13 S) chargers on 14 S builds; they simply stop early, so plan reduced range until the proper charger arrives rather than skipping rides.[^11]
- Reusing a spare Xiaomi pack externally is electrically straightforward once voltages match.
  - the bottleneck is mounting space, so most riders eventually switch to Denis’ purpose-built externals instead.[^12]
- Dual 10 S packs do not strictly require Rita inline, but conservative builders leave it in place for monitoring.
  - expect charge sessions to plateau around 41.2 V because the adapter’s diodes mirror the stock charger behaviour.[^13]
- Charging through Rita tops the internal pack first; unplug externals and use a dedicated XT30 harness when you need to fast-charge auxiliary batteries.[^fast-charge]
- Charging a Happy BMS pack through its XT30 controller lead bypasses overvoltage protection.
  - if you must backfeed that way, babysit the meter to avoid overcharging cells.[^14]
- Expect the internal pack to rest a few tenths below full charge—Rita deliberately leaves headroom for regen and will beep error 39 if sustained pulls exceed its 25 A ceiling.[^undercharge]
- Respect BMS charge ceilings: G30-class Ninebots accept Segway’s 5 A fast charger via the 8 mm barrel, while F-series and Xiaomi packs cap around 4 A continuous.
  - dial adjustable supplies accordingly.[^15]
- Rita draws a small standby current even while the scooter sleeps; recharge storage packs every few weeks or disconnect externals for long layoffs so BMS protection never hits zero.[^16]
- Daly boards only bleed cells above roughly 4.18 V, whereas Happy BMS can trim at any state of charge yet still self-discharges about 0.6 % per day unless you wake it with a charger pulse.[^bms-balancing]
- During discharge, Rita always favors the higher-voltage pack first; equal-voltage 10S+10S builds share current once voltages converge, so avoid tricks to “force” external-first draining.[^voltage-favor]
- Regen is blocked on a full auxiliary pack—bleed a few percent off the top and confirm Rita’s cell-count setting before expecting e-brake recovery again.[^regen-block]
- Set recuperation-off voltage around 4.10 V on 12 S/13 S builds (with future app tweaks toward 4.18 V) and keep braking currents conservative; leaving KERS active on long descents can still overload unreinforced controllers.[^recutoff]
- Skip series experiments through Rita. Stacking extra 3 S boosters trips regen protections, backfeeds low-voltage packs through the negative pole, and can overcharge internals.
  - wire odd-series packs outside the adapter with their own charge leads instead.[^series-skip][^serial-backfeed]
- Trickle sources such as 100 W solar panels work while riding so long as the DC/DC feed stays under ~1.7 A and firmware ignores charge mode; anything higher risks burning the converter.[^solar]
- Treat the internal pack as a rider, not a charger.
  - repurposing it to backfeed other batteries without current limiting is a documented fire risk; build dedicated externals with their own BMS instead.[^pack-fire]
- External packs support direct charging via dedicated harnesses; Denis is developing XT30-to-Xiaomi adapters for easier off-scooter top-ups.[^offboard-charge]
- Cap shared-port charging around 2 A to protect the OEM BMS; use dedicated high-current chargers when faster turnaround is needed.[^charge-limit]
- Budget for a real 50.4 V supply.
  - Mean Well ELG-240-48A-class bricks or modded Xiaomi chargers with 14.3 kΩ feedback stacks
  - and source the OEM coaxial plug before final assembly; acquiring the connector is often the hardest step.[^hv-charger]
- Check pack SOC when shipments arrive.
  - warehouses often target 30–50 % for long-term compliance even if some scooters ship near full, so balance packs before hard use.[^17]
- Keep packs above ~10 °C in winter with heated bags or external warmers to stop Molicel-equipped builds from sagging on cold commutes.[^18]
- Store packs near 3.7 V per cell in temperate spaces—cold garages accelerate degradation.[^storage]
- For oversized Ninebot packs, divide capacity by charger current to plan turnaround times.
  - 38 Ah modules take roughly 13 hours on the stock 3 A brick and about 7.5 hours on a vetted 5 A “speed cable,” which the group confirmed sits within Happy/Ninebot limits.[^g2-charge]
- If Rita “ghosts” an external pack (voltage present but no data), blip the throttle for a second to force re-detection and consult Denis’ living manual for additional recovery steps.[^ghost-pack]
- Dashboards may briefly jump from ~25 % to ~60–70 % during heavy regen; treat the spike as cosmetic until the firmware patch lands.[^soc-swing]

### Riding & Thermal Limits

- Motors and controllers run hotter after voltage upgrades; monitor temperature and raise recuperation-off voltage to 4.15 V to avoid throttle kicks on full batteries.[^thermal-ops]
- Rita’s 25 A ceiling limits how much hill-climb torque a small booster pack can add—plan dual motors or uprated controllers for sustained grades.[^hill-limit]
- Rita delays external-pack engagement until after boot to dodge Xiaomi’s error 24 voltage check; that guard disappears if you run only an external pack without the internal battery connected.[^error24-guard]
- Voltage-matched packs extend range dramatically (~2.1× on the Pro, ~2.8× on base models) but still demand honest capacity and careful current sharing.[^range-planning]
- Avoid hammering low state-of-charge packs with high current—overheating drivetrains is more likely than starving quality cells.[^soc-warning]
- Rita’s 25 A ceiling limits steep hill attempts with tiny boost packs; use controller reinforcements or dual-motor conversions when climbs trigger repeated cutbacks.[^hill-limit]
- 60 V experiments remain provisional—monitor Rita’s alarms, confirm BLE firmware, and stage launches before trusting the higher voltage for commuting.[^rita60v_ext]

### Maintenance & Safety

- Refresh controller thermal paste and add lithium grease to suspension pivots to handle added load.[^maintenance][^denis-thermal-paste]
- Mount the Wildman bag upright and cinch it with heavy clamps or cages—glue fills slow thieves less than they slow legitimate service.[^bag-security]
- Use quality cells (Samsung 35E or vetted 21700s), fish paper on positive terminals, and proper insulation when gluing dense packs.[^pack-build]
- Rita only blends packs once their voltages match; cheap 10S externals that sag early leave the internal battery carrying the load, so test suspect packs alone at light current and expect quality cells to cost more.[^denis-pack-sag]
- Treat the dash’s 50 % reading as the “head home” mark—Rita scrambles stock state-of-charge math once dual packs enter the mix.[^denis-dash-50]
- Without Rita you must equalise voltages before paralleling spare Xiaomi packs; the adapter makes plug-and-play swaps between scooters painless.[^denis-equalise]
- Separate-port BMS boards stay safe under regen because Rita handles discharge flow, but they leave charging unprotected—use the dedicated charge plug or only risk discharge-lead charging once packs sit well below full.[^separate-charge-risk]
- Inspect 3D-printed rear mounts every few rides; heavy 13 S bricks crack around the rear bolt and immediately skew group voltages, so replace fatigued prints with metal or reinforced composites before high-speed runs.[^19]
- The Rita BMS Tool remains Android-only; the crew circulates a debug APK because the Play Store build lags new hardware releases.[^denis-android]
- Clamp the Wildman bag with pipe clamps or a cage so thieves can’t unzip and steal the pack mid-ride.[^security]
- Keep documentation handy: Denis’ storefront hosts installation guides and expects ticket submissions with order IDs for manual payment reconciliation.[^support]
- Skip LiFePO₄-specific BMS boards when you are building li-ion packs—the voltage windows do not align, so protections misfire and cells go unprotected.[^lifepo4-bms]
- Swap Daly 10S boards if they stop balancing after a week; treat the fault as a battery issue first and verify balance-lead pinouts before installing replacements.[^denis-daly-balance]
- Replace Rita’s 30 A fuse with a stout (~65 W) iron and stick with the original rating—overfusing to 40 A risks burning the adapter’s internal circuitry during a fault.[^rita-fuse]
- Recharge Rita-equipped scooters after long storage.
  - the adapter idles around 2 mA (≈0.6 % per day on typical externals), so leave packs near storage voltage only if you plan periodic top-ups.[^16]
- Rita does not speed up Xiaomi’s weak internal balancing routine; equalising a tired pack can still take weeks even with the adapter installed.[^slow-balance]
- Rita always drains the higher-voltage pack first, then shares load once voltages equalise; saggy externals hand control back to the stock pack and should be diagnosed with the BMS tool under load.[^denis-pack-share]

### Hardware Roadmap & Procurement Notes

- Mid-2021 batches introduced a 40 A “Gen 2” Rita after month-long field tests; treat the higher-current hardware as beta until your own logs confirm stability.[^rita40]
- Current production harnesses ship with XT60 leads plus an XT30 adapter—rewire external packs with native XT60 (ideally via anti-spark switches) to reduce resistance.[^xt60-batch]
- Expect roughly one-week fulfillment once Denis returns from vacations; June 2021 buyers saw backlog-clearing shipping the week after ordering.[^leadtime]

## Troubleshooting Quick Reference

| Symptom | Likely Cause | Corrective Actions |
| --- | --- | --- |
| Rita ignores an external pack showing ~27 V | The adapter treats sub-32 V inputs as empty or the pack uses a separate-port BMS. | Top-charge toward nominal voltage and swap to a common-port board so Rita recognises the pack before trying again.[^20]
| External pack drops offline mid-ride | Harness vibration loosened connectors or popped the inline fuse. | Reseat every plug, separate bundled leads, and inspect the external fuse before condemning the pack.[^florian-pack]
| M365 BMS Tool cannot connect | Dashboard on latest BLE firmware blocks access. | Downgrade BLE to 073/090 and close other Bluetooth apps before retrying.[^ble]
| Error 14 on dual dashboards | Cross-pack current leakage after Rita install. | Re-check polarity, isolate each controller, and verify Rita blocks inter-pack flow before commuting.[^error14] |
| Error 18 after controller swap | Damaged hall harness | Replace the hall cable when multiple controllers throw the same fault post-upgrade.[^error18] |
| Error 24 after wiring changes | Supply voltage out of range | Power-cycle for 10 seconds and inspect the charge splitter plus pack voltages before deeper teardown.[^error24] |
| Error 21 after an emergency stop | Regen spike likely cooked the controller data line. | Bench-test with a known-good scooter or send the pack in before blaming the BMS.[^error21] |
| Adapter loses BMS telemetry after flashing | Rita needs a clean reset to the stock harness before reflashing the battery BMS. | Remove the adapter, restore factory wiring, flash the 12800 image via ST-Link, recharge to ≈41–42 V, then reinstall Rita.[^bms-reflash] |
| Telemetry shows 0 W or flips between packs | Rita reports whichever pack sits ~0.5 V higher; current sensor design hides wattage. | Match voltages, disconnect the higher pack temporarily, or use the pack’s BMS app for readings.[^telemetry-hop]
| External telemetry disappears while charging | Rita hides the auxiliary pack indicator whenever a charger is connected. | Treat blank readings as normal until the charger is unplugged; rely on charger LEDs, standalone voltmeters, or the Rita app until Denis ships the promised telemetry update.[^21][^rita-charge-telemetry] |
| Pro 2 setups still cannot open the M365 BMS Tool | The platform lacks BLE support even after flashing paid firmware. | Configure Rita with XiaoFlasher or desktop tools instead of relying on the M365 BMS Tool when working on Pro 2 dashboards.[^22] |
| Regen jerks throttle after full charge | Recuperation threshold too low on 12 S/13 S setups. | Raise recuperation-off voltage to ≈4.15 V and retest braking intensity.[^regen-check]
| Rita fuse blows or pack overheats | Non-common-port BMS or miswired external battery. | Rewire with common-port boards and verify polarity before reconnecting.[^common-port]
| Controller thermal shutdowns | Excessive current or insufficient reinforcement. | Reduce current-change intensity, add cooling mods, and inspect solder reinforcements.[^thermal-prep]
| Repeating beeps with error 39 | Charger or regen pushing Rita above ~25 A. | Check firmware battery/regen limits, log live amps with m365Tools, validate charger voltage, and keep the splitter inline so protections engage.[^error39][^log-current]
| Charger never leaves CV phase | Anonymous “48 V” bricks lack documented CC/CV stages or overshoot voltage. | Source YZPOWER 13 S chargers, solder and heat-shrink connector swaps, and avoid stacking >3 A through Xiaomi’s JST port.[^charger-quality] |

---

## Source Notes

[^parallel]: [^23][^24]
[^antispark]: [^25]
[^common-port]: [^26][^27][^28][^29]
[^denis-daly-common]: Source: knowledge/notes/denis_all_part02_review.md†L873-L873
[^xt30]: [^30][^31][^32][^33]
[^cases]: [^34][^35][^36][^37]
[^common-port-split]: [^27]
[^wildman-stl]: [^38]
[^ble]: [^39][^40][^41]
[^thermal-prep]: [^42][^43][^44][^45]
[^balance]: [^46][^24][^47]
[^mount]: [^34][^35][^37]
[^lead-care]: [^30][^31][^48][^49][^33]
[^splitter]: [^50]
[^balance-wiring]: [^51]
[^telemetry-setup]: [^52][^53][^54]
[^configure]: [^40][^55][^41]
[^harness-swap]: [^56]
[^regen-check]: [^57][^58]
[^current-cap]: [^59][^60][^61][^62]
[^range-boost]: [^63][^64]
[^range-speed-firmware]: [^65]
[^precharge]: Source: knowledge/notes/denis_all_part02_review.md†L616-L616
[^jst-heat]: Source: knowledge/notes/denis_all_part02_review.md†L617-L617
[^denis-3a-port-ext]: Source: knowledge/notes/denis_all_part02_review.md†L874-L874
[^denis-emulation-ext]: Source: knowledge/notes/denis_all_part02_review.md†L731-L731
[^denis-app-voltage-ext]: Source: knowledge/notes/denis_all_part02_review.md†L727-L727,†L776-L776
[^denis-external-mode]: Source: knowledge/notes/denis_all_part02_review.md†L871-L871
[^denis-charge-led]: Source: knowledge/notes/denis_all_part02_review.md†L782-L782
[^denis-charge-cap-ext]: Source: knowledge/notes/denis_all_part02_review.md†L734-L734
[^denis-marry-packs-ext]: Source: knowledge/notes/denis_all_part02_review.md†L736-L736
[^denis-sag-amps-ext]: Source: knowledge/notes/denis_all_part02_review.md†L739-L739
[^denis-range-charge]: Source: knowledge/notes/denis_all_part02_review.md†L795-L795
[^denis-thermal-paste]: Source: knowledge/notes/denis_all_part02_review.md†L781-L781
[^denis-daly-balance]: Source: knowledge/notes/denis_all_part02_review.md†L740-L740
[^error24-guard]: Source: knowledge/notes/denis_all_part02_review.md†L621-L621
[^slow-balance]: Source: knowledge/notes/denis_all_part02_review.md†L623-L623
[^florian-pack]: Source: knowledge/notes/denis_all_part02_review.md†L622-L622
[^denis-pack-share]: Source: knowledge/notes/denis_all_part02_review.md†L688-L689
[^denis-android]: Source: knowledge/notes/denis_all_part02_review.md†L688-L688
[^regen-risk]: [^66]
[^mixed-charge]: [^67][^68]
[^telemetry-hop]: [^69][^47][^41][^70]
[^rita-charge-telemetry]: Source: knowledge/notes/denis_all_part02_review.md†L1064-L1064
[^error39]: [^59][^71][^72]
[^13s-emergency]: Emergency-only note about nudging 12 S packs with 13 S chargers; Denis warns survival depends on the BMS tripping before overcharge.[^73]
[^connector-upgrade]: Builders replacing Xiaomi’s JST charge plug with XT30/XT60 or XT90S hardware to support 5 A charging and cleaner phase upgrades.[^74]
[^parallel-charge]: Dual-pack charging guidance recommending parallel JST leads for balancing while respecting ≈3 A limits and upgrading discharge runs to XT60 for ≥40 A loads.[^75]
[^charger-quality]: Charging quality discussion pointing to YZPOWER 13 S bricks, soldered connector swaps, and warnings about anonymous “48 V” chargers lacking CC/CV stages.[^76]
[^log-current]: [^77]
[^undercharge]: [^78]
[^12s-steps]: [^79][^80]
[^jumper]: [^81][^82]
[^current-limit]: [^42][^43][^44][^45]
[^fiftyone]: [^83][^84]
[^first-ride]: [^85]
[^analog-mode]: [^26][^86]
[^serial]: [^87]
[^clone-upgrade]: [^88][^54][^89]
[^13s-setup]: [^82]
[^13s-risk]: [^90]
[^15s-limit]: [^59][^91][^92]
[^swap-settings]: [^93][^94]
[^smd-lock]: [^95][^96]
[^g2-charge]: [^97]
[^charge-flow]: [^98][^99][^100][^101][^102]
[^lower-pack-first]: [^103]
[^charging-telemetry-guide]: [^101][^102][^104]
[^schottky]: [^105][^106]
[^offboard-charge]: [^107][^108][^109]
[^charge-limit]: [^110][^111]
[^storage]: [^112][^16]
[^thermal-ops]: [^113][^58]
[^range-planning]: [^114][^115][^116]
[^hill-limit]: [^60][^117]
[^soc-warning]: [^42][^118]
[^maintenance]: [^119][^120][^121]
[^pack-build]: [^48][^122][^123][^124][^125]
[^denis-pack-sag]: Source: knowledge/notes/denis_all_part02_review.md†L875-L875
[^denis-dash-50]: Source: knowledge/notes/denis_all_part02_review.md†L876-L876
[^denis-equalise]: Source: knowledge/notes/denis_all_part02_review.md†L877-L877
[^separate-charge-risk]: Source: knowledge/notes/denis_all_part02_review.md†L1040-L1040
[^security]: [^126]
[^support]: [^127][^128]
[^ali-audit]: [^129]
[^tool-warning]: Lawn mower and five-cell tool packs were never designed for Rita’s ~25 A loads; the workshop flagged them as fire risks and recommended sticking to scooter-grade 10–12 S modules instead.[^130][^131]
[^denis-13s-kit]: Source: knowledge/notes/denis_all_part02_review.md†L905-L905
[^denis-13s6p]: Source: knowledge/notes/denis_all_part02_review.md†L906-L906
[^pack-fire]: [^132]
[^bag-security]: [^133]
[^tight-deck]: [^134]
[^lifepo4-bms]: [^135]
[^rita-fuse]: [^136]
[^xiaoflasher_lag]: XiaoFlasher’s 13 S emulator introduces throttle lag, so Denis advises relying on Rita’s emulation to keep large internal packs responsive with the stock dashboard.[^137]
[^error14]: [^138]
[^error18]: [^139]
[^error24]: [^140]
[^rita60v_ext]: Rita 60 V bench tests still demand staged launches, firmware checks, and close monitoring of adapter alarms before anyone relies on the higher voltage for real rides.[^141]
[^bullet]: [^142]
[^voltage-favor]: [^143]
[^regen-block]: [^144]
[^error21]: [^145]
[^bag-volume]: [^146]
[^denis-12s-fit]: Source: knowledge/notes/denis_all_part02_review.md†L872-L872
[^square-10s3p]: Source: knowledge/notes/denis_all_part02_review.md†L1023-L1025
[^bag-stack]: [^147]
[^fast-charge]: [^148]
[^recutoff]: [^149]
[^ghost-pack]: [^150]
[^soc-swing]: [^151]
[^hv-charger]: [^152][^153]
[^pro2-config]: [^154]
[^happy-35a-ext]: [^155]
[^happy-charge-limit]: [^156]
[^bms-balancing]: [^157]
[^series-skip]: Attempting to stack extra 3 S boosters in series through Rita fails.
  - regen shuts down and the adapter risks overcharging the internal pack unless each segment has its own charger.[^158]
[^serial-backfeed]: [^4]
[^solar]: Rita will pass ~1.6–1.7 A from a 100 W solar panel while riding so long as firmware ignores charge mode; higher current overheats the DC/DC source.[^159]
[^bms-reflash]: Recovering lost telemetry requires removing Rita, restoring stock wiring, flashing the 12800 BMS image via ST-Link, charging to ~41–42 V, then reinstalling the adapter.[^160]
[^rita40]: Denis confirmed the 40 A “Gen 2” Rita batch went into production mid-June after extended road tests.[^161]
[^xt60-batch]: Current kits ship with XT60 pigtails plus an XT30 adapter; Denis still recommends wiring externals with native XT60 and anti-spark hardware.[^162][^6]
[^leadtime]: Post-vacation fulfillment resumed with roughly one-week lead times as Denis cleared the June backlog.[^163]


## References

[^1]: Source: knowledge/notes/denis_all_part02_review.md†L116206-L116215
[^2]: Source: knowledge/notes/denis_all_part02_review.md†L508-L508
[^3]: Source: knowledge/notes/denis_all_part02_review.md†L302-L302
[^4]: Source: knowledge/notes/denis_all_part02_review.md†L393-L394
[^5]: Source: knowledge/notes/denis_all_part02_review.md†L122300-L122315
[^6]: Source: knowledge/notes/denis_all_part02_review.md†L445-L445
[^7]: Source: knowledge/notes/denis_all_part02_review.md†L361-L362
[^8]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L89652-L89661
[^9]: Source: knowledge/notes/denis_all_part02_review.md†L58-L59
[^10]: Source: knowledge/notes/denis_all_part02_review.md†L335-L336
[^11]: Source: knowledge/notes/denis_all_part02_review.md†L345-L345
[^12]: Source: knowledge/notes/denis_all_part02_review.md†L101708-L101717
[^13]: Source: knowledge/notes/denis_all_part02_review.md†L97-L98
[^14]: Source: knowledge/notes/denis_all_part02_review.md†L118684-L118688
[^15]: Source: knowledge/notes/input_part006_review.md†L38-L38
[^16]: Source: knowledge/notes/denis_all_part02_review.md†L483-L484
[^17]: Source: knowledge/notes/input_part006_review.md†L39-L39
[^18]: Source: knowledge/notes/input_part006_review.md†L40-L40
[^19]: Source: knowledge/notes/denis_all_part02_review.md†L351-L352
[^20]: Source: knowledge/notes/all_part01_review.md†L304-L305
[^21]: Source: knowledge/notes/denis_all_part02_review.md†L408-L409
[^22]: Source: knowledge/notes/all_part01_review.md†L344-L344
[^23]: Source: knowledge/notes/all_part01_review.md†L16-L21
[^24]: Source: knowledge/notes/all_part01_review.md†L133
[^25]: Source: knowledge/notes/all_part01_review.md†L104-L104
[^26]: Source: knowledge/notes/all_part01_review.md†L19
[^27]: Source: knowledge/notes/all_part01_review.md†L101-L102
[^28]: Source: knowledge/notes/all_part01_review.md†L180
[^29]: Source: knowledge/notes/all_part01_review.md†L241-L242
[^30]: Source: knowledge/notes/all_part01_review.md†L20
[^31]: Source: knowledge/notes/all_part01_review.md†L24
[^32]: Source: knowledge/notes/all_part01_review.md†L61
[^33]: Source: knowledge/notes/all_part01_review.md†L223
[^34]: Source: knowledge/notes/all_part01_review.md†L45
[^35]: Source: knowledge/notes/all_part01_review.md†L48
[^36]: Source: knowledge/notes/all_part01_review.md†L94-L97
[^37]: Source: knowledge/notes/all_part01_review.md†L221-L223
[^38]: Source: knowledge/notes/denis_all_part02_review.md†L345-L346
[^39]: Source: knowledge/notes/all_part01_review.md†L12
[^40]: Source: knowledge/notes/all_part01_review.md†L23
[^41]: Source: knowledge/notes/all_part01_review.md†L219
[^42]: Source: knowledge/notes/all_part01_review.md†L22
[^43]: Source: knowledge/notes/all_part01_review.md†L73
[^44]: Source: knowledge/notes/all_part01_review.md†L123
[^45]: Source: knowledge/notes/all_part01_review.md†L155
[^46]: Source: knowledge/notes/all_part01_review.md†L21
[^47]: Source: knowledge/notes/all_part01_review.md†L139
[^48]: Source: knowledge/notes/all_part01_review.md†L46
[^49]: Source: knowledge/notes/all_part01_review.md†L55
[^50]: Source: knowledge/notes/denis_all_part02_review.md†L29-L30
[^51]: Source: knowledge/notes/denis_all_part02_review.md†L7028-L7068
[^52]: Source: knowledge/notes/all_part01_review.md†L16
[^53]: Source: knowledge/notes/all_part01_review.md†L44
[^54]: Source: knowledge/notes/all_part01_review.md†L206
[^55]: Source: knowledge/notes/all_part01_review.md†L71
[^56]: Source: knowledge/notes/all_part01_review.md†L105-L105
[^57]: Source: knowledge/notes/all_part01_review.md†L169-L171
[^58]: Source: knowledge/notes/all_part01_review.md†L265
[^59]: Source: knowledge/notes/denis_all_part02_review.md†L22
[^60]: Source: knowledge/notes/denis_all_part02_review.md†L31-L33
[^61]: Source: knowledge/notes/denis_all_part02_review.md†L135
[^62]: Source: knowledge/notes/denis_all_part02_review.md†L153
[^63]: Source: knowledge/notes/all_part01_review.md†L18
[^64]: Source: knowledge/notes/all_part01_review.md†L260
[^65]: Source: knowledge/notes/all_part01_review.md†L18-L18
[^66]: Source: knowledge/notes/all_part01_review.md†L171
[^67]: Source: knowledge/notes/all_part01_review.md†L103-L103
[^68]: Source: knowledge/notes/all_part01_review.md†L112-L112
[^69]: Source: knowledge/notes/all_part01_review.md†L25
[^70]: Source: knowledge/notes/all_part01_review.md†L261
[^71]: Source: knowledge/notes/denis_all_part02_review.md†L29-L33
[^72]: Source: knowledge/notes/denis_all_part02_review.md†L199
[^73]: Source: knowledge/notes/denis_all_part02_review.md†L101776-L101787
[^74]: Source: knowledge/notes/denis_all_part02_review.md†L510-L510
[^75]: Source: knowledge/notes/denis_all_part02_review.md†L540-L541
[^76]: Source: knowledge/notes/denis_all_part02_review.md†L598-L600
[^77]: Source: knowledge/notes/denis_all_part02_review.md†L122563-L122575
[^78]: Source: knowledge/notes/denis_all_part02_review.md†L220-L229
[^79]: Source: knowledge/notes/all_part01_review.md†L57
[^80]: Source: knowledge/notes/all_part01_review.md†L121
[^81]: Source: knowledge/notes/all_part01_review.md†L123-L124
[^82]: Source: knowledge/notes/all_part01_review.md†L162-L166
[^83]: Source: knowledge/notes/denis_all_part02_review.md†L27
[^84]: Source: knowledge/notes/denis_all_part02_review.md†L122
[^85]: Source: knowledge/notes/all_part01_review.md†L307-L307
[^86]: Source: knowledge/notes/all_part01_review.md†L114
[^87]: Source: knowledge/notes/all_part01_review.md†L112-L114
[^88]: Source: knowledge/notes/all_part01_review.md†L117
[^89]: Source: knowledge/notes/all_part01_review.md†L208
[^90]: Source: knowledge/notes/all_part01_review.md†L217-L218
[^91]: Source: knowledge/notes/denis_all_part02_review.md†L31
[^92]: Source: knowledge/notes/denis_all_part02_review.md†L115
[^93]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L20056-L20058
[^94]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L122582-L122584
[^95]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L202-L223
[^96]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60029-L60033
[^97]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131278-L131301
[^98]: Source: knowledge/notes/all_part01_review.md†L54
[^99]: Source: knowledge/notes/all_part01_review.md†L103
[^100]: Source: knowledge/notes/all_part01_review.md†L172
[^101]: Source: knowledge/notes/denis_all_part02_review.md†L33
[^102]: Source: knowledge/notes/denis_all_part02_review.md†L46
[^103]: Source: knowledge/notes/denis_all_part02_review.md†L443-L444
[^104]: Source: knowledge/notes/denis_all_part02_review.md†L127
[^105]: Source: knowledge/notes/denis_all_part02_review.md†L103-L104
[^106]: Source: knowledge/notes/denis_all_part02_review.md†L108-L110
[^107]: Source: knowledge/notes/all_part01_review.md†L47
[^108]: Source: knowledge/notes/all_part01_review.md†L56
[^109]: Source: knowledge/notes/all_part01_review.md†L251
[^110]: Source: knowledge/notes/all_part01_review.md†L96
[^111]: Source: knowledge/notes/all_part01_review.md†L250
[^112]: Source: knowledge/notes/all_part01_review.md†L252
[^113]: Source: knowledge/notes/all_part01_review.md†L169
[^114]: Source: knowledge/notes/all_part01_review.md†L229
[^115]: Source: knowledge/notes/all_part01_review.md†L199
[^116]: Source: knowledge/notes/denis_all_part02_review.md†L126-L127
[^117]: Source: knowledge/notes/denis_all_part02_review.md†L35-L38
[^118]: Source: knowledge/notes/all_part01_review.md†L262
[^119]: Source: knowledge/notes/all_part01_review.md†L188
[^120]: Source: knowledge/notes/all_part01_review.md†L211
[^121]: Source: knowledge/notes/all_part01_review.md†L266
[^122]: Source: knowledge/notes/all_part01_review.md†L145
[^123]: Source: knowledge/notes/all_part01_review.md†L185
[^124]: Source: knowledge/notes/all_part01_review.md†L238
[^125]: Source: knowledge/notes/all_part01_review.md†L245
[^126]: Source: knowledge/notes/denis_all_part02_review.md†L44-L45
[^127]: Source: knowledge/notes/all_part01_review.md†L17
[^128]: Source: knowledge/notes/all_part01_review.md†L150
[^129]: Source: knowledge/notes/denis_all_part02_review.md†L19-L23
[^130]: Source: knowledge/notes/denis_all_part02_review.md†L6610-L6635
[^131]: Source: knowledge/notes/denis_all_part02_review.md†L8873-L8893
[^132]: Source: knowledge/notes/denis_all_part02_review.md†L45-L46
[^133]: Source: knowledge/notes/denis_all_part02_review.md†L42-L45
[^134]: Source: knowledge/notes/denis_all_part02_review.md†L7534-L7589
[^135]: Source: knowledge/notes/denis_all_part02_review.md†L7080-L7089
[^136]: Source: knowledge/notes/denis_all_part02_review.md†L446-L446
[^137]: Source: knowledge/notes/denis_all_part02_review.md†L2467-L2470
[^138]: Source: knowledge/notes/denis_all_part02_review.md†L25-L27
[^139]: Source: knowledge/notes/denis_all_part02_review.md†L151-L152
[^140]: Source: knowledge/notes/denis_all_part02_review.md†L152-L153
[^141]: Source: knowledge/notes/denis_all_part02_review.md†L9495-L9520
[^142]: Source: knowledge/notes/denis_all_part02_review.md†L101695-L101722
[^143]: Source: knowledge/notes/denis_all_part02_review.md†L101707-L101728
[^144]: Source: knowledge/notes/denis_all_part02_review.md†L118642-L118646
[^145]: Source: knowledge/notes/denis_all_part02_review.md†L118622-L118635
[^146]: Source: knowledge/notes/denis_all_part02_review.md†L115874-L115898
[^147]: Source: knowledge/notes/all_part01_review.md†L171-L171
[^148]: Source: knowledge/notes/all_part01_review.md†L305-L305
[^149]: Source: knowledge/notes/all_part01_review.md†L212-L213
[^150]: Source: knowledge/notes/all_part01_review.md†L210-L210
[^151]: Source: knowledge/notes/all_part01_review.md†L175-L175
[^152]: Source: knowledge/notes/all_part01_review.md†L106-L107
[^153]: Source: knowledge/notes/all_part01_review.md†L123-L123
[^154]: Source: knowledge/notes/all_part01_review.md†L176-L177
[^155]: Source: knowledge/notes/denis_all_part02_review.md†L401-L401
[^156]: Source: knowledge/notes/denis_all_part02_review.md†L476-L476
[^157]: Source: knowledge/notes/denis_all_part02_review.md†L479-L481
[^158]: Source: knowledge/notes/all_part01_review.md†L92303-L92352
[^159]: Source: knowledge/notes/all_part01_review.md†L93065-L93088
[^160]: Source: knowledge/notes/all_part01_review.md†L92623-L92630
[^161]: Source: knowledge/notes/all_part01_review.md†L105675-L105684
[^162]: Source: knowledge/notes/all_part01_review.md†L107545-L107567
[^163]: Source: knowledge/notes/all_part01_review.md†L107566-L107573
