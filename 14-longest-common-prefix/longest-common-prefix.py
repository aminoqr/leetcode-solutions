class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        strs.sort()
        i = 0
        while i < len(strs[0]) and i < len(strs[len(strs)-1]):
            if strs[0][i] == strs[len(strs)-1][i]:
                prefix += strs[0][i]
                i+=1
            else:
                break
        return prefix
        