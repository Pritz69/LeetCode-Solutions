class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        t=sum(nums)
        rem=t%p
        if rem==0 :
            return 0
        res=len(nums)
        d={0:-1}
        c=0
        for i,n in enumerate(nums) :
            c = (c+n)%p
            pr = (c-rem+p)%p
            if pr in d :
                le=i-d[pr]
                res=min(res,le)
            d[c]=i
        return -1 if res==len(nums) else res