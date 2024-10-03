# The code below will first display the banner fro weight convertor
# Then it will prompt users to entered their weight in lbs
# After that, the weight will then convert it to from into Kgs

username= "SAKA"
my_random_var0 = "#" * 49
my_random_var1= "WELCOME TO WEIGHT CONVERTOR: {}".format(username)
my_random_var2= "#"

print(my_random_var0 + "\n" + my_random_var2 +"\t\t\t\t\t\t"+ my_random_var2 +  "\n\t" + "\n" + my_random_var2 + "  "+ my_random_var1 + "  " + "\t\t" + my_random_var2 + "  " + "\n\n" + my_random_var2 + "\t\t\t\t\t\t"+ my_random_var2 + "\n\n" + my_random_var0)
# Conversion factor: 1 pound = 0.453592 kilograms
body_weight_pounds = float(input("Please enter your body weight in pounds: "))
kilograms = body_weight_pounds * 0.453592
# Print the result with formatted string
print(f"Your body weight is: {body_weight_pounds} pounds and the equivalent weight in kgs is {kilograms:.3f} kgs! Thank you.")

