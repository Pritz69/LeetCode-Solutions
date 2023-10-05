class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t=len(nums)//3
        d={}
        for x in nums :
            d[x]=d.get(x,0)+1
        ans=[]
        for x in d :
            if d[x] > t :
                ans.append(x)
        return ans