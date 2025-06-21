import os
import argparse
from .merger import merge_pdfs

def parse_args():
    parser = argparse.ArgumentParser(description="Merge multiple PDF files into one.")
    parser.add_argument( "-i","--input", required=True,help="Input folder path containing PDFs.")
    parser.add_argument( "-o","--output", required=True,help="Output folder path")
    return parser.parse_args()


def main():
    args = parse_args()
    input_folder= args.input
    output_folder = args.output

    # collect PDF files from input folder
    if not os.path.isdir(input_folder):
        print(f"Error: Input path '{input_folder}' is not a directory.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    input_files = sorted([
        os.path.join(input_folder,f)
        for f in os.listdir(input_folder)
        if f.lower().endswith(".pdf")
    ])

    if not input_files:
        print("No PDF file found in the input folder.")
        return

    output_file_path = os.path.join(output_folder, "merged_output.pdf")

    try:
        merge_pdfs(input_files,output_file_path)
        print(f"Mersed PDF saved to {output_file_path}")
    except Exception as e:
        print(f"Error during merging: {e}")
