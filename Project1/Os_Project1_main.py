import subprocess

import sys
from time import time, sleep
import matplotlib.pyplot


Num = int(sys.argv[1])
name = str(sys.argv[2])

for i in range(Num):
    subprocess.call(['python', 'MultiPro.py', str(i), str(Num), name])

result = 0
t = []

for i in range(Num):
    file = open('Task' + str(i) + '.txt', 'r')
    result = result ^ int(file.readline())
    t.append(float(file.readline()))
    file.close()



x=[]

for i in range(10):
    x.append(i)





matplotlib.pyplot.plot(x,t)
matplotlib.pyplot.xlabel("Iteration")
matplotlib.pyplot.ylabel("Time")
matplotlib.pyplot.show()

file = open('FinalResult_proj1.txt', 'w')
file.write('\n'.join([("FinalResult:"),str(result),("Time:"), str(max(t))]))
file.close()
