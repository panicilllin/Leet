from typing import List


class Solution1:
    def commonFactors(self, a: int, b: int) -> int:
        min_num = min(a, b)
        res = 0
        for i in range(1, min_num + 1):
            if a % i == 0 and b % i == 0:
                res += 1
        return res


class Solution2:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)
        if m < 3 or n < 3:
            return 0

        res = 0
        for i in [1, m - 2]:
            for j in [1, n - 2]:
                mid = [i, j]
                sum_hg = self.cal_sum(grid, mid)
                print(sum_hg)
                res = max(res, sum_hg)
        return res

    def cal_sum(self, grid, mid):
        res = 0
        print(mid)
        for i in grid[mid[1] - 1][mid[0] - 1:mid[0] + 2]:
            res += i
        res += grid[mid[1]][mid[0]]
        for j in grid[mid[1] + 1][mid[0] - 1:mid[0] + 2]:
            res += j
        return res


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        res1 = num1
        res2 = num1
        sb_n2 = self.cal_num1(num2)
        res = []
        while res1!=None or res2!=None:
            if self.cal_num1(res1) == sb_n2:
                res.append(res1)
                res1 = None
            elif self.cal_num1(res2) == sb_n2:
                res.append(res2)
                res2 = None
            if res1 != None:
                res1 += 1
            if res2 == 0:
                res2 = None
            if res2 != None:
                res2 -= 1
        print(res)
        min_xor=res[0]^num1
        ans=res[0]
        if len(res) == 1:
            return ans

        for r in res[1:]:
            if r^num1 < min_xor:
                min_xor = r^num1
                ans = r
        return ans


    def cal_num1(self, num):
        if num == None:
            return -1
        return bin(num).count('1')


if __name__ == '__main__':
    a = Solution()
    b = a.minimizeXor(59,27)
    print(b)
