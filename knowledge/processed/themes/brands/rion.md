# Rion Performance Scooters Brand Dossier

## TL;DR
- RE90 buyers should budget well above the sticker: VAT, customs, and freight push the $6 800 base toward roughly €7 500 even before spares, which makes Paris pickup runs or hand-carrying attractive to avoid repeat taxes.[^1]
- Marketing claims of 400 A phase output and 136 PS motors remain unverified; community consensus is that the 23 S 6 P (~3 kWh) battery is the true bottleneck, so treat stock performance promises as aspirational until logs prove otherwise.[^1][^2]
- The latest Leo Apex/Rion production still leans on LY 60 H 22/3 hubs with 4 mm phase leads, keeping verified top speed near 123 km/h on 24 S and limiting safe motor current to roughly 180–200 A despite premium Tronic X12 controllers and >€9 k pricing.[^4]
- High-KV Rion-spec hubs demand controllers that can really supply ≥250 A phase and thicker-than-stock looms—4 mm² wiring overheats quickly, so Kelly/Sabvoton-class stages and 9.5 AWG leads are now the practical baseline.[^5][^6]
- RX-series carbon frames were styled for lighter builds; once riders chase 400 A tunes they report noticeable flex and still need to add waterproofing, torque arms, and tyre upgrades before all-season duty.[^2][^7]
- Replacement Rion/Weped FF-spec motors can be sourced around €340 in France, but rising freight often erases the deal for overseas owners; plan group shipments or forwarding to keep landed cost sane.[^3]

## Platform Snapshot
| Focus | Stock Insight | Operational Implication |
| --- | --- | --- |
| Battery & power | 23 S 6 P pack (~3 kWh) underpins stock builds; limited headroom makes the battery, not controllers, the first limit you will hit.[^2] | Prioritise cell health monitoring and plan future pack upgrades before chasing more aggressive controller tunes. |
| Chassis | Carbon construction is light but ships with minimal sealing and flexes once 400 A controllers are fitted.[^2][^7] | Budget time for seam sealing, hardware inspections, and reinforcement before relying on the chassis for high-power launches. |
| Cost of entry | Import math shows €7 500 landed cost once VAT/customs/shipping are included.[^1] | Price in protective gear, spares, and a contingency fund—repairs and customs rework can rival the base scooter price. |
| Motor envelope | Production Leo Apex/Rion builds still ship 60 H 22/3 hubs with 4 mm leads, keeping safe current near 200 A and real-world speed around 123 km/h on 24 S.[^4] | Budget for higher-spec hubs or rewinds if you need more torque or speed, and temper expectations until the battery/controller stack is refreshed. |
| Drivetrain service | FF-spec motors are available via specialist contacts at ≈€340 each, yet international freight can double that figure.[^3] | Consolidate orders or partner with EU-based buyers to minimise per-motor logistics overhead. |

## Strengths to Leverage
- **Hill-climb capability:** Riders seeking alpine routes value the RE90’s power-to-weight ratio once the battery is healthy and thermal logging is in place.[^1]
- **Aero-friendly packaging:** Carbon panels and clean wiring make it a top candidate for high-speed tarmac builds with minimal drag add-ons.[^2]
- **Controller headroom (with the right motors):** Compact Tronic X12 stacks shine when paired with hubs that can absorb the current—swap the OEM 60 H cans for 70 mm magnet sets if you want to exploit their potential.[^4][^6]

## Reliability Watchlist
- **Battery truth gap:** Until you have telemetry confirming sustained current delivery, assume marketing numbers overstate real capability.[^1]
- **Weather exposure:** Stock seals are insufficient; moisture ingress will jeopardise both the carbon structure and high-voltage electronics if left untreated.[^2]
- **Chassis flex:** RX carbon frames feel “chewing gum” at 400 A—plan dampers, reinforcement plates, and tyre upgrades if you chase high-speed stability.[^7]
- **Logistics churn:** Replacement motors are attainable but shipping shocks can nullify savings—budget for customs fees or arrange local pickup.[^3]

## Setup Priorities for New Owners
1. **Audit import paperwork** – confirm VAT/customs payments and document serial numbers before first ride; this simplifies future warranty or resale interactions.[^1]
2. **Waterproof the chassis** – strip panels, add gaskets or silicone seams, and protect high-voltage connectors before commuting or riding in damp climates.[^2]
3. **Baseline telemetry** – log pack voltage, current, and controller temps on stock firmware to understand real limits ahead of performance tuning.[^1][^2]
4. **Assess motor and wiring limits** – verify whether your build still runs 4 mm² phase leads; upgrade to 9.5 AWG-class harnesses and controllers capable of ≥250 A phase before targeting the advertised acceleration.[^5][^6]
5. **Plan parts logistics** – if you need spare motors or carbon panels, coordinate consolidated shipments through EU hubs to blunt freight surcharges.[^3]

## Upgrade & Maintenance Roadmap
- **Battery-first tuning:** Focus on validating cell balance and temperature spread; pursue pack upgrades or parallel modules before increasing controller current limits.[^2]
- **Motor swaps & spacing:** “Rion 1337” 70 mm magnet hubs ship with ~155–160 mm axles and 9.5 AWG leads—ensure your frame or fork can clear the width (Zero 11X-scale) before ordering and plan for new torque arms.[^6][^8]
- **Controller pairing:** High-KV hubs routinely cook 75/200-class VESCs; stepping up to Kelly, Sabvoton, or dual Tronic hardware keeps ≥250 A phase targets realistic without sensorless stalls.[^5]
- **Tyre & brake strategy:** Evaluate slicks or semi-slicks that match the platform’s dry-focus geometry, but keep a wet-weather set and mechanical braking upgrades ready because regen-only setups still falter when BMS charge FETs open.[^2][^9]
- **Service kit:** Stock carbon-safe cleaners, torque-limited tools, spare hall boards, and corrosion inhibitors to maintain the frame after weather sealing efforts.[^2][^5]

## Source Notes
[^1]: Cost breakdowns and skepticism toward 400 A/136 PS marketing around the RE90 import experience.【F:knowledge/notes/input_part000_review.md†L49-L51】
[^2]: Praise for the 23 S 6 P battery and carbon build alongside warnings about limited waterproofing and dry-optimised tyres.【F:knowledge/notes/input_part000_review.md†L51-L53】
[^3]: Availability and pricing realities for Rion/Weped FF-spec motors sourced within France.【F:knowledge/notes/input_part000_review.md†L698-L698】
[^4]: Leo Apex/Rion motor limits, phase-lead size, and premium pricing despite performance bottlenecks.【F:knowledge/notes/input_part010_review.md†L68-L69】
[^5]: Controller and wiring requirements for high-KV Rion hubs, including ≥250 A phase demand and 4 mm² lead overheating reports.【F:knowledge/notes/input_part001_review.md†L147-L147】【F:knowledge/notes/input_part001_review.md†L163-L163】
[^6]: “Rion 1337” hub specifications—70 mm magnets, ~9.5 AWG leads, and 155–160 mm axles—plus frame fitment constraints.【F:knowledge/notes/input_part001_review.md†L409-L409】【F:knowledge/notes/input_part001_review.md†L428-L428】
[^7]: Rider feedback calling the RX carbon chassis “chewing gum” under modern power levels and noting stability concerns versus Weped builds.【F:knowledge/notes/input_part001_review.md†L51-L51】【F:knowledge/notes/input_part001_review.md†L800-L801】
[^8]: Reference measurements placing HM, Blade, and Rion hub resistances plus axle width comparisons for swap planning.【F:knowledge/notes/input_part001_review.md†L314-L314】【F:knowledge/notes/input_part001_review.md†L409-L409】
[^9]: Regen-only braking limits when charge MOSFETs open and the need for mechanical brakes alongside VESC tuning.【F:knowledge/notes/input_part013_review.md†L5488-L5492】【F:knowledge/notes/input_part013_review.md†L5639-L5653】
