# Accessory and UX Planning

## Display and Dashboard Options

- VESC lacks a built-in dashboard, so riders rely on the mobile app or third-party TFT units, although the stock screen is viewed as bulky and unattractive.[^dashboard_gap]
- Off-the-shelf TFTs can be zip-tied onto OEM dashboards or replaced entirely with phone mounts; some builders pursue 3D-printed housings and auxiliary handlebars for sturdier accessory mounting.[^tft_mounts]
- Comparative testing spans Davega X, Eye3-compatible ESP32 displays, and Flipsky TFT modules, with stealth installs that reuse factory casings to stay compliant with local regulations.[^display_comparison]
- Smart dashboard wishlists include ESP32 logic for mode toggles, legal-speed presets triggered by button combinations, and selecting CAN over UART to survive high-current noise environments.[^smart_dash_roadmap]

## Media Capture & Logging

- Insta360 cameras still provide native GPS overlays, whereas GoPro’s Hero 12 dropped the feature, so riders chasing on-screen speed data favour Insta360 hardware for documentation runs.[^insta360]

## Lighting Upgrades

- Riders trial 3 000–9 000 lm USB-C headlights that double as power banks, programmable LED tail lights, and 12 V mirror-mounted assemblies to overcome weak, glare-prone stock Xiaomi lamps.[^lighting_tests]
- When pack marketing claims prove inflated, commuters repack MagicShine-style lights with quality 18650/21700 cells or jump to budget 5×P90 AliExpress headlights so night rides aren’t riding on dying “10 000 mAh” packs.[^magicshine_repack]
- Compact, E-marked motorcycle turn signals from AliExpress pair cleanly with dedicated DC-DC converters when you need discreet road-legal flashers on scooter builds.[^emark_signals]
- 🇪🇸AYO#74’s parts list now includes low-cost motorcycle brake lights, waterproof COB strips, and inline three-button dimmers that drop straight onto 12 V rails or reducers for custom lighting suites.[^ayo_lighting]

## Power Control Ergonomics

- The platform supports sleep mode, but implementing a physical power switch requires custom wiring; many builds still rely on anti-spark switches as manual cut-offs.[^sleep_wiring]

[^dashboard_gap]: Source: knowledge/notes/input_part000_review.md, line 38.
[^tft_mounts]: Source: knowledge/notes/input_part000_review.md, line 46.
[^display_comparison]: Source: knowledge/notes/input_part000_review.md, line 57.
[^smart_dash_roadmap]: Source: knowledge/notes/input_part000_review.md, line 59.
[^lighting_tests]: Source: knowledge/notes/input_part000_review.md, line 47.
[^sleep_wiring]: Source: knowledge/notes/input_part000_review.md, line 45.
[^magicshine_repack]: Source: knowledge/notes/input_part010_review.md†L418-L419
[^emark_signals]: Source: knowledge/notes/input_part010_review.md†L585-L585
[^ayo_lighting]: Source: knowledge/notes/input_part010_review.md†L587-L590
[^insta360]: Source: knowledge/notes/input_part010_review.md†L629-L630
