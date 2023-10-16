class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row=[1]
        for i in range(rowIndex):
            new=[0]*(len(row)+1)
            for j in range(len(row)) :
                new[j] += row[j]
                new[j+1] += row[j]
            row=new
        
        return row