# Knowledge Extraction Roadmap

## Reviewed so far

### `input_part000.json` (2021-04-02 23:23 – 2021-04-03 01:45 UTC)
- Captured the initial hardware shopping list that establishes the reference build (dual Flipsky 7550 controllers, V6 Bluetooth module, CAN bus harness, anti-spark protection, and supporting JST cabling).【F:data/raw/telegram_exports/vesc_help_group/input_part000.json†L120-L156】
- Logged early configuration context covering motor power, battery pack architecture (15s8p BMS limited to 40 A), and members' near-term voltage plans (running 13s with the option to scale to 15s).【F:data/raw/telegram_exports/vesc_help_group/input_part000.json†L320-L358】
- Noted firmware and current-limit advice, including links to 100 A and 300 A VESC firmware variants and cautionary guidance on warranty implications and throttle feel around 40 A battery current caps.【F:data/raw/telegram_exports/vesc_help_group/input_part000.json†L3130-L3188】
- Documented high-current experimentation that triggered large phase current deltas when battery amperage exceeded ~56 A, highlighting the need for clearer tuning guidelines and visual references shared in-chat.【F:data/raw/telegram_exports/vesc_help_group/input_part000.json†L4880-L4958】

## Where to continue
- Finish the remaining messages in `input_part000.json` after the 01:45 UTC window to ensure later discussions (pictures, tuning follow-ups) are captured before moving on.
- Process `input_part001.json` next, prioritising recurring questions about firmware, CAN bus wiring, and throttle mapping to build reusable FAQs.
- For each reviewed chunk, promote actionable guidance (e.g., hardware checklist, battery current tuning notes) into structured documents under `knowledge/processed/`, citing message IDs.
- Track outstanding clarifications—such as sourcing JST connectors and safe current thresholds—in the extraction log for targeted follow-up with subject-matter experts or additional chat context.

## Upcoming supporting tasks
- Extend the new `tools/telegram_to_text.py` script with tagging or filtering so reviewers can focus on specific topics (e.g., battery tuning, firmware updates) as they skim transcripts.
- Define metadata templates for the processed guides (hardware setup, firmware selection, battery tuning) to streamline future curation.
