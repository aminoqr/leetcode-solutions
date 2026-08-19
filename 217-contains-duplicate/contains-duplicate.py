from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = {}
        for num in nums:
            if num not in res:
                res[num] = 1
            elif res[num] == 1:
                return True
            else:
                res[num] += 1
        return False