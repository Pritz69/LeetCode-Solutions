class Solution:
    def minOperations(self, n):
        total = 0
        memo = [x * 2 + 1 for x in range(n)]
        target = sum(memo) // n
        for i in memo:
            if (i - target) >= 0:
                total += i - target
        return total
      
      OR
      
class Solution:
    def minOperations(self, n: int) -> int:
        if n%2==0 :
            return (n//2)*(n//2)
        else :
            return (n//2)*((n//2)+1)
