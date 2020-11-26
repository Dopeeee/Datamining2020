import numpy as np
import random 
import argparse

parser = argparse.ArgumentParser(description='Input the dimension to generate the file')
parser.add_argument('--dimension', '-d', help='the data dimension', type=int, required=True)

args = parser.parse_args()

d = args.dimension
N = 10000
w = np.ones(d)
data = np.empty(shape = (N,d+1),dtype = int)

def randomArray(d):
    temp = np.empty(d,dtype = int)
    for i in range(d):
        n = random.randint(0,10)
        x = random.randint(-40 , -20) if n%2==0 else random.randint(20,40)
        temp[i] = x
    return temp

for i in range(N):
    temp = randomArray(d)
    if(np.sum(np.dot(w,temp))>0):
        label = 1
        temp[:] =  temp[:] + 10
    elif(np.sum(np.dot(w,temp))< 0):
        label = 0
        temp[:] = temp[:] - 10
    elif(np.sum(np.dot(w,temp)) == 0):
        temp[:] = temp[:] + 10
        label = 1
    data[i] = np.append(temp, label)
filename = "d" + str(d) + ".txt"

with open(filename,"w") as f:
    f.write(str(N)) 
    f.write(' ')
    f.write(str(d)) 
    f.write("\n")
    for i in range(len(data)-1):
        for j in range(len(data[0])):
            f.write(str(data[i][j]))
            f.write(' ')
        f.write("\n")
    for j in range(len(data[0])):
        f.write(str(data[N-1][j]))
        f.write(' ')
