# Task 1: Division with error handling
# Write a function divide_numbers(a, b) that:
# Returns the result of a / b if b != 0.
# Returns "Division by zero is not allowed" if b == 0.
# Returns "Invalid input type" if either a or b is not a number.

def divide_numbers(a: float,b: float)->float | str:
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    except TypeError:
        return "Invalid input type"
print(divide_numbers(10, 2))     # 5.0
print(divide_numbers(10, 0))     # Division by zero is not allowed
print(divide_numbers(10, "x"))   # Invalid input type

