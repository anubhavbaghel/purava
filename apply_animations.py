import glob
import re

def add_animations():
    html_files = glob.glob("c:/Users/anubh/Desktop/DI_Infotech/Purava/*.html")

    # Patterns to find sections and cards to animate
    section_title_pattern = re.compile(r'(<h2 class="section-title".*?>)', re.IGNORECASE)
    feature_card_pattern = re.compile(r'(<div class="feature-card".*?>)', re.IGNORECASE)
    product_card_pattern = re.compile(r'(<div class="premium-card".*?>)', re.IGNORECASE)
    testimonial_card_pattern = re.compile(r'(<div class="testimonial-card".*?>)', re.IGNORECASE)
    info_card_pattern = re.compile(r'(<div class="contact-info".*?>)', re.IGNORECASE)
    form_card_pattern = re.compile(r'(<div class="contact-form".*?>)', re.IGNORECASE)


    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Inject reveal-up class
        # Add a custom class if not present
        def inject_reveal(match):
            tag = match.group(1)
            if 'reveal-up' not in tag:
                # insert reveal-up right after class="
                return tag.replace('class="', 'class="reveal-up ')
            return tag

        new_content = section_title_pattern.sub(inject_reveal, content)
        new_content = feature_card_pattern.sub(inject_reveal, new_content)
        new_content = product_card_pattern.sub(inject_reveal, new_content)
        new_content = testimonial_card_pattern.sub(inject_reveal, new_content)
        new_content = info_card_pattern.sub(inject_reveal, new_content)
        new_content = form_card_pattern.sub(inject_reveal, new_content)

        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added reveal animations to {file_path}")

if __name__ == "__main__":
    add_animations()
