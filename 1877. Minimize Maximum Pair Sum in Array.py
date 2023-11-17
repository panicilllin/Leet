from typing import List
import pandas as pd

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # print(nums)
        nums.sort()
        n = len(nums)
        arr_1 = nums[: n//2]
        arr_2 = nums[n: n//2-1: -1]
        # print(arr_1, arr_2)
        num_pair = [arr_1[i]+arr_2[i] for i in range(0,n//2)]
        return max(num_pair)

if __name__ == "__main__":
    inputs = [
    [3,5,2,3],
    [3,5,4,2,4,6]
    ]
    a = Solution()
    for i in inputs:
        b = a.minPairSum(nums=i)
        print(b)