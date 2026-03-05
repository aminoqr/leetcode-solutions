class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        i, j = 0, 0
        while j < length:
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return i