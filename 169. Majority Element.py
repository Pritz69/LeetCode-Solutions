class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt,cand=0,0
        for x in nums :
            if cnt==0 :
                cand=x
            if cand==x :
                cnt +=1
            else :
                cnt -=1
        return cand
