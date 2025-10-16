# Ennoid Controllers Brand Dossier

## TL;DR

- MK8 controllers mirror the Spintend 85150 footprint but only reach the advertised 26 S / 500 A phase ceiling after swapping in Infineon IPTC017N12NM6 Toll MOSFETs and reworking the power stage—stock hardware behaves like a derated 20 S unit until those upgrades are complete.[^mk8_swap]
- Smart Repair recommends Ennoid’s shunt-sensed design when Spintend’s current-transformer front end mis-detects motors around 100 A; the MK8 becomes the go-to “fat VESC” footprint when builders are willing to perform the Toll-FET hotplate+hot-air reflow.[^ct_vs_shunt]
- Community labs keep Ennoid controllers on hand alongside Thor, MakerX, Tronic, and upcoming Maxim hardware so new launches can be benchmarked against a known-good shunt platform; document teardowns and telemetry so comparisons stay apples-to-apples.[^museum]
- Ennoid is teasing a compact 100 V/75 A single VESC (~70 × 75 × 16 mm, ≈$200) that could cover small-deck builds waiting on Spintend’s single-channel release.[^single_75a]

## Platform Snapshot

| Model | Nominal Pack Window | Community Envelope | Notes |
| --- | --- | --- | --- |
| MK8 (Toll FET reworked) | 20–26 S after IPTC017N12NM6 swap | Targeting ≈500 A phase with upgraded silicon and reinforced busbars | Shares mounting pattern with Spintend 85150; expect to repaste, re-pot, and validate shunt calibration after reflow.[^mk8_swap] |

## Operating Guardrails & Upgrade Workflow

1. **Source genuine Toll FETs.** Infineon IPTC017N12NM6 devices are the proven drop-in to unlock 26 S ambitions; log lot codes and inspect legs before soldering.[^mk8_swap]
2. **Hotplate + hot-air rework.** Lift stock MOSFETs evenly, preheat the IMS board on a hotplate, and flow the new Toll packages with hot air to avoid warping the aluminum substrate.
3. **Refresh thermal interface.** Replace factory paste and torque hardware before loading the stage—shunt-sensed readings only stay accurate when MOSFET temperatures stay balanced.
4. **Retune detection.** After the swap, rerun motor detection and validate shunt scaling; unlike CT-based platforms the MK8 reports battery current directly, so builders expect more consistent auto-detect behaviour once the upgrade is complete.[^ct_vs_shunt]

## Ecosystem & Benchmarking

- Keep Ennoid units in the comparison fleet when documenting Maxim, Seven, or Tronic launches—JPPL’s “VESC museum” relies on the MK8 as the shunt-based control sample when evaluating new controllers.[^museum]
- Archive firmware and telemetry from each reworked MK8 so future installers can verify that upgraded Toll stages really deliver the promised 26 S headroom before adopting them in production builds.

## When to Reach for Alternatives

- Skip Ennoid if you lack Toll-reflow capability—unmodified MK8 hardware behaves like a Spintend 85150 with less firmware support. Choose 3Shul or Tronic platforms when you need validated >500 A output without touching the power stage.
- Likewise, builders who need turnkey support may still gravitate to Spintend 85/240 or upcoming 18-FET revisions despite their CT quirks, simply because replacement boards remain easier to source.

## Source Notes

[^mk8_swap]: Ennoid MK8 shares the Spintend 85150 footprint but relies on Infineon IPTC017N12NM6 Toll MOSFET swaps to stretch toward 26 S / 500 A phase capability. Source: knowledge/notes/input_part014_review.md, L12 to L13
[^ct_vs_shunt]: Smart Repair’s diagnosis that Spintend’s current-transformer sensing saturates near 100 A and their recommendation to pivot heavy builds to shunt-based MK8/X12 hardware until an 18-FET refresh arrives. Source: knowledge/notes/input_part014_review.md, L12 to L13
[^museum]: JPPL’s “VESC museum” inventory—Thor, MakerX, Tronic, Ennoid—maintained to benchmark future Maxim/Seven releases under identical conditions. Source: knowledge/notes/input_part014_review.md, L27 to L27
[^single_75a]: Source: knowledge/notes/input_part000_review.md, line 211.
