# Accessory and UX Planning

## Display and Dashboard Options

- VESC lacks a built-in dashboard, so riders rely on the mobile app or third-party TFT units, although the stock screen is viewed as bulky and unattractive.[^dashboard_gap]
- Off-the-shelf TFTs can be zip-tied onto OEM dashboards or replaced entirely with phone mounts; some builders pursue 3D-printed housings and auxiliary handlebars for sturdier accessory mounting.[^tft_mounts]
- Comparative testing spans Davega X, Eye3-compatible ESP32 displays, and Flipsky TFT modules, with stealth installs that reuse factory casings to stay compliant with local regulations.[^display_comparison]
- Smart dashboard wishlists include ESP32 logic for mode toggles, legal-speed presets triggered by button combinations, and selecting CAN over UART to survive high-current noise environments.[^smart_dash_roadmap]

## Lighting Upgrades

- Riders trial 3 000–9 000 lm USB-C headlights that double as power banks, programmable LED tail lights, and 12 V mirror-mounted assemblies to overcome weak, glare-prone stock Xiaomi lamps.[^lighting_tests]

## Power Control Ergonomics

- The platform supports sleep mode, but implementing a physical power switch requires custom wiring; many builds still rely on anti-spark switches as manual cut-offs.[^sleep_wiring]

## Security & Immobilisers

- Spintend owners are actively hunting NFC-based locks so they can ditch physical keys on premium builds—document plug-and-play immobiliser options as soon as vetted hardware appears.[^nfc-lock]

[^dashboard_gap]: Source: knowledge/notes/input_part000_review.md, line 38.
[^tft_mounts]: Source: knowledge/notes/input_part000_review.md, line 46.
[^display_comparison]: Source: knowledge/notes/input_part000_review.md, line 57.
[^smart_dash_roadmap]: Source: knowledge/notes/input_part000_review.md, line 59.
[^lighting_tests]: Source: knowledge/notes/input_part000_review.md, line 47.
[^sleep_wiring]: Source: knowledge/notes/input_part000_review.md, line 45.
[^nfc-lock]: Source: knowledge/notes/input_part013_review.md†L723-L723
