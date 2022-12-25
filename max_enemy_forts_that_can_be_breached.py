class Solution: 
    def captureForts(self, forts: List[int]) -> int:
        max_captured = curr_idx = 0
        for index, fort in enumerate(forts): 
            if fort != 0:
                if forts[curr_idx] == -fort: 
                    max_captured = max(max_captured, index - curr_idx - 1)
                curr_idx = index
        return max_captured
