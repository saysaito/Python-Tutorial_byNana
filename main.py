calcutation_to_units=24
nama_of_unit="hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days*calcutation_to_units} {nama_of_unit}"

user_input=input("Hey user, enter a number of days and I will convert it to hours!\n")
user_input_number=int(user_input)
my_var=days_to_units(user_input_number)
print(my_var)






