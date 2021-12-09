# Ryan Lugo: RJL 12/9/21

from random import randint as rand

def guessing_game():
    """It's a guessing game"""
    guessed_correctly = False
    rand_number = str(rand(0,50))

    while not guessed_correctly:
        plr_input = input("Enter what number you think the computer generated: ")
        
        if plr_input.lower() == "stop":
            print("The number was:",rand_number)
            break
        elif plr_input > rand_number:
            print("You need to guess a lower number!")
        elif plr_input < rand_number:
            print("You need to guess a higher number!")
        elif plr_input == rand_number:
            break

    
guessing_game()