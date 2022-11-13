from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        seen = set()
        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c))
                    seen.add((r, c))
        
        coords = [(0,1), (1,0), (0,-1), (-1,0)]
        distance = 1
        while q:
            # for distance += 1 at the end of the level traversal.
            for _ in range(len(q)):
                row, col = q.popleft()
                for rc, cc in coords:
                    r = row + rc
                    c = col + cc

                    if r >= 0 and r < rows and c >= 0 and c < cols and (r, c) not in seen:
                        mat[r][c] = distance
                        q.append((r, c))
                        seen.add((r, c))
                    
            distance += 1
        return mat
