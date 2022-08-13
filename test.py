calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    condition_check = num_of_days > 0
    print(type(condition_check))

    if num_of_days > 0:
        return(f"{num_of_days} days are  {num_of_days * calculation_to_units} {name_of_unit}")
    elif num_of_days == 0:
        return "you entered a number that is 0 days, no conversion value"
    else:
        return "you entered a negative value, no conversion value"

user_input = input("Hey user, enter a number of days and i will convert it to hours!\n")
user_input_number = int(user_input)

calculated_value = days_to_units(int(user_input))
print(calculated_value) #aug 13



