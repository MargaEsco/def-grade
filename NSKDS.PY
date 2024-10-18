def user_grades(grade):
    if grade >= 80 and grade <= 100:
        return "Very good"
    elif grade >= 70 and grade <= 80:
        return "Good"
    elif grade <= 60 and grade >= 50:
        return "needs improvement"
    elif grade < 50:
        return "Failed"

usergrade = int(input("Enter your grade: "))
print(user_grades(usergrade))

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

