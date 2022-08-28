# from __future__ import annotation
from typing import *

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums_up = [i for i in nums if i >= 0]
        nums_dn = [i for i in nums if i < 0]
        nums_up.sort()
        nums_dn.sort()
        for j in range(0, len(nums_dn)):
            if k == 0:
                break
            nums_dn[j] = -nums_dn[j]
            k = k-1
        if k == 0 or k % 2 == 0:
            return sum(nums_dn)+sum(nums_up)
        elif nums_dn and nums_up:
            res = sum(nums_dn[:-1])+sum(nums_up[1:])
            res += max(nums_dn[-1], nums_up[0]) - min(nums_dn[-1], nums_up[0])
            return res
        elif nums_up:
            return sum(nums_up[1:]) - nums_up[0]
        elif nums_dn:
            return sum(nums_dn[:-1]) - nums_dn[-1]



if __name__ == '__main__':
    a = Solution()
    b = a.largestSumAfterKNegations([4,2,3],1)
    print(b)