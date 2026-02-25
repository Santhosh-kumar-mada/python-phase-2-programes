def binary_search(l,k):
    low = 0
    high = len(l)-1
    while low<=high:
        mid = (low+high)/2
        if l[mid]==k:
            return mid
        elif l[mid]>k:
            low = mid+1
        else:
            high = mid-1
            
li = [1,2,3,4,5,6,7,8]
k = 7
binary_search(li,k)