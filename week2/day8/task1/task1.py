# Task: Library Book Records
# Create a file called books.txt.
# Write at least 5 book titles into it, one per line.
# Read the file line by line and print the book titles with line numbers, like this:
    # 1. Harry Potter
    # 2. The Hobbit

# Append two more book titles to the file (without overwriting).
# Read the entire file again as a single string and print it.
# Handle errors gracefully using try/except:
# If the file does not exist, print "File not found." instead of crashing.
# 👉 Bonus: After appending, count and print how many books are now in the file.
def open_file(filename: str):
    """Create, read, append, and display books file with error handling"""
    try:
        # Step 1: Write 5 initial books
        books = [
            "Harry Potter",
            "The Hobbit",
            "Pride and Prejudice",
            "To Kill a Mockingbird",
            "1984"
        ]
        with open(filename, "w") as f:
            for book in books:
                f.write(book + "\n")

        # Step 2: Read line by line with numbering
        print("\nReading file line by line:")
        with open(filename, "r") as f:
            for i, line in enumerate(f, start=1):
                print(f"{i}. {line.strip()}")

        # Step 3: Append 2 more books
        with open(filename, "a") as f:
            f.write("The Hunger Games\n")
            f.write("The Lord of the Rings\n")

        # Step 4: Read full content
        print("\nFull file content:")
        with open(filename, "r") as f:
            content = f.read()
            print(content)

        # Step 5: Bonus - Count total number of books
        total_books = len(content.strip().split("\n"))
        print(f"📚 Total number of books: {total_books}")

    except FileNotFoundError:
        print("File not found")


# Run the function
open_file("books.txt")

