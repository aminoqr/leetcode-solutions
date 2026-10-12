class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = [0] * 26
        window_map = [0] * 26
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            s1_map[ord(s1[i]) - 97] += 1
            window_map[ord(s2[i]) - 97] += 1

        if s1_map == window_map:
            return True        

        for l in range(1, len(s2) - len(s1) + 1):
            window_map[ord(s2[l + len(s1) - 1]) - 97] += 1
            window_map[ord(s2[l-1]) - 97] -= 1
            
            if s1_map == window_map:
                return True

        
        return False


        