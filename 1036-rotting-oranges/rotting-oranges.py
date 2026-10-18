from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        fresh_count = 0
        row_len = len(grid)
        col_len = len(grid[0])
        queue = deque()
        mins = -1

        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        while queue:
            new_rotten_count = len(queue)
            print(queue)

            for i in range(new_rotten_count):
                row, col = queue.popleft()
                for r, c in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                    if 0 <= r < row_len and 0 <= c < col_len and grid[r][c] == 1:
                        queue.append((r, c))
                        grid[r][c] = 2
                        fresh_count -= 1
            
            mins += 1
        
        return mins if fresh_count == 0 else -1

                
                        
        