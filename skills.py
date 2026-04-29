skills_list = [
    "python","machine learning","data science","numpy",
    "pandas","scikit-learn","deep learning","nlp",
    "computer vision","sql","power bi"
]

def extract_skills(text):

    text = text.lower()
    found = []

    for skill in skills_list:
        if skill in text:
            found.append(skill)

    return found