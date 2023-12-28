class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        dp={}
        def rec(i,k,prev,prevc) :
            if k<0 :
                return float("inf")
            if i==len(s) :
                return 0
            if (i,k,prev,prevc) in dp :
                return dp[(i,k,prev,prevc)]
            if s[i]==prev :
                inc = 1 if prevc in [1,9,99] else 0
                res = inc + rec(i+1,k,prev,prevc+1)
            else :
                res = min(rec(i+1,k-1,prev,prevc),1+rec(i+1,k,s[i],1))
            dp[(i,k,prev,prevc)]=res
            return res
        return rec(0,k,"",0)
