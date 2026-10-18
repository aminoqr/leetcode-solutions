from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        fresh_count = 0
        row_len = len(grid)
        col_len = len(grid[0])
        queue = deque()
        days = -1

        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        def rot_next(row, col):
            nonlocal fresh_count
            if row + 1 < row_len:
                if grid[row+1][col] == 1:
                    queue.append((row+1, col))
                    grid[row+1][col] = 2
                    fresh_count -= 1
            if row - 1 >= 0:
                if grid[row-1][col] == 1:
                    queue.append((row-1, col))
                    grid[row-1][col] = 2
                    fresh_count -= 1
            if col + 1 < col_len:
                if grid[row][col+1] == 1:
                    queue.append((row, col+1))
                    grid[row][col+1] = 2
                    fresh_count -= 1
            if col - 1 >= 0:
                if grid[row][col-1] == 1:
                    queue.append((row, col-1))
                    grid[row][col-1] = 2
                    fresh_count -= 1
        
        while queue:
            new_rotten_count = len(queue)
            print(queue)

            for i in range(new_rotten_count):
                row, col = queue.popleft()
                rot_next(row, col)
            
            days += 1
        
        return days if fresh_count == 0 else -1

                
                        
        