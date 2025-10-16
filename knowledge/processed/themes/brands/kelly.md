# Kelly Controllers Field Notes

## TL;DR

- Kelly 7212 singles comfortably push about 200 A phase from 48 V packs, but riders wire horns and lighting directly to the battery through relays because the onboard DC/DC rail browns out if it feeds accessories; continuous battery draw sits near half the quoted phase rating (e.g., 120 A phase ≈ 80 A battery).[^1]
- Dual-controller Kelly installs simply parallel throttle 5 V/signal lines, brake inputs, and power buttons, yet the crew insists on QS8-class antispark hardware because XT90S resistors cannot survive repeated inrush events during autotune or hot plugging.[^2]
- Higher-spec CL/Kelly stacks advertise 350 A continuous and 700 A peak, but veterans still tune them conservatively and finish autotune by hand to avoid firmware bricks on first power-up.[^3]

## Setup & Wiring Patterns

- Mirror the throttle’s 5 V, ground, and signal to both controllers when building AWD rigs; no CAN bridge is required and the same wiring convention applies to brake sensors and enable buttons.[^3]
- Budget a pre-charge circuit or QS8/QS10 antispark connectors—the XT90S resistor was called out explicitly for failing to absorb Kelly inrush compared with 8 mm hardware.[^2]
- Re-terminate signal looms with Higo or JST connectors as you tidy dual-controller harnesses; sealed plugs simplify throttle/key splits and keep water out of the deck.[^4][^5]

## Accessory Power & DC/DC Safety

- Treat the lighting outputs as logic-only triggers: horns or LED strips tied straight into the controller’s 12 V rail force resets, so riders now power accessories directly from the pack and use relays or smart-BMS keys for switching.[^1]
- Disconnect packs before soldering or servicing—one energized repair ignited a nearby Makerbase board, reinforcing that Kelly harness work should be done with the battery physically isolated.[^6]

## Current & Thermal Guardrails

- Expect continuous battery draw to hover around half the advertised phase figure on Kelly datasheets; builders size wiring and fusing for ≈80 A battery when phase limits sit near 120 A on 7212 hardware, then log temps before nudging current higher.[^1]
- CL-series owners still ramp tunes slowly after autotune—even with promised 350 A continuous ceilings—because firmware glitches remain a risk when settings jump straight to the marketing numbers.[^3]

## Source Notes

- Wiring, accessory-power, and current-derating guidance consolidates October 2022 VESC Help Group discussions covering Kelly 7212 singles, dual-controller cabling, and the then-new CL-series claims.[^7][^2]

## References

[^1]: Source: knowledge/notes/input_part003_review.md, L36 to L37
[^2]: Source: knowledge/notes/input_part003_review.md, L83 to L84
[^3]: Source: knowledge/notes/input_part003_review.md, L38 to L38
[^4]: Source: data/vesc_help_group/text_slices/input_part003.txt, L8449 to L8454
[^5]: Source: data/vesc_help_group/text_slices/input_part003.txt, L337 to L345
[^6]: Source: knowledge/notes/input_part003_review.md, L36 to L36
[^7]: Source: knowledge/notes/input_part003_review.md, L36 to L38
