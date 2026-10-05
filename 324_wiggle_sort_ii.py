import copy
from typing import List
import math


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        nums.sort()
        nums2 = copy.deepcopy(nums)
        middle_num = math.ceil(nums_len / 2)
        print(nums)
        left = middle_num - 1
        right = nums_len - 1
        for i in range(0, nums_len):
            if i % 2 == 0:
                nums[i] = nums2[left]
                left -= 1
            else:
                nums[i] = nums2[right]
                right -= 1

        print(nums)


if __name__ == "__main__":
    a = Solution()
    b = a.wiggleSort([1, 5, 1, 1, 6, 4])
# success
