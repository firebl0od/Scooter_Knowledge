# RFP Controllers & Custom Frames

## Overview

RFP produces aftermarket electric scooter controllers and custom chassis designs. They're particularly known for reliable daily-driver controllers and extended frames that accommodate larger battery packs and dual-controller setups.

## 💡 Why Choose RFP?

✅ **Set-and-Forget**: Reliable daily commuter controllers
✅ **Extended Frames**: +15cm battery space vs stock Thunder
✅ **Dual Controller Ready**: Accommodates Tronic Seven-class hardware
⚠️ **Trade-offs**: Conservative performance focus, limited high-power field data

## 📋 Quick Product Overview

| Product | Key Feature | Best For | Price Point |
|---------|-------------|----------|-------------|
| RFP VESC Controller | Reliable daily-driver | Commuter builds | Mid-range |
| Extended Frame | +15cm battery bay | Large packs, dual controllers | Premium |
| Upgrade Path | Staged build support | 22S11P Eve 40PL capable | Flexible |

## ⚠️ Critical RFP Notes

🔴 **Conservative Tuning**: Controllers optimized for reliability over peak performance
🔴 **Extended Frame Planning**: +15cm space enables serious builds—plan from start
🔴 **Staged Approach**: Start conservative, validate each upgrade step
🔴 **Limited High-Power Data**: 600A phase projections not yet field-proven

## 💡 Pro Tips

- **Daily reliability**: Best choice for riders prioritizing uptime over peak power
- **Frame first**: Extended chassis worth investment if planning staged upgrades
- **22S11P capable**: Frame accommodates serious battery capacity
- **Dual controller space**: Plan Tronic Seven or similar class from beginning

## 🔧 Related Brand Dossiers

- [Tronic Controllers](tronic.md) - Controllers that fit RFP extended frame
- [Minimotors Platforms](minimotors.md) - Base Thunder platform comparison
- [Rage Mechanics](rage_mechanics.md) - Alternative custom frame option

## Product Line

### Controllers

**RFP VESC Controllers**: Production units have earned a "set-and-forget" reputation for daily Jetson and commuter duty, provided battery current stays at moderate levels. They stand out as one of the few plug-and-ride options in mixed fleet environments.[^1]

**Key Strength**: Reliability for daily commuting without constant tuning.

### Custom Frames

**RFP Extended Frame**: The signature feature is approximately 15cm more battery bay space compared to stock Thunder layouts. This extra room enables:
- Dual Tronic Seven-class controllers
- Large battery packs (22S11P Eve 40PL configurations)
- Staged upgrade paths as builds evolve[^2]

## Applications

### Daily Commuting

RFP controllers excel in practical, reliable transportation:
- Set conservative current limits
- Minimal ongoing maintenance
- Consistent performance across weather conditions
- Good for riders who want reliability over peak performance

### High-Performance Builds

The extended frame opens possibilities for serious power:
- **Target Configuration**: 75H 22/3 hubs
- **Projected Power**: ~600A phase / 350-400A battery per controller
- **Battery**: 22S11P Eve 40PL packs[^3]

> **📝 Note**: These are staged upgrade targets. Start conservative and validate each step before pushing limits.

## Building with RFP Components

### Planning Checklist

When planning a dual-controller RFP frame build:[^2][^4]

1. **Controller Placement**
   - Map mounting points early in the design phase
   - Reserve adequate space for airflow around both controllers
   - Plan cable routing before finalizing positions
   - Consider heat management from the start

2. **Battery Staging**
   - Begin with the 22S11P Eve 40PL pack the frame was designed for
   - This provides baseline performance and proves the packaging
   - Validates thermal performance before increasing power

3. **Progressive Tuning**
   - Start with conservative current limits
   - Log temperature and performance data
   - Only increase power after confirming cooling is adequate
   - Implement traction control before chasing 600A phase targets

### Motor Selection Strategy

Yamal's approach provides a good model:[^3]
1. Validate high-KV motors on existing platform (e.g., Nami)
2. If torque or thermal performance is inadequate, upgrade
3. Step to 75H 22/3 hubs for better heat handling
4. Only then push toward 600A phase per controller
5. Maintain 350-400A battery current limits

## Integration Tips

### Dual Controller Setup

**Space Requirements**:
- Front and rear controllers need independent mounting
- Each requires thermal pathway to chassis or air
- Plan CAN bus wiring between controllers
- Allow access for service and adjustments

**Thermal Management**:
- Extended bay helps, but active cooling may still be needed
- Monitor both controller temperatures independently
- Consider airflow direction through the bay
- Don't assume more space automatically means better cooling

### Upgrade Path

**Phase 1 - Establish Baseline**:
- Install RFP controllers with conservative settings
- Install properly sized battery pack (22S11P)
- Validate all systems work together
- Collect thermal and performance data

**Phase 2 - Optimize Current Setup**:
- Fine-tune current limits based on real data
- Implement traction control
- Ensure cooling is adequate
- Verify BMS can handle power levels

**Phase 3 - Consider Motor Upgrades**:
- Only if current motors limit performance
- Test on another platform first if possible
- Plan for increased thermal load
- Budget for proper integration

## Comparison with Other Options

### vs. Stock Thunder Frame
- **RFP**: +15cm battery bay, dual controller friendly
- **Thunder**: More compact, simpler integration

### vs. Boutique Controllers
- **RFP**: Proven reliability, plug-and-play
- **High-end**: More tuning potential, higher peak power

## Maintenance & Support

**Daily Use**:
- RFP controllers require minimal intervention
- Standard VESC firmware updates apply
- Community support available for common issues

**Availability**:
- Controllers are production items, not custom orders
- Extended frames may have longer lead times
- Check with RFP directly for current availability

## When to Choose RFP

**Good Fit If**:
- You prioritize reliability over peak performance
- You're building a high-power dual-motor setup
- You need more battery space than stock frames offer
- You want proven components for daily use

**Consider Alternatives If**:
- You need absolute maximum performance
- Stock frame dimensions work for your pack
- You prefer single-controller simplicity
- You're on a tight budget

## Related Resources

- [Controller Setup Guide](../guides/controller_setup.md)
- [Battery Pack Design](../guides/battery_pack_design.md)
- [Power Distribution](../guides/power_distribution.md)

## References

[^1]: Source: knowledge/notes/input_part011_review.md, L400 to L401
[^2]: Source: knowledge/notes/input_part011_review.md, L403 to L404
[^3]: Source: knowledge/notes/input_part011_review.md, L404 to L405
[^4]: Source: knowledge/notes/input_part011_review.md, L403 to L405
