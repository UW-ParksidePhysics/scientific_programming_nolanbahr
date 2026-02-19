# incorrect code from the problem
# summation = 0
# starting_index = 1
# index = starting_index
# maximum_index = 100
#
# while index < maximum_index:
#     summation += 1/index
#
# print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')

# Errors:
# 1) index is never increased inside the while loop (infinite loop)
# 2) while condition should include maximum_index
# 3) summation should be a float


# Correct code

summation = 0.0
starting_index = 1
index = starting_index
maximum_index = 100

while index <= maximum_index:
    summation = summation + 1 / index
    index = index + 1

print("kmax =", maximum_index)
print("sum =", summation)


# kmax = 3

summation = 0.0
index = 1
maximum_index = 3

while index <= maximum_index:
    summation = summation + 1 / index
    index = index + 1

print("kmax =", maximum_index)
print("sum =", summation)
