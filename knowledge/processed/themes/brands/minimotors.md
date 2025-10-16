# Minimotors Platform Notes

## Thunder 3 Roadmap

- Thunder 3 has been homologated as Spain’s first 72 V-legal scooter from January 2027 onward, making certified frames mandatory for future road compliance even though the chassis looks unchanged from earlier runs.[^1]
- Fresh Lonnyo 80 H motors for Thunder-class builds arrive without rims for about €736, include hall/temperature sensors, and require 155 mm fork openings—test them on a known chassis (e.g., Nami) before committing to a wider RFP frame.[^2]

## Achilleus & Victor Tuning Notes

- Dualtron Achilleus still tops out near 200 A phase on a single controller even when 300 A is commanded, and riders now report needing to double commanded phase current on both MakerX G300 and Spintend 85 250 stacks—log shunt calibration or duty-cycle caps on VESC Tool 6.05 before chasing heavier 22 S tunes.[^achilleus-phase][^achilleus-cal]
- Achilleus and عمر logged roughly 575 A combined phase on 22 S 11 P P45B packs but still need correct wheel-diameter inputs to validate the claimed ~38 kW without saturating the rear hub—document tire circumference whenever you tune their dashboards.[^achilleus-wheel]

## Parts & Group Buys

- Rage community organiser Patrick is coordinating a €65 group buy for extended Dualtron rear cartridges/brackets, simplifying longer shock or wider wheel installs without bespoke machining.[^dualtron-bracket]

## References

[^1]: Source: knowledge/notes/input_part011_review.md, L492 to L493
[^2]: Source: knowledge/notes/input_part011_review.md, L494 to L494
[^achilleus-phase]: Source: knowledge/notes/input_part013_review.md†L735-L735
[^achilleus-cal]: Source: knowledge/notes/input_part013_review.md†L840-L840
[^achilleus-wheel]: Source: knowledge/notes/input_part013_review.md†L743-L743
[^dualtron-bracket]: Source: knowledge/notes/input_part013_review.md†L792-L792
