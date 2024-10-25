class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        s=set()
        for x in folder :
            f=0
            for i in range(len(x)) :
                if i+1<len(x) and x[i+1]=='/' and x[:i+1] in s :
                    f=1
            if f==0 :
                s.add(x)
        return list(s)