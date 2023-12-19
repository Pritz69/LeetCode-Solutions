class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n=len(img)
        m=len(img[0])
        nimg=[[0]*m for i in range(n)]
        for i in range(n) :
            for j in range(m) :
                s = img[i][j]
                c = 1  
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        ni, nj = i + x, j + y
                        if i==ni and j==nj :
                            continue
                        if 0 <= ni < n and 0 <= nj < m:
                            s += img[ni][nj]
                            c += 1
                nimg[i][j] = s // c
        return nimg 
