#!/usr/bin/env python3
"""
PDF Generator for Contact Manager Documentation
Converts the markdown documentation to a well-formatted HTML file
that can be printed to PDF using any web browser.
"""

import os
import datetime

def create_html_from_markdown():
    # Read the markdown file
    try:
        with open('ContactManager_Documentation.md', 'r', encoding='utf-8') as f:
            markdown_content = f.read()
    except FileNotFoundError:
        print("Error: ContactManager_Documentation.md not found!")
        return
    
    # Convert markdown to HTML (basic conversion)
    html_content = markdown_to_html(markdown_content)
    
    # Create complete HTML document
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Manager - C# Console Application Documentation</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
            color: #333;
            background-color: #fff;
        }}
        
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-top: 0;
        }}
        
        h2 {{
            color: #34495e;
            border-bottom: 2px solid #ecf0f1;
            padding-bottom: 5px;
            margin-top: 30px;
        }}
        
        h3 {{
            color: #2c3e50;
            margin-top: 25px;
        }}
        
        .code-block {{
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 6px;
            padding: 20px;
            margin: 15px 0;
            overflow-x: auto;
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
            font-size: 13px;
            line-height: 1.4;
        }}
        
        .inline-code {{
            background-color: #f1f3f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
            font-size: 90%;
        }}
        
        .feature-list {{
            background-color: #f8f9fa;
            border-left: 4px solid #28a745;
            padding: 15px;
            margin: 15px 0;
        }}
        
        .feature-list li {{
            margin: 5px 0;
        }}
        
        .checkmark {{
            color: #28a745;
            font-weight: bold;
        }}
        
        .section {{
            margin: 30px 0;
            page-break-inside: avoid;
        }}
        
        .header-info {{
            background-color: #e8f4f8;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
            border-left: 5px solid #3498db;
        }}
        
        .footer {{
            margin-top: 50px;
            padding-top: 20px;
            border-top: 2px solid #ecf0f1;
            text-align: center;
            color: #7f8c8d;
        }}
        
        @media print {{
            body {{
                font-size: 12px;
                line-height: 1.4;
                margin: 0;
                padding: 20px;
            }}
            
            .code-block {{
                font-size: 10px;
                page-break-inside: avoid;
            }}
            
            h1, h2, h3 {{
                page-break-after: avoid;
            }}
            
            .section {{
                page-break-inside: avoid;
            }}
        }}
    </style>
</head>
<body>
    {html_content}
    
    <div class="footer">
        <p>Generated on {datetime.datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
        <p>Contact Manager - Enhanced C# Console Application</p>
    </div>
</body>
</html>"""
    
    # Write HTML file
    output_file = 'ContactManager_Documentation.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"✓ HTML documentation generated: {output_file}")
    print("\nTo convert to PDF:")
    print("1. Open the HTML file in any web browser")
    print("2. Press Ctrl+P (or Cmd+P on Mac)")
    print("3. Select 'Save as PDF' as the destination")
    print("4. Choose appropriate settings and save")
    print("\nAlternatively, you can use online HTML to PDF converters.")

def markdown_to_html(markdown_text):
    """Convert markdown to HTML using basic regex replacements"""
    html = markdown_text
    
    # Headers
    html = html.replace('# ', '<h1>')
    html = html.replace('\n## ', '</h1>\n<div class="section">\n<h2>')
    html = html.replace('\n### ', '</h2>\n<h3>')
    html = html.replace('\n#### ', '</h3>\n<h4>')
    
    # Close headers at line breaks
    import re
    html = re.sub(r'<h1>([^<\n]+)', r'<h1>\1</h1>', html)
    html = re.sub(r'<h2>([^<\n]+)', r'<h2>\1</h2>', html)
    html = re.sub(r'<h3>([^<\n]+)', r'<h3>\1</h3>', html)
    html = re.sub(r'<h4>([^<\n]+)', r'<h4>\1</h4>', html)
    
    # Code blocks
    html = re.sub(r'```[a-zA-Z]*\n(.*?)\n```', r'<div class="code-block">\1</div>', html, flags=re.DOTALL)
    html = re.sub(r'```bash\n(.*?)\n```', r'<div class="code-block">\1</div>', html, flags=re.DOTALL)
    html = re.sub(r'```csharp\n(.*?)\n```', r'<div class="code-block">\1</div>', html, flags=re.DOTALL)
    
    # Inline code
    html = re.sub(r'`([^`]+)`', r'<span class="inline-code">\1</span>', html)
    
    # Bold text
    html = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', html)
    
    # Features section with checkmarks
    html = html.replace('- ✅', '<li><span class="checkmark">✅</span>')
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    
    # Wrap feature lists
    html = re.sub(r'((?:<li>.*</li>\s*)+)', r'<div class="feature-list"><ul>\1</ul></div>', html, flags=re.DOTALL)
    
    # Paragraphs
    paragraphs = html.split('\n\n')
    formatted_paragraphs = []
    
    for para in paragraphs:
        para = para.strip()
        if para:
            if not para.startswith('<'):
                para = f'<p>{para}</p>'
            formatted_paragraphs.append(para)
    
    html = '\n\n'.join(formatted_paragraphs)
    
    # Clean up
    html = html.replace('\n', '<br>\n')
    html = html.replace('<br>\n</', '</')
    html = html.replace('<br>\n<div', '<div')
    html = html.replace('<br>\n<h', '<h')
    html = html.replace('<br>\n<li', '<li')
    html = html.replace('<br>\n<ul', '<ul')
    html = html.replace('<br>\n</ul', '</ul')
    html = html.replace('<br>\n</div', '</div')
    
    # Add section wrapper
    html = f'<div class="header-info">{html}</div>'
    
    return html

if __name__ == "__main__":
    create_html_from_markdown()