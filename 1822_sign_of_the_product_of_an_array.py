from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans=1
        for num in nums:
            if num < 0:
                ans= -1 if ans == 1 else 1
            elif num == 0:
                return 0
        return ans

# AC