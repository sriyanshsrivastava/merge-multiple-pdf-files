# 🧾 PDF Merger CLI Tool

A simple and robust command-line tool to merge multiple PDF files into one.  
Built using Python and PyPDF2, this script takes a folder of PDF files and merges them in alphabetical order.

---

## 🚀 Features

- Merge multiple PDF files from a folder
- Outputs a single merged PDF
- Automatically handles missing or invalid files
- Easy to run from the command line
- Clean and modular code structure

---

## 🛠️ Requirements

- Python 3.6+
- PyPDF2

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/sriyanshsrivastava/pdf-merger.git
cd pdf-merger
````

2. **(Optional) Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🧪 Example Usage

```bash
python main.py -i data/input -o data/output
```

* `-i` or `--input`: Path to the folder containing PDF files
* `-o` or `--output`: Path to the output folder where the merged file will be saved

Output file will be saved as:

```
data/output/merged_output.pdf
```

---

## 📁 Project Structure

```
pdf_merger/
│
├── pdf_merger/                 # Main package
│   ├── __init__.py
│   ├── cli.py                  # CLI argument parser
│   └── merger.py               # PDF merging logic
│
├── tests/                      # Unit tests
│   └── test_merger.py
│
├── data/                       # Input/output folders
│   ├── input/                  # Place PDF files here
│   └── output/                 # Merged file saved here
│
├── main.py                     # CLI entry point
├── requirements.txt            # List of dependencies
├── README.md                   # Project documentation
└── .gitignore
```

---

## ✅ To Do (Optional Enhancements)

* [ ] Add option to name output file from CLI
* [ ] Merge PDFs from subfolders
* [ ] Add logging
* [ ] GUI version using Tkinter or PyQt

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙋‍♂️ Author

Sriyansh Srivastava
Feel free to contribute or raise issues!

