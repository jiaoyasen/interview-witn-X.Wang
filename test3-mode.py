import collections
import operator
import random
import time

def data_generator(n):#生成随机数list，list长度为n
    data= [random.randint(-100,101) for j in range(n)]
    return data


def mode(L):#Counter后的dict，交换k,v组成tuple，max取最大，python cookbook说这种最简单，但没有考虑众数可能有多个的情况
    num_dict = collections.Counter(L)
    num_max = zip(num_dict.values(),num_dict.keys())
    result = max(num_max)
    return result[1]


def mode1(L):#Counter后按value排序，这个我考虑了多个众数的情况
    num_dict = collections.Counter(L)
    num_sorted = sorted(num_dict.items(),key = operator.itemgetter(1),reverse=True)
    _,tmp = num_sorted[0]
    result = []
    for k,v in num_sorted:
        if v == tmp:
            result.append(k)
    return result


def mode2(L):#Counter自带的most_common(1)，也同样没有考虑众数有多个的情况
    num_dict = collections.Counter(L).most_common(len(L))
    result = []
    tmp = num_dict[0][1]
    for k,v in num_dict:
        if v == tmp:
            result.append(k)
    return result

L = data_generator(100000)
print(L)
t1 = time.clock()
print(mode(L))
t2 = time.clock()

t1 = time.clock()
print(mode1(L))
t2 = time.clock()
print("The running time of sort is ",(t2-t1))
t1 = time.clock()
print(mode2(L))
t2 = time.clock()
print("The running time of most_common is ",(t2-t1))