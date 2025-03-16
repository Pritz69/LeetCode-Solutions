class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        min_rank, max_rank = ranks[0], ranks[0]

        for rank in ranks:
            min_rank = min(min_rank, rank)
            max_rank = max(max_rank, rank)

        freq = [0] * (max_rank + 1)
        for rank in ranks:
            freq[rank] += 1

        low = 1
        high = min_rank * cars * cars

        while low < high:
            mid = (low + high) // 2
            cars_repaired = 0

            for rank in range(1, max_rank + 1):
                cars_repaired += freq[rank] * int(math.sqrt(mid // rank))

            # Adjust the search boundaries based on the number of cars repaired
            if cars_repaired >= cars:
                high = mid  # Try to find a smaller time
            else:
                low = mid + 1  # Need more time

        return low