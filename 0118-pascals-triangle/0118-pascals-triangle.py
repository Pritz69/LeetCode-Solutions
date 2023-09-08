class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1 :
            return [[1]]
        l=[[1],[1,1]]
        if numRows==2 :
            return l
        for i in range(numRows-2) :
            cl=l[-1]
            nl=[1]
            for j in range(1,len(cl)) :
                nl.append(cl[j]+cl[j-1])
            nl.append(1)
            l.append(nl)
        return l