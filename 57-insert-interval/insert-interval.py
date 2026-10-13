class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        ans = []
        
        n = len(intervals)
        for i in range(n):
            if newInterval[0] <= intervals[i][0]:
                intervals.insert(i, newInterval)
                break
        
        if len(intervals) == n:
            intervals.append(newInterval)
        
        for inter in intervals:
            if not ans or ans[-1][1] < inter[0]:
                ans.append(inter)
            else:
                if inter[1] > ans[-1][1]:
                    ans[-1][1] = inter[1]
        
        return ans

                
