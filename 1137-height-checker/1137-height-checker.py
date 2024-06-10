class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        nl=sorted(heights)
        c=0
        for i in range(len(heights)) :
            if nl[i]!=heights[i] :
                c +=1
        return c