class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d=defaultdict(int)
        for x in nums :
            d[x] +=1
            if len(d) <=2 :
                continue
            nd=defaultdict(int)
            for x in d :
                if d[x] > 1 :
                    nd[x] = d[x] - 1
            d=nd
        ans=[]
        for x in d :    
            if nums.count(x) > len(nums)//3 :
                ans.append(x)
        return ans