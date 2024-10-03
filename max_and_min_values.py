# The code the will first present a banner
# Then this code will a create list 
# After that it wil print out the Max 
# and the min within the list

# Define my banner variables
player= "SAKA"
my_random_var0 = "#" * 49
my_random_var1= "WELCOME LETS GET MAX & MIN: {}".format(player)
my_random_var2= "#"

# This code below allow to create Banner in python
print(my_random_var0 + "\n" + my_random_var2 +"\t\t\t\t\t\t"+ my_random_var2 +  "\n\t" + "\n" + my_random_var2 + "  "+ my_random_var1 + "  " + "\t\t" + my_random_var2 + "  " + "\n\n" + my_random_var2 + "\t\t\t\t\t\t"+ my_random_var2 + "\n\n" + my_random_var0)

# Define my variale name my_number_list  with integer numbers
my_numbers_list = [10, 20, 30, 40, 50, 60]

# Printing all of my number with the list
print(f"These are the integer numbers within my list : {my_numbers_list}")

# Print out the Max and Min within my list without f-string
print( my_numbers_list[5], my_numbers_list[0]) 

# Printing out the Max and Min within my list using f-string
print(f"These are the Max & Min within my list : {my_numbers_list[5]} {my_numbers_list[0]} ")




