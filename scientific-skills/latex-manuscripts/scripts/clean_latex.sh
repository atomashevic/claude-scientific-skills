#!/bin/bash
# Clean LaTeX auxiliary files

BASE_NAME="${1:-*}"

echo "Cleaning LaTeX auxiliary files..."

FILES=(
    "*.aux" "*.bbl" "*.blg" "*.fdb_latexmk" "*.fls"
    "*.log" "*.out" "*.synctex.gz" "*.toc" "*.lof" "*.lot"
)

REMOVED=0

for pattern in "${FILES[@]}"; do
    for file in $BASE_NAME.$pattern; do
        if [ -f "$file" ]; then
            rm -f "$file"
            echo "Removed: $file"
            ((REMOVED++))
        fi
    done
done

echo "Cleaned $REMOVED file(s)"
