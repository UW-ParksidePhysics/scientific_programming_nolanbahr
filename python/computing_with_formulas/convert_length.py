# distance from campus to home 
distance_from_campus_km = 37

# conversion values
cm_per_inch = 2.54
inches_per_foot = 12
feet_per_yard = 3
yards_per_mile = 1760
meters_per_km = 1000
cm_per_meter = 100

# convert kilometers to centimeters
distance_cm = distance_from_campus_km * meters_per_km * cm_per_meter

# convert centimeters to inches
distance_inches = distance_cm / cm_per_inch

# convert inches to feet
distance_feet = distance_inches / inches_per_foot

# convert feet to yards
distance_yards = distance_feet / feet_per_yard

# convert yards to miles
distance_miles = distance_yards / yards_per_mile

print("Distance from campus:")
print("Kilometers:", distance_from_campus_km)
print("Inches:", distance_inches)
print("Feet:", distance_feet)
print("Yards:", distance_yards)
print("Miles:", distance_miles)
