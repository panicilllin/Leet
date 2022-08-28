from typing import List
import collections


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        num_dict = {}
        res = 0
        for i in nums:
            if not num_dict.get(i):
                num_dict[i] = 1
            else:
                num_dict[i] += num_dict[i]
        keys = [i for i in num_dict.keys()]
        keys.sort()
        if k == 0:
            for num in keys:
                if num_dict.get(num) > 1:
                    res = res + 1
        else:
            for num in keys:
                if num_dict.get(num+k):
                    res = res + 1
        return res



if __name__ == "__main__":
    a = Solution()
    b = a.findPairs(nums=[1,1,1,2,2], k=1)
    print(b)