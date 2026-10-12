class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        longest = 0
        l = 0
        n = len(s)

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            length = r - l + 1
            longest = max(length, longest)
            sett.add(s[r])

        return longest
                    


        