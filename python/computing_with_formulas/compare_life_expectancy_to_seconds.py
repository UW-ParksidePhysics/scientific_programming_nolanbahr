# CDC life expectancy value (in years)
cdc_life_expectancy_years = 77

# time conversion values
days_per_year = 365
hours_per_day = 24
minutes_per_hour = 60
seconds_per_minute = 60

# total seconds in one year
seconds_per_year = days_per_year * hours_per_day * minutes_per_hour * seconds_per_minute

# total seconds a newborn is expected to live
expected_lifetime_seconds = cdc_life_expectancy_years * seconds_per_year

# one billion seconds
one_billion_seconds = 1_000_000_000

print("CDC life expectancy (years):", cdc_life_expectancy_years)
print("Expected lifetime (seconds):", expected_lifetime_seconds)

if expected_lifetime_seconds > one_billion_seconds:
    print("Conclusion: A newborn CAN expect to live one billion seconds.")
else:
    print("Conclusion: A newborn CANNOT expect to live one billion seconds.")
