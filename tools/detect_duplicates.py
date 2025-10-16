#!/usr/bin/env python3
"""
Detect duplicate content across processed knowledge files.

This script analyzes markdown files to find:
- Duplicate paragraphs
- Similar bullet points
- Repeated technical specifications
- Overlapping content that could be consolidated

Usage:
    python tools/detect_duplicates.py [--threshold 0.8] [--output report.md]
"""

import re
import os
import sys
from pathlib import Path
from difflib import SequenceMatcher
from collections import defaultdict
import argparse


def normalize_text(text):
    """Normalize text for comparison by removing formatting and extra whitespace."""
    # Remove markdown formatting
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)  # Remove links
    text = re.sub(r'\[?\^?\d+\]?', '', text)  # Remove footnote markers
    text = re.sub(r'[*_`#]', '', text)  # Remove emphasis markers
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text.lower()


def similarity_ratio(text1, text2):
    """Calculate similarity ratio between two text strings."""
    norm1 = normalize_text(text1)
    norm2 = normalize_text(text2)
    
    if not norm1 or not norm2:
        return 0.0
    
    return SequenceMatcher(None, norm1, norm2).ratio()


def extract_content_blocks(filepath):
    """Extract meaningful content blocks from a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    blocks = []
    
    # Extract paragraphs (non-empty lines not starting with # or -)
    paragraphs = re.findall(r'^(?![#\-\[])[^\n]{30,}$', content, re.MULTILINE)
    for para in paragraphs:
        if para.strip() and not para.startswith('Source:'):
            blocks.append({
                'type': 'paragraph',
                'content': para.strip(),
                'file': filepath
            })
    
    # Extract bullet points
    bullets = re.findall(r'^[\-\*]\s+(.+)$', content, re.MULTILINE)
    for bullet in bullets:
        if len(bullet) > 20:  # Only consider substantial bullets
            blocks.append({
                'type': 'bullet',
                'content': bullet.strip(),
                'file': filepath
            })
    
    # Extract technical specs (voltage, current, etc.)
    specs = re.findall(r'\b(\d+\s*[SV]\s+\d+\s*[PA]|\d+\s*[VA]\s+@\s*\d+|\d+\s*[kK]?[WV])\b', content)
    for spec in specs:
        blocks.append({
            'type': 'spec',
            'content': spec.strip(),
            'file': filepath
        })
    
    return blocks


def find_duplicates(files, threshold=0.85):
    """Find duplicate content across multiple files."""
    
    # Extract all content blocks
    all_blocks = []
    for filepath in files:
        blocks = extract_content_blocks(filepath)
        all_blocks.extend(blocks)
    
    # Find similar blocks
    duplicates = []
    seen_pairs = set()
    
    for i, block1 in enumerate(all_blocks):
        for j, block2 in enumerate(all_blocks):
            if i >= j:
                continue
            
            # Skip if same file
            if block1['file'] == block2['file']:
                continue
            
            # Skip if different types
            if block1['type'] != block2['type']:
                continue
            
            # Skip if we've already compared this pair
            pair_key = tuple(sorted([i, j]))
            if pair_key in seen_pairs:
                continue
            seen_pairs.add(pair_key)
            
            # Calculate similarity
            ratio = similarity_ratio(block1['content'], block2['content'])
            
            if ratio >= threshold:
                duplicates.append({
                    'similarity': ratio,
                    'type': block1['type'],
                    'content1': block1['content'],
                    'file1': os.path.basename(block1['file']),
                    'content2': block2['content'],
                    'file2': os.path.basename(block2['file'])
                })
    
    # Sort by similarity (highest first)
    duplicates.sort(key=lambda x: x['similarity'], reverse=True)
    
    return duplicates


def generate_report(duplicates, output_file=None):
    """Generate a markdown report of duplicates found."""
    
    report = []
    report.append("# Duplicate Content Detection Report\n")
    report.append(f"**Total duplicates found**: {len(duplicates)}\n")
    report.append(f"**Similarity threshold**: {threshold:.0%}\n\n")
    
    if not duplicates:
        report.append("✅ No significant duplicates detected.\n")
        return ''.join(report)
    
    # Group by type
    by_type = defaultdict(list)
    for dup in duplicates:
        by_type[dup['type']].append(dup)
    
    report.append("## Summary by Content Type\n\n")
    for content_type, items in sorted(by_type.items()):
        report.append(f"- **{content_type.capitalize()}**: {len(items)} duplicates\n")
    report.append("\n")
    
    # Detailed findings
    report.append("## Detailed Findings\n\n")
    
    for idx, dup in enumerate(duplicates[:50], 1):  # Limit to top 50
        report.append(f"### {idx}. {dup['type'].capitalize()} ({dup['similarity']:.0%} similar)\n\n")
        report.append(f"**File 1**: `{dup['file1']}`\n")
        report.append(f"> {dup['content1'][:200]}{'...' if len(dup['content1']) > 200 else ''}\n\n")
        report.append(f"**File 2**: `{dup['file2']}`\n")
        report.append(f"> {dup['content2'][:200]}{'...' if len(dup['content2']) > 200 else ''}\n\n")
        report.append("---\n\n")
    
    if len(duplicates) > 50:
        report.append(f"*({len(duplicates) - 50} additional duplicates not shown)*\n\n")
    
    # Recommendations
    report.append("## Recommendations\n\n")
    report.append("1. **Review high-similarity duplicates** (>95%) for consolidation\n")
    report.append("2. **Check technical specifications** for consistency across files\n")
    report.append("3. **Add cross-references** instead of repeating content\n")
    report.append("4. **Preserve unique context** from each source when merging\n")
    report.append("5. **Update extraction process** to avoid future duplication\n\n")
    
    report_text = ''.join(report)
    
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_text)
        print(f"Report written to {output_file}")
    
    return report_text


def main():
    parser = argparse.ArgumentParser(description='Detect duplicate content in knowledge files')
    parser.add_argument('--threshold', type=float, default=0.85,
                        help='Similarity threshold (0.0-1.0, default: 0.85)')
    parser.add_argument('--output', type=str,
                        help='Output file for report (default: print to stdout)')
    parser.add_argument('--guides', action='store_true',
                        help='Only scan guide files')
    parser.add_argument('--brands', action='store_true',
                        help='Only scan brand files')
    
    args = parser.parse_args()
    
    # Find repository root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    processed_dir = repo_root / 'knowledge' / 'processed' / 'themes'
    
    # Collect files to scan
    files = []
    
    if args.guides or not args.brands:
        guides_dir = processed_dir / 'guides'
        if guides_dir.exists():
            files.extend(guides_dir.glob('*.md'))
    
    if args.brands or not args.guides:
        brands_dir = processed_dir / 'brands'
        if brands_dir.exists():
            files.extend(brands_dir.glob('*.md'))
    
    if not files:
        print("Error: No files found to scan", file=sys.stderr)
        return 1
    
    print(f"Scanning {len(files)} files for duplicates...")
    print(f"Similarity threshold: {args.threshold:.0%}")
    print()
    
    # Find duplicates
    global threshold
    threshold = args.threshold
    duplicates = find_duplicates(files, args.threshold)
    
    # Generate report
    report = generate_report(duplicates, args.output)
    
    if not args.output:
        print(report)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
