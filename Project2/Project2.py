import queue
import sys
from threading import Thread
import concurrent.futures
from time import time
import matplotlib.pyplot






def caculate(identifier):
    finalanswer = 0
    for i in range(len(l)):
        if i % Num == identifier:


            finalanswer = finalanswer ^ int(l[i])
    Q.put(finalanswer)


def check(n):
    if  n> 40:
        return 40

    else:
        return n



global Num,lines
Num= int(sys.argv[1])
name = str(sys.argv[2])

Num=check(Num)



Q = queue.Queue()
final_result = 0
file=open(name,'r')
l=file.readlines()

st = time()

with concurrent.futures.ThreadPoolExecutor(max_workers=40) as exe:
    exe.map(caculate,range(Num))

while True:
    if(Q.empty()):
        break

    result = Q.get()
    final_result=final_result^result
et = time()

x=[5,10,15,20,25,30,35]
y=[1.9992,3.4947,3.8882,4.9660,5.8611,6.4447,7.9535]



matplotlib.pyplot.plot(x,y)
matplotlib.pyplot.xlabel("Iteration")
matplotlib.pyplot.ylabel("Time")
matplotlib.pyplot.show()


file = open('FinalResult_proj2.txt', 'w')
file.write('\n'.join([("FinalResult:"),str(final_result),("Time:"), str(et-st)]))
file.close()