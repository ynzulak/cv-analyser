import glob
import os
import tkinter as tk
from tkinter import filedialog

from nlp import natural_language_processing
from cosine_similarity import similarity_score
from parse_file import extract_text_from_file


def main():
    file_paths = glob.glob("data/*.pdf") + glob.glob("data/*.docx")

    print("==== CV Analyser ===")

    job_offer_choice = input(
        "Do you want to paste your own job offer? "
        "If not, a sample 'Frontend Developer' offer will be used. (Y/N): "
    ).strip().upper()

    if job_offer_choice == "N":
        job_quote = "Join XYZ as a Frontend Developer! We're looking for a skilled developer experienced in modern JavaScript frameworks (React, Typescript) to build responsive, user-friendly web applications. Work in a collaborative, innovative environment with global impact. Location: Hybrid (Warsaw or remote in Poland). Full-time, Mid/Senior level. Apply now and shape the future of technology with us!"
        
    elif job_offer_choice == "Y":
        job_quote = input("Please type your job offer:\n")
    else:
        print("Invalid choice. Exiting.")
        return

    resume_choice = input(
        "Do you want to paste your own job resumes? "
        "If not, a three samples CV will be used. (Y/N): "
    ).strip().upper()

    if resume_choice == "N":
        file_paths = glob.glob("data/*.pdf") + glob.glob("data/*.docx")
    elif resume_choice == "Y":
        root = tk.Tk()
        root.withdraw()

        file_paths = filedialog.askopenfilenames(
            title="Choose your PDF or Doc/Docx CV files",
            filetypes=[("Documents", "*.pdf *.doc *.docx"), ("All files", "*.*")]
        )
    else:
        print("Invalid choice. Exiting.")
        return

    print("\nSimilarity score for all resumes:\n")

    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f"File does not exist: {file_path}")
            continue

        cv_text = extract_text_from_file(file_path)
        data_name = os.path.basename(file_path)

        similarity_score(cv_text, job_quote, data_name)


if __name__ == "__main__":
    main()
