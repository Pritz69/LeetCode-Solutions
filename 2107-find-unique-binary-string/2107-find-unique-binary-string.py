class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s=set()
        for x in nums :
            s.add(int(x,2))
        for i in range(0,len(nums)+1) :
            if i not in s :
                ans=bin(i)[2:]
                if len(ans)!=len(nums) :
                    return ((len(nums)-len(ans))*"0" + ans)
                else :
                    return ans

