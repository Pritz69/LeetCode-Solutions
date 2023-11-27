class Solution:
    def knightDialer(self, n: int) -> int:

        jumps=[[4, 6],[6, 8],[7, 9],[4, 8],[3, 9, 0],[],[1, 7, 0],[2, 6],[1, 3],[2, 4]]
        dp=[1]*10
        mod = 10**9 + 7
        for i in range(n-1) :
            newdp=[0]*10
            for n in range(10) :
                for j in jumps[n] :
                    newdp[j] = (newdp[j] + dp[n])%mod
            dp=newdp
        
        ans=0
        for i in range(len(dp)) :
            ans = (ans + dp[i])%mod
        return ans

class Solution:
    def knightDialer(self, n: int) -> int:
        
        jumps=[[4, 6],[6, 8],[7, 9],[4, 8],[3, 9, 0],[],[1, 7, 0],[2, 6],[1, 3],[2, 4]]
        dp={}
        mod=10**9 + 7

        def rec(rem,st) :
            if rem==0 :
                return 1
            if (rem,st) in dp :
                return dp[(rem,st)]
            ans=0
            for nxt in jumps[st] :
                ans = (ans +  rec(rem-1,nxt))%mod
            
            dp[(rem,st)]=ans
            return ans

        res=0
        for st in range(10) :
            res = (res + rec(n-1,st))%mod
        return res
