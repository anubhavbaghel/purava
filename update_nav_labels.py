import glob

files = glob.glob('c:/Users/anubh/Desktop/DI_Infotech/Purava/*.html')

for path in files:
    with open(path, encoding='utf-8') as f:
        content = f.read()

    new_content = content

    # Rename "Health Faucets" to "Products" in nav links
    new_content = new_content.replace(
        '>Health Faucets</a></li>',
        '>Products</a></li>'
    )

    # Rename "Get Quote" to "Business Enquiry"
    new_content = new_content.replace(
        'class="nav-cta">Get Quote</a>',
        'class="nav-cta">Business Enquiry</a>'
    )

    # Add Blogs link before the Business Enquiry CTA if not already there
    if 'blogs.html' not in new_content:
        new_content = new_content.replace(
            '<li><a href="enquiry.html" class="nav-cta">Business Enquiry</a></li>',
            '<li><a href="blogs.html">Blogs</a></li>\n                <li><a href="enquiry.html" class="nav-cta">Business Enquiry</a></li>'
        )

    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated: {path}')
    else:
        print(f'No change: {path}')
