class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def cnt(n) :
            return bin(n).count("1")
        cmin,cmax=nums[0],nums[0]
        pmax=float('-inf')
        for n in nums :
            if cnt(n)==cnt(cmin) :
                cmin=min(cmin,n)
                cmax=max(cmax,n)
            else :
                if cmin < pmax :
                    return False
                pmax=cmax
                cmax,cmin=n,n
        if cmin < pmax :
            return False
        return True
