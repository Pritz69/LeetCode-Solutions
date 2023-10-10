class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length=len(nums)
        arr=sorted(set(nums))
        r=0
        ans=length #float('inf)
        for l in range(len(arr)) :
            while r < len(arr) and arr[r] < arr[l] + length :
                r +=1
            window = r-l
            ans = min(ans, length-window)
        return ans