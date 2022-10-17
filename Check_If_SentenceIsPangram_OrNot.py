class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s='abcdefghijklmnopqrstuvwxyz'
        for i in s:
            if i not in sentence:
                return False
        return True
