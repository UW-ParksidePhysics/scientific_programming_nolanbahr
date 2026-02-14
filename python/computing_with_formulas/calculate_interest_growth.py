# initial amount of money
initial_amount = 1000

# interest rate (percent per year, example value)
interest_rate_percent = 5

# number of years
number_of_years = 3


# compute growth using A = A0 * (1 + p/100)^n
growth_amount = initial_amount * (1 + interest_rate_percent / 100) ** number_of_years


print("Initial amount:", initial_amount)
print("Interest rate (percent per year):", interest_rate_percent)
print("Number of years:", number_of_years)
print("Amount after growth:", growth_amount)
