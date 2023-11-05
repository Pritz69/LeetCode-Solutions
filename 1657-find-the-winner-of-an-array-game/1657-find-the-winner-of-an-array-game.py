class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        curr_winner = arr[0]
        win_count = 0

        for i in range(1, len(arr)):
            if curr_winner > arr[i]:
                win_count += 1
            else:
                curr_winner = arr[i]
                win_count = 1

            if win_count == k:
                return curr_winner
        
        return curr_winner