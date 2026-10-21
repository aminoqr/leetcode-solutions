class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (high + low) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        
        split_idx = low

        if target >= nums[split_idx] and target <= nums[len(nums) - 1]:
            high = len(nums) - 1
        else:
            low = 0
            high = split_idx - 1
        
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
            


