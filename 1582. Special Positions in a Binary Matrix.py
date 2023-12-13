class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        c=0
        for i in range(len(mat)):
            for j in range(len(mat[0])) :
                if mat[i][j]==1 :
                    f=0
                    for k in range(len(mat[0])) :
                        if k!=j and mat[i][k]==1 :
                            f=1
                            break
                    for l in range(len(mat)):
                        if l!=i and mat[l][j]==1 :
                            f=1
                            break
                    if f==0 :
                        c +=1
        return c


--> BETTER SOLUTION ---->

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [0] * len(mat)
        cols = [0] * len(mat[0])
        for i in range(len(mat)):
          for j in range(len(mat[i])):
            if mat[i][j] == 1:
              rows[i] += 1
              cols[j] += 1
        special = 0
        for i in range(len(mat)):
          for j in range(len(mat[i])):
            if mat[i][j] == 1:
              if rows[i] == 1 and cols[j] == 1:
                special += 1
        return special
