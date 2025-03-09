import math
import random


def calculate_damage(attack, defense, dice):

    finaldamage = math.pow(abs(math.floor( attack * (100/(100+defense)) * 1 )), 1.01) + dice

    return finaldamage
def calculate_gacha():

    num = random.randint(1, 1000)
    if 250 >= num <= 1000:
        result = 4 # 4*
    elif 50 >= num <= 249:
        result = 5 # 5*
    elif 1 >= num <= 49:
        result = 6 # 5* LR
    else:
        result = 0

    return result

