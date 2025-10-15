# Tronic Controllers Brand Dossier

## TL;DR
- Race tuners now treat the six-FET Tronic 250 family as ~200 A hardware—pushing toward the marketing 250 A claims triggers thermal cutouts or outright failures, especially once heavy field weakening is layered on top.[^1][^2]
- The Tronic X12 remains the flagship, delivering just under 30 kW on 24 S packs, but its onboard 5 V rail only sources about 150 mA and the stock looms melt without 10 AWG upgrades, so accessories still need dedicated bucks.[^3]
- Reliability work focuses on preventing traction-control current spikes and reinforcing the fragile DC-DC enable pad; moisture or incomplete post-cleaning rework continues to brick boards until those hot spots are addressed.[^4]
- Tronic hardware now ships directly from the contract manufacturer that previously white-labeled the brand, so pricing is steady but support and cooling expectations mirror the bare FR-4 chassis buyers are receiving.[^5][^6]

## Product Line Snapshot
| Model | Pack Window | Proven Operating Envelope | Notes for Builders |
| --- | --- | --- | --- |
| Tronic 250 (v1/v2) | 18–20 S nominal | ≈150 A phase (≈5–8 kW) with moderate field weakening before repeated pulls cook MOSFETs | Treat 230 A phase as a “one pull” ceiling; plan to graduate to larger controllers if you need sustained >8 kW.[^1][^2]
| Tronic 250R | 20–24 S | Similar 200 A phase guardrails; traction becomes the limiter when riders launch 24 S packs toward 120 km/h | Racers are already using 24 S setups—budget for premium tires and chassis bracing to keep the front planted.[^1]
| Tronic X12 | 20–24 S (some stretch to 26 S at their own risk) | ≈200 A battery / 310 A phase per controller when respecting the shared 331 A MOSFET limits | Ships without CAN/hall harnesses; add thermal pads and proper adhesive instead of relying on factory hot glue.[^3][^7]
| Tronic 750 (prototype) | 24–30 S experimental | Marketed 350 A+ battery / 550 A phase, but no warranty and minimal field data | Order only if you accept prototype risk; the community is still gathering credible stress tests.[^8]

## Performance Guardrails
### Battery & Phase Current Targets
- Veteran tuners keep dual Tronic 250 builds near 200 A rear / 180 A front phase current, reserving the published 250 A rating as an absolute ceiling.[^1]
- X12 owners pair roughly 200 A battery with 310 A phase to stay inside the MOSFET envelope, matching Smart Repair’s 24 S playbook.[^3]
- Community baselines for Tronic and Spintend 85‑250 class controllers hover around 150 A battery / 200 A phase continuous on 20 S packs, with higher peaks only after confirming thermal headroom.[^9]

### Voltage & Field-Weakening Discipline
- Field-weakening above ~30–40 A on Tronic 250s has already destroyed boards after 20 kW pulls; cap FW draw or step up to 12‑FET hardware before chasing highway speeds.[^2]
- Enabling ANT BMS discharge mid-commissioning immediately blew an X12, illustrating how toggling pack-side FETs under load can brick the power stage.[^7]

## Thermal & Packaging Playbook
- Replace stock phase looms with 10 AWG silicone leads and clamp controllers to machined heat spreaders; riders solved repeated overheating once they upgraded both wiring and mounting interfaces.[^3]
- X12 installers scrape off factory hot glue, apply thermal pads, and mechanically secure the board to avoid shorts—a must because the PCB ships bare.[^7]
- Treat Tronic 250 auxiliary rails as logic-only: the 5 V accessory feed keeps a 0.6 W taillight energized even when the scooter is “off,” so add latching switches or move lighting to a CAN-adjacent connector.[^10]

## Reliability & Failure Modes
- Traction-control surges have torched MOSFETs despite firmware limits; Rosheee’s rear Tronic ignited when TC caught a slide at 250 A phase / 300 A firmware, reinforcing front-only experiments and tighter slip budgets.[^4]
- The DC-DC enable pad lifts easily during IPA cleaning—technicians now scrape back copper, resolder, and reflow the regulator leg before conformal coating reassembled boards.[^4]
- Moisture exposure can revive otherwise dead boards temporarily, signaling trapped contamination; full cleaning plus conformal coating is the lasting fix—and waterlogged Rion front controllers only recovered after IPA baths, DC-DC pad rework, and conformal coating.[^4]
- A 117 km/h front-ESC fire showed that paste voids, suspect MOSFET bins, and marginal connectors still torch Tronic X-series hardware when traction-control or regen events spike current.[^15]
- Rion race teams now pre-flight every controller before reinstalling—lifting MOSFET clamps, scraping and repasting the baseplate, reseating shunts, and soldering a jumper across the fragile DC-DC enable pad—because the latest teardown found all three defects waiting to trigger another 117 km/h inferno if left untouched.【F:data/vesc_help_group/text_slices/input_part003.txt†L23300-L23653】
- Recent QC autopsies uncovered cracked MOSFET cans, uneven paste, and a fragile DC-DC enable pad that only re-latched after IPA baths—plan solder rework and connector upgrades before sending Tronic boards back into service.【F:data/vesc_help_group/text_slices/input_part003.txt†L23300-L23538】【F:data/vesc_help_group/text_slices/input_part003.txt†L23563-L23653】
- Sudden ABS over-current or regen spikes often track back to mismatched shunts or instrumentation blind spots—log actual phase and battery currents rather than trusting on-screen values.[^2][^11]

## Integration & Accessory Notes
- The X12’s 5 V rail maxes out around 150 mA, so horn, lighting, and telemetry accessories still need external buck converters even though the controller advertises auxiliary power.[^3]
- Tronic looms benefit from voltage-sequencing discipline: bring auxiliary 12 V rails online before waking ADC boards to avoid frying spinny throttles or lighting bridges.[^12]

## Procurement & Support Outlook
- JPPL confirmed the drone factory that built Tronic and Seven controllers now sells them directly, offering immediate stock but no added support.[^5]
- Seven-branded derivatives keep the FR-4 sandwich with Toll-package MOSFETs, yielding only a modest thermal advantage; racers should budget for external heatsinks just as they do with X12 boards.[^6]
- Secondary-market sellers are already moving bare X12 boards for about €350, reinforcing that buyers must self-support wiring, enclosures, and documentation.[^13]

## Outstanding Research Backlog
- Publish verified current limits for the latest Seven 18 / Tronic X12 Toll-FET builds once community tests push past 210 A battery / 310 A phase.[^6][^14]
- Capture teardown photos and torque specs for reinforcing the DC-DC section and connector terminations before the next round of high-speed validations.[^4]
- Log the pending warm-weather bench campaign for Tronic 250 v2, 250R, and Little FOCer v3.1 controllers once ambient temps rise above the -6 °C winter testing ceiling so reliability claims reflect real riding conditions.[^winter_tests]

## Source Notes
[^1]: Guardrails for Tronic 250 current limits and race usage on 24 S packs.【F:knowledge/notes/input_part007_review.md†L43-L55】
[^2]: Field-weakening failures and practical phase ceilings for Tronic 250-class hardware.【F:knowledge/notes/input_part009_review.md†L340-L341】
[^3]: X12 power targets, logic-rail limits, and wiring upgrades from Smart Repair and Rob Ver.【F:knowledge/notes/input_part013_review.md†L359-L362】
[^4]: Tronic traction-control surges, DC-DC enable pad repairs, and moisture mitigation lessons across rear and front-controller failures.【F:knowledge/notes/input_part003_review.md†L116-L124】【F:knowledge/notes/input_part003_review.md†L167-L179】
[^5]: Contract-manufacturer sourcing now handling Tronic/Seven sales directly.【F:knowledge/notes/input_part013_review.md†L790-L793】
[^6]: Seven-branded cooling architecture and Toll-package MOSFET notes.【F:knowledge/notes/input_part014_review.md†L163-L165】
[^7]: X12 failure after toggling ANT discharge and the need for manual harness/thermal prep on Dualtron installs.【F:knowledge/notes/input_part010_review.md†L315-L324】
[^8]: Community caution around Tronic 750 specifications and warranty disclaimers.【F:knowledge/notes/input_part003_review.md†L687-L737】
[^9]: Shared 20 S current baselines for Tronic/Spintend 85‑250 hardware.【F:knowledge/notes/input_part010_review.md†L565-L568】
[^10]: Tronic 250 auxiliary 5 V rail behaviour keeping lights powered.【F:knowledge/notes/input_part009_review.md†L12-L12】
[^11]: Instrumentation reminders to monitor actual current when tuning high-power scooters.【F:knowledge/notes/input_part009_review.md†L351-L352】
[^12]: Accessory power sequencing guidance to avoid frying ADC/Spinny boards.【F:knowledge/notes/input_part013_review.md†L795-L796】
[^13]: Secondary-market pricing and support expectations for bare X12 boards.【F:knowledge/notes/input_part013_review.md†L822-L823】
[^14]: Community request to log verified limits for Toll-FET Seven/Tronic builds as testing expands.【F:knowledge/notes/input_part014_review.md†L212-L218】
[^15]: 117 km/h Rion front-controller fire and ensuing DC-DC diagnostics highlighting paste quality and connector choices.【F:knowledge/notes/input_part003_review.md†L178-L179】
[^winter_tests]: Rosheee’s plan to re-bench Tronic 250 v2, 250R, and Little FOCer v3.1 hardware once temperatures climb above -6 °C so winter pack limits stop masking controller reliability.【F:knowledge/notes/input_part003_review.md†L716-L718】
