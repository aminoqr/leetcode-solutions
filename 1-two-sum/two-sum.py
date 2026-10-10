class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for i, num in enumerate(nums):
            if target - num in num_map:
                return [num_map[target - num], i]
            elif num not in num_map:
                num_map[num] = i