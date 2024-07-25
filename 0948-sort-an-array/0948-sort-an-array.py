class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge_sort(nums):
            if len(nums) <= 1: 
                return nums
            
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            return merge(left, right)
        
        def merge(left, right):
            combined = []
            i, j = 0, 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    combined.append(left[i])
                    i += 1
                else:
                    combined.append(right[j])
                    j += 1
                    
            combined += left[i:]
            combined += right[j:]
            return combined
        
        return merge_sort(nums)  


        

