class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans=[]
        nums.sort()
        #print(nums)
        for i in range(2,len(nums),3) :
            if nums[i]-nums[i-2] > k :
                return []
            nl=[nums[i-2],nums[i-1],nums[i]]
            ans.append(nl)
        return ans

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans=[]
        d={}
        for x in nums :
            d[x]=d.get(x,0)+1
        d=dict(sorted(d.items(),key=lambda x:x[0]))
        #print(d)
        nl=[]
        for x in d :
            while d[x] > 0 :
                nl.append(x)
                d[x]-=1
                if len(nl)==3 :
                    ans.append(nl)
                    nl=[] 
        for arr in ans :
            p=arr[0]
            for x in arr :
                if x - p > k :
                    return []
                p=min(p,x)
        return ans
