import sys
import random
from enum import Enum
game_count=0

def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    
    print("")
    playerchoice = input(
        "Enter...\n1. for Rock,\n2. for Paper, or \n3. for Scissors \n4. Exit:\n\n")

    if playerchoice not in ["1","2","3","4"]:
        print("You must enter 1, 2,3 or 4.")
        return play_rps()

    player = int(playerchoice)
    

    
    if player == 4:
        print("Thanks for playing.!!!")
        exit()

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("")
    print("You chose " + playerchoice + ".")
    print("Python chose " + computerchoice + ".")
    print("")

    def decide_winner(player,computer):
        if player == 1 and computer == 3:
            return" You win!"
        elif player == 2 and computer == 1:
            return" You win!"
        elif player == 3 and computer == 2:
            return" You win!"
        elif player == computer:
            return" Tie game!"
        else:
            return" Python wins!"

    game_result= decide_winner(player,computer)
    print(game_result)
    

    global game_count
    game_count+=1
    print("\n Game count: " + str(game_count))

    while True:
        
        playagain= input("Do you want to play again(y/n): ")
        if playagain.lower() not in ["y","n"]:
            print("Please select (y/n)!!")
            continue
        else:
            break

    if playagain.lower()=="y":
        return play_rps()
    else:
        print()
        print("Thanks for playing!!!!")
        exit()

play_rps()