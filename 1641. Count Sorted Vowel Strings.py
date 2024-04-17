class Solution:
    def countVowelStrings(self, n: int) -> int:
        memo = {}

        def rec(last_vowel, length):
            if length == n:
                return 1
            if (last_vowel, length) in memo:
                return memo[(last_vowel, length)]
            count = 0
            for vowel in ['a', 'e', 'i', 'o', 'u']:
                if vowel >= last_vowel:
                    count += rec(vowel, length + 1)
            memo[(last_vowel, length)] = count
            return count

        return rec('', 0)
