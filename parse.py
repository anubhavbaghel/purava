import os
import sys

try:
    import fitz  # PyMuPDF
except ImportError:
    pass

try:
    import pandas as pd
except ImportError:
    pass

def parse_pdf(filepath, outpath):
    try:
        doc = fitz.open(filepath)
        text = ""
        for page in doc:
            text += page.get_text()
        with open(outpath, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"PDF parsed successfully: {outpath}")
    except Exception as e:
        print(f"Error parsing PDF: {e}")

def parse_xlsx(filepath, outpath):
    try:
        xls = pd.ExcelFile(filepath)
        text = ""
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(filepath, sheet_name=sheet_name)
            text += f"\\n--- Sheet: {sheet_name} ---\\n"
            text += df.to_string()
        with open(outpath, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"XLSX parsed successfully: {outpath}")
    except Exception as e:
        print(f"Error parsing XLSX: {e}")

if __name__ == "__main__":
    pdf_path = "c:/Users/anubh/Desktop/DI_Infotech/Purava/PURAVA 20-11-2025.pdf"
    xlsx_path = "c:/Users/anubh/Desktop/DI_Infotech/Purava/Purava- Keywords and Competitors Analysis .xlsx"
    out_pdf = "c:/Users/anubh/Desktop/DI_Infotech/Purava/purava_pdf_text.txt"
    out_xlsx = "c:/Users/anubh/Desktop/DI_Infotech/Purava/purava_xlsx_text.txt"
    
    parse_pdf(pdf_path, out_pdf)
    parse_xlsx(xlsx_path, out_xlsx)
