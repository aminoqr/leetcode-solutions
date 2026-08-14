class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        dct = {}
        for r in range(len(s)):
            if s[r] in dct:
                dct[s[r]] += 1
            else:
                dct[s[r]] = 1
            
            while dct[s[r]] > 2:
                dct[s[l]] -= 1
                l += 1
            new_ans = r - l + 1
            if new_ans > ans:
                ans = new_ans
        
        return ans
            


        