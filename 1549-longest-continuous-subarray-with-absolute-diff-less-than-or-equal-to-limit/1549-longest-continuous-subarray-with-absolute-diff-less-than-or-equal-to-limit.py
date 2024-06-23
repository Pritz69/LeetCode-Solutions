class Solution:
    def longestSubarray(self, A, limit):
        maxd = collections.deque()
        mind = collections.deque()
        i = 0
        for a in A:
            while len(maxd) and a > maxd[-1]: maxd.pop()
            while len(mind) and a < mind[-1]: mind.pop()
            maxd.append(a)
            mind.append(a)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == A[i]: maxd.popleft()
                if mind[0] == A[i]: mind.popleft()
                i += 1
        return len(A) - i