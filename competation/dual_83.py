import collections
import bisect
import copy
from typing import List
from itertools import product


# 6128
class Solution1:

    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # check flush
        if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
            return "Flush"
        counts = {}
        for rank in ranks:
            if counts.get(rank):
                counts[rank] += 1
            else:
                counts[rank] = 1

        max_rank = max(counts.values())
        if max_rank >= 3:
            return "Three of a Kind"
        elif max_rank == 2:
            return "Pair"
        elif max_rank == 1:
            return "High Card"


# 6129
class Solution2:

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zero_dict = {}
        zero_count = 0
        nums.append(-1)
        for num in nums:
            if num != 0:
                # print(zero_count,zero_dict)
                if zero_count != 0:
                    if zero_dict.get(zero_count):
                        zero_dict[zero_count] += 1
                    else:
                        zero_dict[zero_count] = 1
                    zero_count = 0
            else:
                zero_count += 1
        res = 0
        # print(zero_dict)
        for key, val in zero_dict.items():
            res += sum(range(1, key + 1)) * val
        return res


# 6130
class NumberContainers:

    def __init__(self):
        self.map = collections.OrderedDict()
        self.index = []

    def change(self, index: int, number: int) -> None:
        self.map[index] = number
        bisect.insort(self.index, index)

    def find(self, number: int) -> int:
        for i in self.index:
            if self.map[i] == number:
                return i
        return -1


# 6131
class Solution3:
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


if __name__ == "__main__":
    a = Solution3()
    c = a.shortestSequence(rolls = [3,2,1,3,3,3,3,3,1,2,2,3,1,3,3,1,1,3,1,1,1,3,1,3,3,1,2,3,2,1,1,2], k = 3)
    print(c)
