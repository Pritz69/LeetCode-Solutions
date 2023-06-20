class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        li=[-1]*n
        d=(2*k) + 1
        l,s=0,0
        for r in range(n) :
            s += nums[r]
            if r-l + 1 == d :
                li[l+k] = s//d
                s -= nums[l]
                l +=1
        return li

     
