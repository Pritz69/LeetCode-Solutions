class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l,r=0,1
        ans=0
        f=0
        while r< len(num)-1 :
            if num[l]==num[r] and num[r]==num[r+1] :
                ans = max(ans, int(num[r]*3))
                f=1 
            l=r
            r+=1
        if f==0 :
           return ""
        if ans==0 :
            return "000"
        return str(ans)
