import random
import matplotlib.pyplot as plt
from tqdm import tqdm

def setruns(limit):
    lvl = 20

    i = 0
    while i< limit:
        choices = [-1,1]
        ran=random.choice(choices)
        lvl = lvl + ran
        if lvl == 19: 
            lvl = 20
        i+=1
    return lvl

runs = 10000
attempts = 100

maxlevels =[]
for i in tqdm(range(runs)):
    lvl = setruns(attempts)
    maxlevels.append(lvl)
    
plt.hist(maxlevels, bins=range(20,max(maxlevels)))
plt.title("average level reached after attempting to upgrade "+str(attempts)+"times")
plt.ylabel('frequency of level acheived')
plt.xlabel('maximum level achieved')
plt.show()