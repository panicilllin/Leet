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

class Solution2:
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

# 2026.10.04
# DFS
class Solution3:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        def _check_border(i, j):
            print(f"i={i};j={j};val={grid[i][j]}")
            grid[i][j] = '0'
            if j>0:
                up = grid[i][j-1]
                if up == '1':
                    _check_border(i,j-1)
            if j + 1 < n:
                down = grid[i][j+1]
                if down == '1':
                    _check_border(i,j+1)
            if i>0:
                left = grid[i-1][j]
                if left == '1':
                    _check_border(i-1,j)
            if i + 1 < m:
                right = grid[i+1][j]
                if right =='1':
                    _check_border(i+1,j)

        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == '1':
                    print(f"i={i};j={j};val={grid[i][j]}")
                    res += 1
                    _check_border(i,j)
        return res

# 2026.10.04
# BFS
from collections import deque
class Solution4:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        def _check(i,j):
            queue = deque([(i,j)])
            grid[i][j] = "0"
            while queue:
                node = queue.popleft()
                # grid[node[0]][node[1]] = "0"
                if node[0] >0 and grid[node[0]-1][node[1]] == "1":
                    grid[node[0]-1][node[1]] = "0"
                    queue.append((node[0]-1,node[1]))
                if node[1] >0 and grid[node[0]][node[1]-1] == "1":
                    grid[node[0]][node[1]-1] = "0"
                    queue.append((node[0],node[1]-1))
                if node[0] + 1 < m and grid[node[0]+1][node[1]] == "1":
                    grid[node[0]+1][node[1]] = "0"
                    queue.append((node[0]+1,node[1]))
                if node[1] +1 < n and grid[node[0]][node[1]+1] == "1":
                    grid[node[0]][node[1]+1] = "0"
                    queue.append((node[0],node[1]+1))

        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == '1':
                    res +=1
                    _check(i,j)
        return res

# 2026.10.05
# BFS
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        # BFS 优化后的写法
        def _check(i, j):
            queue = deque([(i, j)])
            grid[i][j] = "0"
            # 只要定义一个方向数组：上，下，左，右
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            while queue:
                r, c = queue.popleft()
                # 用 for 循环自动遍历四个方向
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # 边界检查 + 值检查 写在一行
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                        grid[nr][nc] = "0" # 标记为已访问
                        queue.append((nr, nc))

        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == '1':
                    res +=1
                    _check(i,j)
        return res


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
