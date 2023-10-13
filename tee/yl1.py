numbers = input("Enter a list of numbers separated by spaces: ")
a = numbers.split()

if len(a) >= 3:
    result = float(a[2]) * 60
    print("Result:", result)
else:
    print("Not enough numbers provided.")
