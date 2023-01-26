class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0 #for storing the max final result (The Answer)
        sum = 0 #for calculating the sum of each subsequence
        h = []  #heapq for storing the elements from nums1 in a sorted manner, so that we can remove the smallest value in a single step and append to it the next element and hence make modifications to the sum variable along with it. 
        for max2,n1 in sorted(zip(nums2,nums1), reverse=True) :#Merge the two arrays and sort it in decreasing order based on the values of nums2, as we would like to multiply the subsequence sum with the max value from nums2 to get the max possible result.
            if len(h)==k : #if the heap is already filled then remove the smallest element out of it, and add a element to get the max result. The sum is also reduced along the process , coz we are excluding the the value from the subsequence. 
                sum -= heapq.heappop(h)
            sum += n1
            heapq.heappush(h,n1) #Add the next element from nums1 to the sum to form the new subsequence , also push it into the heap to maintain the track of the subsequence wwe are using.
            if len(h)==k :
                res = max(res,sum*max2) #Finally calculate the result by multiplying the sum and the largest element of nums2 from that subsequence and as we have sorted it in decreasing order, we will get the max result.We will continue this process for every subsequence possible.
        return res
