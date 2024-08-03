#Task-04 : this task is about creating a responsive stone-paper-sissor game.

#it is a user responsive program i.e it will generate random outputs with correspondence to the inputs by the user.

# the rules of the game are same as of the classic one :
#     1. scissor beats paper
#     2. paper beats rock
#     3. rock beats scissor

# the user have to press :
#     "s" for stone i.e 1
#     "p" for paper i.e -1
#     "c" for scissor i.e 0

#update in structure of code----> the main body of code is written in a function thich will run in a conditional loop (depending upon the choine of user to play it again or not)

import random
    
def Play_game():
    computer = random.choice([-1,0,1])
    print("please press :\ns for stone\np for paper\nc for scissor")


    option=(input("Enter your choice please :\n"))
    dict={"s":1,"p":-1,"c":0}
    inp=dict[option]
    ReverseDict={1:"stone",-1:"paper",0:"scissor"}


    print(f"you choose :{ReverseDict[inp]}\ncomputer choose :{ReverseDict[computer]}\n")



#writing the mai body of code- the decision operators of the game 
    if(computer==inp):
       print("IT'S A DRAW !!!")
    elif(computer==-1 and inp==0):
       print("YOU WIN !!!\nCONGRATS !")
    elif(computer==-1 and inp==1):
       print("YOU ARE DEFEATED !\n DON'T LET THIS HAPPEN AGAIN")
    elif(computer==1 and inp==0):
       print("YOU ARE DEFEATED !\n DON'T LET THIS HAPPEN AGAIN")
    elif(computer==1 and inp==-1):
       print("YOU WIN !!!\nCONGRATS !")
    elif(computer==0 and inp==-1):
       print("YOU WIN !!!\nCONGRATS !")
    elif(computer==0 and inp==1):
       print("YOU ARE DEFEATED !\n DON'T LET THIS HAPPEN AGAIN")
    else:
       print("invalid input !!!!")
    
    
def main():
    while True :
        Play_game()
        end=(input("Do you want to play game again\npress 'y' to play :\n and 'n' to exit the game :"))
        if end!='y':
            print("thankyou for playing boss\nsee you soon")
            break;

if __name__ == "__main__":
    main()




