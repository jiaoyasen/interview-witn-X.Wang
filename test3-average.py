from data_generator import data_generator
from functools import reduce
import time
data = data_generator(10000)

def average(data):
    return reduce(lambda x,y:x + y,data)/len(data)

def average1(data):
    result = 0
    for i in data:
        result += i
    return result/len(data)

t1 = time.clock()
print(average(data))
t2 = time.clock()
print("The running time of reduce is ",(t2-t1))
t1 = time.clock()
print(average(data))
t2 = time.clock()
print("The running time of add is ",(t2-t1))