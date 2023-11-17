from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
            
        m = len(matrix)
        n = len(matrix[0])
        
        rows=[]
        cols=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        
        for i in rows:
            matrix[i] = [0]*n
        for j in cols:
            for row in matrix:
                row[j] = 0
 
 # AC
                    
    
    