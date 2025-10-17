# Power Distribution & Wiring Guide

## Overview

Proper power distribution is critical for safety, performance, and reliability in electric scooters. This guide covers cable sizing, connector selection, wiring hygiene, signal filtering, and best practices for managing high-current electrical systems.

## What You'll Learn

- Cable gauge selection for different current levels
- Connector types and their current ratings
- EMI management and signal routing
- Parallel pack wiring discipline
- Lighting and accessory power distribution
- Safety considerations and common failures

## ⚡ Critical Safety Principles

🔴 **Undersized wiring causes fires**. Always size for peak current + safety margin.

## 📋 Quick Reference: Wire Gauge by Current

| Current Range | Minimum AWG | Recommended AWG | Connector Type |
|--------------|-------------|-----------------|----------------|
| 0-30A | 14 AWG | 12 AWG | XT60 |
| 30-60A | 12 AWG | 10 AWG | XT90, AS150 |
| 60-100A | 10 AWG | 8 AWG | QS8, AS150 |
| 100-200A | 8 AWG | 6 AWG | QS8, Anderson |
| 200-350A | 6 AWG | 4 AWG | QS10, Anderson |

💡 **Pro Tip**: Go one size larger than minimum for heat management and longevity.

## 📋 Connector Current Ratings (Real-World)

| Connector | Rated | Conservative Real-World | Notes |
|-----------|-------|------------------------|-------|
| XT30 | 30A | 20A continuous | Commuter use only |
| XT60 | 60A | 40A continuous | Mid-power builds |
| XT90 | 90A | 60A continuous | Common for battery mains |
| AS150 | 150A | 100A continuous | Anti-spark available |
| QS8 | 200A+ | 150A continuous | Heavy-duty, good contact |

## 🔧 Related Guides

- [Battery Current Tuning](battery_current_tuning.md) - Determining current requirements
- [VESC ADC Accessory Integration](vesc-adc-accessory-integration.md) - Low-current signal wiring
- [Smart BMS Integration](smart-bms-integration-handbook.md) - BMS to controller wiring

## Cable Management Fundamentals

### Voltage Drop Issues

**Long Cable Runs**:[^long_leads]
- 16 AWG leads with XT30 connectors caused ~0.5V per-cell drops at 40A
- Occurred on 12S7P pack
- **Solutions**:
  - Shorten cable runs
  - Upgrade to XT60/XT90 connectors
  - Use 10-12 AWG wiring
  - Markedly improves voltage sag

### EMI Reduction

**Cable Routing Strategy**:[^emi_routing]
- Route high-current cables on one side of deck
- Route signal/brake harnesses on opposite side
- Reduces electromagnetic interference
- Especially important in tight Vsett installations
- Upsize connectors to reduce resistance

### Securing Cables

**Metal Zip Ties**:[^metal_zipties]
- Stainless "metal zip ties" stay flexible in cold
- Secure battery looms without hose clamp bulk
- Plastic ties crack in winter storage
- Good for garage-stored scooters

> **💡 Pro Tip**: Plan cable routing before final assembly. Separating power and signal cables prevents many EMI-related issues.

## Cable Gauge Selection

### Current Capacity Guidelines

**AWG vs Current Ratings**:

| Gauge | Continuous Current | Burst Current | Typical Use |
|-------|-------------------|---------------|-------------|
| 16 AWG | ~15A | ~25A | Low-power accessories |
| 12 AWG | ~35A | ~55A | Medium power, short runs |
| 10 AWG | ~55A | ~85A | 60A continuous applications |
| 8 AWG | ~75A | ~115A | High power, dual feeds |
| 6 AWG | ~100A | ~150A | Very high current mains |

> **⚠️ Warning**: These ratings assume good cooling and short runs. Enclosed cables or long runs require derating.

### Specific Applications

**90A Battery Packs**:[^2]
- Default to AWG10 main leads
- Or dual AWG12 runs
- Consider 3-3.5mm solid copper between pack negative and BMS
- 40% more ampacity than single run
- Keep runs short

**100A Continuous Phase**:[^3]
- 12 AWG phase leads comfortable at 100A
- Light riders logged 150A bursts successfully
- Post-ride temps near 45°C
- **Requirements**:
  - Short duty cycles
  - Forced cooling if exceeding published ampacity

**60A Continuous Applications**:[^4]
- 10 AWG practical minimum
- AS120 connectors run cooler than AS150
- Contact geometry matters
- Size wiring before chasing 70A+ limits

### Heavy Current Applications

**90-150A Phase Runs**:[^5]
- Shift toward XT150 bullets or AS150U anti-spark
- ~0.20 mΩ resistance
- Spare signal pins for accessories
- Controllers can feed trackers/smart BMS
- Minimal voltage drop

**120-180A Batteries**:[^ip001-xt90-headroom]
- Demand dual XT60s
- Or XT150/AS150 bullets
- Or QS8 pairs
- Plus 6-8 AWG leads
- Keeps contact temperatures safe

**190A-Class Scooters**:[^ip001-awg]
- Dual 7 AWG battery leads
- Or single 6 AWG
- Wire gauge follows current, not voltage
- Undersized looms make shrink brittle at 135-145°C

> **📝 Definition**: Ampacity - The maximum current a conductor can carry continuously without exceeding its temperature rating.

## Connector Selection

### Understanding Ratings

**XT90S Limitations**:[^ip001-xt90-headroom]
- Single XT90S: ~50A continuous
- ~65A burst ceiling
- Paolo incinerated XT90S with >2,000µF cap banks at 16S+
- **Lesson**: Step up to QS8/AS150 with better precharge

**XT90 Real-World Limits**:[^qs8_hxt]
- Demoted to ~45A continuous service
- Good for light builds
- Repeated hot-plugs cook in-line resistors
- High-power crews use AS150 or QS8/QS10

### Connector Recommendations by Current

**Light Duty (<50A)**:
- XT30: Adequate for accessories
- XT60: Good for moderate power
- XT90S: Anti-spark option

**Medium Duty (50-100A)**:
- XT90: Solid choice
- AS120: Better thermal performance
- MR60: Phase connectors

**Heavy Duty (100-180A)**:
- Dual XT60s
- XT150: Clean and effective
- AS150: Anti-spark capable
- QS8: Proven at high current

**Extreme Duty (180A+)**:
- QS8 pairs
- XT150/AS150 bullets
- Direct soldered (inspected regularly)
- 6-8 AWG minimum

### Special Purpose Connectors

**Higo L1019 Retrofit**:[^ip001-l1019]
- 4mm² (~11 AWG) phases
- Halls and temp lead in one jacket
- Fits VSETT axles
- Map color swap before installing
- Keep on 50mm-class hubs (stays cool)

**L1019 Limitations**:[^ip001-l1019-limit]
- Avoid 60-70mm motors without rework
- Factory "blob" solder inadequate
- Desolder and upsize for high current

**MT60 Phase Connectors**:[^xt150-guidance]
- Bundle three XT60-style bullets
- Tidy triple-phase hookups
- Jason specs XT150 on phases, XT90 on battery

**MT60 Failures**:[^ip001-mt60-failure]
- Melted at ~200A, shorted Kelly controller
- Retire drone-class connectors above 72V
- Step up to XT150/AS150 or lugs at 150-200A

### AS150U Anti-Spark

**For Dual VESC >150A Phase**:[^7]
- Standardizing on AS150U anti-spark pairs
- 8 AWG tails
- XT150/AS150 mains for 500A phase bursts
- XT90s treated as temporary jumpers

## Signal Filtering & Conditioning

### Throttle Signal Filtering

**Capacitor Selection**:[^ceramic_scavenge]
- Scavenge ~100nF ceramic capacitors from dead electronics
- Don't use oversized drone caps
- **Critical**: Discharge and meter salvaged parts first
- Bridge signal-to-ground with known capacitance

### Parallel Pack Signal Discipline

**When Paralleling Packs**:[^parallel_rules]
1. **Tie all grounds together**
2. **Match series counts and capacities**
3. **Pre-balance voltages**
4. **Watch for cross-charging**
5. **Individual BMS protection doesn't prevent pack stress**

### Rita-Style Y Cables

**Proper Configuration**:[^denis-y-cable]
- Two female battery legs
- Single male controller lead
- **Critical**: Match voltages before connection
- Poorly soldered joints have shorted externals
- Can scar decks

> **⚠️ Safety Warning**: Voltage mismatch between parallel packs can cause dangerous cross-charging currents. Always pre-balance.

## Phase Wire Management

### Clearance Issues

**Oversized Phase Wires**:[^phase_wire_clearance]
- Can chafe against axle exits
- Stick with 11 AWG Higo looms
- Proven to survive 80/225A tunes
- No insulation damage

### Kelly 7230 Special Case

**Cramped Harness**:[^kelly_bullet_debate]
- Doubled 4 AWG phase leads
- Crammed into 8mm bullets
- Seasoned racers rewire with:
  - Slimmer conductors
  - Or 10mm hardware
- Don't force oversized plugs

### Wolf-Class Hubs

**Stock Configuration**:[^wolf-phase]
- Ship with ~4mm (AWG 11-12) phase leads
- Tolerate ~130A once properly cooled
- Measure copper cross-section first
- Check frame clearance before upgrades

### Amass Bullet Fitment

**Quality Matters**:[^amass-fit]
- Genuine Amass 8mm bullets superior
- Clamp dual 10 AWG phases tighter
- Generic 8mm copies looser
- May need hand-fit or shaving for mixed brands
- Budget space for 10mm hardware

## Accessory Power Distribution

### 48V Lighting Systems

**Power Requirements**:[^ip001-lighting]
- Compact 25W/3,500lm headlights common
- Parallel high/low beams possible
- **Critical Considerations**:
  - 3A step-downs need heatsinking
  - Nucular controllers: 12V/3A (~6A dual)
  - Prefer lamps with integrated buck converters
  - Avoid voltage drop on long runs

### Voltmeter Integration

**Limitations**:[^ip001-voltmeter]
- Popular mini voltmeters cap at 35V
- Expect 12V feed
- 72-100V builds need dedicated step-downs
- Or repurpose throttle displays
- Control rails only provide ~3.3V

### Horns

**Current Budget**:[^denis-horn]
- Budget ~1-1.5A for 12V horns
- Fuse the supply
- Pair loud horn with polite bell
- Bell for pedestrian zones

### Hidden Trackers

**Power Requirements**:[^denis-tracker-ldo]
- Need own low-dropout regulator
- Example: AMS1117-3.3
- Tie directly to main battery
- Xiaomi controllers lack standby 5V rail

### Quick Reference Sheet

**Publish 48V Lighting Guide**:[^lighting_quickref]
- Fuse sizing
- Gauge picks
- Load calculations
- Prevents oversizing harnesses
- Reminds about inline protection

## Charging Infrastructure

### 13S Limitations

**Xiaomi RCA Type X**:[^charge-port-13s]
- Overheats above ~3A on 13S builds
- OEM wiring inadequate
- **Solutions**:
  - Request custom connectors from charger vendors
  - Convert to GX12-class ports

## Anti-Spark Systems

### XT150 with JK BMS

**Smart Integration**:[^ip001-xt150-routing]
- JK smart BMS antispark stages enable XT150 hot-plugging
- AS150 split shells simplify routing
- Good for cramped VSETT decks

### QS8 High-Current Applications

**When Current Hits ~350A**:[^qs8_awg]
- Step up to 6 AWG for single QS8
- Dual-QS8 layouts: Paired 8 AWG acceptable
- **Warning**: Don't trust "100A" cheap silicone marketing
- Budget thicker copper before finalizing lengths

## Soldering Best Practices

### Mechanical Strength

**Solder as Filler, Not Conductor**:[^6]
- Twist or fold AWG12 leads
- Double contact area before wetting
- Silver-bearing solder conducts 2-5x worse than copper
- Mechanical connection carries current

## Service Safety

### After High-Current Rides

**Phase Connector "Welding"**:[^phase-safety]
1. **Kill pack power**
2. **Discharge controller capacitors**
3. **Expect sparks on reconnection**
4. **Protect BLE boards and ESCs**

### Dual Ubox Stacks

**Capacitor Energy Storage**:
- Briefly wake from stored capacitor energy
- Even with pack unplugged
- Watch status LEDs go dark
- Depower accessories before unplugging

## Troubleshooting Guide

### Voltage Sag Issues

**Symptoms**:
- Significant voltage drop under load
- Reduced performance
- Early battery cutoff

**Causes & Solutions**:
1. Long cable runs → Shorten or upsize
2. Undersized wire → Increase gauge
3. Poor connectors → Upgrade to higher current rating
4. High resistance joints → Reflow solder, ensure mechanical connection

### Overheating Connectors

**Symptoms**:
- Warm/hot connectors after riding
- Discolored housings
- Melted plastic

**Causes & Solutions**:
1. Undersized for current → Upsize connector
2. Poor contact → Clean and reseat
3. Damaged pins → Replace connector
4. Multiple joints in series → Minimize connections

### EMI/Signal Issues

**Symptoms**:
- Throttle glitches
- Display interference
- Brake signal dropouts

**Causes & Solutions**:
1. Poor cable routing → Separate power/signal
2. Missing grounds → Ensure common ground
3. Unshielded cables → Use shielded for sensitive signals
4. Missing filtering → Add appropriate capacitors

## Connector Upgrade Checklist

### When Upgrading Connectors

- [ ] Calculate actual current requirements
- [ ] Select connectors rated for 150-200% of nominal current
- [ ] Choose appropriate wire gauge for connector
- [ ] Plan cable routing before cutting
- [ ] Test fit connectors before soldering
- [ ] Use proper crimping tools
- [ ] Apply heat shrink for strain relief
- [ ] Label all connections
- [ ] Test continuity before powering
- [ ] Monitor temperatures on first ride

## Related Guides

- [Motor Controller Tuning](motor_controller_tuning.md)
- [Battery Pack Design](battery_pack_design.md)
- [Controller Setup](controller_setup.md)
- [Accessories](accessories.md)

## References

[^long_leads]: Source: knowledge/notes/input_part000_review.md, line 84
[^emi_routing]: Source: knowledge/notes/input_part000_review.md, line 85
[^metal_zipties]: Source: knowledge/notes/input_part010_review.md†L672-L673
[^ceramic_scavenge]: Source: knowledge/notes/input_part000_review.md, line 126
[^parallel_rules]: Source: knowledge/notes/input_part000_review.md, line 127
[^antispark_tradeoff]: Source: knowledge/notes/input_part003_review.md†L511-L515
[^1]: Source: knowledge/notes/input_part000_review.md†L325-L325
[^2]: Source: knowledge/notes/input_part000_review.md†L373-L373
[^3]: Source: knowledge/notes/input_part000_review.md†L468-L472
[^4]: Source: knowledge/notes/input_part000_review.md†L472-L474
[^5]: Source: knowledge/notes/input_part000_review.md†L546-L548
[^xt90_failure]: Source: knowledge/notes/input_part001_review.md†L595-L596
[^ip001-l1019]: Source: knowledge/notes/input_part001_review.md†L653-L654
[^ip001-l1019-limit]: Source: knowledge/notes/input_part001_review.md†L653-L655
[^6]: Source: knowledge/notes/input_part000_review.md†L548-L549
[^7]: Source: knowledge/notes/input_part000_review.md†L618-L627
[^ip001-xt90-headroom]: Source: data/vesc_help_group/text_slices/input_part001.txt†L20085-L20177
[^ip001-xt150-routing]: Source: data/vesc_help_group/text_slices/input_part001.txt†L20131-L20177
[^ip001-awg]: Source: data/vesc_help_group/text_slices/input_part001.txt†L18170-L18340
[^ip001-mt60-failure]: Source: data/vesc_help_group/text_slices/input_part001.txt†L17850-L17910
[^ip001-lighting]: Source: data/vesc_help_group/text_slices/input_part001.txt†L24157-L24216
[^ip001-voltmeter]: Source: data/vesc_help_group/text_slices/input_part001.txt†L24411-L24421
[^qs8_awg]: Source: data/vesc_help_group/text_slices/input_part005.txt†L24298-L24309
[^kelly_bullet_debate]: Source: knowledge/notes/input_part008_review.md†L488-L490
[^xt150-guidance]: Source: knowledge/notes/input_part010_review.md†L481-L482
[^wolf-phase]: Source: knowledge/notes/input_part010_review.md†L511-L512
[^amass-fit]: Source: knowledge/notes/input_part010_review.md†L531-L532,†L704-L704
[^lighting_quickref]: Source: knowledge/notes/input_part000_review.md†L809-L809
[^qs8_hxt]: Source: knowledge/notes/input_part002_review.md†L523-L527
[^xt150_vsett9]: Source: knowledge/notes/input_part002_review.md†L525-L526
[^ubox_battery_limits]: Source: data/vesc_help_group/text_slices/input_part002.txt†L24622-L24692
[^phase_wire_clearance]: Source: data/vesc_help_group/text_slices/input_part002.txt†L24711-L24715
[^denis-y-cable]: Source: knowledge/notes/denis_all_part02_review.md†L769-L769
[^denis-horn]: Source: knowledge/notes/denis_all_part02_review.md†L645-L645
[^denis-tracker-ldo]: Source: knowledge/notes/denis_all_part02_review.md†L934-L934
[^connector-upgrade]: Source: knowledge/notes/denis_all_part02_review.md†L1018-L1020
[^dual-feed]: Source: knowledge/notes/denis_all_part02_review.md†L1073-L1073
[^charge-port-13s]: Source: knowledge/notes/denis_all_part02_review.md†L1063-L1063
[^phase-safety]: Source: knowledge/notes/denis_all_part02_review.md†L1091-L1091
