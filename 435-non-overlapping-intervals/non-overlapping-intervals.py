class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        
        selected = []
        last_time = float("-inf")  
        for interval in intervals:
            start, end = interval[0], interval[1]
            if start >= last_time:
                selected.append([start, end])  
                last_time = end  
        
        return len(intervals) - len(selected)
