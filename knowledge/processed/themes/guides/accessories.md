# Accessory and UX Planning

## Display and Dashboard Options

- VESC lacks a built-in dashboard, so riders rely on the mobile app or third-party TFT units, although the stock screen is viewed as bulky and unattractive.[^dashboard_gap]
- Off-the-shelf TFTs can be zip-tied onto OEM dashboards or replaced entirely with phone mounts; some builders pursue 3D-printed housings and auxiliary handlebars for sturdier accessory mounting.[^tft_mounts]
- Comparative testing spans Davega X, Eye3-compatible ESP32 displays, and Flipsky TFT modules, with stealth installs that reuse factory casings to stay compliant with local regulations.[^display_comparison]
- Smart dashboard wishlists include ESP32 logic for mode toggles, legal-speed presets triggered by button combinations, and selecting CAN over UART to survive high-current noise environments.[^smart_dash_roadmap]
- Arduino-driven dashboards are emerging for VESC swaps—Koxx demoed a Xiaomi running custom VESC firmware with an auxiliary microcontroller handling display duties, proving open hardware can backfill Rita telemetry gaps.[^vesc-arduino-dash]

## Lighting Upgrades

- Riders trial 3 000–9 000 lm USB-C headlights that double as power banks, programmable LED tail lights, and 12 V mirror-mounted assemblies to overcome weak, glare-prone stock Xiaomi lamps.[^lighting_tests]
- Xiaomi’s rear light rail only delivers ~3–5 V with tight current limiting, so bright LED strips need a separate 5 V/12 V buck or relay off the controller; otherwise you’re limited to careful lens alignment on the stock rail.[^denis-tail-rail]
- Dense LED strips can pull ~10 A at 5 V (≈100 LED/m), so plan dedicated DC/DC converters with enable pins or pivot to electroluminescent tape to avoid overloading scooter accessory rails.[^led-strip-load]

## Security & Tracking Concepts

- Denis is prototyping plug-and-play tracker/immobilizer modules with onboard 5 V supplies, fingerprint readers, and alarm speakers so scooters can sound off or cut power when moved without authorisation.[^denis-tracker-proto]
- Hidden trackers should run through a low-dropout regulator such as an AMS1117-3.3, fed directly from the main battery because Xiaomi controllers lack standby 5 V rails.[^denis-tracker-ldo]

## Power Control Ergonomics

- The platform supports sleep mode, but implementing a physical power switch requires custom wiring; many builds still rely on anti-spark switches as manual cut-offs.[^sleep_wiring]

## Winter Comfort Planning

- Heated grips borrow power directly from the scooter pack and stay convenient for long rides, while heated gloves add off-scooter utility but require charging routines and extra wiring bulk.[^heated-grips]

[^dashboard_gap]: Source: knowledge/notes/input_part000_review.md, line 38.
[^tft_mounts]: Source: knowledge/notes/input_part000_review.md, line 46.
[^display_comparison]: Source: knowledge/notes/input_part000_review.md, line 57.
[^smart_dash_roadmap]: Source: knowledge/notes/input_part000_review.md, line 59.
[^lighting_tests]: Source: knowledge/notes/input_part000_review.md, line 47.
[^sleep_wiring]: Source: knowledge/notes/input_part000_review.md, line 45.
[^denis-tail-rail]: Source: knowledge/notes/denis_all_part02_review.md†L704-L704
[^denis-tracker-proto]: Source: knowledge/notes/denis_all_part02_review.md†L932-L932
[^denis-tracker-ldo]: Source: knowledge/notes/denis_all_part02_review.md†L934-L934
[^vesc-arduino-dash]: Source: knowledge/notes/denis_all_part02_review.md†L1043-L1043
[^led-strip-load]: Source: knowledge/notes/denis_all_part02_review.md†L1044-L1044
[^heated-grips]: Source: knowledge/notes/denis_all_part02_review.md†L1048-L1048
