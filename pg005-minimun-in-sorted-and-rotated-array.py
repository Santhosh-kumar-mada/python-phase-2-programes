#leet code 153
def findMin(arr):
    l,h=0,len(arr)-1
    while l<h:
        m = l+h//2
        if arr[m]>arr[h]:
            l=m+1
        else:
            r = m
    return arr[l]
arr = [4,5,6,7,0,1,2,3,4]
print(findMin(arr))