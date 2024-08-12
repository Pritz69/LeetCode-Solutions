class KthLargest:
    k=0
    nums=[]
    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        self.nums.sort()
    def add(self, val: int) -> int:
        l=0
        r=len(self.nums)-1
        ans=len(self.nums)
        while l <= r :
            m=(l+r)>>1
            if self.nums[m] > val :
                ans=m
                r=m-1
            else :
                l=m+1
        self.nums.insert(ans,val)
        return self.nums[-self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)