# Generate Data
# Create a 5×5 matrix (list of lists) filled with random integers between 1 and 50.
# Transformations (using list comprehensions only)
# Flatten the 5×5 matrix into a single list.
# Create a list of all even numbers from the matrix.
# Create a new 5×5 matrix where each element is squared.
# Create a dictionary mapping each unique number in the flattened list → its frequency.
# Comparison
# Implement the flattening step using:
# A nested list comprehension.
# A standard nested for-loop.
# Measure and compare their runtimes.
# Output
# Print the original matrix.
# Print each transformed version clearly labeled.
# Show the runtime results for comprehension vs. for-loop.
import random
import time

# Generate Data
numbers = [[random.randint(1, 50) for _ in range(5)] for _ in range(5)]

print("Original matrix:")
for row in numbers:
    print(row)

# Transformations
flatten = [num for row in numbers for num in row]
print("Flattened matrix:", flatten)

even_list = [num for row in numbers for num in row if num % 2 == 0]
print("Even numbers:", even_list)

squared_numbers = [[num ** 2 for num in row] for row in numbers]
print("Squared matrix:")
for row in squared_numbers:
    print(row)

freq = {num: flatten.count(num) for num in set(flatten)}
print("Frequencies:", freq)

# Comparison
start = time.time()
flattened_comp = [num for row in numbers for num in row]
end = time.time()
print("Comprehension time:", end - start)

start = time.time()
flatten_for = []
for row in numbers:
    for num in row:
        flatten_for.append(num)
end = time.time()
print("For-loop time:", end - start)
