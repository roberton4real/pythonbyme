calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return(f"{num_of_days} days are  {num_of_days * calculation_to_units} {name_of_unit}")



def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(int(user_input))
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a number that is 0 days, no conversion value")
    else:
        print("your input is not a number. Don't ruin my program")

user_input = input("Hey user, enter a number of days and i will convert it to hours!\n")
validate_and_execute()



