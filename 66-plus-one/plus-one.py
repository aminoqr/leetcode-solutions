class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        for i in digits:
            res = res * 10 + int(i)
        return [int(i) for i in list(str(res + 1))]