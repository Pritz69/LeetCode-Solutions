class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        d=0
        for c in range(len(strs[0])):
            for r in range(len(strs)-1):
                if strs[r][c] > strs[r+1][c]:
                    d +=1
                    break
        return d
