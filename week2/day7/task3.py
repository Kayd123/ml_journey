# Write a small script that:
# Asks the user for two numbers and divides them using divide_numbers.
# Asks the user for a filename and reads it using read_file.

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"


# --- Main script ---
if __name__ == "__main__":
    # Ask for two numbers
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    result = divide_numbers(a, b)
    print("Division result:", result)

    # Ask for filename
    filename = input("Enter filename to read: ")
    file_content = read_file(filename)
    print("\nFile content:\n", file_content)



