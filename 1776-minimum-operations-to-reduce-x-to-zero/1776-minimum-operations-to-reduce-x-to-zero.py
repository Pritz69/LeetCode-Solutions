class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        s=sum(nums)
        target=s-x
        l=0
        currsum=0
        window=-1
        for r in range(len(nums)) :
            currsum += nums[r]
            while l<=r and currsum>target :
                currsum -= nums[l]
                l +=1
            if currsum==target :
                window = max(window,r-l+1)
        return -1 if window ==-1 else len(nums)-window 
            
        