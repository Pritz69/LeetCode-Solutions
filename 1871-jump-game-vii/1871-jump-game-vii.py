class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        q = deque([0])
        farthest = 0
        while q:
            i = q.popleft()
            if i == n - 1:
                return True
            start = max(i + minJump, farthest + 1)
            end = min(i + maxJump, n - 1)
            for j in range(start, end + 1):
                if s[j] == '0':
                    q.append(j)
            farthest = end
        return False