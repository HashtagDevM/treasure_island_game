print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You\'re at a crossroad, do you go left or right? ").lower()

if choice1 == "left":
    choice2 = input('You reach a lake. There is an island in the middle. You see a sign indicating that a boat will come later. Do you go "swim" across or do you "wait" for the boat? ').lower()
    if choice2 == "wait":
        choice3 = (input('On the island is a house. You go inside and find a room with 3 doors. Which door do you choose? The "red", "yellow" or the "blue" door? ')).lower()
        if choice3 == "red":
            print("You open the door and trigger a trap. The room is engulfed in flames and you die.\nGame Over.")
        elif choice3 == "yellow":
            print("You enter the room and find a hidden stairway behind a bookcase. The stairway leads you through a dark passage into a cave. The cave is filled with treasure. You Win! ")
        else:
            print("You enter through the door and go inside. The creaking sound of the old door wakes the sleeping Vampire and he drains all your blood.\nGame Over. ")
    else:
        print("You get attacked by piranhas and die.\nGame Over.")        
else:
    print("You walk into a forrest. A hungry pack of wolves attack you.\nGame Over.")