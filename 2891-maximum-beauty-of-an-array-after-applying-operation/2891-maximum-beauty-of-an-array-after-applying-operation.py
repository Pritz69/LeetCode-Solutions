class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        intervals=[]
        for x in nums :
            intervals.append((x-k,x+k))
        events = []
        for start, end in intervals:
            events.append((start, 'start'))
            events.append((end, 'end'))

        events.sort(key=lambda x: (x[0], x[1] == 'end'))
        #print(intervals)
        #print(events)
        active_intervals = 0
        max_overlap = 1

        for time, event_type in events:
            if event_type == 'start':
                active_intervals += 1
                max_overlap = max(max_overlap, active_intervals)
            else: 
                active_intervals -= 1
        
        return max_overlap