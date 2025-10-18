# VESC Labs High-Voltage Controllers (2025 Launch)

## Overview

In August 2025, VESC Labs (Vedder's team) launched their official high-voltage controller lineup, including the Maxim 120V, VESC Duet dual controller, and matching Smart BMS. This marks the first official high-voltage VESC hardware from the original developers. However, pricing and performance relative to Chinese alternatives remain subjects of debate.

## What You Need to Know

- Official VESC hardware from Benjamin Vedder's team
- STM32F4-based controllers with documented design
- Higher pricing than Chinese alternatives
- Limited field testing data so far
- Community actively benchmarking against competitors

## 💡 Why Choose VESC Labs?

✅ **Official Hardware**: Direct from VESC creator Benjamin Vedder
✅ **Documented Design**: STM32F4-based with open documentation
✅ **Native Support**: Direct manufacturer support channel
⚠️ **Trade-offs**: Premium pricing (~€530 for Duet), limited field data vs Chinese alternatives

## 📋 Quick Product Lineup

| Product | Voltage | Current | Price | Key Feature | Best For |
|---------|---------|---------|-------|-------------|----------|
| Maxim 120V | 120V | TBD | High | Official flagship | High-voltage racing |
| VESC Duet | 100V | 150A/side | ~€530 | Integrated dual | Plug-and-play dual motor |
| Smart BMS | Varies | Varies | TBD | Official BMS | Integrated VESC ecosystem |

## ⚠️ Critical VESC Labs Notes

🔴 **Premium Pricing**: ~€530 for Duet vs cheaper Chinese alternatives
🔴 **Limited Field Data**: 2025 launch means few community builds yet
🔴 **STM32F4**: Older MCU than some competitors—evaluate for your needs
🔴 **Active Benchmarking**: Community still comparing vs Spintend/Tronic/3Shul

## 💡 Pro Tips

- **Official support**: Worth premium if you value direct manufacturer backing
- **Documentation advantage**: Open design helps troubleshooting
- **Wait for field data**: Consider delaying until more community builds validate performance
- **Price comparison**: Evaluate against proven Spintend/Tronic options

## 🔧 Related Brand Dossiers

- [Spintend Controllers](spintend.md) - Established high-voltage alternative
- [Tronic Controllers](tronic.md) - Another high-voltage option
- [3Shul Controllers](3shul.md) - Premium racing controllers

## Product Line

### Maxim 120V (Single Controller)

**Specifications**:[^1][^2]
- **Voltage**: Up to 120V packs
- **MCU**: STM32F4 control silicon
- **Design**: Exposed capacitor bays for ventilation
- **Status**: Flagship single-motor option

**Target Use**: High-voltage race scooters needing native VESC support and official hardware.

### VESC Duet (Dual Controller)

**Specifications**:[^1][^2]
- **Voltage**: 100V peak (dual channel)
- **Phase Current**: 150A per side
- **Price**: ~€530 bundle
- **Features**:
  - Vented capacitor bays
  - Integrated balancing channels
  - Turnkey CAN coordination

**Target Use**: Dual-motor commuters seeking integrated solution with official support.

### Smart BMS

**Specifications**:[^1]
- **Voltage**: 120V-class packs
- **Features**:
  - Capacitor-equipped management
  - VESC-native telemetry
  - Integrated with Maxim ecosystem

**Target Use**: Builders wanting single-vendor control + BMS stack with seamless integration.

### Minim 100V (Compact)

**Specifications**:[^3]
- **Voltage**: 100V packs
- **Phase Current**: ~180A
- **Battery Current**: ~35A
- **Form Factor**: Compact for e-mopeds
- **Firmware**: VESC Tool aligned

**Target Use**: Lightweight scooters or mopeds prioritizing tidy packaging and VESC features.

## Price-to-Performance Debate

### The Question

At ~€530 for the Duet bundle, early adopters are asking:[^1]
- Does official hardware justify the premium?
- How does it compare to Chinese imports?
- Is the current headroom worth the cost?

### What Needs Validation

**Community Priorities**:[^1][^5]
1. Detailed teardowns with photos
2. Capacitor stack documentation
3. MOSFET part number verification
4. MCU resource confirmation
5. Real-world thermal testing
6. Performance data vs. competitors

> **📝 Note**: Launch marketing needs field validation. Community is actively testing to verify claims.

### Competitive Context

**Alternatives Being Compared**:[^1]
- Tronic controllers
- Spintend high-voltage options
- FarDriver for raw current capability
- Seven 18 (similar specs, different pricing)

## Field Testing Priorities

### Documentation Requirements

**For Every Installation**:[^2][^5]
- [ ] Photograph capacitor bay airflow paths
- [ ] Document thermal interface choices
- [ ] Note MOSFET part numbers
- [ ] Capture MCU identifiers
- [ ] Log vented design performance in enclosed decks

### Thermal Validation

**First Ride Testing**:[^2]
1. Monitor temperatures closely
2. Verify vented design effectiveness
3. Compare to alternatives if available
4. Document thermal throttling behavior
5. Test in enclosed deck installations

### CAN Integration Testing

**Interoperability Checks**:[^4][^6]
- Test with VESC Express modules
- Try third-party telemetry
- Verify reliable handshaking
- Compare to Seven 18 experiences (needed separate modules)

> **⚠️ Learning from Seven 18**: Early units needed separate Express modules for telemetry. Validate Maxim interoperability before deployment.

### Performance Logging

**Critical Data to Capture**:[^3]
- Duty cycle behavior
- Phase current actuals vs. commanded
- Battery sag under load
- Thermal performance
- Comparison with FarDriver (for Minim users)

## Firmware & Software

### VESC Tool Compatibility

**Known Issues**:[^tooling]
- VESC Tool 6.06 Android temporarily broke Bluetooth pairing
- Fixed in 6.06.4
- Desktop flashing recommended for new hardware
- Document software builds with telemetry

**Best Practice**:
- Test firmware before field deployment
- Keep backup of working versions
- Plan desktop flashes initially
- Join community for compatibility updates

### Open Source Compliance

**Important Consideration**:[^licensing]
- VESC firmware is GPL-licensed
- Seven 18 shipped without source code
- Press vendors to publish `.c/.h` files
- Community expects GPL compliance

**Why This Matters**:
- Enables modifications and fixes
- Supports community development
- Legal requirement under GPL
- Critical for long-term support

### VESC Express Boards

**Power Requirements**:[^express_logging]
- Needs external buck converter for 5V supply
- Only draws 5V / 150mA from Spintend rails
- Clean logging on 6.05
- 6.06 restarts every 3 seconds (firmware issue)

**Workarounds**:
- Use separate CAN modules if needed
- Budget for external power supplies
- Test thoroughly before deployment

## Comparison: Minim vs. FarDriver

### Decision Factors

**Minim 100V Advantages**:[^3]
- Tidy harnessing
- VESC firmware features
- Better integration
- ~180A phase / ~35A battery

**FarDriver Advantages**:[^3]
- Higher battery current limit
- Trapezoidal brute force
- Proven for high-current applications

**Choose Minim If**:
- You value firmware polish
- You want VESC Tool features
- Compact packaging is priority
- 35A battery is sufficient

**Choose FarDriver If**:
- You need maximum battery current
- Simplicity over features
- Proven track record matters
- Current is the limiting factor

## Community Benchmarking

### VESC Museum Project

**JPPL's Comparison Fleet**:[^4]
Currently includes:
- Thor controllers
- MakerX hardware
- Tronic controllers
- Ennoid platforms

**Adding for Comparison**:
- VESC Labs Maxim/Duet
- Seven 18 controllers

**Purpose**: Consistent testbed for validating new controller releases against known-good hardware.

### How to Contribute

1. **Share thermal data** from installations
2. **Post detailed teardowns** with photos
3. **Log performance metrics** (phase/battery current, temps)
4. **Document failures and successes**
5. **Help others troubleshoot** issues

## Installation Checklist

### Pre-Installation

- [ ] Research available reviews and field reports
- [ ] Join community forums for latest updates
- [ ] Archive firmware before installation
- [ ] Budget validation time and testing
- [ ] Have backup controller plan

### During Installation

- [ ] Document capacitor configuration
- [ ] Photograph thermal interfaces
- [ ] Note all part numbers
- [ ] Record firmware versions
- [ ] Test CAN communication

### Post-Installation

- [ ] Log first ride temperatures
- [ ] Capture performance data
- [ ] Compare to expected specs
- [ ] Share findings with community
- [ ] Document any issues

## When to Choose VESC Labs

**Good Fit If**:
- You want official VESC hardware
- You value Benjamin Vedder's support
- You need documented, vetted design
- You're willing to pay premium
- You want to support open-source development

**Consider Alternatives If**:
- Budget is primary concern
- You need proven track record
- Higher current limits required
- Chinese import pricing more attractive
- Immediate availability critical

## Current Limitations

### Field Testing

**What We Don't Know Yet**:[^1]
- Long-term reliability data
- Real-world thermal performance in various climates
- Comparative performance vs. competitors
- Failure modes and weak points
- Optimal tuning parameters

**Community actively gathering this data.**

### Availability

- Recently launched (August 2025)
- Shipping status varies by region
- Lead times unknown
- Stock levels unclear

## Related Guides

- [High-Voltage VESC Controller Market](../guides/high-voltage-vesc-controller-market-2025.md)
- [Controller Setup](../guides/controller_setup.md)
- [Motor Controller Tuning](../guides/motor_controller_tuning.md)

## References

[^1]: Source: knowledge/notes/input_part014_review.md, L25 to L27
[^2]: Source: knowledge/notes/input_part014_review.md, L26 to L27
[^3]: Source: knowledge/notes/input_part014_review.md, L203 to L204
[^4]: Source: knowledge/notes/input_part014_review.md, L27 to L27
[^5]: Source: knowledge/notes/input_part014_review.md, L213 to L213
[^6]: Source: knowledge/notes/input_part014_review.md, L146 to L148
[^7]: Source: knowledge/notes/input_part014_review.md, L24 to L148
[^tooling]: Source: knowledge/notes/input_part014_review.md, L4519 to L4524; L5111 to L5114
[^licensing]: Source: knowledge/notes/input_part014_review.md, L147 to L147
[^express_logging]: Source: knowledge/notes/input_part014_review.md, L138 to L140; L146 to L148; L180 to L180
