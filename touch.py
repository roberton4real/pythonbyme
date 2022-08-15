# print("20 days are " + str(50 )+ " minutes") # string concatenation combine string using plus sign
# # + str(50 )+ => string concatenation
# # + str(50 )+ => string concatenation
# print(f"20 days are {50} minutes") #way cooler way then using the plus sign
# # to avoid repeating the same line of use variables 

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

def days_to_units(num_of_days, custom_message): #this line defines a function
    # num_of_days is a variable in my def it's called a parameter 
    print(f"{num_of_days} {20 * calculation_to_units}  {name_of_unit}")
    print("custom_message")

days_to_units(35, "All great") #this is needed to execute my functions
days_to_units(45, "Looks great")