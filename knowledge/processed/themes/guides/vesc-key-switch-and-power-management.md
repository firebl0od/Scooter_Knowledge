# VESC Key Switch & Power Management Guide

## TL;DR
- VESC controllers keep the logic rail live whenever the pack is connected—true power-off requires BMS latching, loop keys, or external contactors, not just VESC's 5 V enable pin.[^vesc_latch]
- Keyed switches hung on the K-line ignition leads have exploded because they're rated for milliamps, not battery-level current—size switches properly or move them to DC/DC enable lines instead of main power.[^antispark_fail]
- Spintend singles lack a true latch rail—the MOSFET stack acts as the "switch," so riders need proper upstream contactors rather than relay hacks on low-voltage wiring.[^spintend_latch]

## Power Architecture Understanding

### VESC Latch Behavior
- **Logic rail stays live.** The logic rail is powered whenever the pack is connected, and tying the 5 V switch pin to ground turns the controller off—but this is not a true power disconnect.[^vesc_latch]
- **Flipsky aluminums need external contactors.** Unlike controllers with proper enable pins, Flipsky aluminum units still need external contactors or BMS gating to avoid MOSFET stress during standby.[^vesc_latch]

### Spintend-Specific Architecture
- **Singles rely on MOSFET stack switching.** Rage Mechanics reiterated that the single-board UBOX relies on its MOSFET stack as a "big switch"; there's no dedicated latch rail to intercept with a key, and cutting traces ahead of the regulator is risky micro-surgery—scooters need proper upstream contactors instead of relay hacks.[^spintend_latch]

### Makerbase Ignition Logic
- **75100 units expect momentary latch.** Bridge 5 V to the AD15 enable pin for roughly a second to turn on (three seconds to shut down), and set the ADC shutdown timer so the controller actually unlatches.[^makerbase_latch]
- **84100HP needs normally-closed switches or pull-down mod.** 84100HP controllers need a normally-closed switch or the documented 1 MΩ pull-down to mimic Ubox-style keys.[^makerbase_84100]
- **Archive the 84100HP key conversion.** @fungus93’s Makerbase 84100HP ignition hack is already easier than the older 75100 conversion—document the pin swap and harness photos before the thread disappears.[^84100hp-key]
- **Trace-cut resets are an emergency-only hack.** Tommy and Mirono have used a 5 V step-down trace cut plus a gated 12 V chip to force a shutdown, but the regulator is fragile—treat it as a last resort, not a daily power workflow.[^trace-cut]

## Anti-Spark & Key Switch Failures

### Common Failure Modes
- **Generic anti-spark buttons explode on K-line.** Attempts to hang generic anti-spark buttons on the "K" ignition leads have caused switch explosions; these keys have strict voltage/current ratings and must be sized properly or replaced with true latching hardware.[^antispark_fail]
- **Key switches must target the DC/DC, not ADC lines.** Martin's attempt to break the ADC line with a relay triggered a full-throttle runaway because 0 V maps to maximum duty; Кирилл and Paolo reminded everyone to switch the DC/DC enable or force e-brake input instead so a keyed relay safely disables power without touching throttle lines.[^key_adc_danger]

### Proper Implementation
- **Size switches for actual current.** If hanging switches on ignition lines, verify they're rated for the actual current path—most "anti-spark" switches are only rated for signal-level currents.
- **Use DC/DC enable or BMS control.** The safest approach is to switch the DC/DC enable pin or use smart-BMS control rather than trying to interrupt main battery power with undersized switches.
- **External contactors for true power-off.** For genuine power isolation, use loop keys (XT90S), smart-BMS latching, or external contactors rated for the pack voltage and current.
- **Smart-BMS toggles are not antisparks.** JK Bluetooth toggles can wake packs, but 100 A bursts still demand a dedicated antispark or contactor—do not rely on the toggle as the main power disconnect.[^jk-toggle]

## ANT BMS Precharge Considerations

### Precharge Current Limits
- **Respect ANT BMS precharge ceilings.** Owners report repeated MOSFET failures when exceeding the 20 A "starting current"; use the built-in limit, external 100 Ω precharge buttons, and remember ANT balances at only ~150 mA compared with JK's 2 A.[^ant_precharge]
- **Cold weather needs external precharge.** ANT owners liked raising precharge from 20 A to 30 A to prevent cold-weather brownouts, but veterans warned that routinely exceeding 20 A has blown the precharge FETs—use external resistors or staged buttons instead.[^ant_cold]

## BMS Wake Behavior

### Happy BMS Latch-Off Recovery
- **Some BMSes require charger wake.** Awyba's Happy BMS latched off after reconnecting the pack; the controller only revived after briefly attaching the charger, confirming that some Xiaomi-oriented BMS boards require charger wake signals when their protection trips on inrush.[^happy_wake]

## Power Management Best Practices

### Daily Operation
1. **Document baseline idle draw.** Expect roughly 20 mA standby current with latching power buttons off—any illuminated LED signals a wiring fault.
2. **Use proper anti-spark connectors.** XT90S loop keys or AS150 anti-spark variants provide reliable make/break without arcing on high-current connections.
3. **Verify polarity before power-up.** Fresh Ubox units have shipped with reversed Bluetooth harnesses, killing modules instantly—check continuity before energizing boards.

### Safety Checklist
1. **Never use ADC lines for power switching.** Breaking ADC throttle lines can cause runaway acceleration—only switch DC/DC enable or use e-brake failsafes.
2. **Size anti-spark switches properly.** Verify current ratings match actual usage—most cheap "anti-spark" switches are signal-level only.
3. **Keep BMS within precharge ratings.** Don't exceed manufacturer precharge current limits; use external staged precharge for large capacitor banks.
4. **Plan for BMS wake requirements.** Some BMSes need charger presence to wake from protection—document this behavior for field troubleshooting.

## Source Notes
[^vesc_latch]: VESC latch behavior and key switch wiring considerations showing logic rail stays live and 5V pin controls enable.【F:knowledge/notes/input_part004_review.md†L56-L56】
[^antispark_fail]: Anti-spark and key-switch explosions from hanging generic buttons on K-line ignition leads.【F:knowledge/notes/input_part004_review.md†L269-L269】【F:knowledge/notes/input_part004_review.md†L595-L595】
[^spintend_latch]: Spintend singles lacking true latch rail and relying on MOSFET stack as switch.【F:knowledge/notes/input_part004_review.md†L24-L24】
[^key_adc_danger]: Key switch relay on ADC line causing full-throttle runaway and proper DC/DC enable switching approach.【F:knowledge/notes/input_part004_review.md†L300-L300】
[^ant_precharge]: ANT BMS precharge current limits and MOSFET failure when exceeding 20A starting current.【F:knowledge/notes/input_part004_review.md†L57-L57】【F:knowledge/notes/input_part004_review.md†L80-L80】
[^ant_cold]: ANT BMS precharge adjustment for cold weather and warnings about exceeding 20A blowing FETs.【F:knowledge/notes/input_part004_review.md†L80-L80】
[^happy_wake]: Happy BMS latch-off recovery requiring charger wake signal after inrush protection trip.【F:knowledge/notes/input_part004_review.md†L302-L302】
[^makerbase_latch]: Makerbase 75100 momentary latch implementation with AD15 enable pin timing.【F:knowledge/notes/input_part004_review.md†L36 (in source notes section of Makerbase file)】
[^makerbase_84100]: Makerbase 84100HP normally-closed ignition logic or 1MΩ pull-down mod requirement.【F:knowledge/notes/input_part004_review.md†L36 (in source notes section of Makerbase file)】
[^84100hp-key]: Makerbase 84100HP key-mod thread shared by @fungus93 that riders want archived for its cleaner wiring approach.【F:knowledge/notes/input_part007_review.md†L112-L112】
[^trace-cut]: Makerbase owners cut the 5 V step-down trace and gate the 12 V chip to force a shutdown only for emergency resets—the regulator is fragile and not a daily-use solution.【F:knowledge/notes/input_part007_review.md†L208-L208】
[^jk-toggle]: JK smart BMS Bluetooth toggles can act as enables, but 100 A bursts still require a proper antispark or contactor instead of overrated relays.【F:knowledge/notes/input_part007_review.md†L227-L227】
