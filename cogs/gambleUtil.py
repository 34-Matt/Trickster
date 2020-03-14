from random import random

def rpsConvertHumanChoice(humanInput):
    if humanInput == "rock":
        return 1
    elif humanInput == "paper":
        return 2
    elif humanInput == "scissors":
        return 3
    else
        return 0

def rpsGetMachineChoice(humanInput):
    machine = random() * 100
    cheat = 0
    if machine < 30:
        machine = 1
    elif machine < 60:
        machine = 2
    elif machine < 90:
        machine = 3
    elif machine < 95:
        cheat = -1
        machine = (humanInput % 3) - 1
    else:
        cheat = 1
        machine = (humanInput % 3) + 1
    return machine,cheat

def rpsGetWinner(human,machine):
    diff = (human - machine) % 3
    if diff == 2:
        return -1
    else:
        return diff

def rpsName(choice):
    if choice == 1:
        return "Rock","./Images/Green_Axe.png"
    elif choice == 2:
        return "Paper","./Images/Red_Sword.png"
    elif choice == 3:
        return "Scissors","./Images/Blue_Sword.png"
    else
        return "Invalid"
