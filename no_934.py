import copy

from typing import List


class Solution:

    def find_first_island(self,grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(m):  # search by row
            for j in range(n):  # search by col
                if grid[i][j] == 1:
                    return [i,j]


    def shortestBridge(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # for i in grid:
        #     print(i)
        
        # infect first island
        edges=[]         
        def infect(coordinate):
            def change(row,col):
                if grid[row][col] == 1:
                    grid[row][col] = 2
                    infect([row,col])
                elif grid[row][col] == 0 and [row,col] not in edges: 
                    edges.append([row,col])
        
        
            i,j=coordinate[0],coordinate[1]
            grid[i][j]=2
                        
            if i != 0:
                change(i-1,j)
            if i != m-1:
                change(i+1,j)
            if j != 0:
                change(i,j-1)
            if j != m-1:
                change(i,j+1)
                
        first_island=self.find_first_island(grid)
        infect(first_island)
        
        # print()
        # for i in grid:
        #     print(i)
        # print()
        # edges.sort()
        # print(edges)
        
        def infect_sea(coordinate, edge_new):
            i,j=coordinate[0],coordinate[1]
            grid[i][j]=2
            
            def change(row,col):
                if grid[row][col] == 1:
                   return True
                elif grid[row][col] == 0:
                    if [row,col] not in edge_new:
                        edge_new.append([row,col])
                    return 0
                else:
                    return 0
            
            res1=res2=res3=res4
            if i != 0:
                res1 = change(i-1,j)
            if i != m-1:
                res2=change(i+1,j)
            if j != 0:
                res3=change(i,j-1)
            if j != m-1:
                res4=change(i,j+1)
            if True in [res1,res2,res3,res4]:
                return True
            else:
                return 0
        edge_new = copy.deepcopy(edges)
        
        ans=0
        while True:
            ans += 1
            edges = copy.deepcopy(edge_new)
            edge_new = []
            for coordinate in edges:
                res = infect_sea(coordinate, edge_new)
                if res == True:
                    return ans
            
            
        
                    
if __name__ == "__main__":
    a = Solution()
    b = a.shortestBridge(grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]])
    print(b)
# AC