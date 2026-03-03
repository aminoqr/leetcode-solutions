class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_num = str(x)
        return str(x) == str(x)[::-1]
        