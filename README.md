# ASM MD-Staff Documentation Converter

A Python tool that converts ASM MD-Staff HTML documentation into organized Markdown format.

## Quick Start

```bash
# Install dependencies
pip install beautifulsoup4 html2text

# Convert Query Endpoint docs
python3 html_to_markdown_converter.py "Query Endpoint – ASM.html"

# Convert Triggered Webhooks docs  
python3 html_to_markdown_converter.py "Triggered Webhooks – ASM.html"
```

## Output Structure

- **Query Documentation**: `asm_docs/query/` - API query endpoints, provider records, security
- **Webhooks Documentation**: `asm_docs/triggered_webhooks/` - Setup, operations, examples

## Features

- Automatic image extraction and path fixing
- JSON code block detection and formatting
- Hierarchical documentation organization
- Index file generation for easy navigation

Generated documentation includes comprehensive examples for MD-Staff API integration including provider queries, sub-records, and webhook configurations.