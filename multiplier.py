"""
This function will allow to Multiplies two even numbers.

Parameters or Arguments:
x (int): The first even number to be multiplied.
y (int): The second even number to be multiplied.

Returns:
int: The product of the two even numbers.

"""
def multiply_even_numbers(x, y):
    product = x*y
    return product

number_list =[8, 9, 11, 20, 32, 101, 100]

# Get user input and add exception handling
try:
    # Define variable user_even_num1 and user_even_num2
    user_num1 = int(input("Welcome to CloudSpace, Please enter your first even number: "))
    user_num2 = int(input("Welcome to CloudSpace, Please enter your second even number: "))

    # Check if the numbers are even and in the list
    if user_num1 not in number_list or user_num2 not in number_list:
        raise ValueError(" Your input number should be from the predefined number_list.Place try again")
    if user_num1 % 2 != 0 or user_num2 % 2 != 0:
        raise ValueError("Your input number should an even number. Please try again")

    # Define variable name product_result, which will provide result from the product
    product_result = multiply_even_numbers(user_num1, user_num2)
    print(f"{user_num1} multiplied by {user_num2} is: {product_result}")

except ValueError as e:
    print(f"Input error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

     