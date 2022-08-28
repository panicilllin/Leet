import math
from typing import List


class Solution1:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        if n < 3:
            return []
        res = [[0 for i in range(n - 2)] for j in range(n - 2)]
        print(res)
        for i in range(2, n):
            for j in range(2, n):
                print(i, j)
                sub_gird = [max(row[j - 2:j + 1]) for row in grid[i - 2:i + 1]]
                print(f"sub_g={sub_gird}")
                max_subg = 0
                for max_row in sub_gird:
                    max_subg = max(max_subg, max_row)
                print(max_subg)
                res[i - 2][j - 2] = max_subg
        return res


class Solution2:
    def edgeScore(self, edges: List[int]) -> int:
        edge_map = [0 for i in range(len(edges))]
        for from_point, to_point in enumerate(edges):
            edge_map[to_point] += from_point
        max_edge = max(edge_map)
        for i, sum_point in enumerate(edge_map):
            if sum_point == max_edge:
                return i


class Solution3:
    def smallestNumber(self, pattern: str) -> str:

        res_l = [1, 2, 3, 4, 5, 6, 7, 8, 9][:len(pattern) + 1]
        last_d = None
        for i, move in enumerate(pattern):
            if move == 'I':
                last_d = None
            elif last_d is None:
                last_d = i
                for j in range(last_d, i + 1):
                    res_l[j] += 1
                res_l[i + 1] = res_l[i] - 1
            else:
                for j in range(last_d, i + 1):
                    res_l[j] += 1
                res_l[i + 1] = res_l[i] - 1
            print(i, move, res_l[:i + 1])

        res = ''
        for i in res_l:
            res += i
        return res


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        if n <=10:
            return 0
        s=str(n)
        non_uniq=0
        for i in s:
            pass




if __name__ == "__main__":
    a = Solution3()
    b = a.smallestNumber(pattern="IIIDIDDD")
    print(b)
