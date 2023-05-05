class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel={'a','e','i','o','u'}
        l,c,ans=0,0,0
        f=0
        for r in range(len(s)) :
            c +=1 if s[r] in vowel else 0
            if r-l+1 > k :
                c -=1 if s[l] in vowel else 0
                l +=1
            if c==k :
                f=1
                break
            ans = max (ans,c)
        if f==1 :
            return k
        return ans
