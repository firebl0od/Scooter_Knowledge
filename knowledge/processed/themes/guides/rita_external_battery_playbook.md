# Rita External Battery Deployment Playbook

## Pre-Build Checklist
| Check | Why it Matters | Notes |
| --- | --- | --- |
| Use a common-port BMS on every auxiliary pack | Separate charge ports let the charger overrun cells through the discharge lead. | Swap third-party boards before pairing AliExpress packs with Rita.[^common-port]
| Inspect harness length and XT30 condition | Rita ships with XT30 pigtails sized for the enclosure; hot-swapping wears them quickly. | Reinforce joints and avoid repeated plugs/unplugs.[^xt30]
| Pre-fit the Wildman 2 L case or equivalent mount | Denis’ 8 Ah/12 S3P modules are sized to the 2 L shell; larger customs need 3 L brackets. | Pad the internal screws and route the lead upward to protect insulation.[^cases]
| Stage firmware tools (M365 BMS Tool or XiaFlasher) and plan BLE downgrades | Configuration toggles (e.g., permanent emulator, cell count) require legacy BLE versions. | BLE 073/090 restore connectivity when the latest dashboard blocks access.[^ble]
| Reinforce controllers for ≥12 S or >27 A tunes | Stock traces and MOSFETs overheat above ~1 kW. | Pair firmware changes with soldered copper, thermal paste refresh, and conservative current ramps.[^thermal-prep]
| Keep Rita’s charge splitter inline | Removing the splitter when relocating charge ports hides charger presence and bypasses surge protections. | Leave the three-way harness installed even when the jack is moved outside the deck.[^splitter]
| Cap battery and regen limits near 27 A | Newer Rita boards beep error 39 above ~25 A continuous, even if firmware sliders allow more. | Match firmware battery/regen limits and monitor for warning beeps during shakedown rides.[^current-cap]

## Installation Workflow
1. **Top-balance packs**: Bring the external battery slightly above the internal pack (≈0.3–0.5 V) so Rita preferentially latches onto it during setup.[^balance]
2. **Mount the enclosure**: Seat the pack inside the Wildman case, add foam over the shallow screws, and secure the bag without pinching the deck latch or wiring.[^mount]
3. **Route and secure leads**: Keep XT30 connectors strain-relieved, add anti-spark switches between Rita and the controller if desired, keep the charge splitter inline, and avoid repeated hot-swaps.[^lead-care][^splitter]
4. **Wire telemetry (if present)**: Retain the Xiaomi dashboard for Bluetooth control; clone scooters need dashboard swaps or serial adapters (CP2102 + pull-up) to access configuration.[^telemetry-setup]
5. **Flash and configure**: Downgrade BLE, connect the M365 BMS Tool, enable the permanent-emulator mode for analog scooters, and set the correct series count before first ride.[^configure]
6. **Perform voltage and regen checks**: Verify recuperation-off voltage (≈4.15 V for 12 S), confirm throttle response using conservative intensity-of-current-change values (~300–350 mA), and watch for error 39 beeps that indicate regen or battery current above Rita’s ceiling.[^regen-check][^current-cap]

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
- Rita charges whichever pack sits lower, continuing to top batteries after the scooter powers down; rely on charger LEDs or the Rita app because the dash may stall near 99 % until balancing finishes.[^charge-flow][^charging-telemetry-guide]
- Expect Rita’s Schottky drop to leave packs just under 42 V; bypass only if you truly need 100 % charge, since the mild undercharge extends pack life.[^schottky]
- External packs support direct charging via dedicated harnesses; Denis is developing XT30-to-Xiaomi adapters for easier off-scooter top-ups.[^offboard-charge]
- Cap shared-port charging around 2 A to protect the OEM BMS; use dedicated high-current chargers when faster turnaround is needed.[^charge-limit]
- Store packs near 3.7 V per cell in temperate spaces—cold garages accelerate degradation.[^storage]

### Riding & Thermal Limits
- Motors and controllers run hotter after voltage upgrades; monitor temperature and raise recuperation-off voltage to 4.15 V to avoid throttle kicks on full batteries.[^thermal-ops]
- Voltage-matched packs extend range dramatically (~2.1× on the Pro, ~2.8× on base models) but still demand honest capacity and careful current sharing.[^range-planning]
- Avoid hammering low state-of-charge packs with high current—overheating drivetrains is more likely than starving quality cells.[^soc-warning]
- Rita’s 25 A ceiling limits steep hill attempts with tiny boost packs; use controller reinforcements or dual-motor conversions when climbs trigger repeated cutbacks.[^hill-limit]

### Maintenance & Safety
- Refresh controller thermal paste and add lithium grease to suspension pivots to handle added load.[^maintenance]
- Use quality cells (Samsung 35E or vetted 21700s), fish paper on positive terminals, and proper insulation when gluing dense packs.[^pack-build]
- Clamp the Wildman bag with pipe clamps or a cage so thieves can’t unzip and steal the pack mid-ride.[^security]
- Keep documentation handy: Denis’ storefront hosts installation guides and expects ticket submissions with order IDs for manual payment reconciliation.[^support]

## Troubleshooting Quick Reference
| Symptom | Likely Cause | Corrective Actions |
| --- | --- | --- |
| M365 BMS Tool cannot connect | Dashboard on latest BLE firmware blocks access. | Downgrade BLE to 073/090 and close other Bluetooth apps before retrying.[^ble]
| Telemetry shows 0 W or flips between packs | Rita reports whichever pack sits ~0.5 V higher; current sensor design hides wattage. | Match voltages, disconnect the higher pack temporarily, or use the pack’s BMS app for readings.[^telemetry-hop]
| Regen jerks throttle after full charge | Recuperation threshold too low on 12 S/13 S setups. | Raise recuperation-off voltage to ≈4.15 V and retest braking intensity.[^regen-check]
| Rita fuse blows or pack overheats | Non-common-port BMS or miswired external battery. | Rewire with common-port boards and verify polarity before reconnecting.[^common-port]
| Controller thermal shutdowns | Excessive current or insufficient reinforcement. | Reduce current-change intensity, add cooling mods, and inspect solder reinforcements.[^thermal-prep]
| Repeating beeps with error 39 | Charger or regen pushing Rita above ~25 A. | Check firmware battery/regen limits, validate charger voltage, and keep the splitter inline so protections engage.[^error39]

---
[^parallel]: Source: `knowledge/notes/all_part01_review.md`, lines 16-21, 133.
[^common-port]: Source: `knowledge/notes/all_part01_review.md`, lines 19, 180, 241-242.
[^xt30]: Source: `knowledge/notes/all_part01_review.md`, lines 20, 24, 61, 223.
[^cases]: Source: `knowledge/notes/all_part01_review.md`, lines 45, 48, 221-223.
[^ble]: Source: `knowledge/notes/all_part01_review.md`, lines 12, 23, 219.
[^thermal-prep]: Source: `knowledge/notes/all_part01_review.md`, lines 22, 73, 123, 155.
[^balance]: Source: `knowledge/notes/all_part01_review.md`, lines 21, 133, 139.
[^mount]: Source: `knowledge/notes/all_part01_review.md`, lines 45, 48, 221-223.
[^lead-care]: Source: `knowledge/notes/all_part01_review.md`, lines 20, 24, 46, 55, 223.
[^splitter]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 29-30.
[^telemetry-setup]: Source: `knowledge/notes/all_part01_review.md`, lines 16, 44, 206.
[^configure]: Source: `knowledge/notes/all_part01_review.md`, lines 23, 71, 219.
[^regen-check]: Source: `knowledge/notes/all_part01_review.md`, lines 169-171, 265.
[^current-cap]: Sources: `knowledge/notes/denis_all_part02_review.md`, lines 22, 31-33, 135, 153.
[^range-boost]: Source: `knowledge/notes/all_part01_review.md`, lines 18, 260.
[^regen-risk]: Source: `knowledge/notes/all_part01_review.md`, line 171.
[^telemetry-hop]: Source: `knowledge/notes/all_part01_review.md`, lines 25, 139, 219, 261.
[^error39]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 22, 29-33, 199.
[^12s-steps]: Source: `knowledge/notes/all_part01_review.md`, lines 57, 121.
[^jumper]: Source: `knowledge/notes/all_part01_review.md`, lines 123-124, 162-166.
[^current-limit]: Source: `knowledge/notes/all_part01_review.md`, lines 22, 73, 123, 155.
[^fiftyone]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 27, 122.
[^analog-mode]: Source: `knowledge/notes/all_part01_review.md`, lines 19, 114.
[^serial]: Source: `knowledge/notes/all_part01_review.md`, lines 112-114.
[^clone-upgrade]: Source: `knowledge/notes/all_part01_review.md`, lines 117, 206, 208.
[^13s-setup]: Source: `knowledge/notes/all_part01_review.md`, lines 162-166.
[^13s-risk]: Source: `knowledge/notes/all_part01_review.md`, lines 217-218.
[^15s-limit]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 22, 31, 115.
[^charge-flow]: Sources: `knowledge/notes/all_part01_review.md`, lines 54, 172; `knowledge/notes/denis_all_part02_review.md`, lines 33, 46.
[^charging-telemetry-guide]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 33, 46, 127.
[^schottky]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 103-104, 108-110.
[^offboard-charge]: Source: `knowledge/notes/all_part01_review.md`, lines 47, 56, 251.
[^charge-limit]: Source: `knowledge/notes/all_part01_review.md`, lines 96, 250.
[^storage]: Source: `knowledge/notes/all_part01_review.md`, line 252.
[^thermal-ops]: Source: `knowledge/notes/all_part01_review.md`, lines 169, 265.
[^range-planning]: Sources: `knowledge/notes/all_part01_review.md`, lines 229, 199; `knowledge/notes/denis_all_part02_review.md`, lines 126-127.
[^hill-limit]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 31, 35-38.
[^soc-warning]: Source: `knowledge/notes/all_part01_review.md`, lines 22, 262.
[^maintenance]: Source: `knowledge/notes/all_part01_review.md`, lines 188, 211, 266.
[^pack-build]: Source: `knowledge/notes/all_part01_review.md`, lines 46, 145, 185, 238, 245.
[^security]: Source: `knowledge/notes/denis_all_part02_review.md`, lines 44-45.
[^support]: Source: `knowledge/notes/all_part01_review.md`, lines 17, 150.
