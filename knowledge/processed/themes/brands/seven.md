# Seven Controllers

## Overview

Seven produces high-voltage VESC controllers designed for extreme performance electric scooters. Their controllers mirror Tronic X12 offerings with 24S and 30S capabilities. However, Seven is a new brand with limited field testing, firmware availability issues, and uncertain support infrastructure. This guide helps you understand what you're getting into if you choose Seven hardware.

## 💡 Why Choose Seven?

✅ **High Voltage**: 24S and 30S capability
✅ **VESC Express**: Bundled telemetry daughterboard
✅ **Toll MOSFETs**: 18-30 FET count
⚠️ **Trade-offs**: New brand, limited field data, firmware support uncertain, higher cost than Chinese alternatives

## 📋 Quick Model Comparison

| Model | FET Count | Voltage | Aux Power | Key Feature | Status |
|-------|-----------|---------|-----------|-------------|--------|
| Seven 18 | 18 Toll FETs | 24S target | 12V/4A | Express board | Limited availability |
| Seven 30 | 30 FETs | 30S ambitions | 12V/4A | Onboard memory | Rumored inventory |

## ⚠️ Critical Seven Warnings

🔴 **New Brand Risk**: Limited field testing and community knowledge
🔴 **Firmware Issues**: Support and documentation scarce
🔴 **Tronic Mirror**: Similar to X12—only 15-20% thermal advantage
🔴 **Conservative Start**: 16S baseline: 180A battery / 300A phase—work up slowly

## 💡 Pro Tips

- **Early adopter risk**: Budget for potential firmware/support issues
- **Conservative tuning**: Start with proven 16S recipe, increase carefully
- **Documentation sparse**: Expect to pioneer rather than follow guides
- **Price comparison**: Evaluate against established Tronic/Spintend options

## 🔧 Related Brand Dossiers

- [Tronic Controllers](tronic.md) - Similar X12 design baseline
- [Spintend Controllers](spintend.md) - Established high-voltage alternative
- [3Shul Controllers](3shul.md) - Premium racing option

## Product Line

### Seven 18 (18-FET)

**Specifications**:[^lineup]
- **Voltage**: 24S marketing target
- **FET Count**: 18 Toll-class MOSFETs
- **Aux Power**: 12V / 4A rail
- **Telemetry**: Bundled VESC Express daughterboard
- **Logging**: Onboard memory

**PCB Construction**:[^thermal]
- 1.6mm FR-4 substrate
- Similar to Tronic X12 design
- Thermal advantage over X12: Only ~15-20%

### Seven 30 (30-FET)

**Specifications**:[^lineup]
- **Voltage**: 30S ambitions (marketing)
- **FET Count**: 30 MOSFETs
- **Aux Power**: 12V / 4A rail
- **Logging**: Onboard memory
- **Status**: Inventory still rumored, limited availability

> **⚠️ Important**: Both variants share the same firmware and support caveats. Expect limited documentation and community knowledge.

## Performance Baselines

### Conservative Starting Point

**Documented 16S Recipe**:[^fw_baseline]
- **Battery Current**: ~180A
- **Phase Current**: 300A
- **Field Weakening**: ~50A at 87% duty cycle

**Why Start Here**:
- Proven baseline from early adopters
- Allows thermal validation
- Provides comparison point
- Can increase gradually with logging

### Field Weakening Cautions

**Progressive Approach**:[^fw_baseline]
1. Start at documented 50A FW
2. Monitor temperatures closely
3. Log traction performance
4. Audit traction control behavior
5. Only increase after validation

> **💡 Pro Tip**: Heavier FW experiments should ramp slowly. Traction control audits are essential to avoid surprises at high speeds.

## Thermal Considerations

### FR-4 Substrate Limitations

**Paolo's Assessment**:[^thermal]
- MOSFETs sandwiched on 1.6mm FR-4
- Thermal improvement over X12: Only 15-20%
- Not a major leap in heat management

**Implications**:
- **Robust cooling still required**
- **Not significantly better than alternatives**
- **Racers may prefer direct-to-heatsink platforms** (e.g., K900)

**Cooling Requirements**:
- Mount to metal chassis with thermal paste
- Consider active cooling (fans)
- External heatsinks may be necessary
- Monitor temperatures on first rides

### Comparison with Alternatives

**vs. Tronic X12**:
- Similar thermal performance
- Seven has slight edge (15-20%)
- Not enough to justify switching if X12 working

**vs. Direct-Mount Controllers**:
- K900 and similar have better heat dissipation
- May be better choice for extreme builds
- Seven's advantage is limited

## Critical Firmware Issues

### Source Code Availability

**The Problem**:[^firmware]
- Ships with VESC Tool 6.06 binaries
- **No published source code**
- Violates GPL licensing
- Creates support and legal grey area

**What You Should Do**:
1. **Demand GPL-compliant source releases**
2. **Archive firmware before installing**
3. **Refuse closed drops on production fleets**
4. **Document everything**

> **⚠️ Legal Issue**: VESC firmware is GPL-licensed. Withholding source code violates the license. This puts users in a difficult position for support and modifications.

### VESC Tool Compatibility

**Known Issues**:[^firmware]
- Bluetooth pairing hiccups on 6.06
- Some users reverted to 6.05
- Wait for patches before updating
- Document software builds

**Best Practice**:
- Test firmware before deployment
- Keep backup of working versions
- Track VESC Tool version compatibility
- Join community forums for updates

### VESC Express Problems

**Bundled Hardware Fails**:[^express]
- Express board fails to enumerate reliably
- Cannot use for telemetry without workarounds
- Forces external solutions

**Workaround**:[^express]
- Hang separate CAN-connected Express module
- Use for telemetry until bundled version fixed
- Budget for external module in BOM

> **📝 Note**: JPPL had to add separate Express module for telemetry. This is an extra cost and complexity you should plan for.

## Supply Chain Reality

### Alibaba Direct Sales

**Current Situation**:[^supply]
- Controllers sold via Alibaba
- Direct from contract manufacturer
- Historical Seven/Tronic pricing
- **No brand support infrastructure**

**What This Means**:
- Treat as boutique hardware
- Self-managed documentation required
- No official warranty support
- Must solve problems yourself

### Availability Issues

**Delivery Problems**:[^1]
- Long lead times (4+ months reported)
- Partial shipments common
- Example: 6-pack order delivered only 2 units
- Plan for delays and shortages

**Recommendations**:
- Order well in advance
- Have backup plan
- Stock spares if possible
- Join community for group buys

### Limited Field Testing

**Documentation Gap**:[^supply]
- Few substantive field reviews
- Mostly promotional materials
- Community lacks long-term data
- Validation gaps remain

**Before Committing**:
- Research available reviews carefully
- Ask in community forums
- Look for actual user experiences
- Budget validation time and testing

## Installation & Setup

### Pre-Installation

**Documentation Requirements**:[^tracking]
1. Catalog serial numbers
2. Note MOSFET batch codes
3. Document thermal interface
4. Photograph all connections
5. Record firmware versions

**Why This Matters**:
- Community building comparison database
- Helps troubleshooting
- Enables warranty claims
- Contributes to collective knowledge

### Validation Testing

**First Ride Protocol**:[^thermal]
1. Start at conservative settings
2. Log thermal profiles immediately
3. Monitor all temperatures
4. Compare to X12 if available
5. Verify FR-4 sandwich delivers promised headroom

**What to Watch**:
- MOSFET temperatures
- Case temperatures
- Thermal throttling
- Performance consistency

## When to Choose Seven

**Good Fit If**:
- You can handle limited support
- You're comfortable with GPL issues
- You need 24S+ capability
- You can validate yourself
- You want to contribute to community knowledge

**Choose Alternatives If**:
- You need reliable support
- You want proven track record
- You need source code access
- You can't afford validation time
- You need guaranteed availability

## Alternative Recommendations

**For Similar Capability**:
- Tronic X12 (more established)
- 3Shul controllers (proven at high voltage)
- Spintend (better support, lower voltage)

**For Better Thermal**:
- K900 (direct-to-heatsink mounting)
- Other platforms with better heat dissipation

## Action Items for Seven Owners

### Before Installation

**Critical Steps**:[^firmware][^express][^thermal]
1. **Archive firmware and demand source**
2. **Verify Express telemetry** with separate board
3. **Log thermal profiles** on first rides
4. **Document pricing and support contacts**

### Ongoing

- Share findings with community
- Contribute to validation database
- Report issues publicly
- Help build collective knowledge

## Community Involvement

### VESC Museum Project

**Comparison Testing**:[^lineup][^tracking]
- Seven queued for benchmarking
- Compared against: Maxim, Tronic, MakerX
- Shared telemetry accelerates validation
- Community-driven documentation

**How to Contribute**:
- Share thermal data
- Post firmware experiences
- Document failures and successes
- Help others troubleshoot

## Related Guides

- [High-Voltage VESC Controller Market](../guides/high-voltage-vesc-controller-market-2025.md)
- [Controller Setup](../guides/controller_setup.md)
- [Motor Controller Tuning](../guides/motor_controller_tuning.md)

## References

[^lineup]: Source: knowledge/notes/input_part014_review.md, L52 to L54; L27 to L27
[^fw_baseline]: Source: knowledge/notes/input_part014_review.md, L54 to L54
[^firmware]: Source: knowledge/notes/input_part014_review.md, L147 to L148
[^express]: Source: knowledge/notes/input_part014_review.md, L146 to L148; L180 to L180
[^supply]: Source: knowledge/notes/input_part014_review.md, L163 to L164
[^thermal]: Source: knowledge/notes/input_part014_review.md, L164 to L164
[^tracking]: Source: knowledge/notes/input_part014_review.md, L217 to L217
[^1]: Source: data/raw/telegram_exports/vesc_help_group/input_part011.json, L21556 to L21680
