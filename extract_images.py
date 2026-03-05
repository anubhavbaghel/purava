import fitz
import os
import io
from PIL import Image

def extract_images(pdf_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    
    img_index = 1
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        image_list = page.get_images(full=True)
        
        # We can also get text blocks to associate images with text nearby if we want.
        # But first let's just dump all images.
        text_blocks = page.get_text("blocks")
        
        # Simple heuristic: sort text blocks and images by Y coordinate
        # This is a bit advanced, let's just extract the images for now to see what we have
        # and maybe name them by page num and index
        
        for img in image_list:
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            # Avoid extracting tiny images (like logos or icons)
            if base_image["width"] < 100 or base_image["height"] < 100:
                continue
                
            image_filename = f"page{page_num+1}_img{img_index}.{image_ext}"
            image_filepath = os.path.join(output_dir, image_filename)
            
            with open(image_filepath, "wb") as f:
                f.write(image_bytes)
                
            print(f"Extracted {image_filename}")
            img_index += 1

if __name__ == "__main__":
    pdf_file = "c:/Users/anubh/Desktop/DI_Infotech/Purava/PURAVA 20-11-2025.pdf"
    out_dir = "c:/Users/anubh/Desktop/DI_Infotech/Purava/images/products_raw"
    extract_images(pdf_file, out_dir)
