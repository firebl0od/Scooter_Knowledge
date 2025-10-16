# Rita External Battery Integration Field Manual

## Core Capabilities at a Glance

- Works with Xiaomi-style data lines, supports only parallel pack additions, and offers a "permanent BMS emulator" mode for scooters without telemetry, configurable over Bluetooth or a serial tool.[^1]
- Sustains roughly 30 A output and tolerates an anti-spark switch between the adapter and controller without upsetting charge management.[^2]
- Ships with XT30 harnesses sized for the enclosure; the connectors comfortably handle Rita’s intended current range without converting to XT60.[^3]
- Telemetry and charging logic follow the pack with the higher or lower voltage by about 0.5 V, so expect dashboard readings to alternate while Rita targets the battery that needs energy.[^4]

## Setup Checklist

1. Use Denis’ BMS Tool to toggle permanent emulation for scooters lacking a smart data line and to declare 13S packs before powering them through Rita.[^5]
2. Raise the Xiaomi firmware’s over-voltage ceiling to about 51 V for 12S builds (higher for 13S), disable charge prompts if needed, and lean on XiaoFlasher or Denis’ walkthrough.[^6]
3. Downgrade BLE to 072 (M365) or 090 (Pro) so the BMS Tool and Rita app can connect, especially when telemetry flips between packs during charging.[^6][^4]

## External Battery Selection & Packaging

| Pack option | Recommended BMS | Enclosure fit | Notes |
| --- | --- | --- | --- |
| Denis 10S4P Wildman kit | Daly 36 V 25 A common-port | Wildman 2 L hard case | ≈€170 pack + ≈€30 bag + ≈€20 shipping; drop-in range boost without charger mods.[^7] |
| Denis 12S3P Range+Speed | 20 A common-port | Wildman 2 L (tight) | Requires a 50.4 V charger mod or Mean Well alternative; firmware voltage limits must rise before riding.[^8] |
| Custom 12S4P / 13S builds | ≥25 A common-port | Wildman 3 L or custom mounts | ≈€230 for 12S4P; 21700 formats strain enclosure volume, so plan for 3 L bags or printed brackets.[^9] |
| Third-party AliExpress packs | Replace with quality common-port board | Verify dimensions (≤180 × 105 × 83 mm for 2 L) | Many listings exaggerate capacity.
  - confirm dimensions, swap in a reliable BMS, and reinforce wiring before pairing with Rita.[^10] |

- Favor quality cells (Samsung 35E, Sony-based 36 V 15 Ah packs) with 12 AWG leads, and treat XT30 joints as semi-permanent to avoid wear from frequent hot-plugging.[^11]

## Charging Behavior & Field Routines

- Rita shares the stock charge inlet across internal and external packs, automatically prioritizing the lower-voltage side and then balancing both; external-only charging needs a harness once the pack leaves the scooter.[^12]
- Common-port BMS boards are mandatory—separate charge jacks prevent Rita from halting over-voltage through the discharge lead.[^13]
- On mixed 10S/12S stacks, Rita halts the internal pack at 42 V and lets the higher-voltage battery continue toward 50.4–54.6 V; treat 54.6 V chargers as “use at your own risk” because the internal BMS becomes the sole over-voltage protection.[^14]
- Add anti-spark switches between Rita and the controller, not between batteries and Rita, so the adapter retains charge-management authority.[^2][^12]
- Expect Rita to continue topping the external pack after the scooter powers down; rely on charger indicators to confirm completion.[^15]

## Logistics & Fulfillment Snapshot

- Denis sells Rita direct to bypass marketplace fees, ships adapters worldwide, but lithium packs still move only within Europe via ground carriers; Kuwait, Norway, and Turkey buyers must source batteries locally.[^16]
- Typical bundle pricing lands around €250–€280 plus ≈€20 shipping for a Rita+bag+battery kit built with Samsung 35E cells and branded XT30 hardware.[^17]
- Summer 2020 lead times saw batches of 30 Rita boards/15 bags/9 batteries leave in late June, with packs assembled within about three business days by mid-August and regional stock nodes in Poland and London accelerating electronics fulfillment.[^18]
- EU customers reported three-day deliveries from Poland and quoted totals of roughly £290 (UK) to €325 (Finland) for full 12S kits, while DHL Express ferried BMS restocks from China.[^19]

## Troubleshooting & Support Boundaries

- Keep Rita’s permanent emulation active on analog clones and ensure parallel packs match voltage before connecting; bypassed BMS boards or mismatched states of charge can destroy packs.[^5][^20]
- Denis’ support stops at wiring errors: blown fuses from miswired externals or non-common-port BMS experiments are owner-responsibility issues.[^21]
- For 13S experiments, cut Rita’s pink sense wire, lift firmware voltage limits, and ignore legacy controller hacks that splice extra wires across cut traces.[^22]
- When app data disappears, raise the external pack about 0.5 V above the internal pack, close other BLE apps, or retry with older Android builds before assuming a hardware fault.[^4]

## Source Notes

[^1]: Rita only supports parallel battery additions, can emulate the BMS permanently, and is configurable over Bluetooth or serial tools.[^1]
[^2]: Rita tolerates roughly 30 A output and can be power-cycled with an anti-spark switch placed between adapter and controller.[^2]
[^3]: Factory harnesses ship with XT30 male leads on the adapter side because they fit the enclosure and handle the targeted current.[^3]
[^4]: Rita directs charge toward the lower-voltage pack and telemetry flips between batteries whenever voltages sit within about 0.5 V.[^4][^5]
[^5]: The BMS Tool exposes permanent emulation for data-line-less scooters and lets riders declare 13S packs before use.[^6]
[^6]: 12S riders must raise firmware voltage ceilings (≈51 V), disable charge prompts, and downgrade BLE firmware to 072/090 for app access.[^7]
[^7]: Denis’ turnkey 10S4P pack uses Daly 36 V 25 A common-port BMS boards, ships in a Wildman 2 L bag, and costs roughly €170 plus ≈€30 bag and ≈€20 shipping.[^8][^9][^10]
[^8]: The 12S3P Range+Speed kit depends on a 50.4 V charger mod or higher-voltage supply and requires firmware voltage-limit tweaks before riding.[^11][^12]
[^9]: Standalone 12S4P packs cost about €230, 21700 builds stretch enclosure volume, and larger packs push riders toward 3 L bags or custom mounts.[^13][^14][^10]
[^10]: Riders compared AliExpress packs to Denis’ builds, recommended verifying dimensions (~180 × 105 × 83 mm for 2 L bags), and swapping suspect BMS boards before pairing with Rita.[^15][^16][^17]
[^11]: Builders favor quality cells, 12 AWG leads, and semi-permanent XT30 joints to avoid repeated hot-plug wear.[^18][^19]
[^12]: Rita shares the stock charge inlet, prioritizes the lower-voltage pack, and requires an adapter harness for off-scooter charging once a pack is removed.[^20][^21]
[^13]: Separate charge-port batteries are incompatible with Rita’s charge-sharing; common-port BMS boards remain the safest option.[^22][^17]
[^14]: Rita sequences mixed-voltage charging, finishing the internal pack at 42 V before letting 12S/13S packs climb toward 50.4–54.6 V, and Denis warns that the internal BMS becomes the only over-voltage backstop when using higher-voltage chargers.[^23][^24]
[^15]: Rita keeps topping the external pack after the scooter powers down; watch the charger LED for completion.[^25]
[^16]: Denis ships adapters globally via his storefront, but lithium packs remain EU-only due to carrier limits, affecting regions such as Kuwait, Norway, and Turkey.[^26][^27]
[^17]: Complete Rita+bag+battery kits cost roughly €250–€280 plus ≈€20 shipping thanks to premium Samsung 35E cells and branded XT30 hardware.[^28][^9]
[^18]: Production updates cited 30 Rita boards/15 bags/9 batteries shipping in late June, three-day assembly timelines by mid-August, and stock nodes in Poland and London for faster fulfillment.[^29][^30]
[^19]: EU riders reported three-day deliveries from Poland, quoted £290–€325 totals for 12S kits, and saw DHL Express move BMS restocks from China.[^31][^32]
[^20]: Without Rita’s safeguards, paralleling packs bypasses BMS protections and can cause catastrophic failures; Rita demands equal-voltage packs and permanent emulation when data lines are absent.[^33]
[^21]: Denis restricts support when miswired externals blow Rita’s fuses or rely on non-common-port BMS hardware.[^34]
[^22]: Community guidance for 13S builds stresses cutting Rita’s pink wire, raising firmware voltage limits, and avoiding legacy controller hacks.[^35]


## References

[^1]: Source: knowledge/notes/all_part01_review.md†L16-L16
[^2]: Source: knowledge/notes/all_part01_review.md†L20-L20
[^3]: Source: knowledge/notes/all_part01_review.md†L24-L24
[^4]: Source: knowledge/notes/all_part01_review.md†L54-L54
[^5]: Source: knowledge/notes/all_part01_review.md†L219-L219
[^6]: Source: knowledge/notes/all_part01_review.md†L23-L23
[^7]: Source: knowledge/notes/all_part01_review.md†L71-L71
[^8]: Source: knowledge/notes/all_part01_review.md†L49-L49
[^9]: Source: knowledge/notes/all_part01_review.md†L61-L61
[^10]: Source: knowledge/notes/all_part01_review.md†L48-L48
[^11]: Source: knowledge/notes/all_part01_review.md†L65-L65
[^12]: Source: knowledge/notes/all_part01_review.md†L74-L74
[^13]: Source: knowledge/notes/all_part01_review.md†L67-L67
[^14]: Source: knowledge/notes/all_part01_review.md†L68-L68
[^15]: Source: knowledge/notes/all_part01_review.md†L42-L42
[^16]: Source: knowledge/notes/all_part01_review.md†L45-L45
[^17]: Source: knowledge/notes/all_part01_review.md†L179-L179
[^18]: Source: knowledge/notes/all_part01_review.md†L46-L46
[^19]: Source: knowledge/notes/all_part01_review.md†L62-L62
[^20]: Source: knowledge/notes/all_part01_review.md†L52-L52
[^21]: Source: knowledge/notes/all_part01_review.md†L56-L56
[^22]: Source: knowledge/notes/all_part01_review.md†L53-L53
[^23]: Source: knowledge/notes/all_part01_review.md†L63-L63
[^24]: Source: knowledge/notes/all_part01_review.md†L57-L57
[^25]: Source: knowledge/notes/all_part01_review.md†L172-L172
[^26]: Source: knowledge/notes/all_part01_review.md†L28-L28
[^27]: Source: knowledge/notes/all_part01_review.md†L177-L177
[^28]: Source: knowledge/notes/all_part01_review.md†L30-L30
[^29]: Source: knowledge/notes/all_part01_review.md†L29-L29
[^30]: Source: knowledge/notes/all_part01_review.md†L35-L35
[^31]: Source: knowledge/notes/all_part01_review.md†L174-L176
[^32]: Source: knowledge/notes/all_part01_review.md†L32-L32
[^33]: Source: knowledge/notes/all_part01_review.md†L64-L64
[^34]: Source: knowledge/notes/all_part01_review.md†L218-L218
[^35]: Source: knowledge/notes/all_part01_review.md†L217-L217
