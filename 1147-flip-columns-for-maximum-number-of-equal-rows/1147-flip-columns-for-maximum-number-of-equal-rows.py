class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d=defaultdict(int)
        for row in matrix :
            key=tuple(row)
            if row[0] :
                key=tuple([0 if n else 1 for n in row])
            d[key] +=1
        return max(d.values())