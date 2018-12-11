from data_generator import data_generator
import math
data = [1,2,3,4]
def threequarterquantile(data):
    data_sorted = sorted(data)
    l = len(data)
    index = round(l*0.75) -1
    return  data_sorted[index]


print(data)
print(threequarterquantile(data))