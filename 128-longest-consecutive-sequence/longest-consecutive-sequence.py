class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        best = 0
        for num in nums:
            if num - 1 not in nums:
                upper = num + 1
                while upper in nums:
                    upper += 1
                
                best = max(best, upper - num)
        
        return best
        