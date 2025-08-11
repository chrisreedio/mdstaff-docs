#!/usr/bin/env python3
"""
HTML to Markdown Converter for ASM Query Endpoint Documentation

This script converts the ASM Query Endpoint HTML documentation into 
organized markdown files based on the table of contents structure.
"""

import os
import re
import shutil
from pathlib import Path
from urllib.parse import quote
from bs4 import BeautifulSoup, NavigableString
import html2text


class DocumentationConverter:
    def __init__(self, html_file_path, output_dir="asm_docs"):
        self.html_file_path = html_file_path
        
        # Extract document name from HTML filename for subdirectory
        html_filename = Path(html_file_path).stem
        # Clean the filename to create a proper subdirectory name
        doc_name = self.clean_filename_for_directory(html_filename)
        
        self.output_dir = Path(output_dir) / doc_name
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.doc_name = doc_name
        
        # Set up asset directory paths
        self.html_file_base = Path(html_file_path).stem
        self.asset_dir = Path(html_file_path).parent / f"{self.html_file_base}_files"
        self.images_dir = self.output_dir / "images"
        
        # Configure html2text converter
        self.h = html2text.HTML2Text()
        self.h.ignore_links = False
        self.h.ignore_images = False
        self.h.ignore_emphasis = False
        self.h.body_width = 0  # Don't wrap lines
        self.h.unicode_snob = True
        self.h.ignore_tables = False
        
        # Document structure based on document type
        self.structure = self.get_document_structure()
    
    def clean_filename_for_directory(self, filename):
        """Clean HTML filename to create a proper directory name"""
        # Remove common suffixes and clean up
        cleaned = filename.lower()
        
        # Handle specific patterns like "Query Endpoint – ASM"
        if "query endpoint" in cleaned:
            return "query"
        elif "provider" in cleaned and "endpoint" in cleaned:
            return "provider"
        elif "lookup" in cleaned and "endpoint" in cleaned:
            return "lookup"
        else:
            # Generic cleanup - extract meaningful part
            cleaned = re.sub(r'\s*–\s*asm.*$', '', cleaned)  # Remove "– ASM" suffix
            cleaned = re.sub(r'\s*-\s*asm.*$', '', cleaned)   # Remove "- ASM" suffix  
            cleaned = re.sub(r'[^\w\s-]', '', cleaned)        # Remove special chars except hyphens
            cleaned = re.sub(r'\s+', '_', cleaned)            # Replace spaces with underscores
            cleaned = re.sub(r'_+', '_', cleaned)             # Collapse multiple underscores
            cleaned = cleaned.strip('_')                      # Remove leading/trailing underscores
            
            return cleaned if cleaned else "documentation"
    
    def get_document_structure(self):
        """Get document structure based on document type"""
        if "triggered" in self.doc_name.lower() or "webhook" in self.doc_name.lower():
            return {
                "setup": {
                    "folder": "01_setup",
                    "sections": ["api-access-key", "webhook-endpoint", "triggered-message"]
                },
                "operations": {
                    "folder": "02_operations", 
                    "sections": ["testing", "webhook-log", "troubleshooting"]
                },
                "examples": {
                    "folder": "03_examples",
                    "sections": ["credential", "examples", "payloads"]
                }
            }
        else:
            # Default Query Endpoint structure
            return {
                "overview": {
                    "folder": "01_overview",
                    "sections": ["overview", "sub-records", "custom-fields", "security"]
                },
                "options": {
                    "folder": "02_options", 
                    "sections": ["options", "fields", "filter", "sort", "counts", "pagination"]
                },
                "provider_records": {
                    "folder": "03_provider_records",
                    "sections": [
                        "appointment", "demographic", "address", "board-certification",
                        "credential", "education", "insurance", "medical-history", 
                        "provider-file", "provider-privilege", "privileges"
                    ]
                },
                "enrollment": {
                    "folder": "04_enrollment",
                    "sections": ["provider-enrollments", "provider-entities", "networks", "network-members"]
                },
                "additional": {
                    "folder": "05_additional",
                    "sections": [
                        "alias", "next-appointment", "appointment-history", "covering-provider",
                        "dues", "employment", "home-address", "leadership", "malpractice-claims",
                        "passport", "preferred-contact-methods", "supervisor"
                    ]
                },
                "security_models": {
                    "folder": "06_security",
                    "sections": ["user", "user-roles", "group", "group-membership", "security-permissions"]
                },
                "other_records": {
                    "folder": "07_other_records",
                    "sections": ["lookup", "reference-source", "history"]
                }
            }
    
    def load_html(self):
        """Load and parse the HTML file"""
        with open(self.html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return BeautifulSoup(content, 'html.parser')
    
    def clean_anchor_id(self, anchor_id):
        """Clean anchor ID to match section names"""
        if not anchor_id:
            return ""
        # Remove common prefixes and clean
        cleaned = anchor_id.replace("user-content-", "").replace("h_", "").lower()
        # Handle special cases
        cleaned = re.sub(r'^[0-9a-f]{26}$', '', cleaned)  # Remove hash-like IDs
        return cleaned
    
    def extract_section_content(self, soup, section_id):
        """Extract content for a specific section"""
        # Find the header with the section ID - try multiple approaches
        header = None
        
        # First try: direct ID match
        header = soup.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'], 
                          id=lambda x: x and section_id in str(x).lower())
        
        if not header:
            # Second try: look for anchor with user-content prefix
            anchor = soup.find('a', {'id': f'user-content-{section_id}'})
            if anchor:
                header = anchor.find_parent(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        
        if not header:
            # Third try: look for headers containing section text
            headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            for h in headers:
                header_text = h.get_text().lower().replace(' ', '-').replace('/', '-')
                if section_id in header_text or header_text in section_id:
                    header = h
                    break
        
        if not header:
            return None, None
        
        # Get header level and text
        header_level = int(header.name[1])
        header_text = header.get_text().strip()
        
        # Collect content until next header of same or higher level
        content_elements = []
        current = header.find_next_sibling()
        
        while current:
            if (current.name and current.name.startswith('h') and 
                int(current.name[1]) <= header_level):
                break
            content_elements.append(current)
            current = current.find_next_sibling()
        
        return header_text, content_elements
    
    def copy_images_and_fix_paths(self):
        """Copy images from asset directory to images folder and return path mapping"""
        if not self.asset_dir.exists():
            print(f"Asset directory not found: {self.asset_dir}")
            return {}
        
        # Create images directory
        self.images_dir.mkdir(exist_ok=True)
        
        # Find all image files in asset directory
        image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'}
        image_files = []
        
        for file_path in self.asset_dir.iterdir():
            if file_path.suffix.lower() in image_extensions:
                image_files.append(file_path)
        
        # Copy images and create path mapping
        path_mapping = {}
        
        for image_file in image_files:
            dest_path = self.images_dir / image_file.name
            try:
                shutil.copy2(image_file, dest_path)
                # Map old path to new relative path (need ../ to go up from subfolder)
                old_path = f"./{self.asset_dir.name}/{image_file.name}"
                new_path = f"../images/{quote(image_file.name)}"
                path_mapping[old_path] = new_path
                print(f"  📷 Copied image: {image_file.name}")
            except Exception as e:
                print(f"  ⚠ Failed to copy {image_file.name}: {e}")
        
        return path_mapping
    
    def fix_image_paths_in_markdown(self, markdown, path_mapping):
        """Fix image paths in markdown content"""
        if not path_mapping:
            return markdown
        
        # Fix markdown image syntax ![alt](path)
        for old_path, new_path in path_mapping.items():
            # Handle various path formats that might appear
            patterns = [
                old_path,  # Exact match
                old_path.replace('./', ''),  # Without ./
                old_path.replace('\\', '/'),  # Windows paths
            ]
            
            for pattern in patterns:
                markdown = markdown.replace(f'({pattern})', f'({new_path})')
                markdown = markdown.replace(f'[{pattern}]', f'[{new_path}]')
        
        return markdown
    
    def detect_and_wrap_json(self, text):
        """Detect JSON code blocks and wrap them with proper markdown syntax"""
        import json
        lines = text.split('\n')
        result_lines = []
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # Look for lines that start with whitespace and contain only '{'
            if re.match(r'^\s*{\s*$', line):
                # Found potential JSON start, collect until matching '}'
                json_lines = [line]
                brace_count = 1
                j = i + 1
                
                while j < len(lines) and brace_count > 0:
                    json_lines.append(lines[j])
                    # Count braces in this line
                    for char in lines[j]:
                        if char == '{':
                            brace_count += 1
                        elif char == '}':
                            brace_count -= 1
                            if brace_count == 0:
                                break
                    j += 1
                
                # Try to parse as JSON
                json_text = '\n'.join(json_lines).strip()
                try:
                    json.loads(json_text)
                    # Valid JSON - wrap it
                    result_lines.append('```json')
                    result_lines.append(json_text)
                    result_lines.append('```')
                    i = j
                    continue
                except (json.JSONDecodeError, ValueError):
                    # Not valid JSON, add the first line and continue
                    result_lines.append(line)
                    i += 1
                    continue
            
            # Look for lines that start with whitespace and contain only '['
            elif re.match(r'^\s*\[\s*$', line):
                # Found potential JSON array start
                json_lines = [line]
                bracket_count = 1
                j = i + 1
                
                while j < len(lines) and bracket_count > 0:
                    json_lines.append(lines[j])
                    # Count brackets in this line
                    for char in lines[j]:
                        if char == '[':
                            bracket_count += 1
                        elif char == ']':
                            bracket_count -= 1
                            if bracket_count == 0:
                                break
                    j += 1
                
                # Try to parse as JSON
                json_text = '\n'.join(json_lines).strip()
                try:
                    json.loads(json_text)
                    # Valid JSON array - wrap it
                    result_lines.append('```json')
                    result_lines.append(json_text)
                    result_lines.append('```')
                    i = j
                    continue
                except (json.JSONDecodeError, ValueError):
                    # Not valid JSON, add the first line and continue
                    result_lines.append(line)
                    i += 1
                    continue
            
            # Regular line, just add it
            result_lines.append(line)
            i += 1
        
        return '\n'.join(result_lines)
    
    def elements_to_markdown(self, elements):
        """Convert a list of HTML elements to markdown"""
        if not elements:
            return ""
        
        # Create a temporary container
        temp_soup = BeautifulSoup('<div></div>', 'html.parser')
        container = temp_soup.div
        
        for element in elements:
            if element and hasattr(element, 'name'):
                container.append(element.extract() if hasattr(element, 'extract') else element)
        
        # Convert to markdown
        markdown = self.h.handle(str(container))
        
        # Clean up markdown
        markdown = re.sub(r'\n\n\n+', '\n\n', markdown)  # Remove excessive newlines
        # Fix malformed headers with empty anchor links
        markdown = re.sub(r'^(#{1,6})\s*\[\]\([^)]+\)(.*)$', r'\1 \2', markdown, flags=re.MULTILINE)
        # Detect and wrap JSON code blocks
        markdown = self.detect_and_wrap_json(markdown)
        markdown = markdown.strip()
        
        return markdown
    
    def create_section_file(self, folder_path, filename, title, content, path_mapping=None):
        """Create a markdown file for a section"""
        file_path = folder_path / f"{filename}.md"
        
        # Fix image paths if content exists and path mapping is available
        if content and path_mapping:
            content = self.fix_image_paths_in_markdown(content, path_mapping)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            if content:
                f.write(content)
            else:
                f.write("*Content not found in source document*\n")
    
    def create_index_files(self):
        """Create index files for each folder and main README"""
        
        # Main README for this document
        doc_title = self.doc_name.replace('_', ' ').title()
        
        if "triggered" in self.doc_name.lower() or "webhook" in self.doc_name.lower():
            readme_content = f"""# ASM {doc_title} Documentation

This documentation covers how to set up and use Triggered Webhooks in MD-Staff.

## 01. Setup
- API Access Key configuration
- Webhook Endpoint creation
- Triggered Message setup

## 02. Operations
- Testing webhooks
- Webhook logging
- Troubleshooting

## 03. Examples
- Sample payloads and configurations

## Usage

Triggered Webhooks allow MD-Staff to send real-time JSON data to your public endpoints when specific events occur. Start with the Setup section to configure your webhook integration.
"""
        else:
            readme_content = f"""# ASM {doc_title} Documentation

This documentation is organized into the following sections:

## 01. Overview
- Understanding the Query Endpoint
- Sub-Records, Custom Fields, and Security

## 02. Options  
- Fields, Filters, Sorting, Counts, and Pagination

## 03. Provider Records
- Core provider data types and examples

## 04. Enrollment/Managed Care
- Provider enrollments, entities, and networks

## 05. Additional Items
- Supplementary provider information

## 06. Security Models
- Users, roles, groups, and permissions

## 07. Other Records
- Lookups, reference sources, and history

## Usage

Each folder contains detailed documentation for that section. Start with the Overview section to understand the basic concepts, then explore specific areas as needed.
"""
        
        with open(self.output_dir / "README.md", 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        # Create index files for each folder
        if "triggered" in self.doc_name.lower() or "webhook" in self.doc_name.lower():
            folder_descriptions = {
                "01_setup": "Setting up API keys, webhook endpoints, and triggered messages",
                "02_operations": "Testing, logging, and troubleshooting webhooks",
                "03_examples": "Sample configurations and payload examples"
            }
        else:
            folder_descriptions = {
                "01_overview": "Overview of the Query Endpoint functionality",
                "02_options": "Available options for customizing queries",
                "03_provider_records": "Provider record types and examples", 
                "04_enrollment": "Enrollment and managed care records",
                "05_additional": "Additional provider information types",
                "06_security": "Security models and permissions",
                "07_other_records": "Other record types and utilities"
            }
        
        for category, info in self.structure.items():
            folder_path = self.output_dir / info["folder"]
            folder_path.mkdir(exist_ok=True)
            
            index_content = f"""# {folder_descriptions.get(info['folder'], info['folder'].title())}

## Sections in this folder:

"""
            for section in info["sections"]:
                section_title = section.replace("-", " ").title()
                index_content += f"- [{section_title}]({section}.md)\n"
            
            with open(folder_path / "README.md", 'w', encoding='utf-8') as f:
                f.write(index_content)
    
    def convert(self):
        """Main conversion process"""
        print(f"Loading HTML from {self.html_file_path}")
        soup = self.load_html()
        
        print(f"Creating output directory: {self.output_dir}")
        
        # Copy images and get path mapping
        print("Copying images...")
        path_mapping = self.copy_images_and_fix_paths()
        
        # Process each category
        for category, info in self.structure.items():
            folder_path = self.output_dir / info["folder"] 
            folder_path.mkdir(exist_ok=True)
            
            print(f"Processing category: {category}")
            
            for section in info["sections"]:
                print(f"  Extracting section: {section}")
                
                title, content_elements = self.extract_section_content(soup, section)
                
                if title and content_elements:
                    markdown_content = self.elements_to_markdown(content_elements)
                    self.create_section_file(folder_path, section, title, markdown_content, path_mapping)
                    print(f"    ✓ Created {section}.md")
                else:
                    # Skip placeholder files - commented out to avoid generating empty files
                    # self.create_section_file(folder_path, section, section.replace("-", " ").title(), None, path_mapping)
                    print(f"    ⚠ Skipped {section}.md (no content found)")
        
        # Create index files
        print("Creating index files...")
        self.create_index_files()
        
        print(f"✓ Conversion complete! Documentation saved to: {self.output_dir}")
        if path_mapping:
            print(f"✓ Copied {len(path_mapping)} images to: {self.images_dir}")


def main():
    """Main function to run the converter"""
    import sys
    
    # Get HTML file from command line argument or use default
    if len(sys.argv) > 1:
        html_file = sys.argv[1]
    else:
        html_file = "Query Endpoint – ASM.html"
    
    if not os.path.exists(html_file):
        print(f"Error: HTML file '{html_file}' not found in current directory")
        return 1
    
    converter = DocumentationConverter(html_file)
    converter.convert()
    
    return 0


if __name__ == "__main__":
    exit(main())