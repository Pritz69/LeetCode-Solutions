class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern) != len(words) :
            return False
        wordtochar={}
        chartoword={}
        for c,w in zip(pattern,words) :
            if c in chartoword and chartoword[c] !=w :
                return False
            if w in wordtochar and wordtochar[w] !=c :
                return False
            wordtochar[w] =c
            chartoword[c] =w
        return True
