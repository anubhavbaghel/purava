import glob
import os

def swap_images():
    html_files = glob.glob("c:/Users/anubh/Desktop/DI_Infotech/Purava/*.html")
    css_files = glob.glob("c:/Users/anubh/Desktop/DI_Infotech/Purava/css/*.css")

    replacements = {
        "faucet_brass.png": "faucet_accurate_1.png",
        "faucet_chrome.png": "faucet_accurate_2.png",
        "faucet_matte.png": "faucet_accurate_3.png",
        "faucet_gold.png": "faucet_accurate_4.png"
    }

    for file_path in html_files + css_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = content
        for old_img, new_img in replacements.items():
            new_content = new_content.replace(old_img, new_img)

        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Swapped images in {os.path.basename(file_path)}")

if __name__ == "__main__":
    swap_images()
