from typing import List

class Solution1:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        lines = [[None,None] for i in range(201)]
        for rect in rectangles:
            left = rect[0][0]
            right = rect[1][0]
            bottom = rect[0][1]
            top = rect[1][1]
            for i in range(left,right):
                if lines[i] == [None,None]:
                    lines[i] = [top,bottom]
                else:
                    lines[i] = [max(top,lines[0]),min(bottom,lines[1])]
        res = 0
        for i in lines:
            if lines != [None,None]:
                res += lines[0]-lines[1]

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        lines = []
        for rect in rectangles:
            # left = rect[0]
            # right = rect[2]
            lines.append(rect[0])
            lines.append(rect[2])
        lines.sort()
        res = 0
        for i in range(1,len(lines)):
            left, right = lines[i-1], lines[i]
            if right == left:
                continue
            lines = [(rect[1],rect[3]) \
                    for rect in rectangles if rect[0] <= left and rect[1] >= right]
            lines.sort()
            h,l,r = 0,-1,-1
            for cur in lines:
                if cur[0] > r:
                    h += r-l
                elif cur[1] > r:
                    r = cur[1]
            h += r-l
            