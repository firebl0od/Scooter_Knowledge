# Rita External Battery Deployment Playbook

## Pre-Build Checklist
| Check | Why it Matters | Notes |
| --- | --- | --- |
| Use a common-port BMS on every auxiliary pack | Separate charge ports let the charger overrun cells through the discharge lead. | Swap third-party boards before pairing AliExpress packs with Rita.[^common-port]
| Inspect harness length and XT30 condition | Rita ships with XT30 pigtails sized for the enclosure; hot-swapping wears them quickly. | Reinforce joints and avoid repeated plugs/unplugs.[^xt30]
| Vet pack specs and Y-cable build quality | Counterfeit “13.8 Ah” 10S2P packs and unsoldered Y-cables have already shorted bags. | Demand cell-level photos, dispute impossible ratings, and rework joints before mounting.[^ali-audit] |
| Confirm donor packs are scooter-grade | Lawn mower/tool batteries overheat near 25 A and barely contribute unless voltage matches scooter packs. | Skip five-cell tool packs and verify wattage before strapping externals to Rita.[^tool-warning] |
| Match external chemistry and wiring | Rita only tolerates identical external packs with common charge/discharge ports—mixing a factory pack and Litokala brick through one harness can pop the adapter. | Keep externals the same series count and BMS topology before paralleling.【F:knowledge/notes/denis_all_part02_review.md†L116206-L116215】 |
| Never parallel 48 V and 36 V packs directly | Voltage deltas dump current violently without Rita handling the blend. | Equalise matching packs before connection and rely on Rita when mixing series counts; direct pairing invites huge inrush and pack damage.【F:knowledge/notes/denis_all_part02_review.md†L508-L508】 |
| Leave modern jumpers intact | Current Rita harnesses ship ready for 13 S use—set cell count in the app before connecting packs instead of cutting jumpers on newer boards.【F:knowledge/notes/denis_all_part02_review.md†L122300-L122315】 | Prevents self-inflicted wiring faults on updated hardware. |
| Stock up on 5–5.5 mm bullet connectors | Rita and Happy harnesses use common “banana” bullets—larger plugs reduce heating on 30 A builds. | Verify diameter before ordering; AliExpress listings vary wildly.[^bullet] |
| Pre-fit the Wildman 2 L case or equivalent mount | Denis’ 8 Ah/12 S3P modules are sized to the 2 L shell; larger customs need 3 L brackets. | Pad the internal screws, route the lead upward, and print Denis’ updated 2 L/3 L STL mounts with bolt sleeves so externals stay fixed instead of floating on foam.[^cases][^wildman-stl]
| Model bag volume for 13S customs | A 13S4P barely fits 3 L shells; Denis’ own 13S4P bricks just squeeze into the Wildman 2 L, and stacking two builds a 13S8P tower that tames voltage sag for dual 500 W hubs. Expect LG MJ1 cores to droop more than Samsung 35E under the same loads. | Mock up layouts before drilling hardware into the pack.[^bag-volume][^bag-stack]
| Stage firmware tools (M365 BMS Tool or XiaFlasher) and plan BLE downgrades | Configuration toggles (e.g., permanent emulator, cell count) require legacy BLE versions. | BLE 073/090 restore connectivity when the latest dashboard blocks access.[^ble]
| Reinforce controllers for ≥12 S or >27 A tunes | Stock traces and MOSFETs overheat above ~1 kW. | Pair firmware changes with soldered copper, thermal paste refresh, and conservative current ramps.[^thermal-prep]
| Keep Rita’s charge splitter inline | Removing the splitter when relocating charge ports hides charger presence and bypasses surge protections. | Leave the three-way harness installed even when the jack is moved outside the deck.[^splitter]
| Confirm balance-lead order before first charge | Daly smart boards have popped when sense wires were doubled or mis-ordered. | Wire the negative first, meter each cell step, and avoid stacking two leads on one pad.[^balance-wiring]
| Cap battery and regen limits near 27 A | Newer Rita boards beep error 39 above ~25 A continuous, even if firmware sliders allow more. | Match firmware battery/regen limits and monitor for warning beeps during shakedown rides.[^current-cap]

## Installation Workflow
1. **Top-balance packs**: Bring the external battery slightly above the internal pack (≈0.3–0.5 V) so Rita preferentially latches onto it during setup.[^balance]
2. **Mount the enclosure**: Seat the pack inside the Wildman case, add foam over the shallow screws, and secure the bag without pinching the deck latch or wiring; in tight decks, stage the harness along the controller side, tuck power runs under the charge port, and use Monorim stem slack before clamping the cover.[^mount][^tight-deck]
3. **Route and secure leads**: Keep XT30 connectors strain-relieved, ensure the Y-cable uses two female battery legs feeding a single male controller lead, add anti-spark switches between Rita and the controller if desired, and avoid repeated hot-swaps.[^lead-care][^ali-audit]
4. **Wire telemetry (if present)**: Retain the Xiaomi dashboard for Bluetooth control; clone scooters need dashboard swaps or serial adapters (CP2102 + pull-up) to access configuration.[^telemetry-setup]
5. **Flash and configure**: Downgrade BLE, connect the M365 BMS Tool, enable the permanent-emulator mode for analog scooters, and set the correct series count before first ride.[^configure]
   - Reopen the app every time you swap external pack voltage—builders toggling between 36 V and 48 V externals update Rita’s series/capacity fields before reconnecting to keep braking protections alive.【F:knowledge/notes/denis_all_part02_review.md†L58-L59】
6. **Perform voltage and regen checks**: Verify recuperation-off voltage (≈4.15 V for 12 S), confirm throttle response using conservative intensity-of-current-change values (~300–350 mA), and watch for error 39 beeps that indicate regen or battery current above Rita’s ceiling.[^regen-check][^current-cap]
- Skip XiaoFlasher’s 13 S emulator for regular use—it adds throttle lag, whereas Rita’s own emulation keeps large internal packs responsive on the stock dash.[^xiaoflasher_lag]

## Configuration Scenarios

### Baseline M365 / Pro (10S Parallel)
- Range Boost kits double usable capacity without firmware edits because the auxiliary pack mirrors stock voltage and the OEM charger feeds both packs through Rita.[^range-boost]
- Range+Speed owners must retune firmware or disable the 12 S profile before riding without the auxiliary pack; the range-only kit can unplug the extra battery with no firmware changes.[^range-speed-firmware]
- Keep regenerative braking within moderate settings—aggressive presets such as CWF W can scorch unreinforced traces in a few emergency stops.[^regen-risk]
- Expect telemetry to hop between packs during charge/discharge; disconnect or top-charge the external pack when you need to read its stats.[^telemetry-hop]

### 12 S Upgrade Path
- Complete three prerequisites: flash 50.4 V-ready firmware, reinforce controller power rails, and secure a 12 S-capable charger (modding OEM bricks with a 14.3 kΩ resistor or sourcing 50.4 V CC/CV units).[^12s-steps]
- Cut Rita’s pink jumper only when stepping beyond 10 S, retain XT30 hardware, and continue matching pack voltages before parallel connection.[^jumper]
- Limit sustained draws near 27 A (~800 W) unless you have robust cooling (ferrofluid, thermal paste refresh) and MOSFET upgrades.[^current-limit]
- Keep nominal voltage at 51 V in XiaoFlasher/XiaoGen profiles so Rita’s charge thresholds and protections remain aligned after the upgrade.[^fiftyone]
- Reprogram Rita every time you swap between 10 S and 12 S externals; the workshop explicitly warned that leaving the adapter on 10 S while plugging a 12 S pack will disable braking protections until you correct the setting.[^swap-settings]

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
- Rita charges whichever pack sits lower, continuing to top batteries after the scooter powers down; rely on charger LEDs to confirm completion.[^charge-flow]
- Treat 13 S chargers on 12 S packs as emergency-only top-ups—unplug early or use a timer, because survival depends on the BMS tripping before the pack overcharges.[^13s-emergency]
- Non-common-port externals still need standalone charging—Rita prioritises the lower-voltage pack first, but feeding a charger through the discharge lead bypasses the external BMS entirely.[^lower-pack-first]
- Capacity tests happen with a constant-current load while the internal pack stays connected—only reconnect externals once voltages sit within about 1 V to avoid hammering the weaker BMS.【F:knowledge/notes/denis_all_part02_review.md†L335-L336】
- Dual 10 S packs do not strictly require Rita inline, but conservative builders leave it in place for monitoring—expect charge sessions to plateau around 41.2 V because the adapter’s diodes mirror the stock charger behaviour.【F:knowledge/notes/denis_all_part02_review.md†L97-L98】
- Charging through Rita tops the internal pack first; unplug externals and use a dedicated XT30 harness when you need to fast-charge auxiliary batteries.[^fast-charge]
- Expect the internal pack to rest a few tenths below full charge—Rita deliberately leaves headroom for regen and will beep error 39 if sustained pulls exceed its 25 A ceiling.[^undercharge]
- Swap Xiaomi’s slim JST charge plug for XT30/XT60 or XT90S hardware before chasing 5 A charging; secure soldered joints with heat-shrink instead of tape.[^connector-upgrade]
- Parallel the JST charge leads (two males into one female) so both BMS boards stay in balance control during dual-pack charging, but keep current under ≈3 A or move to XT60-class hardware for ≥40 A discharge legs.[^parallel-charge]
- Happy BMS coulomb counters peg at 0 % once ~32 Ah flows through 35 A externals; about 10 % energy remains, so treat the display as conservative range margin.[^happy-35a-ext]
- Happy BMS charge limits ship around 3 A; bump the ceiling to ~5.5 A in Embedden BMS Tool before using 5 A bricks so the adapter’s leads stay within spec.[^happy-charge-limit]
- Rita draws a small standby current even while the scooter sleeps; recharge storage packs every few weeks or disconnect externals for long layoffs so BMS protection never hits zero.【F:knowledge/notes/denis_all_part02_review.md†L97264-L97268】
- Daly boards only bleed cells above roughly 4.18 V, whereas Happy BMS can trim at any state of charge yet still self-discharges about 0.6 % per day unless you wake it with a charger pulse.[^bms-balancing]
- During discharge, Rita always favors the higher-voltage pack first; equal-voltage 10S+10S builds share current once voltages converge, so avoid tricks to “force” external-first draining.[^voltage-favor]
- Regen is blocked on a full auxiliary pack—bleed a few percent off the top and confirm Rita’s cell-count setting before expecting e-brake recovery again.[^regen-block]
- Set recuperation-off voltage around 4.10 V on 12 S/13 S builds (with future app tweaks toward 4.18 V) and keep braking currents conservative; leaving KERS active on long descents can still overload unreinforced controllers.[^recutoff]
- Skip series experiments through Rita. Stacking extra 3 S boosters trips regen protections, backfeeds low-voltage packs through the negative pole, and can overcharge internals—wire odd-series packs outside the adapter with their own charge leads instead.[^series-skip][^serial-backfeed]
- Trickle sources such as 100 W solar panels work while riding so long as the DC/DC feed stays under ~1.7 A and firmware ignores charge mode; anything higher risks burning the converter.[^solar]
- Treat the internal pack as a rider, not a charger—repurposing it to backfeed other batteries without current limiting is a documented fire risk; build dedicated externals with their own BMS instead.[^pack-fire]
- External packs support direct charging via dedicated harnesses; Denis is developing XT30-to-Xiaomi adapters for easier off-scooter top-ups.[^offboard-charge]
- Cap shared-port charging around 2 A to protect the OEM BMS; use dedicated high-current chargers when faster turnaround is needed.[^charge-limit]
- Happy BMS-equipped 14 S packs tolerate a 13 S (54.6 V) charger temporarily—it simply stops early until the correct brick arrives, trading range for safe top-ups.【F:knowledge/notes/denis_all_part02_review.md†L345-L345】
- Store packs near 3.7 V per cell in temperate spaces—cold garages accelerate degradation.[^storage]
- For oversized Ninebot packs, divide capacity by charger current to plan turnaround times—38 Ah modules take roughly 13 hours on the stock 3 A brick and about 7.5 hours on a vetted 5 A “speed cable,” which the group confirmed sits within Happy/Ninebot limits.[^g2-charge]
- If Rita “ghosts” an external pack (voltage present but no data), blip the throttle for a second to force re-detection and consult Denis’ living manual for additional recovery steps.[^ghost-pack]
- Dashboards may briefly jump from ~25 % to ~60–70 % during heavy regen; treat the spike as cosmetic until the firmware patch lands.[^soc-swing]

### Riding & Thermal Limits
- Motors and controllers run hotter after voltage upgrades; monitor temperature and raise recuperation-off voltage to 4.15 V to avoid throttle kicks on full batteries.[^thermal-ops]
- Rita’s 25 A ceiling limits how much hill-climb torque a small booster pack can add—plan dual motors or uprated controllers for sustained grades.[^hill-limit]
- Voltage-matched packs extend range dramatically (~2.1× on the Pro, ~2.8× on base models) but still demand honest capacity and careful current sharing.[^range-planning]
- Avoid hammering low state-of-charge packs with high current—overheating drivetrains is more likely than starving quality cells.[^soc-warning]
- Rita’s 25 A ceiling limits steep hill attempts with tiny boost packs; use controller reinforcements or dual-motor conversions when climbs trigger repeated cutbacks.[^hill-limit]
- 60 V experiments remain provisional—monitor Rita’s alarms, confirm BLE firmware, and stage launches before trusting the higher voltage for commuting.[^rita60v_ext]

### Maintenance & Safety
- Refresh controller thermal paste and add lithium grease to suspension pivots to handle added load.[^maintenance]
- Mount the Wildman bag upright and cinch it with heavy clamps or cages—glue fills slow thieves less than they slow legitimate service.[^bag-security]
- Use quality cells (Samsung 35E or vetted 21700s), fish paper on positive terminals, and proper insulation when gluing dense packs.[^pack-build]
- Clamp the Wildman bag with pipe clamps or a cage so thieves can’t unzip and steal the pack mid-ride.[^security]
- Keep documentation handy: Denis’ storefront hosts installation guides and expects ticket submissions with order IDs for manual payment reconciliation.[^support]
- Skip LiFePO₄-specific BMS boards when you are building li-ion packs—the voltage windows do not align, so protections misfire and cells go unprotected.[^lifepo4-bms]
- Replace Rita’s 30 A fuse with a stout (~65 W) iron and stick with the original rating—overfusing to 40 A risks burning the adapter’s internal circuitry during a fault.[^rita-fuse]

### Hardware Roadmap & Procurement Notes
- Mid-2021 batches introduced a 40 A “Gen 2” Rita after month-long field tests; treat the higher-current hardware as beta until your own logs confirm stability.[^rita40]
- Current production harnesses ship with XT60 leads plus an XT30 adapter—rewire external packs with native XT60 (ideally via anti-spark switches) to reduce resistance.[^xt60-batch]
- Expect roughly one-week fulfillment once Denis returns from vacations; June 2021 buyers saw backlog-clearing shipping the week after ordering.[^leadtime]

## Troubleshooting Quick Reference
| Symptom | Likely Cause | Corrective Actions |
| --- | --- | --- |
| M365 BMS Tool cannot connect | Dashboard on latest BLE firmware blocks access. | Downgrade BLE to 073/090 and close other Bluetooth apps before retrying.[^ble]
| Error 14 on dual dashboards | Cross-pack current leakage after Rita install. | Re-check polarity, isolate each controller, and verify Rita blocks inter-pack flow before commuting.[^error14] |
| Error 18 after controller swap | Damaged hall harness | Replace the hall cable when multiple controllers throw the same fault post-upgrade.[^error18] |
| Error 24 after wiring changes | Supply voltage out of range | Power-cycle for 10 seconds and inspect the charge splitter plus pack voltages before deeper teardown.[^error24] |
| Error 21 after an emergency stop | Regen spike likely cooked the controller data line. | Bench-test with a known-good scooter or send the pack in before blaming the BMS.[^error21] |
| Adapter loses BMS telemetry after flashing | Rita needs a clean reset to the stock harness before reflashing the battery BMS. | Remove the adapter, restore factory wiring, flash the 12800 image via ST-Link, recharge to ≈41–42 V, then reinstall Rita.[^bms-reflash] |
| Telemetry shows 0 W or flips between packs | Rita reports whichever pack sits ~0.5 V higher; current sensor design hides wattage. | Match voltages, disconnect the higher pack temporarily, or use the pack’s BMS app for readings.[^telemetry-hop]
| External telemetry disappears while charging | Rita hides the auxiliary pack indicator whenever a charger is connected. | Treat blank readings as normal until the charger is unplugged; rely on charger LEDs or the Rita app for confirmation.【F:knowledge/notes/denis_all_part02_review.md†L408-L409】 |
| Regen jerks throttle after full charge | Recuperation threshold too low on 12 S/13 S setups. | Raise recuperation-off voltage to ≈4.15 V and retest braking intensity.[^regen-check]
| Rita fuse blows or pack overheats | Non-common-port BMS or miswired external battery. | Rewire with common-port boards and verify polarity before reconnecting.[^common-port]
| Controller thermal shutdowns | Excessive current or insufficient reinforcement. | Reduce current-change intensity, add cooling mods, and inspect solder reinforcements.[^thermal-prep]
| Repeating beeps with error 39 | Charger or regen pushing Rita above ~25 A. | Check firmware battery/regen limits, log live amps with m365Tools, validate charger voltage, and keep the splitter inline so protections engage.[^error39][^log-current]
| Charger never leaves CV phase | Anonymous “48 V” bricks lack documented CC/CV stages or overshoot voltage. | Source YZPOWER 13 S chargers, solder and heat-shrink connector swaps, and avoid stacking >3 A through Xiaomi’s JST port.[^charger-quality] |

---

## Source Notes

[^parallel]: 【F:knowledge/notes/all_part01_review.md†L16-L21】【F:knowledge/notes/all_part01_review.md†L133】
[^common-port]: 【F:knowledge/notes/all_part01_review.md†L19】【F:knowledge/notes/all_part01_review.md†L180】【F:knowledge/notes/all_part01_review.md†L241-L242】
[^xt30]: 【F:knowledge/notes/all_part01_review.md†L20】【F:knowledge/notes/all_part01_review.md†L24】【F:knowledge/notes/all_part01_review.md†L61】【F:knowledge/notes/all_part01_review.md†L223】
[^cases]: 【F:knowledge/notes/all_part01_review.md†L45】【F:knowledge/notes/all_part01_review.md†L48】【F:knowledge/notes/all_part01_review.md†L221-L223】
[^wildman-stl]: 【F:knowledge/notes/denis_all_part02_review.md†L345-L346】
[^ble]: 【F:knowledge/notes/all_part01_review.md†L12】【F:knowledge/notes/all_part01_review.md†L23】【F:knowledge/notes/all_part01_review.md†L219】
[^thermal-prep]: 【F:knowledge/notes/all_part01_review.md†L22】【F:knowledge/notes/all_part01_review.md†L73】【F:knowledge/notes/all_part01_review.md†L123】【F:knowledge/notes/all_part01_review.md†L155】
[^balance]: 【F:knowledge/notes/all_part01_review.md†L21】【F:knowledge/notes/all_part01_review.md†L133】【F:knowledge/notes/all_part01_review.md†L139】
[^mount]: 【F:knowledge/notes/all_part01_review.md†L45】【F:knowledge/notes/all_part01_review.md†L48】【F:knowledge/notes/all_part01_review.md†L221-L223】
[^lead-care]: 【F:knowledge/notes/all_part01_review.md†L20】【F:knowledge/notes/all_part01_review.md†L24】【F:knowledge/notes/all_part01_review.md†L46】【F:knowledge/notes/all_part01_review.md†L55】【F:knowledge/notes/all_part01_review.md†L223】
[^splitter]: 【F:knowledge/notes/denis_all_part02_review.md†L29-L30】
[^balance-wiring]: 【F:knowledge/notes/denis_all_part02_review.md†L7028-L7068】
[^telemetry-setup]: 【F:knowledge/notes/all_part01_review.md†L16】【F:knowledge/notes/all_part01_review.md†L44】【F:knowledge/notes/all_part01_review.md†L206】
[^configure]: 【F:knowledge/notes/all_part01_review.md†L23】【F:knowledge/notes/all_part01_review.md†L71】【F:knowledge/notes/all_part01_review.md†L219】
[^regen-check]: 【F:knowledge/notes/all_part01_review.md†L169-L171】【F:knowledge/notes/all_part01_review.md†L265】
[^current-cap]: 【F:knowledge/notes/denis_all_part02_review.md†L22】【F:knowledge/notes/denis_all_part02_review.md†L31-L33】【F:knowledge/notes/denis_all_part02_review.md†L135】【F:knowledge/notes/denis_all_part02_review.md†L153】
[^range-boost]: 【F:knowledge/notes/all_part01_review.md†L18】【F:knowledge/notes/all_part01_review.md†L260】
[^range-speed-firmware]: 【F:knowledge/notes/all_part01_review.md†L18-L18】
[^regen-risk]: 【F:knowledge/notes/all_part01_review.md†L171】
[^telemetry-hop]: 【F:knowledge/notes/all_part01_review.md†L25】【F:knowledge/notes/all_part01_review.md†L139】【F:knowledge/notes/all_part01_review.md†L219】【F:knowledge/notes/all_part01_review.md†L261】
[^error39]: 【F:knowledge/notes/denis_all_part02_review.md†L22】【F:knowledge/notes/denis_all_part02_review.md†L29-L33】【F:knowledge/notes/denis_all_part02_review.md†L199】
[^13s-emergency]: Emergency-only note about nudging 12 S packs with 13 S chargers; Denis warns survival depends on the BMS tripping before overcharge.【F:knowledge/notes/denis_all_part02_review.md†L509-L509】
[^connector-upgrade]: Builders replacing Xiaomi’s JST charge plug with XT30/XT60 or XT90S hardware to support 5 A charging and cleaner phase upgrades.【F:knowledge/notes/denis_all_part02_review.md†L510-L510】
[^parallel-charge]: Dual-pack charging guidance recommending parallel JST leads for balancing while respecting ≈3 A limits and upgrading discharge runs to XT60 for ≥40 A loads.【F:knowledge/notes/denis_all_part02_review.md†L540-L541】
[^charger-quality]: Charging quality discussion pointing to YZPOWER 13 S bricks, soldered connector swaps, and warnings about anonymous “48 V” chargers lacking CC/CV stages.【F:knowledge/notes/denis_all_part02_review.md†L598-L600】
[^log-current]: 【F:knowledge/notes/denis_all_part02_review.md†L122563-L122575】
[^undercharge]: 【F:knowledge/notes/denis_all_part02_review.md†L220-L229】
[^12s-steps]: 【F:knowledge/notes/all_part01_review.md†L57】【F:knowledge/notes/all_part01_review.md†L121】
[^jumper]: 【F:knowledge/notes/all_part01_review.md†L123-L124】【F:knowledge/notes/all_part01_review.md†L162-L166】
[^current-limit]: 【F:knowledge/notes/all_part01_review.md†L22】【F:knowledge/notes/all_part01_review.md†L73】【F:knowledge/notes/all_part01_review.md†L123】【F:knowledge/notes/all_part01_review.md†L155】
[^fiftyone]: 【F:knowledge/notes/denis_all_part02_review.md†L27】【F:knowledge/notes/denis_all_part02_review.md†L122】
[^analog-mode]: 【F:knowledge/notes/all_part01_review.md†L19】【F:knowledge/notes/all_part01_review.md†L114】
[^serial]: 【F:knowledge/notes/all_part01_review.md†L112-L114】
[^clone-upgrade]: 【F:knowledge/notes/all_part01_review.md†L117】【F:knowledge/notes/all_part01_review.md†L206】【F:knowledge/notes/all_part01_review.md†L208】
[^13s-setup]: 【F:knowledge/notes/all_part01_review.md†L162-L166】
[^13s-risk]: 【F:knowledge/notes/all_part01_review.md†L217-L218】
[^15s-limit]: 【F:knowledge/notes/denis_all_part02_review.md†L22】【F:knowledge/notes/denis_all_part02_review.md†L31】【F:knowledge/notes/denis_all_part02_review.md†L115】
[^swap-settings]: 【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L20056-L20058】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L122582-L122584】
[^smd-lock]: 【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L202-L223】【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60029-L60033】
[^g2-charge]: 【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L131278-L131301】
[^charge-flow]: 【F:knowledge/notes/all_part01_review.md†L54】【F:knowledge/notes/all_part01_review.md†L172】【F:knowledge/notes/denis_all_part02_review.md†L33】【F:knowledge/notes/denis_all_part02_review.md†L46】
[^lower-pack-first]: 【F:knowledge/notes/denis_all_part02_review.md†L443-L444】
[^charging-telemetry-guide]: 【F:knowledge/notes/denis_all_part02_review.md†L33】【F:knowledge/notes/denis_all_part02_review.md†L46】【F:knowledge/notes/denis_all_part02_review.md†L127】
[^schottky]: 【F:knowledge/notes/denis_all_part02_review.md†L103-L104】【F:knowledge/notes/denis_all_part02_review.md†L108-L110】
[^offboard-charge]: 【F:knowledge/notes/all_part01_review.md†L47】【F:knowledge/notes/all_part01_review.md†L56】【F:knowledge/notes/all_part01_review.md†L251】
[^charge-limit]: 【F:knowledge/notes/all_part01_review.md†L96】【F:knowledge/notes/all_part01_review.md†L250】
[^storage]: 【F:knowledge/notes/all_part01_review.md†L252】【F:knowledge/notes/denis_all_part02_review.md†L483-L484】
[^thermal-ops]: 【F:knowledge/notes/all_part01_review.md†L169】【F:knowledge/notes/all_part01_review.md†L265】
[^range-planning]: 【F:knowledge/notes/all_part01_review.md†L229】【F:knowledge/notes/all_part01_review.md†L199】【F:knowledge/notes/denis_all_part02_review.md†L126-L127】
[^hill-limit]: 【F:knowledge/notes/denis_all_part02_review.md†L31-L33】【F:knowledge/notes/denis_all_part02_review.md†L35-L38】
[^soc-warning]: 【F:knowledge/notes/all_part01_review.md†L22】【F:knowledge/notes/all_part01_review.md†L262】
[^maintenance]: 【F:knowledge/notes/all_part01_review.md†L188】【F:knowledge/notes/all_part01_review.md†L211】【F:knowledge/notes/all_part01_review.md†L266】
[^pack-build]: 【F:knowledge/notes/all_part01_review.md†L46】【F:knowledge/notes/all_part01_review.md†L145】【F:knowledge/notes/all_part01_review.md†L185】【F:knowledge/notes/all_part01_review.md†L238】【F:knowledge/notes/all_part01_review.md†L245】
[^security]: 【F:knowledge/notes/denis_all_part02_review.md†L44-L45】
[^support]: 【F:knowledge/notes/all_part01_review.md†L17】【F:knowledge/notes/all_part01_review.md†L150】
[^ali-audit]: 【F:knowledge/notes/denis_all_part02_review.md†L19-L23】
[^tool-warning]: Lawn mower and five-cell tool packs were never designed for Rita’s ~25 A loads; the workshop flagged them as fire risks and recommended sticking to scooter-grade 10–12 S modules instead.【F:knowledge/notes/denis_all_part02_review.md†L6610-L6635】【F:knowledge/notes/denis_all_part02_review.md†L8873-L8893】
[^pack-fire]: 【F:knowledge/notes/denis_all_part02_review.md†L45-L46】
[^bag-security]: 【F:knowledge/notes/denis_all_part02_review.md†L42-L45】
[^tight-deck]: 【F:knowledge/notes/denis_all_part02_review.md†L7534-L7589】
[^lifepo4-bms]: 【F:knowledge/notes/denis_all_part02_review.md†L7080-L7089】
[^rita-fuse]: 【F:knowledge/notes/denis_all_part02_review.md†L446-L446】
[^xiaoflasher_lag]: XiaoFlasher’s 13 S emulator introduces throttle lag, so Denis advises relying on Rita’s emulation to keep large internal packs responsive with the stock dashboard.【F:knowledge/notes/denis_all_part02_review.md†L2467-L2470】
[^error14]: 【F:knowledge/notes/denis_all_part02_review.md†L25-L27】
[^error18]: 【F:knowledge/notes/denis_all_part02_review.md†L151-L152】
[^error24]: 【F:knowledge/notes/denis_all_part02_review.md†L152-L153】
[^rita60v_ext]: Rita 60 V bench tests still demand staged launches, firmware checks, and close monitoring of adapter alarms before anyone relies on the higher voltage for real rides.【F:knowledge/notes/denis_all_part02_review.md†L9495-L9520】
[^bullet]: 【F:knowledge/notes/denis_all_part02_review.md†L134-L136】
[^voltage-favor]: 【F:knowledge/notes/denis_all_part02_review.md†L134-L136】
[^regen-block]: 【F:knowledge/notes/denis_all_part02_review.md†L182-L184】
[^error21]: 【F:knowledge/notes/denis_all_part02_review.md†L179-L181】
[^bag-volume]: 【F:knowledge/notes/denis_all_part02_review.md†L164-L167】
[^bag-stack]: 【F:knowledge/notes/all_part01_review.md†L171-L171】
[^fast-charge]: 【F:knowledge/notes/all_part01_review.md†L305-L305】
[^recutoff]: 【F:knowledge/notes/all_part01_review.md†L212-L213】
[^ghost-pack]: 【F:knowledge/notes/all_part01_review.md†L210-L210】
[^soc-swing]: 【F:knowledge/notes/all_part01_review.md†L175-L175】
[^happy-35a-ext]: 【F:knowledge/notes/denis_all_part02_review.md†L401-L401】
[^happy-charge-limit]: 【F:knowledge/notes/denis_all_part02_review.md†L476-L476】
[^bms-balancing]: 【F:knowledge/notes/denis_all_part02_review.md†L479-L481】
[^series-skip]: Attempting to stack extra 3 S boosters in series through Rita fails—regen shuts down and the adapter risks overcharging the internal pack unless each segment has its own charger.【F:knowledge/notes/all_part01_review.md†L92303-L92352】
[^serial-backfeed]: 【F:knowledge/notes/denis_all_part02_review.md†L393-L394】
[^solar]: Rita will pass ~1.6–1.7 A from a 100 W solar panel while riding so long as firmware ignores charge mode; higher current overheats the DC/DC source.【F:knowledge/notes/all_part01_review.md†L93065-L93088】
[^bms-reflash]: Recovering lost telemetry requires removing Rita, restoring stock wiring, flashing the 12800 BMS image via ST-Link, charging to ~41–42 V, then reinstalling the adapter.【F:knowledge/notes/all_part01_review.md†L92623-L92630】
[^rita40]: Denis confirmed the 40 A “Gen 2” Rita batch went into production mid-June after extended road tests.【F:knowledge/notes/all_part01_review.md†L105675-L105684】
[^xt60-batch]: Current kits ship with XT60 pigtails plus an XT30 adapter; Denis still recommends wiring externals with native XT60 and anti-spark hardware.【F:knowledge/notes/all_part01_review.md†L107545-L107567】【F:knowledge/notes/denis_all_part02_review.md†L445-L445】
[^leadtime]: Post-vacation fulfillment resumed with roughly one-week lead times as Denis cleared the June backlog.【F:knowledge/notes/all_part01_review.md†L107566-L107573】
