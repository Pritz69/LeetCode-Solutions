from collections import Counter
class Solution:
    def maximumLength(self, s: str) -> int:
        subarrays = []

        for i in range(len(s)):
            index = i
            while index < len(s) and s[index] == s[i]:
                subarrays.append(s[i:index+1])
                index += 1

        counter = Counter(subarrays)
        max_len = 0

        for j, n in counter.items():
            if n >= 3:
                if len(j) > max_len:
                    max_len = len(j)

        if max_len == 0:
            return -1
            
        return max_len

        