from random import randint

print("Here , this is a game of Guess in which you have to guess a number and u have to take as less repetation as possible to win.\n\n")
target = randint(1,100)

repeat = 0
guess = 0

while guess != -1:
    if repeat == 0:
        guess = int(input("Enter your guess of number between 1 to 100 :"))
    else :
        guess = int(input("Enter your guess of number again :"))

    if guess == target:
        print(f"You have guessed the number {target} in {repeat} attempt !")
        guess = -1
    else:
        if guess < target:
            print("Your guess is too low , try a higher number !\n")
        if guess > target:
            print("Your guess is too high , try a lower number !\n")
    repeat += 1

