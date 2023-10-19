class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ns,nt=[],[]
        for i in s :
            if i=='#' :
                if ns :
                    ns.pop()
                continue
            ns.append(i)
        for i in t :
            if i=='#' :
                if nt :
                    nt.pop()
                continue
            nt.append(i)
        #print(ns,nt)
        return ns==nt