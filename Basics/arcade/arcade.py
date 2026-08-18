
import sys
from rps import rps
from guessnumber import guess


def play_arcade(name):
    welcomeback=False
    print("Welcome to the arcade!!!!\n")
    while True:
        if welcomeback==True:
            print(f"Welcome back to the arcade {name}")

        
        playerchoice=int(input("Which game would you like to play: \n1.Rock Paper Scissors \n2.Guess Number \n3.Exit\n"))
        
        if playerchoice not in [1,2,3]:
            print("Invalid Choice")
            continue

        welcomeback=True
        
        if playerchoice==1:
            rockpaper=rps(name)
            rockpaper()
        elif playerchoice==2:
            guess_number=guess(name)
            guess_number()
    
        else:
            print(f"Thanks for playing {name}!!!")
            sys.exit()

if __name__=="__main__":
    import argparse

    parser=argparse.ArgumentParser(
        description="Provides a detailed user expericence"
    )

    parser.add_argument(
        '-n','--name',metavar='name',
        required=False,
        default='PlayerOne'
    )

    args=parser.parse_args()
    arcade=play_arcade(args.name)
    arcade()
