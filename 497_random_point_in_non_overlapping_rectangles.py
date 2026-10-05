from typing import List
import random


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.points = []
        self.pick_num = 0
        for rect in rects:
            for i in range(rect[0], rect[2]+1):
                for j in range(rect[1], rect[3]+1):
                    self.points.append([i, j])

    def pick(self) -> List[int]:
        self.pick_num += 1
        return self.points[self.pick_num]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
