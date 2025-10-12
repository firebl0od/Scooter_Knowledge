# Rita Adapter Integration Playbook

A structured checklist for planning, installing, and operating Denis Yurev's Rita adapter on Xiaomi-class scooters.

## Core Capabilities & Limits
- Designed around Xiaomi's CAN/data-line behavior: it only supports parallel auxiliary packs, can masquerade as the scooter BMS via the "permanent emulator" mode, and still accepts serial or BLE configuration when the stock dashboard is missing.[^1]
- Factory harnesses ship with XT30 connectors sized for the deck cavity; XT60 shells do not fit without rework, and the adapter's protections assume XT30 current levels.[^2]
- Power handling peaks around 25–30 A continuous (≈1.5 kW on 13S); Rita v4 now reports up to 15S packs but still enforces that battery-current ceiling, so serious hill-climb torque demands uprated controllers or dual motors.[^3][^4]
- Newer hardware revisions add charger and regen over-voltage protection, yet legacy boards rely entirely on pack BMS behavior. Keep the three-way charge splitter inline when relocating the port; otherwise the adapter cannot sense charger events, and anything above 42 V remains advanced use with conservative ~95 % state-of-charge targets.[^5]

## Pre-Installation Readiness Checklist
| Item | Why it matters | How to verify |
| --- | --- | --- |
| Pack voltages within 0.1 V | Rita blocks cross-flow; large deltas trigger error codes or cutoffs. | Balance both packs before the first parallel connection.[^6][^7]
| Common-port BMS on externals | Rita cannot halt charging over a discharge-only lead; separate charge jacks bypass its protections. | Confirm the auxiliary pack charges and discharges through the same XT30 harness.[^8][^9]
| Firmware voltage limits raised (12S+/13S builds) | Keeps charge thresholds aligned with higher pack voltages. | Set Xiaomi firmware nominal voltage to 51–55 V with XiaoFlasher/XiaoGen before riding.[^10][^11]
| Controller thermal interface refreshed | Dried compound causes rapid thermal cutbacks once current climbs. | Replace Kapton tape with 0.5 mm pads or fresh paste on MOSFETs.[^12]

## Wiring & Harness Layout
- **Parallel Y-cable orientation:** two female battery inputs feed a male controller lead; reversed crimps have already shorted packs inside Wildman bags.[^14]
- **Direct-solder high-current leads:** once you chase higher-phase current tunes, solder motor leads directly to controller stubs instead of stacking adapters to trim resistance and connector heating.[^37]
- **Charge-port routing:** relocating Xiaomi's charge jack outside Rita is acceptable if a three-way splitter remains so Rita senses charger presence and enforces protections.[^15]
- **Anti-spark switches:** place them between Rita and the controller, not between the battery and Rita, to preserve charge handoff logic.[^16]
- **Serial diagnostics:** ground to ground, TX (yellow) needs a pull-up, RX (white) feeds configuration tools like CP2102 adapters; any Rita input can power the board for tuning.[^17]

## Battery Compatibility Map
| Configuration | Supported? | Notes |
| --- | --- | --- |
| Dual 10S packs | ✅ | Baseline Rita use-case; enable permanent BMS emulation when the scooter lacks a smart dash.[^18]
| 10S internal + 12S external | ✅ | Raise firmware voltage limits to 51 V; Rita sequences charging so the internal pack stops at 42 V before the external finishes.[^10][^19]
| Matched 12S packs | ✅ (advanced) | Requires upgraded chargers (50.4 V) and reinforced controllers; expect telemetry to flip between packs when voltages are similar.[^3][^20]
| 13S externals | ⚠️ Experimental | Rita reports up to 15S but still caps battery current near 25 A; mixing 15S externals with 10S internals offers little benefit and risks cutoffs.[^4]
| Mixed series counts (e.g., 10S + 13S) | ❌ | Adapter blocks cross-flow but cannot reconcile voltages; Denis discourages the pairing.[^21]

## Charging & Power Management
- Rita directs charge current to whichever pack sits at lower voltage, then shares once they equalize; expect scooter-dash percentages to stall around 99 % until the external finishes balancing.[^19][^22]
- Shared XT30 leads mean off-scooter charging demands an adapter harness once the pack leaves the Rita loom.[^9]
- Range + Speed kits can charge both packs from a 50.4 V supply, but splitting them across chargers shortens downtime and keeps BMS thermals in check.[^23]
- Higher-voltage builds either modify the OEM charger with a ~14.3 kΩ feedback stack or adopt quality CC/CV supplies (e.g., Mean Well ELG-240-48A) to hit 50.4–54.6 V targets.[^24][^25]
- Without Rita, parallel Y-cables bypass BMS protections; leaving the adapter in circuit keeps dual inputs diode-isolated and enforces current sharing.[^18]

## Firmware & Telemetry Configuration
1. Downgrade BLE to 072/090 if the dashboard runs newer firmware that blocks Rita app pairing.[^26]
2. Flash XiaoFlasher/XiaoGen presets that raise nominal voltage and disable charge prompts for 12S builds.[^10]
3. On scooters without smart dashboards, toggle "permanent emulator" inside M365 BMS Tool so Rita spoofs telemetry.[^1]
4. Remember that telemetry alternates between packs when voltages are close; bump the auxiliary ~0.5 V higher or briefly disconnect to inspect external stats.[^20]

## Operating Guardrails
| Risk | Symptom | Mitigation |
| --- | --- | --- |
| Current spikes >30 A | Rita logs surges, controllers overheat, or ABS trips. | Reinforce controller traces, upgrade MOSFET cooling, or step up to dual-motor conversions for hill climbs.[^3][^27][^28]
| Miswired AWD harness | BMS error 21 or dashboards reboot. | Tie both controller grounds, forward only the white data lead to the slave dash, and keep Rita as the master BMS.[^29]
| Regen/charger over-voltage | Error 39 with −10 °C spoof, or charger LED never goes green. | Validate charger voltage, keep splitter in place, and monitor via Rita app during top-offs.[^15][^30]
| Counterfeit auxiliary packs | Capacity sag, overheated wiring, or exaggerated Ah ratings. | Source from vetted builders (Samsung 35E/22PM cells), inspect weld quality, dispute “13.8 Ah” 10S2P claims, and secure the bag with clamps or cages.[^31][^32][^38]
| Charge splitter removed | Charger LED dark, Rita protections inactive. | Keep the OEM/Rita three-way splitter inline whenever relocating the charge port so the adapter still senses charging mode.[^5][^39] |
| Thermal throttling after upgrade | Repeated cutbacks every few minutes. | Replace dried thermal paste, ensure fans or heat sinks make full contact, and verify tire pressures to reduce load.[^12][^27][^33]

## Troubleshooting Quick Reference
| Code/Symptom | Likely cause | First checks |
| --- | --- | --- |
| Error 14 on dual dashboards | Cross-pack current leakage | Inspect polarity, isolate each controller, confirm Rita blocking behavior before riding.[^34]
| Error 18 after controller swap | Damaged hall harness | Swap in a fresh hall cable before blaming firmware; repeated faults on multiple controllers traced back to the harness.[^40] |
| Error 24 post-upgrade | Supply voltage out of range | Power-cycle the scooter for 10 seconds and verify charge splitter wiring plus pack voltage before deeper diagnosis.[^41] |
| Error 21 (post-upgrade) | XT30/battery data fault | Check connector seating, confirm BMS LED activity, and ensure emulation jumper is seated.[^35]
| External pack invisible in app | Voltage delta too small or BLE conflict | Raise auxiliary voltage by ~0.5 V, close competing Bluetooth apps, or downgrade BLE firmware.[^20][^26]
| Charger LED dark yet voltage rising | Separate charge port bypassing Rita | Re-route through common XT30 harness or accept slow standalone charging with manual supervision.[^8]
| Controller won't flash | DRV200 base missing or ST-Link pins reversed | Run m365_DownG XG Mod intermediate package, restore serial via ScooterHacking Utility, verify pin order.[^11][^36]

## Logistics & Sourcing Notes
- Denis hand-builds kits around Samsung 35E cells, Daly-class 20–25 A BMS boards, and Wildman 2 L hard cases; pricing around €250–€280 reflects low-volume production and quality connectors.[^37]
- Lithium shipping remains EU-focused: Rita ships globally, but complete battery kits ride ground carriers with ~10-day delivery inside Europe and limited service to regions like Norway or Kuwait.[^38]
- Secure the Wildman bag upright with heavy pipe clamps or custom cages to deter theft; avoid filling bags with expanding foam, which complicates service.[^32]
- Repurpose spare Xiaomi packs as externals with their own BMS and dedicated chargers instead of using them as improvised power sources for other batteries.[^42]

---

[^1]: `knowledge/notes/all_part01_review.md`, lines 16-18.
[^2]: `knowledge/notes/all_part01_review.md`, lines 45-48, 82-84.
[^3]: `knowledge/notes/all_part01_review.md`, lines 20-21, 123-124.
[^4]: `knowledge/notes/denis_all_part02_review.md`, lines 22-23, 153-154.
[^5]: `knowledge/notes/denis_all_part02_review.md`, lines 29-30.
[^6]: `knowledge/notes/all_part01_review.md`, lines 118-124.
[^7]: `knowledge/notes/denis_all_part02_review.md`, lines 19-23, 31.
[^8]: `knowledge/notes/denis_all_part02_review.md`, lines 23, 33.
[^9]: `knowledge/notes/all_part01_review.md`, lines 47-57.
[^10]: `knowledge/notes/all_part01_review.md`, lines 70-75, 93-101.
[^11]: `knowledge/notes/denis_all_part02_review.md`, lines 27, 50-51, 155-168.
[^12]: `knowledge/notes/denis_all_part02_review.md`, lines 12-13, 32.
[^14]: `knowledge/notes/denis_all_part02_review.md`, lines 19-20.
[^15]: `knowledge/notes/denis_all_part02_review.md`, lines 30, 29-30.
[^16]: `knowledge/notes/all_part01_review.md`, lines 20, 55.
[^17]: `knowledge/notes/all_part01_review.md`, lines 112-114.
[^18]: `knowledge/notes/all_part01_review.md`, lines 16-18, 64.
[^19]: `knowledge/notes/all_part01_review.md`, lines 54-63.
[^20]: `knowledge/notes/all_part01_review.md`, lines 20-25; `knowledge/notes/denis_all_part02_review.md`, lines 33, 46.
[^21]: `knowledge/notes/all_part01_review.md`, lines 63-65, 118-124.
[^22]: `knowledge/notes/denis_all_part02_review.md`, lines 33, 46.
[^23]: `knowledge/notes/denis_all_part02_review.md`, lines 46, 23.
[^24]: `knowledge/notes/all_part01_review.md`, lines 57-58, 95-98.
[^25]: `knowledge/notes/all_part01_review.md`, lines 57-58, 74-75.
[^26]: `knowledge/notes/all_part01_review.md`, lines 70-72.
[^27]: `knowledge/notes/denis_all_part02_review.md`, lines 31-32, 191-193.
[^28]: `knowledge/notes/denis_all_part02_review.md`, lines 35-38.
[^29]: `knowledge/notes/denis_all_part02_review.md`, lines 28, 197.
[^30]: `knowledge/notes/denis_all_part02_review.md`, lines 29-33, 200.
[^31]: `knowledge/notes/all_part01_review.md`, lines 41-48, 60-68; `knowledge/notes/denis_all_part02_review.md`, lines 19-23.
[^32]: `knowledge/notes/denis_all_part02_review.md`, lines 41-45.
[^33]: `knowledge/notes/denis_all_part02_review.md`, lines 56-57, 169-170.
[^34]: `knowledge/notes/denis_all_part02_review.md`, lines 25-27.
[^35]: `knowledge/notes/denis_all_part02_review.md`, lines 149-151, 155.
[^36]: `knowledge/notes/denis_all_part02_review.md`, lines 161-168.
[^37]: `knowledge/notes/denis_all_part02_review.md`, lines 10-13.
[^38]: `knowledge/notes/denis_all_part02_review.md`, lines 19-23.
[^39]: `knowledge/notes/denis_all_part02_review.md`, lines 29-33.
[^40]: `knowledge/notes/denis_all_part02_review.md`, lines 151-152.
[^41]: `knowledge/notes/denis_all_part02_review.md`, lines 152-153.
[^42]: `knowledge/notes/denis_all_part02_review.md`, lines 45-46.
