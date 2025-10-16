# Heatbox Controllers

## Overview

Heatbox produces high-voltage VESC-compatible motor controllers for electric scooters and e-bikes. Their legacy 100V/100A units are known for robust hardware but have specific wiring considerations that builders need to understand before installation.

## Product Line

| Model | Voltage Rating | Current Rating | Key Features |
|-------|----------------|----------------|--------------|
| Heatbox 100V/100A | 100V | 100A | Keyed three-wire ignition harness, legacy design |

## Known Issues & Solutions

### Ignition Harness Wiring

**Problem**: Controllers may show only a few tenths of a volt at the ignition pins

**Common Cause**: The ignition harness is mis-pinned, not a firmware issue[^1]

**Background**: Legacy Heatbox 100V/100A units ship with a keyed three-wire ignition loom that lacks firmware-selectable jumpers. This means the physical wiring must be correct for the controller to power on properly.

#### Diagnosis Steps

1. **Check voltage at ignition pins** with a multimeter
2. **If reading is very low** (few tenths of a volt): Assume mis-pinned harness
3. **Don't assume firmware is bricked** - it's usually a wiring issue

#### Repair Procedure

> **⚠️ Critical Warning**: Supply positive is NOT always the red wire on Heatbox harnesses! Always verify before connecting power.[^2]

**Wire Color Verification**:[^2]
1. Locate community reference photos (check e-scooter forums)
2. Identify each conductor with a multimeter
3. Trace every lead from source to destination
4. Document your specific unit's color coding
5. Only after verification, repin the connector if needed

**Repinning Process**:
1. Carefully extract pins from the keyed connector housing
2. Reference the verified pinout
3. Insert pins in the correct positions
4. Double-check with multimeter before energizing
5. Test keyswitch function at low voltage first

## Safety Considerations

### Before First Power-Up

- [ ] Verify all wire colors with multimeter
- [ ] Check ignition harness pinout against known-good reference
- [ ] Confirm keyswitch operates correctly
- [ ] Test at reduced voltage if possible
- [ ] Have emergency disconnect ready

### Why This Matters

Incorrect ignition wiring can:
- Prevent the controller from powering on
- Potentially damage the control logic if power is applied to wrong pins
- Create frustrating troubleshooting sessions mistaken for firmware issues

## Support & Resources

### Where to Find Help

- E-scooter community forums for reference photos
- VESC community Discord channels
- Heatbox distributor/reseller support channels

### Documentation Gaps

Currently, there's limited official documentation on:
- Standard wire color coding
- Pinout diagrams for ignition harnesses
- Firmware configuration options

Community-sourced photos and reverse-engineering have filled these gaps.

## Comparison with Other Brands

**vs. Spintend/Makerbase**: Heatbox units use a keyed three-wire design rather than firmware-configurable ignition, requiring more careful physical setup.

**vs. Flipsky**: Similar voltage/current ratings but different approach to power switching—Heatbox relies on proper harness wiring rather than software configuration.

## When to Choose Heatbox

**Good Fit If**:
- You need proven 100V operation
- You're comfortable with manual harness verification
- You want robust hardware
- You can access community support for wiring

**Consider Alternatives If**:
- You want plug-and-play ignition
- You need firmware-configurable power switching
- You require extensive manufacturer documentation
- You're new to controller installations

## Maintenance Tips

- Keep spare connectors and pins for harness repairs
- Document your specific unit's wire colors with photos
- Store pinout information with the controller
- Inspect ignition connections periodically for corrosion

## Related Guides

- [Controller Setup](../guides/controller_setup.md)
- [Power Distribution](../guides/power_distribution.md)
- [VESC Key Switch & Power Management](../guides/vesc-key-switch-and-power-management.md)

## References

[^1]: Source: knowledge/notes/input_part011_review.md, L409 to L414
[^2]: Source: knowledge/notes/input_part011_review.md, L413 to L417
