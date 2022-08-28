from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        res = []
        for sum in range(0, m+n):
            x1 = sum if sum < m else m-1
            y1 = sum - x1


if __name__ == "__main__":
    a = Solution()
    b = a.findDiagonalOrder(mat=[[1,2,3],[4,5,6],[7,8,9]])
    print(b)