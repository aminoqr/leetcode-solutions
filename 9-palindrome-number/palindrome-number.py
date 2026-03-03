class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        first_half = x
        second_half = 0
        while(second_half < first_half):
            second_half = second_half * 10 + first_half % 10
            first_half //= 10
        return first_half == second_half or first_half == second_half // 10