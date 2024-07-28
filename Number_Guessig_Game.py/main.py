import random
EASY_LEVEL_ATTEMS=10
HARD_LEVEL_ATTEMS=5
def set_difficulty(level):
    if level=="Easy":
        return EASY_LEVEL_ATTEMS
    else:
        return HARD_LEVEL_ATTEMS

def check_answer(guessed_number,answer,Attems):
    if guessed_number<answer:
        print("Your guess is too low")
        return Attems-1
    elif guessed_number>answer:
        print("your guess is too high")
        return Attems-1
    else:
        print(f"yours guess is right...the answer was{answer}")


def game():
    print("Let me think of a number beteween 1 to 100.")
    answer=random.randint(1,100)
    level=input("Choose level of difficulty-type: Easy or Hard : ")
    Attems=set_difficulty(level)
    guessed_number=0
    while guessed_number != answer:
        print((F"you have {Attems} remaining chances to guess the number"))
        guessed_number=int(input("Guess a number: "))
        Attems=check_answer(guessed_number,answer,Attems)
        if Attems==0:
            print("You are out of guess......you lose!")
            return
        elif guessed_number!=answer:
            print("Guess again..")

game()
