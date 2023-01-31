class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        start_row = start_col = 0
        rows = len(matrix)
        cols = len(matrix[0])
        
        res = []
        
        while start_row < rows or start_col < cols:
            #right
            if start_row < rows : res.extend([matrix[start_row][i] for i in range(start_col, cols)])
            start_row += 1
            
            #down
            if start_col < cols : res.extend([matrix[i][cols-1] for i in range(start_row, rows)])
            cols -= 1

            #left
            if start_row < rows : res.extend([matrix[rows-1][i] for i in range(cols-1, start_col-1, -1)])
            rows -= 1
            
            #right
            if start_col < cols : res.extend([matrix[i][start_col] for i in range(rows-1, start_row-1, -1)])
            start_col += 1
            
        return res
                