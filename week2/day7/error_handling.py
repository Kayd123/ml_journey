#10 / 0   # ❌ ZeroDivisionError
#Step 1: Understand error handling
# errors can stop a program

#'catch' errors with try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# step 2: Write safe_divide(a,b)
# We want a function that:
# Returns the result when division is possible.
# Returns "Cannot divide by zero" if denominator is 0.
def safe_divide(a: float, b: float) -> float | str:
    """Safely divide two numbers, handling division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # Cannot divide by zero

# Step 3:  write function to open a file safely
# function:
def open_file(filename: str) -> str:
    """Open a file and return its contents, handling file not found errors."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"
print(open_file("existing.txt"))   # prints file content
print(open_file("missing.txt"))    # File not found

