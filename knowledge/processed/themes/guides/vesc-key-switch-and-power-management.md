# VESC Key Switch & Power Management Guide

## Overview

VESC controllers require proper power management understanding to implement safe key switches and power-off functionality. This guide explains VESC power architecture, safe switching methods, common failures, and best practices for implementing ignition systems.

## What You'll Learn

- VESC power architecture and latch behavior
- Why simple switches often fail or explode
- Proper key switch implementation methods
- Brand-specific controller considerations
- Anti-spark system requirements
- BMS integration for power control


## 🔧 Related Guides

- [Power Distribution](power_distribution.md) - Wiring and connector sizing
- [VESC Accessory Power](vesc-accessory-power-and-display-integration.md) - Accessory power budgets
- [Controller Setup](controller_setup.md) - Initial VESC configuration
- [Smart BMS Integration](smart-bms-integration-handbook.md) - BMS-based power control

## ⚠️ Critical Safety Warning

> **🔥 DANGER**: Improper key switch implementation can cause:
> - Switch explosions
> - Full-throttle runaways
> - Controller damage
> - Fire hazards
>
> Never hang undersized switches on main power lines. Follow this guide carefully.

## Understanding VESC Power Architecture

### Logic Rail Behavior

**Key Fact**:[^vesc_latch]
- **Logic rail stays live** whenever pack is connected
- Tying 5V switch pin to ground turns controller "off"
- **This is NOT a true power disconnect**
- Battery still connected to controller

**Implications**:
- Standby power draw continues
- True power-off requires upstream disconnect
- BMS latching, loop keys, or contactors needed

### Flipsky Aluminum Units

**Special Requirements**:[^vesc_latch]
- Need external contactors
- Or BMS gating
- Without these: MOSFET stress during standby
- No proper enable pin like some controllers

## Brand-Specific Architectures

### Spintend Controllers

**Single-Board Architecture**:[^spintend_latch]
- Relies on MOSFET stack as "big switch"
- **No dedicated latch rail**
- Can't intercept with simple key
- Cutting traces = risky micro-surgery

**Required Solution**:
- Proper upstream contactors
- Not relay hacks on low-voltage wiring

**Latching Button Polarity**:[^spintend_button]
- Ships wired opposite to Rosheee automotive switch
- Must swap LED and +/− leads
- Controller stays latched on if wrong
- Confirm logic before final assembly

### Makerbase Controllers

**75100 Units**:[^makerbase_latch]
- Expect momentary latch
- Bridge 5V to AD15 enable pin
- Hold ~1 second to turn on
- Hold ~3 seconds to shut down
- Set ADC shutdown timer correctly

**84100HP Units**:[^makerbase_84100][^3]
- Need normally-closed switch
- Or documented 1MΩ pull-down
- Mimics Ubox-style keys
- Source NC hardware or build relay adapter

**84100HP Conversion**:[^84100hp-key]
- @fungus93's hack easier than older 75100
- Document pin swap and harness photos
- Thread may disappear - archive it

**Emergency Trace-Cut**:[^trace-cut]
- Tommy and Mirono used 5V step-down trace cut
- Plus gated 12V chip to force shutdown
- Regulator is fragile
- **Last resort only**, not daily use

### Flipsky 75100 Standby

**Vampire Drain**:[^75100-standby]
- Idles at ~5mA standby
- Without antispark: physically disconnect
- Use XT90S loop keys between rides
- Prevents weeks-long drain

## Common Failure Modes

### Switch Explosions

**The Problem**:[^antispark_fail]
- Generic anti-spark buttons on K-line ignition leads explode
- Switches rated for milliamps, not battery current
- Strict voltage/current ratings ignored

**Why It Happens**:
- Switch rated for signal-level current only
- Hung on main battery power
- Inrush current overwhelms contacts
- Catastrophic failure

> **⚠️ Critical**: Size switches for actual current path or move to DC/DC enable lines.

### Full-Throttle Runaway

**The Danger**:[^key_adc_danger]
- Martin's relay on ADC line triggered runaway
- 0V ADC = maximum duty in some configs
- Can cause uncontrolled acceleration

**Never Do This**:
- Don't break ADC throttle line with switch
- Don't use relay on throttle signal

**Safe Alternatives**:
- Switch DC/DC enable
- Force e-brake input
- Use proper latch control

### Precharge Resistor Damage

**Common Issue**:[^4]
- Noname found precharge strip heating
- After repeated plug cycles
- Can melt under high-current starts

**Prevention**:
- Inspect anti-spark resistors regularly
- Replace browned hardware
- Don't over-cycle connections

## Proper Implementation Methods

### Method 1: DC/DC Enable Switching

**Safest Approach**:
1. Switch the DC/DC enable pin
2. Or use smart-BMS control
3. Don't interrupt main battery power
4. Avoids undersized switches

**Advantages**:
- No high-current switching
- No explosion risk
- Clean power control
- Can use small switch

### Method 2: External Contactors

**For True Power-Off**:
- Loop keys (XT90S)
- Smart-BMS latching
- External contactors rated for pack V/A

**When Needed**:
- True power isolation required
- Multiple controllers
- High-current applications
- Professional installations

### Method 3: Smart-BMS Integration

**Modern Solution**:
- BMS handles main power
- Controller signals BMS for wake/sleep
- Integrated precharge
- Proper current ratings

**Benefits**:
- Safest method
- Proper precharge handling
- Current protection built-in
- Professional grade

## Switch Sizing Guidelines

### If Using Main Power Switch

**Requirements**:
1. **Verify current rating** for actual path
2. **Check voltage rating** matches pack
3. **Confirm contact type** (AC vs DC ratings differ)
4. **Calculate inrush** - much higher than continuous
5. **Add precharge** if needed

**Most "Anti-Spark" Switches**:
- Only rated for signal-level currents
- Can't handle battery power
- Will explode or weld
- Not suitable for main power

### Precharge Resistor Values

**Too High (1kΩ)**:[^precharge_value]
- Stayed hot
- Delayed startup
- High-capacitance controllers affected

**Better Approach**:
- Lower-value resistors
- Purpose-built anti-spark circuits
- Charge capacitors promptly
- Don't cook the switch

### Latching vs Momentary

**Latching Switch**:[^1]
- Stays in position
- No need to hold key
- VESC stays powered
- Proper solution

**Momentary Toggle**:
- Forced riders to hold key
- Not practical
- Timing games required
- Avoid for main power

## Anti-Spark Systems

### XT90S Loop Keys

**Characteristics**:
- Built-in precharge resistor
- Designed for battery connection
- Make/break without arcing
- Practical for most builds

**Limitations**:
- Precharge resistor can overheat
- Repeated hot-plugs cook resistors
- Not rated for 300-600A bursts

### AS150 Anti-Spark

**Advantages**:
- Higher current rating
- Better precharge circuits
- More robust contacts
- Professional grade

**When to Use**:
- High-power systems
- Frequent connect/disconnect
- Professional installations

### QS8/QS10 Connectors

**For Extreme Current**:
- 300-600A burst capability
- Proper crimps and strain relief required
- Heavy-duty solution
- Not for casual builds

## BMS Integration

### ANT BMS Precharge

**Current Limits**:[^ant_precharge][^ant_cold]
- Rated for 20A "starting current"
- Repeated MOSFET failures above this
- Cold weather: Owners wanted 30A
- **Warning**: Exceeding 20A blows FETs

**Safe Approach**:
- Use built-in limit
- External 100Ω precharge buttons
- Don't routinely exceed 20A
- Use external resistors if needed

**Balancing**:
- ANT balances at only ~150mA
- Compare to JK's 2A
- Factor into charge time planning

### Happy BMS Wake Behavior

**Latch-Off Recovery**:[^happy_wake]
- Some units latch off after reconnecting
- Require charger wake signal
- Briefly attach charger to revive
- Xiaomi-oriented BMS boards may need this
- Protection trips on inrush

### JK BMS Toggles

**Not a Substitute**:[^jk-toggle]
- Bluetooth toggles can wake packs
- **But**: 100A bursts need dedicated antispark
- Don't rely on toggle as main disconnect
- Use proper contactor for power

## Power Management Best Practices

### Daily Operation Checklist

1. **Document baseline idle draw**
   - Expect ~20mA standby with latching button off
   - Any illuminated LED = wiring fault

2. **Use proper anti-spark connectors**
   - XT90S loop keys for moderate power
   - AS150 for higher current
   - QS8/QS10 for extreme applications

3. **Verify polarity before power-up**
   - Fresh Ubox units shipped with reversed BT harness
   - Killed modules instantly
   - Check continuity first

4. **Relay heavy lighting loads**:[^2]
   - Spintend clusters source 12V
   - Run through DC/DC and relay
   - Actually shut off when key opens

5. **Wait for capacitor discharge**:[^5][^6]
   - Dual Ubox briefly wakes from stored energy
   - Even with pack unplugged
   - Watch status LEDs go dark
   - Depower accessories before unplugging

6. **Trigger external 12V with controller**:[^7]
   - One Vsett 10+ drives Arduino relay from VESC 5V
   - Energizes battery-fed 12V converter
   - Keeps lights off fragile OEM fuse
   - Powers on with controller

### Safety Checklist

- [ ] Never use ADC lines for power switching
- [ ] Size anti-spark switches properly (current + voltage)
- [ ] Keep BMS within precharge ratings
- [ ] Plan for BMS wake requirements
- [ ] Inspect precharge resistors regularly
- [ ] Test polarity before first power-up
- [ ] Document idle current draw
- [ ] Use proper contactors for true isolation

## Troubleshooting Guide

### Controller Won't Stay On

**Possible Causes**:
1. Momentary switch instead of latching
2. Incorrect enable pin wiring
3. ADC shutdown timer not set
4. BMS cutting power
5. Insufficient precharge time

**Solutions**:
- Verify latch switch type
- Check enable pin connections
- Set shutdown timer correctly
- Check BMS settings
- Allow full capacitor charge

### Switch Overheats or Fails

**Causes**:
1. Undersized for current
2. Too many hot-plug cycles
3. Precharge resistor inadequate
4. Inrush current too high

**Solutions**:
- Upsize to proper rating
- Minimize connect/disconnect cycles
- Add proper precharge circuit
- Use external contactor

### Vampire Drain

**Causes**:
1. No true power disconnect
2. Logic rail staying powered
3. Accessories left connected
4. BMS standby draw

**Solutions**:
- Install loop key or contactor
- Disconnect between long storage periods
- Remove accessory loads
- Check BMS current draw

## Related Guides

- [Power Distribution](power_distribution.md)
- [Controller Setup](controller_setup.md)
- [Smart BMS Integration Handbook](smart-bms-integration-handbook.md)

## References

[^vesc_latch]: Source: knowledge/notes/input_part004_review.md†L56-L56
[^antispark_fail]: Source: knowledge/notes/input_part004_review.md†L269-L269,†L595-L595
[^spintend_latch]: Source: knowledge/notes/input_part004_review.md†L24-L24
[^spintend_button]: Source: data/vesc_help_group/text_slices/input_part002.txt†L12159-L12179
[^key_adc_danger]: Source: knowledge/notes/input_part004_review.md†L300-L300
[^ant_precharge]: Source: knowledge/notes/input_part004_review.md†L57-L57
[^ant_cold]: Source: knowledge/notes/input_part004_review.md†L80-L80
[^happy_wake]: Source: knowledge/notes/input_part004_review.md†L302-L302
[^makerbase_latch]: Source: knowledge/notes/input_part004_review.md†L36
[^makerbase_84100]: Source: knowledge/notes/input_part004_review.md†L36
[^75100-standby]: Source: knowledge/notes/input_part002_review.md†L210-L210
[^precharge_value]: Source: data/vesc_help_group/text_slices/input_part002.txt†L12457-L12463
[^84100hp-key]: Source: knowledge/notes/input_part007_review.md†L112-L112
[^trace-cut]: Source: knowledge/notes/input_part007_review.md†L208-L208
[^jk-toggle]: Source: knowledge/notes/input_part007_review.md†L227-L227
[^1]: Source: knowledge/notes/input_part003_review.md†L101-L101
[^2]: Source: knowledge/notes/input_part003_review.md†L128-L128
[^3]: Source: data/vesc_help_group/text_slices/input_part009.txt†L13398-L13404
[^4]: Source: data/vesc_help_group/text_slices/input_part009.txt†L20442-L20448
[^5]: Source: data/vesc_help_group/text_slices/input_part009.txt†L19021-L19022
[^6]: Source: data/vesc_help_group/text_slices/input_part009.txt†L15284-L15290
[^7]: Source: data/vesc_help_group/text_slices/input_part009.txt†L6603-L6608
