from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pre_sum=[0]
        for i in nums:
            pre_sum.append(pre_sum[-1]+i)
        print(pre_sum)
        ans=len(nums)+10
        q=deque()
        
        for i, cur_s in enumerate(pre_sum):
            print(i,cur_s,q)
            while q and cur_s - pre_sum[q[0]] >= k:
                ans = min(ans, i - q.popleft())
                print(ans)
            while q and pre_sum[q[-1]] >= cur_s:
                q.pop()
            q.append(i)
        return ans if ans <= len(nums) else -1
        

if __name__ == "__main__":
    a = Solution()
    b = a.shortestSubarray(nums = [84,-37,32,40,95], k = 167)
    print(b)