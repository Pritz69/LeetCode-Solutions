class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        l,r=0,len(cells)
        res=-1
        def dfs(m) :
            grid = [[0]*col for i in range(row)]
            for i in range(m):
                r,c= cells[i]
                grid[r-1][c-1]=1

            st = [(0,c) for c in range(col) if grid[0][c]==0]
            visit = set()
            while st :
                r,c = st.pop()
                if r==row-1 :
                    return True
                if (r,c) in visit :
                    continue

                visit.add((r,c))
                for i,j in [(0,1),(0,-1),(1,0),(-1,0)] :
                    nr,nc = r+i,c+j
                    if nr>=0 and nr<row and nc>=0 and nc<col and grid[nr][nc]==0 :
                        st.append((nr,nc))
                
            return False
        while l<=r :
            m = (l+r)//2
            if dfs(m) :
                res = m
                l = m+1
            else :
                r = m-1
        return res
