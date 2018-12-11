import random
import collections
def data_generator(n):#生成随机数list，list长度为n
    data= [random.randint(-100,101) for j in range(n)]
    return data