from typing import List

class Solution0:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        path_map = [[None for i in range(m)] for j in range(n)]
        for i in range(m):
            path_map[0][i] = 1
        for j in range(n):
            path_map[j][0] = 1

        for i in range(n):
            for j in range(m):
                if path_map[i][j] != None:
                    continue
                path_map[i][j] = path_map[i-1][j] + path_map[i][j-1]
        print(path_map)
        return path_map[-1][-1]


if __name__ == "__main__":
    a = Solution()
    b = a.uniquePaths( m = 3, n = 7)
    print(b)

# AC