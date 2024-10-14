# Define an empty list to hold names and numbers
data = []

# Ask the user for input
num_list = int(input("How many number do you want to add? "))

for i in range(num_list):
    # Ask for the name and number
    name = input(f"Enter name for entry {i + 1}: ")
    number = input(f"Enter number for entry {i + 1}: ")
    # Append the name and number as a list to the data array
    data.append([name, number])

# Create separate lists for names and numbers
names = []
numbers = []

# Outer loop to iterate through each person's data
for i in range(len(data)):
    numbers.append(data[i][1])  # Number

# Print names
print("name")
for name in names:
    print(name)

# Print numbers
print("number")
for number in numbers:
    print(number)