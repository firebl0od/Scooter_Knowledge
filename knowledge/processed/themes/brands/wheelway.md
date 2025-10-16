# Wheelway Hub Motors

## Overview

Wheelway manufactures hub motors for electric scooters. While their motors can deliver good performance, they have documented quality control issues that require careful inspection and often sensor replacements. This guide helps you identify and fix common problems before they cause failures.

## Known Quality Issues

### Manufacturing Defects

**Stator Contamination**: Teardowns consistently reveal:[^1]
- Metal debris inside stator cavity
- Inadequate cleaning after manufacturing
- Particles that can cause shorts or noise

**Hall Sensor Problems**: Multiple quality issues documented:[^1][^2]
- Mismatched sensors (SS41F outers with unknown center sensor)
- Inconsistent component grading
- Sensors failing within first 25km
- Unused mounting slots (can be repurposed for thermistors)

**Heat Damage**: Crash analysis has found:[^ip001-wheelway-failure]
- Cooked hall sensor leads
- Heat-soaked windings
- Failed hall boards
- Compromised magnets and sideplates

> **⚠️ Critical**: Do not attempt rewinds on motors with heat damage. Once magnets and windings reach failure temperatures, retire the entire hub.

### Compatibility Issues

**VESC vs. Stock Controllers**:[^2]
- Motors with failing halls often still work on Xiaomi stock controllers
- Same motors desync immediately on VESC hardware
- Suggests marginal sensor quality that works with simpler control schemes
- VESC's more precise sensing exposes the quality issues

## Pre-Installation Inspection

**Mandatory Steps Before Use**:[^1]

1. **Complete Teardown**
   - Open the motor completely
   - Don't skip this even on new motors

2. **Thorough Cleaning**
   - Remove all metal debris from stator
   - Clean magnet surfaces
   - Verify no particles in air gap
   - Use compressed air and clean cloths

3. **Hall Sensor Testing**
   - Bench test all halls at 5V
   - Verify consistent output
   - Check for mismatched sensor types
   - Replace entire set if any are questionable[^5]

4. **Component Inspection**
   - Look for unused sensor slots
   - Check wiring integrity
   - Verify no heat damage
   - Confirm correct sensor positioning

## Adding Temperature Monitoring

Wheelway motors don't include thermistors, but you can add them.

### Installation Procedure

**What You Need**:[^3]
- 100kΩ NTC thermistor (compact package)
- ~30 AWG PTFE wire
- Heat shrink tubing
- Soldering equipment
- Patience (3-4 hours for careful work)

**Steps**:[^3][^4]

1. **Splice Thermistor**
   - Connect NTC between hall ground and new signal lead
   - Use quality solder joints
   - Ensure connections are mechanically secure

2. **Route Wiring**
   - Run PTFE wire through axle cavity
   - Avoid sharp bends that could break wire
   - Leave appropriate service loop

3. **Harness Integration**
   - Cut channel in outer jacket for extra conductor
   - Don't fold insulation (creates bulk)
   - Re-sheath entire loom with heat shrink
   - Verify bundle still fits exit port without chafing[^4]

4. **Testing**
   - Verify thermistor reads reasonable temperature
   - Check resistance curve matches 100kΩ spec
   - Confirm no shorts to motor phases

## Service & Repair

### Hall Sensor Replacement

**When to Replace**:[^2][^5]
- Failures within first 25km are common
- Desync issues on VESC (works on stock controller)
- Inconsistent readings during bench test
- Mismatched sensor types discovered

**Replacement Tips**:[^5]
- Replace entire set, not individual sensors
- Use matched sensors (all SS41 or all SS43)
- Keep sensorless backup profile ready
- Test thoroughly before reassembling

### Troubleshooting VESC Issues

**FOC Won't Complete or Immediate Reboot**:[^6]

This is a common Wheelway problem:

1. **First Step**: Unplug hall harness completely
2. **Retest sensorless**: Run FOC detection without halls
3. **If it works**: Hall board or sensors are faulty
4. **Common causes**:
   - Stray solder bridging hall board traces
   - Bad sensors triggering MCU resets
   - Wiring shorts

**Controller Loses Braking, Only 20A Output**:[^8]

Before assuming controller failure:
1. Check all three motor phase connections
2. Tighten phase wire terminals
3. Verify continuity on all phases
4. Multiple riders restored full power just by securing connections

### Frame Compatibility

**Installing in Xiaomi Frames**:[^7]

Wheelway rear rims can fit with modifications:
1. **Enlarge dropout holes** to accept wider axle
2. **Add ~1mm spacers** so bearings clamp squarely
3. Without spacers, hub floats in wider channel
4. Even cheap 5g aluminum rings work (axle bolts carry braking load)

## Safety Considerations

### Before Riding

- [ ] Complete teardown and cleaning performed
- [ ] Hall sensors tested and verified
- [ ] Temperature monitoring added (recommended)
- [ ] Harness routed without chafing
- [ ] All phase connections tight
- [ ] Sensorless backup profile configured

### Monitor During Break-In

- Watch for unusual noises (may indicate debris)
- Check for desync issues in first 25km
- Monitor temperatures if thermistor installed
- Inspect phase connections after first few rides

### Signs of Impending Failure

- Hall sensors becoming intermittent
- Unusual heating during normal use
- Reduced power output
- Desync events increasing in frequency

## Comparison with Other Motors

**vs. Quality Hub Motors**:
- Wheelway requires much more pre-installation work
- Quality control significantly lower
- Can perform well after proper prep
- Lower cost may not justify the extra effort for some builders

## When to Choose Wheelway

**Acceptable If**:
- You're comfortable with extensive pre-installation inspection
- You can replace hall sensors competently
- Budget is constrained
- You keep spare sensors on hand

**Avoid If**:
- You need reliable out-of-box performance
- You can't do thorough inspection/service
- This is your only transportation
- You lack backup motor configuration skills

## Essential Spares

Keep on hand for Wheelway motors:
- Complete matched hall sensor set
- Thermistors (if adding temperature monitoring)
- Appropriate gauge wire for sensor harness
- Heat shrink in various sizes
- Sensorless motor profile backup

## Related Guides

- [Motor Configuration](../guides/motor_configuration.md)
- [Controller Setup](../guides/controller_setup.md)
- [Scooter Diagnostic Toolkit](../guides/scooter_diagnostic_toolkit.md)

## References

[^1]: Source: knowledge/notes/input_part000_review.md, L408 to L418
[^2]: Source: knowledge/notes/input_part000_review.md, L418 to L422
[^3]: Source: knowledge/notes/input_part000_review.md, L422 to L430
[^4]: Source: knowledge/notes/input_part000_review.md, L430 to L432
[^5]: Source: knowledge/notes/input_part000_review.md, L535 to L546
[^6]: Source: knowledge/notes/input_part000_review.md, L522 to L531
[^7]: Source: knowledge/notes/input_part000_review.md, L572 to L574
[^8]: Source: knowledge/notes/input_part000_review.md, L732 to L736
[^ip001-wheelway-failure]: Source: data/vesc_help_group/text_slices/input_part001.txt†L27264-L27282
