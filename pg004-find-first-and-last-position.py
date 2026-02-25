def find(arr,x):
    n = len(arr)
    def first():
        l,r,ans = 0,n-1,-1
        while l<=r:
            m = (l+r)//2
            if arr[m]>=x:
                r = m-1
            else:
                l = mid+1
            if arr[m] == x:
                ans = m 
            return ans
    def last():
        l,r,ans = 0, n-1 , -1
        while l<= r:
            m = (l+r)//2
            if arr[m]<=x:
                l = m+1
            else:
                r = m-1
            if arr[m] == r:
                ans = m
        return ans
    return [first(),last()]

find([1,3,5,5,5,5,67,123,125])