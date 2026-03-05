import re
import random
import glob
import os

def replace_with_custom_faucets():
    html_files = glob.glob("c:/Users/anubh/Desktop/DI_Infotech/Purava/*.html")
    css_files = glob.glob("c:/Users/anubh/Desktop/DI_Infotech/Purava/css/*.css")

    # The 4 amazing premium health faucet images we generated
    faucets = [
        "images/faucet_brass.png",
        "images/faucet_chrome.png",
        "images/faucet_matte.png",
        "images/faucet_gold.png"
    ]

    # Regex to find any Unsplash image
    unsplash_pattern = re.compile(r'https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+(\?auto=format&fit=crop&q=80&w=\d+)?')

    for file_path in html_files + css_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # We will replace uniquely found ones with a shuffled choice to give variety
        def replacer(match):
            return random.choice(faucets)
        
        # Or better yet, just replace all Unsplash references
        # Ensure we maintain the quotes around it if we're replacing the whole URL
        new_content = unsplash_pattern.sub(replacer, content)

        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Removed unsplash links from {os.path.basename(file_path)} and injected luxury custom renders.")

if __name__ == "__main__":
    replace_with_custom_faucets()
