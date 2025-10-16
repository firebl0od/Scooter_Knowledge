# Power Distribution and Wiring Hygiene

## Cable Management

- Long 16 AWG leads paired with XT30 connectors caused ~0.5 V per-cell drops at 40 A on a 12 S 7 P pack; shortening runs, upgrading to XT60/XT90, and using 10–12 AWG wiring markedly improves voltage sag.[^long_leads]
- Routing high-current cabling on one deck side and signal/brake harnesses on the other reduces EMI in tight Vsett installations, especially once connectors are upsized.[^emi_routing]

## Signal Filtering & Parallel Pack Discipline

- For throttle-signal filtering, the crew scavenges ~100 nF ceramic capacitors from dead electronics instead of grafting oversized drone caps; always discharge and meter salvaged parts before bridging signal-to-ground so you know the exact capacitance you are adding.[^ceramic_scavenge]
- When paralleling 16 S packs, tie all grounds together, match series counts and capacities, pre-balance voltages, and watch for cross-charging so the smaller pack is not over-stressed despite individual BMS protection.[^parallel_rules]
- Rita-style Y cables should present two female battery legs feeding a single male controller lead, with both packs matched in voltage before connection; poorly soldered joints in moving bags have already shorted externals and scarred decks.[^denis-y-cable]

## High-Current Harness Upgrades

- Once current climbs past stock limits, treat connector upgrades as mandatory: swap Xiaomi motor plugs for 4 mm bullets and replace long XT30 harnesses with AWG12 + XT60 leads to keep voltage sag in check on dual-motor or external-pack builds.[^connector-upgrade]
- External battery riders are graduating to 4 mm gold bullets, AS120 mains, and even direct-soldered phase leads after discovering stock 2 mm conductors and MR60 plugs overheat above ~80–100 A; backpack packs stay cool once the heavier hardware is in place.[^1]
- For 90 A packs, default to AWG10 main leads (or dual AWG12 runs) and consider 3–3.5 mm solid-core copper between pack negatives and BMS plates for roughly 40 % more ampacity.
  - as long as the runs stay short.[^2]
- 12 AWG phase leads remain comfortable around 100 A continuous, yet light riders have logged 150 A bursts on 13 S hubs with post-ride temps near 45 °C.
  - plan short duty cycles or forced cooling if you intend to exceed the published ampacity.[^3]
- Community Amass connector testing now pegs 10 AWG as the practical minimum for 60 A continuous, with AS120 shells running cooler than AS150 in scooter-duty cycles thanks to their contact geometry.
  - size wiring and connectors accordingly before chasing 70 A+ battery limits.[^4]
- Heavy 90–150 A phase runs are shifting toward XT150 bullets or AS150U anti-spark leads.
  - roughly 0.20 mΩ resistance and spare signal pins
  - so controllers can feed trackers or smart BMS links without extra connectors while keeping voltage drop minimal.[^5]
- Treat solder as mechanical filler, not the conductor: twist or fold AWG12 leads to double their contact area before wetting bullets, because even silver-bearing solder conducts two to five times worse than copper.[^6]
- Builders graduating dual VESC setups beyond 150 A phase are standardising on Amass AS150U anti-spark pairs with 8 AWG tails and XT150/AS150 mains once burst logs show 500 A phase.
  - XT90s are now treated as temporary jumpers to avoid the 200–300 A desoldering failures others recorded.[^7]
- Splitting 60–70 A batteries between dual controllers still calls for AWG10 feeders, XT90 mains, and MR60 phase connectors; heat both sides of each joint for solid solder wicks and treat Daly BMS “50 A” ratings as optimistic short-burst figures.[^dual-feed]

## Accessory Loads (Denis Part 02)

- Budget roughly 1–1.5 A for 12 V horns and fuse their supply; many riders pair the loud horn with a polite bell for pedestrian zones.[^denis-horn]
- Hidden trackers need their own low-dropout regulator (e.g., AMS1117-3.3) tied directly to the main battery because Xiaomi controllers don’t expose a standby 5 V rail.[^denis-tracker-ldo]

## Charging Interfaces

- Feeding 13 S builds through Xiaomi’s RCA Type X charge jack overheats the OEM wiring above ~3 A; higher-power projects either request custom connectors from charger vendors or convert to GX12-class ports.[^charge-port-13s]

## Service Safety

- After high-current rides, expect phase connectors to “weld” together—kill pack power, discharge controller capacitors, and be ready for sparks on reconnection to protect BLE boards and ESCs.[^phase-safety]

[^long_leads]: Source: knowledge/notes/input_part000_review.md, line 84.
[^emi_routing]: Source: knowledge/notes/input_part000_review.md, line 85.
[^ceramic_scavenge]: Source: knowledge/notes/input_part000_review.md, line 126.
[^parallel_rules]: Source: knowledge/notes/input_part000_review.md, line 127.


## References

[^1]: Source: knowledge/notes/input_part000_review.md†L325-L325
[^2]: Source: knowledge/notes/input_part000_review.md†L373-L373
[^3]: Source: knowledge/notes/input_part000_review.md†L468-L472
[^4]: Source: knowledge/notes/input_part000_review.md†L472-L474
[^5]: Source: knowledge/notes/input_part000_review.md†L546-L548
[^6]: Source: knowledge/notes/input_part000_review.md†L548-L549
[^7]: Source: knowledge/notes/input_part000_review.md†L618-L627
[^denis-y-cable]: Source: knowledge/notes/denis_all_part02_review.md†L769-L769
[^denis-horn]: Source: knowledge/notes/denis_all_part02_review.md†L645-L645
[^denis-tracker-ldo]: Source: knowledge/notes/denis_all_part02_review.md†L934-L934
[^connector-upgrade]: Source: knowledge/notes/denis_all_part02_review.md†L1018-L1020
[^dual-feed]: Source: knowledge/notes/denis_all_part02_review.md†L1073-L1073
[^charge-port-13s]: Source: knowledge/notes/denis_all_part02_review.md†L1063-L1063
[^phase-safety]: Source: knowledge/notes/denis_all_part02_review.md†L1091-L1091
