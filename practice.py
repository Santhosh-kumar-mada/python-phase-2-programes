def findMin(arr):
    l = 0
    h = len(arr)-1
    while l < h:
        m = (l + h) // 2

        if arr[m] > arr[h]:
            l = m + 1
        else:
            h = m
    return arr[l]

arr = [3,4,5,1,2]
print(findMin(arr))