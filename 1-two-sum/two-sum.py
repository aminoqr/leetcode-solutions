class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dct = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dct:
                return [num_dct[complement], i]
            num_dct[num] = i 

        