# Ennoid Controllers

## Overview

Ennoid produces high-voltage VESC controllers designed for extreme performance electric scooter builds. Their MK8 model shares the Spintend 85150 footprint but requires significant modifications to reach its advertised 26S / 500A phase capability. Ennoid controllers use shunt-based current sensing, which provides more accurate motor detection than current-transformer designs.

## Product Line

### MK8 Controller

**Stock vs. Modified Performance**:

| Aspect | Stock Hardware | After Toll FET Upgrade |
|--------|----------------|----------------------|
| Voltage | ~20S (derated) | 26S capable |
| Phase Current | Limited | 500A target |
| MOSFETs | Factory | Infineon IPTC017N12NM6 |
| Status | Not recommended | Community-proven |

**Key Requirement**: MK8 controllers only reach advertised specs after swapping to Infineon IPTC017N12NM6 Toll MOSFETs and reworking the power stage.[^mk8_swap]

### Upcoming: 100V/75A Single

**Specifications** (preliminary):[^single_75a]
- Dimensions: ~70 × 75 × 16mm
- Voltage: 100V capable
- Current: 75A
- Target Price: ~$200
- Application: Small-deck builds

**Status**: Teased product, could fill gap while waiting for Spintend single-channel release.

## Why Choose Ennoid: Shunt-Based Sensing

### Technical Advantage

**Current Sensing Method**:[^ct_vs_shunt]
- **Ennoid**: Shunt-based sensing (direct measurement)
- **Some Competitors**: Current transformer (CT) sensing

**When It Matters**:
- CT-based controllers (like some Spintend models) can mis-detect motors around 100A
- Shunt sensing provides more consistent auto-detect behavior
- Better for high-current applications (>100A)

**Smart Repair Recommendation**: Use Ennoid's shunt-sensed design when CT controllers have detection issues.[^ct_vs_shunt]

> **📝 Technical Note**: Shunt sensors measure current directly through resistive elements, while CT sensors use induction. Shunts are more accurate but generate more heat.

## MK8 Upgrade Workflow

### Prerequisites

**Tools & Materials Needed**:
- Hotplate for board preheating
- Hot air rework station
- Temperature-controlled soldering iron
- Thermal paste
- Infineon IPTC017N12NM6 Toll MOSFETs (genuine parts)

**Skills Required**:
- SMD rework experience
- Understanding of thermal management
- VESC configuration knowledge

### Step-by-Step Upgrade Process

**1. Source Genuine MOSFETs**:[^mk8_swap]
- Part number: Infineon IPTC017N12NM6
- Verify authenticity (counterfeits exist)
- Log lot codes for quality tracking
- Inspect legs before installation

**2. MOSFET Replacement**:
- Preheat IMS board on hotplate
- Use hot air to remove stock MOSFETs evenly
- Clean pads thoroughly
- Flow new Toll packages with hot air
- Avoid warping aluminum substrate

**3. Thermal Interface Refresh**:
- Remove old thermal paste completely
- Apply fresh high-quality paste
- Torque mounting hardware properly
- Ensure even pressure across MOSFETs

**4. Recalibration & Testing**:[^ct_vs_shunt]
- Rerun motor detection after upgrade
- Validate shunt scaling
- Test at low power first
- Gradually increase to target specs
- Monitor temperatures closely

> **⚠️ Warning**: Skip this upgrade if you lack rework capability. Unmodified MK8 hardware behaves like a Spintend 85150 with less firmware support.

## Benchmarking Role

### VESC Museum Reference

**JPPL's Controller Inventory**:[^museum]
- Maintains Ennoid alongside Thor, MakerX, Tronic
- Used as shunt-based control sample
- Enables apples-to-apples comparisons
- Validates new controller launches

**Why This Matters**:
- Having known-good reference controllers is essential
- Shunt-based design provides baseline
- Community can validate new releases against proven platform

**Best Practice**:
- Archive firmware versions with telemetry data
- Document each reworked MK8's performance
- Share findings with community
- Create baseline for future controller comparisons

## Performance Expectations

### After Toll FET Upgrade

**Realistic Targets**:
- 26S pack voltage (validated)
- ~500A phase current (with proper cooling)
- Reinforced busbars required
- Excellent motor detection

**Critical Requirements**:
- Proper thermal management
- Quality busbar connections
- Calibrated shunt readings
- Conservative initial tuning

## When to Choose Ennoid

**Good Fit If**:
- You have SMD rework capability
- You need shunt-based current sensing
- You're building extreme performance scooter (>20S)
- You want to avoid CT sensing issues
- You're willing to modify hardware

**Choose Alternatives If**:
- You need turnkey solution
- You lack rework skills/equipment
- You want easier parts sourcing
- You need extensive support network

## Alternative Recommendations

**For Turnkey High Power**:
- 3Shul (validated >500A output)
- Tronic X-series (when available)
- Spintend 85/240 (if CT sensing works for your motors)

**Advantages of Alternatives**:
- No modification required
- Easier parts sourcing
- More community support
- Validated performance out of box

## Maintenance & Support

**Parts Availability**:
- Replacement MOSFETs available through normal channels
- Toll FET upgrades documented by community
- DIY-focused platform (less official support)

**Community Knowledge**:
- Smaller user base than Spintend
- Focus on high-performance builds
- Technical users sharing upgrade procedures

## Related Guides

- [Controller Setup](../guides/controller_setup.md)
- [High-Power VESC Scooter Reliability Guide](../guides/high-power-vesc-scooter-reliability-guide.md)
- [Motor Controller Tuning](../guides/motor_controller_tuning.md)

## References

[^mk8_swap]: Ennoid MK8 shares the Spintend 85150 footprint but relies on Infineon IPTC017N12NM6 Toll MOSFET swaps to stretch toward 26 S / 500 A phase capability. Source: knowledge/notes/input_part014_review.md, L12 to L13
[^ct_vs_shunt]: Smart Repair's diagnosis that Spintend's current-transformer sensing saturates near 100 A and their recommendation to pivot heavy builds to shunt-based MK8/X12 hardware until an 18-FET refresh arrives. Source: knowledge/notes/input_part014_review.md, L12 to L13
[^museum]: JPPL's "VESC museum" inventory—Thor, MakerX, Tronic, Ennoid—maintained to benchmark future Maxim/Seven releases under identical conditions. Source: knowledge/notes/input_part014_review.md, L27 to L27
[^single_75a]: Source: knowledge/notes/input_part000_review.md, line 211.
