from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        num_dct = defaultdict(int)
        ans = []
        for num in nums:
            if target - num in num_dct:
                return [i, num_dct[target-num]]
            num_dct[num] = i
            i += 1
            

        