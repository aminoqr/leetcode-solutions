class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_map = {}

        for character in s:
            if character in frequency_map:
                frequency_map[character] += 1
            else:
                frequency_map[character] = 1
        
        for character in t:
            if character not in frequency_map:
                return False
            elif frequency_map[character] == 1:
                del frequency_map[character]
            else:
                frequency_map[character] -= 1
        
        return frequency_map == {}

        