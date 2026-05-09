class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        strs.sort()
        i = 0
        last_i = len(strs) - 1
        while i < len(strs[0]) and i < len(strs[last_i]):
            if strs[0][i] == strs[last_i][i]:
                prefix += strs[0][i]
                i+=1
            else:
                break
        return prefix
        