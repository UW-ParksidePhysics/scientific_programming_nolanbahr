n = 10
sum_loop = 0
for i in range(1, n + 1):
    sum_loop = sum_loop + i
sum_formula = n * (n + 1) / 2
print("n =", n)
print("sum using for loop =", sum_loop)
print("sum using formula", sum_formula)