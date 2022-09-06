class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        r=0
        s=set()
        x=0
        y=0
        while y<len(nums) :
            r+=nums[y]
            if y-x+1<2 :
                y+=1
            elif y-x+1 ==2 :
                if r in s :
                    return True
                else :
                    s.add(r)
                r-=nums[x]
                x+=1
                y+=1
        return False
