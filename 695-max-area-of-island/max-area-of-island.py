class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxarea = 0
        
        def dfs_area(row, col):
            if not 0 <= row < rows or not 0 <= col < cols or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0

            return 1 + dfs_area(row+1, col) + dfs_area(row-1, col) + dfs_area(row, col+1) + dfs_area(row, col-1) 


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = dfs_area(row, col)
                    maxarea = max(area, maxarea)

        return maxarea
        
        