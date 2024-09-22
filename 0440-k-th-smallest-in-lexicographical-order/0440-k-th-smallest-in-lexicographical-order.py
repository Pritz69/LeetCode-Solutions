class Solution:
    def findKthNumber(self, n, k):
        cur = 1
        k = k - 1
        while k > 0:
            steps = self.calSteps(n, cur)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur

    def calSteps(self, n, cur):
        steps = 0
        n1, n2 = cur, cur + 1
        while n1 <= n:
            steps += min(n + 1, n2) - n1
            n1 *= 10
            n2 *= 10
        return steps
        
