class Solution:
    def bestClosingTime(self, customers: str) -> int:
        l=[]
        m=float('-inf') # m=0
        s=0
        for i,x in enumerate(customers) :
            if x=='Y':
                s +=1
            else :
                s -=1
            if s>m and s>0:
                m=s
                l.append(i)
        #print(l)
        if len(l)>=1:
            return l[-1]+1
        else :
            return 0
