import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Classification
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    print("\nPassword Strength:", strength)

    if feedback:
        print("Suggestions to improve security:")
        for item in feedback:
            print("-", item)

# Main Program
password = input("Enter your password: ")
check_password_strength(password)