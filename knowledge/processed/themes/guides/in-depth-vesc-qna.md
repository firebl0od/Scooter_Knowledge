# 🏆 The Ultimate In-Depth VESC Q&A

Below is a massive Q&A covering a wide array of topics around VESC-based controllers.
  - ranging from beginner-level queries to advanced technical discussions. It draws on the 3000+ lines of chat knowledge, real-world usage, and the official VESC parameter descriptions.

Use the collapsible sections below to jump straight to the answers that matter most to you.

## Table of Contents

### Part 1 – Core Topics (Q1–30)

- [1. Basic Getting Started](#1-basic-getting-started)
- [2. Battery & Current Limits](#2-battery--current-limits)
- [3. Voltage Cutoffs & Regen](#3-voltage-cutoffs--regen)
- [4. FOC vs. BLDC](#4-foc-vs-bldc)
- [5. Sensorless, Halls & HFI](#5-sensorless-halls--hfi)
- [6. Advanced Torque Features: MTPA & Field Weakening](#6-advanced-torque-features-mtpa--field-weakening)
- [7. Thermal Management](#7-thermal-management)
- [8. Noise, Cogging & Settings Tweaks](#8-noise-cogging--settings-tweaks)
- [9. BMS Integration](#9-bms-integration)
- [10. Troubleshooting & Misc.](#10-troubleshooting--misc)

### Part 2 – Advanced Scenarios (Q31–50)

- [31. Partial Meltdown or “Soft Failure”](#31-partial-meltdown-or-soft-failure)
- [32. High Inductance or Low Inductance Motors](#32-high-inductance-or-low-inductance-motors)
- [33. Traction Control for Dual Motors](#33-traction-control-for-dual-motors)
- [34. Logging & Analysis](#34-logging--analysis)
- [35. Multi-Battery Configurations](#35-multi-battery-configurations)
- [36. Field Weakening Tips](#36-field-weakening-tips)
- [37. FOC_CC_Decoupling](#37-foc_cc_decoupling)
- [38. Custom Firmwares & Features](#38-custom-firmwares--features)
- [39. PPM, ADC, or UART Control](#39-ppm-adc-or-uart-control)
- [40. Lack of Sensor Port on Some Hardware](#40-lack-of-sensor-port-on-some-hardware)
- [41. Parallel Controllers (Shared Throttle without CAN)](#41-parallel-controllers-shared-throttle-without-can)
- [42. When to Use “High Current Sampling Mode”](#42-when-to-use-high-current-sampling-mode)
- [43. Starting in Neutral or “Brake” Mode](#43-starting-in-neutral-or-brake-mode)
- [44. Firmware Updates & Compatibility](#44-firmware-updates--compatibility)
- [45. Advanced Troubleshooting (“My ESC Goes Crazy at Mid Speed”)](#45-advanced-troubleshooting-my-esc-goes-crazy-at-mid-speed)
- [46. Combining MTPA & Field Weakening](#46-combining-mtpa--field-weakening)
- [47. Small ESC Configs (Low Voltage, e.g., 24V)](#47-small-esc-configs-low-voltage-eg-24v)
- [48. Hardware Limits & Shunts](#48-hardware-limits--shunts)
- [49. PWM Mode: Bipolar?](#49-pwm-mode-bipolar)
- [50. Final Best Practices](#50-final-best-practices)

### Part 3 – Additional 50 High-Quality Q&A

- [1. FOC Current KP/KI Manual Tuning](#1-foc-current-kpki-manual-tuning)
- [2. Motor Has Multiple Winding Options](#2-motor-has-multiple-winding-options)
- [3. High-Speed Drones or eJets](#3-high-speed-drones-or-ejets)
- [4. “Memory Overflows” or CPU Overload](#4-memory-overflows-or-cpu-overload)
- [5. Overvoltage on Rapid Deceleration in Race Scooters](#5-overvoltage-on-rapid-deceleration-in-race-scooters)
- [6. Rapid-Fire Throttle Inputs](#6-rapid-fire-throttle-inputs)
- [7. ADC vs. PPM Throttle Curves](#7-adc-vs-ppm-throttle-curves)
- [8. Common Pitfall: Using the Wrong Hardware Version in Tool](#8-common-pitfall-using-the-wrong-hardware-version-in-tool)
- [9. Inconsistent Hall Readings](#9-inconsistent-hall-readings)
- [10. VESC BMS Min/Max Cell Voltage Balancing](#10-vesc-bms-minmax-cell-voltage-balancing)
- [11. Pushing Motor beyond its Nameplate Voltage](#11-pushing-motor-beyond-its-nameplate-voltage)
- [12. Overcurrent on Startup in Sensorless Mode](#12-overcurrent-on-startup-in-sensorless-mode)
- [13. Step-by-Step Hall Table Editing](#13-step-by-step-hall-table-editing)
- [14. Motor “Hooting” or “Growling” at Mid Speed](#14-motor-hooting-or-growling-at-mid-speed)
- [15. Running Outrunner Motors in E-Bike Conversions](#15-running-outrunner-motors-in-e-bike-conversions)
- [16. Multi-Polarity: “Motor Poles” Mismatch](#16-multi-polarity-motor-poles-mismatch)
- [17. Water Damage or Corrosion](#17-water-damage-or-corrosion)
- [18. Belt vs. Hub vs. Direct Drive](#18-belt-vs-hub-vs-direct-drive)
- [19. “FOC Sample in V0 and V7 Interpolation”](#19-foc-sample-in-v0-and-v7-interpolation)
- [20. Motor Overtemp Behavior vs. MOSFET Overtemp](#20-motor-overtemp-behavior-vs-mosfet-overtemp)
- [21. BMS Communication Intermittent](#21-bms-communication-intermittent)
- [22. Inductive Spikes from Long Motor Cables](#22-inductive-spikes-from-long-motor-cables)
- [23. Current Scaling with l_current_max_scale](#23-current-scaling-with-l_current_max_scale)
- [24. High-Voltage (e.g., 20S–30S) and Capacitor Modules](#24-high-voltage-eg-20s30s-and-capacitor-modules)
- [25. Unusual Throttle Dead-Zone](#25-unusual-throttle-dead-zone)
- [26. Overtemp Ramp vs. Fault](#26-overtemp-ramp-vs-fault)
- [27. Fine-Tuning Position Controller Gains](#27-fine-tuning-position-controller-gains)
- [28. Multi-Motor Vehicles (4 WD e-scooter, for example)](#28-multi-motor-vehicles-4-wd-e-scooter-for-example)
- [29. “Motor Loss Torque” in Motor Config](#29-motor-loss-torque-in-motor-config)
- [30. Using a Very Low KV Motor without FW](#30-using-a-very-low-kv-motor-without-fw)
- [31. Motor Feels “Weak” at Partial Throttle](#31-motor-feels-weak-at-partial-throttle)
- [32. Unexpected Reverse](#32-unexpected-reverse)
- [33. PWM Deadtime Variation](#33-pwm-deadtime-variation)
- [34. Ultra-Low Speed Control for Robotics](#34-ultra-low-speed-control-for-robotics)
- [35. NTC 100k vs. PTC 1k in Motor Temp](#35-ntc-100k-vs-ptc-1k-in-motor-temp)
- [36. “I2T” Thermal Modeling](#36-i2t-thermal-modeling)
- [37. Kelly or Sabvoton vs. VESC](#37-kelly-or-sabvoton-vs-vesc)
- [38. Low Battery Voltage but High Phase Current](#38-low-battery-voltage-but-high-phase-current)
- [39. Limit Start vs. End Ratios](#39-limit-start-vs-end-ratios)
- [40. Acceleration Temperature Decrease Tweak](#40-acceleration-temperature-decrease-tweak)
- [41. Diagnosing “ABS Current” vs. “DRV Fault” vs. “MOSFET Shorted”](#41-diagnosing-abs-current-vs-drv-fault-vs-mosfet-shorted)
- [42. “Battery Voltage Too Low” but BMS is Fine](#42-battery-voltage-too-low-but-bms-is-fine)
- [43. Legacy 4.xx + Field Weakening?](#43-legacy-4xx--field-weakening)
- [44. Random Motor Reverse at High Speed?](#44-random-motor-reverse-at-high-speed)
- [45. “FOC Sat Comp” for Hard-Loaded Motor](#45-foc-sat-comp-for-hard-loaded-motor)
- [46. Unusual “Input Latency” on Throttle](#46-unusual-input-latency-on-throttle)
- [47. Resistive Spot Welding Using VESC?](#47-resistive-spot-welding-using-vesc)
- [48. Using a Gimbal Motor](#48-using-a-gimbal-motor)
- [49. Modulating Regen Strength by Throttle](#49-modulating-regen-strength-by-throttle)
- [50. Fast-Swapping Motors or Wheels](#50-fast-swapping-motors-or-wheels)

## 1. BASIC GETTING STARTED

<details>
<summary><strong>Q1. I’m brand new to VESC controllers. What’s the first thing I need to do after installing the hardware?</strong></summary>

**Answer**

1. Wire & Check – Confirm all motor phases, hall sensors (if used), and power/battery connectors are correct, with no reversed polarity or short.
2. Install VESC Tool – On a PC or mobile phone, you’ll configure parameters. 
3. Run Motor Detection – This is crucial: VESC Tool will measure your motor’s winding resistance (R), inductance (L), flux linkage, hall table if any, etc. 
4. Set Battery Limits – L_in_current_max for battery discharge, L_in_current_min for battery regen, plus the battery voltage cutoffs. 

These steps ensure you have the correct fundamental data for your motor and keep the battery safe.

</details>

<details>
<summary><strong>Q2. Why is Motor Detection so critical? Can’t I just pick default numbers and go?</strong></summary>

**Answer**

- Motor Detection tailors the FOC or BLDC commutation specifically to your motor. The controller measures R, L, flux linkage, and hall sensor alignment. 
- If you skip detection, you risk rough operation, random overcurrent faults, or poor torque. 
- FOC is particularly sensitive to incorrect motor parameters—leading to stutter or the ESC failing to track rotor position.

</details>

<details>
<summary><strong>Q3. Are there different detection steps for BLDC mode vs. FOC mode?</strong></summary>

**Answer**

- Yes. In BLDC mode, the firmware tries to measure the back-EMF coupling, zero-cross timing, and (optionally) calibrate hall sensors for the 6-step commutation scheme.
- In FOC mode, detection is more advanced: it measures motor’s stator resistance, inductance, flux linkage, and can do hall sensor mapping. 
- The end result in FOC is more precise data used by the observer or sensors to track rotor angle continuously.

</details>

## 2. BATTERY & CURRENT LIMITS

<details>
<summary><strong>Q4. I have a 60V scooter battery with a 30A BMS. How do I set the battery current limits safely?</strong></summary>

**Answer**

- Set L_in_current_max around the continuous BMS rating (e.g., 30A). That ensures you won’t draw beyond the BMS’s safe limit. 
- Set L_in_current_min (regen) around the BMS’s charge rating. If the BMS says 10A max charging, set around -10A or -12A so you don’t exceed it. 
- Always confirm your cells’ capabilities. Some BMS are 30A continuous but can do short bursts. If you want short bursts of 40A, keep them short, watch BMS temperature logs, or have a BMS that can handle peaks.

</details>

<details>
<summary><strong>Q5. What if my battery can handle 50A continuous, but I want strong braking—how do I avoid overcharging on a full battery?</strong></summary>

**Answer**

1. Battery Regen Current – Use L_in_current_min negative, like -50A, if your pack truly supports big charge current. 
2. Battery Voltage Regen Cutoffs – L_battery_regen_cut_start & end can progressively reduce regen if the battery voltage is near full. E.g., if 4.20V/cell is max, set cut_start ~4.15V/cell, cut_end ~4.2V. 
3. Practical – If you always top up to 100% and immediately go downhill, you risk overvoltage. So ensure the regen cutoff is set or you start at 90% if you have big downhills right away.

</details>

<details>
<summary><strong>Q6. Why do we have separate limits for Motor Current (phase) and Battery Current?</strong></summary>

**Answer**

- Phase Current (l_current_max/min) – This is the torque level in the motor windings. Under partial throttle/duty, the motor can see large phase currents even if battery current is moderate.
- Battery Current (l_in_current_max/min) – The actual DC current from or to the battery. 
- In other words, a motor might be pulling 80A in the phases at only 40A from the battery if the duty cycle is 50%. This is how field-oriented controllers produce high torque at lower voltage.

</details>

## 3. VOLTAGE CUTOFFS & REGEN

<details>
<summary><strong>Q7. I keep hitting “ABS Over Voltage” if I brake hard on a full battery. How to fix that?</strong></summary>

**Answer**

1. Regen Cut Settings – Increase l_battery_regen_cut_start to begin tapering braking near full charge. 
2. Lower L_in_current_min – If your battery is full, it can’t accept big charge current, so reduce negative battery current to -5 or -10A. 
3. Practical Tips – Avoid 100% charge if you know you have big downhills. Some advanced riders charge to 4.1V/cell to keep enough headroom.

</details>

<details>
<summary><strong>Q8. What if my BMS abruptly cuts power during regeneration? Won’t that blow my ESC?</strong></summary>

**Answer**

- Abrupt BMS cut on a high-current regen event can cause a bus voltage spike (the motor is still rotating, generating power).
- Often the ESC tries to clamp or keep it safe, but it can exceed MOSFET ratings if the spike is large.
- Solutions:
  1. Set a more conservative L_in_current_min if your BMS is known to cut at certain voltages.
  2. Configure battery_regen_cut_start/end so the ESC ramps down regen instead of letting the BMS do a hard cutoff.

</details>

<details>
<summary><strong>Q8a. What do Stage 1 and Stage 2 battery voltage cutoffs actually do?</strong></summary>

**Answer**

- Stage 1 (“Cutoff Start”) simply tapers output—it reduces available torque so you feel the scooter softening while voltage approaches the limit.
- Stage 2 (“Cutoff End”) stops motor drive but keeps controller logic alive, letting you coast and retain telemetry instead of hard-shutting the ESC.
- Because the controller stays powered, you can safely set the software cutoff a bit below the BMS threshold.
  - as long as you keep monitoring pack voltage to avoid tripping the discharge FETs.[^cutoff_stages]

</details>

## 4. FOC VS. BLDC

<details>
<summary><strong>Q9. What’s the difference in real-world ride feel between BLDC and FOC?</strong></summary>

**Answer**

- Noise: BLDC has a characteristic “trapezoidal” hum, especially at lower speeds. FOC is nearly silent. 
- Smoothness: FOC gives smoother torque, particularly at low RPM or start. 
- Efficiency & Heat: FOC is generally more efficient or at least comparable at higher loads, though it’s more complex. 
- Setup: BLDC can be simpler to configure on older VESC boards. 

Most modern e-scooter/e-bike conversions use FOC for the quiet operation and advanced torque control.

</details>

<details>
<summary><strong>Q10. My older VESC hardware struggles at high voltage with FOC. Is that normal?</strong></summary>

**Answer**

- Some older 4.xx hardware (DRV8302-based) or under-rated gate drivers can blow DRVs under high-voltage FOC. 
- FOC demands faster sampling, better shunt design, and more accurate current measurement. If the hardware’s layout or DRV is borderline, you get random DRV failures. 
- If you’re above ~12S or pushing 60–80V, you might want a “VESC 6 or better” or a specialized variant with robust gate drivers.

</details>

## 5. SENSORLESS, HALLS & HFI

<details>
<summary><strong>Q11. My motor has hall sensors. Should I use them in FOC or just go sensorless?</strong></summary>

**Answer**

- Keep the hall sensors enabled whenever they are healthy—builders running pure sensorless FOC still report needing a push start or deep HFI tuning to stop squealing stalls at launch.[^1]
- Treat intermittent hall faults as a wiring or PCB issue to fix, not a reason to abandon sensors; repeated “Bad FOC hall detection” threads traced the fault to damaged hall boards that were replaced before smooth starts returned.[^2]
- If you must run sensorless, confirm the motor has at least ~15 % inductance delta (Ld vs. Lq) so high-frequency injection can lock on quickly and deliver hall-like launch torque.[^3]

</details>

<details>
<summary><strong>Q12. What is HFI (High Frequency Injection) and why might I need it?</strong></summary>

**Answer**

- HFI injects a calibrated AC probe into the windings so the controller can estimate rotor angle even at 0 eRPM; Vedder’s 45° V0/V7 routine on FW 6.0 finally gave riders repeatable hall-less launches.[^4]
- Firmware 6.02 and later polish the workflow—wider hall hysteresis, quieter sampling, and better CAN logging make silent HFI viable on phase-shunt ESCs once tuned.[^5]
- Crews still treat HFI as an expert tool: field tests pair it with saturation compensation and start-current trimming before trusting customer scooters without halls.[^6]

</details>

<details>
<summary><strong>Q13. What’s the difference between 45° V0V7 HFI, Coupled HFI, VSS, etc.?</strong></summary>

**Answer**

- 45° V0/V7 HFI keeps firing the probe while you ride, letting the observer stay locked as long as your ESC can sample both zero vectors at ≥30 kHz.[^4]
- Coupled HFI watches the cross-axis current response and tends to favour IPM motors with large saliency splits, while the simpler Vedder Sensorless Start (VSS) just injects a burst, resolves the 180° ambiguity, and hands back to the observer.[^7]
- Builders chasing quiet starts still run VSS or halls on steep launches, then graduate to continuous HFI once they verify temperature inputs and inductance data for the specific motor.[^5]

</details>

## 6. ADVANCED TORQUE FEATURES: MTPA & FIELD WEAKENING

<details>
<summary><strong>Q14. What is MTPA (Maximum Torque per Amp) and do I need it for my motor?</strong></summary>

**Answer**

- Enable MTPA only when the motor actually has saliency—IPM and speed-wound hubs respond, but surface-magnet commuter hubs mostly just make extra heat for little gain.[^8]
- Race builders still see value: Blade-class hubs pick up ~20 km/h of top speed on 15–17 S packs when phase current headroom stays around 250 A, yet they log every run to confirm magnets and stators survive the added negative d-current.[^9]
- Most community dynos now treat MTPA as optional even on big hubs because voltage upgrades or taller windings usually deliver the same speed boost with less tuning overhead.[^8]

</details>

<details>
<summary><strong>Q15. How do I safely enable MTPA in VESC Tool?</strong></summary>

**Answer**

1. Warm the motor and record Ld/Lq manually—builders double-check the wizard because small hubs often report zero saliency.[^3]
2. Populate `foc_motor_ld_lq_diff` (and, if needed, `foc_mtpa_mode`) with those measured values, then log phase current vs. temperature on short pulls before extending runs.[^8]
3. Watch the hardware limits: stacking MTPA with field weakening on 20 S Spintend 85150s already blew MOSFETs, so ensure you have headroom in both the controller and BMS before exploring aggressive settings.[^10]

</details>

<details>
<summary><strong>Q16. What’s Field Weakening (FW) and how does it differ from MTPA?</strong></summary>

**Answer**

- Field weakening adds negative d-axis current at high duty to bend the back-EMF line and squeeze extra RPM; MTPA focuses on torque per amp at lower duty.[^11]
- Community logs show FW delivering only ~8 km/h on dual-motor commuter builds while doubling power draw—voltage or winding changes generally produce cleaner gains.[^11]
- Keep them separate: many racers run modest MTPA for punch but leave FW off until they confirm the controller, motor, and pack can handle the combined thermal and voltage load.[^8]

</details>

<details>
<summary><strong>Q17. Any big risks with Field Weakening?</strong></summary>

**Answer**

- Voltage spikes: Spintend 85150 riders documented MOSFET deaths when stacking 45 A of FW on 20 S packs, prompting a hard stop on “full send” tunes without upgraded silicon.[^10]
- Thermal load: mid-power scooters running 30 A of FW saw hubs overheat even with traction control, so crews now prioritize airflow, ferrofluid, or larger stators before lifting FW ceilings.[^12]
- Pack and BMS stress: once duty approaches 100 %, phase and battery current converge—poor regen cutoffs or Daly/ANT BMS limits have tripped and back-fed controllers during aggressive braking.[^13]
- Plan margin in both controller voltage rating and pack headroom before relying on FW for daily riding.[^10]

</details>

## 7. THERMAL MANAGEMENT

<details>
<summary><strong>Q18. I keep thermal throttling. My ESC hits 85°C quickly. Should I raise l_temp_fet_start/end?</strong></summary>

**Answer**

- Fix the mechanical interface before raising limits: swap thick stock pads for 0.5 mm interfaces or direct paste, clamp the case to real metal, and add airflow so the controller stops rocketing past 80 °C within minutes.[^14]
- Most crews treat ~70 °C MOSFET case temperature as the everyday ceiling; once logs show 85 °C after a short pull, they cut phase/battery current or move the controller to a better heat sink instead of chasing higher firmware thresholds.[^15]
- High-power builds still reserve 90/110 °C start/end only for short tests.
  - race teams log case and stator temps continuously and back off once controller or motor temps brush 90–100 °C to avoid demagnetizing hardware.[^16]

</details>

<details>
<summary><strong>Q19. My motor also has a thermistor. Should I enable motor temp cutoff too?</strong></summary>

**Answer**

- Install a reliable probe first—crews glue 2 × 4 mm EPCOS/TDK NTCs to the hall bundle with high-temp epoxy or RTV so VESC Tool sees true stator temperatures instead of case readings.[^17]
- Route the leads away from phase conductors or shield them; poorly routed sensors have shown signal collapse above 80 A and left riders blind to heating until faults appeared.[^18]
- Once telemetry is trustworthy, set conservative thresholds (e.g., 80–90 °C start, 105–110 °C end for high-grade magnets) and dial current back if logs show repeated climbs into the 90 °C range.[^16]

</details>

## 8. NOISE, COGGING & SETTINGS TWEAKS

<details>
<summary><strong>Q20. My sensorless motor cogs at low speed. How can I reduce it?</strong></summary>

**Answer**

1. FOC detection – Double-check the measured R, L, flux. If it’s inaccurate, re-run detection with a different “Max power loss” or “Motor current” detection parameter. 
2. Observer Gain – You might lower foc_observer_gain if it’s overshooting angle at near-zero speed. 
3. Startup Current – If it saturates, reduce the startup current or use openloop_rpm/time to ramp more gently.
4. Add HFI or use hall sensors if physically possible.
5. Expect compromises on heavy hubs today – even with HFI/VSS, riders still cap launch torque or give a light push because zero-speed starts tend to chatter on sensorless-only scooters.[^1]

</details>

<details>
<summary><strong>Q21. Why do I hear a slight squealing or high-pitch tone at partial throttle in FOC?</strong></summary>

**Answer**

- Typically it’s PWM frequency or random harmonic noise. If your zero vector frequency is around 20 kHz, you might be hearing it in the 16–20 kHz range. 
- Switching to 30 kHz can push it beyond most human hearing. 
- Some hardware or poor layout can also produce audible coil whine at specific loads. 
- Usually harmless if not too loud.

</details>

<details>
<summary><strong>Q22. I see occasional “Over Current” faults on abrupt throttle changes but no real meltdown. Should I enable l_slow_abs_current?</strong></summary>

**Answer**

- Yes, enabling l_slow_abs_current uses a filtered measurement for the absolute max current. This helps avoid false triggers on sub-millisecond spikes. 
- If your usage is large outrunner or a big hub motor with high inductance, you might see short overcurrent bursts that are benign. 
- If they’re truly benign, slow abs can fix it. If not, re-check your hardware for shorted cables or settings that are too high.

</details>

## 9. BMS INTEGRATION

<details>
<summary><strong>Q23. I have a VESC BMS on CAN. How do I leverage it for better battery management?</strong></summary>

**Answer**

1. Set `bms.type = VESC BMS` (or the matching smart-BMS profile) so the controller can read pack current, per-cell voltages, and temperatures over CAN instead of relying on noisy low-side shunts.[^19]
2. Enable “BMS limit mode” for temperature, SoC, and cell-voltage ceilings; the ESC will taper current gracefully instead of waiting for the BMS to hard-cut and back-feed the MOSFETs.[^20]
3. Log the CAN data during shakedowns—builders now record pack and motor telemetry together to verify that firmware limits align with real BMS behaviour before shipping high-power scooters.[^19]

</details>

<details>
<summary><strong>Q24. What if the BMS data is inaccurate or occasionally drops out on CAN?</strong></summary>

**Answer**

- Expect CAN dropouts to show up as stale or zero readings—when telemetry glitches, the ESC can suddenly clamp current or throw faults even though the pack is fine.[^21]
- Start troubleshooting with wiring, shielding, and balance-lead routing; Daly and ANT owners have documented trips from harness shorts or regen spikes that looked like controller failures.[^20]
- Keep conservative local limits in `l_in_current_max/min` so the scooter stays safe even if the BMS feed dies, and recalibrate smart-BMS current sensors when chasing ±500 W accuracy on 30 kW builds.[^21]

</details>

## 10. TROUBLESHOOTING & MISC.

<details>
<summary><strong>Q25. My motor runs backward after detection. Should I physically swap phase wires or use m_invert_direction?</strong></summary>

**Answer**

- Easiest is toggling m_invert_direction = true if everything else is correct. This purely flips the sign of commanded torque. 
- Physically swapping two phases is also valid in BLDC but might require re-checking hall mapping if you rely on halls. 
- For FOC with an encoder or halls, you can do either approach. Typically the software toggle is simpler.

</details>

<details>
<summary><strong>Q26. I see “DRV Fault” on older 4.12 hardware at random. Any tips?</strong></summary>

**Answer**

- That often means the DRV8302 chip saw an overcurrent or undervoltage event. 
- Check your supply wires, battery voltage under load, or see if your MOSFET gate resistors or layout are stressed by FOC. 
- Possibly switch to BLDC mode at high voltage or reduce the maximum battery current to avoid spiking the DRV.

</details>

<details>
<summary><strong>Q27. How do I evaluate if my motor can handle 100A phase without burning up?</strong></summary>

**Answer**

1. Motor Resistance – The winding resistance times I² gives heat. For example, if R is 0.02Ω and you push 100A, that’s 200W of copper loss. 
2. Test Ride – Check real motor shell temperature or internal thermistor after repeated accelerations. 
3. Statorade or Ferrofluid – Some advanced riders use fluid in the hub to transfer heat better if it’s a sealed design. 
4. Use l_temp_motor_start/end if you have a sensor to ensure you don’t exceed 120°C or your magnet rating.

</details>

<details>
<summary><strong>Q28. I want dual motors. Do I just copy the same settings or do I need half the battery current each?</strong></summary>

**Answer**

- If both ESCs share the same battery, each VESC can be set to half the total battery current (so total doesn’t exceed battery limit). 
- Alternatively, if your battery can do 60A and you set each ESC to 60A, you risk pulling 120A. Some riders do this intentionally if they know they rarely max out both motors simultaneously. 
- Also configure CAN so one VESC is “master” for the throttle input, and the other is “slave.” Or separate control signals if that’s your design.

</details>

<details>
<summary><strong>Q29. Which hardware parameters do I tweak for high-speed motors with big ERPM?</strong></summary>

**Answer**

- Increase l_max_erpm if your mechanical rpm is beyond typical 50–60k eRPM. Some people set 100k or 150k for small motors. 
- Possibly raise PWM frequency (foc_f_zv ~ 30 kHz) if you approach extremely high electrical speeds. 
- Ensure you have enough overhead in observer gain or advanced decoupling if your motor has minimal inductance.

</details>

<details>
<summary><strong>Q30. Any final best practices to avoid random faults or damage?</strong></summary>

**Answer**

1. Always do detection with the correct battery voltage available, not a half-charged bench PSU if possible. 
2. Check logs after a test ride. Look for peak battery amps, motor amps, mosfet & motor temps. 
3. Set gentle cutoffs (voltage, current, thermal) to avoid abrupt BMS or ESC-level fault cutouts. 
4. Use properly rated connectors (phase & battery) so you don’t melt them at high current. 
5. If running advanced features like MTPA or Field Weakening, do incremental tests in a safe area, watch for voltage spikes, and confirm it’s stable.
6. Release the throttle when a fault appears.
  - VESC clears the fault automatically once input drops to zero, but holding the trigger keeps the controller in a prolonged shutdown state.[^2]

</details>

# 🏆 Continuing the Ultimate In-Depth VESC Q&A

Below are more advanced or niche questions (continuing from Q30), focusing on edge cases, specialty setups, and deeper parameter tuning. 


## 31. PARTIAL MELTDOWN OR “SOFT FAILURE”

<details>
<summary><strong>Q31. What if my ESC starts to smell or partially burn, yet I see no obvious short? Could it be a “soft failure”?</strong></summary>

**Answer**

- Sometimes MOSFETs or drivers degrade over time from repeated thermal or current spikes, resulting in partial conduction issues or higher Rds(on). 
- You might notice unusual heat at moderate current or see slight performance drop. 
- Steps:
  1. Inspect the MOSFETs for discoloration or bulges on any capacitor.
  2. Check real-time current logs: if you see normal commanded amps but abnormal FET temps, suspect hardware damage.
  3. Lower your current limits and thoroughly test again to avoid a complete blowout.

</details>

## 32. HIGH INDUCTANCE OR LOW INDUCTANCE MOTORS

<details>
<summary><strong>Q32. I hear about certain e-motorcycle hub motors having extremely high inductance, whereas small drone motors have very low inductance. How do I adapt?</strong></summary>

**Answer**

1. Observer Gain Adjust – For high-inductance motors, the default observer gain can be too high, causing overshoot. For very low inductance, you might need a higher gain. 
2. Current Controller KP/KI – The auto-detect might not be 100% accurate if the motor saturates. Sometimes manual tweaking is necessary if you see stuttering at certain speeds.
3. Switching Frequency – If the motor is extremely low inductance (like a small outrunner), raising your PWM to 30 kHz helps reduce ripple current.

</details>

## 33. TRACTION CONTROL FOR DUAL MOTORS

<details>
<summary><strong>Q33. Does VESC firmware offer any built-in traction control for dual-motor e-scooters or e-boards?</strong></summary>

**Answer**

- Yes, there’s a feature sometimes referred to as “Traction Control” or “TC,” which tries to keep motor speeds matched by limiting the difference in measured ERPM across the two wheels. 
- You must connect the two ESCs via CAN, set one as master and the other as slave, and enable the traction control feature. 
- Caveats:
  - It can reduce acceleration if one wheel is lightly loaded (like cornering).
  - Tuning the threshold is important so you don’t hamper normal turning.

</details>

## 34. LOGGING & ANALYSIS

<details>
<summary><strong>Q34. How can I best analyze or log VESC data for advanced tuning?</strong></summary>

**Answer**

1. RT Data in VESC Tool – Provides real-time graphs of current, duty, voltage, RPM, temperature. 
2. App Data Logging – Some forked or advanced VESC Tools allow exporting CSV logs. 
3. Metr Pro or Other Bluetooth Modules – Let you log to a phone app while riding. 
4. Key Metrics – Battery current, motor current, FET & motor temps, duty cycle. Watch for spikes or sudden throttling events.

</details>

## 35. MULTI-BATTERY CONFIGURATIONS

<details>
<summary><strong>Q35. I have two separate battery packs in parallel. Any special VESC settings for that?</strong></summary>

**Answer**

- In parallel, total capacity & discharge rating add up. So if each pack is 20A, you can set L_in_current_max to 40A total (assuming they share the same voltage). 
- Make sure the two packs are at similar voltage before paralleling, or you’ll get large balancing current. 
- Keep your cutoff voltages the same, but ensure both BMS are robust or consider using a single smart BMS that monitors the entire parallel set.

</details>

## 36. FIELD WEAKENING TIPS

<details>
<summary><strong>Q30. Any final best practices to avoid random faults or damage?</strong></summary>

**Answer**

1. Always do detection with the correct battery voltage available, not a half-charged bench PSU if possible. 
2. Check logs after a test ride. Look for peak battery amps, motor amps, mosfet & motor temps. 
3. Set gentle cutoffs (voltage, current, thermal) to avoid abrupt BMS or ESC-level fault cutouts. 
4. Use properly rated connectors (phase & battery) so you don’t melt them at high current. 
5. If running advanced features like MTPA or Field Weakening, do incremental tests in a safe area, watch for voltage spikes, and confirm it’s stable.

</details>

# 🏆 Continuing the Ultimate In-Depth VESC Q&A

Below are more advanced or niche questions (continuing from Q30), focusing on edge cases, specialty setups, and deeper parameter tuning. 


## 31. PARTIAL MELTDOWN OR “SOFT FAILURE”

<details>
<summary><strong>Q31. What if my ESC starts to smell or partially burn, yet I see no obvious short? Could it be a “soft failure”?</strong></summary>

**Answer**

- Sometimes MOSFETs or drivers degrade over time from repeated thermal or current spikes, resulting in partial conduction issues or higher Rds(on). 
- You might notice unusual heat at moderate current or see slight performance drop. 
- Steps:
  1. Inspect the MOSFETs for discoloration or bulges on any capacitor.
  2. Check real-time current logs: if you see normal commanded amps but abnormal FET temps, suspect hardware damage.
  3. Lower your current limits and thoroughly test again to avoid a complete blowout.

</details>

## 32. HIGH INDUCTANCE OR LOW INDUCTANCE MOTORS

<details>
<summary><strong>Q32. I hear about certain e-motorcycle hub motors having extremely high inductance, whereas small drone motors have very low inductance. How do I adapt?</strong></summary>

**Answer**

1. Observer Gain Adjust – For high-inductance motors, the default observer gain can be too high, causing overshoot. For very low inductance, you might need a higher gain. 
2. Current Controller KP/KI – The auto-detect might not be 100% accurate if the motor saturates. Sometimes manual tweaking is necessary if you see stuttering at certain speeds.
3. Switching Frequency – If the motor is extremely low inductance (like a small outrunner), raising your PWM to 30 kHz helps reduce ripple current.

</details>

## 33. TRACTION CONTROL FOR DUAL MOTORS

<details>
<summary><strong>Q33. Does VESC firmware offer any built-in traction control for dual-motor e-scooters or e-boards?</strong></summary>

**Answer**

- Yes, there’s a feature sometimes referred to as “Traction Control” or “TC,” which tries to keep motor speeds matched by limiting the difference in measured ERPM across the two wheels. 
- You must connect the two ESCs via CAN, set one as master and the other as slave, and enable the traction control feature. 
- Caveats:
  - It can reduce acceleration if one wheel is lightly loaded (like cornering).
  - Tuning the threshold is important so you don’t hamper normal turning.

</details>

## 34. LOGGING & ANALYSIS

<details>
<summary><strong>Q34. How can I best analyze or log VESC data for advanced tuning?</strong></summary>

**Answer**

1. RT Data in VESC Tool – Provides real-time graphs of current, duty, voltage, RPM, temperature. 
2. App Data Logging – Some forked or advanced VESC Tools allow exporting CSV logs. 
3. Metr Pro or Other Bluetooth Modules – Let you log to a phone app while riding. 
4. Key Metrics – Battery current, motor current, FET & motor temps, duty cycle. Watch for spikes or sudden throttling events.

</details>

## 35. MULTI-BATTERY CONFIGURATIONS

<details>
<summary><strong>Q35. I have two separate battery packs in parallel. Any special VESC settings for that?</strong></summary>

**Answer**

- In parallel, total capacity & discharge rating add up. So if each pack is 20A, you can set L_in_current_max to 40A total (assuming they share the same voltage). 
- Make sure the two packs are at similar voltage before paralleling, or you’ll get large balancing current. 
- Keep your cutoff voltages the same, but ensure both BMS are robust or consider using a single smart BMS that monitors the entire parallel set.

</details>

## 36. FIELD WEAKENING TIPS

<details>
<summary><strong>Q36. Any practical tips to keep Field Weakening safe on a mid-voltage setup (say 18S ~ 75V)?</strong></summary>

**Answer**

1. Moderate Current – Start with something like 5–10A of FW (foc_fw_current_max) and see how your top speed changes. 
2. Set foc_fw_duty_start around 0.90 or 0.92, so you only engage FW near the top-end. 
3. Battery Voltage Headroom – Keep l_max_vin at least 10V above your highest battery voltage. E.g., if your pack is 75.6V full, set max vin ~85–90V. 
4. Check Logs – If you see “Over Voltage” spikes or your FET temps climb unexpectedly, reduce the FW current or keep duty_start higher.

</details>

## 37. FOC_CC_DECOUPLING

<details>
<summary><strong>Q37. What does FOC_CC_DECOUPLING = ‘CROSS_BEMF’ do, and should I enable it?</strong></summary>

**Answer**

- Decoupling feeds forward cross-coupling terms between d/q axes to stabilize current control at changing speeds. 
- FOC_CC_DECOUPLING_CROSS_BEMF means it uses both cross-coupling and back-EMF feed-forward, making the current controller more responsive under quick acceleration. 
- It can help if you notice overshoot in current or if you want sharper throttle response. 
- Note: Slightly more noise can appear if your speed tracker or motor data aren’t accurate. Usually recommended for performance-driven setups.

</details>

## 38. CUSTOM FIRMWARES & FEATURES

<details>
<summary><strong>Q38. I see custom forks (e.g., for e-skate or big scooter hacks). Are these stable for daily use?</strong></summary>

**Answer**

- They often add specialized features like different throttle curves, advanced BLE modules, or locked parameters for certain scooters. 
- Stability depends on the developer. Some are well-tested, some are experimental. 
- If you rely on advanced features (like advanced BMS integration) and the fork supports it, that’s fine. Just watch for issues merging with main VESC updates.

</details>

## 39. PPM, ADC, OR UART CONTROL

<details>
<summary><strong>Q39. I’m hooking up a throttle via ADC. Any parameter specifics I must watch?</strong></summary>

**Answer**

1. App Settings – In VESC Tool, set “APP to use = ADC” or “ADC and UART,” etc.
2. Calibrate – The min and max voltage for the throttle to ensure 0-100% range.
3. Filter – You can add a small throttle ramp or filter to smooth out noise in analog signals.
4. Hall Throttle vs. Potentiometer – Some throttles are hall-based with ~1–4V output, others are purely resistive. Make sure your wiring and supply voltage match.
5. Input sources – VESC Tool can drive the scooter from the Balance app, UART remotes, or CAN clients even without a physical throttle; lock Bluetooth or power down when you walk away so nobody nearby rewrites settings mid-session.[^3]
6. Keyboard override – Desktop VESC Tool keeps the keyboard control toggle on the right side; enable it after detection before expecting WASD/arrow inputs to move the motor.[^4]

</details>

## 40. LACK OF SENSOR PORT ON SOME HARDWARE

<details>
<summary><strong>Q40. My ESC board lacks a dedicated sensor port, but I want hall sensor or encoder. Can I repurpose pins?</strong></summary>

**Answer**

- Potentially yes, if the hardware has extra ADC or digital inputs. This requires custom firmware or rewriting pin mappings in the code. 
- Some boards with limited pin resources sacrifice functionalities like UART or SWD to gain sensor inputs. 
- If you’re not comfortable editing firmware, you might add an external sensorless approach (like HFI) or find a hardware revision with a built-in sensor port.

</details>

## 41. PARALLEL CONTROLLERS (SHARED THROTTLE WITHOUT CAN)

<details>
<summary><strong>Q41. I want to run two VESCs on the same throttle signal but without CAN. Is that feasible?</strong></summary>

**Answer**

- Yes, you can physically split the ADC or PPM wire to both controllers. Each then does its own motor control. 
- But you lose traction control or combined telemetry. 
- Make sure each ESC has the correct “input app” config and the 5V supply lines from both ESCs might conflict; usually you share the ground and throttle signal, but only one 5V line from one ESC powers the throttle to avoid shorting 5V rails.

</details>

## 42. WHEN TO USE “HIGH CURRENT SAMPLING MODE”

<details>
<summary><strong>Q42. In FOC, there’s a param foc_current_sample_mode with ‘Longest Zero Time, All Sensors Combined, High Current.’ Which is best for big motors?</strong></summary>

**Answer**

- Longest Zero Time: Minimizes noise by choosing the two phases that get the longest sampling window, then calculates the third. 
- All Sensors Combined: Full 3-phase measurement but can be more sensitive to offset mismatch. 
- High Current: Derives the largest phase current from the two smaller measured ones, effectively enabling higher measurement range (about 15% more). 
- For big motors that exceed typical current ranges, “High Current” can be helpful, provided your hardware has 3 phase shunts and the code supports it.

</details>

## 43. STARTING IN NEUTRAL OR “BRAKE” MODE

<details>
<summary><strong>Q43. My e-scooter creeps forward slightly even at zero throttle. I want it to roll freely. Any parameter for that?</strong></summary>

**Answer**

- If you’re in current mode, check cc_min_current. If it’s e.g. 0.1A, that small current might produce a creep. 
- Also if “Short low side FETs on zero duty” is enabled, that can create a mild brake or hold. 
- You could switch to “open in zero duty” to freewheel. 
- Another possibility: your throttle calibration is off, so the ESC sees a small positive input.

</details>

## 44. FIRMWARE UPDATES & COMPATIBILITY

<details>
<summary><strong>Q44. I see the official VESC Tool says ‘firmware out of date’—should I upgrade or keep my vendor’s custom firmware?</strong></summary>

**Answer**

- If your hardware vendor uses a modified firmware (Flipsky, MakerX, etc.), upgrading to the official might lose certain hardware calibrations (like gate resistor offsets or custom DRV settings). 
- Generally, if they comply with the GPL, they should release the source. If they haven’t, you risk hardware misalignment by flashing the official. 
- If you trust the vendor’s custom FW is stable and it has the features you need, you can skip the official. If you want the latest VESC features or bugfixes, test carefully or see if the vendor has an updated fork.

</details>

## 45. ADVANCED TROUBLESHOOTING (“MY ESC GOES CRAZY AT MID SPEED”)

<details>
<summary><strong>Q45. I get random stutters or big current spikes around half throttle. How do I isolate the cause?</strong></summary>

**Answer**

1. Check detection – Possibly the flux linkage or observer gain is slightly off. 
2. Motor Saturation – Some motors saturate badly near certain current levels, messing with the observer. You can lower motor current or add small stator saturation compensation (foc_sat_comp). 
3. Switching Frequency – If your RPM is a multiple of the PWM frequency, you can get resonance. Try 5kHz higher or lower. 
4. Wiring/Connector – Vibrations at certain speed might loosen a bullet connector, causing brief open phases.

</details>

## 46. COMBINING MTPA & FIELD WEAKENING

<details>
<summary><strong>Q46. Can I run MTPA and FW together for maximum performance?</strong></summary>

**Answer**

- Yes, but it’s fairly advanced. MTPA is about optimizing torque below base speed, while FW extends speed above base speed. 
- Ensure your difference between Ld and Lq is set. Negative d-current from MTPA plus the additional negative d-current for FW can cause large phase angles, so watch bus voltage. 
- Typically you set MTPA to “IQ Target” and moderate FW up to maybe 20–30A, verifying no overshoot.

</details>

## 47. SMALL ESC CONFIGS (LOW VOLTAGE, E.G., 24V)

<details>
<summary><strong>Q47. I’m only using a 24V supply. Do I just reduce all voltage cutoffs proportionally?</strong></summary>

**Answer**

- Yes. If it’s 6S LiPo (25.2V max), you might set L_battery_cut_start ~21V, L_battery_cut_end ~19V or so. 
- Also watch the default L_max_vin ~57V might be fine, but you can keep it if you have no reason to lower it. 
- The main difference is your top speed is limited if your motor’s KV is set for higher voltage. Ensure the flux linkage detection is done at your actual supply.

</details>

## 48. HARDWARE LIMITS & SHUNTS

<details>
<summary><strong>Q48. Why does some hardware claim 200A but the VESC Tool only shows 100A capability?</strong></summary>

**Answer**

- Possibly the hardware vendor used shunts or an amplifier stage that saturates at ~100A in standard code. 
- They might advertise 200A “peak” or for short bursts, or they rely on a custom scale that the official VESC Tool doesn’t read. 
- If you exceed the actual measured limit, you risk either abs_over_current faults or inaccurate current readings leading to meltdown. 
- Usually trust the official detection results or re-scale the shunt if you have the real hardware specs.

</details>

## 49. PWM MODE: BIPOLAR?

<details>
<summary><strong>Q49. We see a param ‘pwm_mode’ can be ‘Nonsynchronous HISW, Synchronous, Bipolar.’ When is Bipolar used?</strong></summary>

**Answer**

- Bipolar is a less common driver approach, typically for lab or older industrial BLDC drivers. 
- Modern VESC hardware rarely uses it as Synchronous is more tested. 
- If you set it accidentally, you might see weird conduction overlap or unusual heat. 
- Unless your vendor hardware specifically instructs “Bipolar,” stick to synchronous.

</details>

## 50. FINAL BEST PRACTICES

<details>
<summary><strong>Q50. Summarize best practices for advanced users who constantly push the edge of VESC capabilities.</strong></summary>

**Answer**

1. Monitor real-time logs – Always keep an eye on spikes in battery current, motor current, and bus voltage. 
2. Thermal headroom – Provide extra heatsinking or active cooling if you run at or near hardware limits. 
3. Tune carefully – If you do MTPA + FW, or fancy decoupling modes, test in small increments. 
4. Solder & connector reliability – At high amps, a single bad joint can lead to meltdown. Use quality bullets or AS150 for battery leads. 
5. Use the full sensor suite – If your motor has thermistors, use them. If your battery has a CAN-based BMS, integrate it for smooth limiting. 
6. Stay updated – Keep an eye on new VESC Tool releases or stable vendor forks that fix known issues. 
7. Physical checks – Vibrations, wire chafing, or water ingress can cause random faults. Protect your wiring thoroughly.

</details>

# 50 Additional High-Quality VESC Q&A

Below are 50 more advanced or practical questions with in-depth responses, covering niche scenarios, best practices, and technical tips. Each question includes a detailed explanation that builds on the knowledge from previous Q&A segments.


## 1. FOC Current KP/KI Manual Tuning

<details>
<summary><strong>Q1. How do I manually tune `foc_current_kp` and `foc_current_ki` if detection results feel unstable?</strong></summary>

**Answer**

- Symptoms: If detection gave you, e.g., KP = 0.03 and KI = 20, but you see overshoot or audible chatter, you can systematically reduce KP by ~20% increments until the stuttering lessens.
- Method:
  1. Test ride on flat ground, accelerate from 0–50% throttle, watch for stutter or squeal.
  2. If stable, push 75%–100% throttle. If abrupt surges or oscillations, keep halving KP.
  3. After stable KP, raise KI in small steps to restore torque tracking; too low KI leads to sluggish current ramp.

- Watch Temps: Overly high KI can cause big current spikes at transitions.

</details>

## 2. Motor Has Multiple Winding Options

<details>
<summary><strong>Q2. My motor is offered in 6T, 8T, 10T windings. How does that affect VESC config?</strong></summary>

**Answer**

- The winding changes the motor’s KV and thus the flux linkage. Higher turns (10T) → lower KV → higher torque/amp, lower top speed. 
- FOC detection should measure these differences automatically, but your maximum speed and required field weakening might vary.
- If you choose 6T (faster KV), you might need more battery voltage or field weakening for top-end. If you choose 10T, you get stronger low-speed torque but lower speed.

</details>

## 3. High-Speed Drones or eJets

<details>
<summary><strong>Q3. I’m using VESC for a high-speed EDF (Electric Ducted Fan) drone. Any particular settings?</strong></summary>

**Answer**

- Very Low Inductance: Raise PWM frequency (up to 30 kHz) to reduce current ripple. 
- Observer Gains: Large motors spinning tens of thousands of RPM might need adjusting foc_observer_gain. 
- Phase Filter: If available, disabling it at high ERPM might be wise, or set foc_phase_filter_max_erpm lower. 
- Cooling: Ensure consistent airflow over the ESC or use additional heat sinking.

</details>

## 4. “Memory Overflows” or CPU Overload

<details>
<summary><strong>Q4. Could advanced features (like dual FOC at 30 kHz on older hardware) overload the MCU?</strong></summary>

**Answer**

- Possibly. Some older STM32F4 boards have limited overhead. 
- If you run high sample modes + MTPA + logging, the CPU load can spike → missed interrupts or odd behavior. 
- Solution: Lower the switching freq to 20 kHz, reduce logging speed, or disable extra features like “Sample in V0 & V7.” 
- If you need it all, consider hardware with a faster MCU.

</details>

## 5. Overvoltage on Rapid Deceleration in Race Scooters

<details>
<summary><strong>Q5. My race scooter with 24s battery sees 100 V on the bus if I brake from high speed. Any safety tips?</strong></summary>

**Answer**

- Ensure L_max_vin > your highest voltage spike. For 24s nominal ~ 88.8 V full, you might set 110 V max. 
- Use moderate regen current or add a small external brake resistor if your BMS can’t handle it. 
- If you see frequent “Abs Overvoltage” faults, either you reduce the regen or accept less abrupt braking from top speed.

</details>

## 6. Rapid-Fire Throttle Inputs

<details>
<summary><strong>Q6. I do stunts or trick riding. Rapid throttle changes cause occasional cutouts. Adjustments?</strong></summary>

**Answer**

- Throttle Ramp: Increase ramp time in “Current control” or “Duty control” so the ESC doesn’t see insane steps. 
- Slow ABS Current: Minimizes cutouts from short spikes. 
- Check Battery: If BMS triggers from sudden >C bursts, you’ll get cutouts. Might need bigger battery or a BMS with higher peak rating.

</details>

## 7. ADC vs. PPM Throttle Curves

<details>
<summary><strong>Q7. Does it matter if I use an ADC throttle vs. a PPM remote in terms of power delivery?</strong></summary>

**Answer**

- Internally, VESC just sees an input from 0–100% after calibration. 
- PPM (RC servo signals) is typical in e-skates with handheld remotes. 
- ADC is common for scooters with a hall or pot-based throttle. 
- Setting “Throttle curve exponent” is possible for both, giving a gentler or more aggressive mid-throttle. 
- The choice is about hardware convenience, not raw performance difference.

</details>

## 8. Common Pitfall: Using the Wrong Hardware Version in Tool

<details>
<summary><strong>Q8. I flashed the firmware for v4.12 onto a v6-based ESC. Now it’s bricked. What next?</strong></summary>

**Answer**

- You must pick the correct hardware (e.g., “75_300,” “60_200,” “HW4.xx,” “HW6.xx”). 
- If bricked, you typically need an SWD programmer or STLink to unbrick the MCU at a lower level. 
- Always check the manufacturer’s recommended firmware ID.

</details>

## 9. Inconsistent Hall Readings

<details>
<summary><strong>Q9. At higher speeds, I see random hall sensor dropouts. Is that normal?</strong></summary>

**Answer**

- Possibly the hall wires are picking up noise or the sensor board saturates at high RPM. 
- Some motors use older halls that fail at high electrical frequency. 
- Mitigations:
  1. Add shielding or twisted pairs on hall cables.
  2. Reduce pull-up resistor if the signals are too slow.
  3. Switch to sensorless at high ERPM with “Hybrid” mode.

</details>

## 10. VESC BMS Min/Max Cell Voltage Balancing

<details>
<summary><strong>Q10. If I set bms.vmin_limit_start=3.0 V, bms.vmin_limit_end=2.8 V, how does the ESC respond?</strong></summary>

**Answer**

- As the BMS reports any cell hitting 3.0 V, the ESC gradually reduces battery current. 
- If a cell hits 2.8 V, the ESC disallows further motor load (or triggers a fault). 
- It’s a safer approach than a sudden BMS cutoff, distributing load-limiting earlier. 
- Must ensure the BMS can broadcast accurate cell data.

</details>

## 11. Pushing Motor beyond its Nameplate Voltage

<details>
<summary><strong>Q11. If a motor is rated 48 V, can I run it at 60 V with a VESC?</strong></summary>

**Answer**

- Mechanically yes, but it spins proportionally faster (KV × voltage). You risk structural or bearing overspeed. 
- Thermally, you can saturate the motor if you push too high current. 
- If you keep current in check and physically the motor can handle the RPM, it’s possible. 
- Just watch for excessive back-EMF if you do field weakening near top speed.

</details>

## 12. Overcurrent on Startup in Sensorless Mode

<details>
<summary><strong>Q12. I get “ABS_OVER_CURRENT” if I punch throttle from zero in sensorless. Why?</strong></summary>

**Answer**

- Sensorless at zero speed is tricky: the ESC initially uses open loop. If the rotor isn’t matched, current can spike before the observer locks.
- On dual drives you can let the sensored wheel push first.
  - tune VSS/HFI so the sensorless motor joins once rolling, or script a PWM disable below a set ERPM if rewiring halls is impractical.[^5]
- Fix: Slight ramp or “foc_sl_openloop_time” to avoid big slam.
- Or use HFI/halls for immediate lock.
- Lower l_abs_current_max or enable slow_abs_current to reduce false triggers.

</details>

## 13. Step-by-Step Hall Table Editing

<details>
<summary><strong>Q13. My detection gave weird hall table: [255, 3, 5, 6, 4, 2, 255, 1]. How do I fix it manually?</strong></summary>

**Answer**

- You can manually edit hall_table__x in VESC Tool if you see a repeated 255 or out-of-sequence. 
- Typically, each unique combination of hall states (1–6) must map to the correct commutation step. 
- If the motor runs backward or stutters, reorder them so the progression is logical. Or invert direction if the sequence is reversed.

</details>

## 14. Motor “Hooting” or “Growling” at Mid Speed

<details>
<summary><strong>Q14. I hear a mid-speed resonance. Is it hardware layout or software timing?</strong></summary>

**Answer**

- Could be a mechanical resonance in the stator. FOC might pass certain frequency components. 
- Sometimes changing switching frequency by a few kHz moves the resonance outside your typical speed range. 
- Check if it’s still there under heavier or lighter load. Possibly normal mechanical noise.

</details>

## 15. Running Outrunner Motors in E-Bike Conversions

<details>
<summary><strong>Q15. I took a hobby outrunner, put it on an e-bike. Any unique VESC concerns?</strong></summary>

**Answer**

- Typically outrunners have lower voltage (~8–12S) but want high current. 
- Use high current shunts or a VESC with robust FETs, e.g., 75_200 for overhead. 
- Outrunner with sensorless can have start-up torque issues on a bike. 
- Might add hall sensors or rely on HFI for decent hill starts.

</details>

## 16. Multi-Polarity: “Motor Poles” Mismatch

<details>
<summary><strong>Q16. What if I set si_motor_poles incorrectly, e.g., 7 instead of 14?</strong></summary>

**Answer**

- This only affects speed calculations (ERPM vs mechanical RPM) and distance-based metrics (odometer). 
- The control loop in FOC uses actual measured flux, not the user’s “pole count.” 
- So your speed readout or tracking might be half or double. 
- For BLDC sensor-based commutation, it might mess up the tach readings.

</details>

## 17. Water Damage or Corrosion

<details>
<summary><strong>Q17. If my board got soaked, do VESC parameters matter or is it purely hardware damage?</strong></summary>

**Answer**

- If the PCB or connectors corroded, no parameter fix can help; you need to clean or replace. 
- Water can short sensor signals, causing random hall transitions or ephemeral faults. 
- Even after drying, residue left behind can keep signals misfiring. Thoroughly isopropanol-clean the board. 
- Then retest or re-run detection if sensor readings changed.

</details>

## 18. Belt vs. Hub vs. Direct Drive

<details>
<summary><strong>Q18. Do I set different VESC parameters for a belt drive e-skate vs. a direct drive?</strong></summary>

**Answer**

- Mechanically, they differ in gear ratio. So set si_gear_ratio to reflect pulley ratio, ensuring correct speed readouts. 
- The rest (FOC, current, etc.) depends on the motor specs, not the drive method. 
- If the belt is geared, you can run higher motor RPM with less motor torque needed for the same wheel torque.

</details>

## 19. “FOC Sample in V0 and V7 Interpolation”

<details>
<summary><strong>Q19. Does enabling V0+V7 Interpolation significantly improve performance or just reduce noise?</strong></summary>

**Answer**

- It can help at high speeds so the observer sees effectively double sampling, improving angle tracking. 
- For typical e-scooters <100 eKRPM, the difference might be subtle. 
- Main advantage: smoother wave output, less distortion, but higher CPU usage. 
- If your hardware is stable, it’s often beneficial.

</details>

## 20. Motor Overtemp Behavior vs. MOSFET Overtemp

<details>
<summary><strong>Q20. Is it possible that the motor overheats but the ESC remains cool or vice versa?</strong></summary>

**Answer**

- Absolutely. The motor and ESC have separate thermal paths. 
- If you have a big ESC with a heatsink but a small motor, you’ll hit motor thermal cut first. 
- Conversely, a big motor with small ESC leads to FET or driver overheating first. 
- Setting l_temp_motor_xxx and l_temp_fet_xxx properly helps each side avoid meltdown.

</details>

## 21. BMS Communication Intermittent

<details>
<summary><strong>Q21. I get BMS data half the time, sometimes the ESC doesn’t see it. Solutions?</strong></summary>

**Answer**

- Possibly a CAN wiring issue or RS485 if a special BMS. 
- Use twisted-pair data lines, verify correct termination resistor (120 Ω). 
- Check if your BMS has a stable 5 V or 3.3 V domain for the transceiver. 
- If the data is partial, the ESC might revert to default battery-limits or throw BMS faults. Look at logs to confirm.

</details>

## 22. Inductive Spikes from Long Motor Cables

<details>
<summary><strong>Q22. I have 1.5 m motor cables. Any special caution about cable inductance or voltage spikes?</strong></summary>

**Answer**

- Long wires can raise voltage ringing at the MOSFETs if not well damped. 
- Consider adding small LC filters or snubbers at the ESC output if you see high spikes. 
- Keep cables twisted or together to reduce inductance. 
- Lower your switching speed (some advanced ESCs can tweak gate driver slew) if hardware allows.

</details>

## 23. Current Scaling with l_current_max_scale

<details>
<summary><strong>Q23. Can I set l_current_max_scale dynamically via app for eco vs. sport mode?</strong></summary>

**Answer**

- Yes, if your firmware or front-end supports reading an input to scale it. Typically you can do “profiles” in VESC Tool. 
- Eco mode: scale ~0.5 → half motor current. Sport: scale=1.0 → full. 
- Some advanced e-bikes or scooters implement a handlebar switch to send a CAN command adjusting that scale.

</details>

## 24. High-Voltage (e.g., 20S–30S) and Capacitor Modules

<details>
<summary><strong>Q24. At 100 V, do I need extra bulk capacitance beyond stock ESC?</strong></summary>

**Answer**

- Possibly yes. The internal bus caps might be sized for 60–75 V typical. At 100 V, voltage ripple & transient demands are bigger. 
- If your ESC manufacturer suggests an external “cap bank,” use it. 
- Keep battery leads short to reduce line inductance. 
- Check the recommended “peak current rating” for the internal caps; exceeding it can cause them to overheat or fail.

</details>

## 25. Unusual Throttle Dead-Zone

<details>
<summary><strong>Q25. I see ~25% dead-zone at the start of my throttle. Where to fix that?</strong></summary>

**Answer**

- In VESC Tool → App → ADC or PPM config, calibrate the input range. Possibly your physical throttle outputs ~1.2–2.5 V but the ESC expects 0.8–3.2 V. 
- Adjust “Min Voltage” or “Pulsewidth Start.” 
- For PPM, set the servo min to a smaller microsecond value if the remote has a short range. 
- If you want a smaller dead-band near zero, reduce “center” offset or the “positive ramp” start.

</details>

## 26. Overtemp Ramp vs. Fault

<details>
<summary><strong>Q26. What’s the difference if I set l_temp_fet_start=80, l_temp_fet_end=90 vs. a bigger range like 80–110?</strong></summary>

**Answer**

- The controller linearly throttles current from 80°C to 90°C in the first scenario, and fully faults at 90. 
- In the second scenario, you get a broader slope—less aggressive cut at the same 80°C start, but you don’t fully cut out until 110°C. 
- The bigger range means you keep more performance in mid temps but risk pushing the FETs dangerously high near 110.

</details>

## 27. Fine-Tuning Position Controller Gains

<details>
<summary><strong>Q27. I’m using position PID for a CNC-like setup. How do I keep it from overshooting?</strong></summary>

**Answer**

- Start with low p_pid_kp, zero p_pid_ki, small p_pid_kd. 
- Increase kp until you get near the desired position quickly but not excessive overshoot. 
- Add kd_filter to damp any overshoot. 
- Then add small ki to remove steady-state error if the motor stops short of the target under load.

</details>

## 28. Multi-Motor Vehicles (4 WD e-scooter, for example)

<details>
<summary><strong>Q28. Do I set each motor’s battery current to 1/4th total or keep each at full?</strong></summary>

**Answer**

- If your battery is 100 A total, four ESCs means ideally each is ~25 A for stable operation if all can run full.
- In reality, some do keep each at 100 A because it’s unlikely all four motors pull max simultaneously, but that can be risky.
- You might do partial offset: 50 A each, to not exceed 200 A total if two motors heavily load. Understand your BMS and acceptance of risk.
- Remember that a single VESC cannot run two motors simultaneously.
  - plan one controller per hub plus CAN (or another coordination layer) for multi-motor vehicles.[^6]

</details>

## 29. “Motor Loss Torque” in Motor Config

<details>
<summary><strong>Q29. There’s a param motor_loss_torque in some firmware. What is that?</strong></summary>

**Answer**

- It’s an approximate torque constant for friction or iron/copper losses at no load. The tool can estimate efficiency or do advanced calculations. 
- Rarely used in basic rides. Mostly for advanced data or “motor comparison” features. 
- If you measure the no-load current at a certain RPM, you can estimate the loss torque. Not crucial for most user setups.

</details>

## 30. Using A Very Low KV Motor Without FW

<details>
<summary><strong>Q30. If my motor is low KV (like 60 KV on 48 V), do I need field weakening?</strong></summary>

**Answer**

- Possibly no. A low KV means you already have headroom to reach top speed within that voltage. 
- Field weakening is primarily for high KV motors limited by back-EMF. 
- If your max speed is still under or near the mechanical limit, you can skip FW. 
- If you do want ~5–10% extra speed, small FW might help, but watch for minimal benefit if your motor is truly low KV.

</details>

## 31. Motor Feels “Weak” at Partial Throttle

<details>
<summary><strong>Q31. I get strong top speed, but from 20–40% throttle it’s quite dull. Where to check?</strong></summary>

**Answer**

- Possibly a throttle curve is set to “Exponential negative,” flattening mid-range. 
- In VESC Tool → Input → Throttle curve, ensure it’s neutral or standard. 
- Also check if “Battery Current Max” is too low, capping torque until duty is higher. 
- Or if motor is saturating at mid current (rare, but possible). Try raising l_current_max or verifying detection.

</details>

## 32. Unexpected Reverse

<details>
<summary><strong>Q32. Occasionally my motor attempts a quick spin backwards after stopping. Is it a sensor glitch?</strong></summary>

**Answer**

- Could be random hall sensor noise or observer error near 0 ERPM. 
- If you’re in sensorless or HFI, the rotor angle might slip 180°. 
- Solutions: 
  1. Slight openloop ramp at near 0 speed. 
  2. Ensure no negative throttle commands from your input method (like a slight center offset in PPM). 
  3. Hall sensor shielding or better connectors.

</details>

## 33. PWM Deadtime Variation

<details>
<summary><strong>Q33. If my hardware’s recommended deadtime is 100 ns, but default is 120 ns, do I need to fix it?</strong></summary>

**Answer**

- Typically the difference is small. 120 ns is safer but might have slightly more conduction distortion. 
- If you want every bit of efficiency, set foc_dt_us accordingly. 
- Don’t go lower than your FET driver’s recommended deadtime or you risk shoot-through.

</details>

## 34. Ultra-Low Speed Control for Robotics

<details>
<summary><strong>Q34. I want extremely smooth 1–2 RPM movement for a robot arm. Is VESC suitable?</strong></summary>

**Answer**

- Yes, with a stable sensor (hall or encoder). Sensorless alone at 1–2 RPM can be tricky unless the motor has large saliency for HFI. 
- In “FOC encoder” mode, you can do precise position or speed loops. 
- Tuning p_pid_xxx or s_pid_xxx carefully for slow speeds is crucial. 
- Also ensure the motor has enough gear reduction so it’s not trying to produce big torque at near zero speed just by FOC alone.

</details>

## 35. NTC 100k vs. PTC 1k in Motor Temp

<details>
<summary><strong>Q35. My motor data says it has a KTY84 sensor. Which param do I pick for m_motor_temp_sens_type?</strong></summary>

**Answer**

- That’s typically “KTY84/130” in the “Motor Temperature Sensor Type” drop-down. 
- A 10k NTC or 100k NTC is different. So choosing the correct sensor ensures correct temperature readout. 
- If your motor is mislabeled or uncertain, measure the sensor’s resistance at known temps or consult the motor manufacturer.

</details>

## 36. “I2T” Thermal Modeling

<details>
<summary><strong>Q36. Does VESC implement an I2T (time-based current) limit for motors?</strong></summary>

**Answer**

- Some custom forks or advanced features have partial “I2T” thermal models. Official firmware mainly does direct temp-based limiting. 
- If you want I2T, you either do a custom code or rely on battery & motor real-time temps. 
- Alternatively, set a moderate continuous current and allow short bursts well above that if your hardware can handle short intervals.

</details>

## 37. Kelly or Sabvoton vs. VESC

<details>
<summary><strong>Q37. If I have a bigger brand controller (Kelly, Sabvoton) for e-motorcycles, what do I gain by switching to a VESC?</strong></summary>

**Answer**

- VESC is fully programmable with open firmware, advanced sensorless/HFI, MTPA, field weakening. 
- Often more precise torque control at low speed, plus robust logging. 
- Kelly and Sabvoton can be simpler or locked. But if you want maximum tunability, VESC might be superior. 
- Downside: you must do more manual parameter work.

</details>

## 38. Low Battery Voltage but High Phase Current

<details>
<summary><strong>Q38. I only have a 36 V battery, can I still push 100 A motor current?</strong></summary>

**Answer**

- Yes, at partial duty you can have big phase current. For instance, 36 V × 50 A battery = 1800 W, but if the motor is spinning slowly with 10 V on the phases, you can have 100 A phase = 1000 W. 
- The limiting factor is your ESC’s FET and hardware capacity. 
- Motor torque is primarily phase current. Battery power is limited by battery voltage × battery current.

</details>

## 39. Limit Start vs. End Ratios

<details>
<summary><strong>Q39. What if l_erpm_start=0.7 for the ERPM limit, or l_duty_start=0.8 for duty limit—does that create a ‘double soft cap’?</strong></summary>

**Answer**

- Potentially yes. The ESC will reduce current if either the duty or ERPM is near the set fraction. 
- If you set both to around 0.7 or 0.8, you might get an earlier “soft cap.” 
- Typically pick one (duty or ERPM) if you want a single method to limit top speed. Using both can cause layered or more complicated limiting.

</details>

## 40. Acceleration Temperature Decrease Tweak

<details>
<summary><strong>Q40. If I set l_temp_accel_dec=0.5, how does that help preserve braking?</strong></summary>

**Answer**

- This param reduces the ESC’s effective “end temperature” by 50% during acceleration. 
- Meaning if you allow 100 °C under braking, it might treat it as 75–80 °C limit while accelerating. So the ESC doesn’t push the FETs as hot in acceleration, leaving headroom for braking events. 
- Good for downhill or race usage, ensuring you have safe braking margin.

</details>

## 41. Diagnosing “ABS Current” vs. “DRV Fault” vs. “MOSFET Shorted”

<details>
<summary><strong>Q41. How to interpret the fault code differences?</strong></summary>

**Answer**

- ABS Over Current: The software fault triggered from current sense.
- DRV Fault: The DRV chip signaled an overcurrent or under/overvoltage condition.
- MOSFET Short or Gate Driver Error: Usually results in immediate destructive fault—ESC might not just code an error but physically fail.
- For repeated DRV fault, suspect hardware or config mismatch. For repeated ABS Over Current, adjust or slow down current ramp.
- Once wiring and observers check out, lift `l_abs_current_max` (and optionally disable the slow ABS filter) so transient phase spikes stop tripping the controller mid-launch.[^7]

</details>

## 42. “Battery Voltage Too Low” but BMS is Fine

<details>
<summary><strong>Q42. At half throttle, I see input voltage briefly sag below l_min_vin, then fault. Fix?</strong></summary>

**Answer**

- Possibly your battery has high internal resistance or your leads are too thin. Voltage sags under load. 
- Lower l_min_vin to maybe 6–8 V if you’re sure your system can handle that, or reduce battery current to reduce sag. 
- Improving battery or wiring is recommended. The fault is telling you the supply can’t sustain that draw.

</details>

## 43. Legacy 4.xx + Field Weakening?

<details>
<summary><strong>Q43. Is FW recommended on older 4.12-based hardware?</strong></summary>

**Answer**

- Often discouraged if you push near the hardware’s voltage limit. The DRV8302 can be fragile with voltage spikes. 
- If you do attempt it, keep a small margin.
- A 4.12 at 12S is safer for FW than 4.12 at 14 or 16S.
- Many prefer a 6-based hardware or higher voltage rating for stable FW.
- Trampa’s legacy VESC MK6 firmware effectively caps the platform at 12 S.
  - 13 S experiments killed braking outright, forcing riders back onto low-power Xiaomi hubs until they sourced modern controllers.[^8]

</details>

## 44. Random Motor Reverse at High Speed?

<details>
<summary><strong>Q44. I’ve read about motors flipping direction momentarily. How does that happen?</strong></summary>

**Answer**

- Usually an observer or sensor reading glitch that thinks the rotor angle is ~180° off. The ESC can produce torque in the reverse direction. 
- This can be catastrophic. 
- Solutions: stable sensor or a robust sensorless approach. Possibly limit the max phase amps or check the “HFI Ambiguity Resolve” mode if you use HFI.

</details>

## 45. “FOC Sat Comp” for Hard-Loaded Motor

<details>
<summary><strong>Q45. How to pick a good foc_sat_comp for big direct-drive hub?</strong></summary>

**Answer**

- If your motor saturates heavily near max phase current, start with ~0.1–0.2. 
- If you see stutter under full load from standstill, you might raise it up to 0.3–0.5. 
- Don’t exceed ~0.15–0.2 unless you have serious data or you risk messing observer. 
- Observe if it helps reduce cogging under load.

</details>

## 46. Unusual “Input Latency” on Throttle

<details>
<summary><strong>Q46. I press throttle but there’s a 1–2 second delay. Why?</strong></summary>

**Answer**

- Possibly a large “positive ramp” time in the input settings. 
- Or “Cruise control” logic set incorrectly. 
- If BMS is limiting current or the motor is near temp limit, the ESC might obey that limit → feels delayed. 
- Check real-time for “Temp limiting” or “Over current limiting.”

</details>

## 47. Resistive Spot Welding Using VESC?

<details>
<summary><strong>Q47. Can I hack a VESC to do battery spot welding?</strong></summary>

**Answer**

- Some experimenters try using a motor phase output as a high-current pulse, but it’s not recommended. 
- The firmware isn’t designed for single large DC pulses with near-short conditions. You might blow MOSFETs or the bus capacitors. 
- Dedicated welders or a specialized approach is safer. VESC is for controlling rotating motors, not literal short pulses.

</details>

## 48. Using a Gimbal Motor

<details>
<summary><strong>Q48. Is VESC overkill for a low-power gimbal motor?</strong></summary>

**Answer**

- Possibly. Gimbal motors often want extremely low torque, high resolution, might not need high current or commutation frequencies. 
- VESC can do it if you run FOC with an encoder or sensorless if it’s feasible. 
- The advantage is you get advanced config, but a specialized gimbal driver might be simpler.

</details>

## 49. Modulating Regen Strength by Throttle

<details>
<summary><strong>Q49. I want a separate lever or half-throttle for adjustable e-brake. How to set that up?</strong></summary>

**Answer**

- You can configure “ADC2” for braking input if your hardware has it. 
- Then the firmware can interpret negative current commands from that lever, controlling l_in_current_min up to your chosen max. 
- A dedicated e-brake handle is possible. Some advanced e-scooter builds do that, or use “dual throttle” config in the code.

</details>

## 50. Fast-Swapping Motors or Wheels

<details>
<summary><strong>Q50. I have multiple wheel sizes or motors. Do I have to re-detect each time I swap them?</strong></summary>

**Answer**

- If they’re drastically different motors or windings, yes, you should do a detection or load a saved config specific to that motor.
- If it’s the same motor but just a different wheel diameter, you mainly update si_wheel_diameter for correct speed reading.
- Always label or store config XML for each motor type so you can quickly switch in VESC Tool.

</details>

## Source Notes

[^1]: Sensorless FOC riders still need a push start or intensive HFI tuning to avoid low-speed stalls on Flipsky/MakerX hardware.[^9]
[^2]: “Bad FOC hall detection” investigations traced launch issues to failed hall boards that forced riders toward HFI until the sensors were replaced.[^10]
[^3]: Effective sensorless launches hinge on at least ~15 % Ld/Lq separation so HFI can lock reliably.[^11]
[^4]: Vedder’s FW 6.0 45° V0/V7 HFI profile delivers repeatable hall-less zero starts when the ESC samples both zero vectors at high frequency.[^12]
[^5]: VESC Tool 6.02 widens hall hysteresis, calms sampling noise, and improves CAN logging, making silent HFI practical on phase-shunt controllers.[^13]
[^6]: Builders continue to iterate on hall-less tunes by combining HFI, saturation compensation, and trimmed start currents before trusting premium scooters without sensors.[^14]
[^7]: Riders differentiate Vedder Sensorless Start from continuous HFI.
  - VSS injects a short burst, requires temperature inputs, and then hands control back to the observer.[^15]
[^8]: Hub-motor MTPA trials showed surface-magnet commuters mostly generate heat, whereas saliency-rich motors benefit once settings are logged carefully.[^16][^17]
[^9]: Blade hub owners log ~6 kW per motor and ~20 km/h extra top speed at 15–17 S when MTPA is dialed with ~250 A phase headroom.[^18]
[^10]: Stacking MTPA and heavy field weakening on 20 S Spintend 85150 builds has blown MOSFETs, so veterans now demand upgraded silicon or milder tunes.[^19]
[^11]: Dual-motor commuter logs captured only ~8 km/h gain from field weakening while power draw nearly doubled, reinforcing that gearing or voltage changes are more efficient.[^20]
[^12]: Racers chasing 30 A+ of FW reported hubs overheating despite traction control, prompting airflow, ferrofluid, or stator upgrades before lifting FW ceilings.[^21][^22]
[^13]: Daly and ANT BMS boards can hard-cut during regen, back-feeding controllers unless the ESC tapers current first.[^23][^24]
[^cutoff_stages]: Paolo clarified that Stage 1 tapering simply soft-limits output while Stage 2 halts motor drive but leaves the controller powered, letting riders set software cutoffs slightly under BMS limits if they continue monitoring pack voltage.[^25]
[^14]: Swapping thick stock pads for thin interfaces or paste and clamping the case to metal keeps Ubox/Makerbase controllers from spiking past 80 °C immediately.[^26]
[^15]: Community thermal guidelines keep MOSFET cases under ~70 °C for daily riding and flag sustained 85 °C spikes as a sign to cut current or improve cooling.[^27]
[^16]: Race telemetry targets ≤45 °C controller cases and ≤90–100 °C stators to avoid demagnetizing hubs or cooking controllers during long pulls.[^28]
[^17]: Installing EPCOS/TDK 2 × 4 mm NTCs at the hall bundle provides accurate 150 °C-capable stator telemetry for VESC cutbacks.[^29]
[^18]: Poorly routed sensor leads collapse above 80 A; rerouting and shielding stop thermistor signals from dropping out under load.[^13]
[^19]: Paolo and others log CAN-connected smart BMS data to capture true pack power because VESC low-side shunts under-report at high output.[^30]
[^20]: Daly/ANT packs have latched off mid-ride from regen spikes, so crews rely on ESC-side limit modes to taper current before the BMS hard-cuts.[^23][^24]
[^21]: Smart-BMS telemetry can drop frames or drift; builders recalibrate sensors and inspect boards for damage when CAN data suddenly zeros out.[^31][^32]


## References

[^1]: Source: knowledge/notes/input_part012_review.md†L14-L14
[^2]: Source: knowledge/notes/input_part009_review.md†L100-L100
[^3]: Source: knowledge/notes/input_part009_review.md†L80-L80
[^4]: Source: knowledge/notes/input_part009_review.md†L83-L83
[^5]: Source: knowledge/notes/input_part011_review.md†L540-L542
[^6]: Source: data/vesc_help_group/text_slices/input_part009.txt†L12486-L12489
[^7]: Source: knowledge/notes/input_part009_review.md†L82-L82
[^8]: Source: knowledge/notes/input_part001_review.md†L85-L85
[^9]: Source: knowledge/notes/input_part009_review.md†L80-L87
[^10]: Source: knowledge/notes/input_part013_review.md†L113-L135
[^11]: Source: knowledge/notes/input_part000_review.md†L377-L381
[^12]: Source: knowledge/notes/input_part003_review.md†L221-L224
[^13]: Source: knowledge/notes/input_part004_review.md†L49-L55
[^14]: Source: knowledge/notes/input_part012_review.md†L229-L232
[^15]: Source: knowledge/notes/input_part001_review.md†L304-L307
[^16]: Source: knowledge/notes/input_part007_review.md†L235-L239
[^17]: Source: knowledge/notes/input_part008_review.md†L114-L114
[^18]: Source: knowledge/notes/input_part001_review.md†L228-L229
[^19]: Source: knowledge/notes/input_part014_review.md†L21-L22
[^20]: Source: knowledge/notes/input_part003_review.md†L205-L205
[^21]: Source: knowledge/notes/input_part009_review.md†L178-L179
[^22]: Source: knowledge/notes/input_part013_review.md†L783-L788
[^23]: Source: knowledge/notes/input_part000_review.md†L372-L380
[^24]: Source: knowledge/notes/input_part014_review.md†L98-L101
[^25]: Source: knowledge/notes/input_part014_review.md†L173-L173
[^26]: Source: knowledge/notes/input_part008_review.md†L547-L548
[^27]: Source: knowledge/notes/input_part007_review.md†L198-L202
[^28]: Source: knowledge/notes/input_part014_review.md†L75-L76
[^29]: Source: knowledge/notes/input_part004_review.md†L69-L70
[^30]: Source: knowledge/notes/input_part014_review.md†L80-L82
[^31]: Source: knowledge/notes/input_part014_review.md†L82-L83
[^32]: Source: knowledge/notes/input_part014_review.md†L100-L101
