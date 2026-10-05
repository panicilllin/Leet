from typing import List
class Solution0:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        for i in range(0, len(nums)):
            if nums[i] == target:
                if start == -1:
                    start = i
                    end = i
                else:
                    end = i
        if start==end:
            return [-1,-1]
        return [start, end]


#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or nums[0]> target or nums[-1]<target:
            return [-1,-1]

        l=-1
        r=len(nums)
        while l+1 < r:
            mid = (l+r)//2
            if nums[mid]<target:
                l=mid
            else:
                r=mid
        start=r

        l=r
        r=len(nums)
        while l+1 < r:
            mid = (l+r)//2
            if nums[mid]>target:
                r=mid
            else:
                l=mid
        end=l
        if nums[start]!=target:
            return [-1,-1]
        return[start,end]

if __name__ =="__main__":
    a=Solution()
    b=a.searchRange(nums = [5,7,7,8,8,10], target = 6)
    print(b)
