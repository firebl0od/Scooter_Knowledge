# Xiaomi Battery Maintenance & Recovery Playbook

## TL;DR

- **Balance stubborn packs externally before blaming the BMS.** Clip TP4056 or lab-charger leads onto the weakest parallel groups without removing the board.
  - severely unbalanced M365 packs usually recover once every group tops off within a few millivolts.[^1]
- **Legacy tooling still expects legacy firmware.** Downgrade BLE dashboards to 073/090 so the M365 BMS Tool or ScooterHacking Utility can talk to Rita, Happy BMS, or stock packs without throwing spurious error 21 warnings.[^2][^3]
- **Plan for 30 A-class current, not miracles.** Happy BMS hard-stops around 44 A, Rita beeps at ~30 A, and Xiaomi controllers trip above ~27 A unless reinforced, so size packs, wiring, and brakes for realistic loads rather than marketing fantasy.[^4][^5][^6]
- **Charging mods demand instrumentation.** Raising stock chargers to 50.4–54.6 V works, but monitor voltage manually.
  - backfeeding through XT30 bypasses Happy BMS protection, and regen or chargers above 30 A spike Rita or controller MOSFETs.[^7][^8][^9]
- **Document every recovery attempt.** Keep an ST-Link v2 on hand, log live current before chasing Rita error 39, and probe MOSFET continuity with packs disconnected to catch shorts before reinstalling a battery.[^10][^11][^12]
- **Model upgrades around stock chemistries.** Xiaomi packs usually ship with LG M26 or blue EVE 18650 cells.
  - plan range and sag using those discharge curves rather than assuming MJ1-class performance.[^13]

## Balancing & State-of-Charge Management

| Scenario | Action | Why it Matters |
| --- | --- | --- |
| Pack delta >150 mV | Use TP4056 boards or a bench supply with crocodile clips to top each weak parallel group before reconnecting the charger; leave the BMS in-circuit so protections stay active.[^1] | Prevents unnecessary BMS swaps and restores balance after deep storage. |
| Pack voltages match but output stays weak | Probe each sensing capacitor—failed RC networks on Xiaomi BMS boards starve current despite balanced cells. Replace any capacitor that doesn’t mirror its cell voltage.[^denis-bms-capacitors] | Restores pack output without rebuilding the entire battery. |
| Happy BMS pack reads 0 % with energy remaining | Keep riding cautiously.
  - its coulomb counter saturates near 32 Ah but ~3 Ah remain; recalibrate during the next full charge cycle.[^14][^15] | Avoids panic over false-empty displays on oversized packs. |
| Dash shows ≈91 % at 50.1 V on a 12S pack | Treat it as a UI quirk.
  - the pack is effectively full even though the percentage lags. | Prevents unnecessary troubleshooting when full-charge voltage already confirms capacity.[^16] |
| Pack rests around 3.0–3.3 V per cell and refuses to charge | Treat the cutoff as normal Happy/Ninebot protection; bring voltage up gently and resume balancing before chasing a BMS replacement.[^17] | Prevents unnecessary board swaps when the pack simply hit its low-voltage guardrail. |
| BMS emulation hides error 21 but charger still blinks | Inspect the battery for imbalance instead of reflashing.
  - bypassing the data line never fixes mismatched cell groups.[^18] | Prevents overcharging damaged packs behind spoofed telemetry. |
| Cell groups replaced piecemeal | Rebuild the entire pack; mixed-age cells fall out of balance quickly and waste the repair effort.[^19] | Ensures parallel groups age uniformly after service. |
| External tops off while the internal pack refuses to charge | Failed OEM temperature sensors often lock the stock BMS; disconnect Rita, test both probes, and replace the bad sensor before condemning the adapter.[^20] | Restores normal charge sharing without unnecessary adapter swaps. |
| Repaired packs refuse to balance quickly | Xiaomi BMS boards only bleed around 30 mA; leave the pack on charge overnight or top the low group with a bench supply after disconnecting the BMS.[^denis-balance-slow] | Prevents chasing phantom faults when balance current is simply limited. |
| Refurbished 16 S packs | Manual 0.5 A top-balancing over a week restored ~35 Ah; Xiaomi-class BMS boards barely balance, so plan periodic manual balancing or cell replacements for long-term health.[^denis-manual-balance] | Keeps recycled packs reliable despite weak onboard balancing. |
| Suspect replacement capacity | Time a full charge with the OEM 1.7 A brick.
  - each hour adds ≈1.7 Ah, so a genuine 12 Ah Pro 2 pack should take close to seven hours from empty.[^21] | Confirms marketing claims without opening the case. |
| Charger finishes instantly on a new Happy pack | Wake the BMS with a brief charge pulse; XT60 output remains off until the board sees a charger once.[^22] | Prevents unnecessary teardowns when a fresh build appears dead on arrival. |
| Pack went dark after water ingress | Dry the battery for a week and jump-start with the charger—rear fender grommet leaks can recover without swapping the BMS.[^denis-water-dry] | Saves healthy packs that only tripped after moisture exposure. |
| Long-term storage | Expect ≈0.6 %/day self-discharge on Happy BMS packs.
  - wake them with a charger pulse before use, park Xiaomi packs around 3.7–3.8 V, and keep them above freezing before charging.[^23][^24][^25] | Keeps firmware accurate and cells healthy in winter climates. |
| Emulator shows “empty” near 3.4 V/cell | Treat the warning as conservative.
  - Rita-compatible emulators still shout 0 % even with cutoff set lower, so keep manual voltage checks or a buffer when riding on emulation alone.[^26] | Avoids unnecessary rescues when plenty of voltage remains. |

### Temperature Guardrails

- Charge between ~5 °C and 55 °C; brief 28–29 °C top-offs are fine, but let cold-soaked packs warm before plugging in to avoid plating.[^24]
- When Happy BMS detects ≥40 °C during charging it pauses until the pack cools near 35 °C—provide airflow instead of assuming a fault.[^27]
- Winter commutes can double energy use (~30 Wh/km vs. 18–20 Wh/km); keep packs warm indoors or add gentle heaters so cold batteries deliver rated capacity.[^28]

### Water Intrusion & Corrosion Checks

- Water-damaged M365 packs often recover after flushing the BMS with isopropyl alcohol; if telemetry still misreports, Denis keeps compatible replacements ready.[^29]
- Error 28 beeps often trace to a shorted high-side MOSFET after water ingress; repeated wet/dry cycles leave pink stickers and white corrosion, so swap the controller instead of chasing intermittent faults.[^30]
- Power resets and false-low battery readings usually come from oxidation under the white battery plug.
  - flush with contact cleaner, dry thoroughly, and improve sealing before riding in rain again.[^31]

## Firmware & Diagnostic Workflow

1. **Restore communications first.** Downgrade BLE, close competing apps, and, if a custom dash sits inline, place it in update mode so Rita/Happy can negotiate over the data line.[^2][^32]
2. **Keep an ST-Link kit.** Four clip leads and the stock firmware image recover most soft-bricked controllers; late G30 dashboards now require ST-Link flashes to bypass OTA locks.[^10][^33]
3. **Rescue Mi3 dashboards with legacy firmware.** When BMS Tool refuses to connect, confirm BLE/UUID pairs via m365_DownG or Xiaodash before flashing—Mi Home–locked boards simply reboot until the handshake matches—then load DRV016 alongside NGFW’s model-lock removal via Scooter Hacking Utility and source matching BLE files from mp365.es until broader support lands.[^34][^mi3-uuid]
- **Replace burnt R43 data resistors.** Lost battery bars on M365 Pro packs usually trace to the controller’s ≈120 Ω R43 resistor; swap it instead of blaming the BMS.[^denis-r43]
4. **Probe before power.** With the pack unplugged, meter between battery rails and each phase.
  - anything under ~50 Ω points to a shorted MOSFET that needs replacement before reconnecting cells.[^12]
5. **Log live current.** Rita error 39 and Happy BMS trips often show up when firmware pulls past ~30 A; capture data with m365Tools or XiaoDash before reducing current limits.[^11][^35]
6. **Respect hall geometry.** Glue replacement sensors exactly where stock ICs sat and retain isolation pads when reassembling heat sinks to avoid losing 10 km/h or shorting MOSFETs to the case.[^36]
- **Swap error 21 resistors after impacts.** Rock strikes that burn the controller’s tiny BMS resistor call for a fresh 0805 part around 100–150 Ω rather than leaving it shorted.[^denis-error21]
- **Log MOSFET part numbers before repairs.** Genuine Xiaomi BMS boards use MDE1932 or HY4008 devices rated 120–200 A; cheap clones ship 4 A parts that fail under load, so match replacements accordingly.[^denis-bms-mosfet]
- **Chase cruise-control dropouts at the harness.** Cruise glitches after a Rita install usually mean loose display-to-controller wiring or pinched harnesses inside tight Essential builds.[^denis-cruise]

- **Clear Happy BMS error 24 with a 10 S assist.** Scootermode’s 14 S conversions recover once you flash the firmware while a 10 S pack stays connected, and remember Xiaomi throttles ignore input until the wheel spins slightly after boot.[^happy-error24]

### BMS Reset & Hardware Recovery

- **Use the onboard reset before replacement.** A Pro pack that refuses to charge after overheating often revives by opening the case and pressing the BMS’s tactile button; if LEDs still blink red/green, charge through Rita’s XT30 to confirm whether the internal charge path failed.[^37]
- **Solid blue LEDs usually point to the BMS.** Pop the case, reset or inspect the board, and rule out condensation or controller faults before declaring the pack dead.[^blue_led_reset]
- **Read the BMS LED before swapping hardware.** A steady red indicator or floating sense wire explains many externals that still ride but refuse to charge; re-seat the harness before blaming the charger.[^bms_led_indicator]
- **Use the onboard reset before replacement.** A 10-second press on the BMS tactile button often revives “dead” Pro 2 packs; if LEDs still blink red/green afterward, log per-cell voltages and charge through Rita’s XT30 to confirm whether the internal path failed.[^37][^denis-bms-button]
- **Fall back to the XT30 harness when diagnosing.** When the stock charge inlet won’t engage, top the pack via Rita’s XT30 while testing.
  - owners rotate between charge jack and XT30 until a failing BMS or harness is replaced.[^38][^39]
- **Split factory shells methodically.** Slice both bottom seams, warm the glue, and drift the brick out before metering CF-series capacitors.
  - imbalances often trace back to failed caps that should read infinite resistance.[^40]
- **Meter every group before reviving storage-drained packs.** Denis still checks each series string prior to kick-starting through the discharge port so weak groups don’t get over-driven during recovery.[^revive-groups]

## Charging & Hardware Upgrades

- **Charger mods:** Swapping the stock TL431 feedback network (e.g., two 33 kΩ plus 100 kΩ with a 16 kΩ 0805) and upgrading output capacitors to 100 V lifts Xiaomi bricks toward 57.5 V; meter the result before plugging into a pack.[^41][^7]
- **Respect the charge port ceiling:** The factory Xiaomi inlet safely handles ≈3 A; bigger bricks heat the harness unless you upgrade wiring and connectors, so 42 V 3 A chargers remain the practical limit on stock hardware.[^42]
- **Refresh tired charge leads before blaming the jack.** A “burned” 3 A port turned out to have cooked wiring.
  - replace the short pigtail with heavier (~24 AWG) leads and inspect the socket for looseness once plastic melts.[^43]
- **Verify polarity on replacement charge ports.** Multiple “won’t charge” cases traced back to aftermarket jacks shipped with reversed leads or loose harness connectors that only Rita exposed; refit the OEM inlet before condemning the pack.[^charge_port_polarity]
- **Upgrade charge connectors when raising current:** Swap the slim JST input for XT30/XT60 or XT90S hardware before running 5 A chargers, solder and heat-shrink every joint, and keep JST-only harnesses below ≈3 A even when paralleled for balancing.[^44][^45]
- **Remember the XT30 still works without data.** The stock Xiaomi battery powers accessories and charges through its XT30 even if the data ribbon is disconnected.[^denis-xt30]
- **Treat 13 S chargers on 12 S packs as emergency tools.** They only stay safe while the BMS holds; unplug early or run a timer rather than trusting protection to catch an overcharge.[^13s-emergency]
- **Parallel dual-pack charge leads correctly.** Two male JSTs feeding one female keep both BMS boards balancing; expect the internal BMS to blink red until cells settle before reconnection.[^parallel-jst]
- **Tame DC step-up chargers:** Start with output voltage below pack voltage, connect, then ramp to ≈1 A before adjusting the current-limit pot to avoid sparks and overheated LEDs.[^46]
- **Trust vetted CC/CV bricks:** Anonymous “48 V” chargers frequently skip documented CC/CV stages; the workshop sticks with YZPOWER 13 S supplies and soldered connector swaps instead of taped adapters.[^47]
- **Raise Happy BMS charge ceilings before using 5 A bricks:** Stock firmware blocks chargers above ~3 A; increase the limit to ~5.5 A in Embedden BMS Tool so Rita’s harness survives heavier charging.[^48]
- **Set Rita’s series count before charging and watch charger sag.** Temperature icons clear once the adapter knows whether a 10 S or 12 S external is attached, and suspect chargers that look fine open-circuit can droop toward 40 V under load, starving the auxiliary pack.[^rita-series][^charger-sag]
- **Voltage limits:** Happy BMS tolerates 54.6 V chargers on 14 S packs.
  - it simply stops early
  - while Rita sequences mixed voltages by capping the internal pack around 42 V before finishing the higher-voltage external.[^49][^50]
- **Direct-to-XT30 charging:** Topping a Happy-equipped pack via the controller lead works in emergencies but bypasses over-voltage protection.
  - monitor manually and disconnect once you hit the target voltage.[^8]
- **Plan separate chargers when mixing 36 V and 48 V externals.** Rita only links an auxiliary pack once its voltage matches the internal battery, so mismatched stacks need patience or individual wall chargers.[^mixed-voltage-charge]
- **Backfeeding depleted packs:** Only nudge a 44 V pack with a 36 V charger when its open-circuit voltage sits under ~41 V; otherwise you risk over-voltage damage.[^12]
- **Accessory power:** Dashboards expose just 5 V logic.
  - use dedicated DC/DC converters for 12 V lighting, stress-relieve converter leads with RTV or zip ties, and avoid pulling power from charge ports to keep protections intact.[^51][^52]
- **Step-down LED strips:** Most consumer LED kits are rated ≤24 V; use a buck converter when tapping scooter packs because direct 36 V feeds cook the strip and risk shorts.[^53]
- **Swap flaky “purple” dashboards:** If headlights sag throttle voltage and cap speed, replace the dash.
  - regen current into 36–40 V lamps is safe, but faulty boards throttle output under load.[^54]

## Safety & Upgrade Guardrails

- **Pack selection:** Skip unbelievable “13S4P 60 Ah” or €60 “48 V 62 Ah” packs.
  - the chemistry doesn’t exist and bargain controllers rarely survive 48 V; invest in reputable 12–13 S builds instead.[^55][^56]
- **Treat Daly’s 30 A revision as a downgrade.** New batches use weaker MOSFETs that fail in series connections, so dual-pack scooters stick with 40 A models until Daly resolves the issue.[^denis-daly30]
- **Rita is not a replacement BMS.** External packs still need their own common-port protection, fuses, and sound wiring—otherwise Rita blows its fuse and Happy BMS blocks output once shorts are detected.[^rita-not-bms]
- **Balance heavy front packs before committing.** A 36 V 25 Ah Wildman-mounted pack shifted steering noticeably; test geometry before strapping big batteries to the head tube.[^front-pack-balance]
- **Rebuild weak groups completely.** Replace tired cells, spot-weld fresh nickel, and reseal with non-conductive silicone before trusting a repaired pack; confirm balance again after a few cycles.[^denis-repair]
- **Respect 52 V externals.** Doubling voltage demands reinforced controllers and motors before pairing high-voltage packs with Xiaomi drivetrains.[^denis-52v]
- **Treat “fire emoji” AliExpress packs as suspect.** Riders keep finding laptop-pull bricks that sag early.
  - Denis caps Happy BMS builds near 53 V/40 A and leans on refurbished OEM modules instead of forcing Rita past spec.[^57]
- **Audit Aerdu shipments.** Some owners praise 12 Ah externals while others log imbalance and safety issues—veterans steer EU builders toward Scootermode or Denis’ packs despite higher cost.[^denis-aerdu]
- **Plan Pro 12 Ah transplants carefully.** The aluminum shell must come off to fit Xiaomi frames, and many riders now spec custom 10S3P/21700 packs in the stock housing or pay reputable builders when the trim work looks marginal.[^denis-pro12]
- **Dispute fantasy externals.** Genuine 10 Ah 36 V packs use roughly 40 quality cells (~€70 in cells alone); “30 Ah” bricks that fall to 6 % under load are condemned as unsafe, and repurposed Xiaomi packs should be disconnected for every charge if you insist on using them externally.[^external-myths]
- **Keep Pro 2 BMS firmware on build 126.** Newer stock firmware caps charge around 40.5 V; staying on 126 keeps the full 42 V ceiling and preserves capacity labels (12,400 vs. 12,800 mAh).[^pro2-126]
- **Leave regen headroom.** Stop charging around 95–97 % before long descents; regen on a full battery still cooks MOSFETs, so disable aggressive KERS if needed and disconnect Rita while diagnosing shorted controllers.[^regen-headroom]
- **Keep the internal pack online for braking.** Hard stops on a full external pack without the OEM battery attached dump regen into Rita and can destroy the module—wire packs in parallel or leave the stock battery connected.[^denis-regen]
- **Cell choices:** Refurbished Samsung 35E/50E lots from vetted sellers such as NKON remain viable midlife upgrades.
  - document provenance and avoid mixing them with tired cells from the original pack.[^58]
- **Know pouch-cell trade-offs.** Cylindrical cells tend to fail open when abused, while pouch cells demand constant compression and can vent violently if overcharged.
  - reserve pouch experiments for builders with proper fixtures and monitoring.[^58]
- **Respect chemistry pairings:** Gabe’s 800 W Blade plan combines a fresh 13s5p LG MH1 block with a 3s6p stack of retired EVE ES2 cells to stretch range; treat that as a low-amp experiment, log temps, and expect sag differences compared with the P42A packs he reserves for dual 22×3 80100 race builds.[^59]
- **Know platform limits.** Xiaomi Mi 3/Mi 4 scooters ship with locked firmware, top-entry decks, and warranty-sensitive hardware, so most modders stick with the older Pro series when they need deep battery or controller swaps.[^60]
- **Brake planning:** 12 S conversions hit ~40 km/h on flat ground.
  - upgrade mechanical brakes and keep regen under ~20 A so Rita and controller FETs stay alive.[^61][^62]
- **Controller heat path:** Torque down stock controllers flush to the chassis with fresh thermal paste; loose mounting or cable stacks overheat MOSFETs on the first long ride.[^63]
- **Parallel etiquette:** Only parallel packs with matched voltages and common-port BMS boards.
  - Rita and Happy both block or fault when faced with mismatched hardware.[^64][^65][^66]
- **Don’t rely on “open” BMS data lines.** M365/Pro boards fall back to ≈20 A discharge when telemetry is disconnected or voltage checks are disabled; keep the data link alive for >20 A builds.[^denis-20a]
- **Never tie 48 V and 36 V packs directly together.** The workshop treats Rita as the only safe bridge.
  - direct paralling dumps current violently and risks pack fires.[^67]
- **LiPo discipline:** RC LiPo bricks puff when stored at full charge and develop high internal resistance within days.
  - treat them as short-term boosters, not daily commuter batteries.[^68]
- **Respect BMS ceilings.** Even 80 A-capable cells sag and trip protection if the pack still uses a 40 A BMS.
  - raise ratings alongside parallel count to avoid false cut-outs.[^69]
- **Respond quickly to regen-induced faults.** A regen-heavy stop without Rita scorched a customer’s BMS and controller.
  - disconnect immediately, recharge sub-2 V cells individually, and tidy sloppy sensor wiring before condemning hardware.[^70]
- **Treat headlight-triggered brownouts as BMS clues.** If toggling lights kills the dash or cuts throttle, test with a known-good pack, inspect every parallel group, and replace fuses before blaming the scooter electronics.[^71]
- **Environmental prep:** Seal deck seams, cable ports, and hub joints with silicone plus lithium grease; add humidity sensors or alarms if you commute in heavy rain.[^72][^73]

### Sleeper Packaging Templates

- **Xiaomi Pro 2 20 S sleeper layout.** Gabe splits the 20 S 8 P pack between the deck and an external bag, prints 35–36 mm spacers, reroutes phase cables, and trims foam so dual controllers coexist without killing ground clearance.
  - document the weight distribution before copying the build.[^74]
- **Mind 2021+ Pro 2 packaging.** Newer decks squeeze Rita and can pinch folding hinges or cable bundles; mount the adapter lower and remember the display only reports 12 S pack voltage accurately while the 10 S internal reads high.[^denis-pro2]

## Commissioning Checklist

1. **Balance & inspect cells** before closing the pack, replacing entire groups rather than mixing fresh with aged cells.[^1][^19]
2. **Update firmware and dashboards** with BLE downgrades, ST-Link backups, and Rita/Happy configuration before connecting higher-voltage packs.[^10][^75]
3. **Set conservative current limits:** cap battery current ≈25–28 A, regen below 20 A, and confirm logs show <30 A through Rita or Happy BMS during shakedowns.[^5][^11]
4. **Validate charging paths**.
  - meter chargers after resistor swaps, confirm Happy BMS accepts the amperage limit you expect, and never rely on charge-port power for accessories.[^7][^76][^52]
5. **Log first rides** with m365Tools or XiaoDash, watching pack temperature, voltage sag, and current spikes so you can dial back settings before hardware fails.[^77][^11]


## References

[^1]: Source: knowledge/notes/all_part01_review.md†L10-L11
[^2]: Source: knowledge/notes/all_part01_review.md†L12
[^3]: Source: knowledge/notes/denis_all_part02_review.md†L543-L544
[^4]: Source: knowledge/notes/denis_all_part02_review.md†L11-L12
[^5]: Source: knowledge/notes/all_part01_review.md†L79-L81
[^6]: Source: knowledge/notes/denis_all_part02_review.md†L73-L74
[^7]: Source: knowledge/notes/all_part01_review.md†L221-L224
[^8]: Source: knowledge/notes/denis_all_part02_review.md†L185-L186
[^9]: Source: knowledge/notes/denis_all_part02_review.md†L125-L126
[^10]: Source: knowledge/notes/all_part01_review.md†L46-L49
[^11]: Source: knowledge/notes/denis_all_part02_review.md†L55-L57
[^12]: Source: knowledge/notes/denis_all_part02_review.md†L37-L38
[^13]: Source: knowledge/notes/all_part01_review.md†L88335-L88345
[^14]: Source: knowledge/notes/denis_all_part02_review.md†L16-L17
[^15]: Source: knowledge/notes/denis_all_part02_review.md†L399-L401
[^16]: Source: knowledge/notes/all_part01_review.md†L361-L361
[^17]: Source: knowledge/notes/denis_all_part02_review.md†L101-L101
[^18]: Source: knowledge/notes/denis_all_part02_review.md†L19-L20
[^19]: Source: knowledge/notes/denis_all_part02_review.md†L67-L68
[^20]: Source: knowledge/notes/denis_all_part02_review.md†L505-L505
[^21]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L98595-L98598
[^22]: Source: knowledge/notes/denis_all_part02_review.md†L376-L376
[^23]: Source: knowledge/notes/denis_all_part02_review.md†L479-L481
[^24]: Source: knowledge/notes/denis_all_part02_review.md†L46-L47
[^25]: Source: knowledge/notes/all_part01_review.md†L107120-L107130
[^26]: Source: knowledge/notes/denis_all_part02_review.md†L402-L402
[^27]: Source: knowledge/notes/denis_all_part02_review.md†L316-L316
[^28]: Source: knowledge/notes/denis_all_part02_review.md†L161-L165
[^29]: Source: knowledge/notes/all_part01_review.md†L155-L155
[^30]: Source: knowledge/notes/denis_all_part02_review.md†L307-L308
[^31]: Source: knowledge/notes/denis_all_part02_review.md†L309-L309
[^32]: Source: knowledge/notes/all_part01_review.md†L48
[^33]: Source: knowledge/notes/denis_all_part02_review.md†L103-L104
[^34]: Source: knowledge/notes/denis_all_part02_review.md†L85-L86
[^mi3-uuid]: Source: knowledge/notes/denis_all_part02_review.md†L545-L545
[^35]: Source: knowledge/notes/denis_all_part02_review.md†L618-L618
[^36]: Source: knowledge/notes/denis_all_part02_review.md†L40-L41
[^happy-error24]: Source: knowledge/notes/denis_all_part02_review.md†L544-L544
[^37]: Source: knowledge/notes/all_part01_review.md†L107001-L107105
[^blue_led_reset]: Source: knowledge/notes/all_part01_review.md†L611-L611
[^charge_port_polarity]: Source: knowledge/notes/all_part01_review.md†L804-L804
[^bms_led_indicator]: Source: knowledge/notes/all_part01_review.md†L850-L850
[^38]: Source: knowledge/notes/all_part01_review.md†L107545-L107548
[^39]: Source: knowledge/notes/all_part01_review.md†L107577-L107586
[^40]: Source: knowledge/notes/denis_all_part02_review.md†L496-L497
[^revive-groups]: Source: knowledge/notes/denis_all_part02_review.md†L566-L566
[^41]: Source: knowledge/notes/denis_all_part02_review.md†L585-L586
[^42]: Source: knowledge/notes/all_part01_review.md†L97910-L97915
[^43]: Source: knowledge/notes/denis_all_part02_review.md†L399-L400
[^44]: Source: knowledge/notes/denis_all_part02_review.md†L510-L510
[^45]: Source: knowledge/notes/denis_all_part02_review.md†L540-L541
[^46]: Source: knowledge/notes/denis_all_part02_review.md†L537-L537
[^13s-emergency]: Source: knowledge/notes/denis_all_part02_review.md†L509-L509
[^parallel-jst]: Source: knowledge/notes/denis_all_part02_review.md†L540-L540
[^rita-series]: Source: knowledge/notes/denis_all_part02_review.md†L565-L565
[^charger-sag]: Source: knowledge/notes/denis_all_part02_review.md†L565-L565
[^47]: Source: knowledge/notes/denis_all_part02_review.md†L598-L600
[^denis-r43]: Source: knowledge/notes/denis_all_part02_review.md†L675-L675
[^denis-error21]: Source: knowledge/notes/denis_all_part02_review.md†L636-L636
[^denis-bms-mosfet]: Source: knowledge/notes/denis_all_part02_review.md†L1069-L1069
[^denis-cruise]: Source: knowledge/notes/denis_all_part02_review.md†L639-L639
[^denis-balance-slow]: Source: knowledge/notes/denis_all_part02_review.md†L696-L696
[^denis-manual-balance]: Source: knowledge/notes/denis_all_part02_review.md†L1070-L1070
[^denis-xt30]: Source: knowledge/notes/denis_all_part02_review.md†L677-L677
[^denis-daly30]: Source: knowledge/notes/denis_all_part02_review.md†L674-L674
[^denis-repair]: Source: knowledge/notes/denis_all_part02_review.md†L678-L678
[^denis-52v]: Source: knowledge/notes/denis_all_part02_review.md†L676-L676
[^denis-regen]: Source: knowledge/notes/denis_all_part02_review.md†L694-L694
[^denis-20a]: Source: knowledge/notes/denis_all_part02_review.md†L697-L697
[^denis-aerdu]: Source: knowledge/notes/denis_all_part02_review.md†L692-L692
[^denis-pro12]: Source: knowledge/notes/denis_all_part02_review.md†L690-L691
[^denis-pro2]: Source: knowledge/notes/denis_all_part02_review.md†L637-L637
[^48]: Source: knowledge/notes/denis_all_part02_review.md†L476-L476
[^49]: Source: knowledge/notes/denis_all_part02_review.md†L345-L345
[^50]: Source: knowledge/notes/all_part01_review.md†L112-L112
[^51]: Source: knowledge/notes/denis_all_part02_review.md†L28-L32
[^52]: Source: knowledge/notes/denis_all_part02_review.md†L70-L71
[^53]: Source: knowledge/notes/all_part01_review.md†L156-L156
[^54]: Source: knowledge/notes/denis_all_part02_review.md†L486-L487
[^55]: Source: knowledge/notes/all_part01_review.md†L39-L40
[^56]: Source: knowledge/notes/denis_all_part02_review.md†L146-L147
[^57]: Source: knowledge/notes/denis_all_part02_review.md†L458-L459
[^rita-not-bms]: Source: knowledge/notes/denis_all_part02_review.md†L532-L533
[^front-pack-balance]: Source: knowledge/notes/denis_all_part02_review.md†L531-L531
[^external-myths]: Source: knowledge/notes/denis_all_part02_review.md†L533-L533
[^pro2-126]: Source: knowledge/notes/denis_all_part02_review.md†L559-L559
[^regen-headroom]: Source: knowledge/notes/denis_all_part02_review.md†L564-L564
[^58]: Source: data/E-scooter upgrade workshop by denis yurev/text_slices/all.part02.txt†L97241-L97259
[^59]: Source: data/vesc_help_group/text_slices/input_part007.txt†L495-L599
[^60]: Source: knowledge/notes/input_part007_review.md†L513-L513
[^61]: Source: knowledge/notes/all_part01_review.md†L44-L44
[^62]: Source: knowledge/notes/all_part01_review.md†L79-L80
[^63]: Source: knowledge/notes/denis_all_part02_review.md†L140-L141
[^64]: Source: knowledge/notes/all_part01_review.md†L102-L113
[^65]: Source: knowledge/notes/denis_all_part02_review.md†L64-L65
[^66]: Source: knowledge/notes/denis_all_part02_review.md†L532-L532
[^67]: Source: knowledge/notes/denis_all_part02_review.md†L508-L508
[^mixed-voltage-charge]: Source: knowledge/notes/denis_all_part02_review.md†L601-L601
[^68]: Source: knowledge/notes/denis_all_part02_review.md†L158-L159
[^69]: Source: knowledge/notes/all_part01_review.md†L93571-L93578
[^70]: Source: knowledge/notes/all_part01_review.md†L157-L157
[^71]: Source: knowledge/notes/all_part01_review.md†L158-L158
[^72]: Source: knowledge/notes/all_part01_review.md†L41-L41
[^73]: Source: knowledge/notes/all_part01_review.md†L86-L88
[^74]: Source: knowledge/notes/input_part007_review.md†L514-L514
[^75]: Source: knowledge/notes/all_part01_review.md†L119-L119
[^76]: Source: knowledge/notes/denis_all_part02_review.md†L476-L477
[^77]: Source: knowledge/notes/all_part01_review.md†L105-L105
[^denis-bms-capacitors]: Source: knowledge/notes/denis_all_part02_review.md†L923-L923
[^denis-water-dry]: Source: knowledge/notes/denis_all_part02_review.md†L924-L924
[^denis-bms-button]: Source: knowledge/notes/denis_all_part02_review.md†L983-L983
