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

maxlevels =[]
for i in tqdm(range(100000)):
    lvl = setruns(1000)
    maxlevels.append(lvl)
    
plt.hist(maxlevels, bins=range(20,150,2))
plt.show()