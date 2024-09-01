class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) > m*n or len(original) < m*n:
            return []
        ans=[[0]*n for i in range(m)]
        i=0
        j=0
        for x in original :
            ans[i][j]=x
            j +=1
            if j==n :
                i +=1
                j=0
        return ans