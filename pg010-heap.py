import heapq
data = [2,6,1,8,9,5,11,15]


#heapify
heapq.heapify(data)
print(data)


#push
heapq.heappush(data,4)
print(data)


#pop 
heapq.heappop(data)
print(data)


#heap sort
d1=data.copy()
for i in range(len(d1)):
    print(heapq.heappop(d1))


#print original
print(data)