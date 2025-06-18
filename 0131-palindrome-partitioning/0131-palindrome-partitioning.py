class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalin(st,ed) :
            while st<=ed :
                if s[st] != s[ed] :
                    return False
                st +=1
                ed -=1
            return True
        def rec(i,l) :
            if i==len(s) :
                ans.append(l.copy())
                return
            for ind in range(i,len(s)):
                if ispalin(i,ind) :
                    l.append(s[i:ind+1])
                    rec(ind+1,l)
                    l.pop()
        ans=[]
        rec(0,[])
        return ans        
            