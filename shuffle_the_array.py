class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=[]
        ll=0
        rr=n
        while ll<n and rr<(2*n):
            l.append(nums[ll])
            l.append(nums[rr])
            ll +=1
            rr +=1 
        return l
