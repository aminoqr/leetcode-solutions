class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            result = numbers[left] + numbers[right]
            if result > target:
                right -= 1
            elif result < target:
                left += 1
            else:
                return [left+1, right+1]
        
        return []
        