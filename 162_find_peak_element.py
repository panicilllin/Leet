class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l+1 < r:
            m=(l+r)//2
            if nums[m] > nums[m+1]:
                r=m
            else:
                l=m+1
        if nums[l]>nums[r]:
            return l
        else:
            return r

if __name__ =="__main__":
    a=Solution()
    b=a.findPeakElement(nums = [3,1,2])
    print(b)

# AC