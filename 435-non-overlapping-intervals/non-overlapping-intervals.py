class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        n = len(intervals)
        if n == 1:
            return 0
        counter = 0
        i = 1
        
        while i < len(intervals):
            if intervals[i][0] < intervals[i-1][1]:
                intervals.pop(i)
                counter += 1
            else:
                i+=1

        return counter

            

        