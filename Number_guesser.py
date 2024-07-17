import random


def letsguess():
    tot_guess=0
    while True:
        tot_guess+=1
        user_guess=input("Make a Guess: ")

        if user_guess.isdigit:
            user_guess=int(user_guess)

        else:
            print("Please enter a number!!!")
            continue

        if user_guess==random_num :
            print("You've got it!!!")
            break
        elif user_guess<random_num:
            print('your guess is lower than the number')
        else:
            print('your guess is greater than the number')

    print("you've got it in",tot_guess,"guesses")


top_range=input("Type a Number: ")

if top_range.isdigit():
    top_range=int(top_range)
    if top_range <= 0:
        print("Please Enter a number greater than Zero!!!")
        quit()

else:
    print("Enter a Number Next Time!!!")
    quit()
random_num=random.randint(0,top_range)

letsguess()