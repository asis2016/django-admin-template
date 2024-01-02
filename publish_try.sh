wget --mirror --convert-links --adjust-extension --page-requisites --no-parent -P docs/ -nH --no-clobber 127.0.0.1:8000

# Navigate to the 'docs' directory
cd docs

# Rename index.html files
find . -type f -name 'index.html' -exec sh -c 'mv "$1" "${1%/*}.html"' _ {} \;

# Update href links to remove "index.html" part
find . -type f -name '*.html' -exec sed -i 's/href="\([^"]*\)\/index.html"/href="\1.html"/g' {} \;

# Remove empty directories
find . -type d -empty -delete
