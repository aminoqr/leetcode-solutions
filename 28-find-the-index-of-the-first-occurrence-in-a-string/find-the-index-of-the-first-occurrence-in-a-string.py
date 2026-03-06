class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or not needle or needle not in haystack:
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                start = i
                j = 0
                while j < len(needle):
                    if haystack[i + j] != needle[j]:
                        break
                    j += 1
                if j == len(needle):
                    return start

        