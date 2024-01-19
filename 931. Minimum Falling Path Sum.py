class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        for row in range(1, n):
            for col in range(n):
                options = [matrix[row-1][max(col-1,0)], matrix[row-1][col],matrix[row-1][min(col+1,n-1)]]
                #if col+1 < n:
                #    options.append(matrix[row-1][col+1])
                matrix[row][col] += min(options)
        #print(matrix)
        return min(matrix[-1])



class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        def rec(i,j) :
            if i==n or j==n :
                return 0
            if (i,j) in dp :
                return dp[(i,j)]
            s=matrix[i][j] + min(rec(i+1,j),rec(i+1,j-1) if j > 0 else float('inf'),rec(i+1,j+1) if j < n-1 else float('inf'))
            dp[(i,j)]=s
            return s
        dp={}
        ans=float('inf')
        for i in range(n) :
            ans=min(ans,rec(0,i))
        return ans
