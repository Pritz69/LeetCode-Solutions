class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefix_count = defaultdict(int)
        
        for word in words:
            prefix = ""
            for char in word:
                prefix += char
                prefix_count[prefix] += 1
        
        result = []
        for word in words:
            prefix = ""
            score = 0
            for char in word:
                prefix += char
                score += prefix_count[prefix]
            result.append(score)
        
        return result