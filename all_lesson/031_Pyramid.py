# Display pyramid stars shape in Python

number = int(input("Enter the number of rows: "))
for i in range(0, number):
    for j in range(0, number - i - 1):
        print(end=" ")
    for j in range(0, 2 * i + 1):
        print("*", end="")
    print()