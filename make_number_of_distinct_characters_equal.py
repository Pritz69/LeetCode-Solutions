class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        for c1 in ascii_lowercase: 
            for c2 in ascii_lowercase: 
                if freq1[c1] and freq2[c2]: 
                    freq1[c1] -= 1
                    freq2[c1] += 1
                    freq1[c2] += 1
                    freq2[c2] -= 1
                    if sum(1 for v in freq1.values() if v) == sum(1 for v in freq2.values() if v): return True 
                    freq1[c1] += 1
                    freq2[c1] -= 1
                    freq1[c2] -= 1
                    freq2[c2] += 1
        return False 
