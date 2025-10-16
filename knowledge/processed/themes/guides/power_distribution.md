# Power Distribution and Wiring Hygiene

## Cable Management

- Long 16 AWG leads paired with XT30 connectors caused ~0.5 V per-cell drops at 40 A on a 12 S 7 P pack; shortening runs, upgrading to XT60/XT90, and using 10–12 AWG wiring markedly improves voltage sag.[^long_leads]
- Routing high-current cabling on one deck side and signal/brake harnesses on the other reduces EMI in tight Vsett installations, especially once connectors are upsized.[^emi_routing]

## Signal Filtering & Parallel Pack Discipline

- For throttle-signal filtering, the crew scavenges ~100 nF ceramic capacitors from dead electronics instead of grafting oversized drone caps; always discharge and meter salvaged parts before bridging signal-to-ground so you know the exact capacitance you are adding.[^ceramic_scavenge]
- When paralleling 16 S packs, tie all grounds together, match series counts and capacities, pre-balance voltages, and watch for cross-charging so the smaller pack is not over-stressed despite individual BMS protection.[^parallel_rules]

## High-Current Harness Upgrades

- External battery riders are graduating to 4 mm gold bullets, AS120 mains, and even direct-soldered phase leads after discovering stock 2 mm conductors and MR60 plugs overheat above ~80–100 A; backpack packs stay cool once the heavier hardware is in place.[^1]
- XT90S anti-sparks remain handy for light builds, but repeated hot-plugs cook their in-line resistors; high-power crews step up to AS150 bullets or QS8/QS10 connectors that comfortably ride out 300–600 A bursts once the crimps and strain relief are done properly.[^antispark_tradeoff]
- For 90 A packs, default to AWG10 main leads (or dual AWG12 runs) and consider 3–3.5 mm solid-core copper between pack negatives and BMS plates for roughly 40 % more ampacity.
  - as long as the runs stay short.[^2]
- 12 AWG phase leads remain comfortable around 100 A continuous, yet light riders have logged 150 A bursts on 13 S hubs with post-ride temps near 45 °C.
  - plan short duty cycles or forced cooling if you intend to exceed the published ampacity.[^3]
- Community Amass connector testing now pegs 10 AWG as the practical minimum for 60 A continuous, with AS120 shells running cooler than AS150 in scooter-duty cycles thanks to their contact geometry.
  - size wiring and connectors accordingly before chasing 70 A+ battery limits.[^4]
- Heavy 90–150 A phase runs are shifting toward XT150 bullets or AS150U anti-spark leads.
  - roughly 0.20 mΩ resistance and spare signal pins
  - so controllers can feed trackers or smart BMS links without extra connectors while keeping voltage drop minimal.[^5]
- Paolo has already incinerated XT90S loop keys when feeding >2,000 µF cap banks at 16 S+, pushing builders toward QS8/AS150 connectors paired with beefier pre-charge resistors before heavy current spikes melt solder joints.[^xt90_failure]
- Treat single XT90S plugs as roughly 50 A continuous (~65 A burst) ceiling; 120–180 A batteries demand dual XT60s, XT150/AS150 bullets, or QS8 pairs plus 6–8 AWG leads to keep contact temperatures in check.[^ip001-xt90-headroom]
- JK smart BMS antispark stages make XT150 hot-plugging viable, while AS150 split shells simplify dual-controller routing inside cramped VSETT decks.[^ip001-xt150-routing]
- Higo L1019 retrofit looms bundle 4 mm² (≈11 AWG) phases with halls and a temp lead in one jacket that still fits VSETT axles; map the color swap before landing XT150 bullets and keep the plug on 50 mm-class hubs where it stays cool.[^ip001-l1019]
- Avoid dropping L1019 connectors into 60–70 mm motors without reworking the solder—builders are desoldering the factory “blob” and upsizing leads before higher-current installs.[^ip001-l1019-limit]
- Treat solder as mechanical filler, not the conductor: twist or fold AWG12 leads to double their contact area before wetting bullets, because even silver-bearing solder conducts two to five times worse than copper.[^6]
- A melted MT60 phase plug that shorted a Kelly controller at ~200 A convinced the crew to retire drone-class connectors above 72 V; step up to XT150/AS150 bullets or lugs once battery demand enters the 150–200 A bracket.[^ip001-mt60-failure]
- Builders graduating dual VESC setups beyond 150 A phase are standardising on Amass AS150U anti-spark pairs with 8 AWG tails and XT150/AS150 mains once burst logs show 500 A phase.
  - XT90s are now treated as temporary jumpers to avoid the 200–300 A desoldering failures others recorded.[^7]
- Keep 190 A-class scooters on dual 7 AWG battery leads (or single 6 AWG) and remember that wire gauge requirements follow current draw, not pack series count; undersized looms turn shrink wrap brittle around 135–145 °C in weeks.[^ip001-awg]

## Lighting & Instrumentation Loads

- Compact 25 W/3 500 lm headlights and parallel-wired high/low beams fit scooter cockpits but demand honest current budgets; the touted 3 A step-downs need heatsinking, each Nucular controller only supplies 12 V/3 A (≈6 A dual), and many riders prefer lamps with integrated buck converters to avoid voltage drop across long runs.[^ip001-lighting]
- Popular mini voltmeters cap at 35 V and expect a 12 V feed, forcing 72–100 V builds to add dedicated step-downs or repurpose throttle displays since control rails only provide ~3.3 V.[^ip001-voltmeter]

[^long_leads]: Source: knowledge/notes/input_part000_review.md, line 84.
[^emi_routing]: Source: knowledge/notes/input_part000_review.md, line 85.
[^ceramic_scavenge]: Source: knowledge/notes/input_part000_review.md, line 126.
[^parallel_rules]: Source: knowledge/notes/input_part000_review.md, line 127.
[^antispark_tradeoff]: Source: knowledge/notes/input_part003_review.md†L511-L515


## References

[^1]: Source: knowledge/notes/input_part000_review.md†L325-L325
[^2]: Source: knowledge/notes/input_part000_review.md†L373-L373
[^3]: Source: knowledge/notes/input_part000_review.md†L468-L472
[^4]: Source: knowledge/notes/input_part000_review.md†L472-L474
[^5]: Source: knowledge/notes/input_part000_review.md†L546-L548
[^xt90_failure]: Source: knowledge/notes/input_part001_review.md†L595-L596
[^ip001-l1019]: Source: knowledge/notes/input_part001_review.md†L653-L654
[^ip001-l1019-limit]: Source: knowledge/notes/input_part001_review.md†L653-L655
[^6]: Source: knowledge/notes/input_part000_review.md†L548-L549
[^7]: Source: knowledge/notes/input_part000_review.md†L618-L627
[^ip001-xt90-headroom]: Source: data/vesc_help_group/text_slices/input_part001.txt†L20085-L20177
[^ip001-xt150-routing]: Source: data/vesc_help_group/text_slices/input_part001.txt†L20131-L20177
[^ip001-awg]: Source: data/vesc_help_group/text_slices/input_part001.txt†L18170-L18340
[^ip001-mt60-failure]: Source: data/vesc_help_group/text_slices/input_part001.txt†L17850-L17910
[^ip001-lighting]: Source: data/vesc_help_group/text_slices/input_part001.txt†L24157-L24216
[^ip001-voltmeter]: Source: data/vesc_help_group/text_slices/input_part001.txt†L24411-L24421
