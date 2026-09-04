import re


def analyze_password(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Number
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Special character
    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # Strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    print("\n========== PASSWORD ANALYSIS ==========")
    print("Strength:", strength)
    print("Score:", score, "/ 6")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print("•", item)
    else:
        print("✅ Excellent password!")


password = input("Enter password: ")

analyze_password(password)
