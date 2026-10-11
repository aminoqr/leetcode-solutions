class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = "".join([char for char in s if char.isalnum()]).lower()
        return new_string == new_string[::-1]
        