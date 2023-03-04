class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        answer = []
        left_sum = 0
        right_sum = 0

        total_sum = sum(nums)
        
        for i in nums:
            right_sum = total_sum - i
            answer.append(abs(right_sum - left_sum))
            left_sum += i
            total_sum -= i

        return answer
            
