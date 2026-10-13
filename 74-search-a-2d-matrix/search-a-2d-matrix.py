class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        low = 0
        high = len(matrix) * len(matrix[0]) - 1
        while low <= high:
            mid = (high + low) // 2
            midrow = mid // (len(matrix[0]))
            midcol = mid  % (len(matrix[0]))
            if matrix[midrow][midcol] < target:
                low = mid + 1
            elif matrix[midrow][midcol] > target:
                high = mid - 1
            else:
                return True
        return False 
        