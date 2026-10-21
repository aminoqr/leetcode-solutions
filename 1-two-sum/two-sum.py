class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for i, num in enumerate(nums):
            if target - num in num_map:
                return [i, num_map[target - num]]
            num_map[num] = i
        
