# Number of students to enter grades for
num_students = int(input("Enter the number of students: "))

# List to store performances
performances = []

# Loop through the number of students
for i in range(num_students):
    grade = int(input(f"Enter grade for student {i + 1}: "))
    
    # Determine performance based on the grade
    if grade >= 90:
        performance = "Excellent"
    elif grade >= 80:
        performance = "Good"
    else:
        performance = "Needs Improvement"
    
    # Store the performance
    performances.append(performance)

# Display results
print("\nPerformances:")
for i in range(num_students):
    print(f"Student {i + 1}: {performances[i]}")