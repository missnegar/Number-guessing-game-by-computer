import random

def computer_guess_number():
    low = 1
    high = 99
    guess = random.randint(low, high)
    while True:
        print("Is the number", guess, "? (k=smaller, b=bigger, d=correct)")
        user_input = input()
        if user_input == "k":
            high = guess - 1
            guess = random.randint(low, high)
        elif user_input == "b":
            low = guess + 1
            guess = random.randint(low, high)
        elif user_input == "d":
            print("YESSSS CORRECT.")
            break
        else:
            print("Invalid input. Please enter k, b, or d.")

computer_guess_number()