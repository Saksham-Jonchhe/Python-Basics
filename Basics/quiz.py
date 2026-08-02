#quiz game

questions=(("How many elements are in the periodic table?:"),
            ("Which animal lays the largest eggs?"),
            ("What is the most abundant gas in earth's atmosphere"),
            ("How many bones are there in the human body?:"),
           ( "Which planet in the solar system is the hottest?:"))
options=(("A.116","B.117","c.118"),
         ("A.Whale","B.Crocodile","C:Elephant","D.OStrich"),
         ("A.Nitrogen","B.oxygen","C.Carbon Dioxide","D.Hydrogen"),
         ("A.206","B.207","C.208","D.209"),
         ("A.Mercury","B.Venus","C.Earth","D. Mars"))

answers=("C","D","A","A","B")
guesses=[]
score=0
question_num=0

for question in questions:
    print("------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess=input("Enter (A,B,C,D):").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print(f"CORRECT!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer!")

    question_num+=1
print()
print("---------------------------RESULTS------------------")

print("Guesses:")
for guess in guesses:
    print(guess,end=" ")
print()

print("Answers:")
for answer in answers:
    print(answer,end=" ")
print()
print()


print(f"Final Score:{score}")