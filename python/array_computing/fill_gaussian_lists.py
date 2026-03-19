import math

def gaussian(x):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-x**2 / 2)

x_values = []
g_values = []

start = -4
end = 4
n = 41

step = (end - start) / (n - 1)

for i in range(n):
    x = start + i * step
    g = gaussian(x)
    
    x_values.append(x)
    g_values.append(g)

print(x_values)
print(g_values)