import os

l = [0,1,2,3,4,5,6,7,8]
win = ""
rep = {0:False,1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False}

def frame():
    global l

    for i in range(0,len(l)):
        if isinstance(l[i] , int):
            l[i] = " "
        
    print("\n\n",
        f"{l[0]}  |  {l[1]}  |  {l[2]}\n",
        "--------------\n",
        f"{l[3]}  |  {l[4]}  |  {l[5]}\n",
        "--------------\n",
        f"{l[6]}  |  {l[7]}  |  {l[8]}\n",
        "--------------\n")
    
    for i in range(0,len(l)):
        if l[i] == " ":
            l[i] = i

def update(index,data):  # for update the initial value
    global rep,l
    if rep[index] == True:
        print("What are you trying to do ! This is not how the Game played.")
        index = int(input("Enter again :"))
    
    for i in range(0,len(l)):
        if l[i] == index:
            l[i] = data
            rep[i] = True
        
def logic(user):
    if user == "X":
        win = "USER 1 wins"
    else:
        win = "USER 2 wins"

    if l[0] == l[1] == l[2]:
        print(f"game over and winner is {win}")
        return False
    elif l[0] == l[3] == l[6]:
        print(f"game over and winner is {win}")
        return False
    elif l[0] == l[4] == l[8]:
        print(f"game over and winner is {win}")
        return False
    elif l[1] == l[4] == l[7]:
        print(f"game over and winner is {win}")
        return False
    elif l[2] == l[5] == l[8]:
        print(f"game over and winner is {win}")
        return False
    elif l[2] == l[4] == l[6]:
        print(f"game over and winner is {win}")
        return False
    elif l[3] == l[4] == l[5]:
        print(f"game over and winner is {win}")
        return False
    elif l[6] == l[7] == l[8]:
        print(f"game over and winner is {win}")
        return False
        

print("NOTE: for insterting the upper-left,upper-mid,upper-right,middle-left,middle-mid,middle-right,lower-left,lower-mid,lower-right instert the num 0-9 respectively...........")  
while True:
    
    frame()
    user = "X"
    user_loc = int(input("[USER 1] specifiy the location of your choice :"))
    update(user_loc,user)
    status = logic(user)
    if status == False:
        os.system('cls')
        frame()
        break
    os.system('cls')

    frame()
    user2 = "O"
    user2_loc = int(input("[USER 2] specifiy the location of your choice :"))
    update(user2_loc,user2)
    os.system('cls')
    status2 = logic(user2)
    if status2 == False:
        frame()
        break