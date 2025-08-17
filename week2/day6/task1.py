# Generate Data
# Create a list of 30 random integers between 1 and 200.
# Transformations (using list comprehensions only)
# Create a new list of the cubes of all numbers.
# Extract only the numbers divisible by 5.
# Convert all numbers to strings prefixed with "num_" (example: num_25).
# Comparison
# Using both for-loops and list comprehensions, calculate the sum of squares of all odd numbers.
# Measure the runtime difference with the time module.
# Output
# Print the original list and each transformed list clearly labeled.

import random
import time

# Generate Data
numbers = [random.randint(1, 200) for _ in range(30)]
print("Original numbers:", numbers)

# Transformations (using list comprehensions only)
cubes = [n**3 for n in numbers]
print("Cubes:", cubes)

divisible_by_5 = [n for n in numbers if n % 5 == 0]
print("Numbers divisible by 5:", divisible_by_5)

strings = ['num_' + str(n) for n in numbers]
print("Numbers as strings:", strings)

# Comparison
start = time.time()
squares_odd_comp = sum(n ** 2 for n in numbers if n % 2 != 0)
end = time.time()
print(f"Sum of squares (comprehension): {squares_odd_comp}")
print("Comprehension time:", round(end - start, 6), "seconds")

start = time.time()
squares_odd_loop = 0
for n in numbers:
    if n % 2 != 0:
        squares_odd_loop += n ** 2
end = time.time()
print(f"Sum of squares (loop): {squares_odd_loop}")
print("Loop time:", round(end - start, 6), "seconds")
