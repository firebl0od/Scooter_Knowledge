# Daly Smart BMS Moisture Recovery & Waterproofing Playbook

## TL;DR

- Waterlogged Daly display BMS units manifest ghost 5 V readings on random cell groups even when pack voltages are balanced.
  - open the enclosure immediately, dry the harness, and clean the board before power-cycling.[^1]
- Reassembly should include layered insulation (fish paper, multiple waterproof tape wraps, outer shrink) plus silicone-sealed seams and desiccant packs to prevent repeat condensation failures.[^2]
- After drying sessions, leave the pack open overnight with low heat (hair dryer or warm air) before resealing; rushing the process risks latch-off FETs and lingering moisture.[^3]
- Keep the Daly Bluetooth app handy (default password 123456) to re-enable charge/discharge MOSFETs after moisture-induced trips once the hardware is verified.[^4]
- Daly smart boards only balance at ~30 mA and struggle during 25 A charges.
  - pair them with monitored 4 A active balancers and watch for reverse-current experiments that can fry the helper board.[^1]
- If a Daly 10S board stops balancing after only a week of service, replace it—Rita won’t cover the fault—and double-check the balance-lead pinout when you install the new hardware.[^denis-daly-balance]

## Failure Signals to Watch

- Random 5 V cell-group reports or sudden discharge lockouts despite balanced cells.[^1]
- Pack voltage reporting 3.1 V per cell while the scooter still reads near nominal voltage—often a clue that moisture has upset the sensing harness.[^2]
- BMS refusing to discharge/charge until MOSFETs are toggled in software following a shutoff event.[^4]

## Emergency Dry-Out Procedure

1. **De-energise safely:** Disconnect the pack, isolate both charge and discharge leads, and document cell voltages before disassembly.[^1]
2. **Expose the electronics:** Remove outer shrink and insulation to access the Daly board and harness entry points; note original routing for reassembly.[^1]
3. **Purge moisture:** Use controlled hot air to dry balance leads and PCB surfaces, following with an isopropyl alcohol rinse to displace residual water inside the mostly potted enclosure.[^1]
4. **Rest the pack:** Allow the assembly to air out overnight after heat cycles; confirm no condensation is present before moving on.[^3]

## Rebuild & Waterproofing Stack

- Wrap every series group in fish paper before reinstalling the BMS.[^2]
- Apply at least five alternating wraps of waterproof tape around the pack body, followed by fresh outer shrink tubing.[^2]
- Seal every seam, wire exit, and fastener penetration with silicone to block capillary ingress.[^2]
- Add silica-gel desiccant inside the enclosure cavity to absorb residual humidity.[^2]

## Post-Recovery Validation

- Use the Daly app to re-enable charge/discharge MOSFETs and verify they latch on without fault codes.[^4]
- Monitor cell voltages over several hours; readings should stabilise without reappearing 5 V anomalies.[^1]
- Perform a gentle charge/discharge cycle while logging temperatures to confirm the pack behaves normally before resealing permanently.[^3]

## Preventive Maintenance Checklist

- Schedule periodic inspections of sealant, shrink, and harness boots—especially after wet rides.[^2]
- Keep spare desiccant packs and silicone on hand for mid-season refreshes.[^2]
- Document every moisture event with photos and logs so warranty or future diagnostics can trace component history.[^1]

## Source Notes

[^1]: Moisture fault symptoms and initial recovery steps for Daly smart BMS units.[^2]
[^2]: Recommended insulation stack and silica-gel usage after a moisture incident.[^3]
[^3]: Guidance to dry the assembly with repeated hair-dryer cycles and overnight airing before resealing.[^4]
[^4]: Daly smart BMS discharge/charge MOSFET control via the Bluetooth app (password 123456) required after trips.[^5]


## References

[^1]: Source: knowledge/notes/input_part004_review.md†L290-L290
[^2]: Source: knowledge/notes/input_part000_review.md†L153-L154
[^3]: Source: knowledge/notes/input_part000_review.md†L155-L155
[^4]: Source: knowledge/notes/input_part000_review.md†L156-L156
[^5]: Source: knowledge/notes/input_part000_review.md†L367-L367
[^denis-daly-balance]: Source: knowledge/notes/denis_all_part02_review.md†L740-L740
