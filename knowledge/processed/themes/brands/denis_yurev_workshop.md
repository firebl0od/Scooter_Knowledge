# Denis Yurev Workshop (Rita Ecosystem)

## Overview

Denis Yurev's workshop produces the Rita smart battery adapter and related products for Xiaomi-platform scooters, enabling parallel external packs while retaining stock dashboards and BMS emulation. This comprehensive brand dossier covers the Rita adapter ecosystem, repair BMS products, external battery packs, firmware tools, and integration best practices. Understanding Rita's capabilities and limitations is essential for safe Xiaomi platform upgrades.

## What You'll Learn

- Rita adapter capabilities and current limits (~25-30A)
- BMS emulation modes and data-line requirements
- External pack selection and compatibility
- Charge management and voltage balancing
- Firmware tools (XiaoGen, XiaoFlasher, M365 BMS Tool)
- Common integration issues and solutions
- AWD conversion considerations
- When Rita makes sense vs. controller replacement

## Quick Facts

| Topic | Details |
| --- | --- |
| Flagship products | Rita smart battery adapter, common-port external packs, repair BMS line |
| Target platforms | Xiaomi M365/Pro families and compatible clones |
| Sales channel | Direct via m365.embedden.com with self-published guides and tooling docs |
| Typical customers | Riders extending range or voltage while retaining Xiaomi dashboards |

## Product Portfolio

### Rita Smart Adapter

- Designed for Xiaomi-style data-line traffic and parallel battery expansions; supports Bluetooth configuration or serial tooling when the stock dashboard is absent.[^rita-capabilities]
- Offers a “permanent BMS emulator” mode for scooters that lack data lines yet still orchestrates current like paired smart diodes, routing charger input automatically between packs.[^rita-emulator]
- Caps sustained output near 25–30 A, now beeping and throwing error 39 on newer boards if regen or drivetrain demand pushes past the limit; stay within the published ceiling even when firmware sliders allow higher numbers.[^rita-current-limit]
- Maintains pack isolation instead of voltage-equalizing, so riders must align state-of-charge manually—especially when mixing internal 12S builds or dual externals.[^rita-soh]
- Comfortable running alongside 12S6P externals on 30 A common-port BMS boards, but the adapter’s own ~30 A ceiling still governs discharge headroom no matter how stout the pack is downstream.[^rita-12s6p]
- The built-in 40 A fuse leaves little thermal headroom—logs of 39 A spikes on 13S13P packs showed diminishing torque returns beyond ~35 A, so riders typically settle near 32 A for longevity.[^rita-fuse]
- Rita will ignore externals that boot around 27 V; raise low packs toward nominal voltage and confirm a common-port BMS so the adapter sees more than the controller’s ~32 V empty threshold.[^rita-low-pack]
- Gen 4 hardware adds charger/KERS surge protection and a shunt resistor that spoofs −10 °C during over-voltage events, but first-generation boards still lean entirely on the pack BMS—treat higher-voltage charging as a reduced-SOC tactic and keep Rita inline with the scooter charge splitter.[^rita-overvoltage]
- To keep stock ESCs alive during high-voltage starts, Rita intentionally fakes a sub-zero battery temperature whenever pack voltage spikes; expect a brief cold warning on the dash until the top of charge burns off and KERS re-enables automatically.[^rita-cold-warning]
- Telemetry prioritizes whichever pack sits a few tenths of a volt higher; disconnect or top-charge the auxiliary pack to view its stats.[^rita-telemetry]
- The adapter needs the external pack slightly above the internal before M365 BMS Tool will talk to it, and leaving the wrong cell count configured can disable electric braking or even damage the module when swapping between 10 S and 12 S packs.[^rita-bms-tool]
- Rita tops the internal battery first while a charger is connected; quick-charging externals means unplugging them from Rita and using an XT30 harness or standalone brick.[^rita-charge-order]
- Denis is deferring rider requests for heavier fuses and extra data lines until demand stabilizes—next-gen externals will instead ship with BLE-enabled smart BMS telemetry so the harness stays simple.[^smart-bms]
- Keep the adapter PCB’s red charge lead connected even if you reroute the main positive elsewhere—the board still draws through that pad and will misbehave if it is omitted.[^rita-charge-lead]
- AWD conversions must nominate a single Rita “master” controller, forward only the white data lead to the slave dash, and keep dashboard grounds common to avoid error 14/21 loops while doubling up ESCs, BLEs, motors, and matched batteries; riders also enforce ~3 km/h rolling starts so the hubs do not chatter from a dead stop.[^rita-awd][^awd-roll]
- V4 hardware extends sensing up to 15S while still bottlenecking battery current near 25 A; newer boards add charger and regen over-voltage protection that only works when Rita stays inline with the scooter’s charge path.[^rita-v4]
- Relocating the Xiaomi charge port outside the bag is acceptable if a three-way splitter remains so Rita can detect chargers and enforce safeguards.[^rita-v4]
- Wireless anti-theft relays should interrupt the BLE/dashboard’s 5 V feed instead of the high-current battery line: route the controller’s red/black pair into the relay “in” and send the “out” pair back to the dash.[^rita-relay]
- Leave Rita’s BMS emulation enabled even on analog packs unless you can manually watch voltage in real time; disabling it strips the adapter’s mixed-pack safeguards.[^rita-analog-safeguard]
- Rita firmware still throws a cosmetic dash jump from ~25 % to ~60–70 % state of charge during heavy regen; the fix is queued, so treat the spike as a known quirk for now.[^1]

### Repair BMS Program

- Current production supports 10S4P batteries with ongoing development toward 12S models; units are configurable over simple USB-UART adapters for clone scooters.[^bms-roadmap]
- Default charge ceiling is 4.15 V per cell (≈4.14 V after diode drop) but can be tuned higher or lower for longevity or range.[^bms-ceiling]
- Field tests logged 37 A discharge headroom when paralleled with another 10S pack, while the 3 A charge limit pushes owners toward patience or dual chargers.[^bms-headroom]

### External Battery Kits

- Wildman 2 L hard cases remain the standard enclosure, cleanly fitting 8 Ah-class 10S or 12S packs; 3 L variants are reserved for future 5P customs once supply stabilizes.[^battery-enclosures]
- Wildman E2 (≈180 × 105 × 83 mm) shells comfortably fit Denis’ 8 Ah-class bricks, while the 1 L case only houses compact 36 V hoverboard packs and the 3 L shell needs printed brackets to tame the extra bulk.[^wildman-e2]
- Builds lean on Samsung 35E or equivalent 21700 cells, quality 12 AWG wiring, and Daly 25 A common-port BMS boards; XT30 connectors are intended for semi-permanent joints rather than frequent hot-swaps.[^battery-bom]
- Turnkey 10S4P range kits land around €170 plus roughly €30 for the Wildman 2 L bag and €20 shipping, built from Samsung 35E cells on 20 A common-port BMS boards with genuine XT30 connectors sized to the Xiaomi inlet.[^price-10s]
- Auxiliary packs keep their BMS inline but present a single XT30 common-port lead so Rita can top the internal and external batteries in parallel; unplug Rita and use a dedicated harness whenever the auxiliary pack charges off the scooter.[^common-port]
- Dimitrij still warns that bypassing external BMS hardware or paralleling packs at mismatched voltages without Rita can end in catastrophic failure—keep every auxiliary pack’s protection board in circuit and lean on Rita’s permanent-emulator mode for analog scooters.[^2]
- Range+Speed bundles hinge on a 50.4 V charger; Denis paused full kits when supplies dried up, steering builders toward resistor-modded OEM bricks or Mean Well ELG-240-48A-class chargers while keeping the 10 S range pack as a plug-and-play option.[^3][^4]
- Quality connectors matter—Denis’ harness length coils inside the Wildman bag, but if you relocate plugs stick with genuine Amass XT30 hardware and practice soldering on scrap to avoid melting shells.[^5]
- Current 12S3P packs use Samsung 35E cells (≈10.35 Ah) and retail near €260 with bag, while standalone 12S4P builds sit around €230; chasing 3 L bag experiments escalates cost quickly as parallels increase.[^6]
- 12S4P 21700 bricks roughly match 12S6P 18650 capacity but press against Wildman dimensions; Denis’ 13S4P modules barely fit the 2 L case and stacking two forms a 13S8P tower to tame sag for dual 500 W scooters, with Samsung 35E holding voltage better than LG MJ1 under the same load.[^7][^8]
- Rear mounting brackets are printed by 3Dway Kraków under a commercial license, so customers request custom current limits while Denis keeps the STL private.[^9]
- Wildman 2 L shells remain the default enclosure because larger 3 L cases complicate cable clearance even though they exist for oversized builds.[^10]
- Ultra-long-range experiments include 60 V 40 Ah externals that promise ~130 km at ≈11 kg, underscoring the weight/range trade-offs once riders leave Xiaomi’s 36 V ecosystem.[^11]

### Research & Testing Backlog

- Dual-motor builders still want dyno-style efficiency testing—community logs cannot answer whether km-per-mAh or watts-per-kilometre best capture AWD gains, so Denis notes the need for controlled bench work when time allows.[^12]

### Fulfillment & Logistics (mid-2020 snapshot)

- UK orders led demand in July 2020, with reseller Dimitrij coordinating Rita distribution and staging July 13 dispatches for preorders.[^13]
- Charger shortages forced Denis to pause complete Range+Speed kits even while he debated emergency Wildman bag buys from Polish resellers; lithium shipping stayed ground-only via DPD/UPS/TNT because DHL air refused battery freight.[^14]
- Payment-gateway outages later that month blocked battery and charger sales; Rita adapters, BMS boards, and bags remained available while Denis navigated Russian-to-Polish bank transfers and warned that Revolut workarounds were awkward stopgaps.[^15]
- Range Boost bundles double an M365 Pro’s capacity by matching OEM pack size, while Range+Speed kits demand firmware tweaks whenever the auxiliary pack is removed.[^range-kits]
- AliExpress packs with separate charge ports require BMS swaps before pairing with Rita to avoid uncontrolled overcharge through the discharge leads.[^separate-charge]
- Community buyers now dispute “13.8 Ah” 10S2P listings and inspect harnesses closely after shorts traced back to unsoldered Y-cable joints inside Wildman bags—treat unbelievable capacity claims as fire risks.[^counterfeit]
- Denis resells his battery catalog at cost and asks the community to surface vetted Chinese suppliers while independently verifying capacity claims before ordering elsewhere.[^resell-cost]
- Cylindrical cells typically fail open when abused, while pouch cells demand compression and vent violently—Denis favors vetted Samsung 35E/50E refurb lots for midlife rebuilds over mystery pouch modules.[^16]
- Refurbished Samsung 35E/50E lots from NKON’s late-2021 inventory remain Denis’ go-to when new stock dries up—he logs batch codes so midlife rebuilds stay traceable.[^17]
- Secure the Wildman case upright with clamps or cages instead of glue fills so thieves cannot unzip the pack in seconds and technicians can still service the battery.[^bag-security]
- New mounting hardware bolts packs to Wildman bags with eight screw/wide-washer mounts, fiberglass sleeving, and foam padding so cells cannot rattle or chafe during pothole hits.[^18]
- Keep builds under roughly 20 cm pack length—the shallow Wildman shell will not swallow 25×7×7 cm bricks without stressing the zipper or wiring.[^bag-length]
- Pad the two shallow Wildman screws that face the pack and mount XT30 leads upward so vibration does not scuff the harness insulation.[^wildman-screws]
- Repurposing tool batteries like Makita BL1850B modules rarely works—the 5 S packs sit too low for Rita to blend in, so Denis advises selling them and investing in 10–12 S scooter packs with Daly common-port BMS boards instead; bargain 4 Ah lawnmower bricks built for ~180 W peaks can overheat or ignite when pushed toward Rita’s 25 A ceiling.[^tool-packs][^lawn-pack]
- Cheap “13 Ah” externals often sag early enough that Rita falls back to the OEM battery—test suspect packs alone at low load and expect legitimate Daly-based builds to cost far more than €160 listings.[^cheap-packs]
- Monorim’s off-the-shelf 48 V suspension pack arrives without brake or BMS harnesses, so Denis usually steers riders away unless they are ready to fabricate the missing wiring.[^19]
- Rear-suspension rack mounts sacrifice folding and need full silicone sealing to keep exposed externals weatherproof on commuter builds.[^20]
- Citylion range-kit owners should skip the extra Y-harness and follow the manual—the stock charger should read ~42 V with both 10 S packs full, and a fast green LED simply means the shipped pack arrived topped off.[^21]
- Mirono’s 13 S3 P (≈48 V/15 Ah) deck pack built from LG M50T or Samsung 50E cells fits Denis’ extender with BMS emulation to dodge Happy BMS costs, but Denis notes his Happy-equipped equivalent sells for €290 once labour is included.[^22]
- Spot-welding quality remains the gating tool—Sunkko bench welders (~€300) still anchor Denis’ production because clean nickel seams and sealed housings are what customers pay for.[^22]
- Monorim’s canned external pack hides a series diode on the charge lead; it prevents reverse-polarity mishaps on common-port BMS boards but costs voltage headroom, so experienced builders bypass it once wiring is verified.[^23]
- Deck-mounted dual-pack conduits must be armored and wired for permanent duty; exposed runs strapped along the floor are “self-propelled bombs” unless they receive proper housings and fasteners.[^24]
- Stock Xiaomi packs squeeze into 120 mm heat-shrink, but Denis prefers 170 mm sleeves for Wildman bag builds and caps controller settings around 55 A phase/30 A battery to stay within thermal limits.[^pack-wrap]
- Secondhand cell bundles that swing voltage wildly on a 2 A charger get torn down: he IR-tests every cell, regroups by mileage, and warns that imbalance keeps worsening even after balancing sessions.[^refurb-triage]
- External-pack capacity checks happen with a constant-current load while the internal pack stays connected; reconnect packs only when their voltages sit within ≈1 V to avoid hammering the weaker BMS.[^parallel-test]
- Happy BMS-equipped 14 S packs tolerate a 13 S (54.6 V) charger in a pinch—it simply stops early until a proper brick arrives, trading range for safe top-ups.[^happy-13s]
- Denis published updated Wildman 2 L/3 L mount STLs plus bolt-and-sleeve hardware so externals stay fixed instead of floating on foam blocks.[^wildman-stl]

### Workshop Hardware Notes

- Cold-to-warm transitions deflate 10″ tubeless tires; top pressures off before leaving heated garages so thermal contraction doesn’t mimic a puncture on the first winter ride.[^thermal-expansion]
- Base-model scooters can regain telemetry by swapping in Xiaomi dashboards—simple three-wire harness swaps or aftermarket boards such as m365dash.com restore data-line access even when Rita isn’t present.[^dash-retrofit]
- Boyueda 2800 W/60 H hubs run on Kelly controllers at 200 + A for torque but need temperature monitoring and robust cooling before chasing long hill pulls.[^boyueda-torque]
- Monorim-branded motors earn criticism for price versus output—builders stick with PMT, Vsett, or Blade-spec hubs paired with trusted controllers instead of paying a Monorim premium.[^monorim-motor]
- PMT 10×3 casings need roughly 2 mm removed from Xiaomi rim sidewalls (or Dualtron-class wheels) to seat correctly, while PMT 10×2.125 rubber slips onto 6.1″ rims without machining.[^pmt-fitment]
- Essential kickstand spacers park level around 6.5 cm; taller stacks overstress the bracket, so riders buy longer M6/M8 fasteners (≈80 mm) or tap fresh threads rather than piling washers.[^kickstand-height]
- Tubeless conversions can reuse stock casings with automotive sealant, but rims seep unless sealant is refreshed and aluminum-safe blends such as yellow Slime prevent corrosion.[^tubeless-sealant]
- Worn Monorim star nuts get replaced with paired bicycle star nuts driven on a sacrificial bolt, and longer stem bolts keep the stack aligned after repeated rebuilds.[^25]
- Clone BLE boards fight DIY NeatDash replicas—follow the 120–150 Ω resistor and diode orientation notes, but expect to migrate to Mirono and nvram’s ESP32/OLED design once released.[^26]
- Secure brake-housing runs to the frame and trim excess length so lever travel isn’t wasted flexing the cable before it bites.[^27]
- Inspect 3D-printed rear pack supports regularly; heavy 13 S bricks crack mounts near the rear bolt and immediately skew group voltages if left unchecked.[^28]

### Late-Season Service Notes (Lines 501-600)

- Controller-voltage debates continue: Denis trusts the stock 10 MΩ ADC divider up through 16 S builds, while peers still swap in ~160 kΩ resistors to dodge error 24 when emulating BMS behaviour—XiaoDash now handles the firmware side without legacy RX/TX jumpers.[^adc-16s]
- Rita-charged 12 S externals intentionally stop around 49.2 V (~4.1 V/cell); chasing higher targets nets barely a kilometre of extra range and can cost regenerative braking on long descents.[^rita-49v]
- Chronic split charging usually traces back to failed OEM temperature sensors that lock the internal BMS—disconnect Rita and verify both probes before blaming the adapter.[^temp-sensors]
- Winter commuters swap to 10×2 tubeless off-road casings or Amalibay 9.2″ treads, run conservative screw-stud experiments, and accept slower acceleration once temperatures fall below freezing.[^winter-tyres]
- Monorim suspension hardware still loosens or eats bearings; shops upgrade to 12.9-grade bolts, trim over-length hardware, and inspect for play to protect cable runs.[^monorim-hardware]
- Hybrid Xtech brakes corrode and leak under high-speed loads, pushing workshops toward full Magura hydraulics or premium mechanical calipers.[^xtech]
- Paolo’s 1.2 kW+ hubs deliver better torque via larger magnet stacks but demand inverted Monorim forks or rear-drive conversions to clear 10″ rubber.[^paolo-hubs]
- Seal decks with marine-grade PU50 urethane instead of Sikaflex—the compound cures underwater, sands cleanly, and stays elastic for years; neutral silicones remain the choice when joints must reopen.[^pu50]
- Shenzhen-built 36 V 25 Ah front packs using Samsung 50E2 cells ride fine once steering balance is checked, yet the crew reiterates that every external still needs its own BMS, fuses, and wiring discipline or the adapter fuse/Happy BMS will trip.[^50e2]
- Happy BMS red LEDs after hard braking prompt a safe discharge, capacitor bleed, and staged reconnection before further testing, while DC step-up “chargers” get tamed by starting below pack voltage and easing current up to ≈1 A.[^happy-stepup]
- Parallel charging keeps both BMS boards balancing when riders Y-split the JST charge leads; expect the internal board to blink red until voltages settle, and remember JST pigtails prefer ≤3 A while ≥40 A discharge legs deserve XT60-class hardware.[^parallel-jst]
- Scootermode 14 S conversions clear error 24 by flashing firmware with a 10 S pack attached, and Mi Electric 3 dashboards locked by Mi Home need BLE/UUID checks via Downg or XiaoDash before ST-Link work pays off.[^happy-fw]
- High-speed builds rely on Roscheeee’s metal brake adapter for 160–180 mm rotors, but the crew notes conventional brake fluid boils long before glowing 700 °C rotors and that even premium PMT/CST tires overheat quickly above 80 km/h—protective gear is mandatory.[^highspeed-brakes]
- Winter range planning caps hill pulls around 600 W, keeps throttle near 80 %, and pairs ferrofluid (≈4–6 ml) with cold ambient temps plus full waterproofing—silicone every pass-through, grease bearings, and sandwich 3D-printed spacers between silicone layers while keeping threads clean.[^winter-range]
- 48 V pack plans lean on Samsung 40T 13S5P layouts, 60 A BMS hardware, XT60 upgrades, and awareness that Happy BMS firmware stores capacity in 16-bit signed fields (≈32 Ah max) while Pro 2 owners stick with firmware 126 to preserve a 42 V ceiling.[^40t-bms]
- Harness upgrades replace long AWG16 extensions with AWG12, keep stock motor cable gauge, and remind techs that half a 237 ml slime bottle seals 10″ tires effectively.[^harness-slime]
- Shop sourcing notes praise Voltride for quick PMT shipments and continue steering customers toward Scootermode or Paolo controllers over overpriced MaxMods alternatives.[^vendor]
- Charger modders restack TL431 feedback resistors (two 33 kΩ plus 100 kΩ with a single 16 kΩ 0805) and swap 63 V caps for 100 V parts before testing at 57.5 V, while remembering the transformer’s ≈1.7–2 A ceiling; Android 12 riders sideload Rita/BMS v0.0.12 APKs, and quality YZPOWER 13 S chargers beat anonymous “48 V” bricks as long as connector swaps are soldered and heat-shrunk.[^charger-chain]

### Internal Voltage Upgrades

- Denis began shipping a production-ready custom internal pack for Xiaomi Pro/Pro 2 scooters, hand-braiding the heavy-gauge charge/discharge harness in-house to mirror the robustness of his 36 V kits.[^pro2-internal-pack]
- Pro 2 buyers chasing 48 V internals still order the standard 44 V kit and add a checkout note—Denis ships the higher-voltage variant even though generic AliExpress bricks technically fit but waste deck volume.[^29]
- Gen 1 Xiaomi controllers remain torque-focused—field weakening only lifts them to roughly 32 km/h, so Denis frames voltage upgrades as a way to sustain climbing power rather than chase high top speed on stock electronics.[^30]
- XiaoDash must be set to 13 cells and 20 Ah before riding the 48 V pack; leaving stock sliders in place keeps the scooter locked to 36 V behaviour.[^31]
- Ninebot G2 owners can now retain the factory controller by flashing XiaoDash on the stock ESC, adding the dashboard harness, and applying the SHFW Gen 4 patch to unlock higher speed while preserving blinkers and buzzer support.[^32]
- Matching-capacity 48 V upgrades add watt-hours and noticeably more pull versus 36 V twins, helping heavier riders keep pace without changing the rest of the build.[^33]
- Daily 20 S builds and experimental 30 S stacks really belong on 11-inch frames; Denis warns 84 V/25 A tunes only approach 70 km/h safely when regen stays disabled because stock Xiaomi controllers eventually blow from the spike.[^34]
- Riders targeting 70–130 km/h convert to 50–60 mm Blade/VSETT-class hubs, 15–22 S batteries, and 300 A VESCs with custom waterproof mounting—Denis keeps 20 S as the practical ceiling for daily use before thermal runaway and packaging headaches dominate.[^35]

### Firmware & Unlock Workflow

- Late-model Pro 2 dashboards on BLE 1.55+ still require ST-Link downgrades; clone controllers may spoof serials yet reject OTA flashes, and flashing the latest Xiaomi BMS firmware can permanently brick the board.[^stlink-ble]
- XiaoDash performance profiles occasionally corrupt activation data; reflash stock firmware, power-cycle the scooter, then reapply tweaks if the dash gets stuck “on.”[^xiaodash-reset]
- The newest Pro 2 dashboards unlock only after an ST-Link flash or a temporary swap to an older dash—warranty stickers aren’t a concern because the head unit simply unscrews for the procedure.[^dash-swap]

## Controller, Firmware & Motor Planning

- Current-step tuning on stock controllers balances heat and response—around 350 mA keeps housings cool for conservative riders, while 400 mA “intensity of current change” presets overstress traces even on reinforced boards.[^current-step][^current-step2]
- Sustained 60–65 A pushes have melted OEM motor-to-ESC connector caps; reinforce harnesses or stay near 50–55 A, which testers found sustainable at ~31 °C in mild weather.[^connector-melt]
- Rita may ignore an auxiliary pack after boot; blipping the throttle re-triggers detection, and zero amp/watt telemetry on Xiaomi dashboards is expected because Rita owns the data line while emulating the BMS.[^rita-detection]
- Denis reset his recuperation guidance to 4.10 V per cell (with future app support for 4.18 V), keeps braking currents conservative (≈4 000–20 000), and disables KERS on coasting builds to protect unreinforced 12 S controllers.[^recuperation]
- iOS riders now have the Scooter Companion beta for flashing Xiaomi 1S/Pro2 and Ninebot G30 firmware, bringing Apple parity with Android flashing stacks.[^ios-companion]
- Mixing hub wattages without matching Kv causes the faster motor to drag the slower one; AWD conversions need matched hubs plus duplicate controllers, BLE boards, and ideally discrete packs to share current.[^kv-match]
- 500 W hub swaps demand thicker power traces, MOSFET upgrades, and 13 S charging plans, while even 350 W motors need firmware reflashes that raise phase current limits for brisk launches.[^hub-upgrades]
- Denis is designing a Ninebot G30/G30LP battery bag; riders report Gen 1 motors feel stronger while Gen 2 windings trade torque for durability, so either hub can anchor high-power builds.[^g30-bag]
- Engineers showcased a Ninebot G30 star/delta mod delivering 55–66 km/h bursts, underscoring how much stiffer the G30 controller is compared with stock M365 boards.[^g30-delta]
- XiaoGen-based 12 S tunes push M365 Pros beyond 43 km/h while reporting zero watts in M365 Tools because Rita fakes the stock BMS; treat the missing telemetry as normal rather than a wiring fault.[^zero-watt]
- Xiaomi 1S riders chasing range gains should stay with 10 S kits unless they are confident flashing firmware—XiaoFlasher’s €6.99 upgrade supports Pro/Pro2, and BLE 074 dashboards wake again after holding brake + throttle or reopening the Mi app.[^xiao1s]
- Avoid mixing configuration generators—mismatched 33 k presets and ignored thermal upgrades have already blown MOSFETs even when dashboards showed moderate temperatures.[^config-mismatch]
- Keep storage voltages around 3.7 V, avoid prolonged cold soaking, and expect Rita telemetry to favor whichever pack sits about 0.5 V higher when both stay connected.[^storage-telemetry]
- Community dashboard builders tinker with dual displays, Wi-Fi loggers, and iOS tooling despite Apple’s developer hurdles slowing parity with Android experiments.[^custom-dash]
- Tudor is preparing internal 13S4P, 13S7P, and 15S5P Pro packs (the larger options needing ~23 mm deck extenders) and pairing 30 Ah 13S batteries with dual 500 W hubs plus VESC controllers to reach roughly 3 kW while prioritising torque.[^tudor-internal]
- High-current BMS hardware still balloons toward GPU-sized enclosures around 120 A, pushing experimenters toward 140 A VESC controllers, larger spacers, or even 20 S packs before conceding the platform suits karts more than scooters.[^highcurrent-bms]
- Ninebot Max builders report UPS-friendly shipments from Tudor, new customs paperwork, AWD conversions fed by 13S60A packs, and parallel efforts to run 48 V Monorim motors near 50 km/h once 10" rubber is dialled in.[^max-shipping]
- Monorim 500 W owners compare ~45 km/h results on 13S3P packs and note Pro 2 firmware still enforces ~53 km/h cutoffs unless they revert ESC builds or run 350 W hubs on Xiaogen tunes—both paths add heat that demands extra monitoring.[^monorim-speed]
- Chasing 13 S and beyond means upgrading controllers with beefier capacitors, IRFB4110-class MOSFETs, reinforced traces, and revised divider resistors (e.g., ≈28 kΩ/130 kΩ for 13 S), otherwise Denis steers newcomers toward 12 S externals.[^13s-controller]
- VTA controllers keep up with 35 A daily abuse and short 65 A bursts on 13 S builds when phase wiring is upsized, but 45 A through thin leads has already melted connectors—tight crimps and heavier cable are mandatory before raising current.[^vta-wiring]
- Monorim’s forthcoming controller is expected to drive dual hubs from one ECU, while builders like François still split ~65 A across twin controllers on AWD scooters without overheating.[^monorim-awd]
- Stock Xiaomi controllers can survive brief 12 S use if currents stay near 25 A and aggressive KERS is disabled; once reinforced hardware goes in, Xiaogen or custom firmware can nudge limits upward cautiously.[^stock-12s]
- Thermal alarms at 88 °C on long climbs are the cue to derate or upgrade to VTA/Paolo hardware—the community pegs 60–65 °C as the safe ceiling for stock ECUs even on 36 V packs.[^controller-heat-65c]
- Stacking a 6 S booster onto a 10 S pack effectively creates a 16 S system that demands uprated capacitors and MOSFETs, whereas Denis’ 12 S kits still deliver ~40 km/h with manageable thermal loads.[^16s-risks]
- Xiaogen users chasing longevity aim around 27 000 mA motor current with ≤30 A brake regen on unreinforced boards so controllers last thousands of kilometres.[^xiaogen-target]
- Monorim’s 1000 W hubs arrive with thin phase leads that owners replace with HXT 4 mm connectors after drilling valve holes for tubes; shipping two large hubs privately can cost $300–350, so many rely on Kroxne/VTA group buys.[^monorim-1000w]
- Tudor’s reinforced controllers still cap near 13 S—earlier 17–19 S experiments at ~27 A (≈1.3 kW) risked melting MOSFETs, prompting purpose-built 15–20 S hardware instead.[^tudor-13s-cap]
- Voltage without matching current headroom delivers diminishing returns: 14 S Monorim 500 W setups plateau near 55 km/h until sag is addressed, 12 S builds hover around 44 km/h, and 13 S pushes 45–50 km/h while overheating 350 W motors—swapping to a 500 W hub keeps controller temps in the low 40 °C range even at 40 A.[^voltage-vs-sag]
- Sustained 27 A hill climbs have already shaken magnets loose inside Pro 2 hubs, reinforcing the need for active cooling or beefier motors for long gradients.[^magnet-fatigue]
- Exotic star/delta switching can show 74 km/h freewheel speeds but sits far outside Xiaomi’s safe design envelope.[^star-delta-risk]
- Monorim’s 500 W hub is rated for 48 V; on 10 S it behaves like a 375 W motor, so pairing it with 13 S packs and reinforced controllers keeps torque gains sustainable.[^monorim-48v-rating]
- Hitting 70–80 km/h realistically demands 17 S or higher, upgraded controllers, full suspension, and large 6–10 P packs that cost €500–700 in cells alone—well beyond what the stock deck can house without external bags.[^17s-requirements]

### Firmware & Diagnostic Updates

- Flash BLE 073/DRV 1.5.5 with standard DownG before loading Xiaogen’s modded bundle; Pro 2 dashboards resent aggressive downgrades, so keep a USB ST-Link ready in case a BLE write leaves only a blinking tail light.[^downg-workflow][^pro2-downgrade]
- ST-Link with stock DRV 1.5.5 firmware revives controllers when mismatched images (e.g., BLE 126 on Denis’ BMS) trip error 21; follow the community recovery videos after failed DownG attempts.[^36]
- Xiaomi drivetrains stay happiest near 27 A (≈800 W) sustained—higher battery or phase currents only deliver brief surges before heat climbs and packs sag, even with 350 W aftermarket hubs.[^37]
- Modding Xiaomi’s charger with Vishay 14.3 kΩ feedback stacks demands flux, short checks, and careful soldering before trusting the new 50.4 V output.[^38]
- Workshop cheat sheets map ESC error codes (e.g., 28 for HS FET faults) to likely root causes so post-mod anomalies are easier to triage.[^39]
- Apple still blocks scooterhacking sideloads, leaving iOS riders dependent on an Android device (or emulator) for Xiaomi firmware tools unless they fall back to ST-Link reflashes.[^ios-android]
- Target BLE 074 for stability on Pro dashboards, and remember VTA controllers shipping with ESC 1.5.5 cannot safely drop to BLE 0.90—stay on modern BLE builds and double-flash Xiaogen if the first pass misbehaves.[^ble074-stable][^vta-esc]
- Pro 2 dashboards on firmware newer than DRV 2.2.3 clamp custom builds; stay on DRV 2.2.3 or temporarily downgrade to DRV 155 to configure Rita before returning to the latest release.[^40]
- Denis’ Android Rita app still lacks native Pro 2 BLE support, so riders toggle permanent-emulator mode via desktop tools or flash XiaoGen 2.0.5 with m365Downgrade XG Mod 21 and keep an ST-Link handy for recovery.[^41]
- Match Drive-mode current to pack voltage—32 A on 12 S pulls roughly 1.3 kW, so dial back if you want a ~900 W ceiling.[^42]
- Lap (wet-sand) the ESC baseplate and deck mating surfaces before final assembly so thermal paste spreads evenly and MOSFETs survive 40 A peaks.[^43]
- Dashboards misreport speed after 10" swaps unless you adjust the wheel constant (≈8.1 % in Xiaogen) and confirm against GPS; “Russian” throttle mode keeps lever travel mapped directly to torque for aggressive builds.[^44]
- Inspect XT30/XT60 connectors first when scooters power-cycle after curb strikes—lifted phase pins or loose harnesses cause most symptoms before electronics fail.[^45]
- Rain-damaged packs underscore waterproofing charge ports and dashboards; Denis quotes roughly eight hours to recharge his 13.8 Ah range kit with the stock brick once the scooter dries out.[^46]
- Pro 2 riders chasing 12 S speed gains must reconfigure Rita’s pack parameters via M365 BMS Tool and often soften KERS (≈18 A) to keep the ESC alive during hard braking.[^47]
- If a scooter stays dark after installing Rita, disconnect the dashboard, short the diagnostic pins to confirm the ESC still boots, inspect the controller underside for blown traces, and escalate to ST-Link probing to verify the 5 V rail.[^rita-dark]
- Camilo’s BLE 074 v7 firmware adds throttle filtering and a slow mode but can trigger sluggish launches or random slow-mode engagement on Xiaogen tunes; riders disable cruise or roll back to earlier BLE revisions while waiting for fixes.[^ble074-v7]
- Series-boosting a 10 S pack with an extra 3 S module can brown out on hills as sag or firmware limits trip—monitor current in M365 Dashboard, rein in custom firmware amp draws, and only re-enable boosters once voltages stay stable.[^series-booster-sag]
- Rita still expects matching over-voltage firmware ceilings before you chase 13 S/15 S builds—follow Denis’ manuals, set the proper 63 V cap, and verify the controller tolerates the target voltage before relying on the adapter to clear error 24.[^rita-overvoltage-match]
- Tudor now offers 1–2 day express board replacements and is bench-testing his controllers north of 60 V, giving high-voltage experiments a documented support path.[^tudor-express]
- Error 27 on a Pro 1 often traces back to a mismatched serial baked into custom firmware; reflash and confirm the serial instead of replacing hardware outright.[^error27]
- Keep the diode-mode MOSFET test flow handy—charge the gate, confirm the drain-source drop, discharge through a finger, and inspect gate drivers if any device reads short while chasing 12 S brake-induced shutdowns.[^mosfet-diagnose]
- Denis still ranks paid XiaoFlasher bundles ahead of scooterhacking.org and XiaoGen when generating firmware images, and he tells 12 S experimenters waiting on hardware repairs to stick with conservative Xiaogen defaults while only nudging voltage limits.[^xiaoflasher-priority]
- Stock VTA controllers now refuse Xiaogen firmware unless you spoof a compatible `21886/00XXXXXX` serial via the web changer, flash with a modded M365 DownG, and keep an ST-Link V2 ready in case the dashboard bricks on the first pass.[^vta-sn]
- Xiaomi 1S riders jumping to 12 S externals need to downgrade to `mp365_drv221_1s` and `mp365_ble129_1s`, flash the 51 V custom image in XiaoFlasher, raise sport-mode current toward 25 A (eco ≈15 A), disable KERS, and monitor controller temps—skipping steps has already killed dashboards until they were revived over ST-Link.[^1s-12s]
- XiaoGen migrations for 1S and Essential scooters still start with the bundled “migrate” firmware before any custom file, keeping the stock BLE alive and an ST-Link on standby to recover blank speed/battery readouts.[^xiaogen-migrate]
- Lite/Essential owners running 12 S externals cap custom firmware near 51 V, and Rita only exposes its configuration panel once the auxiliary pack sits a few tenths above the internal so the adapter can seize control.[^lite-12s]
- Rita v5 cut power whenever a full 13 S internal outran a 12 S external; rolling back to v4 or enabling permanent BMS emulation stabilized the blend until Rita v6 shipped with fixes for phantom red temperature icons on 12 S installs.[^rita-v5-v6]
- Custom pack counts such as 11 S require dropping the regen ceiling toward 47 V, matching Rita’s cell count, and charging with a dedicated 11 S supply because Xiaomi’s 10 S brick stops around 41.7 V and leaves the extra cell under-filled.[^11s-firmware]

## Tire, Brake & Chassis Upgrades

- Plan mechanical brake upgrades alongside 12 S Rita builds—the combo touches ~40 km/h on flat ground when fully charged, so stronger stoppers keep the extra speed manageable.[^brake-upgrade]
- Organic pads fade under repeated high-speed stops, so faster riders shift to sintered or ceramic compounds despite faster rotor wear; dual-disc conversions split a single lever’s cable to keep both calipers synchronised.[^sintered-pads]
- Classic cable-disc brakes tighten via the lever’s barrel adjuster for fine tweaks and the caliper’s hex bolt for coarse moves; if levers start bottoming out, inspect pad thickness before chasing cable stretch.[^cable-disc-tuning]
- Confirm Pro 2 hub bolt patterns before ordering 6-bolt MTB rotors, and note Tudor is gauging demand for a Monorim 500 W brake adapter once about 20 riders commit so machining costs pencil out.[^rotor-pattern][^monorim-adapter]
- Ten-inch conversions vary by casing: CST 10×2.25 tyres often need rim sanding, Kenda-branded 152 mm carcasses mount tight, and Wanda 10×2 options stay grippy at ~4.2 bar while outlasting ultra-soft red compounds.[^48]
- SKF-style 2RS bearings seal better for wet riding than 2Z shields, keeping grit out during rainy commutes.[^49]
- Semi-metallic (gold) pads hold up in rain better than the organic sets bundled with Xtech calipers, whereas ceramic pads run hot and demand close rotor monitoring.[^50]
- Rear-suspension kits stretch the wheelbase roughly 10 cm and noticeably stabilise Xiaomi frames for higher-speed builds.[^51]
- Pull the side plate so the hub and tire slide off together, and match 10" solid rubber by inner diameter and width before trimming any metal.[^solid-removal]
- Fitting Deli 10×2" tires on 1S/Pro 2 frames often means relocating or shaving the rear-light connector, extending wiring, and resealing the reroute with hot glue or deck grommets.[^deli-routing]
- Mountain-bike cockpit swaps need oval-to-round stem adapters and relocating the BLE/display harness; expect to dig Xiaomi’s foam-packed frames clear before fishing fresh cabling or motor leads.[^stem-adapter][^frame-foam]
- Monorim 500 W hubs that start vibrating after 45 km/h emergency stops usually implicate controller damage or clamping issues—inspect Rita braking current, MOSFET mounting pressure, and thermal paste coverage before blaming the bearings.[^monorim-vibration]
- Solid tires remain a last resort: expect ~20 % more energy use, harsher rides, and the risk of fatiguing battery tabs; most riders revert to 10" CST or Wanda pneumatics with reinforced tubes and fair labour pricing.[^52]
- Builders now coat controller fasteners with medium-strength thread locker, replace kapton under MOSFETs with high-conductivity pads, and even fill sealed hubs with mineral oil to beat external fin kits.[^controller-fasteners][^oil-cooling]
- CST 10×2.25 tires sized for 152 mm rims refuse to seat on Xiaomi’s 155 mm wheels and can foul the frame even if forced—swap to scooter-specific casings instead of trimming hardware.[^cst-152mm]
- Monorim 500 W tire options remain finicky: riders have reverted to 8" rubber or alternate casings after wobble-induced crashes because the motor bay leaves little clearance for standard pneumatics.[^monorim-tires]
- Riders have squeezed CST 10×2.5" tires onto Pro/1S frames without cutting the deck, but centring the carcass is tedious and suspension upgrades help clear the extra width.[^cst-10x25]
- Xtech hydraulic calipers paired with Monorim hubs perform best with 135–140 mm rotors, matched adapters, and mineral-oil bleeds using golden semi-metallic pads; the community is benchmarking 120/135/140 mm stacks to balance clearance and leverage.[^xtech-rotor-sweep][^xtech-pads][^rotor-benchmark]
- Installing 10" tires on Monorim hubs demands careful drilling plus ongoing vibration checks above 35 km/h while builders hunt rain-friendly tread and experiment with in-hub oil cooling for stability.[^monorim-drilling][^oil-cooling]
- Genuine Xuancheng 10" tires remain the go-to upgrade—dust the carcass with baby powder, reuse the OEM 8.5" tube, run 45–50 PSI, and look for factory labels to avoid counterfeits that wear out around 700 km.[^xuancheng-10in]
- Smaller M365/1S frames sometimes need grinding or bending to clear 10" rubber, whereas Pro frames typically fit without trimming; installers often file mudguard brackets or flex the stays to stop rubbing.[^frame-clearance]
- Monorim solid tires can deform under high torque; preheating them around 100 °C and recruiting a helper eases installation, but many riders eventually swap to pneumatics for better ride quality.[^monorim-solid-heat]
- Monorim front mudguards may kiss 10" wheels—removing spacer foam, shortening screws, or swapping brackets buys a few extra millimetres of clearance.[^mudguard-clearance]
- Higher-speed builds ditch e-brake sensors that pop controllers around 45 km/h, moving to full hydraulic systems (Shimano/Magura) or at least tougher bicycle-grade cables for mechanical setups.[^brake-hydraulic]
- Converting Monorim motors to air tires involves drilling a clean valve hole and ordering angled stems; many riders abandon the bundled solids because they wear quickly under torque.[^monorim-air]
- Konyk’s rear suspension remains the premium option—budget ~€85 for the linkage alone or ~€150 with an EXA A5 air shock—while cheaper ESparts/Monorim combos plus ZGhua solids balance cost against faster tread wear and poor wet grip.[^konyk-suspension]
- Switching to 10×3 inch tires is transformative but generally requires suspension or custom forks; even with dual shocks, solid 10×2.5 rubber transmits every vibration and sends riders back to CST 3" air casings.[^tire-10x3]
- Monorim’s 500 W wheel ships with a solid tire and no valve hole—drilling for tubes still leaves uncertainty about how the side covers clamp the bead, so some wait for purpose-built tubed hubs.[^monorim-valve]
- Killing Monorim stem play starts with loosening the side bolts, tightening the central hinge screw just enough to remove wobble, then re-locking the pinch bolts—over-clamping snaps the fastener and causes crashes.[^stem-play-fix]
- Monorim handlebar adapters raise the folded deck slightly; rotate or shim the bell hook so it still latches the rear fender.[^bell-hook]
- Tire reliability improves with best practices: run Xuancheng 10" rubber at 4.0–4.2 bar, dust tubes with talc so they do not stick, and use slime or careful lever work to avoid pinch flats during swaps.[^tire-maintenance]
- 500 W hub swaps paired with 12 S packs hold 45–48 km/h on flats without the sag toward ~44 km/h seen on 300 W motors once voltage droops.[^53]

## Battery Sourcing, Safety & Maintenance

- Cheap eBay “25 A” BMS boards have tripped around 18 A and dropped externals offline despite balanced cells; swap to trusted 20–30 A units before pairing packs with Rita.[^54]
- Firmware hacks that push Xiaomi charge current to 5 A cook legacy M365 BMS boards near 150 °C—stick with Samsung 35E cells and quality 20 A common-port modules when building auxiliaries.[^55]
- 13 S and even 15 S are electrically possible on newer scooters, but older hardware needs resistor swaps and broader component upgrades before surviving the voltage jump.[^56]
- Water-damaged M365 packs often revive after cleaning the BMS with isopropyl alcohol; Denis keeps compatible replacements on hand when telemetry refuses to recover.[^57]
- External LED strips need proper step-down converters because most consumer strips are rated ≤24 V—tapping the 36 V bus directly is unsafe.[^58]
- A regen-heavy stop without Rita protection scorched both BMS and controller on one customer build; disconnect immediately, recharge sub-2 V cells individually, and tidy any loose sensor wiring before blaming the board.[^59]
- Dashboard brownouts triggered by headlight toggles usually signal BMS faults—swap in a known-good pack, inspect each parallel group, and replace fuses before chasing controller issues.[^60]
- Community teardowns flagged “36 V 20 Ah” AliExpress packs stuffed with only 12 genuine cells; honest 20 Ah builds cost ~€350 and ship as 10S6P, so >42 V “36 V” packs are red flags.[^fake-pack]
- Tudor/VTA common-port externals wire Rita’s XT30 to C-/B- while leaving P- unused so charge and discharge share the same port safely.[^common-port-routing]
- Store packs near 3.7 V (≈50 % SOC), replace water-damaged groups, favor warm indoor storage over cold garages, and keep large assemblies in LiPo-safe bags with extinguishers on hand to curb thermal runaway risk.[^storage]
- Samsung-based packs should avoid charging below 0 °C; gentle 20 km/h cruising barely warms cells, so limit regen and heavy draws until the pack self-heats.[^cold-charge]
- DIY heater pads struggle to raise temperatures—5 V/10 W stickers barely help unless the pack is heavily insulated, so riders instead pull 30–40 A briefly to self-warm while respecting Rita’s 30 A ceiling.[^heater-selfheat]
- Retrofit third-party packs with 40 A UART485 common-port boards (often AliExpress kits bundled with Bluetooth dongles) so Rita can monitor and balance them safely.[^uart485]
- Laudation remains one of the few AliExpress suppliers that hits rated capacity; treat fantastical 60 000 mAh claims as scams even when listings look polished.[^laudation]
- Shoppers hunting 15 S packs look for common-port batteries with integrated BMS boards on AliExpress/Alibaba and expect higher voltage alongside extra available current as parallels increase.[^15s-sourcing]
- Pair 12 S packs with 50.4 V chargers; 42 V bricks leave them around 39 V and erase the expected speed gain until the right charger arrives.[^twelve-s-chargers]
- Denis ships lithium packs half charged (~42 V) for transit compliance and reminds riders that Rita can juggle 13 S internal plus 12 S external stacks when configured correctly.[^shipping-charge]
- 10S4P “range” packs carry similar cell counts to 12S3P “speed” builds; add parallels (e.g., 12S4P) to curb sag when chasing higher current.[^pack-topology]
- Separate charge-port BMS packs stay risky with Rita because it cannot halt over-voltage through discharge leads—swap in common-port boards or replace the pack.[^separate-charge-risk]
- Denis resumed battery sales with 10S4P shipping immediately and limited 12S4P stock (~€230) once charger shortages cleared, still relying on his “Antarctica” shipping workaround.[^battery-sales]
- Repair BMS balancing will eventually top cells back to 100 % if “balance mode” stays on “always,” though stubborn groups may still need manual top-balancing.[^bms-balance]
- 21700 cells fit custom internals for capacity gains, but over-volting ESA-class scooters still hinges on disciplined charger planning.[^21700]
- Rita draws from whichever pack sits higher until voltages equalize, underscoring the need for honest capacity and common-port BMS boards.[^voltage-priority]
- Target 25–30 A common-port 13 S BMS boards for Rita; higher-rated or separate-charge units complicate installs and can starve the adapter.[^bms-sizing]
- Expanding prebuilt 12S3P packs proved impractical—order fresh builds from Denis’ supplier instead of retrofitting extra parallels.[^pack-expansion]
- Denis still recommends Samsung 35E cells for Rita builds; parallel sharing makes 25R-class high-current cells unnecessary for most riders.[^cell-choice]
- Tear-downs of LiitoKala’s advertised 21 Ah packs exposed uncertified 2200 mAh cells, misleading stickers, and poor QC—builders stick with Denis’ Samsung-based assemblies despite shipping limits.[^liitokala-warning]
- A Pro battery showing solid blue LEDs usually just needs the housing opened for a BMS reset or inspection—condensation or controller faults can mimic pack death.[^blue-led-reset]
- Secure external harnesses with proper crimps or soldered joints, add thermal paste under controllers, and replace Kapton with insulating silicone pads to keep case temperatures below ~60 °C.[^thermal-harness]
- Coat controllers with PCB varnish for splash resistance, torque screws evenly so housings seat flat, and treat 60–65 °C as the shutdown target because 88 °C spikes risk MOSFET failure.[^pcb-varnish-tip]
- Stock up on high-conductivity compounds (e.g., Phobya NanoGrease) and 0.5–1 mm Gelid-style pads to replace the factory Kapton insulator under MOSFETs.[^thermal-consumables2]
- Community debates over Samsung 50E versus 35E cells highlight the 50E’s lower voltage sag but 30 A limit on 3 P packs amid global shortages; even official LiitoKala packs arrived with unknown “BICO” cells that veterans avoid for high-current builds.[^50e-35e]
- Cheap AliExpress externals continue to disappoint—a “Samsung” pack caught fire on its first ride, so riders now judge health by cell delta and expect ≤0.011 V spread on quality builds.[^pack-burnout]
- Budget 48 V LiitoKala packs have overheated and shut down within weeks, and salvaged laptop cells demand capacity binning, self-discharge checks, and balanced groupings (e.g., via Repackr) before reuse.[^laptop-cells]
- LiPo bricks can pair with Rita but only with protective BMS boards and tight current limits because the adapter’s 40 A fuse is the last line of defense—pouch packs vent violently compared with reputable 18650s.[^lipo-bms]
- Point novices toward Micah Toll guides and Vruzend prototyping kits before attempting welded packs, and remind them that RC LiPos wired 6S+6S demand a dedicated 12 S BMS plus a non-Xiaomi charger to avoid fire risk.[^lipo-warning]
- Match your BMS to the intended series count—12 S packs need purpose-built 12 S boards rated near Rita’s 30 A ceiling rather than repurposed 10 S modules.[^bms-match]

### Security & Accessory Notes

- Some immobilisers expect 415 MHz remotes; riders running 315 MHz keyfobs need matching radio modules before tapping the controller’s 5 V feed.[^61]
- Compact Master Lock cables suffice for quick stops if you keep the mechanism lubricated with graphite, but couriers warn that leaving scooters unlocked in dense cities invites theft within minutes.[^62]
- Expect reputable 10 S materials to cost at least €100 before labor or taxes; suspiciously cheap packs usually hide weak cells and bargain BMS hardware.[^pack-cost]
- Denis’ go-to cell shortlist still spotlights LG MJ1, Samsung 35E, and Sanyo options vetted with lygte-info’s 18650 comparator before landing in Wildman builds.[^cell-shortlist]

### Pack Planning & Configuration

- Rita always favors the battery sitting a few tenths higher—keep auxiliary packs slightly above the internal if you want them to shoulder discharge first and monitor state-of-charge inside the app rather than assuming the external drains alone once voltages equalize.[^rita-priority][^rita-app-monitor]
- Voltage adds speed, amps add torque, and a 13 S4 P Samsung 35E pack (~672 Wh) more than doubles a stock M365’s 280 Wh capacity; keep throttle current intensity near 100 mA for controllable launches.[^voltage-amps]
- Swapping between 12 S and 14 S externals demands retuning Rita each time and charging higher-voltage packs off-scooter so the 10 S internal BMS never sees over-voltage.[^12s-14s-swap]
- XT30 harnesses still suffice for 13–14 S builds at current community levels, but budget time to rework Rita profiles and charger leads whenever you change voltage.[^xt30-highvoltage]
- Roughly 48 18650 cells fit a Wildman bag, enabling 14 S3 P externals, but the short runtime pushes heavier riders toward 13 S stacks or more parallels for balance.[^wildman-capacity]
- Mixing 10 S internals with 13–14 S externals works when packs charge separately and Rita is retuned each swap; skip those steps and the adapter may refuse to brake or blend current.[^mixed-series]
- Expect 500 W hubs to pull the full 32 A Xiaogen allows once larger packs are attached; start nearer 29 A on 4 P batteries, watch controller temps, then increase only if hardware stays cool.[^500w-current]
- Pro 2 owners swapping BMS 126 boards for BMS 128 units report a closer match to the scooter’s higher-capacity stock pack.[^bms128]
- A 350 W motor on a Xiaomi 1S with the OEM 10 S4 P battery already heats cells to ~40 °C in cool weather, nudging riders toward Rita-managed 12 S externals and higher parallel counts.[^350w-heat]
- Deck planning shows 13 S5 P 18650 assemblies fit a Pro without relocating electronics, while 13 S7 P or 12 S4 P 21700 builds need 20–25 mm deck extensions—map nickel layouts before ordering cells.[^deck-pack-sizing]
- Pairing a 10 S4 P 21700 internal with Denis’ external pack already yields ~65 km at 20 km/h, with ~85 km expected once the denser core is welded.[^hybrid-range]
- Wiring an internal battery without a data line keeps Rita in permanent BMS-emulator mode and still requires the pack’s own charging plug for safety.[^permanent-emulator]
- Chase full-capacity charges by flashing BMS 126 directly at the pack rather than routing through Rita when updating firmware.[^bms126flash]
- A €110 Chamrider 13 S3 P pack (≈9.6 Ah real capacity) fits Denis’ external bag and pushed a 10"/350 W build to GPS-verified 47 km/h, while Aerdu’s 10 S 14 Ah budget pack arrives without a plastic cell cage.[^chamrider-pack]
- Mixed 10 S internal + external Rita builds deliver roughly 30 km of eco riding before both settle around 36 V; update the app’s capacity estimate (e.g., 7 800 mAh stock + 10 350 mAh external = 18 150 mAh) so consumption stays accurate.[^rita-mix-range]
- Dual 12 S builds show 51–52 km/h on the dash (≈48 km/h logged), whereas single 12 S 500 W conversions cruise near 44 km/h—voltage adds speed even before a motor swap.[^dual-12s-speed]
- Stacking 1 S boosters onto a 12 S core only works when the add-on matches the original parallel count and charges separately, making 14 S conversions cumbersome compared with purpose-built 15–17 S packs.[^stacked-boosters]
- Quality packs translate into real-world range: one 13 S 9 P internal returned 35 km with over half the battery remaining, while a Rita + Aerdu 10 S 14 Ah external topped 82 km by daisy-chaining spare externals.[^range-report]
- Large-format experiments underline trade-offs—12 S 9 P 21700 builds still sag like smaller 13 S 3 P arrays, Wildman 3 L bags can host dense sideways PCB layouts, and upgraded Essential scooters at 100 kg realistically see only 8–10 km at 30 km/h.[^large-format-tradeoff]

### Charging, Diagnostics & Instrumentation

- Rita can top external packs that lack common-port BMS hardware, but protection and balancing aren’t enforced—charge those builds directly through their own port instead.[^rita-charge-warning]
- The adapter emulates −10 °C after charging and defaults to a 29 Ah capacity estimate, so dashboard gauge jumps and “missing” watt data in M365 Tools remain normal under Rita.[^rita-emulation]
- Investigate drifting parallel groups early: confirm cell authenticity and verify voltages with a multimeter before they erode usable range.[^bms-drift]
- Handheld wattmeters with XT30 leads (~€10) plus extension cables log charge/discharge current from the handlebar without upsetting KERS.[^wattmeter]
- Tear down any 12 S4 P pack showing 0.12–0.3 V sag on a single group under load—test cells individually, keep RC chargers handy, and inspect BMS traces for faults.[^pack-sag-diagnosis]
- Pin nickel with magnets, add fish paper on positive ends, and iterate weld layouts until busbars sit flush to avoid bowed strips stressing cells.[^spot-weld]
- Aerdu and similar third-party packs must offer common charge/discharge ports when paired with Rita; separate-port BMS boards demand off-scooter charging and raise regen risk even if KERS is disabled.[^common-port-rita]
- Parallel battery setups without Rita only stay safe when voltages match exactly; veterans still treat Rita as the safer long-term upgrade once budgets allow.[^parallel-risk]
- Denis keeps pointing shoppers toward his verified Samsung 35E builds (e.g., €230 13.8 Ah Wildman packs) instead of suspicious AliExpress “13 S” listings.[^trusted-packs]
- Rita firmware v5 now lands via the Google Play BMS Tool once an external battery is plugged in, spoofing −10 °C to disable KERS and needing only ~42 V telemetry to manage regen cutoff.[^rita-fw-upgrade]
- Swapping externals with the same series count needs no reconfiguration, but moving between 10 S and 12 S requires updating Rita’s series setting to avoid slow launches until voltages settle.[^series-swap]
- Third-party dashboards such as m365dash block BLE traffic during updates—disconnect them or switch to update mode before flashing Rita firmware like BLE 072.[^dash-block]
- M365dash beta firmware 2.0.9 improves 13 S reporting for Rita builds, though riders must flash the BIN via Wi-Fi and reboot the scooter to expose all 12 cell groups.[^m365dash-beta]

## Tires, Brakes & Handling

- Budget MTB-style calipers such as Bike Attitude can outperform XTECH when paired with 135 mm rotors and carefully aligned stationary pads; seasoned riders still prefer 10" pneumatic rubber for grip even if solid tires are easier to install when pre-heated.[^brake-upgrades2]
- 10" swaps need firm pressures (~3.5 bar) to reclaim 12 S speed gains; running ~36 psi saps top speed, so check fender and frame clearance after inflating.[^tire-pressure]
- Stem and handlebar experiments often require custom clamps or welded risers; relocating dashboards into bags and powering auxiliary lighting from separate packs keeps cockpit mods tidy.[^stem-mods]
- X-Tech semi-hydraulic brakes, 130–140 mm rotors, and even hydraulic bicycle kits remain community favorites, with Denis recommending Torx T10 fasteners (preferably countersunk) to keep deck plates sealed.[^brake-mix]
- Range Boost kits stay plug-and-play on Xiaomi 1S, but 12 S range + speed bundles need paid XiaoFlasher firmware and only report accurate SOC when both packs share the same series count.[^range-boost]
- 10" pneumatic conversions smooth bumps versus stock 8.5" rubber, yet true rims and optional Monorim suspension matter; riders still revert to 8.5" with Monorim V2 when S-shaped wobbles or bouncy heavy-rider feedback make 10" casings feel vague.[^tire-choice]
- X-Tech squeal on 135 mm rotors fades after clamping the caliper during pad alignment, and stem dampers need properly torqued bolts—inspect latches and hinges before blaming silicone shims.[^brake-alignment]
- Group buys continue for Monorim’s 500 W hub (~€80 shipped) because it tolerates more current without overheating and pairs well with 13 S tunes for torque gains.[^monorim-500w]
- Budget fork kits that bolt to Ninebot Max frames lift the front end nearly 10 cm; reversing the forks can clear wider custom motors on front-wheel conversions.[^fork-lift]
- Monorim’s 500 W hub expects quality 10" solid tires or mixed solid/pneumatic setups—avoid harsh 8.5" solids that crush speed and range.[^solid-fit]
- Ninebot Max experimenters say the original “Gen1/type 6” motor hits harder, while the newer “Gen2/type 9” winding runs cooler and lasts longer at the expense of some punch.[^max-motor]
- Monorim and EXA suspension wobble typically traces to worn bearings—swap the top and bottom races after about a year of heavy riding to restore stability.[^suspension-bearings]
- Heavy riders favour CST V3 or Wanda 10" tires with thick tubes; solid tires burn ~20 % more energy and still risk tube pinches during installation.[^cst-v3]
- HB100 conversions typically ship with 140 mm rotors for M365 Pro and 120 mm for the base scooter, plus spacers that centre the pads.[^xtech-rotors]

## Charging, Connectivity & Instrumentation

- Plug chargers into the scooter before the wall to reduce inrush sparks, and remember Rita automatically shares the stock charge port across both packs.[^charging-etiquette]
- External packs tolerate up to ~10 A when charged directly, but keep the scooter inlet around 2 A to avoid stressing the OEM BMS; buy a dedicated high-current brick for faster off-scooter top-ups.[^charge-current]
- Denis is prototyping an XT30-to-Xiaomi charger adapter so externals can charge independently while Rita still tops the internal pack first through the scooter port.[^xt30-adapter]
- Scooter Companion/BLE telemetry may show blank data after rides unless the external pack sits ~0.5 V above the internal pack; kill competing apps, downgrade BLE if needed, or try older Android builds.[^ble-troubleshooting]
- Rita only reports as the primary BMS when its pack voltage leads by roughly 0.5 V, so expect telemetry to toggle during mixed-charge scenarios.[^primary-bms]
- Serial access needs FTDI ground tied to Rita ground, TX on yellow, RX on white, plus a 1–10 kΩ pull-up because Rita’s TX is open-drain; power the board from any battery during configuration.[^serial-pinout]
- On clone scooters without BMS telemetry, Rita behaves like a smart diode pair—supporting only equal-series packs, requiring regen-off, and making serial tweaks optional.[^clone-behavior]
- Doc Green/ESA owners confirm Rita works in analog mode with stock harnesses, but Bluetooth telemetry demands Xiaomi dashboards and full controller/loom swaps to regain custom firmware support.[^doc-green]
- Alibaba “KCQ” clones vary widely—inspect internals for motor compatibility or sell the copy to fund a genuine Xiaomi when documentation is sparse.[^kcq]
- Repair BMS mounting holes are 4 mm, and the board remains configurable over inexpensive CP2102-class USB-UART adapters even for scooters lacking Xiaomi dashboards.[^repair-bms]
- Denis’ repair BMS slides into ESA-class clone bays without data lines, letting shops reuse analog frames or migrate customers slowly toward full Xiaomi electronics when telemetry becomes important.[^esa-bms]
- Rita still supports scooters without data-line telemetry, keeping external-pack builds viable beyond Xiaomi’s lineup.[^non-telemetry]
- Rita deliberately omits a dedicated data line to simplify wiring; external pack SOC stays hidden in M365 Tools until smart BLE BMS packs arrive, so lean on BMS apps and reseat the white–yellow–green ribbon if repair-BMS error 21 appears.[^rita-data-line]
- Fresh 12 S installs typically show ~51 V at full charge and zero-watt readings in M365 Tools—Rita’s shunt design makes the idle wattage normal even when everything works.[^zero-watt-telemetry]

## High-Voltage Upgrade Playbook

- Moving from 10S to 12S (~44 V) means flashing higher-voltage firmware, reinforcing controller power traces, and sourcing a 50.4 V charger; expect ~36 km/h, ~800 W, and ~50 km range with an auxiliary pack afterward.[^twelve-s-steps]
- Unlocking the hardware speed limit for 12 S adds danger—keep firmware-limited speeds near 34 km/h even though riders report 38.5 km/h on stock frames.[^speed-limit]
- Rita ships with XT30 harnesses (XT60 shells do not fit), caps current near 30 A (~1.5 kW at 13 S), and still expects users to align pack voltages before running dual externals or bumping to 13 S builds.[^rita-harness]
- Denis tells 13 S experimenters to cut Rita’s pink sense lead, keep the XT30 connector, and remember 12 S already delivers tangible performance without extra charger headaches.[^pink-lead]
- 10S packs house 40 cells compared with 36 in Denis’ 12S3P builds, so endurance-focused riders should not dismiss denser 10S options.[^ten-s-cells]
- Higher pack voltage raises achievable speed, but torque still depends on available current and coil resistance—capacity only extends runtime when the cells can supply the amps your tune demands.[^voltage-vs-torque]
- Enthusiasts debating star/delta rewiring on Ninebot Max motors noted delta mode can unlock 50–60 km/h at 36 V, but it requires meticulous switching hardware and beefier controllers to offset the torque loss per amp.[^star-delta]
- Reinforced VTA controllers can stretch to 13 S once Rita’s jumper is cut, with riders reporting 45–50 km/h “in air” on 10" tires—stage firmware flashes carefully to avoid over-voltage boot loops.[^vta-13s]
- Xiaomi’s 1S Range Boost kit remains plug-and-play at 10 S, whereas the 12 S Range+Speed bundle needs a paid XiaoFlasher unlock and only reports accurate SOC when both packs share the same series count; expect ≈51 V full-charge readings, zero-watt telemetry, and remember motors overheat before quality batteries do if you hammer low packs with extra current.[^range-kit-compat]

## Ride Planning & Etiquette

- A Rita-equipped M365 roughly multiplies range 2.8× on base models and 2.1× on the Pro, letting 130 kg riders cover 24 km commutes when they plan higher-capacity packs and voltage matching before paralleling.[^range-multiplier]
- Ride defensively at 30–40 km/h—use wide bike lanes, signal predictably, and watch driveways; the crew argues behavior matters more than hard 20 km/h limits once scooters mix with cars and cyclists.[^defensive-habits]
- Cold autumn temperatures immediately induce extra voltage sag even if you depart with a warm pack, so expect reduced punch as ambient temps fall.[^cold-sag]
- UK riders still face penalties (points, fines, impounds, higher insurance) for private scooters on public roads, so keep upgrades discreet and riding behavior compliant.[^uk-legal]

## Logistics & Community Updates

- Shipping lithium packs to markets like the UK and Australia remains tough; Tudor fills some UK demand with local fabrication while others push legalization petitions to ease import barriers.[^shipping-uk2]
- Germany still enforces 20 km/h caps and insurance requirements, and French police continue catching up on scooter laws—builders hide modifications and ride conservatively to avoid fines.[^legal-de-fr]
- Import math often favors regional resellers: direct China orders rack up ~$40 shipping plus ~€20 customs per motor with multi-week waits, and shipping two 1200 W hubs privately can cost $300–350 before duties.[^import-math]
- Mid-February updates highlighted national safety recalls, 22 mm steering-tube measurements for bar swaps, and renewed reminders to wear proper gear once scooters top 50 km/h.[^safety-recall]
- UK customers still face paused kit shipments amid EU paperwork and global cell shortages—both NKON and UK warehouses ran dry while Tudor quoted bespoke 48 V/25 Ah packs for upcoming weeks.[^uk-pause]
- Denis flagged that regular-post parcels bound for the UK or France after 28 October stalled in transit, so riders should expect delays or spring for UPS shipping.[^uk-delay]
- The refreshed M365 Tools/Rita app hit Google Play in mid-December, giving Pro 2 owners an official download while Denis reiterated he cannot ship complete battery kits outside the EU (e.g., Qatar).[^m365tools-release]
- Tudor can now ship batteries to the US via UPS with customs invoices starting January 2021 and continues stocking cable grommets, brackets, and silicone plugs for tidy deck routing.[^ups-us]
- Denis reminds riders that the Range kit roughly doubles mileage even for 120 kg commuters and that 30–35 km/h cruising is plenty once weather and policing realities sink in.[^range-etiquette]
- Community members trade STL files for 20 mm deck extenders, warn against nordbot.xyz packs, and leverage planning tools like repackr and e4bike before welding custom layouts.[^stl-sharing]

## Accessories, Fabrication & Safety

- Stick-on hub “coolers” are cosmetic—real gains come from better thermal conduction and controller reinforcement once riders chase ~850 W or more.[^hub-coolers]
- Riders secure Xiaomi stems with plastic shims or aftermarket locks such as Foldster Xlock/Phoenix kits; align Denis’ battery-bag brackets carefully to avoid deck scratches or lever punctures.[^stem-locks]
- Scale printable spacers per axis before printing—one rider shrank a 23 mm extender to 10 mm—while sealing LED strips, RGB diffusers, and ESP32/8266 controllers inside housings for weatherproof lighting.[^prints-lighting]
- Pairing two 6 S LiPo packs in series for 12 S requires a proper BMS and dedicated 12 S charger; running bare RC LiPos from a 10 S charger is a fire risk for novices.[^lipo-warning]
- Denis still recommends 10S4P Samsung 35E packs with common-port BMS boards; source cells from NKON or trusted builders instead of gambling on AliExpress listings, and budget lab-grade tools if you insist on vetting cheap packs yourself.[^pack-rec]
- When ordering UART/Bluetooth BMS boards, grab the full UART485 adapter kit to cover both wired configuration and wireless telemetry.[^uart-kit]
- BMS v3.0 (green EU edition) removes the fragile thermal fuse—expect identical hardware otherwise, but note the pack will not self-isolate during thermal runaway.[^thermal-fuse]
- Charge through the scooter port at ~2 A because the internal BMS handles that flow, while external packs can accept ~10 A directly—buy 3 A+ chargers for off-scooter charging.[^charge-current]
- Inspect pack assembly quality: reserve fishpaper rings for positive terminals, avoid damaged sleeves or glued insulation donuts on negatives, and use elastic adhesives plus wide power nickel with thin balance strips to fit Wildman cases cleanly.[^pack-inspection]
- Custom 12S4P builds mix wide nickel busbars for discharge paths with narrow balance strips, while production 12S3P packs remain tailored to Wildman bag dimensions.[^pack-layout]
- Opening factory battery cases still requires brute force—expect to pry or “hammer” packs loose and reference chat archive photos for BMS wiring layouts before resealing.[^bms-disassembly]
- Re-route rear-light harnesses, seal deck seams with epoxy, hot-glue the tail-light connector after 10" conversions, and maintain ~4 bar rear/3.5 bar front pressures to keep relocated wiring from catching road spray or rubbing tires.[^rear-wiring]
- High-mount indicators on helmets or backpacks stay visible in daylight, and reflective tape or budget sticker kits add conspicuity without bulky lighting modules.[^high-mount-signal][^rear-tape]
- 3D-printed fender supports with integrated mudguards, wireless turn-signal pods, Lumos Matrix helmets, and DIY 12 V strobes provide cheaper conspicuity upgrades than the €240 official kit while riders wait on affordable MIPS offerings.[^lighting-diy]
- Dual 12 S packs (~24.6 Ah, 6.1 kg) ride in backpacks via anti-spark jumpers or multi-pack Rita adapters when riders need 80 km range.[^dual-pack-range]
- Trim folding hooks or add Monorim extenders and X-Lock risers so Wildman bags clear the latch without gouging packs; Foldster and other lock extenders still open space while calming ESA clone stem wobble.[^foldster-clearance]
- Bag mounting hacks favor hardware over printed brackets—bolt triangle frame bags on with U-bolts and internal wood or metal plates so heavy batteries stay braced against theft and road shock.[^bag-mount]
- Bluetooth temperature loggers powered by CR2032 cells give cheap live data when stress-testing packs and controllers.[^bt-logger]

## Logistics & Warranty Updates

- Denis’ new workshop has limited mains capacity, so he is exploring DC welders or backup generators to avoid tripping breakers during production.[^workshop-power2]
- BMS warranties remain strict after a missed balance strip incident—Rita units stay covered because they are harder to miswire, but BMS buyers must prove installer innocence.[^bms-warranty2]
- Shipping reopened to Serbia via Polish Post with card payments, Denis scheduled early-September dispatches on the 8th and 14th around a short holiday, and London riders can source hardware via @Kvarkas for roughly €207 delivered on 12 S packs.[^shipping-updates]
- Stepping up to 21700 or 26650 formats fits 12 S4 P energy in a 2 L bag but crowds wiring; riders treat bag volume—not cell chemistry—as the limiter for ultra-long-range experiments.[^large-format]

## Pricing & Bundles

- Complete Rita + bag + battery kits price in the €250–€280 band plus roughly €20 shipping depending on charger inclusion, reflecting low-volume assembly with branded components.[^pricing]
- Denis’ standalone 10S4P pack runs about €170 with Wildman bags around €30 and shipping near €20, pricing driven by Samsung 35E cells, 20 A BMS boards, and genuine XT30 hardware sized for the Xiaomi inlet.[^pack-pricing]
- Late-summer 2020 quotes landed near £290 delivered for 12S kits to the UK and about €325 to Finland, with no additional VAT within the EU customs zone.[^regional-pricing]
- The Range + Speed bundle ships with a 50.4 V brick that tops both batteries sequentially; splitting the packs across chargers finishes faster while keeping BMS thermals comfortable.[^range-speed-charging]

## Fulfillment & Lead Times

- Adapters ship worldwide, but lithium packs stay EU-only because Denis relies on ground carriers; US buyers must self-source packs, Israeli riders are routed to partner builders, and he experiments with UPS options for markets like Kuwait while offering electronics-only deliveries to regions such as Norway or Turkey.[^shipping-scope]
- Production runs ship in weekly batches (e.g., 30 adapters, 15 bags, nine batteries), with typical EU door-to-door timelines around 10 days and three-day deliveries from Poland once regional stock depots are replenished.[^batching]
- Battery assembly lead times fluctuate around two to three weeks when charger inventory tightens; 12S chargers resumed after supplier holidays, and by mid-August he quoted three business days to build a pack.[^lead-times]
- Charging telemetry continues after the scooter powers down—expect the dash to hover near 99 % until the external pack balances, so rely on charger LEDs or the Rita app for confirmation.[^charging-telemetry]
- EU buyers report three-day deliveries from Poland and note Denis’ 12 S packs ship with YZPower chargers rated for 20 A continuous discharge that tolerate short bursts above spec.[^logistics-20a]
- Shipping hazardous goods remains a compliance exercise: Denis’ crew warns that every lithium shipment must be declared and certified under EU ADR/IATA rules with proper paperwork and, in many jurisdictions, a contracted safety advisor—undeclared packs leave senders on the hook for six-figure liabilities if a parcel ignites.[^hazmat]
- Polish Post now carries electronics and packs to Serbia again, and London buyers can source Rita hardware locally via reseller @Kvarkas while UK 12S kits land around €207 after his early-August backlog clears.[^serbia]
- The main workshop recently moved to a space with limited mains power, so Denis is evaluating DC welders and backup generators to keep pack production online without tripping breakers.[^workshop-power]
- Payments still route through Denis’ Russian business—PayPal/eBay remain disabled, card processors can stall orders, and staff manually confirm transfers until banking access improves.[^rub-only]
- Battery production paused 1–10 August while his pack builder vacationed and chargers caught up; orders placed in that window resumed shipping around mid-month.[^aug-pause]

## Support & Documentation

- Denis maintains installation guides for Rita, external batteries, and repair BMS builds on his storefront to avoid marketplace fees and centralize support.[^docs]
- Community members loan ST-Link programmers around the workshop chats and remind newcomers the tools are cheap locally, so keep one on hand for 1S/Pro 2 dashboard recoveries instead of waiting on mail-order replacements.[^stlink-loaner]
- He keeps sales off eBay/PayPal to dodge the ~20 % marketplace fee and associated chargeback exposure, steering buyers to m365.embedden.com where those guides live alongside the order form.[^storefront]
- Customers are urged to include order IDs in support tickets while Denis manually reconciles payments during banking or payment-processor outages.[^support-ops]
- Rita MAX remains on the roadmap as the variant that natively understands Ninebot Max voltage reporting; legacy hardware will need adapters if riders migrate to that platform.[^rita-max]
- BMS coverage is deliberately strict: Rita units stay warrantied because they are harder to miswire, but standalone BMS buyers must prove faults aren’t installer-induced, and Denis keeps sales off PayPal/eBay to avoid anti-seller chargebacks.[^bms-warranty]
- Rita + Speed kits run on Xiaomi Pro 2 scooters with paid XiaoFlasher firmware, but the platform still cannot connect to the M365 BMS Tool so configuration relies on alternate apps.[^pro2-config]
- Miswired externals that pop Rita’s fuses are treated as owner error—verify common-port wiring before shipping hardware back, and remember the M365 BMS Tool still expects BLE 072/090 with telemetry flipping to whichever pack leads by ~0.5 V.[^support-boundary]

## Integration & Maintenance Highlights

- Happy BMS coulomb counters peg at 0 % once ~32 Ah flows; a 35 A external still leaves roughly 10 % energy, so plan range manually even though Rita keeps current inside its limit.[^happy-35a]
- Rita-compatible emulators still call packs “empty” around 3.4 V per cell despite lower cutoff settings—maintain manual voltage checks or leave a buffer when riding on emulation alone.[^emulator-34v]
- Cutting deck vents for PC fans adds water-ingress risk without real cooling; the crew leaves the chassis sealed and relies on thick thermal pads or full VESC swaps for sustained 80 km/h builds.[^fan-mod-risk]
- AliExpress “fire emoji” packs often hide laptop pulls—Denis caps Happy BMS builds near 53 V/40 A and steers riders toward refurbished OEM modules instead of forcing Rita past spec.[^ali-pack-warning]
- Xtech hybrids fade fast on 80 km/h conversions; swap to full hydraulics with dedicated brake sensors so regen stays available without killing lever feel, then bleed hoses after final trimming.[^hydraulic-upgrade]
- XiaoDash or DownG restores serial numbers and odometers wiped by recent flashes; reserve ST-Link reflashes for riders who truly need lifetime mileage restored.[^serial-reset]
- Rear ride-height tweaks use bolt extenders and auxiliary springs so flipped forks or aftermarket suspensions sit level without over-compressing the stock shock.[^suspension-extender]
- Accessory loads on external packs tolerate KERS regen, but flaky “purple” dashboards sag throttle voltage with lights on, capping speed until the dash is replaced.[^accessory-dash]
- Disable traction control on slick surfaces for high-power AWD builds—Roscheeee’s VESC G30 snapped Tronic controllers when TCS dumped an estimated 250 A back through the system.[^tcs-hazard]
- Deck space and cooling make bolt-on dual-motor helpers impractical; serious AWD conversions need matched motors, dual controllers, and proper heat sinking rather than ad-hoc add-ons.[^dual-motor-plan]
- Opening Xiaomi packs requires slicing both lower seams, warming the adhesive, drifting the brick out, and testing CF-series capacitors for infinite resistance during imbalance diagnostics.[^pack-teardown]
- Running externals without Rita still needs a Xiaomi BMS or XiaoDash emulation—simple smart-BMS boards lack the data line and trigger error 21.[^no-rita-emulation]
- Burned hubs that screech after steep 33 A climbs typically have cooked slot insulation—swap in hall-sensored Blade 10 or Vsett 10+ motors instead of forcing sensorless Vsett 11+ units on Xiaomi controllers.[^63]
- Xiaomi V3 controllers tolerate 13S packs without hardware swaps, but Denis’ crew replaces Kapton strips with 0.5 mm thermal pads and direct-solders phase leads to keep MOSFETs cool on higher-current tunes.[^controller-thermals]
- Keep sport-mode peaks near 25–26 A and favor linear throttle curves with 100–200 mA steps—the Xiaogen 0.005 s/300 mA coefficient shows 800 mA steps only add stress and heat without real launch gains.[^throttle-steps]
- Let external packs climb to ~50–51 V before rides, lift recuperation-disable thresholds to ~4.150 V, and raise power-constant values toward 33 000–40 000 to cool controllers; low constants hit harder but overheat 12 S builds.[^power-constant]
- Rita’s 25 A ceiling limits the torque boost from tiny external packs; for long hill climbs riders step up to dual motors or uprated controllers rather than forcing more current through the adapter.[^rita-hill]
- Dual-dash AWD builds treat Rita as the master: tie controller grounds together, forward a single data lead to the slave dash, and investigate any Error 14 immediately because it signals cross-pack leakage the adapter should block.[^awd]
- Treat a sudden Error 14 or 21 on a secondary dash as a wiring or polarity fault—Denis warns it means packs are backfeeding and the scooter should stay parked until the harness and BMS are rechecked.[^error14]
- XiaoFlasher’s 13 S BMS emulator can add throttle lag, whereas Rita’s emulation keeps instant response when blending large internal packs with the stock dashboard.[^xiaoflasher]
- Recurrent thermal shutdowns after a Rita upgrade usually trace to dried controller paste; replace compound (not pads) and monitor logs before pushing harder firmware—quality paste between the deck and controller can add 4–5 km/h at the same amps while keeping temps under ~45 °C.[^thermal-paste] If temps spike immediately after the install, dial back Sport-mode amps and watch motor heat until the tune settles.[^heat-spike]
- Use non-conductive thermal compound between MOSFETs and controller housings to boost heat transfer without risking shorts on the power stage.[^nonconductive-paste]
- Tally charge time when evaluating third-party packs: the stock 1.7 A Xiaomi brick adds roughly 1.7 Ah per hour, so a genuine 12 Ah module should take close to seven hours from empty.[^64]
- Refresh high-load builds regularly: even reinforced controllers run warm at 24–29 A when hauling ~150 kg, so keep thermal paste fresh and monitor temps on extended climbs.[^heavy-load-heat]
- Break stuck front-hub bolts loose with a long, rigid wrench plus penetrating lube while bracing the scooter—replace any rounded hardware with higher-grade fasteners.[^front-bolts]
- Monorim steering that binds after install usually needs the centre stem bolt backed off a quarter turn and the side clamps loosened before reinserting the suspension pump.[^monorim-bind]
- Quiet Monorim pivots with bicycle-grade lithium grease instead of light oils; the heavier lube also seals out water better on daily commuters.[^monorim-grease]
- Water-damaged controllers usually lose their 5 V rail; probe the dash socket, inspect the U4 buck regulator, and reseal every cable entry with silicone once repairs finish.[^water-diagnostics]
- 10" conversions often relocate rear-light wiring, reseal the deck, and may require trimming plastics; heavier riders keep the deck rib intact while lighter owners sometimes shave it for tire clearance.[^deck-rib]
- Stripped deck threads accept the next size up (e.g., M3.5×10 mm) because the stock baseplate aluminum is soft enough to recut new threads.[^deck-threads]
- Relocate charge ports higher on the stem and reseal openings once Wildman bags and 10" tires go on to keep grit out of the deck.[^charge-port-relocate]
- LM2576HV or LM2596HV buck converters survive scooter pack voltage when powering 5 V accessories; Denis quotes roughly three business days to assemble a fresh battery batch once parts land.[^buck-hv]
- Freshly charged 12S4P packs can spike toward 50 °C on hard hill climbs—ease firmware demand, let packs rest after charging, or finish the 50.4 V charger mod before hammering them.[^12s4p-temp]
- Adjust DIY charger trimmers to 50.4 V and avoid sloppy soldering or silicone substitutes like wood glue, which can cook the brick before it reaches Rita.[^charger-trim]
- Expect the scooter to rest a few tenths below full charge because Rita deliberately undercharges the internal pack to preserve regen margin; treat buzzing motors or error 39 beeps as signs to dial battery current back under the adapter’s 25 A ceiling.[^rita-undercharge]
- Rita keeps topping the external pack after the scooter powers down—trust the charger LED (green = full) rather than assuming charging stopped with the dash.[^rita-finish]
- Rita’s Schottky charge diode drops roughly 0.6 V, so stock packs plateau around 97 % unless you bypass the adapter during off-scooter charging; Denis prefers the mild undercharge for longevity and regen headroom.[^rita-schottky]
- Mixed 10S/12S stacks still charge through the scooter inlet with Rita prioritising the lower-voltage pack first; pushing 54.6 V directly into the internal battery leaves only its BMS as over-voltage protection, so reserve high-voltage bricks for Rita-managed sessions.[^sequential-charging]
- High-voltage experiments around 60 V still demand staged launches, BLE firmware checks, and careful thermal monitoring since Rita enforces its own limits even when the drivetrain can pull harder.[^rita-60v]
- Expect Rita to draw a small standby current—packs left connected for months drift toward empty, so recharge to storage voltage every few weeks instead of leaving the adapter plugged in indefinitely.[^65]
- A small Gen 4 batch under-reported output above ~20 A; cross-check logs against stock wiring and lean on Rita’s redundant current sensing if you suspect phantom throttling.[^rita-underreport]
- Dashboard state-of-charge becomes unreliable once Rita blends packs—Denis tells riders to treat ~50 % on the display as the cue to head home and verify voltage inside the app instead.[^rita-soc]
- Gen 4 harness staging matters: route Rita’s potted balance leads along the controller side, keep the three-way charge splitter inline even if the port relocates, and only cut the gray surge jumper when stepping beyond 12 S packs.[^harness_staging]
- Reconfigure Rita every time you swap between 10 S and 12 S externals; mismatched settings can disable regen or blow the adapter, and externals must sit a few tenths of a volt above the internal pack for telemetry to register.[^rita-reconfig]
- Expect mixed-pack builds to start drawing from both batteries once a 12 S external falls near 41 V, effectively leaving about a stock pack’s worth of range after 30 km of spirited riding.[^mixed-pack-range]
- BMS Tool firmware v5 adds regen over-voltage protection but requires a 4.180 V recovery limit the app cannot expose yet, so Denis paused public downloads and ships new units preloaded instead.[^bms-tool-v5]
- Misconfigured dashboards that still show 100 % near 41 V betray Rita units left in 10 S mode—disable strong KERS and reflash the adapter before warranty replacements are considered.[^dash-100]
- Never cut both XT30 leads simultaneously when soldering harnesses, and keep spare connectors ready for full-pack rebuilds to avoid shorts mid-repair.[^xt30-safety]

### Battery Care & Firmware Fundamentals

- Top-balance severely unbalanced Xiaomi packs with TP4056 modules and crocodile clips without disconnecting the BMS, working group by group until voltage spreads close.[^tp4056]
- Downgrade Xiaomi dashboards to BLE 073 when the M365 BMS Tool stops responding; the version still supports custom firmware after configuration.[^ble073]
- Repair BMS units ship today as 10S4P with a 12S variant targeted for August 2020, and Denis still quoted one-to-two-week deliveries to Belgium despite pandemic slowdowns.[^bms-roadmap][^bms-belgium]
- Treat Rita as a 30 A adapter: place anti-spark switches between Rita and the controller so charge routing stays intact, and avoid chasing >1 kW tunes that overheat the module or lean on mismatched packs.[^rita-current-limit][^anti-spark]
- Configure 12 S builds by raising Rita’s series count and recuperation ceiling to ~4.15 V per cell—lower thresholds trigger throttle kicks on 12 S/13 S packs—and disable KERS if settings are uncertain to prevent regen spikes from cracking the adapter.[^rita-12s-config][^recup-throttle]
- Retune chargers for 12 S work by stacking ~14.3 kΩ feedback resistors in the stock brick or moving to 50.4 V CC/CV supplies like Mean Well’s ELG-240-48A—sourcing Xiaomi’s coaxial plug is often the hardest part of the upgrade.[^charger-upgrade]
- Upgrade mechanical brakes alongside 12 S packs because the higher voltage pushes flat-ground speeds toward 40 km/h.[^brake-upgrade]
- Dismiss implausible “13S4P 60 Ah” batteries and stick with reputable 12 S suppliers to avoid fire-risk chemistries and mystery BMS limits.[^fake-60ah]
- Waterproof commuters should seal deck seams, charge doors, and hub interfaces with silicone and lithium grease before riding in sustained rain.[^rain-proof]
- Keep an ST-Link v2 handy and plan to double-flash firmware packages because Bluetooth installs can soft-brick controllers; third-party dashboards must be unplugged or placed in “update mode” so Rita can talk on the data line.[^stlink][^dash-update]
- Leave Face LTD throttle-step settings near the 600 mA default on stock controllers; pushing 800 mA on unreinforced boards overheats traces, so cap virtual battery current near 25 A.[^face-ltd]

## Risks & Watchlist

- Jumping to 13S requires cutting Rita’s sense jumper, reinforcing controllers, and following the manual via the M365 BMS Tool; reverting without restoring the jumper is unsafe.[^thirteen-steps]
- High-power firmware tunes above ~1 kW or aggressive regen profiles can overheat motors and burn MOSFETs unless paired with controller trace reinforcement and mechanical brake upgrades.[^power-risks]
- Avoid heavy CWF W-style regen presets on unreinforced controllers—emergency stops at those levels can burn traces within a few pulls.[^regen-limit]
- Stock Pro harnesses start melting near 29 A on factory connectors, so stay ≤27 A on OEM wiring or hard-solder phase leads before chasing higher numbers.[^connector-melt]
- Treat Rita’s 30 A ceiling as a hard limit; mechanical brakes remain the primary stopper and chasing 40 A bursts risks snapping 180 A MOSFET legs during panic stops on 500 W builds.[^rita-brake-limit]
- Older Rita revisions lack modern surge clamping—treat charger relocations carefully, keep the three-way splitter inline, and respect the adapter’s 25 A ceiling to avoid repeated error beeps or melted harnesses.[^legacy-boards]
- New Rita over-voltage guards still depend on healthy BMS hardware; relocating charge ports without the required splitter blinds the adapter to charger events and removes those protections.[^rita-v4]
- Using Xiaomi packs as ad hoc chargers without proper current limiting remains a fire risk—Denis instead repurposes them as externals with their own BMS and keeps charge circuits separated.[^pack-charger]
- Miswired balance leads have popped Daly smart boards instantly—wire negatives first, confirm each cell step with a meter, and avoid doubling sense wires on the same pad.[^balance-leads]
- Parallel packs without Rita risk bypassing their BMS safeguards—only join equal-voltage packs and enable permanent BMS emulation when the scooter lacks a smart data line.[^parallel-risk]
- LiFePO₄ BMS boards cannot safeguard li-ion packs; return the part or build a dedicated chemistry match instead of forcing it into 12 S scooter builds.[^lifepo4]
- Pairing 12 S externals still demands keeping firmware nominal voltage around 51 V so Rita’s limits align—forgetting the setting after a pack swap risks overcharging or limp modes.[^twelve-s-config]
- Series booster packs (2–3 S) must be charged separately to match the internal battery exactly; any imbalance forces uncontrolled cross-charging and is a strong argument for buying another Rita instead.[^series-boosters]
- “Powercube” 3S boosters push Xiaomi 1S packs beyond 56 V; without reinforced controllers and disabled KERS, regen spikes cook the MOSFETs—Denis steers riders toward proper 13 S upgrades instead.[^66]
- Treat 84 V ambitions cautiously—disable regen and migrate to 11-inch frames before chasing ~70 km/h on Xiaomi decks, otherwise the stock controller eventually blows from voltage spikes.[^34]
- Skip fan-and-hole cooling mods on Xiaomi decks; cutting vents adds water ingress without meaningful heat reduction unless thick thermal pads tie MOSFETs to the chassis.[^67]
- Stacking 2 S boosters on stock 10 S batteries spikes voltage toward 54.6 V and regularly blows Xiaomi ESCs unless the frame, controller, and wiring are heavily reinforced—stick with properly configured Rita builds instead of “shitty cell” add-ons.[^68]
- Water intrusion that triggers error 28 usually means a shorted MOSFET bridge; corroded controllers get replaced rather than debugged, and the white battery plug needs thorough cleaning before the scooter returns to wet service.[^69]
- Extreme Monorim spacer stacks (40–55 mm shocks) punch decks and twist geometry unless stainless plates or repurposed arms spread the load—inspect suspension hardware frequently on tall builds.[^70]
- Happy BMS sustains about 44 A and pops fuses near 60 A, so there’s no hidden headroom for 50–60 A experiments without redundant protections.[^happy-fuse]
- 9.5-inch solid tires stay on the shelf: veterans report harsh, unsafe handling and upgrade to PMT or Wanda tubeless casings with proper sealant instead.[^71]
- Waterlogged motors need stripping, resoldered phase joints, and neutral-cure RTV insulation before reuse—otherwise the next puddle cooks the replacement controller.[^72]
- There’s no cheap path to a reliable 60–70 km/h scooter; Denis points speed chasers toward reinforced Vsett 10+/GT2-class builds after seeing Dualtron sealing and suspension failures stack up.[^73]
- Kapton tape shrugs off moisture but lacks thermal shielding—high-discharge packs still need fish paper or other insulation, especially after seeing 2020 Dualtron Ultras shipped with bare nickel rubbing cell cans.[^74]
- Serial “speed” boosters backfeed low-voltage externals through the negative pole and cook cells; commission a proper 13 S internal upgrade instead of mixing mismatched packs.[^75]
- A scorched Xiaomi charge jack often traces to tired 24 AWG leads—refresh the short harness whenever plastic softens before assuming the port failed.[^76]

---

## Source Notes

[^rita-12s6p]: Source: knowledge/notes/all_part01_review.md, L608 to L608
[^rita-fuse]: Source: knowledge/notes/all_part01_review.md, L619 to L619
[^rita-cold-warning]: Source: knowledge/notes/all_part01_review.md, L640 to L640
[^rita-bms-tool]: Source: knowledge/notes/all_part01_review.md, L639 to L639
[^rita-charge-lead]: Source: knowledge/notes/all_part01_review.md, L641 to L641
[^rita-relay]: Source: knowledge/notes/all_part01_review.md, L642 to L642
[^rita-analog-safeguard]: Source: knowledge/notes/all_part01_review.md, L643 to L643
[^awd-roll]: Source: knowledge/notes/all_part01_review.md, L688 to L688
[^xiaoflasher-priority]: Source: knowledge/notes/all_part01_review.md, L601 to L603
[^vta-sn]: Source: knowledge/notes/all_part01_review.md, L637 to L637
[^1s-12s]: Source: knowledge/notes/all_part01_review.md, L638 to L638
[^xiaogen-migrate]: Source: knowledge/notes/all_part01_review.md, L668 to L668
[^lite-12s]: Source: knowledge/notes/all_part01_review.md, L669 to L669
[^rita-v5-v6]: Source: knowledge/notes/all_part01_review.md, L670 to L670
[^11s-firmware]: Source: knowledge/notes/all_part01_review.md, L671 to L671
[^13s-controller]: Source: knowledge/notes/all_part01_review.md, L605 to L605
[^vta-wiring]: Source: knowledge/notes/all_part01_review.md, L617 to L617
[^monorim-awd]: Source: knowledge/notes/all_part01_review.md, L618 to L618
[^stock-12s]: Source: knowledge/notes/all_part01_review.md, L620 to L620
[^controller-heat-65c]: Source: knowledge/notes/all_part01_review.md, L621 to L621
[^16s-risks]: Source: knowledge/notes/all_part01_review.md, L654 to L654
[^xiaogen-target]: Source: knowledge/notes/all_part01_review.md, L655 to L655
[^monorim-1000w]: Source: knowledge/notes/all_part01_review.md, L652 to L652
[^tudor-13s-cap]: Source: knowledge/notes/all_part01_review.md, L684 to L684
[^voltage-vs-sag]: Source: knowledge/notes/all_part01_review.md, L685 to L685
[^magnet-fatigue]: Source: knowledge/notes/all_part01_review.md, L686 to L686
[^star-delta-risk]: Source: knowledge/notes/all_part01_review.md, L687 to L687
[^monorim-48v-rating]: Source: knowledge/notes/all_part01_review.md, L689 to L689
[^17s-requirements]: Source: knowledge/notes/all_part01_review.md, L676 to L676
[^cable-disc-tuning]: Source: knowledge/notes/all_part01_review.md, L602 to L602
[^xuancheng-10in]: Source: knowledge/notes/all_part01_review.md, L624 to L624
[^frame-clearance]: Source: knowledge/notes/all_part01_review.md, L625 to L625
[^monorim-solid-heat]: Source: knowledge/notes/all_part01_review.md, L626 to L626
[^mudguard-clearance]: Source: knowledge/notes/all_part01_review.md, L627 to L627
[^brake-hydraulic]: Source: knowledge/notes/all_part01_review.md, L628 to L628
[^monorim-air]: Source: knowledge/notes/all_part01_review.md, L658 to L658
[^konyk-suspension]: Source: knowledge/notes/all_part01_review.md, L659 to L659
[^tire-10x3]: Source: knowledge/notes/all_part01_review.md, L692 to L692
[^monorim-valve]: Source: knowledge/notes/all_part01_review.md, L693 to L693
[^stem-play-fix]: Source: knowledge/notes/all_part01_review.md, L694 to L694
[^bell-hook]: Source: knowledge/notes/all_part01_review.md, L695 to L695
[^tire-maintenance]: Source: knowledge/notes/all_part01_review.md, L696 to L696
[^cold-charge]: Source: knowledge/notes/all_part01_review.md, L606 to L606
[^heater-selfheat]: Source: knowledge/notes/all_part01_review.md, L607 to L607
[^15s-sourcing]: Source: knowledge/notes/all_part01_review.md, L609 to L609
[^liitokala-warning]: Source: knowledge/notes/all_part01_review.md, L610 to L610
[^blue-led-reset]: Source: knowledge/notes/all_part01_review.md, L611 to L611
[^thermal-harness]: Source: knowledge/notes/all_part01_review.md, L612 to L612
[^pcb-varnish-tip]: Source: knowledge/notes/all_part01_review.md, L613 to L613
[^thermal-consumables2]: Source: knowledge/notes/all_part01_review.md, L614 to L614
[^50e-35e]: Source: knowledge/notes/all_part01_review.md, L677 to L677
[^pack-burnout]: Source: knowledge/notes/all_part01_review.md, L649 to L649
[^laptop-cells]: Source: knowledge/notes/all_part01_review.md, L678 to L678
[^lipo-bms]: Source: knowledge/notes/all_part01_review.md, L679 to L679
[^rita-app-monitor]: Source: knowledge/notes/all_part01_review.md, L672 to L672
[^chamrider-pack]: Source: knowledge/notes/all_part01_review.md, L646 to L646
[^rita-mix-range]: Source: knowledge/notes/all_part01_review.md, L647 to L647
[^dual-12s-speed]: Source: knowledge/notes/all_part01_review.md, L648 to L648
[^stacked-boosters]: Source: knowledge/notes/all_part01_review.md, L675 to L675
[^range-report]: Source: knowledge/notes/all_part01_review.md, L680 to L680
[^large-format-tradeoff]: Source: knowledge/notes/all_part01_review.md, L681 to L681
[^shipping-uk2]: Source: knowledge/notes/all_part01_review.md, L631 to L631
[^legal-de-fr]: Source: knowledge/notes/all_part01_review.md, L632 to L632
[^import-math]: Source: knowledge/notes/all_part01_review.md, L662 to L662
[^safety-recall]: Source: knowledge/notes/all_part01_review.md, L663 to L663
[^uk-pause]: Source: knowledge/notes/all_part01_review.md, L699 to L699
[^bag-mount]: Source: knowledge/notes/all_part01_review.md, L700 to L700

[^sintered-pads]: Source: knowledge/notes/all_part01_review.md, L501 to L501
[^rotor-pattern]: Source: knowledge/notes/all_part01_review.md, L502 to L502
[^monorim-adapter]: Source: knowledge/notes/all_part01_review.md, L503 to L503
[^solid-removal]: Source: knowledge/notes/all_part01_review.md, L504 to L504
[^deli-routing]: Source: knowledge/notes/all_part01_review.md, L505 to L505
[^stem-adapter]: Source: knowledge/notes/all_part01_review.md, L506 to L506
[^frame-foam]: Source: knowledge/notes/all_part01_review.md, L507 to L507
[^monorim-vibration]: Source: knowledge/notes/all_part01_review.md, L508 to L508
[^controller-fasteners]: Source: knowledge/notes/all_part01_review.md, L509 to L509
[^oil-cooling]: Source: knowledge/notes/all_part01_review.md, L510 to L510. Source: knowledge/notes/all_part01_review.md, L586 to L586
[^rita-priority]: Source: knowledge/notes/all_part01_review.md, L513 to L513
[^voltage-amps]: Source: knowledge/notes/all_part01_review.md, L514 to L514
[^12s-14s-swap]: Source: knowledge/notes/all_part01_review.md, L515 to L515
[^xt30-highvoltage]: Source: knowledge/notes/all_part01_review.md, L516 to L516
[^wildman-capacity]: Source: knowledge/notes/all_part01_review.md, L517 to L517
[^mixed-series]: Source: knowledge/notes/all_part01_review.md, L518 to L518
[^500w-current]: Source: knowledge/notes/all_part01_review.md, L519 to L519
[^downg-workflow]: Source: knowledge/notes/all_part01_review.md, L522 to L522
[^pro2-downgrade]: Source: knowledge/notes/all_part01_review.md, L523 to L523
[^ios-android]: Source: knowledge/notes/all_part01_review.md, L524 to L524
[^ble074-stable]: Source: knowledge/notes/all_part01_review.md, L525 to L525
[^vta-esc]: Source: knowledge/notes/all_part01_review.md, L526 to L526. Source: knowledge/notes/all_part01_review.md, L533 to L533
[^tudor-express]: Source: knowledge/notes/all_part01_review.md, L527 to L527
[^wattmeter]: Source: knowledge/notes/all_part01_review.md, L528 to L528
[^rita-dark]: Source: knowledge/notes/all_part01_review.md, L534 to L534
[^ble074-v7]: Source: knowledge/notes/all_part01_review.md, L535 to L535
[^series-booster-sag]: Source: knowledge/notes/all_part01_review.md, L536 to L536
[^rita-overvoltage-match]: Source: knowledge/notes/all_part01_review.md, L537 to L537
[^bms128]: Source: knowledge/notes/all_part01_review.md, L540 to L540
[^350w-heat]: Source: knowledge/notes/all_part01_review.md, L541 to L541
[^deck-pack-sizing]: Source: knowledge/notes/all_part01_review.md, L542 to L542
[^hybrid-range]: Source: knowledge/notes/all_part01_review.md, L543 to L543
[^rita-charge-warning]: Source: knowledge/notes/all_part01_review.md, L544 to L544
[^rita-emulation]: Source: knowledge/notes/all_part01_review.md, L545 to L545
[^bms-drift]: Source: knowledge/notes/all_part01_review.md, L546 to L546
[^cst-152mm]: Source: knowledge/notes/all_part01_review.md, L554 to L554
[^monorim-tires]: Source: knowledge/notes/all_part01_review.md, L555 to L555
[^cst-10x25]: Source: knowledge/notes/all_part01_review.md, L556 to L556
[^xtech-rotor-sweep]: Source: knowledge/notes/all_part01_review.md, L557 to L557
[^uk-delay]: Source: knowledge/notes/all_part01_review.md, L560 to L560
[^m365tools-release]: Source: knowledge/notes/all_part01_review.md, L561 to L561
[^pack-sag-diagnosis]: Source: knowledge/notes/all_part01_review.md, L566 to L566
[^spot-weld]: Source: knowledge/notes/all_part01_review.md, L567 to L567
[^common-port-rita]: Source: knowledge/notes/all_part01_review.md, L568 to L568
[^trusted-packs]: Source: knowledge/notes/all_part01_review.md, L570 to L570
[^rita-fw-upgrade]: Source: knowledge/notes/all_part01_review.md, L573 to L573
[^series-swap]: Source: knowledge/notes/all_part01_review.md, L574 to L574
[^dash-block]: Source: knowledge/notes/all_part01_review.md, L575 to L575
[^m365dash-beta]: Source: knowledge/notes/all_part01_review.md, L576 to L576
[^tudor-internal]: Source: knowledge/notes/all_part01_review.md, L579 to L579
[^highcurrent-bms]: Source: knowledge/notes/all_part01_review.md, L580 to L580
[^max-shipping]: Source: knowledge/notes/all_part01_review.md, L581 to L581
[^monorim-speed]: Source: knowledge/notes/all_part01_review.md, L582 to L582
[^rotor-benchmark]: Source: knowledge/notes/all_part01_review.md, L585 to L585
[^monorim-drilling]: Source: knowledge/notes/all_part01_review.md, L586 to L586
[^xtech-pads]: Source: knowledge/notes/all_part01_review.md, L587 to L587
[^ups-us]: Source: knowledge/notes/all_part01_review.md, L590 to L590
[^range-etiquette]: Source: knowledge/notes/all_part01_review.md, L591 to L591
[^stl-sharing]: Source: knowledge/notes/all_part01_review.md, L592 to L592
[^error27]: Source: knowledge/notes/all_part01_review.md, L597 to L597
[^permanent-emulator]: Source: knowledge/notes/all_part01_review.md, L598 to L598
[^bms126flash]: Source: knowledge/notes/all_part01_review.md, L599 to L599
[^mosfet-diagnose]: Source: knowledge/notes/all_part01_review.md, L600 to L600

[^current-step]: Source: knowledge/notes/all_part01_review.md, L206 to L206
[^connector-melt]: Source: knowledge/notes/all_part01_review.md, L207 to L207
[^rita-detection]: Source: knowledge/notes/all_part01_review.md, L210 to L211
[^recuperation]: Source: knowledge/notes/all_part01_review.md, L212 to L212
[^ios-companion]: Source: knowledge/notes/all_part01_review.md, L213 to L213
[^kv-match]: Source: knowledge/notes/all_part01_review.md, L222 to L222
[^hub-upgrades]: Source: knowledge/notes/all_part01_review.md, L223 to L224
[^fake-pack]: Source: knowledge/notes/all_part01_review.md, L216 to L216
[^common-port-routing]: Source: knowledge/notes/all_part01_review.md, L217 to L217
[^storage]: Source: knowledge/notes/all_part01_review.md, L218 to L219. Source: knowledge/notes/all_part01_review.md, L430 to L430
[^twelve-s-chargers]: Source: knowledge/notes/all_part01_review.md, L232 to L232
[^shipping-charge]: Source: knowledge/notes/all_part01_review.md, L233 to L233
[^pack-topology]: Source: knowledge/notes/all_part01_review.md, L234 to L234
[^separate-charge-risk]: Source: knowledge/notes/all_part01_review.md, L252 to L253
[^battery-sales]: Source: knowledge/notes/all_part01_review.md, L254 to L255
[^bms-balance]: Source: knowledge/notes/all_part01_review.md, L256 to L256
[^21700]: Source: knowledge/notes/all_part01_review.md, L257 to L257
[^voltage-priority]: Source: knowledge/notes/all_part01_review.md, L258 to L258
[^bms-sizing]: Source: knowledge/notes/all_part01_review.md, L259 to L259
[^pack-expansion]: Source: knowledge/notes/all_part01_review.md, L260 to L260
[^cell-choice]: Source: knowledge/notes/all_part01_review.md, L270 to L270
[^brake-upgrades2]: Source: knowledge/notes/all_part01_review.md, L226 to L227
[^tire-pressure]: Source: knowledge/notes/all_part01_review.md, L228 to L228
[^stem-mods]: Source: knowledge/notes/all_part01_review.md, L229 to L229
[^brake-mix]: Source: knowledge/notes/all_part01_review.md, L268 to L268
[^range-boost]: Source: knowledge/notes/all_part01_review.md, L283 to L283
[^tire-choice]: Source: knowledge/notes/all_part01_review.md, L293 to L293
[^brake-alignment]: Source: knowledge/notes/all_part01_review.md, L294 to L295
[^charging-etiquette]: Source: knowledge/notes/all_part01_review.md, L269 to L269
[^ble-troubleshooting]: Source: knowledge/notes/all_part01_review.md, L262 to L263
[^primary-bms]: Source: knowledge/notes/all_part01_review.md, L264 to L264
[^serial-pinout]: Source: knowledge/notes/all_part01_review.md, L238 to L238
[^clone-behavior]: Source: knowledge/notes/all_part01_review.md, L239 to L239
[^repair-bms]: Source: knowledge/notes/all_part01_review.md, L242 to L242
[^non-telemetry]: Source: knowledge/notes/all_part01_review.md, L243 to L243
[^twelve-s-steps]: Source: knowledge/notes/all_part01_review.md, L245 to L246
[^speed-limit]: Source: knowledge/notes/all_part01_review.md, L247 to L247
[^rita-harness]: Source: knowledge/notes/all_part01_review.md, L248 to L248
[^pink-lead]: Source: knowledge/notes/all_part01_review.md, L249 to L249
[^ten-s-cells]: Source: knowledge/notes/all_part01_review.md, L250 to L250
[^hub-coolers]: Source: knowledge/notes/all_part01_review.md, L267 to L267
[^stem-locks]: Source: knowledge/notes/all_part01_review.md, L272 to L274
[^prints-lighting]: Source: knowledge/notes/all_part01_review.md, L275 to L276
[^lipo-warning]: Source: knowledge/notes/all_part01_review.md, L279 to L279. Source: knowledge/notes/all_part01_review.md, L415 to L415
[^pack-rec]: Source: knowledge/notes/all_part01_review.md, L280 to L283. Source: knowledge/notes/all_part01_review.md, L416 to L416
[^uart-kit]: Source: knowledge/notes/all_part01_review.md, L282 to L282
[^thermal-fuse]: Source: knowledge/notes/all_part01_review.md, L284 to L284. Source: knowledge/notes/all_part01_review.md, L424 to L424
[^charge-current]: Source: knowledge/notes/all_part01_review.md, L285 to L285. Source: knowledge/notes/all_part01_review.md, L428 to L428
[^xt30-adapter]: Source: knowledge/notes/all_part01_review.md, L429 to L429
[^pack-inspection]: Source: knowledge/notes/all_part01_review.md, L288 to L290. Source: knowledge/notes/all_part01_review.md, L423 to L423
[^workshop-power2]: Source: knowledge/notes/all_part01_review.md, L298 to L298
[^bms-warranty2]: Source: knowledge/notes/all_part01_review.md, L299 to L299
[^shipping-updates]: Source: knowledge/notes/all_part01_review.md, L300 to L300. Source: knowledge/notes/all_part01_review.md, L452 to L454
[^rita-low-pack]: Source: knowledge/notes/all_part01_review.md, L304 to L304
[^rita-charge-order]: Source: knowledge/notes/all_part01_review.md, L305 to L305
[^smart-bms]: Source: knowledge/notes/all_part01_review.md, L306 to L306
[^zero-watt]: Source: knowledge/notes/all_part01_review.md, L310 to L310
[^xiao1s]: Source: knowledge/notes/all_part01_review.md, L311 to L311
[^storage-telemetry]: Source: knowledge/notes/all_part01_review.md, L312 to L312
[^custom-dash]: Source: knowledge/notes/all_part01_review.md, L313 to L313
[^bms-match]: Source: knowledge/notes/all_part01_review.md, L316 to L316
[^cell-shortlist]: Source: knowledge/notes/all_part01_review.md, L319 to L319
[^g30-bag]: Source: knowledge/notes/all_part01_review.md, L322 to L322
[^config-mismatch]: Source: knowledge/notes/all_part01_review.md, L333 to L333
[^g30-delta]: Source: knowledge/notes/all_part01_review.md, L334 to L334
[^pro2-config]: Source: knowledge/notes/all_part01_review.md, L344 to L344
[^recup-throttle]: Source: knowledge/notes/all_part01_review.md, L347 to L347
[^current-step2]: Source: knowledge/notes/all_part01_review.md, L348 to L348
[^regen-limit]: Source: knowledge/notes/all_part01_review.md, L349 to L349
[^rita-finish]: Source: knowledge/notes/all_part01_review.md, L350 to L350
[^logistics-20a]: Source: knowledge/notes/all_part01_review.md, L353 to L353
[^nonconductive-paste]: Source: knowledge/notes/all_part01_review.md, L366 to L366
[^front-bolts]: Source: knowledge/notes/all_part01_review.md, L367 to L367
[^monorim-bind]: Source: knowledge/notes/all_part01_review.md, L368 to L368
[^rear-wiring]: Source: knowledge/notes/all_part01_review.md, L369 to L369. Source: knowledge/notes/all_part01_review.md, L412 to L412
[^deck-rib]: Source: knowledge/notes/all_part01_review.md, L370 to L370
[^charge-port-relocate]: Source: knowledge/notes/all_part01_review.md, L371 to L371
[^bt-logger]: Source: knowledge/notes/all_part01_review.md, L372 to L372
[^high-mount-signal]: Source: knowledge/notes/all_part01_review.md, L375 to L375
[^rear-tape]: Source: knowledge/notes/all_part01_review.md, L376 to L376
[^dual-pack-range]: Source: knowledge/notes/all_part01_review.md, L377 to L377
[^foldster-clearance]: Source: knowledge/notes/all_part01_review.md, L378 to L378. Source: knowledge/notes/all_part01_review.md, L401 to L401. Source: knowledge/notes/all_part01_review.md, L411 to L411
[^lighting-diy]: Source: knowledge/notes/all_part01_review.md, L404 to L404
[^uart485]: Source: knowledge/notes/all_part01_review.md, L419 to L419
[^laudation]: Source: knowledge/notes/all_part01_review.md, L420 to L420
[^pack-layout]: Source: knowledge/notes/all_part01_review.md, L425 to L425
[^bms-disassembly]: Source: knowledge/notes/all_part01_review.md, L457 to L457
[^monorim-grease]: Source: knowledge/notes/all_part01_review.md, L444 to L444
[^monorim-500w]: Source: knowledge/notes/all_part01_review.md, L468 to L468
[^fork-lift]: Source: knowledge/notes/all_part01_review.md, L486 to L486
[^solid-fit]: Source: knowledge/notes/all_part01_review.md, L487 to L487
[^max-motor]: Source: knowledge/notes/all_part01_review.md, L449 to L449
[^suspension-bearings]: Source: knowledge/notes/all_part01_review.md, L489 to L489
[^monorim-sourcing]: Source: knowledge/notes/all_part01_review.md, L379 to L380
[^doc-green]: Source: knowledge/notes/all_part01_review.md, L384 to L384
[^kcq]: Source: knowledge/notes/all_part01_review.md, L385 to L385
[^esa-bms]: Source: knowledge/notes/all_part01_review.md, L386 to L386
[^buck-hv]: Source: knowledge/notes/all_part01_review.md, L390 to L390
[^12s4p-temp]: Source: knowledge/notes/all_part01_review.md, L391 to L391
[^charger-trim]: Source: knowledge/notes/all_part01_review.md, L392 to L392
[^support-boundary]: Source: knowledge/notes/all_part01_review.md, L396 to L397
[^bag-length]: Source: knowledge/notes/all_part01_review.md, L328 to L328
[^wildman-screws]: Source: knowledge/notes/all_part01_review.md, L399 to L400
[^pack-cost]: Source: knowledge/notes/all_part01_review.md, L359 to L359
[^cst-v3]: Source: knowledge/notes/all_part01_review.md, L337 to L337
[^xtech-rotors]: Source: knowledge/notes/all_part01_review.md, L338 to L338
[^rub-only]: Source: knowledge/notes/all_part01_review.md, L325 to L325
[^aug-pause]: Source: knowledge/notes/all_part01_review.md, L327 to L327
[^throttle-steps]: Source: knowledge/notes/all_part01_review.md, L466 to L467
[^power-constant]: Source: knowledge/notes/all_part01_review.md, L443 to L443
[^heat-spike]: Source: knowledge/notes/all_part01_review.md, L445 to L445
[^heavy-load-heat]: Source: knowledge/notes/all_part01_review.md, L469 to L469
[^water-diagnostics]: Source: knowledge/notes/all_part01_review.md, L481 to L481
[^deck-threads]: Source: knowledge/notes/all_part01_review.md, L490 to L490
[^rita-reconfig]: Source: knowledge/notes/all_part01_review.md, L472 to L472
[^mixed-pack-range]: Source: knowledge/notes/all_part01_review.md, L473 to L473
[^bms-tool-v5]: Source: knowledge/notes/all_part01_review.md, L474 to L474
[^dash-100]: Source: knowledge/notes/all_part01_review.md, L476 to L476
[^xt30-safety]: Source: knowledge/notes/all_part01_review.md, L482 to L482
[^rita-data-line]: Source: knowledge/notes/all_part01_review.md, L433 to L435
[^zero-watt-telemetry]: Source: knowledge/notes/all_part01_review.md, L439 to L439
[^range-kit-compat]: Source: knowledge/notes/all_part01_review.md, L438 to L440
[^voltage-vs-torque]: Source: knowledge/notes/all_part01_review.md, L464 to L464
[^star-delta]: Source: knowledge/notes/all_part01_review.md, L483 to L483
[^vta-13s]: Source: knowledge/notes/all_part01_review.md, L494 to L494
[^range-multiplier]: Source: knowledge/notes/all_part01_review.md, L407 to L407
[^defensive-habits]: Source: knowledge/notes/all_part01_review.md, L408 to L408
[^cold-sag]: Source: knowledge/notes/all_part01_review.md, L465 to L465
[^uk-legal]: Source: knowledge/notes/all_part01_review.md, L495 to L495
[^series-boosters]: Source: knowledge/notes/all_part01_review.md, L493 to L493
[^rita-brake-limit]: Source: knowledge/notes/all_part01_review.md, L500 to L500

[^rita-capabilities]: Source: knowledge/notes/all_part01_review.md, L16 to L18. Source: knowledge/notes/all_part01_review.md, L23
[^rita-emulator]: Source: knowledge/notes/all_part01_review.md, L19. Source: knowledge/notes/all_part01_review.md, L114
[^rita-current-limit]: Source: knowledge/notes/all_part01_review.md, L20 to L24. Source: knowledge/notes/denis_all_part02_review.md, L22. Source: knowledge/notes/denis_all_part02_review.md, L31 to L33. Source: knowledge/notes/denis_all_part02_review.md, L153
[^rita-soh]: Source: knowledge/notes/all_part01_review.md, L21. Source: knowledge/notes/all_part01_review.md, L133
[^rita-overvoltage]: Source: knowledge/notes/denis_all_part02_review.md, L29 to L33
[^rita-telemetry]: Source: knowledge/notes/all_part01_review.md, L25. Source: knowledge/notes/all_part01_review.md, L139. Source: knowledge/notes/all_part01_review.md, L219. Source: knowledge/notes/denis_all_part02_review.md, L33. Source: knowledge/notes/denis_all_part02_review.md, L100
[^rita-config]: Source: knowledge/notes/denis_all_part02_review.md, L315 to L316
[^rita-awd]: Source: knowledge/notes/denis_all_part02_review.md, L26 to L28. Source: knowledge/notes/denis_all_part02_review.md, L197
[^rita-dual]: Source: knowledge/notes/denis_all_part02_review.md, L385 to L387
[^rita-charge-ui]: Source: knowledge/notes/denis_all_part02_review.md, L408 to L409
[^bms-roadmap]: Source: knowledge/notes/all_part01_review.md, L13. Source: knowledge/notes/all_part01_review.md, L117
[^bms-ceiling]: Source: knowledge/notes/all_part01_review.md, L182
[^bms-headroom]: Source: knowledge/notes/all_part01_review.md, L184
[^battery-enclosures]: Source: knowledge/notes/all_part01_review.md, L45. Source: knowledge/notes/all_part01_review.md, L48
[^wildman-e2]: Source: knowledge/notes/all_part01_review.md, L94 to L97
[^battery-bom]: Source: knowledge/notes/all_part01_review.md, L46. Source: knowledge/notes/all_part01_review.md, L61. Source: knowledge/notes/all_part01_review.md, L66. Source: knowledge/notes/all_part01_review.md, L102. Source: knowledge/notes/all_part01_review.md, L145. Source: knowledge/notes/all_part01_review.md, L238
[^common-port]: Source: knowledge/notes/all_part01_review.md, L101 to L105
[^range-kits]: Source: knowledge/notes/all_part01_review.md, L18. Source: knowledge/notes/all_part01_review.md, L260
[^separate-charge]: Source: knowledge/notes/all_part01_review.md, L180
[^pack-wrap]: Source: knowledge/notes/denis_all_part02_review.md, L329 to L330
[^refurb-triage]: Source: knowledge/notes/denis_all_part02_review.md, L333 to L333
[^parallel-test]: Source: knowledge/notes/denis_all_part02_review.md, L335 to L336
[^happy-13s]: Source: knowledge/notes/denis_all_part02_review.md, L345 to L345
[^wildman-stl]: Source: knowledge/notes/denis_all_part02_review.md, L345 to L346
[^adc-16s]: Controller voltage debates around 13–16 S builds, including resistor swaps and XiaoDash firmware handling without legacy jumpers. Source: knowledge/notes/denis_all_part02_review.md, L501 to L504
[^rita-49v]: Rita charge discussions noting 12 S externals plateau around 49.2 V (~4.1 V/cell) to preserve regen headroom. Source: knowledge/notes/denis_all_part02_review.md, L503 to L504
[^temp-sensors]: Split-charging diagnostics pointing to failed OEM temperature sensors that lock the internal BMS until replaced. Source: knowledge/notes/denis_all_part02_review.md, L505 to L505
[^winter-tyres]: Winter tire recommendations covering 10×2 tubeless off-road casings, Amalibay 9.2″ treads, and studding cautions plus cold-weather range loss. Source: knowledge/notes/denis_all_part02_review.md, L513 to L514
[^monorim-hardware]: Monorim hardware upkeep reminders to upgrade to 12.9-grade bolts, trim excess, and check for play. Source: knowledge/notes/denis_all_part02_review.md, L515 to L515
[^xtech]: Reports of Xtech hybrid brake corrosion/leaks pushing shops toward Magura hydraulics or premium mechanical calipers. Source: knowledge/notes/denis_all_part02_review.md, L517 to L518
[^paolo-hubs]: Paolo’s 1.2 kW+ hub sourcing notes and fork clearance requirements for 10″ tires. Source: knowledge/notes/denis_all_part02_review.md, L523 to L525
[^pu50]: Preference for PU50 marine urethane over Sikaflex for deck sealing plus neutral silicone guidance. Source: knowledge/notes/denis_all_part02_review.md, L527 to L528
[^50e2]: Shenzhen front-pack anecdote using Samsung 50E2 cells while reiterating Rita/BMS safety requirements. Source: knowledge/notes/denis_all_part02_review.md, L531 to L533
[^happy-stepup]: Happy BMS red-blink troubleshooting and DC step-up charger setup (start below pack voltage, ease toward ≈1 A).Source: knowledge/notes/denis_all_part02_review.md, L535 to L537
[^parallel-jst]: JST charge-lead Y-splitting guidance, current limits, and XT60 recommendations for ≥40 A discharge runs. Source: knowledge/notes/denis_all_part02_review.md, L539 to L541
[^happy-fw]: Scootermode 14 S error 24 recovery via 10 S flashing and Mi Electric 3 BLE/UUID checks before ST-Link work. Source: knowledge/notes/denis_all_part02_review.md, L543 to L545
[^highspeed-brakes]: High-speed brake/tire lessons covering Roscheeee adapters, 160–180 mm rotors, brake fluid boiling, and PMT/CST tire overheating above 80 km/h. Source: knowledge/notes/denis_all_part02_review.md, L547 to L549
[^winter-range]: Winter energy planning with 600 W caps, 80 % throttle, ferrofluid fills, and comprehensive waterproofing. Source: knowledge/notes/denis_all_part02_review.md, L551 to L553
[^40t-bms]: 48 V pack planning (Samsung 40T 13S5P, 60 A BMS, XT60 upgrades) plus Happy BMS 32 Ah register limit and Pro 2 firmware 126 guidance. Source: knowledge/notes/denis_all_part02_review.md, L555 to L559
[^harness-slime]: Harness upgrades to AWG12, cautions against thin motor leads, and slime dosing for 10″ tires. Source: knowledge/notes/denis_all_part02_review.md, L558 to L558. Source: knowledge/notes/denis_all_part02_review.md, L578 to L578
[^vendor]: Voltride shipping praise and steering buyers toward Scootermode/Paolo controllers over MaxMods. Source: knowledge/notes/denis_all_part02_review.md, L581 to L582
[^charger-chain]: TL431 charger mod resistor values, capacitor swaps, transformer limits, Android 12 sideload workaround, and YZPOWER vs. anonymous charger recommendations with soldered connector swaps. Source: knowledge/notes/denis_all_part02_review.md, L585 to L600
[^happy-fuse]: Source: knowledge/notes/denis_all_part02_review.md, L322 to L323
[^stlink-ble]: Source: knowledge/notes/denis_all_part02_review.md, L304 to L305
[^xiaodash-reset]: Source: knowledge/notes/denis_all_part02_review.md, L408 to L408
[^dash-swap]: Source: knowledge/notes/denis_all_part02_review.md, L410 to L410
[^pro2-internal-pack]: Source: knowledge/notes/denis_all_part02_review.md, L404 to L405
[^thermal-expansion]: Source: knowledge/notes/denis_all_part02_review.md, L413 to L413
[^boyueda-torque]: Source: knowledge/notes/denis_all_part02_review.md, L414 to L414
[^monorim-motor]: Source: knowledge/notes/denis_all_part02_review.md, L416 to L416
[^pmt-fitment]: Source: knowledge/notes/denis_all_part02_review.md, L424 to L425
[^kickstand-height]: Source: knowledge/notes/denis_all_part02_review.md, L439 to L441
[^tubeless-sealant]: Source: knowledge/notes/denis_all_part02_review.md, L448 to L450
[^happy-35a]: Source: knowledge/notes/denis_all_part02_review.md, L401 to L401
[^emulator-34v]: Source: knowledge/notes/denis_all_part02_review.md, L402 to L402
[^fan-mod-risk]: Source: knowledge/notes/denis_all_part02_review.md, L417 to L421
[^ali-pack-warning]: Source: knowledge/notes/denis_all_part02_review.md, L457 to L459
[^hydraulic-upgrade]: Source: knowledge/notes/denis_all_part02_review.md, L428 to L428. Source: knowledge/notes/denis_all_part02_review.md, L461 to L462
[^serial-reset]: Source: knowledge/notes/denis_all_part02_review.md, L430 to L431. Source: knowledge/notes/denis_all_part02_review.md, L464 to L465
[^suspension-extender]: Source: knowledge/notes/denis_all_part02_review.md, L433 to L435. Source: knowledge/notes/denis_all_part02_review.md, L467 to L468
[^accessory-dash]: Source: knowledge/notes/denis_all_part02_review.md, L486 to L487
[^tcs-hazard]: Source: knowledge/notes/denis_all_part02_review.md, L489 to L490
[^dual-motor-plan]: Source: knowledge/notes/denis_all_part02_review.md, L492 to L494
[^pack-teardown]: Source: knowledge/notes/denis_all_part02_review.md, L496 to L497
[^no-rita-emulation]: Source: knowledge/notes/denis_all_part02_review.md, L500 to L500
[^pricing]: Source: knowledge/notes/all_part01_review.md, L30. Source: knowledge/notes/all_part01_review.md, L61
[^pack-pricing]: Source: knowledge/notes/all_part01_review.md, L110 to L111
[^regional-pricing]: Source: knowledge/notes/all_part01_review.md, L176. Source: knowledge/notes/all_part01_review.md, L274
[^range-speed-charging]: Source: knowledge/notes/denis_all_part02_review.md, L33. Source: knowledge/notes/denis_all_part02_review.md, L46
[^shipping-scope]: Source: knowledge/notes/all_part01_review.md, L27. Source: knowledge/notes/all_part01_review.md, L177. Source: knowledge/notes/all_part01_review.md, L275. Source: knowledge/notes/all_part01_review.md, L453 to L453
[^batching]: Source: knowledge/notes/all_part01_review.md, L29. Source: knowledge/notes/all_part01_review.md, L33. Source: knowledge/notes/all_part01_review.md, L174
[^lead-times]: Source: knowledge/notes/all_part01_review.md, L32. Source: knowledge/notes/all_part01_review.md, L34. Source: knowledge/notes/all_part01_review.md, L35. Source: knowledge/notes/all_part01_review.md, L212
[^charging-telemetry]: Source: knowledge/notes/all_part01_review.md, L172 to L173. Source: knowledge/notes/denis_all_part02_review.md, L33. Source: knowledge/notes/denis_all_part02_review.md, L46
[^docs]: Source: knowledge/notes/all_part01_review.md, L17
[^stlink-loaner]: Source: knowledge/notes/all_part01_review.md, L458 to L458
[^storefront]: Source: knowledge/notes/all_part01_review.md, L17 to L18
[^support-ops]: Source: knowledge/notes/all_part01_review.md, L150
[^rita-max]: Source: knowledge/notes/denis_all_part02_review.md, L195 to L196
[^serbia]: Source: knowledge/notes/all_part01_review.md, L300 to L300. Source: knowledge/notes/all_part01_review.md, L452 to L454
[^workshop-power]: Source: knowledge/notes/all_part01_review.md, L298 to L298
[^bms-warranty]: Source: knowledge/notes/all_part01_review.md, L299 to L301
[^thirteen-steps]: Source: knowledge/notes/all_part01_review.md, L162 to L166. Source: knowledge/notes/all_part01_review.md, L217
[^tp4056]: Source: knowledge/notes/all_part01_review.md, L10 to L11
[^ble073]: Source: knowledge/notes/all_part01_review.md, L12 to L12
[^bms-belgium]: Source: knowledge/notes/all_part01_review.md, L13 to L13
[^anti-spark]: Source: knowledge/notes/all_part01_review.md, L20 to L20. Source: knowledge/notes/all_part01_review.md, L104 to L104
[^rita-12s-config]: Source: knowledge/notes/all_part01_review.md, L42 to L43
[^charger-upgrade]: Source: knowledge/notes/all_part01_review.md, L106 to L107. Source: knowledge/notes/all_part01_review.md, L123 to L123
[^brake-upgrade]: Source: knowledge/notes/all_part01_review.md, L44 to L44
[^fake-60ah]: Source: knowledge/notes/all_part01_review.md, L40 to L40
[^rain-proof]: Source: knowledge/notes/all_part01_review.md, L41 to L41
[^stlink]: Source: knowledge/notes/all_part01_review.md, L47 to L49
[^dash-update]: Source: knowledge/notes/all_part01_review.md, L48 to L48
[^dash-retrofit]: Source: knowledge/notes/all_part01_review.md, L93 to L93
[^face-ltd]: Source: knowledge/notes/all_part01_review.md, L50 to L50
[^power-risks]: Source: knowledge/notes/all_part01_review.md, L22. Source: knowledge/notes/all_part01_review.md, L155. Source: knowledge/notes/all_part01_review.md, L170 to L171
[^legacy-boards]: Source: knowledge/notes/denis_all_part02_review.md, L29 to L33. Source: knowledge/notes/denis_all_part02_review.md, L153
[^rita-v4]: Source: knowledge/notes/denis_all_part02_review.md, L22 to L33
[^controller-thermals]: Source: knowledge/notes/denis_all_part02_review.md, L10 to L13
[^rita-hill]: Source: knowledge/notes/denis_all_part02_review.md, L31 to L33
[^awd]: Source: knowledge/notes/denis_all_part02_review.md, L25 to L28
[^error14]: Source: knowledge/notes/denis_all_part02_review.md, L26 to L31. Source: knowledge/notes/denis_all_part02_review.md, L6433 to L6456
[^thermal-paste]: Source: knowledge/notes/denis_all_part02_review.md, L32 to L33
[^counterfeit]: Source: knowledge/notes/denis_all_part02_review.md, L19 to L23
[^resell-cost]: Source: knowledge/notes/all_part01_review.md, L91 to L92
[^price-10s]: Source: knowledge/notes/all_part01_review.md, L110 to L110
[^bag-security]: Source: knowledge/notes/denis_all_part02_review.md, L42 to L45
[^pack-charger]: Source: knowledge/notes/denis_all_part02_review.md, L45 to L46
[^tool-packs]: Source: knowledge/notes/denis_all_part02_review.md, L235 to L235
[^lawn-pack]: Source: knowledge/notes/denis_all_part02_review.md, L6610 to L6635
[^balance-leads]: Source: knowledge/notes/denis_all_part02_review.md, L7028 to L7068
[^parallel-risk]: Source: knowledge/notes/all_part01_review.md, L113 to L113. Source: knowledge/notes/all_part01_review.md, L569 to L569
[^lifepo4]: Source: knowledge/notes/denis_all_part02_review.md, L7080 to L7089
[^rita-schottky]: Rita’s Schottky drop leaving internal packs near 97 % unless bypassed during off-scooter charging, which Denis still recommends for pack longevity. Source: knowledge/notes/denis_all_part02_review.md, L103 to L103. Source: knowledge/notes/denis_all_part02_review.md, L108 to L108
[^sequential-charging]: Source: knowledge/notes/all_part01_review.md, L103 to L113
[^rita-underreport]: Small Rita Gen 4 batch that under-reported current above ~20 A while redundant sensing still tripped overcurrent protection on Ninebot Max validation builds. Source: knowledge/notes/denis_all_part02_review.md, L198 to L198
[^rita-soc]: Dashboard state of charge drifting after Rita installs, prompting Denis to treat 50 % on the display as the return threshold while using the app for actual voltage. Source: knowledge/notes/denis_all_part02_review.md, L127 to L127
[^rita-undercharge]: Source: knowledge/notes/denis_all_part02_review.md, L220 to L229
[^rita-60v]: Source: knowledge/notes/denis_all_part02_review.md, L256 to L257
[^harness_staging]: Source: knowledge/notes/denis_all_part02_review.md, L7534 to L7589. Source: knowledge/notes/denis_all_part02_review.md, L7567 to L7589. Source: knowledge/notes/denis_all_part02_review.md, L11671 to L11676
[^cheap-packs]: Source: knowledge/notes/denis_all_part02_review.md, L5499 to L5526
[^large-format]: Source: knowledge/notes/all_part01_review.md, L116 to L117
[^xiaoflasher]: Source: knowledge/notes/denis_all_part02_review.md, L2467 to L2470
[^twelve-s-config]: Source: knowledge/notes/denis_all_part02_review.md, L10541 to L10552
[^hazmat]: Source: knowledge/notes/denis_all_part02_review.md, L188 to L193

## References

[^1]: Source: knowledge/notes/all_part01_review.md, L175 to L175
[^2]: Source: knowledge/notes/all_part01_review.md, L113 to L113
[^3]: Source: knowledge/notes/all_part01_review.md, L106 to L107
[^4]: Source: knowledge/notes/all_part01_review.md, L114 to L114
[^5]: Source: knowledge/notes/all_part01_review.md, L182 to L182
[^6]: Source: knowledge/notes/all_part01_review.md, L115 to L116
[^7]: Source: knowledge/notes/all_part01_review.md, L117 to L117
[^8]: Source: knowledge/notes/all_part01_review.md, L171 to L171
[^9]: Source: knowledge/notes/all_part01_review.md, L133 to L133
[^10]: Source: knowledge/notes/all_part01_review.md, L132 to L132
[^11]: Source: knowledge/notes/all_part01_review.md, L134 to L134
[^12]: Source: knowledge/notes/all_part01_review.md, L201 to L201
[^13]: Source: knowledge/notes/all_part01_review.md, L137 to L137
[^14]: Source: knowledge/notes/all_part01_review.md, L138 to L138
[^15]: Source: knowledge/notes/all_part01_review.md, L139 to L140
[^16]: Source: knowledge/notes/denis_all_part02_review.md, L224 to L225
[^17]: Source: knowledge/notes/denis_all_part02_review.md, L97241 to L97259
[^18]: Source: knowledge/notes/denis_all_part02_review.md, L361 to L362
[^19]: Source: knowledge/notes/denis_all_part02_review.md, L119 to L121
[^20]: Source: knowledge/notes/denis_all_part02_review.md, L122 to L123
[^21]: Source: knowledge/notes/denis_all_part02_review.md, L242 to L243
[^22]: Source: knowledge/notes/denis_all_part02_review.md, L252 to L254
[^23]: Source: knowledge/notes/denis_all_part02_review.md, L215 to L216
[^24]: Source: knowledge/notes/denis_all_part02_review.md, L233 to L234
[^25]: Source: knowledge/notes/denis_all_part02_review.md, L318 to L319
[^26]: Source: knowledge/notes/denis_all_part02_review.md, L320 to L320
[^27]: Source: knowledge/notes/denis_all_part02_review.md, L348 to L349
[^28]: Source: knowledge/notes/denis_all_part02_review.md, L351 to L352
[^29]: Source: knowledge/notes/denis_all_part02_review.md, L116 to L118
[^30]: Source: knowledge/notes/denis_all_part02_review.md, L301 to L301
[^31]: Source: knowledge/notes/denis_all_part02_review.md, L149 to L150
[^32]: Source: knowledge/notes/denis_all_part02_review.md, L152 to L153
[^33]: Source: knowledge/notes/denis_all_part02_review.md, L173 to L174
[^34]: Source: knowledge/notes/denis_all_part02_review.md, L248 to L250
[^35]: Source: knowledge/notes/denis_all_part02_review.md, L355 to L355
[^36]: Source: knowledge/notes/all_part01_review.md, L121 to L121
[^37]: Source: knowledge/notes/all_part01_review.md, L122 to L122
[^38]: Source: knowledge/notes/all_part01_review.md, L123 to L123
[^39]: Source: knowledge/notes/all_part01_review.md, L124 to L124
[^40]: Source: knowledge/notes/all_part01_review.md, L176 to L176
[^41]: Source: knowledge/notes/all_part01_review.md, L177 to L178
[^42]: Source: knowledge/notes/all_part01_review.md, L179 to L179
[^43]: Source: knowledge/notes/all_part01_review.md, L180 to L180
[^44]: Source: knowledge/notes/all_part01_review.md, L181 to L181
[^45]: Source: knowledge/notes/all_part01_review.md, L195 to L195
[^46]: Source: knowledge/notes/all_part01_review.md, L196 to L196
[^47]: Source: knowledge/notes/all_part01_review.md, L197 to L197
[^48]: Source: knowledge/notes/all_part01_review.md, L185 to L185
[^49]: Source: knowledge/notes/all_part01_review.md, L186 to L186
[^50]: Source: knowledge/notes/all_part01_review.md, L187 to L187
[^51]: Source: knowledge/notes/all_part01_review.md, L188 to L188
[^52]: Source: knowledge/notes/all_part01_review.md, L159 to L159
[^53]: Source: knowledge/notes/all_part01_review.md, L200 to L200
[^54]: Source: knowledge/notes/all_part01_review.md, L172 to L172
[^55]: Source: knowledge/notes/all_part01_review.md, L151 to L151
[^56]: Source: knowledge/notes/all_part01_review.md, L152 to L152
[^57]: Source: knowledge/notes/all_part01_review.md, L155 to L155
[^58]: Source: knowledge/notes/all_part01_review.md, L156 to L156
[^59]: Source: knowledge/notes/all_part01_review.md, L157 to L157
[^60]: Source: knowledge/notes/all_part01_review.md, L158 to L158
[^61]: Source: knowledge/notes/all_part01_review.md, L167 to L167
[^62]: Source: knowledge/notes/all_part01_review.md, L191 to L192
[^63]: Source: knowledge/notes/denis_all_part02_review.md, L218 to L219
[^64]: Source: knowledge/notes/denis_all_part02_review.md, L98595 to L98598
[^65]: Source: knowledge/notes/denis_all_part02_review.md, L221 to L222
[^66]: Source: knowledge/notes/denis_all_part02_review.md, L97446 to L97459
[^67]: Source: knowledge/notes/denis_all_part02_review.md, L86203 to L86239
[^68]: Source: knowledge/notes/denis_all_part02_review.md, L302 to L302
[^69]: Source: knowledge/notes/denis_all_part02_review.md, L308 to L309
[^70]: Source: knowledge/notes/denis_all_part02_review.md, L311 to L312
[^71]: Source: knowledge/notes/denis_all_part02_review.md, L326 to L327
[^72]: Source: knowledge/notes/denis_all_part02_review.md, L338 to L339
[^73]: Source: knowledge/notes/denis_all_part02_review.md, L341 to L342
[^74]: Source: knowledge/notes/denis_all_part02_review.md, L357 to L359
[^75]: Source: knowledge/notes/denis_all_part02_review.md, L393 to L394
[^76]: Source: knowledge/notes/denis_all_part02_review.md, L399 to L400
