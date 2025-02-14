# Simple Grade Calculator

# Get user input
score = float(input("Enter your score (0-100): "))

# Determine grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Display result
print(f"Your grade is: {grade}")
