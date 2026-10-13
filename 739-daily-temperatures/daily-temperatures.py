class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            if not stack or stack[-1][0] >= temp:
                stack.append([temp, i])
            else:
                while stack and stack[-1][0] < temp:
                    ans[stack[-1][1]] = i  - stack[-1][1]
                    stack.pop()
                stack.append([temp, i])
        
        return ans
                