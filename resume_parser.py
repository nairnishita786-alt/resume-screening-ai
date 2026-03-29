from pdfminer.high_level import extract_text

def extract_resume_text(file_path):
    return extract_text(file_path)
