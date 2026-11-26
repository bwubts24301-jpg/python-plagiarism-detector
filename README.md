# 🔍 Python Plagiarism Detector

## 📌 About the Project
The Python Plagiarism Detector is a software application designed to detect similarities between two Python source code files. It helps users identify potential plagiarism by comparing the structure and content of Python programs.

The project uses Python's built-in libraries to calculate code similarity and display the results in an easy-to-understand format.

## ✨ Features
- Select and compare two Python files.
- Detect similarities between source codes.
- Ignore comments and unnecessary whitespace during comparison.
- Calculate similarity percentage.
- Classify results into High, Moderate, and Low similarity.
- Graphical User Interface (GUI) for easy interaction.
- Generate comparison reports in CSV format.

## 🛠️ Technologies Used
- Python
- difflib (SequenceMatcher)
- Tokenize
- CSV
- Tkinter (GUI)

## 📂 Project Structure

```text
Python-Plagiarism-Detector/
│
├── samples/
├── make_samples.py
├── plagiarism_detector.py
├── plagiarism.py
├── report.csv
└── README.md
```

## ⚙️ How to Run

1. Clone this repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Open the project folder:

```bash
cd Python-Plagiarism-Detector
```

3. Run the application:

```bash
python plagiarism_detector.py
```

~ 📊 How It Works

1. The user selects two Python source code files.
2. The application processes and tokenizes the code.
3. Comments and unnecessary whitespace are ignored.
4. The system compares both files using SequenceMatcher.
5. A similarity percentage is calculated.
6. The result is classified as High, Moderate, or Low similarity.

~ ⚠️ Limitations
- Currently supports Python source code files only.
- Detects textual and token-level similarities.
- Does not fully detect semantic similarities or completely restructured code.

~ 🎯 Project Objective
The main objective of this project is to develop a simple and user-friendly tool that helps students and developers identify similarities between Python programs.

~ 👨‍💻 Author
Ankita Dolai

B.Tech CSE CORE  
Brainware University

---

⭐ If you find this project useful, don't forget to star the repository!
