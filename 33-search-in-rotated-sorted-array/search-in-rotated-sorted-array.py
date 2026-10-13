class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (high + low) // 2
            if nums[mid] > nums[high]:
                low = mid+1
            else:
                high = mid
        
        split_idx = low
        
        if target >= nums[split_idx] and target <= nums[len(nums) - 1]:
            low = split_idx
            high = len(nums) - 1
        
        else:
            low = 0
            high = split_idx - 1
        print(high)
        print(low)
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        
        return -1


