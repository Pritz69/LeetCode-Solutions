class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        loc=[]
        unl=[]
        if len(s)%2==1 :
            return False
        for i in range(len(s)) :
            if locked[i]=="0":
                unl.append(i)
            elif s[i]=='(' :
                loc.append(i)
            else :
                if loc :
                    loc.pop()
                elif unl :
                    unl.pop()
                else :
                    return False
        while loc and unl and loc[-1] < unl[-1] :
            loc.pop()
            unl.pop()
        return loc==[]