# 📌 Ultimate In-Depth VESC Parameter Guide
Use GitHub’s in-page search or the table of contents below to jump to the parameter you need.

Structure for each parameter:
1. **What It Does** – Short definition.
2. **Deeper Insights** – Advanced real-world context.
3. **How / When to Modify** – Practical tuning guidelines.
4. **Potential Side Effects** – Common pitfalls or issues.

## Table of Contents
- [1. PWM & Commutation](#1-pwm--commutation)
- [2. Current & Battery Limits](#2-current--battery-limits)
- [3. RPM & Duty Limits](#3-rpm--duty-limits)
- [4. Thermal Parameters](#4-thermal-parameters)
- [5. BLDC Sensorless (BLDC-Mode Specific)](#5-bldc-sensorless-bldc-mode-specific)
- [6. FOC Parameters](#6-foc-parameters)
- [7. Speed & Position PID](#7-speed--position-pid)
- [8. Current Control (BLDC/DC)](#8-current-control-bldcdc)
- [9. Encoders & Sensor Ports](#9-encoders--sensor-ports)
- [10. BMS Settings](#10-bms-settings)

---

## 1. PWM & COMMUTATION


### 1.1 PWM Mode
**Parameter Key:** `pwm_mode`


**What It Does**
- The PWM mode to use for BLDC motors. Synchronous is the most tested and recommended mode. 
- Possible Values: Nonsynchronous HISW, Synchronous, Bipolar

**Deeper Insights**
- Synchronous ensures both high-side and low-side transistors are used in each switching cycle, often giving better efficiency and lower noise. 
- Nonsynchronous HISW is older: only high-side transistors do PWM, the low-side is fully on or off. 
- Bipolar is typically for specialized or academic contexts.

**How / When to Modify**
- Most modern VESC hardware is stable with Synchronous. 
- Only choose Nonsynchronous or Bipolar if your hardware or documentation explicitly recommends it.

**Potential Side Effects**
- Switching Synchronous → Nonsynchronous can raise MOSFET temperatures or trigger partial conduction issues at certain duty cycles. 
- Bipolar is untested in many mainstream VESC contexts, so proceed with caution.


### 1.2 Commutation Mode
**Parameter Key:** `comm_mode`


**What It Does**
- Used in BLDC sensorless mode to define how zero-cross detection and commutation timing is handled.
- Values: Integrate, Delay

**Deeper Insights**
- Integrate samples back-EMF continuously after a zero crossing, integrating the waveform. More robust at low speed. 
- Delay is simpler: detect zero-cross, then add a fixed time offset. It’s less accurate under heavy load.

**How / When to Modify**
- Integrate is better for typical e-scooters or e-bikes with frequent low-speed starts.
- Delay might suffice if your motor rarely sees low RPM or if you prefer a simpler approach.

**Potential Side Effects**
- Delay can lead to stuttering at very low speed or heavier loads.
- Integrate might require more accurate BEMF coupling parameters from detection.


### 1.3 Motor Type
**Parameter Key:** `motor_type`


**What It Does**
- Chooses the fundamental commutation approach: BLDC (Trapezoidal), DC (brushed motor), or FOC (Field Oriented Control).

**Deeper Insights**
- BLDC = trapezoidal commutation, somewhat louder, slightly less efficient. 
- DC is only for brushed DC motors. Rare in modern setups. 
- FOC is advanced: quieter operation, better torque control, supports field weakening & MTPA.

**How / When to Modify**
- If the hardware supports it, FOC is usually best for noise & efficiency.
- BLDC is still used on older or simpler VESC boards.

**Potential Side Effects**
- If your ESC can’t handle FOC well, you may see DRV or MOSFET errors at high load or voltage.
- DC motor mode is irrelevant for typical brushless scooter/e-bike setups.


### 1.4 Sensor Mode
**Parameter Key:** `sensor_mode`


**What It Does**
- Applies only in BLDC mode. Chooses between Sensorless, Sensored, or Hybrid (low speed with sensors, high speed sensorless).

**Deeper Insights**
- Hybrid = halls at startup, then reverts to sensorless for efficiency. 
- Pure sensored means halls are used throughout the RPM range. 
- Sensorless is for motors without sensors or if you prefer no hall wiring.

**How / When to Modify**
- For a BLDC build with hall sensors, Hybrid is recommended for smooth takeoff.
- If no hall sensors exist, sensorless is your only option.

**Potential Side Effects**
- Sensorless can cause rough startup on heavy loads.
- Sensored-only might have overhead or timing offsets at high RPM, but it’s minor in practice.

## 2. CURRENT & BATTERY LIMITS


### 2.1 Motor Current Max
**Parameter Key:** `l_current_max`

**What It Does**
- Maximum positive (forward) phase current into the motor. Defines peak torque.

**Deeper Insights**
- Phase current can exceed battery current at partial throttle due to duty cycle step-down. 
- Setting too high can overheat the motor or saturate the ESC’s thermal limits.

**How / When to Modify**
- Check motor’s continuous & peak ratings. 
- Watch motor temperature on test rides before going higher.

**Potential Side Effects**
- Excessively high = thermal runaway in motor windings or ESC MOSFET burnouts.
- Too low = weak acceleration, under-utilized motor.
- Firmware quirks matter: Spintend 100/100 controllers on VESC Tool 6.06 refused to spin until owners reverted to 6.05 and rechecked current caps, so log software builds before blaming the limit.[^spintend-606]


### 2.2 Motor Current Max Brake
**Parameter Key:** `l_current_min (negative)`


**What It Does**
- Maximum negative phase current (braking torque). The energy from braking goes back to the ESC and potentially the battery.

**Deeper Insights**
- Large negative phase current can generate very strong braking torque even if your battery regen limit is smaller. The difference is dissipated as heat in MOSFETs.

**How / When to Modify**
- Increase negativity if you want stronger e-brake. 
- If your hardware or motor overheats on repeated downhills, reduce it.

**Potential Side Effects**
- Overstress of the ESC if the negative phase current is too high.
- If battery can’t accept that much regen, you might see BMS cut or overvoltage fault.


### 2.3 Battery Current Max
**Parameter Key:** `l_in_current_max`


**What It Does**
- The maximum drawn from the battery side. Major factor in your “forward” power limit.

**Deeper Insights**
- This must respect your BMS or cell’s discharge capability (continuous/peak).
- The battery current is usually lower than the motor current except at high duty cycles.
- Some Makerbase 75100 batches under-report real draw by roughly half to one-third; trust verified shunt-calibrated logs from a smart BMS or clamp meter before assuming the GUI shows the truth.[^makerbase-current]
- Added capacitance on the low-voltage rails can stabilize telemetry on noisy controllers, so confirm current readings only after solving any brownout behaviour.[^makerbase-cap-fix]
- VESC real-time power traces exaggerate peaks without filtering—compare against SmartDisplay or external meters before assuming a current limit is safe.[^vesc-power]
- Spintend 85150 builds have plateaued around 150 A battery despite 210–280 A commands, signalling firmware ABS caps or BMS enforcement before hardware saturation—validate those clamps before assuming controller failure.[^spintend-85150-cap]

**How / When to Modify**
- If your BMS is rated 60A, set ~60A here.
- If your battery is large and robust, you can push it higher.
- Cross-check real pack current under load—if measured draw never reaches the programmed limit, recalibrate shunts or reduce expectations before raising this number.[^makerbase-current]
- Step changes in 5–10 A increments while monitoring pack and controller temperature logs to catch sag- or heat-induced cutouts early.

**Potential Side Effects**
- Battery or BMS overload if set too high, triggering abrupt BMS cut mid-ride.
- If set too low, your top speed might still be fine at high duty, but acceleration will be limited.
- Controllers with mis-scaled current sensors may leave you thinking the limit is conservative when the pack is already at its threshold—watch BMS telemetry for unexpected high charge/discharge alarms.[^makerbase-current]


### 2.4 Battery Current Max Regen
**Parameter Key:** `l_in_current_min (negative)`


**What It Does**
- Maximum negative battery current. Limits how much regenerative current is fed back into the battery.

**Deeper Insights**
- If your battery can handle 10A charging, set about -10A.
- This is separate from motor braking current max: the ESC will limit battery current accordingly.
- When pack specs are unknown (common on OEM Laotie/Zero-style batteries), start between −5 A and −10 A until you confirm the BMS charge rating and cell chemistry tolerances.[^regen-sizing]
- Field-weakening or high-speed descents can momentarily spike bus voltage well beyond the steady-state regen current—log both voltage and temperature during testing.[^fw-regen]

**How / When to Modify**
- If your BMS or cells can handle more charge current, you can set a bigger negative number for stronger regen.
- If your battery is frequently near full, high regen can cause overvoltage.
- Raise limits only after validating that charge ports, wiring, and connectors stay within their ampacity and temperature ratings during long descents.
- Pair adjustments with Motor Current Max Brake so mechanical and electrical braking remain balanced—strong phase braking with weak battery regen simply heats the MOSFETs.[^regen-sizing]

**Potential Side Effects**
- If set too negative, you risk BMS triggers or cell damage from large charge bursts.
- If set not negative enough, your regen braking power is minimal.
- Excessive regen on a full pack can trigger BMS over-voltage cut while field weakening is still active, abruptly killing power steering—plan for a mechanical brake fallback.[^fw-regen]


### 2.5 Input Current Limit Map Start
**Parameter Key:** `l_in_current_map_start`


**What It Does**
- Tells the ESC to begin limiting Q-axis current once battery current hits some fraction (like 80–90%) of max input current. Default is 1.0 (off).

**Deeper Insights**
- Helpful if you do field weakening or MTPA and see battery current overshoots near top speed.
- E.g., setting 0.8 means at 80% of battery limit, it starts restricting additional torque.

**How / When to Modify**
- If your logs show battery current spikes to 100% instantaneously causing oscillation, set around 0.8 or 0.9.
- If no issues, leaving it at 1 is fine.

**Potential Side Effects**
- If set too low, you artificially reduce max power well before full capacity.
- If set too high, you might see minor current oscillations at top-end.


### 2.6 Input Current Map Filter
**Parameter Key:** `l_in_current_map_filter`


**What It Does**
- A filtering constant (0–1) that smooths battery current data before applying Q-axis limit in the “map start” feature.

**Deeper Insights**
- A smaller number (0.005) = heavier smoothing. 
- A bigger (0.1) = minimal filtering, more real-time reaction but can be noisy.
**How / When to Modify**
- If you see “hunting” or surging at high speed, use heavier filtering (like 0.005–0.01).
- If you need snappier response, go higher.

**Potential Side Effects**
- Too much filtering can let short battery spikes slip through.
- Too little filtering can cause torque pulsing near the limit.


### 2.7 Absolute Maximum Current
**Parameter Key:** `l_abs_current_max`


**What It Does**
- A hard fault threshold. If current magnitude exceeds this, the ESC disables output instantly.

**Deeper Insights**
- Typically set higher than normal to avoid nuisance trips from short spikes (150–300A, for instance).

**How / When to Modify**
- If you get random ABS_OVER_CURRENT faults, either raise this or enable slow filtering (l_slow_abs_current).
- Keep it sufficiently above your normal current to handle transients.

**Potential Side Effects**
- Setting it too high can let a real short-circuit go on longer, risking hardware damage.
- Setting it too low = repeated overcurrent faults on normal spikes.

## 3. RPM & DUTY LIMITS


### 3.1 Max ERPM Reverse
**Parameter Key:** `l_min_erpm`


**What It Does**
- Maximum negative electrical RPM if reversing is allowed.

**Deeper Insights**
- For no reverse, set 0. 
- For partial reverse, set a negative eRPM that matches desired reverse speed.

**How / When to Modify**
- Most e-scooters do not use reverse: set it 0 if you want to disable reversing. 
- For small vehicles needing reverse, pick a negative limit aligned with safe speeds.

**Potential Side Effects**
- If reversing is enabled but user is unaware, accidental negative throttle can jerk you backward.
- Large negative eRPM can cause mechanical stress if you force full speed reverse.


### 3.2 Max ERPM
**Parameter Key:** `l_max_erpm`


**What It Does**
- The maximum electrical RPM. The ESC enforces a speed cap.

**Deeper Insights**
- eRPM = mechanical RPM × number_of_pole_pairs. 
- E.g., 14 magnet motor => 7 pole pairs, so 6000 mechanical RPM => 42000 eRPM.

**How / When to Modify**
- If you want an artificial top-speed limit, reduce it from your default.
- If you have a large motor that can spin beyond 100k eRPM, set a suitably high number.

**Potential Side Effects**
- If too low, you’ll never reach your mechanical potential.
- Hard limit can feel abrupt if l_erpm_start is high (like 0.95 or 1.0 fraction).


### 3.3 ERPM Limit Start
**Parameter Key:** `l_erpm_start`


**What It Does**
- The fraction of l_max_erpm where the current begins to ramp down. So 0.8 means at 80% of max eRPM, torque is gradually limited.

**Deeper Insights**
- This yields a soft approach to top speed rather than an abrupt cutoff.

**How / When to Modify**
- 0.8 is typical if you want a smoother cap.
- 1.0 means no soft zone: a harsh limit near max eRPM.

**Potential Side Effects**
- If set too low (like 0.5), you lose mid-range power unnecessarily.
- If set 1.0, the cutoff can be jarring.


### 3.4 Max ERPM Full Brake / Max ERPM Full Brake Current Control
**Parameter Key:** `l_max_erpm_fbrake, l_max_erpm_fbrake_cc`


**What It Does**
- BLDC-specific parameters for controlling or disallowing a full brake or direction change below certain ERPM thresholds.

**Deeper Insights**
- Typically used if you allow reversing in BLDC mode. 
- In FOC, these are generally ignored or less relevant.

**How / When to Modify**
- If you don’t plan on reversing, default is fine. 
- If you do reversing, be sure you set safe speeds for direction changes.

**Potential Side Effects**
- Setting them too high can let you attempt direction reversals at dangerous speeds in BLDC.


### 3.5 Minimum Input Voltage / Maximum Input Voltage
Params: l_min_vin, l_max_vin

**What It Does**
- ESC throws fault if supply voltage is below min or above max.

**Deeper Insights**
- For 36/42V nominal, a typical max is 57V. 
- For 72V setups (84V full), you must raise l_max_vin to ~90–95V.
**How / When to Modify**
- Always match your battery’s highest charge voltage plus margin.
- Set l_min_vin slightly below your normal cutoff.

**Potential Side Effects**
- If l_max_vin is too low for a 20S battery, you’ll get Over_Voltage fault at full charge.
- If l_min_vin is too high, you get Under_Voltage cutout even if battery is still partially usable.


### 3.6 Battery Voltage Cutoff Start / End
Params: l_battery_cut_start, l_battery_cut_end

**What It Does**
- Gradually reduces motor power as voltage nears the cutoff. Full braking is still allowed.

**Deeper Insights**
- Example: For 10S Li-ion, set start ~34V, end ~30V. 
- This helps avoid abrupt BMS cut.

**How / When to Modify**
- Base on your cell’s recommended min voltage (like 3.0V/cell for Li-ion).
- If your BMS cuts at 2.8V/cell, set a slightly higher end for safety.

**Potential Side Effects**
- If set too high, you lose performance with significant capacity left.
- If too low, you risk damaging cells or hitting BMS cutoff anyway.


### 3.7 Battery Voltage Regen Cutoff Start / End
Params: l_battery_regen_cut_start, l_battery_regen_cut_end

**What It Does**
- Similar concept but for regenerative braking on a full battery to prevent overcharge.

**Deeper Insights**
- For a 20S battery (84V fully charged), you might set start=82V, end=84V. 
- If left default (1000 & 1100), it never triggers, risking overvoltage on steep downhills with full charge.

**How / When to Modify**
- Set according to your pack’s max voltage. 
- If you live in hilly areas, ensure this is correct or BMS may force a dangerous cutoff mid-brake.

**Potential Side Effects**
- If start is set too low, you rarely get regen. 
- If not configured, you could blow the BMS or see “OverVoltage” faults at full battery.


### 3.8 Slow ABS Current Limit
**Parameter Key:** `l_slow_abs_current`


**What It Does**
- Uses a filtered measurement for the absolute max current fault, preventing triggers on very short spikes.

**Deeper Insights**
- If you frequently see “ABS_OVER_CURRENT” on fast throttle changes, this can help.
- Great for large inductive motors or big short bursts.

**How / When to Modify**
- If random overcurrent faults appear with no real sustained high current, enable or keep it on.
- If you truly want immediate fault on any spike, keep it off.

**Potential Side Effects**
- If you rely on the absolute max to protect hardware from short, you might allow small spikes. Usually harmless for typical usage though.

## 4. THERMAL PARAMETERS


### 4.1 MOSFET Temp Cutoff Start / End
Params: l_temp_fet_start, l_temp_fet_end

**What It Does**
- The ESC reduces output current once the MOSFET temperature hits “start”, fully shutting down or faulting at “end”.

**Deeper Insights**
- Default often 85°C start, 100°C end. Some hardware can go 110–120°C safely, verify specs.

**How / When to Modify**
- If you have big heatsinks or forced cooling, you can push it higher (90/110).
- In hot climates or limited cooling, keep a safer margin.

**Potential Side Effects**
- Setting too high can degrade MOSFETs or let them approach meltdown. 
- Setting too low leads to frequent thermal throttling when it might still be safe.


### 4.2 Motor Temp Cutoff Start / End
Params: l_temp_motor_start, l_temp_motor_end

**What It Does**
- If the motor has a temperature sensor, it lowers motor current at start, then full fault at end.

**Deeper Insights**
- Some motors have an NTC (10k or 100k) or PTC sensor. Others have none, so these do nothing.
- Typical start ~85°C, end ~100°C or 110°C, depending on magnet grade.

**How / When to Modify**
- If your motor is high-grade (120°C capable), you can set 100–120°C as the end.
- Watch logs to see if you approach these thresholds.
**Potential Side Effects**
- If set incorrectly low, you lose power even though the motor can handle more.
- If set too high, you risk permanent magnet damage or winding insulation issues.


### 4.3 Acceleration Temperature Decrease
**Parameter Key:** `l_temp_accel_dec`


**What It Does**
- Decrease MOSFET/motor temperature limits by a percentage during acceleration, preserving some headroom for braking torque.

**Deeper Insights**
- If set to 0.15 (15%), then under acceleration, your 100°C limit effectively becomes ~85°C. Once you release acceleration, you get full limit again.

**How / When to Modify**
- If you do repeated accelerate-brake cycles and want guaranteed braking torque left, keep it around 0.15–0.2.
- If you rarely need that, set 0 for no difference.

**Potential Side Effects**
- Too high = acceleration is thermally limited early, sacrificing performance.
- 0 can lead to strong acceleration but no safety margin for braking if near temp limit.


### 4.4 Minimum Duty Cycle / Maximum Duty Cycle
Params: l_min_duty, l_max_duty

**What It Does**
- Forces a clamp on the PWM modulation ratio. For instance, max 0.95 means the ESC never hits full 100% duty.

**Deeper Insights**
- Some designs do l_max_duty=0.95 or 0.99 to avoid saturating sampling windows.
- l_min_duty=0.005 is default so you can release to near zero torque.

**How / When to Modify**
- If you want maximum possible speed, set ~0.99. Check hardware stability near 100% duty.
- If motor stalling issues at zero, raising l_min_duty slightly might help.

**Potential Side Effects**
- Setting max_duty=1.0 can cause issues with current sampling if your hardware can’t handle near 100% well.
- High min_duty can produce a “push” at idle, not fully freewheeling.


### 4.5 Maximum Wattage / Maximum Braking Wattage
Params: l_watt_max, l_watt_min

**What It Does**
- A power-based limit on output or braking. Usually overshadowed by current-based limits.

**Deeper Insights**
- Some e-bike regulations want 250W or 750W nominal. This tries to enforce it, but dynamic conditions can still spike currents.
- If set very high, it effectively does nothing.

**How / When to Modify**
- If local laws or personal preferences require a watt cap, set accordingly.
- If you want no power-based cap, leave them near default (1.5e6 W).

**Potential Side Effects**
- Pure watt-limiting can behave oddly with partial duty cycles or hills.
- If braking wattage is also limited, you might lose needed braking force.


### 4.6 Max Current Scale / Min Current Scale
Params: l_current_max_scale, l_current_min_scale

**What It Does**
- Multipliers that scale your current limits on-the-fly without rewriting them permanently.

**Deeper Insights**
- 1.0 means no scale. 0.5 means half your configured max or min current effectively.

**How / When to Modify**
- If you want an “eco mode” at half torque, set 0.5. 
- If you only run one profile, keep it 1.0.

**Potential Side Effects**
- Forgetting these are not at 1 can cause confusion about why you have low torque or weak brakes.


### 4.7 Duty Cycle Current Limit Start
**Parameter Key:** `l_duty_start`


**What It Does**
- At high duty cycle, the motor can approach battery voltage. This param sets at which duty fraction the ESC starts limiting current.

**Deeper Insights**
- 1.0 means no limit. If your hardware or motor saturates near 90–95% duty, you might set 0.9 so you never truly saturate.

**How / When to Modify**
- If your motor or ESC acts strangely near full duty, set 0.9 or 0.95. 
- If stable at 100% duty, keep it at 1.0.

**Potential Side Effects**
- Lowering it to 0.8 or 0.85 can reduce top-speed torque in that last portion of the duty range.
- If you do advanced field weakening, you might keep it at 1.0 and let FW handle it.

## 5. BLDC SENSORLESS (BLDC-Mode Specific)

Many people use FOC, so this is only relevant if you specifically run BLDC sensorless.

### 5.1 Minimum ERPM, Min ERPM Cycle Int Limit, Max Brake Current at Direction Change
- Control how the ESC transitions to open-loop or prevents reversing at certain currents in BLDC mode.
- Typically set automatically or by detection.

**Deeper Insights**
- If stuttering at low RPM, experiment with these or re-detect your motor constants.

**Potential Side Effects**
- Wrong settings can cause stalling or rough commutation at low speeds.


### 5.2 Cycle Integrator Limit, Phase Advance, BEMF Coupling
Params: sl_cycle_int_limit, sl_phase_advance_at_br, sl_bemf_coupling_k, etc.

What They Do
- Define the zero-cross detection method and commutation timing in BLDC sensorless.

**Deeper Insights**
- Usually set by detection. 
- If you have an unusual motor (very high KV or very low), manual tuning might help.

**Potential Side Effects**
- Incorrect values => early or late commutation => large noise, stutter, or poor efficiency.

## 6. FOC PARAMETERS


### 6.1 Current KP / KI
Params: foc_current_kp, foc_current_ki

**What It Does**
- The D/Q current controller gains in FOC. 
- Typically found automatically by the “detection” procedure.

**Deeper Insights**
- If KP is too high, you might get overshoot or audible squeals. 
- If KI is too high, drifting or low-frequency hunting can occur.

**How / When to Modify**
- If detection is stable, no need to tweak. 
- If you see “ABS OverCurrent” or poor torque response, try lowering KP or re-running detection.

**Potential Side Effects**
- Wrong gains = serious stutter, noise, or slow current loop response.


### 6.2 Zero Vector Frequency
**Parameter Key:** `foc_f_zv`


**What It Does**
- The fundamental switching frequency for SVM zero vectors in FOC. 
- Typically 20–30 kHz to stay above audible hearing range.

**Deeper Insights**
- Going to 30 kHz can make the drive silent but raises switching losses and CPU load.
- 25 kHz is a common compromise.

**How / When to Modify**
- If you hear a whine at 20 kHz, try 30 kHz. 
- If your hardware overheats at 30 kHz, step down to 20–25 kHz.

**Potential Side Effects**
- High f_zv => extra MOSFET heat, potential CPU overhead. 
- Low f_zv => audible noise.


### 6.3 Dead Time Compensation
**Parameter Key:** `foc_dt_us`


**What It Does**
- Compensates for the small off period between high and low MOSFET conduction. 
- Typically ~0.08–0.2 µs on many designs.

**Deeper Insights**
- Proper compensation yields smoother torque at low speed. 
- Overcompensation can cause negative torque or offset.

**How / When to Modify**
- Usually auto-detected or based on hardware suggestions. 
- If you suspect poor low-speed performance, tweak in small increments.

**Potential Side Effects**
- Setting it wrong => stuttering or minor torque inefficiency at very low speeds.


### 6.4 Encoder Inverted / Offset / Ratio
Params: foc_encoder_inverted, foc_encoder_offset, foc_encoder_ratio

**What It Does**
- For an external encoder (ABI, etc.), define orientation, offset degrees, ratio of mechanical to electrical rotations.

**Deeper Insights**
- For a 14-pole motor with an encoder on the shaft, ratio might be 7. 
- If the motor spins backward, toggling invert or offset can fix it.

**How / When to Modify**
- After detection, if the angle is 180° off, invert or shift offset. 
- If a gear is in between, set ratio accordingly.

**Potential Side Effects**
- Wrong offset or ratio => the ESC can’t track rotor, leading to stalling or rough motion.


### 6.5 Sensor Mode (FOC)
**Parameter Key:** `foc_sensor_mode`


**What It Does**
- For FOC, chooses “Sensorless, Encoder, Hall Sensors, HFI, VSS, 45 Deg HFI, Coupled HFI,” etc.

**Deeper Insights**
- Hall Sensors = instant start with no guess. 
- HFI or VSS helps sensorless start from 0 rpm if the motor has enough saliency.
**How / When to Modify**
- If you have physical halls, choose “Hall Sensors.” 
- If sensorless is desired with high torque from standstill, consider 45 Deg V0V7 HFI or Coupled HFI.

**Potential Side Effects**
- HFI is more CPU-intensive and can fail if Ld≈Lq with low saliency. 
- Hall-based might skip if the signals are noisy at high speed.


### 6.6 Speed Tracker Kp / Ki
Params: foc_pll_kp, foc_pll_ki

**What It Does**
- Gains for the speed observer in FOC. Usually 2000 / 30000 by default.

**Deeper Insights**
- If you see speed readout delay or overshoot, tweak. 
- Usually no need to change unless advanced debugging.

**How / When to Modify**
- Double or halve them if you suspect observer “lag” or “noise.”

**Potential Side Effects**
- Overly big = speed reading hunts or flickers. 
- Too small = slow response in the speed estimate.


### 6.7 Motor Inductance, Lq-Ld Diff, Resistance, Flux Linkage
Params: foc_motor_l, foc_motor_ld_lq_diff, foc_motor_r, foc_motor_flux_linkage

**What It Does**
- Fundamental motor parameters for FOC. Usually auto-detected.

**Deeper Insights**
- For IPM motors, Ld ≠ Lq. That difference enables MTPA. 
- If detection is off, you get poor torque or observer misalignment.

**How / When to Modify**
- Usually detection is fine. If a weird motor, you might measure manually with “measure_res/ind” in VESC Tool.

**Potential Side Effects**
- Wrong values => stuttering, huge current spikes, or inaccurate field weakening behavior.


### 6.8 Observer Gain / Slow Gain
Params: foc_observer_gain, foc_observer_gain_slow

**What It Does**
- Controls how strongly the sensorless FOC observer tracks rotor angle. 
- If too high, overshoot. If too low, lag.

**Deeper Insights**
- Gains ~ your motor’s L, R, flux. 
- Lower slow gain can help at low duty cycles.

**How / When to Modify**
- If big cogging or losing sync at certain speeds, try halving the main observer_gain.
- When hall boards die, switch to the Ortega observer with the “medium inrunner” detection preset—builders are running sensorless FOC smoothly up to ~6 kW and ≈60 km/h on heavy hubs by capping detection current this way.【F:data/vesc_help_group/text_slices/input_part013.txt†L5858-L5864】【F:data/vesc_help_group/text_slices/input_part013.txt†L5926-L5930】
- If everything is stable, no changes needed.

**Potential Side Effects**
- Not enough gain => no reliable torque at low speed. 
- Too much => random current or angle spikes.


### 6.9 Duty Downramp Kp / Ki
Params: foc_duty_dowmramp_kp, foc_duty_dowmramp_ki

**What It Does**
- In “duty cycle mode” (rare usage), prevents current overshoot when throttle is reduced quickly. Not used much in standard current control.

**Deeper Insights**
- If purely in “current control mode,” these might be irrelevant.

**How / When to Modify**
- If duty-based control is your mode, adjust to avoid big spikes on throttle release.

**Potential Side Effects**
- Overly large gains => slow speed decrease. 
- Too small => abrupt current surges.


### 6.10 Start Current Decrease / Openloop Settings
Params: foc_start_curr_dec, foc_openloop_rpm, etc.

**What It Does**
- For sensorless FOC, you can do partial open-loop at start, limiting the current to avoid saturating the observer.

**Deeper Insights**
- If your motor saturates easily at 0 rpm, a big current can ruin observer tracking.

**How / When to Modify**
- If stalling or big jerk at zero speed, set a start_curr_dec < 1 or add some openloop ramp time.
- If stable, keep default.

**Potential Side Effects**
- Lower start current means weaker launches. 
- 1.0 means no reduction but might cause stutter at heavy load zero speed.


### 6.11 MTPA Algorithm Mode
**Parameter Key:** `foc_mtpa_mode`


**What It Does**
- Allows negative d-axis current for IPM motors, improving torque-per-amp. 
- Values: Disabled, IQ Target, IQ Measured

**Deeper Insights**
- IPM motors have Ld < Lq. MTPA can significantly boost torque. 
- IQ Measured can be more reactive but noisier.

**How / When to Modify**
- If you have a known IPM motor (like many QS hub motors), enable MTPA. 
- Try IQ Target first, or IQ Measured if transitions feel off.
**Potential Side Effects**
- Negative d-current can raise motor’s back-EMF at sudden fault events => high bus voltage risk. 
- If Ld = Lq, MTPA is pointless.


### 6.12 Field Weakening
Params: foc_fw_current_max, foc_fw_duty_start, etc.

**What It Does**
- Injects negative d-axis current at high speed to exceed base motor speed. Increases top RPM but with caution.

**Deeper Insights**
- Great for “overdrive” ~10–30% more speed.
- Expect roughly 25 % more electrical loss during heavy FW events; racers log stator heat scaling about 1.5× higher compared with non-FW pulls, so plan cooling accordingly.[^fw-loss][^fw-heat]
- Watch for overvoltage if throttle is cut at high RPM.

**How / When to Modify**
- For 5–30A FW as a start, set duty_start ~0.9.
- Validate logs on actual rides.
- Stage FW increases alongside traction-control and phase-current reviews—24 S Rion builds found front-wheel spin and recurring faults when FW stacked on already aggressive 200 A tunes.[^fw-rion]
- If you dial FW back to zero for efficiency testing, be ready to trim phase current too—one commuter logged controller temps jumping from 46 °C to 55 °C within 15 minutes once extra amps replaced the missing FW headroom.[^fw-zero]

**Potential Side Effects**
- Excessive FW => bus volt spikes, MOSFET damage, or battery BMS triggers.
- Motor might overheat if run at high speed heavily.
- Combining deep FW with maxed phase current can reintroduce grinding noises, traction loss, or ABS faults on high-voltage scooters; back limits down before retesting.[^fw-rion]
- Halo 60H hubs also started to stutter around 15–20 km/h when riders stacked 350 A phase with 125 A FW, underscoring how saturation compensation and hall health matter as much as raw current.[^fw-halo]


### 6.13 Speed Tracker Position Source
**Parameter Key:** `foc_speed_soure`


**What It Does**
- Position source for the speed trackers: “Corrected Position” vs. “Observer” only.

**Deeper Insights**
- If you have sensors or HFI, corrected uses that data. 
- Observer might drift slightly at 0 speed but can be smoother at high speed.

**How / When to Modify**
- If you see speed bounce from sensor noise, pick “Observer.” 
- If observer lags at very low speed, “Corrected” might help.

**Potential Side Effects**
- With poor sensor data, “Corrected” can degrade. 
- “Observer” alone might have small offset at near-zero.


### 6.14 Short Low-Side FETs on Zero Duty
**Parameter Key:** `foc_short_ls_on_zero_duty`


**What It Does**
- When duty=0 in FOC, the ESC can short the motor windings via the low-side MOSFETs or leave them open.

**Deeper Insights**
- Shorting can create mild braking torque at zero & reduce driver power. 
- Leaving them open gives freewheel.

**How / When to Modify**
- If you want less rolling at 0 throttle, enable short. 
- If you want free coasting, disable.

**Potential Side Effects**
- Could concentrate heat on the low-side MOSFETs. 
- Slight drag if short is active.


### 6.15 Overmodulation Factor
**Parameter Key:** `foc_overmod_factor`


**What It Does**
- Allows SVM to exceed 100% modulation, e.g., hexagonal wave up to 1.15. Gains slight speed without full field weakening.

**Deeper Insights**
- 1.0–1.15 typical. 
- 1.15 approaches trapezoidal-like conduction at high speed.

**How / When to Modify**
- If you want a small top-speed bump, try 1.05–1.10. 
- At 1.0, no overmod.

**Potential Side Effects**
- Slightly rougher waveforms = more motor heat or noise at top speed.

## 7. SPEED & POSITION PID


### 7.1 PID Loop Rate
**Parameter Key:** `sp_pid_loop_rate`


**What It Does**
- Rate for position & speed controllers. Values: 25Hz to 10000Hz.

**Deeper Insights**
- Higher = more CPU load but faster response. 
- 250–1000Hz is typical for e-scooter.

**How / When to Modify**
- If speed-limiting feels laggy, increase. 
- If CPU is overwhelmed, reduce.

**Potential Side Effects**
- Too high => stuttering if CPU can’t keep up.
- Too low => slow reaction to load changes.


### 7.2 Speed PID Kp, Ki, Kd, Filter
Params: s_pid_kp, s_pid_ki, s_pid_kd, s_pid_kd_filter

**What It Does**
- The speed controller in VESC, layered over the current controller.

**Deeper Insights**
- Usually small because the underlying current loop is already fast. 
- High Kp can overshoot or surge around target speed.

**How / When to Modify**
- If you see big oscillations near set speed, reduce Kp or add Kd. 
- If it’s too slow to respond to hills, raise Kp/Ki carefully.

**Potential Side Effects**
- Excessive gains => jerkiness or noise. 
- Too low => sluggish speed corrections.


### 7.3 Minimum ERPM, Allow Braking, Ramp eRPM
Params: s_pid_min_erpm, s_pid_allow_braking, s_pid_ramp_erpms_s

**What It Does**
- Additional rules for speed control: no speed PID below min ERPM, whether braking is permitted, how fast the speed reference can ramp.
**Deeper Insights**
- If allow_braking is off, the speed controller never commands negative torque. 
- Ramp_erpms_s is how quickly the speed setpoint can climb.

**How / When to Modify**
- For typical e-scooter usage, keep braking on. 
- If you want a soft spool-up in speed mode, define a ramp limit (e.g., 25000 erpms/s).

**Potential Side Effects**
- Disabling braking in speed PID = no slowing under speed commands, coasts downhill. 
- Overly small ramp => slow acceleration requests from the speed loop.


### 7.4 Speed Source
**Parameter Key:** `s_pid_speed_source`


**What It Does**
- PLL vs. Fast / Faster Estimator for deriving speed in the speed PID.

**Deeper Insights**
- PLL is stable but slightly slower. 
- Fast or Faster can be more immediate but noisier.

**How / When to Modify**
- If you want crisp speed-limiting and can handle some noise, pick fast. 
- If you prefer stable readouts, pick PLL.

**Potential Side Effects**
- Too noisy => torque oscillations or speed readout jitter. 
- Too slow => mild speed-limiting lag.


### 7.5 Position PID
Params: p_pid_kp, p_pid_ki, p_pid_kd, etc.

**What It Does**
- For servo-like position control applications. Less common for e-scooters.

**Deeper Insights**
- Typically used in robotics/CNC. 
- If you only do speed or current control, you may ignore this.

**Potential Side Effects**
- Overly high gains => severe oscillations. 
- Usually not relevant for normal PEV usage.

## 8. CURRENT CONTROL (BLDC/DC)


### 8.1 Startup Boost
**Parameter Key:** `cc_startup_boost_duty`


**What It Does**
- In BLDC/DC current control, it’s the minimum duty fraction when throttle is first engaged, to ensure some torque at zero speed.

**Deeper Insights**
- If 0.02, you get a mild “jump.” 
- Too high and it can jerk from standstill.

**How / When to Modify**
- If your motor has trouble launching from zero, raise slightly. 
- If you want gentler starts, lower it.

**Potential Side Effects**
- Too big => unstoppable jump from standstill. 
- Too small => possible stalling under load.


### 8.2 Minimum Current
**Parameter Key:** `cc_min_current`


**What It Does**
- The threshold below which the ESC stops driving in BLDC/DC current mode, effectively releasing the motor.

**Deeper Insights**
- If set 0.1A, you might have a small idle hold. 
- If 0.01, it’s basically free-coasting under that level.

**How / When to Modify**
- If you want a bit of “hold” at near-zero throttle, raise. 
- If you want full freewheel, keep it very low.

**Potential Side Effects**
- Larger min current wastes energy or creates mild forward push at minimal throttle.


### 8.3 cc_gain, cc_ramp_step_max
- Additional BLDC/DC current control parameters for ramping the duty cycle under load. 
- Typically 0.0046 for cc_gain, 0.04 for cc_ramp_step_max.

**Deeper Insights**
- If you have a super low inductance motor, you might reduce cc_gain. 
- If acceleration is jerky, tweak ramp_step.

**Potential Side Effects**
- Wrong gain => overshoot or sluggish throttle response in BLDC/DC mode.


### 8.4 Fault Stop Time / Duty Ramp Step
Params: m_fault_stop_time_ms, m_duty_ramp_step

**What It Does**
- How long the motor is disabled after a fault. 
- The max ramp step in duty mode for BLDC/DC.

**Deeper Insights**
- Typical fault stop is 500 ms. 
- If you want quick auto-recovery, you can reduce it.

**Potential Side Effects**
- Too short => repeated fault triggers rapidly. 
- Too long => annoying downtime if a minor fault occurs.

## 9. ENCODERS & SENSOR PORTS


### 9.1 Encoder Counts, Sin/Cos Gains, Offsets
- For advanced encoders: specify amplitude ~1.0, offsets ~1.65 V for sin/cos, etc.
- If you see weird offset, correct it here.

**Potential Side Effects**
- Wrong offset => angle errors, stutter. 
- Wrong amplitude => poor angle resolution.

### 9.2 Sensor Port Mode
**Parameter Key:** `m_sensor_port_mode`


**What It Does**
- Mode for the sensor port: Hall, ABI, AS5047, Sin/Cos, TS5700N8501, BISSC, etc.

**Deeper Insights**
- Must match your physical sensor wiring or you get garbage signals.

**Potential Side Effects**
- If you pick AS5047 but physically have halls, no reading. 
- Some sensors need advanced or different wiring.


### 9.3 Invert Motor Direction
**Parameter Key:** `m_invert_direction`


**What It Does**
- Flips the commanded direction in software. Alternative to swapping two motor phases physically.

**Deeper Insights**
- Great if detection found reversed rotation or if dual-motor setups need opposite directions on front vs. rear.

**Potential Side Effects**
- If you rely on directional logic for braking or reversing, ensure you also account for inverted direction.


### 9.4 DRV8301 OC Mode / DRV8301 OC Adjustment
- For DRV8301-based hardware, define how hardware overcurrent protection is triggered or latched.
- Usually "Current Limit" is standard.

**Potential Side Effects**
- If the oc_adj is set too low, you get easy fault triggers.
- If too high, real shorts might not be interrupted fast enough.


### 9.5 Min/Max Switching Frequency in BLDC
Params: m_bldc_f_sw_min, m_bldc_f_sw_max

**What It Does**
- If using adaptive switching in BLDC, it can move between min & max freq.

**Deeper Insights**
- Default range ~3 kHz to 35 kHz. 
- Lower freq => audible noise, higher => more heat in MOSFETs.

**Potential Side Effects**
- Too high freq on old boards => driver errors or MOSFET overheating.


### 9.6 Beta Value for Motor Thermistor, etc.
**Parameter Key:** `m_ntc_motor_beta, m_ptc_motor_coeff, etc.`


**What It Does**
- If the motor has an NTC or PTC sensor, set the correct beta or coefficient. 
- Some motors use KTY or PT1000.

**Potential Side Effects**
- Wrong sensor settings => inaccurate temperature reading => poor thermal throttling.

## 10. BMS SETTINGS


### 10.1 BMS Type
**Parameter Key:** `bms.type`


**What It Does**
- If using a CAN-based “VESC BMS,” you can unify data. If none, ignore.

**Deeper Insights**
- “None” means the ESC ignores BMS comm. 
- “VESC BMS” uses messages from the official hardware or similar.

**Potential Side Effects**
- If incorrectly enabled, you might see spurious limiting if no real BMS data is present.


### 10.2 BMS Limit Mode, Temperature Limit, SOC, VCell Min/Max
Params under bms.*

**What It Does**
- The ESC can reduce current smoothly based on battery’s temperature, SOC, or cell voltages from the BMS over CAN.

**Deeper Insights**
- Overtemp or low SOC => input current is scaled down. 
- This prevents abrupt BMS cut at cell-level constraints.

**How / When to Modify**
- If you have an advanced BMS that shares data, set these for gentle limiting. 
- If your BMS is standalone or simple, these do nothing.

**Potential Side Effects**
- If BMS data is invalid or missing, the ESC might clamp power incorrectly. 
- Misconfigured voltage or SOC limits can hamper performance or cause weird cutouts.


## Footnotes

[^makerbase-current]: Multiple builders found Makerbase 75100 controllers reporting only half to one-third of the programmed battery current, forcing them to validate limits with smart-BMS telemetry or clamp meters before raising power targets.【F:knowledge/notes/input_part005_review.md†L75-L76】【F:knowledge/notes/input_part005_review.md†L106-L106】
[^makerbase-cap-fix]: Reviewers noted that bolting additional capacitance onto the 12 V/5 V rails of Flipsky and Makerbase hardware reduced brownouts and restored trustworthy telemetry before any current-limit tuning.【F:knowledge/notes/input_part005_review.md†L494-L520】
[^vesc-power]: SmartDisplay telemetry revealed that VESC Tool real-time power overshoots true pack watts by 10 kW+ unless you add ≥100 ms filtering, so builders verify limits with external meters before trusting GUI peaks.【F:knowledge/notes/input_part014_review.md†L2140-L2154】
[^spintend-606]: Updating Spintend 100/100 controllers to VESC Tool 6.06 left some builds motionless until they downgraded to 6.05 and capped phase current near 130 A / ABS 180 A, underscoring the need to record firmware alongside current limits.【F:knowledge/notes/input_part012_review.md†L80-L82】
[^spintend-85150-cap]: Matthew’s Spintend 85150 logs plateaued near 150 A battery despite 210–280 A commands, implying firmware ABS caps or BMS intervention before the hardware truly saturates—confirm those clamps before blaming the controller.【F:knowledge/notes/input_part011_review.md†L353-L353】
[^regen-sizing]: Community guidance for unknown OEM packs recommends starting regen at −5 A to −10 A and increasing only after confirming BMS charge ratings and wiring health, rather than assuming large Laotie/Zero batteries can absorb high current bursts.【F:knowledge/notes/input_part005_review.md†L25-L25】
[^fw-regen]: Field-weakening and long downhills were shown to spike bus voltage on Spintend builds, so riders log pack voltage/temperature while testing regen to avoid surprise BMS cutoffs or controller faults.【F:knowledge/notes/input_part005_review.md†L259-L259】
[^fw-loss]: Riders estimate roughly 25 % higher losses when field weakening is active, backing off when logs show efficiency plunging during high-speed pulls.【F:knowledge/notes/input_part002_review.md†L68-L70】
[^fw-heat]: MP2 builders recorded about 1.5× stator heat rise under field-weakening compared with non-FW runs, motivating them to skip FW until additional cooling is installed.【F:knowledge/notes/input_part010_review.md†L71-L72】
[^fw-rion]: Jesús’s 24 S Rion experiments showed front-wheel spin near 120 km/h and returning grinding faults whenever phase current and field weakening were maxed simultaneously, prompting a retreat to ~200 A settings before further tests.【F:knowledge/notes/input_part007_review.md†L52-L55】
[^fw-zero]: Dropping FW to zero only for efficiency forced the controller to replace the lost speed with extra phase amps, sending case temps from 46 °C to 55 °C within 15 minutes—plan staged retests instead of jumping current caps immediately.【F:knowledge/notes/input_part012_review.md†L10882-L10888】
[^fw-halo]: Halo 60H testing at 350 A phase plus 125 A FW triggered 15–20 km/h stutter until the rider rechecked hall sensors and trimmed phase amps, highlighting saturation-compensation tuning before leaning on high FW numbers.【F:knowledge/notes/input_part012_review.md†L10916-L10946】

# WRAP-UP & FINAL NOTES

- Always Start with Detection: Let the firmware auto-detect motor parameters (R, L, flux, hall table, etc.).
- Test in Steps: Increase or adjust current limits incrementally, watching temperature logs. 
- Thermal & Voltage Headroom: Large negative braking or field weakening can produce bus voltage spikes. Ensure safety margins.
- Hall vs Sensorless vs HFI: 
  - Hall = simpler immediate start,
  - Sensorless/HFI = advanced but can be just as good if tuned well,
  - Keep an eye on noise or offset at high speeds.
- Smart BMS: If you have a CAN-based BMS, you can coordinate battery info for smooth limiting. If not, the ESC only sees battery voltage and can’t individually protect cell groups.
Ride Safely and enjoy the benefits of a finely tuned VESC-based controller. If something behaves oddly, revert to your last known stable config. Detailed logs are your friend!

## Source Notes
- Parameter tuning workflow, ramp-time effects, observer choices, and ADC precautions consolidate repeated 2025 Slack guidance on VESC configuration, especially the October slices detailing ramp-time targets, throttle-curve blending, and sensor wiring best practices.【F:knowledge/notes/input_part010_review.md†L523-L527】【F:knowledge/notes/input_part011_review.md†L621-L728】【F:knowledge/notes/input_part013_review.md†L329-L337】
- Current, regen, and thermal guardrails echo Smart Repair’s field logs on Motor/Battery Current limits, regen budgeting, and field-weakening risks from the same transcript reviews.【F:knowledge/notes/input_part012_review.md†L423-L431】【F:knowledge/notes/input_part005_review.md†L202-L214】
