
import sys
from time import time

identifier = int(sys.argv[1])
Num = int(sys.argv[2])
name = str(sys.argv[3])


lines = open(name, 'r').readlines()
finalanswer = 0

st = time()
for i in range(len(open(name, 'r').readlines())):
    if i % Num == identifier:
        finalanswer = finalanswer ^ int(lines[i])
et = time()



file = open('Task' + str(identifier) + '.txt', 'w')
file.write('\n'.join([str(finalanswer), str(et-st)]))
file.close()