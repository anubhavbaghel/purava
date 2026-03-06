import os
import glob
import urllib.parse

html_files = glob.glob('*.html')
pdf_filename = "PURAVA 20-11-2025.pdf"
encoded_pdf = urllib.parse.quote(pdf_filename)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Mobile menu update
    old_mobile = '<li class="mobile-only"><a href="enquiry.html" class="nav-cta">Business Enquiry</a></li>'
    new_mobile = f'<li class="mobile-only"><a href="{encoded_pdf}" class="nav-cta-outline" download>Catalogue</a></li>\n                    <li class="mobile-only"><a href="enquiry.html" class="nav-cta">Business Enquiry</a></li>'
    
    # Desktop nav actions update
    old_desktop = '''                <div class="nav-actions desktop-only">
                    <a href="enquiry.html" class="nav-cta">Business Enquiry</a>
                </div>'''
    new_desktop = f'''                <div class="nav-actions desktop-only">
                    <a href="{encoded_pdf}" class="nav-cta-outline" download>Catalogue</a>
                    <a href="enquiry.html" class="nav-cta">Business Enquiry</a>
                </div>'''
                
    content = content.replace(old_mobile, new_mobile)
    content = content.replace(old_desktop, new_desktop)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Added Catalogue download button pointing to {pdf_filename} in HTML files.")
