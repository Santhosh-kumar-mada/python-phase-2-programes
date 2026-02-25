#leetcode 69. Sqrt(x)
def square_root(n):
    #my method
    # a = 1
    # for a in range(n):
    #     if a**2 > n:
    #         return a-1

    #sir method
    # for i in range(1,n+1):
    #     if i*i == n:
    #         return i
    #     if i*i > n:
    #         return i-1
    # return 0

    #Binary search method
    l = 1
    r = n
    while l<=r:
        mid = l+(r-l)//2
        if mid * mid >n:
            r = mid-1
        elif mid * mid <n:
            l = mid+1
        else :
            return mid
    return r

n=8
print(square_root(n))