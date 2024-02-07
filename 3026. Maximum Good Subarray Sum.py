class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d={}
        n=len(nums)
        ps=[0]*n
        ps[0]=nums[0]
        m=float('-inf')
        for i in range(1,n) :
            ps[i]=ps[i-1]+nums[i]
        for j,val in enumerate(nums) :
            if val in d :
                if d[val]==0 : #for tc: [3,3,2] ,k=1
                    if ps[j-1] < 0 :
                        d[val]=j
                elif ps[j-1] < ps[d[val]-1] : #keep the min value so that while it gets subtracted,neg value gets minimised.
                    d[val]=j
            else :
                d[val]=j
            tar1=val + k
            tar2=val - k
            if tar1 in d :
                if d[tar1]==0 : #for tc : [-1,-2,-3,-4],k=2
                    m=max(m,ps[j]-0)
                else :
                    m=max(m,ps[j]-ps[d[tar1]-1])
            if tar2 in d :
                if d[tar2]==0 : #for tc : [-1,-2,-3,-4],k=2
                    m=max(m,ps[j]-0)
                else :
                    m=max(m,ps[j]-ps[d[tar2]-1])  
            #print(d)
        return 0 if m==float('-inf') else m
