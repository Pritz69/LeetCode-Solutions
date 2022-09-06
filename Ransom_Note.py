from  collections import Counter 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_c=Counter(magazine)
        ran_c=Counter(ransomNote)
        for c in ran_c :
            if c not in mag_c or mag_c[c] < ran_c[c] :
                return False 
        return True
