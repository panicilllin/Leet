from itertools import product
from typing import List

# 6131
"""
Tips1：假设一种情况，当前这个数字子序列可以再变长一位的充要条件是什么？
答案是后面必须都要有从1到k的数字，缺一不可。

Tips2：可以证明在打包序列中重复的数字是没有意义的，因为里面总是会缺少你需要的序列。那么在Tips1的情况下，从后往前遍历，将从1到k的数字第一遍出现进行打包，每有一组打包，ans就+1，如此往复。

"""
class Solution1:
    def __init__(self):
        self.k_map = []

    def shortestSequence(self, rolls: List[int], k: int) -> int:
        # i 位子序列
        k_list = [i for i in range(k+1)][1:]
        for i in range(1, len(rolls)):
            for substring in product(k_list, repeat=i):
                s = list(substring)
                if not self.check_substring(s, rolls):
                    return i
        return len(rolls)

    def check_substring(self, s: List, t: List):
        for i in t:
            if s[0] == i:
                del s[0]
            if len(s) == 0:
                return True
        return False


class Solution:

    def shortestSequence(self, rolls: List[int], k: int) -> int:
        # i 位子序列
        k_set = set()
        ans = 0
        for i in range(len(rolls)-1,-1,-1):
            k_set.add(rolls[i])
            if len(k_set) == k:
                ans += 1
                k_set = set()
        return ans+1



if __name__ == "__main__":
    a = Solution()
    c = a.shortestSequence(rolls = [3,2,1,3,3,3,3,3,1,2,2,3,1,3,3,1,1,3,1,1,1,3,1,3,3,1,2,3,2,1,1,2], k = 3)
    print(c)