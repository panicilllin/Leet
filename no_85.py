from typing import List
class Solution:
    def __init__(self):
        self.max_1 = 0
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        for i in range(0,len(matrix[0])):
            for j in range(0,len(matrix)):

