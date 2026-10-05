import copy
from typing import List
class Solution1:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        heights = [['p']+i+['a'] for i in heights]
        heights = [['p' for i in range(n+2)]] + heights + [['a' for i in range(n+2)]] 
        print(heights)
        while True:
            flg=False
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if heights[i][j]in ['p','a','r']:
                        continue
                    elif heights[i][j] == 0: 
                        heights[i][j] = self.check_sea(i,j,heights)
                    else:
                        flg=True
                        heights[i][j] -= 1
                        if heights[i][j] == 0:
                            heights[i][j] = self.check_sea(i,j,heights)
            # print(heights)
            if flg == False:
                break
        heights = heights[1:-1]
        heights = [i[1:-1] for i in heights]
        print(heights)
        res=[]
        for i in range(n):
            for j in range(n):
                if heights[i][j] == 'r':
                    res.append([i,j])
                    
        return res
    
    def check_sea(self, i, j, heights):
        a = heights[i][j-1]
        b = heights[i-1][j]
        c = heights[i][j+1]
        d = heights[i+1][j]
        if 'r' in [a,b,c,d]:
            return 'r'
        elif 'p' in [a,b,c,d] and 'a' in [a,b,c,d]:
            return 'r'
        elif 'p' in [a,b,c,d]:
            return 'p'
        elif 'a' in [a,b,c,d]:
            return 'a'
        else:
            return 0
        
        
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        
        heights = [['p']+i+['a'] for i in heights]
        heights = [['p' for i in range(n+2)]] + heights + [['a' for i in range(n+2)]] 
        print(heights)
        # cal pacific
        flow = copy.deepcopy(heights)
        for i in range(0,m):
            for j in range(0,n):
                pass
    
    def flow(self, i,j,heights,ocean,flow):
        a = heights[i][j-1]
        b = heights[i-1][j]
        c = heights[i][j+1]
        d = heights[i+1][j]
        if heights[i][j] > heights[i][j-1]:
            heights[i][j-1] == heights[i][j]
            
        
        
if __name__ == '__main__':
    a = Solution()
    b=a.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
    print(b)
                        