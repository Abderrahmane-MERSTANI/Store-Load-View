import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length rule
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Uppercase rule
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # Lowercase rule
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # Digit rule
    if re.search(r"[0-9]", password):
        score
