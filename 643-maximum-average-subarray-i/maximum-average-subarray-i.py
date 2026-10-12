class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = 0
        for i in range(k):
            max_sum += nums[i]
        cur_sum = max_sum
        for l in range(1, len(nums) - k + 1):
            cur_sum = cur_sum - nums[l-1] + nums[l + k - 1]
            max_sum = max(max_sum, cur_sum)
        
        return (max_sum/k)
        