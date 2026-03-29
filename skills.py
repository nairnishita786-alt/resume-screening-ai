SKILLS = [
    "python","java","sql","machine learning",
    "data analysis","nlp","deep learning",
    "html","css","javascript"
]

def extract_skills(text):
    return [skill for skill in SKILLS if skill in text]
