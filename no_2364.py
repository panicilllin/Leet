from collections import Counter
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        moves = [item - i for i, item in enumerate(nums)]
        move_map = {}
        for move in moves:
            if not move_map.get(move):
                move_map[move] = 1
            else:
                move_map[move] += 1
        good_count = 0
        for key, value in move_map.items():
            if value != 1:
                good_count += value
        print(good_count,move_map)
        res = (len(nums)+1)*(len(nums))/2 - (1+good_count)*good_count/2
        return int(res)



class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n, cnt = len(nums), Counter()
        ans = n * (n - 1) // 2
        for i, num in enumerate(nums):
            ans -= cnt[num - i]  # 有 cnt[num - i] 个相同的
            cnt[num - i] += 1
        return ans


if __name__ == "__main__":
    a = Solution()
    # b = a.countBadPairs(nums=[56,30,2,73,28,81,75,75,18,63,54,10,69,85,33,89,12,78,57,60,54,65,74,63,53,77])
    b = a.countBadPairs([4,1,3,3])
    print(b)
