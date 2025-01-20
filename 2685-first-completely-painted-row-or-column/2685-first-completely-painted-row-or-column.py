class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n,m=len(mat),len(mat[0])
        d={}
        for i in range(n) :
            for j in range(m) :
                d[mat[i][j]]=(i,j)
        r=[0]*n
        c=[0]*m
        for i in range(len(arr)):
            ro,co=d[arr[i]]
            r[ro]+=1
            c[co]+=1
            if r[ro]==m or c[co]==n :
                return i