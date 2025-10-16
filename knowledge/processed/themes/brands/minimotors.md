# Minimotors (Dualtron & Thunder Series)

## Overview

Minimotors is a major manufacturer of premium electric scooters, producing the Dualtron and Thunder model lines. This page covers technical notes for upgrading and maintaining their platforms, particularly focusing on VESC conversions and high-performance builds.

## Product Lines

### Thunder Series

**Thunder 3**: Spain's first 72V-legal scooter (homologated from January 2027). The certified frame designation will be mandatory for future road compliance, even though the chassis appears unchanged from earlier versions.[^1]

**Key Point**: Future Thunder 3 purchases in Spain will need to verify frame certification for legal on-road use.

### Dualtron Series

**Dualtron Achilleus**: High-performance platform that's popular for VESC conversions and controller upgrades.

## Motor Options

### Lonnyo 80H Motors for Thunder Builds

**Specifications**:[^2]
- **Price**: ~€736 without rims
- **Included**: Hall sensors and temperature sensors
- **Required fork opening**: 155mm
- **Status**: Arrives as motor only, source rims separately

> **💡 Pro Tip**: Test new motors on a known-good chassis (like a Nami) before committing to a wider custom frame like RFP. This validates motor performance before you're locked into a specific build.

## Display Integration

### EY3 Display Protocol

**Compatibility Challenge**: Flipsky FT85BD controllers and their Ubox Lite clones require the VSETT Lisp bridge to communicate with EY3 protocol displays.[^3]

**Critical Warning**: Leaving the bridge's throttle passthrough lead unplugged has killed displays. Treat the adapter as an essential part of the harness, not an optional accessory.[^3]

**Installation Checklist**:
- [ ] Install VSETT Lisp bridge firmware
- [ ] Connect throttle passthrough lead
- [ ] Verify display communication before riding
- [ ] Test all display functions (speed, battery, settings)

## Tuning Notes

### Dualtron Achilleus Specific Issues

**Phase Current Limitation**:[^achilleus-phase][^achilleus-cal]

The Achilleus has documented current limiting behavior:
- **Symptom**: Controller tops out near 200A phase even when commanding 300A
- **Affects**: Both MakerX G300 and Spintend 85 250 controllers
- **Workaround**: Some riders report needing to double commanded phase current
- **Root Cause**: Suspected shunt calibration or duty-cycle caps in VESC Tool 6.05

**Diagnosis Steps**:
1. Log actual phase current vs. commanded
2. Check shunt calibration settings
3. Verify duty cycle isn't hitting limits
4. Test with different firmware versions

**Power Output Validation**:[^achilleus-wheel]

On 22S11P P45B packs:
- Combined phase current: ~575A logged
- Claimed power: ~38kW
- **Critical**: Requires correct wheel diameter input for accurate readings
- Rear hub can saturate if settings are wrong

**Measurement Checklist**:
1. Measure actual tire circumference
2. Input correct wheel diameter in VESC Tool
3. Validate speed readings against GPS
4. Cross-check power calculations
5. Monitor for hub saturation indicators

### Configuration Recommendations

**For Achilleus Builds**:
- Start with conservative phase current (150A per controller)
- Log real vs. commanded current
- Adjust calibration if needed
- Only increase after confirming accurate readings
- Monitor hub temperatures closely

## Parts & Group Buys

### Dualtron Rear Suspension

**Extended Cartridge/Bracket Group Buy**:[^dualtron-bracket]
- **Organizer**: Patrick (Rage community)
- **Price**: €65 per set
- **Purpose**: Simplifies longer shock or wider wheel installs
- **Benefit**: Avoids need for custom machining

**When Needed**:
- Upgrading to higher-performance shocks
- Installing wider wheels
- Modifying suspension geometry
- Race/track builds

## Common Upgrades

### VESC Conversion Considerations

When converting Dualtron models to VESC:
1. **Display**: Plan for EY3 protocol compatibility
2. **Current limits**: Be aware of phase current issues
3. **Wheel diameter**: Measure and configure accurately
4. **Harness**: Budget time for proper integration
5. **Testing**: Validate all functions before relying on setup

### High-Performance Builds

Thunder-class high-power builds typically involve:
- Lonnyo 80H motors (or similar)
- 22S battery packs
- Dual high-current controllers
- Custom frames with extended battery bays
- Active thermal management

## Maintenance Tips

### Display Care

- Protect throttle passthrough connections
- Use proper strain relief on harness
- Waterproof all connectors
- Keep backup display or know sensorless operation

### Motor Monitoring

- Log temperatures if sensors installed
- Watch for saturation indicators
- Verify phase current readings match expectations
- Check wheel diameter settings periodically

## Comparison with Other Platforms

### vs. Custom Frames

**Stock Dualtron/Thunder**:
- Integrated design
- Known dimensions
- Parts availability
- Community support

**Custom (RFP, etc.)**:
- More battery space
- Better controller cooling options
- Requires more planning
- Higher cost

## When to Choose Minimotors Platforms

**Good Fit If**:
- You want premium factory quality
- Parts availability is important
- You need proven platform for upgrades
- Community support valuable

**Consider Alternatives If**:
- Need maximum battery capacity
- Want custom geometry
- Budget is primary concern
- Prefer ground-up custom builds

## Resources

- Active community forums and groups
- Spare parts generally available
- Performance upgrade paths well-documented
- VESC conversion guides exist

## Related Guides

- [Controller Setup](../guides/controller_setup.md)
- [Motor Configuration](../guides/motor_configuration.md)
- [VESC-ADC Accessory Integration](../guides/vesc-adc-accessory-integration.md)

## References

[^1]: Source: knowledge/notes/input_part011_review.md, L492 to L493
[^2]: Source: knowledge/notes/input_part011_review.md, L494 to L494
[^3]: Source: knowledge/notes/input_part009_review.md†L438-L439
[^achilleus-phase]: Source: knowledge/notes/input_part013_review.md†L735-L735
[^achilleus-cal]: Source: knowledge/notes/input_part013_review.md†L840-L840
[^achilleus-wheel]: Source: knowledge/notes/input_part013_review.md†L743-L743
[^dualtron-bracket]: Source: knowledge/notes/input_part013_review.md†L792-L792
