#Number of Ways to Divide a Long Corridor
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        def rec(i,s) :
            if i==n :
                return 1 if s==2 else 0
            if dp[i][s]!=-1 :
                return dp[i][s]
            res=0
            if s==2 :
                if corridor[i]=='S' :
                    res=rec(i+1,1)
                else :
                    res=(rec(i+1,0) + rec(i+1,2))%mod
            else :
                if corridor[i]=='S' :
                    res=rec(i+1,s+1)
                else :
                    res=rec(i+1,s)
            dp[i][s]=res
            return res
        mod=10**9 + 7
        dp=[[-1]*3 for i in range(len(corridor))]
        n=len(corridor)
        return rec(0,0)

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        st=[]
        for i,x in enumerate(corridor) :
            if x=='S' :
                st.append(i)
        if len(st)<2 or len(st)%2==1:
            return 0
        p=1
        for i in range(1,len(st)-2,2):
            p=(p*(st[i+1]-st[i]))%(10**9 + 7)
        return p
