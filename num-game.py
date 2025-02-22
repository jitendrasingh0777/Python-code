import random

loewst_num = 1
Highest_num = 100
answer = random.randint(loewst_num,Highest_num)
guesses = 0
is_running = True

print("-------Welcome To The Game ----------")
print(f"Guess a number between {loewst_num} to {Highest_num}")

while is_running:
    guess = input("Enter Your Guess")

    if guess.isdigit():
        guess = int(guess)
        guesses +=1


        if guess < loewst_num or guess > Highest_num:
            print("This number is out of the range")
            print(f"Guess a number between {loewst_num} to {Highest_num}")
        elif guess < answer :
            print("To low!!Try again!!")
        elif guess> answer :
            print("Too high!! Try Again")
        else : 
            print(f"Correct! The answer was {answer}")
            print(f"Number of guesses : {guesses}")
            is_running = False



    else :
        print("invalid Guess")
        print(f"Guess a number between {loewst_num} to {Highest_num}")

