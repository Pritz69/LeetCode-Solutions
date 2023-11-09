class Solution:
    def countHomogenous(self, s: str) -> int:
        d={}
        #for x in s :
        #   d[x]=d.get(x,0)+1
        d=Counter(s)
        tc=0
        cs=1
        for i in range(1,len(s)) :
            if s[i]==s[i-1] :
                cs +=1
            else :
                tc += (cs*(cs-1))//2
                cs =1
        tc += (cs*(cs-1))//2
        for x in d :
            tc += d[x]
        mod=10**9 + 7
        return tc%(mod)