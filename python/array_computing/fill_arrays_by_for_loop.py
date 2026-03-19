import math

def g(x):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-x**2 / 2)

x_values = []
y_values = []

start = -4
end = 4
n = 41

step = (end - start) / (n - 1)

for i in range(n):
    x = start + i * step
    y = g(x)
    
    x_values.append(x)
    y_values.append(y)

print(x_values)
print(y_values)