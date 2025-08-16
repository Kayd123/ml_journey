# for loop → used when you know the range or are iterating over a collection.
# while loop → used when you loop until a certain condition is met.
# for loop

for i in range(5):
    print(i)
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)
squares = [x**2 for x in range(10)]
print(squares)
for i in range(5):
    print(i)  # 0 1 2 3 4
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
# for idx, value in enumerate(dataset):
#    print(idx, value)
# While Loops
count = 0
while count < 5:
    print(count)
    count += 1
    # condition
loss = 1.0
while loss > 0.05:
    loss *= 0.9
    print(loss)
# ⚠ Tip: Always update variables inside while loops to avoid infinite loops.
# Conditions
accuracy = float(input("Enter your accuracy: "))
if accuracy > 0.9:
    print("High accuracy")
elif accuracy > 0.8:
    print("Moderate accuracy")
else:
    print("Needs improvement")
