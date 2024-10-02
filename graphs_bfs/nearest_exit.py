# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]
        cells = [(entrance, 0)]
        maze[entrance[0]][entrance[1]] = "+"
        while(cells):
            cell_tup = cells.pop(0)
            cell = cell_tup[0]
            cell_row = cell[0]
            cell_column = cell[1]
            distance = cell_tup[1]

            for row, col in directions:
                cell_row1 = cell_row + row
                cell_col1 = cell_column + col
                
                if cell_row1 < 0 or cell_row1 >= rows or cell_col1 < 0 or cell_col1 >= cols:
                    continue
                
                if maze[cell_row1][cell_col1] == ".":
                    if (cell_row1 == 0 or cell_row1 == rows - 1 or cell_col1 == 0 or cell_col1 == cols - 1):
                        return distance + 1
                    else:
                        maze[cell_row1][cell_col1] = "+"
                        cells.append(([cell_row1, cell_col1], distance + 1))
        return -1
    
