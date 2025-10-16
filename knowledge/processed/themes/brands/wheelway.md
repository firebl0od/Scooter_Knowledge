# Wheelway Motor & Parts Watch

## Quality & Reliability Notes
- Teardowns of Wheelway hub motors keep uncovering debris in the stator, mismatched hall sensors (SS41F outers with an unknown center), and even unused slots that riders now repurpose for thermistors—thorough cleaning and inspection is mandatory before sealing a motor.【F:knowledge/notes/input_part000_review.md†L408-L418】
- Multiple riders lost halls within the first 25 km; the motors still ran fine on Xiaomi controllers but desynced on VESC hardware until the sensors were swapped or the build was run sensorless, suggesting inconsistent component grading rather than wiring mistakes.【F:knowledge/notes/input_part000_review.md†L418-L422】

## Service & Troubleshooting
- Adding thermistors requires delicate harness work: splice a compact 100 kΩ NTC between hall ground and a new signal lead, run ≈30 AWG PTFE wire through the axle, and re-sheath the loom with heat-shrink so the bundle still fits the exit port without chafing.【F:knowledge/notes/input_part000_review.md†L422-L430】
- Expect three to four hours of desoldering and rewrapping to insert the extra conductor—cut a channel in the outer jacket instead of folding insulation so the harness can be reassembled without bulking up.【F:knowledge/notes/input_part000_review.md†L430-L432】
- Keep a sensorless profile on hand and bench-test every hall at 5 V before closing the hub; recent replacement boards still ship with mismatched SS41/SS43 sensors that can desync within 20 km.【F:knowledge/notes/input_part000_review.md†L535-L546】
- When FOC refuses to complete or a VESC reboots as soon as the throttle is touched, unplug the hall loom and rerun tests sensorless—Wheelway boards continue to trigger MCU resets until stray solder or bad sensors are replaced.【F:knowledge/notes/input_part000_review.md†L522-L531】
- Wheelway rear rims will drop into Xiaomi frames once the dropout holes are enlarged and ~1 mm spacers are added so the bearings clamp squarely—skipping the shims leaves the hub floating in the wider channel, though even 5 g AliExpress aluminium rings survive because the axle bolts carry the braking load.【F:knowledge/notes/input_part000_review.md†L572-L574】
- If a Wheelway controller loses braking and only crawls at ~20 A, assume a missing phase or loose motor lead first—several riders restored full power after tightening phase wiring before bothering with new FOC detection.【F:knowledge/notes/input_part000_review.md†L732-L736】
