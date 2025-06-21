import os
from PyPDF2 import PdfMerger

def merge_pdfs(input_files,output_file):
    merger= PdfMerger()
    for file in input_files:
        if os.path.exists(file) and file.endswith(".pdf"):
            merger.append(file)
        else:
            raise   FileNotFoundError(f"File not found or invalid:{file}")

    merger.write(output_file)
    merger.close()