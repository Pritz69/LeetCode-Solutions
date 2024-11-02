class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[-1] != sentence[0] :
            return False
        sentence=sentence.split()
        for i in range(len(sentence)-1) :
            if sentence[i][-1]!=sentence[i+1][0] :
                return False
        return True