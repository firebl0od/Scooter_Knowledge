# Rion Performance Scooters Brand Dossier

## TL;DR
- RE90 buyers should budget well above the sticker: VAT, customs, and freight push the $6 800 base toward roughly €7 500 even before spares, which makes Paris pickup runs or hand-carrying attractive to avoid repeat taxes.[^1]
- Marketing claims of 400 A phase output and 136 PS motors remain unverified; community consensus is that the 23 S 6 P (~3 kWh) battery is the true bottleneck, so treat stock performance promises as aspirational until logs prove otherwise.[^1][^2]
- The carbon chassis ships with minimal weather sealing—expect to add waterproofing and consider dry-weather slicks, because the platform is tuned for peak tarmac performance rather than all-season utility.[^2]
- Replacement Rion/Weped FF-spec motors can be sourced around €340 in France, but rising freight often erases the deal for overseas owners; plan group shipments or forwarding to keep landed cost sane.[^3]
- 24 S conversions with Tronic controllers deliver brutal launches but still overwhelm front-wheel traction near 120 km/h unless phase current and ramping stay conservative.[^4]
- Leo Apex rebrands keep the LY 60 H 22/3 hubs with 4 mm phase leads, so practical phase ceilings remain about 180–200 A even with Tronic X12 controllers, and pricing now stretches beyond €9 000 while retaining mid-tier brakes.[^5]

## Platform Snapshot
| Focus | Stock Insight | Operational Implication |
| --- | --- | --- |
| Battery & power | 23 S 6 P pack (~3 kWh) underpins stock builds; limited headroom makes the battery, not controllers, the first limit you will hit.[^2] | Prioritise cell health monitoring and plan future pack upgrades before chasing more aggressive controller tunes. |
| Chassis | Carbon construction is lauded for stiffness and weight, but there is virtually no OEM waterproofing.[^2] | Invest early in sealing seams, cable glands, and connector boots if the scooter will ever see wet conditions. |
| Cost of entry | Import math shows €7 500 landed cost once VAT/customs/shipping are included.[^1] | Price in protective gear, spares, and a contingency fund—repairs and customs rework can rival the base scooter price. |
| Drivetrain service | FF-spec motors are available via specialist contacts at ≈€340 each, yet international freight can double that figure.[^3] | Consolidate orders or partner with EU-based buyers to minimise per-motor logistics overhead. |

## Strengths to Leverage
- **Hill-climb capability:** Riders seeking alpine routes value the RE90’s power-to-weight ratio once the battery is healthy and thermal logging is in place.[^1]
- **Aero-friendly packaging:** Carbon panels and clean wiring make it a top candidate for high-speed tarmac builds with minimal drag add-ons.[^2]

## Reliability Watchlist
- **Battery truth gap:** Until you have telemetry confirming sustained current delivery, assume marketing numbers overstate real capability.[^1]
- **Weather exposure:** Stock seals are insufficient; moisture ingress will jeopardise both the carbon structure and high-voltage electronics if left untreated.[^2]
- **Logistics churn:** Replacement motors are attainable but shipping shocks can nullify savings—budget for customs fees or arrange local pickup.[^3]

## Setup Priorities for New Owners
1. **Audit import paperwork** – confirm VAT/customs payments and document serial numbers before first ride; this simplifies future warranty or resale interactions.[^1]
2. **Waterproof the chassis** – strip panels, add gaskets or silicone seams, and protect high-voltage connectors before commuting or riding in damp climates.[^2]
3. **Baseline telemetry** – log pack voltage, current, and controller temps on stock firmware to understand real limits ahead of performance tuning.[^1][^2]
4. **Plan parts logistics** – if you need spare motors or carbon panels, coordinate consolidated shipments through EU hubs to blunt freight surcharges.[^3]

## High-Voltage Tuning Guardrails
- **Traction still fails first:** 24 S packs and Tronic 250R tunes are spinning the front tyre at ~120 km/h launches, so stagger ramping, warm tyres, and prioritise damper setup before chasing higher phase numbers.[^4]
- **Respect hub lead limits:** Production Rions and the Leo Apex share LY 60 H 22/3 motors with 4 mm phase conductors; riders cap them around 180–200 A continuous despite controller headroom, reserving higher numbers for short dyno pulls only.[^5]
- **Ease off when faults return:** Over-cranking phase current and heavy field-weakening brought grinding noises and cut-outs back on Jesús’s 24 S tune—dial limits back toward the 200 A region and verify traction-control settings before the next test run.[^4]
- **Finish diagnostics after repairs:** Swapping MOSFETs alone didn’t save Rosheee’s controller; latent shorts blew the VESC on the next motor detection, so meter the power stage and gate drivers before reconnecting the pack.[^6]

## Upgrade & Maintenance Roadmap
- **Battery-first tuning:** Focus on validating cell balance and temperature spread; pursue pack upgrades or parallel modules before increasing controller current limits.[^2]
- **Tyre strategy:** Evaluate slicks or semi-slicks that match the platform’s dry-focus geometry, but keep a wet-weather set if the scooter cannot be garage-bound.[^2]
- **Service kit:** Stock carbon-safe cleaners, torque-limited tools, and corrosion inhibitors to maintain the frame after weather sealing efforts.[^2]

## Market & Procurement Signals
- Leo Apex pricing now clears €9 000 while still shipping with Nutt brakes; factor in the premium for branding when comparing against custom Rion builds or competing factory frames.[^5]

## Source Notes
[^1]: Cost breakdowns and skepticism toward 400 A/136 PS marketing around the RE90 import experience.【F:knowledge/notes/input_part000_review.md†L49-L51】
[^2]: Praise for the 23 S 6 P battery and carbon build alongside warnings about limited waterproofing and dry-optimised tyres.【F:knowledge/notes/input_part000_review.md†L51-L53】
[^3]: Availability and pricing realities for Rion/Weped FF-spec motors sourced within France.【F:knowledge/notes/input_part000_review.md†L698-L698】
[^4]: Community logs from Jesús’s 24 S Tronic 250R setup highlighting front-wheel spin near 120 km/h and the need to moderate phase current and field-weakening on high-voltage Rions.【F:knowledge/notes/input_part007_review.md†L52-L55】
[^5]: Discussion of Leo Apex/Rion rebrands retaining LY 60 H 22/3 hubs with 4 mm phase wiring, capping sustainable current near 180–200 A, and still shipping with mid-tier brakes despite >€9 000 pricing.【F:knowledge/notes/input_part010_review.md†L68-L69】
[^6]: Rosheee’s failed controller repair underscoring the need for full diagnostics after MOSFET replacement on Rion hardware.【F:knowledge/notes/input_part002_review.md†L84-L84】
