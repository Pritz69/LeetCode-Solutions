class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res= 0
        cursum= 0
        prefixsums= {0:1}
        for n in nums :
            cursum += n
            diff = cursum-k
            res += prefixsums.get(diff,0)
            prefixsums[cursum] = 1 + prefixsums.get(cursum,0)
        return res
