import re

def load_skills():
    with open("data/skills_list.txt", "r") as f:
        return [skill.strip().lower() for skill in f.readlines()]

def clean_text(text):
    return re.sub(r'[^a-zA-Z0-9\s]', ' ', text.lower())


def get_variations(skill):
    variations_map = {
        "machine learning": ["ml"],
        "artificial intelligence": ["ai"],
        "javascript": ["js"],
        "react": ["reactjs"],
        "node": ["nodejs"],
        "c++": ["cpp"],
        "power bi": ["powerbi"],
        "human resources": ["hr"],
        "search engine optimization": ["seo"]
    }

    variations = [skill]
    if skill in variations_map:
        variations += variations_map[skill]

    return variations


def extract_skills(text, skills_list):
    text = clean_text(text)
    found_skills = []

    for skill in skills_list:
        variations = get_variations(skill)

        for v in variations:
            pattern = r'\b' + re.escape(v) + r'\b'
            if re.search(pattern, text):
                found_skills.append(skill)

    return list(set(found_skills))