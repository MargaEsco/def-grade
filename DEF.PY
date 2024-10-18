def check_grades(grade):
    if grade >= 80 and grade <= 100:
        return "Very Good!"
    elif grade >= 70 and grade <= 80:
        return "Good"
    elif grade >= 50 and grade <= 60:
        return "Needs Improvement"
    elif grade < 60:
        return "Failed"
    else:
        return "Invalid grade"

usergrade = int(input("Enter your grade: "))
print(check_grades(usergrade))

