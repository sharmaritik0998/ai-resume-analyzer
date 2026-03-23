def generate_suggestions(missing_skills, role):
    suggestions = []

    for skill in missing_skills:
        suggestions.append(f"Try gaining practical experience in {skill}.")

    if role == "Data Science":
        suggestions.append("Work on ML projects using real-world datasets.")
    elif role == "Web Development":
        suggestions.append("Build and deploy responsive web apps.")
    elif role == "Marketing":
        suggestions.append("Create campaigns or SEO-based projects.")
    elif role == "Finance":
        suggestions.append("Add Excel or financial analysis projects.")
    elif role == "Human Resources":
        suggestions.append("Include recruitment or HR case studies.")

    return suggestions