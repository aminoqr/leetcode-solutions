class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        n = len(nums)
        while left < right:
            mid = (right + left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        min_idx = left
        if min_idx == 0:
            left = 0
            right = n - 1
        elif target >= nums[0] and target <= nums[min_idx - 1]:
            left = 0
            right = min_idx - 1
        else:
            left = min_idx
            right = n - 1
        
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        
        return -1


        