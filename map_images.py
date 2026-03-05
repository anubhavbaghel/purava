import fitz
import os

def map_images(pdf_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    
    mapping = {}
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # Get text blocks
        blocks = page.get_text("blocks")
        product_codes = []
        for b in blocks:
            lines = b[4].strip().split('\n')
            for line in lines:
                text = line.strip()
                if any(text.startswith(prefix) for prefix in ["HF-", "ST-", "SHB-", "SHA-"]):
                    code = text.split()[0] # e.g., "HF-001"
                    product_codes.append({
                        "code": code,
                        "bbox": fitz.Rect(b[:4])
                    })
        
        # Get image info
        image_infos = page.get_image_info(xrefs=True)
        
        for info in image_infos:
            xref = info["xref"]
            img_bbox = fitz.Rect(info["bbox"])
            
            # Find the closest product code
            if not product_codes:
                continue
                
            closest_code = None
            min_dist = float('inf')
            
            for pc in product_codes:
                # distance between top-lefts
                dist = abs(pc["bbox"].x0 - img_bbox.x0) + abs(pc["bbox"].y0 - img_bbox.y0)
                if dist < min_dist:
                    min_dist = dist
                    closest_code = pc["code"]
            
            # Extract image
            try:
                base_image = doc.extract_image(xref)
                if not base_image:
                    continue
                image_bytes = base_image["image"]
                ext = base_image["ext"]
                
                # Check dimensions
                if base_image["width"] < 100 or base_image["height"] < 100:
                    continue
                    
                area = base_image["width"] * base_image["height"]
                if closest_code not in mapping or mapping[closest_code]['area'] < area:
                    mapping[closest_code] = {'area': area, 'ext': ext, 'bytes': image_bytes}
            except Exception as e:
                print(f"Error extracting image xref {xref}: {e}")
                
    # Save best images
    for code, data in mapping.items():
        filepath = os.path.join(output_dir, f"{code.replace('/', '_')}.{data['ext']}")
        with open(filepath, "wb") as f:
            f.write(data['bytes'])
        print(f"Mapped {code} to {filepath}")

if __name__ == "__main__":
    pdf_file = "c:/Users/anubh/Desktop/DI_Infotech/Purava/PURAVA 20-11-2025.pdf"
    out_dir = "c:/Users/anubh/Desktop/DI_Infotech/Purava/images/products"
    map_images(pdf_file, out_dir)
