# Happy BMS

## Overview

Happy BMS is a smart battery management system developed by Denis Yurev and Happy Giraffe as an alternative to Daly BMS clones. Designed specifically for Xiaomi-compatible electric scooters, it supports 9-15S lithium-ion packs with embedded coulomb counting and telemetry integration.

**Price**: ~€69 plus shipping (sold direct by Denis Yurev)

## 💡 Why Choose Happy BMS?

✅ **Coulomb Counting**: Embedded state-of-charge tracking
✅ **Xiaomi Integration**: Native telemetry for stock dashboards
✅ **Denis Quality**: Designed by community expert Happy Giraffe/Denis Yurev
⚠️ **Trade-offs**: 44A current limit, large pack capacity readout issues

## 📋 Quick Specifications

| Feature | Specification |
|---------|--------------|
| **Chemistry Support** | 9-15S lithium-ion packs |
| **Discharge Current** | 44A continuous (fuses blow ~60A) |
| **Charge Current** | 3A default, 5.5A max (via Embedden tools) |
| **Form Factor** | Compact Xiaomi-compatible PCB |
| **Connectors** | XT30/XT60 harness options |
| **Features** | Coulomb counting, Xiaomi telemetry, USB/UART app access |

## ⚠️ Critical Happy BMS Warnings

🔴 **44A Trip Point**: Not suitable for >3kW builds—trips after 1 second at 44A
🔴 **60A Fuse Limit**: Hard limit at fuse—plan external contactors for high power
🔴 **Large Pack Issues**: Display shows 0% with ~3Ah remaining—use voltage monitoring
🔴 **32Ah Rating**: Works with larger packs but capacity display bottoms out early

## 💡 Pro Tips

- **Voltage monitoring**: Use pack voltage for range on >32Ah builds
- **3kW limit**: Step up to LLT/JBD or ANT for higher power applications
- **Coulomb counting value**: Best feature for accurate SoC on Xiaomi platforms
- **Denis support**: Direct from designer—good for troubleshooting

## 🔧 Related Brand Dossiers

- [LLT/JBD Smart BMS](../guides/llt-jbd-smart-bms-integration-handbook.md) - Higher current alternative
- [Denis Yurev Workshop](denis_yurev_workshop.md) - Designer's other products

## Key Features

### Coulomb Counting

**Smart Capacity Tracking**:[^1][^2]
- Embedded state-of-charge calculation
- Red status LED for visual feedback
- USB/UART tooling for app access
- Xiaomi telemetry integration

### Oversized Pack Support

**Capacity Handling**:[^3][^4]
- Officially rated for 32Ah
- Works with larger packs beyond rating
- **Caveat**: Display bottoms out early on large packs
- ~3Ah remains when counter shows 0%
- **Solution**: Plan range using voltage once counter saturates

> **💡 Pro Tip**: On large packs, rely on voltage monitoring rather than the percentage display for accurate range planning.

## Current Limitations

### Fixed Current Handling

**Hard Limits**:[^5][^6]
- **Trips after ~44A** for more than 1 second
- **Fuses blow near 60A**
- **Not suitable for 3kW builds** (50-60A continuous)
- **Workarounds**: External contactors or different BMS for high power

### Charge Current Management

**Default Conservative Setting**:[^7]
- Ships with 3A charge limit
- Protects Xiaomi charge leads
- **Upgrade**: Use Embedden BMS Tool
- Can raise to 5.5A with thicker harnesses

> **⚠️ Important**: Only increase charge current after upgrading to thicker wiring. Stock Xiaomi leads are not rated for 5.5A.

## Sleep Mode & Wake-Up

### Operational Behavior

**Sleep Characteristics**:[^8][^9]
- Packs sleep until charger connected
- Balancing can occur at any state of charge
- **Self-discharge**: ~0.6% per day when stored
- **Wake-up**: Quick top-up before riding

**Common Issue**: Pack shows voltage but no output
- **Cause**: Board ships asleep
- **Solution**: Connect charger briefly to wake discharge MOSFETs

## Integration with Scooter Systems

### Rita & XiaoDash Compatibility

**Setup Requirements**:[^10][^11][^12]
- Downgrade BLE firmware for compatibility
- Enable live current logging
- Rita enforces ~30A limit
- Happy BMS monitors pack temperature
  - Charging pauses near 40°C
  - Resumes when cooled to ~35°C

### Charging Safety

**Critical Warning**:[^13]
- **Never charge through XT30 discharge lead**
- Bypasses over-voltage protection
- Only do under direct supervision with voltmeter

**Charger Compatibility**:[^14]
- Tolerates wrong voltage chargers (e.g., 54.6V on 14S)
- Stops charging early
- Cells remain safe but range reduced
- Get proper charger for full capacity

### External Pack Wiring

**Best Practices**:[^15][^16]
- Use common-port wiring
- Keep external protection inline
- Happy BMS blocks output on shorts
- Cannot replace fuses or Rita's diode isolation alone

## Installation & Wiring

### Critical Wiring Procedure

**Follow Official Diagram**:[^17]
- Builders who doubled balance wires bricked Daly boards
- Misordered leads cause instant failure
- Documentation prevents these mistakes

**Wiring Order**:
1. Connect negative first
2. Confirm each voltage step with meter
3. Never stack two wires on one pad
4. Double-check before powering on

### Display Calibration

**For Large Packs**:[^3][^4]
- Display hits 0% before pack empty
- Use voltage logs for accuracy
- Or XiaoDash telemetry
- Plan range based on voltage, not percentage

## Troubleshooting Guide

| Symptom | Likely Cause | Resolution |
|---------|--------------|------------|
| **No output despite voltage** | Board asleep until first charge | Connect charger briefly to wake MOSFETs[^8] |
| **Output latched off after reconnect** | Inrush protection tripped | Blip charger to reset MOSFETs[^happy-latch] |
| **Charging stalls below pack voltage** | Supply under 47V on 48V builds | Use true 48V CC/CV charger[^18] |
| **Error 24 or BLE faults after flash** | Flashed without 10S reference pack | Flash with lower voltage pack, reconfigure in app[^19] |
| **Repeated fuse trips above 44A** | Exceeding design envelope | Upgrade wiring, consider Daly/ANT for ≥50A[^5] |
| **Coulomb counter misreads LiFePO₄** | Firmware assumes 4.1V chemistry | Charge above 3.5V to recalibrate[^20] |
| **Daly died after wiring mistake** | Misordered/doubled sense wires | Rewire per Happy documentation carefully[^17] |

## Regional Availability

### Shipping Restrictions

**Cannot Currently Ship To**:[^21]
- Indonesia
- Vietnam

**Workarounds**:
- Use freight forwarders
- Substitute JBD smart boards
- Pair with ScooterHacking Utility

### Pricing Context

**Turnkey vs. DIY**:[^22]
- Denis quotes ~€290 for complete 13S3P pack with Happy BMS
- Includes labor and QA
- Compare to DIY NKON builds
- Consider time vs. money trade-off

## Field Deployments

**Proven Applications**:[^23][^24]
- 10S7P Ninebot Max G2 packs
- 48V Pro/Pro 2 conversions
- XiaoDash configured for 13 cells, 20Ah
- Reliable operation reported

## Safety Guidelines

### Current Limits

**Strict Adherence Required**:[^25]
- Respect 44A discharge ceiling
- Keep regen below ~30A
- Exceeding limits causes:
  - Error 39 trips
  - Pack overheating
  - Can explode Rita on higher voltages

### Accessory Power

**Never Use Charge Port**:[^26]
- Don't power accessories from charge port
- Build DC/DC harnesses off discharge rails
- Preserves Happy BMS protections

### Waterproofing

**Maintenance Requirements**:[^27][^28]
- Seal deck seams
- Grease bearings regularly
- Inspect harnesses after rain
- Prevents latent shorts
- Happy BMS will flag persistent faults

## When to Choose Happy BMS

**Good Fit If**:
- Building Xiaomi-compatible scooter
- Need up to 44A continuous
- Want coulomb counting
- Value Denis Yurev's support
- Can work with capacity display quirks

**Consider Alternatives If**:
- Need >44A continuous current
- Building 3kW+ system
- Shipping to restricted regions
- Require LiFePO₄ support
- Need larger charge current capability

## Related Guides

- [Daly BMS Waterproofing](../guides/daly-bms-waterproofing.md)
- [Smart BMS Integration Handbook](../guides/smart-bms-integration-handbook.md)
- [Battery Pack Design](../guides/battery_pack_design.md)

## References

[^1]: Source: knowledge/notes/denis_all_part02_review.md, L1233 to L1233
[^2]: Source: knowledge/notes/denis_all_part02_review.md, L1595 to L1595
[^3]: Source: knowledge/notes/denis_all_part02_review.md, L16 to L17
[^4]: Source: knowledge/notes/denis_all_part02_review.md, L399 to L401
[^5]: Source: knowledge/notes/denis_all_part02_review.md, L73 to L74
[^6]: Source: knowledge/notes/denis_all_part02_review.md, L322 to L323
[^7]: Source: knowledge/notes/denis_all_part02_review.md, L476 to L477
[^8]: Source: knowledge/notes/denis_all_part02_review.md, L376 to L376
[^9]: Source: knowledge/notes/denis_all_part02_review.md, L479 to L481
[^10]: Source: knowledge/notes/denis_all_part02_review.md, L11 to L12
[^11]: Source: knowledge/notes/denis_all_part02_review.md, L316 to L316
[^12]: Source: knowledge/notes/denis_all_part02_review.md, L55 to L57
[^13]: Source: knowledge/notes/denis_all_part02_review.md, L185 to L186
[^14]: Source: knowledge/notes/denis_all_part02_review.md, L108 to L108
[^15]: Source: knowledge/notes/denis_all_part02_review.md, L64 to L65
[^16]: Source: knowledge/notes/denis_all_part02_review.md, L532 to L532
[^17]: Source: knowledge/notes/denis_all_part02_review.md, L374 to L376
[^18]: Source: knowledge/notes/denis_all_part02_review.md, L396 to L397
[^19]: Source: knowledge/notes/denis_all_part02_review.md, L543 to L544
[^20]: Source: knowledge/notes/denis_all_part02_review.md, L1670 to L1671
[^21]: Source: knowledge/notes/denis_all_part02_review.md, L1586 to L1587
[^22]: Source: knowledge/notes/denis_all_part02_review.md, L253 to L253
[^23]: Source: knowledge/notes/denis_all_part02_review.md, L116 to L117
[^24]: Source: knowledge/notes/denis_all_part02_review.md, L1625 to L1626
[^25]: Source: knowledge/notes/denis_all_part02_review.md, L618 to L618
[^26]: Source: knowledge/notes/denis_all_part02_review.md, L70 to L71
[^27]: Source: knowledge/notes/denis_all_part02_review.md, L553 to L553
[^28]: Source: knowledge/notes/denis_all_part02_review.md, L536 to L536
[^happy-latch]: Source: data/vesc_help_group/text_slices/input_part004.txt†L19788-L19840
