from data_generator import data_generator
data = [1,2,3,4,5,6]
def median(L):
    l = len(L)
    L_sorted = sorted(L)
    print(L_sorted)
    if l%2 == 0:
        result = (L_sorted[l//2-1] + L_sorted[l//2]) / 2
    else:
        result = L_sorted[l//2]
    return result
print(data)
print(median(data))
