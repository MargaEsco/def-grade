#Function to calculate the average grade

def calculate_average(grades_list):
    total = sum(grades_list)
    return total / len(grades_list)

# Function to classify performance based on the average

def classify_performance(average):
    if average >= 90:
        return "Excellent"
    elif average >= 80:
        return "Good"
    else:
        return "Needs Improvement"

# Main function to input and display student grades

def display_student_grades():
    
    # Get the number of students and subjects
    num_students = int(input("Enter the number of students: "))
    num_subjects = int(input("Enter the number of subjects: "))

    students = []  # Store student names
    subjects = []  # Store subject names
    all_grades = []  # Store grades for all students

    # Get the names of subjects
    for _ in range(num_subjects):
        subject = input("Enter subject name: ")
        subjects.append(subject)

    # Get student names and their grades
    for i in range(num_students):
        student_name = input(f"\nEnter the name of student {i + 1}: ")
        students.append(student_name)

        grades = []  # Store grades for the current student
        for subject in subjects:
            grade = int(input(f"Enter grade for {student_name} in {subject}: "))
            grades.append(grade)
        
        all_grades.append(grades)

    # Display grades and performance
    for i in range(num_students):
        print(f"\nGrades for {students[i]}:")
        for j in range(num_subjects):
            print(f"  {subjects[j]}: {all_grades[i][j]}")
        
        average = calculate_average(all_grades[i])
        print(f"  Average: {average:.2f}")
        print(f"  Performance: {classify_performance(average)}")

# Run the main function
display_student_grades()