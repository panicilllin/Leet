from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1) 
        dp=[[0,0] for i in range(n)]
        dp[0][1]=1
        for i in range(1,n):
            if (nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]) and \
                (nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]): # change or not change
                dp[i][0] = min(dp[i-1][0],dp[i-1][1])
                dp[i][1] = dp[i][0]+1
            elif (nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]): # not change
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1]+1
            else: # must change
                dp[i][0] = dp[i-1][1]
                dp[i][1] = dp[i-1][0]+1
        print(dp)
        return min(dp[n-1][0],dp[n-1][1])
                
            

if __name__ == "__main__":
    a = Solution()
    b = a.minSwap(nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9])
    print(b)