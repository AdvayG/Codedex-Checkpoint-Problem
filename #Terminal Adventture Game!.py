#Terminal Adventture Game!

# A Harry-Potter Duel Simulator Based Game!

# You play as Harry Potter duelling other students in Book 5 DA, each action decides whether you win or lose.
# Choose a duel and try to win , if you lose you black out and have to restart 

import random


ophealth =100
phealth = 100
exp = 0
level  = int(input("Select you level 1-5 "))
if level ==1:
    print("Your Opponent: Luna Lovegood- 4th Year Ravenclaw ")
elif level ==2:
    print("Your Opponent:  Ron Weasly- 5th Year Gryffindor ")
elif level ==3:
    print("Your Opponent: Neville Longbottom- 5th Year Gryffindor ") 
elif level ==4:
    print("Your Opponent: Draco Malfoy- 5th Year Slytherin")
elif level ==5:
    print("Your Opponent: Hermione Granger - 5th year Gryffindor")    
else:
    print("Invalid Input")               


#Duel 1
if level ==1:
    ophealth = 75
    while phealth> 0 and ophealth>0:
        action  = int(input("Chose you action 1. Attack 2. Defend 3. Heal "))
        if action ==1:
            print("You send a stinging hex and do 10 damage ")
            ophealth-=10
        elif action ==2:
            print("Luna's whimsical nature distracts you and she catches you with a stunner") 
            phealth-=100
        elif action ==3:
            if phealth == 100:
                print("Maximum Health  ")
            else:
                phealth+=5
                if phealth>100:
                    phealth =100    
        else:
            print("Invalid Input")
    if ophealth <= 0:
        print("You Defeated your opponent")
        print("Exp gained 100 ")
        print("You unlocked the Stunning spell!")       
        exp+=100
    elif phealth<=0:
        print("You blacked out!")    



#Duel 2
if level ==2:
    ophealth =100
    while ophealth> 0 and phealth > 0:
        action = int(input("Choose your action: 1. Attack 2. Defend 3. Heal "))
        if action ==1:
            ophealth-=20
            print("Your stunner partially hits your opponent, doing moderate damage! ")
        elif action ==2:
            phealth -=20
            print("You get nicked with a small cutting curse, doing moderate damage! ")  
        elif action ==3:
            if phealth>100:
                phealth=100
                print("Maximum health! ")
            else:
                phealth+=20
                print("You use a small mending spell to heal a minor amount! ")
                if phealth>100:
                    phealth =100
        else:
            print("Invalid input ") 
    if ophealth <= 0:
        print("You defeated your opponent! ")
        print("You gained 100 exp")
        print("You unlocked the knockback hex! ")
        exp+=100
    elif phealth<=0:
        print("You blacked out!")    




#Duel 3

if level ==3:
    ophealth =125
    while ophealth> 0 and phealth > 0:
        action = int(input("Choose your action: 1. Attack 2. Defend 3. Heal "))
        if action ==1:
            ophealth-=40
            print("You knockback your opponent , doing moderate damage! ")
        elif action ==2:
            phealth -=30
            print("You get hit with a tripping jinx and fall headfirst, doing moderate damage! ")  
        elif action ==3:
            if phealth==100:
                print("Maximum health! ")
            else:
                phealth+=30
                print("You use a healing spell to heal a moderate  amount! ")
                if phealth >100:
                    phealth=100
        else:
            print("Invalid input ") 
    if ophealth <= 0:
        print("You defeated your opponent! ")
        print("You gained 100 exp")
        print("You unlocked the  Killing curse ! ")
        exp+=100
    elif phealth<=0:
        print("You blacked out!")    



#Duel 4

if level ==4:
    ophealth = 200
    while ophealth> 0 and phealth > 0:
        action = int(input("Choose your action: 1. Attack 2. Defend 3. Heal "))
        if action ==1:
            ophealth-=200
            print("You use the killing curse to fully kill your opponent ")
        elif action ==2:
            phealth -=50
            print("You get hit with a buldegeoning curse, doing heavy damage!  ")  
        elif action ==3:
            if phealth==100:
                print("Maximum health! ")
            else:
                phealth+=40
                print("You use a muggle energy drink to recover some enrgy! ")
        else:
            print("Invalid input ") 
    if ophealth <= 0:
        print("You defeated your opponent! ")
        print("You gained 100 exp")
        print("You unlocked the disarming curse!  ")
        exp+=100
    if phealth<=0:
        print("You blacked out!")    


#Duel 5

if level ==5:
    ophealth = 250
    while ophealth> 0 and phealth > 0:
        action = int(input("Choose your action: 1. Attack 2. Defend 3. Heal "))
        if action ==1:
            ophealth-=75
            print("You use the disarming curse, but it fails as the opponent blocks it ")
        elif action ==2:
            phealth -=50
            print("You get hit with a buldegeoning curse, doing heavy damage!  ")  
        elif action ==3:
            if phealth==100:
                print("Maximum health! ")
            else:
                phealth+=45
                print("You use a first-aid kit and heal a decent amount ")
        else:
            print("Invalid input ") 
    if ophealth <= 0:
        print("You defeated your opponent! ")
        print("You gained 100 exp")
        print("You unlocked the disarming curse!  ")
        exp+=100
    if phealth<=0:
        print("You blacked out!")    
