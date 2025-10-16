# Ninebot G30 VESC Conversion Playbook

## TL;DR

- The G30 Max remains the friendliest chassis for VESC swaps thanks to abundant deck space, aftermarket spacers, and new BMS firmware that unlocks >20 A discharge without extra comms harnesses.[^1]
- Expect roughly 140 loose 18650s to fit without grinding the rails.
  - builders are running 20 S 4 P packs inside the deck plus 20 S 4 P shoulder-bag boosters (or 20 S 9 P externals when stealth is optional) while still leaving room for dual controllers.[^2][^3]
- Real-world 16 S builds with Ubox 100/100 controllers and 65 H 17×4 motors hit ~45 mph on 50 A field weakening yet still average roughly 1 mile per amp-hour, proving battery upgrades deliver the biggest gains before motor swaps.[^4]
- Traction control, throttle filtering, and thermal management are mandatory as phase limits climb toward 300 A; positive ramp times (~0.4 s) and careful ADC tuning tame wheelspin and runaway spikes on lightweight decks.[^5][^6]
- SNSC 2.3 donor frames are drying up as fleets migrate to Okai hardware.
  - lock in a chassis or negotiate with operators before planning large VESC conversions around rental leftovers.[^7]

## Base Scooter Preparation

- Flash the latest ScooterHacking G30 BMS firmware to lift discharge ceilings past 20 A while retaining stock harnesses.
  - essential before pushing VESC phase currents.[^8]
- Swap the factory “silver” phase leads for quality 12 AWG silicone.
  - stock G30 wires are just tinned copper and run hot above 20 A continuous even though scooter duty cycles let 12 AWG survive short bursts.[^9]
- Stage an ST-Link and legacy BLE packages before teardown.
  - DE-market Pro 2 dashboards on BLE 1.55+ refuse OTA downgrades, clone controllers spoof serials yet still block flashes, and forcing new Xiaomi BMS firmware through ST-Link has bricked boards mid-conversion.[^10]
- Measure the deck cavity early: builders logged ~120 mm width and 74 mm depth, giving clear constraints before committing to dual controllers or double-stack battery layouts.[^11]
- Map your layout before cutting: document whether the project keeps everything internal (20 S 4 P deck packs, controller at the nose) or adds external 20 S boosters, and capture CNC stem dimensions plus star-nut installation steps when adapting SNSC forks so future builds don’t guess at hardware order.[^g30_layouts]
- Build a spacer/pack checklist before welding: 20 S 4 P layouts fit with printed or CNC spacers plus minor cable reroutes, while 20 S 5 P bricks demand tray trimming, recessed fasteners, and harness standoffs to preserve deck clearance.[^12]
- 20 S 6 P attempts demand 30 mm frame extensions, ultra-low ride height, and ruthless wire pruning.
  - racers still call the setup risky without spacers and reinforced lids, so weigh ground clearance before copying it.[^13]
- Long-range bragging rights still collide with heat: even 20 S 5 P packs that “never run out of power” fight motor temps and push builders toward newer hubs, ferrofluid, or regen-only spares.[^14]
- Zero 11X comparisons highlight what good busbar work looks like.
  - a 21 S pack with just 0.002 V delta and heavy-gauge cabling set the bar for big-wheel race builds before you attempt similar power levels on a Max.[^15]
- Strip the frame and inspect deck welds prior to grinding rails for larger packs; documented builds plan rail relief plus 3 mm aluminum skid plates as interim reinforcement.[^16][^17]
- When shaving deck rails, use a ½″ belt sander, step-drill with cutting fluid, and brace the frame solidly.
  - steady fixturing matters more than owning a floor drill press, and U.S. builders still source metric bits online.[^18]
- Jan measured ~119 mm between the deck rails.
  - expect to grind ~0.5 mm per side and mount the BMS vertically when chasing 22–24 S packs without external rails.[^19]
- Choose battery spacers carefully: JREV units add cable room but misalign slightly with the frame, so plan shims or revised prints when targeting 22 S layouts.[^20]
- Expect the stock ESC to refuse third-party 1 kW hubs.
  - the controller looks for Ninebot’s protocol, so non-OEM motors demand a custom FOC flash or a full VESC swap, and the housings need steel adapters just to clear the fork.[^21]
- Reseal the deck lid and servo-lock cavity after grinding ribs.
  - builders report lost waterproofing unless silicone is restored and the servo void is capped or reused for accessories.[^22]
- Printed deck extenders and 2 mm spacer shims free vertical clearance for BMS harness exits when stacking externals.
  - plan wiring height early so lids close without crushing leads.[^23]
- Rental G30 chassis earn premium status: fixed stems, dual brakes, oil suspension, and thicker tubing swallow 13 S 5 P 21700 packs plus 1.2 kW hubs without the flex or wobble of stock Xiaomi frames.
  - expect ~10 kg more steel but far less frame twist under launch torque.[^24]

## Powertrain Reference Builds

| Configuration | Controllers & Limits | Reported Performance | Notes |
| --- | --- | --- | --- |
| 16 S commuter | Dual Ubox 100/100, Ortega observers, 50 A FW start at 87 % duty | ≈45 mph top speed, ~59 A peaks, ~1 mile per amp-hour above 20 mph | Prioritize battery capacity and cooling before chasing new motors; FW headroom exists but watch temperature logs.[^4] |
| 18 S single-drive debug | Single Ubox 85150 @ 90 A battery / 150 A phase with ~70 A FW | Power “flutter” around 40 mph even after disabling FW; rider is logging video/settings for review.[^25] | Re-run detection, capture logs, and validate wiring before increasing limits; flutter persisted after firmware tweaks, so treat it as a diagnostic exercise rather than a tuning shortcut.[^25] |
| 16 S Blade 800 W swap | Single VESC now, dual Flipsky 75100 CAN link planned; ≈100 A pack ceiling with light FW | 60–68 km/h on a 16 S 4 P Molicel 40T pack while keeping motor current near 100 A | Document CAN harnessing before adding the second 75100.
  - builders are still requesting wiring diagrams.[^26] |
| 20 S stealth upgrade | Planned 20 S4 P 50PL pack with rail grinding and future 50 kW target | In progress.
  - emphasizes fabrication burden (deck grinding, spacer redesign, pack sourcing) | Budget premium cells (50PL/P45B) and labor; expect cost doubling over 30Q baselines.[^16] |
| 11" speed project | Gabe’s 11" mock-up with extended dropouts | Highlighted leverage changes that demand welded U-channel reinforcement or reverting to 10" PMTs for stability above 120 km/h | Reinforce axle carriers before drilling new holes; unbraced extensions compromise geometry.[^27] |
| 22 S race prep | Targeting 22×3 or 33×2 motors, 300 A phase, positive ramp ~0.4 s | Focus on traction control slip windows (11 k–17 k rpm) to avoid wheelspin | Requires spare motors and throttle filtering to mitigate spike-induced controller shutdowns.[^5][^6] |

- Builders chasing 14 S commuter tunes still favor Spintend’s Ubox over Flipsky thanks to beefier MOSFETs and cooling; early Ubox batches like extra thermal pads, and 30Q/40T packs comfortably supply the ~70 A battery draw when motors can stomach it.[^28]

## Battery & BMS Planning

- Budget packs starting with 20 S Samsung 30Q quotes for commuters, but expect premium 21700 builds (50PL, P45B/P50B) to double total cost once welding, insulation, and shipping are included.[^16]
- Expect diminishing returns beyond 18 S on stock Xiaomi/Ninebot hubs.
  - doubling pack voltage roughly doubles free-spin speed, but the commuter-class motors cook themselves at 20 S unless you add serious cooling or swap to beefier hubs like Fiido’s wider L3 stator.[^29]
- Packaging 20 S bricks inside the Xiaomi/M365 deck is a “brain-f***” even for veterans; most builders call 18 S the practical sweet spot unless you are ready to redesign the layout into a G30LP-style chassis with intricate wiring clearances.[^30]
- P45B cells win on energy density, yet 30T’s ~5 mΩ resistance still suits riders chasing peak discharge bursts.
  - log goals before picking chemistry for Max deck rebuilds.[^31]
- Pair motor choices with those packs: Monorim/Xiaomi hub variants range from commuter 28 kV cores that prefer ≤80 A phase to speed-wound 32 kV units that tolerate 110–120 A when hall sensors stay healthy.
  - retire cracked magnets or failing halls before adding voltage.[^32][^33]
- OG Ninebot hubs overheat once battery current climbs past ~40–45 A even on 20 S packs.
  - cap phase/battery settings or upgrade hubs before feeding dual 15 A controllers continuous load.[^34]
- ANT smart BMS units have latched discharge FETs under Spintend-level currents; plan redundant pack protection (loop keys, fuse boards, or dual BMS) for >300 A goals.[^35]
- Calibrate CAN smart BMS logs against VESC telemetry.
  - BMS current remains more trustworthy but may drift; manual calibration preserves ±500 W accuracy on 35 kW builds.[^36]
- Ninebot Max decks can house 50 Ah 10 S bricks or even 15 S 4 P 21700 arrays once controllers move outboard, giving tour-focused builds room for 260-cell packs before adding externals.[^37]
- Source 220 mm shrink early for “thick” 13 S 5 P 21700 rental packs.
  - EU builders are rationing wide sleeves and supplementing with 0.25–0.30 mm copper straps so each series bridge handles ≥35–40 A without bottlenecking the new pack volume.[^38]
- Mirono’s rental-frame build squeezed a Daly smart BMS and 13 S 5 P NCR21700A pack inside after grinding internal ribs, with copper “sandwich” busbars on standby if field weakening needs lower resistance.[^39]
- Expect AWG10 mains (or dual AWG12 runs) once battery current targets hit 90 A.
  - crews even drop 3–3.5 mm solid copper between pack negatives and BMS plates to keep voltage drop in check.[^40]
- Jason’s Max project already packaged a 30 S pack around a 65H 17×4 motor and scoped a fully internal 40 S/3 P layout, proving the deck ceiling once partitions are trimmed and harness routing is planned early.[^41][^42]
- Treat the Ninebot P100 pack as a reminder that chassis upgrades can outpace energy storage.
  - its 52 V 23 Ah battery only returns about 25 mi at 30 mph until firmware efficiency improves, so budget range upgrades alongside structural swaps.[^43]
- Long-range G30 builds still fight motor heat even when they boast “endless power”.
  - plan ferrofluid, spare motors for regen-only duty, or newer hub generations if you promise high-speed touring.[^14]
- Vsett 9 frames can internalize 52 V 30 Ah packs.
  - and even standing 20 S8 P stacks with spacers
  - providing inspiration for auxiliary battery pods or cross-frame transplants on Max conversions.[^44]
- A 21 S Zero 11X pack with ~0.002 V delta showcased proper busbars and heavy-gauge cabling for big-wheel race builds.
  - borrow its harness and reinforcement ideas when scaling Max packs beyond commuter duty.[^15]

## Packaging & Layout Patterns

- **Map deck configurations early.** Builders split 20 S packs between the deck and shoulder bags, slide 20 S4 P externals under the stem, or relocate controllers outside the deck to free space for 9 P cores.
  - document wiring paths before cutting rails.[^45]
- **Plan stem swaps with proper hardware.** Custom CNC stems let SNSC forks drop in without cutting suspension, but remember to hammer star nuts into the new tube so the folding joint stays tight once the swap is complete.[^46]
- **Map deck configurations early.** Builders split 20 S packs between the deck and shoulder bags, slide 20 S4 P externals under the stem, or relocate controllers outside the deck to free space for 9 P cores.
  - document wiring paths before cutting rails.[^47]
- GABE is reprinting critical structural pieces in 100 % PETG and stacking Kapton–copper laminations so every conductor stays on the top side of his wraparound pack, adding plastic isolation sheets to protect bus bars inside the tight deck tolerances.[^48]
- **Plan SNSC fork swaps with CNC fixtures.** The community now machines custom stems that capture SNSC forks while accommodating star nuts and cable routing; print drill guides before sending aluminum to the mill to guarantee headset alignment.[^47]
- **SNSC donor realities.** Grinding rails for mounting plates and sliding motors rearward tames the monofork when running 17×4″ fronts, and the 55 kg frame doesn’t fold.
  - plan freight or ship packs separately when you adopt rental chassis.[^49]
- **Mount MP2 duals carefully.** GABE confirmed twin MP2 controllers fit upright between Ninebot Pro 2 rails when you elevate them with spacers and insulate the rails with Kapton or mesh tape to avoid shorts.[^50]
- **Front disc conversions can reuse Pro 2 hubs.** Repurposing a Ninebot Pro 2 front motor keeps geometry intact, then you only need custom spacers and a caliper bracket to add a disc without Monorim suspension bulk.[^51]
- **Blueprint tall-pack builds before welding.** GABE’s 20 S 12 P concept stacks cells to ~14.5 cm, parks the BMS vertically at the nose, mounts dual MP2 controllers in a welded rear box, and splits current across QS8 leads with parallel 8 AWG runs.
  - mock up the layout so harness slack and deck arches clear before committing to metalwork.[^52]
- Mini-BMX conversions for “Peak G30 v2” projects should confirm dropout width and tire clearance before buying rubber.
  - 10×3.0-6.5 tires shrink the contact patch, but Haku still needed another 10–15 mm of dropout width or a switch to dual 10″ LY 65H motors with 125 mm axles.[^53]
- 10×3.0-6.5 tubeless tires measure about 3 inches wide on 73 mm (≈2.84″) rims and sit safer than stretched 70/65-6.5 casings; use the imperial size math (first number = width, second = aspect) to convert between listings confidently.[^54]

## Control & Traction Tuning

- Update Xiaomi/Ninebot dashboards to firmware 6.05 before pairing dual controllers.
  - the community Lisp build on 6.02 only forwards CAN for a single ESC, so flash Xiaomi firmware or the 6.05 beta images before wiring two VESCs to the dash.[^55]
- Makerbase 75100 retrofits still need the pull-down resistor on dash pin 3; riders leave the suggested capacitor optional but warn that 6.2 firmware locks all modes at ~60 % current until a fix ships, so most stay on older releases.[^g30-pulldown]
- Set motor detection parameters for the G30’s 30-pole hubs and remove any lingering phase filters after repairs.
  - misdiagnosed gate drivers kept blowing MOSFETs until riders retested hardware with the correct pole count.[^56]
- Compress throttle ADC ranges (treat ~0.83 V as idle, activate around 1.0–1.2 V) to eliminate noise-triggered surges on Spintend 100/100 installs.[^57]
- Grounding the chassis cured runaway acceleration for some riders, but document the wiring and verify insulation to avoid frame shorts before adopting the fix broadly.[^58]
- Log traction control adjustments during every shakedown; slip thresholds between 11 k and 17 k rpm and positive throttle ramps (~0.4 s) kept lightweight builds controllable at 300 A phase.[^6]
- When upgrading to hydraulic fronts, transplant the stock hall sensor and magnet into the new lever so proportional regen survives the swap and rear mechanical brakes can stay untouched.[^59]
- Mirono routes the motor cable around the G30 brake-adapter screw to clear the rotor.
  - zip-tying the lead directly to the fork let it rub the disc at speed, so verify steering clearance before buttoning up the front end.[^60]
- Expect a “10 error” on the stock display after dropping in a Makerbase 75100 V2 until you connect the dash to VESC Tool—plan a programming session right after the swap.[^g30-error10]

## Dash Scripting & Secret-Mode Management

- Unlock “secret mode” by holding both brake and throttle while double-tapping the dash button; remember to exit walk mode first or the scooter stays capped near 20 km/h.[^61]
- Point newcomers to 🇪🇸lekrsu’s SHFW walkthrough when flashing Ninebot ES/Max controllers.
  - the guide delivers a no-code firmware baseline that keeps stock indicators and buzzers intact before you migrate to full VESC control.[^62]
- Firmware 6.05’s ADC branch introduces `secret-sport-fw` and `secret-sport-watts` parameters plus a lower ≈470 Ω throttle resistor target.
  - add RC filtering across the hall supply if the headlight drags the brake line low.[^63]
- Late-production dashboards now block OTA downgrades for >32 km/h unlocks.
  - budget ST-Link access and a Windows flash session to push XiaoDash firmware before promising higher speed caps to new G30 owners.[^64]
- Removing the dash entirely.
  - or at least desoldering its Bluetooth radio
  - cuts the parked idle draw on alarmed builds so overnight battery drain no longer eats reserve capacity.[^65]
- Remove dash scripts only after unlocking; deleting them mid-lock freezes the limit, and random mid-ride power cuts are still reported.
  - treat the display as instrumentation once configuration is complete.[^66]

## Thermal & Mechanical Safeguards

- Cap field-weakening around 20 A on stock 6×TO-220 Makerbase 75100 boards.
  - extended 35 A pulls at 130 A phase have already burned MOSFETs, so step up to the aluminum-PCB/vented variants if you need sustained high-speed duty.[^67]
- Pune’s single-motor log showed a Makerbase 75100 holding ~4.2 kW peaks at ~44 °C when clamped inside the stock controller can.
  - treat the OEM enclosure as part of the heatsink if airflow is limited.[^68]
- Monitor per-motor temperatures; aim for ≤45 °C controller temps and ≤90–100 °C stator temps by refreshing thermal paste and clamping controllers to thick skid plates.[^69][^70]
- Bond controllers to the deck with thermal epoxy where possible.
  - Matthew’s single 85150 now idles near 40 °C with ~60 °C peaks after the previous mount let temps spike toward 80 °C and a BMS cutoff shorted its partner.[^71]
- Plan for valve-stem service and bead reseating after pothole hits.
  - tubeless split rims can burp air, so keep compressors and soapy water handy during test rides.[^72]
- Track tire availability: true 12″ tubeless slicks remain limited to rare Touvt 12×4.5‑6.5 listings, so expect lead times or plan alternate wheelsets when chasing maximum footprint on VESC builds.[^73]
- Evaluate braking upgrades alongside power mods; 203 mm rotors add leverage but may be overkill.
  - pair regen tuning with quality hydraulic calipers and DOT 4/5 fluid first.[^74]
- **Front-disc conversions without Monorim.** Repurpose a Ninebot Pro 2 front motor to gain the factory disc mount, then design spacers and caliper mounts around the stock fork so you avoid bulky Monorim swaps.[^g30_front_disc]
- Use the €25 ePowerFun 3 mm aluminum floor plate as a quick cooling stopgap.
  - drill five mounting holes, trim the nose to clear JREV spacers, and plan a thicker custom plate once testing confirms heat loads.[^epowerfun]
- Transparent plexiglass lids look great but need threadlocker, silicone seals, and stronger epoxy/two-part adhesive for LED strips.
  - 6 mm sheets crack without extra support, especially around temperature swings.[^75]
- High-speed conversions (70 km/h GPS on 48 V delta/star rewires) demand wider bars and frame reinforcement before daily riding; treat chassis upgrades as mandatory at those velocities.[^76]

## Hall Sensor Service & Orientation

- Replace failed halls with matching switch types (SS41F vs. R43) and keep the stamped face aligned; mismatches hold ~2 V output and block motor detection until reinstalled correctly.[^77]
- After sensor swaps, rerun motor detection and temporarily cap limits near 40 A battery / 80 A phase while sourcing spares to avoid repeated tear-downs.[^78]

## Sourcing & Accessory Integration

- Avoid too-good-to-be-true controller deals: £50 AliExpress listings are often bare logic boards; prioritize complete Spintend 100/100 Lite kits or 84/150 bundles from trusted resellers to get full harnesses.[^79]
- Source ready-made harnesses when possible: Finn’s €50 Ninebot G30 VESC adapter ships within Germany and mates with Ubox 100/100 and 85150 controllers, saving hours of hand-crimping for future conversions.[^80]
- Panel-mount QS8 connectors remain custom-only; draft plates early or leverage community prints to keep high-current leads tidy once deck space tightens.[^81]
- Magnetic pogo-pin connectors look tidy on paper, but without keyed layouts they can short 200 W chargers.
  - plan polarity guides and isolation before experimenting with quick-swap charge ports.[^82]
- Zero-to-Vsett conversions go smoother with the Zero 10X rear bracket/arm kit than custom plates when fitting Vsett 10+ hubs to a G30 with a Monorim rear end.
  - budget for the swap before cutting metal.[^83]
- Consider Voyage Megan or other CAN dashboards for consolidated telemetry once controllers are upgraded; validate compatibility when mixing CL350 or Express accessories with Ubox hardware.[^84][^85]
- Budget a dedicated buck converter if you add VESC Express boards.
  - the modules only accept 5 V at ~150 mA and currently reset logging every few seconds on 6.06 firmware, so plan CAN updates or stay on 6.05 for stable telemetry.[^express_power]
- Track where SNSC rental frames are still available and catalogue printable accessories (battery spacers, lighting pods, cable saddles) that fit Bambu P1S-class beds so builders can fabricate replacements in-house when fleet stock dries up.[^sns_prints]
- Document J1772 travel adapters as part of the charging kit: a proven harness uses 12 AWG silicone leads plus 2.5 mm² wiring with 2.74 kΩ/1.3 kΩ pilot resistors so public stations handshake cleanly at 3 kW.[^86][^87]
- Happy Giraffe logged key Blade 10 hub dimensions.
  - 130 mm inner axle, ≈160 mm fork span, M12 threads with 10 mm flats, 12 mm rotor offset, and 4 mm hardware
  - helping G30 builders order forks, spacers, and brake adapters without guesswork.[^88]
- Wheelway honoured hall-board complaints for the cost of shipping, but replacements still arrive with inconsistent sensors, so bench-test every board before sealing the motor again.[^89][^90]
- Monorim’s rear footrest kit (~$69 on AliExpress) bolts straight onto Max frames for a quick stance change without fabrication.
  - handy when riders defer custom machining.[^91]

## Pre-Ride Checklist

1. **Firmware Audit** – Confirm VESC Tool version, traction-control settings, and BMS firmware before road tests to avoid regressions from recent 6.06 pairing issues.[^92][^8]
2. **Harness Inspection** – Verify bullet crimps, insulation, and ADC board grounds after every teardown; many “mystery” controller deaths trace back to workmanship lapses.[^93][^94]
3. **Telemetry Logging** – Capture CAN BMS current, controller temperatures, and GPS speed on each shakedown to validate power estimates and traction-control tuning.[^36][^95]
4. **Spare Components Ready** – Keep extra motors, throttle pods, and valve stems in the pit kit; wheelspin experiments and bead burps remain common during high-power tuning.[^72][^6]

## Compliance & Field Interaction

- Prepare polite proof-of-compliance for roadside checks. Rosheee’s 16 S scooter was seized until officers confirmed it held 22 km/h in eco mode despite 1.5 kW logs; homologation stickers and slow-mode profiles diffused the situation.[^96]

## Follow-up Tasks

- Capture Paolo’s pricing tiers and lead times for the 2 mm versus 3 mm rotor batches so riders can budget machining versus bolt-on fitment before committing to the group buy.[^97]
- Gather wiring diagrams showing how the front “local” controller shares throttle input over CAN so dual G300/Spintend stacks stay synchronised during future installs.[^98]

## Source Notes

- G30 conversion strategy, firmware prep, and traction-control tuning synthesize the late-2025 review of controller behaviour, positive ramp targets, and BMS firmware requirements logged by Smart Repair, Yamal, and fellow builders.[^99][^100]
- Battery sourcing, tariff impacts, and accessory planning pull from the same discussion covering premium cell costs, ANT BMS guardrails, and Voyage Megan/Express integration for 20–22 S projects.[^101][^102]
- Deck packaging experiments and travel-charging harness specs stem from the spring 2025 Max threads detailing 30–40 S pack prototypes and J1772 adapter wiring for 3 kW public charging runs.[^103][^104]
[^epowerfun]: Builders documented drilling and trimming the budget ePowerFun 3 mm floor plate as a temporary heatsink before commissioning thicker custom skid plates.[^105]
[^express_power]: VESC Express boards on G30 projects need external 5 V feeds (Spintend rails top out at 150 mA) and stable 6.05 firmware.
  - 6.06 restarts SD logging every three seconds until patched.[^106]
[^g30-pulldown]: G30 dash retrofits on Makerbase 75100s hinge on adding the pull-down resistor from pin 3; firmware 6.2 currently caps all modes around 60 % current so most builders stay on older releases.[^107]
[^bms-parity]: Stacking a healthy OEM 10 S pack with a DIY 4 S extender only worked after matching voltages and BMS discharge ratings; a sagging series stack blocked VESC detection until a regulated 60 V source replaced it.[^108]
[^g30-error10]: Makerbase 75100 V2 swaps trigger a “10 error” on the stock dash until you introduce the display to VESC Tool and program the controller.[^109]


## References

[^1]: Source: knowledge/notes/input_part014_review.md†L94-L104
[^2]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24505-L24536
[^3]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24521-L24524
[^4]: Source: knowledge/notes/input_part014_review.md†L105-L105
[^5]: Source: knowledge/notes/input_part014_review.md†L84-L87
[^6]: Source: knowledge/notes/input_part014_review.md†L107-L107
[^7]: Source: knowledge/notes/input_part005_review.md†L610-L610
[^8]: Source: knowledge/notes/input_part014_review.md†L103-L104
[^9]: Source: knowledge/notes/input_part009_review.md†L369-L369
[^10]: Source: knowledge/notes/denis_all_part02_review.md†L304-L305
[^11]: Source: knowledge/notes/input_part004_review.md†L220-L220
[^12]: Source: knowledge/notes/input_part004_review.md†L247-L248
[^13]: Source: data/vesc_help_group/text_slices/input_part003.txt†L9491-L9564
[^14]: Source: data/vesc_help_group/text_slices/input_part003.txt†L9536-L9561
[^15]: Source: data/vesc_help_group/text_slices/input_part003.txt†L10411-L10415
[^16]: Source: knowledge/notes/input_part014_review.md†L106-L106
[^17]: Source: knowledge/notes/input_part014_review.md†L118-L119
[^18]: Source: knowledge/notes/input_part006_review.md†L251-L251
[^19]: Source: knowledge/notes/input_part008_review.md†L18616-L18654
[^20]: Source: knowledge/notes/input_part014_review.md†L118-L118
[^21]: Source: knowledge/notes/input_part001_review.md†L617-L618
[^22]: Source: knowledge/notes/input_part000_review.md†L291-L291
[^23]: Source: knowledge/notes/input_part000_review.md†L374-L375
[^24]: Source: knowledge/notes/input_part000_review.md†L629-L629
[^25]: Source: knowledge/notes/input_part011_review.md†L33-L34
[^26]: Source: data/vesc_help_group/text_slices/input_part004.txt†L15986-L15997
[^27]: Source: knowledge/notes/input_part008_review.md†L15146-L15210
[^28]: Source: knowledge/notes/denis_all_part02_review.md†L203-L205
[^29]: Source: data/vesc_help_group/text_slices/input_part011.txt†L19101-L19173
[^30]: Source: data/vesc_help_group/text_slices/input_part011.txt†L19173-L19200
[^31]: Source: data/vesc_help_group/text_slices/input_part003.txt†L10501-L10570
[^32]: Source: data/vesc_help_group/text_slices/input_part003.txt†L21420-L21432
[^33]: Source: data/vesc_help_group/text_slices/input_part003.txt†L22104-L22190
[^34]: Source: knowledge/notes/input_part004_review.md†L298-L298
[^35]: Source: knowledge/notes/input_part014_review.md†L98-L101
[^36]: Source: knowledge/notes/input_part014_review.md†L79-L82
[^37]: Source: knowledge/notes/input_part000_review.md†L160-L160
[^38]: Source: knowledge/notes/input_part000_review.md†L681-L682
[^39]: Source: knowledge/notes/input_part000_review.md†L268-L269
[^40]: Source: knowledge/notes/input_part000_review.md†L371-L372
[^41]: Source: knowledge/notes/input_part012_review.md†L7997-L8008
[^42]: Source: knowledge/notes/input_part012_review.md†L8221-L8222
[^43]: Source: knowledge/notes/input_part003_review.md†L701-L748
[^44]: Source: data/vesc_help_group/text_slices/input_part003.txt†L10118-L10132
[^45]: Source: data/vesc_help_group/text_slices/input_part005.txt†L22957-L23024
[^46]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24652-L24661
[^47]: Source: knowledge/notes/input_part005_review.md†L606-L606
[^48]: Source: knowledge/notes/input_part010_review.md†L279-L280
[^49]: Source: knowledge/notes/input_part010_review.md†L331-L333
[^50]: Source: knowledge/notes/input_part010_review.md†L394-L395
[^51]: Source: knowledge/notes/input_part005_review.md†L607-L607
[^52]: Source: data/vesc_help_group/text_slices/input_part009.txt†L21900-L21939
[^53]: Source: knowledge/notes/input_part010_review.md†L285-L288
[^54]: Source: knowledge/notes/input_part010_review.md†L384-L386
[^55]: Source: knowledge/notes/input_part005_review.md†L206-L207
[^56]: Source: knowledge/notes/input_part005_review.md†L512-L512
[^57]: Source: knowledge/notes/input_part014_review.md†L84-L85
[^58]: Source: knowledge/notes/input_part014_review.md†L86-L86
[^59]: Source: knowledge/notes/input_part000_review.md†L296-L296
[^60]: Source: knowledge/notes/input_part001_review.md†L100-L100
[^61]: Source: knowledge/notes/input_part008_review.md†L215-L215
[^62]: Source: knowledge/notes/input_part010_review.md†L60-L60
[^63]: Source: knowledge/notes/input_part008_review.md†L216-L216
[^64]: Source: knowledge/notes/denis_all_part02_review.md†L99608-L99636
[^65]: Source: knowledge/notes/input_part008_review.md†L615-L617
[^66]: Source: knowledge/notes/input_part008_review.md†L217-L217
[^67]: Source: knowledge/notes/input_part005_review.md†L206-L208
[^68]: Source: knowledge/notes/input_part005_review.md†L248-L248
[^69]: Source: knowledge/notes/input_part014_review.md†L73-L76
[^70]: Source: knowledge/notes/input_part014_review.md†L119-L119
[^71]: Source: knowledge/notes/input_part011_review.md†L35-L35
[^72]: Source: knowledge/notes/input_part014_review.md†L46-L46
[^73]: Source: knowledge/notes/input_part005_review.md†L502-L502
[^74]: Source: knowledge/notes/input_part014_review.md†L43-L43
[^75]: Source: knowledge/notes/input_part000_review.md†L373-L374
[^76]: Source: knowledge/notes/input_part000_review.md†L247-L247
[^77]: Source: knowledge/notes/input_part000_review.md†L390-L390
[^78]: Source: knowledge/notes/input_part000_review.md†L391-L391
[^79]: Source: knowledge/notes/input_part014_review.md†L108-L108
[^80]: Source: knowledge/notes/input_part014_review.md†L206-L210
[^81]: Source: knowledge/notes/input_part014_review.md†L8506-L8506
[^82]: Source: knowledge/notes/input_part006_review.md†L254-L254
[^83]: Source: knowledge/notes/input_part008_review.md†L20808-L20831
[^84]: Source: knowledge/notes/input_part014_review.md†L110-L114
[^85]: Source: knowledge/notes/input_part014_review.md†L208-L210
[^86]: Source: knowledge/notes/input_part012_review.md†L10580-L10588
[^87]: Source: knowledge/notes/input_part012_review.md†L11100-L11129
[^88]: Source: data/vesc_help_group/text_slices/input_part000.txt†L20527-L20536
[^89]: Source: data/vesc_help_group/text_slices/input_part000.txt†L20403-L20406
[^90]: Source: data/vesc_help_group/text_slices/input_part000.txt†L20518-L20520
[^91]: Source: knowledge/notes/input_part013_review.md†L100-L100
[^92]: Source: knowledge/notes/input_part014_review.md†L29-L29
[^93]: Source: knowledge/notes/input_part014_review.md†L22-L22
[^94]: Source: knowledge/notes/input_part014_review.md†L84-L86
[^95]: Source: knowledge/notes/input_part014_review.md†L76-L76
[^96]: Source: knowledge/notes/input_part003_review.md†L705-L707
[^97]: Source: knowledge/notes/input_part014_review.md†L10356-L10365
[^98]: Source: knowledge/notes/input_part014_review.md†L10352-L10352
[^99]: Source: knowledge/notes/input_part014_review.md†L79-L119
[^100]: Source: knowledge/notes/input_part014_review.md†L84-L108
[^101]: Source: knowledge/notes/input_part014_review.md†L27-L114
[^102]: Source: knowledge/notes/input_part014_review.md†L98-L200
[^103]: Source: knowledge/notes/input_part012_review.md†L7997-L8222
[^104]: Source: knowledge/notes/input_part012_review.md†L10580-L11129
[^105]: Source: knowledge/notes/input_part014_review.md†L6301-L6325
[^106]: Source: knowledge/notes/input_part014_review.md†L5969-L6037
[^107]: Source: knowledge/notes/input_part007_review.md†L262-L262
[^108]: Source: knowledge/notes/input_part004_review.md†L13-L19
[^109]: Source: data/raw/telegram_exports/vesc_help_group/input_part007.json†L410572-L410744
[^g30_layouts]: Deck-layout and SNSC stem workflow reminder covering internal/external 20 S pack combos plus CNC stem/star-nut steps for fork swaps. Source: data/vesc_help_group/text_slices/input_part005.txt†L24505-L24536; L24652-L24661.
[^g30_front_disc]: Guidance on using a Ninebot Pro 2 front motor and custom spacers to add a front disc without a Monorim fork swap. Source: data/vesc_help_group/text_slices/input_part005.txt†L24468-L24477.
[^sns_prints]: SNSC sourcing and Bambu P1S accessory printing cues for rental-frame conversions. Source: data/vesc_help_group/text_slices/input_part005.txt†L24537-L24568; L24552-L24565.
