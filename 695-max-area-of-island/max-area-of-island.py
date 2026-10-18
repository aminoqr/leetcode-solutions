class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        max_area = 0

        def dfs(row, col):
            if not 0 <= row < row_len or not 0 <= col < col_len or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0

            return 1 + dfs(row+1, col) + dfs(row - 1, col) + dfs(row, col+1) + dfs(row, col-1)

        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 1:
                    max_area = max(dfs(row, col), max_area)
        
        return max_area
        
        