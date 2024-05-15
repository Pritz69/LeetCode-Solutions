class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N=len(grid)
        def inbounds(r,c) :
            if min(r,c) >= 0  and max(r,c) < N :
                return True
            return False
        def precompute() :
            q=deque()
            mindist={}
            for r in range(N) :
                for c in range(N) :
                    if grid[r][c]==1:
                        q.append([r,c,0])
                        mindist[(r,c)]=0
            while q :
                r,c,d=q.popleft()
                nd=[[r+1,c],[r,c+1],[r-1,c],[r,c-1]]
                for nr,nc in nd :
                    if inbounds(nr,nc) and (nr,nc) not in mindist :
                        mindist[(nr,nc)]=d+1
                        q.append([nr,nc,d+1])
            return mindist
        mindist=precompute()
        visit=set()
        maxHeap=[(-mindist[(0,0)],0,0)]
        visit.add((0,0))
        while maxHeap :
            d,r,c=heapq.heappop(maxHeap)
            d=-d
            if r==N-1 and c==N-1 :
                return d
            nd=[[r+1,c],[r,c+1],[r-1,c],[r,c-1]]
            for nr,nc in nd :
                if inbounds(nr,nc) and (nr,nc) not in visit :
                    visit.add((nr,nc))
                    updateddist=min(d,mindist[(nr,nc)])
                    heapq.heappush(maxHeap,(-updateddist,nr,nc))
