class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        p=0
        x=0
        o=0
        l=[]
        for i in range(len(pref)) :
            p=pref[i]
            x=o^p
            l.append(x)
            o=o^x
        return l

