# Ninebot G30 VESC Conversion Playbook

## TL;DR
- The G30 Max remains the friendliest chassis for VESC swaps thanks to abundant deck space, aftermarket spacers, and new BMS firmware that unlocks >20 A discharge without extra comms harnesses.【F:knowledge/notes/input_part014_review.md†L94-L104】
- Real-world 16 S builds with Ubox 100/100 controllers and 65 H 17×4 motors hit ~45 mph on 50 A field weakening yet still average roughly 1 mile per amp-hour, proving battery upgrades deliver the biggest gains before motor swaps.【F:knowledge/notes/input_part014_review.md†L105-L105】
- Traction control, throttle filtering, and thermal management are mandatory as phase limits climb toward 300 A; positive ramp times (~0.4 s) and careful ADC tuning tame wheelspin and runaway spikes on lightweight decks.【F:knowledge/notes/input_part014_review.md†L84-L87】【F:knowledge/notes/input_part014_review.md†L107-L107】

## Base Scooter Preparation
- Flash the latest ScooterHacking G30 BMS firmware to lift discharge ceilings past 20 A while retaining stock harnesses—essential before pushing VESC phase currents.【F:knowledge/notes/input_part014_review.md†L103-L104】
- Strip the frame and inspect deck welds prior to grinding rails for larger packs; documented builds plan rail relief plus 3 mm aluminum skid plates as interim reinforcement.【F:knowledge/notes/input_part014_review.md†L106-L106】【F:knowledge/notes/input_part014_review.md†L118-L119】
- Choose battery spacers carefully: JREV units add cable room but misalign slightly with the frame, so plan shims or revised prints when targeting 22 S layouts.【F:knowledge/notes/input_part014_review.md†L118-L118】
- Expect the stock ESC to refuse third-party 1 kW hubs—the controller looks for Ninebot’s protocol, so non-OEM motors demand a custom FOC flash or a full VESC swap, and the housings need steel adapters just to clear the fork.【F:knowledge/notes/input_part001_review.md†L617-L618】
- Reseal the deck lid and servo-lock cavity after grinding ribs—builders report lost waterproofing unless silicone is restored and the servo void is capped or reused for accessories.【F:knowledge/notes/input_part000_review.md†L291-L291】
- Printed deck extenders and 2 mm spacer shims free vertical clearance for BMS harness exits when stacking externals—plan wiring height early so lids close without crushing leads.【F:knowledge/notes/input_part000_review.md†L374-L375】
- Rental G30 chassis earn premium status: fixed stems, dual brakes, oil suspension, and thicker tubing swallow 13 S 5 P 21700 packs plus 1.2 kW hubs without the flex or wobble of stock Xiaomi frames—expect ~10 kg more steel but far less frame twist under launch torque.【F:knowledge/notes/input_part000_review.md†L629-L629】

## Powertrain Reference Builds
| Configuration | Controllers & Limits | Reported Performance | Notes |
| --- | --- | --- | --- |
| 16 S commuter | Dual Ubox 100/100, Ortega observers, 50 A FW start at 87 % duty | ≈45 mph top speed, ~59 A peaks, ~1 mile per amp-hour above 20 mph | Prioritize battery capacity and cooling before chasing new motors; FW headroom exists but watch temperature logs.【F:knowledge/notes/input_part014_review.md†L105-L105】 |
| 20 S stealth upgrade | Planned 20 S4 P 50PL pack with rail grinding and future 50 kW target | In progress—emphasizes fabrication burden (deck grinding, spacer redesign, pack sourcing) | Budget premium cells (50PL/P45B) and labor; expect cost doubling over 30Q baselines.【F:knowledge/notes/input_part014_review.md†L106-L106】 |
| 22 S race prep | Targeting 22×3 or 33×2 motors, 300 A phase, positive ramp ~0.4 s | Focus on traction control slip windows (11 k–17 k rpm) to avoid wheelspin | Requires spare motors and throttle filtering to mitigate spike-induced controller shutdowns.【F:knowledge/notes/input_part014_review.md†L84-L87】【F:knowledge/notes/input_part014_review.md†L107-L107】 |

## Battery & BMS Planning
- Budget packs starting with 20 S Samsung 30Q quotes for commuters, but expect premium 21700 builds (50PL, P45B/P50B) to double total cost once welding, insulation, and shipping are included.【F:knowledge/notes/input_part014_review.md†L106-L106】
- P45B cells win on energy density, yet 30T’s ~5 mΩ resistance still suits riders chasing peak discharge bursts—log goals before picking chemistry for Max deck rebuilds.【F:data/vesc_help_group/text_slices/input_part003.txt†L10501-L10570】
- Pair motor choices with those packs: Monorim/Xiaomi hub variants range from commuter 28 kV cores that prefer ≤80 A phase to speed-wound 32 kV units that tolerate 110–120 A when hall sensors stay healthy—retire cracked magnets or failing halls before adding voltage.【F:data/vesc_help_group/text_slices/input_part003.txt†L21420-L21432】【F:data/vesc_help_group/text_slices/input_part003.txt†L22104-L22190】
- ANT smart BMS units have latched discharge FETs under Spintend-level currents; plan redundant pack protection (loop keys, fuse boards, or dual BMS) for >300 A goals.【F:knowledge/notes/input_part014_review.md†L98-L101】
- Calibrate CAN smart BMS logs against VESC telemetry—BMS current remains more trustworthy but may drift; manual calibration preserves ±500 W accuracy on 35 kW builds.【F:knowledge/notes/input_part014_review.md†L79-L82】
- Ninebot Max decks can house 50 Ah 10 S bricks or even 15 S 4 P 21700 arrays once controllers move outboard, giving tour-focused builds room for 260-cell packs before adding externals.【F:knowledge/notes/input_part000_review.md†L160-L160】
- Source 220 mm shrink early for “thick” 13 S 5 P 21700 rental packs—EU builders are rationing wide sleeves and supplementing with 0.25–0.30 mm copper straps so each series bridge handles ≥35–40 A without bottlenecking the new pack volume.【F:knowledge/notes/input_part000_review.md†L681-L682】
- Mirono’s rental-frame build squeezed a Daly smart BMS and 13 S 5 P NCR21700A pack inside after grinding internal ribs, with copper “sandwich” busbars on standby if field weakening needs lower resistance.【F:knowledge/notes/input_part000_review.md†L268-L269】
- Expect AWG10 mains (or dual AWG12 runs) once battery current targets hit 90 A—crews even drop 3–3.5 mm solid copper between pack negatives and BMS plates to keep voltage drop in check.【F:knowledge/notes/input_part000_review.md†L371-L372】
- Jason’s Max project already packaged a 30 S pack around a 65H 17×4 motor and scoped a fully internal 40 S/3 P layout, proving the deck ceiling once partitions are trimmed and harness routing is planned early.【F:knowledge/notes/input_part012_review.md†L7997-L8008】【F:knowledge/notes/input_part012_review.md†L8221-L8222】
- Treat the Ninebot P100 pack as a reminder that chassis upgrades can outpace energy storage—its 52 V 23 Ah battery only returns about 25 mi at 30 mph until firmware efficiency improves, so budget range upgrades alongside structural swaps.【F:knowledge/notes/input_part003_review.md†L701-L748】
- Long-range G30 builds still fight motor heat even when they boast “endless power”—plan ferrofluid, spare motors for regen-only duty, or newer hub generations if you promise high-speed touring.【F:data/vesc_help_group/text_slices/input_part003.txt†L9536-L9561】
- Vsett 9 frames can internalize 52 V 30 Ah packs—and even standing 20 S8 P stacks with spacers—providing inspiration for auxiliary battery pods or cross-frame transplants on Max conversions.【F:data/vesc_help_group/text_slices/input_part003.txt†L10118-L10132】
- A 21 S Zero 11X pack with ~0.002 V delta showcased proper busbars and heavy-gauge cabling for big-wheel race builds—borrow its harness and reinforcement ideas when scaling Max packs beyond commuter duty.【F:data/vesc_help_group/text_slices/input_part003.txt†L10411-L10415】

## Control & Traction Tuning
- Compress throttle ADC ranges (treat ~0.83 V as idle, activate around 1.0–1.2 V) to eliminate noise-triggered surges on Spintend 100/100 installs.【F:knowledge/notes/input_part014_review.md†L84-L85】
- Grounding the chassis cured runaway acceleration for some riders, but document the wiring and verify insulation to avoid frame shorts before adopting the fix broadly.【F:knowledge/notes/input_part014_review.md†L86-L86】
- Log traction control adjustments during every shakedown; slip thresholds between 11 k and 17 k rpm and positive throttle ramps (~0.4 s) kept lightweight builds controllable at 300 A phase.【F:knowledge/notes/input_part014_review.md†L107-L107】
- When upgrading to hydraulic fronts, transplant the stock hall sensor and magnet into the new lever so proportional regen survives the swap and rear mechanical brakes can stay untouched.【F:knowledge/notes/input_part000_review.md†L296-L296】

## Thermal & Mechanical Safeguards
- Monitor per-motor temperatures; aim for ≤45 °C controller temps and ≤90–100 °C stator temps by refreshing thermal paste and clamping controllers to thick skid plates.【F:knowledge/notes/input_part014_review.md†L73-L76】【F:knowledge/notes/input_part014_review.md†L119-L119】
- Plan for valve-stem service and bead reseating after pothole hits—tubeless split rims can burp air, so keep compressors and soapy water handy during test rides.【F:knowledge/notes/input_part014_review.md†L46-L46】
- Evaluate braking upgrades alongside power mods; 203 mm rotors add leverage but may be overkill—pair regen tuning with quality hydraulic calipers and DOT 4/5 fluid first.【F:knowledge/notes/input_part014_review.md†L43-L43】
- Use the €25 ePowerFun 3 mm aluminum floor plate as a quick cooling stopgap—drill five mounting holes, trim the nose to clear JREV spacers, and plan a thicker custom plate once testing confirms heat loads.[^epowerfun]
- Transparent plexiglass lids look great but need threadlocker, silicone seals, and stronger epoxy/two-part adhesive for LED strips—6 mm sheets crack without extra support, especially around temperature swings.【F:knowledge/notes/input_part000_review.md†L373-L374】
- High-speed conversions (70 km/h GPS on 48 V delta/star rewires) demand wider bars and frame reinforcement before daily riding; treat chassis upgrades as mandatory at those velocities.【F:knowledge/notes/input_part000_review.md†L247-L247】

## Hall Sensor Service & Orientation
- Replace failed halls with matching switch types (SS41F vs. R43) and keep the stamped face aligned; mismatches hold ~2 V output and block motor detection until reinstalled correctly.【F:knowledge/notes/input_part000_review.md†L390-L390】
- After sensor swaps, rerun motor detection and temporarily cap limits near 40 A battery / 80 A phase while sourcing spares to avoid repeated tear-downs.【F:knowledge/notes/input_part000_review.md†L391-L391】

## Sourcing & Accessory Integration
- Avoid too-good-to-be-true controller deals: £50 AliExpress listings are often bare logic boards; prioritize complete Spintend 100/100 Lite kits or 84/150 bundles from trusted resellers to get full harnesses.【F:knowledge/notes/input_part014_review.md†L108-L108】
- Panel-mount QS8 connectors remain custom-only; draft plates early or leverage community prints to keep high-current leads tidy once deck space tightens.【F:knowledge/notes/input_part014_review.md†L8506-L8506】
- Consider Voyage Megan or other CAN dashboards for consolidated telemetry once controllers are upgraded; validate compatibility when mixing CL350 or Express accessories with Ubox hardware.【F:knowledge/notes/input_part014_review.md†L110-L114】【F:knowledge/notes/input_part014_review.md†L208-L210】
- Budget a dedicated buck converter if you add VESC Express boards—the modules only accept 5 V at ~150 mA and currently reset logging every few seconds on 6.06 firmware, so plan CAN updates or stay on 6.05 for stable telemetry.[^express_power]
- Document J1772 travel adapters as part of the charging kit: a proven harness uses 12 AWG silicone leads plus 2.5 mm² wiring with 2.74 kΩ/1.3 kΩ pilot resistors so public stations handshake cleanly at 3 kW.【F:knowledge/notes/input_part012_review.md†L10580-L10588】【F:knowledge/notes/input_part012_review.md†L11100-L11129】
- Happy Giraffe logged key Blade 10 hub dimensions—130 mm inner axle, ≈160 mm fork span, M12 threads with 10 mm flats, 12 mm rotor offset, and 4 mm hardware—helping G30 builders order forks, spacers, and brake adapters without guesswork.【F:data/vesc_help_group/text_slices/input_part000.txt†L20527-L20536】
- Wheelway honoured hall-board complaints for the cost of shipping, but replacements still arrive with inconsistent sensors, so bench-test every board before sealing the motor again.【F:data/vesc_help_group/text_slices/input_part000.txt†L20403-L20406】【F:data/vesc_help_group/text_slices/input_part000.txt†L20518-L20520】

## Pre-Ride Checklist
1. **Firmware Audit** – Confirm VESC Tool version, traction-control settings, and BMS firmware before road tests to avoid regressions from recent 6.06 pairing issues.【F:knowledge/notes/input_part014_review.md†L29-L29】【F:knowledge/notes/input_part014_review.md†L103-L104】
2. **Harness Inspection** – Verify bullet crimps, insulation, and ADC board grounds after every teardown; many “mystery” controller deaths trace back to workmanship lapses.【F:knowledge/notes/input_part014_review.md†L22-L22】【F:knowledge/notes/input_part014_review.md†L84-L86】
3. **Telemetry Logging** – Capture CAN BMS current, controller temperatures, and GPS speed on each shakedown to validate power estimates and traction-control tuning.【F:knowledge/notes/input_part014_review.md†L79-L82】【F:knowledge/notes/input_part014_review.md†L76-L76】
4. **Spare Components Ready** – Keep extra motors, throttle pods, and valve stems in the pit kit; wheelspin experiments and bead burps remain common during high-power tuning.【F:knowledge/notes/input_part014_review.md†L46-L46】【F:knowledge/notes/input_part014_review.md†L107-L107】

## Compliance & Field Interaction
- Prepare polite proof-of-compliance for roadside checks. Rosheee’s 16 S scooter was seized until officers confirmed it held 22 km/h in eco mode despite 1.5 kW logs; homologation stickers and slow-mode profiles diffused the situation.【F:knowledge/notes/input_part003_review.md†L705-L707】

## Source Notes
- G30 conversion strategy, firmware prep, and traction-control tuning synthesize the late-2025 review of controller behaviour, positive ramp targets, and BMS firmware requirements logged by Smart Repair, Yamal, and fellow builders.【F:knowledge/notes/input_part014_review.md†L79-L119】【F:knowledge/notes/input_part014_review.md†L84-L108】
- Battery sourcing, tariff impacts, and accessory planning pull from the same discussion covering premium cell costs, ANT BMS guardrails, and Voyage Megan/Express integration for 20–22 S projects.【F:knowledge/notes/input_part014_review.md†L27-L114】【F:knowledge/notes/input_part014_review.md†L98-L200】
- Deck packaging experiments and travel-charging harness specs stem from the spring 2025 Max threads detailing 30–40 S pack prototypes and J1772 adapter wiring for 3 kW public charging runs.【F:knowledge/notes/input_part012_review.md†L7997-L8222】【F:knowledge/notes/input_part012_review.md†L10580-L11129】
[^epowerfun]: Builders documented drilling and trimming the budget ePowerFun 3 mm floor plate as a temporary heatsink before commissioning thicker custom skid plates.【F:knowledge/notes/input_part014_review.md†L6301-L6325】
[^express_power]: VESC Express boards on G30 projects need external 5 V feeds (Spintend rails top out at 150 mA) and stable 6.05 firmware—6.06 restarts SD logging every three seconds until patched.【F:knowledge/notes/input_part014_review.md†L5969-L6037】
