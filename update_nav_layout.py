import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update navigation items
    old_nav = '''                    <li><a href="enquiry.html" class="nav-cta">Business Enquiry</a></li>
                </ul>'''
    new_nav = '''                    <li class="mobile-only"><a href="enquiry.html" class="nav-cta">Business Enquiry</a></li>
                </ul>
                <div class="nav-actions desktop-only">
                    <a href="enquiry.html" class="nav-cta">Business Enquiry</a>
                </div>'''
    
    content = content.replace(old_nav, new_nav)

    # 2. Make index.html header solid by default
    if file == 'index.html':
        content = content.replace('<header class="transparent" id="site-header">', '<header class="solid" id="site-header">')
        
        # Remove the inline scroll script
        script_pattern = re.compile(r'\s*// Transparent → solid header on scroll\s*const header = document\.getElementById\(\'site-header\'\);\s*window\.addEventListener\(\'scroll\', \(\) => \{\s*if \(window\.scrollY > 60\) \{\s*header\.classList\.replace\(\'transparent\', \'solid\'\);\s*\} else \{\s*header\.classList\.replace\(\'solid\', \'transparent\'\);\s*\}\s*\}\);\s*', re.DOTALL)
        content = re.sub(script_pattern, '', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated HTML files.')
