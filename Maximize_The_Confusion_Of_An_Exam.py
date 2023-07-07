class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l,r,ans=0,0,0
        ct,cf=0,0
        while r < len(answerKey) :
            if answerKey[r]=='F' :
                cf +=1
            else :
                ct +=1
            while (min(cf,ct) >k) :
                if answerKey[l]=='F' :
                    cf -=1
                else :
                    ct -=1
                l +=1
            ans = max(ans,(cf+ct))
            r +=1
        return ans
