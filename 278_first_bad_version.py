#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.


def isBadVersion(version: int) -> bool:
    if version >= 1:
        return True
    return False

# 1 2 3 4 5
class Solution:
    def firstBadVersion(self, n: int) -> int:
        start=1
        end=n
        mid = (end-start+1)//2+start
        print(start, mid, end)
        res = -1
        while mid > start and mid < end:
            print(start, mid, end)
            if isBadVersion(mid) is True:
                end = mid
                mid = (end-start+1)//2+start
            else:
                start = mid
                mid = (end-start+1)//2+start
        if isBadVersion(start) is False:
            return mid
        return start
        
# @lc code=end


if __name__ == "__main__":
    a = Solution()
    b = a.firstBadVersion(2)
    print(b)