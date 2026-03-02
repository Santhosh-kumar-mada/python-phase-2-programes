#506 leetcode
import heapq
def relative(score):
    heap = []
    for inx,val in enumerate(score):
        heapq.heappush (heap,(-val,inx))
    print(heap)
    res = [""]*(len(score))
    rank = 1
    while heap:
        val,inx = heapq.heappop(heap)
        
        if rank == 1:
            res[inx]="Gold Medal"
        elif rank == 2:
            res[inx]="Silver Medal"
        elif rank == 3:
            res[inx]="Bronze Medal"
        else:
            res[inx]=str(rank)
        rank+=1
    return res
score = [10,3,8,9,4]
print(relative(score))