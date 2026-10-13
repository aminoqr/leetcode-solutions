class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ans = []
        for inter in intervals:
            if not ans:
                ans.append(inter)
            else:
                if inter[0] <= ans[-1][1]:
                    if inter[1] > ans[-1][1]:
                        ans[-1][1] = inter[1]
                else:
                    ans.append(inter)
                    
        
        return ans
        