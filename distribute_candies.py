class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_candies = len(set(candyType))
        return min(unique_candies, len(candyType) // 2)
        
