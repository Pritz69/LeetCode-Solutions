class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_set = set(days)
        T = [0] * 366
        
        for i in range(1, days[-1] + 1):
            if i not in days_set:
                T[i] = T[i - 1]
            else:
                T[i] =  min(T[i - 1] + costs[0],
                           T[max(i - 7, 0)] + costs[1],
                           T[max(i - 30, 0)] + costs[2])
        return T[days[-1]]