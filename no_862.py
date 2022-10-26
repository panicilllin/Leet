from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pre_sums=[0]
        for i in nums:
            pre_sums.append(pre_sums[-1]+i)
        print(pre_sums)
        satisfy_list=[]
        min_substring = len(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                if pre_sums[j]-pre_sums[i] >= k:
                    satisfy_list.append([i,j])
                    min_substring = min(j-i, min_substring)
                    break
        print(satisfy_list)
        if not satisfy_list:
            return -1
        return min_substring

if __name__ == "__main__":
    a = Solution()
    b = a.shortestSubarray(nums = [2,-1,2], k = 3)
    print(b)