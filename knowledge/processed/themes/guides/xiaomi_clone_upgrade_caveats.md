# Xiaomi Clone Upgrade & Expansion Caveats

## TL;DR
- **Treat clone scooters as bare frames.** Without Xiaomi dashboards or data lines, Rita cannot be configured—range upgrades rely on voltage-matched Y-cables, careful wiring, and conservative charging rather than smart adapters.【F:knowledge/notes/denis_all_part02_review.md†L93104-L93308】
- **Plan to transplant the entire Xiaomi electronics stack.** Builders replacing clone controllers routinely add genuine Xiaomi BMS, controller, and dashboard bundles (~€100) because Rita and Xiaomi firmware expect matching data lines.【F:data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L60092-L60113】
- **Equalise voltages before parallel connections.** Builders keep packs tied together once matched to avoid constant inrush surges; disconnecting after every ride accelerates balancing wear and exposes weak connectors.【F:knowledge/notes/denis_all_part02_review.md†L93340-L93386】
- **Budget time for wiring and firmware work.** Purple-case dashboards, GD32 controllers, and clone BMS layouts all require ST-Link access, custom harnesses, and patient configuration before any performance firmware will stick.【F:knowledge/notes/denis_all_part02_review.md†L93680-L93705】【F:knowledge/notes/denis_all_part02_review.md†L95680-L95780】

## Battery Expansion Options
| Scenario | Recommended Action | Watchpoints |
| --- | --- | --- |
| Clone scooter needs more range | Parallel a second 10S pack with a quality Y-cable after matching voltage; keep the packs connected between rides so they stay equalised.【F:knowledge/notes/denis_all_part02_review.md†L93104-L93308】【F:knowledge/notes/denis_all_part02_review.md†L93548-L93558】 | Ensure both packs use common-port BMS boards; mismatched charge/discharge ports overfill cells during regen or charging.【F:knowledge/notes/denis_all_part02_review.md†L93604-L93636】 |
| Rider wants hot-swappable packs | Route XT60 extensions out of the deck (≈50 cm) into a Wildman bag and charge each pack individually off-scooter.【F:knowledge/notes/denis_all_part02_review.md†L94820-L94873】 | Voltage-check every pack before reconnecting; clones lack Rita’s isolation so mis-matched packs spark instantly.【F:knowledge/notes/denis_all_part02_review.md†L94841-L94873】 |
| Considering OEM Xiaomi packs in parallel | Avoid using stock packs without common ports—Rita and Y-cables cannot safely balance them, and regen will overcharge the weaker pack.【F:knowledge/notes/denis_all_part02_review.md†L122761-L122787】 | Install a proper common-port BMS or rebuild the pack before paralleling.【F:knowledge/notes/denis_all_part02_review.md†L93604-L93636】 |

### Wiring Discipline
- **Use genuine connectors.** Replace anonymous banana plugs with 5–5.5 mm bullets or XT60 hardware rated for the current draw; cheap clones melt under 30 A continuous loads.【F:knowledge/notes/denis_all_part02_review.md†L101695-L101722】
- **Strain-relieve charge taps.** Hot-glued or untied DC/DC leads snap from vibration—wrap them with zip ties or RTV and route along the controller wall before closing the deck.【F:knowledge/notes/denis_all_part02_review.md†L31-L32】【F:knowledge/notes/denis_all_part02_review.md†L966-L966】
- **Respect charge-port limits.** Never draw accessory power from the charge socket; build a Y-connector off the discharge rails so BMS protections remain intact.【F:knowledge/notes/denis_all_part02_review.md†L70-L71】【F:knowledge/notes/denis_all_part02_review.md†L122796-L122799】

## Firmware & Controller Notes
- **Locked dashboards demand hardware flashing.** Purple-case clone dashboards program safely at 3.3 V using ST-Link on the rear pads (SWDIO/SWCLK/GND/3V3); loading the wrong BLE image forces a reflash with Camilo’s "purple" package.【F:knowledge/notes/denis_all_part02_review.md†L93680-L93705】
- **Identify MCU families.** Newer Xiaomi controllers ship with GD32 chips—dump markings with magnification and flash GD-specific firmware images to avoid bricking the ESC.【F:knowledge/notes/denis_all_part02_review.md†L95680-L95780】
- **Plan for field-weakening limits.** Gen 1 controllers plateau around 32 km/h even with field weakening; serious speed gains require higher voltage, not just firmware tweaks.【F:knowledge/notes/denis_all_part02_review.md†L86739-L86747】
- **Maintain thermal interfaces.** Bolt controllers flat against the chassis with fresh paste and clear wiring; lifted plates overheat on the first long ride and can pinch brake hoses.【F:knowledge/notes/denis_all_part02_review.md†L101755-L101764】

## Energy Planning & Charging
- **Think in watt-hours.** Two 10S3P packs wired as 20S3P or 10S6P deliver similar Wh—the higher series count simply lowers current draw for the same power, easing cable heating.【F:knowledge/notes/denis_all_part02_review.md†L95313-L95357】
- **Emergency backfeeding only.** Using a 13S charger on a 12S stack is a one-time recovery tactic; daily charging demands proper CC/CV hardware matched to the pack.【F:knowledge/notes/denis_all_part02_review.md†L101776-L101787】
- **Validate pack claims.** Time the OEM charger (≈1.7 Ah per hour) to spot counterfeit "12 Ah" packs that top off too fast.【F:knowledge/notes/denis_all_part02_review.md†L98595-L98598】
- **Mind tubeless sealants.** PMT/Xuancheng tires seal without slime, but if you insist, pick aluminum-safe formulas to avoid corroding clone rims.【F:knowledge/notes/denis_all_part02_review.md†L101765-L101775】

## Risk & Safety Checklist
1. Voltage-match packs before plugging parallel harnesses together; log voltage after rides to verify they remain in lockstep.【F:knowledge/notes/denis_all_part02_review.md†L93548-L93558】
2. Keep mechanical brakes sharp—regen alone fails when controllers overheat or clones lack charge-path MOSFETs.【F:knowledge/notes/denis_all_part02_review.md†L99966-L99999】【F:knowledge/notes/denis_all_part02_review.md†L395-L395】
3. Inspect wiring after rain or transport; oxidation under the white battery plug causes power resets that mimic controller faults.【F:knowledge/notes/denis_all_part02_review.md†L87008-L87031】
4. Armor external packs mounted along the deck—exposed conduit runs become “self-propelled bombs” unless the housing resists impacts and houses permanent wiring.【F:knowledge/notes/denis_all_part02_review.md†L230-L234】
5. Document every harness change with photos so the next technician can trace custom Y-cables, XT60 extensions, and dashboard rewires without guesswork.【F:knowledge/notes/denis_all_part02_review.md†L93340-L93386】【F:knowledge/notes/denis_all_part02_review.md†L93680-L93705】
