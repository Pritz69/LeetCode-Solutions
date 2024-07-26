class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        d=[[float('inf')]*n for i in range(n)]
        for x in edges :
            d[x[0]][x[1]]=x[2]
            d[x[1]][x[0]]=x[2]
        for i in range(n) :
            d[i][i]=0
        for i in range(n) :
            for j in range(n) :
                for k in range(n) :
                    d[j][k]=min(d[j][k],d[j][i]+d[i][k])
        
        m=float('inf')
        ans=0
        for i,x in enumerate(d) :
            c=0
            for e in x :
                if e <= distanceThreshold :
                    c +=1
            if c < m :
                m=c
                ans=i
            elif c==m :
                ans=max(ans,i)
        return ans