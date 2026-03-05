import glob
import re

def update_navigation():
    html_files = glob.glob("c:/Users/anubh/Desktop/DI_Infotech/Purava/*.html")

    new_nav = '''<ul class="nav-links">
                    <li><a href="products.html">Products</a></li>
                    <li><a href="index.html#about">About Us</a></li>
                    <li><a href="contact.html">Contact</a></li>
                    <li><a href="#">Blogs</a></li>
                    <li><a href="#">Options</a></li>
                    <li><a href="enquiry.html" class="btn">Business Enquiry</a></li>
                </ul>'''

    # We need to replace whatever is inside <ul class="nav-links">...</ul>
    nav_pattern = re.compile(r'<ul class="nav-links">.*?</ul>', re.DOTALL)

    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = nav_pattern.sub(new_nav, content)

        # Let's also completely remove any price tags in products.html or anywhere else
        # Because the user said: "Do not include the prices anywhere."
        price_pattern1 = re.compile(r'<p class="price">.*?</p>', re.DOTALL)
        price_pattern2 = re.compile(r'<span class="price-tag">.*?</span>', re.DOTALL)
        
        new_content = price_pattern1.sub('', new_content)
        new_content = price_pattern2.sub('', new_content)

        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated nav & removed prices in {file_path}")

if __name__ == "__main__":
    update_navigation()
