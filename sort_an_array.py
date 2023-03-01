class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # This function recursively splits the list in half until
        # it is only one element, because one element is always sorted.
        # Then call the merge function to combine the split lists back 
        # together by pairs in sorted order.
        def merge_sort(nums):
            if len(nums) <= 1: 
                return nums
            
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            return merge(left, right)
        
        # Merges two lists together in order by iterating through each
        # and checking which number is smaller until the end of one or both
        # of the lists. Then add all the remaining elements because they
        # have already been sorted. Return the combined sorted list.
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
