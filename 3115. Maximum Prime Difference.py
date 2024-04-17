class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        ans=[]
        def prime(x) :
            if x==1 :
                return False
            if x==2 or x==3 :
                return True
            for i in range(2,int(x**0.5)+1) :
                if x%i==0 :
                    return False
            return True
        for i in range(len(nums)) :
            if prime(nums[i]) :
                ans.append(i)
        return ans[-1]-ans[0]
