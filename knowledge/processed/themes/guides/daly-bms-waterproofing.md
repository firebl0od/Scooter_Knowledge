# Daly Smart BMS Moisture Recovery & Waterproofing Guide

## Overview

This guide covers diagnosis, recovery, and waterproofing procedures for Daly smart BMS units that have experienced moisture damage. Waterlogged Daly boards are a common failure mode that manifests as ghost voltage readings and unexpected shutoffs. Following these procedures can restore functionality and prevent future failures.

## What You'll Learn

- How to identify moisture damage symptoms
- Emergency dry-out procedures
- Proper waterproofing techniques
- Post-recovery validation steps
- Preventive maintenance practices

## 📋 Quick Diagnosis: Moisture vs Other Failures

| Symptom | Moisture Damage | Other Cause | Quick Test |
|---------|----------------|-------------|------------|
| Ghost 5V on cells | ✅ Likely | ❌ Unlikely | Dry out board, retest |
| Random shutoffs | ✅ Possible | ✅ Possible | Check balance connector moisture |
| Voltage mismatch (BMS vs dash) | ✅ Likely | ⚠️ Possible | Inspect for water in connectors |
| MOSFETs won't enable | ⚠️ Possible | ✅ Likely | Check for corrosion on traces |
| Blue smoke | ❌ No | ✅ Yes | BMS is toast, replace |

## ⚠️ Critical Safety Warnings

🔴 **Disconnect Pack**: Always disconnect battery before working on wet BMS
🔴 **No Forced Operation**: Never bypass protections on moisture-damaged boards
🔴 **Corrosion Risk**: Water + voltage = permanent trace damage—dry immediately
🔴 **Retest Everything**: Verify cell voltages with multimeter after recovery

## 💡 Pro Tips

- **Act fast**: Dry within 24 hours to prevent corrosion
- **Use rice/silica**: Pack wet BMS with desiccant in sealed container
- **Heat carefully**: Warm air only—no direct heat gun on components
- **Test before sealing**: Run pack through charge/discharge cycles before final waterproofing

## 🔧 Related Guides

- [Smart BMS Integration Handbook](llt-jbd-smart-bms-integration-handbook.md) - Alternative BMS options
- [Scooter Waterproofing & Security](scooter_waterproofing_and_security.md) - Preventive measures
- [Battery Pack Design](battery_pack_design.md) - BMS selection criteria

## Understanding Moisture Damage

### Common Symptoms

**Ghost Voltage Readings**:[^1]
- Random 5V readings on cell groups
- Happens even when pack voltages are properly balanced
- Indicates moisture in the sensing harness or board

**Voltage Reporting Errors**:[^2]
- BMS reports 3.1V per cell
- Scooter dash shows near-nominal voltage
- Discrepancy indicates moisture in sensing circuit

**Unexpected Shutoffs**:[^4]
- BMS refuses to discharge or charge
- MOSFETs latch off without clear cause
- Requires software reset to restore function

> **⚠️ Warning**: Do not attempt to force the BMS to operate while moisture is present. This can cause permanent damage to the board.

### Why Moisture Causes These Issues

Water creates conductive paths on the PCB that:
- Short cell-sense

 inputs causing false readings
- Trigger over/under-voltage protection inappropriately
- Corrode connections leading to intermittent failures
- Cause the MCU to latch off MOSFETs as a safety measure

## Emergency Dry-Out Procedure

### Step 1: Safe De-Energization

**Before Opening the Pack**:[^1]
1. Disconnect pack from all loads
2. Isolate both charge and discharge leads
3. Document cell voltages with multimeter
4. Take photos of current state for reference

> **⚠️ Safety**: Work in a well-ventilated area away from flammable materials.

### Step 2: Disassembly

**Accessing the BMS**:[^1]
1. Remove outer heat-shrink tubing carefully
2. Document insulation layers as you remove them
3. Note wire routing for proper reassembly
4. Access the Daly board and harness entry points

### Step 3: Moisture Purging

**Drying Process**:[^1]
1. **Apply controlled hot air**
   - Use hair dryer on low-medium heat
   - Focus on balance leads and PCB surfaces
   - Keep moving to avoid hot spots
   - 5-10 minutes per drying session

2. **Isopropyl Alcohol Rinse**
   - Apply 90%+ IPA to displace water
   - Works on mostly potted enclosures
   - Allows better penetration than air alone
   - Let evaporate completely

3. **Multiple Drying Cycles**
   - Repeat hot air and IPA process 2-3 times
   - Check for visible moisture between cycles

### Step 4: Extended Rest Period

**Overnight Drying**:[^3]
- Leave assembly in warm, dry location
- Use gentle heat if available (not hot)
- Allow minimum 12 hours for complete drying
- Check for condensation before proceeding

> **💡 Pro Tip**: Place assembly in front of fan with gentle airflow to speed evaporation without excessive heat.

## Shutdown Trip & Back-EMF Recovery

### Diagnostic Checklist

Before re-arming a tripped Daly BMS:[^daly_shutdown_sop]
- [ ] Inspect for any lingering moisture
- [ ] Clear solder balls around controller bay
- [ ] Document fault codes in app
- [ ] Verify cell voltages are balanced
- [ ] Check physical connections are secure

**Why This Matters**: A companion VESC can trigger repeated failures if the root cause isn't addressed.

## Waterproofing Stack (Rebuild)

### Layer-by-Layer Protection

**1. Cell-Level Insulation**:[^2]
- Wrap every series group in fish paper
- Provides electrical insulation
- Slight moisture barrier

**2. Tape Wrapping**:[^2]
- Apply minimum 5 alternating wraps of waterproof tape
- Overlap each wrap by 50%
- Cover entire pack body
- Focus on seams and edges

**3. Outer Shrink Tubing**:[^2]
- Apply fresh heat-shrink over tape layers
- Ensure complete coverage
- Heat evenly to avoid gaps

**4. Silicone Sealing**:[^2]
- Seal every seam
- Seal all wire exits
- Seal fastener penetrations
- Blocks capillary water ingress

**5. Desiccant Addition**:[^2]
- Add silica gel packs inside enclosure
- Absorbs residual humidity
- Replace every 6-12 months

> **📝 Definition**: Capillary action - Water "climbing" into small gaps through surface tension. Silicone blocks these tiny pathways.

## Post-Recovery Validation

### Software Re-Enable

**Using Daly Bluetooth App**:[^4]
- Default password: 123456
- Navigate to MOSFET control
- Re-enable charge MOSFET
- Re-enable discharge MOSFET
- Verify both latch on without fault codes

### Electrical Testing

**Voltage Monitoring**:[^1]
1. Check all cell voltages in app
2. Monitor for several hours
3. Look for stable readings
4. Watch for reappearing 5V anomalies
5. All cells should stay within 0.05V of each other

### Functional Testing

**Gentle Cycling**:[^3]
1. Perform light charge cycle (2-4A)
2. Monitor temperatures throughout
3. Discharge at moderate rate (5-10A)
4. Watch for unexpected shutoffs
5. Verify app shows correct voltages

**Only After Success**:
- Reseal permanently with final layers
- Full documentation of repair
- Return to normal operation

## Known Limitations

### Balancing Performance

**Daly Smart BMS Balancing**:[^1]
- Only balances at ~30mA
- Struggles during 25A charging
- Slow to correct imbalances

**Recommended Solution**:
- Pair with monitored 4A active balancer
- External balancer handles bulk work
- Daly maintains monitoring and protection

> **⚠️ Caution**: Experiments with reverse-current balancing can fry helper boards. Stick to proven configurations.

### Warranty and Replacement

**If BMS Stops Balancing**:[^denis-daly-balance]
- If failure occurs within first week: Replace unit
- Rita typically won't cover balance failures
- Double-check balance-lead pinout on new unit
- Document installation for future reference

## Preventive Maintenance

### Regular Inspections

**Schedule**:[^2]
- Check sealant integrity monthly
- Inspect after wet rides immediately
- Look for shrink tube damage
- Verify wire boots are sealed

**What to Check**:
- Silicone seal condition
- Heat-shrink integrity
- Wire exit points
- Fastener penetrations
- Desiccant pack condition

### Maintenance Supplies

**Keep On Hand**:[^2]
- Spare desiccant packs
- Silicone sealant
- Waterproof tape
- Heat-shrink tubing
- Isopropyl alcohol (90%+)

### Documentation

**Record Everything**:[^1]
- Take photos before and after work
- Log all moisture events
- Document cell voltages
- Save fault codes from app
- Helps with warranty claims and future diagnostics

## Troubleshooting Guide

### BMS Won't Re-Enable After Drying

**Possible Causes**:
1. Moisture still present - dry longer
2. Damaged balance lead - inspect connections
3. Failed MOSFET driver - may need replacement
4. App connection issue - try different device

### Ghost Readings Persist

**If 5V readings continue**:[^1]
- BMS may be permanently damaged
- Check for visible corrosion on PCB
- Verify all connections are dry
- Consider replacement if cleaning doesn't help

### Rapid Re-Failure

**If moisture returns quickly**:
- Waterproofing insufficient - add more layers
- Puncture in heat-shrink - inspect carefully
- Poor wire sealing - reseal all exits
- Riding in deep water - avoid or improve protection

## Related Guides

- [Smart BMS Integration Handbook](smart-bms-integration-handbook.md)
- [Battery Pack Design](battery_pack_design.md)
- [LLT-JBD Smart BMS Integration](llt-jbd-smart-bms-integration-handbook.md)

## References

[^1]: Source: knowledge/notes/input_part004_review.md†L290-L290
[^2]: Source: knowledge/notes/input_part000_review.md†L153-L154
[^3]: Source: knowledge/notes/input_part000_review.md†L155-L155
[^4]: Source: knowledge/notes/input_part000_review.md†L156-L156
[^denis-daly-balance]: Source: knowledge/notes/denis_all_part02_review.md†L740-L740
[^daly_shutdown_sop]: Source: knowledge/notes/input_part000_review.md†L808-L808
