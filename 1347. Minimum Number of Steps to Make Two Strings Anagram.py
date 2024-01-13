class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1=Counter(s)
        c2=Counter(t)
        ans=0
        #print(c1,c2)
        for x in c1 :
            if x in c2 :
                ans +=abs(c2[x]-c1[x])
                c1[x]=0
                c2[x]=0
        for x in c2 :
            if c2[x] != 0:
                ans += c2[x]
        for x in c1 :
            if c1[x] !=0 :
                ans += c1[x]
        return ans//2
