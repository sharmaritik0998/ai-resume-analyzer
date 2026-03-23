def detect_role(text):
    text = text.lower()

    roles = {
        "Data Science": ["machine learning", "data", "python"],
        "Web Development": ["html", "css", "javascript", "react"],
        "Android Development": ["android", "kotlin", "flutter"],
        "Marketing": ["marketing", "seo", "branding"],
        "Finance": ["finance", "accounting", "investment"],
        "Human Resources": ["recruitment", "hr", "talent"]
    }

    for role, keywords in roles.items():
        for word in keywords:
            if word in text:
                return role

    return "General Role"