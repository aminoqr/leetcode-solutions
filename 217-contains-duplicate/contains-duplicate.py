from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for count in counts.values():
            if count != 1:
                return True
        return False