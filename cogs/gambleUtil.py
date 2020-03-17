from random import random

def rpsConvertHumanChoice(humanInput):
    if humanInput in ["rocks","rock","r"]:
        return 1
    elif humanInput in ["papers","paper","p"]:
        return 2
    elif humanInput in ["scissors","scissor","s"]:
        return 3
    else:
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
        machine = humanInput - 1 
        if machine == 0:
            machine = 3
    else:
        cheat = 1
        machine = humanInput + 1
        if machine == 4:
            machine = 1
    return machine,cheat

def rpsGetWinner(human,machine):
    diff = (human - machine) % 3
    if diff == 2:
        return -1
    else:
        return diff
