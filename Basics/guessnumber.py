import random
import sys



def guess(name='PLayerOne'):
    playerwin=0
    computerwin=0
    gamecount=0    

    def guessnumber():
            nonlocal gamecount
            nonlocal name
            nonlocal playerwin
            nonlocal computerwin

            print("")
            playernumber=int(input("Hi!! Please enter a number:"))
            if playernumber<1 or playernumber>3:
                print("Please select between 1,2 and 3")
                return guessnumber()
            
            computernumber=random.choice([1,2,3])
            print(f"Your number is  {playernumber}")
            print(f"I guessed {computernumber}")

            player= int(playernumber)
            computer=int(computernumber)


            def decide_winner(player,computer):
                nonlocal name
                nonlocal playerwin
                nonlocal computerwin
                if player==computer:
                    computerwin+=1
                    print(f"Sorry {name} !!! BEtter luck next time")
                    
                else:
                    playerwin+=1
                    print(f"You win!!!")

            decide_winner(player,computer)

            gamecount+=1

            print(f"{name} win:{playerwin}")
            print(f"Computer Win:{computerwin}")
            print(f"Game count:{gamecount}")
            print(f"Your winning percentage:{playerwin/gamecount:.2%}")


            print("\n")
            while True:

                playerchoice=input("Do you want to play again?(y/n)")
                if playerchoice.lower() not in ["y","n"]:
                    continue
                else:
                    break

            if playerchoice.lower() == "y":
                return guessnumber()
            else:
                print("thanks for playing!!")
                if __name__ == "__main__":
                    sys.exit(f"Bye!!{name}")
                else:
                    return
                
    return guessnumber

if __name__ == "__main__":
    import argparse
    parser=argparse.ArgumentParser(
        description='provides a personalized  game experience.'
    )
    parser.add_argument(
        '-n','--name',metavar='name',
        required=False,help='The name of the person playing'
    )

    args=parser.parse_args()

    guess_my_number=guess(args.name)
    guess_my_number()
    



