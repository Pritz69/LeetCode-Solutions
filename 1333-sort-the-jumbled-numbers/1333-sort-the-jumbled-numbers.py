class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        ans=[]
        for x in nums :
            nn=""
            t=x
            if t==0 :
                ans.append((x,mapping[0]))
                continue
            while t :
                d=t%10
                nn = str(mapping[d]) + nn
                t=t//10
            if nn :
                ans.append((x,int(nn)))
        ans=sorted(ans, key=lambda x:x[1])
        return [x[0] for x in ans]
