import copy
from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        lengths = {}
        points = [[p1,p2],[p1,p3],[p1,p4],[p2,p3],[p2,p4],[p3,p4]]
        for point in points:
            leg = (point[0][0]-point[1][0])*(point[0][0]-point[1][0]) + (point[0][1]-point[1][1])*(point[0][1]-point[1][1])
            if lengths.get(leg):
                lengths[leg].append(point)
            else:
                lengths[leg] = [point]
        # print(lengths)
        if len(lengths)!=2:
            return False
        keys = lengths.keys()
        maxkey = max(keys)
        minkey = min(keys)
        if len(lengths[maxkey]) == 2 and len(lengths[minkey]) == 4:
            return True
        return False

if __name__ == "__main__":
    a = Solution()
    b = a.validSquare( p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1])
    print(b)

# AC
