import random

print("You get 5 tries")

def number_guess():
    tries = 0
    number = random.randint(0, 100)
    while tries < 5:
        try:
            guess_str = input("\nType a number: ")
            if guess_str.lower() in ["exit", "quit"]:
                break
            guess = int(guess_str)
            if guess == number:
                print("\nNice, You Won!!")
                break
            elif guess < number:
                print("\nWrong! Higher")
                tries += 1
            elif guess > number:
                print("\nWrong! Try Lower")
                tries += 1
        except ValueError:
            print("\nMust Type A Number!!\nTo quit Type exit or quit")


number_guess()