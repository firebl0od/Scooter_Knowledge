# Ninebot G30 VESC Conversion Playbook

## TL;DR
- The G30 Max remains the friendliest chassis for VESC swaps thanks to abundant deck space, aftermarket spacers, and new BMS firmware that unlocks >20 A discharge without extra comms harnesses.【F:knowledge/notes/input_part014_review.md†L94-L104】
- Real-world 16 S builds with Ubox 100/100 controllers and 65 H 17×4 motors hit ~45 mph on 50 A field weakening yet still average roughly 1 mile per amp-hour, proving battery upgrades deliver the biggest gains before motor swaps.【F:knowledge/notes/input_part014_review.md†L105-L105】
- Traction control, throttle filtering, and thermal management are mandatory as phase limits climb toward 300 A; positive ramp times (~0.4 s) and careful ADC tuning tame wheelspin and runaway spikes on lightweight decks.【F:knowledge/notes/input_part014_review.md†L84-L87】【F:knowledge/notes/input_part014_review.md†L107-L107】

## Base Scooter Preparation
- Flash the latest ScooterHacking G30 BMS firmware to lift discharge ceilings past 20 A while retaining stock harnesses—essential before pushing VESC phase currents.【F:knowledge/notes/input_part014_review.md†L103-L104】
- Strip the frame and inspect deck welds prior to grinding rails for larger packs; documented builds plan rail relief plus 3 mm aluminum skid plates as interim reinforcement.【F:knowledge/notes/input_part014_review.md†L106-L106】【F:knowledge/notes/input_part014_review.md†L118-L119】
- Choose battery spacers carefully: JREV units add cable room but misalign slightly with the frame, so plan shims or revised prints when targeting 22 S layouts.【F:knowledge/notes/input_part014_review.md†L118-L118】

## Powertrain Reference Builds
| Configuration | Controllers & Limits | Reported Performance | Notes |
| --- | --- | --- | --- |
| 16 S commuter | Dual Ubox 100/100, Ortega observers, 50 A FW start at 87 % duty | ≈45 mph top speed, ~59 A peaks, ~1 mile per amp-hour above 20 mph | Prioritize battery capacity and cooling before chasing new motors; FW headroom exists but watch temperature logs.【F:knowledge/notes/input_part014_review.md†L105-L105】 |
| 20 S stealth upgrade | Planned 20 S4 P 50PL pack with rail grinding and future 50 kW target | In progress—emphasizes fabrication burden (deck grinding, spacer redesign, pack sourcing) | Budget premium cells (50PL/P45B) and labor; expect cost doubling over 30Q baselines.【F:knowledge/notes/input_part014_review.md†L106-L106】 |
| 22 S race prep | Targeting 22×3 or 33×2 motors, 300 A phase, positive ramp ~0.4 s | Focus on traction control slip windows (11 k–17 k rpm) to avoid wheelspin | Requires spare motors and throttle filtering to mitigate spike-induced controller shutdowns.【F:knowledge/notes/input_part014_review.md†L84-L87】【F:knowledge/notes/input_part014_review.md†L107-L107】 |

## Battery & BMS Planning
- Budget packs starting with 20 S Samsung 30Q quotes for commuters, but expect premium 21700 builds (50PL, P45B/P50B) to double total cost once welding, insulation, and shipping are included.【F:knowledge/notes/input_part014_review.md†L106-L106】
- ANT smart BMS units have latched discharge FETs under Spintend-level currents; plan redundant pack protection (loop keys, fuse boards, or dual BMS) for >300 A goals.【F:knowledge/notes/input_part014_review.md†L98-L101】
- Calibrate CAN smart BMS logs against VESC telemetry—BMS current remains more trustworthy but may drift; manual calibration preserves ±500 W accuracy on 35 kW builds.【F:knowledge/notes/input_part014_review.md†L79-L82】
- Jason’s Max project already packaged a 30 S pack around a 65H 17×4 motor and scoped a fully internal 40 S/3 P layout, proving the deck ceiling once partitions are trimmed and harness routing is planned early.【F:knowledge/notes/input_part012_review.md†L7997-L8008】【F:knowledge/notes/input_part012_review.md†L8221-L8222】

## Control & Traction Tuning
- Compress throttle ADC ranges (treat ~0.83 V as idle, activate around 1.0–1.2 V) to eliminate noise-triggered surges on Spintend 100/100 installs.【F:knowledge/notes/input_part014_review.md†L84-L85】
- Grounding the chassis cured runaway acceleration for some riders, but document the wiring and verify insulation to avoid frame shorts before adopting the fix broadly.【F:knowledge/notes/input_part014_review.md†L86-L86】
- Log traction control adjustments during every shakedown; slip thresholds between 11 k and 17 k rpm and positive throttle ramps (~0.4 s) kept lightweight builds controllable at 300 A phase.【F:knowledge/notes/input_part014_review.md†L107-L107】

## Thermal & Mechanical Safeguards
- Monitor per-motor temperatures; aim for ≤45 °C controller temps and ≤90–100 °C stator temps by refreshing thermal paste and clamping controllers to thick skid plates.【F:knowledge/notes/input_part014_review.md†L73-L76】【F:knowledge/notes/input_part014_review.md†L119-L119】
- Plan for valve-stem service and bead reseating after pothole hits—tubeless split rims can burp air, so keep compressors and soapy water handy during test rides.【F:knowledge/notes/input_part014_review.md†L46-L46】
- Evaluate braking upgrades alongside power mods; 203 mm rotors add leverage but may be overkill—pair regen tuning with quality hydraulic calipers and DOT 4/5 fluid first.【F:knowledge/notes/input_part014_review.md†L43-L43】
- Use the €25 ePowerFun 3 mm aluminum floor plate as a quick cooling stopgap—drill five mounting holes, trim the nose to clear JREV spacers, and plan a thicker custom plate once testing confirms heat loads.[^epowerfun]
- Inspect swingarms for fatigue before raising power—stock arms have cracked at the deck cut-outs under ~130 kg loads, so add gusset plates that spread torque around the rear fork bracket and verify axle hardware after bearing swaps.【F:knowledge/notes/input_part006_review.md†L13-L15】
- Machine the swingarm axle if you plan to run 11 inch hubs; forcing wider hubs into stock arms ruins alignment and clearance.【F:knowledge/notes/input_part006_review.md†L34-L34】
- Clean corroded hubs mechanically with drill-mounted wire brushes instead of chemical baths to avoid residue in reusable motors.【F:knowledge/notes/input_part006_review.md†L77-L77】

## Sourcing & Accessory Integration
- Avoid too-good-to-be-true controller deals: £50 AliExpress listings are often bare logic boards; prioritize complete Spintend 100/100 Lite kits or 84/150 bundles from trusted resellers to get full harnesses.【F:knowledge/notes/input_part014_review.md†L108-L108】
- Panel-mount QS8 connectors remain custom-only; draft plates early or leverage community prints to keep high-current leads tidy once deck space tightens.【F:knowledge/notes/input_part014_review.md†L8506-L8506】
- Consider Voyage Megan or other CAN dashboards for consolidated telemetry once controllers are upgraded; validate compatibility when mixing CL350 or Express accessories with Ubox hardware.【F:knowledge/notes/input_part014_review.md†L110-L114】【F:knowledge/notes/input_part014_review.md†L208-L210】
- Budget a dedicated buck converter if you add VESC Express boards—the modules only accept 5 V at ~150 mA and currently reset logging every few seconds on 6.06 firmware, so plan CAN updates or stay on 6.05 for stable telemetry.[^express_power]
- Document J1772 travel adapters as part of the charging kit: a proven harness uses 12 AWG silicone leads plus 2.5 mm² wiring with 2.74 kΩ/1.3 kΩ pilot resistors so public stations handshake cleanly at 3 kW.【F:knowledge/notes/input_part012_review.md†L10580-L10588】【F:knowledge/notes/input_part012_review.md†L11100-L11129】
- Repurpose spare Xiaomi/Ninebot ESCs as interim controllers when budgets are tight—the community bundles precharge cabling and 3D-printed mounts so M365 boards can live inside G30 frames until dual VESC packages are ready.【F:knowledge/notes/input_part006_review.md†L489-L489】

## Pre-Ride Checklist
1. **Firmware Audit** – Confirm VESC Tool version, traction-control settings, and BMS firmware before road tests to avoid regressions from recent 6.06 pairing issues.【F:knowledge/notes/input_part014_review.md†L29-L29】【F:knowledge/notes/input_part014_review.md†L103-L104】
2. **Harness Inspection** – Verify bullet crimps, insulation, and ADC board grounds after every teardown; many “mystery” controller deaths trace back to workmanship lapses.【F:knowledge/notes/input_part014_review.md†L22-L22】【F:knowledge/notes/input_part014_review.md†L84-L86】
3. **Telemetry Logging** – Capture CAN BMS current, controller temperatures, and GPS speed on each shakedown to validate power estimates and traction-control tuning.【F:knowledge/notes/input_part014_review.md†L79-L82】【F:knowledge/notes/input_part014_review.md†L76-L76】
4. **Spare Components Ready** – Keep extra motors, throttle pods, and valve stems in the pit kit; wheelspin experiments and bead burps remain common during high-power tuning.【F:knowledge/notes/input_part014_review.md†L46-L46】【F:knowledge/notes/input_part014_review.md†L107-L107】

## Motor & Performance Notes
- Stock G30 hubs can manage ≈80 km/h solo or ~98 km/h in dual-motor setups, but one motor hauling a 90 kg rider plus 75 kg passenger up hills at 40 A cooked its insulation—respect thermal limits when loading scooters for tandem rides.【F:knowledge/notes/input_part006_review.md†L112-L114】
- Lonnyo 70H hubs use 6003 rotor-side and 6008 stator-side bearings; torque-focused 22×3 winds respond well to ~400 A phase yet even 400 A won’t guarantee burnouts on grippy 11″ PMTs without mid-drive help.【F:knowledge/notes/input_part006_review.md†L114-L114】
- Dual 70 mm hubs still plateau near 150 km/h at sea level regardless of 22 S vs. 30 S pack voltage because phase-current ceilings, not voltage, cap acceleration.【F:knowledge/notes/input_part006_review.md†L115-L115】
- Holding 158 km/h on streamlined builds draws roughly 26–28 kW, and doubling speed from 100 km/h demands ~52–64 kW due to cubic aero losses—plan gearing alongside power headroom.【F:knowledge/notes/input_part006_review.md†L116-L116】
- Despite marketing claims, 3Shul CL controllers only run safely around 29–30 S without regen; the 135 V FET stack leaves little spike headroom and the onboard 12 V DC/DC sags below 1 A, so budget external supplies for high-voltage experiments.【F:knowledge/notes/input_part006_review.md†L117-L117】

## Source Notes
- G30 conversion strategy, firmware prep, and traction-control tuning synthesize the late-2025 review of controller behaviour, positive ramp targets, and BMS firmware requirements logged by Smart Repair, Yamal, and fellow builders.【F:knowledge/notes/input_part014_review.md†L79-L119】【F:knowledge/notes/input_part014_review.md†L84-L108】
- Battery sourcing, tariff impacts, and accessory planning pull from the same discussion covering premium cell costs, ANT BMS guardrails, and Voyage Megan/Express integration for 20–22 S projects.【F:knowledge/notes/input_part014_review.md†L27-L114】【F:knowledge/notes/input_part014_review.md†L98-L200】
- Deck packaging experiments and travel-charging harness specs stem from the spring 2025 Max threads detailing 30–40 S pack prototypes and J1772 adapter wiring for 3 kW public charging runs.【F:knowledge/notes/input_part012_review.md†L7997-L8222】【F:knowledge/notes/input_part012_review.md†L10580-L11129】
[^epowerfun]: Builders documented drilling and trimming the budget ePowerFun 3 mm floor plate as a temporary heatsink before commissioning thicker custom skid plates.【F:knowledge/notes/input_part014_review.md†L6301-L6325】
[^express_power]: VESC Express boards on G30 projects need external 5 V feeds (Spintend rails top out at 150 mA) and stable 6.05 firmware—6.06 restarts SD logging every three seconds until patched.【F:knowledge/notes/input_part014_review.md†L5969-L6037】
