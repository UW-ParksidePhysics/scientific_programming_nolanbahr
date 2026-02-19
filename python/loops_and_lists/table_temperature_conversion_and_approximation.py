print("F C C_approx")
F = 0
while F <= 100:
    C = (F - 32) * 5 / 9
    C_approx = (F - 30) / 2
    print(F, C, C_approx)
    F = F + 10