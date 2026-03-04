class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 1, 1
        length = len(nums)
        while i < length:
            if nums[i] != nums[j-1]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j


        # nums[:] = sorted(set(nums)) 
        # return len(nums)
        