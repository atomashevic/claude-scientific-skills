#!/bin/bash
# =============================================================================
# compile_beamer.sh - Compile Beamer Presentations
# =============================================================================
# Usage: ./compile_beamer.sh presentation.tex [options]
#
# Options:
#   -c, --clean     Clean auxiliary files after compilation
#   -w, --watch     Watch for changes and recompile (requires latexmk)
#   -d, --draft     Draft mode (faster, no images)
#   -e, --engine    LaTeX engine (pdflatex, xelatex, lualatex)
#   -h, --help      Show this help message
# =============================================================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Default options
CLEAN=false
WATCH=false
DRAFT=false
ENGINE="pdflatex"
INPUT_FILE=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -c|--clean)
            CLEAN=true
            shift
            ;;
        -w|--watch)
            WATCH=true
            shift
            ;;
        -d|--draft)
            DRAFT=true
            shift
            ;;
        -e|--engine)
            ENGINE="$2"
            shift 2
            ;;
        -h|--help)
            echo "Usage: $0 presentation.tex [options]"
            echo ""
            echo "Compile Beamer presentations to PDF."
            echo ""
            echo "Options:"
            echo "  -c, --clean     Clean auxiliary files after compilation"
            echo "  -w, --watch     Watch for changes and recompile"
            echo "  -d, --draft     Draft mode (faster, no images)"
            echo "  -e, --engine    LaTeX engine: pdflatex, xelatex, lualatex (default: pdflatex)"
            echo "  -h, --help      Show this help message"
            echo ""
            echo "Examples:"
            echo "  $0 presentation.tex"
            echo "  $0 presentation.tex --clean"
            echo "  $0 presentation.tex --watch"
            echo "  $0 presentation.tex --engine xelatex"
            exit 0
            ;;
        *)
            if [[ -z "$INPUT_FILE" ]]; then
                INPUT_FILE="$1"
            else
                echo -e "${RED}Error: Unknown option $1${NC}"
                exit 1
            fi
            shift
            ;;
    esac
done

# Check if input file is provided
if [[ -z "$INPUT_FILE" ]]; then
    echo -e "${RED}Error: No input file specified${NC}"
    echo "Usage: $0 presentation.tex [options]"
    exit 1
fi

# Check if input file exists
if [[ ! -f "$INPUT_FILE" ]]; then
    echo -e "${RED}Error: File '$INPUT_FILE' not found${NC}"
    exit 1
fi

# Validate engine
if [[ ! "$ENGINE" =~ ^(pdflatex|xelatex|lualatex)$ ]]; then
    echo -e "${RED}Error: Invalid engine '$ENGINE'. Use: pdflatex, xelatex, or lualatex${NC}"
    exit 1
fi

# Get base name without extension
BASENAME="${INPUT_FILE%.tex}"

# Check for required tools
check_tool() {
    if ! command -v "$1" &> /dev/null; then
        echo -e "${RED}Error: $1 is not installed${NC}"
        exit 1
    fi
}

# Function to clean auxiliary files
clean_aux() {
    echo -e "${YELLOW}Cleaning auxiliary files...${NC}"
    rm -f "${BASENAME}.aux" \
          "${BASENAME}.log" \
          "${BASENAME}.nav" \
          "${BASENAME}.out" \
          "${BASENAME}.snm" \
          "${BASENAME}.toc" \
          "${BASENAME}.vrb" \
          "${BASENAME}.bbl" \
          "${BASENAME}.blg" \
          "${BASENAME}.bcf" \
          "${BASENAME}.run.xml" \
          "${BASENAME}.fdb_latexmk" \
          "${BASENAME}.fls" \
          "${BASENAME}.synctex.gz"
    echo -e "${GREEN}Auxiliary files cleaned${NC}"
}

# Function to compile with specific engine
compile_engine() {
    local engine="$1"
    local extra_opts=""
    
    if [[ "$DRAFT" == true ]]; then
        extra_opts="-draftmode"
    fi
    
    check_tool "$engine"
    
    echo -e "${YELLOW}Compiling with $engine...${NC}"
    $engine -interaction=nonstopmode $extra_opts "$INPUT_FILE"
    
    # Check for bibliography
    if grep -q "\\\\bibliography\|\\\\addbibresource" "$INPUT_FILE"; then
        echo -e "${YELLOW}Processing bibliography...${NC}"
        
        # Detect biber vs bibtex
        if grep -q "backend=biber" "$INPUT_FILE"; then
            check_tool biber
            biber "$BASENAME"
        else
            check_tool bibtex
            bibtex "$BASENAME"
        fi
        
        $engine -interaction=nonstopmode $extra_opts "$INPUT_FILE"
        $engine -interaction=nonstopmode $extra_opts "$INPUT_FILE"
    else
        # Second pass for references
        $engine -interaction=nonstopmode $extra_opts "$INPUT_FILE"
    fi
    
    echo -e "${GREEN}Compilation complete: ${BASENAME}.pdf${NC}"
}

# Function to compile with latexmk
compile_latexmk() {
    check_tool latexmk
    
    local opts="-pdf -interaction=nonstopmode"
    
    # Set engine
    case "$ENGINE" in
        pdflatex)
            opts="$opts -pdflatex='pdflatex -interaction=nonstopmode %O %S'"
            ;;
        xelatex)
            opts="$opts -xelatex"
            ;;
        lualatex)
            opts="$opts -lualatex"
            ;;
    esac
    
    if [[ "$DRAFT" == true ]]; then
        opts="$opts -pdflatex='pdflatex -interaction=nonstopmode -draftmode %O %S'"
    fi
    
    if [[ "$WATCH" == true ]]; then
        echo -e "${YELLOW}Watching for changes (Ctrl+C to stop)...${NC}"
        latexmk $opts -pvc "$INPUT_FILE"
    else
        echo -e "${YELLOW}Compiling with latexmk...${NC}"
        latexmk $opts "$INPUT_FILE"
        echo -e "${GREEN}Compilation complete: ${BASENAME}.pdf${NC}"
    fi
}

# Main compilation
if [[ "$WATCH" == true ]]; then
    compile_latexmk
else
    # Check if latexmk is available
    if command -v latexmk &> /dev/null; then
        compile_latexmk
    else
        compile_engine "$ENGINE"
    fi
fi

# Clean if requested
if [[ "$CLEAN" == true ]]; then
    clean_aux
fi

# Show file size
if [[ -f "${BASENAME}.pdf" ]]; then
    SIZE=$(ls -lh "${BASENAME}.pdf" | awk '{print $5}')
    echo -e "${GREEN}Output: ${BASENAME}.pdf (${SIZE})${NC}"
fi
