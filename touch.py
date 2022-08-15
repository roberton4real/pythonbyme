# to avoid repeating the same line of use variables 

calculation_to_units = 24 
name_of_unit = "Hours"
print(f"20 days are  {20 * 24 * 60}  minutes")
print(f"20 days are  {21 * 24 * 60}  minutes")
print(f"20 days are  {22 * 24 * 60}  minutes")
print(f"20 days are  {23 * 24 * 60}  minutes") 

# now this can be written as 

print(f"20 days are  {20 * calculation_to_units}  {name_of_unit}")

# using functions




