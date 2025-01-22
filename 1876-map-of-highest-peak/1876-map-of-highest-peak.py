class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n,m=len(isWater),len(isWater[0])
        res=[[-1]*m for i in range(n)]
        q=deque()
        for r in range(n) :
            for c in range(m) :
                if isWater[r][c] :
                    res[r][c]=0
                    q.append((r,c))
        d=[(1,0),(0,1),(0,-1),(-1,0)]
        while q :
            r,c=q.popleft()
            h=res[r][c]
            for x in d :
                nr=r+x[0]
                nc=c+x[1]
                if nr <0 or nc<0 or nr==n or nc==m or res[nr][nc]!=-1 :
                    continue
                res[nr][nc]=h+1
                q.append((nr,nc))
        return res
            