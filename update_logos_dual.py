import glob
import re

LOGO_MARKUP = '''<a href="index.html" class="logo-wrap">
                    <!-- Light logo: visible on transparent header (dark hero bg) -->
                    <img src="images/logo-light.png" alt="Purava Logo" class="site-logo logo-light">
                    <!-- Dark logo: visible on solid white scrolled header -->
                    <img src="images/logo-dark.png" alt="Purava Logo" class="site-logo logo-dark">
                </a>'''

FOOTER_LOGO = '<img src="images/logo-light.png" class="footer-logo-img" alt="Purava Logo">'

old_logo_patterns = [
    # matches any <a class="logo-wrap"> block including old img/span inside
    re.compile(
        r'<a href="index\.html" class="logo-wrap">.*?</a>',
        re.DOTALL
    ),
]

old_footer_patterns = [
    re.compile(r'<img src="images/logo\.jpeg" class="footer-logo-img"[^>]*>'),
    re.compile(r'<img src="images/logo-light\.png" class="footer-logo-img"[^>]*onerror[^>]*>'),
]

files = glob.glob("c:/Users/anubh/Desktop/DI_Infotech/Purava/*.html")

for path in files:
    with open(path, encoding='utf-8') as f:
        content = f.read()

    orig = content

    # Replace header logo block
    for pat in old_logo_patterns:
        content = pat.sub(LOGO_MARKUP, content, count=1)

    # Replace footer logo
    for pat in old_footer_patterns:
        content = pat.sub(FOOTER_LOGO, content)

    # Replace plain footer logo img with simple logo-light version
    content = content.replace(
        '<img src="images/logo.jpeg" class="footer-logo-img" alt="Purava Logo"\n                    onerror="this.onerror=null; this.style.display=\'none\'; this.nextElementSibling.style.display=\'block\';">',
        FOOTER_LOGO
    )

    if content != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {path}")
    else:
        print(f"No change: {path}")
