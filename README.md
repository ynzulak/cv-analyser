# CV‑Analyser

An application that filters resumes (CVs) using job offer text.

---

## Table of Contents

- [Introduction](#introduction)  
- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Structure](#structure)  
- [Possible Improvements](#possible-improvements)  
- [License](#license)  

---

## Introduction

CV‑Analyser is a Python application that helps streamline the process of matching job offers with applicant CVs. It takes a job offer text and a set of CV documents, and filters/ranks the CVs based on how well they match with the content of the job offer using natural language processing.

---

## Features

- Parses CV files (various formats, depending on implementation).  
- Extracts text from both job offer description and CV documents.  
- Computes similarity between CVs and job offer text (e.g., using cosine similarity).  
- Outputs filtered or ranked list of CVs based on relevance to the job offer.

---

## Requirements

These are the minimal prerequisites to run the project:

- Python (version X.Y or newer)  
- Required Python packages (see `requirements.txt`)  

You’ll need typical NLP libraries, plus possibly PDF / Word document parsing tools depending on what formats of CVs you want to support.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ynzulak/cv-analyser.git
   cd cv-analyser
   ```

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # on macOS / Linux
   # or on Windows:
   # venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Here’s how you can use the application:

```bash
python main.py --job_offer "path/to/job_offer.txt" --cv_dir "path/to/cv_folder/"
```

- `--job_offer`: path to a text file (or document) containing the job offer description.  
- `--cv_dir`: path to a directory containing CV files to compare.

After running, the app will output (to console or as a file, depending on implementation) the CVs ordered or filtered by how well they match the job offer.

You may also find utility scripts/modules:

- `parse_file.py` — for parsing CV files or job offer documents.  
- `nlp.py` — for text processing (e.g. tokenization, cleaning, etc.).  
- `cosine_similarity.py` — for computing similarity metrics between texts.

---

## Structure

Here’s a rough overview of the project structure:

```
cv‑analyser/
├── data/                  # Sample data (CVs, job offers) if included
├── main.py                # Main entry point
├── parse_file.py          # File parsing utilities
├── nlp.py                 # NLP / text cleaning / preprocessing
├── cosine_similarity.py   # Similarity computation
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── .gitignore
```