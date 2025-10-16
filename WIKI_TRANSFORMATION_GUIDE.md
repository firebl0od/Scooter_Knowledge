# Wiki-Style Transformation Guide

## Overview

This document explains the transformation from dense technical documentation to accessible wiki-style articles in the Scooter Knowledge repository. The goal is to make technical information more readable and approachable without losing any knowledge.

## Transformation Philosophy

### Core Principles

1. **Accessibility First**: Write for newcomers while preserving expert-level detail
2. **No Knowledge Loss**: Every technical specification, measurement, and citation must be preserved
3. **Better Organization**: Use clear hierarchy and visual structure
4. **Context Over Brevity**: Explain "why" and "when", not just "what"
5. **Scannable Content**: Make information easy to find with headers, tables, and callouts

## Before & After Examples

### Example 1: Dense Bullet to Structured Content

**Before**:
```markdown
- PETG battery holders crack when printed wet or too fast; veterans dry filament, slow to 80–120 mm/s with 0.6 mm nozzles, run 240–260 °C hotends, and tune retraction/fan settings before trusting cages to hold 21700 cells.[^1]
```

**After**:
```markdown
### For Battery Holders

Battery holders are safety-critical—they must not crack during riding vibration.

**Requirements**:[^1]
1. **Dry filament** - Store in sealed containers with desiccant
2. **Slow down** - 80-120 mm/s prevents layer adhesion issues
3. **Optimize temperature** - 240-260°C for PETG
4. **Tune retraction** - Reduce stringing without causing gaps
5. **Control cooling** - Balance layer adhesion with dimensional accuracy
```

### Example 2: Technical Jargon to Explained Content

**Before**:
```markdown
- Dual Ubox owners are seeing 2×135 A phase / 2×71 A battery setups stay below 70 °C when the cases are externally mounted, and the 75 V hardware survives 17 S packs without regen—just disable braking on a full charge until the pack bleeds a few percent or expect over-voltage trips.[^1]
```

**After**:
```markdown
### Voltage & Regen Management

**17S Pack Operation**:[^1]

Dual Ubox systems can handle 17S packs safely with proper precautions:
- **Current**: 2×135A phase / 2×71A battery per controller
- **Thermal**: Stays below 70°C with external mounting
- **Critical**: Disable regen braking when pack is fully charged
- **Why**: Over-voltage protection will trip if regen occurs at 100% charge
- **Solution**: Wait until pack drops to ~95% before using regen

> **⚠️ Warning**: Over-voltage trips can damage controllers. Always disable regen when charging to 100%.
```

## Document Structure Templates

### For Guide Files

```markdown
# [Guide Title]

## Overview
[2-3 sentences: What this covers, who it's for]

## What You'll Learn
- [Key point 1]
- [Key point 2]
- [Key point 3]

## [Key Concept Section]

### [Subsection]

[Explanatory paragraph with context]

**[Specific Topic]**:
- [Details with inline context]
- [Why this matters]
- [When to apply]

> **💡 Pro Tip**: [Practical advice from community]

### Troubleshooting

**Symptom**: [What user experiences]
**Cause**: [Why it happens]
**Solution**: [Step-by-step fix]

## Quick Reference

| Parameter | Value | Notes |
|-----------|-------|-------|
| [Item] | [Spec] | [Context] |

## Related Guides
- [Link to related content]

## References
[^1]: [Citation]
```

### For Brand Dossiers

```markdown
# [Brand Name]

## Overview
[Who makes these, what they're known for, market position]

## Product Line

| Model | Specs | Key Features |
|-------|-------|--------------|
| [Name] | [Details] | [Notes] |

## What Makes [Brand] Different
[Unique characteristics, strengths, weaknesses]

## Common Applications
[Typical use cases with context]

## Known Issues
[Problems with solutions]

## When to Choose [Brand]
**Good Fit If**: [Scenarios]
**Consider Alternatives If**: [Other scenarios]

## Related Guides
- [Links]

## References
[^1]: [Citations]
```

## Formatting Patterns

### Visual Callouts

Use these to highlight important information:

```markdown
> **⚠️ Safety Warning**: [Critical safety information]

> **💡 Pro Tip**: [Helpful community wisdom]

> **📝 Definition**: [Technical term explanation]

> **⚠️ Important**: [Key point that's often missed]
```

### Comparison Tables

```markdown
| Option A | Option B | Best For |
|----------|----------|----------|
| [Pros/specs] | [Pros/specs] | [Use case] |
```

### Decision Checklists

```markdown
**Good Fit If**:
- [Condition 1]
- [Condition 2]

**Avoid If**:
- [Condition 1]
- [Condition 2]
```

### Step-by-Step Procedures

```markdown
### [Procedure Name]

1. **[Step 1 title]**
   - [Detail]
   - [Why this matters]

2. **[Step 2 title]**
   - [Detail]
   - [Caution or tip]
```

## Technical Term Handling

### First Use: Define

When introducing technical terms:

```markdown
**BMS (Battery Management System)**: The electronic circuit that protects your battery pack from overcharge, overdischarge, and cell imbalance.
```

### Abbreviations

Spell out on first use, then abbreviate:

```markdown
The VESC (Vedder Electronic Speed Controller) provides precise motor control. VESC firmware updates...
```

### Context for Numbers

Add context to specifications:

```markdown
❌ Before: "150A phase current"
✅ After: "150A phase current (the maximum current sent to motor windings during acceleration)"
```

## Preservation Checklist

Every rewrite must verify:

- [ ] All technical specifications preserved
- [ ] All footnote citations maintained with exact same reference numbers
- [ ] No data points removed
- [ ] Source line references intact
- [ ] Numbers and measurements accurate
- [ ] Brand names and model numbers correct
- [ ] Community member attributions preserved
- [ ] All links functional

## Common Transformations

### Headers

- `TL;DR` → `Overview` or `Quick Summary`
- `Product Line Cheat Sheet` → `Product Line` with table
- `When to Choose Alternatives` → `When to Choose [Brand]` with pros/cons

### Content Organization

1. **Split dense paragraphs**: One concept per paragraph
2. **Extract lists**: Pull embedded lists into proper bullet format
3. **Add subheadings**: Break long sections into scannable parts
4. **Group related items**: Combine scattered points about same topic
5. **Add transition text**: Connect sections with context

### Safety & Warnings

Make these prominent:

```markdown
❌ Before: "trim regen near full charge (≈76.6 V on 20 S) to avoid repeated over-voltage faults"
✅ After:
> **⚠️ Safety**: Always reduce regen current when battery approaches full charge (≈76.6V on 20S packs). Over-voltage faults can damage controllers.
```

## Quality Metrics

A good wiki-style transformation shows:

1. **Increased line count** (but more scannable)
2. **More section headings** (better navigation)
3. **Visual callouts** (highlights key points)
4. **Context sentences** (explains why/when)
5. **Tables** (comparison and quick reference)
6. **Preserved citations** (all technical details intact)

## Testing Readability

Ask these questions:

1. Can a beginner find what they need in 30 seconds?
2. Are technical terms explained at first use?
3. Do headers accurately describe content?
4. Are warnings visually prominent?
5. Can experts still find detailed specs quickly?
6. Are related topics cross-referenced?

## Implementation Strategy

### Priority Order

1. **Short simple files first** (build momentum, perfect approach)
2. **High-traffic guides** (maximize impact)
3. **Complex technical docs** (apply refined patterns)
4. **Long comprehensive files** (break into well-organized sections)

### Batch Processing

- Do similar files together (all simple brand files, then complex ones)
- Perfect one pattern, then apply to similar content
- Commit frequently to track progress
- Verify citations after each file

## Tools & Workflow

### Manual Review Points

- Overview sections (must be custom-written)
- Section organization (requires understanding of content)
- Visual callout placement (judgment call)
- Related guides links (manual research)

### Automated Checks

- Citation preservation (verify footnote numbers)
- Link functionality (test all internal links)
- Formatting consistency (markdown linting)
- Spelling/grammar (standard tools)

## Success Criteria

A completed wiki-style transformation should:

1. ✅ Preserve 100% of technical content
2. ✅ Be significantly more readable to newcomers
3. ✅ Still serve expert users efficiently
4. ✅ Follow consistent formatting patterns
5. ✅ Cross-reference related content
6. ✅ Include overview and context sections
7. ✅ Use visual hierarchy effectively
8. ✅ Maintain all source citations

## Files Completed

- [x] xiaomi_fold_and_pole_repair.md
- [x] 3d-printing-and-materials.md
- [x] heatbox.md
- [x] rfp.md
- [x] wheelway.md
- [x] minimotors.md
- [x] medhi_cantin.md (already had overview)

**Progress**: 7/72 files (9.7%)

## Next Priority Files

Based on analysis:
1. Short brand files (faster, build momentum)
2. Key guides (battery, motor, controller basics)
3. Conversion guides (high community value)
4. Long technical references (comprehensive restructuring)
