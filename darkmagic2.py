import random
import matplotlib.pyplot as plt
from tqdm import tqdm
import pandas as pd
import numpy as np

def reachruns(limit):
    lvl = 20
    count=0
    while lvl< limit:
        choices = [-1,1]
        ran=random.choice(choices)
        lvl = lvl + ran
        if lvl == 19: 
            lvl = 20
        count+=1
    return count


maxlevel = 35
runs = 100000

upgradecount=[]
for i in tqdm(range(runs)):
    upgradecount.append(reachruns(maxlevel))

Sum = 0
series = pd.value_counts(upgradecount)
x = series * series.keys() / runs
average = sum(x)
stddev = np.sqrt(sum(series*(series.keys() - average)**2/runs))

plt.hist(upgradecount, bins=range(0,int(average + 5*stddev)))
plt.title("average number of attempts to reach level "+str(maxlevel)+" = " + str(average) + " with a standard deviation of " + str(stddev))
plt.ylabel('frequency of attempts taken')
plt.xlabel('attempts to reach level '+ str(maxlevel))
plt.show()