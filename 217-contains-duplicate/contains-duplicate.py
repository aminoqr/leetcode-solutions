from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for num in nums:
            if num in res:
                return True
            else:
                res.add(num)
        
        return False