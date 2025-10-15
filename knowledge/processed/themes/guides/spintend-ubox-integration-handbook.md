# Spintend Ubox Reliability & Integration Handbook

## TL;DR
- Treat every unit as a kit: tear it down before energising, photograph QC issues for support, and follow VESC-safe power-up rituals (precharge, discharge caps, avoid hot-plugging) to prevent latent shorts or MCU damage.[^1][^2][^3]
- Clamp the case hard to a heat sink and budget active airflow if phase current will exceed ~120 A per channel; pad thickness and surface prep matter more than exotic materials.[^4][^5][^6][^7]
- Keep regen conservative—match battery regen amps to pack capacity, disable traction-control modes on single-motor builds, and check faults via USB before power-cycling if Bluetooth is absent.[^8][^9][^10]
- Plan accessories around the power rails you actually have: the dual exposes cruise/lighting outputs and a 12 V rail, but the single requires external buck converters and careful ADC board wiring.[^11][^12][^13][^14]
- Expect shipping delays without premium couriers; EU buyers still face VAT unless orders route through AliExpress IOSS or arrive mis-declared, so document deliveries for smoother RMAs.[^15][^16][^17]

## Pre-Delivery QC & Bench Setup
1. **Full Disassembly:** Crack the enclosure to inspect for solder balls, missing hardware, or flux residue before the first power-on—multiple riders received “sealed” units with conductive debris or missing faceplate screws.[^1][^2]
2. **Document Everything:** Photograph the internals and keep serials handy; Spintend has honoured RMAs after fires and board failures when owners supplied teardown evidence.[^18]
3. **Bench Rules:** Wire the entire harness before energising, precharge ≥20 S packs, discharge bus caps after unplugging, keep ADC inputs ≤3.3 V, and eliminate ground loops to avoid repeat STM32 deaths.[^3]
4. **Initial Power Tests:** Bring the controller up on a fused bench supply with the BMS discharge FET enabled; if regen previously latched undervoltage faults, confirm the pack’s protection MOSFETs are awake before running detection.[^19]
5. **Detection housekeeping:** Enable the phase-filter checkbox only during motor detection—leaving it on while riding reintroduces noise and ABS overcurrent faults.[^phase-filter]

## Thermal Management & Mounting
- **Firmware Limits:** Stock firmware starts derating around 75–85 °C and shuts down near 100 °C, so increase cutbacks only after verifying thermistor calibration.[^4]
- **Interface Upgrades:** Replacing spongy pads with copper shims or thicker (≈1 mm) thermal sheets plus quality paste dropped MOSFET temps 15–20 °C during 100–140 A runs when the case was clamped directly to the deck.[^5][^6]
- **Airflow & Deck Prep:** Add 40–90 mm fans between stacked boards, machine paint off mounting faces, and bolt the enclosure to aluminium spreaders if regen pushes single-Ubox stacks past 65–70 °C.[^7]
- **Expected Benchmarks:** Well-mounted duals have logged ~100 A battery / 130 A phase at ≈45 °C, while poor contact in sealed Weped decks let cases soar to 80 °C during 500 A combined pulls—plan extra cooling above those loads.[^6][^20]
- **Single-Ubox baseline:** The aluminum single 85/200 held 100 A battery, 200 A phase, and 60–70 A FW on a 20 S MXUS build without thermal rise when clamped to a 20 mm aluminum baseplate—treat it as a compact alternative to boxed duals if you can replicate the mounting.【F:knowledge/notes/input_part005_review.md†L216-L218】
- **Plan hardware for earless cases.** 85/240 housings still ship without mounting ears and rely on tiny M2.5 hardware, so riders print brackets, retap threads, or glue adapters before long-travel suspensions knock under-deck mounts loose.[^31]

## Power Limits, Regen & Current Planning
- **Current Envelope:** Treat 120–130 A phase per motor (≈160 A ABS max) as the practical ceiling for daily dual setups; sensor stutter above ~85 A usually signals failed MOSFETs or loose leads, not tuneable instability.[^21]
- **Regen Discipline:** Bench testing shows that even –5 A battery regen can trip controllers on unloaded wheels; cap regen amps to roughly the pack’s amp-hour rating plus a small overhead so the FETs absorb the excess.[^8]
- **High-Voltage Safeguards:** Dual owners run ~2×135 A phase / 2×71 A battery within 70 °C so long as regen stays off during full-charge launches and higher-voltage packs (17 S+) are bled a few percent before re-enabling braking.[^22]
- **Know the Ubox 100/100 envelope.** Smart Repair still caps the single at 22 S with regen disabled on the e-brake input; it ships at 135 A phase / 180 A absolute without ST-Link pads or beefy 12 V rails, so budget external regulation for accessories.[^u100-guardrails]
- **Duty & Field Weakening:** Keep field-weakening reserved for cooled builds; previous fires stemmed from wizard runs on fresh installs, so validate base detection and duty-cycle ramps before layering FW or traction aids.[^18][^23]
- **App-config watchdog:** Mobile VESC Tool exposes an inactivity shutdown in App Config → General; disable it for long bench sessions and raise Absolute Max current slightly if 200 A overcurrent faults persist after tuning.【F:knowledge/notes/input_part005_review.md†L315-L316】

## Controls, Accessories & IO
- **Remote & Cruise:** The bundled 2.4 GHz remote offers cruise, horn, and light controls via the receiver, reducing parallel looms compared with bare PPM throttles.[^11]
- **Harness connector update:** Recent adapter looms ship with GH1.25 signal plugs—stock pre-crimped jumpers instead of fighting loose hand crimps, label each lead, and route them carefully through the frame.【F:knowledge/notes/input_part005_review.md†L315-L316】
- **Brake Inputs:** The ADC daughterboard supports normally-open/closed levers and selectable 5 V or 3.3 V rails—set the switches before plugging Magura/Shimano sensors to avoid shorting hall supplies.[^13]
- **Lighting Power:** Dual controllers expose a ≈1.5 A 12 V rail for lighting relays, but singles lack this output; budget fused DC-DC converters instead of stealing from the fan header.[^12][^14]
- **CAN & Anti-Slip:** Updated harnesses let one single wake another over CAN, yet anti-slip belongs on dual configurations—leaving it active on a solo motor causes low-speed cut-outs with red/green blink codes.[^10][^24]
- **Bench-start requirements:** Ubox 100/100 controllers refuse to boot from USB-C alone—wire the latching 16 mm start button or a proper low-voltage switch instead of relying on the BMS as a master disconnect.[^start-button]

## Firmware, Logging & Fault Recovery
- **Version Discipline:** Stick with Spintend’s vetted firmware packages (e.g., 100 A battery limit files) unless you have cooling to exploit the 300 A hardware bins; mismatched binaries raise noise and reliability issues.[^25]
- **BLE Options:** Official BLE dongles arrive pre-flashed and tax-paid via AliExpress, while DIY NRF boards need extra programming; keep at least one link for live tuning even if you prefer wired sessions.[^26]
- **Bluetooth range reality:** The onboard Bluetooth radio in the aluminum single routinely maintains ~50 m line-of-sight links once QC cleaning is done—enough to keep pits connected without auxiliary antennas.【F:knowledge/notes/input_part005_review.md†L217-L218】
- **Fault Retrieval:** If Bluetooth is absent, the controller retains the last fault until shutdown—connect via USB before cycling power so valuable diagnostics aren’t lost.[^10]

## Known Field Failures & Mitigations
- **Continuity-check every harness.** A v2 80 V single shipped with its Bluetooth lead reversed and killed the module immediately—probe polarity and confirm JST orientation before first power to avoid sacrificial electronics.[^27]
- **Diagnose ADC adapters before blaming firmware.** VSETT 11+ owners logged CAN dropouts, stuck brake beeps, and latched brake inputs when ADC V2 boards half-failed after 6.0 updates; reflash, reseat grounds, and isolate the adapter before pursuing RMAs.[^28]
- **Keep throttles on the 3.3 V rail and mount adapters close.** Routing halls through 5 V accessory pins or long unshielded runs has blown STM32 inputs; park the ADC board beside the controller, use divider networks, and rely on Vedder’s detach timeout to hand control back to hardware cleanly.[^29]
- **Treat thermal spikes as potential moisture ingress.** Riders seeing 190 °C MOSFET readings traced the fault to condensation inside the case—warm the enclosure, dry the PCB, and reseal gaskets before raising firmware cutoffs.[^30]

## Logistics & Support Notes
- **Warranty Responsiveness:** Spintend has replaced fire-damaged units and keeps spare power/logic boards on hand, which contrasts with poorer experiences on competing FlipSky hardware.[^18]
- **Shipping Choices:** Direct orders sometimes arrive underdeclared (sub-$30) and dodge VAT, but DHL eCommerce frequently delays or loses parcels; veterans now pay for FedEx or AliExpress Standard to avoid customs limbo.[^15][^16]
- **EU VAT Planning:** Accessories shipped without prepaid VAT trigger €30 fees on €20 parts—push for IOSS channels or budget the surcharge when ordering spares.[^17]
- **US distribution hub.** Recent 85/240 batches now ship from a New Jersey warehouse, and sub-$1,000 orders have cleared without added tariffs, cutting replacement lead times for North American riders.[^32]

## Source Notes
[^1]: Controllers routinely arrive with debris; open and inspect before powering up.【F:knowledge/notes/input_part000_review.md†L359-L359】
[^2]: Replacement units have shipped missing screws or with solder splatter, reinforcing the teardown-first habit.【F:knowledge/notes/input_part001_review.md†L119-L119】【F:knowledge/notes/input_part001_review.md†L240-L240】
[^3]: Seven golden rules for safe VESC power-up and wiring discipline.【F:knowledge/notes/input_part001_review.md†L463-L463】
[^4]: Default thermal derating and shutdown thresholds for Ubox firmware.【F:knowledge/notes/input_part000_review.md†L102-L102】
[^5]: Copper shims and improved interfaces cutting MOSFET temperature roughly 20 %.【F:knowledge/notes/input_part000_review.md†L129-L129】
[^6]: Pad compression tweaks keeping MOSFETs near 45 °C at ~100 A battery / 130 A phase, plus data on thicker stock pads in new harness revisions.【F:knowledge/notes/input_part000_review.md†L130-L130】【F:knowledge/notes/input_part000_review.md†L583-L583】
[^7]: Active cooling tactics for dual singles overheating under heavy regen.【F:knowledge/notes/input_part000_review.md†L475-L475】
[^8]: Regen bench tests tripping controllers and the amp-hour-based cap guideline.【F:knowledge/notes/input_part000_review.md†L176-L177】
[^9]: Regen-to-capacity rule of thumb reiterated during community tuning sessions.【F:knowledge/notes/input_part000_review.md†L177-L177】
[^10]: Post-fault USB checks and anti-slip misconfiguration behaviour on single-motor builds.【F:knowledge/notes/input_part000_review.md†L590-L591】
[^11]: Remote-integrated cruise, horn, and lighting outputs reducing harness complexity.【F:knowledge/notes/input_part000_review.md†L110-L110】【F:knowledge/notes/input_part000_review.md†L146-L146】
[^12]: Onboard 12 V rail capacity for accessories on dual controllers.【F:knowledge/notes/input_part000_review.md†L687-L687】
[^13]: ADC board switch options for Magura and Shimano brake sensors.【F:knowledge/notes/input_part000_review.md†L206-L206】
[^14]: Single-channel controllers lack a 12 V rail, necessitating external buck converters.【F:knowledge/notes/input_part000_review.md†L460-L460】
[^15]: Underdeclared parcels and bundled remote features noted in EU shipments.【F:knowledge/notes/input_part000_review.md†L146-L146】
[^16]: Courier reliability comparisons and RMA shipping delays via DHL eCommerce.【F:knowledge/notes/input_part000_review.md†L451-L451】【F:knowledge/notes/input_part000_review.md†L485-L485】
[^17]: EU VAT frustrations and calls for IOSS handling on accessories.【F:knowledge/notes/input_part001_review.md†L469-L469】
[^18]: Warranty cases following catastrophic failures and continued community support.【F:knowledge/notes/input_part000_review.md†L62-L62】【F:knowledge/notes/input_part000_review.md†L183-L183】
[^19]: Smart-BMS precharge and discharge FET requirements before successful motor detection.【F:knowledge/notes/input_part000_review.md†L168-L170】
[^20]: Thermal extremes logged on poorly mounted duals at ~500 A phase combined.【F:knowledge/notes/input_part000_review.md†L614-L614】
[^21]: Practical phase-current ceilings and fault symptoms at higher demand.【F:knowledge/notes/input_part000_review.md†L662-L663】
[^22]: Dual 135 A phase / 71 A battery operating envelope and regen cautions on 17 S packs.【F:knowledge/notes/input_part001_review.md†L840-L840】
[^23]: Early fire incidents during detection runs and the caution to validate baseline tuning before advanced features.【F:knowledge/notes/input_part000_review.md†L62-L62】
[^24]: CAN wake wiring updates and anti-slip recommendations for multi-controller builds.【F:knowledge/notes/input_part000_review.md†L583-L583】【F:knowledge/notes/input_part000_review.md†L590-L590】
[^25]: Official firmware packages with 100 A vs. 300 A limits and the need for matching cooling.【F:knowledge/notes/input_part000_review.md†L42-L42】
[^26]: BLE dongle sourcing and plug-and-play advantages over generic NRF boards.【F:knowledge/notes/input_part001_review.md†L174-L174】
[^27]: Harness polarity failure that destroyed a Bluetooth module on first power-up.【F:knowledge/notes/input_part004_review.md†L287-L287】
[^28]: ADC adapter V2 fault progression—CAN dropouts, brake beeps, and recovery workflow after firmware 6.0 updates.【F:knowledge/notes/input_part004_review.md†L351-L352】
[^29]: ADC placement, detach-timeout behaviour, and the 3.3 V throttle guidance preventing STM32 input failures.【F:knowledge/notes/input_part004_review.md†L286-L286】【F:knowledge/notes/input_part004_review.md†L18-L18】【F:knowledge/notes/input_part004_review.md†L202-L202】
[^30]: Moisture-driven MOSFET temperature spikes that vanished after warming and drying the enclosure.【F:knowledge/notes/input_part004_review.md†L474-L474】
[^31]: 85/240 mounting anecdotes covering custom brackets, retapped threads, and thermal pad tweaks to secure earless housings.【F:knowledge/notes/input_part012_review.md†L20537-L20541】【F:knowledge/notes/input_part012_review.md†L20575-L20583】【F:knowledge/notes/input_part012_review.md†L20581-L20587】
[^32]: Spintend 85/240 shipments now staging through a New Jersey hub for faster, low-tariff deliveries into the United States.【F:knowledge/notes/input_part012_review.md†L17321-L17325】【F:knowledge/notes/input_part012_review.md†L18632-L18638】
[^u100-guardrails]: Smart Repair reiterated that the Ubox 100/100 tops out at 22 S, ships with 135 A phase / 180 A absolute limits, and should keep regen off the e-brake path unless you’re ready to swap FETs; it also omits ST-Link pads and beefy 12 V rails compared with 85xxx units.【F:knowledge/notes/input_part012_review.md†L19186-L19195】
[^start-button]: The same teardown confirmed the 100/100 refuses to boot from USB-C—wire the latching 16 mm start button or another 5 V trigger instead of depending on the BMS as a master switch.【F:knowledge/notes/input_part012_review.md†L19300-L19318】
[^phase-filter]: Motor-wizard phase filters should be disabled after detection to avoid noise and ABS overcurrent faults on Spintend controllers.【F:knowledge/notes/input_part004_review.md†L31-L31】
