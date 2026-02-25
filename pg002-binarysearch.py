def binary_search(a,k):
    l = 0
    h = len(a)-1
    while l <= h:
        mid = (l+h)//2
        if a[mid] == k:
            return mid
        elif a[mid] < k:
            l = mid +1
        else:
            h = mid-1
    return -1

array = [1,2,3,4,5,6,7]
key = 3
print(binary_search(array,key))