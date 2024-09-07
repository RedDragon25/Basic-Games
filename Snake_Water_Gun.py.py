import random

print("Here a rule for this game ! \nYou chose \"g\" for Gun and \"w\" for Water and \"s\" for Snake.")
print("\n\n\t Let's play this Game.")
com_choice = random.choice([1,0,-1])
user_choice = input("Enter your choice : ")

dict = {"s":1 , "w":-1, "g":0}
user_choice = dict[user_choice]
reverseDict = {1:"Snake" , -1:"Water" , 0:"Gun"}
print(f"computer chose {reverseDict[com_choice]} \nYou chose {reverseDict[user_choice]}")

if user_choice == com_choice:
    print("It's a tie!")
else:
    # if user_choice == 1 and com_choice == -1: 2
    #     print("You win!")
    # elif user_choice == 1 and com_choice == 0: 1
    #     print("You Lose!")
    # elif user_choice == -1 and com_choice == 1: -2
    #     print("You Lose!")
    # elif user_choice == -1 and com_choice == 0: -1
    #     print("You win!")
    # elif user_choice == 0 and com_choice == 1: -1
    #     print("You win!")
    # elif user_choice == 0 and com_choice == -1: 1
    #     print("You Lose!")

    if (user_choice - com_choice) == 2 or (user_choice - com_choice) == -1:
        print("You Win !")
    else:
        print("You Lose !")