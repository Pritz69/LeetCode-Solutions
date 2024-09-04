class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        di=[[0,1],[1,0],[0,-1],[-1,0]]
        d=0
        x,y=0,0
        ans=0
        obst={ tuple(l) for l in obstacles}
        for c in commands :
            if c==-1 :
                d=(d+1)%4
            elif c==-2 :
                d=(d-1)%4
            else :
                dx,dy=di[d]
                for i in range(c) :
                    if (x+dx,y+dy) in obst :
                        break
                    x=x+dx
                    y=y+dy
            ans=max(ans,x**2 + y**2)
        return ans
