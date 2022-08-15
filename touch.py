# to avoid repeating the same line of use variables 

calculation_to_units = 24 
name_of_unit = "Hours"
print(f"20 days are  {20 * 24 * 60}  minutes")
print(f"20 days are  {21 * 24 * 60}  minutes")
print(f"20 days are  {22 * 24 * 60}  minutes")
print(f"20 days are  {23 * 24 * 60}  minutes") 

# now this can be written as 

print(f"20 days are  {20 * calculation_to_units}  {name_of_unit}")

# using functions - block of code 
# that does something more complex used to avoid repeating the same logic in you code 

def days_to_units(num_of_days): #this line defines a function
    # num_of_days is a variable in my def it's called a parameter 
    print(f"20 days are  {20 * calculation_to_units}  {name_of_unit}")
    print("All Good")

days_to_units(35) #this is needed to execute my functions
days_to_units(45)
days_to_units(350)
days_to_units(3125)