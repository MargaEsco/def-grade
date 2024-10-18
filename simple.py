# Main program
name = input("Enter student's name: ")

g1 = int(input("Enter grade 1: "))
g2 = int(input("Enter grade 2: "))
g3 = int(input("Enter grade 3: "))

# Calculate average
average = (g1 + g2 + g3) / 3

# Determine performance
if average >= 90:
    performance = "Excellent"
elif average >= 80:
    performance = "Good"
else:
    performance = "Needs Improvement"

# Display results
print(f"\n{name}'s Results:")
print(f"Average: {average:.2f}")
print(f"Performance: {performance}")


