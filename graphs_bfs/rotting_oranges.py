# https://leetcode.com/problems/rotting-oranges/
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        orange_queue = deque()

        mins = 0
        for row_i in range(len(grid)):
            for orange_i in range(len(grid[row_i])):
                if grid[row_i][orange_i] == 2:
                    orange_queue.append((row_i, orange_i, 0))

        max_row_index = len(grid)
        max_orange_index = len(grid[0])

        while orange_queue:
            orange = orange_queue.popleft()
            row_index = orange[0]
            orange_index = orange[1]
            mins = max(mins, orange[2])

            if row_index - 1 >= 0 and grid[row_index - 1][orange_index] == 1:
                grid[row_index - 1][orange_index] = 2
                orange_queue.append((row_index - 1, orange_index, mins + 1))
                
            if row_index + 1 < max_row_index and grid[row_index + 1][orange_index] == 1:
                grid[row_index + 1][orange_index] = 2
                orange_queue.append((row_index + 1, orange_index, mins + 1))
                
            if orange_index - 1 >= 0 and grid[row_index][orange_index - 1] == 1:
                grid[row_index][orange_index - 1] = 2
                orange_queue.append((row_index, orange_index - 1, mins + 1))
                
            if orange_index + 1 < max_orange_index and grid[row_index][orange_index + 1] == 1:
                grid[row_index][orange_index + 1] = 2
                orange_queue.append((row_index, orange_index + 1, mins + 1))
        
            
        for row_i in range(len(grid)):
            for orange_i in range(len(grid[row_i])):
                if grid[row_i][orange_i] == 1:
                    return -1
        return mins
        
