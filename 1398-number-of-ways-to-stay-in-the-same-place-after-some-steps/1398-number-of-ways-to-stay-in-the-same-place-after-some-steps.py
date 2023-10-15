class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp={}
        mod=10**9 + 7

        def rec(ind,steps) :
            if ind>=arrLen or ind<0:
               return 0
            if steps==0 :
                if ind==0 :
                    return 1
                else :
                    return 0
            if (ind,steps) in dp :
                return dp[(ind,steps)] 
            mover,stay,movel=0,0,0
            mover += rec(ind+1,steps-1)
            movel +=rec(ind-1,steps-1)
            stay += rec(ind,steps-1)

            dp[(ind,steps)] = (mover + stay + movel)%mod
            return dp[(ind,steps)]

        return rec(0,steps)