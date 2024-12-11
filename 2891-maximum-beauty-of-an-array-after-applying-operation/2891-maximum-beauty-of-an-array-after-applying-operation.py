class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        intervals=[]
        for x in nums :
            intervals.append((x-k,x+k))
        events = []
        for start, end in intervals:
            events.append((start, 1))  
            events.append((end, -1))  
        events.sort(key=lambda x: (x[0], -x[1]))  #makes st -1 and end +1 , so -1 < +1 and st gets prioritized
        active_intervals = 0
        max_overlap = 1
        for time, value in events:
            active_intervals += value 
            max_overlap = max(max_overlap, active_intervals)
        return max_overlap