class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def gcd(x,y) :
            if y==0 :
                return x
            return gcd(y,x%y)
        c=0
        l=0
        while l < len(nums) :
            for r in range(l+1,len(nums)) :
                x=str(nums[l])
                y=str(nums[r])
                if gcd(int(x[0]),int(y[-1]))==1 :
                    c +=1
            l +=1
        return c
