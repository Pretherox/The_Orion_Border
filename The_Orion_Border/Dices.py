import random

class Dice:
 def dice(head):
    d_dice = random.randint(1,head)
    return d_dice
 def reward2(reward1,reward2):
    d2reward = random.choice([reward1,reward2])
    return d2reward
 def reward3(reward1,reward2,reward3):
    d3reward = random.choice([reward1,reward2,reward3])
    return d3reward