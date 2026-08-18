from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        l = len(nums)
        if k == l:
            return max(nums)
        
        elif k == 1:
            ans = [items for items, count in Counter(nums).items() if count == 1]
            return -1 if not ans else max(ans)
        
        else:
            if nums[0] not in nums[1:]:
                if nums[l-1] not in nums[:l-1]:
                    return nums[0] if nums[0] > nums[l-1] else nums[l-1]
                else:
                    return nums[0]
            else:
                if nums[l-1] not in nums[:l-1]:
                    return nums[l-1]
                else:
                    return -1
            
        