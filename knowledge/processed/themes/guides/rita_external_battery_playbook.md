# Rita External Battery Deployment Playbook

## Pre-Build Checklist
| Check | Why it Matters | Notes |
| --- | --- | --- |
| Use a common-port BMS on every auxiliary pack | Separate charge ports let the charger overrun cells through the discharge lead. | Swap third-party boards before pairing AliExpress packs with Rita.[^common-port]
| Inspect harness length and XT30 condition | Rita ships with XT30 pigtails sized for the enclosure; hot-swapping wears them quickly. | Reinforce joints and avoid repeated plugs/unplugs.[^xt30]
| Vet pack specs and Y-cable build quality | Counterfeit “13.8 Ah” 10S2P packs and unsoldered Y-cables have already shorted bags. | Demand cell-level photos, dispute impossible ratings, and rework joints before mounting.[^ali-audit] |
| Confirm donor packs are scooter-grade | Lawn mower/tool batteries overheat near 25 A and barely contribute unless voltage matches scooter packs. | Skip five-cell tool packs and verify wattage before strapping externals to Rita.[^tool-warning] |
| Pre-fit the Wildman 2 L case or equivalent mount | Denis’ 8 Ah/12 S3P modules are sized to the 2 L shell; larger customs need 3 L brackets. | Pad the internal screws and route the lead upward to protect insulation.[^cases]
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
6. **Perform voltage and regen checks**: Verify recuperation-off voltage (≈4.15 V for 12 S), confirm throttle response using conservative intensity-of-current-change values (~300–350 mA), and watch for error 39 beeps that indicate regen or battery current above Rita’s ceiling.[^regen-check][^current-cap]
- Skip XiaoFlasher’s 13 S emulator for regular use—it adds throttle lag, whereas Rita’s own emulation keeps large internal packs responsive on the stock dash.[^xiaoflasher_lag]

## Configuration Scenarios

### Baseline M365 / Pro (10S Parallel)
- Range Boost kits double usable capacity without firmware edits because the auxiliary pack mirrors stock voltage and the OEM charger feeds both packs through Rita.[^range-boost]
- Keep regenerative braking within moderate settings—aggressive presets such as CWF W can scorch unreinforced traces in a few emergency stops.[^regen-risk]
- Expect telemetry to hop between packs during charge/discharge; disconnect or top-charge the external pack when you need to read its stats.[^telemetry-hop]

### 12 S Upgrade Path
- Complete three prerequisites: flash 50.4 V-ready firmware, reinforce controller power rails, and secure a 12 S-capable charger (modding OEM bricks with a 14.3 kΩ resistor or sourcing 50.4 V CC/CV units).[^12s-steps]
- Cut Rita’s pink jumper only when stepping beyond 10 S, retain XT30 hardware, and continue matching pack voltages before parallel connection.[^jumper]
- Limit sustained draws near 27 A (~800 W) unless you have robust cooling (ferrofluid, thermal paste refresh) and MOSFET upgrades.[^current-limit]
- Keep nominal voltage at 51 V in XiaoFlasher/XiaoGen profiles so Rita’s charge thresholds and protections remain aligned after the upgrade.[^fiftyone]

### Clone Scooters without Data Lines
- Rita can operate as paired smart diodes, sharing current between packs while blocking reverse flow; regenerative braking must remain disabled in this analog mode.[^analog-mode]
- Serial configuration requires grounding FTDI to Rita, TX→yellow, RX→white, and a 1–10 kΩ pull-up because Rita’s TX pin is open-drain.[^serial]
- For full telemetry and firmware control, migrate to Xiaomi dashboards/controllers or adopt Denis’ repair BMS with USB-UART configuration.[^clone-upgrade]

### 13 S Experiments (Advanced Only)
- Cut the sense jumper, reconfigure cell count in the M365 BMS Tool, and raise firmware limits cautiously; reverting to 10 S after cutting the jumper is unsafe.[^13s-setup]
- Plan for aftermarket controllers or extensive reinforcement—the community still treats 13 S as experimental with limited support.[^13s-risk]
- Remember that Rita still enforces ~25 A; even 15 S externals only shine when paired with uprated controllers and properly matched internals.[^15s-limit]

## Operational Practices

### Charging & Energy Management
- Rita charges whichever pack sits lower, continuing to top batteries after the scooter powers down; rely on charger LEDs to confirm completion.[^charge-flow]
- Expect the internal pack to rest a few tenths below full charge—Rita deliberately leaves headroom for regen and will beep error 39 if sustained pulls exceed its 25 A ceiling.[^undercharge]
- Treat the internal pack as a rider, not a charger—repurposing it to backfeed other batteries without current limiting is a documented fire risk; build dedicated externals with their own BMS instead.[^pack-fire]
- External packs support direct charging via dedicated harnesses; Denis is developing XT30-to-Xiaomi adapters for easier off-scooter top-ups.[^offboard-charge]
- Cap shared-port charging around 2 A to protect the OEM BMS; use dedicated high-current chargers when faster turnaround is needed.[^charge-limit]
- Store packs near 3.7 V per cell in temperate spaces—cold garages accelerate degradation.[^storage]

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

## Troubleshooting Quick Reference
| Symptom | Likely Cause | Corrective Actions |
| --- | --- | --- |
| M365 BMS Tool cannot connect | Dashboard on latest BLE firmware blocks access. | Downgrade BLE to 073/090 and close other Bluetooth apps before retrying.[^ble]
| Error 14 on dual dashboards | Cross-pack current leakage after Rita install. | Re-check polarity, isolate each controller, and verify Rita blocks inter-pack flow before commuting.[^error14] |
| Error 18 after controller swap | Damaged hall harness | Replace the hall cable when multiple controllers throw the same fault post-upgrade.[^error18] |
| Error 24 after wiring changes | Supply voltage out of range | Power-cycle for 10 seconds and inspect the charge splitter plus pack voltages before deeper teardown.[^error24] |
| Telemetry shows 0 W or flips between packs | Rita reports whichever pack sits ~0.5 V higher; current sensor design hides wattage. | Match voltages, disconnect the higher pack temporarily, or use the pack’s BMS app for readings.[^telemetry-hop]
| Regen jerks throttle after full charge | Recuperation threshold too low on 12 S/13 S setups. | Raise recuperation-off voltage to ≈4.15 V and retest braking intensity.[^regen-check]
| Rita fuse blows or pack overheats | Non-common-port BMS or miswired external battery. | Rewire with common-port boards and verify polarity before reconnecting.[^common-port]
| Controller thermal shutdowns | Excessive current or insufficient reinforcement. | Reduce current-change intensity, add cooling mods, and inspect solder reinforcements.[^thermal-prep]
| Repeating beeps with error 39 | Charger or regen pushing Rita above ~25 A. | Check firmware battery/regen limits, validate charger voltage, and keep the splitter inline so protections engage.[^error39]

---

## Source Notes

[^parallel]: 【F:knowledge/notes/all_part01_review.md†L16-L21】【F:knowledge/notes/all_part01_review.md†L133】
[^common-port]: 【F:knowledge/notes/all_part01_review.md†L19】【F:knowledge/notes/all_part01_review.md†L180】【F:knowledge/notes/all_part01_review.md†L241-L242】
[^xt30]: 【F:knowledge/notes/all_part01_review.md†L20】【F:knowledge/notes/all_part01_review.md†L24】【F:knowledge/notes/all_part01_review.md†L61】【F:knowledge/notes/all_part01_review.md†L223】
[^cases]: 【F:knowledge/notes/all_part01_review.md†L45】【F:knowledge/notes/all_part01_review.md†L48】【F:knowledge/notes/all_part01_review.md†L221-L223】
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
[^regen-risk]: 【F:knowledge/notes/all_part01_review.md†L171】
[^telemetry-hop]: 【F:knowledge/notes/all_part01_review.md†L25】【F:knowledge/notes/all_part01_review.md†L139】【F:knowledge/notes/all_part01_review.md†L219】【F:knowledge/notes/all_part01_review.md†L261】
[^error39]: 【F:knowledge/notes/denis_all_part02_review.md†L22】【F:knowledge/notes/denis_all_part02_review.md†L29-L33】【F:knowledge/notes/denis_all_part02_review.md†L199】
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
[^charge-flow]: 【F:knowledge/notes/all_part01_review.md†L54】【F:knowledge/notes/all_part01_review.md†L172】【F:knowledge/notes/denis_all_part02_review.md†L33】【F:knowledge/notes/denis_all_part02_review.md†L46】
[^charging-telemetry-guide]: 【F:knowledge/notes/denis_all_part02_review.md†L33】【F:knowledge/notes/denis_all_part02_review.md†L46】【F:knowledge/notes/denis_all_part02_review.md†L127】
[^schottky]: 【F:knowledge/notes/denis_all_part02_review.md†L103-L104】【F:knowledge/notes/denis_all_part02_review.md†L108-L110】
[^offboard-charge]: 【F:knowledge/notes/all_part01_review.md†L47】【F:knowledge/notes/all_part01_review.md†L56】【F:knowledge/notes/all_part01_review.md†L251】
[^charge-limit]: 【F:knowledge/notes/all_part01_review.md†L96】【F:knowledge/notes/all_part01_review.md†L250】
[^storage]: 【F:knowledge/notes/all_part01_review.md†L252】
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
[^xiaoflasher_lag]: XiaoFlasher’s 13 S emulator introduces throttle lag, so Denis advises relying on Rita’s emulation to keep large internal packs responsive with the stock dashboard.【F:knowledge/notes/denis_all_part02_review.md†L2467-L2470】
[^error14]: 【F:knowledge/notes/denis_all_part02_review.md†L25-L27】
[^error18]: 【F:knowledge/notes/denis_all_part02_review.md†L151-L152】
[^error24]: 【F:knowledge/notes/denis_all_part02_review.md†L152-L153】
[^rita60v_ext]: Rita 60 V bench tests still demand staged launches, firmware checks, and close monitoring of adapter alarms before anyone relies on the higher voltage for real rides.【F:knowledge/notes/denis_all_part02_review.md†L9495-L9520】
