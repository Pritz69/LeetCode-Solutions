class Solution:
    def isPathCrossing(self, path: str) -> bool:
        p=(0,0)
        s=set()
        s.add(p)
        f=0
        for x in path :
            if x=='N' :
                a,b=p[0],p[1]
                p=(a,b+1)
                if p in s :
                    f=1
                    break
                s.add(p)
            if x=='S' :
                a,b=p[0],p[1]
                p=(a,b-1)
                if p in s :
                    f=1
                    break
                s.add(p)
            if x=='E' :
                a,b=p[0],p[1]
                p=(a+1,b)
                if p in s :
                    f=1
                    break
                s.add(p)
            if x=='W' :
                a,b=p[0],p[1]
                p=(a-1,b)
                if p in s :
                    f=1
                    break
                s.add(p)
        return f==1
        
