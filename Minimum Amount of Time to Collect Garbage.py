class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans=0
        g,p,m=0,0,0
        for i in range(len(garbage)) :
            for x in garbage[i] :
                if x=='G' :
                    g=i
                if x=='P' :
                    p=i
                if x=='M' :
                    m=i
                ans +=1
        for i in range(g) :
            ans += travel[i]
        for i in range(p) :
            ans += travel[i]
        for i in range(m) :
            ans += travel[i]
        return ans
                
