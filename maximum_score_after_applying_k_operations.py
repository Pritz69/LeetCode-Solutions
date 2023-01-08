class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0 
        pq = [-x for x in nums]
        heapify(pq)
        for _ in range(k): 
            ans -= pq[0] 
            heapreplace(pq,pq[0]//3)
        return ans  
        
