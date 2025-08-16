# Write a program to print numbers 1–20, label odd/even.
for x in range(1, 21):
    if x % 2 == 0:
        print(f"{x} + is even")
    else:
        print(f"{x} + is odd")
