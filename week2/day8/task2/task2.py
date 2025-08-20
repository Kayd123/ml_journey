# Task: Student Records
# Instructions:
# Create a file called students.txt.
# Write at least 5 student names into it, one per line.
# Example:
# Alice
# Brian
# Catherine
# David
# Esther
# Read the file line by line and print the student names with line numbers.
# Example output:
# 1. Alice
# 2. Brian
# 3. Catherine
# 4. David
# 5. Esther
# Append 2 new student names to the file (without overwriting).
# Read the entire file as a single string and print it.
# Count how many students are now in the file and print the total.
# Handle errors gracefully with try/except. If the file doesn’t exist, print "File not found."
# ⚡ Bonus Challenge:
# After appending, print only the new students that were added.
# 👉 Your task: Write a Python script student_records.py to complete the above.

def file_open(filename: str):
    """Create, read, append, and display"""
    try:
        # Step 1: Write initial 5 students
        students = ["Alice", "Brian", "Catherine", "David", "Esther"]
        with open(filename, "w") as file:
            for student in students:
                file.write(student + "\n")

        # Step 2: Read line by line with numbering
        print("\nStudents list (with line numbers):")
        with open(filename, "r") as file:
            for index, line in enumerate(file, start=1):
                print(f"{index}. {line.strip()}")

        # Step 3: Append 2 new students
        new_students = ["John", "Skylar"]
        with open(filename, "a") as file:
            for student in new_students:
                file.write(student + "\n")

        # Step 4: Read full contents
        print("\nFull file contents:")
        with open(filename, "r") as file:
            content = file.read()
            print(content)

        # Step 5: Count total students
        with open(filename, "r") as file:
            students_count = len(file.readlines())
            print(f"Total Students count: {students_count}")

        # Bonus: Print only new students
        print("\nNewly added students:")
        for student in new_students:
            print(student)

    except FileNotFoundError:
        print("File not found")


file_open("students.txt")


