import threading
from threading import Thread
import time
import concurrent.futures
from time import time ,sleep
import queue
import sys
from threading import Lock




num_t = []
finalres = 0

lock = Lock()





def compute(index):
    global finalres

    result = 0
    for i in range(len(lines)):
        if i % Num == index:
            result = result ^ int(lines[i])


    if result == 0:
        print("final_result becuase result be zero : " + str(finalres))

    else :
        if lock.acquire(timeout=2):


           finalres = finalres ^ result
           sleep(1)
           print("Shared amount up to this moment : "+str(finalres))
           lock.release()
        else :
            print("timeOut")


global Num,lines
Num= int(sys.argv[1])
file_name = str(sys.argv[2])



f=open(file_name,'r')
lines=f.readlines()
start = time()



with concurrent.futures.ThreadPoolExecutor(max_workers=Num) as executor:
    executor.map(compute,range(Num))
    for i in range (Num):
        print("thread"+str(i)+"is started\n")



end = time()

print("FinalResult:"+str(finalres))
print("Time:"+str(end-start))


