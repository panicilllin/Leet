from typing import List


class Solution0:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        right = 1
        res = 0
        for i in nums:
            if i < k:
                res += 1
        while right <= len(nums) and left < right:
            product = 1
            for i in range(left, right):
                product = product * nums[i]
            print(f"prd={product},rl={left, right}s={nums[left:right]}")
            if product < k:
                if right - left > 1:
                    res += 1
                right += 1
                if right > len(nums):
                    right = len(nums)
                    left += 1
            else:
                left += 1

            if left == right:
                right += 1
            print(res)
        return res


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k < 2:
            return 0
        res = 0
        n = len(nums)
        left = 0
        right = 0
        res = 0
        prefix = 1
        while right < n:
            prefix = prefix * nums[right]
            while prefix >= k:
                prefix = prefix / nums[left]
                left += 1
            right += 1
            res += right - left
        return res


if __name__ == "__main__":
    a = Solution()
    b = a.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
    print(b)
