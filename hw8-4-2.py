# Ryan Lugo: RJL 12/9/21

from random import randint


def rock_paper_scissors(wins=0,losses=0,ties=0,matches=0): #We set the vars = 0 , so we don't have to call values on start
        """Play rock paper scissors"""
        player = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors: "))
        computer = randint(0, 2)
        looped = False

        # Check if the user or the computer won.
        if not looped:
            if player == computer:
                print("It's a tie!")
                ties += 1
            elif player == 0:
                if computer == 1:
                    losses += 1
                else:
                    print("You win, rock crushes scissors!\n")
                    wins += 1
            elif player == 1:
                if computer == 2:
                    print("You lose, scissors cuts paper.\n")
                    losses += 1
                else:
                    print("You win, paper covers rock!\n")
                    wins += 1
            elif player == 2:
                if computer == 0:
                    print("You lose, rock crushes scissors.\n")
                    losses += 1
                else:
                    print("You win, scissors cuts paper!\n")
                    wins += 1
            elif player >= 3 or player <= -1:
                print("Since you put a number higher than what's given you will start another round!\n")
                rock_paper_scissors()
        
        matches += 1
        messed_up = True

        while messed_up:
            again = input("Do you want to play again?(Y/N): ")
            if again.lower() == "y":
                rock_paper_scissors(wins,losses,ties,matches)
                messed_up = False
            elif again.lower() == "n":
                 print("Here are your wins:",wins,"\nHere are your losses:",losses,"\nHere are your ties:",ties,"\nHere are your matches played:",matches)
                 messed_up = False
            else:
                print("You sure you typed the correct wording for it? (Remember Y or N)")


rock_paper_scissors()
    