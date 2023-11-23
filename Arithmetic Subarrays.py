class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            le, ri = l[i], r[i]
            arr = nums[le:ri+1]
            arr.sort()
            diff = arr[1] - arr[0]
            f=0
            for i in range(1, len(arr)):
                if arr[i] - arr[i-1] != diff:
                    f=1
                    break
            ans.append(f==0)
        return ans
