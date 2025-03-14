class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        max_candies_in_pile = 0
        for candy in candies:
            max_candies_in_pile = max(max_candies_in_pile, candy)

        left = 0
        right = max_candies_in_pile

        while left < right:
            middle = (left + right + 1) // 2
            if self._can_allocate_candies(candies, k, middle):
                left = middle
            else:
                right = middle - 1

        return left

    def _can_allocate_candies(self, candies, k, num_of_candies):
        max_num_of_children = 0

        for pile in candies:
            max_num_of_children += pile // num_of_candies

        return max_num_of_children >= k