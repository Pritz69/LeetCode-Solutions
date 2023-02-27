"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n,r,c) :
            same=True
            for i in range(n) :
                for j in range(n) :
                    if grid[r][c] != grid[r+i][c+j] :
                        same=False
                        break
            if same :
                return Node(grid[r][c],True)
            n=n//2
            left=dfs(n,r,c)
            right=dfs(n,r,c+n)
            leftd=dfs(n,r+n,c)
            rightd=dfs(n,r+n,c+n)
            return Node(0,False,left,right,leftd,rightd)
        return dfs(len(grid),0,0)
