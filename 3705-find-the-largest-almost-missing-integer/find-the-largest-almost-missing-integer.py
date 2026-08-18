from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        n = len(nums)
        if k == n:
            return max(nums)
        elif k == 1:
            ans = [e for e, count in count.items() if count == 1]
            if not ans:
                return -1
            return max(ans)
        
        candidates = []
        if count[nums[0]] == 1:
            candidates.append(nums[0])
        if count[nums[n-1]] == 1:
            candidates.append(nums[n-1])
        
        return -1 if not candidates else max(candidates)

        