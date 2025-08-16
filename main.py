from parse_file import extract_text_from_file
from nlp import natural_language_processing
from cosine_similarity import similarity_score
import os
import glob

def main():

    file_paths = glob.glob("data/*.pdf") + glob.glob("data/*.docx")

    print("====Cv Analyser===")
    print("Similarity score for all resumes:")
    
    for file_path in file_paths:
        text = extract_text_from_file(file_path)
        data_name = os.path.basename(file_path)
        if not os.path.exists(file_path):
            print(f"❌ File does not exist: {file_path}")
            continue
        keywords = natural_language_processing(text)
        similarity_score(keywords, data_name)

if __name__ == "__main__":
    main()
