class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod=int(1e9 + 7)
        def rec(i,s) :
            if i==n :
                return 1
            if (i,s) in dp:
                return dp[(i,s)]
            c=0
            if i==0 :
                c += rec(i+1,"a")
                c += rec(i+1,"e")
                c += rec(i+1,"i")
                c += rec(i+1,"o")
                c += rec(i+1,"u")
            if s and s[-1]=='a' :
                c += rec(i+1,"e")
            if s and s[-1]=='e' :
                c += rec(i+1,"a")
                c += rec(i+1,"i")
            if s and s[-1]=='i' :
                c += rec(i+1,"a")
                c += rec(i+1,"e")
                c += rec(i+1,"o")
                c += rec(i+1,"u")
            if s and s[-1]=='o' :
                c += rec(i+1,"i")
                c += rec(i+1,"u")
            if s and s[-1]=='u' :
                c += rec(i+1,"a")
            dp[(i,s)] = c % mod
            return dp[(i,s)]
        dp={}
        return rec(0,"")