class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:

        n = len(words)

        for left in range(n):
            if words[(startIndex+left)%n ] == target: break
        if target not in words :
            return -1    

        for right in range(n):
            if words[(startIndex-right)%n] == target: break
  
        return  min(left, right)
