from typing import List


class Solution:


    def findLUSlength(self, strs: List[str]) -> int:
        ans = -1
        for i in range(0,len(strs)):
            if len(strs[i]) <= ans:
                continue
            flg = True
            for j in range(0,len(strs)):
                if i == j:
                    continue
                if self.check(strs[i],strs[j]):
                    flg = False
                    break
            if flg:
                ans = len(strs[i])
        return ans

    def check(self, s1, s2):
        lcs = self.lcs(s1, s2)
        if len(s1) == lcs:
            return True
        return False

    def lcs(self, s1: str, s2: str) -> int:
        s1 = ' ' + s1
        s2 = ' ' + s2
        f = {i: {j: None for j in range(0, len(s2))} for i in range(0, len(s1))}
        for i in range(0, len(s1)):
            f[i][0] = 1
        for j in range(0, len(s2)):
            f[0][j] = 1
        for i in range(1, len(s1)):
            for j in range(1, len(s2)):
                if s1[i] == s2[j]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])
        return f[len(s1) - 1][len(s2) - 1] - 1


if __name__ == "__main__":
    a = Solution()
    b = a.findLUSlength( ["aaa","aaa","aa"])
    print(b)
# success

