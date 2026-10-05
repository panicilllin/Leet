from bisect import bisect_left
from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1 = points[0][0]
        y1 = points[0][1]
        x2 = points[1][0]
        y2 = points[1][1]
        k = (y2 - y1) / (x2 - x1)
        b = y1 - k * x1
        x3 = points[2][1]
        print(k,b)
        y3_guess = k * x3 + b
        if y3_guess == points[2][0]:
            return False
        else:
            return True


if __name__ == "__main__":
    a = Solution()
    b = a.isBoomerang(points=[[1,1],[2,3],[3,2]])
    print(b)
