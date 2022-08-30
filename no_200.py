from typing import List
class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res=0
        while  True:
            have_island, grid = self.find_island(grid)
            if have_island is True:
                res += 1
            else:
                break
        return res

    def find_island(self,grid):   
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == '1':
                    # print(m,n)
                    self.scan_element([m,n],grid)
                    return True, grid
        return False, grid
        
    def scan_element(self,mark,grid):
        m=mark[0]
        n=mark[1]
        if m <0 or n <0:
            return
        elif m >= len(grid) or n >= len(grid[0]):
            return
        elif grid[m][n]=='0':
            return
        else:
            grid[m][n]='0'
            self.scan_element([m+1, n], grid)
            self.scan_element([m, n+1], grid)
            self.scan_element([m-1, n], grid)
            self.scan_element([m, n-1], grid)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res=0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == '1':
                    # print(m,n)
                    self.scan_element([m,n],grid)
                    res+=1
        return res
        
    def scan_element(self,mark,grid):
        m=mark[0]
        n=mark[1]
        if m <0 or n <0:
            return
        elif m >= len(grid) or n >= len(grid[0]):
            return
        elif grid[m][n]=='0':
            return
        else:
            grid[m][n]='0'
            self.scan_element([m+1, n], grid)
            self.scan_element([m, n+1], grid)
            self.scan_element([m-1, n], grid)
            self.scan_element([m, n-1], grid)


if __name__ == '__main__':
    a = Solution()
    b=a.numIslands(grid = [
                  ["1","1","1","1","0"],
                  ["1","1","0","1","0"],
                  ["1","1","0","0","0"],
                  ["0","0","0","0","0"]
                ])
    print(b)
    
#AC
               