#!/usr/bin/env python3
"""
Batch convert PDFs to Markdown using MarkItDown

Usage:
    python batch_convert_pdfs.py papers/ -o markdown/
    python batch_convert_pdfs.py papers/ -o markdown/ --focus-keywords "LLM,social simulation"

Requirements:
    pip install markitdown
"""

import argparse
import os
import sys
from pathlib import Path
from typing import List, Optional

try:
    from markitdown import MarkItDown
except ImportError:
    print("Error: markitdown not installed. Install with: pip install 'markitdown[all]'")
    sys.exit(1)


def find_pdfs(directory: Path) -> List[Path]:
    """Find all PDF files in directory and subdirectories."""
    return list(directory.rglob("*.pdf"))


def convert_pdf_to_markdown(
    pdf_path: Path,
    output_dir: Path,
    md_converter: MarkItDown,
    focus_keywords: Optional[List[str]] = None
) -> bool:
    """
    Convert a single PDF to markdown.

    Args:
        pdf_path: Path to PDF file
        output_dir: Directory to save markdown output
        md_converter: MarkItDown instance
        focus_keywords: Optional list of keywords to check for relevance

    Returns:
        True if conversion successful, False otherwise
    """
    try:
        # Convert PDF to markdown
        print(f"Converting: {pdf_path.name}...", end=" ")
        result = md_converter.convert(str(pdf_path))

        # Check for focus keywords if provided
        if focus_keywords:
            text_lower = result.text_content.lower()
            if not any(keyword.lower() in text_lower for keyword in focus_keywords):
                print(f"SKIPPED (no focus keywords found)")
                return False

        # Create output filename
        output_file = output_dir / f"{pdf_path.stem}.md"

        # Write markdown
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# {pdf_path.stem}\n\n")
            f.write(f"**Source PDF**: {pdf_path.name}\n\n")
            f.write("---\n\n")
            f.write(result.text_content)

        print(f"✓ → {output_file.name}")
        return True

    except Exception as e:
        print(f"✗ ERROR: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Batch convert PDFs to Markdown using MarkItDown",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert all PDFs in papers/ directory
  python batch_convert_pdfs.py papers/ -o markdown/

  # Filter by keywords (only convert papers mentioning these topics)
  python batch_convert_pdfs.py papers/ -o markdown/ --focus-keywords "LLM agents,social simulation,toxicity"

  # Use Azure Document Intelligence for complex PDFs
  python batch_convert_pdfs.py papers/ -o markdown/ --azure-endpoint "<endpoint>"
"""
    )

    parser.add_argument(
        'input_dir',
        type=Path,
        help='Directory containing PDF files (searches recursively)'
    )

    parser.add_argument(
        '-o', '--output-dir',
        type=Path,
        default=Path('markdown'),
        help='Output directory for markdown files (default: markdown/)'
    )

    parser.add_argument(
        '--focus-keywords',
        type=str,
        help='Comma-separated keywords to filter papers (e.g., "LLM,toxicity,network science")'
    )

    parser.add_argument(
        '--azure-endpoint',
        type=str,
        help='Azure Document Intelligence endpoint for enhanced PDF processing'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be converted without actually converting'
    )

    args = parser.parse_args()

    # Validate input directory
    if not args.input_dir.exists():
        print(f"Error: Input directory '{args.input_dir}' does not exist")
        sys.exit(1)

    if not args.input_dir.is_dir():
        print(f"Error: '{args.input_dir}' is not a directory")
        sys.exit(1)

    # Create output directory
    args.output_dir.mkdir(parents=True, exist_ok=True)

    # Parse focus keywords
    focus_keywords = None
    if args.focus_keywords:
        focus_keywords = [kw.strip() for kw in args.focus_keywords.split(',')]
        print(f"Focus keywords: {', '.join(focus_keywords)}\n")

    # Find all PDFs
    pdf_files = find_pdfs(args.input_dir)

    if not pdf_files:
        print(f"No PDF files found in {args.input_dir}")
        sys.exit(0)

    print(f"Found {len(pdf_files)} PDF files\n")

    # Dry run mode
    if args.dry_run:
        print("DRY RUN MODE - No files will be converted\n")
        for pdf in pdf_files:
            output_file = args.output_dir / f"{pdf.stem}.md"
            print(f"  {pdf.name} → {output_file}")
        sys.exit(0)

    # Initialize MarkItDown
    md_kwargs = {}
    if args.azure_endpoint:
        md_kwargs['docintel_endpoint'] = args.azure_endpoint
        print(f"Using Azure Document Intelligence: {args.azure_endpoint}\n")

    md = MarkItDown(**md_kwargs)

    # Convert all PDFs
    print(f"Converting to {args.output_dir}/\n")
    successful = 0
    skipped = 0
    failed = 0

    for i, pdf_path in enumerate(pdf_files, 1):
        print(f"[{i}/{len(pdf_files)}] ", end="")

        result = convert_pdf_to_markdown(
            pdf_path,
            args.output_dir,
            md,
            focus_keywords
        )

        if result:
            successful += 1
        elif focus_keywords:
            skipped += 1
        else:
            failed += 1

    # Summary
    print(f"\n{'='*60}")
    print(f"Conversion complete!")
    print(f"  Successful: {successful}")
    if focus_keywords:
        print(f"  Skipped (no keywords): {skipped}")
    if failed > 0:
        print(f"  Failed: {failed}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
