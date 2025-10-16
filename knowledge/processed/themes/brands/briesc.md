# Briesc Controllers

## Overview

Briesc produces Italian-built VESC controllers for high-performance electric scooters. Their compact controllers are known for impressive power density, with some models running 150A battery / 350A phase in minimal packaging. They're particularly suited for tight deck installations where traditional larger controllers won't fit.

## Product Line

### Standard Briesc Controller

**Thermal Performance**:[^1]
- **Tested Output**: 150A battery / 350A phase
- **Case Temperature**: ~55°C at these loads
- **Testing Condition**: Bench tested without heatsinks
- **Advantage**: Real headroom once proper airflow is added

**Form Factor**:
- Compact enough for tight decks
- Comparable footprint to Makerbase 75100-class
- Italian manufacturing quality

**Connectivity Limitation**:[^1]
- No integrated Bluetooth module
- Requires external BLE dongle or SmartDisplay pass-through
- Budget for accessory wireless solution

> **📝 Note**: The lack of built-in Bluetooth keeps the package compact but adds a component to your BOM.

### Briesc 100/200 (Pre-Production)

**Status**: Prototype/development platform[^3][^4]

**Specifications**:
- Positioned between C700 and C1000 hardware capability
- Dual controller setup available

**Field Testing Results**:[^3]
- **On Scooters**: 210A battery / 420A phase per controller logged by Simone
- **Lab Testing**: Touched 900A phase without failure
- **Target Application**: Oil-cooled QS273-class hubs

> **⚠️ Important**: This is pre-production hardware. Smaller scooter builds need serious thermal management before expecting similar current levels.

## Bluetooth Solutions

### External Module Options

**Challenge**: Ultra-small BLE boards flashed with Vedder firmware show unusable range[^2]

**Recommended Approach**:
- Use proven €2 BLE modules
- Or route through SmartDisplay bridge
- Wait for official wireless option if possible

**Why This Matters**: Poor Bluetooth range makes tuning and diagnostics frustrating, especially on sealed builds.

## Installation Considerations

### For Standard Controllers

1. **Plan Airflow Early**
   - 55°C without heatsinks shows potential
   - Proper airflow will keep temperatures even lower
   - Consider fan placement or passive cooling path

2. **Budget for Bluetooth**
   - External dongle adds cost
   - SmartDisplay integration needs planning
   - Test range before sealing deck

3. **Mounting**
   - Compact size fits where 75100s can't
   - Ensure solid thermal contact with mounting surface
   - Leave access for Bluetooth dongle connection

### For 100/200 Prototypes

**Critical Requirements**:[^4][^3]
- Document temperature sensor placement
- Reinforce bus connections
- Plan serious cooling solution
- Don't assume small-hub thermal performance matches QS273 testing

**Battery Management System**:[^5]
- Pair with JK 200A smart BMS or equivalent
- Discharge logging must match controller capability
- Essential for 22S operation

**Before Deployment**:
1. Document all temperature sensors
2. Verify bus bar integrity
3. Test cooling solution thoroughly
4. Validate at lower currents first
5. Log sustained thermal performance

## Testing & Commissioning

### Standard Controller

**Initial Setup**:
- Start with conservative current limits
- Verify Bluetooth connectivity
- Test thermal performance at moderate power
- Gradually increase limits while monitoring temperatures

**Ongoing Monitoring**:
- Log case temperatures
- Watch for thermal throttling
- Verify Bluetooth range is adequate for your needs

### 100/200 Prototypes

**Pre-Production Cautions**:[^3]
- Community still needs scooter-sized telemetry
- Lab dyno results don't translate directly to smaller builds
- Log sustained thermal performance carefully
- Share findings with community

**Progressive Testing**:
1. Begin well below rated limits
2. Monitor all temperature sensors
3. Verify cooling solution effectiveness
4. Document any thermal issues
5. Only increase power after thermal validation

## Comparison with Alternatives

### vs. Makerbase 75100

**Briesc Advantages**:
- Higher power density
- Better thermal performance
- Italian quality control

**Briesc Disadvantages**:
- No integrated Bluetooth
- Less common (harder to find support)
- Higher price point

### vs. Spintend Ubox

**Briesc Advantages**:
- More compact
- Good thermal performance without extreme cooling

**Spintend Advantages**:
- Integrated Bluetooth and accessories
- Wider community support
- More field testing data

## When to Choose Briesc

**Good Fit If**:
- Space is extremely limited
- You can source external Bluetooth solution
- You value power density
- Italian manufacturing appeals to you

**Consider Alternatives If**:
- You want integrated Bluetooth
- You need extensive community support documentation
- Budget is primary concern
- You're doing first VESC build

## Open Questions

**For 100/200 Platform**:[^3]
- How does it perform on standard scooter hubs (not QS273)?
- What cooling solution works for typical deck installations?
- Can smaller builds safely reach 250A battery on 40PL packs?
- What are realistic sustained power limits?

**Community Testing Needed**:
- Thermal data from real-world scooter installations
- Long-term reliability data
- Comparison with similar-spec controllers
- Optimal cooling solutions for deck mounting

## Related Guides

- [Controller Setup](../guides/controller_setup.md)
- [Power Distribution](../guides/power_distribution.md)
- [Motor Configuration](../guides/motor_configuration.md)

## References

[^1]: Source: knowledge/notes/input_part005_review.md, L346 to L349
[^2]: Source: knowledge/notes/input_part005_review.md, L346 to L347
[^3]: Source: knowledge/notes/input_part010_review.md, L347 to L348
[^4]: Source: knowledge/notes/input_part010_review.md, L327 to L329
[^5]: Source: knowledge/notes/input_part010_review.md, L376 to L377
