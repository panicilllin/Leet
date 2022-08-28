import math
from typing import List


def Maximum_common_divisor(num):  # 求任意多个数的最大公约数
    minimum = max(num)
    for i in num:
        minimum = math.gcd(int(i), int(minimum))
    return int(minimum)


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        res = 0
        pool = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                divisor = Maximum_common_divisor([nums[i], nums[j]])
                if divisor > 1:
                    pool.append([nums[i], nums[j]])
        maps = []
        for pair in pool:
            if not maps:
                maps = [pair]
                continue
            for map in maps:
                if pair[0] in map:
                    map.append(pair[1])
                elif pair[1] in map:
                    map.append(pair[0])

        return res


if __name__ == "__main__":
    a = Solution()
    b = a.largestComponentSize(nums=[2, 3, 6, 7, 4, 12, 21, 39])
    print(b)
