from heapq import heapify, heapreplace,heappop,heappush
from typing import List


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        sum_nums = sum(nums)
        half_sum = sum_nums / 2
        res = 0
        while half_sum > 0:
            res += 1
            num = nums.pop(0)
            half_num = num / 2
            half_sum -= half_num
            nums = self.in_sort(half_num, nums)
        return res

    def in_sort(self, num, nums):
        for i in range(len(nums)):
            if num >= nums[i]:
                nums.insert(i, num)
                return nums
        nums.append(num)
        return nums


class Solution1:
    def halveArray(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = -(nums[i] << 20)
        heapify(nums)
        ans = 0
        half = sum(nums) >> 1
        while half < 0:
            half -= nums[0] >> 1
            heapreplace(nums, nums[0] >> 1)
            ans += 1
        return ans

class Solution2:
    def halveArray(self, nums: List[int]) -> int:
        nums = [-i<<20 for i in nums]

        sum_nums = sum(nums)
        half_sum = sum_nums / 2
        heapify(nums)
        res = 0
        while half_sum < 0:
            res += 1
            num = heappop(nums)
            # num = heappushpop((nums, num)
            half_num = int(num / 2)
            half_sum -= half_num
            heappush(nums, half_num)
        return res

if __name__ == "__main__":
    a = Solution()
    b = a.halveArray(nums=[5, 19, 8, 1])
    print(b)
