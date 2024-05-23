class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ans=[]
        def rec(i,l) :
            if i==n :
                ans.append(l)
                return
            rec(i+1,l+[nums[i]])
            rec(i+1,l)
        rec(0,[])
        c=0
        for x in ans :
            if x : 
                    x=set(x)
                    f=0
                    for el in x :
                        if el+k in x or el-k in x :
                            f=1
                            break
                    if f==0 :
                        c +=1
        return c
