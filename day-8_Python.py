import math

# Today's lesson is about Functions with Inputs, Arguments and Parametres

# Create a function called greet() and
# Write 3 print statements inside the function
# Call the greet() function and run your code

# def greet():
#     for _ in range(3):   # Loop to print "hello buddy" three times in a row using range() built-in function
#         print("Hello body")
#
# greet()

# def greet():
#     print("Heelo")
#     print("How do you do?")
#     print("Isn't the weather nice today?")
#
# greet()


# Fucntion with Inputs
# we add some variables inside the brakets when it comes to getting some values

# def greet_with_name(name):   # we enter the name parameter
#     print(f"Hello, {name}")
#     print(f"How do you do {name}")
# greet_with_name("Murodjon")   # insidenside here argument (value of parametre)
# name here is called Parameter and Murodjon is here called Argument.
# Parameter is the name of the date we passed in, and the Argument is the actual value of the data

# Functions with more than 1 input

# def greet_with(name, location):   # Parameters are name and lcoation
#     print(f"Hello, {name}")
#     print(f"What is it like in {location}")
#
#
# greet_with(
#     "Murodjon", "Melbroune"      # Positional Arguments (default way of calling function) : Murodjon and Melbroune
# )
#
# # Functions with keyword arguments
#
# greet_with(location="London", name="Murodjon")


# Paint Can challenge

# test_h = int(input("height of wall: "))
# test_w = int(input("Width of wall: "))
#
# coverage = 5
#
#
# def paint_calc(height, width, cover):
#     number_of_cans = math.ceil((test_h * test_w) / coverage)   # math.ceil() is a function that is used to return the smallest integer greater than or equal to a given number. Essentially, it rounds a number up to the nearest integer.
#     # such as math.ceil(4.2)  =>  Output: 5  if it is negative number, for example -2.3, the result is -2
#     print(f"You'll need {number_of_cans} cans of paint")    # or you may use round() is here
#
#
# paint_calc(height=test_h, width=test_w, cover=coverage)

# Prime Number Checker
# n = int(input("Prime number checker, enter any number: "))



 def prime_checker(number):
     is_prime = True
     for i in range(2, number -1):
         if number % i == 0:  # int(math.sqrt(number)) + 1
             is_prime = False
     if is_prime:
         print("It's a prime number.")
     else:
         print("It's not a prime number.")
prime_checker(number=n)


# or There are some suggestions given by ChatGPT:

def prime_checker(number):
    if number <= 1:
        print("It is not a prime number.")
        return
    is_prime = True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            break # Exit the loop early if a divisor is found
    if is_prime:
        print("It is a prime number.")
    else:
        print("It is not a prime number.")

n = int(input("Prime number checker, enter any number: "))
prime_checker(number=n)