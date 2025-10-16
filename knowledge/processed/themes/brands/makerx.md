# MakerX Controllers Brand Dossier

## TL;DR

- Mini FOC hardware is still a 12 S design; running 13 S (~54.6 V) leaves almost no regen headroom, so builders moving past 50 V should pivot to ≥16 S-rated controllers like Spintend before pushing voltage experiments.[^1]
- Well-cooled MakerX singles routinely handle ~60 A battery and 180–200 A phase, but recurring DOA duals and MOSFET blowouts mean every install needs bench burn-in and spares on hand.[^2][^3]
- Logs still crown MakerX singles over Flipsky boxes when heatsinked—60 A battery / 200 A phase stays stable while Ubox singles overheat near 80 A battery without aggressive cooling, so invest in machined mounts before raising limits.[^4][^5]
- Treat every 3.3 V accessory rail as sacred: footpads, throttles, and ADC gear all expect logic-level supplies, and miswiring to 5 V has already killed sensors and daughterboards.[^6][^7][^8]
- Makerbase’s 75×100 docs now live on GitHub, and the on/off revision simply swaps a resistor pair; riders also confirmed third-party BLE modules run happily from the NRF header once wired correctly.[^9]
- G300-class stacks plateau around 22 S / 320 A phase today, while rumoured K900/KG00 firmwares remain unproven—plan upgrades around documented limits or step to C350/3Shul hardware for higher-voltage racing.[^10][^11]
- European racers confirmed Ambrosini RS500, Rage Robers, and MakerX G300 controllers share the same hardware—pricing reflects branding, not silicon, so focus on firmware provenance and support rather than rebadges.[^12]
- Discounted “MakerX” dual controllers claiming 16 S, 100 A continuous, and 200 A peak appear to be 75 300-derived boards packaged like Nucular 24F clones—validate specs before buying the rebrand.[^13]

## Product Line Cheat Sheet

| Model | Nominal System | Community-Validated Envelope | Notes |
| --- | --- | --- | --- |
| Mini FOC / M100 | 12 S nominal (13 S pushes regen headroom)[^8] | ~40 A battery, ≤120 A phase; raising phase to 70 A cooked an M100 immediately after detection reset | Triple-shunt design, silicone pads, and clean analog isolation impressed teardown crews, but treat it as a compact ebike controller and add stout torque arms before test rides.[^14][^15] |
| GO-FOC HI100 / HI200 | 20 S single | 60 A battery / 200 A phase commuter baseline; hard-mounted enclosures kept FET temps in the 20s °C at 7 °C ambient | Rerun detection after mechanical work, verify thermistor coefficients on VESC 6.0, and keep fire extinguishers handy—bench launches have still blown MOSFET triplets on fresh boards.[^16][^17] |
| GO-FOC G300 / D100S | 20–22 S dual | 150 A battery / 250–300 A phase per controller on 20 S; saturation and heating spike above ~320 A phase at 22 S | Momentary power buttons need the VESC auto-off timer to behave, twin switches are simply paralleled, and ADC profile switches keep burning daughterboards without vetted wiring diagrams—document the harness before powering up.[^18][^8][^10] |
| Ubox 100/100 (MakerX badge) | 16–20 S dual | Shops cap them near 55 A battery / 170 A phase each on resin-backed revisions | Resin-backed shells still lag metal-core cooling; treat heatsinking as mandatory and log temps before raising limits.[^19] |

## Reliability & Support Signals

- Shop owners reported 70 % of incoming duals arriving faulty, with return shipping erasing the budget advantage; keep at least one spare controller on the shelf for every customer deployment.[^20]
- Bench launches are still killing fresh duals—Face de Pin Sucé lost three MOSFETs on the first acceleration and now keeps spare power boards on hand for direct-FET designs.[^21]
- Mirono’s teardown logged tidy soldering, triple copper shunts per phase, and thermal pads bonding FETs to the shell—stark contrast to a DOA Sabvoton with looped throttles and Kapton-isolated MOSFETs that never drew vendor support, explaining why riders keep pivoting back to MakerX despite QC headaches.[^22][^23]
- MakerX’s MOSFET choices (e.g., NECP045N85GU) mirror failure-prone Flipsky runs; continuous current should stay conservative unless the build adds serious heatsinking and airflow.[^24][^25]
- Field logs put Hi200 “200 A continuous” claims in check: Mirono saw ~70 °C after 30 minutes at 45 A battery / 150 A phase inside a bag, so plan external heatsinks, shorter phase leads, and MOSFET part verification before trusting marketing brochures.[^26]
- Sabvoton’s recurring DOA shipments—throttle loops, sloppy Kapton layering, hall failures—are pushing riders toward MakerX despite the need for torque arms and careful QC, especially when paired with proper controller mounting.[^27]
- CAN connectors and isolated low-voltage domains also earned praise in the teardown thread; riders noted MakerX detected halls and throttle immediately while the Sabvoton needed reflashing and days of unanswered tickets.[^28]
- Fire incidents on GO-FOC boards—even at 96 V / 80 A battery with added fans—show new batches need staged validation before matching Spintend or 3Shul duty cycles.[^29]
- MakerX’s MOSFET choices (e.g., NECP045N85GU) mirror failure-prone Flipsky runs; continuous current should stay conservative unless the build adds serious heatsinking and airflow.[^24][^25]
- Blade 10 and Nucular controllers share the same 2.8 mΩ Magnachip devices, so upgrade expectations should be tempered—MakerX singles still survive only ~70–100 A battery / 150 A phase without aggressive cooling. [^30]
- Resellers are rebadging MakerX hardware at hefty markups—the Sur-Ron focused “MTO K2000” is simply a G300 in a cheap aluminium shell—so budget purchases accordingly and verify firmware provenance before assuming you’re getting unique electronics.[^31]

## Setup & QA Checklist

1. **Disassemble on arrival.** Confirm thermal pads actually contact the shell, inspect solder joints, and restake capacitors before the first power-up—vibration still loosens untouched boards.[^32][^33]
   - Leave flux residues intact or reapply fresh flux during repairs; scorching it off invites oxide formation and weakens controller rework joints.[^34]
2. **Rerun motor detection after any mechanical change.** Loose axles and firmware mismatches have corrupted FOC detection until owners reverted to 5.2 binaries and re-tightened hardware; one GO-FOC HI100 only recovered after the axle clamp was re-torqued, VESC Tool 5.2 reflashed, and MakerX firmware reapplied.[^16][^35]
   *Bonus:* A machined enclosure dropped HI100 case temps to ≈23 °C at 60 A battery / 200 A phase in 7 °C ambient versus 60–80 °C inside a Wildman bag—hard-mount controllers whenever possible.[^36]
3. **Verify thermistor coefficients on VESC 6.0+.** HI100 temperature scaling required swapping firmware profiles to regain accurate readings, and the latest MakerX firmware bundles expose separate coefficient tables for 75300 versus HI100 builds—double-check the dropdown before saving so reported temps match real probes.[^37][^38]
4. **Power BLE from the comm header.** Water-damaged boards recovered once techs reflashed firmware, fed BLE modules from the 5 V comm header, and borrowed UART2 lines instead of overloading the 3.3 V rail.[^39]
5. **Ble test harnesses for 3.3 V logic.** Probe footpads, throttles, and ADC rails before closing the case; missing 3.3 V feeds silently disable safety interlocks.[^6][^7]

## G300 Specific Configuration Notes

### ABS Overcurrent Mitigation

- G300 controllers show ABS overcurrent trips during acceleration even when phase current appears within limits—this often traces to aggressive throttle profiles or insufficient ABS slow ramp settings.[^g300-abs]
- **Mitigation steps:**
  1. Enable "ABS Current Limit Slow Absolute" in VESC Tool motor configuration
  2. Lower ABS current limits by 10–20 A below peak phase targets
  3. Add positive ramp time (0.3–0.5 s) to throttle response to soften initial torque requests
  4. Log real-time current during test rides to verify ABS thresholds aren't exceeded during launches[^g300-abs]
- If trips persist after firmware 6.3 updates, verify motor detection was rerun and observer settings match the motor's inductance—outdated parameters from earlier firmware can trigger false ABS events.[^g300-fw63]

### Firmware 6.3 Throttle Fixes

- Firmware 6.3 resolved throttle response issues on G300 platforms where inputs felt sluggish or non-linear compared to earlier versions; update both controllers in dual setups to maintain symmetric behavior.[^g300-fw63]
- After flashing 6.3, clear motor configurations and rerun detection to ensure observer parameters align with the new control algorithms.[^g300-fw63]

### Push-Button Configuration

- JPPL documented the MakerX push-button workflow: change App → General → Shutdown Method to timed auto-off (typically 5–10 seconds of zero throttle) so a single momentary press toggles power cleanly.[^g300-button]
- Both harness buttons are wired in parallel—they do not isolate main battery power, only trigger the controller's soft power logic—so plan external contactors or smart-BMS control for true pack isolation.[^g300-button]
- Red LED fault codes on G300 units indicate various failure modes; consult MakerX documentation for specific blink patterns before assuming hardware failure.[^g300-led]

## Tuning Guardrails

- **Singles:** Start around 60 A battery / 180–200 A phase and raise only with frame-mounted heatsinks or machined enclosures; bag-mounted installs run 30–50 °C hotter under the same load.[^2]
- **Duals:** Keep G300/D100S stacks near 150 A battery and ≤300 A phase on 20 S unless you have thermal telemetry proving headroom; logs above 320 A phase at 22 S showed rapid saturation and heat soak.[^10]
- **Compact builds:** Reset phase limits on Mini FOC/M100 controllers after detection—the firmware’s 70 A default already destroyed one unit meant for 40 A continuous duty.[^15]
- **Future hardware claims:** Treat the “K900” firmware bundle as roadmap noise until hardware ships; its 800 A battery / 1 200 A motor claims remain unverified marketing numbers.[^11]

## Wiring & Accessory Integration

- **Power buttons:** Set App → General → Shutdown Method to a timed auto-off so the stock momentary switch behaves; remember both harness buttons are paralleled and do not isolate power on their own.[^18]
- **ADC profile switches:** Publish wiring that routes throttles to ADC2 before using three-position gear toggles—ad-hoc rewires have already burned MakerX ADC daughterboards.[^8]
- **BLE & telemetry:** When rescuing water-damaged boards, power MakerX BLE modules from the 5 V comm header and borrow UART2 for data to avoid overloading the 3.3 V rail.[^17][^40]
- **Accessory rails:** Never tap 5 V loads directly from the logic PCB—route horns, lights, and fans through dedicated buck converters to protect the controller rails.[^41]

## When to Reach for Alternatives

- If you need warranty-backed uptime or plan to ship customer scooters, shop feedback suggests pivoting to Spintend singles or 3Shul duals once MakerX DOA rates start eating labour margins.[^20]
- Racers chasing sustained >320 A phase on 22 S have already reverted to C350/3Shul hardware; MakerX G300s simply saturate earlier and run hotter in the same chassis.[^10]

## Source Notes

[^1]: MakerX commuter current envelopes, thermistor fixes, water-damage recovery workflow, and BLE power sourcing guidance. Source: knowledge/notes/input_part003_review.md, L93 to L120. Source: knowledge/notes/input_part003_review.md, L136 to L136. Source: knowledge/notes/input_part003_review.md, L151 to L152. Source: knowledge/notes/input_part003_review.md, L552 to L552
[^2]: Mini FOC teardown quality, torque-arm reminders, and MOSFET limit cautions from controller comparison threads. Source: knowledge/notes/input_part002_review.md, L135 to L142. Source: knowledge/notes/input_part002_review.md, L166 to L168
[^3]: Phase-limit failure on MakerX M100 and ongoing QC/resale warnings for MakerX vs. competitors. Source: knowledge/notes/input_part009_review.md, L169 to L177. Source: knowledge/notes/input_part004_review.md, L46 to L46
[^4]: Accessory-voltage expectations across MakerX hardware, including S100 footpads and logic-rail short cautions. Source: knowledge/notes/input_part012_review.md, L248 to L249. Source: knowledge/notes/input_part012_review.md, L255 to L256. Source: knowledge/notes/input_part012_review.md, L347 to L349
[^5]: Push-button workflow, ADC daughterboard failures, and high-voltage saturation limits recorded on MakerX G300 platforms. Source: knowledge/notes/input_part013_review.md, L302 to L329. Source: knowledge/notes/input_part013_review.md, L326 to L329. Source: knowledge/notes/input_part013_review.md, L407 to L409. Source: knowledge/notes/input_part013_review.md, L416 to L417
[^6]: Resin-backed Ubox cooling observations and conservative current targets from field reports. Source: knowledge/notes/input_part011_review.md, L221 to L224
[^7]: MakerX GO-FOC fire reports under 96 V testing and broader warnings about unvetted high-voltage firmware like the rumoured K900 release. Source: knowledge/notes/input_part004_review.md, L321 to L321. Source: knowledge/notes/input_part013_review.md, L462 to L462
[^8]: Mini FOC voltage headroom discussion confirming it remains a 12 S-class controller and recommending Spintend or other ≥16 S hardware for >50 V packs. Source: knowledge/notes/input_part001_review.md, L11 to L11
[^g300-abs]: G300 ABS overcurrent mitigation steps including slow ramp enable and positive throttle ramping. Source: knowledge/notes/input_part013_review.md, L514 to L514
[^g300-fw63]: Firmware 6.3 throttle response fixes and motor detection requirements on G300 platforms. Source: knowledge/notes/input_part013_review.md, L262 to L262
[^g300-button]: MakerX G300 push-button configuration using timed auto-off shutdown method. Source: knowledge/notes/input_part013_review.md, L302 to L302
[^g300-led]: G300 red LED fault codes indicating various failure modes requiring diagnostic reference. Source: knowledge/notes/input_part013_review.md, L654 to L654

## References

[^1]: Source: knowledge/notes/input_part001_review.md, L11 to L11
[^2]: Source: knowledge/notes/input_part003_review.md, L93 to L120
[^3]: Source: knowledge/notes/input_part003_review.md, L151 to L153
[^4]: Source: data/vesc_help_group/text_slices/input_part003.txt, L10795 to L10912
[^5]: Source: data/vesc_help_group/text_slices/input_part003.txt, L11070 to L11104
[^6]: Source: knowledge/notes/input_part012_review.md, L255 to L256
[^7]: Source: knowledge/notes/input_part012_review.md, L347 to L349
[^8]: Source: knowledge/notes/input_part013_review.md, L407 to L409
[^9]: Source: knowledge/notes/input_part006_review.md, L430 to L431
[^10]: Source: knowledge/notes/input_part013_review.md, L416 to L417
[^11]: Source: knowledge/notes/input_part013_review.md, L462 to L462
[^12]: Source: knowledge/notes/input_part012_review.md, L387 to L387
[^13]: Source: data/vesc_help_group/text_slices/input_part001.txt, L25282 to L25299
[^14]: Source: knowledge/notes/input_part002_review.md, L135 to L142
[^15]: Source: knowledge/notes/input_part009_review.md, L169 to L177
[^16]: Source: knowledge/notes/input_part003_review.md, L119 to L120
[^17]: Source: knowledge/notes/input_part003_review.md, L151 to L152
[^18]: Source: knowledge/notes/input_part013_review.md, L302 to L329
[^19]: Source: knowledge/notes/input_part011_review.md, L221 to L224
[^20]: Source: knowledge/notes/input_part003_review.md, L153 to L153
[^21]: Source: data/vesc_help_group/text_slices/input_part003.txt, L19980 to L20090
[^22]: Source: data/vesc_help_group/text_slices/input_part002.txt, L9699 to L9738
[^23]: Source: data/vesc_help_group/text_slices/input_part002.txt, L9826 to L9863
[^24]: Source: knowledge/notes/input_part002_review.md, L166 to L168
[^25]: Source: knowledge/notes/input_part003_review.md, L120 to L120
[^26]: Source: data/vesc_help_group/text_slices/input_part002.txt, L12320 to L12354
[^27]: Source: knowledge/notes/input_part002_review.md, L136 to L138
[^28]: Source: data/vesc_help_group/text_slices/input_part002.txt, L9799 to L9859
[^29]: Source: knowledge/notes/input_part004_review.md, L321 to L321
[^30]: Source: knowledge/notes/input_part003_review.md, L120 to L121
[^31]: Source: knowledge/notes/input_part006_review.md, L401 to L401
[^32]: Source: knowledge/notes/input_part002_review.md, L137 to L138
[^33]: Source: knowledge/notes/input_part004_review.md, L312 to L314
[^34]: Source: knowledge/notes/input_part002_review.md, L138 to L138
[^35]: Source: data/vesc_help_group/text_slices/input_part003.txt, L13725 to L13790
[^36]: Source: knowledge/notes/input_part003_review.md, L119 to L119
[^37]: Source: knowledge/notes/input_part003_review.md, L136 to L136
[^38]: Source: data/vesc_help_group/text_slices/input_part003.txt, L17564 to L17610
[^39]: Source: data/vesc_help_group/text_slices/input_part003.txt, L19798 to L19926
[^40]: Source: knowledge/notes/input_part003_review.md, L552 to L552
[^41]: Source: knowledge/notes/input_part012_review.md, L248 to L249
