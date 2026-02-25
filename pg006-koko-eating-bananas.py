#lc 875

#using lenear search
# import math
# def minEatingSpeed(a, h):
#     k = 1
#     while k<=max(a):
#         sum = 0
#         for i in range(len(a)):
#                 sum += math.ceil(a[i]/k)

#         if sum <= h:
#             return k
#         k += 1

# a = [3,6,7,11]
# h = 8
# print(minEatingSpeed(a,h))  


#using binary search
import math
def minEatingSpeed(a, h):
    l = 1
    r = max(a)
    while l<=r:
        k = l+(r-l)//2
        sum = 0
        for i in range(len(a)):
                sum += math.ceil(a[i]/k)

        if sum <= h:
            r = k-1
        else:
            l = k+1

    return l
a = [30,11,23,4,20]
h = 5
print(minEatingSpeed(a,h))