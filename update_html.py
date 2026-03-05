import os
import re
import glob

def update_products_html(html_path, images_dir):
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all available images
    available_images = {}
    for img_path in glob.glob(os.path.join(images_dir, '*.*')):
        basename = os.path.basename(img_path)
        code = os.path.splitext(basename)[0]
        # Store relative path for HTML
        available_images[code] = f"images/products/{basename}"

    def replacer(match):
        card_start = match.group(1)
        info_start = match.group(2)
        h3_content = match.group(3)
        
        # Find all codes like HF-xxx, ST-xxx
        codes = re.findall(r'(HF-\d+|ST-\d+|SH[BA]-\d+)', h3_content)
        
        img_src = None
        for code in codes:
            if code in available_images:
                img_src = available_images[code]
                break
        
        if not img_src:
            img_src = "https://images.unsplash.com/photo-1584622781564-1d987f7333c1?auto=format&fit=crop&q=80&w=600" # fallback
            
        # construct replacement
        img_div = f'\n                        <div class="product-img">\n                            <img src="{img_src}" alt="{h3_content}">\n                        </div>\n                        '
        return f'{card_start}{img_div}{info_start}{h3_content}</h3>'

    
    new_content = re.sub(r'(<div class="product-card">)\s*(<div class="product-info">\s*<h3>)([^<]+)</h3>', replacer, content)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {html_path}")

if __name__ == "__main__":
    html_file = "c:/Users/anubh/Desktop/DI_Infotech/Purava/products.html"
    images_folder = "c:/Users/anubh/Desktop/DI_Infotech/Purava/images/products"
    update_products_html(html_file, images_folder)
