
# The code below will print the dictionary banner
# Thenthe code allows to print out a specific lastName of the employees within  the directory

# Code to print the dictionary banner
player= "RASAKA"
my_random_var0 = "%" * 49
my_random_var1= "WELCOME2 DICTIONARY CODING:{}".format(player)
my_random_var2= "%"
# This code below allow to create Banner in python
print(my_random_var0 + "\n" + my_random_var2 +"\t\t\t\t\t\t"+ my_random_var2 +  "\n\t" + "\n" + my_random_var2 + "  "+ my_random_var1 + "  " + "\t\t" + my_random_var2 + "  " + "\n\n" + my_random_var2 + "\t\t\t\t\t\t"+ my_random_var2 + "\n\n" + my_random_var0)
# Important remark in python we look up items in dictonary using the key,
# and we use index for the list to retrieve any item.
#Our dictionary has two lists( employees and owners). 
# employees list has 3 dictionaries and owners list has 2 dictionaries
# Define variable in the dictionary
key1="firstName"
key2="lastName"

# Defing the dictionary
d = {"employees":[{"firstName":"John","lastName":"Doe"},
                 {"firstName": "Anna","lastName":"Smith"},
                 {"firstName": "Peter","lastName":"Jones"}], 
    "owners":[{"firstName": "Jack","lastName":"Petter"},
             {"firstName": "Jessy" ,"lastName":"Petter"}]}

employees= [{"firstName":"John","lastName":"Doe"},
            {"firstName":"Anna","lastName":"Smith"}, 
            {"firstName": "Peter","lastName":"Petter"}]

owners= [{"firstName": "Jack", "lastName":"Petter"},
        {"firstName": "Jessy", "lastName":"Petter"}]
# Print the list of employees
print(f'This is the list of employees: {d["employees"]}\n')
# Print the list of owners
print(f'This is the list of owners,however we dont have any interested to owners at this time: {d["owners"]}\n')
# Printing the lastName of the second employees in the dictionary
print(f'This is the lastName of the second employees in our dictionary : {d["employees"][2-1][key2]}\n')


