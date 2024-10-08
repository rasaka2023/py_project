# This code will display translaotor banner
#  It will create an english to french dictionary
# It will prompt user to enter a key word in english
# Then it will help translating the english word into french
# If the word exist within the dictionary it will let tyhe user know

# Allow to print the dictionary banner
player= "RASAKA"
my_random_var0 = "%" * 49
my_random_var1= "WELCOME2 TRANSLATOR CODING:{}".format(player)
my_random_var2= "%"
# This code below allow to create Banner in python
print(my_random_var0 + "\n" + my_random_var2 +"\t\t\t\t\t\t"+ my_random_var2 +  "\n\t" + "\n" + my_random_var2 + "  "+ my_random_var1 + "  " + "\t\t" + my_random_var2 + "  " + "\n\n" + my_random_var2 + "\t\t\t\t\t\t"+ my_random_var2 + "\n\n" + my_random_var0)
# Create english to french dictionary
english_french_dic= {"Dog":"Chien",
                    "Cat":"Chat",
                    "Soccer":"Football", 
                    "Love":"Aimer","Add":"Ajouter",
                    "Prune":"Delete"}

# Prompt the user to enter a word which will be a string
user_word= str(input(f" Please enter your desired word: "))

# Print out english to french dictionary 
print (english_french_dic)

# Prompt User to enter their word
print(f"You have entered: {user_word}")
# Defining or translating the user word
translator = english_french_dic.get(user_word)
# Printing out the translator of the word that user entered
print(f"The translator of your selected word is: {translator}")
if user_word in english_french_dic :
    print(f"{translator} is in my memory")
else: 
    print(f"{translator} is not in my memory")   


