class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        l=[]
        arr=[1,2,3,4,5,6,7,8,9]
        def rec(i,t,x) :
            if i==len(arr) :
                if x==0 and len(t)==k:
                    l.append(t.copy())
                return 
            if arr[i]<=x :
                t.append(arr[i])
                rec(i+1,t,x-arr[i])
                t.pop(len(t)-1)
            rec(i+1,t,x)
        rec(0,[],n)
        return l