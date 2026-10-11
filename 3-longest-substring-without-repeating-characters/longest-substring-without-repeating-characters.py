class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_freq = set()
        n = len(s)
        max_len = 1
        if n < 2:
            return n
        start = 0
        end = 1

        letter_freq.add(s[0])
        while end < n:
            if s[end] not in letter_freq:
                letter_freq.add(s[end])
                max_len = max(len(letter_freq), max_len)
                end += 1
            
            else:
                while s[end] in letter_freq:
                    letter_freq.discard(s[start])
                    start += 1
        
        return max_len
                    


        