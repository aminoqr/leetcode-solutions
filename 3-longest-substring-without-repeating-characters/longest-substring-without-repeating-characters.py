class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        longest = 0
        l = 0
        
        for r in range(len(s)):
            while s[r] in sett:
                sett.discard(s[l])
                l += 1
            
            sett.add(s[r])
            length = r - l + 1
            longest = max(length, longest)
            
        
        return longest


        