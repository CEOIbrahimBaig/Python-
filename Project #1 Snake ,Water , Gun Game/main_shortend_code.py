"""
1 for snake 
-1 for water 
0 for gun 
"""
import random

computer = random.choice([-1,0,1])

you = input("\tEnter your choice:  ")

you_dict = {
    "s": 1,
    "w": -1,
    "g": 0
}

younum = you_dict[you]

reverse_dict={
    1:"Snake",
    -1:"water",
    0:"Gun"
}

print ("\tYou selected ",reverse_dict[younum])
print("\t Computer Selected",reverse_dict[computer])



if (computer == younum):
    print("It is a draw")

''''
else:
    if (computer == -1 and younum == 1):
        print("You win !!!")
    elif (computer == -1 and younum == 0):
        print("You lose !!")
    elif (computer == 1 and younum == -1):
        print("You lose !!")
    elif (computer == 1 and younum == 0):
        print("You win !!")
    elif (computer == 0 and younum == -1):
        print("You lose !")
    elif (computer == 0 and younum == 1):
        print("You win !!")
    else:
        print("Print something went wrong")
'''

if (computer-younum)==-1 or (computer -younum):
    print ("You lose !")
else:
    print("You Win")