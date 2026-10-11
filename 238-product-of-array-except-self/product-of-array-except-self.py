class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        results = [1]
        for i in range(1, len(nums)):
            results.append(results[i-1] * nums[i-1])
        
        temp = 1
        for i in range(len(nums)-1, -1, -1):
            results[i] *= temp
            temp *= nums[i]
        
        return results

        


        