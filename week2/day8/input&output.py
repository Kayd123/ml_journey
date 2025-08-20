students = ["Alice", "Brian", "Cynthia"]

with open("student.txt", "w") as f:   # "w" creates/overwrites file
    for name in students:
        f.write(name + "\n")

# Line by line (useful for looping)
with open("student.txt",'r') as f:
    for line in f:
        print(line.strip()) # strip() removes the "\n"

# Full string at once
with open("student.txt", "r") as f:
    content = f.read()
    print(content)

# Appending data
with open("student.txt", "a") as f:
    f.write("David\n")


