import os
import glob

def update_logos():
    html_files = glob.glob("c:/Users/anubh/Desktop/DI_Infotech/Purava/*.html")
    
    header_old = '<a href="index.html" class="logo">PURAVA</a>'
    header_new = '''<a href="index.html" class="logo">
                    <img src="images/logo.png" alt="Purava Logo" class="site-logo" onerror="this.onerror=null; this.outerHTML='<span class=\\'logo-text\\'>P<span>U</span>RAVA</span>';">
                </a>'''
                
    footer_old = '<h2 class="logo" style="color: var(--white); margin-bottom: 15px;">PURAVA</h2>'
    footer_new = '''<a href="index.html" class="logo" style="margin-bottom: 15px; display: inline-block;">
                        <img src="images/logo.png" alt="Purava Logo" class="footer-logo" onerror="this.onerror=null; this.outerHTML='<span class=\\'logo-text\\' style=\\'color: white;\\'>P<span>U</span>RAVA</span>';">
                    </a>'''
                    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace(header_old, header_new)
        content = content.replace(footer_old, footer_new)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated logos in {os.path.basename(file_path)}")

if __name__ == "__main__":
    update_logos()
