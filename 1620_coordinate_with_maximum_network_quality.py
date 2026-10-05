
import math
from typing import List


class Solution_false:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        n = 110
        g = [[0] * 110 for _ in range(110)]
        max_signal = -1
        ans = towers[0][:2]
        for (a,b,q) in towers:
            for i in range(max(0,a-radius), a+radius+1):
                for j in range(max(0,b-radius),b+radius+1):
                    g[i][j] = self.cal_quality([i,j],[a,b,q],radius)
                    if g[i][j] > max_signal:
                        max_signal = g[i][j]
                        ans = [i,j]
                    elif g[i][j] == max_signal:
                        ans = self.min_point(ans,[i,j])
        
        return ans


    def cal_quality(self,poi,tower,radius):
        dist = math.sqrt(pow(poi[0]-tower[0],2)+pow(poi[1]-tower[1],2))
        if dist > radius:
            return 0
        ans = math.floor(tower[2]/(1+dist))
        # print(ans)
        return ans
    
    def min_point(self,poi1,poi2):
        if poi1[0] < poi2[0]:
            return poi1
        elif poi1[0] == poi2[0]:
            return poi1 if poi1[1] < poi2[1] else poi2
        else:
            return poi2



class Solution:
    def bestCoordinate(self, towers: List[List[int]], k: int) -> List[int]:
        g = [[0] * 110 for _ in range(110)]
        x, y, val = 0, 0, 0
        for (a, b, q) in towers:
            for i in range(max(0, a - k), a + k + 1):
                for j in range(max(0, b - k), b + k + 1):
                    d = math.sqrt((a - i) * (a - i) + (b - j) * (b - j))
                    if d > k:
                        continue
                    g[i][j] += int(q / (1 + d))
                    if g[i][j] > val:
                        val, x, y = g[i][j], i, j
                    elif g[i][j] == val and ((i < x or (i == x and j < y))):
                        x, y = i, j
        return [x, y]


if __name__ == "__main__":
    a = Solution()
    b = a.bestCoordinate(towers = [[42,0,0]], radius = 7)
    print(b)