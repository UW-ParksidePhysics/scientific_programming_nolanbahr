a = 1.0
b = 2.0
n = 20

h = (b - a) / n
x = [a + i * h for i in range(n + 1)]

print("Using list comprehension:")
print(x)