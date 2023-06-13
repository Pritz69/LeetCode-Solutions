class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n =len(grid)
        c =0
        r = defaultdict(int)
        for x in grid :
            r[tuple(x)] += 1
        coln =[[0]*n for i in range(len(grid[0]))]
        for i in range(n) :
            for j in range(len(grid[0])) :
                coln[j][i] = grid[i][j]
        for x in coln :
            if tuple(x) in r :
                c +=r[tuple(x)]
        return c
