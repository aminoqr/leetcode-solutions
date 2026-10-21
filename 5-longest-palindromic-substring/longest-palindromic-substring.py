class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            
            return j - i - 1
        

        ans = [0, 0]

        for i in range(len(s)):
            odd_case = expand(i, i)

            if odd_case > ans[1] - ans[0] + 1:
                ans[0] = i - odd_case//2
                ans[1] = i + odd_case//2

            if i < len(s) - 1:
                even_case = expand(i, i+1)

                if even_case > ans[1] - ans[0] + 1:
                    ans[0] = i - even_case//2 + 1
                    ans[1] = i + even_case//2
        
        return s[ans[0]:ans[1]+1]

        
