class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_products = []
        right_products = [1] * len(nums)
        result = []

        temp = 1
        for num in nums:
            temp *= num
            left_products.append(temp)
        
        temp = 1
        index = len(nums) - 1
        while index >= 0:
            temp *= nums[index]
            right_products[index] = temp
            index -=1
        
        for i in range(len(nums)):
            l_product = left_products[i-1] if i - 1 >= 0 else 1
            r_product = right_products[i+1] if i + 1 < len(nums) else 1
            result.append(l_product * r_product)
        
        return result
        


        