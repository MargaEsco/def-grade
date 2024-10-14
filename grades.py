# Sample data: List of students and their grades in different subjects
students = ["Juan", "Ana", "Mark"]
subjects = ["Math", "Science", "English"]

# Store grades for each student and subject
grades = [
    [85, 90, 88],  # Grades for Juan
    [78, 82, 80],  # Grades for Ana
    [92, 89, 95]   # Grades for Mark
]

# Loop through each student
for i in range(len(students)):
    print(f"Grades for {students[i]}:")

    total = 0  # Initialize total for average calculation

    # Loop through each subject to print grades
    for j in range(len(subjects)):
        print(f"  {subjects[j]}: {grades[i][j]}")
        total += grades[i][j]  # Add grade to total

    # Calculate the average grade
    average = total / len(subjects)
    print(f"  Average: {average:.2f}")

    # Use if-elif-else to classify the student's performance
    if average >= 90:
        print("  Performance: Excellent\n")
    elif average >= 80:
        print("  Performance: Good\n")
    else:
        print("  Performance: Needs Improvement\n")


# Sample data: List of students and their grades in different subjects
students = ["Juan", "Ana", "Mark"]
subjects = ["Math", "Science", "English"]

grades = [
    [85, 90, 88],  # Grades for Juan
    [78, 82, 80],  # Grades for Ana
    [92, 89, 95]   # Grades for Mark
]

# Function to calculate the average grade
def calculate_average(grades_list):
    total = 0
    for grade in grades_list:
        total += grade
    return total / len(grades_list)

# Function to classify performance based on average
def classify_performance(average):
    if average >= 90:
        return "Excellent"
    elif average >= 80:
        return "Good"
    else:
        return "Needs Improvement"

# Main function to display student grades and performance
def display_student_grades():
    for i in range(len(students)):
        print(f"Grades for {students[i]}:")
        
        # Print each subject's grade
        for j in range(len(subjects)):
            print(f"  {subjects[j]}: {grades[i][j]}")

        # Calculate average and classify performance
        average = calculate_average(grades[i])
        print(f"  Average: {average:.2f}")
        print(f"  Performance: {classify_performance(average)}\n")

# Run the main function
display_student_grades()