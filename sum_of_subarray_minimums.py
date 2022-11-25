#Not Understood
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        stack, sums = [], [0] * len(arr)

        for i,n in enumerate(arr):
            while stack and arr[stack[-1]] > n:
                stack.pop()
            j = stack[-1] if stack else -1
            
            sums[i] = sums[j] + (i-j)*n
            stack.append(i)
        
        return sum(sums) % (1_000_000_007)
