"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while  True:
    try:
        print("Enter a list of numbers separated by commas:")
        numbers = [float(value) for value in input().split(",")]
        while len(numbers) > 2:
            numbers.pop(0)
            numbers.pop()
        if len(numbers) == 2:
            median = (numbers[0] + numbers[1])/ 2
        else:
             median = numbers[0]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median)
