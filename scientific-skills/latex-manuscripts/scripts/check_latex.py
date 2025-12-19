#!/usr/bin/env python3
"""LaTeX document validation script."""
import re
import sys
import argparse
from pathlib import Path


def check_file_exists(tex_file):
    """Check if LaTeX file exists."""
    if not Path(tex_file).exists():
        print(f"❌ Error: File '{tex_file}' not found")
        return False
    return True


def check_packages(content):
    """Check for common package issues."""
    issues = []
    if '\\includegraphics' in content and '\\usepackage{graphicx}' not in content:
        issues.append("⚠️  Warning: \\includegraphics used but graphicx package not loaded")
    return issues


def check_references(content):
    """Check for reference issues."""
    issues = []
    labels = re.findall(r'\\label\{([^}]+)\}', content)
    refs = re.findall(r'\\(?:ref|cref|Cref)\{([^}]+)\}', content)
    undefined = set(refs) - set(labels)
    if undefined:
        issues.append(f"⚠️  Warning: {len(undefined)} undefined reference(s)")
    return issues


def main():
    parser = argparse.ArgumentParser(description='Check LaTeX document')
    parser.add_argument('tex_file', help='LaTeX file to check')
    args = parser.parse_args()
    
    if not check_file_exists(args.tex_file):
        sys.exit(1)
    
    with open(args.tex_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"Checking {args.tex_file}...\n")
    
    all_issues = []
    all_issues.extend(check_packages(content))
    all_issues.extend(check_references(content))
    
    if all_issues:
        for issue in all_issues:
            print(issue)
    else:
        print("✅ No issues found!")
    
    sys.exit(0)


if __name__ == '__main__':
    main()
