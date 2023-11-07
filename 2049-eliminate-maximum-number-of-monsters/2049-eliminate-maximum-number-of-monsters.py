class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        na=[]
        for i in range(len(dist)) :
            na.append(math.ceil(dist[i]/speed[i]))
        na.sort()
        #print(na)
        if na[0]==0:
            return 1
        c=0
        for i in range(len(na)) :
            if na[i]>i :
                c +=1
            else :
                break
        return c