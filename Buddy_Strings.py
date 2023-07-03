class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal) :
            return False
        if s==goal :
            c={}
            for x in s :
                c[x] = c.get(x,0) +1
                if c[x]==2 :
                    return True
            return False
        l,r=-1,-1
        for i in range(len(s)) :
            if s[i] != goal[i] :
                if l==-1 :
                    l=i
                elif r==-1 :
                    r=i
                else :
                    return False
        if r==-1 :
            return False
        if s[l]==goal[r] and s[r]==goal[l] :
            return True
