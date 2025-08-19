# Task 2: Reading a file
# Write a function read_file(filename) that:
# Opens the file and returns its contents.
# If the file does not exist, return "File not found".
# If there’s another error (like permission denied), return "Error opening file".

def read_file(filename: str) -> str:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"

print(read_file("notes.txt"))        # file contents
print(read_file("missing.txt"))      # File not found

