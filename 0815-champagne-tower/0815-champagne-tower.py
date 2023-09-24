class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prevrow=[poured]
        for row in range(1,query_row+1) :
            currrow=[0]*(row+1)
            for i in range(row) :
                extra=prevrow[i]-1
                if extra > 0 :
                    currrow[i]=currrow[i] + (0.5)*extra
                    currrow[i+1]=currrow[i+1] + (0.5)*extra
            prevrow=currrow
        return min(1,prevrow[query_glass])