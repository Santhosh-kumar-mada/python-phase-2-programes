def lenearsearch (a,key):
    for i in range(len(a)):
        if a[i] == key:
            return i
        
    return -1

array = [1,2,3,4,5,6,7]
key = 3
print(lenearsearch(array,key))