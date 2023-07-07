# 0->0 = 0
# 1->0 = 1
# 0->1 = 2
# 1->1 = 3
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows,cols = len(board), len(board[0])
        def cnt(i,j) :
            s=0
            for k, l in (i + 1, j), (i + 1, j - 1), (i + 1, j + 1), (i, j + 1), (i - 1, j + 1), (i, j - 1), (i - 1, j - 1), (i - 1, j):
                if not (0 <= k < rows) or not (0 <= l < cols):
                    continue         
                if board[k][l] in [1,3] :
                    s +=1
            return s
        for r in range(rows) :
            for c in range(cols) :
                count = cnt(r,c)
                if board[r][c]==1 :
                    if count in [2,3] :
                        board[r][c]=3
                else :
                    if count==3 :
                        board[r][c]=2
        
        for r in range(rows) :
            for c in range(cols) :
                if board[r][c]==1 :
                    board[r][c]=0
                elif board[r][c] in [2,3] :
                    board[r][c]=1
                
        
                
                
