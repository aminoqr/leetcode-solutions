class Solution:
    def isPalindrome(self, x: int) -> bool:
        og = x
        new = 0
        while(og > 0):
            new = new * 10 + og % 10
            og //= 10
        return x == new