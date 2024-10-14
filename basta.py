#More simple
grade = int(input("Enter your grade: "))

# Determine performance based on the grade
if grade >= 90:
    performance = "Kana jud tarung skwela!"
elif grade >= 80:
    performance = "Pwede na maka Ice cream"
else:
    performance = "Needs Improvement sa dong"

# Display result
print(f"Your Performance: {performance}")