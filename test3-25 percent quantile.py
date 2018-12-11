from data_generator import data_generator
import math
data = [1,2,3,4,5,6,7,8,9]
def onequarterquantile(data):
    data_sorted = sorted(data)
    l = len(data)
    index = round(l*0.25)-1
    return  data_sorted[index]


print(data)
print(onequarterquantile(data))
