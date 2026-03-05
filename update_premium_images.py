import os
import glob
import re

def update_images():
    html_files = glob.glob("c:/Users/anubh/Desktop/DI_Infotech/Purava/*.html")
    css_files = glob.glob("c:/Users/anubh/Desktop/DI_Infotech/Purava/css/*.css")
    
    # Let's map different generic images to specific "premium bidet / faucet" images from Unsplash
    # We'll use these specific IDs that look more like luxury faucets/bidets
    image_replacements = {
        # Generic big bathroom -> Premium Brass Faucet close up
        "1584622650111-993a426fbf0a": "1584622781564-1d987f7333c1", # Actually, 1d987f7333c1 is the brass faucet one.
        # Generic hotel room -> Sleek modern silver faucet
        "1616486029423-aaa4789e8c9a": "1620626011761-996317b8d101",
        # Generic clean aesthetic -> Shower/Jet spray head
        "1552321554-5fefe8c9ef14": "1584622781564-1d987f7333c1", # We need a few more. Let's just use source.unsplash keywords as fallback.
    }
    
    # Actually, a better approach is to just use a list of specific Unsplash photos that match "luxury bidet" or "premium faucet"
    premium_ids = [
        "1620626011761-996317b8d101", # Modern silver faucet
        "1584622781564-1d987f7333c1", # Brass/gold faucet macro
        "1584622650111-993a426fbf0a", # Luxury marble bathroom (keep a few for context)
    ]
    
    # But since the user specifically requested "not any other bathroom accessories" we should restrict to just faucets/bidets.
    # We can use source.unsplash API which redirects to random images but since it's deprecated, let's just find 3 good Unsplash IDs.
    
    # 1. Premium Faucet: 1620626011761-996317b8d101
    # 2. Golden Faucet: 1584622781564-1d987f7333c1
    # 3. Modern Chrome: 1523688881245-7ad734027c17 (Actually another faucet)
    # 4. Shower head / jet: 1504333634005-ee2db97a5135 (Shower head)
    # 5. Handheld spray: 1552321554-5fefe8c9ef14 (Was generic bathroom, let's swap)
    
    faucet_image_1 = "1620626011761-996317b8d101" # Faucet
    faucet_image_2 = "1584622781564-1d987f7333c1" # Golden
    faucet_image_3 = "1520699049698-134f9a01662a" # Sink/Faucet
    faucet_image_4 = "1504333634005-ee2db97a5135" # Shower
    faucet_image_5 = "1595123041936-cbdf0bd21c17" # Brass tap
    
    # Replace in HTML
    for file_path in html_files + css_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace the generic bathroom ones with the faucet specific ones
        content = content.replace("1584622650111-993a426fbf0a", faucet_image_3)
        content = content.replace("1616486029423-aaa4789e8c9a", faucet_image_4)
        content = content.replace("1552321554-5fefe8c9ef14", faucet_image_5)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated images in {os.path.basename(file_path)}")

if __name__ == "__main__":
    update_images()
