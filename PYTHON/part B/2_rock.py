import random

def comp_choice():
    n=random.randint(0,10)
    if n<3 and n>=0:
        print("Comp got Rock\n")
        return 1
    if n<=6 and n>=3:
        print("Comp got Paper\n")
        return 2
    if n<=10 and n>6:
        print("Comp got Scissors\n")
        return 3
def res(u_choice,c_choice):
    if(u_choice==c_choice):
        print("Match Draw")
    if(u_choice==1):
        if(c_choice==2):
            print("You Lost the match\n")
        elif(c_choice==3):
            print("You WON the match\n")
        
    if(u_choice==2):
        if(c_choice==3):
            print("You Lost the match\n")
        elif(c_choice==1):
            print("You WON the match\n")
        
    if(u_choice==3):
        if(c_choice==1):
            print("You Lost the match\n")
        elif(c_choice==2):
            print("You WON the match\n")
while(True):
    print("press 1 to enter the Game")
    print("press 0 to Exit  the Game")
    ch=int(input())

    if(ch==0):
        exit()
    choice = int(input("\n\n\nEnter your choice for \nRock-->1\nPaper-->2\nScissors-->3\n\n\n"))
    print("\n\n")
    res(choice,comp_choice())