class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1, words2 = sentence1.split(), sentence2.split()
        n1, n2 = map(len, (words1, words2))
        if n1 > n2:
            return self.areSentencesSimilar(sentence2, sentence1)
        i = 0
        while i < n1 and words1[i] == words2[i]:
            i += 1
        while i < n1 and words1[i] == words2[n2 - n1 + i]:
            i += 1
        return i == n1