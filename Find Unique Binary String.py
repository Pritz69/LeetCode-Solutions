class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def conv(x) :
            sm=0
            p=0
            for i in range(len(x)-1,-1,-1) :
                sm += 2**p * int(x[i])
                p +=1
            return sm
        l=len(nums)
        r=2**l -1
        s=set()
        ans=0
        for x in nums :
            s.add(conv(x))
        for i in range(r+1) :
            if i not in s :
                ans=i
                break
        sans=""
        while ans > 0 :
            sans = str(ans%2) + sans
            ans = ans//2
        eo=l-len(sans)
        sans = "0"*(eo) + sans
        return sans 
