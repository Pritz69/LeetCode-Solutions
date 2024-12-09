class Solution:
    def isArraySpecial(self, nums: List[int], Q: List[List[int]]) -> List[bool]:
        arr = [0] * (len(nums)-1)
        for i in range(1,len(nums)):
            if nums[i] % 2 == nums[i-1] % 2:
                arr[i-1] = 0
            else:
                arr[i-1] = 1
                
        preSum = [1]
        for v in arr:
            preSum.append(preSum[-1] + v)
        #print(arr,preSum)
        res = []
        for s,e in Q:
            if preSum[e] - preSum[s] == e-s:
                res.append(True)
            else:
                res.append(False)
        return res