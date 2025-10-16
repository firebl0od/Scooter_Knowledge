# Kelly Controllers

## Overview

Kelly produces motor controllers for electric vehicles including scooters. Their controllers are known for solid basic performance but require careful attention to accessory power management and wiring practices. Kelly controllers use a simpler control approach than VESC systems, with different strengths and limitations.

## Product Line

### Kelly 7212 Single Controller

**Performance Profile**:[^1]
- **Phase Current**: ~200A from 48V packs comfortable
- **Battery Draw**: ~50% of phase current rating
  - Example: 120A phase ≈ 80A battery draw
- **Pack Voltage**: 48V typical (other voltages available)

**Power Management Issue**:[^1]
- Onboard DC/DC rail brownouts under accessory load
- **Solution**: Wire horns and lighting direct to battery through relays
- Do not rely on controller's DC/DC for significant loads

### KLS7230 Dual Controller System

**Applications**:[^ip001-kelly-7230]
- Blade conversions
- 20S10P Samsung 40T packs
- ~350A discharge capability
- Oversized hub motors

**Requirements**:
- TIG-reinforced frames
- External controller mounting
- Robust wiring and connectors

### CL/Kelly High-Spec Models

**Advertised Ratings**:[^3]
- 350A continuous
- 700A peak

**Reality Check**:[^3]
- Veterans tune conservatively despite ratings
- Complete autotune by hand to avoid firmware bricks
- Start below max ratings and work up gradually

## Wiring & Setup

### Dual Controller Configuration

**Signal Wiring** (for AWD builds):[^3]
- **Throttle**: Parallel 5V, ground, and signal to both controllers
- **Brake**: Parallel brake sensor inputs
- **Power Button**: Parallel enable signals
- **No CAN Bridge Required**: Simpler than VESC dual setups

**Connection Quality Matters**:[^4][^5]
- Use Higo or JST sealed connectors
- Keep water out of deck
- Simplifies throttle/key splits
- Enables clean dual-controller harnesses

### Power Connection Requirements

**Antispark Hardware**:[^2]
- **Don't Use**: XT90S resistor connectors
- **Problem**: Cannot survive Kelly inrush during autotune
- **Use Instead**: QS8/QS10 class antispark connectors
- **Or**: Proper pre-charge circuit

> **⚠️ Critical**: XT90S resistors fail explicitly with Kelly controllers. This is a known issue, not user error.

## Accessory Power Management

### DC/DC Rail Limitations

**The Problem**:[^1]
- Onboard 12V rail browns out under load
- Horns cause controller resets
- LED strips can force resets
- Not suitable for real accessory loads

**The Solution**:
1. **Power accessories direct from battery**
2. **Use relays for switching**
3. **Or use smart-BMS switching**
4. **Treat controller outputs as logic-level triggers only**

**Why This Works**:
- Battery can supply the current
- Relays isolate controller from load
- Controller stays stable
- More reliable overall system

### Example Wiring

```
Battery (+) ──► Relay ──► Horn/Lights
               │
Controller ────┘ (trigger only, not power)
```

## Current Ratings & Thermal Management

### Understanding Specifications

**Battery vs. Phase Current**:[^1]
- Kelly datasheets show phase current
- Actual battery draw is ~50% of phase rating
- Example: 120A phase = 80A battery continuous

**Wiring Implications**:
- Size wiring for battery current, not phase
- Fusing based on battery draw
- Thermal calculations use battery power

**Monitoring**:
- Log temperatures before increasing current
- Start conservative and work up
- Validate thermal performance at each step

### CL-Series Cautions

**Even with High Ratings**:[^3]
- Start below advertised specs
- Ramp slowly after autotune
- Firmware glitches possible at max ratings
- Conservative approach prevents issues

## Safety Procedures

### During Service

**Battery Disconnection**:[^6]
- **Always disconnect battery before soldering**
- **Never work on energized harnesses**
- **Lesson**: One energized repair ignited nearby Makerbase board

**Why This Matters**:
- Lithium fires are serious
- Controller damage possible
- Personal safety risk
- Simple precaution prevents disasters

### During Installation

1. **Disconnect battery first**
2. **Complete all wiring work**
3. **Double-check all connections**
4. **Verify no shorts**
5. **Only then reconnect battery**

## Autotune & Commissioning

### Initial Setup

**CL-Series Approach**:[^3]
- Don't jump straight to maximum ratings
- Complete autotune carefully
- Finish tuning by hand
- Prevents firmware bricks on first power-up

**Progressive Testing**:
1. Start at 50% of rated current
2. Verify operation at low power
3. Gradually increase limits
4. Monitor temperatures throughout
5. Log any unusual behavior

### Dual Controller Sync

**Simpler Than VESC**:
- No complex CAN configuration
- Parallel wiring naturally syncs controllers
- Both respond to same throttle input
- Less tuning required for balanced operation

## Applications

### Daily Commuting

**7212 Works Well For**:
- Single motor builds
- Moderate power (200A phase comfortable)
- 48V systems
- Riders who want simplicity

### High Performance

**KLS7230 Dual Setup**:[^ip001-kelly-7230]
- 350A discharge from 20S10P packs
- Oversized hubs
- Requires frame reinforcement
- External mounting needed

## Comparison with Other Controllers

### vs. VESC Controllers

**Kelly Advantages**:
- Simpler setup for dual controllers
- No CAN bus complexity
- Proven reliability
- Lower cost

**VESC Advantages**:
- More tuning options
- Better motor detection
- Active development
- More accessories available

### vs. Stock Controllers

**Kelly Advantages**:
- Higher power capability
- Better thermal management
- Replaceable if damaged

**Stock Advantages**:
- Integrated with scooter
- No wiring modifications
- Warranty coverage

## When to Choose Kelly

**Good Fit If**:
- You want simplicity over advanced features
- You're doing dual-motor build
- You can work around DC/DC limitations
- You prefer proven technology

**Consider Alternatives If**:
- You need extensive tuning options
- You want integrated accessory power
- You need CAN bus features
- You prefer active development community

## Essential Spares

- Antispark connectors (QS8/QS10 class)
- Sealed signal connectors (Higo/JST)
- Relays for accessory power
- Thermal paste
- Fuses appropriate for battery current

## Related Guides

- [Controller Setup](../guides/controller_setup.md)
- [Power Distribution](../guides/power_distribution.md)
- [Throttle & Brake Signals](../guides/throttle_brake_signals.md)

## References

[^1]: Source: knowledge/notes/input_part003_review.md, L36 to L37
[^2]: Source: knowledge/notes/input_part003_review.md, L83 to L84
[^3]: Source: knowledge/notes/input_part003_review.md, L38 to L38
[^4]: Source: data/vesc_help_group/text_slices/input_part003.txt, L8449 to L8454
[^5]: Source: data/vesc_help_group/text_slices/input_part003.txt, L337 to L345
[^6]: Source: knowledge/notes/input_part003_review.md, L36 to L36
[^7]: Source: knowledge/notes/input_part003_review.md, L36 to L38
[^ip001-kelly-7230]: Source: data/vesc_help_group/text_slices/input_part001.txt†L27399-L27415
