class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        dict=defaultdict(int)
        i=0
        count=res=0
        for j in range(len(nums)):
            count+=dict[nums[j]]
            dict[nums[j]]+=1
            # if count exceeds or equlas to k, we start decrementing frequency from 
            # ith index and decrementing all pairs formed using that index
            while count>=k:
                dict[nums[i]]-=1
                count-=dict[nums[i]]
                i+=1
            res+=i
        return res
