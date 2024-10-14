#INTR0DUCTION TO NESTED LOOPS - REFERS TO A LOOP WITHIN A LOOP
#NESTED LOOPS STRUCTURE LOOKS LIKE:

#SYNTAX: OUTER_LOOP
            #INNER_LOOP
                # STATEMENTS INSIDE INNER LOOP
            # STATEMENTS INSIDE OUTER LOOP

#NESTED FOOR LOOP - REFERS TO A FOR LOOP WITIHN A ANOTHER FOR LOOP THEN ITS CALLED NESTED FOR LOOP

#EXAMPLE AND HOW IT LOOKS LIKE

list1 = [1, 2, 3]
list2 = [4, 5, 6]

for i in list1:
    for j in list2:
        print(i, j)
    print()

#Basic Nested Loop (Multiplication Table)
for i in range(1, 6):  # Outer loop: numbers 1 to 5
    for j in range(1, 6):  # Inner loop: numbers 1 to 5
        print(f"{i} * {j} = {i * j}", end="\t")  # Multiply i and j
    print()  # Prints a newline after each row

#Nested Loops with Lists (Pair Combinations)
colors = ["Red", "Green", "Blue"]
shapes = ["Circle", "Square"]

for color in colors:  # Outer loop over colors
    for shape in shapes:  # Inner loop over shapes
        print(f"{color} {shape}")

#Nested Loops with 2D Lists (Matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:  # Outer loop over rows
    for elem in row:  # Inner loop over elements in each row
        print(elem, end=" ")  # Print elements in the same row
    print()  # Newline after each row

# Nested Loops for Patterns

n = 5
for i in range(1, n+1):  # Outer loop for rows
    for j in range(i):  # Inner loop for columns
        print("*", end="")  # Print star
    print()  # Newline after each row

#Nested Loops with Strings (Character Combination)

string1 = "AB"
string2 = "XY"

for char1 in string1:  # Outer loop over string1
    for char2 in string2:  # Inner loop over string2
        print(f"{char1}{char2}")
        
# Nested Loop for Cartesian Product

list1 = [1, 2]
list2 = ['A', 'B']

for i in list1:  # Outer loop over numbers
    for j in list2:  # Inner loop over letters
        print(f"({i}, {j})")

#Nested Loop to Sum Pairs

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

for num1 in numbers1:  # Outer loop
    for num2 in numbers2:  # Inner loop
        print(f"{num1} + {num2} = {num1 + num2}")

#Basic Nested Loops

names_matrix = [
    ["Alice", "Bob", "Charlie"],
    ["David", "Eva", "Frank"],
    ["Grace", "Hannah", "Ian"]
]

for row in names_matrix:  # Outer loop over rows
    for name in row:  # Inner loop over names in each row
        print(name, end=" ")  # Print names in the same row
    print()  # Newline after each row

#Using List Comprehension and join()

names_matrix = [
    ["Alice", "Bob", "Charlie"],
    ["David", "Eva", "Frank"],
    ["Grace", "Hannah", "Ian"]
]

for row in names_matrix:
    print(" ".join(name for name in row))  # Join names with a space

#Using a Function

def print_names_matrix(matrix):
    for row in matrix:
        print(" ".join(name for name in row))  # Join names with a space

names_matrix = [
   ["MIKO", "MARGA", "MARGAUX"],
    ["ESCOBIDO", "GARET", "CUTE"],
    ["CUTEKO", "CUTIE", "MARGACUTIE"]
]

print_names_matrix(names_matrix)

#Using a Single Print Statement
names_matrix = [
    ["MIKO", "MARGA", "MARGAUX"],
    ["ESCOBIDO", "GARET", "CUTE"],
    ["CUTEKO", "CUTIE", "MARGACUTIE"]
]

print("\n".join(" ".join(name for name in row) for row in names_matrix))