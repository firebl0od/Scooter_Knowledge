# Rita Adapter Integration Playbook

A structured checklist for planning, installing, and operating Denis Yurev's Rita adapter on Xiaomi-class scooters.

## Core Capabilities & Limits

- Designed around Xiaomi's CAN/data-line behavior: it only supports parallel auxiliary packs, can masquerade as the scooter BMS via the "permanent emulator" mode, and still accepts serial or BLE configuration when the stock dashboard is missing.[^1]
- Factory harnesses historically shipped with XT30 connectors sized for the deck cavity, but current batches include XT60 leads plus an XT30 adapter.
  - plan harness routing accordingly and keep anti-spark hardware in-line so the adapter’s protections still trip correctly.[^2][^17]
- Power handling peaks around 25–30 A continuous (≈1.5 kW on 13S); Rita v4 now reports up to 15S packs but still enforces that battery-current ceiling, so serious hill-climb torque demands uprated controllers or dual motors.[^3][^4]
- Newer hardware revisions add charger and regen over-voltage protection, yet legacy boards rely entirely on pack BMS behavior. Keep the three-way charge splitter inline when relocating the port; otherwise the adapter cannot sense charger events, and anything above 42 V remains advanced use with conservative ~95 % state-of-charge targets.[^5]
- Expect a floating +5 V on whichever battery input is idle; Rita energises the sense rail even with one pack disconnected, which Denis calls normal during bench diagnostics.[^5a]

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
- **Gray surge jumper discipline:** Leave the gray loop near Rita’s status LED intact for 10–12 S builds and cut it only when stepping up to 13–15 S packs so the inrush limiter and current-sense hardware stay calibrated.[^surge_loop]
- **Power-down before rewiring:** Never reconnect trace-cut harnesses or jumpers while the wheel is spinning.
  - tests have torched the U4 regulator instantly, so kill power before touching Rita leads.[^rewire]
- **Serial diagnostics:** ground to ground, TX (yellow) needs a pull-up, RX (white) feeds configuration tools like CP2102 adapters; any Rita input can power the board for tuning.[^17]

## Battery Compatibility Map

| Configuration | Supported? | Notes |
| --- | --- | --- |
| Dual 10S packs | ✅ | Baseline Rita use-case; enable permanent BMS emulation when the scooter lacks a smart dash.[^18]
| 10S internal + 12S external | ✅ | Raise firmware voltage limits to 51 V; Rita sequences charging so the internal pack stops at 42 V before the external finishes.[^10][^19]
| Matched 12S packs | ✅ (advanced) | Requires upgraded chargers (50.4 V) and reinforced controllers; expect telemetry to flip between packs when voltages are similar.[^3][^20]
| 13S externals | ⚠️ Experimental | Rita reports up to 15S but still caps battery current near 25 A; mixing 15S externals with 10S internals offers little benefit and risks cutoffs.[^4]
| Mixed series counts (e.g., 10S + 13S) | ❌ | Adapter blocks cross-flow but cannot reconcile voltages; Denis discourages the pairing.[^21]
| Tool batteries (e.g., Makita BL1850B) | ❌ | Rita waits for ≈36 V before blending, so five-cell tool packs barely contribute.
  - sell them and invest in scooter-class 10–12 S packs with Daly common-port BMS boards instead.[^43]

## Charging & Power Management

- Rita directs charge current to whichever pack sits at lower voltage, then shares once they equalize; expect scooter-dash percentages to stall around 99 % until the external finishes balancing.[^19][^22]
- Denis caps 12 S externals around 49.2 V (~4.1 V/cell) so regen retains headroom—raising the ceiling gains roughly 1 km of range while risking e-brake loss on long descents.[^49v-headroom]
- Shared XT30 leads mean off-scooter charging demands an adapter harness once the pack leaves the Rita loom.[^9]
- Range + Speed kits can charge both packs from a 50.4 V supply, but splitting them across chargers shortens downtime and keeps BMS thermals in check.[^23]
- Higher-voltage builds either modify the OEM charger with a ~14.3 kΩ feedback stack or adopt quality CC/CV supplies (e.g., Mean Well ELG-240-48A) to hit 50.4–54.6 V targets.[^24][^25]
- Without Rita, parallel Y-cables bypass BMS protections; leaving the adapter in circuit keeps dual inputs diode-isolated and enforces current sharing.[^18]
- Expect the internal pack to rest around 41 V at 100 %.
  - Rita deliberately undercharges a few tenths to preserve regen headroom, so chase error 39 by reducing current or staggering pack voltages rather than forcing a full top-off.[^undercharge]
- External-pack telemetry disappears while a charger is connected—Rita hides the auxiliary voltage on Gen 1–Gen 5 boards, so blank readings during top-offs are normal.[^charge-ui]
- Analog clone scooters still benefit: Rita behaves like paired smart diodes that prioritise whichever pack sits higher in voltage, but riders lose the fine-grained cutoff control provided by Xiaomi dashboards and must manage pack voltage manually.[^analog-clone]
- Happy BMS coulomb counters peg at 0 % once roughly 32 Ah flows through a 35 A external; expect about 10 % energy remaining and plan range manually even though Rita keeps current inside spec.[^happy-35a-rita]

## Firmware & Telemetry Configuration

1. Downgrade BLE to 072/090 if the dashboard runs newer firmware that blocks Rita app pairing.[^26]
2. Flash XiaoFlasher/XiaoGen presets that raise nominal voltage and disable charge prompts for 12S builds.[^10]
3. On scooters without smart dashboards, toggle "permanent emulator" inside M365 BMS Tool so Rita spoofs telemetry.[^1]
4. Remember that telemetry alternates between packs when voltages are close; bump the auxiliary ~0.5 V higher or briefly disconnect to inspect external stats.[^20]

- When Android builds lag behind, connect a USB-UART adapter (ground plus yellow/white leads with a pull-up) and configure Rita from a PC; Denis even sells a ready-made cable for hassle-free bench tuning.[^1]
- Avoid XiaoFlasher’s 13 S emulator for daily riding—it introduces throttle lag, whereas Rita’s emulation keeps instant response once large internal packs share the dash.[^xiaoflasher_lag]

## Operating Guardrails

| Risk | Symptom | Mitigation |
| --- | --- | --- |
| External pack not configured | Rita throws error 39 and may beep after long pulls; charging pauses near 40 °C pack temperature. | Set series count/capacity in the app before paralleling packs and let them cool to ≈35 °C before resuming charge current.[^2] |
| Error 39 after firmware tunes or swapping between 36 V and 48 V externals | Adapter overheats or ignores the new pack once voltages change, especially when current logs show >30 A pulls. | Record live amps with m365Tools, dial battery current back under 30 A, and reconfigure Rita’s series/capacity settings every time you connect a pack with a different voltage profile.[^3][^4] |
| Internal pack refuses to share charge | Rita fills the external while the OEM pack stays low; Happy app may show missing temperature data. | Disconnect Rita, verify both OEM temperature sensors, and replace the failed probe before blaming the adapter.[^5] |
| Current spikes >30 A | Rita logs surges, controllers overheat, or ABS trips. | Reinforce controller traces, upgrade MOSFET cooling, or step up to dual-motor conversions for hill climbs.[^3][^27][^28]
| Miswired AWD harness | BMS error 21 or dashboards reboot. | Tie both controller grounds, forward only the white data lead to the slave dash, and keep Rita as the master BMS.[^29]
| Regen/charger over-voltage | Error 39 with −10 °C spoof, or charger LED never goes green. | Validate charger voltage, keep splitter in place, and monitor via Rita app during top-offs.[^15][^30]
| Counterfeit auxiliary packs | Capacity sag, overheated wiring, or exaggerated Ah ratings. | Source from vetted builders (Samsung 35E/22PM cells), inspect weld quality, dispute “13.8 Ah” 10S2P claims, and secure the bag with clamps or cages.[^31][^32][^38]
| Charge splitter removed | Charger LED dark, Rita protections inactive. | Keep the OEM/Rita three-way splitter inline whenever relocating the charge port so the adapter still senses charging mode.[^5][^39] |
| Thermal throttling after upgrade | Repeated cutbacks every few minutes. | Replace dried thermal paste, ensure fans or heat sinks make full contact, and verify tire pressures to reduce load.[^12][^27][^33]
| Dual-motor conversion plans | Each motor sees ~15 A even with dual Ritas, limiting gains. | Budget for stronger single rear motors or uprated controllers before chasing AWD builds around Rita’s current ceiling.[^6] |
| 60 V experimentation | Adapter alarms or noisy motors during bench tests. | Stage launches gradually, confirm BLE firmware, and monitor Rita temperature warnings before leaning on 60 V packs.[^rita60v]
| Emulator shows 0 % with voltage remaining | Emulator “empty” warnings appear around 3.4 V per cell even with lower cutoffs configured. | Keep manual voltage checks or a conservative range buffer when riding on BMS emulation instead of a Xiaomi board.[^emulator-34v-rita] |

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
- Daly smart-BMS charge negatives exit on the yellow lead—route it between the pack and both Rita/charger feeds or the board sits idle and repeats the shorts that fried earlier builds.[^daly]

---

## Source Notes

[^1]: [^7]
[^2]: [^8][^9]
[^3]: [^10][^11]
[^4]: [^12][^13]
[^5]: [^14]
[^5a]: [^15]
[^6]: [^16]
[^7]: [^17][^18]
[^8]: [^19][^20]
[^9]: [^21]
[^10]: [^22][^23]
[^11]: [^24][^25][^26]
[^12]: [^27][^28]
[^14]: [^29]
[^15]: [^30][^14]
[^16]: [^31][^32]
[^rewire]: [^33]
[^17]: [^34][^1]
[^18]: [^7][^35]
[^19]: [^36]
[^20]: [^37][^20][^38]
[^analog-clone]: [^39]
[^21]: [^40][^16]
[^22]: [^20][^38]
[^23]: [^38][^19]
[^24]: [^41][^42]
[^25]: [^41][^43]
[^26]: [^44]
[^49v-headroom]: Rita charge discussions noting 12 S externals plateau around 49.2 V (~4.1 V/cell) to preserve regen headroom.[^45]
[^27]: [^46][^47]
[^28]: [^48]
[^29]: [^49][^50]
[^30]: [^51][^52]
[^31]: [^53][^54][^17]
[^32]: [^55]
[^33]: [^56][^57]
[^34]: [^58]
[^35]: [^59][^60]
[^36]: [^61]
[^37]: [^62]
[^38]: [^17]
[^39]: [^51]
[^40]: [^63]
[^41]: [^64]
[^42]: [^65]
[^43]: [^66]
[^daly]: [^67]
[^xiaoflasher_lag]: XiaoFlasher’s 13 S BMS emulator adds noticeable throttle lag, so Denis’ crew leans on Rita’s emulation to keep large internal packs responsive with the stock dashboard.[^68]
[^surge_loop]: Rita Gen 4’s gray loop beside the LED acts as a surge jumper.
  - leave it intact for 10–12 S packs and cut it only when moving to 13–15 S layouts so the inrush limiter and current monitor stay calibrated.[^69]
[^undercharge]: New hardware revisions intentionally rest the internal pack near 41 V so regen headroom remains; if error 39 hits during >25 A pulls, drop current or stagger pack voltages before the next ride.[^70][^71]
[^rita60v]: Riders dabbling with 60 V packs were told to stage launches, confirm BLE firmware, and watch Rita’s temperature alarms before leaning on the higher voltage.
  - adapter limits still apply even when the scooter spins freely.[^72]
[^charge-ui]: [^73]
[^happy-35a-rita]: [^74]
[^emulator-34v-rita]: [^75]


## References

[^1]: Source: knowledge/notes/denis_all_part02_review.md†L473-L474
[^2]: Source: knowledge/notes/denis_all_part02_review.md†L315-L316
[^3]: Source: knowledge/notes/denis_all_part02_review.md†L55-L59
[^4]: Source: knowledge/notes/denis_all_part02_review.md†L365-L368
[^5]: Source: knowledge/notes/denis_all_part02_review.md†L505-L505
[^6]: Source: knowledge/notes/denis_all_part02_review.md†L385-L387
[^7]: Source: knowledge/notes/all_part01_review.md†L16-L18
[^8]: Source: knowledge/notes/all_part01_review.md†L45-L48
[^9]: Source: knowledge/notes/all_part01_review.md†L82-L84
[^10]: Source: knowledge/notes/all_part01_review.md†L20-L21
[^11]: Source: knowledge/notes/all_part01_review.md†L123-L124
[^12]: Source: knowledge/notes/denis_all_part02_review.md†L22-L23
[^13]: Source: knowledge/notes/denis_all_part02_review.md†L153-L154
[^14]: Source: knowledge/notes/denis_all_part02_review.md†L29-L30
[^15]: Source: knowledge/notes/all_part01_review.md†L23-L24
[^16]: Source: knowledge/notes/all_part01_review.md†L118-L124
[^17]: Source: knowledge/notes/denis_all_part02_review.md†L19-L23
[^18]: Source: knowledge/notes/denis_all_part02_review.md†L31
[^19]: Source: knowledge/notes/denis_all_part02_review.md†L23
[^20]: Source: knowledge/notes/denis_all_part02_review.md†L33
[^21]: Source: knowledge/notes/all_part01_review.md†L47-L57
[^22]: Source: knowledge/notes/all_part01_review.md†L70-L75
[^23]: Source: knowledge/notes/all_part01_review.md†L93-L101
[^24]: Source: knowledge/notes/denis_all_part02_review.md†L27
[^25]: Source: knowledge/notes/denis_all_part02_review.md†L50-L51
[^26]: Source: knowledge/notes/denis_all_part02_review.md†L155-L168
[^27]: Source: knowledge/notes/denis_all_part02_review.md†L12-L13
[^28]: Source: knowledge/notes/denis_all_part02_review.md†L32
[^29]: Source: knowledge/notes/denis_all_part02_review.md†L19-L20
[^30]: Source: knowledge/notes/denis_all_part02_review.md†L30
[^31]: Source: knowledge/notes/all_part01_review.md†L20
[^32]: Source: knowledge/notes/all_part01_review.md†L55
[^33]: Source: knowledge/notes/denis_all_part02_review.md†L6979-L6986
[^34]: Source: knowledge/notes/all_part01_review.md†L112-L114
[^35]: Source: knowledge/notes/all_part01_review.md†L64
[^36]: Source: knowledge/notes/all_part01_review.md†L54-L63
[^37]: Source: knowledge/notes/all_part01_review.md†L20-L25
[^38]: Source: knowledge/notes/denis_all_part02_review.md†L46
[^39]: Source: knowledge/notes/all_part01_review.md†L19-L25
[^40]: Source: knowledge/notes/all_part01_review.md†L63-L65
[^41]: Source: knowledge/notes/all_part01_review.md†L57-L58
[^42]: Source: knowledge/notes/all_part01_review.md†L95-L98
[^43]: Source: knowledge/notes/all_part01_review.md†L74-L75
[^44]: Source: knowledge/notes/all_part01_review.md†L70-L72
[^45]: Source: knowledge/notes/denis_all_part02_review.md†L503-L504
[^46]: Source: knowledge/notes/denis_all_part02_review.md†L31-L32
[^47]: Source: knowledge/notes/denis_all_part02_review.md†L191-L193
[^48]: Source: knowledge/notes/denis_all_part02_review.md†L35-L38
[^49]: Source: knowledge/notes/denis_all_part02_review.md†L28
[^50]: Source: knowledge/notes/denis_all_part02_review.md†L197
[^51]: Source: knowledge/notes/denis_all_part02_review.md†L29-L33
[^52]: Source: knowledge/notes/denis_all_part02_review.md†L200
[^53]: Source: knowledge/notes/all_part01_review.md†L41-L48
[^54]: Source: knowledge/notes/all_part01_review.md†L60-L68
[^55]: Source: knowledge/notes/denis_all_part02_review.md†L41-L45
[^56]: Source: knowledge/notes/denis_all_part02_review.md†L56-L57
[^57]: Source: knowledge/notes/denis_all_part02_review.md†L169-L170
[^58]: Source: knowledge/notes/denis_all_part02_review.md†L25-L27
[^59]: Source: knowledge/notes/denis_all_part02_review.md†L149-L151
[^60]: Source: knowledge/notes/denis_all_part02_review.md†L155
[^61]: Source: knowledge/notes/denis_all_part02_review.md†L161-L168
[^62]: Source: knowledge/notes/denis_all_part02_review.md†L10-L13
[^63]: Source: knowledge/notes/denis_all_part02_review.md†L151-L152
[^64]: Source: knowledge/notes/denis_all_part02_review.md†L152-L153
[^65]: Source: knowledge/notes/denis_all_part02_review.md†L45-L46
[^66]: Source: knowledge/notes/denis_all_part02_review.md†L235-L235
[^67]: Source: knowledge/notes/denis_all_part02_review.md†L9453-L9467
[^68]: Source: knowledge/notes/denis_all_part02_review.md†L2467-L2470
[^69]: Source: knowledge/notes/denis_all_part02_review.md†L7567-L7589
[^70]: Source: knowledge/notes/denis_all_part02_review.md†L7744-L7751
[^71]: Source: knowledge/notes/denis_all_part02_review.md†L8327-L8338
[^72]: Source: knowledge/notes/denis_all_part02_review.md†L9495-L9520
[^73]: Source: knowledge/notes/denis_all_part02_review.md†L408-L409
[^74]: Source: knowledge/notes/denis_all_part02_review.md†L401-L401
[^75]: Source: knowledge/notes/denis_all_part02_review.md†L402-L402
