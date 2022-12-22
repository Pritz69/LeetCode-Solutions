class Solution:
    def isPerfectSquare(self, num):
        left = 0
        right = num
        
        while left <= right:
            mid = left + (right-left)//2
            if  mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid -1
            else:
                left = mid +1
        return False
