# Accessories & UX Planning Guide

## Overview

This guide covers displays, lighting, security, power management, and comfort accessories for electric scooters. It focuses on practical solutions that have been field-tested by the community, with specific attention to VESC builds that lack integrated displays.

## What You'll Learn

- Display and dashboard options
- Accessory power distribution
- Lighting upgrades and requirements
- Security and tracking solutions
- Power control ergonomics
- Winter comfort accessories

## Display & Dashboard Solutions

### The VESC Display Gap

**The Challenge**:[^dashboard_gap]
- VESC controllers have no built-in dashboard
- Riders must choose between mobile app or third-party displays
- Stock TFT screens often viewed as bulky and unattractive

### Mounting Solutions

**Practical Approaches**:[^tft_mounts]
1. **Zip-tie TFT to OEM dashboard**
   - Quick and reversible
   - Not the cleanest look
   - Works for testing

2. **Replace dashboard entirely with phone mount**
   - Use phone for VESC Tool app
   - Clean installation
   - Phone battery drain

3. **3D-printed housings**
   - Custom fit to your scooter
   - Can integrate with auxiliary handlebars
   - Requires design and printing

### Display Comparison

**Options Being Tested**:[^display_comparison]
- **Davega X** - Popular VESC display
- **Eye3-compatible ESP32 displays** - Versatile platform
- **Flipsky TFT modules** - VESC-specific

**Stealth Installations**: Some builders reuse factory casings to stay compliant with local regulations while upgrading internals.

### Smart Dashboard Features

**Community Wishlist**:[^smart_dash_roadmap]
- ESP32 logic for mode toggles
- Legal-speed presets (button combinations)
- CAN communication (survives high-current noise better than UART)
- Profile switching
- Data logging

### Minimotors EY3 Displays

**Compatibility Requirements**:[^ey3_bridge]
- Requires VSETT Lisp bridge
- Works with Flipsky FT85BD
- Works with Ubox Lite clones

> **⚠️ Critical**: The bridge's throttle-out lead must be connected. Leaving it disconnected has bricked displays. Treat passthrough as mandatory wiring.

### Budget Option: USB GPS Speedometer

**Simple Solution**:[^usb_gps]
- $10 USB GPS speedometer
- Boots in under 1 minute
- Powered from 5V feed
- Good when TFT won't fit cockpit
- Basic but functional

## Accessory Power Distribution

### High-Voltage Buck Converters

**Power Supply Strategy**:[^hv_buck]
- Use wide-input buck modules (9-120V)
- Step down to 5V at 2-3A
- Powers lighting and telemetry

**Critical Testing Required**:
- Bench-test every unit before installation
- Mislabeled boards have overvolted 6V lamps
- Verify standby draw (~1mA advertised)
- Confirm actual vs. claimed specs

> **📝 Important**: VESC ADC daughterboard is an analog interface, NOT a substitute step-down supply. Don't use it for power distribution.

### Dense LED Strip Loads

**Power Requirements**:[^led-strip-load]
- Dense strips can pull ~10A at 5V
- Example: ~100 LED/m strips
- Plan dedicated DC/DC converters
- Use enable pins for control
- Or pivot to electroluminescent tape

**Why This Matters**: Overloading accessory rails can cause brownouts, resets, or damage to controllers.

## Lighting Upgrades

### Headlight Options

**High-Output Solutions**:[^lighting_tests]
- 3,000-9,000 lumen USB-C headlights
- Doubles as power bank
- Bright enough for night riding
- Good for commuters

**Budget Alternative**:
- 5×P90 AliExpress headlights
- Adequate brightness
- Lower cost
- Acceptable quality

### Battery Pack Quality

**MagicShine-Style Lights**:[^magicshine_repack]
- Marketing claims often inflated
- "10,000mAh" packs may be weak
- **Solution**: Repack with quality 18650/21700 cells
- Much better runtime and reliability

### Tail Lights & Turn Signals

**Xiaomi Rear Light Rail**:[^denis-tail-rail]
- Only delivers ~3-5V
- Tight current limiting
- Bright LED strips need separate power
- Use 5V/12V buck or relay off controller
- Limited to careful lens alignment if using stock rail

**Turn Signal Options**:[^emark_signals]
- Compact E-marked motorcycle signals from AliExpress
- Pair with dedicated DC-DC converters
- Discreet and road-legal
- Good for compliance

**AYO's Parts List**:[^ayo_lighting]
- Low-cost motorcycle brake lights
- Waterproof COB strips
- Inline three-button dimmers
- Drop straight onto 12V rails or reducers

> **💡 Pro Tip**: Combine multiple small lights rather than one big one for redundancy and better visibility angles.

## Media Capture & Logging

### Action Cameras

**Insta360 vs. GoPro**:[^insta360]
- **Insta360**: Native GPS overlays still supported
- **GoPro Hero 12**: Dropped GPS overlay feature
- Choose Insta360 for on-screen speed data
- Important for documentation runs

### Custom Dashboards

**Arduino-Based Solutions**:[^vesc-arduino-dash]
- Koxx demonstrated Xiaomi with custom VESC firmware
- Auxiliary microcontroller handles display
- Proves open hardware can replace proprietary displays
- Fills Rita telemetry gaps

## Security & Tracking

### Tracker/Immobilizer Modules

**Denis's Prototype**:[^denis-tracker-proto]
- Plug-and-play design
- Onboard 5V supply
- Fingerprint reader
- Alarm speaker
- Can sound alarm or cut power when moved unauthorized

### Power Requirements

**Standalone Trackers**:[^denis-tracker-ldo]
- Use low-dropout regulator (e.g., AMS1117-3.3)
- Feed directly from main battery
- Xiaomi controllers lack standby 5V rails
- Must be battery-powered for 24/7 operation

### NFC-Based Locks

**Community Interest**:[^nfc-lock]
- Spintend owners hunting NFC locks
- Eliminate physical keys on premium builds
- Waiting for vetted hardware options
- Document solutions as they emerge

## Power Control Ergonomics

### Sleep Mode & Switches

**Implementation Challenges**:[^sleep_wiring]
- Platform supports sleep mode
- Physical power switch requires custom wiring
- Many builds use anti-spark switches as manual cut-offs

### Premium Switchgear

**Tusk Compact Control Switch**:[^tusk_switch]
- Survives vibration better than generic pods
- Handles lighting and horn duties
- Motorcycle-grade quality
- Worth the upgrade for reliability

## Winter Comfort

### Helmet Selection

**Cold Weather Priorities**:[^winter-helmets]
- Full-face helmets are essential
- Winter balaclavas layer underneath
- Budget at least $120 for quality lid
- Keep helmet on indoors (theft deterrent + warmth)
- Critical for -15°C conditions

### Heated Accessories

**Heated Grips**:[^heated-grips]
- Power directly from scooter pack
- Convenient for long rides
- Always available when riding
- No charging routine needed

**Heated Gloves**:
- Add off-scooter utility
- Require charging routines
- Extra wiring bulk
- More versatile but less convenient

**Recommendation**: Heated grips for convenience on long commutes, heated gloves if you need hand warmth off the scooter too.

## Accessory Planning Checklist

### Before Purchasing

- [ ] Measure available space for displays/lights
- [ ] Calculate total accessory power draw
- [ ] Verify controller has adequate aux power
- [ ] Check compatibility with your controller
- [ ] Read community reviews

### Power Budget

1. **List all accessories** with current draw
2. **Sum total current** required
3. **Choose appropriate buck converter** (add 25% margin)
4. **Verify controller aux rail** can handle it
5. **Plan separate power** if needed

### Installation

- [ ] Bench-test all electronics before installation
- [ ] Use proper connectors and strain relief
- [ ] Route wiring away from heat sources
- [ ] Waterproof all connections
- [ ] Label all wires
- [ ] Document your setup with photos

## Troubleshooting Common Issues

### Display Won't Power On

1. Check buck converter output voltage
2. Verify power connections
3. Test with multimeter
4. Try different power source
5. Check for shorts

### Lights Flickering

- Insufficient current capacity
- Poor connections
- Buck converter unstable
- Ground loop issues
- Try dedicated power supply

### Bluetooth Connection Issues

- VESC Tool version incompatibility
- Interference from other accessories
- Distance/obstacles
- Try desktop connection first
- Update firmware if needed

## Related Guides

- [Controller Setup](controller_setup.md)
- [Power Distribution](power_distribution.md)
- [VESC ADC Accessory Integration](vesc-adc-accessory-integration.md)
- [SmartDisplay Integration Guide](smartdisplay-integration-guide.md)

## References

[^dashboard_gap]: Source: knowledge/notes/input_part000_review.md, line 38
[^tft_mounts]: Source: knowledge/notes/input_part000_review.md, line 46
[^display_comparison]: Source: knowledge/notes/input_part000_review.md, line 57
[^smart_dash_roadmap]: Source: knowledge/notes/input_part000_review.md, line 59
[^lighting_tests]: Source: knowledge/notes/input_part000_review.md, line 47
[^sleep_wiring]: Source: knowledge/notes/input_part000_review.md, line 45
[^winter-helmets]: Source: knowledge/notes/input_part006_review.md†L91-L91
[^ey3_bridge]: Source: knowledge/notes/input_part009_review.md†L438-L439
[^usb_gps]: Source: knowledge/notes/input_part009_review.md†L441-L441
[^hv_buck]: Source: knowledge/notes/input_part009_review.md†L440-L440
[^tusk_switch]: Source: knowledge/notes/input_part008_review.md†L301-L302
[^magicshine_repack]: Source: knowledge/notes/input_part010_review.md†L418-L419
[^emark_signals]: Source: knowledge/notes/input_part010_review.md†L585-L585
[^ayo_lighting]: Source: knowledge/notes/input_part010_review.md†L587-L590
[^insta360]: Source: knowledge/notes/input_part010_review.md†L629-L630
[^nfc-lock]: Source: knowledge/notes/input_part013_review.md†L723-L723
[^denis-tail-rail]: Source: knowledge/notes/denis_all_part02_review.md†L704-L704
[^denis-tracker-proto]: Source: knowledge/notes/denis_all_part02_review.md†L932-L932
[^denis-tracker-ldo]: Source: knowledge/notes/denis_all_part02_review.md†L934-L934
[^vesc-arduino-dash]: Source: knowledge/notes/denis_all_part02_review.md†L1043-L1043
[^led-strip-load]: Source: knowledge/notes/denis_all_part02_review.md†L1044-L1044
[^heated-grips]: Source: knowledge/notes/denis_all_part02_review.md†L1048-L1048
