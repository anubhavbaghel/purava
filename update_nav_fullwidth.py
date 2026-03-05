import os
import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change container to container-fluid for the header
    old_header = '''    <header class="solid" id="site-header">
        <div class="container">
            <nav class="navbar">'''
    
    new_header = '''    <header class="solid" id="site-header">
        <div class="container" style="max-width: 100%; padding: 0 40px;">
            <nav class="navbar">'''
            
    content = content.replace(old_header, new_header)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated header container width in HTML files.')
