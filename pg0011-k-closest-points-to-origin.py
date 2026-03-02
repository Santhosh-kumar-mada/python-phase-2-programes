import heapq
#function 
def origin(points,k):
    heap = []
    for x,y in points:
        dist = (x*x+y*y)
        heapq.heappush(heap,(-dist,[x,y]))


        if len(heap)>k:
            heapq.heappop(heap)
    for i in heap:
        print(i)

points = [[1,3],[-2,2]]
k=2
origin(points,k)