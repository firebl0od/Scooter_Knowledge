# Rage Mechanics Deck & Chassis Notes

## Product Snapshot

- **Extended Dualtron deck:** €410 in black or €470 in carbon, measuring ~672 mm overall with ≈622 mm of usable floor once the 25 mm lips at each end are subtracted; budget machining time to fit controller plates and harness channels cleanly.[^deck_specs]

## Buyer Guidance

- **Skip ill-fitting alternatives:** Community feedback flags FastRide decks for sloppy tolerances and calls Sonken swingarms overbuilt, difficult to align, and locked to stock Dualtron pole geometry—stick with Rage Mechanics or RFP hardware when you need precise packaging.[^fitment_caveats]
- **Expect permanent frame work:** Mirko’s Dualtron conversion required enlarging the rear forks before the Rage Mechanics deck would sit correctly, so plan for irreversible metal work rather than a drop-in swap.[^fork_machining]
- **Victor swaps stay bolt-on:** Skrtt’s Thunder box transplant onto a Dualtron Victor confirmed the 7.5 cm mount spacing matches and cost about €200; pair it with Thunder swingarms and shortened phase leads when prepping for 70 H or 11" drivetrains.[^victor_transplant]

## Track & Hyper Builds

- **FH60 vs. FHT60 hubs:** The high-speed FH60 paired with dual 20 S controllers targets roughly 120–130 km/h, while the FHT60 torque wind tops around 100 km/h and takes e-Fire 10×2/2.5/3.0 tyres on 6-inch rims—10×2 rubber remains a tight fit unless you adopt Xiaomi-width rims.[^1]
- A Swedish “hyper” customer pushing Rage Mechanics drivetrain parts past 117 km/h now runs 22×3 windings, 700 mm bars, and a steering damper—evidence that chassis bracing and dampers become mandatory once G30-based builds cross triple-digit speeds.[^2]
- **R-spec Surron hub preview:** The upcoming Rage Mechanics 30 kW motor handles ≈45 Ah 80 V packs, survives burst launches, and still delivers ~150 km of range at <45 km/h cruising—plan premium stators and thermal management when chasing dirt-bike power on scooters.[^3]
- The RM-Light race scooter pairs a Dualtron Compact frame with a 22 S 4 P tabless pack, C350 RM-X motor, Beringer brakes, and a titanium pole to hit roughly 140 km/h at just 37 kg, underscoring that the platform targets short sprint sessions rather than street duty.[^4]
- Rage’s latest customer build packages dual XHS75 hubs, paired CL350 controllers, and a 20 S 10 P P45B pack inside twin waterproof cases with a steel steering pole, SmartDisplay dash, and Hope Tech 4 V4 brakes—ready for 0–100 km/h testing once weather cooperates.[^5]

## Motor Portfolio

- Rage Mechanics’ 75 mm stator hubs sustain over 10 kW per wheel on Weped builds without overheating but command roughly €650 each depending on order volume, so plan axle spacing and budget before chasing 120 km/h targets.[^6]

## SmartDisplay & Telemetry Program

- The CNC aluminium SmartDisplay now boots in ≈10 s, bridges VESC Tool, Minimotors, Kelly, Zero, and VSETT controllers, logs GPS, and exposes RTC/media controls; modular harnesses ship with the head unit and knob controls are planned for the production wave later this year.[^7][^8]
- Production pricing is targeting €400–€600 retail with €199.99 launch slots for the first batch, and Rage Mechanics is prepping web sales once the initial 100-piece run lands.[^8]
- SmartDisplay still cold-boots far faster than Raspberry Pi dashboards (≈10 s versus 60–95 s) and retains double-click button mapping today, making it the go-to HUD for riders who need quick telemetry without juggling full SBCs.[^9]
- RM-series customer builds lean on Spintend controllers, 21 S7 P EVE 50PL packs, always-on traction control, and staggered kV splits (lower front, higher rear) proven in racing—but the team is ready to pivot to dual CL350s if repeated Spintend attrition returns, so document controller swaps and telemetry as the fleet evolves.[^10]

## Source Notes

[^deck_specs]: Rage Mechanics’ Dualtron deck pricing, dimensions, and usable floor length once the lips are removed.Source: knowledge/notes/input_part012_review.md, L19 to L19
[^fitment_caveats]: Builder comparisons knocking FastRide decks for tolerance issues and Sonken swingarms for awkward geometry versus Rage Mechanics or RFP options.Source: knowledge/notes/input_part012_review.md, L20 to L20
[^fork_machining]: Mirko’s deck install required machining the Dualtron rear forks before the hardware would seat correctly.Source: knowledge/notes/input_part012_review.md, L18 to L18
[^victor_transplant]: Skrtt paid ≈€200 for a used Thunder battery box that bolts straight to the Victor’s 7.5 cm mounts and planned Thunder swingarms plus shorter phase leads for incoming 70 H/11" hardware.Source: knowledge/notes/input_part012_review.md, L215 to L219

## References

[^1]: Source: data/vesc_help_group/text_slices/input_part004.txt, L3475 to L3496
[^2]: Source: knowledge/notes/input_part012_review.md, L391 to L392
[^3]: Source: knowledge/notes/input_part004_review.md, L297 to L297
[^4]: Source: knowledge/notes/input_part012_review.md, L393 to L394
[^5]: Source: knowledge/notes/input_part009_review.md, L306 to L306
[^6]: Source: knowledge/notes/input_part000_review.md, L494 to L498
[^7]: Source: data/vesc_help_group/text_slices/input_part004.txt, L935 to L975
[^8]: Source: data/vesc_help_group/text_slices/input_part004.txt, L5214 to L5237
[^9]: Source: data/vesc_help_group/text_slices/input_part004.txt, L6980 to L6993
[^10]: Source: knowledge/notes/input_part014_review.md, L71 to L71
