#geeks for geeks practice problem

import heapq
def ropes(arr):
    heapq.heapify(arr)
    d=0
    while len(arr)>1:
        s=heapq.heappop(arr)
        f=heapq.heappop(arr)
        c = s+f
        d+=c
        heapq.heappush(arr,c)
    return d

arr= [4, 3, 2, 6]
print(ropes(arr))