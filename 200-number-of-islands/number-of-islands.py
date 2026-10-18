class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        col_len = len(grid[0])
        row_len = len(grid)
        def dfs(row, col):
            if not 0 <= col < col_len or not 0 <= row < row_len or grid[row][col] == "0":
                return 
            grid[row][col] = "0"
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == "1":
                    counter += 1
                    dfs(row, col)
        return counter
        