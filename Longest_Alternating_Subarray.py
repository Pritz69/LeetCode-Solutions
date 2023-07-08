class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        for i in range(n) :
            c=1
            s=1
            nxt = nums[i]
            for j in range(i+1,n) :
                nxt += s
                if nums[j]==nxt :
                    c +=1
                else :
                    break
                s = s*(-1)
            ans = max(ans,c)
        if ans==1 :
            return -1
        return ans
