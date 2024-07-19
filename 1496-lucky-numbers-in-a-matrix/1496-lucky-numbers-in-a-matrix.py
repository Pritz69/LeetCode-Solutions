class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        for i in range(len(matrix)):
            m=min(matrix[i])
            ind=matrix[i].index(m)
            f=0
            for i in range(len(matrix)) :
                if m < matrix[i][ind] :
                    f=1
                    break
            if f==0 :
                ans.append(m)
        return ans 