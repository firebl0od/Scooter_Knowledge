# Accessory and UX Planning

## Display and Dashboard Options

- VESC lacks a built-in dashboard, so riders rely on the mobile app or third-party TFT units, although the stock screen is viewed as bulky and unattractive.[^dashboard_gap]
- Off-the-shelf TFTs can be zip-tied onto OEM dashboards or replaced entirely with phone mounts; some builders pursue 3D-printed housings and auxiliary handlebars for sturdier accessory mounting.[^tft_mounts]
- Comparative testing spans Davega X, Eye3-compatible ESP32 displays, and Flipsky TFT modules, with stealth installs that reuse factory casings to stay compliant with local regulations.[^display_comparison]
- Smart dashboard wishlists include ESP32 logic for mode toggles, legal-speed presets triggered by button combinations, and selecting CAN over UART to survive high-current noise environments.[^smart_dash_roadmap]
- Minimotors EY3 displays still require a VSETT Lisp bridge when paired with Flipsky FT85BD or Ubox Lite clones; leaving the bridge’s throttle-out lead disconnected has already bricked retrofits, so treat the passthrough as mandatory wiring.[^ey3_bridge]
- Builders without CAN accessories lean on $10 USB GPS speedometers that boot in under a minute from a 5 V feed, offering a simple overlay when TFT dashboards will not fit the cockpit.[^usb_gps]

## Accessory Power Planning

- High-voltage scooters power lighting and telemetry through wide-input (≈9–120 V) buck modules stepped down to 5 V at 2–3 A, but veterans now bench-test every unit: mislabeled boards have overvolted 6 V lamps, standby draw needs confirmation against the advertised ≈1 mA, and the VESC ADC daughterboard remains an analog interface rather than a substitute step-down supply.[^hv_buck]

## Lighting Upgrades

- Riders trial 3 000–9 000 lm USB-C headlights that double as power banks, programmable LED tail lights, and 12 V mirror-mounted assemblies to overcome weak, glare-prone stock Xiaomi lamps.[^lighting_tests]

## Power Control Ergonomics

- The platform supports sleep mode, but implementing a physical power switch requires custom wiring; many builds still rely on anti-spark switches as manual cut-offs.[^sleep_wiring]

[^dashboard_gap]: Source: knowledge/notes/input_part000_review.md, line 38.
[^tft_mounts]: Source: knowledge/notes/input_part000_review.md, line 46.
[^display_comparison]: Source: knowledge/notes/input_part000_review.md, line 57.
[^smart_dash_roadmap]: Source: knowledge/notes/input_part000_review.md, line 59.
[^lighting_tests]: Source: knowledge/notes/input_part000_review.md, line 47.
[^sleep_wiring]: Source: knowledge/notes/input_part000_review.md, line 45.
[^ey3_bridge]: Source: knowledge/notes/input_part009_review.md†L438-L439.
[^usb_gps]: Source: knowledge/notes/input_part009_review.md†L441-L441.
[^hv_buck]: Source: knowledge/notes/input_part009_review.md†L440-L440.
