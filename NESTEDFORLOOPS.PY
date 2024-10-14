# Ask the user how many items to add in two lists
n1 = int(input("How many items for list1? "))
n2 = int(input("How many items for list2? "))

# Initialize the lists
list1 = []
list2 = []

# Get items for list1
print("Enter items for list1:")
for i in range(n1):
    item = input(f"Item {i + 1}: ")
    list1.append(item)

# Get items for list2
print("\nEnter items for list2:")
for i in range(n2):
    item = input(f"Item {i + 1}: ")
    list2.append(item)

# Nested loop to print all combinations of list1 and list2
print("\nCombinations of items from list1 and list2:")
for i in list1:
    for j in list2:
        print(f"{i} - {j}")