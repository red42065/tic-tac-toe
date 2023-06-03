import random
user= 0
computer = 0
l = ["rock", "paper", "scissors"]
winningquotes = ["Winning is my habit. Unfortunately, so is your losing", "The person that said winning isn't everything never won anything","The critics are always right. The only way you shut them up is by winning.","Winning solves everything." ]
afterscores = ["The harder the battle the sweeter the victory.","gg bro","It's never just a game when you're winning." ]
losingquotes = ["Congratulations!","Well done!","You did it!","Great job!"," You should be proud of yourself!"]
exit= False

def showscore():
    return f"scores:\nuser:{user}\ncomputer:{computer}"

def computer_choice_display():
    return f"computer choice: {comp_choice}"

while exit == False:
    
    comp_choice = random.choice(l)
    user_choice = input("enter rock or paper or scissors or exit or display score \n")
    
    if user_choice == "score":
        print(showscore())
        
    
    if user_choice == "rock":
        if comp_choice=="paper":
            print("computer wins")
            print(computer_choice_display())
            print()
            computer +=1
        elif comp_choice=="scissors":
            print("you win")
            print(computer_choice_display())
            print()
            user +=1
        elif comp_choice == "rock":
            print("Tie")
            print(computer_choice_display())
            print()
   
    if user_choice == "paper":
        if comp_choice=="paper":
            print("Tie")
            print(computer_choice_display())
            print()
        elif comp_choice=="scissors":
            print("computer wins")
            print(computer_choice_display())
            print()
            computer +=1  
        elif comp_choice == "rock":
            print("you win")
            print(computer_choice_display())
            print()
            user +=1
           
    if user_choice == "scissors":
        if comp_choice=="paper":
            print("you win")
            print(computer_choice_display())
            print()
            user +=1
        elif comp_choice=="scissors":
            print("Tie")
            print(computer_choice_display())
            print()
        elif comp_choice == "rock":
            print("computer wins")
            print(computer_choice_display())
            print()
            computer +=1
    
    if user_choice=="exit":
        exit = True


if user < computer:
    print(random.choice(winningquotes))
    print(random.choice(afterscores))
elif user > computer:
    print(random.choice(losingquotes))
    print(random.choice(afterscores))
elif user == computer ==0:
    print("play broo")
else:
    print("broo its a tie")
print(showscore())