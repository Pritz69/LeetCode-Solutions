class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i,x in enumerate(word) :
            if x==ch :
                word=word[:i+1][::-1] + word[i+1:]
                break
        return word
