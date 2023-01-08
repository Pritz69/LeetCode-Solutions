class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p,n=0,0
        for no in nums :
            if no < 0 :
                n +=1
            elif no > 0 :
                p +=1
        return (max(n,p)) 
