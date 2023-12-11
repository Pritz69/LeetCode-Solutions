class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n=len(arr)
        can=[arr[n//4],arr[n//2],arr[3*n//4]]
        tar=n/4
        for c in can :
            l=0
            r=n-1
            lb=n
            while l<=r :
                m=(l+r)//2
                if arr[m] >=c :
                    lb=m
                    r=m-1
                else :
                    l=m+1
            l=0
            r=n-1
            ub=n
            while l<=r :
                m=(l+r)//2
                if arr[m] >c :
                    ub=m
                    r=m-1
                else :
                    l=m+1
            if ub-lb > tar :
                return c
        return -1

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n=len(arr)
        c=n//4
        Co=Counter(arr)
        for x in Co :
            if Co[x] > c :
                return x
        return 0
