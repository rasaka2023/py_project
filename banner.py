figther= "SAKA"
my_random_var0 = "#" * 49
my_random_var1= "WELCOME TO STREET FIGHTER: {}".format(figther)
my_random_var2= "#"


# Option#1: This code below allow to create Banner in python
print(my_random_var0 + "\n" + my_random_var2 +"\t\t\t\t\t\t"+ my_random_var2 +  "\n\t" + "\n" + my_random_var2 + "  "+ my_random_var1 + "  " + "\t\t" + my_random_var2 + "  " + "\n\n" + my_random_var2 + "\t\t\t\t\t\t"+ my_random_var2 + "\n\n" + my_random_var0)

# Option#2: This code below works perfectly and it does not leverage the the format() function, it used my_random_var1
#print(my_random_var0 + "\n" + my_random_var2 +"\t\t\t\t\t\t"+ my_random_var2 +  "\n\t" + "\n" + my_random_var2 + "  "+ my_random_var1 + "fighter" + "  " + "\t" + my_random_var2 + "  " + "\n\n" + my_random_var2 + "\t\t\t\t\t\t"+ my_random_var2 + "\n\n" + my_random_var0)

# Option#3: This code below allow to create Banner in python
#print(my_random_var0 + "\n" + my_random_var2 +"\t\t\t\t\t\t"+ my_random_var2 +  "\n\t" + "\n" + my_random_var2 + "  "+ " WELCOME TO STREET FIGHTER: {}".format(figther) + "  " + "\t\t" + my_random_var2 + "  " + "\n\n" + my_random_var2 + "\t\t\t\t\t\t"+ my_random_var2 + "\n\n" + my_random_var0)



