import random
numbers = [random.randint(1, 100) for _ in range(20)]
print(numbers)
squared = [n**2 for n in numbers]
print("Squared:",squared)
even = [n for n in numbers if  n % 2 == 0]
print("Even numbers:",even)
string = [str(n) for n in numbers]
print("Strings:",string)

#Comparison: List Comprehension vs For Loop (30 min)
# Timing with list comprehension
import time
start = time.time()
squares_comp = [n**2 for n in numbers]
end = time.time()
print("Comprehension time:", end - start)
#timing with for loop
start = time.time()
squares_loop = []
for n in numbers:
    squares_loop.append(n**2)
end = time.time()
print("For Loop time:", end - start)
