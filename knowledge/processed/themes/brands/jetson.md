# Jetson Bolt 20S Conversion Dossier

## Platform Snapshot
- Stock Jetson Bolt frames provide roughly 230 mm of dropout width, ship with a 36 V/6 Ah pack, and retain mounting points for a second motor, but the narrow “bean” battery cavity limits on-board electronics volume without printed enclosures or spacers.[^1]
- Successful community builds now target 72 V (20 S) packs while keeping battery current conservative—typically 30–50 A phase on the stock hub—to avoid overwhelming the small stator and dropouts.[^2]
- Field measurements peg the dropout closer to 230 mm and confirm the OEM hub tolerates ≈30 A at 72 V with active temperature monitoring; serious burnout torque calls for 12×6 (60 H) hubs that fit wider builds better than heavy 10" QS units.[^13]
- Haku’s reference commuter build runs a 20 S 3 P Samsung 35E pack, hydraulic discs, and a Spintend 85/150 controller, demonstrating ~50 mile real-world range when power is capped near 1.6 kW to control heat.[^3]

## Packaging & Mechanical Fitment
- The OEM bay can swallow folded 20 S packs if cells are arranged with custom PETG/ABS carriers; shared STL sets extend the compartment and add removable covers for balance-lead routing and BMS mounting.[^4]
- Full-size VESCs rarely fit internally; builders lean on Mini Ubox/Lite-class controllers or external mounts, and test-fit any 10" QS hub alternatives because the stock swingarm cannot accept their width or mass without reinforcement.[^5]
- NetworkDir recommends 12×6 (60 H) Lonnyo hubs for 20 S burnout builds since their higher resistance/lower Kv characteristics suit the frame once torque arms and reinforcement are in place.[^13]
- Before structural mods, spin the hub on a current-limited bench supply, discharge capacitors, and confirm the direct-drive core (no plastic reduction gears) so shunt mods or dual-motor brackets don’t mask mechanical drag.[^6]

### Quick Fitment Checklist
| Inspection | Pass Criteria | Mitigation if Failed |
| --- | --- | --- |
| Dropout clearance | ≤230 mm hub with stock spacers seats without bearing preload | Retain OEM motor or machine new swingarms before attempting 10″ QS swaps.[^1] |
| Controller envelope | Mini-format VESC (e.g., single Lite, Voyage Megan bundle) seats under deck or on external plate | Relocate controller externally and budget for CAN display cabling when internal space is exhausted.[^5] |
| Battery carrier | Printed tray supports 20 S wiring, balance leads, and BMS without flexing under heat | Reprint in higher infill PETG/nylon, add mesh protectors, or step down to 16–18 S while iterating holders.[^4] |

## Electrical Guardrails
- Keep battery current moderate (≈30 A per motor, ≤50 A phase) on the stock hub; Sabvoton and Spintend users alike report thermal saturation or outright motor burnout when sustained current exceeds this envelope.[^2]
- Monitor 72 V shakedowns closely—community feedback caps the OEM hub at ~30 A battery until upgraded motors arrive, even though voltage experiments continue.[^10]
- Configure VESC low-voltage cutoffs around 72 V start / 65 V end for 20–22 S experimentation, double-checking the cell count so undervoltage faults do not appear mid-ride.[^7]
- Stay within 20 S on unmodified HY/Spintend stages; repeated high-voltage faults persisted even after setting an 85 V cap, and vendor guidance warns 21–22 S requires hardware-level filtering.[^3]
- Protect controllers from BMS cut-outs—Flipsky 75xxx units have died after a single regen-triggered trip—by matching regen to BMS thresholds and avoiding sudden pack disconnects.[^8]

## Control & Firmware Setup
- If hall detection fails, rerun Motor Wizard after verifying hall continuity; temporarily enable VSS zero-start with ERPM loop set to zero to keep launches smooth until sensors pass detection.[^9]
- Once halls work, log inductance/resistance (≈493 µH / 175 mΩ on reference builds) and cap estimated phase output (~70 A) until thermal behavior is validated.[^9]
- Any shunt or controller swap should begin on a 30–50 mA current-limited bench supply to catch shorts before connecting the full pack.[^10]
- Spintend ADC rails are cramped inside the Jetson chassis—power auxiliary lighting from a dedicated DC-DC converter rather than loading the controller logic rail.[^11]

## Thermal & Performance Management
- Expect the hub to overheat once the stator is heat-soaked; practical street duty keeps output around 1.6 kW and avoids field weakening, which has fried stock motors at only 4 A in testing.[^3]
- Haku still refuses to run field weakening after killing multiple stock hubs at ~4 A—he limits the Jetson to 20 S commuter duty with hydraulic brakes and monitors stator temps closely on long errands.【F:knowledge/notes/input_part011_review.md†L322-L332】
- Monitor voltage discrepancies between VESC Tool and the JBD BMS—the readings often converge only under load, making it easy to misdiagnose faults during bench tests.[^3]
- Avoid field-weakening experiments until cooling upgrades (ferrofluid, heatsinks, forced airflow) are proven; modest FW increments still spike both battery and phase current on this platform.[^3]

## Lighting, Brakes & Daily Use
- Budget-friendly hydraulic conversions and DOT brake fluid dramatically improve stopping power; riders report reliable modulation even after controller swaps so long as the hub remains direct drive.[^6]
- Space constraints favor external or printed light mounts—consider USB-rechargeable bars or flashlight setups, and isolate their power supplies to prevent noise on the control harness.[^11]
- For delivery or commuter duty, plan for swappable battery modules or higher-capacity cells only after validating shift length; 5 Ah-class cells add ~0.8 kWh versus P42A baselines but may demand enclosure redesigns.[^12]

## Ownership & Resale Outlook
- Custom Jetson builds with 20 S 3 P packs, JBD BMS, Spintend 85/150 controllers, and hydraulic discs are fetching offers around $400, but owners weigh family hand-me-down plans and evolving regulations before selling.【F:knowledge/notes/input_part011_review.md†L327-L332】

## Build Readiness Checklist
1. **Document pack layout and connector choices** before sealing the battery bay so future service can trace balance leads.[^4]
2. **Log thermal data on shakedown rides** (motor temp, controller temp, voltage sag) to confirm the 1.6 kW ceiling keeps the hub within safe operating range.[^3]
3. **Validate regen and brake interaction** with incremental tests to ensure the BMS never drops the controller offline under hard braking.[^8]
4. **Capture wiring diagrams and VESC XML backups** once hall sensors, DC-DC converters, and lighting harnesses are stable, streamlining future troubleshooting.[^9]

## Source Notes
[^1]: Jetson Bolt dropout width, stock battery cavity limits, and second-motor mounting points plus warnings against 10″ QS hub swaps.【F:knowledge/notes/input_part010_review.md†L556-L558】
[^2]: Community guidance to hold phase current near 30–50 A on 72 V Jetson builds and sustained-current anecdotes around 72 V Sabvoton conversions.【F:knowledge/notes/input_part010_review.md†L557-L557】【F:knowledge/notes/input_part010_review.md†L670-L670】
[^3]: Jetson 20 S 3 P Samsung 35E pack performance, 1.6 kW cap, high-voltage faults despite 85 V limits, long-range usage notes, and field-weakening burnout cautions.【F:knowledge/notes/input_part011_review.md†L15-L15】【F:knowledge/notes/input_part011_review.md†L55-L58】【F:knowledge/notes/input_part011_review.md†L301-L304】
[^4]: Printable Jetson battery carriers, compartment extensions, and mesh-protected holders for compact frames.【F:knowledge/notes/input_part010_review.md†L558-L559】【F:knowledge/notes/input_part010_review.md†L627-L627】
[^5]: Mini-format VESC requirements, lack of internal space for full-size controllers, and hub fitment cautions for wide motors.【F:knowledge/notes/input_part010_review.md†L583-L583】【F:knowledge/notes/input_part010_review.md†L556-L558】
[^6]: Bench-supply spin tests, dual-motor mounting provisions, and confirmation that the Jetson hub is direct drive with proven four-piston brake upgrades.【F:knowledge/notes/input_part010_review.md†L559-L560】
[^7]: Recommended VESC low-voltage start/end values for 22 S Jetson experiments to avoid undervoltage flags.【F:knowledge/notes/input_part010_review.md†L343-L343】
[^8]: Controller failures tied to BMS cut-offs and regen spikes on Flipsky hardware plus general caution about sudden pack disconnects.【F:knowledge/notes/input_part011_review.md†L15-L15】【F:knowledge/notes/input_part011_review.md†L53-L53】
[^9]: Jetson hall-detection troubleshooting, sensorless zero-start fallback, post-detection electrical measurements, and the need to re-run motor detection after wiring fixes.【F:knowledge/notes/input_part011_review.md†L10-L14】
[^10]: Community reminder to power suspect hardware on a 30–50 mA current-limited bench supply before connecting full packs.【F:knowledge/notes/input_part011_review.md†L186-L187】
[^11]: Advice to power Jetson lighting from dedicated DC-DC converters because ADC expanders are space-constrained in this chassis.【F:knowledge/notes/input_part011_review.md†L142-L142】
[^12]: Delivery-range planning discussions weighing higher-capacity cells versus packaging limits for commuter duty.【F:knowledge/notes/input_part011_review.md†L145-L147】
[^13]: OEM Jetson hub current tolerance (~30 A at 72 V), dropout measurement, and 12×6 (60 H) hub recommendations for higher-torque 20 S builds.【F:knowledge/notes/input_part010_review.md†L60-L62】
