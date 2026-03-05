import re

def update_products_html(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Add new CSS file link
    if 'css/products_page.css' not in content:
        content = content.replace(
            '<link rel="stylesheet" href="css/style.css">',
            '<link rel="stylesheet" href="css/style.css">\n    <link rel="stylesheet" href="css/products_page.css">'
        )
    
    # Step 2: Wrap existing sections in the new aesthetic wrapper and section tags
    # Section replacer for Health Faucets, Tubes, and Hooks
    def section_replacer(match):
        id_attr = match.group(1)
        title = match.group(2)
        grid_content = match.group(3)
        
        # Determine if it needs a premium badge (e.g., Faucets)
        is_premium = "Health Faucets" in title or "Tubes" in title
        
        # Process the grid content to update classes
        # Regex to match the old product card structure
        card_pattern = r'(<div class="product-card">)\s*(<div class="product-img">)\s*(<img[^>]+>)\s*(</div>)\s*(<div class="product-info">)\s*(<h3>[^<]+</h3>)\s*(<p class="price">[^<]+</p>)\s*(</div>)\s*(</div>)'
        
        def card_replacer(card_match):
            img_tag = card_match.group(3)
            h3_tag = card_match.group(6)
            price_content = re.search(r'>([^<]+)<', card_match.group(7)).group(1)
            
            badge_html = '\n                        <div class="premium-badge">Best Seller</div>' if is_premium and ("Queen" in h3_tag or "Evo" in h3_tag or "Zen" in h3_tag) else ''
            
            return f'''
                    <div class="premium-card">{badge_html}
                        <div class="premium-card-img">
                            {img_tag}
                        </div>
                        <div class="premium-card-info">
                            {h3_tag}
                            <span class="price-tag">{price_content}</span>
                        </div>
                    </div>'''
            
        new_grid_content = re.sub(card_pattern, card_replacer, grid_content)
        
        # Construct the new section block
        return f'''
            <div id="{id_attr}" class="product-category-section">
                <div class="product-category-header">
                    <h2>{title}</h2>
                    <p>Explore our highly engineered collection of {title.lower()} designed for exceptional performance and longevity.</p>
                </div>
                <div class="premium-product-grid">
{new_grid_content}
                </div>
            </div>'''

    
    # Let's replace the outer container
    content = content.replace('<section class="section" style="padding-top: 0;">\n        <div class="container">', 
                              '<section class="products-page-wrapper">\n        <div class="container">')
    
    # Remove the HR tags
    content = re.sub(r'<hr style="[^"]+">\s*', '', content)
    
    # Apply the section replacer to all 3 sections
    section_pattern = r'<div id="([^"]+)"[^>]*>\s*<h2 class="section-title">([^<]+)</h2>\s*<div class="product-grid">(.*?)</div>\s*</div>'
    
    content = re.sub(section_pattern, lambda m: section_replacer(m), content, flags=re.DOTALL)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Updated products.html with premium aesthetics.")

if __name__ == "__main__":
    update_products_html("c:/Users/anubh/Desktop/DI_Infotech/Purava/products.html")
