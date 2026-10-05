from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        n = len(nums)
        start = 0
        end = 0
        min_satisfy = n
        sum_n = nums[start]
        while end < n:
            # not enough
            if sum_n < target and end < n-1:
                end += 1
                sum_n += nums[end]
                # print('c ', start,end,nums[start:end+1],sum_n)
            
            # enoug h
            else:
                # zip window
                # print('a ',start,end,nums[start:end+1],sum_n)
                while start < end and sum_n - nums[start] >= target:
                    sum_n -= nums[start]
                    start += 1
                # print('b', start,end,nums[start:end+1],sum_n)
                min_satisfy = min(min_satisfy, end + 1 - start)
                
                # move forward
                end += 1
                if end <= n - 1:
                    sum_n += nums[end] - nums[start]
                else:
                    sum_n -= nums[start]
                start += 1
        return min_satisfy


if __name__ == "__main__":
    a = Solution() 
    b = a.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    print(b)

# AC