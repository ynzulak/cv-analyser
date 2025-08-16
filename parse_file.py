import fitz

file_path = ""

def extract_text_from_file(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text
