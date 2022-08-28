from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        start = 0
        end = 0
        min_satisfy = len(nums)
        sum_n = 0
        while end < len(nums):
            # not enough
            if sum_n < target:
                end += 1
                sum_n += nums[end]
            # enoug h
            else:
                # zip window
                while start < end and sum_n - nums[start] >= target:
                    sum_n -= nums[start]
                    start += 1
                # print(start,end)
                min_satisfy = min(min_satisfy, end - start)
                # move forward

                end += 1
                start += 1
                if end < len(nums) - 1:
                    sum_n += nums[end] - nums[start]
        # print(start,end)
        return min_satisfy


if __name__ == "__main__":
    a = Solution()
    b = a.minSubArrayLen(11, [1, 1, 1, 1, 1, 1])
    print(b)
