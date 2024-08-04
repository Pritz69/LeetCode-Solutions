class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l=[]
        for i in range(n) :
            s=nums[i]
            l.append(s)
            for j in range(i+1,n) :
                s += nums[j]
                l.append(s)
        l.sort()
        return (sum(l[left-1:right]))%(10**9 + 7)
