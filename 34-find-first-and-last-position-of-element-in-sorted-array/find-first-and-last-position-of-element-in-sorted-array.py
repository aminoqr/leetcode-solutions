class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        low = 0
        high = len(nums) - 1
        split_idx = -1
        ans = []

        while low <= high:
            mid = (high + low) // 2

            if nums[mid] == target:
                split_idx = mid
                break
            
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if split_idx == -1:
            return [-1, -1]

        
        low = 0
        high = split_idx

        while low < high:
            mid = (high + low) // 2
            if nums[mid] == target:
                high = mid
            else:
                low = mid + 1
        
        ans.append(low)

        low = split_idx
        high = len(nums) - 1

        while low < high:
            mid = (high + low) // 2 + 1
            if nums[mid] == target:
                low = mid
            else:
                high = mid - 1
        
        ans.append(low)

        return ans