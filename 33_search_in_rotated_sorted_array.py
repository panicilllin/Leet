from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if nums[0] > nums[-1]:  # rotate
            l = 0
            r = len(nums) - 1
            while l + 1 < r:
                mid = (l + r) // 2
                if nums[mid] > nums[l]:
                    l = mid
                else:
                    r = mid
            # print(l, r, nums[l], nums[r])
        else:
            l = len(nums) - 1
            r = len(nums)

        if nums[:l + 1][0] <= target <= nums[:l + 1][-1]:
            r = l
            l = 0

        elif nums[r:] and nums[r:][0] <= target <= nums[r:][-1]:
            l = r
            r = len(nums) - 1
        else:
            return -1

        # print(l, r)
        if nums[l] == target:
            return l

        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        # print(l, r, nums[l], nums[r])

        if nums[r] == target:
            return r
        else:
            return -1


if __name__ == "__main__":
    a = Solution()
    b = a.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0)
    print(b)
