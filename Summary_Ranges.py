class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans=[]
        if len(nums)==0:
            return []
        l=nums[0]
        r=nums[0]
        for i in range(1,len(nums)) :
            if nums[i]==(r+1) :
                r=nums[i]
                continue
            else :
                if l==r :
                    ans.append(str(l))
                else :
                    x = str(l) + "->" + str(r)
                    ans.append(x)
                l,r=nums[i],nums[i]
        if l==r :
            ans.append(str(l))
        else :
            x = str(l) + "->" + str(r)
            ans.append(x)
        return ans
