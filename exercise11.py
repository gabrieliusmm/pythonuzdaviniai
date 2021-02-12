# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.

repeat_prime = True


def check_for_prime(user_number):
    if (user_number % 2 == 1) or (user_number == 2):
        print(f"The number {user_number} is prime")
    else:
        print(f"The number {user_number} isn't prime")

while repeat_prime == True:
    user_input = int(input("Type a number: "))
    check_for_prime(user_input)
    repeat_input = input("Do you want to try another number?(y/n): ")
    if repeat_input == "n":
        repeat_prime = False
        print("Thank you for trying!")